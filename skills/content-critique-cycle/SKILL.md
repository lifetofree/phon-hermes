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
