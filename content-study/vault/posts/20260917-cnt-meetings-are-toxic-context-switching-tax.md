# System Diagnostic: Meetings Are Toxic — ประชุม 1 ชั่วโมงไม่เคยกินเวลาแค่ 1 ชั่วโมง (Rework Chapter 5 × Duck OS)

<!--
ContentID: 20260917-CNT-MEET-TOXIC
Title: System Diagnostic: Meetings Are Toxic — ประชุม 1 ชั่วโมงไม่เคยกินเวลาแค่ 1 ชั่วโมง (Rework Chapter 5 × Duck OS)
Slug: system-diagnostic-meetings-are-toxic
Type: Core Content (System / Mindset — medium form ~600 words)
Law: Law #1 System > Emotion / Law #2 Asset > Activity / Law #3 Protect System
Series: Rework rework — ref: 20260915-cnt-system-diagnostic-reasons-to-quit (2026-09-15), 20260913-cnt-real-artifact-single-source-of-truth (2026-09-13), 20260916-cnt-interruption-glitch-alone-zone-protocol (2026-09-16)
Status: draft
Date: 2026-09-17
Sources (verified 2026-09-17):
  - Primary: Rework (Jason Fried & David Heinemeier Hansson, 2010) — chapter "Meetings are toxic" (p. 108): "The worst interruptions of all are meetings." / "They usually convey an abysmally small amount of information per minute." / 1-hr x 10-person meeting = "at least ten productivity hours lost. More likely fifteen because of context switching." / "Meetings procreate… one leads to another." — verified via 37assets excerpt mirror (yumpu p.108) + loudjet.com/a/rework + webnovel chapter-by-chapter upload + williammeller.com full TOC (wayback 2026-05)
  - Chapter number: user instruction = "chapter 5" (2026-09-17, explicit correction — previous draft's "chapter 50" was Hermes's unverified error, flagged to user). Continuous TOC count + webnovel per-chapter upload number this chapter 33; number deliberately left OUT of the title, body follows user's "chapter 5"
  - 37signals REWORK podcast (Feb 2018 + Season 2 2022, 37signals.com/podcast/meetings-are-toxic/): "Meetings are the worst type of interruption. A one-hour meeting with five people is actually five hours of productivity lost. They're also horrible at conveying information."
  - Neuroscience (cross-verified in 2026-09-16 draft): Gloria Mark, UC Irvine — 23 min 15 s to refocus; Sophie Leroy, U Minnesota — Attention Residue
  - User source text (2026-09-17): System Diagnostic — The Context Switching Tax / The Worst Interruption / Hardware Degradation + 3 Laws filter (FOMO / REAL-01 / firewall + async + Alone Zone)
  - Style: content-study/WRITING_STYLE_GUIDE.md + STYLE_CORPUS.md (2026-09 headingless ".", สรุปแบบวิศวกรเป็ด closer)
-->

เคยมีวันที่คุณประชุม 1 ชั่วโมง 2 รอบ 3 รอบ — แล้วพอตกเย็นมองกลับ — งานสำคัญที่สุดของวันนี้ มันยังไม่ทันเริ่มเลยมั้ยคับ

คุณบอกตัวเองว่า "ก็มันเรื่องงาน" "ก็ต้องเข้าประชุมเพื่อแสดงความร่วมมือ" "ก็ไม่เข้าแล้วจะรู้เรื่องอะไร"

แล้วพรจะบอกตรง ๆ เลยนะคับ — **คุณกำลังวินิจฉัยโรคผิด (Misdiagnosis)** — ทุกทีเราคิดว่าการประชุมคือ Collaboration — แต่ในภาษาวิศวกรรม มันคือ **FORCED SYSTEM-WIDE INTERRUPT** — คำสั่งบังคับให้ process ทุกตัวในห้อง stop พร้อมกัน เพื่อมารอฟังข้อมูล

.

Rework ของ Jason Fried กับ DHH มีบทชื่อ **Meetings Are Toxic** (chapter 5) — และเปิดบทด้วยประโยคนี้:

