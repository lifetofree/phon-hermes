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
- **Owner answers a gate in one message** ("เลือก a แล้ว rewrite เลย") → agent-rewrite round; grade the eventual publish against the LAST REAL critique's keys, never the agent's own vocabulary.
- **Owner sovereignty over gates:** when the owner's gate answer contradicts the critic's recommendation, the spec follows the OWNER's answer verbatim (pair #103 r3: owner picked ข้อแรก, Benz แนะข้อสอง → Benz served the owner's answer and supplied closer lines).

## Intake (always in this order)

1. **Archive the critique verbatim** before touching the draft: `content-study/web-archive/<date>-<slug>-benz-r<N>-gate-spec.md` with a header: which version the critic read, the gate question(s), owner answer, post-gate spec summary. Paste paths (`~/.hermes/pastes/paste_*_*.txt`) are ephemeral — the archive is the durable copy.
2. **Quote-verify** every quoted fragment against the current draft — critic quoting stale text ≠ stale critique: if the quotes are load-bearing and still true, the critique stands (rule 43). If the critic read version N, note it; never silently implement against version N-1.
3. **Snapshot the current draft** (`…-v<N>.md` in web-archive) before any rewrite. FP declarations are never "fixed" (lesson 22) — verify the FP list first.

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
- Rebuild the Notion page (patch or delete+insert; ≤100 blocks/request — split batches), read-back verify (blocks, empty 0, raw `**` 0, CUT 0, keep-lines PASS), retitle if the publish retitles.
- Update: index.json entry (title/status/form/words/note with the full loop), `references/pair-history.md` entry, STYLE_CORPUS.md publish entry, STATE.md.
- Commit + push (all file work lives in `~/hermes-agent/`).

## Learning step (standing owner rule §12, 2026-11-06)

EVERY real Benz-DNA comment → reverse-engineer ความคิด/วิธีคิด/การวางแผน/การวางแกน of the critic into the skill system IN THE SAME ROUND as implementing it — no separate request needed. Owner announces extra context per message and names which skill each piece belongs to.

- **Content-pattern lessons** (rules about the POST) → folds in the repo copy `/home/lifetofree/hermes-agent/skills/content-pipeline/SKILL.md` (Evolution Notes / File maintenance — the pair ledger itself lives in its `references/pair-history.md`), numbered continuing from the highest existing number. Provenance = pair #.
- **Critic-side patterns** (how the critique itself works — compliment→forcing-question→spec→preserve→verdict; calibration round shape) → Benz-DNA section pointer here + the pattern paragraph in content-pipeline.
- Fold naming convention: `**(N) name — rule (pair #X round):** evidence → fix → gate`. Extends/supersedes links to earlier folds explicitly.
