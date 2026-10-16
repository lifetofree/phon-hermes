# 45 wpm กับ 220 wpm — ช่องทางที่ช้ากว่าคือตัวที่คุณยังใช้พิมพ์อยู่

### ตัวที่ให้ raw text รอแก้ กับตัวที่ให้ข้อความที่กดส่งได้

<!--
ContentID: 20261016-CNT-WISPR-FLOW
Series: standalone tool review — ref: 20260917-cnt-orca-ade-parallel-coding-agents (2026-09-17, v2 TECH form)
Type: v2 line-per-sentence TECH form (stat-line / signals / mental model / table / two-fork)
Status: Draft r1 — self-rewrite pre-critique (user direction 2026-10-16: "self-review ตามกฎ corpus แล้ว self-rewrite คง spine เดิม" — pair #46 r1 / #48 r1 pattern)
R1 SELF-REVIEW (v1 findings, fixes applied):
- FORM: v1 ใช้ H2 ล้วน 14 หัว (top sections ต้องเป็น `#`, signals `## 1.`–`## 5.` ซ้อนใต้ `# 5 สัญญาณ`) — แก้ตาม canonical v2; ใส่ `###` subtitle ที่หายไป; `#สรุปแบบวิศวกรเป็ด` เป็น H1
- CLOSER: 🦆⚡ + "System > Keyboard." sign-off ถูกตัด (v2 closer rule — แยกจาก 2026-09 สายเก่า, corpus wins); คับ particle 2→1 (เหลือแค่บรรทัด "คำถามที่แท้จริง…คับ")
- SSOT UNLABELED: "First Principle: User ≠ Machine" label + `≠` ออกจาก body — เหลือหลักเป็นภาษาไทยไม่ติดป้าย (mapping คงไว้ใน header นี้)
- BORROWED-LINE (EN #149): caveat v1 ยม canonical sample verbatim ("Evidence ที่ต่อเนื่องกว่า") → เขียนใหม่เป็นถ้อยคำของโพสต์นี้ (ใครเป็นคนทำขั้นแก้)
- EVIDENCE SPECIFICS (EN #108 class): ชื่อตัวอย่าง "Adithya / Guillain-Barre / Andreessen Horowitz" ไม่มี receipt จาก source — แทนด้วย class ของคำ; ตัวอย่าง self-correction ติดป้าย "feature ที่หน้าเว็บเขาโชว์"
- REGISTER: คุณ 28→7 / พร 2→5 (expert-credence lines) / bold ลดเหลือ thesis + killer lines + pricing tiers
- HONESTY: stat-line เติม "ที่ Wispr บอกว่า" (evidence-status verb, rule 178); pricing "ณ วันที่ตรวจ"; funding เหลือบริบท 1 บรรทัด
- v1 snapshot: web-archive/20261016-wispr-flow-voice-dictation-v1.md
Sources (researched live 2026-10-16, primary):
- wisprflow.ai (homepage, fetched live 2026-10-16): "4x faster than typing" — Keyboard 45 wpm vs Flow 220 wpm (vendor demo, not independent test)
  + features: filler removal / punctuation / formatting / self-corrections / 100+ languages auto-detect / personal dictionary /
  snippets / per-app style (Formal-Casual-Very casual) + "no plugins required... wherever your cursor is" +
  privacy: "never sold" + opt-in data use + SOC 2 Type II / ISO 27001 / HIPAA + testimonials
  (Steven Bartlett "gap between my thought and my delivery collapses", Alex Lieberman "I literally do not use my fingers to type anymore",
  Elena Verna, Dave Gilboa Warby Parker)
- wisprflow.ai/pricing (fetched live 2026-10-16): Free $0 = 2,000 words/week desktop + 1,000/week mobile, 100+ languages,
  dictionary+snippets, limited Notetaker, "no trial countdown or credit card" / Pro $15/user/mo monthly = $12/user/mo annual (20% off)
  = unlimited dictations + Notetaker longer history + shared dictionary + team analytics / Growth $33→$23 = SSO SAML + enforced HIPAA BAA
  + admin model-training control / Enterprise custom = SCIM, audit logs, MDM, model training locked off, domain capture
  + students/educators 50% off + Notetaker full access promo "through October 31"
- wisprflow.ai/why-flow (fetched live 2026-10-16): Zero-Edit Rate Benchmark — Wispr Flow 90% / OpenAI 71% / ElevenLabs 63% / Siri 52%
  (SOURCE = Wispr's own benchmark — vendor-reported, no independent replication found) + "most people save over an hour a day" (vendor claim)
  + "we predate OpenAI's Whisper" + dev features: camelCase/snake_case, file tagging in Cursor+Windsurf, tool names
  + Wall Street Journal quote "replaces built-in voice transcription with a model that's scary good"
- docs.wisprflow.ai "What is Wispr Flow?" (fetched live 2026-10-16): internet REQUIRED for transcription; Mac = hold Fn,
  Windows = Ctrl+Win (customizable; Mac without Fn = Ctrl+Option); iPhone = Flow keyboard; Android = Flow Bubble (hidden in password
  fields); desktop inserts completed text AFTER stop, not live word-by-word; dictation history stored on-device, deletion permanent
- wisprflow.ai/notetaker (fetched live 2026-10-16): Mac + Windows only (mobile on roadmap); NO bot joins the meeting (runs on your device);
  transcript with named speakers + topic-organized summary + next steps; "What did I miss?" catch-up; Ask-across-meetings + web search;
  MCP = use notes in Claude/ChatGPT; works in-person too; zoom/meet/teams/slack huddles
- wisprflow.ai/new-funding (via search, dated 2025-11-20): $25M new funding led by Notable Capital w/ Steven Bartlett's Flight Fund,
  total ~$81M, "to build the Voice OS" (secondary confirmation: vctavern 2026-04-26, aivoicenewsletter 2026-04-14)
SSOT anchors (verified 2026-10-16, used UNLABELED in body): First Principle "User ≠ Machine — Productivity พังเพราะใช้ระบบผิดประเภท"
= ~/hermes-agent/duck-os/Main_Data_for_UDO.md:38 (input-channel bottleneck framing); Asset>Activity (งานที่ควรเป็น asset ไม่จมเป็น activity)
Benchmarks: NOT self-run — all speed/accuracy numbers are vendor-reported (Anti-Hype note in body).
Candidate hooks (for critique round): (1) 45 vs 220 stat-line (used) (2) "พิมพ์มาทั้งชีวิต — แต่ไม่เคยถามว่ามือมันเร็วได้สุดที่เท่าไร"
(3) "คุณไม่ได้พิมพ์ช้า — คุณใช้ช่องทางที่ช้ากว่าคิด"
-->

คุณพิมพ์เร็วแค่ไหน

.

45 wpm คือค่าเฉลี่ยความเร็วพิมพ์ของคีย์บอร์ด

220 wpm คือความเร็วที่ Wispr บอกว่าเสียงของคุณคิดได้จริง

.

ถ้าของเดิมทำงานได้ — ไม่ต้องเปลี่ยน

โพสต์นี้ไม่ได้มาให้เลิกพิมพ์คีย์บอร์ด

มันมาสำหรับคนที่ "พิมพ์ด้วยเสียงแล้วต้องแก้" — คนที่ voice input ในตัวให้มาทั้งก้อน แล้วต้องนั่งขัดทั้งก้อนก่อนกดส่ง

.

คำถามที่แท้จริงของโพสต์นี้คับ:

> **เมื่อไหร่ที่ "พิมพ์ด้วยเสียง" ในตัวยังพอ — และเมื่อไหร่ที่มันเริ่มไม่พอ**

.

# 5 สัญญาณว่า voice input ในตัว เริ่มไม่พอ

## 1. แก้ข้อความหลังหยุดพูด ทุกครั้ง

voice input ในตัว (Siri / Apple Dictation / Gboard / Windows) transcribe ตรงตัว — ทุก "เอ่อ" ทุกจุดที่พูดผิด ทุกครั้งที่คิดใหม่

พูดว่า "นัดบ่าย 3 — เอ้ย บ่าย 4" — มันเขียนทั้ง 3 และ 4 ลงไป — แล้วคนแก้คือมือที่พิมพ์ตาม

Flow ออกแบบมาเพื่อจุดนี้ — ตัด filler จับการแก้กลางประโยค ได้เวอร์ชันสุดท้ายกลับมา (feature ที่หน้าเว็บเขาโชว์ — ยังไม่ได้วัดเอง)

## 2. ได้ "กำแพงข้อความ" กลับมา ไม่ใช่ข้อความที่ส่งได้

ตัวในตัวใส่จุดได้ — แต่ไม่จัด list ไม่แยกย่อหน้า ไม่จัดโครงอีเมล

Flow จัด format ระหว่างพูด — numbered list ย่อหน้า โครงอีเมล — จากประโยคที่พูดไปเรื่อย ๆ

## 3. ชื่อคน ศัพท์เฉพาะ — ผิดซ้ำทุกวัน

ตัวในตัวไม่มี context ของผู้ใช้ — ชื่อที่สะกดไม่แบบพจนานุกรม ศัพท์เฉพาะทีม ชื่อระบบภายใน = นั่งแก้ซ้ำเป็นวิธีการทำงาน

Flow มี personal dictionary — เพิ่มคำเองได้ ครั้งต่อไปสะกดถูก (docs + homepage)

## 4. prompt AI ด้วยนิ้ว — แล้ว AI ได้บริบทครึ่งเดียว

พิมพ์ต้องสรุป — พูดจะเล่าครบ — homepage อ้างว่าคนใช้ Flow ให้ context เยอะขึ้นมากตอน prompt ChatGPT/Claude

ข้อนี้เป็น claim ของ vendor — พรยังไม่ได้วัดเอง — แต่มันตรงกับประสบการณ์ที่หลายคนเล่าเหมือนกัน

## 5. พิมพ์ใน 5 แอป — แต่ละแอปมี voice ของมันเอง

Gboard มีของ Gboard — Apple มี dictation — Cursor มี voice mode — 5 ตัว 5 quirk

Flow = ตัวเดียว — cursor อยู่ที่ไหน พูดได้ที่นั่น — "If you can type there, you can Flow there" — Mac / Windows / iPhone / Android

.

# Flow = Post-Processing Layer ไม่ใช่ "เครื่องพิมพ์ดีดเสียง"

raw transcription คือขั้นแรกเท่านั้น — ตัวในตัวจบที่ขั้นนั้น

Flow เติมชั้นหลัง: จับการแก้ตัวเอง จัด format ใส่คำศัพท์ส่วนตัว ปรับ tone ตามแอป (Formal / Casual / Very casual)

**คุณต้องการ raw transcript หรือข้อความที่กดส่งได้เลย?**

ตัวในตัวก็แต่งได้ — ถ้ายอมนั่งแก้เองทุกครั้ง — ความต่างไม่ได้อยู่ที่ความสามารถ อยู่ที่ว่าใครเป็นคนทำขั้นแก้ — เครื่อง หรือมือ

.

# เปรียบเทียบ — Flow vs ตัวในตัว vs voice mode ของแอป

| | Wispr Flow | Built-in (Siri/Apple/Gboard) | ChatGPT/Cursor voice mode |
|---|---|---|---|
| Zero-edit rate | 90% (vendor bench) | 52% Siri (vendor bench) | n/a — วัดต่างเกณฑ์ |
| ใช้ข้ามแอปทุก device | ได้ — 1 app ทุก text field | จำกัด — ยึด ecosystem ของมัน | ไม่ได้ — ในแอปตัวเองเท่านั้น |
| จัด format/list/email | ได้ — ระหว่างพูด | ไม่ได้ — raw text | แล้วแต่แอป |
| คำศัพท์ส่วนตัว + style ต่อแอป | ได้ | ไม่ได้ | จำกัด |
| ราคา | Free 2,000 คำ/สัปดาห์ | $0 | ตาม subscription ของแอป |
| Platform | Mac/Win/iOS/Android | ตาม device | ตามแอป |

One-line จากตาราง: **ตัวในตัว = raw text รอแก้ / Flow = ข้อความที่กดส่งได้ — ส่วน voice mode ของแต่ละแอป = ของดี แต่ติดอยู่ในแอปตัวเอง**

.

# ตัวเลข — และสิ่งที่พรต้องบอกตรง ๆ

220 wpm / "4x faster" / "save over an hour a day" / zero-edit 90% — ทั้งหมดเป็นตัวเลขจาก vendor (wisprflow.ai) — benchmark ที่เทียบ Siri/OpenAI/ElevenLabs ก็รันโดย Wispr เอง

พรไม่ได้ลง Flow ไว้บนเครื่องนี้ — ไม่มีการวัดเอง — ตัวเลขข้างบนคือ claim ที่ควรไป verify กับ 2,000 คำฟรีของตัวเอง — และไม่ควรเอาไปเทียบเครื่องอื่นโดยไม่ควบคุมเงื่อนไข — ถ้าใครมี independent benchmark เทียบตรง ๆ ส่งมาในคอมเมนต์ได้เลย

ข้อควรรู้จาก docs (ไม่ใช่ marketing):

— ต้องมีอินเทอร์เน็ตตอน transcribe
— desktop ใส่ข้อความหลังหยุดพูด — ไม่ใช่พิมพ์ตามคำแบบ live
— AirPods / Bluetooth earbuds ลดความแม่นยำ (docs แนะนำไมค์ในตัวเครื่อง)
— dictation history เก็บบน device — ลบแล้วหายทุก platform

.

# Notetaker — ของแถมใน subscription เดียว

Wispr Notetaker (Mac + Windows, mobile ยังอยู่ใน roadmap) — ไม่มี bot เข้าประชุม รันบนเครื่องเอง — transcript + ชื่อผู้พูด + สรุปตามหัวข้อ + next steps — หลุดช่วงไหนถาม "What did I miss?" แล้วมันสรุปช่วงนั้น — ใช้ได้ตั้งแต่ Zoom/Meet/Teams/Slack huddles จนถึงประชุมตัวต่อตัว — MCP ดัน note ไปใช้ต่อใน Claude/ChatGPT

.

# Pricing (ตรวจ 2026-10-16)

— **Free $0** — 2,000 คำ/สัปดาห์ desktop + 1,000 คำ/สัปดาห์ mobile — 100+ ภาษา — dictionary + snippets — ไม่ต้องใช้บัตร ไม่มี countdown
— **Pro $15/user/mo** (annual = $12) — unlimited dictation + Notetaker เต็ม + shared dictionary + team analytics
— **Growth $23/user/mo annual** — SSO/SAML + HIPAA BAA + admin คุม model training
— **Enterprise** — SCIM + audit logs + MDM + model training locked off
— นักเรียน/อาจารย์ 50% off — Notetaker full-access promo ถึง 31 ต.ค. (ณ วันที่ตรวจ)

บริบท: บริษัท raise รวม ~$81M (รอบล่าสุด $25M นำโดย Notable Capital, 2025-11) ประกาศว่าจะ "build the Voice OS" — funding ไม่ใช่เหตุผลซื้อ — แต่บอกทิศว่า feature จะไหลไปทางไหน

.

# มุมของ Duck OS

คีย์บอร์ดคือ input channel ที่ ceiling 45 wpm — เสียงคือ channel ที่คิดได้ 220 — ปัญหาไม่ใช่คนพิมพ์ช้า — **ปัญหาคือระบบยังบังคับให้ความคิดเดินทางผ่านท่อที่เล็กกว่ามัน**

หลักที่พรใช้ทุกวัน: งานที่ควรเป็น asset (ข้อความที่กดส่งได้ note ที่ใช้ต่อได้) ไม่ควรจมกลายเป็น activity (นั่งแก้ transcript ทั้งวัน) — ทุก channel ที่ช้ากว่าความคิด คือจุดที่ความคิดต้องรอท่อ

Flow ปิดช่องว่างนั้นได้ — แต่ตัวตัดสินว่า "อันนี้ส่งได้" ยังเป็นคุณเสมอ — เครื่องเร็วขึ้นแค่กลายเป็นเครื่องแปล — **คนอนุมัติ = คุณ**

.

# สรุปแบบวิศวกรเป็ด

voice input ในตัวยังจบงานได้ — อย่าลงมา — Free tier ไม่ได้บังคับอะไร ใช้ของเดิมต่อไป

ทุกครั้งที่พูดจบต้องแก้ — ชื่อคนผิดทุกครั้ง — prompt AI แล้ว context ไม่ครบ — ค่อยลงมา — 2,000 คำ/สัปดาห์ฟรีคือ window ทดลองที่ไม่มีต้นทุน

**The bottleneck was never your head — it was the pipe.**

คุณพิมพ์ได้กี่ wpm — และถ้าเสียงให้จริง 220 — จะเอาความเร็วที่คืนมาไปทำอะไรต่อ คอมเมนต์ด้านล่างได้เลย

#Adduckivity #DuckOS #WisprFlow #VoiceTyping #Dictation #Productivity #AI
