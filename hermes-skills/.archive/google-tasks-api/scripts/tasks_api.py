#!/usr/bin/env python3
"""
Google Tasks API CLI wrapper.
Usage:
  python3 tasks_api.py lists                          # list task lists
  python3 tasks_api.py list                           # list uncompleted tasks across all lists
  python3 tasks_api.py list --prefix "#Maintenance"   # filter by prefix
  python3 tasks_api.py complete TASK_ID [TASKLIST_ID] # mark task completed
"""

import json
import sys
from pathlib import Path

try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request as GRequest
    from googleapiclient.discovery import build
except ImportError as e:
    print(f"ERROR: Missing dependency. Install with:\n"
          f"  pip install google-api-python-client google-auth-oauthlib google-auth\n"
          f"Detail: {e}", file=sys.stderr)
    sys.exit(1)

HERMES_DIR = Path.home() / '.hermes'
TOKEN_PATH = HERMES_DIR / 'google_token.json'


def get_service():
    if not TOKEN_PATH.exists():
        print(f"ERROR: Token file not found at {TOKEN_PATH}", file=sys.stderr)
        print("Run OAuth setup first. See skill: google-tasks-api", file=sys.stderr)
        sys.exit(1)

    with open(TOKEN_PATH) as f:
        info = json.load(f)

    creds = Credentials.from_authorized_user_info(info)

    if creds.expired and creds.refresh_token:
        creds.refresh(GRequest())
        # Update token file for next time
        info['token'] = creds.token
        with open(TOKEN_PATH, 'w') as f:
            json.dump(info, f)

    return build('tasks', 'v1', credentials=creds)


def cmd_lists(service):
    result = service.tasklists().list(maxResults=100).execute()
    items = result.get('items', [])
    print(f"Task lists ({len(items)}):")
    for item in items:
        print(f"  [{item['id']}] {item['title']}")
    return items


def cmd_list(service, prefix=None):
    lists = service.tasklists().list(maxResults=100).execute().get('items', [])
    found = []
    for tasklist in lists:
        result = service.tasks().list(
            tasklist=tasklist['id'],
            showCompleted=True,
            showHidden=True,
            maxResults=100
        ).execute()
        items = result.get('items', [])
        if prefix:
            items = [t for t in items if t.get('title', '').startswith(prefix) and t.get('status') != 'completed']
        for t in items:
            found.append({
                'id': t['id'],
                'tasklist_id': tasklist['id'],
                'tasklist_title': tasklist['title'],
                'title': t.get('title', ''),
                'status': t.get('status', 'needsAction'),
                'updated': t.get('updated', ''),
            })
    print(json.dumps(found, ensure_ascii=False, indent=2))
    print(f"\nTotal: {len(found)} task(s)")
    return found


def cmd_complete(service, task_id, tasklist_id=None):
    if not tasklist_id:
        # Search all lists for this task
        lists = service.tasklists().list(maxResults=100).execute().get('items', [])
        for tasklist in lists:
            try:
                service.tasks().update(
                    tasklist=tasklist['id'],
                    task=task_id,
                    body={'status': 'completed'}
                ).execute()
                print(f"✅ Task {task_id} marked as completed (list: '{tasklist['title']}')")
                return
            except Exception:
                continue
        print(f"ERROR: Task {task_id} not found in any list", file=sys.stderr)
        sys.exit(1)
    else:
        service.tasks().update(
            tasklist=tasklist_id,
            task=task_id,
            body={'status': 'completed'}
        ).execute()
        print(f"✅ Task {task_id} marked as completed")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    service = get_service()
    command = sys.argv[1]

    if command == 'lists':
        cmd_lists(service)
    elif command == 'list':
        prefix = None
        if '--prefix' in sys.argv:
            idx = sys.argv.index('--prefix')
            if idx + 1 < len(sys.argv):
                prefix = sys.argv[idx + 1]
        cmd_list(service, prefix=prefix)
    elif command == 'complete':
        task_id = sys.argv[2] if len(sys.argv) > 2 else None
        tasklist_id = sys.argv[3] if len(sys.argv) > 3 else None
        if not task_id:
            print("ERROR: TASK_ID required", file=sys.stderr)
            sys.exit(1)
        cmd_complete(service, task_id, tasklist_id)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()
