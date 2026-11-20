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
