def pl(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))
def query():
    o, c = [], None
    while True:
        b = {'page_size': 100}
        if c:
            b['start_cursor'] = c
        r = rq('/data_sources/%s/query' % PDS, json.dumps(b).encode(), 'POST')
        if '__error__' in r:
            break
        o += r.get('results', [])
        if not r.get('has_more'):
            break
        c = r.get('next_cursor')
    return o
