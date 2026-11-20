import json
d = json.load(open('bk_body_check_out.json'))
es = [x for x in d if x['book'] == 'Essentialism'][0]
print('page', es['page_id'], 'blocks', es['nblocks'])
bs = kids(es['page_id'])
for i, b in enumerate(bs[:24]):
    t = b['type']
    tx = ''.join(x.get('plain_text', '') for x in (b.get(t, {}).get('rich_text') or []))
    extra = b.get('child_database', {}).get('title', '') if t == 'child_database' else ''
    print(i, t, '|', (tx or extra)[:70], '| kids' if b.get('has_children') else '')
