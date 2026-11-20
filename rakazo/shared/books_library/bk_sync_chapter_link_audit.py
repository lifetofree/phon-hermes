#!/usr/bin/env python3
"""
ตรวจว่า sync_books_library.py จะ 'มองเห็น' child DB กี่เล่ม
เพราะสคริปต์เลือก child_database ที่ title มีคำว่า 'chapter' (case-insensitive)
แต่ 34/41 child DB มี title ว่าง -> อาจหายไปทั้งหมด
read-only
"""
import os, json, urllib.request, urllib.error, time, re

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}


def api(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(9):
        try:
            req = urllib.request.Request('https://api.notion.com/v1' + path,
                                         data=data, headers=H, method=method)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(1.5 * (i + 1))
                continue
            raise
    raise RuntimeError('rl')


books = json.load(open('chapters2.json'))
found_db, found_head, none_at_all = [], [], []
for e in books:
    blocks, cur = [], None
    while True:
        d = api('GET', '/blocks/%s/children?page_size=100%s' % (e['book_id'], '&start_cursor=' + cur if cur else ''))
        blocks += d.get('results', [])
        if not d.get('has_more'):
            break
        cur = d.get('next_cursor')
    dbs = [b for b in blocks if b['type'] == 'child_database'
           and 'chapter' in b['child_database'].get('title', '').lower()]
    h3 = [b for b in blocks if b['type'] == 'heading_3'
          and re.search(r'chapter\s*#?\s*\d+', ''.join(x['plain_text'] for x in b['heading_3']['rich_text']), re.I)]
    if dbs:
        found_db.append((e['book'], [b['child_database'].get('title', '') for b in dbs]))
    if h3:
        found_head.append((e['book'], len(h3)))
    if not dbs and not h3:
        none_at_all.append(e['book'])

print('=== สคริปต์ sync จะเจอ child DB ที่มีคำว่า "chapter" ===')
print('  เจอ %d / 41 เล่ม' % len(found_db))
for b, t in found_db:
    print('   -', b[:45], '|', t)
print('\n=== เล่มที่มี heading_3 "Chapter #N" (fallback ที่สคริปต์ใช้) ===')
print('  จำนวน %d เล่ม' % len(found_head))
for b, n in found_head[:12]:
    print('   -', b[:45], '(%d headings)' % n)
print('\n=== เล่มที่สคริปต์จะได้ chapter = 0 (ไม่มีทั้ง child DB ที่ match และไม่มี h3) ===')
print('  จำนวน %d เล่ม' % len(none_at_all))
for b in none_at_all:
    print('   -', b[:50])
