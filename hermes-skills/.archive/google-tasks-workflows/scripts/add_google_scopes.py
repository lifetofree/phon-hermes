#!/usr/bin/env python3
"""
Add / update Google OAuth scopes on an existing Hermes token.

Purpose
-------
The bundled google-workspace skill's setup.py does NOT expose a `--services`
flag (despite the docs). When a user already has a google_token.json but
wants to ADD a scope (e.g. Google Tasks), this script lets you do it
without losing the existing setup flow.

Usage
-----
    # Must be run with the Hermes venv Python, e.g.:
    /Users/lifetofree/.hermes/hermes-agent/venv/bin/python \\
        add_google_scopes.py \\
        --scopes "https://www.googleapis.com/auth/tasks"
           --merge-existing    # keep scopes already in token (default)
           --append            # append --scopes to existing token scopes

Typical flow
------------
    add_google_scopes.py --scopes "https://www.googleapis.com/auth/tasks" \\
                         --append

1. Reads client credentials from ~/.hermes/google_client_secret.json
2. Optionally reads existing scopes from ~/.hermes/google_token.json
3. Builds an OAuth URL with PKCE (redirect to http://localhost:1)
4. Opens the browser; user copies the redirect URL back into the prompt
5. Exchanges the code, overwrites ~/.hermes/google_token.json
6. Prints the resulting scope string for verification

Why http://localhost:1? Google will show an error in the browser — this is
normal / expected. The user just needs the full redirected URL from the
address bar to paste back.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import secrets
import sys
import urllib.parse
import webbrowser
from urllib.request import Request, urlopen
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
CLIENT_SECRET_PATH = HERMES_HOME / "google_client_secret.json"
TOKEN_PATH = HERMES_HOME / "google_token.json"


def load_client_secret() -> tuple[str, str]:
    """Return (client_id, client_secret) from the downloaded credentials."""
    if not CLIENT_SECRET_PATH.exists():
        print(f"❌ Missing client secret: {CLIENT_SECRET_PATH}", file=sys.stderr)
        print("Run the google-workspace setup.py --client-secret <path> first.",
              file=sys.stderr)
        sys.exit(1)
    cs = json.loads(CLIENT_SECRET_PATH.read_text())
    # Top-level key may be "installed", "web", or similar
    inner = next(iter(cs.values()))
    return inner["client_id"], inner["client_secret"]


def existing_scopes() -> list[str]:
    """Read scope list from the current token file (if it exists)."""
    if not TOKEN_PATH.exists():
        return []
    try:
        tok = json.loads(TOKEN_PATH.read_text())
        scope_str = tok.get("scope", "")
        return [s for s in scope_str.split(" ") if s]
    except (json.JSONDecodeError, KeyError, AttributeError):
        return []


def build_auth_url(
    client_id: str, scopes: list[str]
) -> tuple[str, str, str]:
    """Return (auth_url, code_verifier, state) for the PKCE flow."""
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()
    challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest())
        .rstrip(b"=")
        .decode()
    )
    state = base64.urlsafe_b64encode(secrets.token_bytes(16)).rstrip(b"=").decode()

    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": "http://localhost:1",
        "scope": " ".join(sorted(set(scopes))),
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "access_type": "offline",
        "prompt": "consent",
    }
    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)
    return url, verifier, state


def exchange(
    code: str,
    client_id: str,
    client_secret: str,
    verifier: str,
) -> dict:
    """POST authorization code to Google and return the token JSON."""
    body = urllib.parse.urlencode(
        {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": "http://localhost:1",
            "grant_type": "authorization_code",
            "code_verifier": verifier,
        }
    ).encode()

    req = Request("https://oauth2.googleapis.com/token", data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urlopen(req) as resp:
        return json.loads(resp.read())


def parse_redirect(redirect_url: str) -> tuple[str | None, str | None]:
    """Extract code + state from the pasted redirect URL."""
    qs = urllib.parse.parse_qs(urllib.parse.urlparse(redirect_url).query)
    code_list = qs.get("code", [])
    state_list = qs.get("state", [])
    return (code_list[0] if code_list else None,
            state_list[0] if state_list else None)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--scopes", required=True,
        help="Space- or comma-separated list of scopes to authorize",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--append", action="store_true",
        help="Append --scopes to any scopes already in google_token.json",
    )
    mode.add_argument(
        "--merge-existing", action="store_true", default=False,
        help="Merge: keep existing scopes AND add --scopes (alias for --append). "
             "This is the default.",
    )
    parser.add_argument(
        "--replace", action="store_true",
        help="Only authorize the --scopes, ignoring whatever is already in token",
    )
    args = parser.parse_args()

    new_scopes_raw = [
        s for s in args.scopes.replace(",", " ").split() if s
    ]
    if not new_scopes_raw:
        print("❌ No scopes provided", file=sys.stderr)
        return 1

    client_id, client_secret = load_client_secret()

    if args.replace:
        scopes = new_scopes_raw
    else:
        scopes = sorted(set(existing_scopes() + new_scopes_raw))

    auth_url, verifier, state = build_auth_url(client_id, scopes)

    print("=" * 60)
    print("Scopes to authorize:")
    for s in scopes:
        print(f"  • {s}")
    print("=" * 60)
    print()
    print("Auth URL (also opening in browser):")
    print(auth_url)
    print()
    print("⚠️  After authorizing, browser WILL error at http://localhost:1.")
    print("    That is normal. Copy the ENTIRE redirected URL from the")
    print("    browser address bar and paste it below.")
    print()

    try:
        webbrowser.open(auth_url)
    except Exception:
        pass  # headless; user will paste manually

    redirect_url = input("👉 Paste redirect URL: ").strip()
    code, returned_state = parse_redirect(redirect_url)
    if not code:
        print("❌ Could not find 'code' in that URL.", file=sys.stderr)
        return 1
    if returned_state != state:
        print("⚠️  State mismatch — continuing anyway, but this is suspicious.")

    print("Exchanging code for token...")
    token = exchange(code, client_id, client_secret, verifier)

    TOKEN_PATH.write_text(json.dumps(token, indent=2))
    print()
    print("✅ Token saved to:", TOKEN_PATH)
    print("   Scopes granted:", token.get("scope", "(unknown)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
