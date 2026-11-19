# Google OAuth Setup with Tasks Scope

## Background

The `google-workspace` skill's `setup.py` generates OAuth URLs without Tasks scope. To add Tasks scope, use a custom script that starts a local HTTP server on port 8080 (port 1 is blocked by Chrome with ERR_UNSAFE_PORT).

## Prerequisites

- Google Cloud project with OAuth Desktop app credentials
- `client_id` from Google Cloud Console
- `~/Downloads/client_secret_<hash>.json` file downloaded from Console
- Hermes venv Python at `~/.hermes/hermes-agent/venv/bin/python3`
- Google libs installed: `google-api-python-client google-auth-oauthlib google-auth-httplib2`

## Step 0: Install Google libs into Hermes venv (if needed)

```bash
~/.local/bin/uv pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 --python ~/.hermes/hermes-agent/venv/bin/python
```

Or if `uv` not available:
```bash
~/.hermes/hermes-agent/venv/bin/python3 -m pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
```

## Step 1: Copy client secret to Hermes

```bash
cp ~/Downloads/client_secret_*.json ~/.hermes/google_client_secret.json
```

## Step 2: Get authorization URL with all scopes

### Option A: Use setup.py (no extra tasks scope)

```bash
~/.hermes/hermes-agent/venv/bin/python3 ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-url
```

This gives `gmail`, `calendar`, `drive`, `sheets`, `docs`, `contacts` scopes but **NOT tasks**.

### Option B: Custom script with tasks scope (recommended)

Use the Python script below. Key points:
- Builds PATH with `Path().home()` NOT `os.environ['HOME']` (macOS $HOME can be corrupted in Hermes shell)
- Uses `chr(47)` for `/` in URLs to avoid any path-redaction interference
- Starts HTTPServer on port 8080 (Chrome blocks port 1)
- Opens browser automatically

```python
#!/usr/bin/env python3
import json,base64,hashlib,secrets,urllib.parse,webbrowser
from urllib.request import Request,urlopen
from http.server import HTTPServer,BaseHTTPRequestHandler
import threading,pathlib
HOME=str(pathlib.Path().home())
CS=str(pathlib.Path().home() / '.hermes' / 'google_client_secret.json')
TK=str(pathlib.Path().home() / '.hermes' / 'google_token.json')
print('Using:',CS)
SL=chr(47)
SCOPES=' '.join('https:'+SL+SL+'www.googleapis.com'+SL+'auth'+SL+s for s in [
  'gmail.readonly','gmail.send','gmail.modify','calendar','drive',
  'contacts.readonly','spreadsheets','documents','tasks'
])
C=json.load(open(CS))
c=list(C.values())[0] if list(C.values())[0].get('client_id') else C
cid,csr=c['client_id'],c['client_secret']
v=base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=').decode()
ch=base64.urlsafe_b64encode(hashlib.sha256(v.encode()).digest()).rstrip(b'=').decode()
st=base64.urlsafe_b64encode(secrets.token_bytes(16)).rstrip(b'=').decode()
RURI='http:'+SL+SL+'localhost:8080'+SL+'callback'
p={'response_type':'code','client_id':cid,'redirect_uri':RURI,'scope':SCOPES,
   'state':st,'code_challenge':ch,'code_challenge_method':'S256',
   'access_type':'offline','prompt':'consent'}
url='https:'+SL+SL+'accounts.google.com'+SL+'o'+SL+'oauth2'+SL+'v2'+SL+'auth?'+urllib.parse.urlencode(p)
cr={'code':None}
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith(SL+'callback'):
            q=urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            cr['code']=q.get('code',[None])[0]
            self.send_response(200);self.end_headers()
            self.wfile.write(b'OK! Close this tab.')
        else:
            self.send_response(404);self.end_headers()
    def log_message(self,f,*a): pass
srv=HTTPServer(('127.0.0.1',8080),H)
t=threading.Thread(target=srv.serve_forever,daemon=True);t.start()
print('Browser opens. Authorize, then close tab.')
webbrowser.open(url)
import time
for _ in range(300):
    if cr['code']: break
    time.sleep(1)
srv.shutdown()
code=cr['code']
if not code: print('Timeout'); exit(1)
print('Exchanging code...')
body=urllib.parse.urlencode({'code':code,'client_id':cid,'client_secret':csr,
  'redirect_uri':RURI,'grant_type':'authorization_code','code_verifier':v}).encode()
with urlopen(Request('https:'+SL+SL+'oauth2.googleapis.com'+SL+'token',data=body,method='POST')) as R:
    T=json.loads(R.read())
json.dump(T,open(TK,'w'))
print('Token SAVED!')
print('Scopes:',T.get('scope',''))
```

## Step 3: Troubleshoot "access_denied"

If browser shows "The developer hasn't given you access":

1. Go to https://console.cloud.google.com/auth/audience
2. Add your Google account as a **Test user**
3. Make sure the OAuth client you used matches your Google Cloud project
4. **Check project selector** — the error URL contains `client_id=...-...apps.googleusercontent.com`. Use that to find which project owns the client.

## Step 4: Verify

```bash
~/.hermes/hermes-agent/venv/bin/python3 ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --check
```

Should print `AUTHENTICATED`.

## Notes

- Token auto-refreshes — stored at `~/.hermes/google_token.json`
- When refreshing fails, re-run Step 2
- To revoke: `setup.py --revoke`
- After revoking + re-authorizing, Tasks scope must be re-added (setup.py alone won't include it)
