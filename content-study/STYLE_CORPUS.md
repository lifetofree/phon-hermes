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

### 2026-09-19 — new posts: 15 (09-12..09-19 window)
Sync note: cron run 09-13 (Sun) went silent — first fetch returned a stale/empty page and the script saw "nothing new"; manual rerun 09-19 caught all 15 (commit 244201e). Archive 13→28 files, index 301.

New cohort = 10 System Diagnostic (rework-*/sam-altman/real-artifact/four-thousand-weeks/interruption-glitch) + 4 tool reviews (grok-bot, lm-studio ×2, orca) + 1 mindset (four-thousand-weeks is diagnostic-style). 9 of 10 are published edits of UDO drafts from the same week.

**Corpus table additions** (wc -w incl. header):

| date | slug | words | type |
|---|---|---|---|
| 2026-09-13 | grok-bot-managed-agent-ops | 1110 | B |
| 2026-09-13 | four-thousand-weeks-time-trap | 721 | A |
| 2026-09-13 | real-artifact-single-source-of-truth | 571 | A |
| 2026-09-15 | sam-altman-writing-compiler-ink-01 | 557 | A |
| 2026-09-16 | rework-reasons-to-quit-quit-50 | 497 | A |
| 2026-09-16 | interruption-glitch-alone-zone-sleep-07 | 442 | A |
| 2026-09-17 | lm-studio-local-llm-gui | 1808 | B |
| 2026-09-17 | lm-studio-bionic-local-agent | 2071 | B |
| 2026-09-17 | rework-meetings-are-toxic | 347 | A |
| 2026-09-17 | orca-ade-parallel-agents-fleet-01 | 1467 | B |
| 2026-09-18 | rework-quick-wins | 509 | A |
| 2026-09-18 | rework-hero-complex-hero-01 | 705 | A |
| 2026-09-18 | rework-estimates-chunking | 1435 | A |
| 2026-09-19 | rework-long-lists-leak | 701 | A |
| 2026-09-19 | rework-tiny-decisions-ice-01 | 669 | A |

**Draft→publish edit pattern (measured on 9 matched pairs):** user edits before publishing, and the edits are systematic — future drafts should pre-apply them:
1. **"พร" → "เรา" in hooks/body** — published versions swap most first-person พร for เรา (chunking kept 26 พร; hero-complex 11; but meetings/quick-wins/reasons-to-quit dropped to 5-9; tool reviews keep พร only in the expert-credence lines). คับ-density drops with it (e.g. ice-01 draft had 8+ คับ; pub has 3).
2. **"วินิจฉัยโรคผิด (Misdiagnosis)" is cut entirely — 0/15 published posts keep it.** The signature move survives only as softened "เราก็พยายามบอกตัวเองว่า…" — do NOT include the Misdiagnosis line in drafts meant for publishing.
3. **Protocol commands survive fully (9/9 posts with XX-0N kept all 3 `--commands`; protocols now total 14 names: REAL-01, INK-01, QUIT-50, SLEEP-07, FLEET-01, SHIP-01, HERO-01, CHUNK-01, LIST-01, ICE-01 + prior MEET-01 cut from meetings pub).** Exception: meetings post lost its whole MEET-01 block (pub = 54% of draft length — user cut the protocol, kept the summary).
4. **Emoji sign-off 🦆⚡ removed in 7/15** (kept in 8: the tool reviews + real-artifact/sam-altman/reasons-to-quit/interruption/quick-wins/hero-complex).
5. **"มุมของ Duck OS" subheading kept in 11/15** (absent in the 4 tool reviews, as expected for type B).
6. **Cross-refs kept but light**: "โพสต์ X (YYYY-MM)" or "(ref: X YYYY-MM + PROTO-NN)" — 5/15 posts carry one; the rest drop them. Series "Part N" language is gone from tool reviews.
7. **Hashtag core unchanged**: #Adduckivity #DuckOS #NeuroDivergent + 4–9 topic tags; #NeuroDivergent missing only in orca (tool review). Closer label is now always "#สรุปแบบวิศวกรเป็ด" with the hash (15/15; previously 7/13 hash form).
8. **Length bands**: Type A pub 347–721 wc-w (nominal medium ~500–650); the 1435-word chunking is the long-form exception. Type B 1110–2071. Pub length = 87–107% of draft (meetings 54% the outlier) — user trims, rarely expands.

