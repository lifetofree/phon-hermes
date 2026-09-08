# Memento Mori — "จงจำไว้ว่าเธอจะต้องตาย" ฝึกเก่า 2,000 ปี ที่ช่วยให้เราใช้ชีวิตได้ดีขึ้น (ไม่ใช่กลัวมากขึ้น)

<!--
ContentID: 20260908-CNT-MEMENTO-LF
Series: Stoicism / productivity-systems — ผูกกับ Task Logger (task-logger.adduckivity.com) ที่พรสร้างเป็น PWA บน Cloudflare Worker + D1
Type: Long Form (~2500-3000 words)
Status: Draft — รอย review
Sources (researched 2026-09-08):
- Memento Mori: ฝึกสโตอิกหลัก = ถือความตายไว้ในใจเพื่อ clarify ว่าเวลาเหลือควรใช้ยังไง ไม่ใช่หมกมุ่นกับความตาย
- ราก: ธรรมเนียม Roman triumph (ผู้ติดตามกระซิบเตือนแม่ทัพ "memento mori" หลังชัยชนะ) — เป็น "tradition" ที่เล่ากันมาก ไม่ใช่ข้อเท็จจริงที่พิสูจน์แล้ว (บางแหล่งตั้งคำถาม)
- สโตอิกจัด death เป็น "indifferent" (ไม่ดียังไม่เลว) → ตัดฐานของ fear ออก → ผลลัพธ์ตรงข้าม morbidity (energize ไม่ใช่ depress)
- Marcus Aurelius (Meditations 12.1, 7.56, 2.11, 12.3)
- Seneca (On the Shortness of Life 1.1; Letters to Lucilius 10.4 "you postpone enjoying your life")
- Epictetus (Discourses 1.2 "when you are bathing, represent to yourself what happens in the baths")
- Modern psych: death awareness / mortality salience (Pyszczynski — Terror Management Theory); buffer = self-worth, meaning, close relationships; CAVEAT: ไม่มี buffer → เพิ่ม anxiety
- App: Task Logger v5.1.0 — Memento tab = life grid 80 ปี (~29,200 cell) แต่ละวันสีตาม average happiness (red→amber→green) + days lived/days remaining + rotating verified Stoic quote + "New quote" shuffle + collapsible PhilosophyPanel (Thai)
Vendor: adduckivity (พร)
Note: บทความนี้สอนปรัชญา memento mori แบบตรงไปตรงมา (รวม caveat จริง ๆ ว่าทำไมมันถึง help) แล้วชี้ไปที่ app ที่พรสร้างเป็น "practice tool" — บันทึกความสุขรายวันเป็น buffer ที่ทำให้การฝึกนี้ work
-->

## 00: Hook — "คุณเคยนับจำนวนวันที่เหลือมั้ยคับ"

ลองเปิดเครื่องคิดเลขดู — สมมติคุณอายุ 30 ปี และจะอยู่ถึง 80 ปี

นั่นแปลว่าวันข้างหน้าคุณมีประมาณ **29,200 วัน**

พรเคยพิมพ์ตัวเลขนั้นลงใน console ของตัวเอง แล้วค้างไปสัก 30 วิ — ไม่ใช่เพราะตกใจ แต่เพราะมัน "render" ขึ้นมาชัดมาก — มันไม่ใช่ความตายแบบ abstract อีกต่อไป — มันคือ number ที่ concrete — 29,200 cells ที่รอให้ถูก paint

และถ้าคุณ scroll ขึ้นไปอีก — คุณจะเห็น **days ที่ผ่านไปแล้ว** — 30 ปีของคุณ — 10,950 วัน — ซึ่งในจำนวนนั้น มีกี่วันที่คุณ "record" ไว้? กี่วันที่คุณจำได้ว่ามีความสุข? กี่วันที่คุณแค่ "รอดผ่าน" ไป?

**Memento Mori** (เมเมนโต มอริ) = ภาษาลาติน แปลว่า "จงจำไว้ว่าเธอจะต้องตาย" — และบทความนี้จะบอกคับว่ามันไม่ใช่การนั่งจ้องความตายจนกลัว แต่มันคือ **การถือความตายไว้ในใจ** เพื่อให้เราเห็นชัดว่าเวลาที่เหลืออยู่ ควรใช้กับอะไร

