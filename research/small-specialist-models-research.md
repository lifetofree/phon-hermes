---
type: research
topic: 7 small specialist models vs giant LLMs (pair #105)
used_by: [20261106-cnt-small-specialist-models]
---

# 7 Small Specialist Models (pair #105) — research 2026-11-06

## ต้นฉบับ (source of the brief)
- **KDnuggets:** "7 Small Specialist Models That Beat Giant LLMs at One Job" — Shittu Olumide, 4 พ.ย. 2026
  https://www.kdnuggets.com/7-small-specialist-models-that-beat-giant-llms-at-one-job
- กฎคัดเลือกของต้นฉบับ 4 ข้อ: open weights / งานเดียวชัด / มี proof ที่ตีพิมพ์เทียบของใหญ่ / footprint รันบนเครื่องเดียวได้
- ปิดท้ายต้นฉบับ: "pick one job in your own stack... keep the giant for what only it can do"

## ตัวเลขจริงต่อโมเดล (verify กับ primary source 2026-11-06)

### 1. Parakeet TDT 0.6B v3 — transcription (0.6B, CC-BY-4.0)
- **ชนะที่:** WER 6.32 vs Whisper large-v3 7.44 (Open ASR Leaderboard paper — avg WER) + เร็ว ~23× (RTFx 3,330 vs 146)
- **primary:** HF model card nvidia/parakeet-tdt-0.6b-v3 (card เองขึ้น 6.34% — paper 6.32; 25 European languages, auto-detect)
- **catch (จริง):** ภาษา 25 vs Whisper 99; snapshot พ.ย. 2026 (ของต้นฉบับ): English Parakeet ชนะ (5.66 vs 6.5) แต่**แพ้ Whisper ใน 5 จาก 6 ภาษายุโรปอื่นที่วัด**
- **catch เพิ่ม (verify):** WER ขึ้นตามสัญญาณรบกวน — 6.34 (clean) → 8.23 @SNR 5dB → 11.66 @0dB; AMI (เสียงประชุม) 11.31% vs LibriSpeech clean 1.93% — งาน "เสียงประชุม" ที่ draft พูดถึง คือจุดที่ตัวเล็กทำ хужеสุดใน set ของมัน
- หมายเหตุ: ตัวที่แพ้คือ "speech model ใหญ่" (Whisper) ไม่ใช่ chat LLM — ต้นฉบับบอกเอง

### 2. PaddleOCR-VL-1.6 — OCR/document parsing (0.9B, Apache 2.0, release 28 พ.ค. 2026)
- **ชนะที่:** OmniDocBench v1.6 = 96.33 vs Gemini 3 Pro 92.91, GPT-5.2 86.59
- **primary:** HF PaddlePaddle/PaddleOCR-VL-1.6 (SOTA overall/text/formula/tables; ตัว Gemini-3 Pro + Qwen3-VL-235B + ตัวเอง = ประเมินอิสระ, ตัวอื่น cite จาก leaderboard ทางการ)
- **catch (จริง + verify):** ไม่ได้อยู่คนเดียวที่ top — **TeleOCR 96.91 และ OvisOCR2 96.47 อยู่ข้างบน** (roundup ก.ย. 2026 ที่ต้นฉบับใช้) → ใจความจริง = "top 3" ไม่ใช่ "#1"; บน leaderboard ทางการอันดับ 1 เปลี่ยนตามรอบได้
- หมายเหตุ: 96.33 เป็น overall score ของ benchmark (รวม text/formula/table) ไม่ใช่ "accuracy 96.33%" ในความหมายทั่วไป — draft เขียน "คะแนนอ่านเอกสาร" ถูกทาง

### 3. GLiNER — entity extraction zero-shot (50M–~300M, repo Apache-2.0 แต่**เช็ค license ราย checkpoint** — checkpoint เก่าบางตัว CC BY-NC)
- **ชนะที่:** GLiNER-S (50M) = 52.7 vs ChatGPT 47.5 (out-of-domain table ใน paper NAACL 2024, zero-shot NER avg)
- **primary:** arXiv 2311.08526 (abstract: outperforms ChatGPT + fine-tuned LLMs ใน zero-shot)
- **catch (จริง + verify):** "ChatGPT" ที่เทียบคือ**รุ่นยุค 2023** — ตัว GPT ปัจจุบันไม่ได้ถูกเทียบ; GLiNER ตัด span ออกได้ แต่ไม่ reason/ไม่เติมของขาด → งาน "pull names + amounts แล้วใช้ต่อ" ต้องมีอะไรทำต่อ

### 4. EmbeddingGemma — embeddings (308M, Gemma terms, gated)
- **ชนะที่ (honest framing ของทั้งต้นฉบับและ Google):** อันดับ 1 **ใน class open multilingual embedding <500M** บน MTEB (100+ languages, quantize แล้ว <200MB RAM)
- **primary:** Google Developers Blog "Introducing EmbeddingGemma" + arXiv 2509.20354 (SOTA multilingual/English/code ใน class)
- **catch (จริง + verify):** **ไม่ใช่การชนะ giant LLM** — ตัวต้นฉบับเองก็เขียนว่า "a claim about its size class, not a win over a giant"; มีตัวใหญ่กว่าที่คะแนนสูงกว่า เช่น jina-embeddings-v5-text-small (~677M); context 2,048 tokens — เอกสารยาวต้อง chunk
- หมายเหตุ: นี่คือตัวที่ "อ่อนสุด" ใน 7 ตัวเรื่อง claim ชนะ — draft ต้องไม่ขายมันในรูป "แซงตัวใหญ่" (header draft เขียนถูกต้องแล้ว)

### 5. Arch-Router — routing (1.5B, finetune จาก Qwen2.5-1.5B-Instruct บน 43k examples, Katanemo research license)
- **ชนะที่:** routing score 93.17% — สูงกว่า proprietary ที่วัด (GPT-4o, Claude-Sonnet-3.7) เฉลี่ย 7.71%
- **primary:** arXiv 2506.16655 + HF katanemo/Arch-Router-1.5B
- **latency:** ~50ms/decision vs ~510ms (Gemini-2.0-flash-lite) / ~1,450ms (Claude-Sonnet-3.7) (PromptHub ที่ต้นฉบับ cite)
- **catch (จริง):** (1) **routing เท่านั้น — โมเดลหลังแต่ละ route ยังต้องจัดเอง** (2) quality ขึ้นกับ description ที่เราเขียน → ต้อง test (3) license = research ของ Katanemo ไม่ใช่ Apache — อ่านก่อนเอาไป ship
- หมายเหตุ: 93.17 = ความแม่นในการจับ query→route ตาม human preference บน conversational dataset ไม่ใช่ "แม่นกว่า GPT-4o ในทุกเรื่อง"

### 6. Nemotron-Orchestrator-8B — tool decisions (8B, Qwen3-8B base, NVIDIA License **research only**)
- **ชนะที่:** HLE 37.1% vs GPT-5 35.1% + 2.5× more efficient + ~30% cost (τ²-Bench 80.2 vs 77.7, FRAMES 76.3 vs 74.0)
- **primary:** NVIDIA Research ToolOrchestra page + arXiv 2511.21689 + HF nvidia/Nemotron-Orchestrator-8B (NVLabs/ToolOrchestra)
- **catch สำคัญ (จริง + verify):** บน τ²-Bench มัน**ยังเรียก GPT-5 ~40% ของ steps** + ตัวถูกกว่าที่เหลือ → "win" = การตัดสินใจว่าจะส่งงานให้ใคร (orchestration) ไม่ใช่การแทนที่ giant — นี่คือตัวอย่างที่ draft ใช้ (ประโยค "ยังส่งงานกลับไปให้ตัวใหญ่ราวสี่สิบเปอร์เซ็นต์") — ตรงกับ primary ✓
- **catch เพิ่ม (verify):** ตัวเทียบ GPT-5 ก็ไม่ใช่ frontier แล้ว (ต้นฉบับบอกเอง); license research-only → production ยังไม่ได้

### 7. Kokoro-82M — TTS (82M, Apache 2.0, weights ~327MB)
- **ชนะที่:** ตอนเปิดตัว (ธ.ค. 2024) = อันดับ 1 บน TTS Spaces Arena ชนะ XTTS v2 (467M) ฯลฯ (UnfoldAI)
- **primary:** GitHub hexgrad/kokoro (82M, Apache 2.0, v0.19 ปล่อยเต็ม fp32 25 ธ.ค. 2024)
- **catch (จริง + verify):** **ไม่ใช่ leader แล้ว** — roundup 2026: ยืนอันดับ 6 บน Artificial Analysis Speech Arena (Elo 1,060); **NVIDIA Magpie (357M) แซงแล้ว**; ไม่มี voice cloning
- หมายเหตุ: ตัวนี้ "win" เป็นอดีต — ใช้ได้ถ้าขายว่า "ตอนเปิดตัว" เท่านั้น (header draft เขียน "ตอนเปิด" + "ยืนอันดับ 6 ปัจจุบัน" ถูกแล้ว)

## สรุป pattern (สิ่งที่ 7 ตัวร่วมกัน — แกนของ draft)
1. ทุกตัวชนะ **งานเดียว** ที่พูดจบได้ในประโยคเดียว (transcribe / read doc / extract / embed / route / decide / speak)
2. ทุกตัวมี **catch ที่จำกัดขอบเขต win** — ภาษาที่รองรับ / class size / license / ตัวเทียบที่ล้าสมัย / อันดับเปลี่ยน / ยังต้องพึ่ง giant → "ตัวเล็กชนะ" ไม่ใช่ "ตัวใหญ่ไร้ประโยชน์"
3. ตัวที่ win แบบ "การตัดสินใจ" (Nemotron) คือตัวอย่างที่ชัดสุดว่า win คือ orchestration ไม่ใช่ replacement — ตรงกับ spine ของ draft
4. ต้นฉบับตั้งกติกาเองว่า "giant ไม่ได้แปลว่า chat LLM เสมอไป — บางตัวแพ้ speech model ใหญ่ ไม่ใช่ LLM" → claim "ชนะ giant" ในบางแถวต้องอ่านให้ถูกชั้น

## Discrepancies (draft vs ต้นฉบับ vs primary) — ตรวจแล้ว
- ตัวเลขทั้ง 7 ตัวใน header draft ตรงกับทั้งต้นฉบับและ primary (6.32/7.44, 23×/3330 vs 146, 96.33/92.91/86.59, 52.7/47.5, <500M MTEB, 93.17/+7.71/~50ms vs 510-1450, 37.1/35.1/~40% steps, TTS Arena #1→6)
- **header draft เขียน "pair #104" แต่ index.json + STATE.md = pair #105** — typo ใน header (แก้เป็น #105)
- ตัวเลข 5.66 vs 6.5 (English, snapshot พ.ย. 2026) อยู่ในต้นฉบับเท่านั้น — ไม่ได้ verify กับ leaderboard โดยตรง (ไม่จำเป็น ถ้าไม่ cite ในตัว post)

## Parked (วัตถุดิบที่เหลือ — ใช้ถ้า Benz r1 ให้จุด)
- AMI 11.31% (เสียงประชุมของตัวเล็กเอง) — ใช้ตอก "งานที่พูดไม่จบตัวเล็กก็ช่วยไม่ได้" ได้แรงขึ้น
- TeleOCR/OvisOCR2 อยู่บน PaddleOCR → "แม้ top-3 ก็ยังมีตัวอื่นชิง" = ตัวอย่างว่างานเดียวก็ไม่ได้มีตัวเล็กเดียว
- jina-embeddings-v5 677M > EmbeddingGemma → ตัวเล็กใน class หนึ่งก็แพ้ตัวใหญ่ใน class เดียวกัน — ขยาย "ถูกงาน ≠ ถูกขนาด"
- Parakeet WER ใต้ noise 11.66% → งานจริง (ประชุมห้องดัง) ตัวเลขสวยหาย
- "43,000 examples" ที่ Arch-Router finetune → ตัวเล็กถูก"เลือก"ด้วย data ที่เลือกมา — ข้างหลัง win คือ curation ไม่ใช่เวทมนตร์
- Magpie 357M แซง Kokoro → leaderboard คือ snapshot ไม่ใช่สถานะถาวร

## SOURCES (primary — verify 2026-11-06)
- https://www.kdnuggets.com/7-small-specialist-models-that-beat-giant-llms-at-one-job (ต้นฉบับ — ดึงเต็มบทความผ่าน browser)
- https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3 (model card: 25 lang, 6.34 avg, AMI 11.31, LS 1.93, noise curve)
- https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6 (model card: OmniDocBench v1.6 SOTA + note ประเมินอิสระ)
- https://arxiv.org/abs/2311.08526 (GLiNER paper)
- https://developers.googleblog.com/en/introducing-embeddinggemma/ + https://arxiv.org/abs/2509.20354 (EmbeddingGemma: #1 open <500M MTEB)
- https://arxiv.org/abs/2506.16655 + https://huggingface.co/katanemo/Arch-Router-1.5B (93.17%, +7.71%, Qwen2.5-1.5B finetune 43k)
- https://research.nvidia.com/labs/lpr/ToolOrchestra/ + https://arxiv.org/abs/2511.21689 + https://huggingface.co/nvidia/Nemotron-Orchestrator-8B (HLE 37.1 vs 35.1, 2.5×, τ² 80.2/77.7, FRAMES 76.3/74.0)
- https://github.com/hexgrad/kokoro (82M, Apache 2.0, v0.19 25 ธ.ค. 2024)
- secondary (verify catches): localaimaster.com (RTFx 3,332.74, 25 vs 99), liner.com review (93.17%), CSDN/aibase (PaddleOCR 96.33 release 2 พ.ค. 2026)
