---
type: lesson
status: standing
first: "pair #54 (2026-10-19)"
recurrence: 8+ ครั้งติดกัน
---

# Paste import artifacts — ของที่ Notion import สร้างเอง

## ตระกูล artifact ที่เจอซ้ำ
- บรรทัด `> ` ว่างท้าย quote (ครั้งที่ 6+ — #54/#55/#56/#58/#63/#79)
- H1 ใน paste → ซ้ำกับ Name prop → strip ก่อน replace ([[pair-064]] pitfall 265)
- บรรทัดว่างของ paste → empty paragraph 41 บล็อก ([[pair-070]])
- bold ใน quote หลายบรรทัด import ไม่รอด (single-line รอด)

## กฎ
read-back ต้องสแกน empty paragraph + empty quote + H1 count ทุกครั้ง — กันตั้งแต่ import ไม่ใช่ไล่ลบทีหลัง
