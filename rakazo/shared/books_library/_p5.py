json.dump(res, open('bk_body_check_out.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print('books', len(res))
print('first block type:', Counter(r['img0'] for r in res).most_common())
print('image index:', Counter(r['img_idx'] for r in res).most_common(6))
print('child_db index:', Counter(r['cdb_idx'] for r in res).most_common(6))
print('page cover:', Counter(r['page_cover'] for r in res).most_common())
bad = [r for r in res if r['img_idx'] != 0 or r['cdb_idx'] < 0 or not r['page_cover']]
print('NOT ok:', len(bad))
for r in bad[:15]:
    print('   ', r['book'][:44], r['img0'], r['img_idx'], r['cdb_idx'], r['page_cover'], r['nblocks'])
