from __future__ import annotations

import argparse
import concurrent.futures
import fnmatch
import json
import os
import re
import shlex
import subprocess
import sys
import threading
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None


REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_FILE = "queue.json"
RESULTS_FILE = "results.jsonl"
SUMMARY_FILE = "summary.json"
REPORT_FILE = "report.md"
SUMMARY_REPORT_FILE = "report.summary.md"
DEFAULT_DATASET = "terminal-bench/terminal-bench-2"
TB2_GIT_URL = "https://github.com/harbor-framework/terminal-bench-2"
DEFAULT_AGENT_IMPORT_PATH = (
    "tb2_claude_bench.agents.versioned_claude_code:VersionedClaudeCode"
)


@dataclass
class QueueJob:
    id: str
    task_name: str
    agent: str
    model: str | None
    version: str
    mode: str
    dataset: str
    harbor_job_name: str
    agent_import_path: str | None = None
    agent_kwargs: dict[str, Any] = field(default_factory=dict)
    status: str = "queued"
    attempts: int = 0
    created_at: str = field(default_factory=lambda: utc_now())
    started_at: str | None = None
    ended_at: str | None = None
    exit_code: int | None = None
    log_path: str | None = None
    harbor_job_dir: str | None = None
    error: str | None = None


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9_.-]+", "-", value)
    return value.strip("-") or "item"


def command_text(cmd: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in cmd)


def default_harbor_command() -> str:
    local_harbor = REPO_ROOT / ".venv" / "bin" / "harbor"
    if local_harbor.exists():
        return str(local_harbor)
    return "harbor"


def load_queue(queue_dir: Path) -> dict[str, Any]:
    path = queue_dir / QUEUE_FILE
    if not path.exists():
        raise SystemExit(f"Queue file does not exist: {path}")
    return json.loads(path.read_text())


def save_queue(queue_dir: Path, state: dict[str, Any]) -> None:
    queue_dir.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = utc_now()
    path = queue_dir / QUEUE_FILE
    tmp_path = path.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    tmp_path.replace(path)


def resolve_tb2_task_names(args: argparse.Namespace) -> list[str]:
    all_tasks = list_tb2_tasks(args.task_source_dir)
    selected = all_tasks
    if args.task_name:
        selected = resolve_globs(args.task_name, all_tasks)
    if args.exclude_task_name:
        excluded = set(resolve_globs(args.exclude_task_name, all_tasks))
        selected = [task for task in selected if task not in excluded]
    if args.n_tasks is not None:
        selected = selected[: args.n_tasks]
    return selected


def list_tb2_tasks(task_source_dir: Path | None) -> list[str]:
    source_dir = task_source_dir or (REPO_ROOT / "data" / "terminal-bench-2")
    if not source_dir.exists():
        source_dir.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--depth", "1", TB2_GIT_URL, str(source_dir)],
            cwd=REPO_ROOT,
            check=True,
        )
    tasks = sorted(path.parent.name for path in source_dir.glob("*/task.toml"))
    if not tasks:
        raise SystemExit(f"No Harbor task.toml files found in {source_dir}")
    return tasks


def resolve_globs(patterns: list[str], values: list[str]) -> list[str]:
    matched: list[str] = []
    for pattern in patterns:
        hits = [value for value in values if fnmatch.fnmatch(value, pattern)]
        if not hits:
            raise SystemExit(f"No values matched pattern: {pattern}")
        matched.extend(hits)
    return sorted(dict.fromkeys(matched))


def parse_version_spec(value: str, default_simple: bool) -> tuple[str, str]:
    if ":" not in value:
        return value, "simple" if default_simple else "regular"
    version, mode = value.rsplit(":", 1)
    mode = mode.lower().strip()
    if mode in {"simple", "s"}:
        return version, "simple"
    if mode in {"regular", "r", "vanilla", "no-simple", "nosimple"}:
        return version, "regular"
    return value, "simple" if default_simple else "regular"


def resolve_version_entries(args: argparse.Namespace) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for value in args.version or []:
        entries.append(parse_version_spec(value, args.simple))
    for value in args.simple_version or []:
        entries.append((value, "simple"))
    for value in args.regular_version or []:
        entries.append((value, "regular"))
    return list(dict.fromkeys(entries))


