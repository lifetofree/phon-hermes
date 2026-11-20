#!/usr/bin/env python3
"""
PROBE (read-mostly): ทดสอบว่ากู้ child DB ที่ถูกย้ายเข้า Trash กลับมาได้ไหม
ขั้นตอน: restore DB เก่า -> query อ่าน notes -> บันทึกลงไฟล์ -> ย้ายกลับเข้า Trash
(ย้ายกลับเข้า Trash = คืนสภาพเดิมทุกประการ) ไม่แตะหนังสือ/แถวที่มีอยู่

ใช้: python3 bk_probe_restore.py "<ชื่อหนังสือ>"
"""
import os, sys, json, time, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
HDR = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
       'Content-Type': 'application/json'}


def req(url, method='GET', body=None, tries=6):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers=HDR, method=method)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2 + i * 2)
                continue
            return {'__err__': e.code, 'body': e.read().decode()[:250]}
        except Exception:
            time.sleep(2)
    return {'__err__': 'retry-exhausted'}


def query(db_id):
    rows = []
    cur = None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        res = req('https://api.notion.com/v1/databases/%s/query' % db_id, 'POST', body)
        if '__err__' in res:
            return rows, res
        rows += res.get('results', [])
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return rows, None


def ptext(v):
    t = v.get('type')
    if t == 'title':
        return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))
    if t == 'rich_text':
        return ''.join(x.get('plain_text', '') for x in (v.get('rich_text') or []))
    if t == 'select':
        return (v.get('select') or {}).get('name') or ''
    return ''


name = sys.argv[1] if len(sys.argv) > 1 else 'Atomic Habits'
old = {c['book']: c for c in json.load(open('chapters2.json'))}
key = [k for k in old if k.startswith(name[:18])][0]
dbid = old[key]['db_id']
print('book:', key)
print('old db id:', dbid)

db = req('https://api.notion.com/v1/databases/%s' % dbid)
print('before: in_trash=%s archived=%s props=%s' % (
    db.get('in_trash'), db.get('archived'),
    {k: v['type'] for k, v in db.get('properties', {}).items()}))

r1 = req('https://api.notion.com/v1/databases/%s' % dbid, 'PATCH', {'in_trash': False})
if '__err__' in r1:
    print('RESTORE FAILED:', r1)
    sys.exit(1)
print('restored -> in_trash=%s' % r1.get('in_trash'))
time.sleep(1)

rows, err = query(dbid)
print('query rows:', len(rows), 'err', err)
filled = {}
for x in rows:
    pr = x.get('properties', {})
    for k, v in pr.items():
        filled.setdefault(k, 0)
        if ptext(v).strip():
            filled[k] += 1
print('filled per column:', filled)
if rows:
    print('sample:', {k: ptext(v)[:50] for k, v in rows[0].get('properties', {}).items()})

out = {'book': key, 'old_db_id': dbid, 'rows': []}
for x in rows:
    pr = x.get('properties', {})
    out['rows'].append({'page_id': x['id'],
                        'values': {k: ptext(v) for k, v in pr.items()}})
fn = 'bk_recovered_%s.json' % key.split(':')[0].replace(' ', '_')[:30]
json.dump(out, open(fn, 'w'), ensure_ascii=False, indent=1)
print('saved ->', fn)

r2 = req('https://api.notion.com/v1/databases/%s' % dbid, 'PATCH', {'in_trash': True})
print('re-trashed -> in_trash=%s' % r2.get('in_trash'))
