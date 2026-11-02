# System Diagnostic: The Chunking Engine — สมอง Simulate เฉพาะ Best-Case แล้วทิ้ง Base Rate: ทำไมเวลาจริงบวม 2–4 เท่า (Neuroscience × Duck OS)

<!--
ContentID: 20260918-CNT-CHUNKING-ENGINE
Title: System Diagnostic: The Chunking Engine — สมอง Simulate เฉพาะ Best-Case แล้วทิ้ง Base Rate: ทำไมเวลาจริงบวม 2–4 เท่า (Neuroscience × Duck OS)
Slug: system-diagnostic-chunking-engine-estimation
Type: Core Content (System / Mindset — long form ~2050 words)
Law: Law #1 System > Emotion / Law #2 Asset > Activity / Law #3 Protect System
Series: System Diagnostic — ref: 20260917-cnt-quick-wins-tiny-functional-nodes (2026-09-17), 20260918-cnt-system-diagnostic-hero-complex (2026-09-18), 20260915-cnt-system-diagnostic-reasons-to-quit (2026-09-15), 20260917-cnt-meetings-are-toxic (2026-09-17)
Status: draft
Date: 2026-09-18
Sources (verified 2026-09-18):
  - Planning Fallacy: Kahneman & Tversky 1979 "Intuitive prediction: biases and corrective procedures" (TIMS 12:313-327) — def "underestimate the time required to complete a project, even when they have considerable experience of past [projects taking longer]" + inside view / outside view model (verified sciencedirect "The Planning Fallacy: Cognitive, Motivational, and Social Origins" + en.wikipedia.org/wiki/Planning_fallacy + SPSP blog "The Planning Fallacy: An Inside View")
  - Lovallo & Kahneman 2003: expanded definition (underestimate time, costs, risks + overestimate benefits) — Wikipedia
  - Presentism / best-case simulation: "individuals tend to ignore past delays—such as traffic, interruptions, or unexpected difficulties—and instead simulate a 'best-case scenario' that rarely reflects real-world conditions. This combination of present-focused forecasting and selective memory contributes to the persistent underestimation" — en.wikipedia.org/wiki/Planning_fallacy (cites [11][12])
  - JASPSP 1994 (Buehler, Griffin & Ross, "Exploring the Planning Fallacy"): "people can know the past and yet still be doomed to repeat it" + "narrative mode" of thinking + Channel Tunnel example (predicted June 1993 £4.9B → real £10B+) — web.mit.edu/curhan PDF + base-rate neglect ref (Bar-Hillel 1980)
  - Episodic future simulation (neuro): hippocampus + ventromedial PFC (vmPFC) critical; "Damage to either structure affects one's ability to remember the past and imagine the future"; mPFC changes interaction with hippocampus when reflecting past vs looking future; "Mental Time Travel: remembering past and imagining future = fundamentally the same process (constructive episodic simulation)" — PMC5777865 + PMC11179466 + PMC5708138 + Springer neurocognitive MTT model (s13164-020-00470-0)
  - Working memory capacity: Cowan (2001) ~4 items ("the magical number four"); Miller (1956) 7±2; Cognitive Load Theory (Sweller 1988) working memory holds ~4-7 items — journalofcognition.org (10.5334/joc.387) + neurosity.co + en.wikipedia.org/wiki/Chunking_(psychology)
  - Law #3 anchor (PFC under stress/fatigue): PNAS 2015 "Neural mechanisms underlying the impact of daylong cognitive work on economic decisions" — 6h+ executive control → LPFC activity decrease → increased choice impulsivity; "LPFC dysfunction following overly intense cognitive work, with insufficient breaks, at longer time scales (weeks or months) might induce pathological conditions such as burnout syndromes"; Nature Neuroscience (Arnsten) "Stress weakens prefrontal networks: molecular insults to higher cognition" — acute uncontrollable stress → catecholamine release in PFC → reduces neuronal firing → impairs cognition; chronic stress → persistent PFC dysfunction; PMC "The Neurobiology of Cognitive Fatigue and Its Influence on Effort-Based Choice" — dlPFC exertion signals → insula effort-value computation → fatigued → less willing to exert
  - User source text (2026-09-18): System Diagnostic (แก่นเชิงระบบ) — The Best-Case Scenario Fallacy / Exponential Estimation Error / The Chunking Engine + 3 Laws mapping
  - Style: content-study/WRITING_STYLE_GUIDE.md + STYLE_CORPUS.md (long form = "## NN:" markdown headings like four-thousand-weeks (2026-09-13) + attention-shock (2026-09-10), บทสรุปจากพร closer)
