---
name: google-tasks-api
description: "Manage Google Tasks (list, create, complete) via REST API + OAuth2."
version: 1.0.0
author: Nous Research
license: MIT
tags: [Google, Tasks, OAuth, API]
related_skills: [google-workspace]
metadata:
  hermes:
    tags: [Google, Tasks, OAuth, API]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [google-workspace]
---

# Google Tasks API

Manage Google Tasks — create task lists, list tasks, mark tasks completed, create new tasks — via the REST API with OAuth2.

## When to Use

- User wants to fetch/manage Google Tasks (the mobile/web app "Tasks")
- User wants to mark tasks as completed via automation
- User mentions "#Maintenance" prefix pattern for task filtering
- Complements `google-workspace` skill which covers Gmail/Calendar/Drive/Sheets/Docs but NOT Tasks

## Auth Requirements

**CRITICAL**: The `google-workspace` skill's `setup.py` does NOT support the `--services` flag. It generates a fixed scope URL. To add Tasks scope, you must either:

1. Re-authorize with Tasks scope added (custom OAuth script needed — see `references/oauth-setup.md`)
2. Use `--auth-url` alone (no extra args) and check if Tasks scope is included

Required OAuth scope: `https://www.googleapis.com/auth/tasks`

Other scopes (optional): `gmail.readonly gmail.send gmail.modify calendar drive contacts.readonly spreadsheets documents`

### Token Location

`~/.hermes/google_token.json`

Token file format: standard Google OAuth2 JSON with `access_token`, `refresh_token`, `client_id`, `client_secret`, `token_uri`.

## API Endpoints

Base URL: `https://tasks.googleapis.com/tasks/v1`

### List Task Lists

```
GET /users/@me/lists
```

Response: `{ "items": [{"id": "...", "title": "..."}, ...] }`

### List Tasks in a List

```
GET /tasklists/{tasklist}/tasks?showCompleted=false&showHidden=false&maxResults=100
```

Response: `{ "items": [{"id": "...", "title": "...", "status": "needsAction", "updated": "..."}, ...] }`

Filter for completed tasks: pass `showCompleted=true&showHidden=true`

### Mark Task Completed

```
PUT /tasklists/{tasklist}/tasks/{task}
Content-Type: application/json

{"status": "completed"}
```

Or use PATCH:
```
PATCH /tasklists/{tasklist}/tasks/{task}
Content-Type: application/json

{"status": "completed"}
```

### Create a Task

```
POST /tasklists/{tasklist}/tasks
Content-Type: application/json

{"title": "Task title", "status": "needsAction"}
```

## Reference Implementation (Python)

The working Python implementation is in `scripts/tasks_api.py`. Usage:

```bash
# List all task lists
python3 scripts/tasks_api.py lists

# List uncompleted tasks across all lists
python3 scripts/tasks_api.py list

# List tasks matching a prefix filter
python3 scripts/tasks_api.py list --prefix "#Maintenance"

# Mark a task as completed
python3 scripts/tasks_api.py complete TASK_ID [TASKLIST_ID]

# If tasklist_id is not provided, searches all lists for the TASK_ID
```

## Pitfalls

1. **Chrome blocks port 1** (ERR_UNSAFE_PORT). Use port 8080 with a local HTTPServer for OAuth redirect. See `references/oauth-setup.md` for the working flow.

2. **macOS `$HOME` can be corrupted**: Hermes shell overrides `$HOME` to literal string `os.path.expanduser(~)`. When writing Python scripts for the user to run, use `Path.home()` from pathlib or hardcode `/Users/USERNAME` — do NOT rely on `os.environ.get('HOME')`.

3. **Python interpreter on macOS**: `python` command not found. Must use `/Users/USERNAME/.hermes/hermes-agent/venv/bin/python3`.

4. **No `--services` flag**: The bundled `google-workspace/scripts/setup.py --auth-url` does NOT accept `--services` or `--format` arguments. Use it bare.

5. **Task list ID required for PATCH**: To mark a task completed, you need both `tasklist_id` and `task_id`. List tasklists first to find the right list, or iterate all lists to find which one contains the target task.

## Related Files

- `references/oauth-setup.md` — Working OAuth flow with Tasks scope (port 8080 workaround)
- `scripts/tasks_api.py` — CLI wrapper for Google Tasks API
