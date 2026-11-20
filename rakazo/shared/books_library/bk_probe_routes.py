#!/usr/bin/env python3
"""probe 3: หา route ที่ query ได้จริงสำหรับ child DB ทุกเล่ม (read-only)"""
import os, json, urllib.request, urllib.error, time

TOK = os.environ['NOTION_TOKEN']


def api(path, method='GET', body=None, ver='2025-09-03', tries=6):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        req = urllib.request.Request(
            'https://api.notion.com/v1' + path, data=data, method=method,
            headers={'Authorization': 'Bearer ' + TOK, 'Notion-Version': ver,
                     'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(1.5 * (i + 1)); continue
            return e.code, e.read().decode()[:200]
        except Exception as e:
            return 'ERR', str(e)[:200]
    return 'ERR', 'rate limited'


def query_all(path, ver):
    rows, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur:
            b['start_cursor'] = cur
        st, d = api(path, 'POST', b, ver)
        if st != 200:
            return None, d
        rows += d['results']
        if not d.get('has_more'):
            break
        cur = d.get('next_cursor')
    return rows, None


books = json.load(open('chapters2.json'))
report = {}
for b in books:
    did = b['db_id']
    st, meta = api('/databases/%s' % did)
    dss = (meta.get('data_sources') or []) if isinstance(meta, dict) else []
    dsid = dss[0]['id'] if dss else None
    rows, err = (None, None)
    route = None
    if dsid:
        rows, err = query_all('/data_sources/%s/query' % dsid, '2025-09-03')
        if rows is not None:
            route = 'ds(2025)+%s' % dsid[:8]
    if rows is None:
        r2, e2 = query_all('/data_sources/%s/query' % did, '2025-09-03')
        if r2 is not None:
            rows, route = r2, 'ds(2025)+dbid'
    if rows is None:
        r3, e3 = query_all('/databases/%s/query' % did, '2022-06-28')
        if r3 is not None:
            rows, route = r3, 'dbquery(2022)'
    report[b['book']] = {'db_id': did, 'ds_id': dsid, 'route': route,
                         'n': len(rows) if rows is not None else None,
                         'err': (err or '')[:120] if rows is None else ''}
    print('%-46s n=%-4s route=%s' % (b['book'][:44], report[b['book']]['n'], route))
    time.sleep(0.2)

tot = sum(v['n'] or 0 for v in report.values())
print('\nTOTAL rows:', tot, '| dbs resolved:', sum(1 for v in report.values() if v['n'] is not None))
json.dump(report, open('bk_probe_routes.json', 'w'), ensure_ascii=False, indent=1)
