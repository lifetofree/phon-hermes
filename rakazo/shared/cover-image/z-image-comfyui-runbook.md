# Runbook: ComfyUI (Z-Image Turbo) — server GPU1 (เครื่องของเจ้าของ) — สำหรับงานภาพ adduckivity

เขียนโดย Image Gen · 21 พ.ย. 2026 · อัปเดต 22 พ.ย. 2026 โดย Chief (ComfyUI ย้าย Mac → server)

> ⚠️ **แก้ไข 22 พ.ย. 2026 (สำคัญ — บรรทัดเก่าทำให้ยิงผิดเครื่อง):**
> ComfyUI ย้ายจาก Mac → **server GPU1** เมื่อ 21 พ.ย. เย็น (Mac swap ล้น 26.9 GB, gen 40 นาที/รูป)
> **ComfyUI บน Mac ปิดถาวร** (LaunchAgents ถูก disable) → **8189 / 8188 ตายถาวร (HTTP 000) ห้ามยิง**
> โมเดลบน server ใช้ **ชื่อชุดใหม่** (ไม่มี fp8_mixed / ae.safetensors) → ต้องใช้ template ของ server
> ตรวจเอง 22 พ.ย. 05:1x: `GET http://172.18.0.1:8190/system_stats` → **200** (ComfyUI 0.34.0) · `/queue` → ว่าง
> และ `GET /object_info` → ยืนยันชื่อโมเดลตาม §2 ด้านล่าง

## 1. จุดเชื่อมต่อ (ปัจจุบัน = server)
| ข้อ | ค่า |
|---|---|
| เครื่อง | **server ของเจ้าของ (GPU1)** — เข้าถึงจาก container ผ่าน bridge |
| endpoint สำหรับ fleet | **`http://172.18.0.1:8190`** (ComfyUI 0.34.0, RAM 66 GB) |
| ~~พอร์ต 8189 (Mac)~~ | ❌ **ตายถาวร** — เครื่อง Mac ปิด ComfyUI แล้ว (HTTP 000) |
| ~~พอร์ต 8188 (Mac)~~ | ❌ **ตายถาวร** (HTTP 000) |
| ~~`http://100.107.249.87:8189`~~ | ❌ Tailscale IP ของ Mac — ใช้ไม่ได้แล้ว |
| คีย์/โทเคน | **ไม่ต้องใช้** (ไม่มี auth layer) |
| ความเร็ว | **~25 วินาที/รูป** (เทียบ Mac 40 นาที → เร็วขึ้น ~96 เท่า) |
| ตรวจสอบว่าพร้อมยิง | `curl -s -o /dev/null -w '%{http_code}' http://172.18.0.1:8190/system_stats` → ต้องได้ **200** |
| โมเดล LLM บนเครื่องเดียวกัน | llama = **gemma-4-12B** GPU0 ctx64k (Qwen3.8-27B อยู่บน disk สลับกลับได้) |

## 2. โมเดลที่ติดตั้ง **บน server** (ชื่อไม่เหมือนเครื่อง Mac เดิม!)
- UNet: `z_image_turbo_bf16.safetensors` (Z-Image Turbo)
- CLIP: **`qwen_3_4b.safetensors`** (type `lumina2`) — ⚠️ **ไม่มี** `qwen_3_4b_fp8_mixed.safetensors` บน server
- VAE: **`z_image_vae.safetensors`** — ⚠️ **ไม่มี** `ae.safetensors` บน server
- sampler: `euler` · scheduler `simple` · steps 8 · cfg 1.0 · denoise 1 (ค่าที่ได้ผลจริง)

> ⚠️ **ผล reroll จะไม่เหมือนเดิมแม้ใช้ seed เดิม** — เฟรม LDE ชุดเดิม (21 พ.ย. 22:37–22:50) เรนเดอร์บน Mac
> ด้วย `qwen_3_4b_fp8_mixed` + `ae.safetensors` ซึ่ง server ไม่มี → คนละ CLIP/VAE = คนละภาพ
> (`/history` ของ server ไม่มี prompt_id เดิม) → **รอบใหม่ต้อง QA + เทียบใหม่ทั้งชุด ห้ามคิดว่าเป็นไฟล์เดิม**

