#!/usr/bin/env python3
"""
Books Library — เพิ่มหนังสือใหม่ + สร้าง Chapter List child DB (Book Keeper)
=======================================================================
ใช้:
  python3 bk_add_book.py --title "ชื่อหนังสือ" --author "ผู้แต่ง" \
      --energy "G.3" --tags "#Strategy #Management" [--chapters 12] [--apply --yes]

ค่าเริ่มต้น = DRY-RUN (แสดงแผน ไม่เขียนฐาน)
--apply --yes = เขียนจริง (ใช้เมื่อเจ้าของสั่งเพิ่มหนังสือ)

Energy Group: G.1 | G.2 | G.3 | Boss  ->  🟢 G.1 / 🟡 G.2 / 🟠 G.3 / 🔴 Boss
Status ที่สร้าง: ⬜ QUEUED (ยังไม่มี chapter)
Schema Chapter List (ตามแบบที่ใช้จริง 37/41 เล่ม):
  - '#'                      title   (เลขบท)
  - 'Chapter Title (Original)' rich_text (ชื่อบทต้นฉบับ)
  - 'Core Message (ฉบับ PHON)' rich_text (notes)
  - 'Status'                 select  (⬜ QUEUED / ⏳ LOADING... / ✅ INSTALLED)
"""
import os, sys, json, time, urllib.request, urllib.error, argparse

TOK = os.environ['NOTION_TOKEN']
DB = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
DS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}

ENERGY = {'G.1': '🟢 G.1', 'G.2': '🟡 G.2', 'G.3': '🟠 G.3', 'Boss': '🔴 Boss'}
STATUS_OPTS = ['⬜ QUEUED', '⏳ LOADING...', '✅ INSTALLED']
COL_NUM = '#'
COL_ORIG = 'Chapter Title (Original)'
COL_CORE = 'Core Message (ฉบับ PHON)'


def api(method, path, body=None, tries=9):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
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
    raise RuntimeError('rate limited')


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


def existing_titles():
    t = set()
    for p in q(DB):
        for k, v in (p.get('properties') or {}).items():
            if v.get('type') == 'title':
                t.add(plain(v.get('title')).strip().lower())
                break
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--title', required=True)
    ap.add_argument('--author', default='')
    ap.add_argument('--energy', default='G.3')
    ap.add_argument('--tags', default='')
    ap.add_argument('--chapters', type=int, default=0)
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--yes', action='store_true')
    a = ap.parse_args()

    energy = ENERGY.get(a.energy.strip(), a.energy.strip())
    tags = [t for t in a.tags.split() if t.startswith('#')]
    # กัน tag ซ้ำ + ตัด tag ที่ไม่มีใน option (multi_select: ชื่อต้องตรง)
    ds = api('GET', '/databases/%s' % DB)
    props = ds.get('properties', {})
    valid = {o['name'] for o in props.get('Tags', {}).get('multi_select', {}).get('options', [])}
    bad = [t for t in tags if t not in valid]

    print('=== แผนเพิ่มหนังสือ ===')
    print('  Title       : %s' % a.title)
    print('  Author      : %s' % (a.author or '(ไม่ระบุ)'))
    print('  Energy Group: %s' % energy)
    print('  Tags        : %s' % (' '.join(tags) or '(ไม่ระบุ)'))
    if bad:
        print('  ! tag ที่ไม่มีใน schema (จะไม่ถูกเขียน): %s' % ', '.join(bad))
    print('  Status      : ⬜ QUEUED')
    print('  Chapter List: %d แถว' % a.chapters)

    dup = a.title.strip().lower() in existing_titles()
    if dup:
        print('  ! มีชื่อนี้ในฐานแล้ว (normalized match) — ตรวจก่อนเขียน')

    if not (a.apply and a.yes):
        print('\n(dry-run — ยังไม่เขียน; ใช้ --apply --yes เมื่อได้รับคำสั่งเจ้าของ)')
        return

    if bad and not a.yes:
        raise SystemExit('มี tag ที่ไม่รู้จัก')

    # 1) สร้างแถวหนังสือ
    body = {'parent': {'database_id': DB}, 'properties': {
        'Title': {'title': [{'type': 'text', 'text': {'content': a.title}}]},
        'Author': {'rich_text': [{'type': 'text', 'text': {'content': a.author}}] if a.author else []},
        'Energy Group': {'select': {'name': energy}},
        'Status': {'select': {'name': '⬜ QUEUED'}},
        'Tags': {'multi_select': [{'name': t} for t in tags if t in valid]},
    }}
    page = api('POST', '/pages', body)
    pid = page['id']
    print('\n  สร้างแถวหนังสือแล้ว: %s' % pid)
    print('  URL: %s' % page.get('url'))

    if a.chapters > 0:
        time.sleep(0.5)
        child = api('POST', '/databases', {
            'parent': {'type': 'page_id', 'page_id': pid},
            'title': [{'type': 'text', 'text': {'content': 'Chapter List'}}],
            'is_inline': True,
            'properties': {
                COL_NUM: {'title': {}},
                COL_ORIG: {'rich_text': {}},
                COL_CORE: {'rich_text': {}},
                'Status': {'select': {'options': [{'name': n} for n in STATUS_OPTS]}},
            },
        })
        cid = child['id']
        print('  สร้าง Chapter List แล้ว: %s' % cid)
        for i in range(a.chapters):
            api('POST', '/pages', {
                'parent': {'database_id': cid},
                'properties': {
                    COL_NUM: {'title': [{'type': 'text', 'text': {'content': str(i + 1)}}]},
                    'Status': {'select': {'name': '⬜ QUEUED'}},
                },
            })
            time.sleep(0.35)
        print('  ใส่ chapter แถวที่ว่าง %d แถว (เลขบท 1-%d)' % (a.chapters, a.chapters))

    print('\nเสร็จแล้ว — ยังไม่มี notes/ต้นฉบับ สถานะยังเป็น ⬜ QUEUED')


if __name__ == '__main__':
    main()