**Evolution Notes extension (new conventions):**
9. **Register softening continues**: hooks now open with เรา/คุณ, not พร; "มั้ยคับ" survives (8× across cohort) but sparser. Expert-credence "ในฐานะที่พร…" lines and self-deprecation in tool reviews are the last พร strongholds.
10. **The Rework series (2026-09-15..19, 7 posts) is a new recurring format**: book-chapter anchor (quote + page) → 3 named errors → XX-01 protocol → 3 Laws → cross-ref. Slugs prefix "rework-".
11. **English pull-quote convention**: each post carries one bolded English one-liner before the closer ("The pole is 1,000 miles away — but your next foothold is a few yards."; "System > Meetings. 🦆⚡"). Present in 14/15.
12. **"System > X." closer formula is now standard** (14/15) — always English "System > <topic>." + short Thai tagline.

### 2026-09-20 — llama.cpp social repost (draft→publish pair #10, THIRD format discovered)
Provenance: user pasted the published social version of the 2026-09-09 llama.cpp long-form draft and directed: **"หลังจากนี้ content ต้องการ pattern แบบนี้ ลองวิเคราะห์และบันทึกไว้ด้วย"** — this line-break social format is now a target pattern for future content. Archived as `web-archive/20260920-llama-cpp-wrapper-vs-engine-social.md`, index.json 304. NOT on WP (searched live — no llama.cpp post; this is a social derivative referencing "ในบทความเดิม").

**It is not a trim — pub 1435 vs draft 1382 wc-w (ratio 1.04) — it is a full re-architecture into a third format: the long-form → social line-break repost.**

| metric | draft (long-form) | published (social) |
|---|---|---|
| words | 1382 | 1435 |
| non-empty lines | 94 | 446 |
| avg words/line | 14.7 | 3.2 (416/446 lines ≤60 chars) |
| headings | 9 (`## NN:`) | 33 (`#` sections, `## N.` signals, `### N.` profiles) |
| `-` bullets / `—` dash lines | 26 / 0 | 3 / 72 |
| `.` separator lines | 0 | 46 |
| `>` blockquotes | 0 | 2 |
| คุณ / เรา | 10 / 2 | 62 / 4 |
| genuine พร | ~8 | 1 ("เครื่องของพร" — expert-credence only) |
| ครับ / คับ | 4 / 4 | 0 / 1 (คับ only inside the Law closer) |