> **"The worst interruptions of all are meetings."**

(ในบรรดาสิ่งขัดจังหวะทั้งหมด — การประชุมคือ interrupt ที่แย่ที่สุด)

บทเดียวกันคำนวณให้ดูว่า: ประชุม 1 ชั่วโมง x คน 10 คน = **"at least ten productivity hours lost. More likely fifteen because of context switching."** — เสียอย่างน้อย 10 ชั่วโมงของ productivity — และน่าจะ 15 ชั่วโมง เพราะ context switching

.

ในภาษาของระบบ — ทุก invite ประชุมมี 3 error ซ่อนอยู่:

**Error 1: The Context Switching Tax** — ประชุม 1 ชั่วโมงไม่เคยกินเวลาแค่ 1 ชั่วโมง — ภาษามันคือ **Mental Switching Cost** — งานเดิมที่หยุดกลางทาง (Gloria Mark จาก UC Irvine วัดไว้: สมองใช้เวลาเฉลี่ย 23 นาที 15 วินาที กว่าจะกลับเข้า focus เดิม) + เวลาเตรียมตัวเข้าประชุม + เวลาพยายามกู้คืนสมาธิเดิมหลังประชุม — รวมกันแล้ว ประชุม 1 ชั่วโมง = ระบบหลุด focus ไปครึ่งวัน

**Error 2: The Worst Interruption** — Rework ระบุตรง ๆ ว่าการประชุม **"usually convey an abysmally small amount of information per minute"** — ปริมาณข้อมูลต่อหนึ่งนาทีต่ำมาก — เพราะมันบังคับให้ทุกคน stop process พร้อมกัน เพื่อมารอฟัง **ข้อมูลที่ส่วนใหญ่สามารถสรุปเป็นข้อความสั้น ๆ ได้** — และ Rework ย้ำ: **"Meetings procreate… one leads to another."** — ประชุมมัน spawn ตัวเอง — follow-up → follow-up → follow-up

**Error 3: Hardware Degradation** — การถูกลากเข้าประชุมบ่อย ๆ บังคับให้สมองส่วนหน้า (Prefrontal Cortex) ต้องเคลียร์ cache ของงานเดิม แล้ว load context ใหม่ของประชุม — แล้วหลังประชุมก็เคลียร์อีกครั้งเพื่อกลับงานเดิม — **cache thrashing** — ผลคือแบตเตอรี่ระบบหมดเกลี้ยงก่อนจะทันเริ่มรันงานหลัก — และ Attention Residue (ตะกอนสมาธิของงานเก่า) ก็ค้างอยู่ในหัวทุกครั้งที่สวิตช์

.

แล้ว filter ผ่าน 3 Laws ของ Duck OS มันหน้าตาเป็นยังไง — พรย่อมันให้เป็นโพรโทคอล **MEET-01 — The Meeting Firewall** — 3 commands:

**Step 1: `meet --refuse` (ก่อนรับทุก invite — 30 วินาที)**

ถาม 3 ข้อ: (1) เรื่องนี้สรุปเป็นข้อความ 3 บรรทัดได้ไหม (2) คุณจำเป็นต่อการตัดสินใจ หรือแค่ไปรับทราบ (3) ความหนาแน่นของข้อมูล คุ้มกับ Context Switching Tax ไหม — ถ้า 2 ใน 3 ตอบ "ไม่" = **refuse** — ความรู้สึก "ไม่เข้าแล้วจะดูไม่ร่วมมือ" หรือ FOMO คืออารมณ์ — ระบบที่ดีไม่รับ invite ด้วยอารมณ์

**Step 2: `meet --async` (default ของทีม)**

สลับการสื่อสารเป็น **Asynchronous** — ข้อมูล = ข้อความสั้น + **Artifact ของจริง** (ref: REAL-01 — ของจริง 1 ชิ้น = cache ที่ทุกคนแชร์) — ประชุมเหลือไว้สำหรับ **decision** เท่านั้น — ไม่ใช่สำหรับ **การแจ้ง** — การนั่งคุยวนไปมาในห้องประชุม = Activity ที่สูญเปล่า — งานไม่เดิน