ถ้าอ่านจบแล้วอยากได้ "practice tool" จริง ๆ — พรสร้าง **Task Logger** (task-logger.adduckivity.com) เป็น PWA ที่เอาปรัชญานี้มาเป็น core feature — มี "life grid" 80 ปี ให้คุณ paint วันแต่ละวันด้วยสีของความสุข — ไปดูที่ section 07

## 01: Memento Mori คืออะไร — "การฝึกถือความตายไว้ในใจ"

> **Memento Mori** = ฝึกปฏิบัติหลักของปรัชญาสโตอิก (Stoicism) — **ถือความตายไว้ในใจอย่างต่อเนื่อง** ไม่ใช่เพื่อหมกมุ่น แต่เพื่อ **clarify ว่าเวลาที่เหลือควรใช้ยังไง** — เป้าหมายคือทำให้ชัดว่าอะไรสำคัญจริง ๆ + ปลูกฝังความขอบคุณต่อปัจจุบัน + เพิ่มสมาธิกับสิ่งรอบตัว

จุดสำคัญที่สุดที่คนมักเข้าใจผิด: **ผลลัพธ์มันตรงข้ามกับ morbidity**

สโตอิกมองว่าความตายเป็น **"indifferent"** (adiaphoron) — คือ "สิ่งที่เป็นกลาง" ไม่ใช่สิ่งดี ไม่ใช่สิ่งเลว — เหมือนฝนตก ไม่ใช่ good weather ไม่ใช่ bad weather — มันแค่ "เป็น" — พอเราจัด death เข้า category นี้ **ฐานของความกลัวมันหายไปเลย** เพราะเราไม่ได้กลัว "ผลลัพธ์ที่เลวร้าย" แต่เรากลัว "สิ่งที่เป็นกลาง" ซึ่งไม่มีเหตุผลจะกลัว

ดังนั้นการฝึกนี้ไม่ได้ทำให้เราหดหู่ — มันทำให้เรา **energize** — มันเหมือนเราเปิด `--verbose` flag บนชีวิตของเราเอง — ทุกอย่างชัดขึ้น — ไม่มีอะไรซ่อนตัวอีกต่อไป

และไม่ใช่แค่ "คิดถึงความตาย" แบบหยาบ ๆ — สโตอิกมี **เทคนิค** ละเอียด: Epictetus แนะนำให้ "visualize" สถานการณ์ก่อนเกิดจริง (เช่น ก่อนไปอาบน้ำ ให้จินตนาการว่าข้างในวุ่นวายแค่ไหน — พอไปถึงจริง มันก็จะ "pass") — Marcus Aurelius เขียนใน Meditations ทุกเช้า — Seneca เขียนจดหมายเตือนเพื่อนว่า "ชีวิตกำลังหมดอายุ" — ทั้งหมดนี้เป็น **daily practice** ไม่ใช่ "moment of death" ที่เกิดปีละครั้ง

## 02: Diagnostic Logs — "Bug Report ของการลืมว่าเราต้องตาย"

ถ้าเราไม่ฝึก Memento Mori — life จะเกิด **error** อะไรบ้าง?

**Error 1: `LIFE_ON_HOLD.exe` (Life Deferred)**
เราเลื่อนทุกสิ่งที่สำคัญไป "วันหลัง" — ไปออกกำลังกาย "พรุ่งนี้" พูดกับคนที่รัก "สักวัน" เริ่มโปรเจกต์ "รอพร้อม" — เรา live แบบเหมือนมี infinite runtime — แต่เราไม่มี — และ runtime ที่ "infinite" ในความคิด มันคือ **lie ที่เรา tell ตัวเองทุกวัน**

**Error 2: `CONTEXT_SWITCHING_INFINITE` (Trivial Overload)**
เราเอาเวลาไปเสียกับสิ่งที่ไม่สำคัญ — scroll social media 3 ชม. นอนดึกเพราะ "ยังทำไม่เสร็จ" — Seneca พูดชัด: *"It is not that we have a short time to live, but that we waste much of it."* — ปัญหาไม่ใช่ชีวิตสั้น แต่เรา **waste** มัน — เขา estimate ว่าคนเรา take ไป 1/3 ของชีวิตไปนอน, 1/4 ไป "รอ", 1/8 ไป worry — แล้วเรา wonder ว่าทำไมชีวิตมัน "short"

