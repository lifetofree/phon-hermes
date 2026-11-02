Title: 27B ที่เคยต้องพึ่ง datacenter วันนี้รันในห้องนอนด้วยการ์ด 2 หมื่นบาท — ~8 tok/s (llama.cpp — Wrapper vs Engine)
Date: 2026-09-20
Link: (social version — user-pasted 2026-09-20; not yet in WP archive at analysis time)
Provenance: published edit of draft posts/20260909-cnt-llama-cpp-engine-intro.md (ContentID 20260909-CNT-LLAMACPP-LF). Archived for STYLE_CORPUS draft→publish analysis.

---

**27B ที่เคยต้องพึ่ง datacenter วันนี้รันในห้องนอนด้วยการ์ด 2 หมื่นบาท — ~8 tok/s**

.

**คุณกำลังใช้ llama.cpp อยู่**

แม้ไม่เคยพิมพ์ชื่อมันเลยก็ตาม

ถ้าเคยรัน Ollama บน laptop

เคยเปิด LM Studio คุยกับโมเดลในเครื่อง

หรือเคยลาก GGUF ไปวางในแอปใด ๆ

โอกาสสูงมากว่า engine ที่อยู่ข้างใต้คือ **llama.cpp**

มันคือ inference engine ที่อยู่ใต้ ecosystem ของ local LLM จำนวนมาก

เขียนด้วย C/C++

รันได้ตั้งแต่ CPU, Apple Silicon, GPU หลายค่าย ไปจนถึง hardware ที่เฉพาะทางมากขึ้น

และจุดสำคัญไม่ใช่แค่ว่า

.

> "llama.cpp ทำอะไรได้บ้าง?"

.

แต่คือ

.

> **"เมื่อไหร่เราควรเลิกใช้ Wrapper แล้วลงมาเรียก engine เอง?"**

.

เพราะถ้าแค่ต้องการรัน LLM ในเครื่อง

**Ollama หรือ LM Studio อาจพอแล้ว**

ไม่จำเป็นต้องลงมาแตะ llama.cpp

แต่ถ้าวันหนึ่งคุณเริ่มต้องการควบคุมสิ่งที่ Wrapper ตั้งใจซ่อนจากคุณ

ตรงนั้นเรื่องจะเปลี่ยน

.

# llama.cpp คืออะไร — Engine ไม่ใช่รถ

ถ้าเปรียบ local LLM เป็นรถ:

**GGUF** = น้ำมัน

**Ollama / LM Studio / Bionic** = รถสำเร็จรูป

มีหน้าปัด มีระบบจัดการ ขับง่าย

**llama.cpp** = เครื่องยนต์

มันคือส่วนที่เอา model file อย่าง GGUF ไปทำ inference แล้วสร้าง tokens ออกมา

เพราะฉะนั้นเวลาคุณใช้ Wrapper

ไม่ได้แปลว่าคุณกำลังใช้คนละโลกกับ llama.cpp

หลายครั้งคุณกำลังใช้ **llama.cpp ผ่านชั้น abstraction ที่ใช้ง่ายกว่า**

นี่คือเหตุผลที่ควรมองมันเป็นคนละ layer

ไม่ใช่คู่แข่งแบบ

— Ollama vs llama.cpp

— LM Studio vs llama.cpp

แต่เป็นประมาณว่า

**— รถ vs เครื่องยนต์**

รถมีไว้ให้ขับ

เครื่องยนต์มีไว้ให้ควบคุมกลไกข้างใน

.

.

# แล้วถ้า Wrapper ใช้งานได้อยู่ ทำไมต้องลงมา?

คำตอบสั้น ๆ คือ

**ไม่ต้อง**

ถ้า Ollama หรือ LM Studio ทำสิ่งที่คุณต้องการได้

ใช้ต่อไป

เพราะ Wrapper มีประโยชน์ตรงนี้พอดี

มันเอาความซับซ้อนของ inference engine ออกไปจากคุณ

ไม่ต้องรู้ว่า:

— layer ไหนอยู่ GPU

— context กิน VRAM เท่าไร

— backend ไหนกำลังทำงาน

