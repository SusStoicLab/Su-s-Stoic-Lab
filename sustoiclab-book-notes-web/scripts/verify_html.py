#!/usr/bin/env python3
"""
单文件 HTML 交付前校验（三步）

用法:
    python verify_html.py <file.html>

1. JS 语法   —— 提取 <script> 用 node --check
2. SVG 路径  —— path 的 d 属性命令白名单
3. HTML 结构 —— 标签闭合 + 锚点 href/id 配对

退出码 0 = 全通过，1 = 有问题。
"""
import os
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

# SVG path 合法命令
PATH_CMDS = set("MmLlHhVvCcSsQqTtAaZz")
# SVG / void 元素，不计入标签栈
VOID = {
    "img", "br", "hr", "meta", "link", "input", "source", "area", "base",
    "col", "embed", "param", "track", "wbr",
    "path", "circle", "rect", "line", "ellipse", "polygon", "polyline",
    "use", "stop", "image",
}


def check_js(html, path):
    """提取 script 并交给 node --check。"""
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.S)
    scripts = [s for s in scripts if s.strip()]
    if not scripts:
        print("  [JS] 无 <script>，跳过")
        return True

    node = shutil_which("node")
    if not node:
        print("  [JS] 未找到 node，跳过语法检查")
        return True

    ok = True
    for i, js in enumerate(scripts):
        fd, tmp = tempfile.mkstemp(suffix=".js", prefix="_verify_")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(js)
        r = subprocess.run([node, "--check", tmp], capture_output=True, text=True)
        if r.returncode == 0:
            print(f"  [JS] script#{i + 1} 语法 OK ({len(js)} 字符)")
        else:
            ok = False
            print(f"  [JS] script#{i + 1} 语法错误:")
            for line in (r.stderr or "").strip().split("\n")[:6]:
                print(f"       {line}")
            print("       常见原因: 中文引号被转成半角 —— 用「」代替 \"\"")
        os.remove(tmp)
    return ok


def check_svg(html):
    """校验 <svg> 内 path 的 d 属性命令。"""
    bad = []
    total = 0
    for sm in re.finditer(r"<svg[^>]*>(.*?)</svg>", html, re.S):
        for m in re.finditer(r'\sd="([^"]+)"', sm.group(1)):
            total += 1
            d = m.group(1)
            for tok in re.findall(r"[A-Za-z]", d):
                if tok not in PATH_CMDS:
                    bad.append((tok, d[:60]))
    if bad:
        print(f"  [SVG] {len(bad)} 处非法命令 (共 {total} 条 path):")
        for tok, d in bad[:8]:
            print(f'       命令 "{tok}" in: {d}')
        print("       合法命令只有: M m L l H h V v C c S s Q q T t A a Z z")
        print("       最常见: 想写 Q 却打成 O（整条 path 会静默失效）")
        return False
    print(f"  [SVG] {total} 条 path 命令全部合法")
    return True


class _TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.mismatch = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass  # <foo /> 自闭合，不入栈

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
            self.mismatch.append(tag)
        else:
            self.mismatch.append(tag)


def check_structure(html):
    """标签闭合 + 锚点配对。"""
    c = _TagChecker()
    c.feed(html)

    ok = True
    if c.stack:
        ok = False
        print(f"  [HTML] 未闭合标签: {c.stack[:10]}")
    else:
        print("  [HTML] 标签全部闭合")
    if c.mismatch:
        print(f"  [HTML] 嵌套错位: {c.mismatch[:8]}")

    ids = set(re.findall(r'id="([A-Za-z0-9_\-]+)"', html))
    hrefs = set(re.findall(r'href="#([A-Za-z0-9_\-]+)"', html))
    broken = sorted(hrefs - ids)
    if broken:
        ok = False
        print(f"  [HTML] 断锚点 (href 无对应 id): {broken}")
    else:
        print(f"  [HTML] {len(hrefs)} 个锚点全部有效")

    # 占位符残留
    placeholders = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if placeholders:
        ok = False
        print(f"  [HTML] 占位符未替换: {set(placeholders)}")

    return ok


def shutil_which(cmd):
    from shutil import which
    return which(cmd)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    if not os.path.isfile(path):
        sys.exit(f"文件不存在: {path}")

    html = open(path, "r", encoding="utf-8").read()
    kb = len(html.encode("utf-8")) / 1024

    print(f"校验: {os.path.basename(path)}  ({kb:.1f} KB)")
    print("-" * 60)

    r1 = check_js(html, path)
    r2 = check_svg(html)
    r3 = check_structure(html)

    print("-" * 60)
    if r1 and r2 and r3:
        print("全部通过 ✓")
        sys.exit(0)
    print("存在问题 ✗")
    sys.exit(1)


if __name__ == "__main__":
    main()
