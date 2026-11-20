import json
B = json.load(open('bk_body_check_out.json'))
pid = [x for x in B if x['book'] == 'Essentialism'][0]['page_id']
bs = kids(pid)
cdbs = [b for b in bs if b['type'] == 'child_database']
dup = '41edf8d8-8d8c-817c-a0f1-e471a028f6b3'
for b in cdbs:
    if b['id'] == dup:
        r = rq('/blocks/%s' % dup, json.dumps({'archived': True}).encode(), 'PATCH')
        print('archive dup Chapter List:', r.get('__error__', 'OK'))
time.sleep(1.5)
bs2 = kids(pid)
print('order now:', [(i, b['type'], b.get('child_database', {}).get('title', '')) for i, b in enumerate(bs2[:4])])
print('blocks:', len(bs2))
