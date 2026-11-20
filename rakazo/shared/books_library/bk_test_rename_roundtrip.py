#!/usr/bin/env python3
"""
ทดสอบ API rename property แบบ reversible บน 1 child DB
(เปลี่ยนชื่อ -> ตรวจว่าข้อมูลยังอยู่ -> คืนชื่อเดิม)
"""
import os, json, urllib.request, urllib.error, time

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}
DB = '2ffdf8d8-8d8c-8016-acf6-f50ee8209354'   # Four Thousand Weeks child DB
OLD = 'Core Message (ฉบับ PHON/Duck OS)'
NEW = 'Core Message (ฉบับ PHON)'


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
            return {'__error__': e.code, 'body': e.read().decode()[:300]}
    raise RuntimeError('rl')


def snap(colname):
    out, cur = [], None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        res = api('POST', '/databases/%s/query' % DB, body)
        out += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
        time.sleep(0.15)
    vals = []
    for r in out:
        v = (r.get('properties') or {}).get(colname)
        if v and v.get('type') == 'rich_text':
            vals.append(''.join(x.get('plain_text', '') for x in v.get('rich_text', [])))
        else:
            vals.append(None)
    return out, vals


print('=== ก่อน rename ===')
ds = api('GET', '/databases/%s' % DB)
props = ds.get('properties', {})
pid = props[OLD]['id']
print('  property id:', pid)
print('  ชื่อที่มี:', [k for k in props if 'core' in k.lower()])
rows_before, vals_before = snap(OLD)
print('  rows:', len(rows_before), '| ค่าไม่ว่าง:', sum(1 for v in vals_before if v))
chars_before = sum(len(v) for v in vals_before if v)

print('\n=== PATCH rename ===')
r = api('PATCH', '/databases/%s' % DB,
        {'properties': {OLD: {'name': NEW, 'rich_text': {}}}})
if '__error__' in r:
    print('  ERROR:', r['__error__'], r['body'])
    raise SystemExit(1)
print('  OK ->', NEW)

time.sleep(0.6)
ds2 = api('GET', '/databases/%s' % DB)
props2 = ds2.get('properties', {})
print('  ชื่อหลัง rename:', [k for k in props2 if 'core' in k.lower()])
print('  id เดิมยังอยู่:', pid in props2.get(NEW, {}).get('id', '') or props2.get(NEW, {}).get('id') == pid)

rows_after, vals_after = snap(NEW)
chars_after = sum(len(v) for v in vals_after if v)
print('  rows:', len(rows_after), '| ค่าไม่ว่าง:', sum(1 for v in vals_after if v))
print('  จำนวนอักขระรวม: ก่อน %d -> หลัง %d' % (chars_before, chars_after))
same = vals_before == vals_after
print('  ข้อมูลเหมือนเดิมทุกแถว:', same)

print('\n=== คืนชื่อเดิม ===')
r2 = api('PATCH', '/databases/%s' % DB,
         {'properties': {NEW: {'name': OLD, 'rich_text': {}}}})
if '__error__' in r2:
    print('  ERROR:', r2['__error__'], r2['body'])
    raise SystemExit(1)
time.sleep(0.6)
ds3 = api('GET', '/databases/%s' % DB)
props3 = ds3.get('properties', {})
print('  ชื่อหลังคืน:', [k for k in props3 if 'core' in k.lower()])
rows_back, vals_back = snap(OLD)
print('  rows:', len(rows_back), '| ค่าไม่ว่าง:', sum(1 for v in vals_back if v))
print('  ข้อมูลกลับมาเหมือนเดิม:', vals_back == vals_before)
