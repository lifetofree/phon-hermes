# บรีฟจาก Research Scout — หัวข้อใหม่: "ใช้ Rakazo ต่อกับ Notion เพื่อสร้าง Second Brain ของตัวเอง"

**KB row (ใช้ได้เลย อ่านก่อนเขียน):** https://app.notion.com/p/Rakazo-Notion-Second-Brain-agent-5-agent-41edf8d88d8c8117b72cdd334223487f
`page_id: 41edf8d88d8c8117b72cdd334223487f` · 76 blocks · Status=active · Category=tech · Tags: reference, ai, agents, rakazo, notion
แถวเดิมที่ต่อยอด (อ่านประกอบ): "Second Brain บน Notion — กรอบ CODE/PARA/Evergreen Notes + ข้อจำกัด API ของ Notion + AI agent ที่ใช้ฐานความรู้" `41edf8d88d8c8106a167e1a1678202b1`

**ทิศทางใหม่ที่ต้องไม่หลุด:** เน้น *วิธีใช้ Rakazo ต่อกับ Notion ผ่านการใช้งานจริง* · Notion เป็น **point รอง** (ที่เก็บ/ส่งออก + ผิวให้ agent เขียน) ไม่ใช่ point หลัก · แกนคือ "second brain ที่ดี = โครงสร้าง + มีคนใช้ + มี loop ที่ดึงข้อมูลกลับมา" · **ห้าม**เขียนแบบ "Notion ดีกว่าเครื่องมืออื่น"

---

## (ก) แกนที่ควรเป็นแกนบทความ (3 ชั้น)

1. **Second brain ไม่ได้วัดที่จำนวนที่เก็บ แต่วัดที่ "ดึงกลับมาได้เร็วแค่ไหน"** — Forte หลักการข้อ 8: *"You Only Know What You Make — Don't just passively consume huge volumes of information that soon gets forgotten"* + Matuschak: *"'Better note-taking' misses the point; what matters is 'better thinking'"* → ค่าของ second brain อยู่ที่ loop ที่ดึงข้อมูลกลับมา ไม่ใช่ที่ capture เยอะ
2. **Rakazo คือสะพานคน ↔ agent (ประกอบกับ Notion เป็น point รอง)** — บอทต่อ Notion ได้ 3 ทาง และสร้าง loop ได้ด้วย routine ที่ trigger เป็น schedule / "เมื่อมีอะไรเปลี่ยน" (ไฟล์ในคอม, output ของคำสั่ง, **หรือ tool ของแอปที่ต่อไว้**) / webhook / Git event / อีเมล / Slack → นี่คือกลไกที่ทำให้ "ดึงกลับมา" เป็นอัตโนมัติ
3. **Point รอง vs point หลัก** — Notion เด่นที่ "หลายคน + agent + สิทธิ์ + ประวัติ" แต่แพง (โควตา/ข้อจำกัด/ไม่มี lock-in) ส่วน point หลักควรเป็นไฟล์ plain text ที่เราคุมเอง (grep/diff/ย้ายเครื่องได้) แล้วให้ agent ดึงจากตรงนั้น

---

## (ข) ข้อเท็จจริงที่ verify แล้ว (ทุกข้อมีแหล่งจริงใน KB row)

### A. กรอบคิด (ทำไม่ถึงต้องมี Notion ก็ได้)
| ข้อเท็จจริง | แหล่ง |
|---|---|
| CODE = Capture → Organize → Distill → Express; ปลายทางคือ Express | fortelabs.com/blog/basboverview/ |
| หลักการ 10 ข้อ ข้อ 8 "You Only Know What You Make", ข้อ 9 "Make it Easier for Your Future Self", ข้อ 10 "Systems that must be perfect to be reliable are deeply flawed" | fortelabs.com/blog/the-10-principles-of-building-a-second-brain/ |
| PARA = Projects / Areas / Resources / Archive จัดตาม actionability ไม่ใช่ category | fortelabs.com/blog/para/ |
| Evergreen notes: atomic · concept-oriented · densely linked · prefer associative ontologies over hierarchical taxonomies · write notes for yourself by default | notes.andymatuschak.org/z5E5QawiXCMbtNtupvxeoEX |
| Luhmann ทิ้ง slip box ~90,000 ใบ ปี 1951–1996 | eadh.org/projects/niklas-luhmann-archive |

