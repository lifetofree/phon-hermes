import json
B = json.load(open('bk_body_check_out.json'))
pid = [x for x in B if x['book'] == 'Essentialism'][0]['page_id']
bs = kids(pid)
img = [b for b in bs if b['type'] == 'image'][0]
body = {'parent': {'type': 'page_id', 'page_id': pid},
        'title': [{'type': 'text', 'text': {'content': 'ZZ POSITION TEST'}}],
        'is_inline': True, 'after': img['id']}
r = rq('/databases', json.dumps(body).encode(), 'POST')
print('create:', r.get('__error__', 'OK'), str(r.get('msg', ''))[:200])
nid = r.get('id')
if nid:
    time.sleep(2)
    bs2 = kids(pid)
    print('order now:', [(i, b['type'], b.get('child_database', {}).get('title', '')) for i, b in enumerate(bs2[:5])])
    a = rq('/blocks/%s' % nid, json.dumps({'archived': True}).encode(), 'PATCH')
    print('archive test db:', a.get('__error__', 'OK'))
