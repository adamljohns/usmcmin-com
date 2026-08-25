'use strict';

// Focused contract for the content-complete Module 3 field-manual page.
// Module 3 is the first module built from a fully reconciled research package
// (5 sources / 17 artifacts), so it carries obligations the generic module
// template never had: provenance separation, safety distinctions, a withheld
// heavy-media disclosure, and a guarantee that regeneration cannot erase it.

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.resolve(__dirname, '..');
const PAGE = path.join(ROOT, 'tmc-husband', 'module-03.html');
const MEDIA = path.join(ROOT, 'assets', 'media', 'tmc-husband', 'm03');

const { course } = require('../tmc-husband/course.v1.js');
const { renderAll } = require('../tmc-husband/generate.js');

const read = () => fs.readFileSync(PAGE, 'utf8');
const all = (html, pattern) => Array.from(html.matchAll(pattern), (match) => match[1]);

const SOURCE_SLUGS = [
  'episode-3-transcript',
  'chatgpt-review',
  'claude-review',
  'gemini-review',
  'grok-review'
];

// 17 completed artifacts: 3 audio + 3 video + 3 slides + 3 infographics + 3 reports + 1 quiz + 1 flashcards.
const LOCAL_ARTIFACTS = {
  'slides-engineering-us': 'Engineering Us',
  'slides-marital-conflict-blueprint': 'Marital Conflict Blueprint',
  'slides-the-marriage-blueprint': 'The Marriage Blueprint',
  'infographic-conflict-resolution-field-guide': 'Marriage Conflict Resolution Field Guide',
  'infographic-conflict-and-teamwork-guide': 'Marriage Conflict and Teamwork Guide',
  'infographic-teamwork-guide': 'Marriage Teamwork Guide',
  'report-conflict-resolution-and-partnership': 'Conflict Resolution and Partnership',
  'report-from-clashing-oars-to-gliding-boats': 'From Clashing Oars to Gliding Boats',
  'report-biggest-disagreements-secret-weapon': 'Why Your Biggest Disagreements Might Actually Be Your Relationship',
  'quiz-marriage-quiz': 'Marriage Quiz',
  'flashcards-marriage-flashcards': 'Marriage Flashcards'
};

const WITHHELD_ARTIFACTS = {
  'audio-when-good-marriage-advice-goes-wrong': 'When Good Marriage Advice Goes Wrong',
  'audio-when-marriage-tools-become-dangerous-weapons': 'When Marriage Tools Become Dangerous Weapons',
  'audio-why-your-partner-is-not-the-problem': 'Why your partner is not the problem',
  'video-how-to-externalize-marriage-conflict': 'How to Externalize Marriage Conflict',
  'video-navigating-conflict': 'Navigating Conflict',
  'video-resolving-conflict': 'Resolving Conflict'
};

const REQUIRED_SECTIONS = [
  'mission-brief',
  'scripture-frame',
  'core-framework',
  'fair-insight',
  'caution-boundary',
  'self-check',
  'pause-protocol',
  'five-steps',
  'field-action',
  'discussion-prompts',
  'conversation-guide',
  'support-boundary',
  'resources',
  'completion'
];

test('module 3 keeps the seven-module navigation and local-progress contract', () => {
  const html = read();
  assert.match(html, /<body data-course-page="m03">/);

  const buttons = all(html, /<button[^>]*data-complete-module="([^"]+)"/g);
  assert.deepEqual(buttons, ['m03'], 'exactly one reversible completion control');
  assert.match(html, /<button[^>]*data-complete-module="m03"[^>]*aria-pressed="false"/);
  assert.match(html, /type="button"[^>]*data-complete-module="m03"|data-complete-module="m03"[^>]*type="button"/);
  assert.match(html, /data-completion-message="m03"/);
  assert.match(html, /You can change this status later/i, 'completion must be honestly reversible');

  assert.ok(html.includes('href="module-02.html"'), 'previous module link');
  assert.ok(html.includes('href="module-04.html"'), 'next module link');
  assert.match(html, /data-progress-summary/);
  assert.match(html, /data-progress-short/);
  assert.match(html, /Saved only on this device/);
  assert.match(html, /no login, upload, or cross-device sync/);

  assert.match(html, /<meta name="robots" content="noindex, nofollow">/);
  assert.match(html, /class="prototype-banner"/);
  assert.match(html, /Draft pending Adam, doctrinal, editorial, and rights review\./);
});

