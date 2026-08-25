'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {
  initializeTestEnvironment,
  assertSucceeds,
  assertFails
} = require('@firebase/rules-unit-testing');
const {doc, getDoc, setDoc, getDocs, collection, Timestamp} = require('firebase/firestore');

const PROJECT_ID = process.env.GCLOUD_PROJECT || 'demo-tmc-husband-local';
const now = Timestamp.fromMillis(1_700_000_000_000);
let env;

const modules = (overrides = {}) => ({
  m01: false, m02: false, m03: false, m04: false, m05: false, m06: false, m07: false,
  ...overrides
});
const userData = (overrides = {}) => ({
  schemaVersion: 1, createdAt: now, lastSeenAt: now, authKind: 'anonymous', ...overrides
});
const progressData = (overrides = {}) => ({
  courseId: 'tmc-husband-v1', contentVersion: 1, modules: modules(), lastModule: null,
  startedAt: now, updatedAt: now, completedAt: null, ...overrides
});
const consentData = (overrides = {}) => ({
  email: 'husband@example.com', subscribed: true, consentVersion: 1,
  source: 'tmc-husband-course', consentedAt: now, unsubscribedAt: null, ...overrides
});

function dbFor(uid) { return env.authenticatedContext(uid).firestore(); }

// Emulator host is injected by firebase emulators:exec. Keeping this guard makes the
// harness fail honestly rather than silently skipping security tests.
test.before(async () => {
  assert.ok(process.env.FIRESTORE_EMULATOR_HOST, 'Run via npm run test:emulator');
  env = await initializeTestEnvironment({
    projectId: PROJECT_ID,
    firestore: {rules: fs.readFileSync(path.join(__dirname, '..', 'firestore.rules'), 'utf8')}
  });
});
test.after(async () => { if (env) await env.cleanup(); });
test.beforeEach(async () => { if (env) await env.clearFirestore(); });

test('unauthenticated clients are denied', async () => {
  const db = env.unauthenticatedContext().firestore();
  await assertFails(getDoc(doc(db, 'users/alice')));
  await assertFails(setDoc(doc(db, 'users/alice'), userData()));
});

test('authenticated user may create and get only their valid user document', async () => {
  const db = dbFor('alice');
  await assertSucceeds(setDoc(doc(db, 'users/alice'), userData()));
  await assertSucceeds(getDoc(doc(db, 'users/alice')));
  await assertFails(getDoc(doc(db, 'users/bob')));
  await assertFails(setDoc(doc(db, 'users/bob'), userData()));
});

test('user collections cannot be listed by clients', async () => {
  await assertFails(getDocs(collection(dbFor('alice'), 'users')));
});

test('user profile rejects extra keys, invalid types, and unknown auth kind', async () => {
  const ref = doc(dbFor('alice'), 'users/alice');
  await assertFails(setDoc(ref, userData({journal: 'private'})));
  await assertFails(setDoc(ref, userData({schemaVersion: '1'})));
  await assertFails(setDoc(ref, userData({authKind: 'password'})));
});

test('owner may read and write the one exact course progress document', async () => {
  const ref = doc(dbFor('alice'), 'users/alice/courseProgress/tmc-husband-v1');
  await assertSucceeds(setDoc(ref, progressData({modules: modules({m01: true}), lastModule: 'm01'})));
  await assertSucceeds(getDoc(ref));
});

test('progress rejects cross-user access, other courses, extra module keys, and malformed values', async () => {
  const db = dbFor('alice');
  await assertFails(setDoc(doc(db, 'users/bob/courseProgress/tmc-husband-v1'), progressData()));
  await assertFails(setDoc(doc(db, 'users/alice/courseProgress/other-course'), progressData({courseId: 'other-course'})));
  const own = doc(db, 'users/alice/courseProgress/tmc-husband-v1');
  await assertFails(setDoc(own, progressData({modules: modules({m08: true})})));
  await assertFails(setDoc(own, progressData({modules: modules({m01: 1})})));
  await assertFails(setDoc(own, progressData({lastModule: 'm08'})));
  await assertFails(setDoc(own, progressData({reflection: 'private'})));
});

test('progress collections cannot be listed', async () => {
  await assertFails(getDocs(collection(dbFor('alice'), 'users/alice/courseProgress')));
});

test('owner can subscribe and unsubscribe with exact normalized consent values', async () => {
  const ref = doc(dbFor('alice'), 'users/alice/consents/field-brief');
  await assertSucceeds(setDoc(ref, consentData()));
  await assertSucceeds(setDoc(ref, consentData({subscribed: false, unsubscribedAt: now})));
  await assertSucceeds(getDoc(ref));
});

test('consent rejects other users, other records, bad email/source/version, inconsistent unsubscribe, and extra fields', async () => {
  const db = dbFor('alice');
  await assertFails(setDoc(doc(db, 'users/bob/consents/field-brief'), consentData()));
  await assertFails(setDoc(doc(db, 'users/alice/consents/admin-list'), consentData()));
  const own = doc(db, 'users/alice/consents/field-brief');
  await assertFails(setDoc(own, consentData({email: 'bad'})));
  await assertFails(setDoc(own, consentData({email: `${'a'.repeat(244)}@example.com`})));
  await assertFails(setDoc(own, consentData({source: 'newsletter'})));
  await assertFails(setDoc(own, consentData({consentVersion: 2})));
  await assertFails(setDoc(own, consentData({subscribed: false, unsubscribedAt: null})));
  await assertFails(setDoc(own, consentData({oauthToken: 'secret'})));
});

test('subscriber and consent collections cannot be listed and unmatched admin paths stay denied', async () => {
  const db = dbFor('alice');
  await assertFails(getDocs(collection(db, 'users/alice/consents')));
  await assertFails(getDocs(collection(db, 'subscribers')));
  await assertFails(getDoc(doc(db, 'admin/subscribers')));
});
