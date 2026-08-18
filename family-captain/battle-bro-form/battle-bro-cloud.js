/**
 * Battle Brother cloud client — magic-link auth + D1 sync.
 * Tries https://bb.usmcmin.com first, then the workers.dev fallback
 * (some local DNS stubs still NXDOMAIN on the custom domain).
 */
(function (global) {
  'use strict';

  var SESSION_KEY = 'fc_bb_session_v1';
  var PRIMARY_BASE = 'https://bb.usmcmin.com';
  var FALLBACK_BASE = 'https://usmcmin-battle-bro-sync.usmcministries2022.workers.dev';
  var resolvedBase = null;

  function configuredBase() {
    if (global.BB_API_BASE) return String(global.BB_API_BASE).replace(/\/$/, '');
    return null;
  }

  function apiBase() {
    return resolvedBase || configuredBase() || PRIMARY_BASE;
  }

  async function probe(base) {
    try {
      var res = await fetch(base + '/api/bb/health', {
        method: 'GET',
        headers: { Accept: 'application/json' },
      });
      if (!res.ok) return false;
      var data = await res.json();
      return !!(data && data.ok);
    } catch (e) {
      return false;
    }
  }

  async function ensureBase() {
    if (resolvedBase) return resolvedBase;
    var forced = configuredBase();
    if (forced) {
      resolvedBase = forced;
      return resolvedBase;
    }
    if (await probe(PRIMARY_BASE)) {
      resolvedBase = PRIMARY_BASE;
      return resolvedBase;
    }
    if (await probe(FALLBACK_BASE)) {
      resolvedBase = FALLBACK_BASE;
      return resolvedBase;
    }
    resolvedBase = PRIMARY_BASE;
    return resolvedBase;
  }

  function loadSession() {
    try {
      return JSON.parse(localStorage.getItem(SESSION_KEY)) || null;
    } catch (e) {
      return null;
    }
  }

  function saveSession(sess) {
    try {
      if (sess) localStorage.setItem(SESSION_KEY, JSON.stringify(sess));
      else localStorage.removeItem(SESSION_KEY);
    } catch (e) {}
  }

  async function request(path, options) {
    options = options || {};
    await ensureBase();
    var headers = Object.assign({ Accept: 'application/json' }, options.headers || {});
    if (options.body && !headers['Content-Type']) headers['Content-Type'] = 'application/json';
    var sess = loadSession();
    if (sess && sess.sessionToken) headers.Authorization = 'Bearer ' + sess.sessionToken;

    async function once(base) {
      var res = await fetch(base + path, {
        method: options.method || 'GET',
        headers: headers,
        body: options.body ? JSON.stringify(options.body) : undefined,
      });
      var data = null;
      try { data = await res.json(); } catch (e) { data = null; }
      return { ok: res.ok, status: res.status, data: data, base: base };
    }

    try {
      return await once(apiBase());
    } catch (e) {
      // Custom domain DNS failure → try workers.dev once
      if (apiBase() !== FALLBACK_BASE && !configuredBase()) {
        try {
          var alt = await once(FALLBACK_BASE);
          resolvedBase = FALLBACK_BASE;
          return alt;
        } catch (e2) {
          throw e;
        }
      }
      throw e;
    }
  }

  async function health() {
    try {
      await ensureBase();
      var r = await request('/api/bb/health');
      return !!(r.ok && r.data && r.data.ok);
    } catch (e) {
      return false;
    }
  }

  async function requestMagicLink(email) {
    return request('/api/bb/auth/request', { method: 'POST', body: { email: email } });
  }

  async function verifyMagic(token, name) {
    var r = await request('/api/bb/auth/verify', {
      method: 'POST',
      body: { token: token, name: name || '' },
    });
    if (r.ok && r.data && r.data.sessionToken) {
      saveSession({
        sessionToken: r.data.sessionToken,
        user: r.data.user,
        signedInAt: new Date().toISOString(),
      });
    }
    return r;
  }

  async function logout() {
    try { await request('/api/bb/auth/logout', { method: 'POST', body: {} }); } catch (e) {}
    saveSession(null);
  }

  async function me() {
    var r = await request('/api/bb/me');
    if (r.ok && r.data && r.data.user) {
      var sess = loadSession() || {};
      sess.user = r.data.user;
      sess.brother = r.data.brother || null;
      saveSession(sess);
    }
    if (r.status === 401) saveSession(null);
    return r;
  }

  async function pullSync() {
    return request('/api/bb/sync');
  }

  async function pushSync(state, updatedAt) {
    return request('/api/bb/sync', {
      method: 'PUT',
      body: { state: state, updatedAt: updatedAt || null },
    });
  }

  async function inviteBrother(email) {
    return request('/api/bb/pair/invite', { method: 'POST', body: { email: email } });
  }

  async function acceptInvite(code) {
    return request('/api/bb/pair/accept', { method: 'POST', body: { code: code } });
  }

  async function unlinkBrother() {
    return request('/api/bb/pair/unlink', { method: 'POST', body: {} });
  }

  async function fetchBrotherPack() {
    return request('/api/bb/brother');
  }

  global.BBCloud = {
    apiBase: apiBase,
    ensureBase: ensureBase,
    loadSession: loadSession,
    saveSession: saveSession,
    health: health,
    requestMagicLink: requestMagicLink,
    verifyMagic: verifyMagic,
    logout: logout,
    me: me,
    pullSync: pullSync,
    pushSync: pushSync,
    inviteBrother: inviteBrother,
    acceptInvite: acceptInvite,
    unlinkBrother: unlinkBrother,
    fetchBrotherPack: fetchBrotherPack,
  };
})(window);
