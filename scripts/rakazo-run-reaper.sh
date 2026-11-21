#!/bin/bash
# Rakazo Run Reaper — clears orphaned 'running' runs whose lease is dead.
# Why: a bot with a stuck 'running' run can't start queued runs (slot held) — seen 20 & 21 Nov 2026.
# Rule: clear ONLY when lease expired >10min (or lease NULL and started >2h). Never touches queued/active runs.
LOG="$HOME/rakazo-inbox/reaper.log"
ALERTS="$HOME/rakazo-inbox/alerts"
mkdir -p "$ALERTS"
PSQL="docker exec -i rakazo-postgres-1 psql -U rakazo -d rakazo -At"
ROWS=$($PSQL -c "SELECT id||'|'||\"botId\"||'|'||coalesce(\"leaseExpiresAt\"::text,'none')||'|'||coalesce(extract(epoch from now()-\"startedAt\")::int,0) FROM runs WHERE status='running' AND ((\"leaseExpiresAt\" IS NOT NULL AND \"leaseExpiresAt\" < now() - interval '10 minutes') OR (\"leaseExpiresAt\" IS NULL AND \"startedAt\" < now() - interval '2 hours'))" 2>>"$LOG")
[ -z "$ROWS" ] && exit 0
while IFS='|' read -r RID BOTID LEASE AGE; do
  [ -z "$RID" ] && continue
  $PSQL -c "UPDATE runs SET status='failed', error='auto-reaper: lease dead — orphaned run was holding the bot slot', \"completedAt\"=now(), \"leaseOwner\"=NULL, \"leaseExpiresAt\"=NULL, \"updatedAt\"=now() WHERE id='$RID' AND status='running';" >/dev/null 2>>"$LOG"
  echo "$(date '+%F %T') cleared $RID bot=$BOTID lease_expired=$LEASE age=${AGE}s" >> "$LOG"
  printf '{"source":"run-reaper","run_id":"%s","bot_id":"%s","action":"cleared orphaned running run (lease dead)","lease_expired_at":"%s","age_seconds":%s,"at":"%s"}\n' "$RID" "$BOTID" "$LEASE" "$AGE" "$(date -Iseconds)" > "$ALERTS/reaper-$RID.json"
done <<< "$ROWS"
