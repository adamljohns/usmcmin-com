/**
 * Battle Brother cloud client — magic-link auth + D1 sync.
 * Expects API at window.BB_API_BASE (default https://bb.usmcmin.com).
 */
(function (global) {
  'use strict';

  var SESSION_KEY = 'fc_bb_session_v1';
  var DEFAULT_BASE = 'https://bb.usmcmin.com';

  function apiBase() {
    return String(global.BB_API_BASE || DEFAULT_BASE).replace(/\/$/, '');
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
    var headers = Object.assign({ Accept: 'application/json' }, options.headers || {});
    if (options.body && !headers['Content-Type']) headers['Content-Type'] = 'application/json';
    var sess = loadSession();
    if (sess && sess.sessionToken) headers.Authorization = 'Bearer ' + sess.sessionToken;
    var res = await fetch(apiBase() + path, {
      method: options.method || 'GET',
      headers: headers,
      body: options.body ? JSON.stringify(options.body) : undefined,
    });
    var data = null;
    try { data = await res.json(); } catch (e) { data = null; }
    return { ok: res.ok, status: res.status, data: data };
  }

  async function health() {
    try {
      var r = await request('/api/bb/health');
      return !!(r.ok && r.data && r.data.ok);
    } catch (e) {
      return false;
    }
  }

  async function register(email, pin, name) {
    var r = await request('/api/bb/auth/register', {
      method: 'POST',
      body: { email: email, pin: pin, name: name || '' },
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

  async function login(email, pin) {
    var r = await request('/api/bb/auth/login', {
      method: 'POST',
      body: { email: email, pin: pin },
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

  async function setPin(pin) {
    return request('/api/bb/auth/set-pin', { method: 'POST', body: { pin: pin } });
  }

  async function requestPinReset(email) {
    return request('/api/bb/auth/reset-request', { method: 'POST', body: { email: email } });
  }

  async function confirmPinReset(email, code, pin) {
    return request('/api/bb/auth/reset', {
      method: 'POST',
      body: { email: email, code: code, pin: pin },
    });
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
    loadSession: loadSession,
    saveSession: saveSession,
    health: health,
    register: register,
    login: login,
    setPin: setPin,
    requestPinReset: requestPinReset,
    confirmPinReset: confirmPinReset,
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