def cmd_enqueue(args: argparse.Namespace) -> int:
    queue_dir = args.queue_dir.resolve()
    jobs_dir = (queue_dir / "harbor-jobs").resolve()
    logs_dir = (queue_dir / "logs").resolve()
    reports_dir = (queue_dir / "reports").resolve()
    for path in (jobs_dir, logs_dir, reports_dir):
        path.mkdir(parents=True, exist_ok=True)

    if (queue_dir / QUEUE_FILE).exists() and not args.force and not args.append:
        raise SystemExit(f"{queue_dir / QUEUE_FILE} exists. Use --force or --append.")

    existing_jobs: list[dict[str, Any]] = []
    if args.append and (queue_dir / QUEUE_FILE).exists():
        existing_jobs = load_queue(queue_dir).get("jobs", [])

    task_names = resolve_tb2_task_names(args)
    jobs = list(existing_jobs)
    existing_ids = {job["id"] for job in jobs}
    run_prefix = args.run_prefix or datetime.now(timezone.utc).strftime("tb2-%Y%m%dt%H%M%Sz")

    if args.agent == "oracle":
        for task_name in task_names:
            job_id = f"{slug(task_name)}__oracle"
            if job_id in existing_ids:
                continue
            jobs.append(
                asdict(
                    QueueJob(
                        id=job_id,
                        task_name=task_name,
                        agent="oracle",
                        model=None,
                        version="oracle",
                        mode="oracle",
                        dataset=args.dataset,
                        harbor_job_name=f"{run_prefix}__{job_id}",
                    )
                )
            )
            existing_ids.add(job_id)
    else:
        version_entries = resolve_version_entries(args)
        if not version_entries:
            raise SystemExit("Set at least one --version, --simple-version, or --regular-version")
        for task_name in task_names:
            for version, mode in version_entries:
                job_id = f"{slug(task_name)}__cc-{slug(version)}__{slug(mode)}"
                if job_id in existing_ids:
                    continue
                agent_kwargs = {
                    "version": version,
                    "claude_code_simple": mode == "simple",
                }
                if args.effort:
                    agent_kwargs["reasoning_effort"] = args.effort
                if args.max_turns is not None:
                    agent_kwargs["max_turns"] = args.max_turns
                jobs.append(
                    asdict(
                        QueueJob(
                            id=job_id,
                            task_name=task_name,
                            agent="versioned-claude-code",
                            agent_import_path=args.agent_import_path,
                            model=args.model,
                            version=version,
                            mode=mode,
                            dataset=args.dataset,
                            harbor_job_name=f"{run_prefix}__{job_id}",
                            agent_kwargs=agent_kwargs,
                        )
                    )
                )
                existing_ids.add(job_id)

    state = {
        "schema_version": 1,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "settings": {
            "dataset": args.dataset,
            "queue_dir": str(queue_dir),
            "jobs_dir": str(jobs_dir),
            "logs_dir": str(logs_dir),
            "reports_dir": str(reports_dir),
            "harbor_command": args.harbor_command or default_harbor_command(),
            "env_file": str(args.env_file) if args.env_file else None,
            "delete_environment": args.delete_environment,
            "force_build": args.force_build,
            "extra_harbor_arg": args.extra_harbor_arg or [],
        },
        "jobs": jobs,
    }
    save_queue(queue_dir, state)
    write_reports(queue_dir, state)
    print(f"Queued {len(jobs)} jobs in {queue_dir / QUEUE_FILE}")
    print(f"Tasks: {len(task_names)}")
    return 0


def harbor_command(job: dict[str, Any], state: dict[str, Any]) -> list[str]:
    settings = state["settings"]
    dataset = job["dataset"]
    cmd = [
        settings.get("harbor_command") or default_harbor_command(),
        "run",
        "--jobs-dir",
        settings["jobs_dir"],
        "--job-name",
        job["harbor_job_name"],
        "--yes",
        "--quiet",
    ]
    if Path(dataset).exists():
        cmd.extend(["-p", dataset, "-i", job["task_name"]])
    else:
        task_name = job["task_name"]
        if dataset == DEFAULT_DATASET and not task_name.startswith("terminal-bench/"):
            task_name = f"terminal-bench/{task_name}"
        cmd.extend(["-d", dataset, "-i", task_name])

    if settings.get("force_build"):
        cmd.append("--force-build")
    else:
        cmd.append("--no-force-build")
    if settings.get("delete_environment"):
        cmd.append("--delete")
    else:
        cmd.append("--no-delete")

    if job["agent"] == "oracle":
        cmd.extend(["-a", "oracle"])
    else:
        cmd.extend(["--agent-import-path", job["agent_import_path"] or DEFAULT_AGENT_IMPORT_PATH])
        if job.get("model"):
            cmd.extend(["-m", job["model"]])
        for key, value in sorted((job.get("agent_kwargs") or {}).items()):
            cmd.extend(["--ak", f"{key}={value}"])

    env_file = settings.get("env_file")
    if env_file:
        cmd.extend(["--env-file", env_file])
    for extra_arg in settings.get("extra_harbor_arg", []):
        cmd.append(extra_arg)
    return cmd


