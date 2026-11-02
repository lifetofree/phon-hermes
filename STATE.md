# STATE.md — KhaoKlong (สถานะปัจจุบัน — ประวัติย้ายออกหมด ดู vault)

## Content Vault (ระบบจัดเก็บใหม่ 2026-11-02)

- **ประวัติ pair ทั้งหมดย้ายไป `content-study/vault/`** — markdown + wiki-link (เปิดใน Obsidian ได้):
  - `vault/index.md` = สารบัญกลาง (คู่ล่าสุด / คู่ที่ยังเปิด / กิ่ง / สายเรื่อง)
  - `vault/pairs/pair-0NN.md` = 1 ไฟล์/คู่ (generate จาก index.json — ห้ามแก้มือ, regenerate ด้วย `python3 skills/content-pipeline/scripts/generate_vault.py` — merge-safe, ลบไฟล์ stale เอง)
  - `vault/branches/` = กิ่งที่ยังเปิด/stock/graduated (แก้มือได้ — generator ไม่แตะ)
  - `vault/families/` = สายเรื่องข้ามคู่ (แก้มือได้)
  - กติกาทั้งหมดใน `vault/README.md`
- คู่สุดท้ายที่ปิด: **#79 (locked-system-still-breaks)** + **#80 (let-them-fight)** — ทั้งคู่ published 2026-11-02 — brief-chain #57/#64/#80 จบครบทุกกิ่ง
- กิ่ง stock สำคัญ: กิ่ง B/C ของ #79 ([[branch-stock-79BC]] — รายงานปกติแต่ผิดปกติ / ทางไปต่อเมื่อพัง) — รอเคสจริง/owner เรียก ตาม rule 10; กิ่ง open อื่นดู vault/index.md
- โน้ต: หมายเลข pair มี collision เดิม 1 จุด — "pair #40" ถูกใช้ซ้ำ 2 โพสต์ 10-06 (daily-repetition = #40, embrace-the-limit = #40b ใน vault)

## Content workflow ปัจจุบัน (คงเดิม)

- Skill หลัก: `skills/content-pipeline/SKILL.md` (items ถึง 316 — รวม 313-316 ที่ fold จาก #78-#80: D-with-primary gate / double-gate / critic-offered principle / metaphor-stronger-than-conclusion) + `references/pair-history.md`
- จบคู่ = append index.json + STYLE_CORPUS.md + Notion PATCH → รัน generate_vault.py → สร้าง/อัปเดต pair-N.md ตาม workflow ใน vault/README.md
- สถานะ: ไม่มี draft ค้าง ไม่มี publish รอเกรด

## Infra สถานะ

- **llama-server = systemd service:** `~/.config/systemd/user/llama-server.service` (enabled) — Qwen3.8-27B-UD-Q4_K_M, -ngl 95 -t 12 -c 262144 q8_0 KV, port 8080 --host 0.0.0.0; log journalctl --user -u llama-server; **user rule: ไม่ start/restart เอง**; boot race แก้ด้วย ExecStartPre wait-for-cuda.sh (2026-09-25)
- **daily-foreign-news** cron `4be8c05534b4` (08:00 GMT+7 → Telegram News topic): UNPINNED จาก local Qwen — ตาม fallback chain (custom/Qwen → zai/glm-5.3); pinned job ไม่ยืม fallback (by design)
- **ComfyUI:** ~/ComfyUI + .venv, models ครบ 14/14 (2026-09-06), GPU 0 / Hermes LLM GPU 1, port 8188
- **Notion:** token bot "Hermes-connection" = NOTION_API_KEY ใน ~/.hermes/.env — re-verify ก่อนใช้ (เคย 401 flapping); Content Drafts DB `3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520`; KB DB `3c9df8d8-8d8c-81ac-ba5e-fa129e493638`; pitfalls ครบใน skill content-pipeline (PATCH /markdown replace_content, H1 strip, Date type, dashed-UUID, empty-paragraph จาก paste, ฯลฯ)
- **weekly-wp-archive-sync** cron `972b24976bf0` (อาทิตย์ 10:00): sync_wp_posts.py → web-archive/ + index.json + auto-commit
- **notion_drafts_watcher** watchdog: ping Telegram เมื่อมี draft ใหม่จาก model อื่น (เช็ค state file ก่อนเรียก "new")

## Pitfalls เรียนรู้ (ComfyUI era — คงไว้)

- download.pytorch.org throttle → ใช้ PyPI ปกติ; pypi.nvidia.com ช้ามาก; ห้ามรัน download script ซ้ำซ้อน 2 ตัว (เขียนทับ .part เดียวกัน → corrupt); HF ช้าให้ลอง hf-mirror.com
