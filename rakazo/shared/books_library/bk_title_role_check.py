#!/usr/bin/env python3
"""ตรวจว่าคอลัมน์ title ของแต่ละ child DB เก็บ 'เลขบท' หรือ 'ชื่อบท' (read-only)"""
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


def q(did):
    out, cur = [], None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        res = api('POST', '/databases/%s/query' % did, body)
        out += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
        time.sleep(0.15)
    return out


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


books = json.load(open('chapters2.json'))
num_title, name_title = [], []
for e in books:
    ds = api('GET', '/databases/%s' % e['db_id'])
    props = ds.get('properties', {})
    tcol = [k for k, v in props.items() if v.get('type') == 'title'][0]
    rows = q(e['db_id'])
    vals = [plain((r.get('properties') or {}).get(tcol, {}).get('title')).strip()
            for r in rows]
    numeric = sum(1 for v in vals if v.isdigit())
    kind = 'เลขบท' if numeric > len(vals) / 2 else 'ชื่อบท'
    (num_title if kind == 'เลขบท' else name_title).append((e['book'], tcol, numeric, len(vals)))
    print('  %-46s title=%-26r %s (%d/%d เป็นตัวเลข)' % (e['book'][:46], tcol, kind, numeric, len(vals)))

print('\n=== สรุป ===')
print('  title col เก็บ "เลขบท"  : %d เล่ม' % len(num_title))
print('  title col เก็บ "ชื่อบท" : %d เล่ม' % len(name_title))
print('  -> ชื่อบทอยู่ในคอลัมน์ "Chapter Title (Original)" (rich_text) เสมอ')
