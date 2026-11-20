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
