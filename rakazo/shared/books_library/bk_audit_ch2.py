"""BK: scan child DB rows/status/schema (read-only). API 2025-09-03."""
import os, json, urllib.request, urllib.error, time
from collections import Counter
TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
API = 'https://api.notion.com/v1'
OUT = 'bk_audit_ch2_out.json'

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
res = []
for i, c in enumerate(cdbs):
    db = req('/databases/%s' % c['ds_id'])
    dss = (db.get('data_sources') or []) if '__error__' not in db else []
    if not dss:
        res.append({'book': c['book'], 'title': c['title'], 'db_id': c['ds_id'], 'rows': -1, 'err': 'no ds'})
        continue
    dsi = dss[0]['id']
    rows = q(dsi)
    n = len(rows) if isinstance(rows, list) else -1
    schema = {}
    if n >= 0:
        sch = req('/data_sources/%s' % dsi)
        schema = {k: v['type'] for k, v in (sch.get('properties') or {}).items()} if '__error__' not in sch else {'ERR': str(sch)}
    stat = Counter(); notes_col = None; tkind = None
    if n > 0:
        pr0 = rows[0]['properties']
        for k, v in pr0.items():
            if v['type'] == 'title':
                s = plain(v['title']); tkind = 'num' if s.strip().isdigit() else ('name' if s.strip() else 'empty')
        for r in rows:
            for k, v in r['properties'].items():
                if k.strip().lower() == 'status' and v['type'] == 'select':
                    stat[(v.get('select') or {}).get('name')] += 1
        for k in pr0:
            kl = k.lower()
            if 'note' in kl or 'summary' in kl or 'core message' in kl: notes_col = k
    res.append({'book': c['book'], 'title': c['title'], 'db_id': c['ds_id'], 'ds_id': dsi, 'rows': n,
                'schema': schema, 'status': {str(k): v for k, v in stat.items()},
                'notes_col': notes_col, 'title_kind': tkind})
    if (i + 1) % 10 == 0:
        print('  %d/%d' % (i + 1, len(cdbs)), flush=True)
        json.dump(res, open(OUT, 'w'), ensure_ascii=False, indent=1)
json.dump(res, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('WROTE', OUT, flush=True)
print('with rows:', sum(1 for r in res if r.get('rows', 0) > 0), 'rows:', sum(r.get('rows', 0) for r in res), flush=True)
st = Counter()
for r in res:
    for k, v in (r.get('status') or {}).items(): st[k] += v
print('chapter Status:', dict(st), flush=True)
for s, n in Counter(json.dumps(r.get('schema'), sort_keys=True, ensure_ascii=False) for r in res).most_common(12):
    print('  x%d %s' % (n, s[:260]), flush=True)
