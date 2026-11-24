#!/bin/bash
# rakazo-context-monitor.sh — ตรวจขนาด context ของ thread ทุกบอทใน Rakazo
# ถ้า thread ใหญ่เกินเพดาน: backup ข้อความเก่า → ลบเหลือ 40 ข้อความล่าสุด (clear context)
# ทุก thread ที่ trim จะถูกบันทึก alert ลง ~/rakazo-inbox/alerts/context-trim.log
# cron: */10 * * * *  (ติดตั้ง 23 พ.ย. 2026 — ตามสั่ง Phon หลัง Chief context เต็ม)
set -u
ARCHIVE_DIR="/home/lifetofree/rakazo-inbox/backups/thread-archive"
ALERT_LOG="/home/lifetofree/rakazo-inbox/alerts/context-trim.log"
MAX_KB=1200      # เพดานขนาด thread (KB ของ blocks text)
MAX_MSGS=800     # เพดานจำนวนข้อความ
KEEP=40          # จำนวนข้อความล่าสุดที่เก็บไว้
mkdir -p "$ARCHIVE_DIR" "$(dirname "$ALERT_LOG")"

# หา thread ที่เกินเพดาน (thread ของบอทเท่านั้น)
OVER=$(docker exec rakazo-postgres-1 psql -U rakazo -d rakazo -t -A -F'|' -c "
SELECT t.id, b.name, count(m.id), round(sum(octet_length(m.blocks::text))/1024.0)
FROM threads t JOIN bots b ON b.id = t.\"botId\"
LEFT JOIN messages m ON m.\"threadId\" = t.id
GROUP BY t.id, b.name
HAVING sum(octet_length(m.blocks::text))/1024.0 > $MAX_KB OR count(m.id) > $MAX_MSGS")

if [ -z "$OVER" ]; then
  exit 0
fi

STAMP=$(date +%Y%m%d-%H%M%S)
echo "$STAMP === context trim run ===" >> "$ALERT_LOG"

echo "$OVER" | while IFS='|' read -r TID BNAME MSGS KB; do
  [ -z "$TID" ] && continue
  echo "[$STAMP] TRIM thread=$TID bot=$BNAME msgs=$MSGS size=${KB}KB (เกินเพดาน — Chief context เต็มก่อนหน้านี้)" >> "$ALERT_LOG"
  # 1) backup ข้อความที่จะลบ (ทุกอันยกเว้น 40 ล่าสุด) เป็น JSON
  docker exec rakazo-postgres-1 psql -U rakazo -d rakazo -t -A -c "
    SELECT COALESCE(json_agg(row_to_json(d)), '[]')
    FROM (SELECT * FROM messages WHERE \"threadId\"='$TID'
          ORDER BY \"createdAt\" DESC OFFSET $KEEP) d" \
    | gzip > "$ARCHIVE_DIR/${TID}_${STAMP}.json.gz"
  # 2) ลบ (เก็บ 40 ล่าสุด)
  docker exec rakazo-postgres-1 psql -U rakazo -d rakazo -c "
    DELETE FROM messages WHERE id IN (
      SELECT id FROM messages WHERE \"threadId\"='$TID'
      ORDER BY \"createdAt\" DESC OFFSET $KEEP)" >/dev/null 2>&1
  AFTER=$(docker exec rakazo-postgres-1 psql -U rakazo -d rakazo -t -A -c "
    SELECT count(*) || ' msgs / ' || round(coalesce(sum(octet_length(blocks::text)),0)/1024.0) || 'KB'
    FROM messages WHERE \"threadId\"='$TID'")
  echo "[$STAMP]   → after: $AFTER (backup: ${TID}_${STAMP}.json.gz)" >> "$ALERT_LOG"
done

echo "$STAMP === done ===" >> "$ALERT_LOG"
exit 0
