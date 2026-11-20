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
import urllib.request as _u
def q(ds):
    o, c = [], None
    while True:
        b = {'page_size': 100}
        if c:
            b['start_cursor'] = c
        rq = _u.Request('https://api.notion.com/v1/data_sources/%s/query' % ds,
                        data=json.dumps(b).encode(), headers=H, method='POST')
        try:
            r = json.load(_u.urlopen(rq, timeout=90))
        except Exception as ex:
            print('err', ex)
            break
        o += r.get('results', [])
        if not r.get('has_more'):
            break
        c = r.get('next_cursor')
    return o
import json
d = json.load(open('bk_audit_ch2_out.json'))
es = [x for x in d if x['book'] == 'Essentialism' and x.get('rows', 0) > 0]
print('dbs:', [(x['db_id'], x['ds_id'], x['rows']) for x in es])
def rowsig(ds):
    out = []
    for r in q(ds):
        vals = {}
        for k, v in r['properties'].items():
            if v['type'] == 'title':
                vals[k] = pl(v['title'])
            elif v['type'] == 'rich_text':
                vals[k] = pl(v['rich_text'])
            elif v['type'] == 'select':
                vals[k] = (v.get('select') or {}).get('name')
        out.append(json.dumps(vals, ensure_ascii=False, sort_keys=True))
    return out
a = rowsig(es[0]['ds_id'])
b = rowsig(es[1]['ds_id'])
print('rows', len(a), len(b))
print('identical sets:', set(a) == set(b))
print('identical lists:', a == b)
oa = [x for x in a if x not in set(b)]
ob = [x for x in b if x not in set(a)]
print('only A:', len(oa))
for x in oa[:5]:
    print('   A', x[:140])
print('only B:', len(ob))
for x in ob[:5]:
    print('   B', x[:140])
