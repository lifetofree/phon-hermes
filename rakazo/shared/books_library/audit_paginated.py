"""ตรวจแบบ PAGINATE ถูกต้อง: นับบล็อกทั้งหมด + เทียบ snapshot
แก้บั๊ก: เดิม kids() ดึงแค่หน้าแรก (100) -> นับผิด
"""
import os, json, time, urllib.request, urllib.error
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'


def req(path, data=None, headers=None, method=None, tries=6):
    h = dict(H)
    if headers:
        h.update(headers)
    for a in range(tries):
        r = urllib.request.Request('https://api.notion.com/v1' + path, data=data, headers=h, method=method)
        try:
            return json.load(urllib.request.urlopen(r, timeout=120))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and a < tries - 1:
                time.sleep(min(25, 2 * (2 ** a)))
                continue
            return {'__error__': e.code, 'msg': e.read().decode()[:250]}
        except Exception as e:
            if a < tries - 1:
                time.sleep(2)
                continue
            return {'__error__': 'EXC', 'msg': repr(e)[:200]}
    return {'__error__': 'MAX'}


def kids_all(pid):
    """ดึงลูกทั้งหมดแบบ paginate"""
    out, cur = [], None
    while True:
        url = '/blocks/%s/children?page_size=100' % pid
        if cur:
            url += '&start_cursor=' + cur
        r = req(url)
        if '__error__' in r:
            break
        out += r.get('results', [])
        if not r.get('has_more'):
            break
        cur = r.get('next_cursor')
    return out


def norm(s):
    return ' '.join((s or '').split())


def live_counts(pid):
    c = Counter()
    n = [0]

    def walk(bid):
        for b in kids_all(bid):
            t = b.get('type')
            if t in ('child_database', 'image'):
                continue
            s = norm(''.join(x.get('plain_text', '') for x in (b.get(t, {}).get('rich_text') or [])))
            if s:
                c[(t, s)] += 1
                n[0] += 1
            if b.get('has_children'):
                walk(b['id'])
    walk(pid)
    return c, n[0]


def snap_counts(blocks):
    c = Counter()
    n = [0]

    def walk(items):
        for it in items:
            if it['type'] in ('child_database', 'image'):
                continue
            s = norm(''.join(x.get('plain_text', '') for x in (it.get('payload', {}).get('rich_text') or [])))
            if s:
                c[(it['type'], s)] += 1
                n[0] += 1
            if it.get('children'):
                walk(it['children'])
    walk(blocks)
    return c, n[0]


store = {}
for f in ['layout_snapshot.json', 'reorder_snapshot.json']:
    if os.path.exists(f):
        for k, v in json.load(open(f)).items():
            blocks = v.get('blocks', []) if isinstance(v, dict) else v
            if blocks:
                store.setdefault(k, blocks)

out, cur = [], None
while True:
    b = {'page_size': 100}
    if cur: b['start_cursor'] = cur
    r = req('/data_sources/%s/query' % PDS, json.dumps(b).encode(), None, 'POST')
    out += r.get('results', [])
    if not r.get('has_more'): break
    cur = r.get('next_cursor')


def title(p):
    for k, v in (p.get('properties') or {}).items():
        if v.get('type') == 'title':
            return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))


over = under = same = 0
worst = []
for p in out:
    snap = store.get(p['id'])
    if not snap:
        continue
    cs, ns = snap_counts(snap)
    cl, nl = live_counts(p['id'])
    d = nl - ns
    if d > 0:
        over += 1
        worst.append((title(p)[:42], ns, nl, d, 'เกิน'))
    elif d < 0:
        under += 1
        worst.append((title(p)[:42], ns, nl, d, 'ขาด'))
    else:
        same += 1
print('=== ตรวจแบบ paginate (ถูกต้อง) ===')
print('  live เท่ากับ snapshot:', same, '| เกิน:', over, '| ขาด:', under)
print()
worst.sort(key=lambda x: abs(x[3]))
for t, ns, nl, d, kind in worst[:20]:
    print('   %-44s snapshot=%-5d live=%-5d (%+d) %s' % (t, ns, nl, d, kind))
