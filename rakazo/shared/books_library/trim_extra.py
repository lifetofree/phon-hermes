"""ลบบล็อกเกินให้ตรงกับ snapshot (แบบ paginate ถูกต้อง)
เก็บตัวแรกของแต่ละ signature ตามจำนวนที่ snapshot ต้องการ ที่เหลือ archive
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


def sig_live(b):
    t = b.get('type')
    if t in ('child_database', 'image'):
        return None
    return (t, norm(''.join(x.get('plain_text', '') for x in (b.get(t, {}).get('rich_text') or []))))


def sig_snap(it):
    if it['type'] in ('child_database', 'image'):
        return None
    s = norm(''.join(x.get('plain_text', '') for x in (it.get('payload', {}).get('rich_text') or [])))
    return (it['type'], s) if s else None


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


tot = 0
for p in out:
    snap = store.get(p['id'])
    if not snap:
        continue
    pid = p['id']

    want = Counter()

    def w_walk(items):
        for it in items:
            s = sig_snap(it)
            if s:
                want[s] += 1
            if it.get('children'):
                w_walk(it['children'])
    w_walk(snap)

    # ไล่บล็อกทั้งหมดแบบ paginate เก็บลำดับ (เก็บตัวแรกไว้)
    live = []

    def l_walk(bid):
        for b in kids_all(bid):
            s = sig_live(b)
            if s:
                live.append((s, b['id']))
            if b.get('has_children'):
                l_walk(b['id'])
    l_walk(pid)

    have = Counter(s for s, _ in live)
    if not (have - want):
        continue

    keep = Counter(want)
    removed = 0
    for s, bid in live:
        if keep[s] > 0:
            keep[s] -= 1
            continue
        req('/blocks/%s' % bid, json.dumps({'archived': True}).encode(), None, 'PATCH')
        removed += 1
        time.sleep(0.22)
    tot += removed
    print('  %-46s ลบ %d บล็อกเกิน' % (title(p)[:46], removed), flush=True)
    time.sleep(0.4)

print('\n=== สรุป ===')
print('  ลบบล็อกเกินรวม:', tot)
