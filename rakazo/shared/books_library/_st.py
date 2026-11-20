import json
B = json.load(open('bk_body_check_out.json'))
for x in B:
    if x['book'] in ('Essentialism', 'Steal Like an Artist'):
        bs = kids(x['page_id'])
        types = [b['type'] for b in bs]
        print(x['book'], '| blocks', len(bs), '| image@', types.index('image') if 'image' in types else -1,
              '| cdb@', [i for i, t in enumerate(types) if t == 'child_database'])
