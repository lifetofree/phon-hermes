#!/usr/bin/env python3
"""นับกล่องเขียว (ก้อนเรืองแสง) แบบ component + นับห่วงเหลือง (วงที่มีรูชัด) จากภาพ
ใช้วิเคราะห์เชิงพิกเซล ไม่ตีความภาพ
"""
import sys, glob
import numpy as np
from PIL import Image
from scipy import ndimage


def analyse(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    mx = a.max(axis=2); mn = a.min(axis=2)
    h, w = R.shape

    green = (G > 100) & (G - R > 30) & (G - B > 30)
    lab, n = ndimage.label(green)
    comps = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        if len(xs) < 120:
            continue
        comps.append((len(xs), int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())))
    comps.sort(reverse=True)

    # ห่วงเหลือง: โทนเหลือง/ทอง (R,G สูง B ต่ำ) และมีรูข้างใน (สีเข้มกว่า) → ลดลูกหลอม
    amber = (R > 120) & (G > 80) & (R - B > 55) & (G - B > 25) & (np.abs(R - G) < 95)
    lab2, n2 = ndimage.label(amber)
    rings = []
    for i in range(1, n2 + 1):
        ys, xs = np.where(lab2 == i)
        if len(xs) < 100:
            continue
        bw = xs.max() - xs.min() + 1
        bh = ys.max() - ys.min() + 1
        if bw < 8 or bh < 8:
            continue
        fill = len(xs) / float(bw * bh)
        hole = (~amber[ys.min():ys.max() + 1, xs.min():xs.max() + 1]).mean()
        rings.append(dict(area=len(xs), bw=int(bw), bh=int(bh), fill=round(fill, 2),
                          hole=round(hole, 2), x0=int(xs.min()), x1=int(xs.max()),
                          y0=int(ys.min()), y1=int(ys.max())))
    rings.sort(key=lambda r: -r["area"])

    print(f"--- {path}  {w}x{h}")
    print(f"    GREEN components: {len(comps)}  (areas/bbox)")
    for c in comps[:8]:
        print(f"       area={c[0]:6d} x {c[1]}-{c[2]} y {c[3]}-{c[4]}")
    print(f"    AMBER components (candidate rings): {len(rings)}")
    for r in rings[:8]:
        print(f"       area={r['area']:6d} bbox={r['bw']}x{r['bh']} fill={r['fill']} hole={r['hole']} "
              f"x {r['x0']}-{r['x1']} y {r['y0']}-{r['y1']}")
    print()


for p in (sys.argv[1:] or sorted(glob.glob("/mnt/inbox/imagegen-ftw/*.png"))):
    try:
        analyse(p)
    except Exception as e:
        print(f"{p} ERROR {e}\n")
