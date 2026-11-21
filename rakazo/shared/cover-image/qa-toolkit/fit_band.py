#!/usr/bin/env python3
"""บังคับเลย์เอาต์ v1.2 โดยไม่ต้องยิง ComfyUI (pure PIL, ไม่กิน GPU)
ขั้นตอน: หาแถบเนื้อหาจริง (content band) → ย่อภาพทั้งใบให้เนื้อหาพอดีในแถบ 20%-70%
→ เติมบน 20% ด้วยเทาอ่อน (เฉดไล่จากขอบบนฉาก) → เติมล่าง 30% ด้วยพื้น glossy สะอาด
ใช้: uv run --with pillow --with numpy python3 fit_band.py <in.png> <out.png>
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
w, h = im.size
a = np.asarray(im).astype(np.float64)
gray = a.mean(axis=2)

d_x = np.abs(np.diff(gray, axis=1)).max(axis=1)
d_y = np.abs(np.diff(gray, axis=0)).max(axis=1)
d_y = np.append(d_y, d_y[-1])
row_edge = np.maximum(d_x, d_y)

THR = 8.0
idx = np.where(row_edge > THR)[0]
c0, c1 = int(idx.min()), int(idx.max())
print(f"content rows {c0}..{c1} ({100*c0/h:.1f}%..{100*c1/h:.1f}%)")

BAND_TOP, BAND_BOT = 0.20, 0.70
band_px = int(h * (BAND_BOT - BAND_TOP))
content_px = c1 - c0 + 1
scale = min(1.0, band_px / content_px)
new_w = int(round(w * scale))
new_h = int(round(content_px * scale))
print(f"scale={scale:.4f}  new content {new_w}x{new_h}")

crop = im.crop((0, c0, w, c1 + 1)).resize((new_w, new_h), Image.LANCZOS)
carr = np.asarray(crop).astype(np.float64)

canvas = Image.new("RGB", (w, h))

# ---- บน 20%: เทาอ่อนไล่เฉดจากขอบบนฉาก ----
top_px = int(h * BAND_TOP)
bg_top = float(np.median(carr[0].mean(axis=1)))
bg_bot = float(np.median(carr[-1].mean(axis=1)))
grad = np.linspace(bg_top, bg_bot, top_px)
top_arr = np.repeat(grad[:, None, None], 3, axis=2)          # (top_px,1,3)
top_arr = np.repeat(top_arr, w, axis=1)                      # (top_px,w,3)
top_img = Image.fromarray(np.clip(top_arr, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
canvas.paste(top_img, (0, 0))

# ---- เนื้อหา กลาง ----
cx = (w - new_w) // 2
canvas.paste(crop, (cx, top_px))

# ---- ล่าง 30%: พื้น glossy สะอาด ----
bot_px = h - top_px - new_h
b_top = float(np.median(carr[-1].mean(axis=1)))
b_bot = b_top * 0.92
if bot_px > 0:
    g = np.linspace(b_top, b_bot, bot_px)
    floor = np.repeat(g[:, None, None], 3, axis=2)
    floor = np.repeat(floor, w, axis=1)
    fl = Image.fromarray(np.clip(floor, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
    canvas.paste(fl, (0, top_px + new_h))

canvas.save(dst, "PNG")
print(f"saved {dst} {canvas.size}")

# ---- ตรวจผล ----
b = np.asarray(canvas).astype(np.float64)
g2 = b.mean(axis=2)
dx2 = np.abs(np.diff(g2, axis=1)).max(axis=1)
dy2 = np.abs(np.diff(g2, axis=0)).max(axis=1)
dy2 = np.append(dy2, dy2[-1])
re = np.maximum(dx2, dy2)
print(f"QA top20  max_edge={re[:int(h*0.2)].max():.4f}")
print(f"QA bot30  max_edge={re[int(h*0.7):].max():.4f}")
i2 = np.where(re > THR)[0]
print(f"QA content rows {i2.min()}..{i2.max()} = {100*i2.min()/h:.1f}%..{100*i2.max()/h:.1f}%")