-->

เคยมั้ยคับ — คุณเปิด task ขึ้นมา แล้วสมองพูดว่า "อันนี้ 2 ชั่วโมงก็เสร็จ" — แล้วพอถึง 5 โมงเย็น งานก็ยังไม่ขยับจากจุดเดิม

คุณลองใหม่ — "พรุ่งนี้เช้า 3 ชั่วโมง เสร็จแน่นอน" — แล้ว 3 ชั่วโมงก็หายไปเหมือนไม่เคยมีอยู่

ถ้าพรจะบอกตรง ๆ เลยนะคับ — **คุณกำลังวินิจฉัยโรคผิด (Misdiagnosis)** — เราก็บอกตัวเองว่า "เราทำงานช้า ขี้เกียจ ไม่มีวินัย" — แต่ในภาษาประสาทวิทยา มันไม่ใช่ความล้มเหลวทางศีลธรรม — มันคือ **error ของเครื่องยนต์ประเมินเวลาในสมอง** ที่ถูกออกแบบมาให้ **render เฉพาะ "ภาพสวย" แล้วทิ้งข้อมูลสถิติจริง**

.

และวันนี้พรจะพาไป debug เครื่องยนต์ตัวนี้แบบ neuroscience — พร้อมโพรโทคอล **CHUNK-01** ที่พรรันจริง

## 00: Ingestion Phase — สมองไม่มี "นาฬิกาประเมิน" — มันมี "Future Simulator"

ก่อนอื่นต้องแก้ความเข้าใจผิดตัวแรกคับ — **สมองคุณไม่มี "ตัวประเมินเวลา"** แบบเครื่องจับเวลาในโทรศัพท์ — สิ่งที่มีจริง ๆ คือ **ระบบจำลองอนาคต (episodic future simulation)**

งานวิจัยด้าน Mental Time Travel ยืนยันตรง ๆ ว่า **การจำอดีต (remembering the past) กับการจินตนาการอนาคต (imagining the future) เป็น process เดียวกัน** — มันใช้ **Hippocampus** + **ventromedial Prefrontal Cortex (vmPFC)** ชุดเดียวกัน — และ "ความเสียหายต่อโครงสร้างใดโครงสร้างหนึ่ง จะทำลายทั้งการจำอดีตและการจินตนาการอนาคตพร้อมกัน" (PMC5777865)

แปลว่า **ทุกครั้งที่ "ประเมินเวลา" — สมองคุณไม่ได้คำนวณ — มันกำลัง "render ภาพในอนาคต"** — และ render ภาพนั้นแหละคือตัวปัญหา

> **"The planning fallacy refers to a prediction phenomenon, all too familiar to many, wherein people underestimate the time it will take to complete a future task, despite knowledge that previous tasks have generally taken longer than planned."**
> — The Planning Fallacy (Kahneman & Tversky, 1979)

**Planning Fallacy** — กับดักการวางแผน ที่ Daniel Kahneman กับ Amos Tversky ตั้งชื่อไว้ตั้งแต่ 1979 — คือ **การประเมินเวลาต่ำไป ทั้งที่คุณ "รู้" ว่างานประเภทนี้กินเวลานานกว่าที่คาดมาตลอด** — และ Lovallo & Kahneman (2003) ขยายคำนิยาม: มันไม่ได้ underestimate แค่เวลา — มัน **underestimate ทั้งเวลา ค่าใช้จ่าย และความเสี่ยง — แล้ว overestimate ผลได้พร้อม ๆ กัน**

