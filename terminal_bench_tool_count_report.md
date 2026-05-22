# Terminal-Bench 2.0 Harness Tool Count Analysis

Date: 2026-05-22

## Summary

We investigated whether the number of tools/actions exposed by a Terminal-Bench 2.0 harness is associated with benchmark accuracy. The clearest signal appears when comparing harnesses against Terminus 2 on the same model, which controls for model capability more directly than a pooled leaderboard regression.

Main finding:

> Relative to Terminus 2 on the same model, harnesses with more tools show a statistically significant negative association between extra tool count and accuracy gain.

For the same-model comparison against Terminus 2:

- `n = 17` harness/model comparisons
- Regression: `accuracy_delta_vs_terminus2 = 11.99 - 0.60 * extra_tools`
- Slope: `-0.60` percentage points per additional tool
- `R^2 = 0.52`
- `t(15) = -4.06`
- Two-sided `p = 0.0010`

This remains significant after excluding Claude Code:

- `n = 13`
- Slope: `-0.35` percentage points per additional tool
- `R^2 = 0.39`
- Two-sided `p = 0.021`

This should be interpreted as observational evidence, not causal proof. Tool count is confounded with harness design, prompting style, scaffolding, tool affordances, and execution strategy.

## Sources

- Terminal-Bench 2.0 leaderboard: https://www.tbench.ai/leaderboard/terminal-bench/2.0
- Terminal-Bench 2.0 submission dataset: https://huggingface.co/datasets/harborframework/terminal-bench-2-leaderboard
- Mux source repository: https://github.com/coder/mux
- Capy documentation: https://docs.capy.ai/using-capy and https://docs.capy.ai/configs/settings
- Adya/MAYA public site: https://adya.ai/ and https://adya.ai/maya

## Tool Count Audit

The table below includes only harnesses for which we found numeric tool-count evidence. Some counts are stronger than others: several come directly from submitted artifacts or package/source inspection, while Capy's count comes from current public documentation rather than the exact submitted leaderboard artifact.

| Harness | Tool count | Evidence basis |
|---|---:|---|
| Meta-Harness | 1 | Submitted trajectory/tool call: `execute_commands` |
| Terminus-KIRA | 1 | Submitted trajectory/tool call: `bash_command` |
| Terminus 2 | 2 | Submitted trajectory/tool calls: `bash_command`, `mark_task_complete` |
| TongAgents | 3 | Submitted trajectory/tool calls: `save_plan`, `run_shell_command`, `write_file` |
| Capy | 7 | Capy docs list hookable Build tools: `bash_run`, `edit`, `multi_edit`, `write`, `read`, `glob`, `grep` |
| Droid | 9 | Submitted command enabled 10 tools, but stdout says `ApplyPatch` was unavailable and skipped |
| Claude Code | 19 | `@anthropic-ai/claude-code@2.1.34` SDK tool input schemas |
| Mux | 20 | Inferred run commit `f6218c255`, package `0.16.0`; 24 Anthropic tools minus 4 disabled by submitted policy |

Open or unresolved cases:

| Harness | Status |
|---|---|
| MAYA-V2 | No public source/tool schema found for `terminal_bench.agents.eval.adya1:Final` version `1.5-official`; public Adya site gives platform-level counts, not the exact benchmark harness count. |
| Crux | Metadata points to `https://github.com/0xDarkMatter/crux-agent`, but the repo was not publicly cloneable during audit; no exact tool count verified. |

## Opus 4.6-Only Regression

For the Opus 4.6 rows with numeric tool counts:

| Agent | Tools | Accuracy |
|---|---:|---:|
| Meta-Harness | 1 | 76.4 |
| Terminus-KIRA | 1 | 74.7 |
| TongAgents | 3 | 71.9 |
| Terminus 2 | 2 | 62.9 |
| Droid | 9 | 69.9 |
| Mux | 20 | 66.5 |
| Claude Code | 19 | 58.0 |

Linear regression:

```text
accuracy = 72.68 - 0.518 * tool_count
```

Statistics:

- `n = 7`
- Pearson `r = -0.662`
- `R^2 = 0.439`
- `t(5) = -1.98`
- Two-sided `p = 0.105`
- One-sided negative-direction `p = 0.053`

Including Capy's docs-derived 7-tool count:

```text
accuracy = 73.55 - 0.529 * tool_count
```

Statistics:

- `n = 8`
- Pearson `r = -0.631`
- `R^2 = 0.398`
- `t(6) = -1.99`
- Two-sided `p = 0.093`
- One-sided negative-direction `p = 0.047`

Interpretation:

The Opus 4.6-only relationship is negative but not significant under the standard two-sided `p < 0.05` threshold. It is suggestive, but the sample is too small to treat as robust.

## Full Known-Count Leaderboard Rows

When expanding beyond Opus 4.6 to all leaderboard rows where a harness has an assigned numeric tool count, there are 54 single-model rows. A naive pooled regression gives a positive association:

