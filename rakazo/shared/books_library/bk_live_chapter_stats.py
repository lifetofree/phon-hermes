#!/usr/bin/env python3
"""
สถานะ chapter สดทั้ง 41 เล่ม + จัดอันดับ "อ่านต่อ" (read-only)
"""
import os, json, urllib.request, urllib.error, time
from collections import Counter

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
report = []
for e in books:
    ds = api('GET', '/databases/%s' % e['db_id'])
    props = ds.get('properties', {})
    tcol = [k for k, v in props.items() if v.get('type') == 'title'][0]
    core_cols = [k for k in props if 'core message' in k.lower()]
    rows = q(e['db_id'])
    st = Counter()
    notes_filled = 0
    part_rows = 0
    for r in rows:
        P = r.get('properties') or {}
        sv = P.get('Status') or {}
        name = (sv.get('select') or {}).get('name') or ''
        st[name or '(ว่าง)'] += 1
        has_note = False
        for cc in core_cols:
            t = plain((P.get(cc) or {}).get('rich_text')).strip()
            if t:
                has_note = True
        if has_note:
            notes_filled += 1
        # ตรวจว่าแถวเป็นแถวหัวข้อ PART/Section หรือไม่
        tv = plain((P.get(tcol) or {}).get('title')).strip()
        if not tv or tv.lower().startswith('part') or tv.lower().startswith('section'):
            part_rows += 1
    report.append({
        'book': e['book'], 'db': e['db_id'], 'rows': len(rows),
        'status': dict(st), 'notes_filled': notes_filled,
        'title_col': tcol, 'core_cols': core_cols,
    })

json.dump(report, open('bk_live_chapter_stats.json', 'w'), ensure_ascii=False, indent=1)

tot = Counter()
for r in report:
    for k, v in r['status'].items():
        tot[k] += v
print('=== สถานะ chapter รวมทั้ง 41 เล่ม (สด) ===')
for k, v in tot.most_common():
    print('  %-12s %d' % (k, v))
print('  รวมแถว        %d' % sum(tot.values()))

full = [r for r in report
        if r['status'].get('✅ INSTALLED', 0) == r['rows'] and r['rows'] > 0]
print('\nหนังสือที่อ่านครบทุกบท (ทุกแถว INSTALLED): %d เล่ม' % len(full))
for r in full:
    print('  -', r['book'])

print('\n=== จัดอันดับ: ใกล้จบสุด (มี notes ครบ + เหลือ INSTALLED น้อย) ===')
cand = [r for r in report if r['notes_filled'] == r['rows'] and r['status'].get('✅ INSTALLED', 0) < r['rows']]
cand.sort(key=lambda r: (r['status'].get('✅ INSTALLED', 0), -r['rows']))
for r in cand[:12]:
    s = r['status']
    print('  %-46s rows=%-3d INST=%-2d LOAD=%-2d QUEUED=%-3d ว่าง=%d' % (
        r['book'][:46], r['rows'], s.get('✅ INSTALLED', 0), s.get('⏳ LOADING...', 0),
        s.get('⬜ QUEUED', 0), s.get('(ว่าง)', 0)))

print('\n=== งานเดินไปไก (INSTALLED มากสุด) ===')
for r in sorted(report, key=lambda r: -r['status'].get('✅ INSTALLED', 0))[:10]:
    s = r['status']
    print('  %-46s INST=%-2d/%-3d notes=%d/%d' % (
        r['book'][:46], s.get('✅ INSTALLED', 0), r['rows'], r['notes_filled'], r['rows']))

print('\n=== notes ไม่ครบ ===')
for r in report:
    if r['notes_filled'] < r['rows']:
        print('  %-46s notes=%d/%d' % (r['book'][:46], r['notes_filled'], r['rows']))
print('\nsaved -> bk_live_chapter_stats.json')
