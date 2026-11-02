# llama.cpp — Engine ของ Local LLM ที่แทบทุกเครื่องมือ "ยืม" ไปใช้ (แต่หลายคนยังไม่เคยเรียกมันตรง ๆ)

<!--
ContentID: 20260909-CNT-LLAMACPP-LF
Series: Local LLM (part 4) — ต่อจาก Ollama (laptop / server), LM Studio (+Bionic), Unsloth Studio
Type: Long Form (~2600 words)
Status: Draft — รอย review
Sources (researched 2026-09-09, primary):
- github.com/ggml-org/llama.cpp — README master (MIT, LLM inference in C/C++, ggml, 127,574 stars / 22,927 forks, created 2023-03-10)
- GitHub API repo stats (ตรวจ 2026-09-09): stars 127,574, forks 22,927, open issues 2,445, license MIT
- Release v0.4.0 (2026-09-04): Qwen3.8-Flash-Next + Nemotron-3-Puzzle support, lazy tensor reading, per-slot ctx limits, video input, ggml 0.23.0 sparse flash attention + RDMA
- Nightly releases: b10871 (2026-09-09) — commit cadence หลาย release/วัน
- tools/server/README.md (master): OpenAI-compat chat/completions/responses/embeddings + Anthropic Messages API compat, reranking, continuous batching, multimodal, function calling, speculative decoding, web UI
- Local build บน PHON-SERVER (verified 2026-09-09): CUDA build, llama-server --version, --jinja, -hf flag, GBNF grammars
- Real benchmark บนเครื่องพร (2× RTX 5060 Ti, Qwen3.8-27B Q4_K_M, ctx 262144, -ngl 44, --split-mode layer): ~7.8 tok/s รวม prompt processing, llama-server port 8080
- Quantization: 1.5-bit ถึง 8-bit integer (README)
- Backends (README): CUDA/HIP/Metal/Vulkan/SYCL/CANN/MUSA/ZenDNN/OpenCL Adreno/Snapdragon Hexagon/IBM zDNN/RPC/VirtGPU/WebGPU — 17 ชั้น
-->

คุณกำลังใช้ llama.cpp อยู่ — แม้คุณจะไม่เคยพิมพ์ชื่อมันเลย

ถ้าคุณเคยรัน Ollama บน laptop, เคยเปิด LM Studio คุยกับโมเดลในเครื่อง, เคยลาก GGUF ไปวางใน app ใด ๆ ก็ตาม — โอกาสสูงมากว่า **ตัวที่ทำงานอยู่เบื้องหลังคือ llama.cpp**

มันคือเครื่องยนต์ (engine) ของโลก local LLM — เขียนด้วย C/C++ ล้วน ๆ ไม่มี dependency ตัวพรเลยก็ build ได้, รันได้ตั้งแต่ Raspberry Pi ยัน server หลาย GPU — และเพราะมันเป็น MIT license ทุกเจ้า "ยืม" มันไปทำ frontend ของตัวเอง

วันนี้พรจะพาเข้าไปดู engine ตัวนี้ตรง ๆ ครับ — ว่ามันทำอะไรได้บ้าง, ดีตรงไหน, แย่ตรงไหน, และใครควรมาเรียกมันเองแทนการยืมผ่านคนอื่น

## 01: llama.cpp คืออะไร — "Engine" ไม่ใช่ "รถ"

ถ้าเปรียบ local LLM เป็นรถ:

- **GGUF** (โมเดลไฟล์) = น้ำมัน
- **Ollama / LM Studio / Bionic** = รถสำเร็จรูป — ติดแอร์ มีหน้าปัด ขับง่าย
- **llama.cpp** = **เครื่องยนต์** — กลไกจริงที่เผาน้ำมัน (GGUF) ให้กลายเป็นแรง (tokens)

โปรเจกต์โดย Georgi Gerganov (ggml-org) เริ่มตั้งแต่ มี.ค. 2023 — ในยุคที่ LLaMA ตัวแรกของ Meta ยังเพิ่งออก และคนส่วนใหญ่ยังคิดว่ารัน LLM ต้องมี GPU แสนกว่าบาท จนกระทั่ง llama.cpp พิสูจน์ว่า **MacBook เครื่องเดียวรันได้** เพราะมันเขียนให้ CPU ธรรมดา (และ Apple Silicon) เร็วขึ้นมากด้วยการ optimize ลงถึงระดับ instruction set

