# Z-Image Turbo (ComfyUI บน Mac ของเจ้าของ) — บทเรียนสำหรับ cover image 1:1

เขียนโดย Image Gen · 21 พ.ย. 2026 · อ้างอิงงาน cover "Second Brain → Finished Work"

## วิธีรัน
- **โหนดที่ใช้งานได้จริง = port 8189** (template: `/mnt/hermes-agent/rakazo/shared/comfyui/z-image-template-imagegen.json`) · 8188 เป็นอีกตัว/เก่า
- โมเดล: Z-Image Turbo (`z_image_turbo_bf16.safetensors`) + CLIP `qwen_3_4b_fp8_mixed` + VAE `ae` · ไม่ต้องใช้คีย์
- 1024×1024 ใช้เวลา 233–337 วิ (3.9–5.6 นาที) ต่องาน · **ห้าม gen 2048 ตรง** (ค้าง ~30 นาทีและบล็อกคิว)
- **websocket ไม่มี progress event ราย step** (มีแค่ status/executing) → ต้อง poll `GET /history/<prompt_id>` ทุก 10 วิ
- upscale master 2048 ทำด้วย ImageMagick Lanczos (PNG lossless)

## หมวกกลับหลัง (สำคัญที่สุด)
Z-Image ไม่ค่อยฟังคำว่า "worn backwards" — ต้องบรรยาย **หลักฐานภาพที่มองเห็นได้**:
> *"a red baseball cap worn backwards, so the curved **peak** of the cap points away from the bill and sticks out behind the duck's head, while the **cap opening** and the small adjustable strap with its buckle are visible at the front of the forehead"*
+ negative: `brim above the bill, peak over the eyes, front-facing cap, hat facing forward`

ผลจริง: 5 รอบ → 1 รอบถูก (v4, seed 426614869) · รอบที่ใช้คำว่า "brim"/"turned the wrong way round" ได้หมวกหันหน้าเกือบทุกครั้ง

## เลย์เอาต์ safe zone — ต้องทำ canvas surgery เอง
**Z-Image วางฐานฉากไว้ที่ 75–80% ของเฟรมเสมอ** ไม่ว่าจะสั่งเลย์เอาต์ยังไง → บรรทัดสั่งเลย์เอาต์ใน prompt แทบไม่มีผล
1. **ล้างพื้น**: ต่อกำหนดเงา/ประกายสีใต้วัตถุด้วย per-row quadratic fit บนคอลัมน์พื้นที่สะอาด แล้ว **ตัด chroma ให้เป็นเทาล้วน** (ถ้าคง chroma เดิม ประกายเขียวจะค้างอยู่)
2. **เลื่อนฉากขึ้น ~113px** ให้ฐานฉากตกที่ ~67% (แถบกลาง 20–70%) และขยายแถบพื้นท้ายด้วย Lanczos (ไม่มีรอยต่อ)

ตรวจผลด้วย: ค่า stddev/edge energy รายแถว (บน 20% ≈ stddev 2.3 edge 0.4 · ล่าง 30% ≈ stddev 4.5 edge 0.15)

## ⚠️ ห้าม resample ซ้ำ (เจอเอง 21 พ.ย. 16:00)
script เดิมเขียน `RAW = MASTER(2048) → ย่อกลับ 1024` ทับไฟล์ raw ทิ้ง → pipeline กลายเป็น
`raw 1024 → 2048 → 1024 → (surgery) → 1024 → 2048` = **resample ซ้ำ 3 รอบ** เสียความคมชัด
- วัดที่ 2048 แถบ active: mean |dx| **0.428**
- แก้: เก็บ raw ดิบจาก ComfyUI แยกไว้ (`img_00004_.png` md5 2633f29070d202a015dd6a0f235c96f5) → surgery → upscale ครั้งเดียว = mean |dx| **0.657** (+6%)
- ไฟล์ที่ส่งมอบเดิมยังผ่าน 4 ข้อที่เจ้าของตั้งไว้ แต่แก้แล้วคมกว่า → `duck-pipeline-v1-dk-2048.png`

## ⚠️ proxy วัดทิศหมวก
เทียบกับ **ปาก (bill)** เท่านั้น — ห้ามเทียบกับแกนคอนโซล (ให้ผลผิด)
ข้อมูลจากพิกเซลจริง: master ที่ส่งมอบ cap x 599–800 / bill x 599–685 (1024) = ปีกหมวกยื่นไปข้างหลังขวา ~115px = **สวมกลับหลังถูกต้อง**
ข้อควรระวัง: metric "ปาวนี้ขยายออกทางขวาของปาก" ให้ค่าบวกในทุก seed (65–125px) จึง **แยกทิศหมวกไม่ได้** — ทิศต้องดูด้วยตา ห้ามอ้าง metric นี้เป็นหลักฐาน

## ⚠️ นับลูกบาศก์เขียว / ห่วงตรวจด้วยพิกเซล
- กองลูกบาศก์เขียวในภาพที่ส่งมอบเป็น **ก้อนเรืองแสงเชื่อมกันหมด (1 connected component n=14820, x 413–615)** → นับ "8 ลูกแยกกัน" ไม่ได้ (ตาเห็นรอยตัดบางจุดแต่พิกเซลไม่แยก)
- ห่วงตรวจสีเหลือง: พิกเซลแยกได้เพียง 2 วงที่มีรูด้วย (15×18px, 18×17px) + ก้อนท่อทองเหลืองใหญ่ — วงที่ 3 ถูกกลืนกับท่อ
- สรุป: องค์ประกอบที่ "นับด้วยพิกเซล" ได้แบบมั่นใจคือตู้กระจก/ช่องฟ้า/ท่อทอง/เป็ดแว่นดำ ส่วนจำนวนลูกบาศก์-ห่วงให้ถือว่า "ไม่ยืนยัน"

## ข้อควรระวัง
- สั่ง "tiny / far away miniature" แล้วรายละเอียดหาย (ลูกบาศก์เขียว ห่วงตรวจหวานเล่นหายไป) — ใช้ขนาดฉากปานกลาง (สูง ~45% ของเฟรม)
- รอบ v1–v5 ของงานนี้เก็บไว้ที่ `/home/rakazo/generated/` (duck-pipeline-v1..v5) · raw ดิบจาก ComfyUI ที่ `/home/rakazo/generated/_comfy_pull/img_0000*.png`
- สคริปต์ที่ใช้ได้: `gen_duck_pipeline_v4.py`, `dk_rebuild.py` (surgery + single-resample master), `verify_final.py` (safe-zone + วัดทิศหมวก), `scene_audit.py`, `cap_per_seed.py`, `ring_check.py`
- Runbook ฉบับเต็ม (endpoint/พอร์ต/โมเดล/คีย์/ตัวอย่าง API): `shared/generated/z-image-comfyui-runbook.md`