**Error 3: `FEAR_LOCK` (Death Anxiety Without Buffer)**
คนที่ไม่เข้าใจ Memento Mori จะกลัวความตายแบบไม่มี structure — กลัวแบบ abstract → ruminate → anxiety — นี่คือ **bug ที่ต้องระวัง**: การฝึก Memento Mori **ไม่มี buffer** (meaning, relationships, self-worth) มันจะ **ทำให้อาการแย่ลง** ไม่ใช่ดีขึ้น — และถ้าคุณกำลังอยู่ใน state นี้ (burnout ซ้ำ ๆ, รำคาญตัวเองทุกวัน) — อย่าเริ่มการฝึกนี้ก่อน — **build buffer ก่อน** (section 04 จะอธิบายว่า buffer คืออะไร)

**Error 4: `SNAPSHOT_MISS` (No Record)**
เราไม่ "record" วันของตัวเอง — พอถึงวันเกิดครบรอบ 30 — เราจำไม่ได้ว่า "ปีนั้นเราเป็นยังไง" — เราไม่มี telemetry ของชีวิตตัวเอง — Life grid ของ Task Logger (section 07) แก้ error นี้ตรง ๆ — ทุกวันที่คุณ paint = snapshot 1 อัน — 29,200 snapshots = ภาพเต็มของชีวิตคุณ

## 03: Primary Sources — "ใครสอนอะไร"

### Marcus Aurelius — จักรพรรดิที่เขียน diaries ให้ตัวเอง

> "You could leave life right now. Let that determine what you do and say and think." — Meditations 12.1

> "Think of yourself as dead. You have lived your life. Now take what is left and live it properly." — Meditations 7.56

> "You have your life. Your life has you." — Meditations 12.3

Marcus ไม่เคย publish Meditations — เขาเขียนเป็น **personal journal** ในสนามรบ — ทุกเช้าเขา "boot up" ด้วยคำถามเดียวกัน: วันนี้จะ live ยังไงถ้าเป็นวันสุดท้าย? — นี่คือ **daily Memento Mori ritual** — และเขาทำมันในฐานะ **จักรพรรดิ** — คนที่มีอำนาจสูงสุดของ empire — ถ้าการฝึกนี้ work สำหรับคนที่มีทุกอย่าง — มันก็ work สำหรับเรา

### Seneca — "ชีวิตมันยาวพอ ถ้าเราใช้มันถูก"

> "It is not that we have a short time to live, but that we waste much of it." — On the Shortness of Life 1.1

> "Life is long if you know how to use it." — On the Shortness of Life 1.1

> "You postpone enjoying your life, and some unusual scheme engrosses you... you make preparations for your life, and so your life is lost." — Letters to Lucilius 10.4

Seneca เขียน On the Shortness of Life **ทั้งเล่ม** เป็น Memento Mori — เขา argue ว่าเราไม่ได้มีเวลาน้อย — เรามีเวลาพอ — แต่เรา **ไม่ allocate มันถูก** — เขา observe ว่าคนส่วนใหญ่ "prepare to live" ตลอดชีวิต — เตรียมตัวไปทำงาน เตรียมตัวไปพักผ่อน เตรียมตัวไปรัก — แต่ไม่เคย "live" จริง ๆ — นี่คือ **Life Deferred (Error 1)** ในภาษาของ Seneca

### Epictetus — "visualize ก่อนเกิดจริง"

> "When you are bathing, represent to yourself what happens in the baths: some men push, some strike, some abuse." — Discourses 1.2

Epictetus เป็นทาสมาก่อน — เขาไม่ได้ "เลือก" ให้เป็น Stoic — เขา **survive** ในฐานะทาสด้วย Stoicism — การฝึก Memento Mori สำหรับเขาจึงไม่ใช่ luxury — มันคือ **survival tool** — และเทคนิค "visualize" ของเขา (premeditatio malorum = การฝึกภาพด้านลบไว้ล่วงหน้า) คือ **cognitive rehearsal** ที่งานวิจัยสมัยใหม่พบว่าลด surprise + ลด anxiety ได้จริง

## 04: Modern Psychology — "ทำไมการฝึกนี้ถึง work (และเมื่อไหร่ที่มัน fail)"

งานวิจัยด้าน **death awareness / mortality salience** (เช่น งานของ Tom Pyszczynski — **Terror Management Theory**) พบ pattern ที่ clear:

