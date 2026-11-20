import json
d = json.load(open('bk_audit_ch2_out.json'))
es = [x for x in d if x['book'] == 'Essentialism' and x.get('rows', 0) > 0]
print('dbs:', [(x['db_id'], x['ds_id'], x['rows']) for x in es])
def rowsig(ds):
    out = []
    for r in q(ds):
        vals = {}
        for k, v in r['properties'].items():
            if v['type'] == 'title':
                vals[k] = pl(v['title'])
            elif v['type'] == 'rich_text':
                vals[k] = pl(v['rich_text'])
            elif v['type'] == 'select':
                vals[k] = (v.get('select') or {}).get('name')
        out.append(json.dumps(vals, ensure_ascii=False, sort_keys=True))
    return out
