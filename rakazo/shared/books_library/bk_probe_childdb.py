#!/usr/bin/env python3
"""probe: ทำไม query child db 404 ทั้งที่ GET database ยังได้ (read-only)"""
import os, json, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
DB = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'


def api(path, method='GET', body=None, ver='2022-06-28'):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        'https://api.notion.com/v1' + path, data=data, method=method,
        headers={'Authorization': 'Bearer ' + TOK, 'Notion-Version': ver,
                 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:250]
    except Exception as e:
        return 'ERR', str(e)


books = json.load(open('chapters2.json'))
sample = [b for b in books if b['book'].startswith('Rework')][0]
did = sample['db_id']
print('sample book :', sample['book'])
print('child db id :', did)
print()

for ver in ['2022-06-28', '2025-09-03']:
    print('--- Notion-Version', ver)
    for path, method, body in [
        ('/databases/%s' % did, 'GET', None),
        ('/databases/%s/query' % did, 'POST', {'page_size': 3}),
        ('/data_sources/%s/query' % did, 'POST', {'page_size': 3}),
    ]:
        st, d = api(path, method, body, ver)
        head = ''
        if isinstance(d, dict):
            head = d.get('message') or (('object=%s results=%d' % (d.get('object'), len(d.get('results', [])))) if d.get('object') else str(d)[:80])
            if 'data_sources' in d:
                head += ' data_sources=%s' % [x.get('id') for x in d['data_sources']]
        else:
            head = str(d)[:120]
        print('  %-40s %s %s' % (path[-38:], st, head))
    print()

print('=== top-level Books Library ===')
for ver in ['2022-06-28', '2025-09-03']:
    st, d = api('/databases/%s' % DB, 'GET', None, ver)
    if isinstance(d, dict):
        print(' ver', ver, 'GET db ->', st, 'data_sources=', [x.get('id') for x in d.get('data_sources', [])])
    else:
        print(' ver', ver, 'GET db ->', st, d)
    st, d = api('/databases/%s/query' % DB, 'POST', {'page_size': 3}, ver)
    print(' ver', ver, 'POST db/query ->', st, (d.get('message') if isinstance(d, dict) else str(d)[:100]))
    st, d = api('/data_sources/%s/query' % PDS, 'POST', {'page_size': 3}, ver)
    print(' ver', ver, 'POST ds/query ->', st, (d.get('message') if isinstance(d, dict) else str(d)[:100]))