— quantization แบบไหนเหมาะกับเครื่อง

— batch ตั้งเท่าไร

— server เปิดด้วย flag อะไร

— hardware แต่ละตัวต้อง optimize ยังไง

คุณแค่โหลดโมเดลแล้วใช้งาน

**และนั่นเป็นเรื่องดี**

ปัญหาเริ่มเกิดเมื่อคุณต้องการคำตอบที่ Wrapper ไม่ได้ออกแบบมาให้คุณควบคุม

เช่น

— "ทำไมมันช้า?"

— "ทำไมโมเดลนี้ลง GPU ไม่หมด?"

— "ผมมี GPU สองใบ จะกระจาย layer ยังไง?"

— "Hardware นี้ทำไมรองรับไม่เต็ม?"

— "ผมอยากทำ inference server เอง"

— "ผมอยากบังคับ output ให้เป็น schema"

— "ผมอยากบีบ performance ทุก tok/s ที่เครื่องมี"

ตรงนี้คุณไม่ได้แค่ **ใช้ LLM**

คุณกำลังเริ่มทำ **inference engineering**

และนี่คือจุดที่ llama.cpp เริ่มมีความหมาย

.

.

# 5 สัญญาณว่า Wrapper เริ่มไม่พอ

## 1. คุณเริ่มสนใจ Performance มากกว่าแค่ "รันได้"

ตอนแรกคำถามคือ

— "โมเดลนี้รันได้ไหม?"

พอเริ่มจริงจัง คำถามจะกลายเป็น

— "ทำยังไงให้มันเร็วขึ้น?"

ตรงนี้ llama.cpp ให้คุณลงไปควบคุมรายละเอียดของ inference ได้มากขึ้น

ตั้งแต่

— threads

— batch

— context

— Flash Attention

— quantization

— GPU offload

— layer split

— speculative decoding

เพราะ performance ของ local LLM ไม่ได้ขึ้นกับแค่ "โมเดลเก่งแค่ไหน"

มันขึ้นกับว่า

**โมเดล + quantization + memory + hardware + runtime**

ทำงานเข้ากันอย่างไร

ถ้าคุณไม่สนใจเรื่องพวกนี้

ไม่ต้องลงมา

แต่ถ้าคุณเริ่ม benchmark เครื่องตัวเองจริงจัง

Wrapper อาจเริ่มกลายเป็น abstraction ที่คุณอยากเปิดออก

.

# 2. โมเดลใหญ่กว่า VRAM ที่คุณมี

นี่เป็นอีกจุดที่เห็นภาพชัดมาก

สมมติคุณมี GPU ใบเดียว

แต่โมเดลที่อยากรันใหญ่เกินกว่าจะยัดลงไปทั้งหมด

ทางเลือกไม่ได้มีแค่

— "ซื้อ GPU ใหม่"

คุณสามารถใช้ quantization เพื่อลดขนาดโมเดล

หรือกระจาย layer ระหว่าง GPU กับ CPU RAM

หรือกระจายข้าม GPU หลายใบ

llama.cpp รองรับการควบคุมพวกนี้ในระดับ runtime เช่น `-ngl` และ `--split-mode layer`

ตรงนี้เองที่ engine-level control เริ่มมีประโยชน์

เพราะปัญหาของคุณไม่ใช่

— "จะใช้ local LLM ยังไง?"

แต่เป็น

**— "จะเอาโมเดลนี้ลงบน hardware ที่ผมมีได้ยังไง?"**

สองคำถามนี้คนละเรื่องกัน

.

.

# 3. คุณมี Hardware ที่ไม่ใช่ Happy Path

ถ้าคุณใช้ NVIDIA GPU เครื่องเดียว

ชีวิตง่าย

แต่ local inference ไม่ได้มีแค่ NVIDIA

llama.cpp มี backend สำหรับ hardware หลายกลุ่ม เช่น CUDA, HIP, Metal, SYCL, Vulkan รวมถึง backend เฉพาะทางอื่น ๆ ตาม ecosystem ที่โปรเจกต์รองรับ

ข้อดีตรงนี้ไม่ใช่

— "17 backend = ดีกว่าเสมอ"

