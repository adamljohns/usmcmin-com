'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const {
  MODULE_KEYS,
  normalizeProgress,
  mergeProgress,
  normalizeConsent,
  createFirebaseAdapter
} = require('../assets/js/tmc-husband-firebase.v1.js');

const blankModules = () => Object.fromEntries(MODULE_KEYS.map((key) => [key, false]));

test('normalizeProgress emits exactly m01..m07 and accepts only literal booleans', () => {
  const normalized = normalizeProgress({
    modules: {m01: true, m02: 1, m03: 'true', m07: false, m08: true},
    lastModule: 'm08'
  });
  assert.deepEqual(normalized.modules, {...blankModules(), m01: true});
  assert.equal(normalized.lastModule, null);
  assert.deepEqual(Object.keys(normalized.modules), MODULE_KEYS);
});

test('normalizeProgress safely recovers from null and malformed module containers', () => {
  assert.deepEqual(normalizeProgress(null).modules, blankModules());
  assert.deepEqual(normalizeProgress({modules: []}).modules, blankModules());
  assert.deepEqual(normalizeProgress({modules: Object.create({m01: true})}).modules, blankModules());
});

test('mergeProgress is a monotonic union over exactly seven modules', () => {
  const local = {modules: {m01: true, m02: false, extra: true}, lastModule: 'm01'};
  const cloud = {modules: {m01: false, m02: true, m07: true}, lastModule: 'm07'};
  const merged = mergeProgress(local, cloud);
  assert.deepEqual(merged.modules, {...blankModules(), m01: true, m02: true, m07: true});
  assert.equal(merged.lastModule, 'm01');
  assert.deepEqual(Object.keys(merged.modules), MODULE_KEYS);
});

test('normalizeConsent trims and lowercases a bounded valid email', () => {
  assert.deepEqual(normalizeConsent({
    email: '  Husband.Example@Example.COM ',
    subscribed: true,
    consentVersion: 1,
    source: 'tmc-husband-course'
  }), {
    email: 'husband.example@example.com',
    subscribed: true,
    consentVersion: 1,
    source: 'tmc-husband-course'
  });
});

test('normalizeConsent rejects malformed, oversized, implicit, or unknown consent', () => {
  const base = {email: 'h@example.com', subscribed: true, consentVersion: 1, source: 'tmc-husband-course'};
  for (const bad of [
    {...base, email: 'not-an-email'},
    {...base, email: `${'a'.repeat(244)}@example.com`},
    {...base, subscribed: 1},
    {...base, consentVersion: 2},
    {...base, source: 'newsletter'},
    {...base, journal: 'private'}
  ]) assert.throws(() => normalizeConsent(bad), TypeError);
});

test('feature kill flag prevents Firebase service calls and preserves local progress', async () => {
  let calls = 0;
  const services = new Proxy({}, {get: () => async () => { calls += 1; }});
  const adapter = createFirebaseAdapter({enabled: false, services});
  const result = await adapter.initialize({modules: {m03: true}});
  assert.equal(calls, 0);
  assert.equal(result.syncStatus, 'disabled');
  assert.equal(result.progress.modules.m03, true);
});

test('anonymous initialization merges cloud progress and reports synced', async () => {
  const writes = [];
  const services = {
    ensureAnonymous: async () => ({uid: 'anon-1', isAnonymous: true}),
    readProgress: async () => ({modules: {m02: true}}),
    writeProgress: async (uid, progress) => writes.push([uid, progress])
  };
  const result = await createFirebaseAdapter({services}).initialize({modules: {m01: true}});
  assert.equal(result.syncStatus, 'synced');
  assert.deepEqual(result.progress.modules, {...blankModules(), m01: true, m02: true});
  assert.equal(writes[0][0], 'anon-1');
});

test('Firebase failure remains local and reports sync pending without throwing', async () => {
  const adapter = createFirebaseAdapter({services: {ensureAnonymous: async () => { throw new Error('offline'); }}});
  const result = await adapter.initialize({modules: {m04: true}});
  assert.equal(result.syncStatus, 'pending');
  assert.equal(result.progress.modules.m04, true);
  assert.match(result.error.message, /offline/);
});

test('Google linking uses link-first and merges into linked account', async () => {
  const events = [];
  const services = {
    linkGoogle: async () => { events.push('link'); return {uid: 'google-1', isAnonymous: false}; },
    readProgress: async () => ({modules: {m06: true}}),
    writeProgress: async (uid, progress) => events.push([uid, progress.modules])
  };
  const result = await createFirebaseAdapter({services}).linkGoogle({modules: {m05: true}});
  assert.equal(result.accountMerge, 'linked');
  assert.equal(result.progress.modules.m05, true);
  assert.equal(result.progress.modules.m06, true);
  assert.equal(events[0], 'link');
});

test('existing-account fallback signs in then union-merges without progress loss', async () => {
  const events = [];
  const credential = {providerId: 'google.com'};
  const conflict = Object.assign(new Error('exists'), {code: 'auth/credential-already-in-use', credential});
  const services = {
    linkGoogle: async () => { events.push('link'); throw conflict; },
    signInGoogle: async (received) => { events.push(['signIn', received]); return {uid: 'existing-1'}; },
    readProgress: async () => ({modules: {m01: true}}),
    writeProgress: async (uid, progress) => events.push(['write', uid, progress.modules])
  };
  const result = await createFirebaseAdapter({services}).linkGoogle({modules: {m07: true}});
  assert.equal(result.accountMerge, 'existing-account');
  assert.equal(result.syncStatus, 'synced');
  assert.equal(result.progress.modules.m01, true);
  assert.equal(result.progress.modules.m07, true);
  assert.deepEqual(events[1], ['signIn', credential]);
});

test('failed progress sync returns dirty pending state', async () => {
  const services = {writeProgress: async () => { throw new Error('quota'); }};
  const result = await createFirebaseAdapter({services}).syncProgress('uid-1', {modules: {m03: true}});
  assert.equal(result.syncStatus, 'pending');
  assert.equal(result.dirty, true);
  assert.equal(result.progress.modules.m03, true);
});

test('subscribe and unsubscribe write only normalized consent payloads', async () => {
  const writes = [];
  const services = {writeConsent: async (uid, consent) => writes.push([uid, consent])};
  const adapter = createFirebaseAdapter({services});
  const subscribed = await adapter.saveConsent('uid-1', {
    email: ' H@Example.com ', subscribed: true, consentVersion: 1, source: 'tmc-husband-course'
  });
  const unsubscribed = await adapter.saveConsent('uid-1', {
    email: 'h@example.com', subscribed: false, consentVersion: 1, source: 'tmc-husband-course'
  });
  assert.equal(subscribed.syncStatus, 'synced');
  assert.equal(unsubscribed.consent.subscribed, false);
  assert.deepEqual(Object.keys(writes[0][1]).sort(), ['consentVersion', 'email', 'source', 'subscribed']);
});
