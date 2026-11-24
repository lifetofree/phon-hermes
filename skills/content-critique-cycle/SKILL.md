---
name: content-critique-cycle
version: 1.0.0
author: KhaoKlong (Hermes)
license: internal
metadata:
  hermes:
    tags: [adduckivity, content, critique, benz-dna, notion]
    related_skills: [content-pipeline, content-pipeline-sessions]
description: "Use when a Benz-DNA critique lands on an adduckivity draft."
---

# Content Critique Cycle (Benz-DNA track)

## When to Use

Load this when a Benz-DNA comment (real, pasted from the owner) or a simulated Benz critique is being implemented on an adduckivity draft — intake, gate, publish-keys, pair closure, and the fold-learning step. Do NOT load for pure drafting (that is `content-pipeline`).

Overview: use when a real or simulated Benz-DNA critique arrives on an adduckivity draft — implementing it is a DIFFERENT job from writing the draft. This skill owns that job end-to-end: intake → verify → implement → gate → publish-keys → close. Writing/rewriting rules live in `content-pipeline`; that SKILL.md keeps only a pointer here plus its critic-side patterns (r2-cycle, r3-shape, §12 rule).

## Round type selector (read first — fold 359 two-round contract)

- **Critique + no publish version** → agent may rewrite (gate by paste, owner answers, spec → rewrite) — EXCEPT owner-authors track: owner announces it.
- **Critique + "publish version" pasted from the critic** → NO agent rewrite: archive → baselines → publish-keys only. The skill-learning step STILL runs.
- **Critique + owner gate answer + owner publish arriving in ONE message** (the fastest full round; recurring on the news-event lane) → the publish's own framing answers the gate — do not re-ask via clarify and do not rewrite. Round = archive both paste files byte-true → quote-verify the critique against the current draft → measure the publish in code (no HTML header) → grade against the critique's keys (the critic's recommended replacement lines are the keys, verbatim-or-function) → rebuild the same Notion page to Status `published` → fold the loop (content-pattern lessons to content-pipeline folds; this round-shape stays described HERE). Un-chosen gate axis = 0 in the publish; a minority-axis phrase surviving as a subordinate clause is a NOTE, not a FAIL.
- **Owner answers a gate in one message** ("เลือก a แล้ว rewrite เลย") → agent-rewrite round; grade the eventual publish against the LAST REAL critique's keys, never the agent's own vocabulary. Grade each key BY DEFINITION (what it permits/forbids in the publish), never by a proxy count — mention counts drift when the critic splits or merges sentences, and a key failed on a miscounted proxy is a wrong entry in a permanent ledger; recheck every apparent FAIL against the key's own wording before recording it.
- **Critique carries NEW SYSTEM FACTS — reposition round (pair #123 round, 2026-11-19, folds 439-442 in content-pipeline):** the paste is an ANALYSIS (change log + corrected mental model + repositioned thesis), not a line-edit list — run: extract → challenge (only misunderstanding-breaking questions) → reconstruct (current state / actual workflow / capability / limitation / future state, each sourced) → reposition the thesis → OWNER APPROVES the direction → rewrite LAST. Deliverable order: Original Thesis / Misunderstandings / New Information / Change Log / Revised Thesis / Recommended Structure / Rewrite (on approval) / Fact Audit. Machine-verify every new fact against the source system before it enters the ledger (roster counts carry an as-of date — they move within a day); garbled proper names (STT class) correct against the roster; never rewrite while a detected misunderstanding is unresolved; if the reposition retitles, the old title is DEAD vocabulary for the rewrite's checks. A wholesale proposed replacement skill ("OPB Article RE & Editorial Intelligence" shape) is NOT adopted over the existing two-skill split — extract its non-duplicative stages into folds instead (owner directive 2026-11-19).
- **Critique arrives as a RETROSPECTIVE ROUND SUMMARY — Benz DNA v2 shape (pair #125, 2026-11-21):** the paste is a multi-round document (r1 findings + owner's new data + owner's revision list + r2 re-audit + audience-feedback analysis + the critic's own generalized lessons section) about an already-POSTED article — no rewrite track. Run: archive the summary (PROVISIONAL class if owner-pasted inline; replace with byte-true pastes if they surface later) → grade the posted version against the critique's OWN lessons section → report residual defects to the owner (what the lessons demand that the posted text still violates — e.g. #125 shipped with 253−211≠41 unresolved, no Notion-doc link, the 7-rows cause-mix) → fold: post-pattern rules → content-pipeline folds (449-460), the critic's METHOD → the "v2 retrospective-round pattern" paragraph there. Signature of the v2 method worth reproducing in any future sim: the open-findings ledger (r2 re-audits r1's items and names which persist) — implement critique rounds the same way, never re-derive findings from scratch.
- **Critique lands on a draft the owner has ALREADY published, with a learn-only directive ("ไม่ต้องแก้ใน draft — เอา comment ไป reverse engineering/analyze/learning", left-digit round 2026-11-21):** archive critique + publish (PROVISIONAL-inline class ถ้า paste จากแชต) → quote-verify against the version the critic ACTUALLY read (หน้า Notion drift ทำให้ต่างจาก vault md — verify กับเวอร์ชัน Notion) → grade the publish against the critique's named fixes → report residuals → fold lessons (content-pattern → content-pipeline folds; round shape → round-type ที่นี่). NO rewrite, NO Notion rebuild/retitle/Status-flip — publish กับหน้า draft diverge กันโดยเจตนา owner ให้บันทึก ไม่ใช่ให้ซ่อม; grading against publish-keys เป็น optional เมื่อ directive ระบุ deliverable = learning
- **Critique arrives as a RULE-LEDGER — ก่อนแก้/หลังแก้/เพราะ/กฎ รายข้อ + "กฎรวม สำหรับ train AI" + ส่วน emotion — on a draft that is already published/fixed, learn-only directive (9router-fallback round 2026-11-23):** critic ถอดกฎมาให้เองครบ — รัน learning step แบบ VALIDATION ไม่ใช่ derivation: quote-verify บรรทัด "ก่อน" และระบุเวอร์ชันที่ critic อ่าน (อาจเป็น owner-updated draft ที่ไม่เคยเข้าระบบเรา — หน้า Notion อาจยังถือ v1 เก่า ให้ archive v1 snapshot ด้วย), ตรวจทุก fact ที่ critic ใช้ตัด/คง กับแหล่งจริงด้วยตัวเองแล้วจดผลใน archive header แม้ขัดกับคอมเมนต์ (publish ของ owner ยืนตามเดิม ไม่แตะ), dedupe กฎที่ถอดมากับ folds เดิมทีละข้อ (wire เป็น extends), เกรด publish กับกฎ BY DEFINITION ในโค้ด, แล้ว fold — กฎเนื้อหา → content-pipeline folds, รูปแบบรอบ → bullet นี้ บล็อก "กฎรวม" ใช้ต่อเป็น portable voice spec ได้ — คัดลอกลง fleet voice guide (`duck-os/Rakazo_Drafting_Voice_Guide.md`)
- **Owner sovereignty over gates:** when the owner's gate answer contradicts the critic's recommendation, the spec follows the OWNER's answer verbatim (pair #103 r3: owner picked ข้อแรก, Benz แนะข้อสอง → Benz served the owner's answer and supplied closer lines).

## Intake (always in this order)

1. **Archive the critique verbatim** before touching the draft: `content-study/web-archive/<date>-<slug>-benz-r<N>-gate-spec.md` with a header: which version the critic read, the gate question(s), owner answer, post-gate spec summary. Paste paths (`~/.hermes/pastes/paste_*_*.txt`) are ephemeral — the archive is the durable copy.
2. **Quote-verify** every quoted fragment against the current draft — critic quoting stale text ≠ stale critique: if the quotes are load-bearing and still true, the critique stands (rule 43). If the critic read version N, note it; never silently implement against version N-1.
3. **Snapshot the current draft** (`…-v<N>.md` in web-archive) before any rewrite. Post files resolve through a symlink: the real file lives at `content-study/vault/posts/<slug>.md` (`content-study/posts/` only points at it) — read and write the resolved path; addressing the symlink path trips the stale-write guard on overwrite. FP declarations are never "fixed" (lesson 22) — verify the FP list first.

## Implementing a critique

- The critique's SKELETON (its final section) is the new spine — do not retrofit the old draft.
- Critic's verbatim lines (definitions, spine sentence, closer) go in as-is; every CUT named is a zero-count check (verify in file AND Notion read-back).
- Keep-list lines the critic praises are protected anchors: rewrite around them, never paraphrase them away.
- A precision round (critic marks spine clear, residue = word choice) touches ONLY those sentences — length growth is a violation.
- Runs the draft battery with the post's CUT list + FP declarations before anything ships (scripts live in `content-pipeline/scripts/`).

## Gates

- One question, few options, written so only the true option has a story behind it ("อย่าเลือกข้อที่ฟังดูดีที่สุด เลือกข้อที่เกิดขึ้นจริง").
- Calibrate against what the post can prove: evidence class (first-look vs REAL-USAGE 125 วัน) decides verb strength and closer scope.
- Calibration rounds (spine already survived): repairs are parse/precision/scoping only; expect the critic to upgrade implicit structure into named levels and role-label the keep-list — adopt those names.

## Closing the pair (publish-keys ledger)

- Baselines: wc-w, pronoun counts, H1/H2/H3, beat dots, blockquotes, quote counts.
- Publish-keys: keep-list verbatim, dead vocab of un-chosen axes = 0, CUT = 0, layer/evidence-label claims audited by structure (count carriers, not words).
- Critic-authored publishes may carry CUT-list words inside their own guard sentences — grade those as critic-override (the same override right an owner has), not as violations.
- Rebuild the Notion page (patch or delete+insert; ≤100 blocks/request — split batches), read-back verify (blocks, empty 0, raw `**` 0, CUT 0, keep-lines PASS — extend the forbidden list with the un-chosen-axis names when grading), retitle if the publish retitles, then flip Status → `published` with a properties PATCH and confirm from the properties read-back (a body verify does not touch Status).
- Update: index.json entry (title/status/form/words/note with the full loop), `references/pair-history.md` entry, STYLE_CORPUS.md publish entry, STATE.md.
- Regenerate the vault (`python3 skills/content-pipeline/scripts/generate_vault.py` — merge-safe, prunes stale pair files) before the closing commit.
- Commit + push (all file work lives in `~/hermes-agent/`).

## Learning step (standing owner rule §12, 2026-11-06)

EVERY real Benz-DNA comment → reverse-engineer ความคิด/วิธีคิด/การวางแผน/การวางแกน of the critic into the skill system IN THE SAME ROUND as implementing it — no separate request needed. Owner announces extra context per message and names which skill each piece belongs to.

- **Content-pattern lessons** (rules about the POST) → folds in the repo copy `/home/lifetofree/hermes-agent/skills/content-pipeline/SKILL.md` (Evolution Notes / File maintenance — the pair ledger itself lives in its `references/pair-history.md`), numbered continuing from the highest existing number. Provenance = pair #.
- **Critic-side patterns** (how the critique itself works — compliment→forcing-question→spec→preserve→verdict; calibration round shape; evidence-audit arc pair #105 r1sim→r5: process gate → retract-on-evidence → show-the-artifact → per-item source audit → criteria-ownership line → spine-convergence gate) → Benz-DNA section pointer here + the pattern paragraph in content-pipeline.
- Fold naming convention: `**(N) name — rule (pair #X round):** evidence → fix → gate`. Extends/supersedes links to earlier folds explicitly.

## Critic-grammar folds from real Benz (Wispr Flow 37-day draft, 2026-11-22, pair #Wispr37-r1real)

Real Benz's r1 on the Wispr Flow 37-day draft — his method adds five grammar moves the fleet's sim critics missed (Benz Critic r1 AND Hermes r1 both missed #1; both cited the same doc line Benz used to catch it):

1. **(W1) "ยังไม่ได้เปิดดู" ≠ "ข้อจำกัดของข้อมูล":** Benz hit the claim "ยังบอกไม่ได้ว่า อื่นๆ 63% คืออะไร" with the docs' own hover spec (hover shows exact word counts + top app) → "ที่ว่าบอกไม่ได้ = ยังไม่ได้ลอง ไม่ใช่ข้อจำกัดของข้อมูล". Rule: before writing "บอกไม่ได้ / ยังไม่รู้", verify the TOOL offers no way to know in ~10 minutes (hover/export/settings) — otherwise it's an unperformed action, and Benz orders the 10-minute check as the fix with everything else rewritten after it (fix-order by information gain).
2. **(W2) headline scope leak = self-admitted residue:** the draft ADMITTED "0% ไม่ได้แปลว่าไม่เคยใช้" in the body while the headline still implied it ("0% ใน 37 วันติดกัน" = streak number + scoped share glued together). Benz: the admission must propagate to headline + quote + closer, or the grade drops for "รู้แล้วไม่แก้" — heavier than not knowing. Fix shape: rewrite the headline as a plain sentence ("ซื้อมาพิมพ์อีเมลกับข้อความงาน แต่แผงสถิติเขียนว่าสองหมวดนั้น 0%") instead of stat-gluing.
3. **(W3) over-numbering:** numbers that don't drive the argument (53,417 / 2,005 / 247 / 1,758 / 45) are noise — keep only numbers that PROVE the point (e.g. 120 wpm as "ค่าล่าสุด ไม่ใช่ค่าเฉลี่ย"). Rule: every number must do argument work.
4. **(W4) binary framing check + third path:** "ซื้อผิดตัว หรือใช้ตามประโยชน์จริง" closes too early — Benz adds the third path (the tool's own categorization is inaccurate). Rule: before presenting a two-way fork, hunt the third option (measurement error / tool misclassification / in-between).
5. **(W5) closer structure drift:** the #สรุปแบบวิศวกรเป็ด closer + pull-quote lost the house shape (สาระ / เงื่อนไข / มุมสังเกต) — Benz compares against PREVIOUS published sets, not just intra-article. Rule: closer shape is a cross-article invariant; drift = finding.
6. **(W6) producer claim = link required:** "คำสั่ง AI ที่มีรายละเอียดกว่า" reported without a link → must carry the source URL (reported speech alone is not enough when the claim is a marketing assertion).
7. **(W7) text-only critique limits:** Benz states he sees NO image — image-backed claims must reach the critic as exact numbers in text (or attached image). Writers citing screenshots: transcribe every load-bearing figure.
8. **(W8) percentile base exists somewhere:** "Top 0.8% — เอกสารไม่บอกว่าเทียบกับใคร" was WRONG per Benz (docs tie the percentile to WPM vs Flow users). Rule: "the doc doesn't say X" requires having read the WHOLE doc (both critics cited the same line and missed the other line). Verify-by-absence needs a full-page read.

### Benz r2-real folds (same draft, 2026-11-22 — his second pass caught the rewrite)

- **(X1) hover/query results = interpretation, never fact:** the rewritten line "อื่น ๆ = การใช้งานทั่วไปที่แอประบุประเภทแอปไม่ได้" was MY hover interpretation written as a fact — Benz: the docs page NAMES the category but does NOT define it. Fix shape: "เอกสารตั้งชื่อหมวดนี้ไว้แต่ไม่ได้นิยามความหมายของมัน" + link. Rule: a query result (hover/CLI output) answers "how much", not "what it means" — the meaning question is only answerable by the docs, and if the docs are silent, say they are silent.
- **(X2) one denominator per article:** 63%-of-desktop in one line and "กว่าครึ่งของคำทั้งหมด" in the closer = two bases that contradict (26,858/53,417 = 50.3%). Rule: pick the base once (here: desktop, because the category panel is desktop-only) and hold it everywhere including quote and closer.
- **(X3) closer may not conclude what the body declares undecidable:** "ถูกใช้ไปคิดและคุย" in the closer contradicted "สามทางนี้ยังตัดสินไม่ได้" — and the closer carried a number (120 wpm) that no longer existed in the body. Rule: whatever the body says "ยังตัดสินไม่ได้", the closer must keep it undecided; closer numbers must still exist in the body.
- **(X4) "รีวิวไม่พูดถึง" needs corpus evidence:** user reviews DID report the same panel (AI ~62% of words, ~89% desktop in another) — Benz: either write "รีวิวที่อ่านเน้นอะไร" or cut. Rule: claims about what reviews say require having surveyed the reviews.
- **(X5) weighting phrasing:** state the mechanism once, coherently ("นับจำนวนครั้ง ถ่วงอีเมลครึ่งหนึ่ง เอกสารหนึ่งในห้า แล้วปัดเศษ" + link) — never "วัดสัดส่วนคำ ไม่ใช่ครั้ง" followed by "นับครั้งละครึ่ง" in the same sentence.
- **(X6) critic self-correction is public:** Benz's own prior request (top app per category) turned out impossible per the docs ("app-level data exists only in the daily heatmap labels") — he said so plainly ("ผมต้องแก้ของผมด้วย") and redirected to the daily heatmap (5 heaviest word-days + each day's #1 app = the only app-name path). Rule: when a requested action is impossible by the docs, the critic states it and supplies the possible alternative in the same message.

### Benz r1-real folds — Nvidia/Jensen return draft (pair #Nvidia-return, 2026-11-24; news-event lane, multi-outlet self-survey)

Benz critiqued the Rakazo-side AW draft on the Huang resignation→reinstatement news (Nov 12-23, 2026) AFTER reading the news himself across outlets — method additions:

1. **(NR1) Read-coverage transparency per source:** he opened the critique by stating his read depth per outlet ("เปิดอ่านเต็มได้แค่หน้าเดียว (IBTimes) ส่วนอีกหลายสำนักอ่านได้เฉพาะส่วนต้น") — grading weight is calibrated to what the critic actually read, declared up front.
2. **(NR2) Alternative-cause enumeration (marked as his own extension):** the market move mixes three causes (คนกลับ / ความเสี่ยงที่รัฐปลดไป / ความชัดเจนจบความไม่แน่นอน) each with a DIFFERENT lesson — Benz orders "ตอบว่า" → "ชี้ว่าอาจ" หรือเขียนสามกรณีสั้น ๆ. Note: he explicitly marks this decomposition as AI-ต่อยอด (his own extension, not Benz-core) in the provenance line.
3. **(NR3) Percent-recovery arithmetic + added ≠ recovered:** ลง 25% แล้วขึ้น 30% = 97.5% ของเดิม, ไม่ใช่ "กลับมาทั้งลูก"; "$952B added" → "เกือบหนึ่งล้านล้าน" AND มูลค่าที่เพิ่ม ≠ มูลค่าที่กลับมา (เพราะไม่รู้เสียไปเท่าไร). Rule: run the compounding math on every recovery/decline pair; never equate "added back" with "recovered".
4. **(NR4) Attribution counting → two structural paths:** "ตามรายงาน" 7 ครั้ง (บรรทัด 7×2, 13, 15, 19×2, 28) ไม่มีชื่อผู้รายงาน = ผู้อ่านตรวจไม่ได้. Two fixes offered, writer picks: (a) เล่าข่าว → ใส่ชื่อ Nvidia/Jensen + ลิงก์ท้ายบท + วันที่เช็ค + "ตามรายงาน" ครั้งเดียว (b) เล่าหลักการ → ตัดรายละเอียดข่าวลงมาก.
5. **(NR5) Per-sentence provenance audit:** each factual sentence traced to what the sources say/don't — จับได้ 5 ประโยค (ใครชวนคุย / "กรรมการยังปฏิเสธ" → ประธานพูดสาธารณะ 6 วันก่อน / "รับช่วงกลางน้ำ" ไม่เจอ / "แรงขายลามทั้งตลาด AI" แหล่งไม่เชื่อม / "สอบสวนถึงสุดทาง" เกินขอบเขต) + date claim fixed by calendar ("ลาออกต้นเดือน" → 12/13 พ.ย. = กลางเดือน). Rule: no sentence survives without a source that actually says it; date words check against the calendar.
6. **(NR6) Official-language substitution for sensitive matters:** "เรื่องส่วนตัว" → ถ้อยคำตามแถลงบอร์ด "ข้อกังวลด้านความมั่นคงของชาติ" — never write unverified personal-allegation details (not needed for the point + it's an allegation per reports), and the official phrase strengthens the main claim.
7. **(NR7) Priority + open question back to the writer:** "ถ้ามีเวลาน้อย แก้ข้อ 1 กับข้อ 3 ก่อน" (time-constrained fix ordering) AND the critique ENDS with a question that opens a verification loop back to the writer ("ตัวเลขหนึ่งในสี่ มาจากแหล่งไหน?") — forcing the writer to trace their own number's provenance.
8. **(NR8) Keep-list and confirmed-facts named explicitly:** สิ่งที่ควรเก็บ = hook "ไม่ใช่ผลประกอบการ…" + "การกลับมา ไม่ใช่การปิดไฟล์" (ตรงข้อเท็จจริง); plus a CONFIRMED section ("ยืนยันได้ ไม่ต้องแก้": คณะกรรมการความมั่นคง + chief compliance officer) — positive confirmations prevent wasted fix rounds. Ends with provenance line: ความรู้เบ๊น (OPB Replaceability) vs AI-ต่อยอด marked separately.

Round-selector bullet: **news-event critique with multi-outlet self-survey** — the critic reads the actual coverage across outlets, declares read-depth per source (NR1), grades the draft's sentences against what the sources actually say (NR5), adds his own cause-decomposition marked as extension (NR2), sets fix priorities (NR7), and hands an open provenance question back to the writer. Hermes-side: archive the critique + run the provenance question to ground (web search) BEFORE answering the writer.

### Benz r2-real folds — same draft after AW fix (pair #Nvidia-return r2, 2026-11-24)

Benz's r2 opened with a DIFF-VS-PREVIOUS verification ("ผมเทียบกับฉบับก่อนแล้ว แก้ไป 3 จุด ที่เหลือยังเหมือนเดิม") — three additions to the method:

9. **(NR9) Diff-verify before critiquing + restate the unresolved list:** compare against the previous version FIRST — credit what was actually fixed (3 จุด, verified with the sources: หนึ่งในสาม per Reuters 33%, เห็นตรงกันทั้งบอร์ด, Trump detail added) — then RESTATE every unresolved item from the previous round item-by-item (ข้อ 1/3/5/6 + เลขล้านล้าน + ต้นเดือน + ทั้งลูก) so nothing silently survives between rounds.
10. **(NR10) Recovery-fraction consistency trap + decline date-range:** "ลง 1 ใน 4 ขึ้น 1 ใน 3" บวกกันครบ 100% พอดี (0.75×1.333) — that claim holds ONLY if "หนึ่งในสี่" has a source. AND: one source reports the stock hit a 7-MONTH low on Monday during the board investigation, BEFORE the Nov 12 resignation → part of the drop preceded the resignation → the decline claim must specify date range (จากวันไหนถึงวันไหน).
11. **(NR11) Direct-with-person vs conflated-with-board:** "Trump คุยกับบอร์ดทั้งทางตรงและทางอ้อม" — Benz couldn't verify. What sources DO say: Trump called Huang directly urging him to fight for the position (NYT) + told reporters "ไม่ขัดข้อง" if Huang returns; the board received input from UNNAMED senior government officials, initiator unknown. Rule: don't conflate talking-to-the-person with talking-to-the-board; replace with the verifiable facts or cut (unless the writer supplies a direct source).
12. **(NR12) Use the source's term:** sources say "unanimous" → เอกฉันท์; "เห็นตรงกันทั้งบอร์ด" = same meaning but longer — revert to the source's term.
13. **(NR13) In-article time-reference consistency:** "วันจันทร์ที่ผ่านมา" at the top vs "วันนี้" mid-article when the event was yesterday → absolute date "23 พ.ย." everywhere.
14. **(NR14) Em-dash is an AI-text tell:** — inside the pull quote → period or line break (readers use it to flag AI writing).
15. **(NR15) Rounding must not exceed the source:** "ราวหนึ่งล้านล้าน" for CNN's 9.52 แสนล้าน = rounding UP beyond what the source states → use the exact figure.
