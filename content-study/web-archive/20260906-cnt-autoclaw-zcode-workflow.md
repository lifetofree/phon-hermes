<!-- Archived from https://wp.adduckivity.com/20260906-cnt-autoclaw-zcode-workflow/ on 2026-09-06 by sync_wp_posts.py -->
Title: AutoClaw x ZCode: 2 เครื่องมือ 1 แผน — Workflow ตั้งแต่ Design ถึง Deploy
Date: 2026-09-06T19:01:42
Link: https://wp.adduckivity.com/20260906-cnt-autoclaw-zcode-workflow/
-->

AutoClaw x ZCode: 2 เครื่องมือ 1 แผน — Workflow ตั้งแต่ Design ถึง Deploy

เคยมั้ยคับ — AI tool ตัวหนึ่งใช้เขียนโค้ด อีกตัวใช้รันงาน agent บน desktop พอจะให้ทั้งคู่ทำงานร่วมกัน กลับต้องต่อ API key อีกชุด เติมเงินอีกบัญชี คิดเงินคนละแบบ — พรคนนึงแหละที่เคยเป็นแบบนั้น แล้วมีเสียงในหัวถามว่า “มันคนละระบบกันเหรอวะ”

.

ถ้าคุณเคยลองใช้ AutoClaw (one-click local agent ที่พรรีวิวไปก่อนหน้านี้) แล้วรู้สึกว่างานสาย code ยังไม่มีที่ลง — วันนี้พรจะเชื่อมสองตัวนี้เข้าด้วยกันครับ เพราะทั้งคู่อยู่ใน ecosystem เดียวกันของ Z.ai และใช้ GLM Coding Plan แผนเดียวรันได้ทั้งสองฝั่ง

.

Diagnostic — 2 เครื่องมือ ≠ 2 ระบบ

AutoClaw กับ ZCode เป็นคนละ runtime กันจริงๆ — ZCode คือ Agentic Development Environment (IDE สาย agent) ส่วน AutoClaw คือ agent runtime สำหรับงานนอกโค้ด แต่ชั้นกลางของทั้งสองตัวคือ subscription เดียว:

Layerสิ่งที่ทำ
GLM-5.3ชั้นสมอง — model ที่ optimize สำหรับ tool calling
GLM Coding Planชั้น subscription ที่ share กัน — ZCode, AutoClaw, Claude Code ใช้ quota แผนเดียวกัน
ZCodeชั้น execution สาย code — IDE + terminal + Git + browser + Goal Mode
AutoClawชั้น execution สายงาน — browser automation, office, content, IM

นี่คือจุดที่ “combo” ของมันอยู่จริง ไม่ใช่แค่ marketing: แผนเดียว, quota เดียว และ Z.ai ยืนยันตรงๆ ในหน้า pricing ของ ZCode ว่า “Supports 20+ agent tools, including ZCode, Claude Code, and more”

.

ZCode — งาน Design & Code

ZCode เป็น IDE เต็มสูบ (VS Code base) ที่มี agent ของตัวเองฝังอยู่:

Goal Mode — พิมพ์ /goal <เป้าหมาย> แล้ว agent ทำงานเป็นรอบๆ แต่ละรอบจบด้วย verification แยก ที่ดูหลักฐานจริง (ไฟล์ที่เปลี่ยน, output, test results) ไม่ใช่แค่คำว่า “เสร็จแล้ว” ถ้าไม่ผ่านก็เริ่มรอบใหม่เอง ไม่ต้องมานั่งพิมพ์ continue — เหมาะกับงานแบบ “refactor โมดูลนี้ทั้งก้อนแล้วให้ test ยัง pass อยู่”

Bot Channel / Remote Control — ต่อ WeChat, Feishu (และ Telegram ผ่าน remote control) แล้วสั่งงานจากมือถือได้เลย: เปิด workspace, ดู progress, ส่งคำสั่งต่อ

เครื่องมือครบ — terminal, Git panel, file tree, live browser preview, subagents, MCP, Skills

Idle-time tasks — ตั้งให้ agent ทำงานช่วง idle ได้

Setup ต่อ GLM Coding Plan: Settings → Model Providers → วาง API key (หรือกด Use Subscription) — base URL ที่ต้องจำ: https://api.z.ai/api/coding/paas/v4 (OpenAI-compatible) และ https://api.z.ai/api/anthropic — ใส่ผิด endpoint = quota ไม่เดินนะค้าบ

.

AutoClaw — งานหลัง Code

ส่วน AutoClaw คือฝั่งงาน operation ครบสูตร:

browser automation แบบ screenshot-driven

office automation (Word/Excel/PPT)

content ops (IG/TikTok/X/Substack)

multi-agent dashboard

IM integration (Telegram/WhatsApp/Slack/Discord/Lark)

.

Workflow Combo — Design → Code → Run → Post

มุมที่น่าสนใจคือ pipeline เดียว ที่ทั้งสองตัวแบ่งงานกัน:

