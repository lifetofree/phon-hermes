#!/usr/bin/env python3
"""Google Tasks helper with ensure-task + complete-and-recreate for recurring tasks.

This script enables recurring task support on Google Tasks API (which has no native recurrence).
- ensure-task <HHMM>: Find/create open task for time slot
- complete-and-recreate <task_id>: Mark done + create next occurrence
- filter <HHMM>: Find open task by time slot pattern
- list: Show all open #Maintenance tasks
- complete <task_id>: Simple mark completed (no recreate)

Required env: Google OAuth token at ~/.hermes/google_token.json with Tasks scope.
Also requires ~/.hermes/google_client_secret.json for client_id/secret.
"""

import json, os, sys, urllib.request, urllib.parse, time
from pathlib import Path

TOKEN_PATH = Path("~/.hermes/google_token.json").expanduser()
CS_PATH = Path("~/.hermes/google_client_secret.json").expanduser()
LIST_ID = None  # Set to actual list ID or auto-detect
TOKEN_DATA = None


def load_json(p):
    with open(p) as f:
        return json.load(f)


def save_json(p, data):
    with open(p, 'w') as f:
        json.dump(data, f, indent=2)


def get_valid_token():
    """Get token with valid access_token, refreshing if needed."""
    global TOKEN_DATA
    if TOKEN_DATA is None:
        TOKEN_DATA = load_json(TOKEN_PATH)
        # Merge client_id/secret from client_secret file if missing
        if 'client_id' not in TOKEN_DATA or 'client_secret' not in TOKEN_DATA:
            cs = load_json(CS_PATH)
            # Handle both nested and flat formats
            ci = list(cs.values())[0] if 'installed' in cs or 'web' in cs else cs
            TOKEN_DATA['client_id'] = ci['client_id']
            TOKEN_DATA['client_secret'] = ci['client_secret']
            save_json(TOKEN_PATH, TOKEN_DATA)
    
    refreshed_at = TOKEN_DATA.get('_refreshed_at', 0)
    expires_in = TOKEN_DATA.get('expires_in', 3600)
    if time.time() > refreshed_at + expires_in - 300:  # 5min buffer
        # Refresh access token
        body = urllib.parse.urlencode({
            'client_id': TOKEN_DATA['client_id'],
            'client_secret': TOKEN_DATA['client_secret'],
            'refresh_token': TOKEN_DATA['refresh_token'],
            'grant_type': 'refresh_token',
        }).encode()
        req = urllib.request.Request('https://oauth2.googleapis.com/token',
                                    data=body, method='POST')
        with urllib.request.urlopen(req) as r:
            resp = json.loads(r.read())
        TOKEN_DATA['access_token'] = resp['access_token']
        TOKEN_DATA['expires_in'] = resp.get('expires_in', 3600)
        TOKEN_DATA['_refreshed_at'] = int(time.time())
        save_json(TOKEN_PATH, TOKEN_DATA)
    
    return TOKEN_DATA


def api_request(method, path, body=None):
    """Make API request to Google Tasks."""
    token_data = get_valid_token()
    url = f'https://tasks.googleapis.com{path}'
    headers = {'Authorization': f"Bearer {token_data['access_token']}"}
    if body:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(body).encode()
    else:
        data = None
    
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Google Tasks API error {e.code}: {e.read().decode()}")


def get_list_id():
    """Get task list ID (auto-detect if not set)."""
    global LIST_ID
    if LIST_ID:
        return LIST_ID
    result = api_request('GET', '/tasks/v1/users/@me/lists')
    if result.get('items'):
        LIST_ID = result['items'][0]['id']
        return LIST_ID
    raise RuntimeError("No task lists found")


def list_tasks(show_completed=False, show_hidden=False):
    """List tasks from default list."""
    list_id = get_list_id()
    params = urllib.parse.urlencode({
        'showCompleted': str(show_completed).lower(),
        'showHidden': str(show_hidden).lower(),
        'maxResults': 100
    })
    result = api_request('GET', f'/tasks/v1/lists/{list_id}/tasks?{params}')
    return result.get('items', [])


