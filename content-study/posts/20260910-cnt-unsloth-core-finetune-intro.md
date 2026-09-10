# Unsloth Core — "Kernel" ที่เขียนใหม่ให้ Fine-tuning: 2x เร็วกว่า, VRAM น้อยลง 70%, และความแม่นยำไม่ตก

<!--
ContentID: 20260910-CNT-UNSLOTHCORE-LF
Series: Local LLM (part 5) — ต่อจาก Ollama (laptop / server), LM Studio (+Bionic), llama.cpp, Unsloth Studio
Type: Long Form (~2600 words)
Status: Draft — รอ review
Sources (researched 2026-09-10, primary):
- GitHub unslothai/unsloth — README main (fetch 2026-09-10)
- GitHub API repo stats (ตรวจ 2026-09-10): 75,961 stars / 6,915 forks / 1,316 open issues / created 2023-11-29 / pushed 2026-09-10 / topics: fine-tuning, rl, llm, self-hosted
- License (README, ใหม่): dual — Core = Apache-2.0, Studio UI = AGPL-3.0
- Releases API: v0.1.808-beta (2026-09-09) 250+ bug fixes, 60% smaller binaries, PyTorch 2.11, diffusion 1.2-1.7x faster; v0.1.804→808 ออก 5 release ใน 2 สัปดาห์
- unsloth.ai/docs/get-started/install/pip-install — Core install (uv + `uv pip install unsloth --torch-backend=auto`, Python 3.13, torch/CUDA matrix advanced install, Docker unsloth/unsloth + tag :core)
- unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements — Core requirements (Linux/Windows, NVIDIA compute cap 7.0+ V100→RTX 50→DGX Spark, AMD/Intel guides, Apple/MLX in the works, VRAM table QLoRA/LoRA 3B→405B)
- unsloth.ai/docs/get-started/fine-tuning-llms-guide — workflow, QLoRA/LoRA/FFT/RL, dynamic 4-bit, train+serve same precision, loss 0.5-1.0, epochs 1-3, export GGUF/vLLM/LoRA ~100MB
- README free notebooks table (Colab/Kaggle: Llama 3.1 8B 2x/70%, gpt-oss 20B 2x/70-80%, Gemma 4 E2B 1.5x/50%)
- README claims: 2x faster / 70% less VRAM no accuracy loss; MoE 12x faster 35% less VRAM; embedding 1.8-3.3x; padding-free+packing 3x + 30% less; 500K ctx on 80GB; 7x longer ctx RL; FastLanguageModel 2x inference; unsloth start (Claude Code/Codex/Hermes)
-->

พรเคยบอกไว้ในบทความ llama.cpp ว่า "คุณกำลังใช้ engine ของโลก local LLM อยู่แล้ว โดยไม่เคยเรียกมันตรง ๆ"

บทความนี้พรจะพาไปเจอ library ที่ "อยู่เบื้องหลัง" การทำให้คนธรรมดาเทรนโมเดลได้ — ถ้า llama.cpp เป็นเครื่องยนต์ที่รันโมเดล **Unsloth ก็คือตัวที่สอนโมเดล** และเวอร์ชันที่พรจะพาไปดูวันนี้คือ **Unsloth Core** — เวอร์ชันโค้ด, เวอร์ชันแรก, และเป็นตัวที่ทุกคนในวงการ fine-tuning ใช้จริง

## 01: Unsloth Core คืออะไร — "ตัวคอมไพล์" ของโลก fine-tuning

ก่อนอื่นแยกชื่อให้ชัดก่อนครับ เพราะ Unsloth มี 3 ตัวที่คนมักสับสน:

| ตัว | คืออะไร | ใครใช้ |
| --- | --- | --- |
| **Unsloth Core** | Python library (ต้นฉบับตั้งแต่ พ.ย. 2023) — เทรนโมเดลด้วยโค้ด/โน้ตบุ๊ก | นักพัฒนา, นักวิจัย, คนที่อยากควบคุมทุกตัวแปร |
| **Unsloth Studio** | Web UI (ออกมี.ค. 2026) — no-code, คุย-เทรน-เอ็กซ์พอร์ตในเบราว์เซอร์ | คนไม่แตะโค้ด (พรเขียนไว้แล้วใน part ก่อน) |
| **Unsloth Desktop** | Native app (Win/Mac/Linux) — wrapper ของ Studio ติดตั้งง่ายสุด | มือใหม่ที่อยากได้ครบชุด |

Core คือรากของทั้งสามตัว — Studio ทุกปุ่มที่กดอยู่เบื้องหลังคือโค้ด Core ทั้งหมด

ตัวเลขจริง (ตรวจ GitHub 10 ก.ย. 2026): **75,961 stars** (อันดับต้น ๆ ของ GitHub ทั้งเว็บ), 6,915 forks, 1,316 issues เปิดอยู่, เริ่มโปรเจกต์ พ.ย. 2023 โดย Daniel Han, Michael Han และทีม — และ cadence โหด: release 2 สัปดาห์ล่าสุดพรเห็น 5 ตัว (v0.1.804 → 808) ตัวล่าสุด **v0.1.808-beta ออก 9 ก.ย. 2026** พร้อม 250+ bug fixes

_license เป็น dual: ตัว Core = **Apache-2.0** (เอาไปใช้เชิงพาณิชย์ได้เลย), ส่วน UI ของ Studio = **AGPL-3.0** — ใครจะ embed UI ลงสินค้าต้องคิดเรื่อง AGPL แต่ใช้ Core ล้วน ๆ ไม่เกี่ยว_

## 02: ทำไมถึง "2x เร็ว VRAM น้อยลง 70%" — อธิบายแบบวิศวกร

ถ้า framework ทั่วไป (transformers + PEFT) เหมือนคอมไพล์โค้ดแบบ release build มาตรฐาน — Unsloth คือคนที่ **เปิดเครื่องคอมไพล์แล้วเขียน kernel ใหม่เอง**

กลไกหลักที่พรเห็นจาก docs + release notes:

**1. Triton Kernels ของตัวเอง** — RoPE (ส่วน rotation ที่ทำ positional encoding) และ MLP เขียนด้วย Triton ใหม่ แทนที่จะใช้ CUDA op มาตรฐานที่ PyTorch มี — ลด memory traffic ได้จริง ไม่ใช่แค่ "optimization เล็กน้อย"

**2. Padding-Free + Packing** — ตอนเทรน ข้อมูลแต่ละตัวอย่างยาวไม่เท่ากัน framework ปกติจะ padding ทุกแถวให้ยาวเท่ากัน → GPU คำนวณ token ที่ไม่ใช่ข้อมูลจริงฟรี ๆ Unsloth ตัด padding ออก + แพ็คหลายตัวอย่างลง sequence เดียว — ผลที่ประกาศ: **เทรนเร็วขึ้น 3x + VRAM น้อยลง 30%** (ตัวนี้คือของใหม่จาก blog อย่างเป็นทางการ)

**3. Dynamic 4-bit Quantization** — โมเดลที่ชื่อลงท้าย `unsloth-bnb-4bit` คือ quant 4-bit สูตรของตัวเอง กิน VRAM มากกว่า BitsAndBytes มาตรฐานเล็กน้อย **แต่ความแม่นยำสูงกว่า** — docs ระบุชัดว่าความแม่นที่หายไปเมื่อเทียบ LoRA 16-bit "ถูกกู้คืนมาเกือบหมด"

**4. Fuse operations + 4-bit training** — คำนวณ update ของ LoRA ใน 4-bit โดยตรง แทนการแปลงกลับเป็น 16-bit ทุก step

