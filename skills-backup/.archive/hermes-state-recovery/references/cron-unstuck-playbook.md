# Cron Unstuck Playbook (verified 2026-09-01)

Incident: `~/.hermes/state.db` corruption (~18:28) killed a cron job fire mid-flight with "disk I/O error". The job (`daily-foreign-news`) never ran again: `last_run_at: null`, ticker alive, no errors at fire time. Root cause: orphaned `fire_claim` in jobs.json + stale `.fire-*.lock`.

## Evidence pattern

```
# jobs.json
"fire_claim": {"at": "2026-09-01T18:28:08...+07:00", "by": "PHON-SERVER:133660:<uuid>"}

# errors.log at the same timestamp
WARNING ... Tool cronjob returned error: {"error": "disk I/O error"}

# ps -p 133660 → no such process; fuser on the .fire lock → held by nothing
```

## Repair script (run as the Hermes user)

```python
import json, fcntl, os
base = os.path.expanduser("~/.hermes/cron")
lock = open(os.path.join(base, ".jobs.lock"), "w")
fcntl.flock(lock, fcntl.LOCK_EX)
jp = os.path.join(base, "jobs.json")
data = json.load(open(jp))
for job in data["jobs"]:
    if job.get("fire_claim") and job["id"] == "<JOB_ID>":
        job["fire_claim"] = None
        job["state"] = "scheduled"
with open(jp, "w") as f:
    json.dump(data, f, indent=2)
for f in os.listdir(base):
    if f.startswith(".fire-") and f.endswith(".lock"):
        os.remove(os.path.join(base, f))
fcntl.flock(lock, fcntl.LOCK_UN)
```

(Clear claims only for jobs whose claiming PID is verified dead. If ANY live process holds a fire lock via `fuser`, do not remove that lock.)

## Verification chain

1. `cronjob(action='run', job_id=...)` → returns `executed: true` + `delegation_id`.
2. While running: `sqlite3 ~/.hermes/cron/executions.db "select id,status,started_at from executions order by rowid desc limit 1;"` → `running`.
3. After: same query → `completed`; jobs.json `last_status` → `ok`; output file at `~/.hermes/cron/output/<job_id>/<ts>.md` contains the job's final response.
4. For Telegram delivery: `last_delivery_error` stays null; the async delegation completion message also reports the delivery target. Final proof = message visible on the platform.

Timing reference: a web-research digest job took ~2.5 min end-to-end; don't declare failure before then.
