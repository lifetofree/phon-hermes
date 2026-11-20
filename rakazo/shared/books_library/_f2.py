D = json.load(open('bk_audit_ch2_out.json'))
OPT = [{'name': '⬜ QUEUED'}, {'name': '⏳ LOADING...'}, {'name': '✅ INSTALLED'}]
for x in D:
    sch = x.get('schema') or {}
    if x.get('rows', 0) > 0 or 'Status' in sch: continue
    add = {'Status': {'select': {'options': OPT}},
           'Core Message (ฉบับ PHON)': {'rich_text': {}},
           'Chapter Title (Original)': {'rich_text': {}}}
    print('normalize', x['book'][:36], list(sch))
    r = P('/data_sources/%s' % x['ds_id'], {'properties': add})
    print('   ->', r.get('__error__', 'OK'), str(r.get('msg', ''))[:120])
    time.sleep(0.4)