**เมื่อมี buffer → positive effect:**
- เพิ่ม life satisfaction + gratitude
- ช่วยจัดลำดับค่าของสิ่งต่าง ๆ (value-alignment) — ทิ้งเรื่องเล็กน้อย
- ลด rumination (คิดซ้ำเรื่องเดิม)
- เพิ่ม presence (อยู่กับปัจจุบัน)
- เพิ่ม prosocial behavior ( altruism, ความเมตตา)

**เมื่อไม่มี buffer → negative effect (⚠️):**
- เพิ่ม anxiety
- ลด well-being
- เพิ่ม rumination
- เพิ่ม defensive behaviour (ปกป้อง ego)

**Buffer คืออะไร?** — งานวิจัยชี้ไปที่ 3 อย่าง:
1. **Self-worth** — คุณมีคุณค่าในตัวเอง (ไม่ใช่จาก external validation)
2. **Meaning** — ชีวิตมี purpose (สิ่งที่คุณ "record" ว่าสำคัญ)
3. **Close relationships** — คุณมีความสัมพันธ์ที่ solid

นี่คือเหตุผลที่ **Task Logger** ถึงมี **daily happiness logging** — ไม่ใช่แค่ "track productivity" แต่คือ **buffer builder** — ทุกวันที่คุณ record ว่าวันนี้มีความสุข 7/10 — คุณกำลัง **build evidence** ว่าชีวิตคุณมี meaning — และ evidence นี้คือ **buffer** ที่ทำให้การฝึก Memento Mori work

**⚠️ Caveat ตรง ๆ:** ถ้าคุณกำลังอยู่ใน state ที่ buffer ยังไม่พร้อม (burnout ซ้ำ ๆ, ไม่เห็นคุณค่าในตัวเอง, ไม่มีความสัมพันธ์ที่ solid) — **อย่าเริ่มการฝึก Memento Mori ก่อน** — build buffer ก่อน (เริ่มจากการ record happiness รายวันใน Task Logger — ไม่จำเป็นต้อง "ฝึก" อะไร) — พอ buffer พร้อมแล้ว ค่อยเพิ่ม Memento tab เข้ามา — นี่คือ **order of operations** ที่งานวิจัยแนะนำ

## 05: ประวัติ — "Roman Triumph กับกระซิบข้างหู"

ที่มาที่เล่ากันมากสุด: หลังชัยชนะครั้งใหญ่ของแม่ทัพโรมัน — ในพิธี **Triumph** — ผู้ติดตามจะยืนอยู่ **หลัง** รถม้าของแม่ทัพ แล้วกระซิบ:

> "มemento mori" — "จงจำไว้ว่าเธอจะต้องตาย"

หรือบางเวอร์ชัน: "จงจำไว้ว่าเจ้ายังเป็นมนุษย์" (not a god)

ภาพนี้ฝังลึกในวัฒนธรรมตะวันตก — ตั้งแต่ยุคกลางจนถึง **vanitas** (still life painting ที่มีหัวกระโหลก + ดอกไม้ + นาฬิกาทราย — reminder ว่าทุกสิ่งจะจบ) — และมันยังอยู่ถึงปัจจุบัน: นักแสดง/นักกีฬาหลายคนพูดว่า "memento mori" ก่อนเข้างาน/เข้าแข่ง

⚠️ **คำเตือนเรื่อง accuracy:** เรื่อง "ทาสกระซิบ memento mori" เป็น **tradition ที่เล่ากันมาก** — แต่บางแหล่งทางวิชาการตั้งคำถามว่ามันเป็นข้อเท็จจริงที่พิสูจน์ได้จริงมั้ย — พรจึงเล่ามันเป็น "the well-known tradition" ไม่ใช่ "proven fact" — เพราะ **hard rule: never guess** — และถ้าคุณอยากอ่านต้นตอจริง ๆ — ไปที่ **Meditations** ของ Marcus (section 03) — นั่นคือ primary source ที่ "พิสูจน์" ได้

## 06: Protocol — "ฝึก Memento Mori แบบ 3 ขั้น (MEMENTO-01/02/03)"

### MEMENTO-01: Morning Check (2 นาที / เช้า)
ทุกเช้า — ก่อนเปิด app อะไร — ถามตัวเอง 3 คำถาม:
1. วันนี้ถ้าเป็นวันสุดท้าย — จะทำอะไรมากที่สุด?
2. เรื่องอะไรที่ "เลื่อน" มาหลายวันแล้ว?
3. วันนี้จะ "record" happiness กี่โมง?

