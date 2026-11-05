# Research: Notion เป็นสมุดกลางของตัวช่วยหลายตัว (MCP hub)

Researched: 2026-11-05 | เรียกใช้โดย: brief "รีเสิร์ชหาข้อมูลเกี่ยวกับการใช้ notion ต่อกับฮาร์เนสต่าง ๆ เช่น claude code, codex, cursor และอื่น ๆ เพื่อให้เป็นสมองส่วนกลาง แล้วลอง draft มาเป็น content"

## ข้อเท็จจริงที่ยืนยันแล้ว (ข้ามแหล่ง)

1. **Notion มี MCP server เป็นทางการ (hosted)** — `https://mcp.notion.com/mcp` (Notion docs overview + scalekit + usecarly) — ผู้ใช้เชื่อมผ่าน OAuth แล้วตัวช่วยทำงานด้วยสิทธิ์ของผู้ใช้นั้น
2. **ทิศทางเข้า (assistant → Notion):** clients ที่ docs ระบุ = Claude, ChatGPT, Gemini (developers.notion.com/guides/mcp/overview); tool families 8 กลุ่ม = search/read, comments, pages, databases, files, skills+agents, calendars (developers.notion.com/guides/mcp/mcp-supported-tools)
3. **Claude Code:** docs เป็นทางการ `claude mcp add` (code.claude.com/docs/en/mcp) + plugin เป็นทางการจาก Notion เอง `makenotion/claude-code-notion-plugin` (MCP server + slash commands, one-click install)
4. **Cursor:** docs เป็นทางการ — MCP connects Cursor to external tools "like GitHub, Linear, or Notion so Agent can use them during conversations" (cursor.com/help/customization/mcp)
5. **Codex:** docs เป็นทางการ (developers.openai.com/codex/mcp) — config อยู่ `~/.codex/config.toml`, คำสั่ง `codex mcp add`, รองรับ stdio + streamable HTTP + OAuth; แชร์ config ข้าม Codex CLI / IDE extension / ChatGPT desktop
6. **ทิศทางกลับ (Notion Agent → แอปอื่น):** Notion Agent/Custom Agents ต่อออกไปยัง MCP server อื่นได้ (notion.com/help/connect-mcp-servers-to-your-notion-agent + mcp-connections-for-custom-agents) — Notion อยู่ได้ทั้งสองขั้วของสายพาน
7. **ขีดจำกัด MCP-vs-API:** multi-user product ยังต้อง REST API layer (one token per user/workspace) + hosted MCP ทำงานในสิทธิ์ per-user (scalekit) — จุดที่ MCP "หยุด" คือ auth หลายผู้ใช้และงาน batch หนัก ไม่ใช่ความสามารถอ่านเขียน

## มุมที่เลือก (lens)

**สมุดกลาง (shared notebook)** — ตัวช่วยหลายตัว คนละโปรแกรม ทำงานต่อกันได้เพราะสิ่งที่สะสมไว้อยู่นอกตัวมัน ไม่ใช่เพราะตัวช่วยเก่งขึ้น — แกน = "ความต่อเนื่องของงานอยู่ที่ที่เก็บ ไม่ใช่ที่ตัว"
- ทำไม lens นี้: brief ใช้คำ "สมองส่วนกลาง" แต่ สมอง = signature vocab ของ #98 (โมเดล=สมอง harness=ร่างกาย) → ต้องหลบไปใช้ภาพ "สมุด/โน้ต" แทน และเลี่ยงทั้ง สมอง/ร่างกาย
- parked: รายละเอียด setup แต่ละ client (เป็น TECH form อีกโพสต์), OAuth multi-user (ขั้น enterprise), ทิศทางกลับ Notion Agent→apps (กิ่งไว้ทำต่อ)

## Sibling guards (สแกนแล้ว)

- **#98 ai-harness-body-brain (published 11-04):** สมอง/ร่างกาย/โมเดล = 0 — แกนต่าง: #98 = กายวิภาคของ "ตัวเดียว", ที่นี่ = ที่เก็บร่วมของ "หลายตัว"
- **20261105 compression-random-board (filed วันนี้, feed-adjacent):** กระดาน/บีบอัด/ความจำหนัก = 0 — แกนต่าง: compression = การบีบอัด "ในตัวคนเดียว", ที่นี่ = สิ่งที่สะสมอยู่ "นอกตัว" (ความจำ ≤1 ครั้ง ใช้ โน้ต/สมุด/สิ่งที่สะสม เป็นพาหะหลัก)
- **external-ram-three-lists (2026-09-24):** RAM/รายการสามแผ่น = 0 — ของเก่า, คนละกรอบ (personal lists)
- **dissonance lane (วันนี้):** ความเชื่อ/ลงรอย = 0

## Evidence class (rule 178)

- capabilities ทั้งหมด = DOCUMENTED (docs เป็นทางการทั้งสองฝั่ง) ไม่ใช่ hands-on ทุก client — ในเนื้อต้องมีบรรทัด label ("ระบุไว้ในเอกสาร ยังไม่ใช่ผลทดลองทุกการตั้งค่า")
- เคสจริงที่ narrator attested: ร่างที่เขียนเมื่อคืนถูกยิงเข้าฐานกลาง เช้ามาอีกตัวอ่านต่อได้ — เล่าระดับ class ได้ (ไม่อ้างชื่อโพสต์/จำนวน block)

## Register

CURRENT FORM (system/mindset) — story opener (สองตัวช่วยต่องานกัน) → old way (โน้ตตายพร้อมหน้าต่าง) → pattern (สมุดกลาง + ช่องมาตรฐาน MCP gloss ×1) → two-way movement → > bold fork → near-miss (สมุดไม่ฟรี: ต้องคัด/ต้องตรวจ) → duck closer + สัญญาณ "เล่าใหม่ครั้งที่สอง"
- เรา 1 / คุณ 0 / พร 0 / '?' 0 / เพราะ 0 / เลขอารบิก 0 / brands ใน body มีแค่ Notion (subject), Claude Code-Codex-Cursor-ChatGPT-Gemini = header only
