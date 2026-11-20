def pl(rt): return ''.join(x.get('plain_text', '') for x in (rt or []))
def q(ds):
    o, c = [], None
    while True:
        b = {'page_size': 100}
        if c: b['start_cursor'] = c
        r = rq('/data_sources/%s/query' % ds, json.dumps(b).encode(), 'POST')
        if '__error__' in r: return r
        o += r['results']
        if not r.get('has_more'): return o
        c = r['next_cursor']
def P(p, body): return rq(p, json.dumps(body).encode(), 'PATCH')