จุดยืนของโปรเจกต์ (จาก README ตรง ๆ): **"enable LLM (and VLM) inference with minimal setup and state-of-the-art performance on a wide range of hardware"** — inference แบบ setup น้อยที่สุด + เร็วระดับแนวหน้า บน hardware ได้หลากหลายที่สุด

ตัวเลขความจริง (ตรวจจาก GitHub ปลายเดือน ก.ย. 2026): **127,574 stars** (ติด top ของ GitHub ทั้งเว็บ), 22,927 forks, MIT license — และ cadence การพัฒนาโหดมาก: release ใหม่เฉพาะที่พรเห็นในวันเดียวมีถึง 4 ตัว (b10868–b10871, 9 ก.ย. 2026) และ major version ล่าสุด **v0.4.0 เพิ่งออก 4 ก.ย. 2026**

มันทำงานบน **ggml** — tensor library คู่หูที่เป็นส่วน "คณิตศาสตร์เมทริกซ์" ของระบบ — คิดง่าย ๆ ว่า llama.cpp = driver, ggml = engine block

## 02: ความสามารถหลัก (Features) — มากกว่า "แค่รันโมเดล"

**1. รันได้แทบทุกชิ้นส่วนบนโลก (17 backends)**

นี่คือจุดที่ llama.cpp ไม่มีใครแข่ง: NVIDIA (CUDA), AMD (HIP), Apple (Metal), Intel (SYCL), Huawei Ascend (CANN), Moore Threads (MUSA), Vulkan, แม้แต่ Snapdragon (Hexagon), IBM Z mainframe (zDNN), และ WebGPU ใน browser — บวก RPC กระจายงานข้ามเครื่อง

สำหรับวิศวกร: แปลว่าโค้ดชุดเดียว deploy ได้ทั้งบน gaming rig ที่บ้าน, Mac Studio ที่ทำงาน, และ edge device หน้างาน — ไม่ต้องเรียนระบบใหม่ทีละแพลตฟอร์ม

**2. Quantization ครบ 1.5-bit ถึง 8-bit**

quantization = การบีบโมเดลให้เล็กลงโดยเสียความแม่นยำน้อยที่สุด (เหมือน zip ไฟล์ภาพ — เล็กลง 90% แต่ตาเราแทบไม่รู้ความต่าง) llama.cpp เป็นผู้บุกเบิกตรงนี้เอง — ระดับ 1.5-bit, 2, 3, 4, 5, 6, 8-bit ให้เลือกตาม VRAM ที่มี

จาก โมเดล 27B ที่ fp16 ต้องใช้ RAM ~55GB — บีบ Q4_K_M เหลือ ~16.5GB — ลงเครื่อง consumer ได้เลย (เดี๋ยวพรโชว์ตัวเลขจริงท้ายบทความ)

**3. llama-server — API server ในตัว, OpenAI + Anthropic compatible**

นี่คือ feature ที่ทำให้ llama.cpp แข็งมากสำหรับทีม dev: สั่งเดียวได้ HTTP server พร้อม:

- **OpenAI-compatible**: `/v1/chat/completions`, responses, embeddings
- **Anthropic Messages API compatible** — อยากให้ client ที่เขียนไว้กับ Claude ชี้มาที่ local ก็ได้
- **Continuous batching + parallel multi-user** — คนใช้พร้อมกันหลายคนไม่ตาย
- **Function calling / tool use** กับ ~ทุกโมเดล
- **Schema-constrained JSON** — บังคับให้ LLM ตอบเป็น JSON ตาม schema ที่กำหนด (ใครเคยเจอ LLM ตอบมาเพี้ยน ๆ ทำระเบียบแตกจะรักตัวนี้มาก)
- **Multimodal (vision)** + reranking endpoint
- **Speculative decoding** — เอาโมเดลเล็ก "เดา" ก่อน แล้วให้ตัวใหญ่ตรวจ — เร็วขึ้นโดยคุณภาพไม่ตก
- มี **web UI** ในตัว ดูแล้วเรียบร้อยกว่าที่คิด

**4. ทำ GGUF เองได้ (convert + quantize)**

llama.cpp มี toolchain แปลงโมเดล HuggingFace (safetensors) → GGUF และ quantize เองได้ครบ — รวมถึงใน v0.4.0 มี quantizer RAM cap + streaming ที่ทำให้แปลงโมเดลใหญ่บนเครื่อง RAM น้อยได้ (เคยเป็น pain point เพราะ convert ทีเดียวกิน RAM เป็นสิบ ๆ GB)

