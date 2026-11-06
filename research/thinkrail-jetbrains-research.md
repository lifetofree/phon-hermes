# Research: ThinkRail (JetBrains incubator — agentic IDE)

Researched: 2026-11-05 | brief: "รีเสิร์ชหาข้อมูลเรื่อง Thinkrail IDE ของ jetbrains และเอามา draft content"

## ข้อเท็จจริงยืนยันข้ามแหล่ง (≥3 อิสระ)

1. **ตัวตน:** ThinkRail = โปรเจกต์ incubator ของ JetBrains (JetBrains InnovationHub), open source Apache-2.0, repo `JetBrains/thinkrail`, เว็บ thinkrail.ai — ประกาศเมื่อ ส.ค. 2026 (blog แรก 2026-08-19 โดย Maciej Gorywoda) — ยัง early stage (release ล่าสุด 0.3.1, พ.ย. 2026)
2. **มันคืออะไร:** agentic IDE ที่หุ้ม (wrap) coding agent ชื่อ `pi` — pi เก็บครอง models/skills/compaction/cost/session-state, ThinkRail เก็บครอง workspace/editor/wire ("thin host" — piagent.fyi + README)
3. **Worktree isolation (core):** ทุก workspace = git worktree จริง — สาขา + ไดเรกทอรีของตัวเอง; agent หลายตัวทำงานขนานได้โดยแต่ละตัวอยู่สาขาตัวเอง; **สายหลัก (main) สะอาดจนกว่าจะสั่ง merge** (blog เปิดตัว + landing + besthub)
4. **Spec graph (หัวข้อแยก):** SPEC.md หลายฉบับอ้างถึงกันเป็นกราฟ — agent อ่าน/ค้น/บำรุงรักษาเป็น "documentation, guidelines, and handrails for thinking" = ความรู้โปรเจกต์ที่มีชีวิต (living specs)
5. **0.3.1 (พ.ย. 2026):** search box รวม, ต่อ model server เองได้ (Ollama/LM Studio/vLLM/llama.cpp presets), ติดตั้ง pi package ผ่าน UI — เก็บไว้หัวข้อ TECH อนาคต
6. **ขีดจำกัด (honesty):** ยัง early stage; Intel mac ไม่มี prebuilt; ของ oflight review ระบุ "as of October 2026 it is..." (ยังดิบ) — เขียนเคสเป็น documented ไม่ใช่ hands-on

## แหล่ง

- https://github.com/JetBrains/thinkrail (repo เจ้าของ)
- https://thinkrail.ai/blog/introducing-thinkrail/ (ประกาศทางการ 2026-08-19)
- https://thinkrail.ai/ (landing — "spec-first", Apache-2.0)
- https://piagent.fyi/news/thinkrail-jetbrains-pi-ide/ (community รายงาน 2026-08-21 — thin host จำแนก ownership)
- https://www.oflight.co.jp/en/columns/jetbrains-thinkrail-ide-pi-agent-2026 (รีวิว)
- https://thinkrail.ai/blog/thinkrail-0-3-1-release/ (release ล่าสุด)

## Lens ที่เลือก (ONE lens — news/tool-event recipe)

**สายแยก (isolated lane)** — ทุก workspace เป็น worktree แยก สายหลักไม่ถูกแตะจนกว่าจะ merge → แกน content: **ความกล้าทดลองมาจากการแยกความเสี่ยง ไม่ใช่ความมั่นใจ** — ทดลองได้เต็มที่เมื่อการทดลองไม่ยืนอยู่บนของที่ใช้จริง
- ต่างจากโพสต์ที่ค้าง (notion-shared-notebook = สมุดกลาง/ความต่อเนื่อง) — อันนี้ = การแยกสาย/ความกล้า
- parked: spec graph (ความรู้โปรเจกต์ที่มีชีวิต — ทำโพสต์ต่อหรือผูกกับ notebook draft ได้), 0.3.1 features (TECH form), pi ownership split (ชน sibling #98 ร่างกาย-สมอง → ห้ามแตะ)

## Sibling guards (CUT 0)

- #98 ai-harness-body-brain: สมอง/ร่างกาย/โมเดล/harness = 0
- #101 compression/map: แผนที่/ถามทาง = 0
- notion-shared-notebook (ค้าง): สมุด/โน้ต/สมองกลาง = 0
- charted-course: เส้นทาง/เข็มทิศ = 0
- ตัวเลข/วันที่/เวอร์ชัน = header only (0.3.1, ส.ค. 2026 ไม่ลง body)

## Evidence class (rule 178)

- capabilities ทั้งหมด = DOCUMENTED ("ตามเอกสารโปรเจกต์/ทางทีมระบุ") — ไม่ใช่ hands-on ทุก flow
- ชื่อแบรนด์ใน body: JetBrains / ThinkRail (เป็นหัวเรื่องของงาน — โอเคสำหรับ tool post), pi + ชื่อ model servers = header only
