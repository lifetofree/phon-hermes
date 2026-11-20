#!/usr/bin/env python3
"""ตรวจค่าในคอลัมน์ '#' / 'Chapter Title (Original)' / 'ผ่านฟิลเตอร์ 3 Laws ของ OPB' (read-only)"""
import os, json, urllib.request, urllib.error, time

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


def q(did):
    out, cur = [], None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        req = urllib.request.Request(
            'https://api.notion.com/v1/databases/%s/query' % did,
            data=json.dumps(body).encode(), headers=H, method='POST')
        res = json.load(urllib.request.urlopen(req))
        out += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
        time.sleep(0.2)
    return out


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


schema = json.load(open('bk_childdb_schema_scan.json'))
targets = [s for s in schema
           if 'ผ่านฟิลเตอร์' in json.dumps(s['props'], ensure_ascii=False)]
print('child DB ที่มีคอลัมน์ "ผ่านฟิลเตอร์..." :', len(targets), '/ 41')

print('\n=== ตัวอย่างค่า 5 เล่มแรก ===')
for s in targets[:5]:
    rows = q(s['db_id'])
    col = [k for k in s['props'] if 'ผ่านฟิลเตอร์' in k][0]
    vals = []
    for r in rows[:6]:
        v = (r.get('properties') or {}).get(col) or {}
        vals.append(plain(v.get('rich_text')))
    filled = sum(1 for r in rows if plain(((r.get('properties') or {}).get(col) or {}).get('rich_text')).strip())
    print('\n%s' % s['book'])
    print('   column : %r  (filled %d/%d)' % (col, filled, len(rows)))
    for v in vals:
        print('     - %r' % v[:90])

print('\n=== ค่าในคอลัมน์ "#" และ title ของ 3 เล่มตัวอย่าง ===')
for s in schema[:3]:
    rows = q(s['db_id'])
    print('\n%s  (title col = %r)' % (s['book'], s['title_col']))
    for r in rows[:5]:
        p = r.get('properties') or {}
        tcol = s['title_col']
        tv = plain((p.get(tcol) or {}).get('title')) or plain((p.get(tcol) or {}).get('rich_text'))
        hv = plain((p.get('#') or {}).get('rich_text'))
        cto = plain((p.get('Chapter Title (Original)') or {}).get('rich_text'))
        print('   title=%-28r  #=%-12r  ChapterTitleOrig=%r' % (tv[:28], hv[:12], cto[:34]))
