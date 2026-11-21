#!/usr/bin/env python3
"""
ตรวจคอลัมน์ดำซ้าย/ขวา (แนวตั้ง) — QA แนวนอนของ toolkit ตรวจไม่ได้

usage: python3 check_black_cols.py file.png [more.png ...]
       (ต้องมี numpy + pillow: uv run --with numpy --with pillow python3 check_black_cols.py <file>)

รายงาน 2 เกณฑ์ (เพราะเคยมีตัวเลข 2 ชุดจาก 2 บอท — รวมไว้ให้ทีมใช้เครื่องมือเดียวกัน):
  A) fixed-band : แถบเนื้อหา rows 21-67% · นับพิกเซลที่ max<=8 (ดำแท้) >=50% ของแถบ
  B) auto-band  : หาแถบเนื้อหาจาก gradient อัตโนมัติ · นับพิกเซล max<30 (ดำ/มืด) >=50%
  + max_col_seam (ความต่างสูงสุดระหว่างคอลัมน์ในแถบ = ตัวบอก seam หลุด)
  + ความสว่างขอบซ้าย/ขวา 40 px เทียบกลางภาพ (ขอบเข้ม = อาการแถบดำขอบ)
"""
import hashlib
import sys

import numpy as np
from PIL import Image


def analyze(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(int)
    h, w = a.shape[:2]
    gray = a.mean(axis=2)

    # --- A) fixed band 21-67%
    top, bot = int(h * 0.21), int(h * 0.67)
    band = a[top:bot, :, :]
    fixed_frac = (band.max(axis=2) <= 8).mean(axis=0)
    fixed_cols = np.where(fixed_frac >= 0.5)[0]

    # --- B) auto band (gradient)
    d = np.abs(np.diff(gray, axis=0)).max(axis=1)
    idx = np.where(d > 8)[0]
    c0, c1 = (int(idx.min()), int(idx.max())) if len(idx) else (0, h - 1)
    autob = a[c0:c1 + 1]
    auto_dark = autob.max(axis=2) < 30
    auto_frac = auto_dark.mean(axis=0)
    auto_cols = np.where(auto_frac >= 0.5)[0]

    def groups(cols, limit=4):
        out = []
        if not len(cols):
            return out
        s = prev = int(cols[0])
        for c in cols[1:]:
            c = int(c)
            if c != prev + 1:
                out.append((s, prev))
                s = c
            prev = c
        out.append((s, prev))
        return out[:limit]

    seam = float(np.abs(np.diff(gray[c0:c1 + 1], axis=1)).max())
    lum = 0.2126 * a[:, :, 0] + 0.7152 * a[:, :, 1] + 0.0722 * a[:, :, 2]

    return {
        "size": f"{w}x{h}",
        "md5": hashlib.md5(open(path, "rb").read()).hexdigest(),
        "fixed_blackcols": int(len(fixed_cols)),
        "auto_band": f"{100*c0/h:.1f}-{100*c1/h:.1f}%",
        "auto_blackcols": int(len(auto_cols)),
        "groups": groups(auto_cols),
        "seam": round(seam, 2),
        "left40": round(float(lum[:, :40].mean()), 1),
        "right40": round(float(lum[:, -40:].mean()), 1),
        "mid": round(float(lum.mean()), 1),
    }


for p in sys.argv[1:]:
    try:
        r = analyze(p)
        print(p)
        print("   size={size} md5={md5}".format(**r))
        print("   fixed-band blackcols={fixed_blackcols}  auto-band={auto_band} auto-blackcols={auto_blackcols} groups={groups}".format(**r))
        print("   max_col_seam={seam}  left40={left40} right40={right40} mid={mid}".format(**r))
    except Exception as e:
        print("ERR %s: %s" % (p, e))
