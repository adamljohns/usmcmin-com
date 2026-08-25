'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.resolve(__dirname, '..');
const COURSE_DIR = path.join(ROOT, 'tmc-husband');
const { course } = require('../tmc-husband/course.v1.js');
const { renderAll } = require('../tmc-husband/generate.js');

const REQUIRED_SECTIONS = [
  'mission-brief',
  'scripture-frame',
  'fair-insight',
  'caution-boundary',
  'self-check',
  'field-action',
  'conversation-guide',
  'support-boundary',
  'resources',
  'completion'
];

test('course definition owns exactly seven complete, ordered modules', () => {
  assert.equal(course.id, 'tmc-husband-v1');
  assert.equal(course.contentVersion, 1);
  assert.equal(course.modules.length, 7);
  assert.deepEqual(course.modules.map((module) => module.id), [
    'm01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07'
  ]);

  for (const [index, module] of course.modules.entries()) {
    assert.equal(module.number, index + 1);
    assert.match(module.title, /\S/);
    assert.match(module.question, /\?$/);
    assert.ok(module.missionBrief.join(' ').split(/\s+/).length >= 800,
      `${module.id} mission brief must be at least 800 words`);
    assert.ok(module.selfCheck.length >= 3 && module.selfCheck.length <= 5);
    assert.match(module.fieldAction.finishLine, /\S/);
    assert.ok(module.scripture.length >= 2);
    assert.ok(module.resources.length >= 2);
  }
});

test('generator emits landing, progress, and seven substantive module pages', () => {
  renderAll(ROOT);
  const routes = ['index.html', 'progress.html', ...Array.from({ length: 7 }, (_, i) => `module-${String(i + 1).padStart(2, '0')}.html`)];
  for (const route of routes) {
    assert.ok(fs.existsSync(path.join(COURSE_DIR, route)), `${route} missing`);
  }

  for (let number = 1; number <= 7; number += 1) {
    const filename = `module-${String(number).padStart(2, '0')}.html`;
    const html = fs.readFileSync(path.join(COURSE_DIR, filename), 'utf8');
    for (const section of REQUIRED_SECTIONS) {
      assert.match(html, new RegExp(`id="${section}"`), `${filename} lacks ${section}`);
    }
    assert.match(html, /<button[^>]+data-complete-module="m0[1-7]"/);
    assert.match(html, /Draft pending Adam, doctrinal, editorial, and rights review\./);
    assert.match(html, /\.\.\/assets\/css\/tmc-husband\.v1\.css/);
    assert.match(html, /\.\.\/assets\/js\/tmc-husband\.v1\.js/);
  }
});
