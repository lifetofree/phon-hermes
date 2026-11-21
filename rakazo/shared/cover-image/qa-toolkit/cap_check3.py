#!/usr/bin/env python3
"""ทดสอบว่า proxy "หมวกกลับหลัง" แยกได้จริงไหม โดยดูช่องว่างหน้าผาก (สีขาว) ระหว่างขอบล่างหมวกกับแว่น

v2 (21 พ.ย. 2026 18:50) — แก้การหาแว่น: เดิมใช้ dark component ก้อนเดียวที่ ≥300 px
   ทำให้ master 70095fbc (แว่นเป็น 2 เลนส์แยกกัน) รายงานว่า "glasses not found"
   → ใช้ union ของทุก dark component ในบริเวณหน้า (≥120 px) แทน

หมวกกลับหลัง → หน้าผากเปิด + บิลยื่นไปข้างหลัง
หมวกหันหน้า  → บิล/ท่อนหน้าหมวกกดลงมาใกล้แว่น/บังแว่น
ใช้: uv run --with pillow --with numpy --with scipy python3 cap_check3.py <file...>
"""
import sys, glob
import numpy as np
from PIL import Image
from scipy import ndimage


def analyse(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    mx = a.max(axis=2)
    mn = a.min(axis=2)

    red = (R > 110) & (R - G > 140) & (R - B > 140)   # แดงเข้มเฉพาะหมวก (ไม่จับปากส้ม)
    dark = (mx < 110) & (mx > 18) & ((mx - mn) < 60)
    light = (mn > 150) & ((mx - mn) < 40)   # ขาว/ผิวสว่าง

    lab, n = ndimage.label(red)
    if n == 0:
        return None
    sizes = ndimage.sum(red, lab, range(1, n + 1))
    k = int(np.argmax(sizes)) + 1
    cap = (lab == k)
    ys, xs = np.where(cap)
    cx0, cx1, cy0, cy1 = int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())

    # แว่น = union ของ dark component ทุกก้อนในบริเวณหน้า (ไม่ต้องเป็นก้อนเดียว)
    gl, gn = ndimage.label(dark)
    gm = np.zeros_like(dark)
    picks = []
    for i in range(1, gn + 1):
        gy, gx = np.where(gl == i)
        if len(gx) < 120:
            continue
        if gy.min() < cy0 - 40 or gy.max() > cy1 + 260:
            continue
        if gx.min() > cx1 + 250 or gx.max() < cx0 - 250:
            continue
        gm |= (gl == i)
        picks.append((int(len(gx)), i, int(gx.min()), int(gx.max()), int(gy.min()), int(gy.max())))
    if not picks:
        return dict(path=path, cap=(cx0, cx1, cy0, cy1), glasses=None)

    gy, gx = np.where(gm)
    gx0, gx1, gy0, gy1 = int(gx.min()), int(gx.max()), int(gy.min()), int(gy.max())

    # ช่องขาว/ผิวหน้าระหว่างขอบล่างของหมวก (ในคอลัมน์ของแว่น) กับขอบบนของแว่น
    col_lo = max(cx0, gx0)
    col_hi = min(cx1, gx1)
    gap_white = 0
    gap_cols = 0
    if col_hi > col_lo:
        for c in range(col_lo, col_hi + 1):
            cap_rows = np.where(cap[:, c])[0]
            if len(cap_rows) == 0:
                continue
            cap_bottom = int(cap_rows.max())
            gl_rows = np.where(gm[:, c])[0]
            if len(gl_rows) == 0:
                continue
            gl_top = int(gl_rows.min())
            if gl_top > cap_bottom:
                gap_cols += 1
                gap_white += int(light[cap_bottom + 1:gl_top, c].sum())
    return dict(path=path, cap=(cx0, cx1, cy0, cy1), glasses=(gx0, gx1, gy0, gy1),
                glasses_parts=picks, gap_white=gap_white, gap_cols=gap_cols,
                glasses_over_cap=int((gm & cap).sum()))


files = (sys.argv[1:] or
         sorted(glob.glob("/mnt/inbox/imagegen-ftw/*.png")) +
         sorted(glob.glob("/home/rakazo/work/cf*/seed*_1024.png")))
for p in files:
    try:
        r = analyse(p)
    except Exception as e:
        print(f"{p} ERROR {e}")
        continue
    if not r:
        continue
    print(p)
    print(f"   cap {r['cap']}")
    if r.get("glasses"):
        print(f"   glasses {r['glasses']} parts={r['glasses_parts']}  "
              f"white_gap_px={r['gap_white']} over {r['gap_cols']} cols  "
              f"overlap_cap={r['glasses_over_cap']}")
    else:
        print("   glasses not found")
    print()