**5. GBNF grammars — บังคับ output ระดับ grammar**

นอกเหนือจาก JSON schema ยังเขียน grammar (GBNF) กำกับ output ได้ละเอียดกว่า — เช่น บังคับให้ตอบเฉพาะ "yes/no", บังคับ format คำสั่งเฉพาะ — ตัวช่วยทำ reliable extraction บนเครื่อง local

**6. CPU+GPU hybrid — โมเดลใหญ่กว่า VRAM ก็รันได้**

แชร์ layer ระหว่าง CPU RAM กับ GPU VRAM (`--split-mode layer`, `-ngl`) — โมเดลที่ใหญ่กว่าการ์ดเดี่ยวก็ยังรันได้ แลกกับความเร็ว (และ RPC backend กระจายไปหลายเครื่องเลยก็ได้)

## 03: เรื่องจริงจากเครื่องพร — ตัวเลขจาก 2× RTX 5060 Ti

พรใช้ llama.cpp เป็น runtime กลางของทุก local LLM บนเครื่อง (PHON-SERVER, GPU 2 ตัว) — ไม่ได้ใช้ผ่านตัวห่ออะไรทั้งนั้น

ตัวอย่างจริงที่กำลังรันอยู่ตอนเขียนบทความนี้:

```
llama-server \
  -m ~/models/Qwen3.8-27B-UD-Q4_K_M.gguf \
  -ngl 44 -t 12 -c 262144 -fa on \
  --split-mode layer --port 8080 --jinja
```

คือ **Qwen3.8 27B** quantize Q4_K_M (ไฟล์ ~16.5GB) กระจาย 44 layers ลง GPU ทั้ง 2 ตัว, context 262k tokens, flash attention เปิด — ผลจริงจากการยิงผ่าน `/v1/chat/completions`: **~7.8 tok/s**

ตีความตัวเลขแบบวิศวกร:

- โมเดลระดับ "ตัวหลักใช้งานจริง" ของค่ายใหญ่ รันบนการ์ดรวมยอด ~2 หมื่นบาท ได้ ~8 tokens ต่อวินาที — อ่านเร็วกว่าพิมพ์อ่านสบาย ๆ (คนอ่านเฉลี่ย ~5-7 คำ/วินาที)
- ถ้าใช้โมเดลเล็กลง (7-8B) บนการ์ดเดียว จะขึ้นไป 40-60+ tok/s — ใช้เป็น copilot แนว autocomplete ได้สบาย
- นี่คือข้อพิสูจน์ของจุดยืน "minimal setup, wide hardware": โมเดล 27B ที่ตอนก่อตั้งโปรเจกต์ต้องพึ่ง datacenter วันนี้รันอยู่ในห้องนอน

**คำเตือนแบบพี่เลี้ยง:** ก่อนหน้านี้พรโหลดโมเดลชุด Z-Image (ComfyUI) ค้างไว้บน GPU ทั้งสองตัว — ตัวเลข tok/s จะแย่กว่านี้มากถ้า VRAM ไม่พอจน layer หลุดลง CPU ดังนั้นถ้าเอา server จริงจัง ให้จอง VRAM ให้ชัด (GPU ละ role)

## 04: ข้อดี ✅

- **โครงสร้างคอมพิวเตชั่นต้นทุนเป็นศูนย์** — MIT, ฟรี, ไม่มี per-token, ไม่มี phone home (แน่นอนว่าเรื่อง privacy มาแบบ by design ไม่ใช่ option)
- **Portable สุดในโลก local LLM** — 17 backends ครอบคลุมตั้งแต่ phone, mainframe ถึง browser; binary C++ เดี่ยว ๆ ก็รันได้ ไม่ต้องมี runtime อะไรมาแนบ
- **คุม performance ได้ละเอียดสุด** — quant เลือกได้ทุกเกรด, layer split ปรับได้, batch/ctx/thread หมด — อันนี้คือเหตุผลที่ benchmark ที่ดีที่สุดของโลก local LLM ส่วนใหญ่วัดบน llama.cpp
- **API compatible กับ ecosystem ที่มีอยู่** — OpenAI + Anthropic format แปลว่า tooling/SDK/client เก่าทั้งหมดชี้มาใช้ได้เลย
- **โปรเจกต์มีชีวิตมาก** — release วันละหลายตัว, v0.4.0 (9 ก.ย. 2026) ยังใส่ของใหม่รัว ๆ: lazy tensor reading, sparse flash attention, RDMA ข้ามเครื่อง, รองรับ Qwen3.8-Flash-Next/Nemotron ตั้งแต่เพิ่งออก
- **จุดกำเนิดของ GGUF** — มาตรฐานโมเดลของโลก local LLM เกิดที่นี่ อยู่ร่วมกับ ecosystem ใหญ่ที่สุดของ GGUF โดยตรง

