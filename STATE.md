# STATE.md — KhaoKlong (สถานะปัจจุบัน — ประวัติย้ายออกหมด ดู vault)

## Content Vault (ระบบจัดเก็บใหม่ 2026-11-02)

- **ประวัติ pair ทั้งหมดย้ายไป `content-study/vault/`** — markdown + wiki-link (เปิดใน Obsidian ได้):
  - `vault/index.md` = สารบัญกลาง (คู่ล่าสุด / คู่ที่ยังเปิด / กิ่ง / สายเรื่อง)
  - `vault/pairs/pair-0NN.md` = 1 ไฟล์/คู่ (generate จาก index.json — ห้ามแก้มือ, regenerate ด้วย `python3 skills/content-pipeline/scripts/generate_vault.py` — merge-safe, ลบไฟล์ stale เอง; มีลิงก์ Research: กลับ research node)
  - `vault/research/` = symlink → `~/hermes-agent/research/` (RESEARCH VAULT — ต้นฉบับ 21 ไฟล์ + `books/` โครงรับ book database: books/<slug>/book.md + quotes.md + notes.md; skill อ่านผ่าน symlink ที่ references/, Obsidian เปิดที่ repo root เพื่อให้สอง vault อยู่ graph เดียว)
  - `vault/posts/` = ไฟล์โพสต์จริง (`content-study/posts/` = symlink เข้า vault — path เดิมใช้ได้); **WP snapshots ย้ายออก vault 2026-11-02** → `content-study/web-archive/` ไฟล์จริง (WP sync ไม่ผ่าน vault แล้ว — ไม่ชนกับ notion-content); loop artifacts (critique/publish/gates) อยู่ `vault/artifacts/` (219 ไฟล์)
  - `vault/branches/` = กิ่งที่ยังเปิด/stock/graduated (แก้มือได้ — generator ไม่แตะ)
  - `vault/families/` = สายเรื่องข้ามคู่ (แก้มือได้)
  - กติกาทั้งหมดใน `vault/README.md`
