---
name: duck-os-ssot
version: 1.0.0
author: curator
license: MIT
description: "Use when merging frameworks into the Duck OS SSOT files."
metadata:
  hermes:
    tags: [duck-os, knowledge-base, ssot]
    related_skills: [udo-knowledge-base]
---

# Duck OS SSOT maintenance

## When to Use

- The user sends a list of frameworks / models / กฎ and asks to compare, merge, rewrite, or sync them into Duck OS knowledge files (any phrasing of "เทียบกับของเดิม / merge เข้า SSOT / update Main_Data").
- Any edit to files under `~/hermes-agent/duck-os/` — including sync checks, version bumps, or conflict review.
- NOT for Notion KB page CRUD (that is udo-knowledge-base) and NOT for content-study posts.

Governs edits to `~/hermes-agent/duck-os/` — the single source of truth all 5 Duck OS bots (udo, adduck, sales, scout, vault) read via their SOUL.md.

## File roles

- `Main_Data_for_UDO.md` — MASTER copy, detailed (PART 1–9; PART 1 holds หมวด 1–8). Framework knowledge lands here first.
- `OPB_Core_System.md` — CONDENSED copy of the same frameworks. Every framework change in Main_Data must be synced here; drifting copies are the failure mode.
- `Duck_OS_Instruction.md` / `Duck_Book_Library.md` — system prompt / book library; rarely touched by framework merges.
- `~/duck-os/` (2 stale files at home) is a LEGACY copy — never update it, even though Duck_OS_Instruction.md's workspace section still names that path. Bots read `~/hermes-agent/duck-os/`.
- Versioning: bump the H1 build stamp to `build YYYYMMDDNNN` and add a one-line `> **Update YYYY-MM-DD:**` note under the title summarizing what merged.

## Merge procedure (user sends a framework set)

User directive style: "เปรียบเทียบ … create, merge, rewrite — if >95% confident proceed". Act without further questions once classification is clear; ask only on genuine conflicts.

1. **Classify** — grep all 4 SSOT files for each framework name. Per item: EXPAND (already present, new definition fuller → rewrite that block in place, keep user's fuller wording) or NEW (absent → add under the matching หมวด; create a new หมวด only when a whole group is new — number sequentially, e.g. หมวด 7, หมวด 8).
2. **Conflict-check** — each framework against the 3 Laws and Phon DNA filters (Asset over Activity, anti-hype, low-effort maintenance). Flag conflicts to the user; never silently drop or "correct" user-supplied content. It is fine (expected) to append a NEW Phon DNA Filter line for a newly added หมวด so the merged material inherits the house rules.
3. **Apply** — targeted patches (patch tool), never whole-file rewrites; untouched content stays byte-identical. Sync OPB_Core_System.md in the same pass: condensed rendering of every expanded/new framework.
4. **Verify before committing**
   - CJK/codepoint scan on both touched files = 0 hits: regex `[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af\u0400-\u04ff]` (established repo convention; CJK has leaked into Thai drafts before).
   - Assert every framework key string is present in its target file (count them — e.g. 23/23) so nothing was silently dropped.
   - Re-read the Thai prose in the diff: generated Thai silently duplicates or drops letters (valid codepoints, so scans pass) — grep long technical words for stray/dropped characters, e.g. อุตสาหกรรม misspelled as อุตสุตสาหกรรม passes CJK scans.
5. **Record + ship** — prepend a dated entry under STATE.md `## Recent Activity`, then commit + push (standing rule: all repo work is committed and pushed to GitHub).

## Pitfalls

- Do not renumber or reorganize existing หมวด to make a merge fit — new groups get the next free number; renumbering breaks every cross-reference in bot SOUL files and STATE history.
- The condensed OPB_Core_System.md uses plain-line formatting (no markdown bullets/headings inside sections) — match its house style when syncing, don't paste Main_Data's bullet syntax.
- `write_file` on STATE.md after a partial (paginated) read gets refused — use `patch` with a unique anchor like the `## Recent Activity` heading.
