# Content Study Vault — กติกาการจัดเก็บ

ระบบจัดเก็บงาน content writing ของ adduckivity เป็น markdown + wiki-link (เปิดใน Obsidian ได้)
แหล่งความจริงเดิมคงเดิมทั้งหมด — vault นี้คือชั้นเชื่อมโยง:

| ของจริง | ตำแหน่ง | vault ชี้ไปทางเดียว (อ่านอย่างเดียว ไม่แก้ที่นี่) |
|---|---|---|
| คู่ draft→publish | `content-study/index.json` (534 entries) | `pairs/` 1 ไฟล์/คู่ (สร้างจาก index.json) |
| หลักการเขียน | `skills/content-pipeline/SKILL.md` | — |
| ตัวโพสต์จริง | `content-study/posts/` + `content-study/web-archive/` | ลิงก์แบบ relative |

## โครงสร้าง

```
vault/
  README.md        ← ไฟล์นี้
  index.md         ← สารบัญกลาง (MOC): pair ล่าสุด / กิ่งเปิด / สายเรื่อง
  pairs/           ← 1 ไฟล์/คู่ pair-001.md ... pair-080.md (generate จาก index.json)
  branches/        ← กิ่งที่ยังเปิด (status: open / stock / graduated / dead)
  families/        ← สายเรื่องที่ข้ามหลายคู่
```

## กติกา wiki-link

- ลิงก์ไปคู่: `[[pair-080]]` (ไฟล์ pairs/pair-080.md)
- ลิงก์ไปกิ่ง: `[[branch-stock-79BC]]` ฯลฯ (ไฟล์ branches/*.md)
- ลิงก์ไปสายเรื่อง: `[[family-ai-brief-chain]]` ฯลฯ
- ไฟล์ pair ข้ามลิงก์กันเองได้ (กิ่งที่ graduate ลิงก์กลับคู่ต้นทาง)
- Obsidian: เปิด vault ที่ `content-study/vault/` → graph view จะเชื่อมโยงทั้งหมดให้เอง

## วงจรข้อมูล (ไปข้างหน้า ไม่ย้อน)

1. จบคู่ใหม่ → append `index.json` + `STYLE_CORPUS.md` + Notion ตามเดิม (ไม่เปลี่ยน workflow)
2. สร้างไฟล์ `pairs/pair-0NN.md` ให้คู่ใหม่ + อัปเดต `vault/index.md`
3. กิ่งที่เกิดใหม่ → สร้างไฟล์ใน `branches/` (status: open)
4. กิ่ง graduate → เปลี่ยน status + ลิงก์ไปคู่ที่เขียนจริง
5. กิ่งตาย/ถูกดูดเข้าโพสต์อื่น → status: dead + อ้างเหตุผล

## สิ่งที่ย้ายออกจาก STATE.md (2026-11-02)

- ประวัติ pair #1-#80 ทั้งหมด → `pairs/` (source = index.json)
- กิ่ง stock ที่ยังเปิด → `branches/`
- รายละเอียด infra (ComfyUI, llama-server, cron, Notion pitfalls) ค้างอยู่ใน STATE.md section infra — ไม่ย้าย (เป็นของเครื่อง ไม่ใช่ของ content)

## ข้อจำกัด

- `pairs/*.md` generate จาก `index.json` — ถ้า index เปลี่ยน (เช่น status อัปเดตหลัง CLOSED) รัน generator ซ้ำได้:
  `python3 skills/content-pipeline/scripts/generate_vault.py`
- สคริปต์ merge-safe: ไม่ทับไฟล์ที่แก้มือไว้แล้วถ้า entry ไม่เปลี่ยน
