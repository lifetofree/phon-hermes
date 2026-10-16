# 45 wpm กับ 220 wpm — ช่องทางที่ช้ากว่าคือตัวที่คุณยังใช้พิมพ์อยู่

<!--
ContentID: 20261016-CNT-WISPR-FLOW
Series: standalone tool review — ref: 20260917-cnt-orca-ade-parallel-coding-agents (2026-09-17, v2 TECH form)
Type: v2 line-per-sentence TECH form (stat-line / signals / mental model / table / two-fork)
Status: Draft — รอย review
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
SSOT anchors (verified 2026-10-16, used UNLABELED): First Principle "User ≠ Machine — Productivity พังเพราะใช้ระบบผิดประเภท"
= ~/hermes-agent/duck-os/Main_Data_for_UDO.md:38 (input-channel bottleneck framing)
Benchmarks: NOT self-run — all speed/accuracy numbers are vendor-reported (Anti-Hype note in body).
Candidate hooks (for critique round): (1) 45 vs 220 stat-line (used) (2) "พิมพ์มาทั้งชีวิต — แต่ไม่เคยถามว่ามือมันเร็วได้สุดที่เท่าไร"
(3) "คุณไม่ได้พิมพ์ช้า — คุณใช้ช่องทางที่ช้ากว่าคิด"
-->

คุณพิมพ์เร็วแค่ไหน

45 wpm คือค่าเฉลี่ยของคีย์บอร์ด — และ 220 wpm คือความเร็วที่เสียงของคุณคิดได้จริง

.

ถ้าของเดิมทำงานได้ — ไม่ต้องเปลี่ยน

โพสต์นี้ไม่ได้มาให้คุณเลิกพิมพ์คีย์บอร์ด

มันมาสำหรับคนที่ "พิมพ์แล้วต้องแก้" — คนที่ voice input ในตัวให้มาทั้งก้อน แล้วต้องนั่งขัดทั้งก้อน

.

## คำถามที่แท้จริงของโพสต์นี้คับ:

> **เมื่อไหร่ที่ "พิมพ์ด้วยเสียง" ในตัวไม่พอ — และเมื่อไหร่ที่คุณยังไม่ต้องแตะมันเลย**

.

## 5 สัญญาณว่า voice input ในตัว เริ่มไม่พอ

## 1. คุณแก้ข้อความหลังหยุดพูด ทุกครั้ง

voice input ในตัว (Siri / Apple Dictation / Gboard / Windows) **transcribe ตรงตัว** — ทุก "เอ่อ" ทุกจุดที่พูดผิด ทุกครั้งที่คิดใหม่

พูดว่า "นัดกันบ่าย 3 — เอ้ย บ่าย 4" — ตัวในตัวยังเขียนทั้ง 3 และ 4 — แล้วคุณเป็นคนแก้เอง

Flow (Wispr Flow) ตัดขั้นตอนนั้นออก — พูดว่า "5... actually 6" — ได้กลับมาว่า "6pm" — ตัวที่แก้ไขถูกกินไปเอง

.

## 2. คุณได้ "กำแพงข้อความ" กลับมา ไม่ใช่ข้อความที่ส่งได้

ตัวในตัวใส่เครื่องหมายจุดได้ — แต่ไม่จัด list ไม่แยกย่อหน้า ไม่จัดโครงสร้างอีเมล

Flow จัด format ระหว่างพูด — numbered list, ย่อหน้า, โครงร่างอีเมล — จากประโยคที่พูดไปเรื่อย ๆ

.

## 3. ชื่อคน / คำเฉพาะทาง — ผิดทุกครั้งที่ต้องพิมพ์

"Adithya" / "Guillain-Barre" / "Andreessen Horowitz" — ตัวในตัวไม่มี context ของคุณ

Flow เรียนคำศัพท์ส่วนตัว — ชื่อลูกค้า คำศัพท์ทีม — เพิ่มเองได้ — และแม่นยำขึ้นตามการใช้ (docs + homepage)

.

## 4. คุณ prompt AI ด้วยนิ้ว — แล้ว AI ได้รับบริบทครึ่งเดียว