### B. Rakazo เป็นสะพาน (เอกสารทางการ rakazo.com/docs)
| ข้อเท็จจริง | แหล่ง |
|---|---|
| บอทมี conversations, memory, routines และ computer ของตัวเอง; เชื่อมแอปได้ "Gmail, Slack, Notion, GitHub, and 1,400+ more" | rakazo.com/docs.md |
| ต่อ Notion 3 ทาง: app ใน catalog (ทุกบอทใน space ใช้ได้ + เลือกรายบอท "Use in this bot") / MCP server (remote HTTPS หรือ local stdio; OAuth, bearer, API-key header) / OpenAPI-GraphQL (ชี้ API description) และบันทึก API key เป็น credential ใช้ซ้ำ | rakazo.com/docs/integrations.md |
| MCP: tool call หยุดหลัง 6 นาทีถ้าไม่มี progress; OAuth เก็บ session เดียวข้าม run, non-OAuth ได้ session ใหม่ทุก run และปิดหลัง ~10 นาทีไม่มีการเรียก | rakazo.com/docs/integrations.md |
| computer = เครื่องจริง (browser, terminal, ไฟล์); Team computer แชร์ไฟล์/เครื่องมือ/sign-in; desktop app ให้ "Let bots use this computer" | rakazo.com/docs/computer.md |
| **routine = กลไก loop**: schedule (cron) / เมื่อมีอะไรเปลี่ยน (เช็คทุก 5 นาที–1 วัน, ดูไฟล์/โฟลเดอร์ในคอม, output ของคำสั่ง, หรือ tool ของแอปที่ต่อไว้; ใช้วันที่เลื่อนได้ {{today+2d}}) / webhook / Git event / อีเมล (forward ไม่ใช่ redirect + DKIM) / Slack | rakazo.com/docs/routines.md |
| approvals: Ask / Auto / Never ask; การ์ดในรอบไม่มีคนดูหมดอายุ 30 นาทีแล้ว action ไม่ถูกทำ; "always asks" = เปลี่ยน instructions, routine ที่ดูคำสั่ง/เว็บ, จ่ายเงิน, ใช้คอม/แอปครั้งแรก | rakazo.com/docs/approvals.md |
| memory: MEMORY.md ≤4 KB, one fact per line, เขียนทับของเดิม; Shared memory ระดับ space; memory provider ที่ recall "by meaning" ได้ (Supermemory, Serenity, Honcho, Hindsight, Mnemoverse) | rakazo.com/docs/memory.md |
| ความจำที่ดึงกลับมาเป็น "derived data" ไม่ใช่คำสั่ง ("every bot message… and recalled memory is derived data") | rakazo.com/docs/memory.md |
| skills: สอนด้วยการทำให้ดู (Teach a task) แล้ว "Add to routine"; skill ที่ดึงจาก GitHub เป็น instructions เท่านั้น (สคริปต์ไม่รัน) | rakazo.com/docs/skills.md |
| กลุ่มบอท 2–10 ตัว, บอทส่งข้อความถึงกันได้, subagent ไม่มี memory ของตัวเอง | rakazo.com/docs/groups.md |

