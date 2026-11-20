#!/bin/bash
# backup-freshness-check — cron watchdog (no_agent): outputs alert ONLY when stale; silent when OK
LAST=$(git -C /home/lifetofree/backups/hermes-home log -1 --format=%ct 2>/dev/null || echo 0)
NOW=$(date +%s)
AGE=$(( (NOW - LAST) / 86400 ))
if [ "$LAST" -eq 0 ]; then
  echo "🚨 Backup hermes-home-backup: ไม่พบ commit เลย — backup ยังไม่เคยรันสำเร็จ | ตรวจ: journalctl --user -u backup-hermes-home + ~/.hermes/logs/backup.log"
elif [ "$AGE" -ge 8 ]; then
  echo "🚨 Backup เกินกำหนด: commit ล่าสุดอายุ ${AGE} วัน ($(date -d "@$LAST" '+%F %T')) | ตรวจ: journalctl --user -u backup-hermes-home + ~/.hermes/logs/backup.log"
fi
# silent when fresh (weekly backup = อายุ <= 7 วัน)
