# Book chapter-list pipeline (Books Library → body tables, at library scale)

Class: generating a per-book chapter list table (ordered, OPB-filtered, status-tracked) into each book page's Notion body — for one book or a 250+ book library, WITHOUT the owner typing book names.

## Canonical command template (per book)

```
ทำ Chapter List ของหนังสือ "<title>" (Notion page id: <page_id>) ตามนี้:
1) หาสารบบจริงจากแหล่งจริงเท่านั้น (child DB ของเล่ม / สำนักพิมพ์ / official summary) —
   ห้ามเรียงจากความจำ ห้ามสลับ/ข้าม/เติมบท ถ้าหาสารบบชัวร์ไม่ได้ ให้รายงานว่าหาไม่ได้แล้วจบ (ห้ามเดา)
   หน้าเป็น template เปล่าก็ทำได้ปกติ — สารบบมาจาก research ไม่ใช่จากเนื้อหาหน้า;
   ถ้า body มี section 📚 Chapter List อยู่แล้ว ให้ข้ามและรายงานว่ามีอยู่แล้ว (กันซ้ำ)
2) เขียน section ใหม่ท้ายสุดของ body (append block เท่านั้น) หัวข้อ "## 📚 Chapter List (OPB Filter)"
   — ห้ามแก้/ลบ/แตะ block เดิมใดๆ
3) ตาราง markdown 5 คอลัมน์: # | Chapter Title (Original) | Core Message (ฉบับ PHON) |
   ผ่านฟิลเตอร์ 3 Laws ของ OPB | Status
   - Core Message: สรุปแก่นบท 1-2 ประโยค ภาษาพูดแบบพร
   - ตัดสินผ่าน/ไม่ผ่านด้วยกฎนี้ตรงๆ:
     • Law #1 System > Emotion: อย่าให้อารมณ์เป็นคนตัดสินใจ ความรู้สึกคือ ข้อมูล ไม่ใช่ คำสั่ง
     • Law #2 Action Precedes Motivation: ไฟไม่มาก่อน การขยับต่างหากที่จุดไฟ
     • Law #3 Protect the System: งานยังไม่สำคัญเท่าระบบที่ทำงานได้พรุ่งนี้
     บทที่แก่นไม่ตรงกฎใดๆ เลย ใส่ -
   - Status 3 ค่าเท่านั้น: ⬜ QUEUED / ⏳ LOADING... / ✅ INSTALLED (ตัวอย่างต้องเห็นครบ 3 สถานะ)
ห้าม dispatch บอทอื่น ห้ามแตะฐาน/หน้าอื่น เสร็จรายงาน: กี่บท แหล่งสารบบคืออะไร
```

Non-negotiable guards (each maps to a real past failure):
- **Order from source, never model memory** — model-recalled chapter order scrambles; allow the bot to REPORT 'source not found' instead of guessing.
- **Paste the 3 Laws verbatim into the prompt** (source of truth: `duck-os/Main_Data_for_UDO.md` §The 3 Laws) — no fleet bot knows the criteria; unprompted it invents a filter.
- **Append-only body write** — existing body blocks are owner content; the bot adds its own section at the end only.
- **Lock the status vocabulary + format** — otherwise output drifts every run.

## Scale pattern (250+ books, owner never types titles)

1. Build the queue: query Books Library data source (title + page_id per row) → `books_queue.json` persisted in the repo shared dir (a /tmp copy dies).
2. TEST BATCH FIRST (5 books: 1 known-problem book + 4 from the queue) as one-shot routines to the chosen bot (Chief = proven Notion-MCP writer) before opening the full queue.
3. Snapshot-before-QC: before the batch, dump the sample page's body blocks (`GET /blocks/{page_id}/children` → ids+types+count to a JSON file). After, verify the old block list is intact and new blocks only APPENDED at the end — this is the proof that 'ของเดิมไม่โดนแตะ'; without it, an overwrite claim is unverifiable.
4. One book = one routine run (serial per bot). A 250-book library is days of queued runs, not one mega-run — a single run over the whole library dies on context, the failure that killed the ebook attempts.
5. Books without a real chapter source in the system must get their TOC researched per book (web, authoritative source); never let the batch fall back to model recall for missing books — skip-and-report instead.

## Validated run facts (test batch, QC-passed)
- Template-page rows exist in Books Library: some rows point at unfilled template pages (`Chapter #x- template`, `======` placeholder walls). OWNER DECISION — template pages STILL get the full chapter list: the TOC comes from web research, NOT from the page's own content, so the ONLY skip case is a TOC that cannot be verified from any reliable source (a skip list is still a deliverable, but it must hold only truly unverifiable books). When a rule changes mid-queue, already-skipped books never re-enter on their own — re-queue exactly those with the corrected prompt, staggered behind the main queue (e.g. +11h).
- Add a duplicate guard to the per-book prompt: if the body already contains a `📚 Chapter List (OPB Filter)` section, skip-with-report — prevents stacked sections on re-runs or previously-processed pages.
- Runtime expectations: a real book lands in ~5-10 min; a book needing multi-source TOC cross-checking can run 25+ min with 60+ tool calls (web_search ×14, web_fetch ×11) — that pace is CORRECT behavior, not a stall; confirm activity from `docker logs rakazo-worker-1 | grep agent.tool.completed` before declaring anything stuck.
- QC reads: Notion `table_row.cells` are lists of rich_text DIRECTLY (iterate and join each cell's list — no `.get("rich_text")` inside a cell); a long page read needs pagination AND a >60s timeout or the children endpoint times out mid-loop.
- `/v1/search` is FUZZY: querying the section heading loosely matches ~100 pages that merely mention 'chapter list' in prose — never infer widespread duplicate/old sections from a search hit count; open sample pages and check for actual `heading_2` + `table` blocks.
- Book pages hold per-chapter reading notes as `heading_3` (`Chapter #N- …`) — partially filled and that is fine; the new table is additive context, and a missing-chapter-notes page still gets a full table.
