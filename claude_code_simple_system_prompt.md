# Claude Code Simple System Prompt

Captured from a local fake Anthropic endpoint while invoking `@anthropic-ai/claude-code@2.1.145` with the benchmark wrapper-style environment.

## Capture Metadata

- Mode: `simple`
- CLI package: `@anthropic-ai/claude-code@2.1.145`
- Model argument/env: `claude-sonnet-4-6`
- `CLAUDE_CODE_SIMPLE`: `1`
- Request path: `/v1/messages?beta=true`
- Tool count in captured API request: `3`
- Tools: `Bash, Edit, Read`

## Concatenated System Text

### System Block 1

```text
x-anthropic-billing-header: cc_version=2.1.145.b21; cc_entrypoint=sdk-cli; cch=1b164;
```

### System Block 2

```text
You are a Claude agent, built on Anthropic's Claude Agent SDK.
```

### System Block 3

```text
CWD: /tmp/cc-work-simple
Date: 2026-05-22
```

## Raw API `system` Value

```json
[
  {
    "type": "text",
    "text": "x-anthropic-billing-header: cc_version=2.1.145.b21; cc_entrypoint=sdk-cli; cch=1b164;"
  },
  {
    "type": "text",
    "text": "You are a Claude agent, built on Anthropic's Claude Agent SDK.",
    "cache_control": {
      "type": "ephemeral"
    }
  },
  {
    "type": "text",
    "text": "CWD: /tmp/cc-work-simple\nDate: 2026-05-22",
    "cache_control": {
      "type": "ephemeral"
    }
  }
]
```
