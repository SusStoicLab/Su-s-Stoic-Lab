---
name: "meta-systems-thinking"
description: "Apply systems thinking — causal loop diagrams, stock-and-flow models, system archetypes, and leverage-point analysis — to organizational, economic, or social problems where feedback loops, delays, or emergent behavior drive recurring failure across multiple interacting actors. Use this skill when the user describes a multi-actor situation that resists linear fixes: policy interventions that backfire, org-level fixes that break other teams, market symptoms that return after being solved, or time-lagged second-order consequences, even if they say 'why does fixing X make Y worse' or 'identify the leverage points in this system'. Do NOT use for single-cause software bugs, flaky tests, or regressions — those are debugging problems, not systems-thinking problems, even when phrased as 'this keeps coming back'. 中文触发词：系统思维、整体思维、因果回路、反馈循环、杠杆点、系统性问题、为什么越改越糟、治标不治本。"
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "systems-thinking", "complexity"]
---

## 中文使用说明（搬运补充）

- **中文名**：系统思维（Systems Thinking）
- **中文触发词**：系统思维、整体思维、因果回路、反馈循环、杠杆点、系统性问题、为什么越改越糟、治标不治本
- **来源备注**：本 skill 搬运自 GitHub 仓库 `asgard-ai-platform/skills`（目录 `meta-systems-thinking`），原作者 asgard。仅作个人学习使用，未改动原文核心内容，仅补充中文索引与触发词。随附 `references/system-archetypes.md`、`examples/sample_scenario.md`。

### 章节中文索引
| 原文章节 | 中文速查 |
|------|------|
| Framework / IRON LAW | 铁律：复杂系统里"直接修症状"会在 2 个周期内引发二阶反弹——干预前先画反馈回路 |
| Analysis Steps | 六步：定边界 → 列变量(存量/流量) → 找反馈回路(增强/调节) → 找延迟 → 定位杠杆点 → 查副作用 |
| Output Format | 输出格式：系统边界 / 关键变量 / 反馈回路 / 延迟 / 杠杆点 / 副作用风险 |
| Examples | 正例：多加人反而拖慢项目（布鲁克斯定律）；反例：营收下降就加营销（线性单因思维） |
| Gotchas | 误区：系统会抵抗改变；心智模型都是片面的；副作用是常态；不是所有问题都是系统问题 |
| References | 系统基模见 references/system-archetypes.md |

# Systems Thinking

## Framework

```
IRON LAW: First-Order Fixes in Complex Systems Produce Second-Order
Backlash Within 2 Cycles — Map the Feedback Loop BEFORE Intervening

Agents default to "fix the symptom directly" (e.g., high turnover → raise
salaries). In systems with feedback loops, the direct fix triggers a
compensating response that makes the original problem worse OR creates
a new one (raise salaries → budget squeeze → cut training → worse
onboarding → higher turnover). Before recommending any intervention,
draw the causal loop diagram and identify at least one reinforcing and
one balancing loop. If you can't find any, the problem may not be a
systems problem — don't force the framework.
```

### Analysis Steps

Key concepts assumed known: feedback loops (reinforcing/balancing), emergence,
delays, leverage points, stocks and flows. For system archetypes (Fixes That
Fail, Shifting the Burden, Limits to Growth, etc.) see
[`references/system-archetypes.md`](references/system-archetypes.md).

1. **Define the system boundary**: What's in, what's out?
2. **Map key variables**: What are the important stocks (quantities that accumulate)?
3. **Identify feedback loops**: Which loops are reinforcing? Which are balancing?
4. **Find delays**: Where is cause separated from effect in time?
5. **Locate leverage points**: Where would small interventions produce the biggest shift?
6. **Check for unintended consequences**: What might this intervention break elsewhere in the system?

## Output Format

```markdown
# Systems Analysis: {Problem}

## System Boundary
- In scope: ...
- Out of scope: ...

## Key Variables
- {Variable A}: {description}

## Feedback Loops
- Reinforcing: {A → B → A (amplifying)}
- Balancing: {A → B → C → opposes A (stabilizing)}

## Delays
- {Input} → {Effect} (delay: {timeframe})

## Leverage Points
1. {where small change = big impact}

## Unintended Consequences Risk
- If we {intervention}, it might also {side effect} because {loop/connection}
```

## Examples

### Correct Application
**Scenario:** Why does hiring more engineers not speed up the project?

**Reinforcing loop (intended)**: More engineers → more code → faster progress
**Balancing loop (unintended)**: More engineers → more communication overhead → more meetings → less coding time → slower progress (Brooks' Law)
**Delay**: New engineers need 3-6 months to become productive

**Leverage point**: Instead of adding people, reduce communication overhead (smaller teams, clearer ownership, better documentation) ✓

### Incorrect Application
- "Revenue is down. Increase marketing spend." → Linear, single-cause thinking. Ignoring: Why is revenue down? Is it demand (balancing loop from saturation)? Is it churn (reinforcing loop of poor quality → complaints → more churn)? Different root causes require different interventions.

## Gotchas

- **Systems resist change**: Balancing feedback loops maintain the status quo. Pushing against them without addressing the loop structure leads to "fixes that fail."
- **Mental models are partial**: Everyone's mental model of a system is incomplete. Mapping the system with diverse stakeholders reveals blind spots.
- **Unintended consequences are the norm, not the exception**: In complex systems, interventions always produce side effects. The question is whether you've identified the important ones.
- **Not everything is a system**: Simple problems with clear cause-and-effect don't need systems thinking. Use it for problems where linear thinking fails.

## References

- For system archetypes (Limits to Growth, Shifting the Burden, etc.), see `references/system-archetypes.md`
