<!--
ContentID: 20260904-CNT-<PENDING>
Series: AutoClaw (Part 2) — Combo & Workflow
Status: draft
Date: 2026-09-04
Verified sources:
- https://zcode.z.ai/en (features, Goal Mode, Bot Channel, pricing)
- https://docs.z.ai/devpack/tool/zcode (Coding Plan setup, base URLs)
- https://zcode.z.ai/en/docs/goal (Goal Mode semantics)
- https://zcode.z.ai/en/docs/bot-channel (WeChat/Feishu/Telegram bots)
- https://autoclaw.z.ai/ (Coding Plan integration, 150% quota boost, free credits)
- https://daisuke.masuda.tokyo/article-2026-08-24-0212 (stack overview, endpoint hygiene)
- https://www.chineseaitools.com/en/articles/glm-ecosystem-selection-guide (access contract warning)
-->

# AutoClaw + ZCode: 2 เครื่องมือ 1 แผน — Workflow ตั้งแต่ Design ถึง Deploy

คุณเคยซื้อ AI coding tool ตัวหนึ่ง ใช้เขียนโค้ดได้ลื่น แล้วอีกตัวใช้รันงาน agent บน desktop พอจะรันยาวๆ ก็ต้องต่อ API key อีกชุด ชาร์ตอีกบัญชี — คุยกับตัวเองมั้ยครับว่า "มันคนละระบบเหรอวะ"

ถ้าคุณกำลังใช้ **AutoClaw** (one-click local agent ที่พรเคยรีวิวไว้ใน Part 1) อยู่แล้ว แล้วติดว่างานสาย code ของคุณยังไม่มีที่ลง — วันนี้พรจะเชื่อมสองตัวนี้เข้าด้วยกันครับ เพราะทั้งสองตัวอยู่ใน ecosystem เดียวกันของ Z.ai และใช้ **GLM Coding Plan** แผนเดียวเลี้ยงได้ทั้งคู่

## 01: Diagnostic — 2 เครื่องมือ ≠ 2 ระบบ

AutoClaw กับ ZCode เป็นคนละ runtime จริงๆ — ZCode คือ Agentic Development Environment (IDE สาย agent) ส่วน AutoClaw คือ agent runtime สำหรับงานนอกโค้ด แต่ชั้นกลางของทั้งสองตัวคือ subscription เดียว:

| Layer | สิ่งที่ทำ |
|---|---|
| GLM-5.3 | ชั้นสมอง — model ที่ optimize สำหรับ tool calling |
| **GLM Coding Plan** | **ชั้น subscription ที่ share กัน — ZCode, AutoClaw, Claude Code ใช้ quota แผนเดียวกัน** |
| ZCode | ชั้น execution สาย code — IDE + terminal + Git + browser + Goal Mode |
| AutoClaw | ชั้น execution สายงาน — browser automation, office, content, IM |

นี่คือจุดที่ "combo" ของมันอยู่จริง ไม่ใช่แค่ marketing: แผนเดียว, quota เดียว, และ Z.ai ยืนยันตรงๆ ในหน้า pricing ของ ZCode ว่าแผน "Supports 20+ agent tools, including ZCode, Claude Code, and more"

## 02: ZCode — งาน Design & Code

ZCode เป็น IDE ตัวเต็ม (VS Code base) ที่มี agent ของตัวเองฝังอยู่:

- **Goal Mode** — พิมพ์ `/goal <เป้าหมาย>` แล้ว agent ทำงานเป็นรอบๆ โดยแต่ละรอบจบด้วย **verification แยก** ที่ดูหลักฐานจริง (ไฟล์ที่เปลี่ยน, output, test results) ไม่ใช่คำพูด "เสร็จแล้ว" ถ้าไม่ผ่าน ก็เริ่มรอบใหม่เองโดยที่คุณไม่ต้องพิมพ์ continue — เหมาะกับงานแบบ "refactor โมดูลนี้ทั้งก้อนแล้วให้ test ยัง pass อยู่"
- **Bot Channel / Remote Control** — ต่อ WeChat, Feishu (และ Telegram ผ่าน remote control) แล้วสั่งงานจากมือถือ: เปิด workspace, ดู progress, ส่งคำสั่งต่อได้
- **เครื่องมือครบ** — terminal, Git panel, file tree, live browser preview, subagents, MCP, Skills
- **Idle-time tasks** — ตั้งให้ agent ทำงานช่วง idle ได้

Setup ต่อ GLM Coding Plan: Settings → Model Providers → วาง API key (หรือกด Use Subscription) — base URL ที่ต้องจำ: `https://api.z.ai/api/coding/paas/v4` (OpenAI-compatible) และ `https://api.z.ai/api/anthropic` — ใส่ผิด endpoint = quota ไม่เดิน (ข้อนี้ Z.ai warning เองใน docs)

## 03: AutoClaw — งานหลัง Code

ส่วน AutoClaw (Part 1) คือฝั่ง "งาน" — browser automation แบบ screenshot-driven, office automation (Word/Excel/PPT), content ops (IG/TikTok/X/Substack), multi-agent dashboard, และ IM integration (Telegram/WhatsApp/Slack/Discord/Lark)

