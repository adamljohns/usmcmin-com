'use strict';

/* Rename freshly downloaded Notebook by Gemini artifacts to the repo's
 * kebab-case convention.
 *
 *   node tmc-husband/normalize-media.js [--apply]
 *
 * The CLI writes Google's display titles verbatim ("Marriage Quiz.html",
 * "From _We_ to _Me__ Navigating the Seasons.md"), which are hostile as URLs.
 * Without --apply this only prints the plan.
 */

const fs = require('node:fs');
const path = require('node:path');

const MEDIA_ROOT = path.resolve(__dirname, '..', 'assets', 'media', 'tmc-husband');
const APPLY = process.argv.includes('--apply');

function kebab(name) {
  const ext = path.extname(name);
  return `${path.basename(name, ext)
    .normalize('NFKD')
    .replace(/[‘’“”]/g, '')
    .replace(/[—–]/g, '-')
    .replace(/&/g, ' and ')
    .replace(/[^a-zA-Z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .toLowerCase()}${ext.toLowerCase()}`;
}

function run() {
  if (!fs.existsSync(MEDIA_ROOT)) return;
  let planned = 0;
  for (const moduleId of fs.readdirSync(MEDIA_ROOT).filter((n) => /^m\d\d$/.test(n)).sort()) {
    for (const group of fs.readdirSync(path.join(MEDIA_ROOT, moduleId)).sort()) {
      const dir = path.join(MEDIA_ROOT, moduleId, group);
      if (!fs.statSync(dir).isDirectory()) continue;
      for (const name of fs.readdirSync(dir).sort()) {
        if (name.endsWith('.tmp') || name.startsWith('.')) continue;
        const target = kebab(name);
        if (target === name) continue;
        const from = path.join(dir, name);
        const to = path.join(dir, target);
        if (fs.existsSync(to)) {
          console.log(`SKIP  ${moduleId}/${group}/${name} -> ${target} (target exists)`);
          continue;
        }
        planned += 1;
        console.log(`${APPLY ? 'MOVE ' : 'PLAN '} ${moduleId}/${group}/${name} -> ${target}`);
        if (APPLY) fs.renameSync(from, to);
      }
    }
  }
  console.log(`${planned} file(s) ${APPLY ? 'renamed' : 'to rename'}.`);
}

if (require.main === module) run();

module.exports = { kebab, run };