คนที่พิมพ์ จะสรุป — พูด จะเล่าครบ — homepage อ้างว่าคนใช้ Flow ให้ context เยอะขึ้นมากเวลา prompt ChatGPT/Claude

ข้อนี้พรยังไม่ได้วัดเอง — เป็น claim ของ vendor — แต่ตรงกับประสบการณ์ที่หลายคนเล่า

.

## 5. คุณพิมพ์ใน 5 แอป — และแต่ละแอปมี voice ของมันเอง

Gboard ของ Gboard, dictation ของ Apple, voice mode ของ Cursor — 5 ตัว 5 quirk

Flow = 1 ตัว — cursor อยู่ที่ไหนก็พูดที่นั่น — "If you can type there, you can Flow there" (FAQ) — Mac / Windows / iPhone / Android

.

## Flow = Post-Processing Layer ไม่ใช่ "เครื่องพิมพ์ดีดเสียง"

raw transcription คือขั้นแรกเท่านั้น — ตัวในตัวจบที่ขั้นนั้น

Flow เติมชั้นหลัง: จับการแก้ไขตัวเอง / จัด format / ใส่คำศัพท์ส่วนตัว / ปรับ tone ตามแอป (Formal / Casual / Very casual)

**คุณต้องการ raw transcript หรือข้อความที่ส่งได้เลย?**

HONESTY CAVEAT: ตัวในตัวก็ "แต่ง" ได้ถ้าคุณยอมแก้เอง — ความต่างคือ **Evidence ที่ต่อเนื่องกว่า** — Flow ทำให้คุณไม่ต้องแก้ — ตัวในตัวทำให้คุณแก้แล้วค่อยส่ง

.

## เปรียบเทียบ — Flow vs ตัวในตัว vs ตัวอื่น

| | Wispr Flow | Built-in (Siri/Apple/Gboard) | ChatGPT/Cursor voice mode |
|---|---|---|---|
| Zero-edit rate | 90% (vendor bench) | 52% Siri (vendor bench) | n/a — วัดต่างเกณฑ์ |
| ทำงานข้ามแอปทุก device | ได้ — 1 app ทุก text field | จำกัด — ยึด ecosystem ของมัน | ไม่ได้ — ในแอปตัวเองเท่านั้น |
| จัด format/list/email | ได้ — ระหว่างพูด | ไม่ได้ — raw text | แล้วแต่แอป |
| คำศัพท์ส่วนตัว + style per-app | ได้ | ไม่ได้ | จำกัด |
| ราคา | Free 2,000 คำ/สัปดาห์ | $0 | ตาม subscription ของแอป |
| Platform | Mac/Win/iOS/Android | ตาม device | ตามแอป |

**One-line จากตาราง: ตัวในตัว = raw text ที่ต้องแก้ / Flow = text ที่ส่งได้ — ส่วน voice mode ของแต่ละแอป = ของดี แต่ติดอยู่ในแอปตัวเอง**

.

## ตัวเลข — และสิ่งที่พรต้องบอกตรง ๆ

220 wpm / "4x faster" / "save over an hour a day" / zero-edit 90% — **ทั้งหมดเป็นตัวเลขจากตัว vendor** (wisprflow.ai) — benchmark zero-edit ที่เทียบ Siri/OpenAI/ElevenLabs ก็รันโดย Wispr เอง

**พรไม่ได้ลง Flow ไว้บนเครื่องนี้ — ไม่มีการวัดเอง** — ตัวเลขข้างบนคือ claim ที่คุณควรไป verify กับ 2,000 คำฟรีของคุณเอง — ไม่ควรนำไปเทียบตรงกับเครื่องอื่นโดยไม่ควบคุมเงื่อนไข — และถ้ามีใครมี independent benchmark ที่เทียบตรง ๆ — ส่งมาในคอมเมนต์ได้เลย

ข้อควรรู้จาก docs (ไม่ใช่ marketing):

— ต้องมีอินเทอร์เน็ตตอน transcribe
— desktop insert ข้อความหลังหยุดพูด — ไม่ได้พิมพ์ตามคำต่อคำแบบ live
— AirPods/Bluetooth earbuds = ลดความแม่นยำ (docs แนะนำไมค์ในตัว)
— dictation history อยู่บน device — ลบแล้วหายทุก platform

