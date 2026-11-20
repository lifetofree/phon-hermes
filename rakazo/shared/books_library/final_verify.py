"""ตรวจสถานะสุดท้ายของฐาน Books Library: body = [ปก, Chapter List, ...] + page cover"""
import os, json, urllib.request, urllib.error, subprocess
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'


def req(path, data=None, headers=None, method=None):
    h = dict(H)
    if headers:
        h.update(headers)
    r = urllib.request.Request('https://api.notion.com/v1' + path, data=data, headers=h, method=method)
    try:
        return json.load(urllib.request.urlopen(r, timeout=120))
    except urllib.error.HTTPError as e:
        return {'__error__': e.code, 'msg': e.read().decode()[:200]}


def q(ds):
    out, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur: b['start_cursor'] = cur
        r = req('/data_sources/%s/query' % ds, json.dumps(b).encode(), None, 'POST')
        out += r['results']
        if not r.get('has_more'):
            return out
        cur = r['next_cursor']


def title(p):
    for k, v in (p.get('properties') or {}).items():
        if v.get('type') == 'title':
            return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))
    return ''


rows = q(PDS)
c = Counter()
bad = []
for p in rows:
    t = title(p)
    ks = req('/blocks/%s/children' % p['id']).get('results', [])
    types = [b['type'] for b in ks]
    img_i = types.index('image') if 'image' in types else -1
    cdb_i = types.index('child_database') if 'child_database' in types else -1
    has_pc = bool(p.get('cover'))
    ok = img_i == 0 and cdb_i >= 0 and has_pc
    if ok:
        c['ครบ: ปกบล็อกแรก + Chapter List + page cover'] += 1
    else:
        why = []
        if img_i != 0:
            why.append('image@%s' % (img_i if img_i >= 0 else 'none'))
        if cdb_i < 0:
            why.append('no_chapter_list')
        if not has_pc:
            why.append('no_page_cover')
        bad.append((t, ', '.join(why)))
        c['ยังไม่ครบ: ' + ', '.join(why)] += 1

print('=== สถานะสุดท้าย 251 เล่ม ===')
for k, v in c.most_common():
    print('  %-52s %d' % (k, v))
print()
if bad:
    print('=== ที่ยังต้องแก้ ===')
    for t, w in bad:
        print('  %-52s %s' % (t[:52], w))
else:
    print('ทุกเล่มครบโครงสร้างแล้ว')
