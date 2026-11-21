// Probe a Rakazo model credential: decrypt secret, POST 1-token chat, print ONLY status.
// env: K = ENCRYPTION_KEY, CRED = credential id, CT = ciphertext (v2:<b64>), MODEL = model id
const crypto = require('crypto');
const raw = process.env.CT || '';
const cred = process.env.CRED || '';
const K = process.env.K || '';
const model = process.env.MODEL || '';
(async () => {
  try {
    const b64 = raw.slice(raw.indexOf(':') + 1);
    const buf = Buffer.from(b64, 'base64');
    const salt = buf.subarray(0, 16), iv = buf.subarray(16, 28), tag = buf.subarray(28, 44), ct = buf.subarray(44);
    const key = crypto.scryptSync(K, salt, 32, { N: 16384, r: 8, p: 1, maxmem: 64 * 1024 * 1024 });
    const d = crypto.createDecipheriv('aes-256-gcm', key, iv);
    d.setAAD(Buffer.from(cred)); d.setAuthTag(tag);
    const plain = Buffer.concat([d.update(ct), d.final()]).toString('utf8');
    let baseUrl, apiKey;
    try { const j = JSON.parse(plain); baseUrl = j.baseUrl || j.baseURL || j.url; apiKey = j.apiKey || j.key || j.api_key || j.token; } catch (e) {}
    if (!baseUrl || !apiKey) { const u = plain.match(/https?:\/\/[^"'\s]+/); baseUrl = u && u[0]; apiKey = plain.length ? 'guess-from-body' : null; if (!apiKey) { console.log('PARSE_ERROR'); return; } const m2 = plain.match(/"(?:apiKey|key|api_key|token)"\s*:\s*"([^"]+)"/); if (m2) apiKey = m2[1]; }
    const r = await fetch(baseUrl.replace(/\/$/, '') + '/chat/completions', {
      method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + apiKey },
      body: JSON.stringify({ model, max_tokens: 1, messages: [{ role: 'user', content: 'ping' }] }),
      signal: AbortSignal.timeout(20000)
    });
    const body = await r.text();
    if (r.ok) console.log('OK');
    else if (r.status === 429 || /insufficient|quota|balance|billing/i.test(body)) console.log('QUOTA_OUT');
    else if (r.status === 401 || r.status === 403) console.log('AUTH_FAIL');
    else console.log('OTHER ' + r.status + ' ' + body.slice(0, 120).replace(/\s+/g, ' '));
  } catch (e) { console.log('ERROR ' + String(e && e.message || e).slice(0, 100)); }
})();
