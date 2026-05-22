from __future__ import annotations

import json
import os
import shlex
from pathlib import Path
from typing import Any

from harbor.agents.installed.claude_code import ClaudeCode
from harbor.agents.installed.base import with_prompt_template
from harbor.environments.base import BaseEnvironment
from harbor.models.agent.context import AgentContext
from harbor.models.trial.paths import EnvironmentPaths


class VersionedClaudeCode(ClaudeCode):
    """Claude Code Harbor agent with compatibility for pinned historical CLI versions.

    Harbor's built-in Claude Code agent is the right baseline for TB2, but it assumes a
    modern CLI surface. This variant installs exact npm versions and detects supported
    flags at runtime so older versions can participate in the same benchmark matrix.
    """

    def __init__(
        self,
        logs_dir: Path,
        claude_code_simple: bool = False,
        claude_config_isolation: bool = True,
        *args: Any,
        **kwargs: Any,
    ):
        self.claude_code_simple = claude_code_simple
        self.claude_config_isolation = claude_config_isolation
        super().__init__(logs_dir=logs_dir, *args, **kwargs)

    @staticmethod
    def name() -> str:
        return "versioned-claude-code"

    async def install(self, environment: BaseEnvironment) -> None:
        await self.exec_as_root(
            environment,
            command=(
                "if command -v apk >/dev/null 2>&1; then "
                "apk add --no-cache curl bash nodejs npm util-linux sudo shadow; "
                "elif command -v apt-get >/dev/null 2>&1; then "
                "apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y "
                "ca-certificates curl nodejs npm util-linux sudo; "
                "elif command -v yum >/dev/null 2>&1; then "
                "yum install -y curl nodejs npm util-linux sudo shadow-utils; "
                "else echo 'Warning: no known package manager found' >&2; fi; "
                "if ! id claude-agent >/dev/null 2>&1; then "
                "useradd -m -s /bin/bash claude-agent 2>/dev/null || "
                "adduser -D -s /bin/bash claude-agent 2>/dev/null || true; "
                "fi; "
                "for group in root sudo wheel; do "
                "if getent group \"$group\" >/dev/null 2>&1 && command -v usermod >/dev/null 2>&1; then "
                "usermod -aG \"$group\" claude-agent 2>/dev/null || true; "
                "fi; "
                "done; "
                "if command -v sudo >/dev/null 2>&1; then "
                "mkdir -p /etc/sudoers.d; "
                "printf 'claude-agent ALL=(ALL) NOPASSWD:ALL\\n' > /etc/sudoers.d/claude-agent; "
                "chmod 0440 /etc/sudoers.d/claude-agent; "
                "fi"
            ),
            env={"DEBIAN_FRONTEND": "noninteractive"},
        )

        package = "@anthropic-ai/claude-code"
        if self._version:
            package += f"@{self._version}"
        await self.exec_as_agent(
            environment,
            command=(
                "set -euo pipefail; "
                "mkdir -p \"$HOME\"; "
                f"npm install -g {shlex.quote(package)}; "
                "npm cache clean --force >/dev/null 2>&1 || true; "
                "claude --version"
            ),
        )

    def _base_env(self) -> dict[str, str]:
        use_bedrock = self._is_bedrock_mode()
        env = {
            "ANTHROPIC_API_KEY": os.environ.get("ANTHROPIC_API_KEY")
            or os.environ.get("ANTHROPIC_AUTH_TOKEN")
            or "",
            "ANTHROPIC_BASE_URL": os.environ.get("ANTHROPIC_BASE_URL", ""),
            "CLAUDE_CODE_OAUTH_TOKEN": os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", ""),
            "CLAUDE_CODE_MAX_OUTPUT_TOKENS": os.environ.get(
                "CLAUDE_CODE_MAX_OUTPUT_TOKENS", ""
            ),
            "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
            "DISABLE_TELEMETRY": os.environ.get("DISABLE_TELEMETRY", "1"),
            "FORCE_AUTO_BACKGROUND_TASKS": "1",
            "ENABLE_BACKGROUND_TASKS": "1",
            "IS_SANDBOX": "1",
            "npm_config_cache": os.environ.get("npm_config_cache", "/tmp/claude-npm-cache"),
        }

        if use_bedrock:
            env["CLAUDE_CODE_USE_BEDROCK"] = "1"
            env["AWS_REGION"] = os.environ.get("AWS_REGION", "us-east-1")
            for key in (
                "AWS_BEARER_TOKEN_BEDROCK",
                "AWS_ACCESS_KEY_ID",
                "AWS_SECRET_ACCESS_KEY",
                "AWS_SESSION_TOKEN",
                "AWS_PROFILE",
                "ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION",
                "DISABLE_PROMPT_CACHING",
            ):
                if os.environ.get(key):
                    env[key] = os.environ[key]

        if self.model_name:
            if use_bedrock:
                env["ANTHROPIC_MODEL"] = (
                    self.model_name.split("/", 1)[-1]
                    if "/" in self.model_name
                    else self.model_name
                )
            elif env.get("ANTHROPIC_BASE_URL"):
                env["ANTHROPIC_MODEL"] = self.model_name
            else:
                env["ANTHROPIC_MODEL"] = self.model_name.split("/")[-1]
        elif os.environ.get("ANTHROPIC_MODEL"):
            env["ANTHROPIC_MODEL"] = os.environ["ANTHROPIC_MODEL"]

        if env.get("ANTHROPIC_BASE_URL") and env.get("ANTHROPIC_MODEL"):
            env["ANTHROPIC_DEFAULT_SONNET_MODEL"] = env["ANTHROPIC_MODEL"]
            env["ANTHROPIC_DEFAULT_OPUS_MODEL"] = env["ANTHROPIC_MODEL"]
            env["ANTHROPIC_DEFAULT_HAIKU_MODEL"] = env["ANTHROPIC_MODEL"]
            env["CLAUDE_CODE_SUBAGENT_MODEL"] = env["ANTHROPIC_MODEL"]

        for key in (
            "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING",
            "CLAUDE_CODE_EFFORT_LEVEL",
            "MAX_THINKING_TOKENS",
        ):
            if os.environ.get(key):
                env[key] = os.environ[key]

        env.update(self._resolved_env_vars)
        env["CLAUDE_CONFIG_DIR"] = (EnvironmentPaths.agent_dir / "sessions").as_posix()
        if self.claude_code_simple:
            env["CLAUDE_CODE_SIMPLE"] = "1"
        if self._version and self._version.startswith("0.2."):
            env["CI"] = "1"

        return {key: value for key, value in env.items() if value}

    @with_prompt_template
    async def run(
        self, instruction: str, environment: BaseEnvironment, context: AgentContext
    ) -> None:
        env = self._base_env()
        escaped_instruction = shlex.quote(instruction)
        escaped_version = shlex.quote(self._version or "latest")
        escaped_cli_flags_json = shlex.quote(json.dumps(self._resolved_flags))

        setup_command = (
            "mkdir -p $CLAUDE_CONFIG_DIR/debug $CLAUDE_CONFIG_DIR/projects/-app "
            "$CLAUDE_CONFIG_DIR/shell-snapshots $CLAUDE_CONFIG_DIR/statsig "
            "$CLAUDE_CONFIG_DIR/todos $CLAUDE_CONFIG_DIR/skills /logs/agent && "
            "if [ -d ~/.claude/skills ]; then "
            "cp -r ~/.claude/skills/. $CLAUDE_CONFIG_DIR/skills/ 2>/dev/null || true; fi"
        )
        skills_command = self._build_register_skills_command()
        if skills_command:
            setup_command += f" && {skills_command}"
        memory_command = self._build_register_memory_command()
        if memory_command:
            setup_command += f" && {memory_command}"
        mcp_command = self._build_register_mcp_servers_command()
        if mcp_command:
            setup_command += f" && {mcp_command}"

        await self.exec_as_agent(environment, command=setup_command, env=env)
        await self.exec_as_agent(
            environment,
            command=_runner_command(escaped_instruction, escaped_version, escaped_cli_flags_json),
            env=env,
        )


