---
name: hermes-state-recovery
description: "Use when Hermes state.db corrupts, FTS5 breaks (JSONL fallback), or cron jobs never fire."
version: 1.0.0
license: MIT
---

# Hermes State Recovery

Recover Hermes Agent's local state (~/.hermes or $HERMES_HOME) after corruption or crashes. Symptoms this skill covers:

- `sqlite3 ~/.hermes/state.db "PRAGMA quick_check"` reports corruption, or any tool returns "database disk image is malformed" / "disk I/O error"
- Cron job shows `last_run_at: null` forever, never fires, or `cronjob(action='run')` silently does nothing
- Gateway was killed mid-operation and things behave oddly afterwards
- Gateway log repeats `Warning: SQLite session store unavailable, falling back to JSONL: fts5: error creating shadow table messages_fts_data: table 'messages_fts_data' already exists` (see references/fts5-orphaned-shadow-repair.md — restart alone does NOT fix it)

## Key facts about the layout

- `~/.hermes/state.db` — sessions/messages store (SQLite + FTS5). Cron jobs do NOT live here.
- `~/.hermes/cron/jobs.json` — cron job definitions AND runtime claims (`fire_claim` per job).
- `~/.hermes/cron/executions.db` — per-execution history (id, status, started/finished timestamps).
- `~/.hermes/cron/output/<job_id>/` — full run transcripts (prompt + final response) per execution.
- `~/.hermes/cron/.fire-<hash>.lock`, `.jobs.lock`, `.tick.lock` — advisory flock files; empty, harmless-looking, but a stale `.fire-*` lock plus a live-looking `fire_claim` can wedge a job.
- `~/.hermes/cron/ticker_heartbeat` / `ticker_last_success` — epoch floats; compare with `date +%s` to check the scheduler ticker is alive.

## Diagnosis sequence (cheap first)

1. `cronjob(action='list')` — check `last_run_at`, `last_status`, `last_fire_error`, `state`, `enabled`.
2. Read `jobs.json` for a non-null `fire_claim`. A claim older than minutes with a dead PID = orphaned claim; the scheduler thinks the job is mid-fire and will never retry.
3. Verify the claiming process: `ps -p <pid>` (PID is the middle field of `by: "HOST:PID:UUID"`). Dead process + surviving claim = stale.
4. Check `~/.hermes/logs/errors.log` and `gateway.log` around the claim timestamp for the original failure (e.g. "disk I/O error" during a state.db corruption window).
5. Confirm ticker health via heartbeat file timestamps.

## Repair procedure for a stuck cron job

See references/cron-unstuck-playbook.md for the full worked procedure (verified 2026-09-01). Summary:

1. Confirm the claim's PID is dead and no process holds the locks (`fuser`).
2. Take `.jobs.lock` with `fcntl.flock(LOCK_EX)` in Python, then edit `jobs.json`: set the stuck job's `fire_claim` to null and `state` to `"scheduled"`. Never edit jobs.json without the lock.
3. Delete the matching stale `.fire-*.lock` file.
4. Verify end-to-end with `cronjob(action='run', job_id=...)`, then confirm: execution row in `executions.db` reaches `completed`, `last_status` in jobs.json is `ok`, and the output file exists in `~/.hermes/cron/output/<job_id>/`.
5. For delivery-verified jobs (Telegram etc.), empty `last_delivery_error` means the gateway accepted the send; only the message appearing on the platform is final proof.

## FTS5 shadow tables orphaned (session store stuck on JSONL)

`integrity_check` is `ok`, `hermes sessions repair` says the DB "opens cleanly", yet the gateway keeps logging `falling back to JSONL: fts5: error creating shadow table ... already exists`. The vtable catalog row for `messages_fts` was lost while its shadow tables/objects survived — and the repair tool's health probe is blind to this exact state (it treats "no such table" as benign), so it refuses to act. Fix: back up, delete the orphaned `messages_fts%` catalog rows under `writable_schema`, let the next `SessionDB` open rebuild the FTS layer. Full verified procedure (2026-09-04): references/fts5-orphaned-shadow-repair.md. Note: the gateway reopens state.db periodically, so a disk-level fix usually self-heals a running gateway; restart is only needed to move a session out of JSONL. Restarting the gateway from inside the agent: send `SIGUSR1` to the gateway PID (graceful drain, restart after the current turn) — `systemctl`/`hermes gateway restart` are terminal-guard-blocked inside the gateway process.

## After ANY state.db corruption

Even after the DB itself is recovered, always check `~/.hermes/cron/jobs.json` for orphaned fire_claims — a fire that died during the corruption window leaves state that outlives the incident.

Also verify untracked files the user relies on survived — e.g. `~/hermes-agent/.env` (held NOTION_TOKEN) was lost in the 2026-09-01 incident and never restored (it was never in git). Recovered env dumps in `recovered_files/docs/*.txt` exist but secret values are redacted in them (only a masked prefix/suffix is shown), so they cannot be used to restore credentials. If a credential file is missing, tell the user it was lost and ask for a fresh token/secret — never mine the dumps for it.

## Pitfalls

- `executions.db` has no `delivered_at` column — check `.schema executions` before querying.
- The cron tool's `last_*` fields live in jobs.json, not executions.db; `cronjob(action='list')` reads both.
- Lock files are zero-byte; `ls -la` timestamps are your only aging signal.