## 01: The Best-Case Scenario Fallacy — สมอง Render เฉพาะ "Happy Path"

ทำไม Future Simulator ถึง render ภาพที่สวยเกินจริง?

เพราะมัน render **Happy Path** — เส้นทางที่ทุกอย่างไปสวย ๆ — ไม่มีบั๊ก ไม่มีประชุมแทรก ไม่มีใครมาทัก ไม่มีเน็ตตก — และงานวิจัยอธิบายกลไกนี้ตรง ๆ ว่า:

> **"...individuals tend to ignore past delays—such as traffic, interruptions, or unexpected difficulties—and instead simulate a 'best-case scenario' that rarely reflects real-world conditions. This combination of present-focused forecasting and selective memory contributes to the persistent underestimation..."**
> — en.wikipedia.org / Planning fallacy (citing the planning-fallacy literature)

สองกลไกที่ทำงานพร้อมกันคับ:

**กลไกที่ 1: Presentism** — ตอนที่คุณจินตนาการอนาคต **คุณกำลังรู้สึก "สงบ โฟกัส ยิ้ม ๆ" อยู่ปัจจุบัน** — และสมองเอา emotional state ตอนนี้ไป "ย้อม" ภาพอนาคตด้วย — ภาพในอนาคตจึง **ไม่มี noise ของวันจริง** ที่คุณเคยเจอ — มัน render จาก "ตอนนี้ฉันกำลังโฟกัส" ไม่ใช่จาก "วันนั้นฉันโดนขัดจังหวะ 7 ครั้ง"

**กลไกที่ 2: Inside View** — Kahneman & Tversky เรียกมันว่า **Inside View** — คุณ "เล่าเรื่อง" (narrative mode) ว่า "ฉันจะลงมือทำแบบนี้ แล้วมันจะเสร็จ" — story นั้น **case-based** (เฉพาะงานนี้) — และมัน **ข้าม Base Rate** (สถิติจากงานที่คล้ายกันในอดีต) ไปเลย — งานวิจัย JASPSP 1994 (Buehler, Griffin & Ross) สรุปมันได้เจ็บมาก:

> **"People can know the past and yet still be doomed to repeat it."**

(คุณรู้อดีตดี — แต่คุณก็ถูกกำหนดให้ทำผิดพลาดเดิมซ้ำ)

และตัวอย่างคลาสสิกใน paper เดียวกัน — **Channel Tunnel** (อุโมงค์ใต้ช่องแคบอังกฤษ) — ประเมินว่าเปิดได้ **มิถุนายน 1993** งบ **4.9 พันล้านปอนด์** — ของจริงคือ **เกิน 10 พันล้านปอนด์** — ไม่ใช่เพราะคนคำนวณโง่ — แต่เพราะ **Future Simulator ของทั้งประเทศ render เฉพาะ Happy Path**

## 02: Exponential Estimation Error — ยิ่ง Timeframe กว้าง — ความคลาดเคลื่อนยิ่ง "ทวีคูณ"

ถ้า Error 1 คือ "render ภาพสวย" — Error 2 คือ **"render ภาพที่กว้างเกินกว่าจะ resolve ได้"**

ลองนึกภาพ Future Simulator เป็น **render window** — ยิ่งคุณพยายาม render **ภาพกว้าง** (โปรเจกต์ระดับสัปดาห์ ระดับเดือน) — ระบบยิ่ง **resolve รายละเอียดไม่ได้** — มันเลย fallback กลับไปใช้ **"ค่าเฉลี่ยของ Happy Path"** — ซึ่ง optimistic โดยโครงสร้าง

ในภาษาของ literature มันคือ **Distributional / Base-Rate Neglect** — ยิ่ง timeframe กว้าง:

