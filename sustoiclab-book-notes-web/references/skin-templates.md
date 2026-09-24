# 两套皮肤完整 CSS

从已交付的 4 本里提炼的真实样式。直接抄，不要重新发明。

---

# A. 学术笔记风

适用：思想类、心理学、经管、科普等非虚构。
观感：米色纸感、衬线标题、深红书签色带、照片 hero 压渐变蒙版。

## 变量

```css
:root{
  --paper:        #f5efe0;   /* 米色纸 */
  --paper-2:      #faf6ec;   /* 卡片浅底 */
  --paper-3:      #ede4cf;   /* 分隔/边框 */
  --ink:          #2a1f15;   /* 正文 */
  --ink-soft:     #4a3a28;
  --ink-mute:     #6b5a44;
  --gold:         #b58838;   /* 金线 */
  --gold-soft:    #d6b271;
  --crimson:      #8b1e1e;   /* 书签色带 */
  --crimson-soft: #a8482a;
  --rule:         #c8b890;
  --serif:  "Microsoft YaHei","Microsoft YaHei UI","微软雅黑",sans-serif;
  --display:"Georgia","Times New Roman",serif;   /* 仅英文装饰 */
  --sans:   "Microsoft YaHei","微软雅黑","PingFang SC","Hiragino Sans GB",sans-serif;
}
```

## 纸感背景（关键，别用纯色）

```css
body{
  font-family:var(--serif);
  line-height:1.75;
  font-size:17px;
  -webkit-font-smoothing:antialiased;
  background-color:var(--paper);
  background-image:
    radial-gradient(ellipse 80% 60% at 50% 0%, #fff8e6 0%, transparent 60%),
    radial-gradient(ellipse 100% 80% at 50% 100%, #e8dcc0 0%, transparent 70%),
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.55  0 0 0 0 0.45  0 0 0 0 0.30  0 0 0 0.05 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  background-attachment:fixed;
}
```

第三层是 SVG feTurbulence 噪点，纸感全靠它。**注意 `%23n` 是 `#n` 的 URL 编码，不能写成 `#`。**

## 顶部书签色带导航

```css
.bookmark{
  background:#2a1d10;
  color:#e9d9b6;
  border-bottom:1px solid #1a1209;
  position:sticky; top:0; z-index:50;
}
.bookmark__inner{
  max-width:1100px;margin:0 auto;
  display:flex;flex-wrap:wrap;
  font-family:var(--sans);font-size:13px;letter-spacing:.06em;
}
.bookmark__tab{
  position:relative;
  padding:14px 22px 14px 28px;
  color:#c8b890;
  text-decoration:none;
  border-right:1px solid #1a1209;
  transition:background .2s,color .2s;
}
.bookmark__tab:hover{background:#3a2818;color:#f5d993}
.bookmark__tab::before{               /* 左侧深红竖条 = 书签丝带 */
  content:"";
  position:absolute;left:14px;top:50%;
  width:4px;height:14px;
  background:var(--crimson);
  transform:translateY(-50%);
  border-radius:1px;
}
.bookmark__tab--home{color:#f5d993;font-weight:500}
```

## 书籍信息卡（带深红色带侧栏）

```css
.bookcard{display:grid;grid-template-columns:300px 1fr;border:1px solid var(--rule)}
.bookcard__ribbon{
  background:linear-gradient(180deg,#8b1e1e 0%,#6b1414 100%);
  color:#f7e9c8;
  padding:32px 30px;
  position:relative;
}
.bookcard__ribbon::after{               /* 左侧金-红-金渐变条 */
  content:"";position:absolute;left:0;top:0;bottom:0;width:6px;
  background:linear-gradient(180deg,#d6b271 0%,#8b1e1e 50%,#d6b271 100%);
}
.bookcard__ribbon h3{
  font-family:var(--display);font-weight:600;
  font-size:22px;letter-spacing:.04em;margin-bottom:18px;
  border-bottom:1px solid rgba(247,233,200,.25);
  padding-bottom:12px;
}
```

## 金句引用块

```css
.quotes{display:grid;gap:20px}
.quote{
  background:var(--paper-2);
  border:1px solid var(--rule);
  padding:30px 34px;
  position:relative;
}
.quote::before{
  content:"\201C";                      /* 左双引号 */
  position:absolute;left:18px;top:6px;
  font-family:var(--display);
  font-size:56px;color:var(--gold-soft);
  line-height:1;
}
```

## Hero（照片 + 渐变蒙版）

```css
.hero{
  position:relative;
  min-height:min(62vh,520px);
  background-image:var(--hero);         /* JS 或内联 style 里给 base64 */
  background-size:cover;
  background-position:center;
  display:flex;align-items:flex-end;
}
.hero::after{                           /* 压暗下半部分，保证白字可读 */
  content:"";
  position:absolute;inset:0;
  background:linear-gradient(180deg,
    rgba(26,18,9,.28) 0%,
    rgba(26,18,9,.55) 45%,
    rgba(26,18,9,.88) 100%);
}
.hero__body{position:relative;z-index:2;color:#fff;padding:0 28px 56px}
```

