# System Diagnostic: Reasons to Quit — Sunk Cost คือ Error ที่ระบบรันต่อโดยไม่ถามว่า "ทำไปทำไม" (Rework Ch.50 × Duck OS)

<!--
ContentID: 20260915-CNT-QUIT-PROCESS
Title: System Diagnostic: Reasons to Quit — Sunk Cost คือ Error ที่ระบบรันต่อโดยไม่ถามว่า "ทำไปทำไม" (Rework Ch.50 × Duck OS)
Slug: system-diagnostic-reasons-to-quit
Type: Core Content (System / Mindset — medium form ~600 words)
Law: Law #1 System > Emotion / Law #2 Asset > Activity / Law #3 Protect System
Series: standalone — ref: critical_thinking_kill_ai (2025-12-07), memento-mori-override-force-quit (2026-03-12), system-audit-foibles-scan (2026-09-06)
Status: draft
Date: 2026-09-15
Sources (verified 2026-09-15):
  - Primary: Rework (Jason Fried & David Heinemeier Hansson, 2010) — "Reasons to Quit" = chapter 50, PRODUCTIVITY section (chapter sequence verified via williammeller.com full TOC + sipreads summary: Illusions of agreement = 49, Reasons to quit = 50, Interruption is the enemy = 51); chapter theme = "Don't throw good time at bad work" (verified loudjet/techneur chapter commentary)
  - Primary: 37signals REWORK Revisited podcast, Season 2 Ep.0031 (Jun 21 2022) "Reasons to Quit with Jason Fried and DHH" (https://37signals.com/podcast/reasons-to-quit/) — fetched live 2026-09-15: DHH quote "Just because you've begun does not mean you need to finish. In fact, in a lot of cases, the best course of action is to quit." + the 8 questions: Why are you doing this? / What problem are you solving? / Is this actually useful? / Are you adding value? / Will this change behavior? / Is there an easier way? / What could you be doing instead? / Is it really worth it? + "Scope hammering" (Shape Up) + The Decision Lab sunk-cost ref
  - User source text (2026-09-15): Sunk Cost Trap + Don't Throw Good Time After Bad Work + 3 Laws mapping (System > Emotion / Asset > Activity / Protect the System)
  - Style: content-study/WRITING_STYLE_GUIDE.md + STYLE_CORPUS.md (2026-09 headingless ".", สรุปแบบวิศวกรเป็ด closer)
  - KB: ~/hermes-agent/duck-os/Main_Data_for_UDO.md (Duck OS Laws)
-->

เคยมีงานที่ลงมือไปแล้ว 3 เดือน แล้วทุกเช้าที่ตื่นมา คุณไม่ได้รู้สึก "อยากทำต่อ" — แต่รู้สึก "ต้องทำต่อ" — เพราะทิ้งไปไม่ได้แล้ว 3 เดือนมั้ยคับ

แล้วสุดท้ายคุณก็ก้มหน้าทำงานต่อ — ไม่ใช่เพราะมันสำคัญ — แต่เพราะ **คุณลงแรงไปเยอะแล้ว**

ถ้าพรจะบอกตรง ๆ เลยนะคับ — **คุณกำลังวินิจฉัยโรคผิด (Misdiagnosis)** — ทุกทีเราคิดว่าการทำงานต่อไปคือ "ความมีวินัย" — แต่ในภาษาวิศวกรรม งานแบบนี้มันคือ **process ที่ crash ไปนานแล้ว แต่ระบบยังส่ง resource เข้าไปไม่หยุด**

.

Rework ของ Jason Fried กับ DHH — ในส่วน Productivity — มีบทสั้น ๆ บทหนึ่งชื่อ **Reasons to Quit** (chapter 50) — และประโยคแกนของบทคือ: **"Don't throw good time at bad work."** (อย่าเอาเวลาดีไปทิ้งกับงานแย่)

บทนั้นตั้งคำถาม 8 ข้อ เพื่อหยุดคนก่อนจะลงแรงเพิ่ม — และ DHH ย้ำใหม่ใน podcast ของ 37signals เอง (REWORK Revisited 2022) ว่า:

> **"Just because you've begun does not mean you need to finish. In fact, in a lot of cases, the best course of action is to quit."**

เริ่มแล้ว ไม่ได้แปลว่าต้องจบ — บางครั้งคำสั่งที่ถูกต้องที่สุดคือ **quit**

.

ในภาษาของระบบ — พฤติกรรมนี้มันมีชื่ออยู่แล้วคับ — **Sunk Cost Trap**

แรงที่คุณลงไป 3 เดือน 6 เดือน 1 ปี — เป็น **ข้อมูลที่ไม่ได้เปลี่ยน decision วันนี้** — เหมือนค่า compute ที่จ่ายไปแล้ว มันไม่ได้อยู่ในสมการว่า "งานนี้ยังคุ้มไหม" — มันอยู่แค่ในหัวคุณ — และสมองมนุษย์รัน bias ตัวนี้อยู่ background ตลอดเวลา โดยไม่ถามก่อนด้วยซ้ำ

ช่องโหว่ที่จริง ๆ ร้ายกว่า sunk cost — คือการ **ไม่กล้าเงยหน้ามาถามว่า "ทำไปทำไม"** — เพราะวินาทีที่คุณถาม — คำตอบอาจเป็น "ก็เพราะลงไปแล้ว 3 เดือน" — ซึ่งเป็น **เหตุผลที่ไม่เกี่ยวกับงาน** — มันเกี่ยวกับ **ความรู้สึก**

.

แล้ว 8 คำถามของ Rework มันหน้าตาเป็นยังไงในภาษา engineer — พรย่อมันให้เป็นโพรโทคอล **QUIT-50** — 3 commands:

**Step 1: `quit --why` (5 นาที, ทุกสัปดาห์ 1 ครั้ง)**

เขียน 1 บรรทัดตอบ: "งานนี้แก้ปัญหาอะไร — ใครได้ประโยชน์ — ถ้าไม่มีใครตอบได้ = งานนี้กำลังรันด้วย inertia ไม่ใช่ด้วยเป้าหมาย" — 8 คำถามของ Rework (ทำไปทำไม / แก้ปัญหาอะไร / มัน useful จริงไหม / คุณกำลัง add value ไหม / มันเปลี่ยนพฤติกรรมใครไหม / มีทางที่ง่ายกว่าไหม / คุณกำลังเสียอะไรไปเพื่อทำมัน / คุ้มจริง ๆ ไหม) คือ checklist ของ command ตัวนี้

**Step 2: `quit --asset-check` (ถาม 2 ข้อ)**

งานนี้สร้าง **Reusable Asset** หรือสร้างแค่ **activity** — asset = ของที่ยังมีค่าแม้คุณหยุด (code ที่คนอื่นใช้ต่อได้, ระบบ, ความรู้,ความสัมพันธ์) — activity = การวิ่งที่หยุดเมื่อขาหยุด — ถ้าคำตอบคือ "หยุดแล้วทุกอย่างหาย" — นั่นไม่ใช่ asset — นั่นคือ loop ที่สูบพลังงาน

**Step 3: `kill --signal 9` (กล้า kill process)**

ถ้า 2 commands ก่อนตอบว่า "ควรหยุด" — **หยุดเลย — ไม่ต้องรอให้เสร็จ** — การ abandon งานที่ไร้ impact ไม่ใช่ความพ่ายแพ้ — มันคือการ **ตัด Technical Debt ทิ้งก่อนระบบล่ม** — และกฎ: ทุกครั้งที่คุณ kill งาน — เขียน 1 บรรทัด "ถ้าต้องเริ่มใหม่ ผมจะเลือกอะไร" — นั่นคือ asset ชิ้นเดียวที่งานทิ้งไว้

Success Criteria: เดือนนี้ — คุณมีอย่างน้อย 1 งานที่ถูก `kill --signal 9` — และ RAM/พลังงานที่คืนกลับมามาถึงงานที่มี impact จริง — วัดจากจำนวนชั่วโมงที่ทำงาน "ต้องทำต่อ" ลดลง

.

**มุมของ Duck OS**

**Law #1: System > Emotion** — Sunk Cost Fallacy คือ **อารมณ์หลอก** — ความเสียดายแรงที่ลงไป เป็น data เก่าที่ cache ไว้ — ระบบที่ดีอ่าน decision จาก input ปัจจุบัน — ไม่ใช่อารมณ์จากการลงทุนเก่า

**Law #2: Asset > Activity** — คำถามเดียวที่ตอบได้ทุกอย่าง: งานนี้หยุดแล้ว **asset** ยังอยู่ไหม — ถ้าอยู่ = คุ้มที่จะทำต่อ — ถ้าหาย = คุณกำลังวิ่งใน loop

**Law #3: Protect System** — การหยุดงานที่ไร้ค่า = **คืน RAM + แบตเตอรี่ให้ระบบรอดไปถึงพรุ่งนี้** — ระบบที่เอาพลังงานไปจ่าย process ที่ crash แล้ว — จะ crash ตามไปด้วยในวันที่ไม่ควร crash

.

โพสต์ Memento Mori Override (2026-03) พรใช้ "ความตาย" เป็น force quit สำหรับ habit — โพสต์ System Audit (2026-09) ใช้ความจริงเป็น diagnostic tool — โพสต์นี้คือเวอร์ชัน **work** — และมันคือรากเดียวกันกับ Critical Thinking (2025-12): สิ่งที่ AI แย่งไม่ได้ไม่ใช่ output — แต่คือ **การตัดสินใจว่า output ไหนควรได้กิน resource**

.

#สรุปแบบวิศวกรเป็ด

ลงแรงไปเยอะ ≠ ต้องทำต่อ — Sunk Cost คือ error ที่ระบบรันต่อโดยไม่ถามว่า "ทำไปทำไม" — และคำสั่งที่แพงที่สุดในชีวิตคุณ ไม่ใช่ start — แต่คือ **kill process ที่ควร kill ไปนานแล้ว**

**Don't throw good time at bad work — kill it, log it, move on.**

ถ้าเดือนนี้คุณมีงานที่กำลัง "ต้องทำต่อ" อยู่ — ลองรัน QUIT-50 กับมันสักครั้ง แล้วมาเล่าให้ฟังนะคับ — ถ้าอยากให้พรทำภาคต่อ Rework บทไหนอีก บอกได้เลยคร้าบ

System > Sunk Cost. Kill the process แล้วคืน RAM ให้ระบบของคุณคับ! 🦆⚡

#Adduckivity #DuckOS #NeuroDivergent #SunkCost #Rework #DeepWork #SystemThinking
