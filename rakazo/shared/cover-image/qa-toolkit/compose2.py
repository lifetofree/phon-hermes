#!/usr/bin/env python3
"""compose2 — build the final 1:1 cover from a rendered scene.

  * scene stays inside the 20%-70% band (top 20% empty gray, bottom 30% empty floor)
  * coloured reflections are faded out above the floor line
  * everything below the floor line is replaced by a clean glossy-floor gradient
    (no objects, no shadows, no reflections)

usage: python3 compose2.py <src_1024.png> <out_2048.png> [floor_frac] [fade_start_frac]
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

src, out = sys.argv[1], sys.argv[2]
floor_frac = float(sys.argv[3]) if len(sys.argv) > 3 else 0.70
fade_start = float(sys.argv[4]) if len(sys.argv) > 4 else 0.625

im = Image.open(src).convert("RGB")
if im.size != (2048, 2048):
    im = im.resize((2048, 2048), Image.LANCZOS)
a = np.asarray(im).astype(np.float64)
H, W, _ = a.shape

B = int(H * floor_frac)        # floor line (top of the reserved bottom 30%)
F = int(H * fade_start)        # where reflection fading begins

sat = a.max(axis=2) - a.min(axis=2)
med_all = np.median(a, axis=1)                     # (H,3) robust row colour
med = med_all[F:]                                  # floor rows

# ---- 1) fade coloured reflections between F and B -------------------------------
seg = a[F:B]
sat_seg = sat[F:B]
colored = sat_seg > 32
n = B - F
t = np.linspace(0.0, 1.0, n)[:, None, None]
alpha = np.clip(1.0 - t, 0.0, 1.0)                  # 1 at F -> 0 at B
med_seg = med_all[F:B][:, None, :]
seg = seg * alpha + med_seg * (1 - alpha)
seg[~colored] = a[F:B][~colored]                   # keep unsaturated pixels (objects, shadows)
a[F:B] = seg

# ---- 2) synthetic clean floor from B downwards ----------------------------------
rows = a[B:, :, :]
med_b = np.median(rows, axis=1)                     # (n,3)
k = 25
pad = np.pad(med_b, ((k, k), (0, 0)), mode="edge")
med_s = np.stack([np.convolve(pad[:, c], np.ones(2 * k + 1) / (2 * k + 1), mode="valid") for c in range(3)], axis=1)

left = rows[:, :70, :].mean(axis=1)
right = rows[:, -70:, :].mean(axis=1)
xf = W * 0.30
ramp = np.ones(W)
for i in range(W):
    if i < xf:
        ramp[i] = (left[0, 0] / med_s[0, 0]) * (1 - i / xf) + (i / xf)
    elif i > W - xf:
        t2 = (W - i) / xf
        ramp[i] = (right[0, 2] / med_s[0, 2]) * (1 - t2) + t2
floor = np.clip(med_s[:, None, :] * ramp[None, :, None], 0, 255)

ys = np.arange(floor.shape[0], dtype=np.float64) / max(1, floor.shape[0] - 1)
floor = floor * (1.0 - 0.05 * ys)[:, None, None]     # gentle depth falloff

# ---- 3) seam blend (last 24 rows above the floor line) --------------------------
seam = 24
for i in range(seam):
    y = B - seam + i
    al = (i + 1) / float(seam)
    al = al * al * (3 - 2 * al)
    a[y] = a[y] * (1 - al) + floor[0] * al
a[B:] = floor

out_im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGB").filter(ImageFilter.SMOOTH)
out_im.save(out)
print("saved %s %s  floor_line=%.1f%%  fade_start=%.1f%%" % (out, out_im.size, 100 * B / H, 100 * F / H))