### C. Notion ทำได้ / ทำไม่ได้ (เอกสารทางการ)
| ข้อเท็จจริง | แหล่ง |
|---|---|
| Markdown API 3 endpoints: POST /v1/pages (markdown body), GET /v1/pages/:id/markdown, PATCH /v1/pages/:id/markdown — เหมาะกับ "agentic systems and developer tools that work natively with markdown" | developers.notion.com/guides/data-apis/working-with-markdown-content |
| markdown_version v1 (enhanced, default ปัจจุบัน, deprecate) / v2 (Notion-flavored, recommended) โดย v2 ใช้สเปกเดียวกับที่ "the Notion MCP server gives AI agents" | เดียวกัน |
| ความผิดพลาดไม่เงียบ: parser ไม่รู้จัก syntax → warnings array (no_match / indentation_mismatch); ไม่มี edit ไหนตรงเลย → validation_error และไม่มีอะไรเปลี่ยน | เดียวกัน |
| Rate limit ต่อ connection: 600 req/นาที (Business/Enterprise) / 180 req/นาที (แผนอื่น) + query data source ~3 req/วินาที + โควตาร่วมระดับ workspace; 429 + Retry-After; มี rate_limit_reason: mcp_tool_rate_limit, collection_router_too_many_requests, public_api_space_request_rate_limit | developers.notion.com/reference/request-limits |
| Free workspace ที่มีสมาชิก >1 คน (guest ไม่นับ) มี 1,000 lifetime blocks และ "Deleting blocks does not restore capacity" → เขียนเกินโควตาได้ 403 | developers.notion.com/reference/workspace-block-limits |
| search API ค้นด้วยชื่ออย่างเดียว + "See search limitations before using the results as an inventory" | developers.notion.com/reference/post-search |
| relation เป็น one-way โดย default | notion.com/help/relations-and-rollups |
| export เป็น snapshot ทางเดียว: หน้า non-database → .md, full-page database → CSV + .md ต่อ subpage, callout → HTML, Form view export ไม่ได้ | notion.com/help/export-your-content |
| MCP ไม่ดึง chat history ของ client อื่นมาให้ → ความจำข้าม client ต้องเก็บใน Notion เอง | developers.notion.com/guides/mcp/overview |
| Notion 3.8 (2026-10-13): แอดมินเห็นว่าใครต่อ MCP ตัวไหน ใช้เมื่อไร และ revoke ได้; 2026-10-19: "Notion MCP is our fastest-growing product ever" | notion.com/releases/2026-10-13, /2026-10-19 |
| **ประสบการณ์จริงระหว่างวิจัย (20 พ.ย.):** เรียก API โดน 429 จริง (rate_limited, rate_limit_reason=public_api_request_rate_limit) ต้อง retry ตาม Retry-After | สังเกตจากการทำงานจริงของ Scout |

