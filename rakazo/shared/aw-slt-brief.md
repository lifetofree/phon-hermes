# บรีฟจาก Chief → Adduck Writer: rewrite โพสต์ Social Learning Theory

**ภารกิจ:** Phon สั่งให้คุณเป็นคนถือปากกา — ทำ critique + rewrite บน**หน้าเดิม** (ห้ามสร้างหน้าใหม่)
หน้า draft: https://www.notion.com/p/41adf8d88d8c814ea83cfa4ca506f8c6 (ฐาน Content Drafts, Status=draft)

## กติกาบังคับ

1. **โหลด skill `/adduck-writer` ก่อนลงมือ** (kit อยู่ `/mnt/hermes-agent`) — ใช้ **CURRENT FORM** เท่านั้น (brief นี้เป็น system/mindset)
2. **ข้อเท็จจริงล็อกแล้ว ห้ามแก้:**
   - Bandura เสียชีวิต **26 กรกฎาคม 2021** (โน้ตเดิมบอก 26 ต.ค. = **ผิด** — ยืนยันแล้ว 5 แหล่ง: Stanford Report / NYT / Wikipedia / APS / Palo Alto Online)
   - Bobo doll experiment **1961** ที่ Stanford
   - 4 กระบวนการ: attention / retention / reproduction / motivation
   - reciprocal determinism
   - ถ้าจะเพิ่มข้อเท็จจริงใหม่ → ต้องยืนยัน ≥3 แหล่ง แล้วบันทึกแหล่งใน header ของหน้า
3. **ตรวจด้วย draft_battery.py ให้ PASS** รัน: `uv run --python 3.12 /mnt/hermes-agent/skills/content-pipeline/scripts/draft_battery.py <ไฟล์> --cut คับ`
   - เกณฑ์: "คุณ" = 0, quote ×2 (ใน Notion ใช้ tag form `<quote>` + `<b>` เพื่อให้ bold รอด), ความยาวแนว 500–680 wc-w, H1×1 / H3×1, จังหวะย่อหน้าคั่น `.` ตามสเปก
4. **story seeds เป็นฉากเรียบเรียง ยังไม่ยืนยันจริง** — คง flag "รอยืนยันเจ้าของก่อน publish" ไว้ใน header ของหน้า ห้ามตัด
5. **Status คง `draft` ห้าม publish** — ห้ามแตะฐาน Adduckivity Content / publish master; ปิดโพสต์ด้วย night question (duck closer ยังไม่มีตัวอย่างยืนยันในไฟล์ประวัติรูปแบบ)
6. **แก้บนหน้าเดิม** ตาม pipeline (rewrite ในหน้าเดิม ไม่ทิ้งร่างเก่าแยกหน้า)

## เมื่อเสร็จ

- รายงาน Phon ในแชทของคุณ: สรุปสิ่งที่แก้ + ผล battery
- ส่ง `message_bot` กลับมาหา **Chief (cmwj2kqkfl1cdznjl9fxz39ik)** พร้อมผล battery — **Chief จะ re-verify (รัน battery บนหน้าจริง + เช็ค checklist) ก่อนปิดงาน** ไม่ผ่านจะสั่ง rewrite รอบถัดไป
