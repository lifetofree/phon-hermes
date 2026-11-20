"""Rollback: restore Tags to the original per-row values from books_tags_snapshot.json.

SAFE VERSION (fixed 19 Nov 2026):
  The old version PATCHed rows with the 193 original tag names. Notion AUTO-CREATES
  multi_select options on page PATCH, so the schema would end up with ~193 options
  instead of the current 76 -> the rollback would not restore a clean schema.
  Fix: FIRST reset the option list to the 193 original names (colors preserved from
  current schema where names still exist), THEN write per-row values.

Usage:
  python3 restore_tags.py          # dry-run: prints plan, writes nothing
  python3 restore_tags.py --apply  # performs the rollback
"""
import os, json, sys, time, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
BASE = 'https://api.notion.com/v1'
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'   # Books Library data source
APPLY = '--apply' in sys.argv

def api(path, data=None, method=None):
    req = urllib.request.Request(
        BASE + path,
        data=json.dumps(data).encode() if data is not None else None,
        headers={'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03',
                 'Content-Type': 'application/json'}, method=method)
    for a in range(10):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and a < 9:
                time.sleep(min(60, 3 * (2 ** a))); continue
            raise

snap = json.load(open('books_tags_snapshot.json'))
rows = snap['rows']
all_names = sorted({t for r in rows for t in r['tags']})
print('snapshot rows      :', len(rows))
print('distinct old tags  :', len(all_names))

ds = api('/data_sources/%s' % PDS)
cur_opts = ds['properties']['Tags']['multi_select']['options']
cur = {o['name']: o for o in cur_opts}
print('current options    :', len(cur_opts))

new_opts = []
for n in all_names:
    if n in cur:
        new_opts.append({'name': n, 'color': cur[n].get('color', 'default')})
    else:
        new_opts.append({'name': n, 'color': 'default'})
print('target options     :', len(new_opts))
print('mode               :', 'APPLY' if APPLY else 'DRY-RUN (no writes)')

if not APPLY:
    print('\nDRY-RUN done. Re-run with --apply to execute.')
    sys.exit(0)

# 1) reset option list to the 193 original names (idempotent endpoint test)
r = api('/data_sources/%s' % PDS,
        {'properties': {'Tags': {'multi_select': {'options': new_opts}}}}, 'PATCH')
after = r['properties']['Tags']['multi_select']['options']
print('  options after reset:', len(after))
time.sleep(0.5)

# 2) write per-row values
ok = fail = 0
for i, row in enumerate(rows):
    try:
        api('/pages/%s' % row['page_id'],
            {'properties': {'Tags': {'multi_select': [{'name': t} for t in row['tags']]}}}, 'PATCH')
        ok += 1
    except urllib.error.HTTPError as e:
        fail += 1
        print('FAIL', row['title'], e.code, flush=True)
    time.sleep(0.32)
    if i % 50 == 0:
        print('  ...%d/%d ok=%d fail=%d' % (i, len(rows), ok, fail), flush=True)
print('restore done: ok=%d fail=%d' % (ok, fail))
