import os, json, urllib.request, urllib.error, time
T = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + T, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
def rq(p, d=None, m='GET', n=7):
    for i in range(n):
        r = urllib.request.Request('https://api.notion.com/v1' + p, data=d, headers=H, method=m)
        try:
            return json.load(urllib.request.urlopen(r, timeout=90))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < n - 1:
                time.sleep(2 ** i); continue
            return {'__error__': e.code}
        except Exception:
            if i < n - 1:
                time.sleep(2); continue
            return {'__error__': 'exc'}
def kids(pid):
    o, c = [], None
    while True:
        u = '/blocks/%s/children?page_size=100' % pid
        if c:
            u += '&start_cursor=' + c
        r = rq(u)
        if '__error__' in r:
            break
        o += r.get('results', [])
        if not r.get('has_more'):
            break
        c = r.get('next_cursor')
    return o
def pl(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))
def query():
    o, c = [], None
    while True:
        b = {'page_size': 100}
        if c:
            b['start_cursor'] = c
        r = rq('/data_sources/%s/query' % PDS, json.dumps(b).encode(), 'POST')
        if '__error__' in r:
            break
        o += r.get('results', [])
        if not r.get('has_more'):
            break
        c = r.get('next_cursor')
    return o
rows = query()
res = []
for p in rows:
    pr = p['properties']
    ti = ''
    for k, v in pr.items():
        if v['type'] == 'title':
            ti = pl(v['title'])
            break
    bs = kids(p['id'])
    types = [b['type'] for b in bs]
    res.append({'book': ti, 'nblocks': len(bs),
                'img0': types[0] if types else None,
                'img_idx': types.index('image') if 'image' in types else -1,
                'cdb_idx': types.index('child_database') if 'child_database' in types else -1,
                'page_cover': bool(p.get('cover')), 'page_id': p['id']})
json.dump(res, open('bk_body_check_out.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print('books', len(res))
print('first block type:', Counter(r['img0'] for r in res).most_common())
print('image index:', Counter(r['img_idx'] for r in res).most_common(6))
print('child_db index:', Counter(r['cdb_idx'] for r in res).most_common(6))
print('page cover:', Counter(r['page_cover'] for r in res).most_common())
bad = [r for r in res if r['img_idx'] != 0 or r['cdb_idx'] < 0 or not r['page_cover']]
print('NOT ok:', len(bad))
for r in bad[:15]:
    print('   ', r['book'][:44], r['img0'], r['img_idx'], r['cdb_idx'], r['page_cover'], r['nblocks'])
