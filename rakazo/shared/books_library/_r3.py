def kids(pid):
    o, c = [], None
    while True:
        u = '/blocks/%s/children?page_size=100' % pid
        if c: u += '&start_cursor=' + c
        r = rq(u)
        if '__error__' in r: break
        o += r.get('results', [])
        if not r.get('has_more'): break
        c = r.get('next_cursor')
    return o
REN = [('Core Message (สรุปแก่นฉบับ PHON)', 'Core Message (ฉบับ PHON)'),
       ('Core Message (ฉบับ PHON/Duck OS)', 'Core Message (ฉบับ PHON)'),
       ('Chapter Title', 'Chapter Title (Original)')]
D = json.load(open('bk_audit_ch2_out.json'))
