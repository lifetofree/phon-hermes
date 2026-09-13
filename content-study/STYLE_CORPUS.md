<!--
LIVING FILE — Do not rewrite wholesale.
This is the evidence layer under WRITING_STYLE_GUIDE.md (the distilled guide).
Updated weekly by cron job `weekly-wp-archive-sync`.
To add analysis of newly archived posts: APPEND a new entry under "## Updates"
in the form "### YYYY-MM-DD — new posts: <slugs>" and extend "## Evolution Notes"
with any new conventions. Do not delete or re-order existing sections.
All quotes below are verbatim from the corpus (same orthography as source files).
-->

# Adduckivity Style Corpus — evidence-based analysis (21 posts)

## Corpus

| date | slug | file path | words | type |
|---|---|---|---|---|
| 2026-01-13 | energy-budget-vs-time-management | posts/energy-budget-vs-time-management.md | 99 | A |
| 2026-02-26 | engineering-friction-habit-design | posts/engineering-friction-habit-design.md | 182 | A |
| 2026-04-06 | weekly-calibration-monday-frictionless | posts/weekly-calibration-monday-frictionless.md | 484 | A |
| 2026-05-04 | binary-decision-protocol-zero-friction | posts/binary-decision-protocol-zero-friction.md | 384 | A |
| 2026-05-09 | the-black-box-protocol-logs-05 | posts/the-black-box-protocol-logs-05.md | 422 | A |
| 2026-05-10 | one-person-business-os-ai | posts/one-person-business-os-ai.md | 419 | A |
| 2026-05-11 | system-failure-not-lazy | posts/system-failure-not-lazy.md | 414 | A |
| 2026-05-14 | context-switching-hidden-cost | posts/context-switching-hidden-cost.md | 388 | A |
| 2026-09-03 | 9router-keyring-security | web-archive/9router-keyring-security.md | 684 | B |
| 2026-09-04 | 20260904-cnt-tailscale-serve-local-llm | web-archive/20260904-cnt-tailscale-serve-local-llm.md | 806 | B |
| 2026-09-05 | 20260905-cnt-autoclaw-one-click-ai-agent | web-archive/20260905-cnt-autoclaw-one-click-ai-agent.md | 1480 | B |
| 2026-09-06 | 20260906-cnt-autoclaw-zcode-workflow | web-archive/20260906-cnt-autoclaw-zcode-workflow.md | 717 | B |
| 2026-09-07 | 20260907-cnt-local-llm-laptop-offline-guide | web-archive/20260907-cnt-local-llm-laptop-offline-guide.md | 949 | B |
| 2026-09-07 | 20260907-cnt-local-llm-speed-of-your-own | web-archive/20260907-cnt-local-llm-speed-of-your-own.md | 100 | C |
| 2026-09-07 | 20260907-cnt-ollama-server-team-infrastructure | web-archive/20260907-cnt-ollama-server-team-infrastructure.md | 1531 | B |
| 2026-09-08 | superclick-macos-media-io-layer | web-archive/superclick-macos-media-io-layer.md | 1111 | B |
| 2026-09-09 | task-logger-memento-mori | web-archive/task-logger-memento-mori.md | 492 | B |
| 2026-09-09 | unfair-game-protocol | web-archive/unfair-game-protocol.md | 372 | A |
| 2026-09-10 | dopamine-system-diagnostic-protocol | web-archive/dopamine-system-diagnostic-protocol.md | 494 | A |
| 2026-09-10 | unsloth-studio-local-finetune | web-archive/unsloth-studio-local-finetune.md | 1440 | B |
| 2026-09-11 | essentialism-the-admin-access | web-archive/essentialism-the-admin-access.md | 355 | A |

Type key: A = System/Mindset, B = Tool Review, C = other. (Word count = `wc -w` on the archived file, including front-matter lines.)

## Voice Markers (evidence)