def cmd_dequeue(args: argparse.Namespace) -> int:
    queue_dir = args.queue_dir.resolve()
    state = load_queue(queue_dir)
    state_lock = threading.Lock()
    if load_dotenv is not None:
        env_file = state["settings"].get("env_file") or REPO_ROOT / ".env"
        if Path(env_file).exists():
            load_dotenv(env_file, override=False)

    jobs = state["jobs"]
    selected = [job for job in jobs if job["status"] in {"queued", "running"}]
    if args.limit is not None:
        selected = selected[: args.limit]
    if not selected:
        write_reports(queue_dir, state)
        print("No queued jobs.")
        return 0

    def run_one(job: dict[str, Any]) -> dict[str, Any]:
        job["status"] = "running"
        job["attempts"] = int(job.get("attempts") or 0) + 1
        job["started_at"] = utc_now()
        job["error"] = None
        job["harbor_job_dir"] = str(Path(state["settings"]["jobs_dir"]) / job["harbor_job_name"])
        log_path = Path(state["settings"]["logs_dir"]) / f"{job['id']}.log"
        job["log_path"] = str(log_path)
        with state_lock:
            save_queue(queue_dir, state)

        cmd = harbor_command(job, state)
        started = time.time()
        with log_path.open("w") as log:
            log.write(f"$ {command_text(cmd)}\n\n")
            log.flush()
            proc = subprocess.run(
                cmd,
                cwd=REPO_ROOT,
                env=os.environ.copy(),
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
            )
        job["exit_code"] = proc.returncode
        job["ended_at"] = utc_now()
        job["duration_sec"] = round(time.time() - started, 3)
        ingest_harbor_result(job)
        if proc.returncode == 0:
            job["status"] = "completed"
        else:
            job["status"] = "failed"
            job["error"] = job.get("error") or f"harbor exited with {proc.returncode}"
        with state_lock:
            save_queue(queue_dir, state)
            write_reports(queue_dir, state)
        return job

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = [executor.submit(run_one, job) for job in selected]
        for future in concurrent.futures.as_completed(futures):
            job = future.result()
            print(f"{job['status']}: {job['id']}")

    with state_lock:
        save_queue(queue_dir, state)
        write_reports(queue_dir, state)
    return 0


def ingest_harbor_result(job: dict[str, Any]) -> None:
    result_path = Path(job["harbor_job_dir"]) / "result.json"
    if not result_path.exists():
        job["passed"] = False
        job["reward"] = None
        job["error"] = "missing Harbor result.json"
        return
    try:
        result = json.loads(result_path.read_text())
    except json.JSONDecodeError as exc:
        job["passed"] = False
        job["reward"] = None
        job["error"] = f"invalid Harbor result.json: {exc}"
        return

    reward = extract_job_reward(result)
    trial = extract_trial_result(result) or {}
    exception = trial.get("exception_info")
    job["reward"] = reward
    job["passed"] = bool(reward is not None and reward >= 1.0 and not exception)
    job["exception_type"] = (exception or {}).get("exception_type")
    job["exception_message"] = (exception or {}).get("message")
    metrics = trial.get("agent_result") or trial.get("agent_info") or {}
    usage_metrics = extract_usage_metrics(job, result, trial)
    job["harbor_result_path"] = str(result_path)
    job["harbor_metrics"] = metrics
    job.update(usage_metrics)
    if exception:
        job["error"] = job["exception_type"] or "Harbor trial exception"


def refresh_finished_results(state: dict[str, Any]) -> None:
    for job in state["jobs"]:
        if job.get("status") not in {"completed", "failed"} or not job.get("harbor_job_dir"):
            continue
        ingest_harbor_result(job)


