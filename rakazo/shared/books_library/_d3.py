import urllib.request as _u
def q(ds):
    o, c = [], None
    while True:
        b = {'page_size': 100}
        if c:
            b['start_cursor'] = c
        rq = _u.Request('https://api.notion.com/v1/data_sources/%s/query' % ds,
                        data=json.dumps(b).encode(), headers=H, method='POST')
        try:
            r = json.load(_u.urlopen(rq, timeout=90))
        except Exception as ex:
            print('err', ex)
            break
        o += r.get('results', [])
        if not r.get('has_more'):
            break
        c = r.get('next_cursor')
    return o
