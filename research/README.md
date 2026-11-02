# Research Vault — ของจริงที่รวบรวมจากภายนอก

แหล่งความจริงของ research ทั้งหมด (ปัจจุบัน: research ต่อเรื่องสำหรับ content — อนาคต: book database)

## โครงสร้าง

```
research/
  README.md       ← ไฟล์นี้
  index.md        ← สารบัญ (generate จาก generate_research_index.py)
  *-research.md   ← research ต่อเรื่อง (front-matter: type: research / topic / used_by)
  books/          ← book database (1 โฟลเดอร์/เล่ม)
```

## โครง books/ (สำหรับ database หนังสือที่จะนำเข้า)

```
books/<slug-เล่ม>/
  book.md         ← หน้าหลักเล่ม (front-matter: type: book / title / author / status: verified|reading|queued)
  quotes.md       ← quote ที่ verify แล้ว (แหล่ง+ตำแหน่ง ทุกตัว — ตามกฎ quote-provenance ของ skill)
  notes.md        ← โน้ต/สรุปต่อบท
```

## กติกาการเชื่อมกับ content (single direction — research เป็นต้นทาง)

- content side ลิงก์มาหา: `pairs/pair-0NN.md` มี `Research: [[xxx-research]]` (generator ใส่ให้จาก RESEARCH_LINKS)
- research side ลิงก์กลับ: front-matter `used_by: [[pair-0NN]]`
- หนังสือ → โพสต์: หน้าเล่ม (book.md) ลิงก์ `used_in: [[pair-0NN]]`; โพสต์อ้าง quote จากเล่มได้เฉพาะ quote ที่อยู่ใน quotes.md แล้วเท่านั้น (quote-provenance rule)

## กติกา symlink

- ไฟล์จริงอยู่ที่นี่เท่านั้น — content-study/vault/research และ skills/content-pipeline/references/*-research.md เป็น symlink
- แก้ไฟล์ = แก้ที่นี่

## Obsidian

เปิด vault ที่ระดับ `~/hermes-agent/` (repo root) — content vault กับ research vault จะอยู่ใน graph เดียวกัน คลิกข้ามได้
