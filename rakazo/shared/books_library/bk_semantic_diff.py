#!/usr/bin/env python3
"""
เทียบสภาพจริงหลัง merge (live) กับแผนของ BK (bk_tag_merge_dryrun.py --plan hybrid)
เพื่อหาว่า "ต่างกันตรงไหน" + เช็ค semantic integrity (ไม่มีความหมายหาย)
read-only
"""
import os, json, sys, importlib.util, urllib.request, urllib.error, time
from collections import Counter

DB_ID = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
SNAP = '../../bots/cmwj2kqkfl1cdznjl9fxz39ik/books_tags_snapshot.json'
HDR = {'Authorization': 'Bearer ' + os.environ['NOTION_TOKEN'],
       'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}


def req(url, method='GET', body=None, tries=9):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers=HDR, method=method)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(1.5 * (i + 1))
                continue
            raise
    raise RuntimeError('rate limited')


def query_db(did):
    rows, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur:
            b['start_cursor'] = cur
        res = req('https://api.notion.com/v1/databases/%s/query' % did, 'POST', b)
        rows += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return rows


def title_of(p):
    for k, v in (p.get('properties') or {}).items():
        if v.get('type') == 'title':
            return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))
    return ''


def tags_of(p):
    for k, v in (p.get('properties') or {}).items():
        if v.get('type') == 'multi_select':
            return [x['name'] for x in v.get('multi_select', [])]
    return []


spec = importlib.util.spec_from_file_location('m', 'bk_tag_merge_dryrun.py')
m = importlib.util.module_from_spec(spec)
sys.argv = ['x', '--plan', 'hybrid']
spec.loader.exec_module(m)

snap = {r['page_id']: r for r in json.load(open(SNAP))['rows']}
rows = query_db(DB_ID)

diff_rows, identical, missing = [], 0, []
for p in rows:
    pid = p['id']
    live = tags_of(p)
    s = snap.get(pid)
    if not s:
        missing.append(title_of(p))
        continue
    plan_tags, dropped = m.plan_for(s['tags'], 'hybrid')
    if set(plan_tags) == set(live):
        identical += 1
    else:
        diff_rows.append({'title': title_of(p), 'page_id': pid,
                          'snapshot': s['tags'], 'plan': sorted(set(plan_tags)),
                          'live': live, 'dropped': dropped})

print('rows compared      :', len(rows))
print('identical to BK plan:', identical)
print('different          :', len(diff_rows))
print('not in snapshot    :', len(missing), missing[:5])

# สรุปรูปแบบความต่าง
kinds = Counter()
for d in diff_rows:
    only_live = set(d['live']) - set(d['plan'])
    only_plan = set(d['plan']) - set(d['live'])
    kinds[(tuple(sorted(only_live)), tuple(sorted(only_plan)))] += 1
print('\n=== รูปแบบความต่าง (only_live | only_plan) ===')
for (ol, op), n in kinds.most_common(30):
    print('  x%-3d live_extra=%s | plan_extra=%s' % (n, ol, op))

print('\n=== ตัวอย่าง 12 แถวที่ต่าง ===')
for d in diff_rows[:12]:
    print('  %s' % d['title'])
    print('     snap : %s' % ' '.join(d['snapshot']))
    print('     live : %s' % ' '.join(d['live']))
    print('     plan : %s' % ' '.join(d['plan']))

json.dump({'diff_rows': diff_rows, 'identical': identical, 'missing': missing},
          open('bk_semantic_diff.json', 'w'), ensure_ascii=False, indent=1)
print('\nsaved -> bk_semantic_diff.json')
