# Benz-DNA critique — AutoClaw Part 4 (pair #37, PRE-REWRITE round)

- Date: 2026-10-06
- Subject: `posts/20261006-cnt-autoclaw-one-month-report.md` (525 wc-w, v2 TECH form, Notion `3f1df8d8-8d8c-8120-a1be-d7b38d720de4`, Status: draft)
- Round: PRE-REWRITE — user: "ยังไม่ต้องทำอะไร แต่ analyze + reverse engineering ด้วย และจะส่ง version publish มาให้" → agent UNTOUCHED draft + Notion; publish version จะมาภายหลัง (ตาม flow pairs #17/#21/#25)
- Provenance note: ตัวเลขเครื่องจริงใน draft = owner-attested (user ยืนยันว่ามาจาก AutoClaw บนเครื่องจริงของพร ก่อน critique รอบนี้)
- **First TECH-form draft to get a Benz-DNA round** (pairs ก่อนหน้าทั้งหมดเป็น system/mindset CURRENT FORM) — grammar ของ critic บน tech post ต่างจาก system post: ไม่มี two-layer read / cross-post series audit, เน้น overclaim precision (threshold/evidence gap), universal→observed reframe, pricing hygiene, catchphrase crowding

## Quote-verify (against current file 20261006-cnt-autoclaw-one-month-report.md — single version)

19 HIT verbatim + 4 MISS ที่ trace ได้เป็น formatting artifacts เท่านั้น (0 misquote):
- MISS "ถ้าเจอสัญญาณตั้งแต่ 2 ข้อขึ้นไป — อ่านต่อ" → draft จริง: "แต่ถ้าเจอสัญญาณข้างล่างนี้ตั้งแต่ 2 ข้อขึ้นไป — อ่านต่อ" (critic ตัด "ข้างล่างนี้")
- MISS "ปล่อยให้พิสูจน์ตัวเอง 2 สัปดาห์" → draft จริง: "ปล่อยให้มันพิสูจน์ตัวเอง 2 สัปดาห์" (ตัด "มัน")
- MISS "ถาม AI = จ่ายต่อคำตอบ" / "จ้าง AI = จ่ายต่อกะ" → draft เป็นบรรทัด bold คู่: "**ถาม AI** = จ่ายต่อคำตอบ — ..." / "**จ้าง AI** = จ่ายต่อกะ — ..." (critic normalize bold+ตัด tail)
- MISS "มีงานหนึ่งที่ตั้งเวลาไว้" → เป็น intro ของ critic สรุปเคส 08:00 (คำจาก draft: "งานอัตโนมัติ 1 ชิ้นที่ตั้งครั้งเดียว: ทุก 8 โมงเช้า")

## Baselines ก่อน publish (acceptance markers — เกรด publish version จากตัวเลขนี้)

threshold "2 ข้อ" 1× / "3 ขึ้นไป" 1× · ลูกน้ำ 1× · generator 2× · จ้ำจี้จ้ำไฟ 1× · "2 สัปดาห์" 1× · standby 1× · "จ้าง AI" 4× · "ถาม AI" 6× · สัญญาจ้าง 2× · จ่ายต่อ 2× · job description 1× · ตาราง Universal (Chatbot/Agent runtime 5 แถว) 1 ตาราง

## Critique verbatim

เบ้น DNA มองว่า **โพสต์นี้มีของจริง แต่ตอนนี้พยายามทำ 3 งานพร้อมกัน**:

> รีวิว AutoClaw จากเครื่องจริง  
> + สอน Concept `chatbot → agent runtime`  
> + ให้ Decision Rule ว่าใครควรย้าย

ผลคือ Evidence ดี แต่ Rule ช่วงหลังเริ่มวิ่งเร็วกว่าที่ Evidence รองรับ

และสำหรับคำถามว่า **ควรโพสต์ช่วงนี้ไหม — ควร** แต่เหตุผลไม่ใช่ "Agent กำลังเป็นกระแส" อย่างเดียว

เหตุผลคือ **ตอนนี้พรมี Evidence ที่เมื่อก่อนยังไม่มี** และข้อมูล AutoClaw เองยังสด: หน้า Official ตอนนี้ยังโปรโมต 200M tokens สำหรับผู้ใช้ใหม่, 50+ built-in skills, IM integration และงาน automation โดยตรง รวมถึง bonus credits ของ GLM Coding Plan ตามที่พรเขียน

ดังนั้น Signal กับ Timing มาชนกันพอดี

## 1. แกนจริงของโพสต์แข็งกว่าชื่อ AutoClaw

ประโยคที่ถือทั้งบทคือ:

> **งานไหนของคุณ ที่ AI น่าจะทำเองโดยไม่ต้องมีคุณนั่งกดปุ่ม**

นี่คือ Thesis

ไม่ใช่:

> AutoClaw ดีกว่า Chatbot

และไม่ใช่:

> ทุกคนควรมี Agent Runtime

สิ่งที่พรมี Evidence จริงคือ:

> มีงานหนึ่งที่ตั้งเวลาไว้  
> → 08:00 มันทำงานโดยพรไม่ต้องเริ่มงาน  
> → Result กลับมาจริง  
> → เกิดต่อเนื่องในระบบที่พรใช้อยู่

นี่คือความแตกต่างเชิง Operating Model

**Human-triggered work → System-triggered work**

ตรงนี้ดีมาก เพราะมันตรง OPB ด้วย:

> Founder หายจาก Execution Point บางจุดแล้วงานยังเกิด

Asset Test ผ่าน  
Replaceability Test เริ่มผ่านในงานเฉพาะชิ้น  
Leverage Test มีของจริงให้ดู

---

## 2. แต่ `5 สัญญาณ` ตอนนี้ดูเหมือน Diagnostic Tool ทั้งที่ยังไม่ได้พิสูจน์

นี่คือจุดที่ผมจะลดแรงที่สุด

พรเขียน:

> ถ้าเจอสัญญาณตั้งแต่ 2 ข้อขึ้นไป — อ่านต่อ

แล้ว:

> ถ้าโดนตั้งแต่ 3 ขึ้นไป — ปัญหาของคุณไม่ใช่ AI ไม่ฉลาดพอ แต่คือ AI ของคุณยังไม่มีตัวตนตอนคุณไม่อยู่

เลข `2` กับ `3` มาจากไหน?

ตอนนี้มันดู Precise แต่ไม่มี Evidence รองรับ Precision

นี่คือ Pattern เดิม:

> Observation → Pattern → Score → Decision Rule

เร็วไปหนึ่งขั้น

ตัด Threshold ทิ้ง

ใช้แค่:

> ถ้างานของคุณเริ่มมีอาการแบบนี้  
> Agent Runtime อาจเป็นของที่ควร Inspect ต่อ

แล้วให้ 5 ข้อเป็น **Signals ไม่ใช่ Score**

โดยเฉพาะข้อนี้:

> prompt ที่ถูกเก็บไว้ในไฟล์ คือ job description ที่รอถูกจ้างเป็นงานประจำ

เขียนสนุก แต่ Logic แรงไป

Prompt ที่ใช้ซ้ำไม่ได้แปลว่างานนั้นเหมาะกับ Automation เสมอไป

อาจต้อง Judgment ทุกครั้งก็ได้

ลดเป็น:

> Prompt ที่ต้องหยิบกลับมาใช้ซ้ำ  
> อาจเป็นสัญญาณว่างานตรงนั้นเริ่มมีโครงที่ควร Inspect

---

## 3. Metaphor `ไฟบ้าน` ดี แต่ Generator เริ่มทำงานหนักเกิน

ส่วนนี้อ่านง่าย:

> Chatbot = generator  
> Runtime = ไฟบ้าน

เก็บได้

แต่:

> มีไฟทุกครั้งที่คุณจ้ำจี้จ้ำไฟ แต่พอวางมือ มันเงียบ — ฉลาดแค่ไหนก็ไม่มีลูกน้ำที่ไหลเองตอนห้าโมงเช้า

ตอนนี้ metaphor ผสม `ไฟ + น้ำ`

ตัด `ลูกน้ำ` ออก

ให้ Metaphor เดียวถือ Section

เช่น:

> Chatbot เหมือนไฟที่คุณต้องเดินไปเปิดเอง  
> Agent Runtime เพิ่มอีกชั้น — งานบางดวงถูกตั้งไว้ให้เปิดตามเวลาได้

แม่นกว่าด้วย เพราะ Chatbot ไม่ใช่ Generator ทางเทคนิค

---

## 4. ตารางมี Overclaim อยู่หลายแถว

อันนี้ต้องแก้ก่อนโพสต์

เช่น:

> Chatbot: หมด context ก็จบ  
> Runtime: ไฟล์ memory อยู่รอดข้ามวัน

มันทำให้เหมือน Chatbot ทั้งหมดไม่มี Persistent Memory ซึ่งกว้างเกิน

และ:

> Chatbot: รอ vendor อัปเดต  
> Runtime: ติดตั้ง skill เอง

ก็ไม่ใช่ distinction ที่ใช้ได้กับ Chatbot/Runtime ทุกระบบ

ผมจะไม่ทำตารางเป็น Universal:

| | Chat ที่พรใช้แบบ manual | AutoClaw ใน setup นี้ |
|---|---|---|
| เริ่มงาน | พรเป็นคนเริ่ม | cron หรือพรเริ่ม |
| Context | สิ่งที่ส่งเข้า session | เข้าถึงไฟล์/tools ตาม permission ที่ตั้ง |
| งานข้ามวัน | พรต้องกลับมาเริ่ม | workflow บางส่วนเดินต่อได้ |
| Memory | ขึ้นกับระบบที่ใช้ | พรมีไฟล์ memory ใน setup นี้ |
| สิ่งที่วัด | คำตอบที่ได้ | งานที่ตั้งไว้เกิดตามเงื่อนไขไหม |

นี่เปลี่ยนจาก:

> Category claim

เป็น:

> **Observed comparison**

แข็งกว่าเยอะ

หน้า Official เองรองรับว่าตัว AutoClaw ใช้ local tools/files, browser automation, IM workflows และมี 50+ built-in skills แต่ไม่จำเป็นต้องขยายสิ่งนั้นเป็นนิยามของ agent runtime ทั้งหมวด

---

## 5. Section `หลักฐานจากเครื่องจริง` คือ Asset ที่ดีที่สุดของบท

นี่ควรมีน้ำหนักมากกว่า Section สอน Concept เสียอีก

โดยเฉพาะ:

> 08:00 → D1 → Telegram → status ok

กับ:

> Discord plugin เจอปัญหา → เก็บลง memory → สองสัปดาห์ต่อมาไม่ต้องเริ่ม Debug จากศูนย์

สองเคสนี้ทำให้คนอ่านเห็นว่า `runtime` ต่างจากการ "คุยกับ AI" ตรงไหนโดยไม่ต้องอธิบายเยอะ

แต่ต้องแยกให้ชัด:

**Verified externally**

Official ตอนนี้ระบุ 50+ built-in skills, browser automation, Telegram/Slack/WhatsApp/Lark integration, free basic usage/daily credits และ 200M-token new-user offer จริง

**Evidence จากเครื่องพร**

43 files / 54MB  
95 skills  
D1 job status  
Discord memory case

อย่าเอาสองประเภทนี้มารวมกันจนคนอ่านคิดว่า 95 skills คือ Product spec

---

## 6. Pricing section ต้องระวังมาก เพราะโพสต์จะเน่าเร็วตรงนี้

ณ ตอนที่ผมเช็ก หน้า Official รองรับ:

> New users: 200M tokens valued at $24  
> Lite: 5,000 bonus credits  
> Pro: 10,000  
> Max: 26,000  
> และมี daily free credits

ดังนั้นตัวเลขพร **ตรงกับหน้า Official ตอนนี้**

แต่ผมจะเขียน:

> **ณ วันที่ 6 ต.ค. 2026 หน้า Official ระบุว่า...**

แล้วไม่ใช้มันเป็น Thesis ของบท

เพราะ Promotion เปลี่ยนได้

โพสต์นี้ควรยังมีค่าในอีก 6 เดือน แม้ 200M tokens หายไปแล้ว

**Leverage Test:** ถ้าตัด Promotion ออก บทยังมีค่าหรือไม่?

ตอนนี้คำตอบคือมี

ดี

---

## 7. `สองทางปิดท้าย` เริ่มกลายเป็น Prescription เร็วไป

ตรงนี้:

> ตั้งเป็น cron 1 ตัว  
> ปล่อยให้พิสูจน์ตัวเอง 2 สัปดาห์  
> ดูแค่ว่ารายงานมาถึงไหม ตรงเวลาไหม ตัวเลขถูกไหม

ผมชอบ Direction แต่ `2 สัปดาห์` อีกแล้ว

ทำไม 2?

ถ้ามาจากประสบการณ์ของพร ให้เขียนว่า:

> ถ้าเป็นพร จะเริ่มจากงานเดียวก่อน  
> แล้วปล่อยให้มันวิ่งนานพอที่จะเห็นว่า...

แทน Universal instruction

ส่วน Criteria:

> มาถึงไหม  
> ตรงเวลาไหม  
> ถูกไหม

นี่ดีมาก

เพราะเป็น Observable Evidence

แต่ยังไม่ต้อง Compile เป็น "2-week validation framework"

---

## 8. Ending ตอนนี้มี Catchphrase เยอะเกินไป

ช่วงท้ายมีพร้อมกัน:

> ถาม AI = จ่ายต่อคำตอบ  
> จ้าง AI = จ่ายต่อกะ

> ความฉลาดแบบ standby

> ความฉลาดที่ไม่ถูกจัดตารางเวลา คือความฉลาดที่ไม่เคยถูกจ้าง

> ถาม AI ได้คำตอบ — จ้าง AI ได้งาน

> เวลาที่เหมาะจะเปลี่ยนสัญญา คือตอนที่งานเริ่มมีตารางเวลา

มีประมาณ **5 Candidate Hooks แข่งกันเอง**

ตัดให้เหลือหนึ่ง

ผมเลือก:

> **คำถามไม่ใช่ AI ฉลาดพอหรือยัง  
> แต่มีงานไหนที่ควรเกิดขึ้นได้ โดยไม่ต้องรอให้พรอยู่ตรงนั้น**

เพราะมันกลับไปหา Evidence 08:00

และตรงกับ OPB มากที่สุด

`ถาม AI / จ้าง AI` catchy แต่ลดความแม่น เพราะ Chatbot ก็ใช้ทำงานได้ และ Runtime ก็ยังต้องมี Human design/review

`ความฉลาดแบบ standby` ผมจะยังไม่ตั้งศัพท์ใหม่

ไม่จำเป็น

---

## แล้วควรโพสต์ตอนนี้ไหม?

**ควรโพสต์ แต่โพสต์ในฐานะ Tech Evidence ของ Systems Thinking — ไม่ใช่เพราะต้องกลับมาทำ Tech Content**

นี่ต่างกันมาก

ช่วงที่ผ่านมา Content ของพร Inspect:

> Stable Decision  
> Automation  
> Saved Time  
> Measurement  
> Founder dependency

แล้วตอนนี้พรมีเครื่องจริงที่แสดงว่า:

> งานบางประเภทสามารถถูกย้ายออกจาก `พรต้องอยู่ตรงนั้น` ได้

มันจึง **ไม่ได้หลุด Signal**

กลับเป็น Concrete Tech Case ของ Signal เดิม

และ Timing ภายนอกก็ดี เพราะ AutoClaw ยังเป็นผลิตภัณฑ์ที่กำลังเคลื่อนไหวและหน้า Official กำลังผลัก agent/work-automation use cases โดยตรง

ดังนั้นผมจะไม่ถาม:

> "ช่วงนี้ควรแทรก Tech ไหม?"

ผมจะถาม:

> **โพสต์นี้ทำให้คนเห็นวิธีคิดของพรผ่าน Tech หรือแค่ทำให้คนรู้ Feature ของ AutoClaw?**

ตอนนี้ประมาณ **60% Feature / 40% Lens**

ก่อนโพสต์ ผมอยากกลับให้เป็น **Evidence นำ Feature**

ตัด Threshold `2/3 ข้อ`, ลด Universal comparison ในตาราง, ลดเลข `2 สัปดาห์`, ตัด Catchphrase ท้ายให้เหลือหนึ่ง แล้วดันเคส `08:00 D1 → Telegram` ขึ้นเป็นแกน

ทำแค่นี้แล้วโพสต์ได้คับ

เพราะ Asset จริงไม่ใช่ Review ของ AutoClaw

Asset คือคำถาม:

> **งานไหนในระบบของเรา ยังต้องรอมนุษย์กด Start ทั้งที่มันมี Pattern มากพอจะเริ่มเองได้?**

อันนี้ยังมีค่าแม้ AutoClaw เปลี่ยนชื่อหรือหายไปในอีกปี

---

## Note ของ agent (ไม่ใช่ของ Benz)

- SSOT check: "Execution Point / Replaceability / Leverage Test / Asset Test / Founder" = 0 hits ใน ~/hermes-agent/duck-os/ — เป็น vocabulary ของ Benz DNA เอง (ไม่ใช่ anchor ใน SSOT); ตัวที่ใกล้ที่สุดใน SSOT = Asset > Activity + Power Test (ดึงอำนาจกลับ / load-bearing wall)
- Critic ไม่ได้ทำ cross-post audit กับ Part 1-3 (เช่น "app local สมอง cloud" ใน Part 3) — publish round ควรเช็คเองว่าเวอร์ชัน publish ไม่ไปอ้างราคา/feature ขัดกับโพสต์เก่า