**ไม่ใช่ "meditation"** — เป็น **check-in** — เหมือน boot sequence ของระบบ — 2 นาที — แล้วไป

### MEMENTO-02: Weekly Review (15 นาที / สัปดาห์)
ทุกปลายสัปดาห์ — เปิด Task Logger → Insights tab → ดู **weekly digest** (7 วันล่าสุด vs 7 วันก่อนหน้า) + **streak** — แล้วถาม:
- สัปดาห์นี้มีวันไหนที่ "paint" สีเขียว? อะไรทำให้มันเขียว?
- สัปดาห์นี้มีวันไหนที่ "paint" สีแดง? อะไรทำให้มันแดง?
- ถ้าสัปดาห์นี้คือ "สัปดาห์สุดท้าย" — จะทำอะไรมีคนละ?

**นี่คือ "post-mortem" ของสัปดาห์** — ไม่ใช่ "วิเคราะห์ตัวเอง" — แต่เป็น **diagnostic** — เหมือนดู telemetry ว่าระบบทำงานยังไง

### MEMENTO-03: Annual Paint (1 ชม. / ปี)
ทุกวันเกิด (หรือวันใดก็ได้ที่คุณเลือก) — เปิด Task Logger → Memento tab → **scroll ผ่าน life grid ปีที่แล้ว** — ดูว่า "paint" ไปกี่วัน — สีเฉลี่ยเป็นยังไง — แล้ว **paint cell ของวันนี้** — นี่คือ **annual snapshot** — 1 cell ใน 29,200 cells — และมันคือ **evidence** ว่าชีวิตคุณ "เกิดจริง"

**ทำไมต้อง "paint"?** — เพราะ "paint" คือ **action** — ไม่ใช่ "คิด" — มันคือ **commit** — คุณ commit ว่า "วันนี้เกิดขึ้นจริง" — และ commit นี้คือ **buffer** ที่ build ทุกวัน

## 07: Task Logger — "Memento Mori ในฐานะ practice tool"

> **Task Logger** (task-logger.adduckivity.com) = PWA (Progressive Web App) ที่พรสร้างบน **Cloudflare Worker + D1** (SQLite at the edge) + **React + Vite** frontend — multi-user, JWT auth, auto-update

### Core feature: "Memento" tab (ADR 0004)

- **Life Grid** — 80 ปี × 365 วัน = **~29,200 cells** (28 วัน/แถว) เริ่มจากวันเกิดของคุณ
- แต่ละวัน **paint ด้วยสีของ average happiness** (red → amber → green — same gradient as the slider)
- Past days without entries = "lived" (grey); future days = soft outline; **today = highlighted**
- Top block: **days lived** + **days remaining** + **rotating verified Stoic quote** + 1-10 happiness legend
- Auto-scroll: today's row เป็น row ที่ 10 (มี 9 rows ข้างบน)

### v5.1.0 (2026-09-08) — Philosophy layer (ADR 0008)

- **PhilosophyPanel** (collapsible, Thai) — "Memento Mori คืออะไร" — อธิบายปรัชญาแบบเดียวกับบทความนี้: what it is / Stoic roots / Roman triumph / modern psych + "read next" (Meditations, On the Shortness of Life, Letters to Lucilius, Enchiridion)
- **Quote pool** → `frontend/src/quotes.js` — ทุก quote มี `{ text, author, source }` — **verified** (2 quotes ถูก remove เพราะ misattributed: "Every new beginning…" + "Luck is what happens when preparation meets opportunity." — ทั้งสอง **ไม่ใช่ของ Seneca**)
- **"New quote" shuffle** button — กดแล้วเปลี่ยน quote (เดิม = random once per mount)

### ทำไมถึงเป็น "buffer builder"

ทุกวันคุณ record happiness (1-10) + progress (1-10) — system เก็บ **streak**, **weekly digest** (เทียบ 7 วันล่าสุด vs 7 วันก่อนหน้า), **days logged this year** — ทั้งหมดนี้คือ **evidence** ว่าชีวิตคุณมี pattern — และ evidence นี้คือ **buffer** ที่ทำให้การฝึก Memento Mori ไม่กลายเป็น `FEAR_LOCK`

