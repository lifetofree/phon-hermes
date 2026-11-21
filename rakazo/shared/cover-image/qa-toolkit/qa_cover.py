#!/usr/bin/env python3
"""QA cover image 1:1 ตาม character sheet v1.2 (DK)
วัด 4 ข้อ: (ก) หมวก/สี (ต้องดูด้วยตา) (ข) ล่าง 30% ว่างจริง (ค) บน 20% ว่างจริง (ง) ไม่มีตัวอักษร
ใช้: uv run --with pillow --with numpy python3 qa_cover.py <file.png> [label]
"""
import sys, hashlib
from PIL import Image
import numpy as np

path = sys.argv[1]
label = sys.argv[2] if len(sys.argv) > 2 else path

im = Image.open(path)
w, h = im.size
rgb = im.convert("RGB")
a = np.asarray(rgb).astype(np.float64)
md5 = hashlib.md5(open(path, "rb").read()).hexdigest()

print(f"== {label} ==")
print(f"path : {path}")
print(f"md5  : {md5}")
print(f"size : {w}x{h}  mode={im.mode}")

gray = a.mean(axis=2)
d_x = np.abs(np.diff(gray, axis=1)).max(axis=1) if w > 1 else np.zeros(h)   # len h
d_y = np.abs(np.diff(gray, axis=0)).max(axis=1) if h > 1 else np.zeros(h)   # len h-1
d_y = np.append(d_y, d_y[-1] if len(d_y) else 0.0)
row_edge = np.maximum(d_x, d_y)

def band(y0, y1, name):
    sl = slice(y0, y1)
    g = gray[sl]
    if g.shape[0] > 3:
        idx = np.arange(g.shape[0], dtype=np.float64)
        A = np.vstack([idx, np.ones_like(idx)]).T
        coef, *_ = np.linalg.lstsq(A, g, rcond=None)
        resid = g - A @ coef
    else:
        resid = g - g.mean(axis=1, keepdims=True)
    sat = (a[sl].max(axis=2) - a[sl].min(axis=2)).max()
    print(f"{name}: rows {y0}-{y1} ({100*y0/h:.1f}%-{100*y1/h:.1f}%)")
    print(f"   max_edge_in_band      = {row_edge[sl].max():.4f}")
    print(f"   row_detrended_resid   = {np.abs(resid).max():.3f}")
    print(f"   max_channel_spread    = {sat:.1f}")
    print(f"   gray_min_max_mean     = {g.min():.0f}/{g.max():.0f}/{g.mean():.1f}")

print("TOP20_CHECK")
band(0, int(h * 0.20), "TOP20")
print("BOT30_CHECK")
band(int(h * 0.70), h, "BOT30")
print("MID_CHECK")
band(int(h * 0.20), int(h * 0.70), "MID")

thr = 0.05
idx = np.where(row_edge > thr)[0]
if len(idx):
    print(f"CONTENT_ROWS edge>{thr}: {idx.min()}..{idx.max()} = {100*idx.min()/h:.1f}%..{100*idx.max()/h:.1f}%")
    print(f"TOP_MARGIN {100*idx.min()/h:.1f}% (need >=20)")
    print(f"BOTTOM_MARGIN {100*(h-1-idx.max())/h:.1f}% (need >=30)")
else:
    print("CONTENT_ROWS none")

print("PROFILE")
for y in range(0, h, max(1, h // 32)):
    print(f"PROF y={y} pct={100*y/h:.1f} edge={row_edge[y]:.3f} gray={gray[y].mean():.0f}")
