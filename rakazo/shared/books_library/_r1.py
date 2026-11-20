import os, sys, json, time, urllib.request, urllib.error
T = os.environ['NOTION_TOKEN']
H = {'Authorization': 'Bearer ' + T, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
APPLY = '--apply' in sys.argv
def rq(p, d=None, m='GET', n=7):
    for i in range(n):
        r = urllib.request.Request('https://api.notion.com/v1' + p, data=d, headers=H, method=m)
        try:
            return json.load(urllib.request.urlopen(r, timeout=90))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < n - 1:
                time.sleep(2 ** i); continue
            return {'__error__': e.code, 'msg': e.read().decode()[:150]}
        except Exception as e:
            if i < n - 1:
                time.sleep(2); continue
            return {'__error__': 'exc', 'msg': str(e)[:100]}
