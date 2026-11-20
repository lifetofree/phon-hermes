"""BK audit: read-only live scan of Books Library. python3 bk_audit_live.py"""
import os, json, urllib.request, urllib.error, time
from collections import Counter
TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
API = 'https://api.notion.com/v1'

def req(path, data=None, method=None, tries=6):
    for i in range(tries):
        r = urllib.request.Request(API + path, data=data, headers=H, method=method)
        try:
            return json.load(urllib.request.urlopen(r, timeout=120))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(2 ** i); continue
            return {'__error__': e.code, 'msg': e.read().decode()[:300]}
        except Exception as e:
            if i < tries - 1:
                time.sleep(2 ** i); continue
            return {'__error__': 'exc', 'msg': str(e)[:300]}

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

def blocks(pid):
    out, cur = [], None
    while True:
        p = '/blocks/%s/children?page_size=100' % pid
        if cur: p += '&start_cursor=' + cur
        r = req(p)
        if '__error__' in r: return r
        out += r['results']
        if not r.get('has_more'): return out
        cur = r['next_cursor']

def plain(rt): return ''.join(x.get('plain_text', '') for x in (rt or []))

def title_of(pr):
    for k, v in (pr or {}).items():
        if v['type'] == 'title': return plain(v['title'])
    return ''

ds = req('/data_sources/%s' % PDS)
props = ds.get('properties', {})
print('=== SCHEMA ===')
for k, v in props.items():
    print('  %-32s %s' % (k, v['type']))
    if v['type'] in ('multi_select', 'select'):
        print('      options=%d' % len(v.get(v['type'], {}).get('options', [])))
rows = q(PDS)
print('\n=== ROWS ===')
print('  rows = %d' % len(rows))
eg, st = Counter(), Counter()
used = Counter(); slots = 0; no_tag = []; no_auth = []; no_eg = []; no_st = []
for p in rows:
    pr = p['properties']; t = title_of(pr)
    e = pr.get('Energy Group', {}); s = pr.get('Status', {})
    en = (e.get('select') or {}).get('name'); sn = (s.get('select') or {}).get('name')
    eg[en] += 1; st[sn] += 1
    if not en: no_eg.append(t)
    if not sn: no_st.append(t)
    if not plain(pr.get('Author', {}).get('rich_text', [])): no_auth.append(t)
    tg = pr.get('Tags', {})
    names = [o['name'] for o in tg.get('multi_select', [])] if tg['type'] == 'multi_select' else \
            [x for x in plain(tg.get('rich_text', [])).split() if x]
    slots += len(names)
    for n in names: used[n] += 1
    if not names: no_tag.append(t)
print('  Energy Group:', dict(eg))
print('  Status:', dict(st))
print('  tag slots=%d distinct_used=%d rows_no_tag=%d' % (slots, len(used), len(no_tag)))
print('  missing Author=%d Energy=%d Status=%d' % (len(no_auth), len(no_eg), len(no_st)))
if no_tag: print('  NO-TAG:', no_tag[:20])
cdbs = []
for p in rows:
    bs = blocks(p['id'])
    if isinstance(bs, dict): continue
    for i, b in enumerate(bs):
        if b['type'] == 'child_database':
            cdbs.append({'book': title_of(p['properties']), 'page_id': p['id'],
                         'ds_id': b['id'], 'title': b['child_database']['title'], 'index': i})
print('\n=== CHILD DB ===')
print('  child_db blocks = %d' % len(cdbs))
for name, n in Counter(c['title'] for c in cdbs).most_common():
    print('   %-34r x%d' % (name, n))
json.dump({'cdbs': cdbs, 'eg': dict(eg), 'status': dict(st), 'tags_used': dict(used),
           'slots': slots, 'no_tag': no_tag}, open('bk_audit_live_out.json', 'w'), ensure_ascii=False, indent=1)
print('\nwrote bk_audit_live_out.json')
