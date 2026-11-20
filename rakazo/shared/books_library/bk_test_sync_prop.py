#!/usr/bin/env python3
"""
ทดสอบว่า sync_books_library.py ยังอ่าน Tags ได้หรือไม่หลังเปลี่ยนเป็น multi_select
(read-only: ไม่เขียนไฟล์ใน repo)
"""
import os, json, urllib.request

TOK = os.environ['NOTION_TOKEN']
DB = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'
H = {'Authorization': 'Bearer ' + TOK, 'Notion-Version': '2022-06-28',
     'Content-Type': 'application/json'}

# ฟังก์ชัน prop() ของ sync_books_library.py (คัดลอกตรง ๆ ตามต้นฉบับ)
def prop(p):
    t = p["type"]
    if t == "title":
        return "".join(x["plain_text"] for x in p["title"]).strip()
    if t == "rich_text":
        return "".join(x["plain_text"] for x in p["rich_text"]).strip()
    if t == "select":
        return p["select"]["name"] if p["select"] else ""
    return ""


req = urllib.request.Request('https://api.notion.com/v1/databases/%s/query' % DB,
                             data=json.dumps({'page_size': 3}).encode(),
                             headers=H, method='POST')
res = json.load(urllib.request.urlopen(req))

print('=== ทดสอบ prop() กับ Tags ที่เป็น multi_select ===')
for r in res['results']:
    P = r['properties']
    t = P['Title']
    title = ''.join(x['plain_text'] for x in t['title']).strip()
    got = prop(P['Tags'])
    real = [o['name'] for o in P['Tags'].get('multi_select', [])]
    print('  %-42s' % title[:42])
    print('     prop(Tags) -> %r   <-- เขียนลง catalog.md' % got)
    print('     ค่าจริง multi_select -> %s' % real)

empty = sum(1 for r in res['results'] if not prop(r['properties']['Tags']))
print('\n  จาก %d แถวที่สุ่มมา: prop(Tags) ว่าง %d แถว' % (len(res['results']), empty))
print('  => ถ้า prop() คืน "" ทั้งหมด แปลว่า catalog.md จะไม่มี tag ต่อไปนี้')
