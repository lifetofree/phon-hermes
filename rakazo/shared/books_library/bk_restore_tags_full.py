#!/usr/bin/env python3
"""
Rollback ที่ "สมบูรณ์" หลัง merge tag (Book Keeper) — ยังไม่รัน รอคำสั่งเจ้าของ

ปัญหาของ restore_tags.py (ของ Chief):
  มัน PATCH ค่า multi_select ของแต่ละแถวด้วยชื่อ tag เก่า (193 ชื่อ)
  แต่ตอนนี้ schema มีแค่ 76 option -> Notion จะ "สร้าง option ใหม่" ให้อัตโนมัติ
  (ตามเอกสาร: "A new option name adds an option to the schema")
  => rollback คืนค่าได้ แต่ schema จะเหลือ option เก่า 117 ชื่อที่ไม่มีใครใช้
  (ต้อง reset option list กลับด้วย)

สคริปต์นี้ทำ 2 ขั้น:
  1) reset multi_select options = รายชื่อเดิม 193 ชื่อ (จาก snapshot)
  2) คืนค่า tag ทุกแถวจาก snapshot
  (ลำดับสลับกันก็ได้ แต่แบบนี้ schema สะอาดตั้งแต่แรก)

ใช้: python3 bk_restore_tags_full.py            # แสดงแผน (dry-run)
      python3 bk_restore_tags_full.py --apply --yes
"""
import os, sys, json, time, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
DS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
DB = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
SNAP = '../../bots/cmwj2kqkfl1cdznjl9fxz39ik/books_tags_snapshot.json'
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}


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


snap = json.load(open(SNAP))
rows = snap['rows']
names = sorted({t for r in rows for t in r['tags']})
print('=== แผน rollback ===')
print('  แถวที่จะคืนค่า      : %d' % len(rows))
print('  option ที่จะคืน schema: %d' % len(names))

ds = api('GET', '/databases/%s' % DB)
cur = {o['name'] for o in ds.get('properties', {}).get('Tags', {}).get('multi_select', {}).get('options', [])}
print('  option ปัจจุบัน       : %d' % len(cur))
print('  ต้องเพิ่มกลับ          : %d' % len(set(names) - cur))

if not ('--apply' in sys.argv and '--yes' in sys.argv):
    print('\n(dry-run — ยังไม่เขียน)')
    raise SystemExit(0)

# 1) reset options
r = api('PATCH', '/databases/%s' % DB,
        {'properties': {'Tags': {'multi_select': {'options': [{'name': n} for n in names]}}}})
print('\n  reset options -> %d ชื่อ' % len(r['properties']['Tags']['multi_select']['options']))

# 2) คืนค่าแต่ละแถว
ok = fail = 0
for i, row in enumerate(rows):
    try:
        api('PATCH', '/pages/%s' % row['page_id'],
            {'properties': {'Tags': {'multi_select': [{'name': t} for t in row['tags']]}}})
        ok += 1
    except urllib.error.HTTPError as e:
        fail += 1
        print('  FAIL', row['title'], e.code, e.read().decode()[:120])
    time.sleep(0.32)
    if i % 50 == 0:
        print('   ...%d/%d ok=%d fail=%d' % (i, len(rows), ok, fail), flush=True)
print('restore done: ok=%d fail=%d' % (ok, fail))