.

## Notetaker — ของแถมที่มากับ subscription เดียว

Wispr Notetaker (Mac + Windows, mobile ยัง roadmap) — **ไม่มี bot เข้าประชุม** — รันบนเครื่องคุณ — transcript + ชื่อคนพูด + สรุปตามหัวข้อ + next steps — ใช้ได้ทั้ง Zoom/Meet/Teams/Slack huddles/ประชุมตัวต่อตัว — บวก "What did I miss?" (หลุดช่วงไหนสรุปให้) + ถามข้าม meeting + MCP ให้เอา note เข้า Claude/ChatGPT

.

## Pricing (ตรวจ 2026-10-16)

— **Free $0** — 2,000 คำ/สัปดาห์ (desktop) + 1,000/สัปดาห์ (mobile) — 100+ ภาษา — dictionary + snippets — Notetaker จำกัด — **ไม่ต้องใช้บัตรเครดิต ไม่มี trial countdown**
— **Pro $15/user/mo** (annual = $12/user/mo) — unlimited dictation + Notetaker เต็ม + shared dictionary + team analytics
— **Growth $23/user/mo annual** — SSO/SAML + HIPAA enforced (BAA) + admin คุม model training
— **Enterprise** — SCIM, audit logs, MDM, model training locked off
— นักเรียน/อาจารย์ = 50% off — Notetaker full access promo ถึง 31 ต.ค. (ณ วันที่ตรวจ)

บริบท: บริษัท raise $81M (รอบล่าสุด $25M นำโดย Notable Capital, 2025-11) บอกว่าจะ "build the Voice OS" — ตัวเลข funding ไม่ใช่เหตุผลซื้อ — แต่บอกทิศทางว่า feature จะไหลไปทางไหน

.

## มุมของ Duck OS

คีย์บอร์ดคือ input channel ที่ ceiling 45 wpm — เสียงคือ channel ที่คิดได้ 220 — ปัญหาไม่ใช่คุณพิมพ์ช้า — **ปัญหาคือระบบยังบังคับให้คุณส่งความคิดผ่านท่อที่เล็กกว่ามัน**

First Principle ที่พรใช้ทุกวัน: **User ≠ Machine** — คุณรันต่อเนื่องไม่ได้ — และทุก channel ที่ช้ากว่าคิด = ทุกครั้งที่ความคิดรอท่อ — งานที่ควรเป็น asset (ข้อความที่ส่งได้ / note ที่ใช้ต่อได้) กลายเป็น activity (นั่งแก้ transcript ทั้งวัน)

Flow = post-processing layer ที่ปิดช่องว่างนั้น — แต่ตัวตัดสินใจว่า "อันนี้ส่งได้" ยังเป็นคุณเสมอ — เครื่องเร็วขึ้น = เครื่องแปลง — **คนอนุมัติ = คุณ**

.

## สรุปแบบวิศวกรเป็ด

ถ้า voice input ในตัวยังจบงานได้ — **อย่าลงมา** — Free tier ของ Flow ไม่ได้บังคับอะไรคุณ — ใช้ของเดิมต่อไป

ถ้าทุกครั้งที่พูดจบ คุณต้องแก้ — ถ้าชื่อคนผิดทุกครั้ง — ถ้า prompt AI แล้ว context ไม่ครบ — **ค่อยลงมา** — 2,000 คำ/สัปดาห์ฟรีคือ window ทดลองที่ปลอดภัย

**The bottleneck was never your head — it was the pipe.**

คุณพิมพ์เร็วเท่าไร — และถ้า 220 wpm จริงบนเครื่องคุณ — คุณจะเอาความเร็วที่คืนมานี้ไปไว้ที่ comment ด้านล่างได้เลย

System > Keyboard. ลองพูดแล้วส่ง โดยไม่ต้องแก้คับ! 🦆⚡

#Adduckivity #DuckOS #WisprFlow #VoiceTyping #Dictation #Productivity #AI