Design & Build ใน ZCode — /goal สร้าง landing page ของงาน xxx → agent วางแผน, เขียน code, verify ทุก round → commit ขึ้น Git

Deploy & Verify ใน AutoClaw — browser automation เปิดหน้าเว็บจริง เช็ค layout, กรอก form ทดสอบ, ส่งสกรีนช็อตกลับมา

Content ops ใน AutoClaw — ตัวเดียวกันนี่แหละ ดันเนื้อหาจากโปรเจกต์ขึ้น IG/X/Substack/Telegram ตามตาราง

สั่งจาก Telegram ทั้งคู่ — ZCode มี Bot Channel, AutoClaw มี IM integration — มือถือเครื่องเดียวสั่งงานได้ทั้งสองฝั่ง

ในทางปฏิบัติ: เขียนโค้ดใน ZCode ด้วย GLM-5.3 แล้วโยกงาน “หลังโค้ด” (ทดสอบ, deploy, โปรโมต, ตอบลูกค้า) ไป AutoClaw — โดย quota ทั้งสองฝั่งเดินในแผน GLM Coding Plan เดียวกัน

และยังมีอีกท่านึงที่พรชอบมาก: สั่งจาก AutoClaw แล้วให้มันแอบไปสั่ง ZCode ทำงานต่อเอง ส่วนเราก็เอาเวลาไปจิบกาแฟ เอ้ย! ไปทำงานอื่น…

.

Pricing (ก.ย. 2026)

GLM Coding Plan (ราคาที่แสดงบน zcode.z.ai — โปร 30%):

Planราคา/เดือนUsage
Lite$12.6 (ปกติ $18)10,000 credits/สัปดาห์
Pro$56 (ปกติ $80)6x Lite + MCP tools curation
Max$117.6 (ปกติ $168)14x Lite + dedicated resources peak hours

ฝั่ง AutoClaw: free 5,000 credits + daily free credits สำหรับผู้ใช้ใหม่ และ limited-time 150% quota boost เมื่อต่อ GLM Coding Plan เข้า AutoClaw + bonus credits รายเดือน (Lite 5,000 / Pro 10,000 / Max 26,000)

.

Pros ✅ / Cons ❌

✅ แผนเดียวเลี้ยง 2 runtime + Claude Code — ไม่ต้องต่อ API key 2 บัญชี

✅ Goal Mode + verification — agent ทำงานยาวแบบมีหลักฐาน ไม่ใช่ “เดาว่าเสร็จ”

✅ สั่งงานจากมือถือได้ทั้งสองฝั่ง (WeChat/Feishu/Telegram)

✅ AutoClaw ฟรีเริ่มต้น — ลองงาน agent ก่อน แล้วค่อยอัปเกรดแผน

❌ Vendor lock-in ซ้ำซ้อน — ทั้งคู่พึ่ง GLM ecosystem ของ Zhipu

❌ “Local” ≠ ข้อมูลไม่ออกเครื่อง — model calls ส่ง task description + context ออกไป inference — งาน sensitive ต้อง declare allowed paths ก่อน

❌ Access contract แยกกัน — shared branding ไม่ได้แปลว่า permission/billing/สิทธิ์ output แลกเปลี่ยนกันได้ — ต้อง audit แต่ละตัว

❌ GLM-5.3 ยังเป็น cloud-first — API + open weights ยังปล่อยเป็นขั้นๆ ส่วนตัวคิดว่าน่าจะมีลุ้นอยู่

.

Pro Tips

มือใหม่: เริ่มจาก AutoClaw free 5,000 credits ก่อน (ไม่ต้องมีแผน) — พอติด quota ค่อยขึ้น Lite

ใช้จริงจัง: Pro — จุดคุ้มสุดคือ 6x quota + MCP tools curation สำหรับ workflow combo ทั้งสาย

ทีม/องค์กร: base URL ต้องมาจาก config source เดียวที่ review แล้ว — Z.ai เตือนเองว่า endpoint ผิด = quota ไม่เดิน แล้วไปกิน pay-as-you-go แทน (billing surprise ตัวจริง)

.

สรุปแบบวิศวกรเป็ด

Duck OS Law #2: Asset > Activity — การมี subscription 2 อันที่ quota ไม่คุยกัน คือ technical debt ของสาย AI tooling ครับ แผน GLM Coding Plan แผนเดียวที่เลี้ยงทั้ง ZCode (สาย code) กับ AutoClaw (สายงาน) คือ Single Source of Truth ของ workflow — ครบจบ สั่งจากมือถือเครื่องเดียว

.

ระบบที่คุยกันเป็นภาษาเดียวกัน ไม่ต้องมี middleware แปลง — คือระบบที่ซ่อมง่ายครับ

.

#Adduckivity #DuckOS #NeuroDivergent #AICoding #GLM #ZCode #AutoClaw #SystemsFirst #ProductivityHacks
