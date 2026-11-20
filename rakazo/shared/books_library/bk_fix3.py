import os, sys, json, time, urllib.request, urllib.error
T = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + T, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
APPLY = '--apply' in sys.argv
def rq(p, d=None, m='GET', n=7):
    for i in range(n):
        r = urllib.request.Request('https://api.notion.com/v1' + p, data=d, headers=H, method=m)
        try:
            return json.load(urllib.request.urlopen(r, timeout=90))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < n - 1:
                time.sleep(2 ** i); continue
            return {'__error__': e.code, 'msg': e.read().decode()[:150]}
        except Exception as e:
            if i < n - 1:
                time.sleep(2); continue
            return {'__error__': 'exc', 'msg': str(e)[:100]}
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
D = json.load(open('bk_audit_ch2_out.json'))
OPT = [{'name': '⬜ QUEUED'}, {'name': '⏳ LOADING...'}, {'name': '✅ INSTALLED'}]
for x in D:
    sch = x.get('schema') or {}
    if x.get('rows', 0) > 0 or 'Status' in sch: continue
    add = {'Status': {'select': {'options': OPT}},
           'Core Message (ฉบับ PHON)': {'rich_text': {}},
           'Chapter Title (Original)': {'rich_text': {}}}
    print('normalize', x['book'][:36], list(sch))
    r = P('/data_sources/%s' % x['ds_id'], {'properties': add})
    print('   ->', r.get('__error__', 'OK'), str(r.get('msg', ''))[:120])
    time.sleep(0.4)