### Opening hooks
- Dominant pattern: first-person question with คับ — 13/21 posts contain "เคย" in the first body paragraph. Verbatim examples:
  - "คุณเคยสงสัยมั้ยคับว่า ทำไมในวันที่คุณ 'รู้' ทุกอย่างว่าต้องทำอะไร… แต่ร่างกายของคุณกลับเลือกที่จะ 'นั่งนิ่ง' อยู่ที่โต๊ะทำงาน?" (system-failure-not-lazy)
  - "เคยมีวันที่คุณนั่งอยู่หน้างานที่สำคัญที่สุดของวัน… แล้วมือก็หยิบโทรศัพท์ขึ้นมาไถ โดยไม่มีเป้าหมายเลยมั้ยคับ" (dopamine-system-diagnostic-protocol)
  - "เคยมั้ยคับ — AI tool ตัวหนึ่งใช้เขียนโค้ด อีกตัวใช้รันงาน agent บน desktop" (20260906-cnt-autoclaw-zcode-workflow)
- Secondary pattern: quoted overheard line, then "คุณเคยเจอประโยคนี้มั้ยคับ?" — "เธอๆ… รบกวนถามอะไรนิดหนึ่งได้มั้ยคับ? แป๊บเดียวจริงๆ" (context-switching-hidden-cost)
- Rarer: rhetorical list (unfair-game-protocol: "จะมีสักกี่คนบนโลกนี้ ที่เก่งเท่าอัลเบิร์ต ไอน์สไตน์"), a single aphorism (20260907-cnt-ollama: "ค่า API เดือนละเท่าไหร่ — แล้วถ้าเป็น $0 ล่ะ"), or a quote (task-logger: "Dance to the Death").
- Signature misdiagnosis move: "พรขอบอกคุณตรงๆ เลยนะคับว่า… คุณกำลังวินิจฉัยโรคผิด (Misdiagnosis) คับ" (system-failure-not-lazy); repeated nearly verbatim in 9router-keyring-security: "เป็นการวินิจฉัยโรคผิด (Misdiagnosis) — ปัญหาไม่ใช่… แต่มันคือ Single Point of Failure ในสถาปัตยกรรมการทำงานของคุณ"

### First person: พร + particles
- "พร" as self-reference: 203 occurrences across 21 files; "คับ" 202 times — they appear in near lockstep. "มั้ยคับ" 9 times ("เคยสงสัยมั้ยคับ").
- Variant spellings: "คร้าบ" 2×, "ค้าบ" 5× (e.g. "คอมเมนต์บอกแอดหน่อย… เดี๋ยวแอดช่วยออกแบบกำแพงให้คร้าบ! 👇", "แล้วพบกันในโพรโทคอลถัดไปนะค้าบ!"). Older posts (2026-01..02) use "แอด" occasionally instead of "พร" (engineering-friction-habit-design, energy-budget).
- Expert-credence framing: "ในฐานะที่พร…" appears 3× (system-failure-not-lazy: "ในฐานะที่พรทำงานด้านระบบวิศวกรรมข้อมูลและพัฒนาแพลตฟอร์มระดับประเทศมาหลายปี"), binary-decision ("ในฐานะที่พรต้องคุมระบบที่มีความเสี่ยง").
- Self-deprecation in tool posts: "เพราะพรก็ไม่ได้ลงลึก หรือเก่งอะไรมากมาย" (20260907-cnt-local-llm-speed-of-your-own); "ถ้าให้พรอธิบายเป็นภาษาบ้านๆ" (9router-keyring-security).