def find_task_by_slot(tasks, slot):
    """Find task matching time slot pattern #Maintenance(HHMM) or #Maintenance:(HHMM)."""
    for task in tasks:
        title = task.get('title', '')
        if f'#Maintenance({slot})' in title or f'#Maintenance:({slot})' in title:
            return task
    return None


def create_task(title):
    """Create new task in default list."""
    list_id = get_list_id()
    return api_request('POST', f'/tasks/v1/lists/{list_id}/tasks',
                      {'title': title, 'status': 'needsAction'})


def update_task(task_id, updates):
    """Update task (mark completed, etc)."""
    list_id = get_list_id()
    return api_request('PATCH', f'/tasks/v1/lists/{list_id}/tasks/{task_id}', updates)


def ensure_task(slot):
    """Ensure open task exists for time slot. Creates if needed, else returns existing.
    
    Returns: {"id": "<task_id>", "title": "<title>", "created": <bool>}
    """
    # 1. Check for open task
    open_tasks = list_tasks(show_completed=False)
    task = find_task_by_slot(open_tasks, slot)
    if task:
        return {'id': task['id'], 'title': task['title'], 'created': False}
    
    # 2. Check completed task (to get title for recreation)
    closed_tasks = list_tasks(show_completed=True, show_hidden=True)
    closed_task = find_task_by_slot(closed_tasks, slot)
    if closed_task:
        # Recreate with same title
        new_task = create_task(closed_task['title'])
        return {'id': new_task['id'], 'title': new_task['title'], 'created': True,
                'recreated_from': closed_task['id']}
    
    # 3. No task found
    raise RuntimeError(f"No task found with slot {slot} (neither open nor completed)")


def complete_and_recreate(task_id):
    """Mark task completed and create next occurrence with same title.
    
    Returns: {"old_id": ..., "new_id": ..., "title": ...}
    """
    list_id = get_list_id()
    # Get current task to read title
    task = api_request('GET', f'/tasks/v1/lists/{list_id}/tasks/{task_id}')
    title = task['title']
    
    # Mark completed
    update_task(task_id, {'status': 'completed'})
    
    # Create next occurrence
    new_task = create_task(title)
    
    return {
        'old_id': task_id,
        'new_id': new_task['id'],
        'title': title
    }


def complete_simple(task_id):
    """Mark task completed without recreation."""
    update_task(task_id, {'status': 'completed'})
    return {'completed': task_id}


def filter_by_slot(slot):
    """Return all open tasks #Maintenance(<slot>)."""
    tasks = list_tasks(show_completed=False)
    task = find_task_by_slot(tasks, slot)
    return [task] if task else []


def list_maintenance_tasks():
    """Return all open tasks starting with #Maintenance."""
    tasks = list_tasks(show_completed=False)
    return [t for t in tasks if t.get('title', '').startswith('#Maintenance')]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: tasks_helper.py <command> [args...]')
        print('Commands: ensure-task <HHMM>, complete-and-recreate <id>,')
        print('          complete <id>, filter <HHMM>, list')
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    try:
        if cmd == 'ensure-task':
            if len(sys.argv) < 3:
                print('Usage: ensure-task <HHMM>', file=sys.stderr)
                sys.exit(1)
            result = ensure_task(sys.argv[2])
            print(json.dumps(result, indent=2))
        
        elif cmd == 'complete-and-recreate':
            if len(sys.argv) < 3:
                print('Usage: complete-and-recreate <task_id>', file=sys.stderr)
                sys.exit(1)
            result = complete_and_recreate(sys.argv[2])
            print(json.dumps(result, indent=2))
        
        elif cmd == 'complete':
            if len(sys.argv) < 3:
                print('Usage: complete <task_id>', file=sys.stderr)
                sys.exit(1)
            result = complete_simple(sys.argv[2])
            print(json.dumps(result, indent=2))
        
        elif cmd == 'filter':
            if len(sys.argv) < 3:
                print('Usage: filter <HHMM>', file=sys.stderr)
                sys.exit(1)
            result = filter_by_slot(sys.argv[2])
            print(json.dumps(result, indent=2, ensure_ascii=False))
        
        elif cmd == 'list':
            result = list_maintenance_tasks()
            print(json.dumps(result, indent=2, ensure_ascii=False))
        
        else:
            print(f'Unknown command: {cmd}', file=sys.stderr)
            sys.exit(1)
    
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