## 04: Workflow Combo — Design → Code → Run → Post

มุมที่พรอยากให้เห็นคือ **pipeline หนึ่งสาย** ที่ทั้งสองตัวแบ่งงานกัน:

1. **Design & Build ใน ZCode** — `/goal สร้าง landing page โปรนี้` → agent plan, เขียน code, verify ทุก round → commit ขึ้น Git
2. **Deploy & Verify ใน AutoClaw** — browser automation เปิดหน้าเว็บจริง เช็ค layout, กรอก form ทดสอบ, สกรีนช็อตกลับมา
3. **Content ops ใน AutoClaw** — ตัวเดียวกันนี่แหละดันเนื้อหาจากโปรเจกต์ขึ้น IG/X/Substack/Telegram ตามตาราง
4. **สั่งจาก Telegram ทั้งคู่** — ZCode มี Bot Channel, AutoClaw มี IM integration — มือถือหนึ่งเครื่องสั่งงานได้สองฝั่ง

ในทางปฏิบัติ: คุณเขียนโค้ดใน ZCode ด้วย GLM-5.3, แล้วงาน "หลังโค้ด" (ทดสอบ, deploy, โปรโมต, ตอบลูกค้า) โยกไป AutoClaw — โดย quota ทั้งสองฝั่งเดินในแผน GLM Coding Plan เดียวกัน

## 05: Pricing (ก.ย. 2026)

**GLM Coding Plan** (ค่าที่แสดงบน zcode.z.ai — โปร 20%):

| Plan | ราคา/เดือน | Usage |
|---|---|---|
| Lite | $12.6 (ปกติ $18) | 10,000 credits/สัปดาห์ |
| Pro | $56 (ปกติ $80) | 6x Lite + MCP tools curation |
| Max | $117.6 (ปกติ $168) | 14x Lite + dedicated resources peak hours |

ฝั่ง AutoClaw: **free 5,000 credits + daily free credits** สำหรับผู้ใช้ใหม่, และ limited-time **150% quota boost** เมื่อต่อ GLM Coding Plan เข้า AutoClaw + bonus credits รายเดือน (Lite 5,000 / Pro 10,000 / Max 26,000)

## 06: ข้อดี ✅ / ข้อเสีย ❌

✅ **แผนเดียวเลี้ยง 2 runtime + Claude Code** — ไม่ต้องต่อ API key 2 บัญชี
✅ **Goal Mode + verification** — agent ทำงานยาวแบบมีหลักฐาน ไม่ใช่ "เดาว่าเสร็จ"
✅ **สั่งงานจากมือถือได้ทั้งสองฝั่ง** (WeChat/Feishu/Telegram)
✅ **AutoClaw ฟรีเริ่มต้น** — ลองงาน agent ก่อน แล้วค่อยอัปเกรดแผน
❌ **Vendor lock-in ซ้ำซ้อน** — ทั้งคู่พึ่ง GLM ecosystem ของ Zhipu
❌ **"Local" ≠ ข้อมูลไม่ออกเครื่อง** — daisuke.masuda.tokyo ชี้ชัด: model calls ส่ง task description + context ออกไป inference — งาน sensitive ต้อง declare allowed paths ก่อน
❌ **Access contract แยกกัน** — ecosystem guide เตือนตรงๆ: shared branding ไม่ได้แปลว่า permission/billing/สิทธิ์ output แลกเปลี่ยนกันได้ — ต้อง audit แต่ละตัว
❌ **GLM-5.3 ยังเป็น cloud-first** — API + open weights ยังปล่อยเป็นขั้นๆ

## 07: Pro Tips

- **มือใหม่:** เริ่ม AutoClaw จาก free 5,000 credits ก่อน (ไม่ต้องมีแผน) — พอติด quota ค่อยขึ้น Lite
- **ใช้จริงจัง:** Pro — MCP tools curation + 6x quota เป็นจุดคุ้มสำหรับ workflow combo ทั้งสาย
- **ทีม/องค์กร:** base URL ต้องมาจาก config source เดียวที่ review แล้ว — Z.ai warning เองว่า endpoint ผิด = quota ไม่เดิน แล้วไปกิน pay-as-you-go แทน (billing surprise ตัวจริง)

## บทสรุปจากพร

Duck OS Law #2: **Asset > Activity** — การมี subscription 2 อันที่ quota ไม่คุยกัน คือ technical debt ของสาย AI tooling ครับ แผน GLM Coding Plan แผนเดียวที่เลี้ยงทั้ง ZCode (สาย code) กับ AutoClaw (สายงาน) คือ Single Source of Truth ของ workflow — design ใน IDE, deploy และ content ops ใน agent, สั่งจากมือถือตัวเดียว

ระบบที่คุยกันเป็นภาษาเดียวกัน ไม่ต้องมี middleware แปลง — คือระบบที่ซ่อมง่ายครับ

#Adduckivity #DuckOS #NeuroDivergent #AICoding #GLM #ZCode #AutoClaw

---

🦆 ติดตามคอนเทนต์สายระบบจากพร:
WordPress — wp.adduckivity.com | X — @adduckivity | Threads — @adduckivity | Telegram — t.me/adduckivity