## 3. Template
| ไฟล์ | ใช้กับ |
|---|---|
| `shared/comfyui/z-image-template-server.json` | ✅ **server (ปัจจุบัน)** — node 3 = positive prompt, 4 = negative, 6 = size, 7 = seed |
| `shared/comfyui/z-image-template-imagegen.json` | ❌ **ของเครื่อง Mac เก่า — ใช้กับ server ไม่ได้** (ชี้ชื่อโมเดลผิดชุด) |
| `shared/comfyui/z-image-template.json` | ❌ เครื่อง Mac เก่า |

ห้ามแก้ config/โมเดล/workflow ของ ComfyUI — แก้แค่ node `3` (prompt), `4` (negative), `6` (w/h), `7` (seed)

## 4. ขั้นตอนยิงงาน (ตัวอย่างคำสั่ง API)
```bash
# 1) POST graph -> ได้ prompt_id
curl -s -X POST http://172.18.0.1:8190/prompt \
  -H 'Content-Type: application/json' \
  -d '{"client_id":"imagegen","prompt": <graph json>}'
# → {"prompt_id": "...."}

# 2) poll สถานะ (ทุก 10 วิ)
curl -s http://172.18.0.1:8190/history/<prompt_id>
# → status.status_str = success และ outputs["9"].images[0].filename

# 3) ดึงไฟล์ดิบ
curl -s -o out.png \
  'http://172.18.0.1:8190/view?filename=imagegen/img_000NN_.png&subfolder=imagegen&type=output'

# 4) ยกเป็น master 2048 (Lanczos) — upscale ครั้งเดียว
convert out.png -resize 2048x2048 -filter Lanczos -strip -define png:compression-level=9 master.png
```

สคริปต์ที่ใช้จริง (ฝั่ง Image Gen): `scripts/ld_gen_server.py` (ยิงทีละ seed ด้วย template server),
`scripts/validate_server_graph.py` (dry-run เทียบ node/inputs/enum/model กับ `/object_info` — ผ่าน = READY)

## 5. กฎที่ต้องจำ (เจ็ยว่าครั้งนี้)
- **ห้าม gen 2048 ตรง** — เคยค้าง ~30 นาทีบน Mac → gen 1024 แล้ว upscale Lanczos (บน server เร็วขึ้นมาก แต่ยังทำตามนี้)
- **อย่าเขียนทับ raw ด้วยไฟล์ที่ย่อจาก master** — เคยพลาดแล้ว: pipeline เดิมเขียน
  `RAW = MASTER(2048) → ย่อกลับ 1024` ทำให้ master ที่ส่งมอบถูก resample ซ้ำ 3 รอบ
  (ดู §6) → ให้เก็บ raw ดิบจาก ComfyUI แยกไว้เสมอ แล้วค่อย upscale ครั้งเดียว
- **หมวกกลับหลัง**: Z-Image ไม่ฟัง "worn backwards" เฉย ๆ ต้องบรรยายหลักฐานที่มองเห็นได้
  > *"a red baseball cap worn backwards, so the curved **peak** of the cap points away from the bill and sticks out behind the duck's head, while the **cap opening** and the small adjustable strap with its buckle are visible at the front of the forehead"*
  + negative: `brim above the bill, peak over the eyes, front-facing cap, hat facing forward`
  ผลจริง (Mac รอบ 21 พ.ย.): 5 รอบ → 1 รอบถูก (seed 426614869) — รอบที่ใช้คำว่า "brim"/"turned the wrong way round" ได้หมวกหันหน้าเกือบทุกครั้ง
- **safe zone**: Z-Image วางฐานฉากที่ 75–80% ของเฟรมเสมอ ไม่ว่าจะสั่งเลย์เอาต์ยังไง
  → ต้องทำ canvas surgery เอง (ล้างเงา/ปริศนีย์ด้วย quadratic fit → เลื่อนฉากขึ้น ~113 px → ยืดแถบพื้น)
