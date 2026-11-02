# Content Study Vault — กติกาการจัดเก็บ

ระบบจัดเก็บงาน content writing ของ adduckivity เป็น markdown + wiki-link (เปิดใน Obsidian ได้)
แหล่งความจริงเดิมคงเดิมทั้งหมด — vault นี้คือชั้นเชื่อมโยง:

| ของจริง | ตำแหน่งใน vault | จุดเข้าเดิม (ยังใช้ได้เหมือนเดิม) |
|---|---|---|
| คู่ draft→publish | `pairs/` 1 ไฟล์/คู่ (generate จาก index.json) | `content-study/index.json` |
| ตัวโพสต์จริง | `posts/` + `web-archive/` (ไฟล์จริงอยู่ที่นี่) | `content-study/posts/`, `content-study/web-archive/` = symlink กลับเข้า vault |
| Research ต่อเรื่อง | `research/` (ไฟล์จริงอยู่ที่นี่) | `skills/content-pipeline/references/*-research.md` = symlink กลับเข้า vault |
| หลักการเขียน | (อยู่นอก vault) | `skills/content-pipeline/SKILL.md` |

## โครงสร้าง

```
vault/
  README.md        ← ไฟล์นี้
  index.md         ← สารบัญกลาง (MOC): pair ล่าสุด / คู่เปิด / research / กิ่ง / สายเรื่อง
  pairs/           ← 1 ไฟล์/คู่ (generate จาก index.json) — มีลิงก์ Research: กลับไป research node
  research/        ← ไฟล์ research จริง (front-matter type: research + used_by ลิงก์กลับ pair)
  posts/           ← ไฟล์ draft จริง
  web-archive/     ← ไฟล์ publish/critique archive จริง
  branches/        ← กิ่ง (แก้มือได้)
  families/        ← สายเรื่อง (แก้มือได้)
```

## กติกา wiki-link

- ลิงก์ไปคู่: `[[pair-080]]` (ไฟล์ pairs/pair-080.md)
- ลิงก์ไปกิ่ง: `[[branch-stock-79BC]]` ฯลฯ (ไฟล์ branches/*.md)
- ลิงก์ไปสายเรื่อง: `[[family-ai-brief-chain]]` ฯลฯ
- ไฟล์ pair ข้ามลิงก์กันเองได้ (กิ่งที่ graduate ลิงก์กลับคู่ต้นทาง)
- Obsidian: เปิด vault ที่ `content-study/vault/` → graph view จะเชื่อมโยงทั้งหมดให้เอง

## วงจรข้อมูล (ไปข้างหน้า ไม่ย้อน)

1. จบคู่ใหม่ → append `index.json` + `STYLE_CORPUS.md` + Notion ตามเดิม (ไม่เปลี่ยน workflow)
2. research ใหม่ที่เขียนลง `vault/research/<slug>-research.md` (เขียนที่นี่เท่านั้น — skill อ่านผ่าน symlink)
3. รัน `python3 skills/content-pipeline/scripts/generate_vault.py` → สร้าง/อัปเดต `pairs/pair-0NN.md` + index.md
   - ถ้าคู่ใหม่ใช้ research เดิม: เพิ่ม key ใน RESEARCH_LINKS ของ generator ก่อนรัน (ลิงก์จะโผล่ในไฟล์ pair เอง)
   - research ใหม่ 1 ไฟล์: เพิ่มลิงก์ใน front-matter used_by + มันจะขึ้นใน MOC เอง
4. กิ่งที่เกิดใหม่ → สร้างไฟล์ใน `branches/` (status: open)
5. กิ่ง graduate → เปลี่ยน status + ลิงก์ไปคู่ที่เขียนจริง
6. กิ่งตาย/ถูกดูดเข้าโพสต์อื่น → status: dead + อ้างเหตุผล

## หลัก symlink (ต้นฉบับเดียว)

- ไฟล์จริงอยู่ใน vault เท่านั้น — จุดเข้าเดิมทุกจุดเป็น symlink ชี้เข้ามา
- skill (`skill_view`/สคริปต์) และ cron (sync_wp_posts.py) ยังใช้ path เดิมได้เต็มรูปแบบ
- **ห้ามแก้ไฟล์ผ่านจุดเข้า symlink โดยไม่รู้ว่าเป็น symlink** — แก้ที่ไฟล์ใน vault คือแก้ต้นฉบับเดียวกัน

## สิ่งที่ย้ายออกจาก STATE.md (2026-11-02)

- ประวัติ pair #1-#80 ทั้งหมด → `pairs/` (source = index.json)
- กิ่ง stock ที่ยังเปิด → `branches/`
- รายละเอียด infra (ComfyUI, llama-server, cron, Notion pitfalls) ค้างอยู่ใน STATE.md section infra — ไม่ย้าย (เป็นของเครื่อง ไม่ใช่ของ content)

## ข้อจำกัด

- `pairs/*.md` generate จาก `index.json` — ถ้า index เปลี่ยน (เช่น status อัปเดตหลัง CLOSED) รัน generator ซ้ำได้:
  `python3 skills/content-pipeline/scripts/generate_vault.py`
- สคริปต์ merge-safe: ไม่ทับไฟล์ที่แก้มือไว้แล้วถ้า entry ไม่เปลี่ยน