ผลลัพธ์รวมที่ README ประกาศ (และ community benchmark ยืนยันมาตลอด): **เทรนเร็วขึ้น ~2x, VRAM น้อยลง ~70%, ความแม่นยำไม่ตก** — และมีสถิติเฉพาะทางที่น่าจดจำ:

- **MoE LLMs เทรนเร็วขึ้น 12x** VRAM น้อยลง 35% (DeepSeek, GLM, Qwen, gpt-oss)
- **Embedding models เร็ว 1.8-3.3x**
- **Context 500K เทรนได้บน GPU 80GB** (20B)
- **RL context ยาวกว่า setup อื่น 7x** ด้วย batching algorithm ใหม่
- **FastLanguageModel** — ตัวเดียวกันรัน inference ให้เร็วขึ้นอีก 2x

พูดแบบระบบ: Unsloth ไม่ได้ "ทำ framework ง่ายกว่า" — มันทำ **layer ระหว่าง PyTorch กับ GPU ให้ฉลาดขึ้น** เลย

## 03: Feature map — ครอบคลุมกว่าที่คิด

**Methods ครบทั้ง spectrum:**
- **SFT (Supervised Fine-Tuning)** — มาตรฐาน คุยจาก dataset แบบ question-answer
- **LoRA / QLoRA** — เทรนแค่ ~1% ของ weights (LoRA = 16-bit, QLoRA = 4-bit) — docs บอกชัด: "ถ้าทำถูก LoRA ให้ผลเทียบเท่า full fine-tuning"
- **Full Fine-Tuning (FFT) + Pretraining** — ได้ แต่ docs เองเตือนว่า "FFT มักไม่จำเป็น"
- **Reinforcement Learning: GRPO, GSPO, DPO, ORPO** — สอนด้วย reward function แทน labeled data (เช่น สอน tool-calling) — อันนี้หายากมากใน OSS ที่รันบน GPU consumer
- **FP8 + QAT (Quantization-Aware Training)** — เทรนใน precision ที่จะ serve — หลักจาก docs: "train กับ serve ควรใช้ precision เดียวกัน"

**Model types ไม่จำกัด LLM:** diffusion (ภาพ/วิดีโอ), TTS, embedding, vision/multimodal — ครบ

**Free Notebooks — จุดที่คนเริ่มทุกคน:** Colab + Kaggle notebooks สำเร็จรูป กด ▶️ ตัวเดียว เช่น Llama 3.1 8B (2x เร็ว, VRAM น้อยลง 70%), gpt-oss 20B (2x, น้อยลง 70-80%), Gemma 4 (1.5x, 50%) — **zero GPU ของตัวเองก็เริ่ม fine-tuning ได้ฟรี**

**Export — ผูกกับ series นี้ทั้งชุด:**
- **GGUF** → ลง Ollama / llama.cpp / LM Studio (ต่อจากบทความ part 1-4 พอดี)
- **vLLM** (FP8/AWQ) → deploy multi-user / องค์กร
- **LoRA adapter** — ไฟล์เล็ก ~100MB — push ขึ้น Hugging Face ได้เลย

**Docker:** `unsloth/unsloth` (Studio + notebooks) มี tag `:core` สำหรับ notebooks ล้วน ๆ

## 04: ตัวเลข VRAM จริง — โมเดลไหนลงเครื่องคุณได้

ตารางขั้นต่ำจาก docs อย่างเป็นทางการ (QLoRA = 4-bit / LoRA = 16-bit):

| Parameters | QLoRA (4-bit) | LoRA (16-bit) |
| --- | --- | --- |
| 3B | 3.5 GB | 8 GB |
| 7B | 5 GB | 19 GB |
| 8B | 6 GB | 22 GB |
| 14B | 8.5 GB | 33 GB |
| **27B** | **22 GB** | **64 GB** |
| 32B | 26 GB | 76 GB |
| 70B | 41 GB | 164 GB |
| 405B | 237 GB | 950 GB |

