# Z-Image ComfyUI Runbook — เวอร์ชัน SERVER (22 พ.ย. 2026 แก้โดย Image Gen)

> ไฟล์นี้คือ **ฉบับแก้ไขของ** `shared/cover-image/z-image-comfyui-runbook.md` (ฉบับเดิมยังเขียน endpoint/โมเดลของเครื่องเก่า ซึ่งตายถาวรแล้ว → บอทอื่นที่เปิด runbook จะยิงผิดที่)
> ผู้รับผิดชอบ commit = Chief หรือ Design Keeper (IG เขียน shared ไม่ได้ read-only)

## 0) สถานะ (22 พ.ย. 05:1x ตรวจโดย Image Gen)
| รายการ | ค่า |
|---|---|
| endpoint สำหรับบอท (ใช้ได้) | **http://172.18.0.1:8190** |
| เครื่องเก่า | 100.107.249.87:8189 / :8188 + 172.18.0.1:8188 → **ตายถาวร (http 000) อย่าตรวจอีก** |
| ComfyUI | 0.34.0 (linux, GPU server) · /system_stats 200 · /queue ว่าง |
| ความเร็ว | ~25 วิ/รูป (server) — เครื่องเก่าเคย 150–338 วิ/รูป |

## 1) โมเดลบน server (ยืนยันจาก /object_info)
- UNET: `z_image_turbo_bf16.safetensors`
- CLIP: `qwen_3_4b.safetensors` (CLIPLoader type = `lumina2`)
- VAE: `z_image_vae.safetensors`
- **ไม่มีบน server**: `qwen_3_4b_fp8_mixed.safetensors`, `ae.safetensors` (คู่นี้คือของเครื่องเก่า)
- ⚠️ ผลลัพธ์จึง**ต่างจากของเครื่องเก่าแม้ seed เดียวกัน** (CLIP/VAE คนละชุด) — reroll = ได้ภาพใหม่เสมอ ห้า QA ใหม่ทุกครั้ง

## 2) Template (API graph)
- **ใช้กับ server**: `shared/comfyui/z-image-template-server.json`
  - node `3` = positive prompt · node `4` = negative prompt · node `6` = width/height/batch · node `7` = seed/steps/cfg/sampler/scheduler/denoise
  - sampler `euler` · scheduler `simple` · steps 8 · cfg 1 · denoise 1 · 1024×1024
- ฉบับเดิม `z-image-template-imagegen.json` = ของเครื่องเก่า → **ใช้กับ server ไม่ได้**
- ก่อนยิงเสมอ: ลบ key `_readme` ออกจาก graph (ไม่งั้น ComfyUI ตอบ 500)

## 3) สายการผลิต (runbook เดิม ยังใช้ได้)
raw 1024 (จาก ComfyUI ตรง ๆ ห้ามย่อ-ขยายก่อน) → canvas surgery (fit/fit2/fit3) → upscale **Lanczos ครั้งเดียว** → master 2048
- **ห้าม resample ซ้ำ** (ย่อ 2048 แล้วขยายกลับ = ภาพเบลอ + ผิดบทเรียน 21 พ.ย.)
- `fit_band.py` ของ toolkit วางเนื้อหาที่ ~19.8% → seam หลุดเข้า top20 (TOP20 edge 127–219) → **ใช้ fit2/fit3 (margin ~21%) แทน**
- `compose2.py` ของ toolkit บังคับ resize เป็น 2048 = resample ซ้ำ → ใช้ `compose2_1k` (logic เดิม ไม่บังคับขนาด) แล้ว upscale ทีหลัง

## 4) QA (toolkit v2 = commit 35822c0 ที่ `shared/cover-image/qa-toolkit/`)
รันด้วย `uv run --with scipy --with numpy --with pillow python3 <tool>.py <file>` (ต้องมี scipy)
- `qa_summary.py` → TOP20 edge ≲ 3 · BOT30 edge ≲ 2 · แถบเนื้อหา 20–70%
- `cap_metric.py` → EXACT: red_left_of_beak / red_over_beak_rows / red_over_glasses = 0 (proxy ที่พิมพ์มาแยกทิศหมวกไม่ได้ — README ข้อจำกัด 1)
- `cap_check3.py` → white_gap + overlap_cap
- `text_check.py` → glyph-like dark components = 0
- ⚠️ **toolkit v2 ยังตรวจขอบซ้าย–ขวาแนวตั้งไม่ได้** (qa_summary ตรวจแค่แนวนอน) → แถบดำข้างผ่าน QA ได้
  → ใช้สคริปต์เสริม `check_black_cols.py` (เกณฑ์: คอลัมน์ที่พิกเซลดำ (0,0,0) ≥ 50% ของแถบเนื้อหา) — แนบมาพร้อม runbook นี้

## 5) สิ่งที่ห้ามเด็ดขาด
- ห้าม gen 2048 ตรง (ค้างนาน) · ห้ามยิงพร้อมกันกับ port ของบอทอื่น · ห้ามยิงซ้ำคิวเดิม
- ห้ามยิง /interrupt เอง (เมื่อ 21 พ.ย. มีบอท interrupt คิว → error execution_interrupted ทั้งที่ /system_stats ปกติ)
- ห้าม upload WordPress (publish = เจ้าของเท่านั้น) · ห้ามแตะงานเขียน
