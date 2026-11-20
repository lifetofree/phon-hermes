#!/usr/bin/env python3
"""probe 2: query child db ผ่าน data_source id (read-only)"""
import os, json, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']


def api(path, method='GET', body=None, ver='2025-09-03'):
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
tot = 0
ok = 0
for b in books[:6]:
    did = b['db_id']
    st, d = api('/databases/%s' % did)
    dss = d.get('data_sources') or [] if isinstance(d, dict) else []
    dsid = dss[0]['id'] if dss else None
    print('%-44s db=%s ds=%s' % (b['book'][:42], did[:8], (dsid or '-')[:8]))
    for cand in ([dsid] if dsid else []) + [did]:
        st2, d2 = api('/data_sources/%s/query' % cand, 'POST', {'page_size': 100})
        if st2 == 200:
            print('    ds/query %s -> 200 rows=%d' % (cand[:8], len(d2.get('results', []))))
            tot += len(d2.get('results', []))
            ok += 1
            break
        else:
            msg = d2.get('message') if isinstance(d2, dict) else str(d2)[:80]
            print('    ds/query %s -> %s %s' % (cand[:8], st2, msg[:70]))
print('\nworked dbs:', ok, 'rows seen:', tot)
