import json, collections
d = json.load(open('bk_audit_ch2_out.json'))
print('---- non-standard titles ----')
for x in d:
    if x['title'] != 'Chapter List':
        print(repr(x['title']), '|', x['book'][:40], '| rows', x.get('rows'), '|', list(x.get('schema', {}).keys()))
print('---- books with >1 child db ----')
c = collections.Counter(x['book'] for x in d)
for b, n in c.items():
    if n > 1:
        print(b, [(y['title'], y.get('rows')) for y in d if y['book'] == b])
print('---- empty DBs that are standard ----')
emp = [x for x in d if x.get('rows', 0) == 0 and x['title'] == 'Chapter List']
print('count', len(emp))
print('---- rows total excluding dup Essentialism ----')
tot = sum(x.get('rows', 0) for x in d)
print('total', tot)
