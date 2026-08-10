/* audit-mobile-polish.js — the two defects that most make a site feel amateur
 * on a phone, measured rather than eyeballed.
 *
 * 1. HORIZONTAL OVERFLOW. Something wider than the viewport makes the whole
 *    page scroll sideways, headings get clipped, and every section looks
 *    slightly misaligned. Reports the widest offenders so the cause is
 *    actionable, not just "the page is wide".
 *
 * 2. TAP TARGETS. Links and buttons under ~44px are hard to hit accurately.
 *    Only counts controls that are actually visible and in the flow.
 *
 * Deliberately NOT flagged: elements a reader can never reach (off-canvas skip
 * links, closed menus, display:none), inline links inside a paragraph — those
 * are normal prose, not controls, and flagging them buries the real findings.
 *
 * usage: node audit-mobile-polish.js <baseUrl> <pageListFile> [outJson] [width]
 */
'use strict';

const fs = require('fs');
const { chromium } = require('/Users/moop_bot_pro/Scripts/cdp-tmc/node_modules/playwright-core');

const BASE = process.argv[2];
const LIST = process.argv[3];
const OUT = process.argv[4] || '/tmp/mobile-polish.json';
const WIDTH = parseInt(process.argv[5] || '390', 10);
const MIN_TAP = 44;

const probe = (MIN_TAP) => {
  const vw = document.documentElement.clientWidth;
  const de = document.documentElement;

  const visible = el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    if (r.right <= 0 || r.left >= vw) return false;   // parked off-canvas
    return true;
  };

  /* ---- horizontal overflow ---- */
  const scrollW = Math.max(de.scrollWidth, document.body.scrollWidth);
  const overflowPx = Math.round(scrollW - vw);
  const culprits = [];
  if (overflowPx > 1) {
    for (const el of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      if (cs.position === 'fixed') continue;          // fixed bars don't scroll the page
      const r = el.getBoundingClientRect();
      if (r.width < 1 || r.height < 1) continue;
      const over = Math.round(r.right - vw);
      if (over > 1 && r.left < vw) {                  // starts on-screen, ends past the edge
        culprits.push({
          over,
          tag: el.tagName.toLowerCase(),
          cls: String(el.className || '').trim().split(/\s+/).slice(0, 2).join('.').slice(0, 40),
          w: Math.round(r.width),
          text: (el.textContent || '').trim().slice(0, 40),
        });
      }
    }
    culprits.sort((a, b) => b.over - a.over);
  }

  /* ---- tap targets ---- */
  const small = [];
  for (const el of document.querySelectorAll('a[href], button, input[type=submit], input[type=button], [role=button]')) {
    if (!visible(el)) continue;
    // An anchor sitting inside a run of prose is a text link, not a control.
    if (el.tagName === 'A') {
      const p = el.parentElement;
      if (p && /^(P|LI|SPAN|TD|DD|SMALL|EM|STRONG|BLOCKQUOTE)$/.test(p.tagName)) {
        const own = (el.textContent || '').trim().length;
        const par = (p.textContent || '').trim().length;
        if (par > own + 20) continue;                 // embedded in a sentence
      }
    }
    const r = el.getBoundingClientRect();
    if (r.height < MIN_TAP - 0.5 || r.width < 24) {
      small.push({
        tag: el.tagName.toLowerCase(),
        h: Math.round(r.height), w: Math.round(r.width),
        text: (el.textContent || '').trim().slice(0, 34) || el.getAttribute('aria-label') || '',
      });
    }
  }

  return {
    overflowPx,
    culprits: culprits.slice(0, 4),
    tapTotal: document.querySelectorAll('a[href],button').length,
    tapSmall: small.length,
    tapSample: small.slice(0, 4),
  };
};

(async () => {
  const pages = fs.readFileSync(LIST, 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
  const browser = await chromium.launch({ headless: true });
  const results = [];

  for (const page of pages) {
    const ctx = await browser.newContext({ viewport: { width: WIDTH, height: 850 }, isMobile: false });
    const p = await ctx.newPage();
    try {
      await p.goto(`${BASE}/${page}`, { waitUntil: 'domcontentloaded', timeout: 20000 });
      await p.waitForTimeout(400);
      const r = await p.evaluate(probe, MIN_TAP);
      results.push({ page, ...r });
      if (r.overflowPx > 1) {
        const c = r.culprits[0];
        console.log(`  OVERFLOW ${String(r.overflowPx).padStart(5)}px  ${page}` +
                    (c ? `   <- ${c.tag}${c.cls ? '.' + c.cls : ''} (${c.w}px wide)` : ''));
      }
    } catch (e) {
      results.push({ page, error: String(e).slice(0, 120) });
    }
    await ctx.close();
  }

  fs.writeFileSync(OUT, JSON.stringify(results, null, 1));

  const errored = results.filter(r => r.error);
  if (errored.length) {
    console.error(`\nAUDIT INVALID — ${errored.length}/${results.length} pages failed to load.`);
    console.error(`  first: ${errored[0].page} :: ${errored[0].error}`);
    process.exit(2);
  }

  const over = results.filter(r => r.overflowPx > 1);
  const taps = results.filter(r => r.tapSmall > 0);
  console.log(`\nwidth              : ${WIDTH}px`);
  console.log(`pages scanned      : ${results.length}`);
  console.log(`horizontal overflow: ${over.length}`);
  console.log(`pages w/ small taps: ${taps.length}  (total undersized controls: ${
    results.reduce((n, r) => n + (r.tapSmall || 0), 0)})`);
  console.log(`report             : ${OUT}`);
  await browser.close();
})();
