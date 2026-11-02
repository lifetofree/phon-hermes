# Content Study Vault — กติกาการจัดเก็บ

ระบบจัดเก็บงาน content writing ของ adduckivity เป็น markdown + wiki-link (เปิดใน Obsidian ได้)
แหล่งความจริงเดิมคงเดิมทั้งหมด — vault นี้คือชั้นเชื่อมโยง:

| ของจริง | ตำแหน่งใน vault | จุดเข้าเดิม (ยังใช้ได้เหมือนเดิม) |
|---|---|---|
| คู่ draft→publish | `pairs/` 1 ไฟล์/คู่ (generate จาก index.json) | `content-study/index.json` |
| ตัวโพสต์จริง | `posts/` (ไฟล์จริงอยู่ที่นี่) | `content-study/posts/` = symlink กลับเข้า vault |
| WP snapshot archive | — (อยู่นอก vault) | `content-study/web-archive/` = ไฟล์จริง (WP sync เขียนตรงนี้ — ไม่ผ่าน vault) |
| Loop artifacts | `artifacts/` (critique/publish archives ของ loop) | wiki-link หาด้วยชื่อไฟล์ — path ไม่สำคัญ |
| Research ต่อเรื่อง | `research/` (ไฟล์จริงอยู่ที่นี่) | `skills/content-pipeline/references/*-research.md` = symlink กลับเข้า vault |
| หลักการเขียน | (อยู่นอก vault) | `skills/content-pipeline/SKILL.md` |

## โครงสร้าง

```
~/hermes-agent/
  research/            ← RESEARCH VAULT (ต้นฉบับ): *-research.md + books/ (โครงรับ book DB) + index.md
  content-study/
    vault/             ← CONTENT VAULT
      README.md        ← ไฟล์นี้
      index.md         ← MOC: pair / แท็ก / research / lessons / events / กิ่ง / สายเรื่อง
      pairs/           ← 1 ไฟล์/คู่ (generate จาก index.json) — มีลิงก์ Research: → research node
      research/        ← symlink → ../../research
      posts/           ← ไฟล์ draft จริง
      artifacts/       ← loop artifacts (critique/publish/gates — wiki-link หาด้วยชื่อไฟล์)
      branches/ families/
    posts/               ← symlink → vault (จุดเข้าเดิม)
    web-archive/         ← ไฟล์จริง (WP snapshots — sync_wp_posts.py เขียนตรงนี้)
  skills/content-pipeline/references/ ← symlink → research (จุดเข้าเดิมของ skill)
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

## ประเภท node + contract (เพิ่มชนิดใหม่ทำตามนี้)

| type | โฟลเดอร์ | ใครสร้าง | generator ทำอะไร |
|---|---|---|---|
| `pair` | pairs/ | generator | สร้าง/ลบ stale อัตโนมัติ (มี hash) |
| `tag` | tags/ | generator (สแกน hashtag จาก archive) | สร้าง/ลบ stale อัตโนมัติ (มี hash) |
| `research` | **อยู่นอก vault** — `~/hermes-agent/research/` (vault มี symlink ชี้) | มือ (front-matter `type: research` + used_by) | ไม่แตะ — ขึ้น MOC จาก research/ |
| `branch` | branches/ | มือ (status: open/stock/graduated/dead) | ไม่แตะ — open/stock ขึ้น MOC |
| `family` | families/ | มือ | ไม่แตะ — ขึ้น MOC |
| `lesson` | lessons/ | มือ (แบบแผน critique ที่วนซ้ำ — สร้างเมื่อวน ≥2 ครั้ง) | ไม่แตะ — ขึ้น MOC |
| `event` | events/ | มือ (**เงื่อนไข: เหตุการณ์เดียวกำเนิด ≥2 ชิ้นงานเท่านั้น**) | ไม่แตะ — ขึ้น MOC |

กติกาเพิ่ม node ชนิดใหม่: (1) ตัดสินใจว่า generated (ต้องมี data source + hash + stale cleanup) หรือ curated (มือ + MOC section) (2) เพิ่มแถวในตารางนี้ (3) ถ้า generated ให้เข้า generator + มี hash เหมือน pair/tag

## หลัก symlink (ต้นฉบับเดียว)

- ไฟล์จริง: posts/ อยู่ใน vault, web-archive/ (WP snapshots) อยู่นอก vault ที่ `content-study/web-archive/`, loop artifacts อยู่ `vault/artifacts/` — research/ อยู่ที่ `~/hermes-agent/research/` (repo root)
- skill (`skill_view`/สคริปต์) และ cron (sync_wp_posts.py) ยังใช้ path เดิมได้เต็มรูปแบบ
- Obsidian: **เปิด vault ที่ระดับ `~/hermes-agent/`** — content vault กับ research vault อยู่ graph เดียว คลิกข้ามได้
- **ห้ามแก้ไฟล์ผ่านจุดเข้า symlink โดยไม่รู้ว่าเป็น symlink** — แก้ที่ไฟล์ใน vault คือแก้ต้นฉบับเดียวกัน

## สิ่งที่ย้ายออกจาก STATE.md (2026-11-02)

- ประวัติ pair #1-#80 ทั้งหมด → `pairs/` (source = index.json)
- กิ่ง stock ที่ยังเปิด → `branches/`
- รายละเอียด infra (ComfyUI, llama-server, cron, Notion pitfalls) ค้างอยู่ใน STATE.md section infra — ไม่ย้าย (เป็นของเครื่อง ไม่ใช่ของ content)

## ข้อจำกัด

- `pairs/*.md` generate จาก `index.json` — ถ้า index เปลี่ยน (เช่น status อัปเดตหลัง CLOSED) รัน generator ซ้ำได้:
  `python3 skills/content-pipeline/scripts/generate_vault.py`
- สคริปต์ merge-safe: ไม่ทับไฟล์ที่แก้มือไว้แล้วถ้า entry ไม่เปลี่ยน