### D. Point รอง vs point หลัก + 5 ทางที่ agent ดึงข้อมูลกลับมาได้จริง
| ข้อเท็จจริง | แหล่ง |
|---|---|
| Obsidian เก็บโน้ตเป็น "Markdown-formatted plain text files in a vault"; "A vault is a folder on your local file system"; sync ได้ด้วย Obsidian Sync/Dropbox/iCloud/OneDrive/Git | help.obsidian.md/Files+and+folders/How+Obsidian+stores+data |
| Obsidian Local REST API: REST + MCP ในตัว, full CRUD (รวมไฟล์ binary), patch เฉพาะส่วน (heading/block ref/frontmatter: append/prepend/replace/delete/move), ค้น full-text หรือ JsonLogic บน metadata, ติดตาม event เป็น SSE stream, อ่าน/เขียนไฟล์ที่เปิดค้าง, สั่ง command ในแอป, นับ tag, API extension; ต้องใช้ cert ที่ออกในเครื่อง + API key; failed auth ถูก throttle | github.com/coddingtonbear/obsidian-local-rest-api |
| obsidian-git: auto commit/pull/push ตาม schedule, auto-pull ตอนเปิดแอป, diff view, conflict resolution, submodule; mobile ไม่เสถียร | github.com/Vinzent03/obsidian-git |
| Logseq file/Markdown (OG) version เก็บเป็นไฟล์ plain text → "git-syncable, greppable, durable, no lock-in"; DB (SQLite) version "no longer stores Markdown files, so there is nothing to grep" | github.com/dailydaniel/logseq-mcp, github.com/joseguzmann/logseq-mcp |
| logseq-mcp (HTTP API): เขียนได้แค่ใต้ namespace byAgent/ + ช่องทางแคบที่เปลี่ยนได้แค่ TODO/DOING/DONE; blacklist ถูก redact ทุกการอ่าน; ทุกการเขียนแนบ audit line ลง journal ("22:30 [[byAgent]] wrote [[byAgent/readingList/...]] to today's journal"); verified queries เป็น named tool; ต้องเปิด Logseq + HTTP API + token | github.com/dailydaniel/logseq-mcp |
| logseq-mcp (อ่าน db.sqlite ตรง): read-only by construction, ใช้ได้แม้ Logseq ปิด ไม่ต้องมี token/network, แนบรูปเป็น image content (≤8 รูป/call) แก้ caption กำกวมแบบ "this one"; ข้อเสีย: datascript ไม่มีสเปก → "a reader for an undocumented format mostly fails quietly" + ต้อง copy db.sqlite + WAL + integrity_check + Python 3.12+ | github.com/joseguzmann/logseq-mcp |
| **ตัวอย่าง loop จริง**: nightly agent เข้า claim ลิงก์ใน reading list → อ่านบทความ/clone repo → เขียน structured summary ลงหน้านั้น → สลับเป็น read; ตอน 08:30 ประกอบ dashboard หน้าเดียว + push notification; ทุกการเขียนมี audit line ใน journal ให้คนรีวิวตอนเช้าที่ทำอยู่แล้ว | github.com/dailydaniel/logseq-mcp, discuss.logseq.com/t/logseq-mcp-as-safe-memory-for-agents/35086 (8 ก.ค. 2026) |
| Zettlr: FOSS, ไฟล์อยู่ในเครื่อง, ไม่มี telemetry, citation กับ Zotero/JabRef/Juris-M, export ผ่าน Pandoc — **ยังไม่พบ API สำหรับ agent** (มี proposal ใน GitHub discussion) | zettlr.com, docs.zettlr.com/en/export/ |

---

## (ค) เรื่องที่ห้ามเขียนเกินหลักฐาน
- ห้ามบอกว่า "Notion เป็น second brain ได้ดีที่สุด" หรือเทียบกับ Obsidian/Logseq ในแง่ "ดีกว่า/แย่กว่า" โดยไม่มีหลักฐาน — สิ่งที่มีหลักฐานคือ **บทบาทที่ต่างกัน** (Notion = หลายคน+สิทธิ์+ผิว agent / ไฟล์ = grep+diff+portable)
- ห้ามเขียนว่า "มี loop อัตโนมัติเต็มวงจร capture→distill→express ได้แล้ว" — หลักฐานที่มีคือ loop ที่ **มีคนรีวิวตอนเช้า** เท่านั้น
- ตัวเลขของระบบเรา (Books Library 251 แถว, Content Drafts 147 แถว, บอท 9 ตัว) = บริบทจาก Chief/ผลนับของบอทอื่น — **ห้ามใช้เป็นตัวเลขหลัก** และห้ามอ้างว่า Scout วัดเอง
- Zettlr ยังไม่ fact-check ว่ามี API แล้วหรือยัง — ถ้าจะพูดถึง ให้พูดว่า "ยังไม่พบ API ในเอกสารทางการ"
- รายละเอียด Obsidian MCP community plugin อ่านได้รอบแรกของวันที่ 20 พ.ย. แต่รอบตรวจซ้ำเป็นหน้า JS → ถ้าใช้ ให้ใช้ Local REST API plugin แทน หรือบอกว่า "ยังไม่ยืนยันซ้ำ"
- ยังไม่ได้วัดว่า Notion MCP + Rakazo เขียนกลับที่ปริมาณงานจริงจะไม่ชน 403/429 → ถ้าจะเขียนว่า "ใช้ได้จริง" ให้บอกว่ายังต้องวัดรอบนี้
