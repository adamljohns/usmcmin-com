/**
 * usmcmin-battle-bro-sync
 * Magic-link auth + habit / share sync for The Family Captain Battle Brother module.
 */
const MAGIC_TTL_MS = 20 * 60 * 1000;
const SESSION_TTL_MS = 90 * 24 * 60 * 60 * 1000;
const INVITE_TTL_MS = 14 * 24 * 60 * 60 * 1000;

export default {
  async fetch(request, env) {
    try {
      if (request.method === 'OPTIONS') return cors(env, request, new Response(null, { status: 204 }));

      const url = new URL(request.url);
      const path = url.pathname.replace(/\/+$/, '') || '/';

      if (request.method === 'GET' && (path === '/' || path === '/health' || path === '/api/bb/health')) {
        return cors(env, request, json({ ok: true, service: 'battle-bro-sync', ts: new Date().toISOString() }));
      }

      if (request.method === 'POST' && path === '/api/bb/auth/request') {
        return cors(env, request, await authRequest(request, env));
      }
      if (request.method === 'POST' && path === '/api/bb/auth/verify') {
        return cors(env, request, await authVerify(request, env));
      }
      if (request.method === 'POST' && path === '/api/bb/auth/logout') {
        return cors(env, request, await authLogout(request, env));
      }
      if (request.method === 'GET' && path === '/api/bb/me') {
        return cors(env, request, await me(request, env));
      }
      if (request.method === 'GET' && path === '/api/bb/sync') {
        return cors(env, request, await syncGet(request, env));
      }
      if (request.method === 'PUT' && path === '/api/bb/sync') {
        return cors(env, request, await syncPut(request, env));
      }
      if (request.method === 'POST' && path === '/api/bb/pair/invite') {
        return cors(env, request, await pairInvite(request, env));
      }
      if (request.method === 'POST' && path === '/api/bb/pair/accept') {
        return cors(env, request, await pairAccept(request, env));
      }
      if (request.method === 'POST' && path === '/api/bb/pair/unlink') {
        return cors(env, request, await pairUnlink(request, env));
      }
      if (request.method === 'GET' && path === '/api/bb/brother') {
        return cors(env, request, await brotherShared(request, env));
      }

      return cors(env, request, json({ error: 'not_found' }, 404));
    } catch (err) {
      console.error(err);
      return cors(env, request, json({ error: 'server_error', detail: String(err && err.message || err) }, 500));
    }
  },
};

function cors(env, request, response) {
  const origin = request.headers.get('Origin') || '';
  const allowed = String(env.CORS_ORIGINS || 'https://usmcmin.com')
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean);
  const headers = new Headers(response.headers);
  if (allowed.includes(origin) || allowed.includes('*')) {
    headers.set('Access-Control-Allow-Origin', origin || '*');
    headers.set('Vary', 'Origin');
  } else if (!origin) {
    // same-origin / curl
  }
  headers.set('Access-Control-Allow-Methods', 'GET,POST,PUT,OPTIONS');
  headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  headers.set('Access-Control-Max-Age', '86400');
  return new Response(response.body, { status: response.status, headers });
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}

function nowIso() {
  return new Date().toISOString();
}

function plusMs(ms) {
  return new Date(Date.now() + ms).toISOString();
}

function normalizeEmail(email) {
  return String(email || '').trim().toLowerCase();
}

function validEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function sha256Hex(text) {
  const data = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest('SHA-256', data);
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

function randomToken(bytes = 32) {
  const arr = new Uint8Array(bytes);
  crypto.getRandomValues(arr);
  return [...arr].map((b) => b.toString(16).padStart(2, '0')).join('');
}

async function readJson(request) {
  try {
    return await request.json();
  } catch {
    return {};
  }
}

function bearer(request) {
  const h = request.headers.get('Authorization') || '';
  const m = h.match(/^Bearer\s+(.+)$/i);
  return m ? m[1].trim() : '';
}

async function requireUser(request, env) {
  const token = bearer(request);
  if (!token) return { error: json({ error: 'unauthorized' }, 401) };
  const tokenHash = await sha256Hex(token);
  const row = await env.DB.prepare(
    `SELECT s.user_id, s.expires_at, u.email, u.name, u.brother_id
     FROM sessions s JOIN users u ON u.id = s.user_id
     WHERE s.token_hash = ?`
  ).bind(tokenHash).first();
  if (!row) return { error: json({ error: 'unauthorized' }, 401) };
  if (row.expires_at < nowIso()) {
    await env.DB.prepare('DELETE FROM sessions WHERE token_hash = ?').bind(tokenHash).run();
    return { error: json({ error: 'session_expired' }, 401) };
  }
  return {
    user: {
      id: row.user_id,
      email: row.email,
      name: row.name || '',
      brotherId: row.brother_id || null,
    },
    tokenHash,
  };
}

async function ensureUser(env, email, name) {
  const existing = await env.DB.prepare('SELECT id, email, name, brother_id FROM users WHERE email = ?')
    .bind(email).first();
  if (existing) {
    if (name && name !== existing.name) {
      await env.DB.prepare('UPDATE users SET name = ?, updated_at = ? WHERE id = ?')
        .bind(name, nowIso(), existing.id).run();
      existing.name = name;
    }
    return existing;
  }
  const id = 'u_' + randomToken(8);
  const ts = nowIso();
  await env.DB.prepare(
    'INSERT INTO users (id, email, name, brother_id, created_at, updated_at) VALUES (?, ?, ?, NULL, ?, ?)'
  ).bind(id, email, name || '', ts, ts).run();
  return { id, email, name: name || '', brother_id: null };
}

async function sendMagicEmail(env, to, magicUrl) {
  if (!env.RESEND_API_KEY) {
    return { sent: false, reason: 'resend_not_configured' };
  }
  const from = env.EMAIL_FROM || 'The Family Captain <noreply@usmcmin.com>';
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from,
      to: [to],
      subject: 'Your Battle Brother sign-in link',
      text:
        'Sign in to The Family Captain Battle Brother module:\n\n' +
        magicUrl +
        '\n\nThis link expires in 20 minutes. If you did not request it, ignore this email.\n',
      html:
        '<p style="font-family:Georgia,serif;color:#1E293B;">Captain,</p>' +
        '<p style="font-family:system-ui,sans-serif;color:#334155;">Sign in to your Battle Brother habit board:</p>' +
        '<p><a href="' + magicUrl + '" style="display:inline-block;background:#CE8E31;color:#fff;padding:12px 18px;text-decoration:none;font-weight:700;">Sign in</a></p>' +
        '<p style="font-family:system-ui,sans-serif;color:#6B7280;font-size:13px;">Or paste this link:<br>' + magicUrl + '</p>' +
        '<p style="font-family:system-ui,sans-serif;color:#6B7280;font-size:13px;">Expires in 20 minutes.</p>',
    }),
  });
  if (!res.ok) {
    const body = await res.text();
    console.error('resend error', res.status, body);
    return { sent: false, reason: 'resend_' + res.status };
  }
  return { sent: true };
}

async function authRequest(request, env) {
  const body = await readJson(request);
  const email = normalizeEmail(body.email);
  if (!validEmail(email)) return json({ error: 'invalid_email' }, 400);

  const token = randomToken(24);
  const tokenHash = await sha256Hex(token);
  await env.DB.prepare(
    'INSERT INTO magic_tokens (token_hash, email, expires_at, used_at) VALUES (?, ?, ?, NULL)'
  ).bind(tokenHash, email, plusMs(MAGIC_TTL_MS)).run();

  const appOrigin = (env.APP_ORIGIN || 'https://usmcmin.com').replace(/\/$/, '');
  const magicUrl = appOrigin + '/family-captain/battle-bro-form/viewform.html?magic=' + encodeURIComponent(token);
  const mail = await sendMagicEmail(env, email, magicUrl);

  const out = {
    ok: true,
    emailed: !!mail.sent,
    message: mail.sent
      ? 'Check your email for the sign-in link.'
      : 'Sign-in link created. Email delivery is not configured yet — use the returned link in development.',
  };
  // Only expose the raw link when Resend is not configured (local/dev).
  if (!mail.sent) out.devMagicUrl = magicUrl;
  return json(out);
}

