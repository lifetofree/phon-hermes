a = rowsig(es[0]['ds_id'])
b = rowsig(es[1]['ds_id'])
print('rows', len(a), len(b))
print('identical sets:', set(a) == set(b))
print('identical lists:', a == b)
oa = [x for x in a if x not in set(b)]
ob = [x for x in b if x not in set(a)]
print('only A:', len(oa))
for x in oa[:5]:
    print('   A', x[:140])
print('only B:', len(ob))
for x in ob[:5]:
    print('   B', x[:140])
