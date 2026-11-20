#!/usr/bin/env python3
"""
สแกน child_database block ของหนังสือทั้ง 251 แถว + เช็คสถานะ (active / in_trash / title)
read-only — ไม่เขียนฐาน
"""
import os, json, time, urllib.request, urllib.error
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
HDR = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
       'Content-Type': 'application/json'}


def req(url, method='GET', body=None, tries=9):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers=HDR, method=method)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(min(2 + i * 2, 30))
                continue
            return {'__err__': e.code, 'body': e.read().decode()[:200]}
        except Exception:
            time.sleep(2)
    return {'__err__': 'retry-exhausted'}


def ttl(p):
    return ''.join(x.get('plain_text', '') for x in (p.get('title') or []))


def blocks(page_id):
    out = []
    cur = None
    while True:
        url = 'https://api.notion.com/v1/blocks/%s/children' % page_id
        if cur:
            url += '?start_cursor=' + cur
        res = req(url)
        if '__err__' in res:
            return out, res
        out += res.get('results', [])
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return out, None


rows = json.load(open('live_rows_2011.json'))
books = []
for r in rows:
    pr = r['properties']
    books.append({'page_id': r['id'], 'title': ttl(pr.get('Title', {})),
                  'status': (pr.get('Status', {}).get('select') or {}).get('name')})

report = []
for b in books:
    bl, err = blocks(b['page_id'])
    cds = [x for x in bl if x.get('type') == 'child_database']
    info = []
    for c in cds:
        db = req('https://api.notion.com/v1/databases/%s' % c['id'])
        if '__err__' in db:
            info.append({'id': c['id'], 'title': c.get('child_database', {}).get('title'),
                         'error': db['__err__']})
            continue
        info.append({'id': c['id'], 'title': db.get('title'),
                     'in_trash': db.get('in_trash'), 'archived': db.get('archived'),
                     'data_sources': [ds.get('id') for ds in (db.get('data_sources') or [])],
                     'props': {k: v['type'] for k, v in db.get('properties', {}).items()}})
    report.append({'title': b['title'], 'page_id': b['page_id'],
                   'status': b['status'], 'child_dbs': info, 'err': err})

json.dump(report, open('bk_childdb_scan.json', 'w'), ensure_ascii=False, indent=1)

n_with = sum(1 for r in report if r['child_dbs'])
n_none = sum(1 for r in report if not r['child_dbs'])
print('books with child_database block:', n_with)
print('books without:', n_none)
tc = Counter()
for r in report:
    for c in r['child_dbs']:
        t = ''.join(x.get('plain_text', '') for x in (c.get('title') or []))
        tc[(t, c.get('in_trash'), c.get('archived'))] += 1
print('\n(child db title, in_trash, archived) -> count')
for k, v in tc.most_common():
    print('  %-28s trash=%-5s arch=%-5s  %d' % (repr(k[0]), k[1], k[2], v))
