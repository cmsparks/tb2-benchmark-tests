# TB2 Claude Bench

Harbor-backed queue runner for Terminal-Bench 2.0 Claude Code version sweeps.

This repo intentionally uses Harbor as the execution harness for TB2:

```bash
harbor run -d terminal-bench/terminal-bench-2 ...
```

The local scripts only handle queue state, version/mode matrices, background-friendly dequeueing, and Markdown/JSON reporting.

## Setup

```bash
uv venv
uv pip install -e .
cp /root/terminal-bench/.env .env  # if needed
```

## Smoke Tests

Oracle:

```bash
scripts/tb2_queue.py enqueue queues/oracle-smoke \
  --agent oracle \
  --task-name adaptive-rejection-sampler \
  --force

scripts/tb2_queue.py dequeue queues/oracle-smoke --concurrency 1
```

Claude Code:

```bash
scripts/tb2_queue.py enqueue queues/claude-smoke \
  --model anthropic/claude-sonnet-4-6 \
  --effort medium \
  --version 2.1.145:regular \
  --task-name adaptive-rejection-sampler \
  --force

scripts/tb2_queue.py dequeue queues/claude-smoke --concurrency 1
```

## Full Matrix Example

```bash
scripts/tb2_queue.py enqueue queues/tb2-sonnet46 \
  --model anthropic/claude-sonnet-4-6 \
  --effort medium \
  --version 0.2.66:regular \
  --version 1.0.0:regular \
  --version 2.0.0:regular \
  --version 2.1.0:regular \
  --version 2.1.48:regular \
  --version 2.1.48:simple \
  --version 2.1.115:regular \
  --version 2.1.115:simple \
  --version 2.1.116:regular \
  --version 2.1.116:simple \
  --version 2.1.145:regular \
  --version 2.1.145:simple \
  --force
```

Reports are regenerated after enqueue/dequeue/report:

- `queues/<name>/reports/report.summary.md`
- `queues/<name>/reports/report.md`
- `queues/<name>/reports/results.jsonl`
- `queues/<name>/reports/summary.json`
