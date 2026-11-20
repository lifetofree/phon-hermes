#!/usr/bin/env python3
"""ลองหา saved views ผ่าน endpoint ต่าง ๆ (read-only)"""
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
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {'__error__': e.code, 'body': e.read().decode()[:160]}
    except Exception as e:
        return {'__error__': 'EXC', 'body': str(e)[:160]}


paths = [
    '/databases/%s' % DB,
    '/data_sources/%s' % PDS,
    '/databases/%s/views' % DB,
    '/data_sources/%s/views' % PDS,
    '/databases/%s/queries' % DB,
    '/data_sources/%s/queries' % PDS,
    '/data_sources/%s/pages' % PDS,
]
for p in paths:
    r = api(p)
    if '__error__' in r:
        print('%-58s -> ERR %s %s' % (p, r['__error__'], r['body'][:110].replace('\n', ' ')))
    else:
        keys = list(r.keys())
        extra = ''
        if 'views' in r:
            extra = ' views=%s' % json.dumps(r['views'], ensure_ascii=False)[:400]
        if 'results' in r:
            extra = ' results=%d' % len(r['results'])
        print('%-58s -> OK keys=%s%s' % (p, keys, extra))
