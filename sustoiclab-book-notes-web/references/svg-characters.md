# SVG 手绘小人库

漫画手绘风专用。全部 `viewBox="0 0 118 96"`，可直接复用、改配色、加动画。

## 通用规范

```css
stroke="#2B2B2B"          /* 统一描边色，不要换 */
stroke-width="3 ~ 3.5"    /* 主体轮廓 */
stroke-width="2.5 ~ 3"    /* 五官和细节 */
stroke-linecap="round"    /* 所有线条必带，否则显得硬 */
```

**身体结构三件套**（按这个顺序叠）：
1. 地面影子：`<ellipse cx="59" cy="88" rx="30" ry="4" fill="#000" opacity=".1"/>`
2. 身体：`<path>` 或 `<rect>`，`fill` 用主题色
3. 头：`<circle cx="59" cy="34" r="17" fill="#FFD9B3" .../>`（肤色固定）

**path 命令白名单**：`M m L l H h V v C c S s Q q T t A a Z z`
写错（如把 `Q` 打成 `O`）整条 path 静默失效，页面上就是一块空白 —— 必须跑校验脚本。

---

## 配色系统（5 章主题色 + 中性）

```css
--red:    #FF6B6B   /* 卡住 / 紧急 */
--orange: #FF9F45   /* 不堪重负 */
--yellow: #FFD23F   /* 没动力 / 提示 */
--teal:   #4ECDC4   /* 混乱 / 进行中 */
--purple: #9B72E8   /* 泄气 / 隐藏彩蛋 */
--blue:   #5AA9E6   /* 辅助线条（眼泪、雨、流动） */
--skin:   #FFD9B3   /* 肤色，固定不改 */
--hair:   #6B4A32   /* 头发，固定不改 */
--ink:    #2B2B2B   /* 描边，固定不改 */
```

---

## 1. 卡住（Stuck）· 死机

红衣小人僵住，头顶一条虚线写着"开始"，两条手臂直挺挺下垂。

```html
<svg viewBox="0 0 118 96">
  <ellipse cx="59" cy="88" rx="34" ry="4" fill="#000" opacity=".1"/>
  <path d="M22 88 L22 60 Q22 54 30 54 L88 54 Q96 54 96 60 L96 88 Z" fill="#FF6B6B" stroke="#2B2B2B" stroke-width="3.5"/>
  <circle cx="59" cy="34" r="19" fill="#FFD9B3" stroke="#2B2B2B" stroke-width="3.5"/>
  <circle cx="52" cy="32" r="2.8" fill="#2B2B2B"/>
  <circle cx="66" cy="32" r="2.8" fill="#2B2B2B"/>
  <path d="M51 42 Q59 38 67 42" stroke="#2B2B2B" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M40 60 L26 70 M78 60 L92 70" stroke="#2B2B2B" stroke-width="8" stroke-linecap="round"/>
  <path d="M46 24 Q59 14 72 24" stroke="#6B4A32" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M104 30 L104 78" stroke="#2B2B2B" stroke-width="3" stroke-dasharray="3 4"/>
  <text x="100" y="24" font-family="Comic Sans MS" font-size="11" fill="#d63b52" text-anchor="middle">开始</text>
</svg>
```

## 2. 不堪重负（Overwhelmed）· 摇摇欲坠的塔

三个箱子叠在头顶，小人被压得眼睛成了叉叉。

```html
<svg viewBox="0 0 118 96">
  <ellipse cx="59" cy="88" rx="32" ry="4" fill="#000" opacity=".1"/>
  <circle cx="59" cy="56" r="17" fill="#FFD9B3" stroke="#2B2B2B" stroke-width="3.5"/>
  <path d="M52 54 L48 50 M52 58 L48 58 M60 54 L64 50 M60 58 L64 58" stroke="#2B2B2B" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M52 66 Q59 62 66 66" stroke="#2B2B2B" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M42 70 L36 84 M76 70 L82 84" stroke="#2B2B2B" stroke-width="7" stroke-linecap="round"/>
  <rect x="34" y="40" width="50" height="10" rx="2" fill="#FF9F45" stroke="#2B2B2B" stroke-width="3"/>
  <rect x="30" y="30" width="58" height="10" rx="2" fill="#FF6B6B" stroke="#2B2B2B" stroke-width="3"/>
  <rect x="40" y="20" width="38" height="10" rx="2" fill="#FFD23F" stroke="#2B2B2B" stroke-width="3"/>
  <path d="M59 12 L59 6" stroke="#2B2B2B" stroke-width="3" stroke-linecap="round"/>
</svg>
```

## 3. 没动力（Unmotivated）· 电量 0%

黄衣小人半闭眼，旁边手机显示 0%，头顶两团紫色"不想动"的气。

