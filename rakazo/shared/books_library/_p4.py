rows = query()
res = []
for p in rows:
    pr = p['properties']
    ti = ''
    for k, v in pr.items():
        if v['type'] == 'title':
            ti = pl(v['title'])
            break
    bs = kids(p['id'])
    types = [b['type'] for b in bs]
    res.append({'book': ti, 'nblocks': len(bs),
                'img0': types[0] if types else None,
                'img_idx': types.index('image') if 'image' in types else -1,
                'cdb_idx': types.index('child_database') if 'child_database' in types else -1,
                'page_cover': bool(p.get('cover')), 'page_id': p['id']})
