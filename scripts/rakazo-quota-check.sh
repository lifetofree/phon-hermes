#!/bin/bash
# Quota recovery watcher — probes the PRIMARY chain credential; alerts when quota comes back.
# Chain (Phon, 21 Nov): MiniMax primary -> gemini -> glm -> Qwen. Fallback is automatic in Rakazo;
# this job only detects "quota back" transition and notifies (alert file -> alert-watch -> Hermes).
LOG="$HOME/rakazo-inbox/quota-watch.log"
ALERTS="$HOME/rakazo-inbox/alerts"
STATE="$HOME/rakazo-inbox/quota-state"
mkdir -p "$ALERTS" "$STATE"
KEY=$(grep -E '^ENCRYPTION_KEY=' "$HOME/rakazo/.env" | cut -d= -f2- | tr -d '"' )
CT=$(docker exec -i rakazo-postgres-1 psql -U rakazo -d rakazo -At -c "SELECT ciphertext::text FROM secrets WHERE id='8b0e3f24debe16934c5e6c7d'" 2>/dev/null)
[ -z "$CT" ] && { echo "$(date '+%F %T') ERROR: no ciphertext for minimax cred" >> "$LOG"; exit 1; }
OUT=$(docker exec -i -e K="$KEY" -e CRED="8b0e3f24debe16934c5e6c7d" -e MODEL="MiniMax-M3.1-Flash" -e CT="$CT" rakazo-api-1 node - < "$HOME/hermes-agent/scripts/quota-probe.js" 2>/dev/null)
echo "$(date '+%F %T') minimax probe: $OUT" >> "$LOG"
LAST=$(cat "$STATE/minimax" 2>/dev/null || echo unknown)
echo "$OUT" | head -c 24 > "$STATE/minimax.new" && mv "$STATE/minimax.new" "$STATE/minimax"
case "$LAST" in
  QUOTA_OUT|AUTH_FAIL|ERROR*|unknown)
    case "$OUT" in
      OK*) printf '{"source":"quota-watch","provider":"MiniMax-M3.1-Flash","event":"quota recovered - chain head active again","prev":"%s","at":"%s"}\n' "$LAST" "$(date -Iseconds)" > "$ALERTS/quota-minimax-ok.json";;
    esac;;
esac
exit 0
