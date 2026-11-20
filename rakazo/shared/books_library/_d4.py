import json
B = json.load(open('bk_body_check_out.json'))
pid = [x for x in B if x['book'] == 'Essentialism'][0]['page_id']
bs = kids(pid)
cdbs = [b for b in bs if b['type'] == 'child_database']
print('cdb blocks:', [(b['id'], b['child_database']['title']) for b in cdbs])
sigs = []
for b in cdbs:
    db = rq('/databases/%s' % b['id'])
    dsi = (db.get('data_sources') or [{}])[0].get('id')
    sc = {k: v['type'] for k, v in (rq('/data_sources/%s' % dsi).get('properties') or {}).items()}
    rows = q(dsi)
    out = []
    for r in rows:
        vals = {}
        for k, v in r['properties'].items():
            if v['type'] == 'title': vals[k] = pl(v['title'])
            elif v['type'] == 'rich_text': vals[k] = pl(v['rich_text'])
            elif v['type'] == 'select': vals[k] = (v.get('select') or {}).get('name')
        out.append(json.dumps(vals, ensure_ascii=False, sort_keys=True))
    print('  db', b['id'][:16], 'rows', len(rows), 'schema', list(sc))
    sigs.append(out)
