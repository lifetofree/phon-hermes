D = json.load(open('bk_audit_live_out.json'))
print('=== rename remaining non-canonical child DB titles ===')
TT = [{'type': 'text', 'text': {'content': 'Chapter List'}}]
for x in D['cdbs']:
    if x['title'] == 'Chapter List': continue
    print('  %-36s %r -> Chapter List' % (x['book'][:36], x['title']))
    r = P('/databases/%s' % x['ds_id'], {'title': TT})
    print('     ->', r.get('__error__', 'OK'), str(r.get('msg', ''))[:160])
    time.sleep(0.4)
