<!--
pair #76 v1 — TECH post (v2 form) — fresh draft from news brief (2026-10-30)
Brief (owner): TechCrunch 2026-10-29 "Mistral opens the weights of its trillion-parameter Le Chonk model" — https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/
Primary sources verified 2026-10-30:
- mistral.ai/news/mistral-large-4-oss/ (primary announcement, Oct 29): weights released; 1T MoE; FrontierCode 2.0 lead 19.7%; AA Coding Agent Index 48% "effectively tied with GLM-5.3, while using 47% fewer tokens per task on average"; Terminal-Bench 4.0 28%→41% (+13pts, output tokens -30%); AA Cyber Index 51% (top of chart vs GLM-5.3 57%? — chart shows ML4 51%, GLM-5.3 57%, DeepSeek 57%...); refusal on malicious cyber 96.6% "highest we measure among open models"; license = Mistral Ecosystem Open-Weight License (modified MIT — MaaS ต้องขอ commercial license แยก); API price $0.70 in / $0.07 cached / $2.10 out per M; 3 reasoning modes (Low/Medium/High default); trained on 3,800 Grace Blackwell in own EU datacenters; €3B Series D
- HF mistralai/Mistral-Large-4-1T-A52B (LICENSE + README raw, 2026-10-30): license text verified verbatim ("modified version of the MIT license" + MaaS clause #2); README: 1T total / ~52B active (128 routed experts, 4 active/token + 1 shared), 1M context, Pixtral-style vision, 160+ languages, DSpark speculative head embedded, NVFP4 quantized checkpoint available; repo tree = 54 safetensors shards ~20GB each = 1,060GB (1TB+ BF16)
- TechCrunch (secondary, Lucas Ropek 2026-10-29): nickname Le Chonk; quotes Mensch "empowerment, not dominance"; Pierre Stock (VP Science): access "can't be cut off by definition"; MaaS-clause context; VentureBeat via aiweekly flags factual accuracy 26% (below several rivals) — จดไว้เป็น anti-hype footnote ไม่ใส่บท (เชื่อมั่นแหล่งรองแบบเดียวไม่พอ — ถ้าไม่ verify ต่อห้ามอ้าง)
Evidence classes: ผู้ผลิตอ้างเอง (benchmarks, 47%, refusal 96.6%) ≠ independent (AA index = third-party benchmark ที่ Mistral อ้าง) ≠ ไม่ได้ทดสอบเอง — ทุกตัวเลขในบทติด label "Mistral อ้าง/จากการวัดของ Artificial Analysis"
Spine (TECH v2): stat-line (1TB ที่เคยเป็นของห้องแถวโมเดลปิด ตอนนี้โหลดได้ 54 ไฟล์) → hook (เปิดไม่ใช่แค่ "ฟรี" — คือซื้ออิสระจากจุดเดียวของ fail) → คำถามแท้ (หน่วยงานที่เก็บข้อมูลอ่อนไหว ควรยกโมเดล 1TB มาอยู่ในบ้านจริงไหม หรือ API ก็พอ?) → ML4 คืออะไร + ตารางสเปก → ทำไมตลาด cyber ถึงเป็นเป้า (provider-refusal mid-incident = ความเสี่ยงที่โมเดลปิดมีแต่ไม่มีใครพูด) → ตารางเทียบ GLM-5.3/ตัวเปิดอื่น → Anti-Hype (ตัวเลขผู้ผลิตอ้าง + MaaS clause + 26% ข่าวรอง ยังไม่ verify — ไม่อ้าง / 1TB เต็มคืองานบ้านคุมไม่ทำนองเศรษฐี) → ฟอร์กใครควรลอง/ไม่ควร (two-fork) → สรุปวิศวกรเป็ด (v2 TECH closer = bold definitions + true question re-ask + one-liner problem + bold pair)
Register: TECH = พรใช้ได้ (persona review voice) / คุณ ≥0 ตาม form / ตัวเลขเป๊ะทุกตัว (WP form) / '?' เฉพาะคำถามแท้ + closer | LAYOUT-CHANGE (owner 2026-10-30: "ปรับจากตารางได้ไหม เพราะใส่บน facebook ไม่ได้ — แก้ใน draft เดิม"): ตาราง 2 ตัว collapse เป็น flat `- ` bullet list ตาม FB MICRO-derivative form (skill line 191) — ข้อมูลครบทุก cell ย้ายเป็น bullet เดี่ยว, header note เดิมคงไว้
Guards/CUT (declared): #45 Snapzy TECH sibling: ราคา-tier-ตัด/first-look-vs-hands-on gate = First Look (ไม่มีประสบการณ์ใช้จริง — ห้ามใช้ experience verbs: ลองแล้ว/ใช้มา = 0) | #22 wispr-notetaker: notetaker/ประชุม = 0 | #76-กิ่งอื่น: ไม่มี | เทรดข่าว AI: "แข่งกันแหลก/hallyu/hype" เทศนา = 0 | โครง CURRENT FORM (story/dispatch-2modes) ห้ามหลุดมา — TECH ใช้ stat-line/table/benchmark/fork | Le Chonk = ชื่อจริงที่ Mistral ตั้ง (quote-safe) | แหล่งรองอื่น (unite.ai/aiweekly/daily.dev/thenewstack) = research-only ไม่ quote
Do-not-build (item 291): ห้ามสอนวิธี self-host ละเอียด / สูตรคำนวณค่า GPU / benchmark ที่ verify ไม่ได้ — ลิงก์ model card พอ
Honesty: ทุก benchmark = ตัวเลขที่ Mistral ยกมาเองหรือจาก AA (third-party ที่ Mistral อ้าง) — บทนี้ไม่ได้รันโมเดล; เลข 26% factual จาก VentureBeat ยังไม่ verify ต้นทาง → ไม่ใส่บท
Candidate hooks: (1) โมเดลล้านล้านพารามิเตอร์ น้ำหนัก 1TB — โหลดมาเป็นของตัวเองได้แล้ว (2) 47% ตัวเลขเดียวที่ทำให้ GLM-5.3 เริ่มมีคู่แท้ (3) เปิด weights ไม่ใช่ใจดี — มันคือข้อเสนอซื้ออิสระ
-->
# Le Chonk เปิดน้ำหนักตัวแล้ว — โมเดลล้านล้านพารามิเตอร์ที่หน่วยงานรัฐจับลงบ้านตัวเองได้

### Mistral Large 4 ปล่อย weights เต็มชุด 1TB บน Hugging Face — ใบอนุญาตแก้ไข MIT + เงื่อนไขเดียว

1 ล้านล้านพารามิเตอร์ = 1,060 GB บน Hugging Face แบ่งเป็น 54 ไฟล์ ไฟล์ละ ~20 GB

โมเดลปิดที่ใหญ่ที่สุดในโลกตอนนี้ เปิดให้แกะกล่องที่บ้านแล้ว

.

Mistral ปล่อย weights ของ **Mistral Large 4 (ML4)** ฉนวชื่อ **Le Chonk** เมื่อ 29 ต.ค. 2026

พรีวิวเริ่ม 6 ต.ค. — อีก 3 สัปดาห์ต่อมาน้ำหนักตัวหลุดมือแล้ว

.

**คำถามที่แท้จริงของโพสต์นี้คับ:**

> **องค์กรที่ข้อมูลอ่อนไหว ควรยกโมเดลล้านล้านพารามิเตอร์มาอยู่ในบ้านจริงไหม — หรือ API ก็พอ?**

.

## ML4 คืออะไร

ตัวเลขจาก model card บน Hugging Face (ตรวจแล้ว 30 ต.ค.):

- พารามิเตอร์รวม ~1T — MoE 128 experts ใช้จริง 4+1 ตัวต่อโทเคน
- พารามิเตอร์ที่ทำงานจริง ~52B ต่อโทเคน
- Context ยาว 1M โทเคน
- อินพุต ข้อความ + รูป (Pixtral-style encoder)
- ภาษา 160+ ภาษา รวมทุกภาษาราชการ EU
- ไฟล์ weights 54 shards ไฟล์ละ ~20 GB รวม ~1,060 GB แถมเวอร์ชัน NVFP4 quantized
- เทรนบน GPU 3,800 ตัว (NVIDIA Grace Blackwell) ใน datacenter ยุโรปของ Mistral เอง
- ใบอนุญาต Mistral Ecosystem Open-Weight — MIT ดัดแปลง

ใบอนุญาตตรวจจากไฟล์ LICENSE จริงบน HF — เอกสารบอกว่าเป็น "modified version of the MIT license"

ใช้ แก้ไข fine-tune และขายเป็นสินค้าได้ ยกเว้นเงื่อนไขเดียว: ธุรกิจที่ขาย **Model-as-a-Service** ต้องขอไลเซนส์พาณิชย์แยกจาก Mistral ก่อน

.

## ทำไมเป้าคืองาน cybersecurity

จุดที่น่าสนใจไม่ใช่ตัวเลข benchmark แต่เป็นประโยคใน announcement ของ Mistral เอง:

โมเดลปิดมี "provider-level refusals" ที่บล็อกงานวิจัยช่องโหว่และ incident response ที่ถูกต้องตามกฎหมาย

และ "การเสียสิทธิ์เข้าถึง capability กลางเหตุการณ์ คือความเสี่ยงด้านความปลอดภัยเอง"

.

แปลง่าย ๆ: ถ้าทีม SOC กำลังไล่ช่องโหว่อยู่แล้วดันเจอผู้ให้บริการโมเดลปิดสวิตช์ — งานหยุดกลางเหตุการณ์

open-weight ตัดความเสี่ยงนี้ทิ้ง เพราะโมเดลอยู่ในเครือข่ายตัวเอง Pierre Stock รองประธานสาย Science ของ Mistral บอก TechCrunch ว่าการเข้าถึงแบบนี้ "ถูกตัดไม่ได้ตามนิยาม"

.

ตัวเลขที่ Mistral อ้าง (จากประกาศ 29 ต.ค. — ยังไม่ได้ทดสอบเอง):

- AA Cyber Index **51%** — งานหาช่องโหว่ reproduce แล้ว patch โดยไม่พังของเดิม
- ปฏิเสธงาน cyber ที่เป็นพิษจริง **96.6%** — สูงสุดที่ Mistral วัดได้ในกลุ่ม open models
- งาน coding: FrontierCode 2.0 (ของ Cognition) **19.7%** นำ open-weight ทั้งกลุ่ม, Terminal-Bench 4.0 **41%** (+13 จากพรีวิว)

.

## เทียบกับคู่แข่งเปิด

- AA Coding Agent Index: ML4 48% — GLM-5.3 อยู่ระดับเดียวกัน ("effectively tied")
- โทเคนที่ใช้ต่องาน: ML4 น้อยกว่า GLM-5.3 อยู่ 47% (baseline คือ GLM-5.3)
- FrontierCode 2.0: ML4 19.7% — GLM-5.3 17.3%
- AA Cyber Index: GLM-5.3 57% สูงกว่า ML4 ที่ 51% — แต่ ML4 ปฏิเสธงานพิษสูงกว่า
- เจ้าของเทคโนโลยี: ยุโรป กับ จีน — เปิด weights ทั้งคู่

ตัวเลข 47% น้อยกว่าของ GLM-5.3 คือข้อเสนอเชิงต้นทุน — ค่า inference พุ่งตามจำนวนโทเคน

API ของ ML4 ราคา $0.70 / $0.07 (cached) / $2.10 ต่อ M tokens ตามลำดับ in / cached / out

หมายเหตุ: ตัวเลขทั้งหมดด้านบนเป็นการอ้างของ Mistral เองหรือจาก Artificial Analysis (third-party benchmark ที่ Mistral หยิบมายก) — ยังไม่มีใครทดสอบซ้ำอิสระเต็มรอบ

.

## สิ่งที่ยังต้องรอดู

- การแก้ไข MIT ที่บล็อก MaaS ทำให้ "เปิด" ของ ML4 เปิดแบบมีขอบ — บริษัทที่อยากขาย API ต่อใช้ไม่ได้ฟรี
- ไฟล์เต็ม 1TB คืองานย้ายจริง (NVFP4 quantized ช่วยลดได้ แต่ยังหนัก)
- เลข factual accuracy ต่ำที่สื่อบางสำนักยกมา ยังตรวจต้นทางไม่ได้ในรอบนี้ — ไม่อ้าง

.

## ใครควรลอง ใครไม่ต้อง

**ควรดูต่อ:** ทีม security/SOC ขององค์กรที่ถูกผูก data-residency, หน่วยงานรัฐที่ทำ sovereign-AI, ทีมที่เคยโดน refusal ตัดงานกลางคัน

**ไม่ต้องเปลี่ยน:** คนใช้โมเดลทั่วไปผ่าน API อยู่แล้ว งานไม่ได้อ่อนไหวเรื่องข้อมูล — 1TB ไม่ใช่ของเล่นสวนทางเศรษฐกิจ, GLM-5.3 ก็ยังเก่งและถูกอยู่

.

## #สรุปแบบวิศวกรเป็ด

**Open weights** = น้ำหนักตัวโมเดลที่แกะออกจากบริการผู้ให้บริการได้

**Self-deploy** = รันในเครือข่ายตัวเอง ข้อมูลไม่ออกไปไหน

**Provider refusal** = จุดตายเดียวของโมเดลปิดที่ open-weight ซื้อมาไม่ได้

กลับคำถามแท้: ถ้างานขององค์กรเดินอยู่บนโมเดลคู่หนึ่ง แล้วจุดเดียวที่ทำให้งานหยุดคือ "เขาปิดสวิตช์" — โมเดลที่โหลดมาวางในบ้านเอง ซื้ออิสระจากจุดนั้นด้วยต้นทุนบ้าน server

**ML4 เปิดไม่ใช่เพราะใจดี — มันคือข้อเสนอขายอิสระ ในราคา 1TB บน Hugging Face**

.

#Adduckivity #DuckOS #NeuroDivergent #AI #OpenWeights #Mistral
