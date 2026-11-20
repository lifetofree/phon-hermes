#!/usr/bin/env python3
"""
สกัดข้อมูลบทจาก child DB เก่า (ที่ถูกย้ายเข้า Trash ตอน rebuild) ทั้งหมด
เพื่อ (1) เป็น backup (2) ตรวจว่าข้อมูลหายไหม

วิธี: PATCH in_trash=false -> query อ่าน -> PATCH in_trash=true (คืนสภาพเดิม)
เขียนฐานชั่วคราวเฉพาะการ "ย้ายเข้า/ออก Trash" ของ DB ที่ถูกลบไปแล้ว ไม่แก้ข้อมูลแถวใด ๆ
"""
import os, json, time, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
HDR = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
       'Content-Type': 'application/json'}
OUT = 'bk_old_chapters_backup.json'


def req(url, method='GET', body=None, tries=8):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers=HDR, method=method)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(min(2 + i * 2, 30))
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


old = json.load(open('chapters2.json'))
backup = {}
for o in old:
    book = o['book']
    dbid = o['db_id']
    db = req('https://api.notion.com/v1/databases/%s' % dbid)
    was_trash = bool(db.get('in_trash'))
    if not was_trash:
        print('%-46s | not in trash, skip' % book[:46])
        continue
    r = req('https://api.notion.com/v1/databases/%s' % dbid, 'PATCH', {'in_trash': False})
    if '__err__' in r:
        print('%-46s | RESTORE FAILED %s' % (book[:46], r))
        continue
    time.sleep(0.6)
    rows, err = query(dbid)
    props = {k: v['type'] for k, v in r.get('properties', {}).items()}
    data = []
    for x in rows:
        pr = x.get('properties', {})
        data.append({'page_id': x['id'],
                     'values': {k: ptext(v) for k, v in pr.items()}})
    backup[book] = {'old_db_id': dbid, 'props': props, 'n': len(rows),
                    'rows': data, 'err': err}
    json.dump(backup, open(OUT, 'w'), ensure_ascii=False, indent=1)
    back = req('https://api.notion.com/v1/databases/%s' % dbid, 'PATCH', {'in_trash': True})
    time.sleep(0.6)
    print('%-46s | rows=%-3d props=%s | re-trash=%s' % (
        book[:46], len(rows), list(props.keys()), back.get('in_trash')))

print('\nbacked up %d books -> %s' % (len(backup), OUT))
tot = sum(b['n'] for b in backup.values())
print('total rows extracted:', tot)
