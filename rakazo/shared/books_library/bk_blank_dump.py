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
def pl(rt): return ''.join(x.get('plain_text', '') for x in (rt or []))
def q(ds):
    o, c = [], None
    while True:
        b = {'page_size': 100}
        if c: b['start_cursor'] = c
        r = rq('/data_sources/%s/query' % ds, json.dumps(b).encode(), 'POST')
        if '__error__' in r: return r
        o += r['results']
        if not r.get('has_more'): return o
        c = r['next_cursor']
def P(p, body): return rq(p, json.dumps(body).encode(), 'PATCH')
import re
PART_RE = re.compile(r'^\s*(?:\U0001F4C4\s*)?(PART|Part|Section|SECTION)\b', re.I)
D = json.load(open('bk_audit_ch2_out.json'))
for x in D:
    if x.get('rows', 0) <= 0: continue
    sch = x.get('schema') or {}
    if 'Status' not in sch: continue
    rows = q(x['ds_id'])
    if not isinstance(rows, list): continue
    for rr in rows:
        pr = rr['properties']
        sv = pr.get('Status')
        nm = (sv.get('select') or {}).get('name') if sv else None
        if nm: continue
        ti = ''
        for k, v in pr.items():
            if v['type'] == 'title': ti = pl(v['title'])
        core = ''
        for k, v in pr.items():
            if v['type'] == 'rich_text' and 'core message' in k.lower(): core = pl(v['rich_text'])
        print('%-30s | %-44s | PART=%s | notes=%s' % (x['book'][:30], ti[:44], bool(PART_RE.match(ti)), 'yes' if core.strip() else 'no'))