- **ห้ามแทรกงานอื่นเข้าคิว** — ComfyUI คิว FIFO เดียว ใช้ร่วมกัน
- **ตรวจขอบซ้าย–ขวาด้วยเสมอ** (ข้อใหม่ 22 พ.ย.) — `qa_summary.py` ตรวจแค่แนวนอน (top20/bot30) → **แถบดำขอบซ้าย–ขวาผ่าน QA ได้**
  ใช้ `qa-toolkit/check_black_cols.py` (เพิ่ม 22 พ.ย. โดย Chief) + ตรวจ seam ให้ต่ำ

## 6. บันทึก resample ซ้ำ (เจอเอง 21 พ.ย. 16:00)
pipeline เดิม:
```
raw 1024 (ComfyUI) ──Lanczos──▶ 2048 ──Lanczos──▶ 1024 (ถูกเขียนทับ raw) ──surgery──▶ 1024 ──Lanczos──▶ 2048 (ส่งมอบ)
```
= 3 รอบ resample วัดความคมชัดในแถบ active ที่ 2048: mean |dx| 0.428
แก้แล้ว: เก็บ raw ดิบแยก (`img_00004_.png` md5 2633f29070d202a015dd6a0f235c96f5) → surgery → upscale ครั้งเดียว
= mean |dx| 0.450 (+5%) และไฟล์เล็กลง (1.34 MB vs 1.30 MB เดิมเล็กน้อยแต่คมกว่า)

> 22 พ.ย. — วิธี `fit3` (edge-replicate คอลัมน์ขอบ ไม่ resize ใหม่) ของ Image Gen สะอาดกว่าวิธี
> "ย่อ–ขยาย 1.05×" (มี resample เพิ่ม 1 รอบ) และไม่เปลี่ยน geometry แม้แต่พิกเซล — seam สูงสุด 40–50 เทียบ 78.67

## 7. วิธีวัดทิศหมวก (เทียบกับ **ปาก** เท่านั้น — อย่าเทียบกับแกนคอนโซล)
วัด centroid ของเม็ดสีแดง (หมวก) กับสีส้ม (ปาก) จากพิกเซลจริง:
- ไฟล์ส่งมอบ (Mac รอบเดิม): หมวก centroid x = 717 (ขอบขวาสุด x 800) · ปาก centroid x = 647 (ขอบขวาสุด x 685)
- → มวลหมวกอยู่**ขวาของ**ปาก = ปีกหมวกชี้ไปทางหลัง = **สวมกลับหลังถูกต้อง**
- **ข้อจำกัดสำคัญ (README qa-toolkit ข้อ 1):** proxy นี้แยก "กลับหลัง" ออกจาก "หันหน้า" ไม่ได้
  (ผลจาก 17 เฟรม: `d_cx` +39…+78 px, ปากอยู่ซ้ายของหมวกทุกเฟรม) → **ต้องให้เจ้าของตัดสินด้วยตา**
  (ช่องเปิดหน้าหมวก + สายปรับหัวเข็มที่หน้าผาก + บิลชี้ไปข้างหลัง)

---

## 8) บทเรียนจากรอบ 22 พ.ย. 05:2x (Image Gen เจอ + Chief ยืนยันซ้ำ)

**8.1 `fit_band` วางเนื้อหาต่ำเกิน → seam หลุดเข้า top20**
- `fit_band.py` วางเนื้อหาที่ ~19.8% ของความสูงภาพ → ขอบบนหลุดเข้า top20 (edge 127–219) → QA แนวนอนจะตก
- **ให้ใช้ `fit2` / `fit3` แทน** (fit3 = edge-replicate คอลัมน์ขอบ **โดยไม่ resize ใหม่** → geometry ไม่เปลี่ยนแม้แต่พิกเซล)

**8.2 `compose2` บังคับ resize เป็น 2048 = resample ซ้ำ → ใช้ `compose2_1k`**
- `compose2.py` resize เป็น 2048 ตรง ๆ → ได้ resample ซ้ำอีกรอบ (ผิวไม่คมเท่า)
- **`compose2_1k` = คงขนาด 1024 แล้วค่อย Lanczos ×2 ครั้งเดียวท้ายสุด** (ไม่มี resample ซ้ำ)