### Engineering metaphor density (counts across all 21 files, case-insensitive)
Top terms: RAM 83, Server 52, GPU 50, API 48, CLI 44, VRAM 28, Token 27, Protocol/โพรโทคอล 45 combined, Quota 19, Friction 18, สถาปัตยกรรม 17, Dopamine 15, Runtime 14, Inference 12, CPU 11, "ค้าง" 11, "แบต" 10, Offline 10, Quant 8, Latency 6, Crash 6, Single Source of Truth 5, sudo 5, Cortisol 5, Patch 4, Firewall 4, Reboot 2, Overclock 2, Circuit Breaker 3, Queue 3, Cache 3, Bunker 1, Telemetry 1, Firmware 1.
- Core brain mapping (constant across corpus): สมอง = RAM/Server (e.g. "พลังงานใน RAM ของสมองจะค่อยๆ ถูกใช้ไปจนหมด" — system-failure-not-lazy), อารมณ์ = background process (unfair-game-protocol: "comparison bias คือ background app ที่กิน RAM โดยไม่สร้าง output ใดๆ"), การพัก/ซ่อม = maintenance (dopamine: "D.O.P.A.M.I.N.E. คือ maintenance schedule ที่ Lembke เขียนไว้ให้").
- 2026-09 corpus adds a hardware/LLM layer the originals lack: VRAM, Quant/Q4_K_M, offload, GPU (50 hits), Inference, VRAM 28, Quota, Token — e.g. "รัน Qwen3 27B quant Q4_K_M offload ลง GPU" (20260904-cnt-tailscale-serve).

### Protocol & framework naming
- XX-0N pattern (only 4 names in corpus, all from the 2026-05 originals): CORE-06 (one-person-business-os-ai), LOGS-05 (the-black-box-protocol-logs-05), ACT-05 (referenced in one-person-business-os-ai), DEC-01 (binary-decision-protocol-zero-friction).
- Acronym frameworks: N.E.S.T (binary-decision: "เช็กผ่าน N.E.S.T — N – Nervous System, E – Energy, S – System, T – Trajectory"), D.O.P.A.M.I.N.E. (dopamine-system-diagnostic-protocol: 8 steps "เก็บ Log → หา Trigger → บันทึก Error → Factory Reset 30 วัน → Monitor → วิเคราะห์ → เซ็ต Firewall → A/B Test"), "The Calibration Loop" / "The Unfair Game Protocol" (4 ขั้น).
- Named conditions in quotes: "System Freeze", "Spinning Wheel of Death", "Decision Fatigue", "Attention Residue", "Sunday Scaries Bug", "The Self-Gaslighting Script", "Media Fragmentation", "The Curse of AI Bloat" — each coined with a quote + one-line definition.
- Named devices: "Circuit Breaker", "Digital Bunker", "Managerial Firewall", "Single Source of Truth", "Brand DNA Vault", "The Recovery Protocol V1".

### Duck OS Laws
- Law #1: System > Emotion; Law #2: Asset > Activity; Law #3: Protect System — recited as a set only in unfair-game-protocol (2026-09-09), where all three are applied one-by-one. Single-law invocation is the norm elsewhere ("ใน Duck OS เรามีกฎเหล็กข้อที่ 3 คือ Protect System").
- Sign-off lines: "System > Emotion. เลิกเดาชีวิต แล้วเริ่มดู Data กันเถอะคับ! 🦆⚡" (the-black-box); "System > Emotion. ตัดความลังเลทิ้ง แล้วรันระบบของคุณด้วยความแม่นยำคับ! 🦆⚡" (binary-decision). 2026-09 variant: "Map your mind. Run your system. แล้วพบกันในโพรโทคอลถัดไปนะค้าบ!" (9router).
- "มุมของ Duck OS" is a recurring 2026-09 subheading (5×) that translates the post's lesson into the 3 Laws.

