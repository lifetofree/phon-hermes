# Pending canon sync — folds 443-444 + 429 triage note (2026-11-20)

สถานะ: folds 433-442 sync ลง canon `skills/content-pipeline/SKILL.md` ใน session แล้ว (append หลัง fold 442) — สอง folds ด้านล่างยังไม่อยู่ใน canon เพราะ skill_manage patch ไม่ได้ทั้งจาก registry gap (categorized symlink skills) และ SKILL.md >100k limit — session ถัดไป append ต่อท้าย fold 442 ใน canon แล้วลบไฟล์นี้

## Fold 443 — Facebook-ready conversion of a comparison table (pair #124 v3)

A Notion table block cannot be pasted onto Facebook — when the owner wants the comparison postable there, replace the table with paired bold-lead lines, one paragraph per axis, in the form `**แกน** — บ้านเช่า: … / บ้านเรา: …` (blank line between axes); the bold rides as a Notion annotation and strips to clean plain text on paste, so no markdown syntax survives on the feed. Then rename the H2 away from "ตาราง" when no table remains, fix downstream references ("ตารางไม่ได้บอก" → "หกแกนข้างบนไม่ได้บอก"), and add "FB" to the Platform multi_select so the draft's post target is recorded.

## Fold 444 — Bot-authored drafts come in sets (pair #125 intake)

Cross-check numbers between pages before grading either: one bot run landed two second-brain pages whose counts contradicted each other (637 vs 644 rows) — the later page explained the earlier page's numbers were partial because 429s skipped child tables silently. Intake rule: when one bot run produces multiple drafts, read ALL of them before grading; the newest page is not automatically the corrected one — find the page that explains the discrepancy and take its numbers as the reported facts, label superseded counts as superseded, and archive every page of the set (non-target pages are evidence, not rewrite targets unless ordered). Unverified counts inside a bot draft get dropped or re-derived locally, never carried into the rewrite (same ledger standard as 433).

## Transport note — content-notion-ops triage (ยังไม่มี 429 ที่นั่น)

429 `rate_limited` (`public_api_request_rate_limit`) carries `additional_data.retry_after` (seconds) — wait N+2s and retry the SAME idempotent request (body replace via `/pages/{id}/markdown` and property PATCHes are safe to retry; a CREATE that 429s has unknown state — title-search before re-creating). The Notion workspace budget is shared with other integrations (rakazo bots run Notion-MCP audits on the same workspace), so 429 bursts land while bots are active, not only from your own loop speed. Same rule folded into rakazo-ops (Shared Notion API budget section): bulk audits that hit 429 must record skipped items — a silent skip produces a plausible-looking wrong total.

## ที่เกี่ยวข้องแต่ sync แล้ว
- folds 433-438 (pair #122) + 439-442 (pair #123 reposition) — อยู่ใน canon แล้ว
- reposition round type — อยู่ใน content-critique-cycle (Round type selector) แล้ว
- voice guide สำหรับบอต rakazo — `duck-os/Rakazo_Drafting_Voice_Guide.md` (repo)