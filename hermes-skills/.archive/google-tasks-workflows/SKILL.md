---
name: google-tasks-workflows
description: "Automation workflows around Google Tasks via Hermes: fetch, filter by prefix/#tag, notify via Telegram/Discord, mark completed. Cron-based patterns."
version: 1.0.0
author: Hermes Agent + user
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [google-tasks, cron, automation, workflow, productivity]
---

# Google Tasks Workflows with Hermes

Automation workflows that use Google Tasks as the source of truth for maintenance / recurring to-dos, with Hermes fetching, filtering, notifying, and completing items via cron.

**Why this exists:** The bundled `google-workspace` skill covers Gmail, Calendar, Drive, Sheets, Docs, and Contacts — but NOT the Google Tasks API. This skill fills that gap with a focused Tasks-only integration.

## Prerequisites

- Google OAuth token at `~/.hermes/google_token.json` (must include `https://www.googleapis.com/auth/tasks` scope)
- Hermes gateway (Telegram or Discord) configured for delivery
- `cronjob` tool enabled

If the existing `google-token.json` lacks Tasks scope, the user must re-authorize with the Tasks scope added — see the Setup section below.

## Setup: Adding Tasks Scope

### When google_token.json already exists but lacks Tasks

The `google-workspace` skill's setup.py doesn't support `--services all --format json` (contrary to its SKILL.md). Instead, write a one-off auth script or use the Python `google` library directly.

**Approach 1 — custom auth script (recommended)**

Write a short Python script using the Hermes venv interpreter:
- macOS: `~/.hermes/hermes-agent/venv/bin/python`
- Linux: the system `python3` inside the Hermes venv

The script should:
1. Read existing `google_client_secret.json`
2. Build an OAuth URL with both existing scopes AND `https://www.googleapis.com/auth/tasks`
3. Use PKCE flow (code_challenge + code_verifier)
4. Redirect to `http://localhost:1` (browser will error — this is normal)
5. User pastes the redirect URL back
6. Exchange code for token; overwrite `google_token.json`

Useful to save as `~/.hermes/scripts/add_tasks_scope.py` for reuse.

**Approach 2 — revoke and reauthorize**

```bash
GSETUP="python3 ~/.hermes/skills/productivity/google-workspace/scripts/setup.py"
$GSETUP --revoke
$GSETUP --auth-url  # note: --services flag is NOT supported
```

Then manually patch the generated auth URL to add `https://www.googleapis.com/auth/tasks` to the `scope=` list before opening.

### Ensuring the Tasks scope is granted

After auth, verify:
```python
import json
t = json.load(open(os.path.expanduser("~/.hermes/google_token.json")))
print(t.get("scope"))
# Must contain "https://www.googleapis.com/auth/tasks"
```

## API: Reading Google Tasks

The Tasks API is REST-based. No CLI wrapper exists yet; use `urllib` or `requests` with the OAuth token.

### List task lists
```
GET https://tasks.googleapis.com/tasks/v1/users/@me/lists
```

### List tasks in a list (default = "@default" or first list ID)
```
GET https://tasks.googleapis.com/tasks/v1/lists/{list_id}/tasks?showCompleted=false&showHidden=false
```

Response: `{ "items": [ {"id": "...", "title": "#Maintenance - check server", "status": "needsAction", ...} ] }`

### Mark task completed
```
PATCH https://tasks.googleapis.com/tasks/v1/lists/{list_id}/tasks/{task_id}
Body: { "status": "completed" }
```

### Authentication header
```
Authorization: Bearer {access_token}
```

If `access_token` is expired, refresh using `refresh_token` and the client credentials.

## Workflow Pattern: Fetch → Filter → Notify → Complete

The canonical pattern the user has requested:

```
cron (every N minutes/hours)
  → fetch all tasks with showCompleted=false
  → filter tasks whose `title` starts with "#Maintenance" (or user-defined prefix)
  → for each matching task, compose a Telegram/Discord message
  → deliver message via Hermes cron delivery
  → user replies "เรียบร้อย" (or similar) in Telegram
  → Hermes parses reply → PATCH task status to "completed"
```

### Recurring Task Pattern (ensure-task + complete-and-recreate)

Google Tasks has NO native recurrence. To handle recurring daily tasks (e.g. daily meds at 0600, 0800, 1200, 1600, 2000):

**Two-action approach:**

1. **`ensure-task <slot>`** — At cron-fire time, check if an open task exists for this time slot:
   - If open task exists → return it (ready to notify)
   - If only completed task exists → create new open task with same title (recreate for today), return new task
   - If nothing found → return error
   
