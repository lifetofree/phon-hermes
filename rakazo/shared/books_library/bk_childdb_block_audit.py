#!/usr/bin/env python3
"""ยืนยันว่า child DB 34 เล่มที่ title ว่าง เป็น child_database block จริงในหน้าหนังสือ (read-only)"""
import os, json, urllib.request, urllib.error, time

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
ok = 0
mismatch = []
for e in books:
    blocks, cur = [], None
    while True:
        d = api('GET', '/blocks/%s/children?page_size=100%s' % (e['book_id'], '&start_cursor=' + cur if cur else ''))
        blocks += d.get('results', [])
        if not d.get('has_more'):
            break
        cur = d.get('next_cursor')
    cdbs = [b for b in blocks if b['type'] == 'child_database']
    ids = [b['id'] for b in cdbs]
    if e['db_id'] in ids:
        ok += 1
    else:
        mismatch.append((e['book'], [b['child_database'].get('title', '') for b in cdbs]))
    time.sleep(0.2)

print('หนังสือที่มี child_database block ตรงกับ db_id ที่บันทึกไว้: %d / 41' % ok)
if mismatch:
    print('ไม่ตรง %d เล่ม:' % len(mismatch))
    for b, t in mismatch:
        print('  -', b[:50], t)
else:
    print('=> ทุกเล่มมี child_database block จริง แต่ 34 เล่มมี title ว่าง '
          '(สคริปต์ sync ที่กรองคำว่า "chapter" จึงมองไม่เห็น)')
