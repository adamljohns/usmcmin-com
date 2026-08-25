'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.join(__dirname, '..');
const authored = [
  'assets/js/tmc-husband-firebase.v1.js',
  'assets/js/tmc-husband-firebase.config.example.js',
  '.github/firebase/firebase.json',
  '.github/firebase/.firebaserc.example',
  '.github/firebase/firestore.rules',
  '.github/firebase/firestore.indexes.json',
  '.github/firebase/package.json'
];
const sources = Object.fromEntries(authored.map((file) => [file, fs.readFileSync(path.join(root, file), 'utf8')]));
const combined = Object.values(sources).join('\n');

test('authored Firebase files contain no credential-shaped secrets', () => {
  for (const pattern of [
    /AIza[0-9A-Za-z_-]{20,}/,
    /-----BEGIN [A-Z ]+PRIVATE KEY-----/,
    /["'](?:client_secret|private_key)["']\s*:/i
  ]) assert.doesNotMatch(combined, pattern);
});

test('runtime adapter contains no dynamic execution or HTML injection sinks', () => {
  const runtime = sources['assets/js/tmc-husband-firebase.v1.js'];
  for (const pattern of [/\beval\s*\(/, /\bFunction\s*\(/, /\b(?:innerHTML|outerHTML|insertAdjacentHTML|document\.write)\b/]) {
    assert.doesNotMatch(runtime, pattern);
  }
});

test('runtime and rules omit prohibited private data fields', () => {
  const dataFiles = sources['assets/js/tmc-husband-firebase.v1.js'] + sources['.github/firebase/firestore.rules'];
  assert.doesNotMatch(dataFiles, /\b(?:journal|reflection|wife|counseling|oauthToken|accessToken|refreshToken)\b/i);
});

test('Firestore grants no list operation and retains an explicit deny-all fallback', () => {
  const rules = sources['.github/firebase/firestore.rules'];
  assert.doesNotMatch(rules, /allow\s+list\s*:/);
  assert.match(rules, /match \/\{document=\*\*\}[\s\S]*allow read, write: if false;/);
  assert.match(rules, /data\.keys\(\)\.hasOnly\(keys\)/);
  assert.match(rules, /match \/users\/\{uid\}/);
  assert.match(rules, /request\.auth\.uid == uid/);
});
