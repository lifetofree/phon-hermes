#!/usr/bin/env python3
"""dump ทุกแถวของ child DB ที่ระบุ เพื่อดูว่าคอลัมน์ไหนมีข้อมูลจริง"""
import os, sys, json, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
HDR = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
       'Content-Type': 'application/json'}


def req(url, method='GET', body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, headers=HDR, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {'__err__': e.code}


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


scan = {r['title']: r for r in json.load(open('bk_childdb_scan.json'))}
targets = [t for t in sys.argv[1:]] if len(sys.argv) > 1 else []
for name in targets:
    r = scan.get(name)
    if not r:
        print('!! not found:', name)
        continue
    dbid = r['child_dbs'][0]['id']
    db = req('https://api.notion.com/v1/databases/%s' % dbid)
    print('=' * 78)
    print(name[:60], '| props:', {k: v['type'] for k, v in db.get('properties', {}).items()})
    rows, err = query(dbid)
    print('rows:', len(rows), 'err', err)
    for i, x in enumerate(rows[:4]):
        pr = x.get('properties', {})
        print('  row%d: %s' % (i, {k: ptext(v)[:45] for k, v in pr.items()}))
    # สรุปว่าคอลัมน์ไหนมีค่าบ้าง
    cols = {}
    for x in rows:
        for k, v in x.get('properties', {}).items():
            cols.setdefault(k, 0)
            if ptext(v).strip():
                cols[k] += 1
    print('  filled per column:', cols)