def extract_usage_metrics(
    job: dict[str, Any], result: dict[str, Any], trial: dict[str, Any]
) -> dict[str, Any]:
    stats = result.get("stats") or {}
    agent_result = trial.get("agent_result") or {}
    metrics = {
        "n_input_tokens": first_number(stats, agent_result, key="n_input_tokens"),
        "n_cache_tokens": first_number(stats, agent_result, key="n_cache_tokens"),
        "n_output_tokens": first_number(stats, agent_result, key="n_output_tokens"),
        "cost_usd": first_number(stats, agent_result, key="cost_usd"),
    }
    if all(value is not None for value in metrics.values()):
        metrics["n_total_tokens"] = sum_token_metrics(metrics)
        return metrics

    jsonl_metrics = extract_claude_jsonl_metrics(job)
    for key, value in jsonl_metrics.items():
        if metrics.get(key) is None:
            metrics[key] = value
    metrics["n_total_tokens"] = sum_token_metrics(metrics)
    return metrics


def first_number(*objects: dict[str, Any], key: str) -> int | float | None:
    for obj in objects:
        value = obj.get(key)
        if isinstance(value, (int, float)):
            return value
    return None


def sum_token_metrics(metrics: dict[str, Any]) -> int | None:
    values = [
        metrics.get("n_input_tokens"),
        metrics.get("n_cache_tokens"),
        metrics.get("n_output_tokens"),
    ]
    numeric = [int(value) for value in values if isinstance(value, (int, float))]
    if not numeric:
        return None
    return sum(numeric)


def extract_claude_jsonl_metrics(job: dict[str, Any]) -> dict[str, Any]:
    job_dir = Path(job.get("harbor_job_dir") or "")
    if not job_dir.exists():
        return {}
    metrics: dict[str, Any] = {
        "n_input_tokens": 0,
        "n_cache_tokens": 0,
        "n_output_tokens": 0,
        "cost_usd": None,
    }
    saw_usage = False
    cost = 0.0
    saw_cost = False
    for path in sorted(job_dir.glob("*/agent/messages/*.stdout.jsonl")):
        for event in iter_json_objects(path.read_text(errors="replace")):
            usage = event.get("usage")
            if isinstance(usage, dict):
                saw_usage = True
                metrics["n_input_tokens"] += int(usage.get("input_tokens") or 0)
                metrics["n_output_tokens"] += int(usage.get("output_tokens") or 0)
                metrics["n_cache_tokens"] += int(usage.get("cache_creation_input_tokens") or 0)
                metrics["n_cache_tokens"] += int(usage.get("cache_read_input_tokens") or 0)
            event_cost = event.get("cost_usd")
            if isinstance(event_cost, (int, float)):
                saw_cost = True
                cost += float(event_cost)
    if not saw_usage:
        for key in ("n_input_tokens", "n_cache_tokens", "n_output_tokens"):
            metrics[key] = None
    if saw_cost:
        metrics["cost_usd"] = cost
    return metrics


def iter_json_objects(text: str) -> list[dict[str, Any]]:
    decoder = json.JSONDecoder()
    objects: list[dict[str, Any]] = []
    index = 0
    length = len(text)
    while index < length:
        while index < length and text[index].isspace():
            index += 1
        if index >= length:
            break
        try:
            value, index = decoder.raw_decode(text, index)
        except json.JSONDecodeError:
            next_line = text.find("\n", index)
            if next_line == -1:
                break
            index = next_line + 1
            continue
        if isinstance(value, dict):
            objects.append(value)
    return objects


def extract_job_reward(result: dict[str, Any]) -> float | None:
    trial = extract_trial_result(result)
    if trial is not None:
        reward = extract_reward((trial.get("verifier_result") or {}).get("rewards"))
        if reward is not None:
            return reward

    rewards: list[float] = []
    for eval_result in ((result.get("stats") or {}).get("evals") or {}).values():
        for metric in eval_result.get("metrics") or []:
            reward = extract_reward(metric)
            if reward is not None:
                rewards.append(reward)
                break
        if rewards:
            continue
        reward_stats = (eval_result.get("reward_stats") or {}).get("reward") or {}
        numeric_rewards = [float(value) for value in reward_stats if is_number_string(value)]
        if len(numeric_rewards) == 1:
            rewards.append(numeric_rewards[0])
    if len(rewards) == 1:
        return rewards[0]
    return None


def extract_trial_result(result: dict[str, Any]) -> dict[str, Any] | None:
    trials = result.get("trial_results") or []
    if trials:
        return trials[0]
    if "verifier_result" in result or "exception_info" in result:
        return result
    return None


def extract_reward(rewards: Any) -> float | None:
    if rewards is None:
        return None
    if isinstance(rewards, (int, float)):
        return float(rewards)
    if isinstance(rewards, dict):
        for key in ("reward", "score", "mean", "accuracy"):
            value = rewards.get(key)
            if isinstance(value, (int, float)):
                return float(value)
        numeric = [float(value) for value in rewards.values() if isinstance(value, (int, float))]
        if len(numeric) == 1:
            return numeric[0]
    return None


