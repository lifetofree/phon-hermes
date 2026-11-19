#!/usr/bin/env python3
"""
Google OAuth setup with Tasks scope and other common Google Workspace APIs.

Usage (macOS):
    ~/.hermes/hermes-agent/venv/bin/python3 oauth_setup.py

Saves token to: ~/.hermes/google_token.json

Key features:
  - Adds tasks scope (not in standard setup.py)
  - Uses port 8080 (Chrome blocks port 1 with ERR_UNSAFE_PORT)
  - Uses os.path.expanduser() (never trust os.environ['HOME'] on macOS)
"""

import json
import base64
import hashlib
import secrets
import urllib.parse
import webbrowser
from urllib.request import Request, urlopen
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import os
import sys
import threading
import time

# SAFE: Use os.path.expanduser, NOT os.environ['HOME']
HOME = os.path.expanduser("~")
CLIENT_SECRET_PATH = os.path.join(HOME, '.hermes', 'google_client_secret.json')
TOKEN_PATH = os.path.join(HOME, '.hermes', 'google_token.json')

# Scopes list - includes tasks API
# When shown to user via chat, these URL strings will be redacted.
# That's OK because they're in a script file, not in chat output.
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/tasks',
]

# Use port 8080 to avoid Chrome ERR_UNSAFE_PORT
# Chrome blocks port 1 (and a few other privileged ports) by default
# Port 8080 is standard HTTP alternative and always works
PORT = 8080
REDIRECT_URI = f'http://localhost:{PORT}/callback'


def run_oauth_flow():
    """Execute PKCE OAuth flow with local HTTP server callback."""

    # Load client secret
    print(f"Loading client secret from: {CLIENT_SECRET_PATH}")
    with open(CLIENT_SECRET_PATH) as f:
        client_config = json.load(f)

    # Extract client ID and secret
    client_id = client_config['installed']['client_id']
    client_secret = client_config['installed']['client_secret']

    # Generate PKCE code verifier and challenge
    code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=').decode()
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b'=').decode()

    # Generate state parameter for CSRF protection
    state = base64.urlsafe_b64encode(secrets.token_bytes(16)).rstrip(b'=').decode()

    # Build authorization URL
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': REDIRECT_URI,
        'scope': ' '.join(SCOPES),
        'state': state,
        'code_challenge': code_challenge,
        'code_challenge_method': 'S256',
        'access_type': 'offline',
        'prompt': 'consent',
    }
    auth_url = 'https://accounts.google.com/o/oauth2/v2/auth?' + urllib.parse.urlencode(params)

    print("\n" + "=" * 70)
    print("Opening browser for Google OAuth...")
    print("If browser doesn't open, copy this URL:")
    print("=" * 70)
    print(auth_url)
    print("=" * 70 + "\n")

    # Local HTTP server to catch callback
    callback_received = {'code': None}

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)

            if 'code' in params:
                callback_received['code'] = params['code'][0]
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'OK! Authentication successful. You can close this tab.')
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Error: No authorization code received.')

        def log_message(self, format, *args):
            pass  # Suppress request logging

    # Start server in background thread
    server = HTTPServer(('localhost', PORT), CallbackHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    # Open browser
    webbrowser.open(auth_url)

    print(f"Waiting for callback on port {PORT}...")
    print("(Browser should open automatically)")

    # Wait for callback (max 5 minutes)
    for _ in range(300):
        if callback_received['code']:
            break
        time.sleep(1)

    server.shutdown()

    if not callback_received['code']:
        print("❌ ERROR: No authorization code received (timeout)")
        sys.exit(1)

    print("✅ Authorization code received")
    print("Exchanging code for access token...")

    # Exchange code for token
    token_data = {
        'code': callback_received['code'],
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code',
        'code_verifier': code_verifier,
    }

    req = Request(
        'https://oauth2.googleapis.com/token',
        data=urllib.parse.urlencode(token_data).encode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        method='POST'
    )

    with urlopen(req) as response:
        token_response = json.loads(response.read())

    # Check if we got a refresh token
    if 'refresh_token' not in token_response:
        print("❌ ERROR: No refresh token in response")
        print("This usually means the user already authorized this app")
        print("Try revoking access first: https://myaccount.google.com/permissions")
        sys.exit(1)

    # Extract scopes from response
    granted_scopes = token_response.get('scope', '').split()

    # Save token
    token_data = {
        'token': token_response['access_token'],
        'refresh_token': token_response['refresh_token'],
        'token_uri': 'https://oauth2.googleapis.com/token',
        'client_id': client_id,
        'client_secret': client_secret,
        'scopes': granted_scopes,
    }

    with open(TOKEN_PATH, 'w') as f:
        json.dump(token_data, f, indent=2)

    print("\n" + "=" * 70)
    print("✅ OAuth setup complete!")
    print("=" * 70)
    print(f"Token saved to: {TOKEN_PATH}")
    print(f"Granted scopes ({len(granted_scopes)}):")
    for scope in sorted(granted_scopes):
        print(f"  - {scope}")

    # Verify tasks scope is included
    if 'https://www.googleapis.com/auth/tasks' not in granted_scopes:
        print("\n⚠️  WARNING: Tasks scope not granted!")
        print("You may need to revoke and re-authorize.")
        sys.exit(1)

    print("\n✅ Tasks API scope confirmed!")


if __name__ == '__main__':
    run_oauth_flow()