**The conversion pattern (11 moves, apply to future social drafts):**
1. **Re-flow to one clause per line** — break every sentence at its natural pause, ≤60 chars/line, blank line between thoughts; a "." on its own line = beat break; ". [blank] ." before a new heading = section break.
2. **Capability tour → decision framework.** The draft's "02: Features 1–6" became "**5 สัญญาณว่า Wrapper เริ่มไม่พอ**" — from "what it can do" to "when do YOU need to come down". The biggest editorial re-architecture of the pair.
3. **Title = proof-point stat, not tool name** ("27B ที่เคยต้องพึ่ง datacenter วันนี้รันในห้องนอนด้วยการ์ด 2 หมื่นบาท — ~8 tok/s"). Hook = invisible-presence reveal ("คุณกำลังใช้ llama.cpp อยู่ แม้ไม่เคยพิมพ์ชื่อมันเลย").
4. **Blockquote pair as framing device** — setup question > "llama.cpp ทำอะไรได้บ้าง?" then payoff > "เมื่อไหร่เราควรเลิกใช้ Wrapper แล้วลงมาเรียก engine เอง?" (curiosity loop in 2 lines).
5. **"—" em-dash bullets everywhere** (72 lines); plain `-` bullets essentially eliminated.
6. **Heading hierarchy maps to listicle depth**: `#` big sections, `## N.` the 5 signals, `### N.` the 4 profiles.
7. **Pronoun/politeness swap complete**: คุณ ×6; พร survives only in the machine-credence line; zero ครับ — one คับ, inside "Law #1 System > Emotion คับ" (draft said ครับ).
8. **Kept verbatim**: comparison table (row labels simplified: ชั้น/จุดเด่น/เหมาะกับ…), the real `llama-server` command block, 7.8 tok/s + 16.5GB + 262k ctx numbers, 4 profiles, Pro Tips 3 ระดับ, Law #1 closer, hashtag tail identical.
9. **Cut entirely**: project lore (Gerganov origin, MacBook story), 127,574 stars, ggml, v0.4.0 release notes, the 7-8B 40-60 tok/s aside, the VRAM คำเตือนพี่เลี้ยง, series Part-4 cross-links, ✅❌ emoji headings (→ prose "ข้อเสียจริง ๆ"), TL;DR.
10. **Added**: benchmark honesty note ("ไม่ควรนำไปเทียบตรง ๆ กับเครื่องอื่นโดยไม่ควบคุมเงื่อนไขเดียวกัน") + "ในบทความเดิม" meta-ref (social post positions itself as derivative of the long-form) + "เปิดฝากระโปรง" hood-opening closing callback on the รถ/เครื่องยนต์ metaphor, which was promoted from an aside into the organizing spine.
11. **Closer override**: the source long-form's `## บทสรุปจากพร` came back as `# #สรุปแบบวิศวกรเป็ด` (hash form) — the hash closer rules even when converting a long-form that used the long-form closer.

### 2026-09-21 — v2 line-per-sentence format: canonical sample "Resume vs Public Terminal" (user-published, NOT on WP)
Provenance: user pasted the PUBLISHED v2 post (Learn In Public / Daily Dispatch × Duck OS, STREAM-01) + its FB micro-variant and directed "published content analyze and update content style and insert into content draft in notion". Verified NOT on wp.adduckivity.com (live WP search — only false-positive title matches). This is the CANONICAL clean form of the v2 pattern (the first paste on 2026-09-21 arrived with the tail scrambled; this clean version orders the tail sensibly). Archived to skill `references/v2-approved-sample-resume-vs-stream.md` + the skill v2 sections were corrected against it.

**Metrics (measured):**

| metric | main post | FB micro-variant |
|---|---|---|
| words | 777 | 68 |
| `#` H1 | 8 | 0 |
| `##` H2 | 8 (5 signals + 3 protocol steps) | 0 |
| `###` H3 | 2 (subtitle + Success Criteria) | 0 |
| `.` beat-break lines | 73 | 0 |
| `—` bullets | 9 | 0 |
| `- ` bullets | 0 | 7 |
| bold spans | 33 | 0 |
| `>` blockquote lines | 2 (true question) | 0 |
| tables | 1 (9 rows) | 0 (collapsed to `-` bullets) |