แต่คือ

**engine เดียวสามารถถูกนำไปปรับใช้กับ hardware หลายประเภท**

สำหรับคนทั่วไป เรื่องนี้อาจไม่สำคัญ

แต่ถ้าคุณมี

— AMD

— Intel

— Apple Silicon

— edge device

— accelerator เฉพาะทาง

— hardware ที่ Wrapper ที่คุณใช้รองรับไม่เต็ม

คำถามจะเปลี่ยนจาก

— "แอปนี้รองรับไหม?"

เป็น

**— "engine นี้ทำอะไรกับ hardware ตัวนี้ได้บ้าง?"**

นี่คือระดับที่ llama.cpp เริ่มมีประโยชน์จริง

.

.

# 4. คุณไม่ได้อยาก "ใช้ LLM" แล้ว แต่อยาก "เอา LLM ไปเป็นส่วนหนึ่งของระบบ"

นี่เป็นเส้นแบ่งอีกจุด

ถ้าคุณเปิด chatbot เล่นในเครื่อง

GUI หรือ Wrapper ดีมาก

แต่ถ้าคุณกำลังสร้าง application

คุณอาจต้องการ endpoint ของตัวเอง เช่น

`/v1/chat/completions`

หรือ endpoint สำหรับ embeddings

หรือ function calling

หรือ structured output

ตรงนี้ `llama-server` เข้ามามีบทบาท

มันสามารถเปิด HTTP server สำหรับ inference และรองรับรูปแบบ API ที่เข้ากับ ecosystem อย่าง OpenAI-compatible และ Anthropic Messages API ได้

รวมถึงความสามารถอย่าง

— continuous batching

— parallel requests

— function calling

— schema-constrained JSON

— multimodal

— speculative decoding

และ web UI ก็มีมาให้ด้วย

จุดสำคัญคือ

**คุณไม่ได้เปิด llama.cpp เพราะอยากได้ chatbot อีกตัว**

คุณเปิดมันเพราะต้องการให้ inference engine กลายเป็น **ส่วนหนึ่งของระบบของคุณ**

.

.

# 5. คุณต้องการควบคุม Output มากกว่า Prompt

LLM มีปัญหาอย่างหนึ่ง

เราบอกมันว่า

— "ตอบเป็น JSON"

มันก็อาจตอบเป็น JSON

หรืออาจตอบว่า

— "Sure! Here is your JSON:"

ถ้าคุณกำลังทำระบบจริง

สิ่งนี้เริ่มไม่ตลก

llama.cpp มีทั้ง schema-constrained JSON และ GBNF grammar สำหรับควบคุมรูปแบบ output ในระดับที่ละเอียดขึ้น

เช่น

ต้องการให้ output เป็น schema เฉพาะ

หรือบังคับ grammar

หรือจำกัดรูปแบบคำตอบ

ตรงนี้ไม่ใช่เรื่อง

— "อยากเล่นของ"

แต่เป็นเรื่อง

**— "output ของ model ต้องกลายเป็น input ของระบบถัดไป"**

เมื่อถึงจุดนี้ inference control มีความหมายมากขึ้น

.

.

# Quantization — จุดที่ Hardware กับ Model เริ่มคุยกัน

หนึ่งในเหตุผลที่ local LLM โตขึ้นมากคือ quantization

พูดง่าย ๆ คือ

เอา model ที่ใหญ่ไปเกิน

มาลด precision ลง

เพื่อแลกขนาดและ memory footprint กับความแม่นยำบางส่วน

ตัวอย่างง่าย ๆ:

27B ที่ fp16 อาจต้องใช้หน่วยความจำระดับหลายสิบ GB

แต่เมื่อ quantize เป็น Q4_K_M

ขนาดไฟล์สามารถลดลงมาอยู่ราว 16.5GB ตามตัวอย่างในบทความนี้

ผลคือ

โมเดลที่ก่อนหน้านี้ต้องการ hardware ใหญ่

เริ่มเข้ามาอยู่บน consumer hardware ได้

และนี่คือสิ่งที่ทำให้คำว่า

**— local inference**

มีความหมายมากขึ้นเรื่อย ๆ

