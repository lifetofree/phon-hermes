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
import json
D = json.load(open('bk_audit_ch2_out.json'))
for x in D:
    sch = x.get('schema') or {}
    for old, new in [('Core Message (สรุปแก่นฉบับ PHON)', 'Core Message (ฉบับ PHON)'),
                     ('Chapter Title', 'Chapter Title (Original)')]:
        if old in sch and new not in sch:
            print('rename', x['book'][:30], old, '->', new)
            r = P('/data_sources/%s' % x['ds_id'], {'properties': {old: {'name': new}}})
            print('   ->', r.get('__error__', 'OK'), str(r.get('msg', ''))[:120])
            time.sleep(0.4)
    if x['book'] == 'Essentialism':
        rows = q(x['ds_id'])
        c = {}
        for rr in rows:
            sv = rr['properties'].get('Status')
            nm = (sv.get('select') or {}).get('name') if sv else None
            c[nm] = c.get(nm, 0) + 1
        print('Essentialism rows', len(rows), c)
