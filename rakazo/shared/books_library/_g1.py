import json
D = json.load(open('bk_audit_ch2_out.json'))
for x in D:
    sch = x.get('schema') or {}
    for old, new in [('Core Message (สรุปแก่นฉบับ PHON)', 'Core Message (ฉบับ PHON)'),
                     ('Chapter Title', 'Chapter Title (Original)')]:
        if old in sch and new not in sch:
            print('rename', x['book'][:30], old, '->', new)
            r = P('/data_sources/%s' % x['ds_id'], {'properties': {old: {'name': new}}})
            print('   ->', r.get('__error__', 'OK'), str(r.get('msg', ''))[:120])
            time.sleep(0.4)
    if x['book'] == 'Essentialism':
        rows = q(x['ds_id'])
        c = {}
        for rr in rows:
            sv = rr['properties'].get('Status')
            nm = (sv.get('select') or {}).get('name') if sv else None
            c[nm] = c.get(nm, 0) + 1
        print('Essentialism rows', len(rows), c)
