#!/usr/bin/env python3
"""ตรวจความพร้อมของ rollback + ดู saved views ที่อ้างชื่อ tag เก่า (read-only)"""
import os, json, urllib.request, urllib.error

TOK = os.environ['NOTION_TOKEN']
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
SNAP = '../../bots/cmwj2kqkfl1cdznjl9fxz39ik/books_tags_snapshot.json'


def api(path, ver='2025-09-03'):
    req = urllib.request.Request(
        'https://api.notion.com/v1' + path,
        headers={'Authorization': 'Bearer ' + TOK, 'Notion-Version': ver,
                 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {'__error__': e.code, 'body': e.read().decode()[:300]}


print('=== 1) snapshot พร้อม rollback ไหม ===')
snap = json.load(open(SNAP))
rows = snap.get('rows', snap if isinstance(snap, list) else [])
print('snapshot keys      :', list(snap.keys()) if isinstance(snap, dict) else 'list')
print('rows in snapshot   :', len(rows))
if rows:
    print('sample row         :', {k: rows[0][k] for k in list(rows[0])[:5]})
    distinct = sorted({t for r in rows for t in r.get('tags', [])})
    print('distinct tags      :', len(distinct))
    print('rows w/ empty tags :', sum(1 for r in rows if not r.get('tags')))

print()
print('=== 2) views ที่อ้างชื่อ tag เก่า ===')
for ver in ('2025-09-03', '2022-06-28'):
    ds = api('/data_sources/%s' % PDS, ver)
    if '__error__' in ds:
        print('  ver %s -> ERROR %s %s' % (ver, ds['__error__'], ds['body'][:120]))
        continue
    print('  ver %s -> keys: %s' % (ver, list(ds.keys())))
    v = ds.get('views')
    if v:
        print('    views:', json.dumps(v, ensure_ascii=False)[:1500])
        break
