print('=== STEP 6: archive duplicate cover image in Essentialism ===')
B = json.load(open('bk_body_check_out.json'))
for x in B:
    if x['book'] != 'Essentialism': continue
    bs = kids(x['page_id'])
    imgs = [b for b in bs if b['type'] == 'image']
    cdbs = [b for b in bs if b['type'] == 'child_database']
    print('  image blocks:', len(imgs), '| child_db blocks:', len(cdbs))
    for b in imgs:
        print('   img', b['id'][:16], (b.get('image') or {}).get('file', {}).get('url', '')[:70])
    for b in imgs[1:]:
        print('   archive image', b['id'][:16])
        if APPLY:
            r = P('/blocks/%s' % b['id'], {'archived': True})
            time.sleep(0.4)
            print('     ->', r.get('__error__', 'OK'))
print('done. APPLY =', APPLY)
