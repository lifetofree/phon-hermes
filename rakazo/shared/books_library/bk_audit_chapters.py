"""BK: scan every child DB (Chapter List) rows/status/notes columns. read-only.
usage: python3 bk_audit_chapters.py [out.json]
"""
import os, json, urllib.request, urllib.error, time, sys
from collections import Counter
TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
API = 'https://api.notion.com/v1'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'bk_audit_chapters_out.json'

def req(path, data=None, method=None, tries=7):
    for i in range(tries):
        r = urllib.request.Request(API + path, data=data, headers=H, method=method)
        try:
            return json.load(urllib.request.urlopen(r, timeout=120))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(min(2 ** i, 20)); continue
            return {'__error__': e.code, 'msg': e.read().decode()[:200]}
        except Exception as e:
            if i < tries - 1:
                time.sleep(min(2 ** i, 20)); continue
            return {'__error__': 'exc', 'msg': str(e)[:200]}

def q(ds):
    out, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur: b['start_cursor'] = cur
        r = req('/data_sources/%s/query' % ds, json.dumps(b).encode(), 'POST')
        if '__error__' in r: return r
        out += r['results']
        if not r.get('has_more'): return out
        cur = r['next_cursor']

def plain(rt): return ''.join(x.get('plain_text', '') for x in (rt or []))

cdbs = json.load(open('bk_audit_live_out.json'))['cdbs']
print('child dbs to scan:', len(cdbs), flush=True)
res = []
for i, c in enumerate(cdbs):
    ds = req('/data_sources/%s' % c['ds_id'])
    schema = {k: v['type'] for k, v in (ds.get('properties') or {}).items()} if '__error__' not in ds else {'ERR': ds}
    rows = q(c['ds_id'])
    n = len(rows) if isinstance(rows, list) else -1
    stat = Counter(); notes_col = None; title_kind = None
    if n > 0:
        pr0 = rows[0]['properties']
        for k, v in pr0.items():
            if v['type'] == 'title':
                sample = plain(v['title'])
                title_kind = 'number' if sample.strip().isdigit() else ('name' if sample.strip() else 'empty')
        for r in rows:
            pr = r['properties']
            sv = None
            for k, v in pr.items():
                if k.lower() in ('status',) and v['type'] == 'select':
                    sv = (v.get('select') or {}).get('name')
            stat[sv] += 1
        for k, v in pr0.items():
            if 'note' in k.lower() or 'summary' in k.lower() or 'core message' in k.lower():
                notes_col = k
    res.append({'book': c['book'], 'title': c['title'], 'ds_id': c['ds_id'], 'rows': n,
                'schema': schema, 'status': {str(k): v for k, v in stat.items()},
                'notes_col': notes_col, 'title_kind': title_kind})
    if (i + 1) % 10 == 0:
        print('  %d/%d done' % (i + 1, len(cdbs)), flush=True)
        json.dump(res, open(OUT, 'w'), ensure_ascii=False, indent=1)
json.dump(res, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('WROTE', OUT, flush=True)
tot = sum(r['rows'] for r in res if r['rows'] > 0)
print('dbs with rows:', sum(1 for r in res if r['rows'] > 0), '| total rows:', tot, flush=True)
st = Counter()
for r in res:
    for k, v in (r['status'] or {}).items(): st[k] += v
print('chapter Status tally:', dict(st), flush=True)
print('schema variants:', Counter(tuple(sorted((r['schema'] or {}).items())) for r in res).most_common(6), flush=True)