**Step 3: `meet --firewall` (ป้องกัน Process หลัก)**

**The Alone Zone** ของคุณ = firewall — ปัก status, ปิด sync ทุกทางระหว่างบล็อกนั้น — และสำหรับประชุมที่ refuse ไม่ได้ — ยึด 5 กฎของ Rework: **ตั้ง timer (ดัง = จบ) / เรียกคนน้อยสุด / agenda ชัด / เริ่มที่ problem / จบด้วย solution + เจ้าของ** — ประชุม 1 ชั่วโมงห้ามยืดเป็น 3 ชั่วโมง

Success Criteria: เดือนนี้ — มีอย่างน้อย 3 ประชุมที่ถูก refuse หรือแปลงเป็น async — จำนวน follow-up ประชุมที่ spawn ตัวเองลดลง — และ The Alone Zone ของคุณรอดถึงปลายสัปดาห์

.

**มุมของ Duck OS**

**Law #1: System > Emotion** — "เข้าประชุมเพื่อแสดงความร่วมมือ" คือ **อารมณ์หลอก** — การสละเวลาไปนั่งเฉย ๆ เพื่อให้คนอื่นสบายใจ คือการรันระบบด้วยอารมณ์ — ระบบที่ดีอ่านค่าของ decision — ไม่ใช่อารมณ์ของห้อง

**Law #2: Action Precedes Motivation (Asset > Activity)** — ประชุม 3 ชั่วโมงที่จบแบบไม่มี solution ไม่มีเจ้าของ = **activity ที่หายไปในอากาศ** — artifact 1 ชิ้น + ข้อความ 3 บรรทัด = **asset** ที่ยังอยู่พรุ่งนี้ — เลิกจัดประชุมเพื่อคุยไอเดียลอย ๆ — วางของจริงลงบนโต๊ะแทน

**Law #3: Protect the System** — การปฏิเสธการประชุมที่ไม่จำเป็น = **การตั้ง firewall ให้ Process หลักไม่ให้พัง** — Asynchronous คือ default — sync คือ exception — The Alone Zone คือที่ที่งานสำคัญจริง ๆ ถูก compile

.

โพสต์ที่แล้วพรเขียนเรื่อง **Reasons to Quit** (Rework) — ตอนนั้นพรบอกว่าการ kill process คือคำสั่งที่แพงที่สุด — โพสต์นี้คือภาค "ไม่เปิด process ไร้ค่าตั้งแต่แรก" — และมันเชื่อมตรง ๆ กับ Interruption Glitch (2026-09) ที่พรใช้ The Alone Zone + SLEEP-07 — เพราะศัตรูตัวเดียวกัน: **การถูก interrupt จนระบบไม่มีวันปิดงาน**

.

#สรุปแบบวิศวกรเป็ด

ประชุม 1 ชั่วโมงไม่เคยกินเวลาแค่ 1 ชั่วโมง — มันคือ Context Switching Tax ที่ขโมยวันทั้งวัน — และ invite ที่คุณ "รับเพราะเกรงใจ" คือ interrupt ที่คุณอนุญาตให้ kill Process หลักของคุณเอง

**The worst interruptions of all are meetings — so make the meeting an exception, not the default.**

ถ้าสัปดาห์นี้คุณมีประชุมที่ "น่าจะเป็นข้อความ 3 บรรทัดได้" — ลองรัน MEET-01 กับมัน แล้วมาเล่าให้ฟังนะคับ — ถ้าอยากให้พรทำภาคต่อ Rework บทไหนอีก บอกได้เลยคร้าบ

System > Meetings. ตั้ง firewall แล้วรันงานหลักของคุณคับ! 🦆⚡

#Adduckivity #DuckOS #NeuroDivergent #Meetings #ContextSwitching #AsyncFirst #DeepWork #Rework