def is_number_string(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True


def cmd_status(args: argparse.Namespace) -> int:
    state = load_queue(args.queue_dir.resolve())
    counts: dict[str, int] = {}
    for job in state["jobs"]:
        counts[job["status"]] = counts.get(job["status"], 0) + 1
    print(json.dumps({"total": len(state["jobs"]), "statuses": counts}, indent=2, sort_keys=True))
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    queue_dir = args.queue_dir.resolve()
    state = load_queue(queue_dir)
    refresh_finished_results(state)
    save_queue(queue_dir, state)
    write_reports(queue_dir, state)
    print(f"Wrote reports to {state['settings']['reports_dir']}")
    return 0


def cmd_reset(args: argparse.Namespace) -> int:
    queue_dir = args.queue_dir.resolve()
    state = load_queue(queue_dir)
    for job in state["jobs"]:
        if args.only_failed and job["status"] != "failed":
            continue
        job["status"] = "queued"
        job["started_at"] = None
        job["ended_at"] = None
        job["exit_code"] = None
        job["error"] = None
        job.pop("passed", None)
        job.pop("reward", None)
    save_queue(queue_dir, state)
    write_reports(queue_dir, state)
    return 0


def write_reports(queue_dir: Path, state: dict[str, Any]) -> None:
    reports_dir = Path(state["settings"]["reports_dir"])
    reports_dir.mkdir(parents=True, exist_ok=True)
    rows = list(state["jobs"])
    aggregates = aggregate_rows(rows)
    (reports_dir / SUMMARY_FILE).write_text(json.dumps(aggregates, indent=2, sort_keys=True) + "\n")
    with (reports_dir / RESULTS_FILE).open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\n")
    (reports_dir / SUMMARY_REPORT_FILE).write_text(render_summary_markdown(aggregates))
    (reports_dir / REPORT_FILE).write_text(render_full_markdown(state, aggregates, rows))


def aggregate_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = f"{row['agent']}|{row.get('model') or ''}|{row['version']}|{row['mode']}"
        group = groups.setdefault(
            key,
            {
                "agent": row["agent"],
                "model": row.get("model"),
                "version": row["version"],
                "mode": row["mode"],
                "total": 0,
                "completed": 0,
                "passed": 0,
                "failed": 0,
                "status_failed": 0,
                "queued": 0,
                "running": 0,
                "n_input_tokens": 0,
                "n_cache_tokens": 0,
                "n_output_tokens": 0,
                "n_total_tokens": 0,
                "cost_usd": 0.0,
            },
        )
        group["total"] += 1
        status = row["status"]
        if status in {"queued", "running"}:
            group[status] += 1
        if status == "completed":
            group["completed"] += 1
        elif status == "failed":
            group["status_failed"] += 1
        if row.get("passed") is True:
            group["passed"] += 1
        elif status in {"completed", "failed"}:
            group["failed"] += 1
        add_numeric(group, row, "n_input_tokens")
        add_numeric(group, row, "n_cache_tokens")
        add_numeric(group, row, "n_output_tokens")
        add_numeric(group, row, "n_total_tokens")
        add_numeric(group, row, "cost_usd")
    for group in groups.values():
        denominator = group["completed"] + group["status_failed"]
        group["accuracy"] = (group["passed"] / denominator) if denominator else None
    return {"updated_at": utc_now(), "groups": sorted(groups.values(), key=aggregate_key)}


def add_numeric(target: dict[str, Any], source: dict[str, Any], key: str) -> None:
    value = source.get(key)
    if isinstance(value, (int, float)):
        target[key] += value


def aggregate_key(group: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(group.get("agent") or ""),
        str(group.get("model") or ""),
        str(group.get("version") or ""),
        str(group.get("mode") or ""),
    )


def render_summary_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# TB2 Queue Summary",
        "",
        f"Updated: `{summary['updated_at']}`",
        "",
        "| Agent | Model | Version | Mode | Done | Passed | Failed | Accuracy | Input Tokens | Cache Tokens | Output Tokens | Total Tokens | Cost USD |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for group in summary["groups"]:
        accuracy = "" if group["accuracy"] is None else f"{group['accuracy']:.3f}"
        lines.append(
            "| {agent} | {model} | {version} | {mode} | {done}/{total} | {passed} | {failed} | {accuracy} | {input_tokens} | {cache_tokens} | {output_tokens} | {total_tokens} | {cost_usd} |".format(
                agent=group["agent"],
                model=group.get("model") or "",
                version=group["version"],
                mode=group["mode"],
                done=group["completed"] + group["status_failed"],
                total=group["total"],
                passed=group["passed"],
                failed=group["failed"],
                accuracy=accuracy,
                input_tokens=format_int(group["n_input_tokens"]),
                cache_tokens=format_int(group["n_cache_tokens"]),
                output_tokens=format_int(group["n_output_tokens"]),
                total_tokens=format_int(group["n_total_tokens"]),
                cost_usd=format_cost(group["cost_usd"]),
            )
        )
    return "\n".join(lines) + "\n"


def format_int(value: Any) -> str:
    if not isinstance(value, (int, float)):
        return ""
    return str(int(value))


def format_cost(value: Any) -> str:
    if not isinstance(value, (int, float)):
        return ""
    return f"{value:.6f}" if value else "0"


def render_full_markdown(
    state: dict[str, Any], summary: dict[str, Any], rows: list[dict[str, Any]]
) -> str:
    lines = [
        "# TB2 Queue Report",
        "",
        f"Queue: `{state['settings']['queue_dir']}`",
        f"Dataset: `{state['settings']['dataset']}`",
        "",
        render_summary_markdown(summary).strip(),
        "",
        "## Jobs",
        "",
        "| Status | Task | Agent | Model | Version | Mode | Reward | Input Tokens | Cache Tokens | Output Tokens | Total Tokens | Cost USD | Error |",
        "|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        reward = "" if row.get("reward") is None else str(row.get("reward"))
        error = (row.get("error") or row.get("exception_type") or "").replace("|", "\\|")
        lines.append(
            f"| {row['status']} | {row['task_name']} | {row['agent']} | {row.get('model') or ''} | {row['version']} | {row['mode']} | {reward} | {format_int(row.get('n_input_tokens'))} | {format_int(row.get('n_cache_tokens'))} | {format_int(row.get('n_output_tokens'))} | {format_int(row.get('n_total_tokens'))} | {format_cost(row.get('cost_usd'))} | {error} |"
        )
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    enqueue = sub.add_parser("enqueue")
    enqueue.add_argument("queue_dir", type=Path)
    enqueue.add_argument("--dataset", default=DEFAULT_DATASET)
    enqueue.add_argument("--task-source-dir", type=Path)
    enqueue.add_argument("--task-name", action="append")
    enqueue.add_argument("--exclude-task-name", action="append")
    enqueue.add_argument("--n-tasks", type=int)
    enqueue.add_argument("--agent", choices=["claude-code", "oracle"], default="claude-code")
    enqueue.add_argument("--agent-import-path", default=DEFAULT_AGENT_IMPORT_PATH)
    enqueue.add_argument("--model")
    enqueue.add_argument("--version", action="append")
    enqueue.add_argument("--simple-version", action="append")
    enqueue.add_argument("--regular-version", action="append")
    enqueue.add_argument("--simple", action="store_true")
    enqueue.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"])
    enqueue.add_argument("--max-turns", type=int)
    enqueue.add_argument("--env-file", type=Path)
    enqueue.add_argument("--harbor-command")
    enqueue.add_argument("--delete-environment", action=argparse.BooleanOptionalAction, default=True)
    enqueue.add_argument("--force-build", action=argparse.BooleanOptionalAction, default=False)
    enqueue.add_argument("--extra-harbor-arg", action="append")
    enqueue.add_argument("--run-prefix")
    enqueue.add_argument("--append", action="store_true")
    enqueue.add_argument("--force", action="store_true")
    enqueue.set_defaults(func=cmd_enqueue)

    dequeue = sub.add_parser("dequeue")
    dequeue.add_argument("queue_dir", type=Path)
    dequeue.add_argument("--concurrency", type=int, default=1)
    dequeue.add_argument("--limit", type=int)
    dequeue.set_defaults(func=cmd_dequeue)

    status = sub.add_parser("status")
    status.add_argument("queue_dir", type=Path)
    status.set_defaults(func=cmd_status)

    report = sub.add_parser("report")
    report.add_argument("queue_dir", type=Path)
    report.set_defaults(func=cmd_report)

    reset = sub.add_parser("reset")
    reset.add_argument("queue_dir", type=Path)
    reset.add_argument("--only-failed", action="store_true")
    reset.set_defaults(func=cmd_reset)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