แต่ถ้าคุณแค่โหลด GGUF มาใช้

คุณไม่จำเป็นต้องเข้าใจ quantization ลึก

จนกว่าจะถึงวันที่คุณถามว่า

— ทำไม Q4 ตัวนี้ถึงพอดีกับเครื่องผม แต่ Q5 ไม่พอดี?"

วันนั้นคุณกำลังเริ่มเข้าใกล้ engine

.

.

# สิ่งที่ llama.cpp ทำได้จริง

ถ้าตัดเรื่อง decision ออกมาเป็น capability

llama.cpp มีพื้นที่ให้ควบคุมหลายชั้น

### Hardware

รองรับ backend หลายแบบ

ตั้งแต่ CUDA, HIP, Metal, SYCL, Vulkan และอื่น ๆ

### Model size

มี quantization หลายระดับ

เพื่อให้ model ใหญ่ขึ้นสามารถลง hardware ขนาดเล็กลงได้

### Memory

สามารถ offload และ split layer ระหว่าง hardware ได้

รวมถึง CPU + GPU hybrid

### Serving

มี `llama-server`

สำหรับเปิด inference endpoint ของตัวเอง

### Output

มี JSON schema และ GBNF grammar

สำหรับงานที่ต้องการ output ที่ควบคุมได้

### Optimization

คุณสามารถลงไปปรับ runtime parameters ได้ละเอียดกว่า abstraction layer ที่ออกแบบมาเพื่อความง่าย

และนี่คือประเด็นสำคัญ:

**ความสามารถพวกนี้ไม่ได้แปลว่าทุกคนควรใช้**

มันแปลว่า

**เมื่อคุณต้องการควบคุมสิ่งเหล่านี้ คุณมีทางลงมา**

.

.

# แล้วมันต่างจาก Ollama / LM Studio ยังไง?

ให้คิดเป็น layer

|  | llama.cpp | Ollama | LM Studio | vLLM |
| --- | --- | --- | --- | --- |
| ชั้น | Engine | Wrapper + model manager | GUI + model manager | Serving platform |
| จุดเด่น | Control | Simplicity | GUI / usability | Production serving |
| เหมาะกับ | Dev / optimizer | ใช้งานทั่วไป | คนที่อยากได้ GUI | ทีมที่ต้องการ serving stack |
| Customization | สูง | ปานกลาง | ปานกลาง | สูงในแนว serving |
| Model management | ต้องจัดการเองมากกว่า | มีให้ | มีให้ | คนละโจทย์ |
| API | มี server ในตัว | มี API | มี API | มี serving API |

ในบทความเดิม จุดที่น่าสนใจคือ Ollama และ LM Studio สามารถใช้ llama.cpp อยู่ข้างใต้ในบางกรณี

นั่นทำให้เห็นภาพว่า

**Wrapper ไม่ได้แทนที่ Engine**

มันทำหน้าที่อีกชั้นหนึ่ง

ดังนั้นอย่าถามว่า

— "อันไหนดีกว่า?"

ให้ถามว่า

**— "ตอนนี้ผมต้องการ abstraction หรือ control?"**

.

.

# ถ้าแค่ใช้งาน — อย่าลงมา

ถ้าคุณต้องการแค่

— โหลดโมเดล

— คุยกับ LLM

— ทำ coding assistant

— ทดลอง local AI

— เปิด API ง่าย ๆ

— ใช้ GUI จัดการโมเดล

**อยู่บน Wrapper ต่อไป**

คุณไม่ได้พลาดอะไร

เพราะ abstraction มีไว้ลด cognitive load

และถ้า abstraction ยังตอบโจทย์

ไม่มีเหตุผลต้องเปิด complexity เพิ่ม

.

.

# ถ้าคุณเริ่มต้อง "ควบคุม" — ค่อยลงมา

แต่ถ้าคุณเริ่มต้อง

— บีบ performance

— จัดการ VRAM

— split model ข้าม GPU

— รองรับ hardware เฉพาะ

— ทำ inference server

— embed inference เข้า product

— บังคับ output format

— benchmark runtime

— quantize model เอง