ลองคิดกับเครื่องพรเอง: **2× RTX 5060 Ti (16GB × 2 = 32GB)** — ตามตาราง QLoRA 27B ต้อง 22GB → **พอ** ถ้าใช้ multi-GPU (Unsloth รองรับ multi-GPU training + split model) — แปลว่าเครื่องที่พรรัน Qwen3.8-27B inference อยู่แล้ว (จากบทความ llama.cpp) ก็คือเครื่องที่ **fine-tune ตัวเดียวกันได้** ด้วย — วงจรปิดทั้งหมดบนเครื่องเดียว: เทรน → export GGUF → serve

(ตัวเลขนี้เป็นการอ่านตาราง docs + arithmetic ไม่ใช่ benchmark ที่พรรันจริง — ถ้าพรได้ลองจริงจะอัปเดตตัวเลขในบทความก่อน publish)

**Requirements ของ Core โดยเฉพาะ:**
- **Linux / Windows** (+ WSL), NVIDIA ตั้งแต่ GPU ยุค 2018 (compute capability 7.0: V100, T4, Titan V, RTX 20xx/30xx/40xx/50xx, A100, H100, L40) — รวมถึง **Blackwell RTX 50 + DGX Spark**
- **AMD / Intel** = มี guide แยกเฉพาะ
- **Apple / MLX = "in the works"** สำหรับ Core — Mac เทรนผ่านเส้น Studio/MLX ได้ (ดูบทความ Unsloth Studio)
- **Python 3.11–3.13** (ยังไม่ 3.14), ติดตั้ง: `uv venv unsloth_env --python 3.13` + `uv pip install unsloth --torch-backend=auto` — หรือ `pip install unsloth` สั้น ๆ

## 05: ข้อดี ✅

**1. เร็วจริง VRAM จริง — ไม่ใช่ marketing** — 2x/70% มาจากการเขียน kernel + packing ใหม่ มี blog ละเอียดอธิบายกลไก + community benchmark ยาวนาน 3 ปี

**2. Free ทั้งระบบ** — Core = Apache-2.0, notebooks Colab/Kaggle ฟรี = คนไม่มี GPU เริ่มได้จริง (3.5GB สำหรับ 3B QLoRA)

**3. ครบที่สุดสำหรับสายเทรน** — SFT → QLoRA → FFT → pretrain → RL (GRPO/DPO) → FP8 → QAT → embedding → TTS → vision — หา OSS ตัวเดียวที่ครอบคลุมทั้ง spectrum นี้ยากมาก โดยเฉพาะ **RL บน GPU consumer**

**4. Code-based = reproducible** — ทุกอย่างคือ script/โน้ตบุ๊ก: commit ได้, run ซ้ำได้, ใส่ CI/CD ได้, debug ได้ — Studio กดปุ่มสวยแต่ Core คือสิ่งที่ทีม production ต้องจบที่

**5. Export สะดวกกับ ecosystem ที่คุณมีอยู่แล้ว** — GGUF → Ollama/llama.cpp (series นี้), vLLM → multi-user, LoRA ~100MB → HF hub — ไม่ lock-in

**6. Active จริง** — 76k stars, release แทบทุกสัปดาห์, 1,316 issues กำลังถูกจัดการ, ทีมตอบใน Discord/Reddit — โปรเจกต์ 3 ปีที่ไม่ dead

## 06: ข้อเสีย ❌

**1. ต้องเขียนโค้ด** — ถ้าไม่แตะ Python/โน้ตบุ๊กเลย = ใช้ Studio หรือ Desktop แทน Core จะทำให้คุณเจ็บเปล่า

**2. Windows training = หนัก** — Python 3.11-3.13 + CUDA + build tools + torch/CUDA version matrix (advanced install แยก cu118/cu121/cu124/ampere ตาม torch version) — docs เองมีหน้า "Advanced Pip Installation" ยาวเป็นหน้าเพราะ dependency จริง ๆ ยาก

