    if x.get('title_kind') == 'num' and 'Name' in sch:
        print('  %-34s Name -> # (title holds numbers)' % x['book'][:34])
        if APPLY:
            r = P('/data_sources/%s' % x['ds_id'], {'properties': {'Name': {'name': '#'}}})
            time.sleep(0.4)
            print('     ->', r.get('__error__', 'OK'))
    if x.get('title_kind') == 'name' and 'Name' in sch:
        print('  %-34s SKIP Name-># (title holds chapter NAMES)' % x['book'][:34])