- คู่สุดท้ายที่ปิด: **#79 (locked-system-still-breaks)** + **#80 (let-them-fight)** — published 2026-11-02 — brief-chain #57/#64/#80 จบครบ; **#81 (blind-spot-count)** CLOSED 2026-11-02 (gate A, publish 97wc keys 13/13) — บทเปิดตระกูล blind spot; **#82 (problem-prevention-over-solving)** อยู่ขั้น rewritten รอ owner publish (Benz r1 5/5 + gate B + spec — keys 10 ใน archive)
- กิ่ง stock สำคัญ: กิ่ง B/C ของ #79 ([[branch-stock-79BC]] — รายงานปกติแต่ผิดปกติ / ทางไปต่อเมื่อพัง) — รอเคสจริง/owner เรียก ตาม rule 10; กิ่ง open อื่นดู vault/index.md
- โน้ต: หมายเลข pair มี collision เดิม 1 จุด — "pair #40" ถูกใช้ซ้ำ 2 โพสต์ 10-06 (daily-repetition = #40, embrace-the-limit = #40b ใน vault)

## Content workflow ปัจจุบัน (คงเดิม)

- Skill หลัก: `skills/content-pipeline/SKILL.md` (items ถึง 319 — 313-316 จาก #78-#80, 317 opener-post class, 318 owner-pick-non-top-ranked-gate, 319 insight-level ladder (L1-4 ปกติ / L5-6 event-driven เฉพาะมีกลไก+เคสจริง — owner rule)) + `references/pair-history.md`
- จบคู่ = append index.json + STYLE_CORPUS.md + Notion PATCH → รัน generate_vault.py → สร้าง/อัปเดต pair-N.md ตาม workflow ใน vault/README.md
- สถานะ: ไม่มี draft ค้าง ไม่มี publish รอเกรด

## Infra สถานะ

- **llama-server = systemd service:** `~/.config/systemd/user/llama-server.service` (enabled) — Qwen3.8-27B-UD-Q4_K_M, -ngl 95 -t 12 -c 262144 q8_0 KV, port 8080 --host 0.0.0.0; log journalctl --user -u llama-server; **user rule: ไม่ start/restart เอง**; boot race แก้ด้วย ExecStartPre wait-for-cuda.sh (2026-09-25)
- **daily-foreign-news** cron `4be8c05534b4` (08:00 GMT+7 → Telegram News topic): UNPINNED จาก local Qwen — ตาม fallback chain (custom/Qwen → zai/glm-5.3); pinned job ไม่ยืม fallback (by design)
- **ComfyUI:** ~/ComfyUI + .venv, models ครบ 14/14 (2026-09-06), GPU 0 / Hermes LLM GPU 1, port 8188
- **Notion:** token bot "Hermes-connection" = NOTION_API_KEY ใน ~/.hermes/.env — re-verify ก่อนใช้ (เคย 401 flapping); Content Drafts DB `3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520`; KB DB `3c9df8d8-8d8c-81ac-ba5e-fa129e493638`; pitfalls ครบใน skill content-pipeline (PATCH /markdown replace_content, H1 strip, Date type, dashed-UUID, empty-paragraph จาก paste, ฯลฯ)
- **weekly-wp-archive-sync** cron `972b24976bf0` (อาทิตย์ 10:00): sync_wp_posts.py → web-archive/ + index.json + auto-commit
- **weekly-notion-content-sync** cron `578a24d9a04a` (อาทิตย์ 10:30, no_agent): Notion DB **"Adduckivity Content" `303df8d8-8d8c-8013-baa1-c2fd25e7c9a5` = publish master** (248 rows: Published 227/Ready 11/Drafting 6/Idea 3 — owner: "publish เป็นหลัก draft เป็นรอง") → `sync_adduckivity_content.py` → `vault/notion-content/` (Published = body เต็ม / อื่น index-only; hubs laws+categories+tags≥3; **paired 110 กลับ vault/posts**; skip ด้วย last_edited_time → รอบเงียบ ~3 วิ ไม่ commit; **secret redaction ใน sync ทุกครั้ง** — เคยจับ Discord+CF token ในหน้า writing-ai-skills ของ Notion, พร rotate เอง 2026-11-02); **+ Books Library** `2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0` → `sync_books_library.py`: catalog 253 เล่ม (chapter rows พร้อม Core Message/Status) + **chapter notes อัตโนมัติ** เฉพาะเล่มที่ graduate (มีโฟลเดอร์ใน research/books/) — ดึง body ของ row ✅ INSTALLED เท่านั้น (owner rule: body ส่วนอื่นของหน้าเล่ม = กระดาษทด ห้ามแตะ) → `research/books/<slug>/notes/ch-NN.md` (image external เท่านั้น — Notion-hosted URL หมดอายุทำลาย idempotency); เล่ม graduate แรก: **four-thousand-weeks** (Ch.2+3 INSTALLED, pair-017 ↔ research ↔ book เชื่อม 3 ทิศผ่าน BOOKS_LINKS ใน generator); wrapper `~/.hermes/scripts/sync_adduckivity_content_and_commit.sh` (sync ทั้งสอง + auto-commit เฉพาะมี diff)
- **notion_drafts_watcher** watchdog: ping Telegram เมื่อมี draft ใหม่จาก model อื่น (เช็ค state file ก่อนเรียก "new")
- **KB pages (2026-09-28):** "International News Digest — 2026-09-28" `3f0df8d8-8d8c-815b-985f-f9ff4632b49c` (17 blocks) + "AI Harness — นิยาม + วิธีเลือก harness" `40ddf8d8-8d8c-8194-ace5-f2772f2ceae7` — **ขยาย landscape 2026-11-03 → 74 blocks** (Kendr 50-harness scorecard 19 full rows, winder fleet-tested 9, TechStackUps minimal/business, นอกสาย coding, +3 ref sources, Updated=2026-11-03, verify read-back ผ่าน); Notion pitfall: /databases/{id}/query ไม่รับ page_size ทั้ง body และ query string (400) — ใช้ body `{}` ได้ (default กลับมาครบถ้า ≤100 หน้า); **Notion pitfall (2026-11-03): PATCH /blocks/{paragraph_id}/children = NEST ใต้ block นั้น ไม่ใช่ sibling** — ต้อง PATCH /pages/{id}/children พร้อม `"after": <block_id>` แล้ว rebuild rich_text ของ nested originals + DELETE ทิ้ง
- **Six-level harness draft (2026-11-03):** owner brief "storytelling about harness + 6 levels" → ร่าง 6 ร่าง (ไฟล์ trial: `posts/20261103-cnt-ai-harness-six-levels.md`) → owner เลือก L2 → pair **#98** เปิดจริง: `posts/20261103-cnt-ai-harness-pair-not-piece.md` (66wc, L2 doing-wrong-unnoticed) → **steer รอบสอง (เย็น 2026-11-03):** owner ขอเล่าใหม่แบบ storytelling ไม่วิชาการ (non-tech อ่านจบ) + ภาพ "harness=ร่างกาย model=สมอง" + ทำเป็น 6 ขั้น → ร่างใหม่ `posts/20261103-cnt-ai-harness-body-brain-six-levels.md` (ภาพสมอง-ร่างกายเดียวทั้ง 6 level, prose paragraphs ตาม steer #58, เรา 9 / '?' 0 / CUT zero ครบ) → owner directive ปรับ title + **push แทน draft เดิม**: หน้า Notion เดิม `40ddf8d8-8d8c-819a-8770-fe9b8ea478a7` (props ใหม่: title "ถ้า AI เป็นคน โมเดลคือสมอง แล้ว harness คือทุกส่วนที่เหลือ", Status draft) → **directive รอบสาม: "เอาทั้ง 6 level ให้อยู่บทความเดียวกัน"** → รวมเป็นบทเดียวไหลขึ้น 6 ขั้น (H3 ภาษาคน ขั้นที่หนึ่ง…หก, quote bold เดียวที่ขั้นสอง, closer bold เดียว, ~163wc, เรา 6 / '?' 0 / เลขอารบิก 0 / CUT clean) — push รอบสอง + verify read-back 42 blocks / empty 0 / H3 6 / tail ครบ; เนื้อ pair #98 v1 + ร่าง 6 แยก + ห้องนักบิน อยู่ใน git history / pair-not-piece / cockpit-story ตามลำดับ — รอ Benz r1 หรือ owner ปรับต่อ (index.json slug = body-brain-six-levels)

## Pitfalls เรียนรู้ (ComfyUI era — คงไว้)

- download.pytorch.org throttle → ใช้ PyPI ปกติ; pypi.nvidia.com ช้ามาก; ห้ามรัน download script ซ้ำซ้อน 2 ตัว (เขียนทับ .part เดียวกัน → corrupt); HF ช้าให้ลอง hf-mirror.com