**v2 canonical structure (8 H1 sections, in order):** title+`###`subtitle → stat-line pair (real contrast: "Resume แก้ล่าสุด: ก.ย. 2024" / "Daily Dispatch ล่าสุด: วันนี้ 14:07") → `>` true question (blockquote, bold, decision-level) → not-pitching block → `# 5 สัญญาณว่า…เริ่มไม่พอ` (`## 1.`–`## 5.` self-check) → `# Resume = Snapshot / Daily Dispatch = Stream` (mental model + `top` metaphor + "Stream ก็แต่งได้" honesty caveat + Learn In Public 2018 anchor) → `# Unconstrained Format` (`—` forms + Friction=0) → `# Social Media as a Public Terminal` (Stream/Terminal/Public Artifact) → `# Resume กับ Daily Dispatch ทำหน้าที่ต่างกัน` (comparison TABLE) → `# โพสต์ที่กำลังอ่านอยู่นี้ คือตัวอย่างสด` (lists the author's own recent protocols ICE-01/SHIP-01/CHUNK-01/DISPATCH-01/LIST-01/HERO-01/String Tax/llama.cpp/LM Studio/Orca as proof) → `# Protocol STREAM-01 — 3 Commands` (`## Step N` + `### Success Criteria` INSIDE) → `# สรุปแบบวิศวกรเป็ด`.

**v2 CLOSER — overrides the 2026-09 System Diagnostic closer (Evolution Notes #11/#12):** the v2 closer has NO "System > X." sign-off, NO 🦆⚡, NO "Law #1" line, NO English pull-quote. Instead: restate the 4 concepts as bold definitions (Snapshot/Stream/Terminal/Public Artifact) → re-ask the true question → name the problem in a bold one-liner ("**Evidence Lag**") → a bold pair ("ฉันเคยทำอะไร" / "ตอนนี้ฉันกำลังทำอะไรอยู่"). `# สรุปแบบวิศวกรเป็ด` is a plain `#` H1 (intentional #). This is a DRIFT from the 14/15 "System > X." + English pull-quote convention — the v2 format is the newer signal (corpus rule: when the corpus contradicts the guide, follow the corpus).

**Success Criteria placement:** lives INSIDE the Protocol section as `### Success Criteria` (after Step 3), not in the closer.

**FB micro-variant (second derivative):** the comparison TABLE → flat `- ` bullet list (7 lines: ชนิด/เวลา/ความถี่/Format/เนื้อหา/หลักฐาน/ผู้อ่าน), 1 title line + 7 bullets, ~68 words. Uses `-` hyphen bullets (NOT `—`). Distinct from the 2026-09-20 llama.cpp social "2 opening paragraphs + CTA" FB form — both FB forms coexist; choose by what the source contains. Filed as a SEPARATE Notion Content Drafts page.

**Register:** คุณ/เรา body; พร appears only in the live-example section ("ถ้าพรเอาทั้งหมดนี้มาจัด Portfolio") — the self-referential proof line; คับ 1 (in "คำถามที่แท้จริงของโพสต์นี้คับ"); no ครับ.

### 2026-09-21 — draft→publish pair #11: show-your-work-reverse (personal-diagnostic v2 transform)
Provenance: user published an edit of the same day's SHIP-90 long-form draft (713 wc-w) and directed "content ที่ published จริง ลอง analyze แล้วปรับใช้ดู". Archived `web-archive/20260921-show-your-work-reverse-published.md`, index 309. NOT on WP (searched live). **Fifth format discovered: the personal-diagnostic transform** — a v2-shaped post rewritten from third-person engineering voice into first-person personal narrative.

| metric | draft (SHIP-90 v2) | published (show-your-work-reverse) |
|---|---|---|
| words | 713 | 564 (0.79×) |
| non-empty lines | 148 | 295 (avg 1.9 words/line vs 4.8) |
| H1 / H2 | 10 / 6 | 9 / 3 |
| `.` beat breaks | 18 | 39 |
| `---` hr separators | 0 | 10 |
| `—` dash bullets | 35 | **0** |
| `>` blockquotes | 2 | 14 |
| bold spans | 16 | 35 |
| protocol names (XX-0N) | 11 (INK-01×7, DISPATCH-01, STREAM-01, SHIP-01, SHIP-90) | **0** |
| พร / คุณ / คับ | 0 / 13 / 3 | 0 / 11 / 2 — BUT first-person narrative is now "พร" as STORYTELLER ("ช่วงหนึ่งพรเข้าใจ…", "พรเลยเปลี่ยนคำถาม", "กฎเดียวที่พรกำลังทดลอง") — the corpus's first post where the narrative self is พร in a SYSTEM post (previous rule: พร only in expert-credence lines) |

**The 12 conversion moves (personal-diagnostic transform):**
1. **Hook reframe — from external claim to internal confession.** Draft title = Sturgeon stat claim ("90% ของงาน…คือขยะ"); pub = "ถ้าการ Show Your Work ทำให้คุณไม่มีแรงทำ Work — คุณกำลังทำมันกลับด้าน". The stat (90%) moves from TITLE to mid-post ("แล้วเรื่อง Perfection ล่ะ?" section). The "กลับด้าน" (inverted) framing survives from the draft's Precedence Inversion but is renamed to a self-check the reader can perform on themselves.
2. **Narrative self = the diagnostic case.** "ช่วงหนึ่งพรเข้าใจคำว่า Show Your Work ผิด" — the author's own wrong model (working → finding time to "make content" → hook/image/caption/checking likes) IS the 3-symptoms evidence. Draft's abstract "คนส่วนใหญ่ไม่กล้า…" became a personal before/after.
3. **Stat-line pair + "คำถามที่แท้จริงของโพสต์นี้คับ" CUT.** Replaced by a single question in a blockquote: "วันนี้คุณกำลังทำงานจริงหรือกำลังทำงานเพื่อให้มีอะไรไปโพสต์?" (one question, not the decision-level pair).
4. **Not-pitching block CUT.**
5. **3 signals → 3 symptoms of INVERSION.** Draft's self-check signals (drafts pile up / "no time" / content days kill main work) → pub's "จุดที่ระบบเริ่มกลับด้าน" (post-time > work-time / "อันนี้โพสต์ยังไง" mid-work / content-heavy day = no new evidence). Signal 2 is NEW — attention-splitting mid-work, the subtlest failure mode. Each symptom ends with a bold named state: **Work for Showing**, "Exhaust เริ่มพยายามบังคับ Engine", "Activity แต่ไม่มี Evidence ใหม่".
6. **Pipeline added — the post's actual thesis:** `Doing → Evidence → Compile → Show` (vs "คิดว่าจะ Show อะไร → หาอะไรไปทำ"). Draft had Core Engine/Exhaust metaphor but no named pipeline; pub makes the pipeline the spine and reuses it in the closer.
7. **New concept split: Raw Evidence vs Compiled Asset** (Screenshot/Note/Error/number → 3 lines/image/case study/checklist) — "Showing ไม่จำเป็นต้องสร้าง Content ใหม่ — มันอาจเป็นแค่ Compile สิ่งที่มีอยู่แล้ว — ความต่างเล็กมาก แต่ต้นทุนคนละเรื่อง".
8. **Protocol CUT — replaced with Tiny Experiment + single rule.** SHIP-90's 3 `--commands` + Success Criteria gone. Pub: "พรยังไม่รู้ว่าระบบนี้ควรเป็นยังไง — ดังนั้นยังไม่อยากสร้าง Protocol ใหญ่ — ลองแค่ 7 วัน" — time-budget compile test with the debug question "ทำไมการ Show สิ่งที่เกิดขึ้นแล้วถึงต้องใช้แรงขนาดนี้?" — and ONE quoted rule: "Core Engine ต้องสร้าง Evidence ก่อน Showing ถึงจะเริ่มต้นได้". Explicit anti-protocol: "ไม่ใช่ 'ต้องโพสต์ทุกวัน' / ไม่ใช่ 'ต้องปล่อย 5 ชิ้นต่อสัปดาห์' / ไม่ใช่ 'ต้องใช้เวลา 11 นาที'" (the 11-minute INK-01 anchor is named ONLY to be excluded).
9. **Cross-refs CUT entirely** (INK-01 / DISPATCH-01 / STREAM-01 / SHIP-01 / โพสต์ตัวอย่างสด section all gone) — the personal post carries zero protocol cross-links.
10. **Sturgeon demoted to one section + reinterpreted.** The 1945/"More Than a Hundred" attribution CUT — "Theodore Sturgeon มีประโยคที่ถูกอ้างถึงบ่อยว่า" (weaker, safer phrasing). New honest read: 90% ≠ "ปล่อยงานห่วยๆ ไปเถอะ" but "อย่าคาดหวังว่า Output ทุกชิ้นต้องกลายเป็น Asset ที่ดี" + self-deprecating "กูโพสต์อะไรไปวะ 55555" (FIRST กู/55555 in the corpus — register break for personal-diagnostic posts only). Killer line: **Perfection กำลังเก็บภาษีจาก Work**.
11. **Layout: `---` hr sections + 1-word-per-line flow + `>` for every direct question (14×)** — dash bullets eliminated (35→0), beats doubled. Blockquote now carries all quoted questions and the single rule.
12. **Closer = v2 closer, but pipeline restated instead of concept defs:** Doing/Evidence/Compile/Showing as bold definitions (replacing Snapshot/Stream/Terminal/Public Artifact) → pipeline re-ask ("ถ้าวันไหนกลายเป็น Show → หาเรื่องมาทำ → สร้าง Evidence ให้เข้ากับโพสต์ = ระบบกลับด้านแล้ว") → metaphor callback (รถไม่ได้วิ่งด้วยไอเสีย — kept verbatim from draft) → final night question "วันนี้ Core Engine ของคุณทิ้ง Evidence อะไรไว้?" + "ถ้าตอบได้ ค่อย Compile มัน" — NO Law #1 line, NO EN pull-quote, NO CTA number (draft's "คอมเมนต์ตอบเป็นตัวเลขตัวเดียว" CUT).

**Rule-of-thumb for future drafts (draft→publish pair #11):** when the user publishes a personal-diagnostic version of a system post, the draft should have ALREADY been written as a personal before/after with (a) one named pipeline as spine, (b) 3 symptoms each ending in a bold named state, (c) a Tiny Experiment section INSTEAD of the protocol (7-day, time-budget, debug-question), (d) the single quoted rule, (e) zero cross-refs/protocol names, (f) closer = pipeline restatement + night question. The engineering protocol draft remains the SOURCE asset; the personal post is its narrative derivative — both keep the same hashtags.

**Evolution Notes extension:**
13. **Personal-diagnostic is the 5th format** (after: System Diagnostic 3-error / N-signals level-up / tool review B / v2 line-per-sentence / social line-break repost). It shares v2's layout (H1 sections, `.` beats, bold) but swaps the engineering voice for first-person confession, cuts all protocol machinery, and ends on a night question instead of a Law line.
14. **Register break (personal-diagnostic only):** กู/55555 self-deprecation appears for the first time in the corpus; narrative self = พร in system posts (previously expert-credence lines only).
15. **Anti-protocol is now a content position:** "พรยังไม่รู้ — ยังไม่สร้าง Protocol ใหญ่ — ลอง Tiny Experiment 7 วัน" is itself the Duck OS position (PACT Tiny Experiment) — future system posts may deliberately ship a rule + experiment INSTEAD of a 3-command protocol when the system is unproven.
### 2026-09-21 — pair #12: share-imperfect-gate (user's OWN personal-diagnostic rewrite of SHIP-GATE-01, to-be-posted)
Provenance: user pasted their OWN rewrite of the same day's SHIP-GATE-01 engineering draft (`posts/20260921-cnt-internet-copy-machine-ship-gate.md`, 931 wc-w) after running it past a "Bent DNA" 10-point critique; said "ต้นฉบับที่จะ post ลองเอาไป analyze" (NOT yet published). Archived verbatim `web-archive/20260921-share-imperfect-gate-user-rewrite.md`.

| metric | SHIP-GATE-01 draft (UDO) | user rewrite |
|---|---|---|
| words | 931 | 539 (0.58×) |
| non-empty lines | 159 | 262 (~1 thought/line) |
| H1 / H2 | 7 / 8 | 9 / 0 |
| `.` beats | 16 | 42 (doubled `.` as section breaks) |
| `—` bullets | 24 | **0** |
| `>` blockquotes | 6 | **20** (every question + every raw/compiled note) |
| curly quotes “ ” | 0 | **11** (NEW register element) |
| tables | 2 | 0 |
| protocol names (XX-0N) | 4 (SHIP-90/STREAM-01/QUIT-50/SHIP-GATE-01) | **0** |
| cross-refs | 3 | 0 |
| พร / คุณ / เรา | 3 / 29 / 1 | **12 / 3 / 25** (narrator shift) |
| คับ | 2 | 0 |

**It implements ALL 10 of the Bent DNA critique points**: reduce 4→2 gates / cut the "Generosity vs Ego" motive question → observable "คนรับได้อะไรโดยไม่ต้องถอด Raw Data" / merge Noise + So-What into one Value gate / soften Copy-Machine absolutes (drop "ไม่จำกัด/ลบไม่ได้", drop "AI ที่เอาไป train") / cut "2 นาที / default ไม่กด / 0 อยากลบ" certainty claims / no new protocol name / demote "Overthinking" from a 4th filter to a gate-CONSTRAINT / promote "Editor open / Exit gated" as the mental model / "Share imperfect ≠ Share everything" as the title hook / worked Raw→Compiled example as the centerpiece.

**Evolution vs pair #11 (rule-of-thumb gets sharper):** the user now executes the transform THEMSELVES (UDO no longer needs to pre-apply it in the engineering draft). The spine is a **2-GATE flow** (PRIVATE→BOUNDARY→VALUE→PUBLIC, ↓ arrows), not a 3-symptom list or 4-stage pipeline. The 2 gates map 1:1 to two Laws **without naming them** (Boundary=Law #3 Protect the System, Value=Law #2 Asset>Activity) while "gate must stay light / don't overthink" = Law #1 as the meta-constraint. A concrete worked example (Raw onboarding note → Compiled pattern) replaces abstract symptoms.

**Series signal (do NOT name it yet — user said "ยังไม่ตั้งชื่อ Series"):** Post 1 = Doing→Evidence→Compile→Show (the burn loop, SHIP-90) / Post 2 = Share imperfect ≠ Share everything (this gate). Spine quote: "พื้นที่ Private มีไว้ให้คุณคิดโดยไม่ต้องระวัง / Gate มีไว้ให้คุณ Publish โดยไม่ต้องเอาทุกอย่างออกไปด้วย".

**Nits flagged pre-post:** (1) hashtags `#SoWhatTest` + `#ShipGate` are leftovers from the engineering draft (post has 2 gates, no So-What test, no protocol) → update to reflect Boundary/Value; (2) closer typed `# #สรุปแบบวิศวกรเป็ด` (double #/leading space) vs corpus `#สรุปแบบวิศวกรเป็ด`; (3) "คนสอง" → "คนที่สอง"; (4) the worked example asserts "ติดคนละจุด แต่มี Pattern เดียวกัน" without SHOWING the pattern — tighten so the raw→compiled lesson is airtight.

**Evolution Notes extension:**
16. **Personal-diagnostic is now user-executable (pair #12).** Stop pre-building 4-filter "OS" scaffolding over a single insight. Ship the 2-gate spine: a concrete worked Raw→Compiled example, "Editor open / Exit gated" as the load-bearing model, curly quotes (“”) alongside `>`, the 3 Laws embedded unnamed (Boundary=Law #3, Value=Law #2, lightness=Law #1), and NO certainty claims (the gate doesn't guarantee no regret — only "ตอนปล่อย ฉันรู้ว่ากำลังปล่อยอะไร").