async function authVerify(request, env) {
  const body = await readJson(request);
  const token = String(body.token || '').trim();
  if (!token) return json({ error: 'missing_token' }, 400);
  const tokenHash = await sha256Hex(token);
  const row = await env.DB.prepare(
    'SELECT email, expires_at, used_at FROM magic_tokens WHERE token_hash = ?'
  ).bind(tokenHash).first();
  if (!row) return json({ error: 'invalid_token' }, 400);
  if (row.used_at) return json({ error: 'token_used' }, 400);
  if (row.expires_at < nowIso()) return json({ error: 'token_expired' }, 400);

  await env.DB.prepare('UPDATE magic_tokens SET used_at = ? WHERE token_hash = ?')
    .bind(nowIso(), tokenHash).run();

  const user = await ensureUser(env, row.email, body.name || '');
  const sessionToken = randomToken(32);
  const sessionHash = await sha256Hex(sessionToken);
  await env.DB.prepare(
    'INSERT INTO sessions (token_hash, user_id, expires_at, created_at) VALUES (?, ?, ?, ?)'
  ).bind(sessionHash, user.id, plusMs(SESSION_TTL_MS), nowIso()).run();

  return json({
    ok: true,
    sessionToken,
    user: {
      id: user.id,
      email: user.email,
      name: user.name || '',
      brotherId: user.brother_id || null,
    },
  });
}

async function authLogout(request, env) {
  const token = bearer(request);
  if (token) {
    const tokenHash = await sha256Hex(token);
    await env.DB.prepare('DELETE FROM sessions WHERE token_hash = ?').bind(tokenHash).run();
  }
  return json({ ok: true });
}

async function me(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  let brother = null;
  if (auth.user.brotherId) {
    brother = await env.DB.prepare('SELECT id, email, name FROM users WHERE id = ?')
      .bind(auth.user.brotherId).first();
  }
  return json({
    ok: true,
    user: auth.user,
    brother: brother
      ? { id: brother.id, email: brother.email, name: brother.name || '' }
      : null,
  });
}

function parsePayload(raw) {
  try {
    return JSON.parse(raw || '{}');
  } catch {
    return {};
  }
}

async function syncGet(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  const row = await env.DB.prepare('SELECT payload, updated_at FROM habit_state WHERE user_id = ?')
    .bind(auth.user.id).first();
  return json({
    ok: true,
    updatedAt: row ? row.updated_at : null,
    state: row ? parsePayload(row.payload) : null,
  });
}

async function syncPut(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  const body = await readJson(request);
  if (!body || typeof body.state !== 'object' || body.state === null) {
    return json({ error: 'invalid_state' }, 400);
  }
  // Keep payload bounded (habits + checks + profile + submissions slice).
  const serialized = JSON.stringify(body.state);
  if (serialized.length > 750000) return json({ error: 'state_too_large' }, 413);

  const clientUpdated = body.updatedAt || null;
  const existing = await env.DB.prepare('SELECT updated_at, payload FROM habit_state WHERE user_id = ?')
    .bind(auth.user.id).first();

  if (existing && clientUpdated && existing.updated_at > clientUpdated) {
    // Server is newer — return it so the client can merge/reload.
    return json({
      ok: false,
      conflict: true,
      updatedAt: existing.updated_at,
      state: parsePayload(existing.payload),
    }, 409);
  }

  const ts = nowIso();
  if (existing) {
    await env.DB.prepare('UPDATE habit_state SET payload = ?, updated_at = ? WHERE user_id = ?')
      .bind(serialized, ts, auth.user.id).run();
  } else {
    await env.DB.prepare('INSERT INTO habit_state (user_id, payload, updated_at) VALUES (?, ?, ?)')
      .bind(auth.user.id, serialized, ts).run();
  }

  if (body.state.profile && body.state.profile.name) {
    await env.DB.prepare('UPDATE users SET name = ?, updated_at = ? WHERE id = ?')
      .bind(String(body.state.profile.name).slice(0, 120), ts, auth.user.id).run();
  }

  return json({ ok: true, updatedAt: ts });
}