**8.3 toolkit ต้องมี scipy → รันด้วย `uv run`**
```bash
uv run --with scipy --with numpy --with pillow python3 qa_summary.py <file>
```
- ถ้ารัน `python3 qa_summary.py` ตรง ๆ → `ModuleNotFoundError: No module named 'scipy'`
- ไฟล์ .py ใน qa-toolkit (8 ไฟล์) เหมือนกันทุกบอท byte-for-byte · README อาจต่างกัน

**8.4 ข้อห้าม (เพิ่ม 22 พ.ย.)**
- **ห้าม `/interrupt` เอง** (ยกเลิกงานของบอทอื่นในคิว)
- **ห้าม publish เอง** (การเผยแพร่เป็นมือเจ้าของ)
- **ห้ามยิงชนคิวบอทอื่น** (ComfyUI คิว FIFO เดียว ใช้ร่วมกัน)

**8.5 QA ขอบซ้าย–ขวา: ใช้เครื่องมือเดียวกันทั้งทีม**
- `qa-toolkit/check_black_cols.py` (v3, 22 พ.ย.) รายงาน **2 เกณฑ์พร้อมกัน**:
  - `fixed-band` = แถบเนื้อหา rows 21–67% · พิกเซล max≤8 (ดำแท้) ≥50%
  - `auto-band` = หาแถบเนื้อหาจาก gradient อัตโนมัติ · พิกเซล max<30 (ดำ/มืด) ≥50%
  - พร้อม `max_col_seam` + ความสว่างขอบ 40px (ซ้าย/ขวา/กลาง)
- ตัวเลขอ้างอิงชุด LDE (ทั้ง 2 เกณฑ์ตรงกัน):
  | ไฟล์ (v2 = มีแถบดำ) | fixed | auto | seam | left40/right40 |
  |---|---|---|---|---|
  | DISCARD-v2-810244-full | 76 | 78 | 70.33 | 109.7 / 109.7 |
  | DISCARD-v2-710244-full | 244 | 246 | 68.67 | 105.1 / 105.1 |
  | DISCARD-v2-910244-full | 328 | 330 | 70.00 | 110.8 / 110.8 |
  | DISCARD-v2-110733-full | 406 | 408 | 68.67 | 109.2 / 109.2 |
  | DISCARD-v2-120957-full | 264 | 266 | 70.67 | 107.0 / 107.0 |
  | ✅ master v3 (810244) | **0** | **0** | **40.67** | **225.5 / 225.5** |
  (mid ของ v3 = 200.5 → ขอบสว่างกว่ากลาง = ปกสะอาด)

**8.6 provenance: raw 1024 (cef68bf3) = ต้นทางจริงของ master v3**
- raw ฝัง metadata ของ ComfyUI อ่านจาก tEXt ตรง ๆ:
  - node 2 CLIPLoader = `qwen_3_4b_fp8_mixed.safetensors` (type lumina2)
  - node 5 VAELoader = `ae.safetensors`
  - node 7 KSampler = seed **810244**, steps 8, cfg 1.0, sampler euler, scheduler simple, denoise 1.0, 1024×1024
  - node 9 SaveImage = filename_prefix `imagegen/ld_810244`
  - node 1 UNET = `z_image_turbo_bf16.safetensors`
  → **ชุดโมเดลของเครื่อง Mac (เก่า)** ไม่ใช่ของ server
- master v3 ได้จาก raw นี้ผ่าน fit3 (crop + edge-replicate) → compose2_1k → Lanczos ×2 ครั้งเดียว
  (Chief วัดเอง: raw กับ master ลงทะเบียนกันที่ crop ~186 แถวจากบน; raw คนละ seed (710244) ให้ RMSE สูงกว่าชัดเจน → เป็นภาพเดียวกันชุด)
- **ดังนั้น**: ถ้าจะ reroll seed เดิม **บน server (8190, qwen_3_4b + z_image_vae)** → ได้ภาพใหม่ ไม่ใช่ภาพเดิม (ต่างชุด CLIP/VAE)
