#!/usr/bin/env python3
"""
Books Library - POST-MERGE VERIFICATION (Book Keeper, read-only)
==============================================================
ตรวจสอบสภาพจริงหลัง Chief merge tag + แปลง Tags เป็น multi_select
อ่านอย่างเดียว: ไม่ PATCH ไม่ DELETE ไม่เขียนฐาน

ใช้: python3 bk_verify_post_merge.py
"""
import os, sys, json, time, urllib.request, urllib.error
from collections import Counter

DB_ID = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
DS_ID = '2ffdf8d8-8d8c-80d6-913d-000b102ca15a'
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
                w = 1.5 * (i + 1)
                print('   429 -> sleep %.1fs' % w, file=sys.stderr)
                time.sleep(w)
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
    return None


def main():
    out = {}
    # ---------- 1) schema: property types + options
    ds = req('https://api.notion.com/v1/databases/%s' % DB_ID)
    props = ds.get('properties', {})
    schema = {}
    for name, p in props.items():
        schema[name] = p.get('type')
    out['schema'] = schema
    tags_prop = props.get('Tags') or {}
    options = [o['name'] for o in (tags_prop.get('multi_select') or {}).get('options', [])]
    out['tags_prop_type'] = tags_prop.get('type')
    out['tag_options_count'] = len(options)
    out['tag_options'] = sorted(options)

    # ---------- 2) rows
    rows = query_db(DB_ID)
    out['rows_total'] = len(rows)
    tag_lists, empty, no_prop = [], [], []
    for p in rows:
        t = tags_of(p)
        if t is None:
            no_prop.append(title_of(p))
            continue
        if not t:
            empty.append(title_of(p))
        tag_lists.append((title_of(p), t))

    out['rows_without_tags_prop'] = no_prop
    out['rows_with_empty_tags'] = empty
    out['distinct_tags_used'] = len({x for _, ts in tag_lists for x in ts})
    out['tag_slots'] = sum(len(ts) for _, ts in tag_lists)
    out['rows_with_tags'] = len(tag_lists)

    cnt = Counter(x for _, ts in tag_lists for x in ts)
    out['singleton_count'] = sum(1 for k, v in cnt.items() if v == 1)
    out['singletons'] = sorted(k for k, v in cnt.items() if v == 1)

    used = set(cnt)
    out['dead_options'] = sorted(set(options) - used)
    out['used_but_missing_option'] = sorted(used - set(options))

    dup_rows = [(t, ts) for t, ts in tag_lists if len(ts) != len(set(ts))]
    out['rows_with_duplicate_tags'] = len(dup_rows)
    out['tag_counts'] = dict(sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])))

    # ---------- 3) bleed test: multi_select "contains" exact match?
    print('\n=== BLEED TEST (filter จริง) ===')
    probes = ['#DuckOS', '#DuckOS_Core', '#Systems', '#Pro', '#Psy', '#Skill',
              '#systems', '#SYSTEMS', '#Productivity', '#Business', '#Life',
              '#Habits', '#SelfTalk', '#Sociology', '#SocialMedia', '#DigitalWellbeing']
    bleed = {}
    for probe in probes:
        n = 0
        try:
            res = req('https://api.notion.com/v1/databases/%s/query' % DB_ID, 'POST', {
                'page_size': 100,
                'filter': {'property': 'Tags', 'multi_select': {'contains': probe}},
            })
            n = len(res['results'])
            err = None
        except urllib.error.HTTPError as e:
            err = 'HTTP %s %s' % (e.code, e.read().decode()[:160])
            n = 0
        exact = cnt.get(probe, 0)
        bleed[probe] = {'filter_rows': n, 'exact_uses': exact,
                        'error': err,
                        'bleed': (n - exact) if not err else None}
        print('  %-22s filter=%-4s exact=%-4s %s' % (
            probe, n, exact,
            ('ERR ' + err) if err else ('BLEED +%d' % (n - exact) if n != exact else 'exact OK')))
    out['bleed_test'] = bleed

    # ---------- 4) Energy Group / Status ยังครบไหม
    eg, st = Counter(), Counter()
    for p in rows:
        for k, v in (p.get('properties') or {}).items():
            if v.get('type') == 'select' and k == 'Energy Group':
                eg[(v.get('select') or {}).get('name')] += 1
            if v.get('type') == 'select' and k == 'Status':
                st[(v.get('select') or {}).get('name')] += 1
    out['energy_group'] = dict(eg)
    out['status'] = dict(st)

    with open('bk_verify_post_merge.json', 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print('\n=== SUMMARY ===')
    print('Tags property type      :', out['tags_prop_type'])
    print('tag options (schema)    :', out['tag_options_count'])
    print('distinct tags used      :', out['distinct_tags_used'])
    print('tag slots               :', out['tag_slots'])
    print('rows total              :', out['rows_total'])
    print('rows with empty tags    :', len(empty))
    print('rows without Tags prop  :', len(no_prop))
    print('dead options (unused)   :', len(out['dead_options']), out['dead_options'][:10])
    print('singleton tags          :', out['singleton_count'])
    print('duplicate tags in row   :', out['rows_with_duplicate_tags'])
    print('Energy Group            :', out['energy_group'])
    print('Status (book level)     :', out['status'])
    print('\nsaved -> bk_verify_post_merge.json')


if __name__ == '__main__':
    main()