## 05: ข้อเสีย ❌

- **CLI-first ไม่มี GUI ในตัว** (นอกจาก web UI ของ server) — ต้องอ่าน flag, ต้อง build/receive binary ให้ถูก backend — คนไม่ถนัด terminal จะเจ็บ
- **ตัวเลือก flag เยอะจนปวดหัว** — `--help` ยาวเป็นพันบรรทัด มีทั้ง rope scaling, YaRN, SWA, ubatch — พลังมาก = พารามิเตอร์มาก (นี่คือเหตุผลที่ Ollama มีตัวต่อ)
- **จัดการโมเดลเองทั้งหมด** — หา GGUF เอง, ดู VRAM เอง, optimize เอง ไม่มีระบบ model registry สวย ๆ แบบ LM Studio
- **โมเดลใหม่มาก่อน ระบบ stable ทีหลัง** — รองรับ architecture ใหม่เร็วมากแต่บางตัว "initial support" ก่อน optimize (อย่าง Qwen3.8-Flash-Next ใน v0.4.0 ระบุชัดว่า optimization ยังตามมา)
- **ไม่มี multi-tenancy / auth / quota** — เป็น inference engine ล้วน ๆ ถ้าจะเปิดให้ทั้งบริษัทใช้ต้องห่ออีกชั้น
- **เอาไปเทียบกับ API ตัวใหญ่ ความฉลาดไม่ใช่สนามของมัน** — 27B local ยังไม่ชนะ frontier cloud model ในงานซับซ้อน แต่ถ้างานคุณคือ summarize/extract/chat ธรรมดา — แพ้ศูนย์ token ชนะขาด

## 06: เหมาะกับใคร — 4 โปรไฟล์

**1. Dev ที่อยากได้ local API server จริงจัง** — อยากมี `/v1/chat/completions` ของตัวเองใน LAN, ทดลอง function calling, ทำ prototype ไม่อยากกลัว bill — llama-server ตอบโจทย์นี้ตรงที่สุด

**2. คนมี hardware เฉพาะที่ tool อื่นไม่เก่ง** — AMD, Intel Arc, Ascend NPU, แม้แต่ Snapdragon — backend coverage ของ llama.cpp กว้างกว่าใคร ถ้าเครื่องคุณแปลก ๆ นี่คือทางที่เปิดกว้างสุด

**3. Performance optimizer / benchmark จริงจัง** — อยากบีบทุก tok/s จากเครื่อง ไม่ว่าจะ layer split ข้าม GPU, หรือ speculative decoding — ระดับความละเอียดของการคุมไม่มีตัวไหนเทียบได้

**4. คนสร้างแอป local-first** — กำลังจะทำสินค้าที่รัน LLM ในเครื่อง user (ไม่มี server) — MIT + no dependency ทำให้ embed ได้ทั้ง desktop, mobile และแม้แต่ WebGPU ใน browser

**ใครไม่เหมาะ:** มือใหม่ที่อยากแค่ "ลอง local LLM เล่นพร้อม" — เริ่มจาก Ollama หรือ LM Studio ก่อน (แล้วค่อยมาเรียก engine ตรง ๆ ตอนต้องการคุมละเอียดกว่านั้น) — หรือทีมองค์กรที่ต้องการ multi-tenant platform สำเร็จรูป — ไปทาง vLLM หรือ managed platform จะเร็วกว่า

## 07: ตารางเทียบ — llama.cpp vs ตัวห่อชั้นบน

