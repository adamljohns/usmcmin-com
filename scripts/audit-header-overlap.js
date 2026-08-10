/* audit-header-overlap.js — find pages where a fixed/sticky banner sits on top
 * of the first line of content.
 *
 * This is measured, not eyeballed. For every page, at each viewport width, we:
 *   1. find the topmost element whose computed position is fixed or sticky and
 *      which is actually pinned to the top of the viewport,
 *   2. walk the real text nodes in document order and find the first one that is
 *      visible and inside the page's main content,
 *   3. report how many pixels of that text sit above the banner's bottom edge.
 *
 * A positive `overlap` means a reader literally cannot see that text at rest.
 *
 * Also checks anchor landing: with `#hash` navigation a fixed header needs
 * `scroll-margin-top` or the target heading lands underneath it.
 *
 * usage: node audit-header-overlap.js <baseUrl> <pageListFile> [outJson]
 */
'use strict';

const fs = require('fs');
const { chromium } = require('/Users/moop_bot_pro/Scripts/cdp-tmc/node_modules/playwright-core');

const BASE = process.argv[2] || 'http://localhost:8955';
const LIST = process.argv[3];
const OUT = process.argv[4] || '/tmp/header-overlap.json';
const WIDTHS = [390, 768, 1280];

const probe = () => {
  const vw = window.innerWidth;

  // --- the banner: pinned to the top, actually painted, actually wide ---
  let banner = null;
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.height < 8 || r.width < vw * 0.5) continue;   // not a full-width bar
    if (r.top > 4) continue;                            // not pinned to the top
    // A full-viewport overlay is a modal, not a masthead. scorecard.html's
    // #welcomeModal is 900px tall and covers everything by design; counting it
    // reported three healthy pages as 815px broken.
    if (r.height > window.innerHeight * 0.4) continue;
    if (!banner || r.bottom > banner.rect.bottom) {
      banner = { rect: { top: r.top, bottom: r.bottom, height: r.height },
                 tag: el.tagName.toLowerCase(),
                 cls: (el.className || '').toString().slice(0, 60),
                 position: cs.position };
    }
  }

  // --- first visible content text, skipping anything inside the banner ---
  const bannerEls = new Set();
  if (banner) {
    for (const el of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(el);
      if ((cs.position === 'fixed' || cs.position === 'sticky')) {
        const r = el.getBoundingClientRect();
        if (r.top <= 4 && r.width >= vw * 0.5 && r.height >= 8) {
          bannerEls.add(el);
          el.querySelectorAll('*').forEach(c => bannerEls.add(c));
        }
      }
    }
  }

  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let first = null;
  while (walker.nextNode()) {
    const node = walker.currentNode;
    if (!node.nodeValue || !node.nodeValue.trim()) continue;
    const el = node.parentElement;
    if (!el || bannerEls.has(el)) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    if (cs.position === 'fixed' || cs.position === 'sticky') continue;
    const range = document.createRange();
    range.selectNodeContents(node);
    const r = range.getBoundingClientRect();
    if (r.height < 1 || r.width < 1) continue;
    if (r.bottom < 0) continue;                          // scrolled off, not our case at rest
    // Skip links and other visually-hidden text park themselves off-canvas
    // (left:-10000, or a 1px clip box). They are not what a reader sees, and
    // counting them reported 32 healthy pages as broken on the first run.
    if (r.right <= 0 || r.left >= vw) continue;
    const clipped = cs.clip !== 'auto' || (cs.clipPath !== 'none' && /inset\(\s*50%/.test(cs.clipPath));
    if (clipped && r.width <= 2 && r.height <= 2) continue;
    first = { top: r.top, bottom: r.bottom,
              text: node.nodeValue.trim().slice(0, 60),
              tag: el.tagName.toLowerCase() };
    break;
  }

  // --- anchor landing: do in-page targets clear the banner? ---
  let anchorRisk = 0, anchorTotal = 0;
  const ids = new Set();
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    const id = a.getAttribute('href').slice(1);
    if (id) ids.add(id);
  });
  for (const id of ids) {
    const t = document.getElementById(id);
    if (!t) continue;
    anchorTotal++;
    // Either mechanism is sufficient: scroll-margin-top on the target, or
    // scroll-padding-top on the scrollport. Checking only the former reported
    // 23 at-risk pages that a real #anchor navigation showed were fine.
    const smt = parseFloat(getComputedStyle(t).scrollMarginTop) || 0;
    const spt = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
    if (banner && Math.max(smt, spt) < banner.rect.bottom - 2) anchorRisk++;
  }

  const scrollPad = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;

  return {
    banner,
    first,
    overlap: banner && first ? Math.round((banner.rect.bottom - first.top) * 10) / 10 : null,
    anchorTotal, anchorRisk, scrollPad,
    docHeight: document.documentElement.scrollHeight,
  };
};

(async () => {
  const pages = fs.readFileSync(LIST, 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
  const browser = await chromium.launch({ headless: true });
  const results = [];

  for (const page of pages) {
    const row = { page, widths: {} };
    for (const w of WIDTHS) {
      const ctx = await browser.newContext({ viewport: { width: w, height: 900 } });
      const p = await ctx.newPage();
      const errs = [];
      p.on('pageerror', e => errs.push(String(e).slice(0, 120)));
      try {
        await p.goto(`${BASE}/${page}`, { waitUntil: 'domcontentloaded', timeout: 20000 });
        await p.waitForTimeout(350);
        // Measure the page at rest. Some pages focus a field or scroll a widget
        // into view on load; content that has legitimately scrolled up under the
        // banner is not the defect we are hunting, and house-rules.html was
        // reported at 62px purely because it had scrolled ~1950px.
        await p.evaluate(() => window.scrollTo(0, 0));
        await p.waitForTimeout(120);
        const r = await p.evaluate(probe);
        r.jsErrors = errs;
        row.widths[w] = r;
      } catch (e) {
        row.widths[w] = { error: String(e).slice(0, 120) };
      }
      await ctx.close();
    }
    results.push(row);
    const worst = Math.max(...WIDTHS.map(w => (row.widths[w] && row.widths[w].overlap) || -999));
    if (worst > 0) {
      const at = WIDTHS.filter(w => (row.widths[w] || {}).overlap > 0).join(',');
      console.log(`  OVERLAP ${String(Math.round(worst)).padStart(4)}px  ${page}  @${at}`);
    }
  }

  fs.writeFileSync(OUT, JSON.stringify(results, null, 1));

  const bad = results.filter(r => WIDTHS.some(w => (r.widths[w] || {}).overlap > 0));
  const anchors = results.filter(r => WIDTHS.some(w => (r.widths[w] || {}).anchorRisk > 0));

  /* A page that failed to load contributes zero findings, so a dead server
     reports a perfect score. That happened on the first run of this audit —
     the http.server had not started and all 74 pages came back
     ERR_CONNECTION_REFUSED under a headline of "0 problems". Refuse to report
     a clean bill of health that was really a total failure. */
  const errored = results.filter(r => WIDTHS.some(w => (r.widths[w] || {}).error));
  if (errored.length) {
    console.error(`\nAUDIT INVALID — ${errored.length}/${results.length} pages failed to load.`);
    console.error(`  first: ${errored[0].page} :: ${Object.values(errored[0].widths)[0].error}`);
    process.exit(2);
  }

  console.log(`\npages scanned : ${results.length}`);
  console.log(`text under banner : ${bad.length}`);
  console.log(`anchor-landing risk : ${anchors.length}`);
  console.log(`report : ${OUT}`);
  await browser.close();
})();
