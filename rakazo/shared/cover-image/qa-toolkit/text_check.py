#!/usr/bin/env python3
"""ค้นหา "ตัวอักษร" แบบ proxy: component เล็กสีเข้มที่มี edge สูง (คล้ายตัวเกิร์ฟ) ในพื้นที่ฉาก
ใช้: uv run --with pillow --with numpy --with scipy python3 text_check.py <file...>
"""
import sys, glob
import numpy as np
from PIL import Image
from scipy import ndimage


def check(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    mx = a.max(axis=2)
    mn = a.min(axis=2)
    gray = a.mean(axis=2)
    dark = (mx < 120) & ((mx - mn) < 60)
    lab, n = ndimage.label(dark)
    h, w = dark.shape
    glyphish = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        area = len(xs)
        if area < 40 or area > 1200:
            continue
        bw = xs.max() - xs.min() + 1
        bh = ys.max() - ys.min() + 1
        if bw < 6 or bh < 8 or bw > 160 or bh > 160:
            continue
        fill = area / float(bw * bh)
        if fill < 0.18 or fill > 0.92:
            continue
        # edge density inside the component
        sub = gray[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        ex = np.abs(np.diff(sub, axis=1)).max() if sub.shape[1] > 1 else 0
        ey = np.abs(np.diff(sub, axis=0)).max() if sub.shape[0] > 1 else 0
        ed = max(ex, ey)
        if ed < 40:
            continue
        glyphish.append((area, int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max()), round(fill, 2), round(float(ed), 1)))
    glyphish.sort(reverse=True)
    print(f"{path}")
    print(f"   glyph-like dark components: {len(glyphish)}")
    for g in glyphish[:12]:
        print(f"      area={g[0]:5d} x {g[1]}-{g[2]} y {g[3]}-{g[4]} fill={g[5]} edge={g[6]}")
    print()


for p in (sys.argv[1:] or sorted(glob.glob("/home/rakazo/work/cand/*.png"))):
    try:
        check(p)
    except Exception as e:
        print(f"{p} ERROR {e}\n")
