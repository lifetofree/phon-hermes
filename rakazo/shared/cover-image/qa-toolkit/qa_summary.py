#!/usr/bin/env python3
"""สรุป QA แบบกระชับสำหรับหลายไฟล์"""
import sys, hashlib, glob
from PIL import Image
import numpy as np

def qa(path):
    im = Image.open(path)
    w, h = im.size
    a = np.asarray(im.convert("RGB")).astype(np.float64)
    md5 = hashlib.md5(open(path, "rb").read()).hexdigest()
    gray = a.mean(axis=2)
    d_x = np.abs(np.diff(gray, axis=1)).max(axis=1)
    d_y = np.abs(np.diff(gray, axis=0)).max(axis=1)
    d_y = np.append(d_y, d_y[-1])
    row_edge = np.maximum(d_x, d_y)
    top = slice(0, int(h * 0.20))
    bot = slice(int(h * 0.70), h)
    # content rows: row_edge > 8 (ignore faint gradient noise)
    idx = np.where(row_edge > 8)[0]
    if len(idx):
        c0, c1 = idx.min(), idx.max()
    else:
        c0, c1 = 0, h - 1
    # saturated colour pixels (letters/logos often have strong chroma) in whole image
    spread = a.max(axis=2) - a.min(axis=2)
    n_sat = int((spread > 60).sum())
    return dict(md5=md5, size=(w, h),
                top_edge=float(row_edge[top].max()),
                bot_edge=float(row_edge[bot].max()),
                top_spread=float(spread[top].max()),
                bot_spread=float(spread[bot].max()),
                top_gray=(float(gray[top].min()), float(gray[top].max())),
                bot_gray=(float(gray[bot].min()), float(gray[bot].max())),
                content=(c0, c1, 100 * c0 / h, 100 * c1 / h),
                n_sat=n_sat)

paths = sys.argv[1:]
if not paths:
    paths = sorted(glob.glob("/mnt/inbox/imagegen-ftw/*.png"))
for p in paths:
    try:
        r = qa(p)
    except Exception as e:
        print(f"{p}\n  ERROR {e}\n")
        continue
    c0, c1, p0, p1 = r["content"]
    print(f"{p}")
    print(f"  md5={r['md5']} size={r['size'][0]}x{r['size'][1]}")
    print(f"  TOP20 edge={r['top_edge']:.3f} spread={r['top_spread']:.1f} gray={r['top_gray'][0]:.0f}-{r['top_gray'][1]:.0f}")
    print(f"  BOT30 edge={r['bot_edge']:.3f} spread={r['bot_spread']:.1f} gray={r['bot_gray'][0]:.0f}-{r['bot_gray'][1]:.0f}")
    print(f"  content rows {c0}..{c1} = {p0:.1f}%..{p1:.1f}%  | top_margin={p0:.1f}% bot_margin={100-p1:.1f}%")
    print(f"  strong-chroma pixels in frame = {r['n_sat']}")
    print()
