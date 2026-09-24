---
name: "meta-first-principles"
description: "Apply first principles thinking to break problems down to fundamental truths and reason up from there. Use this skill when the user is stuck in conventional thinking, needs to challenge assumptions, find breakthrough solutions, or evaluate whether something is truly impossible vs just assumed to be — even if they say 'everyone does it this way', 'is there a fundamentally better approach', 'why does it have to cost this much', or 'challenge my assumptions'. 中文触发词：第一性原理、拆解到本质、基本事实、挑战假设、追到根上、为什么一定要这样、成本拆解。"
metadata:
  category: "WP-22 跨學科"
  tags: ["meta-thinking", "first-principles", "problem-solving"]
---

## 中文使用说明（搬运补充）

- **中文名**：第一性原理思维（First Principles Thinking）
- **中文触发词**：第一性原理、第一性原理拆解、拆解到本质、基本事实、挑战假设、追到根上、为什么一定要这样、成本拆解
- **来源备注**：本 skill 搬运自 GitHub 仓库 `asgard-ai-platform/skills`（目录 `meta-first-principles`），原作者 asgard。仅作个人学习使用，**未改动原文核心内容**，仅补充本中文索引与触发词，便于中文语境下调用。

### 章节中文索引
| 原文章节 | 中文速查 |
|------|------|
| Framework / IRON LAW | 铁律：假设≠事实——多数"约束"是约定俗成，不是物理定律 |
| The Method | 三步法：①识别假设 ②拆解到基本事实（五问法/成本分解/物理层分析）③从事实向上推导 |
| Example: Elon Musk on Battery Costs | 案例：马斯克电池成本（市价 $600 → 原材料 ~$80/kWh，差额是制造与供应链，不是物理） |
| Five Whys | 五问法：连问 5 次"为什么"挖到未检验的惯例 |
| Cost Decomposition Template | 成本拆解模板：逐项判断"物理成本 vs 惯例成本" |
| Output Format | 输出格式：假设 / 拆解表 / 基本事实 / 向上推导 / 建议方案 |
| Gotchas | 误区：别事事重发明；物理约束真实存在；惯例也有价值（要审视而非自动否定）；执行才是关键 |

# First Principles Thinking

## Framework

```
IRON LAW: Assumptions Are Not Facts

Most "constraints" are assumed, not physical. "We can't do X" usually means
"We haven't seen anyone do X" or "The current method doesn't allow X."
First principles thinking distinguishes between:
- Physical laws (actual constraints: gravity, thermodynamics)
- Conventions (assumed constraints: "this is how it's done")
```

### The Method

**1. Identify the assumption**: What do "everyone knows" or "everyone does"?

**2. Break it down to fundamentals**: What are the basic, irreducible facts?
- Techniques: "Five Whys" (ask why 5 times), cost decomposition, physics-level analysis

**3. Reason up from fundamentals**: Given only the base facts, what's the best solution?

### Example: Elon Musk on Battery Costs (2010s)

- **Convention**: "Batteries cost $600/kWh. Electric cars will always be too expensive."
- **First principles**: What are batteries made of? Cobalt, nickel, lithium, carbon, metals, polymers. What do these raw materials cost? ~$80/kWh at commodity prices.
- **Reasoning up**: If we buy materials and build batteries ourselves, we can potentially reduce costs to near $80/kWh. The $520 gap is manufacturing inefficiency and supply chain markup, not physics.

### Five Whys for Assumption Drilling

1. "Why is our product priced at $100?" — Because our COGS is $60 and we need 40% margin.
2. "Why is COGS $60?" — Because we use supplier X for component Y.
3. "Why do we use supplier X?" — Because we've always used them.
4. "Why haven't we looked at alternatives?" — Because the procurement team hasn't been asked to.
5. "Why not?" — **There's no real reason. It's just convention.**

→ Fundamental constraint found: the COGS includes an unexamined supplier relationship, not a physical constraint.

### Cost Decomposition Template

For any "it costs too much" problem:
1. List every cost component
2. For each, identify: Is this cost from physics (materials, energy) or from convention (markup, inefficiency, legacy process)?
3. Question every convention-based cost

## Output Format

```markdown
# First Principles Analysis: {Problem}

## The Assumption
{What "everyone knows" or the conventional constraint}

## Decomposition
| Component | Cost/Fact | Physics or Convention? |
|-----------|----------|----------------------|
| {element} | {value} | Physics / Convention |

## Fundamental Truths
{What remains after stripping away assumptions}

## Reasoning Up
{Given only fundamental truths, what's the best approach?}

## Proposed Solution
{What changes if we ignore conventions and reason from fundamentals}
```

## Gotchas

- **Don't reinvent the wheel for everything**: First principles is expensive (time, effort). Use it for high-stakes problems where conventional approaches clearly fail. For routine decisions, best practices and heuristics are fine.
- **Physics constraints are real**: Don't confuse first principles thinking with ignoring physical reality. You can't reason your way past thermodynamics.
- **"Convention" has value**: Conventions encode collective experience. Dismissing all conventions as "assumptions" is arrogance, not first principles thinking. The point is to EXAMINE conventions, not automatically reject them.
- **Execution matters**: A first-principles insight is worthless without execution capability. SpaceX didn't just THINK about cheap rockets — they BUILT a vertically integrated manufacturing operation.

## References

- For Socratic questioning method (complementary), see the hum-socratic skill
