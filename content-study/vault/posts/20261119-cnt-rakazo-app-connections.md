<!--
PAIR: #122 rakazo-app-connections (TECH lane)
Status: draft v1 (2026-11-19 — owner brief: "research rakazo ว่าสามารถต่อในแอปอะไรได้บ้าง แล้วเอามา draft content" + steer "เหมือนรีวิว tech นิดๆ แต่เป็นสไตล์ adduckivity")
FORM: TECH v2 — first-look review มุมการเชื่อมต่อ (ไม่ใช่ docs recap — ทุกตัวเลขสถานะมาจาก DB ของเซิร์ฟเวอร์จริง)
REGISTER: TECH — เลขอารบิก form-legitimate, ชื่อผลิตภัณฑ์/protocol ในเนื้อได้, พร 1 (เจ้าของเครือข่ายส่วนตัว), เรา = มุมผู้ใช้
RESEARCH: research/rakazo-integrations-research.md (verified 2026-11-19)
FACT LEDGER (ยืนยันจากเครื่อง 2026-11-19, query Postgres + .env ของเซิร์ฟเวอร์): (1) connections = 0 แถว (2) mcp_servers = 2 — ทั้งคู่ชื่อ "Notion MCP", transport streamable_http, healthToolCount 77, enabled — ชื่อซ้ำ = ลงทะเบียนสองรายการ (3) user_model_credentials = 4 รายการ (4) memory_documents = 9 (5) COMPOSIO_API_KEY ว่าง (len=0), ไม่มี PIPEDREAM_* (6) grep messaging (telegram/slack/whatsapp/imessage/sendblue/photon/lark/feishu/teams) ในไฟล์ตั้งค่า = 0 บรรทัด (7) bot_email_addresses = 0, INBOUND_EMAIL_DOMAIN ว่าง (8) cloud_agents = 0 (9) git = credential ใน home ของบอต (ยืนยันจากสายงานจริง 16-18 พ.ย.)
VENDOR CLAIMS (reported speech เท่านั้น): docs ของทีมผู้ทำ (github.com/elie222/rakazo — README, docs/integrations.md, docs/self-host-integrations.md, docs/models.md, docs/self-host-meetings.md ดึง 2026-11-19) — ชั้นการเชื่อมต่อ 4 ชั้น / แอปสำเร็จรูป Gmail-Slack-GitHub-Notion-Linear "and thousands more" / MCP-OpenAPI-GraphQL-Executor-plugin GitHub / messaging 6 platform / catalog ต้องใส่ key ผู้ให้บริการก่อนบน self-host / credentials เข้ารหัสไม่ถูกส่งให้โมเดล
SIBLING GUARD: #121 rakazo-local-docker-first-days (การติดตั้ง + เหตุการณ์ push วันแรก — published) — axis แยก = #121 เล่ากระบวน deployment + บทเรียน push, บทนี้แผนที่ช่องทางเชื่อมต่อ + สถานะจริงของแต่ละชั้น; คำ guard = 0: 403, cherry-pick, egress, RAM 2GB, compose up, 5.2GB, 2.82GB, YouTube Library, token; พอร์ต 5173 = 0; โมเดล local พูดใหม่ด้วยภาษา endpoint/OpenAI-compatible ไม่รีเลย์เรื่องติดตั้ง; sibling อีกตัว (#123 automation — เขียนพร้อมกัน) — axis แยก = ช่องทาง (อะไรต่ออะไรได้) vs กลไกจุดงานเอง; คำ routine/webhook/Git event/watch ในเนื้อ = 0 ยกเว้นไม่มี (ชั้นแชตพูดถึงการเข้าถึงบอตเท่านั้น)
GUARDS (วัดจริงรอบสุดท้าย): พร 1 real (เครือข่ายส่วนตัวของพร) / FP พร-lookalike 0 (พร้อม 0, เพราะ 0 — เขียนเลี่ยงแล้ว) / เรา 4 real (title + heading + body + closer — ตัวนับ battery รายงาน 1 = undercount compound ตาม precedent #121) / คุณ-ผม-คับ-ฉัน 0 / sibling guard terms 0 (battery CUT 14 terms all-zero PASS) / odd codepoints form-legitimate (TECH): ',' ×12 ใน tech-lists + '/' ×2 + '_' ×1 (ชื่อตาราง mcp_servers)
SECRET HYGIENE: ไม่มีค่าจาก .env ใดในเนื้อ — เขียนเป็น "ไฟล์ตั้งค่าไม่มี credential ของ platform แชตตัวไหน"; ไม่มี hostname, ไม่มี endpoint URL
Notion: POST ใหม่ Content Drafts DB หลัง battery PASS | Status draft รอ Benz r1
-->

# ต่อแอปกับ Rakazo — ระบบเปิดช่องไว้สี่ชั้น แต่บนเครื่องเรามีสองสายที่วิ่งจริง

### ตัวเลขสถานะทั้งบทอ่านจากฐานข้อมูลของเซิร์ฟเวอร์จริง วันที่ 19 พ.ย. — นับจากตาราง ไม่ใช่จากโบรชัวร์

.

## สี่ชั้นของการเชื่อมต่อ

เอกสารของทีมผู้ทำแบ่งการต่อของภายนอกเป็นสี่ชั้น — โมเดล แอปสำเร็จรูป เครื่องมือที่ต่อเอง และช่องทางแชต

โมเดลต่อได้สามทาง — ใส่ API key, ล็อกอินด้วยแผนที่จ่ายอยู่แล้ว หรือชี้ไปที่ endpoint แบบ OpenAI-compatible ที่ host เอง

แอปสำเร็จรูปที่ทีมผู้ทำระบุมี Gmail, Slack, GitHub, Notion, Linear และอีกหลายพัน — แต่บนเครื่อง self-host รายการนี้จะโผล่ก็ต่อเมื่อผู้ดูแลใส่ key ของผู้ให้บริการ catalog เข้าไปก่อน

เครื่องมือที่ต่อเองมีห้าแบบ — MCP server, OpenAPI, GraphQL, Executor และ plugin จาก GitHub โดย credential ทั้งหมดถูกเข้ารหัสและไม่ถูกส่งให้โมเดล เอกสารระบุไว้ตรง ๆ

ช่องทางแชตรองรับ Slack, Microsoft Teams, iMessage/SMS, WhatsApp, Telegram และ Feishu/Lark — เปิดเมื่อใส่ credential ครบเท่านั้น

.

## บนเครื่องของเรา ต่อใช้จริงอยู่สองสาย

สายแรกคือโมเดล — บอตเรียก endpoint บนเครื่องเดียวกันผ่านช่อง OpenAI-compatible งานไม่ออกนอกบ้าน ระบบมีบันทึกโมเดลไว้ 4 รายการ

เอกสารบอกด้วยว่าโมเดลหลักพังหรือถึงเพดานเมื่อไร ระบบเลื่อนไปตัวสำรองตัวถัดไปเองตามลำดับที่จัดไว้ และบอตแต่ละตัวเลือกโมเดลของตัวเองได้แยกกัน

สายที่สองคือ MCP — ตาราง mcp_servers มีสองรายการ ทั้งคู่เป็น Notion MCP แบบ streamable HTTP เปิดเครื่องมือให้บอต 77 ตัว อ่านเขียน Notion ได้ทั้ง workspace

ยังมีสายที่สามที่ไม่ได้อยู่ในระบบ integration เลย — git บอตใช้ credential ของตัวเองใน home บนคอมพิวเตอร์ของมัน แล้ว push เข้า repo ตรง ๆ

ตรวจละเอียดขึ้นอีกนิดเจอรายการซ้ำ — Notion MCP ถูกลงทะเบียนไว้สองรายการชื่อเดียวกัน เปิดเครื่องมือชุดเดียวกัน น่าจะลงมือสองครั้งตอนตั้งค่า ใช้งานได้อยู่ แต่เราควรรวมเหลือตัวเดียวให้สะอาด

.

## ชั้นที่ยังปิดอยู่

ตาราง connections ในฐานข้อมูลนับได้ 0 แถว — แอปสำเร็จรูปต่อแล้วยังไม่มีตัวใดเลย และ key ของผู้ให้บริการ catalog ยังว่างอยู่ในไฟล์ตั้งค่า

ไฟล์ตั้งค่าไม่มี credential ของ platform แชตตัวไหน — ทางเข้าบอตตอนนี้มีทางเดียว คือหน้าเว็บในเครือข่ายส่วนตัวของพร

โหมดประชุม ที่อยู่อีเมลให้บอต และ cloud coding agent — ทั้งสามอย่างเอกสารว่าทำได้ แต่บนเครื่องนี้ยังไม่ได้ตั้งค่าอะไรเลย

ความจำก็เหมือนกัน — เอกสารระบุว่าเอาเซิร์ฟเวอร์ความจำมา host เองได้สามชื่อ แต่ทั้งหมดยังไม่ได้ต่อ บอตบันทึกสิ่งที่เรียนรู้ไว้ในความจำในตัวอยู่ 9 เอกสาร

.

## #สรุปแบบวิศวกรเป็ด

ต่อแล้วสองสาย — โมเดลบนเครื่อง และ MCP เข้า Notion

ที่เหลือรอเราตั้งค่า ไม่ใช่รอระบบอัปเดต — เอกสารบอกว่าทุกชั้นมีอยู่แล้ว

ต่ออันต่อไปเมื่องานเรียกใช้ ไม่ใช่ต่อไว้ก่อนแล้วค่อยหางานให้ทำ

.

#Adduckivity #DuckOS #NeuroDivergent #SelfHosted #AIAgent #MCP
