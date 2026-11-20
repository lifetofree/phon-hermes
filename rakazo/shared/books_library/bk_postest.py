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
import json
B = json.load(open('bk_body_check_out.json'))
pid = [x for x in B if x['book'] == 'Essentialism'][0]['page_id']
bs = kids(pid)
img = [b for b in bs if b['type'] == 'image'][0]
body = {'parent': {'type': 'page_id', 'page_id': pid},
        'title': [{'type': 'text', 'text': {'content': 'ZZ POSITION TEST'}}],
        'is_inline': True, 'after': img['id']}
r = rq('/databases', json.dumps(body).encode(), 'POST')
print('create:', r.get('__error__', 'OK'), str(r.get('msg', ''))[:200])
nid = r.get('id')
if nid:
    time.sleep(2)
    bs2 = kids(pid)
    print('order now:', [(i, b['type'], b.get('child_database', {}).get('title', '')) for i, b in enumerate(bs2[:5])])
    a = rq('/blocks/%s' % nid, json.dumps({'archived': True}).encode(), 'PATCH')
    print('archive test db:', a.get('__error__', 'OK'))
