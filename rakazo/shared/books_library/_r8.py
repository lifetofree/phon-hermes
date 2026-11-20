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