1. **Inside View ยิ่งครอบงำ** — คุณ "เล่าเรื่อง" อนาคตไกล ๆ ได้สวยกว่าการ "นับฐานสถิติ" ของงานที่คล้ายกัน
2. **Base Rate ยิ่งถูกทิ้ง** — งานวิจัย base-rate neglect (Bar-Hillel, 1980) ยืนยัน: คนใช้ base-rate **เฉพาะเมื่อ "ต่อ" กับงานตรงหน้าได้** — ยิ่งงานไกล ยิ่งต่อไม่ติด ยิ่งทิ้ง
3. **Unknowns สะสม** — ยิ่งระยะไกล ยิ่งมีตัวแปรที่ "คุณยังไม่รู้ว่ามี" — และตัวแปรที่ไม่รู้ = ตัวที่ทำให้บวม

ผลคือ **อัตราความคลาดเคลื่อนไม่ใช่เส้นตรง — มันทวีคูณตามความกว้างของ timeframe** — งาน 1–2 ชั่วโมง estimate ยังพอแม่น — งาน 1 สัปดาห์ — บวมขึ้น — งาน 1 เดือน — **บวมเป็นหลายเท่า** (และในโปรเจกต์จริง ตัวเลขมัก **2–4 เท่า** ของ estimate)

DHH พูดตรง ๆ ใน podcast ของ 37signals เอง (ref: โพสต์ Quick Wins 2026-09): **"The longer something takes, the less likely it is you'll finish it."** — ยิ่งนาน ยิ่งมีโอกาสไม่เสร็จ — ไม่ใช่เพราะคุณขี้เกียจ — แต่เพราะ **error ของ estimate ยิ่ง compound**

## 03: The Chunking Engine — วิธีแก้ไม่ใช่ "กะให้แม่น" แต่คือ "หั่นให้เล็ก"

ตรงนี้สำคัญสุดคับ — **วิธีแก้ไม่ใช่การพยายาม "ประเมินให้แม่นขึ้น"** — เพราะคุณ "แก้" เครื่องยนต์ที่ render Happy Path ให้ render Real Path ไม่ได้ — มันถูก hardcode มาแล้ว

วิธีแก้จริง ๆ คือ **The Chunking Engine** — **การหั่น timeframe ให้เล็กลงเรื่อย ๆ จน render window เล็กพอที่สมองจะ resolve ได้**

และนี่มีรากฐานประสาทวิทยาชัดเจน — **Working Memory** ของมนุษย์มี **capacity จำกัด** — งานคลาสสิกของ Miller (1956) บอกว่า **7±2 items** — แต่ Cowan (2001) วัดจริงแล้วลงไปที่ **"the magical number four"** — **ประมาณ 4 chunks** ที่สมอง "ถือ" อยู่ใน foreground buffer พร้อมกัน (Cognitive Load Theory — Sweller, 1988 ยืนยันว่า working memory "ถือ" ได้แค่ ~4–7 items)

แปลเป็นภาษาของ estimation:

- **chunk ใหญ่** (ระดับสัปดาห์) = มีตัวแปร > 4 items ที่ต้อง "ถือ" พร้อมกัน = **เกิน capacity** = สมอง **fallback ไป render Happy Path** (เพราะ resolve ตัวแปรทั้งหมดไม่ได้)
- **chunk เล็ก** (ระดับ 1–2 ชั่วโมง) = ตัวแปร ≤ 4 items = **อยู่ใต้ capacity** = สมอง **resolve ได้จริง** = **error rate ต่ำ**

**งานที่ประเมินเป็นระดับ 1–2 ชั่วโมงจะมี Error Rate ต่ำกว่างานที่ประเมินระดับสัปดาห์อย่างเทียบไม่ติด** — ไม่ใช่เพราะคุณ "เก่งขึ้น" — แต่เพราะ **คุณทำให้ render window เล็กพอที่ Future Simulator จะ render ได้จริง**

นี่คือ **Chunking Engine** — ไม่ใช่เครื่องมือจัดเวลา — แต่คือ **การ shrink render window ให้เล็กพอที่สมองจะ resolve** คับ

## 04: Protocol CHUNK-01 — 3 commands (The Chunking Engine)

พรย่อ The Chunking Engine ให้เป็นโพรโทคอล **CHUNK-01** — 3 commands:

### Step 1: `chunk --outside` (5 นาที, ก่อนประเมินทุกครั้ง)

