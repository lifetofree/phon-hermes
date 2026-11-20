#!/usr/bin/env python3
"""
สแกนบทบาทคอลัมน์ใน child DB ทั้ง 41 เล่ม + สถานะคอลัมน์ 'ผ่านฟิลเตอร์ 3 Laws ของ OPB'
read-only
"""
import os, json, urllib.request, urllib.error, time

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}


def q(did):
    out, cur = [], None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        req = urllib.request.Request(
            'https://api.notion.com/v1/databases/%s/query' % did,
            data=json.dumps(body).encode(), headers=H, method='POST')
        for i in range(9):
            try:
                res = json.load(urllib.request.urlopen(req))
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(1.5 * (i + 1))
                    continue
                raise
        out += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
        time.sleep(0.15)
    return out


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


schema = json.load(open('bk_childdb_schema_scan.json'))
print('%-46s %-26s %-24s %s' % ('BOOK', 'TITLE COL', 'NUMBER COL', 'OPB col (filled/blank/-)'))
print('-' * 130)
tot = {'opb_db': 0, 'filled': 0, 'blank': 0, 'dash': 0}
for s in schema:
    rows = q(s['db_id'])
    props = s['props']
    tcol = s['title_col']
    # หาคอลัมน์ที่เก็บ "เลขบท" (ไม่ใช่ชื่อบท)
    numcol = None
    for cand in ('#', 'Chapter #'):
        if cand in props and cand != tcol:
            numcol = cand
            break
    opb = [k for k in props if 'ผ่านฟิลเตอร์' in k]
    opbs = ''
    if opb:
        tot['opb_db'] += 1
        col = opb[0]
        f = b = d = 0
        for r in rows:
            v = plain(((r.get('properties') or {}).get(col) or {}).get('rich_text')).strip()
            if not v:
                b += 1
            elif v == '-':
                d += 1
            else:
                f += 1
        tot['filled'] += f
        tot['blank'] += b
        tot['dash'] += d
        opbs = '%r %d/%d/%d' % (col, f, b, d)
    print('%-46s %-26s %-24s %s' % (s['book'][:46], repr(tcol), repr(numcol), opbs))

print('\n=== สรุปคอลัมน์ OPB ===')
print('DB ที่มีคอลัมน์ OPB      : %d / 41' % tot['opb_db'])
print('ช่องที่มีค่าจริง          : %d' % tot['filled'])
print('ช่องว่างเปล่า           : %d' % tot['blank'])
print("ช่องที่เป็น '-' (ไม่ผ่าน): %d" % tot['dash'])
