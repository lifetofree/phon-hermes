#!/usr/bin/env python3
"""
นับ chapter rows ของ child DB 'Chapter List' ทุกเล่ม (legacy endpoint, ver 2022-06-28)
read-only
"""
import os, json, time, urllib.request, urllib.error
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
V = '2022-06-28'
HDR = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': V,
       'Content-Type': 'application/json'}


def req(url, method='GET', body=None, tries=8):
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
            return {'__err__': e.code, 'body': e.read().decode()[:250]}
        except Exception:
            time.sleep(2)
    return {'__err__': 'retry-exhausted'}


def query(db_id):
    rows = []
    cur = None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        res = req('https://api.notion.com/v1/databases/%s/query' % db_id, 'POST', body)
        if '__err__' in res:
            return rows, res
        rows += res.get('results', [])
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return rows, None


scan = json.load(open('bk_childdb_scan.json'))
out = []
tot = Counter()
for r in scan:
    for c in r['child_dbs']:
        rows, err = query(c['id'])
        cnt = Counter()
        notes = 0
        for x in rows:
            pr = x.get('properties', {})
            st = None
            has_note = False
            for k, v in pr.items():
                kl = k.lower()
                if kl == 'status':
                    st = (v.get('select') or {}).get('name')
                    if st is None and v.get('type') == 'rich_text':
                        st = ''.join(t.get('plain_text', '') for t in (v.get('rich_text') or []))
                if 'core message' in kl:
                    txt = ''.join(t.get('plain_text', '') for t in (v.get('rich_text') or []))
                    if txt.strip():
                        has_note = True
            cnt[st if st is not None else 'NO_PROP'] += 1
            if has_note:
                notes += 1
        tot.update(cnt)
        out.append({'book': r['title'], 'db_id': c['id'], 'n': len(rows),
                    'status': dict(cnt), 'notes': notes,
                    'err': err['__err__'] if err else None})
        if err:
            print('ERR', r['title'][:40], err)

json.dump(out, open('bk_chapter_rows_scan.json', 'w'), ensure_ascii=False, indent=1)

print('child dbs scanned :', len(out))
print('total chapter rows:', sum(o['n'] for o in out))
print('rows with notes   :', sum(o['notes'] for o in out))
print('status totals     :', dict(tot))
nz = [o for o in out if o['n']]
print('child dbs with rows:', len(nz), '| empty:', len(out) - len(nz))
print('\nbooks with chapter rows:')
for o in sorted(nz, key=lambda o: -o['n']):
    print('  %-46s %4d  notes=%-4d %s' % (o['book'][:46], o['n'], o['notes'], o['status']))
