#!/usr/bin/env python3
"""
แผน rename คอลัมน์ Core Message ให้เป็นชื่อเดียวกันทั้ง 41 child DB (DRY-RUN)
default = แสดงแผนอย่างเดียว (ไม่เขียน)
ใช้: python3 bk_rename_core_message_plan.py            # แสดงแผน
      python3 bk_rename_core_message_plan.py --apply --yes   # เขียนจริง (ต้องได้รับอนุมัติก่อน)
"""
import os, sys, json, time, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}

CANON_NAME = 'Core Message (ฉบับ PHON)'   # ชื่อมาตรฐาน (33/41 เล่มใช้อยู่แล้ว)


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
        props = ds.get('properties', {})
        cands = [k for k, v in props.items()
                 if 'core message' in k.lower() and v.get('type') == 'rich_text']
        if not cands:
            out.append({'book': e['book'], 'db': e['db_id'], 'action': 'SKIP (ไม่มีคอลัมน์ core message)'})
            continue
        if len(cands) > 1:
            out.append({'book': e['book'], 'db': e['db_id'],
                        'action': 'SKIP (มี %d คอลัมน์ - ต้อง merge ก่อน)' % len(cands),
                        'cols': cands})
            continue
        old = cands[0]
        if old == CANON_NAME:
            out.append({'book': e['book'], 'db': e['db_id'], 'action': 'OK (ชื่อมาตรฐานอยู่แล้ว)'})
            continue
        # กันชน: ถ้ามีคอลัมน์ชื่อมาตรฐานอยู่แล้ว -> ต้อง merge ก่อน
        clash = CANON_NAME in props
        out.append({'book': e['book'], 'db': e['db_id'],
                    'action': 'RENAME -> %r' % CANON_NAME if not clash else 'SKIP (ชนกับชื่อที่มีอยู่)',
                    'old': old, 'new': CANON_NAME})
    return out


def apply(pl):
    done = fail = 0
    for p in pl:
        if not p['action'].startswith('RENAME'):
            continue
        body = {'properties': {p['old']: {'name': p['new']}}}
        try:
            # rename property: ส่ง key = ชื่อเดิม, value = {name: ชื่อใหม่}
            api('PATCH', '/databases/%s' % p['db'], body)
            print('  OK  %-45s %s -> %s' % (p['book'][:45], p['old'], p['new']))
            done += 1
        except urllib.error.HTTPError as e:
            fail += 1
            print('  FAIL %-45s %s %s' % (p['book'][:45], e.code, e.read().decode()[:160]))
        time.sleep(0.4)
    print('rename done: ok=%d fail=%d' % (done, fail))


if __name__ == '__main__':
    pl = plan()
    print('=== แผน rename คอลัมน์ Core Message -> %r ===' % CANON_NAME)
    for p in pl:
        print('  %-46s %s' % (p['book'][:46], p['action']))
    n = sum(1 for p in pl if p['action'].startswith('RENAME'))
    print('\nต้อง rename: %d / 41 เล่ม' % n)
    json.dump(pl, open('bk_rename_core_message_plan.json', 'w'), ensure_ascii=False, indent=1)
    print('saved -> bk_rename_core_message_plan.json')
    if '--apply' in sys.argv and '--yes' in sys.argv:
        print('\n>>> APPLY')
        apply(pl)
    else:
        print('(dry-run — ยังไม่เขียน; ใช้ --apply --yes เมื่อได้รับอนุมัติ)')