```text
accuracy = 39.27 + 0.89 * tool_count
```

Statistics:

- `n = 54`
- Slope: `+0.89` percentage points per tool
- Pearson `r = +0.28`
- Two-sided `p = 0.039`

This result is misleading because higher-tool harnesses are more often paired with newer or stronger models. This is a Simpson's-paradox-style confound: pooling across models mixes model capability with harness design.

## Model-Overlap Analysis

To reduce model confounding, we restricted the data to models that appear under at least two different tool counts. This produced:

- `n = 28`
- 9 overlapping models

Overlapping model groups:

| Model | Harness/tool-count observations |
|---|---|
| Claude Haiku 4.5 | Terminus 2: 2 tools, Claude Code: 19 |
| Claude Opus 4.1 | Terminus 2: 2 tools, Claude Code: 19 |
| Claude Opus 4.5 | Terminus 2: 2, Droid: 9, Claude Code: 19, Mux: 20 |
| Claude Opus 4.6 | Meta-Harness: 1, Terminus-KIRA: 1, Terminus 2: 2, TongAgents: 3, Capy: 7, Droid: 9, Claude Code: 19, Mux: 20 |
| Claude Sonnet 4.5 | Terminus 2: 2, Claude Code: 19 |
| GPT-5.2 | Terminus 2: 2, Droid: 9, Mux: 20 |
| GPT-5.3-Codex | Terminus 2: 2, Droid: 9, Mux: 20 |
| Gemini 3 Pro | Terminus 2: 2, Droid: 9 |
| Gemini 3.1 Pro | Terminus-KIRA: 1, TongAgents: 3 |

With model fixed effects:

```text
accuracy ~ tool_count + model
```

Tool coefficient:

- Slope: `-0.13` percentage points per tool
- `t(18) = -0.91`
- Two-sided `p = 0.377`

Interpretation:

After controlling for model identity with fixed effects, the tool-count coefficient is negative but not statistically significant. The overlap data is still sparse and unevenly distributed.

## Same-Model Comparison Against Terminus 2

The strongest analysis compares each harness/model run to Terminus 2 on the same model. This uses Terminus 2 as a baseline because it has broad model coverage and a verified 2-tool harness.

For each comparable row:

```text
accuracy_delta = harness_accuracy - terminus2_accuracy_for_same_model
extra_tools = harness_tool_count - 2
```

Regression:

```text
accuracy_delta = 11.99 - 0.60 * extra_tools
```

Statistics:

- `n = 17`
- Slope: `-0.60` percentage points per additional tool
- Pearson `r = -0.724`
- `R^2 = 0.524`
- `t(15) = -4.06`
- Two-sided `p = 0.0010`
- One-sided negative-direction `p = 0.00051`

This means that, relative to Terminus 2 on the same model, each additional tool is associated with about a `0.60` percentage point reduction in accuracy delta.

Sensitivity check excluding Claude Code:

- `n = 13`
- Slope: `-0.35` percentage points per additional tool
- Pearson `r = -0.628`
- `R^2 = 0.395`
- `t(11) = -2.68`
- Two-sided `p = 0.021`

This suggests the negative relationship is not only driven by Claude Code.

## Interpretation

The evidence does not support a simple claim that more tools improve Terminal-Bench 2.0 performance. In the cleanest same-model comparison against Terminus 2, more tools are associated with lower relative performance.

The most plausible interpretation is not that tools are inherently bad. Rather, larger tool surfaces may increase action-space complexity unless the harness has strong tool selection, prompting, tool descriptions, guardrails, and recovery behavior. Tool count may also proxy for broader harness complexity: multiple tools can create more opportunities for mis-selection, schema friction, permission issues, state inconsistency, or context overhead.

In this data:

- Pooled across all models, tool count is confounded by model strength and can even look positively associated with accuracy.
- Within overlapping model groups, the coefficient is negative but not statistically significant.
- Against Terminus 2 as a same-model baseline, the relationship is consistently negative and statistically significant.

## Caveats

1. This is observational, not causal.
2. Tool count is an imperfect proxy for action-space complexity. A single shell tool can be far more expressive than many narrow tools.
3. Some counts are not exact submitted-run counts. Capy's count is based on public docs, not the exact leaderboard artifact.
4. Harnesses differ in prompting, timeouts, execution policy, environment setup, retries, pass@k strategy, and context management.
5. The same-model comparison uses Terminus 2 as a baseline. That is useful because of its broad coverage, but it means the result is relative to one specific harness.
6. Sample sizes remain small, especially after controlling for model identity.

## Bottom Line

The best-supported conclusion is:

> In Terminal-Bench 2.0 rows where tool counts can be assigned, larger harness tool surfaces do not show a performance advantage. Relative to Terminus 2 on the same model, additional tools are associated with a statistically significant decrease in accuracy delta.

This should motivate a more careful harness-design study: compare fixed models across controlled harness variants where the only manipulated factor is the tool surface.
