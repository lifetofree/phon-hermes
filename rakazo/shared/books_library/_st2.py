import json
B = json.load(open('bk_body_check_out.json'))
for x in B:
    if x['book'] != 'Steal Like an Artist': continue
    bs = kids(x['page_id'])
    print('blocks', len(bs))
    for i, b in enumerate(bs[:12]):
        t = b['type']
        tx = ''.join(z.get('plain_text', '') for z in (b.get(t, {}).get('rich_text') or []))
        print(' ', i, t, '|', tx[:60])