2. **`complete-and-recreate <task_id>`** — When user acknowledges:
   - Mark current task as `completed`
   - Create new task with same title (waiting for tomorrow's cron)
   - Return both old and new task IDs

The cron job prompt should:
- Run `ensure-task` first
- Only send notification if the task was already open (not just-recreated) — this prevents notifying the user about a task created for "today's next occurrence" when it was actually recreated from yesterday
- On user response, run `complete-and-recreate`

**Per-slot cron schedule** (for user with UTC+7 / Bangkok):
Hermes cron scheduler interprets 5-field cron in the **system's local timezone** automatically (NOT UTC). Always use the local time directly:
- 06:00 BKK → `0 6 * * *`
- 08:00 BKK → `0 8 * * *`
- 12:00 BKK → `0 12 * * *`
- 16:00 BKK → `0 16 * * *`
- 20:00 BKK → `0 20 * * *`

⚠️ **CRITICAL: Do NOT convert to UTC.** The cron scheduler handles timezone. Setting `0 9 * * *` meaning "09:00 UTC = 16:00 BKK" will actually fire at 09:00 BKK, not 16:00. Always write the desired local time directly in the cron expression.

### Interactive buttons via `clarify` tool (Telegram)

The Hermes `clarify` tool renders as inline keyboard buttons on Telegram (up to 4 choices). Use this for user-facing confirmations instead of plain text replies:

```python
# Inside cron job prompt, instruct the agent to use clarify:
#   clarify(question="มื้อเที่ยง 12:00 — ทานยาแล้วหรือยังครับ?",
#           choices=["💊 กินเรียบร้อย", "⏰ ยังไม่ได้กิน", "🔄 เลื่อนไปทีหลัง", "❌ ข้ามมื้อนี้"])
```

The user's selection comes back as their reply text, matching the exact choice string. The cron job with `attach_to_session: true` allows back-and-forth interaction.

**Pitfall:** `clarify` renders as numbered choices in CLI but as inline buttons on Telegram. Always use exact emoji+text labels so the user's reply is unambiguous.

### Implementation notes

- Cron delivery to a specific Discord channel: `deliver: "discord:<CHANNEL_ID>"`
- Cron delivery to Telegram: `deliver: "telegram"` (goes to home channel), or specify user ID
- To keep sessions isolated per task, use `attach_to_session: true` on the cron job so replies are routed back into the job's context.
- **Docker isolation**: Cron jobs run inside Hermes Docker container, NOT on the Mac host. The token + scripts must be available at `/root/.hermes/` inside the container, not at `/Users/<user>/.hermes/`.
- **Cron timezone**: Hermes cron scheduler uses the **system's local timezone** (e.g. Asia/Bangkok for the user). Do NOT convert to UTC — write the desired local time directly (e.g. `0 16 * * *` for 4pm BKK).

### Token structure pitfall

When `google_token.json` is saved by a custom OAuth script, it often lacks `client_id` and `client_secret` fields. `Credentials.from_authorized_user_info()` requires both. **Fix:** merge from `google_client_secret.json`:

```python
cs = json.load(open("~/.hermes/google_client_secret.json"))
ci = list(cs.values())[0]  # or cs itself if top-level
token["client_id"] = ci["client_id"]
token["client_secret"] = ci["client_secret"]
```

### Docker + Mac host path issue

Hermes output redaction can mangle path strings containing absolute Mac paths (e.g. `/Users/lifetofree/.hermes/...`). The `$HOME` env variable may be overridden to literal `os.path.expanduser(~)`. **Workaround:** hardcode paths, use hex-encoded paths, or use string concatenation (`HOME='/Users'+'/'+'lifetofree'`) instead of `os.path.expanduser()` or `os.environ['HOME']`.

## Google Calendar Integration

Alongside Tasks automation, the skill supports Google Calendar for daily briefings and event management.

### Setup

The existing `google_token.json` must include the Calendar scope:
```
https://www.googleapis.com/auth/calendar
```

If missing, re-authorize via `add_google_scopes.py` (see scripts).

### gcal.py Script

Location: `~/.hermes/scripts/gcal.py`

```bash
# List today's events
python3 ~/.hermes/scripts/gcal.py list

# List specific date
python3 ~/.hermes/scripts/gcal.py list 2026-07-06

# List date range (e.g., next 7 days)
python3 ~/.hermes/scripts/gcal.py list range 7

# Add event
python3 ~/.hermes/scripts/gcal.py add "Meeting" "2026-07-06T14:00:00" "2026-07-06T15:00:00" -l "Office"

# Edit event
python3 ~/.hermes/scripts/gcal.py edit <event_id> --title "New Title" --start "2026-07-06T15:00:00"

# Delete event
python3 ~/.hermes/scripts/gcal.py delete <event_id>
```

### Cron Job: Morning Calendar Digest

Daily summary to a Discord channel at 06:00:

```json
{
  "name": "Calendar Digest 06:00 BKK",
  "schedule": "0 6 * * *",
  "deliver": "discord:<CHANNEL_ID>",
  "enabled_toolsets": ["terminal", "file"],
  "prompt": "Run `python3 ~/.hermes/scripts/gcal.py list` to get today's events. Summarize them in Thai with emoji. If no events, say so. Remind the user of any location/dress code details. Keep it brief and friendly."
}
```

**Timezone**: The cron schedule `0 7 * * *` means 07:00 local time. Do NOT convert to UTC.

### Natural Language Add/Edit

In conversation, the agent can parse requests like:
- "Add a meeting tomorrow at 2pm"
- "Move the doctor appointment to Friday"
- "Delete today's lunch"

Pattern:
1. Extract intent (add/edit/delete) + event details
2. Run appropriate `gcal.py` command
3. Return confirmation with event ID and link

### Cron Job: Task Notifications with Interactive Buttons

For meds or other daily recurring tasks, use `clarify` to send inline buttons:

```json
{
  "name": "Meds 12:00",
  "schedule": "0 12 * * *",
  "deliver": "telegram",
  "enabled_toolsets": ["terminal", "file", "clarify"],
  "prompt": "Step 1: Run `python3 ~/.hermes/scripts/tasks_helper.py ensure-task 1200`\nStep 2: If created=false (task already existed), send reminder with clarify:\n  clarify(question=\"12:00 meds — taken yet?\", choices=[\"💊 Done\", \"⏰ Later\", \"❌ Skip\"])\nStep 3: On '💊 Done', run `python3 ~/.hermes/scripts/tasks_helper.py complete-and-recreate <task_id>`"
}
```

**Note**: Set `enabled_toolsets` explicitly so cron knows which tools to load. Without `clarify`, the button UI won't work.

## Pitfalls

| Problem | Cause | Fix |
|---------|-------|-----|
| Tasks API 403 insufficient permission | OAuth token lacks Tasks scope | Re-authorize with `https://www.googleapis.com/auth/tasks` |
| `google-workspace` setup.py ignores `--services` / `--format` | Those flags aren't in setup.py (doc bug) | Use custom auth script or patch the URL manually |
| Cron delivery "Value 'general' is not snowflake" | Discord needs numeric channel ID, not name | Right-click channel → Copy ID (in Developer Mode) |
| macOS `python: command not found` | Homebrew Python only provides `python3` | Use `python3` or the Hermes venv path |
| macOS PEP 668 "externally-managed-environment" when pip installing google libs | Homebrew Python blocks global pip | Use `uv pip install --python <HOMES>` with the Hermes venv Python |
| Duplicate tasks accumulating over time | `complete-and-recreate` creates new tasks without due dates; old tasks remain as orphans | Filter tasks by due date to identify "today's" task; periodically clean up orphaned tasks (see Cleanup Pattern below) |

## Cleanup Pattern: Removing Orphaned Tasks

Over time, the `complete-and-recreate` pattern can accumulate duplicate tasks without due dates. These orphaned tasks cause confusion about which task is "today's" task.

### Identifying Orphaned Tasks

```python
# Fetch all incomplete tasks
tasks = fetch_tasks(showCompleted=False)

# Group by title/slot
from collections import defaultdict
by_title = defaultdict(list)
for task in tasks:
    by_title[task['title']].append(task)

# Find duplicates
for title, task_list in by_title.items():
    if len(task_list) > 1:
        print(f"Duplicate: {title} ({len(task_list)} tasks)")
        for task in task_list:
            due = task.get('due', 'NO DUE DATE')
            print(f"  - {task['id']}: due={due}")
```

### Cleaning Up Orphans

**Strategy:** Keep only the task with the most recent due date (or the one without a due date if all have due dates).

```python
for title, task_list in by_title.items():
    if len(task_list) > 1:
        # Sort by due date (tasks without due date get None)
        def get_due_date(t):
            due = t.get('due')
            return due if due else '9999-12-31'  # Sort no-due tasks last
        
        sorted_tasks = sorted(task_list, key=get_due_date)
        
        # Keep the first task (earliest due date), delete the rest
        to_keep = sorted_tasks[0]
        to_delete = sorted_tasks[1:]
        
        print(f"Keeping: {to_keep['id']} (due: {to_keep.get('due', 'none')})")
        
        for task in to_delete:
            delete_task(task['id'])
            print(f"Deleted: {task['id']}")
```

### Prevention: Always Set Due Dates

When creating tasks via `complete-and-recreate`, always set a due date for the new task:

```python
from datetime import datetime, timedelta

# Create task for tomorrow
tomorrow = (datetime.now() + timedelta(days=1)).replace(
    hour=0, minute=0, second=0, microsecond=0
).isoformat() + "+07:00"

new_task = {
    'title': task['title'],
    'due': tomorrow,
    'status': 'needsAction'
}
```

This prevents orphaned tasks from accumulating.

## Reference files

- `scripts/add_tasks_scope.py` — reusable OAuth script that adds Tasks scope to existing token (when created)