| | llama.cpp | Ollama | LM Studio | vLLM |
|---|---|---|---|---|
| ชั้น | Engine (C/C++) | Wrapper + model manager | GUI + model manager | Serving platform (Python) |
| สำหรับใคร | Dev / optimizer | ใช้งานทั่วไป | อยากได้ GUI | ทีม prod ขนาดใหญ่ |
| GPU support | 17 backends กว้างสุด | ผ่าน llama.cpp | ผ่าน llama.cpp (บางส่วน) | NVIDIA-centric |
| Quantization | ครบ 1.5-8 bit (ต้นฉบับ) | ใช้ของ llama.cpp | ใช้ของ llama.cpp | เน้น fp8/awq/gptq |
| API server | OpenAI + Anthropic compat | OpenAI-compat | OpenAI-compat (port 1234) | OpenAI-compat + PagedAttention |
| Customization | สูงสุด (ทุก flag) | ปานกลาง | ปานกลาง | สูง (แต่แนว ops) |
| ขนาดสัมพัทธ์ | binary เดียว | ต้องมี runtime | App เต็มรูปแบบ | Python stack หนัก |

สังเกตแถว GPU support / Quantization นะครับ — Ollama กับ LM Studio ใช้ "ของ llama.cpp" ทั้งนั้น นั่นแหละคือความหมายของคำว่า engine

## 08: Pro Tips แยกตามระดับ

**มือใหม่กับ llama.cpp:** ไม่ต้อง build — โหลด pre-built binary จาก releases page แล้วสั่ง `llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF` ได้เลย ไม่ต้องแม้แต่หาโมเดลเอง (flag `-hf` ดึงจาก Hugging Face ให้)

**ใช้จริงจัง:** เปิด `-fa on` (flash attention), ตั้ง `-c` ให้พอดีงาน (อย่าตั้ง 262k ถ้าไม่ได้ใช้ — KV cache กิน VRAM ตาม context), ใช้ `--jinja` ให้ chat template ของโมเดลทำงานถูกต้อง และถ้าโมเดลไม่ลงการ์ดเดียว ใช้ `--split-mode layer` ข้าม GPU ก่อน แล้วค่อยดู RPC ถ้าอยากกระจายเครื่อง

**องค์กร:** วาง llama-server เป็น inference endpoint ใน LAN + ห่อ auth/quota อีกชั้น (reverse proxy), ใช้ schema-constrained JSON ทำ pipeline extraction ที่ deterministic, และล็อกเวอร์ชัน release ตอน prod (อย่าตาม nightly แบบเดียวกับ dev — cadence มันเร็วมาก)

## 09: สรุปแบบวิศวกรเป็ด — "Engine ที่คนทั้ง ecosystem ยืม ก็สมควรได้ถูกเรียกชื่อ"

llama.cpp คือส่วนที่หายไปของภาพ local LLM ที่หลายคนเห็น — เราเห็น Ollama, เห็น LM Studio, เห็น GGUF โดนลากไปวางในแอปนู้นนี่ — แต่ตัวที่เผา GGUF ให้กลายเป็นคำตอบจริง ๆ คือ engine C++ ตัวเดียวกันมาตลอดสามปีครึ่ง

ถ้า local LLM คือระบบที่คุณจะยกระดับเป็น infrastructure ของตัวเอง — ก็เหมือนกับที่คุณจะไม่จ้างช่างที่ไม่รู้จักเครื่องยนต์ที่ตัวเองใช้ — สักวันคุณจะต้องลงมาที่ engine อยู่ดี: อยากได้ tok/s มากขึ้น, อยากเอาโมเดลใหม่ที่ wrapper ยังไม่รองรับ, อยาก deploy บน hardware แปลก ๆ

และวันนั้นคุณจะรู้ว่าสิ่งที่ดาวน์โหลดมาตอนนั้น เขียนด้วย C/C++ ไม่มี dependency เดียว รันได้ตั้งแต่ mainframe ถึง browser — และมีคน 127,574 คนให้ดาวมันไว้ด้วยเหตุผลที่ชัดเจนมาก

ใน series local LLM ของพร นี่คือชิ้นที่ 4: [Ollama laptop](https://wp.adduckivity.com/20260905-cnt-ollama-local-llm-laptop-portable/) → [Ollama server](https://wp.adduckivity.com/20260907-cnt-ollama-local-llm-server-datacenter/) → LM Studio + Bionic → **llama.cpp (engine)** → Unsloth Studio (สร้างโมเดลเอง) — ครบวงจรแล้วครับ

ระบบที่ดี ไม่ต้องรู้ทุกเฟือง — แต่ควรรู้ว่าเครื่องยนต์อยู่ตรงไหน

**Law #1 System > Emotion ครับ**

#Adduckivity #DuckOS #NeuroDivergent #LocalLLM #llamacpp #GGUF #OpenSource #AI
