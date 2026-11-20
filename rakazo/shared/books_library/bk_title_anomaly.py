#!/usr/bin/env python3
"""ตรวจ Title ผิดปกติ + หนังสือซ้ำ + ชื่อ child DB ที่จะ rename (read-only)"""
import os, json, urllib.request, urllib.error, re, time
from collections import Counter

TOK = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}


def api(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(9):
        try:
            req = urllib.request.Request('https://api.notion.com/v1' + path,
                                         data=data, headers=H, method=method)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(1.5 * (i + 1))
                continue
            raise
    raise RuntimeError('rl')


def q(did):
    out, cur = [], None
    while True:
        body = {'page_size': 100}
        if cur:
            body['start_cursor'] = cur
        res = api('POST', '/databases/%s/query' % did, body)
        out += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
        time.sleep(0.15)
    return out


DB = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
rows = q(DB)


def title_of(p):
    for k, v in (p.get('properties') or {}).items():
        if v.get('type') == 'title':
            return ''.join(x.get('plain_text', '') for x in (v.get('title') or []))
    return ''


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


titles = []
for p in rows:
    P = p.get('properties') or {}
    author = ''
    for k, v in P.items():
        if v.get('type') == 'rich_text' and k == 'Author':
            author = plain(v.get('rich_text'))
    t = title_of(p)
    tags = []
    for k, v in P.items():
        if v.get('type') == 'multi_select':
            tags = [o['name'] for o in v['multi_select']]
    titles.append({'title': t, 'author': author, 'tags': tags, 'id': p['id'],
                   'created': p.get('created_time', '')})

print('=== Title ผิดปกติ ===')
for x in titles:
    t = x['title']
    flags = []
    if t != t.strip():
        flags.append('มีช่องว่างหน้า/ท้าย')
    if '  ' in t:
        flags.append('มีช่องว่างซ้ำ')
    if re.search(r'\*{2,}', t):
        flags.append('มี *** marker')
    if x['author'] != x['author'].strip():
        flags.append('Author มีช่องว่าง')
    if flags:
        print('  %-50r  %s' % (t, ' + '.join(flags)))
        print('       author=%r tags=%s' % (x['author'], x['tags']))

print('\n=== ชื่อคล้ายกัน (normalized) ===')
norm = Counter(re.sub(r'[^a-z0-9]+', '', x['title'].lower()) for x in titles)
for k, c in norm.items():
    if c > 1:
        print('  [%s]' % k)
        for x in titles:
            if re.sub(r'[^a-z0-9]+', '', x['title'].lower()) == k:
                print('     - %-50r author=%-28r tags=%s' % (x['title'], x['author'], x['tags']))

print('\n=== Author ที่ซ้ำ/กำกวม (คนละแถว) ===')
au = Counter(x['author'] for x in titles)
for a, c in au.most_common(8):
    if c > 1:
        print('  %-32r x%d' % (a, c))
        for x in titles:
            if x['author'] == a:
                print('     - %s' % x['title'][:60])

print('\n=== สรุป ===')
print('  rows                 :', len(rows))
print('  title มีช่องว่างหน้า/ท้าย:', sum(1 for x in titles if x['title'] != x['title'].strip()))
print('  title มีช่องว่างซ้ำ  :', sum(1 for x in titles if '  ' in x['title']))
print('  title มี ***          :', sum(1 for x in titles if re.search(r'\*{2,}', x['title'])))
print('  author มีช่องว่าง    :', sum(1 for x in titles if x['author'] != x['author'].strip()))
print('  author ว่าง           :', sum(1 for x in titles if not x['author'].strip()))
json.dump(titles, open('bk_titles.json', 'w'), ensure_ascii=False, indent=1)