**3. VRAM ceiling ยังมี** — 27B QLoRA = 22GB, 70B = 41GB — การ์ด 16GB ตัวเดียว (5060 Ti/4080) ไปถึง 14B QLoRA (8.5GB) ก็ต้องคุม batch/ctx ให้ดี — "70% น้อยลง" คือเทียบกับมาตรฐาน ไม่ใช่ "เทรน 70B บนการ์ด 8GB"

**4. ยังเป็น beta ทั้งหมด** — แม้ Core ก็ยังเป็น v0.1.x-beta — API อาจเปลี่ยนระหว่าง minor versions (release notes ยืนยันว่ามี fix โครงสร้างทุกตัว)

**5. License dual = ต้องคิดถ้าทำ product** — Core = Apache-2.0 ไม่มีปัญหา แต่ถ้าเอา Studio UI (AGPL-3.0) ไป embed ลง commercial product ต้องอ่านเงื่อนไข AGPL

**6. Dependency หนัก** — ดึง torch/transformers/TRL/BitsAndBytes/xformers/triton มาด้วย — กิน disk เยอะ และถ้า version ขัด docs ต้องใช้ force-reinstall procedure (มีใน docs แต่เป็น friction จริง)

**7. ไม่มี experiment tracking ระดับ MLOps** — log การเทรน, เปรียบเทียบ runs, lineage — ต้องต่อ W&B/MLflow เอง — สำหรับทีมที่เทรนหลายร้อย runs นี่คืองานเพิ่ม

## 07: เทียบกับทางเลือกอื่น (ก.ย. 2026)

| | **Unsloth Core** | **Unsloth Studio** | **DIY (transformers + PEFT + TRL)** | **Cloud fine-tuning API (OpenAI etc.)** |
| --- | --- | --- | --- | --- |
| ราคา | ฟรี (Apache-2.0) | ฟรี (UI = AGPL-3.0) | ฟรี (MIT/Apache) | $$$ ต่อ token + โมเดลถูก lock |
| ความเร็วเทรน | 2x เร็วกว่า | เหมือน Core | ฐาน (ช้าสุด) | n/a (เขาเทรนให้) |
| VRAM | น้อยลง 70% | เหมือน Core | ฐาน | n/a |
| เริ่มง่ายสุด? | Notebook ฟรี | กดปุ่ม | ต้องตั้งเองทุกอย่าง | ง่ายสุดแต่ไม่ local |
| ควบคุม/แก้ bug | เต็มที่ | จำกัดที่ UI | เต็มที่ | ไม่มี |
| RL (GRPO/DPO) | ✅ | ✅ (จำกัด) | ✅ (ต้องเขียนเอง) | ❌ (บางเจ้ามี DPO อย่างเดียว) |
| Export local (GGUF) | ✅ | ✅ | ทำเอง | ❌ (weights ไม่ออก) |
| เหมาะกับ | ทีม/dev ที่ deploy local | มือใหม่ → power user | คนอยากเรียนกลไก | คนไม่ต้องการ local |

_หมายเหตุ: Studio ใช้ Core เป็น backend — ความเร็ว/VRAM เท่ากัน ต่างกันที่ interface ไม่ใช่ engine_

## 08: เหมาะกับใคร (และใครควรข้ามไป)

**1. คนที่รัน local LLM อยู่แล้ว แต่โมเดล "ไม่ตรงงาน"** — มี Ollama + llama.cpp อยู่ (part 1-4) แต่โมเดลตอบไม่ถูก domain ของคุณ — Core คือ bridge จาก "รัน" ไป "เทรน" แล้ว export GGUF กลับลงมาเครื่องเดิม

**2. คนเขียน Python ได้ + อยากควบคุม** — ทุก hyperparameter, kernel, dataset pipeline เป็นโค้ดของคุณ — reproducible = ทีมอื่นรันซ้ำได้

**3. นักวิจัยสาย RL / reasoning** — GRPO + GSPO + long-context RL บน GPU consumer = หนึ่งในไม่กี่ทาง OSS ที่ทำได้จริง — notebook สำเร็จรูปมีให้

