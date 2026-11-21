#!/usr/bin/env python3
"""วัดเรขาคณิตของหมวก/ปาก/แว่น เพื่อดูว่า proxy แยก "หมวกกลับหลัง" ออกจาก "หมวกหันหน้า" ได้จริงไหม

v2 (21 พ.ย. 2026 18:50) — แก้ 2 จุดที่ทำให้ตัวเลขหลอก:
  1) mask แดงแบบหลวม (R-G>45) จับ "ปากส้ม" (221,138,34 → R-G=83) เข้าไปด้วย
     → เพิ่ม mask แดงเข้ม (R-G>140) และแยกตัวเลขให้ชัดว่าตัวไหนมาจากปาก
  2) เพิ่ม "exact-mask facts" 4 ข้อ ที่เป็นหลักฐานตัดสินได้จริง (ดูด้านล่าง)

เกณฑ์: ถ้า proxy ให้ค่าเดียวกันทั้งเฟรมที่หมวกกลับหลังและเฟรมที่หมวกคลุมหน้า
       → proxy ใช้ตัดสินไม่ได้ ต้องให้คนดูด้วยตา
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

    red_loose = (R > 110) & (R - G > 45) & (R - B > 45)      # จับปากส้มด้วย (ระวัง!)
    red_strict = (R > 110) & (R - G > 140) & (R - B > 140)   # แดงจริงของหมวกเท่านั้น
    orange = (R > 160) & (G > 85) & (G < 195) & (R - B > 75) & (G - B > 18)
    dark = (mx < 110) & (mx > 18) & ((mx - mn) < 60)

    def biggest(mask, minarea=150):
        lab, n = ndimage.label(mask)
        if n == 0:
            return None
        sizes = ndimage.sum(mask, lab, range(1, n + 1))
        k = int(np.argmax(sizes)) + 1
        ys, xs = np.where(lab == k)
        if len(xs) < minarea:
            return None
        return dict(area=int(len(xs)), x0=int(xs.min()), x1=int(xs.max()),
                    y0=int(ys.min()), y1=int(ys.max()),
                    cx=float(xs.mean()), cy=float(ys.mean()), mask=(lab == k))

    bill = biggest(orange, 200)          # ปากส้ม
    cap_strict = biggest(red_strict, 400)  # หมวก (แดงเข้ม)
    cap_loose = biggest(red_loose, 800)    # หมวก+เงาแดง (ปนปากได้)
    darkc = biggest(dark, 150)
    if not bill or not cap_strict:
        return None

    # ---- proxy เดิม (ยังใช้ได้แค่ดูรูปทรง ไม่ใช้ตัดสินทิศ) ----
    d_cx = cap_loose["cx"] - bill["cx"] if cap_loose else cap_strict["cx"] - bill["cx"]
    bill_side = "LEFT" if bill["cx"] < (cap_loose or cap_strict)["cx"] else "RIGHT"
    d_cy = bill["cy"] - cap_strict["cy"]

    # ---- exact-mask facts (หลักฐานที่ตัดสินได้จริง) ----
    bx0, bx1, by0, by1 = bill["x0"], bill["x1"], bill["y0"], bill["y1"]
    col = np.arange(a.shape[1])
    left_of_beak = red_strict[:, :bx0]
    over_beak_rows = red_strict[by0:by1 + 1, bx0:bx1 + 1]
    right_of_beak = red_strict[:, bx1 + 1:]
    facts = dict(
        red_left_of_beak=int(left_of_beak.sum()),
        red_over_beak_rows=int(over_beak_rows.sum()),
        red_right_of_beak=int(right_of_beak.sum()),
        red_over_glasses=int(red_strict[darkc["y0"]:darkc["y1"] + 1,
                                        darkc["x0"]:darkc["x1"] + 1].sum()) if darkc else -1,
        cap_strict_bbox=(cap_strict["x0"], cap_strict["x1"], cap_strict["y0"], cap_strict["y1"]),
        beak_bbox=(bx0, bx1, by0, by1),
        glasses_bbox=(darkc["x0"], darkc["x1"], darkc["y0"], darkc["y1"]) if darkc else None,
    )

    # ---- ช่องขาวบนหมวก: สเปกคูลาร์ไฮไลต์ หรือ ช่องเปิดหน้าหมวก? ----
    light = (mn > 225) & ((mx - mn) < 14)
    sub = light[cap_strict["y0"]:cap_strict["y1"] + 1, cap_strict["x0"]:cap_strict["x1"] + 1]
    white_info = None
    if sub.any():
        lab, n = ndimage.label(sub)
        sizes = ndimage.sum(sub, lab, range(1, n + 1))
        k = int(np.argmax(sizes)) + 1
        wm = (lab == k)
        wy, wx = np.where(wm)
        if len(wx) >= 40:
            wx0, wx1 = int(wx.min()), int(wx.max())
            wy0, wy1 = int(wy.min()), int(wy.max())
            gl = cap_strict["y0"] + wy0
            gr = cap_strict["y0"] + wy1
            cl = cap_strict["x0"] + wx0
            cr = cap_strict["x0"] + wx1
            surround = {}
            for name, sl in (("above", (slice(gl - 5, gl), slice(cl, cr + 1))),
                             ("below", (slice(gr + 1, gr + 6), slice(cl, cr + 1))),
                             ("left", (slice(gl, gr + 1), slice(cl - 5, cl))),
                             ("right", (slice(gl, gr + 1), slice(cr + 1, cr + 6)))):
                band = red_strict[sl]
                surround[name] = round(float(band.mean()) * 100, 1)
            rows = []
            for yy in range(gl, gr + 1, max(1, (gr - gl) // 5)):
                w = np.where(light[yy, cl:cr + 1])[0]
                rows.append((yy, int(len(w))))
            white_info = dict(bbox=(cl, cr, gl, gr), px=int(wm.sum()),
                              mean_rgb=[round(float(v), 1) for v in a[gl:gr + 1, cl:cr + 1].reshape(-1, 3).mean(axis=0)],
                              red_cover_pct=surround, width_by_row=rows)
    return dict(bill=bill, cap_strict=cap_strict, cap_loose=cap_loose, dark=darkc,
                d_cx=d_cx, bill_side=bill_side, d_cy=d_cy, facts=facts, white=white_info)


rows = []
files = (sys.argv[1:] or
         sorted(glob.glob("/mnt/inbox/imagegen-ftw/*.png")) +
         sorted(glob.glob("/home/rakazo/work/cf*/seed*_1024.png")))
for p in files:
    try:
        m = analyse(p)
    except Exception as e:
        print(f"{p} ERROR {e}")
        continue
    if not m:
        print(f"{p}: no cap/bill")
        continue
    rows.append((p, m))
    f = m["facts"]
    print(p)
    print(f"   beak {f['beak_bbox']} | cap(strict) {f['cap_strict_bbox']} | glasses {f['glasses_bbox']}")
    print(f"   proxy: d_cx={m['d_cx']:+.0f}px bill_side={m['bill_side']} d_cy={m['d_cy']:+.0f}px "
          f"(proxy นี้แยกทิศหมวกไม่ได้ — ดู README ข้อจำกัด 1)")
    print(f"   EXACT: red_left_of_beak={f['red_left_of_beak']}  red_over_beak_rows={f['red_over_beak_rows']}  "
          f"red_over_glasses={f['red_over_glasses']}  red_right_of_beak={f['red_right_of_beak']}")
    if m["white"]:
        w = m["white"]
        print(f"   white patch {w['bbox']} px={w['px']} mean_rgb={w['mean_rgb']} "
              f"red_cover%={w['red_cover_pct']}")
        print(f"      width_by_row={w['width_by_row']}")

if rows:
    print("\n== spread ==")
    dcx = np.array([m["d_cx"] for _, m in rows])
    dcy = np.array([m["d_cy"] for _, m in rows])
    lft = np.array([m["facts"]["red_left_of_beak"] for _, m in rows])
    ovb = np.array([m["facts"]["red_over_beak_rows"] for _, m in rows])
    print(f"d_cx    : min {dcx.min():+.0f} max {dcx.max():+.0f} std {dcx.std():.1f}")
    print(f"d_cy    : min {dcy.min():+.0f} max {dcy.max():+.0f}")
    print(f"red_left_of_beak : min {lft.min()} max {lft.max()}")
    print(f"red_over_beak_rows: min {ovb.min()} max {ovb.max()}")
