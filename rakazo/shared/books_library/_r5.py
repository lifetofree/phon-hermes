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