## 章节标题

```css
h2.section__title{
  font-family:var(--display);
  font-weight:600;
  font-size:clamp(28px,3.4vw,40px);
  margin-bottom:8px;
  position:relative;padding-left:18px;
}
h2.section__title::before{              /* 左侧金色竖条 */
  content:"";position:absolute;left:0;top:.28em;bottom:.28em;
  width:5px;background:var(--gold);
}
```

---

# B. 漫画手绘风

适用：工具书、自助书、童书、原书本身是插画/漫画风格的。
观感：粗黑描边、硬阴影、奶油底、分章主题色。

## 变量

```css
:root{
  --stuck:#FF6B6B;    /* 卡住 · 珊瑚红 */
  --over:#FF9F45;     /* 不堪重负 · 橙 */
  --unmot:#FFD23F;    /* 没动力 · 明黄 */
  --disorg:#4ECDC4;   /* 混乱 · 青绿 */
  --disc:#9B72E8;     /* 泄气 · 紫 */
  --ink:#2B2B2B;      /* 描边墨色，全站唯一 */
  --paper:#FFFDF5;    /* 奶油纸 */
  --paper2:#FFF6E0;
  --paper3:#FFEFD0;
  --grey:#8A8172;
  --font-cute:"YouYuan","幼圆","Microsoft YaHei","微软雅黑",sans-serif;  /* 标题 */
  --font-body:"Microsoft YaHei","微软雅黑","PingFang SC",sans-serif;      /* 正文 */
  --font-en:"Comic Sans MS","Chalkboard SE","Marker Felt",cursive;        /* 英文/数字 */
  --maxw:1040px;
}
```

## 波点背景（不用噪点，用彩色圆点）

```css
body{
  font-family:var(--font-body);
  background:var(--paper);
  color:var(--ink);
  line-height:1.75;
  font-size:16px;
  background-image:
    radial-gradient(circle at 12% 8%, rgba(255,107,107,.07) 0 8%, transparent 8.5%),
    radial-gradient(circle at 88% 14%, rgba(255,210,63,.10) 0 6%, transparent 6.5%),
    radial-gradient(circle at 78% 76%, rgba(78,205,196,.08) 0 7%, transparent 7.5%),
    radial-gradient(circle at 18% 88%, rgba(155,114,232,.07) 0 6%, transparent 6.5%);
}
```

## 贴纸卡（这套皮肤的核心识别元素）

```css
.card{
  background:#fff;
  border:3px solid var(--ink);
  border-radius:16px;
  box-shadow:6px 6px 0 var(--ink);   /* 硬阴影，不要模糊 */
  padding:22px 24px;
}
.tag{
  display:inline-block;
  font-family:var(--font-en);
  font-size:12px;letter-spacing:.14em;
  padding:2px 10px;
  border:2px solid var(--ink);
  border-radius:20px;
  background:#fff;
  margin-bottom:10px;
}
```

## 章节标题

```css
h2.sec{
  font-family:var(--font-cute);
  font-size:34px;line-height:1.25;
  margin-bottom:8px;
}
h2.sec .en{
  display:block;
  font-family:var(--font-en);
  font-size:14px;letter-spacing:.22em;
  color:var(--grey);
  margin-bottom:2px;
}
```

---

# 通用

## 响应式断点（两个，别只做一个）

```css
/* 760px：网格折两列 / 单列，导航换行 */
@media (max-width:760px){
  main{padding:44px 20px 60px}
  .bookcard{grid-template-columns:1fr}     /* 色带改横排在上 */
  h2.section__title{font-size:26px}
  .hero{min-height:46vh}
}
/* 420px：极限窄屏，防止文字被裁 */
@media (max-width:420px){
  main{padding:36px 16px 48px}
  h2.sec{font-size:26px}
  .hero__body{padding-bottom:36px}
}
```

**手机上不裁切的三条硬规则**：
1. 标题统一用 `clamp(min, vw, max)`，不要写死 px
2. hero 用 `min-height` 不用 `height`
3. 网格用 `grid-template-columns:repeat(auto-fit,minmax(260px,1fr))` 让它自己折

## 打印样式（可打印小卡片专用）

```css
@media print{
  body{background:#fff}
  .no-print,.bookmark,.hero{display:none !important}
  .card{box-shadow:none;border:2px solid #000;page-break-inside:avoid}
  @page{margin:12mm}
}
```

## 落款

```html
<footer>— 苏庶 @ 钝感实验室 · 读书笔记 —</footer>
```