```html
<svg viewBox="0 0 118 96">
  <ellipse cx="59" cy="88" rx="30" ry="4" fill="#000" opacity=".1"/>
  <path d="M30 84 L34 60 Q36 50 48 50 L70 50 Q82 50 84 60 L88 84 Z" fill="#FFD23F" stroke="#2B2B2B" stroke-width="3.5"/>
  <circle cx="52" cy="36" r="17" fill="#FFD9B3" stroke="#2B2B2B" stroke-width="3.5"/>
  <path d="M45 34 L49 34 M55 34 L59 34" stroke="#2B2B2B" stroke-width="3" stroke-linecap="round"/>
  <path d="M46 44 Q52 42 58 44" stroke="#2B2B2B" stroke-width="3" fill="none" stroke-linecap="round"/>
  <rect x="88" y="52" width="18" height="28" rx="2" fill="#fff" stroke="#2B2B2B" stroke-width="3"/>
  <rect x="94" y="48" width="6" height="5" fill="#2B2B2B"/>
  <path d="M93 62 L101 62" stroke="#FF6B6B" stroke-width="3" stroke-linecap="round"/>
  <text x="97" y="76" font-family="Comic Sans MS" font-size="10" fill="#FF6B6B" text-anchor="middle">0%</text>
  <path d="M24 30 Q30 22 36 30" stroke="#9B72E8" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M20 22 Q26 14 32 22" stroke="#9B72E8" stroke-width="3" fill="none" stroke-linecap="round"/>
</svg>
```

## 4. 混乱（Disorganized）· 满天飞的碎片

青衣小人，四角散落彩色纸片，中央一个大问号。

```html
<svg viewBox="0 0 118 96">
  <ellipse cx="59" cy="88" rx="30" ry="4" fill="#000" opacity=".1"/>
  <circle cx="59" cy="34" r="17" fill="#FFD9B3" stroke="#2B2B2B" stroke-width="3.5"/>
  <circle cx="53" cy="32" r="2.6" fill="#2B2B2B"/>
  <circle cx="65" cy="32" r="2.6" fill="#2B2B2B"/>
  <path d="M52 42 Q59 39 66 42" stroke="#2B2B2B" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M44 52 L44 76 Q44 84 52 84 L66 84 Q74 84 74 76 L74 52 Z" fill="#4ECDC4" stroke="#2B2B2B" stroke-width="3.5"/>
  <path d="M44 60 L28 54 M74 60 L90 54" stroke="#2B2B2B" stroke-width="7" stroke-linecap="round"/>
  <g stroke="#2B2B2B" stroke-width="2.5">
    <rect x="12" y="16" width="15" height="11" rx="1" fill="#FF6B6B" transform="rotate(-24 19 21)"/>
    <rect x="92" y="14" width="15" height="11" rx="1" fill="#FFD23F" transform="rotate(20 99 19)"/>
    <rect x="20" y="76" width="15" height="11" rx="1" fill="#9B72E8" transform="rotate(14 27 81)"/>
    <rect x="88" y="74" width="15" height="11" rx="1" fill="#FF9F45" transform="rotate(-16 95 79)"/>
  </g>
  <text x="59" y="12" font-family="Comic Sans MS" font-size="14" fill="#9B72E8" text-anchor="middle">?</text>
</svg>
```

## 5. 泄气（Discouraged）· 头顶下雨

紫衣小人低着头，头顶一朵云在下蓝色雨。

```html
<svg viewBox="0 0 118 96">
  <ellipse cx="59" cy="88" rx="26" ry="4" fill="#000" opacity=".1"/>
  <circle cx="59" cy="52" r="17" fill="#FFD9B3" stroke="#2B2B2B" stroke-width="3.5"/>
  <path d="M52 50 Q55 45 58 50 M60 50 Q63 45 66 50" stroke="#2B2B2B" stroke-width="2.8" fill="none" stroke-linecap="round"/>
  <path d="M53 60 Q59 56 65 60" stroke="#2B2B2B" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M42 66 L36 80 Q34 84 40 84 L78 84 Q84 84 82 80 L76 66 Z" fill="#9B72E8" stroke="#2B2B2B" stroke-width="3.5"/>
  <path d="M46 70 L40 78 M72 70 L78 78" stroke="#2B2B2B" stroke-width="6" stroke-linecap="round"/>
  <g fill="#9B72E8" stroke="#2B2B2B" stroke-width="2.5">
    <circle cx="42" cy="22" r="9"/>
    <circle cx="59" cy="17" r="10"/>
    <circle cx="76" cy="22" r="9"/>
    <rect x="33" y="22" width="52" height="9" rx="4.5"/>
  </g>
  <path d="M42 33 L41 42 M52 33 L52 43 M66 33 L66 43 M76 33 L77 42" stroke="#5AA9E6" stroke-width="3" stroke-linecap="round"/>
</svg>
```

---

## 表情速查（改五官即可换状态）

| 状态 | 眼睛 | 嘴 |
|---|---|---|
| 正常 | `<circle r="2.6"/>` ×2 | `M52 42 Q59 39 66 42`（微笑） |
| 开心 | 同上 | `M51 41 Q59 47 67 41`（大笑弧） |
| 疲惫 | `M45 34 L49 34 M55 34 L59 34`（横线） | `M53 44 Q59 42 65 44`（平） |
| 崩溃 | `M52 54 L48 50` 等四条斜线（叉） | `M52 66 Q59 62 66 66`（倒弧） |
| 难过 | `M52 50 Q55 45 58 50`（倒 V 弧）×2 | `M53 60 Q59 56 65 60`（倒弧） |

## 加动画（可选，别滥用）

```css
@keyframes bob { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-5px)} }
.char { animation: bob 3s ease-in-out infinite; }
@media (prefers-reduced-motion: reduce) { .char { animation: none } }
```

**只给 hero 区的小人加动画**，内容区静止 —— 满屏都在动会分散注意力。
