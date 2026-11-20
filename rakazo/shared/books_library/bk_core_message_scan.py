#!/usr/bin/env python3
"""
สแกนชื่อคอลัมน์ Core Message จริงในทั้ง 41 child DB + เช็ค collision ก่อน rename
read-only
"""
import os, json, urllib.request, urllib.error, time
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
                time.sleep(1.5 * (i + 1))
                continue
            raise
    raise RuntimeError('rate limited')


def query_db(did):
    rows, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur:
            b['start_cursor'] = cur
        res = req('https://api.notion.com/v1/databases/%s/query' % did, 'POST', b)
        rows += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return rows


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


books = json.load(open('chapters2.json'))   # book title -> child db id
print('child dbs in file:', len(books))

TARGET = 'Core Message'
report = []
for ent in books:
    title, dbid = ent['book'], ent['db_id']
    ds = req('https://api.notion.com/v1/databases/%s' % dbid)
    props = ds.get('properties', {})
    cands = [k for k in props if 'core message' in k.lower()]
    info = []
    for k in cands:
        p = props[k]
        # นับแถวที่มีค่าจริง + ความยาวรวม
        filled, total_chars = 0, 0
        for row in query_db(dbid):
            v = (row.get('properties') or {}).get(k)
            if v and v.get('type') == 'rich_text':
                t = plain(v.get('rich_text'))
                if t.strip():
                    filled += 1
                    total_chars += len(t)
        info.append({'name': k, 'type': p.get('type'), 'filled_rows': filled,
                     'total_chars': total_chars})
    report.append({'book': title, 'db': dbid, 'core_message_props': info,
                   'n_props': len(cands)})

names = Counter()
for r in report:
    for i in r['core_message_props']:
        names[i['name']] += 1

print('\n=== ชื่อคอลัมน์ Core Message ทั้งหมด ===')
for n, c in names.most_common():
    print('  x%-3d %s' % (c, n))

print('\n=== เคสที่มี property "core message" มากกว่า 1 ตัว (rename จะชน) ===')
for r in report:
    if r['n_props'] > 1:
        print('  %s' % r['book'])
        for i in r['core_message_props']:
            print('     - %-55s type=%-9s filled=%d chars=%d' %
                  (i['name'], i['type'], i['filled_rows'], i['total_chars']))

print('\n=== เคสที่ไม่มี property core message เลย ===')
for r in report:
    if r['n_props'] == 0:
        print('  %s' % r['book'])

json.dump(report, open('bk_core_message_scan.json', 'w'), ensure_ascii=False, indent=1)
print('\nsaved -> bk_core_message_scan.json')
