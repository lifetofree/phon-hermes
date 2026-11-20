if len(sigs) == 2:
    a, b = sigs
    print('identical rows:', a == b, '| set equal:', set(a) == set(b))
    onlya = [x for x in a if x not in set(b)]
    onlyb = [x for x in b if x not in set(a)]
    print('only A:', len(onlya), '| only B:', len(onlyb))
    for x in onlya[:4]: print('  A', x[:120])
    for x in onlyb[:4]: print('  B', x[:120])
