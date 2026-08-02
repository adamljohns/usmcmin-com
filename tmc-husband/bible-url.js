'use strict';

const BIBLE_BASE = 'https://usmcmin.org/bible.html';

function normalizeDashes(text) {
  return text.replace(/[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]/g, '-');
}

function expandCommaVerses(ref) {
  const normalized = normalizeDashes(ref).trim();
  const match = normalized.match(/^(.+?)\s+(\d+)\s*:\s*(.+)$/);
  if (!match) {
    return [normalized.replace(/\s+/g, ' ')];
  }

  const book = match[1].trim();
  const chapter = match[2];
  const segments = match[3].split(',').map((part) => part.trim()).filter(Boolean);

  return segments.map((segment) => {
    if (/\d\s*:\s*\d/.test(segment)) {
      return `${book} ${segment}`.replace(/\s+/g, ' ');
    }
    return `${book} ${chapter}:${segment}`.replace(/\s+/g, ' ');
  });
}

function parseScriptureReference(reference) {
  const normalized = normalizeDashes(reference).trim();
  if (!normalized) return [];

  if (normalized.includes(';')) {
    const chunks = normalized.split(';').map((part) => part.trim()).filter(Boolean);
    let bookPrefix = '';
    const results = [];

    for (const chunk of chunks) {
      if (/^\d*\s*[A-Za-z]/.test(chunk)) {
        bookPrefix = chunk.replace(/\s+\d+\s*:.*/, '').trim();
        results.push(...expandCommaVerses(chunk));
      } else if (bookPrefix) {
        results.push(...expandCommaVerses(`${bookPrefix} ${chunk}`));
      } else {
        results.push(...expandCommaVerses(chunk));
      }
    }

    return results;
  }

  return expandCommaVerses(normalized);
}

function bibleUrl(reference) {
  const parts = parseScriptureReference(reference);
  if (!parts.length) return BIBLE_BASE;
  if (parts.length === 1) {
    return `${BIBLE_BASE}?ref=${encodeURIComponent(parts[0])}`;
  }
  return `${BIBLE_BASE}?refs=${encodeURIComponent(parts.join(';'))}`;
}

module.exports = { bibleUrl, parseScriptureReference };
