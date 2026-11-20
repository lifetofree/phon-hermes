#!/usr/bin/env python3
"""
Books Library - เติม Status ให้ chapter rows ที่ยังว่าง (Book Keeper)
====================================================================
ค้นหา chapter rows ที่ Status ว่าง ใน 41 child DB แล้วแยกเป็น
  (ก) แถวหัวข้อ PART/Section  -> ไม่ต้องใส่ status (ไม่กระทบการนับ)
  (ข) บทจริงที่มี notes แล้ว  -> ควรเป็น ⬜ QUEUED
  (ค) บทจริงที่ยังไม่มี notes -> ควรเป็น ⬜ QUEUED

รันแบบ dry-run (default) ไม่แตะฐาน:
  python3 bk_fill_status.py
เขียนจริง (ยังไม่อนุมัติ!):
  python3 bk_fill_status.py --apply --yes
"""
import os, sys, json, re, time, urllib.request, urllib.error
from collections import Counter

TOKEN = os.environ['NOTION_TOKEN']
HDR = {'Authorization': 'Bearer ' + TOKEN, 'Notion-Version': '2022-06-28',
       'Content-Type': 'application/json'}
QUEUED = '⬜ QUEUED'
PART_RE = re.compile(r'^\s*(?:\U0001F4C4\s*)?(PART|Part|Section|SECTION)\b', re.I)


def req(url, method='GET', body=None, tries=9):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers=HDR, method=method)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 1.5 * (i + 1)
                print('   429 -> sleep %.1fs' % w, file=sys.stderr)
                time.sleep(w)
                continue
            if e.code == 404:
                return None
            raise
    raise RuntimeError('rate limited')


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


def query_db(did):
    rows, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur:
            b['start_cursor'] = cur
        res = req('https://api.notion.com/v1/databases/%s/query' % did, 'POST', b)
        if res is None:
            return None
        rows += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return rows


def main():
    apply_flag = '--apply' in sys.argv
    confirm = '--yes' in sys.argv

    books = json.load(open('chapters2_live.json'))       # 41 child DBs (book -> db_id)
    plan, part_rows, stat = [], [], Counter()
    details = []
    for entry in books:
        did = entry['db_id']
        db = req('https://api.notion.com/v1/databases/%s' % did)
        if db is None:
            print('  !! child db gone:', entry['book'])
            continue
        props = db['properties']
        status_key = title_key = None
        note_keys = []
        for k, v in props.items():
            kl = k.lower()
            if kl == 'status':
                status_key = k
            if v['type'] == 'title':
                title_key = k
            if 'core message' in kl:
                note_keys.append(k)
        rows = query_db(did)
        if rows is None:
            print('  !! query failed:', entry['book'])
            continue
        c = Counter()
        for r in rows:
            p = r['properties']
            sp = p.get(status_key) if status_key else None
            if sp and sp['type'] == 'select':
                st = (sp.get('select') or {}).get('name') or ''
            elif sp and sp['type'] == 'rich_text':
                st = plain(sp.get('rich_text'))
            else:
                st = ''
            title = plain((p.get(title_key) or {}).get('title')) if title_key else ''
            notes = ''
            for nk in note_keys:
                np = p.get(nk) or {}
                notes += plain(np.get('rich_text')) if np.get('type') == 'rich_text' else ''
            c[st] += 1
            if st != '':
                continue
            is_part = bool(PART_RE.match(title))
            rec = {'page_id': r['id'], 'book': entry['book'], 'db_id': did,
                   'title': title, 'has_notes': bool(notes.strip()), 'status_key': status_key,
                   'kind': 'PART' if is_part else 'CHAPTER'}
            details.append(rec)
            if is_part:
                part_rows.append(rec)
            else:
                plan.append(rec)
        stat.update(c)
        print('  %-46s rows %3d | %s' % (entry['book'][:44], len(rows), dict(c)))
        time.sleep(0.25)

    with_notes = [r for r in plan if r['has_notes']]
    without = [r for r in plan if not r['has_notes']]
    print()
    print('=== chapter rows with EMPTY Status ===')
    print('  total empty          :', len(details))
    print('  PART/Section rows    :', len(part_rows), '(leave blank - not a real chapter)')
    print('  real chapters empty  :', len(plan))
    print('     - has notes       :', len(with_notes), '-> set to %s' % QUEUED)
    print('     - no notes        :', len(without), '-> set to %s' % QUEUED)
    print()
    print('--- target rows to patch (%d) ---' % len(plan))
    for r in plan:
        print('  [%s] %-42s | %s | notes=%s'
              % ('notes' if r['has_notes'] else 'NO-NOTES', r['book'][:42], r['title'][:44],
                 'yes' if r['has_notes'] else 'no'))
    out = {'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'target_status': QUEUED,
           'chapter_rows_to_patch': plan,
           'part_rows_left_blank': part_rows,
           'all_empty_rows': details}
    json.dump(out, open('bk_fill_status_plan.json', 'w'), ensure_ascii=False, indent=1)
    print('\n-> bk_fill_status_plan.json')

    if apply_flag:
        if not confirm:
            print('\n!! --apply needs --yes (and owner approval). Nothing was written.')
            return
        print('\n!! PATCHing %d rows -> %s' % (len(plan), QUEUED))
        for r in plan:
            req('https://api.notion.com/v1/pages/%s' % r['page_id'], 'PATCH',
                {'properties': {r['status_key']: {'select': {'name': QUEUED}}}})
            time.sleep(0.35)
        print('   done')


if __name__ == '__main__':
    main()
