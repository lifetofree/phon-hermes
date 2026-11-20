#!/usr/bin/env python3
"""
เทียบ child DB เก่า (อยู่ใน Trash) กับของใหม่ 'Chapter List' ว่าข้อมูลหายไหม
read-only
"""
import os, json, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
V = '2022-06-28'
HDR = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': V,
       'Content-Type': 'application/json'}


def req(url, method='GET', body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, headers=HDR, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {'__err__': e.code, 'body': e.read().decode()[:200]}


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
    if not v:
        return ''
    t = v.get('type')
    if t == 'title':
        return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))
    if t == 'rich_text':
        return ''.join(x.get('plain_text', '') for x in (v.get('rich_text') or []))
    if t == 'select':
        return (v.get('select') or {}).get('name') or ''
    if t == 'multi_select':
        return ','.join(x['name'] for x in (v.get('multi_select') or []))
    return ''


old = {c['book']: c for c in json.load(open('chapters2.json'))}
scan = {r['title']: r for r in json.load(open('bk_childdb_scan.json'))}

for name in list(old)[:6]:
    o = old[name]
    n = scan.get(name)
    print('=' * 70)
    print(name[:60])
    odb = req('https://api.notion.com/v1/databases/%s' % o['db_id'])
    print('  OLD db: trash=%s arch=%s props=%s' % (
        odb.get('in_trash'), odb.get('archived'),
        {k: v['type'] for k, v in odb.get('properties', {}).items()}))
    orows, oerr = query(o['db_id'])
    print('  OLD rows:', len(orows), 'err', oerr)
    if orows:
        pr = orows[0].get('properties', {})
        print('    sample row props:', {k: (v['type'], ptext(v)[:40]) for k, v in pr.items()})
    if n and n['child_dbs']:
        ndb = req('https://api.notion.com/v1/databases/%s' % n['child_dbs'][0]['id'])
        print('  NEW db: trash=%s props=%s' % (
            ndb.get('in_trash'), {k: v['type'] for k, v in ndb.get('properties', {}).items()}))
        nrows, nerr = query(n['child_dbs'][0]['id'])
        print('  NEW rows:', len(nrows), 'err', nerr)
        if nrows:
            pr = nrows[0].get('properties', {})
            print('    sample row props:', {k: (v['type'], ptext(v)[:40]) for k, v in pr.items()})
