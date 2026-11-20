"""ปรับ body ให้ตรงกับ snapshot ต้นฉบับ: เติมที่ขาด + ลบที่เกิน (ตาม signature)

วิธีเติมที่ขาด (สำคัญ):
  - เดินตาม snapshot ตามลำดับ
  - ถ้า block ที่หายเป็นลูกของ parent ที่ match ได้ -> ใส่เป็นลูกของ parent นั้น (ถ้า parent รับได้)
  - ถ้า parent รับลูกไม่ได้ (heading_*) -> ใส่ต่อท้าย parent ที่ระดับเดียวกัน (flatten 1 ชั้น)
  - ถ้าไม่มี parent ที่ match -> ใส่ต่อท้าย Chapter List
"""
import os, json, time, urllib.request, urllib.error
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
PDS = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
CAN_CHILDREN = {'paragraph', 'bulleted_list_item', 'numbered_list_item', 'to_do',
                'quote', 'toggle', 'callout', 'code'}
STATE = {'add': 0, 'del': 0}


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


def q(ds):
    out, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur: b['start_cursor'] = cur
        r = req('/data_sources/%s/query' % ds, json.dumps(b).encode(), None, 'POST')
        if '__error__' in r:
            return out
        out += r.get('results', [])
        if not r.get('has_more'):
            return out
        cur = r.get('next_cursor')


def title(p):
    for k, v in (p.get('properties') or {}).items():
        if v.get('type') == 'title':
            return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))
    return ''


def norm(s):
    return ' '.join((s or '').split())


def live_sig(b):
    t = b.get('type')
    if t in ('child_database', 'image'):
        return None
    return (t, norm(''.join(x.get('plain_text', '') for x in (b.get(t, {}).get('rich_text') or []))))


def snap_sig(it):
    if it['type'] in ('child_database', 'image'):
        return None
    s = norm(''.join(x.get('plain_text', '') for x in (it.get('payload', {}).get('rich_text') or [])))
    return (it['type'], s) if s else None


def rt(items):
    r = []
    for z in (items or []):
        if z.get('type', 'text') == 'text':
            c = z.get('plain_text', '') or (z.get('text') or {}).get('content', '')
            r.append({'type': 'text', 'text': {'content': c}})
        else:
            r.append({'type': z.get('type')})
    return r


def body_of(it):
    return {'type': it['type'], it['type']: {'rich_text': rt(it.get('payload', {}).get('rich_text', []))}}


def live_index(pid):
    """(signature) -> [(block_id, parent_id)] ทุกระดับ"""
    idx = {}

    def walk(bid, parent):
        for b in req('/blocks/%s/children' % bid).get('results', []):
            s = live_sig(b)
            if s:
                idx.setdefault(s, []).append((b['id'], parent))
            if b.get('has_children'):
                walk(b['id'], b['id'])
    walk(pid, None)
    return idx


def children_of(bid):
    return req('/blocks/%s/children' % bid).get('results', [])


def add_missing(pid, snap_items, want, idx):
    """เดิน snapshot ตามลำดับ เติมที่ขาด"""
    for it in snap_items:
        s = snap_sig(it)
        if s and want.get(s, 0) > 0:
            want[s] -= 1
            # เรียกซ้ำเพื่อเติม children ของมัน
            if it.get('children'):
                bid, parent = find_parent(it, idx)
                if bid:
                    add_missing(bid, it['children'], want, idx)
            continue
        if not s and not it.get('children'):
            continue
        # บล็อกนี้หายไป -> สร้างใหม่
        target_parent, parent_snapshot = find_parent(it, idx) if it.get('children') else (None, None)
        if it.get('children'):
            # กรณีนี้คือ parent ที่หาย -> สร้างแล้วเติมลูกต่อท้าย
            place = anchor_of(pid)
        else:
            place = anchor_of(pid)
        if place is None:
            continue
        r = req('/blocks/%s/children' % pid, json.dumps({'children': [body_of(it)]}).encode(), None, 'PATCH')
        if '__error__' in r:
            continue
        nb = (r.get('results') or [{}])[0].get('id')
        STATE['add'] += 1
        time.sleep(0.26)
        if s:
            idx.setdefault(s, []).append((nb, pid))
        if nb and it.get('children'):
            add_missing(nb, it['children'], want, idx)


def anchor_of(pid):
    cdbs = [b for b in children_of(pid) if b['type'] == 'child_database']
    return cdbs[0]['id'] if cdbs else pid


def find_parent(it, idx):
    """หา block จริงที่จะเป็น parent ของ children ของ it (ถ้ามี)"""
    ps = snap_sig(it)
    if not ps:
        return None, None
    for bid, parent in idx.get(ps, [])[:8]:
        return bid, parent
    return None, None


store = {}
for f in ['layout_snapshot.json', 'reorder_snapshot.json']:
    if os.path.exists(f):
        for k, v in json.load(open(f)).items():
            blocks = v.get('blocks', []) if isinstance(v, dict) else v
            if blocks:
                store.setdefault(k, blocks)

rows = q(PDS)
for p in rows:
    snap = store.get(p['id'])
    if not snap:
        continue
    pid = p['id']

    want = Counter()

    def w_walk(items):
        for it in items:
            s = snap_sig(it)
            if s:
                want[s] += 1
            if it.get('children'):
                w_walk(it['children'])
    w_walk(snap)

    idx = live_index(pid)
    have = Counter()
    for s, lst in idx.items():
        have[s] = len(lst)

    diff = want - have
    extra = have - want
    if not diff and not extra:
        continue

    # ---- ลบที่เกิน (เก็บตัวแรกไว้ตามจำนวนที่ snapshot ต้องการ) ----
    keep = Counter(want)
    for s, lst in idx.items():
        for bid, _ in lst:
            if keep[s] > 0:
                keep[s] -= 1
                continue
            req('/blocks/%s' % bid, json.dumps({'archived': True}).encode(), None, 'PATCH')
            STATE['del'] += 1
            time.sleep(0.22)

    # ---- เติมที่ขาด ----
    if diff:
        add_missing(pid, snap, diff, idx)

    print('  %-46s +%d / -%d' % (title(p)[:46], STATE['add'], STATE['del']), flush=True)
    time.sleep(0.3)

print('\n=== สรุป ===')
print('  เพิ่ม:', STATE['add'], '| ลบ:', STATE['del'])
