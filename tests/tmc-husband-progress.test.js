'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const Progress = require('../assets/js/tmc-husband.v1.js');

class MemoryStorage {
  constructor(initial = {}) { this.values = new Map(Object.entries(initial)); }
  getItem(key) { return this.values.has(key) ? this.values.get(key) : null; }
  setItem(key, value) { this.values.set(key, String(value)); }
  removeItem(key) { this.values.delete(key); }
}

const MODULE_KEYS = ['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07'];

test('default state has versioned namespace and seven false flags', () => {
  assert.equal(Progress.STORAGE_KEY, 'usmcmin:tmc-husband:v1:progress');
  const state = Progress.createDefaultState();
  assert.equal(state.schemaVersion, 1);
  assert.deepEqual(Object.keys(state.modules), MODULE_KEYS);
  assert.ok(MODULE_KEYS.every((key) => state.modules[key] === false));
  assert.equal(state.lastModule, null);
  assert.deepEqual(Progress.deriveProgress(state), { completed: 0, total: 7, percent: 0, isComplete: false });
});

test('loadState recovers malformed and wrong-version storage without false completion', () => {
  for (const raw of ['{bad json', 'null', '[]', JSON.stringify({ schemaVersion: 999, modules: { m01: true } })]) {
    const storage = new MemoryStorage({ [Progress.STORAGE_KEY]: raw });
    const state = Progress.loadState(storage);
    assert.deepEqual(state, Progress.createDefaultState());
    assert.equal(storage.getItem(Progress.STORAGE_KEY), JSON.stringify(Progress.createDefaultState()));
  }
});

test('loadState accepts only exact boolean module values and valid last module', () => {
  const raw = JSON.stringify({
    schemaVersion: 1,
    modules: { m01: true, m02: 'true', m03: 1, m04: false, extra: true },
    lastModule: 'extra'
  });
  const state = Progress.loadState(new MemoryStorage({ [Progress.STORAGE_KEY]: raw }));
  assert.equal(state.modules.m01, true);
  assert.equal(state.modules.m02, false);
  assert.equal(state.modules.m03, false);
  assert.equal(state.modules.m04, false);
  assert.equal(state.lastModule, null);
  assert.equal(Progress.deriveProgress(state).completed, 1);
  assert.equal(Progress.deriveProgress(state).percent, 14);
});

test('toggleModule persists completion and last module, and can undo completion', () => {
  const storage = new MemoryStorage();
  let state = Progress.toggleModule(storage, 'm03');
  assert.equal(state.modules.m03, true);
  assert.equal(state.lastModule, 'm03');
  assert.equal(Progress.loadState(storage).modules.m03, true);

  state = Progress.toggleModule(storage, 'm03');
  assert.equal(state.modules.m03, false);
  assert.equal(state.lastModule, 'm03');
  assert.equal(Progress.deriveProgress(state).completed, 0);
  assert.throws(() => Progress.toggleModule(storage, 'm99'), /Unknown module/);
});

test('derived progress rounds percentage and reset clears every local flag', () => {
  const storage = new MemoryStorage();
  Progress.toggleModule(storage, 'm01');
  Progress.toggleModule(storage, 'm04');
  Progress.toggleModule(storage, 'm07');
  assert.deepEqual(Progress.deriveProgress(Progress.loadState(storage)), {
    completed: 3, total: 7, percent: 43, isComplete: false
  });
  const reset = Progress.resetState(storage);
  assert.deepEqual(reset, Progress.createDefaultState());
  assert.deepEqual(Progress.loadState(storage), Progress.createDefaultState());
});
