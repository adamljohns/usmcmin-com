/**
 * Battle Brother cloud client — magic-link auth + D1 sync.
 *
 * Prefer workers.dev (reliable), then custom domain bb.usmcmin.com.
 * Some Mac stub resolvers still NXDOMAIN the custom domain; a hung DNS
 * lookup used to make the "Email magic link" button look dead.
 */
(function (global) {
  'use strict';

  var SESSION_KEY = 'fc_bb_session_v1';
  var PRIMARY_BASE = 'https://usmcmin-battle-bro-sync.usmcministries2022.workers.dev';
  var ALT_BASE = 'https://bb.usmcmin.com';
  var PROBE_MS = 4000;
  var REQUEST_MS = 12000;
  var resolvedBase = null;
  var lastError = null;

  function configuredBase() {
    if (global.BB_API_BASE) return String(global.BB_API_BASE).replace(/\/$/, '');
    return null;
  }

  function apiBase() {
    return resolvedBase || configuredBase() || PRIMARY_BASE;
  }

  function withTimeout(ms, label) {
    var ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    var timer = null;
    if (ctrl) {
      timer = setTimeout(function () {
        try { ctrl.abort(); } catch (e) {}
      }, ms);
    }
    return {
      signal: ctrl ? ctrl.signal : undefined,
      clear: function () { if (timer) clearTimeout(timer); },
      label: label || 'timeout',
    };
  }

  async function probe(base) {
    var t = withTimeout(PROBE_MS, 'probe');
    try {
      var res = await fetch(base + '/api/bb/health', {
        method: 'GET',
        headers: { Accept: 'application/json' },
        signal: t.signal,
      });
      if (!res.ok) return false;
      var data = await res.json();
      return !!(data && data.ok);
    } catch (e) {
      return false;
    } finally {
      t.clear();
    }
  }

  async function ensureBase() {
    if (resolvedBase) return resolvedBase;
    var forced = configuredBase();
    if (forced) {
      resolvedBase = forced;
      return resolvedBase;
    }
    // workers.dev first — custom domain DNS is flaky on some Macs.
    if (await probe(PRIMARY_BASE)) {
      resolvedBase = PRIMARY_BASE;
      return resolvedBase;
    }
    if (await probe(ALT_BASE)) {
      resolvedBase = ALT_BASE;
      return resolvedBase;
    }
    // Last resort: still point at workers.dev so errors are actionable.
    resolvedBase = PRIMARY_BASE;
    lastError = 'health_probe_failed';
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
      var t = withTimeout(REQUEST_MS, 'request');
      try {
        var res = await fetch(base + path, {
          method: options.method || 'GET',
          headers: headers,
          body: options.body ? JSON.stringify(options.body) : undefined,
          signal: t.signal,
        });
        var data = null;
        try { data = await res.json(); } catch (e) { data = null; }
        return { ok: res.ok, status: res.status, data: data, base: base };
      } finally {
        t.clear();
      }
    }

    try {
      var first = await once(apiBase());
      lastError = null;
      return first;
    } catch (e) {
      lastError = String(e && e.name === 'AbortError' ? 'timeout' : (e && e.message) || e);
      var other = apiBase() === PRIMARY_BASE ? ALT_BASE : PRIMARY_BASE;
      if (!configuredBase() && other !== apiBase()) {
        try {
          var alt = await once(other);
          resolvedBase = other;
          lastError = null;
          return alt;
        } catch (e2) {
          lastError = String(e2 && e2.name === 'AbortError' ? 'timeout' : (e2 && e2.message) || e2);
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
      lastError = String(e && e.message || e);
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
    lastError: function () { return lastError; },
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