**4. คนไม่มี GPU เลย** — เริ่มจาก Colab notebooks ฟรี (QLoRA 8B บน T4) แล้วค่อยขยับมาเครื่องตัวเอง — เส้นทางนี้ docs ออกแบบมาให้ชัด

**ข้ามไปถ้า:**
- ยังไม่เคยแตะโค้ด → **Unsloth Studio** (บทความ part ก่อน)
- แค่อยากคุยกับโมเดล → **Ollama** (fine-tuning = overkill — RAG ก่อน แล้วค่อยพิจารณา)
- องค์กร multi-tenant production → fine-tune ด้วย Core ก็ถูก แต่ **serving ต้องจบที่ vLLM + MLOps** ไม่ใช่ Unsloth

## 09: Pro Tips แยกตามระดับ

**มือใหม่:**
- เริ่ม QLoRA 8B + Colab notebook สำเร็จรูป — loss ~0.5-1.0 = สัญญาณดี, loss ลง 0 = overfit
- epochs 1-3 เท่านั้น (docs แนะนำ), เริ่มจาก **Instruct models** (chat template พร้อม) ไม่ใช่ Base
- gradient_accumulation_steps แทนการดัน batch size (ประหยัด VRAM)

**ใช้จริงจัง:**
- **Train precision = Serve precision** — ถ้าจะ serve 4-bit ให้เทรน 4-bit
- ใช้โมเดล `unsloth-bnb-4bit` (dynamic quant) แทน bnb-4bit มาตรฐาน — แม่นยำสูงกว่า
- packing + padding-free เปิดไว้เสมอ — 3x เร็วไม่มีเหตุผลไม่เปิด
- เครื่องพร (2× 5060 Ti) = ลอง QLoRA 27B (22GB) ด้วย multi-GPU — 27B คือ sweet spot ของ VRAM 32GB

**องค์กร:**
- Docker `unsloth/unsloth:core` สำหรับ pipeline ที่ repeatable
- เทรน QLoRA/LoRA → export GGUF (edge/laptop) + vLLM FP8/AWQ (server) จาก run เดียว
- ต่อ W&B/MLflow เองตั้งแต่ runแรก — อย่ารอจน runs พอก่อน

## 10: สรุปแบบวิศวกรเป็ด

ถ้า local LLM ecosystem เป็นโรงงาน: **llama.cpp คือเครื่องจักรผลิต (inference), Ollama/LM Studio คือหน้าร้าน, และ Unsloth Core คือห้องวิจัยที่สร้างสูตรใหม่**

จุดยืนของ Unsloth ที่พรสรุปจาก research คือ: "fine-tuning ไม่ควรต้อง data center" — และ 3 ปีที่ผ่านมา มันพิสูจน์ด้วยตัวเลข ไม่ใช่คำสัญญา — kernel ของตัวเอง, packing, dynamic 4-bit — ทำให้ 70B QLoRA ลง GPU 41GB และ 27B ลงเครื่อง 2× 16GB ที่บ้านคุณได้

สำหรับ series นี้ Unsloth Core คือ **loop ปิด** — คุณอ่านมา 4 part ว่า "รัน" โมเดล local ยังไง (Ollama → LM Studio → llama.cpp → Studio) — part นี้คือ "สร้าง" โมเดลของคุณเอง แล้วเอากลับลงเครื่องเดิมด้วย GGUF — ครบวงจร บนเครื่องเดียว

พรจะเอาเครื่อง 2× 5060 Ti ลอง QLoRA 27B จริง แล้วมาอัปเดตตัวเลข benchmark ในบทความนี้ก่อน publish ครับ — เหมือนที่ทำในบทความ llama.cpp

#Adduckivity #DuckOS #NeuroDivergent #Unsloth #FineTuning #LoRA #QLoRA #GRPO #LocalLLM
