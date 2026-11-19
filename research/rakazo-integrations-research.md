---
type: research
topic: "Rakazo — ช่องทางเชื่อมต่อแอปภายนอก (integrations): โมเดล / แอปสำเร็จรูป / เครื่องมือเอง / ช่องทางแชต + สถานะจริงบนเซิร์ฟเวอร์ของพร"
used_by: "[[pair-122]]"
verified: 2026-11-19
---

# Rakazo integrations — หลักฐาน 2 ชั้น (docs upstream + DB เครื่องจริง)

## ชั้น 1 — เอกสาร upstream (primary: github.com/elie222/rakazo, ดึง 2026-11-19)

### 4 ชั้นของการเชื่อมต่อ

1. **โมเดล** (docs/models.md) — 3 ทางต่อ: (a) sign in ด้วยแผนที่มีอยู่ (ChatGPT → Codex allowance), (b) API key (OpenAI, Anthropic, Google, OpenRouter "and many others"), (c) **OpenAI-compatible server URL** สำหรับโมเดล self-host (Ollama, vLLM — เครื่องนี้คือ llama-server พอร์ต 8080, พิสูจน์ fetch ผ่านแล้ว 16 พ.ย.) + main model + fallbacks + per-bot/per-routine model & thinking (Minimal–Max) + approval model แยกต่างหาก
2. **แอปสำเร็จรูป (app catalog)** — README: "Gmail, Slack, GitHub, Notion, Linear and thousands more" ผ่าน catalog; docs/self-host-integrations.md: **catalog บน self-host ต้องตั้ง COMPOSIO_API_KEY หรือ PIPEDREAM_CLIENT_ID+_CLIENT_SECRET+_PROJECT_ID ถึงจะโผล่** (INTEGRATIONS_CATALOG_URL = catalog แบบ integrations.sh-compatible เช่าเองได้)
3. **เครื่องมือเอง** (docs/integrations.md) — 5 แบบ: MCP server (remote HTTPS; self-host ต่อ localhost/LAN ได้เมื่อ MCP_ALLOW_PRIVATE_ENDPOINT=true — เครื่องนี้ตั้งแล้ว), OpenAPI, GraphQL, Executor (tool gateway 1 token), plugin จาก GitHub (instructions only — script ใน plugin ไม่รัน, ตรงกับที่เจอจริง); auth: No auth / Bearer / API key header; **credentials เข้ารหัส ไม่ถูกส่งให้โมเดล**; tool call timeout 6 นาที; apps in chat = view sandbox ของ tool result (chart/map/board)
4. **ช่องทางแชต** (docs/self-host-integrations.md + rakazo.com) — Slack, Microsoft Teams, iMessage & SMS (Sendblue หรือ Photon), WhatsApp, Telegram (หลายบอตต่อกันได้ด้วย TELEGRAM_BOT_TOKEN_<n>), Feishu/Lark — **mount เมื่อใส่ credential ครบเท่านั้น**; webhook inbound = /api/v1/messaging/webhook/<provider>

### เสริม
- **memory ภายนอก**: Supermemory (≥v0.0.9) / Honcho (ต้องการ PostgreSQL+pgvector เอง) / Hindsight (≥1.0) — self-host ได้ผ่าน Settings → Memory + MCP_ALLOW_PRIVATE_ENDPOINT
- **meetings** (docs/self-host-meetings.md): bot เข้าห้อง Zoom / Google Meet / Teams ผ่าน **Recall.ai** (MEETING_PROVIDER=recall) → transcript มีชื่อผู้พูด, cap 20 ครั้ง/วัน/space, อัดได้ 2 ชม., audio-only, provider retention 24 ชม. แล้วขอลบ recording
- **cloud coding agents**: default none; รองรับ Cursor (CLOUD_AGENT_PROVIDER=cursor + key + Space ID)
- **git** ไม่ได้อยู่ในระบบ integration — bot ใช้ credential ใน home ของตัวเองบน computer (เส้นทางที่ youtube-sync ใช้จริง)

## ชั้น 2 — สถานะจริงบนเซิร์ฟเวอร์ของพร (query DB + .env วันที่ 2026-11-19)

| ชั้น | docs ว่าได้อะไร | บนเครื่องนี้ (2026-11-19) |
|---|---|---|
| โมเดล | API key / OpenAI-compatible / sign-in | `user_model_credentials` = **4 รายการ**; llama-server 8080 ใช้จริง (16 พ.ย.) |
| MCP / เครื่องมือเอง | MCP remote+stdio, OpenAPI, GraphQL, Executor, GitHub plugin | `mcp_servers` = **2** — ทั้งคู่ "Notion MCP" streamable_http, 77 tools, enabled (ชื่อซ้ำ = ลงทะเบียนสองรายการ); `bot_mcp_servers` = 2; stdio ยังปิด (ไม่มี MCP_STDIO_ENABLED) |
| แอปสำเร็จรูป | Gmail/Slack/GitHub/Notion/Linear + หลายพัน | `connections` = **0 แถว**; COMPOSIO_API_KEY **ว่าง** (len=0), ไม่มี PIPEDREAM_* → catalog ยังไม่เปิด |
| ช่องทางแชต | Slack/Teams/iMessage/WhatsApp/Telegram/Lark | .env grep (telegram/slack/whatsapp/imessage/sendblue/photon/lark/feishu/teams) = **0 บรรทัด** → ทางเข้าบอตมีทางเดียว = เว็บ (tailnet-only) |
| bot email | บอตมีที่อยู่เมลเอง | `bot_email_addresses` = 0; INBOUND_EMAIL_DOMAIN ว่าง |
| meetings | Zoom/Meet/Teams ผ่าน Recall.ai | ไม่มี MEETING_* ใน .env → ปิด |
| cloud agents | Cursor | `cloud_agents` = 0 (default none) |
| memory ภายนอก | Supermemory/Honcho/Hindsight | ใช้ memory ในตัว (`memory_documents` = 9) |

ข้อสังเกตแกน: **สายที่ต่อใช้จริง = โมเดล + MCP (Notion) + git ผ่าน credential — ที่เหลือยังปิดอยู่เพราะไม่ได้ใส่ค่า ไม่ใช่เพราะระบบไม่มี**

## สำหรับ draft (#122)
- ทุกประโยค docs = vendor claim ติดป้าย "ทีมผู้ทำระบุ/เอกสารระบุ"
- ตัวเลข DB = machine-verifiable (ตาราง/นับแถว วันที่ 2026-11-19)
- ห้าม print ค่า .env ใด ๆ — เขียนเป็น "ไม่มี credential ของ platform แชตตัวไหนในไฟล์ตั้งค่า"
- Sibling guard: #121 rakazo-local-docker (การติดตั้ง+เหตุการณ์ push วันแรก) — คำ 403/cherry-pick/egress/RAM 2GB/compose up/YouTube Library = 0; โมเดล local พูดใหม่ด้วยภาษา OpenAI-compatible ไม่รีเลย์เรื่องติดตั้ง