async function pairInvite(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  const body = await readJson(request);
  const toEmail = normalizeEmail(body.email);
  if (!validEmail(toEmail)) return json({ error: 'invalid_email' }, 400);
  if (toEmail === auth.user.email) return json({ error: 'cannot_pair_self' }, 400);

  const code = randomToken(4).slice(0, 8).toUpperCase();
  await env.DB.prepare(
    'INSERT INTO pair_invites (code, from_user_id, to_email, expires_at, accepted_at) VALUES (?, ?, ?, ?, NULL)'
  ).bind(code, auth.user.id, toEmail, plusMs(INVITE_TTL_MS)).run();

  const appOrigin = (env.APP_ORIGIN || 'https://usmcmin.com').replace(/\/$/, '');
  const acceptUrl = appOrigin + '/family-captain/battle-bro-form/viewform.html?mode=habits&invite=' + encodeURIComponent(code);

  // Email invite when possible (best-effort).
  if (env.RESEND_API_KEY) {
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: env.EMAIL_FROM || 'The Family Captain <noreply@usmcmin.com>',
        to: [toEmail],
        subject: 'Battle Brother invite — The Family Captain',
        text:
          (auth.user.name || auth.user.email) +
          ' invited you as their Battle Brother.\n\n' +
          'Accept code: ' + code + '\n' +
          'Or open: ' + acceptUrl + '\n',
      }),
    }).catch(() => {});
  }

  return json({ ok: true, code, acceptUrl, toEmail });
}

async function pairAccept(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  const body = await readJson(request);
  const code = String(body.code || '').trim().toUpperCase();
  if (!code) return json({ error: 'missing_code' }, 400);

  const invite = await env.DB.prepare(
    'SELECT code, from_user_id, to_email, expires_at, accepted_at FROM pair_invites WHERE code = ?'
  ).bind(code).first();
  if (!invite) return json({ error: 'invalid_code' }, 400);
  if (invite.accepted_at) return json({ error: 'already_accepted' }, 400);
  if (invite.expires_at < nowIso()) return json({ error: 'invite_expired' }, 400);
  if (normalizeEmail(invite.to_email) !== auth.user.email) {
    return json({ error: 'invite_email_mismatch', expected: invite.to_email }, 403);
  }
  if (invite.from_user_id === auth.user.id) return json({ error: 'cannot_pair_self' }, 400);

  const ts = nowIso();
  await env.DB.batch([
    env.DB.prepare('UPDATE pair_invites SET accepted_at = ? WHERE code = ?').bind(ts, code),
    env.DB.prepare('UPDATE users SET brother_id = ?, updated_at = ? WHERE id = ?')
      .bind(invite.from_user_id, ts, auth.user.id),
    env.DB.prepare('UPDATE users SET brother_id = ?, updated_at = ? WHERE id = ?')
      .bind(auth.user.id, ts, invite.from_user_id),
  ]);

  const brother = await env.DB.prepare('SELECT id, email, name FROM users WHERE id = ?')
    .bind(invite.from_user_id).first();

  return json({
    ok: true,
    brother: brother
      ? { id: brother.id, email: brother.email, name: brother.name || '' }
      : null,
  });
}

async function pairUnlink(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  const brotherId = auth.user.brotherId;
  const ts = nowIso();
  await env.DB.prepare('UPDATE users SET brother_id = NULL, updated_at = ? WHERE id = ?')
    .bind(ts, auth.user.id).run();
  if (brotherId) {
    await env.DB.prepare(
      'UPDATE users SET brother_id = NULL, updated_at = ? WHERE id = ? AND brother_id = ?'
    ).bind(ts, brotherId, auth.user.id).run();
  }
  return json({ ok: true });
}

async function brotherShared(request, env) {
  const auth = await requireUser(request, env);
  if (auth.error) return auth.error;
  if (!auth.user.brotherId) return json({ ok: true, brother: null, pack: null });

  const brother = await env.DB.prepare('SELECT id, email, name FROM users WHERE id = ?')
    .bind(auth.user.brotherId).first();
  if (!brother) return json({ ok: true, brother: null, pack: null });

  const row = await env.DB.prepare('SELECT payload, updated_at FROM habit_state WHERE user_id = ?')
    .bind(brother.id).first();
  const state = row ? parsePayload(row.payload) : { habits: { items: [], checks: {} } };
  const items = ((state.habits && state.habits.items) || []).filter((h) => h && h.shared);
  const checks = {};
  const allChecks = (state.habits && state.habits.checks) || {};
  Object.keys(allChecks).forEach((key) => {
    const habitId = key.split('|')[0];
    if (items.some((h) => h.id === habitId)) checks[key] = true;
  });

  return json({
    ok: true,
    brother: { id: brother.id, email: brother.email, name: brother.name || '' },
    updatedAt: row ? row.updated_at : null,
    pack: {
      v: 1,
      type: 'fc_battle_brother_share',
      name: brother.name || brother.email,
      exportedAt: row ? row.updated_at : nowIso(),
      items,
      checks,
    },
  });
}
