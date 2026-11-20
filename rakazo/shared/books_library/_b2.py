import json
d = json.load(open('bk_body_check_out.json'))
es = [x for x in d if x['book'] == 'Essentialism'][0]
bs = kids(es['page_id'])
print('total', len(bs))
for i, b in enumerate(bs):
    if b['type'] in ('image', 'child_database'):
        print('POS', i, b['type'], b.get('child_database', {}).get('title', ''))
for i in range(165, len(bs)):
    b = bs[i]
    t = b['type']
    tx = ''.join(x.get('plain_text', '') for x in (b.get(t, {}).get('rich_text') or []))
    print(i, t, '|', tx[:60])
