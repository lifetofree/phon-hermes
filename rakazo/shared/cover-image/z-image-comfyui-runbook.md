# Runbook: ComfyUI (Z-Image Turbo) บน Mac ของเจ้าของ — สำหรับงานภาพ adduckivity

เขียนโดย Image Gen · 21 พ.ย. 2026 · ตรวจกับ API จริงทุกข้อ

## 1. จุดเชื่อมต่อ
| ข้อ | ค่า |
|---|---|
| เครื่อง | Mac ของเจ้าของ (บ้าน) เข้าถึงผ่าน LAN |
| พอร์ตของ Image Gen | **8189** (`http://100.107.249.87:8189`) |
| พอร์ตของ Design Keeper | 8188 (ห้ามชนพอร์ตกัน — GPU เครื่องเดียวกัน) |
| คีย์/โทเคน | **ไม่ต้องใช้** (ไม่มี auth layer) |
| ComfyUI version | 0.46.2 · required_frontend 1.59.6 |
| RAM เครื่อง | 38 GB (ต้องเหลือ ≥ 4 GB ตอน gen) |

## 2. โมเดลที่ติดตั้ง (มีแค่ชุดเดียว)
- UNet: `z_image_turbo_bf16.safetensors` (Z-Image Turbo)
- CLIP: `qwen_3_4b_fp8_mixed.safetensors` (type `lumina2`)
- VAE: `ae.safetensors`
- sampler: `euler` · scheduler `simple` · steps 8 · cfg 1.0 (ค่าที่ได้ผลจริง)

## 3. Template
`/mnt/hermes-agent/rakazo/shared/comfyui/z-image-template-imagegen.json` (API graph)
ห้ามแก้ config/โมเดล/workflow ของ ComfyUI — แก้แค่ node `3` (prompt), `4` (negative), `6` (w/h), `7` (seed)

## 4. ขั้นตอนยิงงาน (ตัวอย่างคำสั่ง API)
```bash
# 1) POST graph -> ได้ prompt_id
curl -s -X POST http://100.107.249.87:8189/prompt \
  -H 'Content-Type: application/json' \
  -d '{"client_id":"imagegen","prompt": <graph json>}'
# → {"prompt_id": "...."}

# 2) poll สถานะ (ทุก 10 วิ) — websocket ไม่มี progress event ราย step
curl -s http://100.107.249.87:8189/history/<prompt_id>
# → status.status_str = success และ outputs["9"].images[0].filename

# 3) ดึงไฟล์ดิบ
curl -s -o out.png \
  'http://100.107.249.87:8189/view?filename=imagegen/img_000NN_.png&subfolder=imagegen&type=output'

# 4) ยกเป็น master 2048 (Lanczos)
convert out.png -resize 2048x2048 -filter Lanczos -strip -define png:compression-level=9 master.png
```

สคริปต์ที่ใช้จริง: `/home/rakazo/scripts/gen_duck_pipeline_v4.py` (gen + upscale),
`/home/rakazo/scripts/dk_rebuild.py` (canvas surgery + single-resample master),
`/home/rakazo/scripts/verify_final.py` (ตรวจ safe-zone + วัดทิศหมวก),
`/home/rakazo/scripts/scene_audit.py` (นับลูกบาศก์/ห่วงตรวจ)

## 5. กฎที่ต้องจำ (เจ็ยว่าครั้งนี้)
- **ห้าม gen 2048 ตรง** — ค้าง ~30 นาที และบล็อกคิวทั้งเครื่อง → gen 1024 แล้ว upscale Lanczos
- **อย่าเขียนทับ raw ด้วยไฟล์ที่ย่อจาก master** — เคยพลาดแล้ว: pipeline เดิมเขียน
  `RAW = MASTER(2048) → ย่อกลับ 1024` ทำให้ master ที่ส่งมอบถูก resample ซ้ำ 3 รอบ
  (ดู §6) → ให้เก็บ raw ดิบจาก ComfyUI แยกไว้เสมอ แล้วค่อย upscale ครั้งเดียว
- **หมวกกลับหลัง**: Z-Image ไม่ฟัง "worn backwards" เฉย ๆ ต้องบรรยายหลักฐานที่มองเห็นได้
  > *"a red baseball cap worn backwards, so the curved **peak** of the cap points away from the bill and sticks out behind the duck's head, while the **cap opening** and the small adjustable strap with its buckle are visible at the front of the forehead"*
  + negative: `brim above the bill, peak over the eyes, front-facing cap, hat facing forward`
  ผลจริง: 5 รอบ → 1 รอบถูก (seed 426614869) — รอบที่ใช้คำว่า "brim"/"turned the wrong way round" ได้หมวกหันหน้าเกือบทุกครั้ง
- **safe zone**: Z-Image วางฐานฉากที่ 75–80% ของเฟรมเสมอ ไม่ว่าจะสั่งเลย์เอาต์ยังไง
  → ต้องทำ canvas surgery เอง (ล้างเงา/ประกายด้วย quadratic fit → เลื่อนฉากขึ้น ~113 px → ยืดแถบพื้น)
- **ห้ามแทรกงานอื่นเข้าคิว** และ **ห้ามยิงพร้อมกันกับ 8188**

## 6. บันทึก resample ซ้ำ (เจอเอง 21 พ.ย. 16:00)
pipeline เดิม:
```
raw 1024 (ComfyUI) ──Lanczos──▶ 2048 ──Lanczos──▶ 1024 (ถูกเขียนทับ raw) ──surgery──▶ 1024 ──Lanczos──▶ 2048 (ส่งมอบ)
```
= 3 รอบ resample วัดความคมชัดในแถบ active ที่ 2048: mean |dx| 0.428
แก้แล้ว: เก็บ raw ดิบแยก (`img_00004_.png` md5 2633f29070d202a015dd6a0f235c96f5) → surgery → upscale ครั้งเดียว
= mean |dx| 0.450 (+5%) และไฟล์เล็กลง (1.34 MB vs 1.30 MB เดิมเล็กน้อยแต่คมกว่า)

## 7. วิธีวัดทิศหมวก (แทนการเดา/เทียบกับแกนคอนโซล)
วัด centroid ของเม็ดสีแดง (หมวก) กับสีส้ม (ปาก) จากพิกเซลจริง:
- ไฟล์ส่งมอบ: หมวก centroid x = 717 (ขอบขวาสุด x 800) · ปาก centroid x = 647 (ขอบขวาสุด x 685)
- → มวลหมวกอยู่**ขวาของ**ปาก = ปีกหมวกชี้ไปทางหลัง = **สวมกลับหลังถูกต้อง**
- proxy ที่เทียบกับ "แกนคอนโซล" จะให้ผลผิด — ให้เทียบกับ **ปาก** เท่านั้น
