import re
PART_RE = re.compile(r'^\s*(?:\U0001F4C4\s*)?(PART|Part|Section|SECTION)\b', re.I)
D = json.load(open('bk_audit_ch2_out.json'))
for x in D:
    if x.get('rows', 0) <= 0: continue
    sch = x.get('schema') or {}
    if 'Status' not in sch: continue
    rows = q(x['ds_id'])
    if not isinstance(rows, list): continue
    for rr in rows:
        pr = rr['properties']
        sv = pr.get('Status')
        nm = (sv.get('select') or {}).get('name') if sv else None
        if nm: continue
        ti = ''
        for k, v in pr.items():
            if v['type'] == 'title': ti = pl(v['title'])
        core = ''
        for k, v in pr.items():
            if v['type'] == 'rich_text' and 'core message' in k.lower(): core = pl(v['rich_text'])
        print('%-30s | %-44s | PART=%s | notes=%s' % (x['book'][:30], ti[:44], bool(PART_RE.match(ti)), 'yes' if core.strip() else 'no'))
