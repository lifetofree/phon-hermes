#!/bin/bash
# Quota recovery watcher — probes chain-head credentials (gemini + minimax); alerts on QUOTA_OUT -> OK transition.
# Chain (Phon, 21 Nov evening): gemini primary -> MiniMax fallback-1 -> glm -> Qwen. Fallback is automatic in Rakazo;
# this job only detects recovery and notifies (alert file -> alert-watch -> Hermes).
LOG="$HOME/rakazo-inbox/quota-watch.log"
ALERTS="$HOME/rakazo-inbox/alerts"
STATE="$HOME/rakazo-inbox/quota-state"
mkdir -p "$ALERTS" "$STATE"
KEY=$(grep -E '^ENCRYPTION_KEY=' "$HOME/rakazo/.env" | cut -d= -f2- | tr -d '"')

check() { # $1=credential_id $2=model $3=label
  local SID=$(docker exec -i rakazo-postgres-1 psql -U rakazo -d rakazo -At <<SQL
SELECT "secretId" FROM user_model_credentials WHERE id='$1'
SQL
)
  local CT=$(docker exec -i rakazo-postgres-1 psql -U rakazo -d rakazo -At <<SQL
SELECT ciphertext::text FROM secrets WHERE id='$SID'
SQL
)
  if [ -z "$CT" ]; then echo "$(date '+%F %T') $3: ERROR no ciphertext (SID=$SID)" >> "$LOG"; return; fi
  local OUT=$(docker exec -i -e K="$KEY" -e CRED="$SID" -e MODEL="$2" -e CT="$CT" rakazo-api-1 node - < "$HOME/hermes-agent/scripts/quota-probe.js" 2>/dev/null)
  echo "$(date '+%F %T') $3 probe: $OUT" >> "$LOG"
  local LAST=$(cat "$STATE/$3" 2>/dev/null || echo unknown)
  printf '%s' "$(echo "$OUT" | head -c 24)" > "$STATE/$3.new" && mv "$STATE/$3.new" "$STATE/$3"
  case "$LAST" in
    QUOTA_OUT*|AUTH_FAIL*|ERROR*|unknown)
      case "$OUT" in
        OK*) printf '{"source":"quota-watch","provider":"%s","event":"quota/credit recovered - chain active again","prev":"%s","at":"%s"}\n' "$3" "$LAST" "$(date -Iseconds)" > "$ALERTS/quota-$3-ok.json";;
      esac;;
  esac
}

check cmwotpsar04or07tnymbek1r5 "models/gemini-3.8-flash" gemini
check cmmmoaibebf6eaff9e25588 "MiniMax-M3.1-Flash" minimax
exit 0