## 08: Pro / Cons — "ตรงไปตรงมา"

### ✅ Pros
- **Free** (PWA, no subscription)
- **Private** (data ใน D1 ของคุณ — multi-user isolation)
- **Installable** (PWA — add to home screen)
- **Auto-update** (service worker)
- **Philosophy + practice ในที่เดียว** (Memento tab = grid + quotes + explainer)
- **Verified quotes** (ทุก quote มี source — ไม่มี misattribution)

### ❌ Cons
- **80 ปี = 29,200 cells** — grid ใหญ่มาก (auto-scroll ช่วย แต่ scroll นานถ้า birthday ค่อนข้างนานมาแล้ว)
- **Happiness = 1-10 slider** — subjective — ถ้าวันนั้นคุณ "ไม่รู้สึก" อะไรเลย — record 5 (กลาง) มั้ย?
- **No offline data** (PWA = app shell only, no offline entries — ADR 0002)
- **Multi-user แต่ single-tenant** (ทุก user = separate JWT — ไม่ share data)

## 09: เหมาะกับใคร / ไม่เหมาะกับใคร

**เหมาะ:**
- คนที่ต้องการ **daily ritual** ที่ช่วยให้ live อย่าง mindful
- คนที่ **neurodivergent** (ADHD/Burnout) ที่ต้องการ "external buffer" — system ที่ช่วย build evidence ของ meaning
- คนที่อยาก **track happiness** (ไม่ใช่ productivity) เป็น metric หลัก
- คนที่อ่าน Stoicism แล้วอยากได้ "practice tool" (ไม่ใช่แค่ read)

**ไม่เหมาะ:**
- คนที่ต้องการ **productivity tracker** (task list, deadlines, Gantt) — Task Logger = reflection tool ไม่ใช่ project manager
- คนที่ต้องการ **offline-first** (PWA นี้ app-shell only — no offline data)
- คนที่ไม่ต้องการ **philosophy** (ถ้าไม่อยากอ่าน Memento Mori — Memento tab อาจเป็น noise)
- คนที่กำลังอยู่ใน `FEAR_LOCK` state (section 02) — build buffer ก่อน

## 10: Duck OS Tie-in — "Memento Mori ในระบบ"

**Law #1: System > Emotion** — Memento Mori คือ **system** ที่ช่วย clarify emotion — มันไม่ได้ "suppress" ความกลัว — แต่ทำให้ **visible** — พอเห็นชัด — ก็จัดการได้

**Law #2: Asset > Activity** — Life grid = **asset** (evidence ของชีวิต) — ไม่ใช่ **activity** (แค่ "do") — ทุก cell ที่ paint = asset ที่ build

**Law #3: Protect System** — Buffer (meaning, self-worth, relationships) = **system integrity** — Memento Mori **protect** buffer นี้ — ถ้า buffer ไม่พร้อม — ระบบจะ "fail" (FEAR_LOCK) — ดังนั้น **protect buffer ก่อน** แล้วค่อย "run" Memento Mori

## 11: บทสรุปจากพร — "Memento Mori = `--verbose` flag ของชีวิต"

ถ้าพรต้องสรุป Memento Mori ในบรรทัดเดียว:

> **Memento Mori = การเปิด `--verbose` flag บนชีวิต — ทุกอย่างชัดขึ้น — ไม่มีอะไรซ่อนตัว — และสิ่งที่ชัดที่สุดคือ: เวลาที่เหลืออยู่ มันจำกัด — และเราควร allocate มันกับสิ่งที่สำคัญจริง ๆ**

Task Logger คือ **practice tool** ที่พรสร้าง — life grid 80 ปี + daily happiness logging + verified Stoic quotes + philosophy explainer — ทั้งหมดนี้คือ **buffer** ที่ทำให้การฝึก Memento Mori **work** แทนที่จะ fail

ถ้าคุณอยากลอง: เปิด [task-logger.adduckivity.com](https://task-logger.adduckivity.com) → sign up (email + password + birthday) → ไป Memento tab → scroll down → คุณจะเห็น life grid ของคุณ — 29,200 cells ที่รอให้ถูก paint

**วันนี้ — cell ที่ highlighted — เป็น cell ของคุณ — paint มันคับ**

#Adduckivity #DuckOS #NeuroDivergent #MementoMori #Stoicism #TaskLogger #Productivity