def _runner_command(
    escaped_instruction: str,
    escaped_version: str,
    escaped_cli_flags_json: str,
) -> str:
    return f"""set -uo pipefail
mkdir -p /app /logs/agent/messages "$CLAUDE_CONFIG_DIR"
if ! id claude-agent >/dev/null 2>&1; then
  useradd -m -s /bin/bash claude-agent >/dev/null 2>&1 || adduser -D -s /bin/bash claude-agent >/dev/null 2>&1 || true
fi
for group in root sudo wheel; do
  if getent group "$group" >/dev/null 2>&1 && command -v usermod >/dev/null 2>&1; then
    usermod -aG "$group" claude-agent >/dev/null 2>&1 || true
  fi
done
mkdir -p /home/claude-agent
chown claude-agent /home/claude-agent 2>/dev/null || true
chmod -R a+rwX /app /logs/agent "$CLAUDE_CONFIG_DIR" /home/claude-agent 2>/dev/null || true
VERSION={escaped_version}
export VERSION
CLI_FLAGS_JSON={escaped_cli_flags_json}

node <<'EOF'
const fs = require("fs");
const os = require("os");
const path = require("path");
const configPaths = [path.join(os.homedir(), ".claude.json")];
if (process.env.CLAUDE_CONFIG_DIR) {{
  configPaths.push(path.join(process.env.CLAUDE_CONFIG_DIR, "config.json"));
}}
for (const configPath of configPaths) {{
  let config = {{}};
  try {{ config = JSON.parse(fs.readFileSync(configPath, "utf8")); }} catch {{}}
  fs.mkdirSync(path.dirname(configPath), {{recursive: true}});
  config.theme = config.theme || "dark";
  config.hasCompletedOnboarding = true;
  config.lastOnboardingVersion = process.env.VERSION || "unknown";
  config.autoUpdaterStatus = "disabled";
  config.bypassPermissionsModeAccepted = true;
  if (process.env.ANTHROPIC_API_KEY) config.primaryApiKey = process.env.ANTHROPIC_API_KEY;
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
}}
EOF
chown -R claude-agent /app /logs/agent "$CLAUDE_CONFIG_DIR" /home/claude-agent 2>/dev/null || true
chmod -R a+rwX /app /logs/agent "$CLAUDE_CONFIG_DIR" /home/claude-agent 2>/dev/null || true

HELP="$(claude --help 2>&1 || true)"
printf '%s\n' "$HELP" > /logs/agent/claude-help.txt

OUTPUT_ARGS=()
ADAPTER_MODE="text-legacy"
if printf '%s\n' "$HELP" | grep -q -- '--output-format'; then
  OUTPUT_ARGS=(--verbose --output-format stream-json)
  ADAPTER_MODE="stream-json"
fi

PERMISSION_ARGS=()
if printf '%s\n' "$HELP" | grep -q -- '--permission-mode'; then
  PERMISSION_ARGS=(--permission-mode bypassPermissions)
elif printf '%s\n' "$HELP" | grep -q -- '--dangerously-skip-permissions'; then
  PERMISSION_ARGS=(--dangerously-skip-permissions)
elif printf '%s\n' "$HELP" | grep -q -- '--allowedTools'; then
  PERMISSION_ARGS=(--allowedTools Task Bash Glob Grep LS Read View Edit Replace MultiEdit Write Create NotebookRead NotebookEdit WebFetch Batch TodoRead TodoWrite WebSearch)
fi

MODEL_ARGS=()
if [ -n "${{ANTHROPIC_MODEL:-}}" ] && printf '%s\n' "$HELP" | grep -q -- '--model'; then
  MODEL_ARGS=(--model "$ANTHROPIC_MODEL")
fi

EFFORT_ARGS=()
if [ -n "${{CLAUDE_CODE_EFFORT_LEVEL:-}}" ] && printf '%s\n' "$HELP" | grep -q -- '--effort'; then
  EFFORT_ARGS=(--effort "$CLAUDE_CODE_EFFORT_LEVEL")
fi

EXTRA_ARGS=()
node - "$CLI_FLAGS_JSON" "$HELP" > /tmp/claude-extra-args.sh <<'EOF'
const flags = JSON.parse(process.argv[2] || "{{}}");
const help = process.argv[3] || "";
function emit(flag, value) {{
  if (value === undefined || value === null || value === "") return;
  if (!help.includes(flag)) return;
  console.log(`EXTRA_ARGS+=(${{JSON.stringify(flag)}} ${{JSON.stringify(String(value))}})`);
}}
emit("--max-turns", flags.max_turns);
emit("--thinking", flags.thinking);
emit("--thinking-display", flags.thinking_display);
emit("--max-thinking-tokens", flags.max_thinking_tokens);
emit("--max-budget-usd", flags.max_budget_usd);
emit("--fallback-model", flags.fallback_model);
emit("--append-system-prompt", flags.append_system_prompt);
emit("--allowedTools", flags.allowed_tools);
emit("--disallowedTools", flags.disallowed_tools);
EOF
. /tmp/claude-extra-args.sh

cat > /logs/agent/claude-code-invocation.json <<EOF
{{"adapter_mode":"$ADAPTER_MODE","version":"$VERSION","claude_code_simple":"${{CLAUDE_CODE_SIMPLE:-}}","model":"${{ANTHROPIC_MODEL:-}}","effort":"${{CLAUDE_CODE_EFFORT_LEVEL:-}}"}}
EOF

INSTRUCTION={escaped_instruction}
CLAUDE_CMD=(claude "${{OUTPUT_ARGS[@]}}" "${{PERMISSION_ARGS[@]}}" "${{MODEL_ARGS[@]}}" "${{EFFORT_ARGS[@]}}" "${{EXTRA_ARGS[@]}}" -p "$INSTRUCTION")
if [ "$(id -u)" = "0" ] && command -v setpriv >/dev/null 2>&1 && id claude-agent >/dev/null 2>&1; then
  CAP_ARGS=()
  CAP_BOUNDS="$(setpriv --dump 2>/dev/null | awk -F': ' '/Capability bounding set:/ {{print $2}}')"
  if [ -n "$CAP_BOUNDS" ] && [ "$CAP_BOUNDS" != "[none]" ]; then
    CAP_PLUS="$(printf '%s' "$CAP_BOUNDS" | tr -d ' ' | sed 's/^/+/' | sed 's/,/,+/g')"
    CAP_ARGS=(--inh-caps="$CAP_PLUS" --ambient-caps="$CAP_PLUS")
  fi
  IS_SANDBOX=1 HOME=/home/claude-agent setpriv --reuid=claude-agent --regid=claude-agent --init-groups "${{CAP_ARGS[@]}}" "${{CLAUDE_CMD[@]}}" \\
    > >(tee /logs/agent/claude-code.txt /logs/agent/messages/message-001.stdout.jsonl) \\
    2> >(tee /logs/agent/claude-code.stderr.log /logs/agent/messages/message-001.stderr.log >&2)
  exit $?
fi
IS_SANDBOX=1 HOME="${{HOME:-/home/claude-agent}}" "${{CLAUDE_CMD[@]}}" \\
  > >(tee /logs/agent/claude-code.txt /logs/agent/messages/message-001.stdout.jsonl) \\
  2> >(tee /logs/agent/claude-code.stderr.log /logs/agent/messages/message-001.stderr.log >&2)
exit $?
"""