### Closing patterns
- Originals (2026-05): section "## บทสรุปจากพร" (2×) or "## 6. บทสรุป: …", then CTA: Session online "พรรับจำกัดเพียง 20 ท่าน/ที่นั่ง เท่านั้น", free "Duck OS Stater Kit" via duckshort.cc link (note the brand's own misspelling "Stater Kit" in 2 posts), sign-off "แล้วพบกันใน Session นะค้าบ".
- 2026-09: closer is "สรุปแบบวิศวกรเป็ด" as a literal hashtag-style section label (12/13 web-archive posts; written "#สรุปแบบวิศวกรเป็ด" in 7, plain "สรุปแบบวิศวกรเป็ด" in 5), then a one-line Duck OS takeaway, then soft CTA. Example (unfair-game-protocol): "ถ้าพรช่วยคุณหาไพ่ของคุณได้ — … มาคุยกันที่ Session กระจุกคุณภาพ (รับจำกัด 20 ท่าน)".
- Tool-review closers are question CTAs: "ลองแล้วเป็นยังไงกันบ้าง? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้พรทำภาคต่อเรื่องไหน บอกได้เลยค้าบ" (20260904-cnt-tailscale-serve); "ใครลองแล้วเป็นยังไงบ้างแวะมาเล่าให้ฟังกันหน่อยนะค้าบ" (20260905-cnt-autoclaw).
- Product launch variant: "ตอนนี้เป็น 1st pilot 50 ที่นั่งคับ first come first serve" (task-logger-memento-mori).
- "PS." / "ป.ล." asides appear in 4 posts (weekly-calibration, task-logger, 20260904-cnt-tailscale, 20260907-cnt-local-llm-speed).

### Hashtags (all 21 tag lines collected)
- Constant core: #Adduckivity (21/21), #DuckOS (20/21), #NeuroDivergent (17/21).
- Per-post topic tags follow; most frequent extras: SystemThinking 6, LocalLLM 5, Productivity 4, SystemsFirst 3, DataDrivenLife 2, AIDev 2, DevOps 2, ADHD 2, Ollama 2.
- Old posts (2026-01..02) used Thai tags (#เป็ดปิดงาน #TheUnbreakableDuckOS #พัฒนาตัวเอง #มนุษย์เงินเดือน); 2026-09 uses no Thai tags.
- 2026-09 quirk: "#สรุปแบบวิศวกรเป็ด" appears as a section label 6× — it is a heading convention, not a tag (the real tag line follows it).

## Structure Patterns

### Word count by type (measured)
- Type A (11 posts): avg 365 words (range 99–494).
- Type B (9 posts): avg 1023 words (range 492–1531).
- Type C (1 post): 100 words.
- Originals (8, 2026-01..05) avg 349; web-archive (13, 2026-09) avg 810.

### Section headings
- Originals use markdown `##`/`###` headings; web-archive posts use **no markdown headings at all** — plain text with "." separator lines (207 such lines across the 21 files; 2026-04..05 originals 1–2 per post, 2026-01..02 originals 9–11, web-archive 9–25 per post).
- Two numbering conventions in originals:
  1. Zero-padded debug style (2 posts): "## 00: Ingestion Phase", "## 01: The Prefrontal Cortex Server", "### 00: The Ping of Doom (Cortisol Hook)", "### 01: RAM Analogy: …" — heading = NN: English name (Thai gloss).
  2. "N. Title" style (5 posts): "## 1. Bug Report: …", "## 2. …", "## 3. …", "## N. บทสรุป: …". "Bug Report" is the standard first section (4×).
- Sub-steps: "### Stage 1: Clearing the Logs (การล้างแคชอดีต)" (weekly-calibration), "### A. Status Logs / B. Performance Logs / C. Error Logs" (the-black-box), "### Department A: The CEO (Vision & Strategy)" (one-person-business).
- English term convention: English term in quotes + Thai gloss in parentheses — "'Decision Fatigue' หรือการต้องตัดสินใจเรื่องเล็กๆ น้อยๆ ตลอดวัน"; or Thai first + English in parens — "ความไม่แน่นอน (Uncertainty)".

### Data conventions
- Concrete numbers always: "23 นาที" (context-switching), "35,000 ครั้ง" (binary-decision), "20 ท่าน", "$19.99", "$0.22 per 1M input / $0.66 per 1M output", "5,000 free credits".
- Comparison tables in tool reviews (markdown tables: AutoClaw vs OpenClaw, Ollama vs Unsloth Core, "Part 1 (laptop) / Part 2 (server)").
- Pros/cons + pricing + "เหมาะกับใคร / ไม่เหมาะกับใคร" + per-user-level tips (มือใหม่ / power user) in type B posts.
- Citations: researcher + institution + year — "ศาสตราจารย์ Sophie Leroy จาก University of Minnesota", "Ericsson (1993)", "David Epstein เขียนไว้ใน Range (2019)", "Leon Festinger … ตั้งแต่ 1954 ใน A Theory of Social Comparison Processes", "Dr. Anna Lembke (Dopamine Nation)". English book quotes with attribution: "'Begin at once to live, and count each separate day as a separate life.' — Seneca".

## Evolution Notes

1. **Length & format shift (2026-05 → 2026-09).** Originals: 349 words avg, markdown headings, numbered sections. Web-archive: 810 words avg, no markdown headings, "."-separated short paragraphs (stream-of-consciousness, e.g. 20260907-cnt-local-llm-speed: one continuous paragraph). Type B reviews now run 700–1500 words with tables, pricing, TL;DR ("TL;DR" appears 2× only in 20260905-cnt-autoclaw).
2. **Closing convention changed.** "## บทสรุปจากพร" (2026-05) → "สรุปแบบวิศวกรเป็ด" as a hashtag-style section label (12/13 of 2026-09 posts) + "มุมของ Duck OS" subheading (5×). The 3-Laws block became a standing checklist in mindset posts (unfair-game-protocol).
3. **CTA maturation.** 2026-05: Session online + "จำกัด 20 ท่าน" + "Duck OS Stater Kit ฟรี". 2026-09: product-pilot CTAs ("1st pilot 50 ที่นั่ง first come first serve"), series follow-ups ("ถ้าอยากให้พรทำภาคต่อเรื่องไหน บอกได้เลยค้าบ", "คราวที่แล้วพรเขียนเรื่อง…"), and the new sign-off "Map your mind. Run your system." (9router).
4. **Metaphor vocabulary expanded.** Originals: RAM/Server/CPU/Cache/Reboot/Circuit Breaker. 2026-09 adds the full LLM/infra layer — VRAM, Quant, offload, Quota, Token, Inference, CLI, GPU — because the tool-review line became a local-LLM series (5 consecutive posts 2026-09-04..07: tailscale serve → AutoClaw → AutoClaw x ZCode → laptop guide → ollama server → "speed of your own").
5. **Voice softened in personal posts.** 2026-09 personal posts are conversational and self-deprecating ("พรก็ไม่ได้ลงลึก หรือเก่งอะไรมากมาย", "ถึงจุดหนึ่งเราต้องรู้จักคำว่า 'พอ'") while protocol posts keep the exact 2026-05 register (คับ density unchanged).
6. **Topic-tag language shifted.** Thai tags (#เป็ดปิดงาน, #พัฒนาตัวเอง, #มนุษย์เงินเดือน) in 2026-01..02; all-English tags from 2026-04 onward, with a stable core #Adduckivity #DuckOS #NeuroDivergent.
7. **New recurring devices in 2026-09:** "Misdiagnosis" as named first move (9router), "single point of failure" → "พวงกุญแจทั้งพวง" extended metaphors (9router, superclick), "ระบบ > X" one-liners ("ระบบ > ค่า token", "ระบบ > rent", "ระบบ > ความพยายาม") as closing formulas, emoji status chips (🔴/🟢/✔️/📝/🐞/📁 in weekly-calibration; ✓/☰/◉ tab icons in task-logger).

## Updates

### 2026-09-13 — seed analysis (21 posts)
- The brand's register is stable (พร + คับ, RAM/server metaphors, XX-0N protocols, 3 Duck OS Laws) across both cohorts, but the **structure migrated**: originals use markdown headings ("00: Ingestion Phase", "N. Bug Report") while all 13 web-archive posts are headingless "."-separated paragraphs — future drafts should match whichever format the post type implies (A = headingless or "N." style; B = headingless with tables).
- **สรุปแบบวิศวกรเป็ด** is the dominant 2026-09 closer (12/13) replacing "บทสรุปจากพร", and hashtag core is now fixed: #Adduckivity #DuckOS #NeuroDivergent + 3–6 topic tags, no Thai tags.
- Tool reviews are now a **local-LLM series** (5 posts in 4 days, 2026-09-04..07) with cross-references ("คราวที่แล้วพรเขียนเรื่อง…", "Part 1/Part 2"), concrete pricing/VRAM/quant numbers, TL;DR, and soft question CTAs — the series format is the main new convention to replicate for type B.