test('module 3 reconciles exactly five sources and seventeen named artifacts', () => {
  const html = read();

  const sources = all(html, /data-source="([^"]+)"/g);
  assert.equal(sources.length, 5, 'exactly 5 reconciled sources');
  assert.deepEqual([...sources].sort(), [...SOURCE_SLUGS].sort());
  assert.match(html, /\b5\b[^<]{0,40}sources|sources[^<]{0,40}\b5\b/i);

  const artifacts = all(html, /data-artifact="([^"]+)"/g);
  assert.equal(artifacts.length, 17, 'exactly 17 completed artifacts');
  assert.deepEqual(
    [...artifacts].sort(),
    [...Object.keys(LOCAL_ARTIFACTS), ...Object.keys(WITHHELD_ARTIFACTS)].sort()
  );
  assert.match(html, /\b17\b[^<]{0,40}artifacts|artifacts[^<]{0,40}\b17\b/i);

  const states = all(html, /data-artifact-state="([^"]+)"/g);
  assert.equal(states.filter((state) => state === 'local').length, 11);
  assert.equal(states.filter((state) => state === 'withheld').length, 6);

  for (const title of [...Object.values(LOCAL_ARTIFACTS), ...Object.values(WITHHELD_ARTIFACTS)]) {
    assert.ok(html.includes(title), `artifact must be named on the page: ${title}`);
  }

  // The six heavy media files stay in the research package, with the gate named.
  for (const gate of [/rights/i, /caption/i, /transcript/i, /codec/i, /hosting/i, /Adam/]) {
    assert.match(html, gate, `withheld-media disclosure must name gate ${gate}`);
  }
  assert.match(html, /research package/i);
  assert.doesNotMatch(html, /<audio|<video|\.mp3|\.mp4/i, 'no audio or video may be shipped locally');

  assert.match(
    html,
    /https:\/\/notebooklm\.google\.com\/notebook\/9237c8b2-4f96-4cb7-9f32-040305833123/,
    'verified NotebookLM notebook link for authenticated review'
  );
});

test('module 3 ships every required field-manual section with provenance and safety separation', () => {
  const html = read();
  for (const id of REQUIRED_SECTIONS) {
    assert.match(html, new RegExp(`id="${id}"`), `missing section ${id}`);
  }

  const teaching = html.match(/Original source teaching/g) || [];
  const analysis = html.match(/U\.S\.M\.C\. Ministries analysis/g) || [];
  assert.ok(teaching.length >= 3, 'source teaching must be labelled repeatedly');
  assert.ok(analysis.length >= 3, 'ministry analysis must be labelled repeatedly');

  // Ordinary marital conflict is not any of these; joint exercises are not for unsafe marriages.
  for (const term of [
    /coercive control/i,
    /threat/i,
    /stalking/i,
    /violence/i,
    /sexual coercion/i,
    /active addiction/i,
    /retaliation/i
  ]) {
    assert.match(html, term, `safety distinction missing: ${term}`);
  }
  assert.match(html, /ordinary (marital )?conflict is not/i);
  assert.match(html, /joint exercise/i);
  assert.match(html, /Observable finish line/);
  assert.match(html, /Support and safety boundary/);

  // Core teaching structures actually taught by Episode 3.
  assert.match(html, /five steps|five-step/i);
  assert.match(html, /pause/i);
  assert.match(html, /return/i);
  assert.match(html, /Day 7|Day&nbsp;7/, 'one-week field exercise');
});

