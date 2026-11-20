#!/usr/bin/env python3
"""
แผน rename child DB ให้ชื่อเดียวกัน 'Chapter List' (DRY-RUN)
เหตุผล: sync_books_library.py เลือก child_database ที่ title มีคำว่า 'chapter'
         ตอนนี้ 34/41 เล่ม title ว่าง -> สคริปต์มองเห็นแค่ 7/41
ใช้: python3 bk_rename_childdb_plan.py
      python3 bk_rename_childdb_plan.py --apply --yes   (ต้องได้รับอนุมัติ)
"""
import os, sys, json, time, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}
TARGET = 'Chapter List'


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


def plan():
    books = json.load(open('chapters2.json'))
    out = []
    for e in books:
        ds = api('GET', '/databases/%s' % e['db_id'])
        cur = ''.join(x.get('plain_text', '') for x in (ds.get('title') or []))
        action = 'OK' if cur.strip() == TARGET else 'RENAME %r -> %r' % (cur, TARGET)
        out.append({'book': e['book'], 'db': e['db_id'], 'old': cur, 'new': TARGET,
                    'action': action})
    return out


def apply(pl):
    done = fail = 0
    for p in pl:
        if p['action'] == 'OK':
            continue
        try:
            api('PATCH', '/databases/%s' % p['db'],
                {'title': [{'type': 'text', 'text': {'content': TARGET}}]})
            print('  OK  %-45s %r -> %r' % (p['book'][:45], p['old'], TARGET))
            done += 1
        except urllib.error.HTTPError as e:
            fail += 1
            print('  FAIL %-45s %s %s' % (p['book'][:45], e.code, e.read().decode()[:160]))
        time.sleep(0.4)
    print('rename done: ok=%d fail=%d' % (done, fail))


if __name__ == '__main__':
    pl = plan()
    print('=== แผน rename child DB -> %r ===' % TARGET)
    for p in pl:
        print('  %-46s %s' % (p['book'][:46], p['action']))
    n = sum(1 for p in pl if p['action'] != 'OK')
    print('\nต้อง rename: %d / 41' % n)
    json.dump(pl, open('bk_rename_childdb_plan.json', 'w'), ensure_ascii=False, indent=1)
    print('saved -> bk_rename_childdb_plan.json')
    if '--apply' in sys.argv and '--yes' in sys.argv:
        print('\n>>> APPLY')
        apply(pl)
    else:
        print('(dry-run — ยังไม่เขียน)')