**นี่คือจุดที่ควรเริ่มรู้จัก llama.cpp โดยตรง**

ไม่ใช่เพราะ llama.cpp "ดีกว่า" Wrapper

แต่เพราะ

**— คุณกำลังต้องการสิ่งที่ Wrapper ตั้งใจซ่อนจากคุณ**

.

.

# ทดสอบจากเครื่องจริง — 2× RTX 5060 Ti

ทีนี้มาดูว่าความต่างนี้หน้าตาเป็นอย่างไรในโลกจริง

เครื่องของพรใช้ llama.cpp เป็น runtime กลางของ local LLM

ไม่ได้ผ่าน Wrapper

ตัวอย่างที่กำลังรัน:

```bash
llama-server \
  -m ~/models/Qwen3.8-27B-UD-Q4_K_M.gguf \
  -ngl 44 -t 12 -c 262144 -fa on \
  --split-mode layer --port 8080 --jinja
```

โมเดลคือ

**Qwen3.8 27B**

quantize แบบ **Q4_K_M**

ไฟล์ประมาณ **16.5GB**

กระจาย 44 layers ลง GPU ทั้งสองใบ

เปิด Flash Attention

และตั้ง context 262k tokens

ผลจากการยิงผ่าน `/v1/chat/completions`

**ประมาณ 7.8 tok/s**

ตัวเลขนี้ไม่ได้มีไว้เพื่อบอกว่า

— "ทุกคนควรซื้อ GPU สองใบ"

มันมีไว้แสดงให้เห็นว่า

**เมื่อคุณลงมาอยู่ระดับ engine คุณสามารถควบคุมวิธีที่ model ใช้ hardware ได้ละเอียดขึ้น**

ในกรณีนี้ model ใหญ่เกินกว่าจะมองเป็นแค่

— "กดโหลดแล้วใช้งาน"

มันกลายเป็นปัญหาเรื่อง

**model + quantization + memory + GPU topology + runtime**

และนี่แหละคือเหตุผลที่ engine-level control มีประโยชน์

หมายเหตุ: ตัวเลข benchmark นี้เป็นผลจากเครื่องและ configuration ณ เวลาที่เขียน ไม่ควรนำไปเทียบตรง ๆ กับเครื่องอื่นโดยไม่ควบคุมเงื่อนไขเดียวกัน

.

# แต่ llama.cpp ก็ไม่ได้เหมาะกับทุกคน

ตรงนี้สำคัญ

เพราะถ้าเราพูดแต่ข้อดี

บทความจะกลายเป็นการเชียร์ technology

ซึ่งไม่ใช่ประเด็น

## ข้อเสียจริง ๆ

**CLI-first**

คุณต้องอยู่กับ terminal และ flags

ไม่ได้มี UX แบบ LM Studio

**ตัวเลือกเยอะ**

- `-help` มี parameter จำนวนมาก

พลังมากขึ้น

ก็แปลว่าต้องตัดสินใจมากขึ้น

**จัดการ model เองมากขึ้น**

ต้องรู้ว่า GGUF ตัวไหนเหมาะกับ hardware

ต้องดู VRAM

ต้องเข้าใจ configuration

**ไม่ได้เป็น platform สำเร็จรูป**

ตัว engine ไม่ได้ถูกออกแบบมาเพื่อแก้เรื่อง

— authentication

— quota

— multi-tenancy

— user management

ถ้าจะเอาไปทำระบบใหญ่

คุณยังต้องประกอบ layer อื่นเพิ่ม

ดังนั้นถ้าคุณกำลังมองหา

— "เปิดโปรแกรมแล้วใช้ได้เลย"

llama.cpp อาจไม่ใช่สิ่งที่คุณต้องการ

.

.

# ใครควรลงมาใช้ llama.cpp เอง?

### 1. Developer ที่ต้องการ Local API จริงจัง

ต้องการ inference endpoint ของตัวเอง

ต้องการควบคุม runtime

ต้องการเอา local model ไปต่อกับ application

.

### 2. คนที่มี Hardware เฉพาะ

เครื่องไม่ได้อยู่ใน happy path ของ Wrapper

