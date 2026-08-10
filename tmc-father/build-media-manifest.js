#!/usr/bin/env node
'use strict';
/*
 * build-media-manifest.js — record what course media exists, so the site can
 * version its media URLs deterministically.
 *
 *   node tmc-father/build-media-manifest.js
 *
 * Why this file exists. Course media is served from R2 with
 * `cache-control: immutable, max-age=31536000` on filenames that never change,
 * so replacing a graphic in place is invisible to anyone who already loaded it
 * — for a year. The cure is stamping a version onto the media URLs, and the
 * version has to move whenever the media moves.
 *
 * It cannot be derived from the media on disk: audio, video, slides and
 * infographics are gitignored and live only in the R2 bucket, so a fresh clone
 * or a CI runner has none of them and would compute a different version than
 * this machine. That would either bust every reader's cache for nothing or
 * quietly stamp the wrong version.
 *
 * So the manifest is committed. It is the one artifact that always travels
 * with the repo, and `render-field-manual.js` hashes it to get MEDIA_VERSION.
 * `sync-media.sh --apply` rebuilds it as part of uploading, which means
 * replacing a graphic and pushing it live bumps the version on its own — the
 * step that used to be a hand-edited date string a person had to remember.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..', 'assets', 'media', 'tmc-father');
const OUT = path.join(__dirname, 'media-manifest.json');

function walk(dir, acc) {
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch {
    return acc;
  }
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    if (entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, acc);
    else {
      try {
        acc[path.relative(ROOT, full).split(path.sep).join('/')] = fs.statSync(full).size;
      } catch { /* unreadable file — skip rather than fail the build */ }
    }
  }
  return acc;
}

const files = walk(ROOT, {});
const count = Object.keys(files).length;

if (!count) {
  console.error(
    'No media found under assets/media/tmc-father.\n' +
    'Refusing to write an empty manifest — that would bust every reader\'s cache.\n' +
    'Restore the media first (see tmc-father/sync-media.sh).'
  );
  process.exit(1);
}

// Guard against writing a manifest that has lost most of its entries, which
// usually means the gitignored media simply is not on this machine.
if (fs.existsSync(OUT)) {
  try {
    const prev = JSON.parse(fs.readFileSync(OUT, 'utf8'));
    const prevCount = Object.keys(prev.files || {}).length;
    if (prevCount && count < prevCount * 0.75) {
      console.error(
        `Manifest would drop from ${prevCount} to ${count} files.\n` +
        'That looks like missing local media rather than a real deletion. Refusing.\n' +
        'Pass --force if the removal is intentional.'
      );
      if (!process.argv.includes('--force')) process.exit(1);
    }
  } catch { /* unreadable previous manifest — just overwrite */ }
}

fs.writeFileSync(OUT, JSON.stringify({ files }, null, 2) + '\n');
console.log(`Wrote ${path.relative(process.cwd(), OUT)} — ${count} media files.`);
