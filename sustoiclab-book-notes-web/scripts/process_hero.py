#!/usr/bin/env python3
"""
hero 图处理：裁水印 → 压缩 → base64 → 注入 HTML 模板 → 删中间文件

用法:
    python process_hero.py <原图> <模板.html> <输出.html> [--mode crop|blur] [--width 1280]

模板里放占位符 {{HERO_B64}}，例如:
    <div class="hero" style="background-image:url('data:image/jpeg;base64,{{HERO_B64}}')">

水印模式:
    crop  右下角一整块水印  -> 直接裁掉右下 (默认裁 220x52)
    blur  右下+右上小水印   -> 采样邻近像素 + 高斯模糊覆盖

依赖: pillow
    pip install pillow
"""
import argparse
import base64
import os
import sys

try:
    from PIL import Image, ImageFilter
except ImportError:
    sys.exit("需要 pillow: pip install pillow")


def remove_watermark_crop(img, w=220, h=52):
    """右下角整块水印：直接裁掉。会改变图片比例。"""
    W, H = img.size
    return img.crop((0, 0, W - w, H - h))


def remove_watermark_blur(img, regions=None):
    """多个小水印：采样邻近像素填补 + 高斯模糊。

    regions: [(x0, y0, x1, y1), ...] 归一化坐标(0~1)，默认右下+右上。
    """
    W, H = img.size
    if regions is None:
        regions = [(0.82, 0.90, 1.0, 1.0), (0.90, 0.0, 1.0, 0.06)]
    out = img.copy()
    for (rx0, ry0, rx1, ry1) in regions:
        box = (int(rx0 * W), int(ry0 * H), int(rx1 * W), int(ry1 * H))
        # 从水印正上方同尺寸区域取像素当补丁（同色调，不会有色块感）
        ph = box[3] - box[1]
        src = (box[0], max(0, box[1] - ph - 10), box[2], max(ph, box[1] - 10))
        patch = out.crop(src).filter(ImageFilter.GaussianBlur(6))
        out.paste(patch, box)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="原图路径（AI 生成的 PNG）")
    ap.add_argument("template", help="含 {{HERO_B64}} 的 HTML 模板")
    ap.add_argument("output", help="输出 HTML 路径")
    ap.add_argument("--mode", choices=["crop", "blur"], default="blur")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--quality", type=int, default=82)
    ap.add_argument("--crop-box", default="220,52", help="crop 模式的裁剪尺寸 w,h")
    ap.add_argument("--keep-tmp", action="store_true", help="保留中间 JPG")
    args = ap.parse_args()

    print(f"[1/5] 打开 {args.src}")
    img = Image.open(args.src).convert("RGB")
    print(f"      尺寸 {img.size}")

    print(f"[2/5] 去水印 mode={args.mode}")
    if args.mode == "crop":
        w, h = (int(x) for x in args.crop_box.split(","))
        img = remove_watermark_crop(img, w, h)
    else:
        img = remove_watermark_blur(img)
    print(f"      处理后 {img.size}")

    print(f"[3/5] 压缩到宽 {args.width}, quality={args.quality}")
    ratio = args.width / img.size[0]
    img = img.resize((args.width, int(img.size[1] * ratio)), Image.LANCZOS)

    tmp = os.path.splitext(args.output)[0] + ".__hero_tmp.jpg"
    img.save(tmp, "JPEG", quality=args.quality, optimize=True)
    kb = os.path.getsize(tmp) / 1024
    print(f"      {kb:.0f} KB")

    print("[4/5] base64 编码 + 注入模板")
    with open(tmp, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")

    with open(args.template, "r", encoding="utf-8") as f:
        html = f.read()

    if "{{HERO_B64}}" not in html:
        sys.exit("模板里没找到 {{HERO_B64}} 占位符")

    html = html.replace("{{HERO_B64}}", b64)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)

    print("[5/5] 清理中间文件")
    if not args.keep_tmp:
        os.remove(tmp)
        print(f"      已删 {os.path.basename(tmp)}")

    final_kb = os.path.getsize(args.output) / 1024
    print(f"\n完成: {args.output}  ({final_kb:.0f} KB)")
    print("提示: 原图 PNG 也要删 —— python -c \"import os;os.remove(r'<png>')\"")


if __name__ == "__main__":
    main()