หรือคุณต้องการควบคุม backend เอง

.

### 3. คนที่ Performance เป็น Requirement

ไม่ได้ถามแค่ว่า

— "รันได้ไหม?"

แต่ถามว่า

— "ทำยังไงให้ hardware ตัวนี้รีด performance ได้มากที่สุด?"

.

### 4. คนสร้าง Local-first Application

ถ้าคุณกำลังสร้าง product ที่ต้องให้ LLM ทำงานอยู่บนเครื่องของ user

engine-level control เริ่มมีความหมาย

โดยเฉพาะเรื่อง binary, backend, memory และ deployment

.

.

# ใครยังไม่ควรลงมา?

มือใหม่ที่แค่อยากลอง local LLM

คนที่ต้องการ GUI

คนที่ไม่อยากจัดการ model เอง

คนที่ไม่ได้มีปัญหาเรื่อง performance

คนที่ไม่ได้ต้องการควบคุม hardware

ถ้าคุณอยู่ตรงนี้

**ใช้ Ollama หรือ LM Studio ต่อไป**

ไม่มีอะไรต้องพิสูจน์

.

.

# Pro Tips ตามระดับ

## ถ้ายังใหม่

ไม่ต้อง build เอง

ใช้ pre-built binary ได้

และสามารถสั่งให้ `-hf` ดึง model จาก Hugging Face ได้โดยตรง

เป้าหมายตอนนี้ไม่ใช่เรียนทุก flag

แค่ให้เข้าใจว่า

**— คุณกำลังลงมาอีกหนึ่ง layer**

.

## ถ้าเริ่มใช้จริงจัง

ค่อยเริ่มเข้าใจสิ่งที่มีผลกับ performance จริง

เช่น

- `fa`

context

GPU offload

- `-split-mode layer`

และ chat template อย่าง `--jinja`

แต่ไม่ต้องเปิดทุก flag เพราะแค่ "เปิดได้" ไม่ได้แปลว่า "ควรเปิด"

configuration ที่ดีต้องสัมพันธ์กับ workload และ hardware ของคุณ

.

## ถ้าจะเอาไปใช้เป็นระบบ

อย่าลืมว่า

**llama.cpp คือ inference engine**

ไม่ใช่ระบบ production ทั้งหมด

ถ้าต้องการ auth

quota

multi-tenancy

monitoring

access control

คุณยังต้องวาง layer เหล่านั้นเอง

อย่าเอา engine ไปแบกงานที่ engine ไม่ได้ถูกออกแบบมาให้แบก

.

.

# #สรุปแบบวิศวกรเป็ด

llama.cpp ไม่ได้มีไว้แทน Ollama

ไม่ได้มีไว้แทน LM Studio

และไม่ได้แปลว่า

— "ถ้า serious ต้องใช้ llama.cpp"

คำถามที่ถูกกว่าคือ

**— "ตอนนี้ผมต้องการความง่าย หรือผมต้องการการควบคุม?"**

ถ้าต้องการความง่าย

ใช้ Wrapper

ถ้าต้องการควบคุม

ลงมา Engine

.

ระบบที่ดี

ไม่จำเป็นต้องรู้ทุกเฟือง

แต่ถ้าวันหนึ่งคุณต้องควบคุมเครื่องยนต์

ก็ควรรู้ว่า

**เครื่องยนต์อยู่ตรงไหน**

และ llama.cpp คือหนึ่งในจุดนั้นของ local LLM ecosystem

**ไม่ใช่เพราะทุกคนต้องลงมาใช้**

แต่เพราะบางวัน

ปัญหาที่คุณกำลังแก้

อาจไม่ใช่เรื่อง "ใช้ LLM ยังไง" อีกแล้ว

มันอาจกลายเป็น

**— "จะทำให้ LLM ตัวนี้ทำงานบน hardware นี้ด้วยวิธีที่เราต้องการได้ยังไง?"**

และนั่นคือวันที่ควรเปิดฝากระโปรง

.

**Law #1 System > Emotion คับ**

.

#Adduckivity #DuckOS #NeuroDivergent #LocalLLM #llamacpp #GGUF #OpenSource #AI
