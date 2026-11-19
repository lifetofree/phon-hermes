# OAuth Troubleshooting for Google-Tasks

## 1. Path redaction in agent output
Hermes's `security.redact_secrets` truncates full `~/` paths in output (visible as `/Users...json`).
**Workaround**: compute paths inside Python via `os.path.expanduser("~")`, don't embed literals in agent-visible output.

## 2. Access denied at OAuth consent ("developer hasn't given you access")
User email not in Test user list of the project's OAuth consent screen. Fix:
1. Open https://console.cloud.google.com/auth/audience (switch project dropdown)
2. Add user's email to Test users
3. In browser, sign out of all Google accounts, sign back in with the test user email
4. Re-run the auth script

## 3. Externally-managed-environment on macOS
Homebrew Python 3.13+ blocks pip. Use Hermes venv:
```
HTPYTHON="${HERMES_HOME:-$HOME/.hermes}/hermes-agent/venv/bin/python3"
"$HTPYTHON" -m pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
```

## 4. Cross-project client_secret confusion
When user has multiple Google Cloud projects, the OAuth client ID in `client_secret.json` must match the project where APIs were enabled AND where the user is a test user.
**Diagnosis**: `jq -r 'to_entries[0].value.client_id' ~/.hermes/google_client_secret.json` — compare with project dropdown in Google Console.

## 5. Tasks scope missing from existing token
If google-workspace calls work but Tasks 403 — token lacks tasks scope. Run `scripts/auth_with_tasks.py` to re-authorize with full scopes.

## 6. hermes command not found in subshell
Always use full path: `$HOME/.local/bin/hermes` instead of `hermes` in scripts/subshells.

## 7. Bash heredoc gotchas
When sending Python scripts via chat:
- Use `cat > /tmp/name.py << 'PYEOF'` (quoted delimiter) to prevent shell expansion
- Long messages may be silently truncated — split if > 200 lines
- Prefer variables for paths (`HOME=$(echo ~)`) so literal doesn't appear in agent text
