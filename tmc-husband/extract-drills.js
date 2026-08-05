'use strict';

/* Pull the flashcard + quiz payloads out of the Notebook by Gemini HTML exports
 * and write them to `tmc-husband/drills/<moduleId>.json`.
 *
 *   node tmc-husband/extract-drills.js
 *
 * The exports live at assets/media/tmc-husband/<moduleId>/{flashcards,quiz}/*.html.
 * Each one carries its content in a single HTML-escaped `data-app-data` attribute;
 * everything else in the file is ~1.3 MB of Google app shell we do not ship.
 * Re-run this after dropping new exports in, then `node tmc-husband/generate.js`.
 */

const fs = require('node:fs');
const path = require('node:path');
const { DRILL_DIR } = require('./drills.js');

const MEDIA_ROOT = path.resolve(__dirname, '..', 'assets', 'media', 'tmc-husband');
const MODULE_IDS = ['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07'];

function unescapeHtml(value) {
  return value
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&');
}

// The attribute holds one JSON object followed by trailing app state; take the
// first complete object by tracking brace depth outside of strings.
function firstJsonObject(text) {
  let depth = 0;
  let inString = false;
  let escaped = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (escaped) { escaped = false; continue; }
    if (ch === '\\') { escaped = true; continue; }
    if (ch === '"') { inString = !inString; continue; }
    if (inString) continue;
    if (ch === '{') depth += 1;
    else if (ch === '}') {
      depth -= 1;
      if (depth === 0) return text.slice(0, i + 1);
    }
  }
  return null;
}

function readExport(file) {
  const html = fs.readFileSync(file, 'utf8');
  const match = html.match(/data-app-data="(\{[\s\S]*?)"\s*>/);
  if (!match) return null;
  const slice = firstJsonObject(unescapeHtml(match[1]));
  if (!slice) return null;
  return JSON.parse(slice);
}

/* Some notebooks were built with AI critiques of the course sitting alongside the
 * lesson material, so Gemini wrote drills about them — "According to the AI
 * reviews (ChatGPT, Claude, etc.), what is the course's blind spot?", "the
 * 'Claude' critique suggests…". A man studying his marriage should never be
 * quizzed on what a chatbot thought of the curriculum. The critiques were review
 * input, not teaching. Filtering here rather than in the JSON means a re-pull
 * cannot quietly put them back. */
const REVIEW_ARTIFACT = /\b(chatgpt|claude|gemini|copilot|the ai reviews?|ai critiques?|ai-generated critique)\b/i;

function dropReviewArtifacts(moduleId, key, items) {
  const kept = items.filter((item) => {
    const text = [item && item.question, item && item.f, item && item.b]
      .filter(Boolean).join(' ');
    return !REVIEW_ARTIFACT.test(text);
  });
  const dropped = items.length - kept.length;
  if (dropped) {
    console.log(`${moduleId}: dropped ${dropped} ${key} that quizzed on the AI review notes`);
  }
  return kept;
}

function collect(moduleId) {
  const bundle = {};
  for (const [key, dir] of [['flashcards', 'flashcards'], ['quiz', 'quiz']]) {
    const folder = path.join(MEDIA_ROOT, moduleId, dir);
    if (!fs.existsSync(folder)) continue;
    for (const name of fs.readdirSync(folder).filter((n) => n.endsWith('.html'))) {
      const data = readExport(path.join(folder, name));
      if (data && Array.isArray(data[key]) && data[key].length) {
        bundle[key] = dropReviewArtifacts(moduleId, key, data[key]);
        bundle.meta = Object.assign({}, bundle.meta, { [key]: { source: name, topics: data.topics || {} } });
      }
    }
  }
  return bundle;
}

function run() {
  fs.mkdirSync(DRILL_DIR, { recursive: true });
  for (const moduleId of MODULE_IDS) {
    const bundle = collect(moduleId);
    if (!bundle.flashcards && !bundle.quiz) {
      console.log(`${moduleId}: no exports found — skipped`);
      continue;
    }
    fs.writeFileSync(path.join(DRILL_DIR, `${moduleId}.json`), `${JSON.stringify(bundle, null, 2)}\n`);
    console.log(`${moduleId}: ${(bundle.flashcards || []).length} flashcards, ${(bundle.quiz || []).length} quiz questions`);
  }
}

if (require.main === module) run();

module.exports = { run, readExport, collect };
