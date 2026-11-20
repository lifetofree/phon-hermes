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
def kids(pid):
    o, c = [], None
    while True:
        u = '/blocks/%s/children?page_size=100' % pid
        if c: u += '&start_cursor=' + c
        r = rq(u)
        if '__error__' in r: break
        o += r.get('results', [])
        if not r.get('has_more'): break
        c = r.get('next_cursor')
    return o
REN = [('Core Message (สรุปแก่นฉบับ PHON)', 'Core Message (ฉบับ PHON)'),
       ('Core Message (ฉบับ PHON/Duck OS)', 'Core Message (ฉบับ PHON)'),
       ('Chapter Title', 'Chapter Title (Original)')]
D = json.load(open('bk_audit_ch2_out.json'))
print('=== STEP 1: rename columns ===')
for x in D:
    if x.get('rows', 0) <= 0: continue
    sch = x.get('schema') or {}
    for old, new in REN:
        if old in sch and new not in sch:
            print('  %-34s %s -> %s' % (x['book'][:34], old, new))
            if APPLY:
                r = P('/data_sources/%s' % x['ds_id'], {'properties': {old: {'name': new}}})
                time.sleep(0.4)
                print('     ->', r.get('__error__', 'OK'))
    if x.get('title_kind') == 'num' and 'Name' in sch:
        print('  %-34s Name -> # (title holds numbers)' % x['book'][:34])
        if APPLY:
            r = P('/data_sources/%s' % x['ds_id'], {'properties': {'Name': {'name': '#'}}})
            time.sleep(0.4)
            print('     ->', r.get('__error__', 'OK'))
    if x.get('title_kind') == 'name' and 'Name' in sch:
        print('  %-34s SKIP Name-># (title holds chapter NAMES)' % x['book'][:34])
print('=== STEP 3: archive leftovers (ZZ test db + duplicate Essentialism) ===')
for x in D:
    if x['title'] == 'ZZ test db':
        print('  archive %r in %s (rows %s)' % (x['title'], x['book'][:34], x.get('rows')))
        if APPLY:
            r = P('/blocks/%s' % x['db_id'], {'archived': True})
            time.sleep(0.4)
            print('     ->', r.get('__error__', 'OK'))
es = [x for x in D if x['book'] == 'Essentialism' and x.get('rows', 0) > 0]
if len(es) == 2:
    keep, dup = es[0], es[1]
    print('  archive duplicate Chapter List in Essentialism (keep db %s)' % keep['db_id'][:12])
    if APPLY:
        r = P('/blocks/%s' % dup['db_id'], {'archived': True})
        time.sleep(0.4)
        print('     ->', r.get('__error__', 'OK'))
print('=== STEP 4: add Status + Core Message cols to child DBs that lack them ===')
OPT = [{'name': '⬜ QUEUED'}, {'name': '⏳ LOADING...'}, {'name': '✅ INSTALLED'}]
nrow = 0
for x in D:
    if x.get('rows', 0) <= 0: continue
    sch = x.get('schema') or {}
    if 'Status' in sch: continue
    add = {'Status': {'select': {'options': OPT}}}
    if 'Core Message (ฉบับ PHON)' not in sch:
        add['Core Message (ฉบับ PHON)'] = {'rich_text': {}}
    if 'Chapter Title (Original)' not in sch:
        add['Chapter Title (Original)'] = {'rich_text': {}}
    print('  %-34s rows %-4d add %s' % (x['book'][:34], x['rows'], list(add)))
    if APPLY:
        r = P('/data_sources/%s' % x['ds_id'], {'properties': add})
        time.sleep(0.5)
        if '__error__' in r:
            print('     -> ERR', r); continue
        rows = q(x['ds_id'])
        if not isinstance(rows, list):
            print('     -> query err'); continue
        for rr in rows:
            P('/pages/%s' % rr['id'], {'properties': {'Status': {'select': {'name': '⬜ QUEUED'}}}})
            nrow += 1
            time.sleep(0.25)
print('  rows set to QUEUED:', nrow if APPLY else '(dry-run)')
print('=== STEP 5: patch blank Status of REAL chapters (leave PART dividers) ===')
import re
PART_RE = re.compile(r'^\s*(?:\U0001F4C4\s*)?(PART|Part|Section|SECTION)\b', re.I)
npatch = npart = 0
for x in D:
    if x.get('rows', 0) <= 0: continue
    sch = x.get('schema') or {}
    if 'Status' not in sch: continue
    rows = q(x['ds_id'])
    if not isinstance(rows, list): continue
    for rr in rows:
        sv = rr['properties'].get('Status')
        nm = (sv.get('select') or {}).get('name') if sv else None
        if nm: continue
        ti = ''
        for k, v in rr['properties'].items():
            if v['type'] == 'title': ti = pl(v['title'])
        if PART_RE.match(ti):
            npart += 1
            continue
        print('  patch %-28s | %s' % (x['book'][:28], ti[:40]))
        if APPLY:
            P('/pages/%s' % rr['id'], {'properties': {'Status': {'select': {'name': '⬜ QUEUED'}}}})
            time.sleep(0.25)
        npatch += 1
print('  patched:', npatch, '| PART rows left blank:', npart)
print('=== STEP 6: archive duplicate cover image in Essentialism ===')
B = json.load(open('bk_body_check_out.json'))
for x in B:
    if x['book'] != 'Essentialism': continue
    bs = kids(x['page_id'])
    imgs = [b for b in bs if b['type'] == 'image']
    cdbs = [b for b in bs if b['type'] == 'child_database']
    print('  image blocks:', len(imgs), '| child_db blocks:', len(cdbs))
    for b in imgs:
        print('   img', b['id'][:16], (b.get('image') or {}).get('file', {}).get('url', '')[:70])
    for b in imgs[1:]:
        print('   archive image', b['id'][:16])
        if APPLY:
            r = P('/blocks/%s' % b['id'], {'archived': True})
            time.sleep(0.4)
            print('     ->', r.get('__error__', 'OK'))
print('done. APPLY =', APPLY)
