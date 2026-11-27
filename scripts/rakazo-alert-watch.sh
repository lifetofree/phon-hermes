#!/usr/bin/env bash
# rakazo-alert-watch — poll alerts written by Stall Watcher (Rakazo bot)
# Empty output = silent (cron delivers nothing). Alert found = report + my own host-side verification.
ALERTS="$HOME/rakazo-inbox/alerts"
DONE="$HOME/rakazo-inbox/alerts-processed"
mkdir -p "$DONE"
shopt -s nullglob
files=("$ALERTS"/*.json)
[ ${#files[@]} -eq 0 ] && exit 0

# นโยบายเจ้าของ (27 พ.ย.): error/warning → Telegram DM เท่านั้น
# info/ok/status (รายงานปกติ) → ไม่ส่ง Telegram (ดูสถานะรวมใน thread ของ Stall Watcher ใน Rakazo)
is_error() { python3 -c "
import json,sys
try:
    s=json.load(open(sys.argv[1])).get('severity','').lower()
    sys.exit(0 if s in ('error','warning','critical') else 1)
except Exception: sys.exit(0)" "$1"; }

H=$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 http://127.0.0.1:8080/health)
if [ "$H" = "200" ]; then
  VERDICT="ตรวจยืนยันจาก host: llama-server ตอบ 200 ปกติตอนนี้ (alert อาจเก่า หรือ systemd Restart=on-failure ฟื้นแล้ว)"
else
  VERDICT="ตรวจยืนยันจาก host: llama-server DOWN จริง (health=$H) — systemd กำลัง retry เอง; ถ้ายัง down เกิน 10 นาที ต้องพิจารณา restart ด้วยมือ (รออนุมัติพร)"
fi

OUT=""
SKIPPED=0
ERRCOUNT=0
for f in "${files[@]}"; do
  if ! is_error "$f"; then
    SKIPPED=$((SKIPPED+1))
    mv "$f" "$DONE/$(basename "$f")"
    continue
  fi
  ERRCOUNT=$((ERRCOUNT+1))
  OUT+=$'\n'"— $(basename "$f")"
  OUT+=$'\n'"  $(python3 -c "import json,sys;d=json.load(open(sys.argv[1]));print('severity:',d.get('severity'),'| check:',d.get('check'),'| detail:',json.dumps(d.get('detail'),ensure_ascii=False))" "$f" 2>/dev/null || echo '(parse fail — ดูไฟล์ใน alerts-processed)')"
  mv "$f" "$DONE/$(basename "$f")"
done
if [ "$ERRCOUNT" -eq 0 ]; then
  # มีแต่รายงานสถานะปกติ → เงียบ (สถานะรวมอยู่ใน Rakazo)
  exit 0
fi
OUT="🚨 Stall Watcher แจ้ง — พบ ${ERRCOUNT} alert"$'\n'"$OUT"
if [ "$SKIPPED" -gt 0 ]; then
  OUT+=$'\n'"(ข้ามรายงานสถานะปกติ $SKIPPED ไฟล์ — ไม่ส่ง Telegram ตามนโยบาย)"
fi
OUT+=$'\n'"$VERDICT"
printf '%s\n' "$OUT"
