#!/usr/bin/env python3
"""วัดเรขาคณิตของหมวก/ปาก/แว่น เพื่อดูว่า proxy แยก "หมวกกลับหลัง" ออกจาก "หมวกหันหน้า" ได้จริงไหม
เกณฑ์: ถ้า proxy ให้ค่าเดียวกันทั้งเฟรมที่หมวกกลับหลังและเฟรมที่หมวกคลุมหน้า
       → proxy ใช้ตัดสินไม่ได้ ต้องให้คนดูด้วยตา
"""
import sys, glob
import numpy as np
from PIL import Image
from scipy import ndimage


def metrics(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    mx = a.max(axis=2)
    red = (R > 110) & (R - G > 45) & (R - B > 45)
    orange = (R > 160) & (G > 85) & (G < 195) & (R - B > 75) & (G - B > 18)
    dark = (mx < 95) & (mx > 22)

    def biggest(mask, minarea=150):
        lab, n = ndimage.label(mask)
        if n == 0:
            return None
        sizes = ndimage.sum(mask, lab, range(1, n + 1))
        k = int(np.argmax(sizes)) + 1
        ys, xs = np.where(lab == k)
        if len(xs) < minarea:
            return None
        return dict(area=len(xs), x0=int(xs.min()), x1=int(xs.max()),
                    y0=int(ys.min()), y1=int(ys.max()),
                    cx=float(xs.mean()), cy=float(ys.mean()), mask=(lab == k))

    cap = biggest(red, 800)
    bill = biggest(orange, 200)
    darkc = biggest(dark, 400)
    if not cap or not bill:
        return None

    # ระยะแนวนอนศูนย์กลางหมวก - ปาก (บวก = หมวกอยู่ขวาของปาก)
    d_cx = cap["cx"] - bill["cx"]
    # ปากอยู่ซ้าย/ขวาของหมวก
    bill_side = "LEFT" if bill["cx"] < cap["cx"] else "RIGHT"
    # สัดส่วนมวลแดงที่ทับกรอบ x ของปาก (หมวกหันหน้า → ทับหน้ามาก)
    band = (np.arange(a.shape[1]) >= bill["x0"] - 15) & (np.arange(a.shape[1]) <= bill["x1"] + 15)
    overlap_ratio = red[:, band].sum() / max(1.0, cap["area"])
    # ระยะแนวตั้ง: หมวกอยู่เหนือปากกี่ px (บวก = หมวกสูงกว่า = ปกติ)
    d_cy = bill["cy"] - cap["cy"]
    return dict(cap=cap, bill=bill, d_cx=d_cx, bill_side=bill_side,
                overlap=overlap_ratio, d_cy=d_cy,
                dark_box=(darkc["x0"], darkc["x1"], darkc["y0"], darkc["y1"]) if darkc else None)


rows = []
files = (sys.argv[1:] or
         sorted(glob.glob("/mnt/inbox/imagegen-ftw/*.png")) +
         sorted(glob.glob("/home/rakazo/work/cf*/seed*_1024.png")))
for p in files:
    try:
        m = metrics(p)
    except Exception as e:
        print(f"{p} ERROR {e}")
        continue
    if not m:
        print(f"{p}: no cap/bill")
        continue
    rows.append((p, m))
    print(f"{p}")
    print(f"   bill {m['bill']['x0']}-{m['bill']['x1']} (cx {m['bill']['cx']:.0f}) | "
          f"cap {m['cap']['x0']}-{m['cap']['x1']} (cx {m['cap']['cx']:.0f}) | "
          f"bill_side={m['bill_side']}")
    print(f"   d_cx(cap-bill) = {m['d_cx']:+.0f}px | red_over_bill_x = {m['overlap']*100:.0f}% | "
          f"bill_below_cap = {m['d_cy']:+.0f}px | darkbox={m['dark_box']}")

if rows:
    print("\n== spread ==")
    dcx = np.array([m["d_cx"] for _, m in rows])
    ov = np.array([m["overlap"] for _, m in rows])
    dcy = np.array([m["d_cy"] for _, m in rows])
    print(f"d_cx    : min {dcx.min():+.0f} max {dcx.max():+.0f} std {dcx.std():.1f}")
    print(f"overlap : min {ov.min()*100:.0f}% max {ov.max()*100:.0f}%")
    print(f"d_cy    : min {dcy.min():+.0f} max {dcy.max():+.0f}")
