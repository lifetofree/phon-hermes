print('=== STEP 5: report blank Status rows in DBs that HAVE Status ===')
for x in D:
    if x.get('rows', 0) <= 0: continue
    sch = x.get('schema') or {}
    if 'Status' not in sch: continue
    rows = q(x['ds_id'])
    if not isinstance(rows, list): continue
    blank = 0
    for rr in rows:
        sv = rr['properties'].get('Status')
        nm = (sv.get('select') or {}).get('name') if sv else None
        if not nm: blank += 1
    if blank:
        print('  %-34s blank %d (PART divider rows)' % (x['book'][:34], blank))
print('done. APPLY =', APPLY)
