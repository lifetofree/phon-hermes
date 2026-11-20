#!/bin/bash
# backup-hermes-home.sh — weekly backup to GitHub (private repo hermes-home-backup)
# Scope (owner decisions 2026-11-20): secrets PLAIN in private repo (option B);
# state.db + rakazo appdata full tar = LOCAL ONLY (too big for GitHub);
# schedule: weekly Sun 03:00 via systemd user timer backup-hermes-home.timer
set -uo pipefail
TS=$(date +%Y%m%d-%H%M)
REPO=/home/lifetofree/backups/hermes-home
HM=/home/lifetofree/.hermes
LOG=/home/lifetofree/.hermes/logs/backup.log
LOC=/home/lifetofree/hermes/backups
GIT_ID=(-c user.name="Hermes backup" -c user.email="lifetofree@users.noreply.github.com")
log(){ echo "$(date '+%F %T') $*" >> "$LOG"; }
log "=== backup run $TS ==="

mkdir -p "$REPO" "$LOC/state-db" "$LOC/appdata"

# --- 1. hermes home -> github (exclude runtimes/caches/state.db) ---
STAGE="$REPO/hermes"
mkdir -p "$STAGE"
rsync -a --delete \
  --exclude 'hermes-agent' --exclude 'tools' --exclude 'cache' --exclude 'installs' \
  --exclude 'node' --exclude 'lsp' --exclude 'bin' --exclude 'logs' \
  --exclude 'models_dev_cache.json' --exclude 'state.db' --exclude 'state.db-wal' \
  --exclude 'state.db.bak.*' --exclude 'state.db.corrupt.*' --exclude 'gateway.sock' \
  --exclude 'audio_cache' --exclude 'image_cache' \
  --exclude 'profiles/*/audio_cache' --exclude 'profiles/*/cache' \
  "$HM/" "$STAGE/"
# strip embedded git repos so plugins/skills content is stored as real files (gitlinks store nothing)
find "$STAGE" -mindepth 2 -name ".git" \( -type d -o -type f \) -exec rm -rf {} + 2>/dev/null
log "hermes home rsync done"

# --- 2. state.db: LOCAL ONLY (sqlite online backup, keep 4) ---
if sqlite3 "$HM/state.db" ".backup '$LOC/state-db/state.db.$(date +%Y%m%d).bak'" 2>>"$LOG"; then
  log "state.db local backup OK"
  ls -1t "$LOC/state-db"/state.db.*.bak 2>/dev/null | tail -n +5 | xargs -r rm -f
else
  log "WARN: state.db backup FAILED"
fi

# --- 3. rakazo DB dump -> LOCAL dated (keep 3) + repo single latest file ---
mkdir -p "$REPO/rakazo" "$LOC/rakazo-db"
if docker exec rakazo-postgres-1 sh -c 'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' | gzip > "$LOC/rakazo-db/rakazo-db-$TS.sql.gz" 2>>"$LOG"; then
  log "rakazo pg_dump OK (local)"
  ls -1t "$LOC/rakazo-db"/rakazo-db-*.sql.gz | tail -n +4 | xargs -r rm -f
  cp "$LOC/rakazo-db/rakazo-db-$TS.sql.gz" "$REPO/rakazo/rakazo-db-latest.sql.gz"
  rm -f "$REPO/rakazo"/rakazo-db-20*.sql.gz
else
  log "WARN: rakazo pg_dump FAILED"
fi

# --- 4. rakazo appdata homes: LOCAL full tar (keep 2) + GITHUB selective bundle (keep 2) ---
if docker run --rm -v rakazo_appdata:/src:ro alpine sh -c 'tar -czf - -C /src homes' > "$LOC/appdata/homes-$TS.tar.gz" 2>>"$LOG"; then
  log "appdata full tar OK ($(du -h "$LOC/appdata/homes-$TS.tar.gz" | cut -f1))"
  ls -1t "$LOC/appdata"/homes-*.tar.gz | tail -n +3 | xargs -r rm -f
else
  log "WARN: appdata full tar FAILED"
fi
# github bundle: credentials (.gitconfig/.config/gh) + shared/ + work/ per home
docker run --rm -v rakazo_appdata:/src:ro alpine sh -c '
  cd /src || exit 1
  ARGS=""
  for h in homes/*; do
    [ -d "$h" ] || continue
    for p in "$h/.gitconfig" "$h/.config/gh" "$h/.git-credentials" "$h/shared" "$h/work"; do
      [ -e "$p" ] && ARGS="$ARGS \"$p\""
    done
  done
  [ -n "$ARGS" ] && eval tar -czf - $ARGS
' > "$REPO/rakazo/bot-home-essential-$TS.tar.gz" 2>>"$LOG"
ls -1t "$REPO/rakazo"/bot-home-essential-*.tar.gz | tail -n +3 | xargs -r rm -f
log "appdata github bundle OK"

# --- 5. home extras -> github ---
mkdir -p "$REPO/home-extras"
for d in duck-os notes scripts rakazo rakazo-inbox; do
  [ -e "/home/lifetofree/$d" ] && rsync -a --delete "/home/lifetofree/$d" "$REPO/home-extras/"
done
log "home extras rsync done"

# --- 6. keep README in sync, commit + push ---
cp /home/lifetofree/hermes-agent/BACKUP.md "$REPO/README.md" 2>>"$LOG"
cd "$REPO"
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  if git "${GIT_ID[@]}" commit -q -m "backup $TS"; then
    git pull --rebase -q origin main 2>>"$LOG" || true
    if git push -q origin main 2>>"$LOG"; then
      log "git push OK"
    else
      log "WARN: git push FAILED"
    fi
  fi
else
  log "no changes to commit"
fi
log "=== backup run end $TS ==="