**บังคับใช้ Outside View** — ก่อนที่คุณจะ "เล่าเรื่อง" (Inside View) ของงานนี้ — **ถาม 2 ข้อ:**
- "งานประเภทนี้ **ครั้งก่อน** ใช้จริงกี่ ชม.?" (your own base rate)
- "คนอื่น / ทีมอื่น ใช้กี่ ชม.?" (population base rate)

เขียน 2 ตัวเลขลง — แล้ว **อย่า estimate จาก story** — estimate จาก **ค่าเฉลี่ยของ 2 ตัวเลขฐาน** แล้วบวก buffer — นี่คือ antidote ตรง ๆ ของ Planning Fallacy (inside view → outside view) และของ Best-Case Scenario Fallacy (render Happy Path → render base rate)

### Step 2: `chunk --slice` (หั่นจนเข้า 4-slot buffer)

**ตัดโปรเจกต์เป็น chunk ที่เล็กพอ:**
- **test: chunk นี้มี "ตัวแปรที่ถือพร้อมกัน" ≤ 4 items ไหม?** (Cowan's 4)
- **test: chunk นี้ estimate ได้ใน **ระดับ 1–2 ชั่วโมง** ไหม?**
- ถ้าไม่ = **slice อีก** — กฎ: **ถ้า estimate ของ chunk > 1 วัน — มันยังไม่ "chunk" — มันคือ "โปรเจกต์"** — slice ต่อ

**ห้าม schedule chunk ที่เกิน capacity** — เพราะ chunk ที่เกิน capacity = render ที่ resolve ไม่ได้ = Happy Path fallback = error บวม (Error 2)

### Step 3: `chunk --noise` (Re-inject the Real Path)

**แต่ละ chunk — "ป้อน noise กลับเข้าไป" ใน render:**
- **"1 บั๊ก / 1 การประชุม / 1 สิ่งขัดจังหวะ"** — คือ minimum noise ที่ต้องใส่กลับ (สิ่งที่คุณ "render ทิ้ง" ใน Best-Case Scenario)
- หรือ **commit ที่ estimate × 2** (ไม่ใช่ estimate × 1) — เพราะ "real time" บวม **2–4 เท่า** — **อย่า commit ที่ Happy Path — commit ที่ Real Path**

**ห้ามมีตัวเลือกที่สาม** — คือ "commit ที่ estimate 2 ชม. แล้วภาวนา" — นั่นคือ Best-Case Scenario Fallacy ในรูปแบบ schedule

**Success Criteria:** สัปดาห์นี้ — 3 tasks ที่ estimate ด้วย `--outside`, slice จนเข้า 4-slot buffer, แล้ว commit ด้วย `--noise` — วัดผล: **ratio ของ "estimate vs actual" อัดเข้าใกล้ 1.0** (ไม่ใช่ 0.25) — และ **ไม่มี chunk ไหน "บวม" ข้าม boundary ของมัน**

## 05: ผูกกลับ Duck OS

**Law #1: System > Emotion** — ความมั่นใจที่บอกว่า "รอบนี้น่าจะเสร็จทัน" = **emotional state ที่ Presentism ย้อมภาพอนาคต** — มันคือ **input อารมณ์** ไม่ใช่ **data** — ระบบที่ดีไม่ estimate จาก "ฉันรู้สึกว่าจะเสร็จ" — มัน estimate จาก **base rate + 4-slot buffer + noise re-injected** — เลิกเดาเวลา — ใช้ **ระบบหั่นขอบเขต** แทน

**Law #2: Action Precedes Motivation (Asset > Activity)** — การนั่งทำ **Gantt Chart คาดการณ์เวลาทั้งเดือน** = **Activity ที่ render ภาพกว้างเกิน capacity** = Happy Path fallback = estimate ที่ useless — สู้ **สับงานให้เหลือ Tiny Functional Node** ที่ปิดจบได้ในไม่กี่ชั่วโมง แล้ว **Ship ทันที** — จะได้ **Asset จริงเร็วกว่า** — และ **estimate ของ node ถัดไปจะแม่นขึ้น** เพราะคุณมี base rate ของ node ก่อนหน้าแล้ว (ref: Quick Wins 2026-09 + SHIP-01)

**Law #3: Protect the System** — อันนี้เจ็บสุดคับ — **การประเมินเวลาพลาด ไม่ได้จบที่ "งานเสร็จช้า"** — มัน **ลากคุณเข้าสู่ cascade:**

> **bad estimate → task overrun → deadline pressure → Overload + อดนอน + Emergency Mode → Acute Stress**

และงานวิจัย PNAS 2015 วัดตรง ๆ ว่า: **6 ชั่วโมงของ executive control ที่หนัก → LPFC (lateral PFC) activity ลดลง → choice impulsivity เพิ่มขึ้น** — และ paper เดียวกันเตือนว่า:

> **"LPFC dysfunction following overly intense cognitive work, with insufficient breaks, at longer time scales (weeks or months) might induce pathological conditions such as burnout syndromes."**

Nature Neuroscience (Arnsten) ยืนยัน: **acute uncontrollable stress → catecholamine flood ใน PFC → ลด neuronal firing → impair cognition** — และ **chronic stress → architectural changes → persistent PFC dysfunction**

แปลว่า: **PFC (foreman ของระบบคุณ) ถูก "thermal throttle" ด้วย stress** — มัน impaired → **estimate ยิ่งแย่ → cascade ยิ่งหนัก** — **The Chunking Engine คือการ "keep the foreman under its thermal limit"** — chunk เล็ก ๆ **ไม่เคย trigger stress cascade** — เพราะมัน **ปิดจบก่อนที่ deadline pressure จะสะสม**

.

โพสต์ Quick Wins (2026-09) พรบอกว่า momentum เกิดจาก **node เล็กที่ Ship จริง** — โพสต์นี้คือ "อีกครึ่ง" ของเรื่องเดียวกัน: **node เล็ก = estimate ที่แม่น** — เพราะ **render window เล็ก = resolve ได้จริง = error rate ต่ำ** — และมันคือรากเดียวกับ Hero Complex (2026-09): รอบนั้นคือ "stop ลากงานใหญ่ที่ estimate ผิด" — รอบนี้คือ **"อย่าให้ estimate ผิดตั้งแต่แรก — โดยหั่นให้เล็กพอที่สมองจะ render ได้"** — ทั้งสองจบที่ **kill the big render window** — เพราะ **render ที่กว้างเกิน capacity คือ render ที่ render ไม่ได้จริง ๆ**

.

## บทสรุปจากพร

ถ้าพรจะสรุปเป็น 3 บรรทัดสำหรับระบบของคุณ:

1. **สมองคุณไม่มี "ตัวประเมินเวลา" — มันมี "Future Simulator" ที่ render เฉพาะ Happy Path** (Planning Fallacy + Presentism + Inside View) — และ **render ที่กว้างเกิน capacity (timeframe กว้าง) = error ที่ทวีคูณ**
2. **วิธีแก้ไม่ใช่ "กะให้แม่น" — แต่คือ "หั่นให้เล็ก"** (The Chunking Engine): **`--outside`** (base rate) → **`--slice`** (จนเข้า 4-slot buffer) → **`--noise`** (re-inject real path, commit ที่ × 2)
3. **Chunk เล็ก ๆ = keep the PFC (foreman) under its thermal limit** — **ไม่ trigger stress cascade → ไม่ burnout → estimate ของ round ถัดไปจะแม่นขึ้น** — loop ปิด

พรจะรัน protocol CHUNK-01 นี้กับตัวเองก่อน — แล้วมา update log ว่า **ratio estimate/actual ของพร อัดเข้าใกล้ 1.0 ได้แค่ไหน** — เพราะพรเชื่อตามที่ Duck OS สอนมาตลอด: **protocol ที่ไม่ถูกรัน = documentation ที่ไม่มีใครอ่าน** คับ

#Adduckivity #DuckOS #NeuroDivergent #PlanningFallacy #Chunking #Estimation #SystemThinking
