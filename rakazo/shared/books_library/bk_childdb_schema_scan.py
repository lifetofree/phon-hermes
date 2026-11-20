#!/usr/bin/env python3
"""สแกน schema จริงของ child DB ทั้ง 41 เล่ม: ชื่อ title column, property ที่มี, ชื่อ DB (read-only)"""
import os, json, urllib.request, urllib.error, time
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}


def get(url):
    for i in range(9):
        try:
            r = urllib.request.Request(url, headers=H)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(1.5 * (i + 1))
                continue
            raise
    raise RuntimeError('rl')


books = json.load(open('chapters2.json'))
out = []
for e in books:
    ds = get('https://api.notion.com/v1/databases/%s' % e['db_id'])
    props = ds.get('properties', {})
    titles = [k for k, v in props.items() if v.get('type') == 'title']
    dbtitle = ''.join(x.get('plain_text', '') for x in (ds.get('title') or []))
    out.append({
        'book': e['book'],
        'db_id': e['db_id'],
        'db_title': dbtitle,
        'title_col': titles[0] if titles else None,
        'n_title_cols': len(titles),
        'props': {k: v.get('type') for k, v in props.items()},
        'has_status': 'Status' in props and props['Status'].get('type') == 'select',
        'status_options': ([o['name'] for o in props['Status']['select']['options']]
                            if 'Status' in props and props['Status'].get('type') == 'select' else None),
    })
    time.sleep(0.25)

print('=== ชื่อ title column ของ child DB ===')
for k, v in Counter(o['title_col'] for o in out).most_common():
    print('  x%-3d %s' % (v, k))
print('\n=== ชื่อ child DB (db title) ===')
for k, v in Counter(o['db_title'] for o in out).most_common():
    print('  x%-3d %r' % (v, k))
print('\n=== มี Status select ครบไหม ===')
bad = [o['book'] for o in out if not o['has_status']]
print('  ไม่มี/ไม่ใช่ select:', bad if bad else 'ไม่มี - ครบ 41/41')
opt_sets = Counter(tuple(sorted(o['status_options'] or [])) for o in out)
print('  ชุด option ของ Status:')
for k, v in opt_sets.most_common():
    print('    x%d %s' % (v, list(k)))
print('\n=== property อื่นนอกจากมาตรฐาน (title col, Status, Core Message, #) ===')
for o in out:
    extra = [k for k in o['props'] if k not in (o['title_col'], 'Status')
             and 'core message' not in k.lower() and k != '#']
    if extra:
        print('  %-45s %s' % (o['book'][:45], extra))
json.dump(out, open('bk_childdb_schema_scan.json', 'w'), ensure_ascii=False, indent=1)
print('\nsaved -> bk_childdb_schema_scan.json')