test('module 3 links only resources that exist locally, with safe external links', () => {
  const html = read();

  const refs = [
    ...all(html, /href="((?!https?:|mailto:|#)[^"]+)"/g),
    ...all(html, /src="((?!https?:|data:)[^"]+)"/g)
  ];
  assert.ok(refs.length > 0);
  for (const ref of refs) {
    const target = path.resolve(path.dirname(PAGE), decodeURIComponent(ref.split('#')[0]));
    assert.ok(fs.existsSync(target), `broken local reference: ${ref}`);
  }

  // Every copied artifact lives under a stable, spaceless media path.
  for (const slug of Object.keys(LOCAL_ARTIFACTS)) {
    const pattern = new RegExp(`data-artifact="${slug}"[\\s\\S]{0,900}?(?:href|src)="(\\.\\./assets/media/tmc-husband/m03/[^"]+)"`);
    const match = html.match(pattern);
    assert.ok(match, `local artifact ${slug} must link into assets/media/tmc-husband/m03`);
    assert.doesNotMatch(match[1], /[ %]/, `unstable filename in ${match[1]}`);
    assert.ok(fs.existsSync(path.resolve(path.dirname(PAGE), match[1])), `missing file for ${slug}`);
  }
  assert.ok(fs.existsSync(MEDIA), 'assets/media/tmc-husband/m03 must exist');

  for (const tag of html.match(/<a\b[^>]*>/g) || []) {
    if (/target="_blank"/.test(tag)) {
      assert.match(tag, /rel="[^"]*noopener[^"]*"/, tag);
      assert.match(tag, /rel="[^"]*noreferrer[^"]*"/, tag);
    }
  }

  const amazon = (html.match(/<a\b[^>]*amazon\.com[^>]*>/g) || []);
  assert.equal(amazon.length, 1, 'one optional journal link');
  assert.match(amazon[0], /https:\/\/www\.amazon\.com\/dp\/0310116694\?tag=usmcministrie-20/);
  assert.match(amazon[0], /rel="[^"]*sponsored[^"]*"/);
  assert.match(html, /Amazon Associate/i, 'sponsored disclosure');

  for (const tag of html.match(/<img\b[^>]*>/g) || []) {
    const alt = tag.match(/alt="([^"]*)"/);
    assert.ok(alt && alt[1].trim().length >= 12, `image needs useful alt text: ${tag}`);
  }
});

test('module 3 carries no placeholders, secrets, CDN dependencies, or transcript dump', () => {
  const html = read();
  assert.doesNotMatch(html, /\b(TODO|TBD|FIXME|Lorem ipsum|PLACEHOLDER|XXX)\b/i);
  assert.doesNotMatch(html, /sk-[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{12,}|api[_-]?key\s*=|Bearer\s+[A-Za-z0-9._-]{16,}/i);
  assert.doesNotMatch(html, /cdn\.|unpkg\.com|jsdelivr|fonts\.googleapis\.com|ajax\.googleapis\.com/i);
  assert.doesNotMatch(html, /<script[^>]+src="https?:/i);
  assert.doesNotMatch(html, /\[\d{2}:\d{2}:\d{2}\]/, 'no raw transcript lines');
  assert.doesNotMatch(html, /I stand by the bed where a young woman lies/i, 'no long copyrighted excerpt');
  assert.ok(html.length < 120000, 'page must stay a field manual, not a transcript republication');
});

test('regenerating the course cannot silently erase authored module 3 content', () => {
  const before = read();
  renderAll(ROOT);
  const after = read();
  assert.equal(after, before, 'generator output must reproduce the authored module 3 page byte for byte');

  const m03 = course.modules.find((module) => module.id === 'm03');
  assert.ok(m03.fieldManual, 'module 3 content must live in the canonical generation path');
  assert.equal(m03.fieldManual.sources.length, 5);
  assert.equal(m03.fieldManual.artifacts.length, 17);
  assert.equal(m03.fieldManual.artifacts.filter((artifact) => artifact.state === 'local').length, 11);
  assert.equal(m03.fieldManual.artifacts.filter((artifact) => artifact.state === 'withheld').length, 6);
});
