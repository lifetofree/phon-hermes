#!/usr/bin/env python3
"""หา saved views/queries ของ Books Library ที่อ้างชื่อ tag เก่า (read-only)"""
import os, json, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
DB = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'


def api(path, ver='2025-09-03'):
    req = urllib.request.Request(
        'https://api.notion.com/v1' + path,
        headers={'Authorization': 'Bearer ' + TOK, 'Notion-Version': ver,
                 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {'__error__': e.code, 'body': e.read().decode()[:200]}


for path in ('/databases/%s/queries' % DB,
             '/data_sources/%s/queries' % PDS,
             '/data_sources/%s/views' % PDS):
    r = api(path)
    if '__error__' in r:
        print('%-58s -> ERR %s %s' % (path, r['__error__'], r['body'][:100]))
    else:
        print('%-58s -> OK keys=%s' % (path, list(r.keys())))
        res = r.get('results', [])
        print('   count:', len(res))
        for q in res:
            name = q.get('name') or (q.get('title') or {}).get('title') or q.get('id')
            print('   -', name, '|', json.dumps(q.get('filter') or q.get('query') or {}, ensure_ascii=False)[:200])
