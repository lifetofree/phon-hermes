# Rakazo TECH lane — round notes (pairs #122/#123/#124, 2026-11-19/20)

Staged during a review turn: skill_manage cannot reach the symlinked repo skills (creative/content-pipeline, content-notion-ops, content-critique-cycle — see memory note), so the repo edits below must be applied with the patch tool on a normal turn. Everything else from this lane's rounds is ALREADY committed in the repo (folds 433-442 in content-pipeline; reposition-round type in critique-cycle).

## 1. STAGED fold 443 — append to repo `content-pipeline/SKILL.md` after item (442)

**(443) Comparison tables don't survive social copying — paired-line format for FB-destined TECH posts (pair #124 v3):** a markdown/Notion table carries structure that a social paste renders broken; when a draft is FB-destined, replace the table with one paired line per axis — `**axis** — side A: value / side B: value` — bold rides as a Notion annotation, so a copy to social lands as clean plain text with no literal `*` or `|`; set the Platform multi_select to include the target platform so the page self-documents its destination. Date hygiene rides along: when the posting day differs from the writing day, pin absolute dates in the subtitle and section heads ("เทียบกัน 20 พ.ย.", "คืนวันที่ 18 พ.ย.") instead of "เมื่อคืน / ค่ำวันที่ X" (receipt/timeline gate), and sweep in-body references to the replaced structure too ("ตารางไม่ได้บอก" → "หกแกนข้างบนไม่ได้บอก").

## 2. STAGED edit — `content-notion-ops/SKILL.md` Error triage (insert after the 401 line)

- 429 `rate_limited` with `additional_data.retry_after` → sleep at least that many seconds and retry the SAME request once — `replace_content` is a full-body replace, so the retry is idempotent and cannot double-apply; verify with the read-back only after a 200 (a 429 left the body untouched).

## 3. STAGED edit — `content-critique-cycle/SKILL.md` (reposition-round bullet)

The reposition-round bullet cites "fold 443 in content-pipeline" — that fold number was never used there (content-side folds for this lane = 439-442; the next free number is 443, now used by the FB-ready fold in §1). Fix the citation to: "(pair #123 round, 2026-11-19; content-side lessons = folds 439-442 in content-pipeline)".

## 4. Pending owner decisions (NOT resolved — do not touch these pages without the owner's answer)

- #122 publish (Benz-authored, archived `web-archive/20261119-rakazo-app-connections-publish-benz-authored.txt`) carries 2 factual errors: "บอททั้ง 77 ตัว" and "77 Pages และ Databases" — machine truth: 77 = `healthToolCount` (tool count), roster 9, only 2 bots MCP-assigned ("Notion"↔Chief, "Notion MCP"↔Idea Keeper, distinct secretIds, same endpoint — NOT duplicates, do not merge). Owner chose not yet between: (a) apply the 3 corrected sentences + rebuild + published, (b) rebuild as-is with NOTEs, (c) send back to Benz.
- #123 publish (owner-pasted "คนสั่งงานครั้งเดียว...", archived `web-archive/20261119-rakazo-automation-publish.md`) graded 10/10 on reposition keys but 3 fact flags: bots 8→9 (Design Keeper, as-of), runs 270→277 (268+9) same-day drift, doc triggers 5→6 (Slack message is the 6th; the "2 ต้องเปิด Channel" line is only consistent in the 6-frame). Owner choice a/b/c pending.
- #123 reposition rewrite was approved directionally (new title "คนสั่งงานครั้งเดียว — แล้ว AI ทั้งทีมทำงานต่อกันอย่างไร?") and the pasted publish IS that rewrite — grade keys and holds above apply to it, not to the old v1 draft.

## 5. Transport notes (verified this lane)

- `PATCH /pages/{id}/markdown` replace_content: 429 `rate_limited` carries `additional_data.retry_after` — sleep ≥ retry_after and retry once; full-body replace is idempotent (cannot double-apply); read-back verify only after a 200.
- Draft-update sync trio: vault/posts file (HTML header Status/GUARDS re-measured) → Content Drafts page (props first if changed, then markdown replace) → repo commit; index.json + STATE.md ride the closing commit.
