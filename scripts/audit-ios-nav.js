/* audit-ios-nav.js — check the fixed masthead in WEBKIT at phone width.
 *
 * Why a separate audit: the Chromium pass reported 0 problems on wire.html
 * while a real iPhone had the banner sitting on the headline. Two reasons it
 * missed — both worth keeping in mind:
 *
 *   1. Wrong engine. Chromium and WebKit wrap the brand block differently.
 *   2. Wrong thing measured. The nav BOX is a fixed 70px, so measuring the box
 *      always says "fine". What matters is where the nav's painted CONTENT
 *      ends, which can be past the bar.
 *
 * So this measures ink, not boxes, in WebKit.
 *
 * usage: node audit-ios-nav.js <baseUrl> <pageListFile> [outJson] [width]
 */
'use strict';

const fs = require('fs');
const { webkit } = require('/Users/moop_bot_pro/Scripts/cdp-tmc/node_modules/playwright-core');

const BASE = process.argv[2];
const LIST = process.argv[3];
const OUT = process.argv[4] || '/tmp/ios-nav.json';
const WIDTH = parseInt(process.argv[5] || '390', 10);

const IPHONE_UA =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 ' +
  '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';

const probe = () => {
  const nav = document.querySelector('body > nav');
  if (!nav) return { noNav: true };
  const nb = nav.getBoundingClientRect();

  // Where does the masthead's painted content actually end?
  // NOTE: this is the LAYOUT extent, not the painted extent. `body > nav` sets
  // overflow:hidden, so a child box may report a bottom past the bar while
  // being clipped and never drawn there. A positive `spill` therefore means
  // "would paint over the page if the bar were not clipping" — treat it as a
  // fragility signal and confirm with a screenshot before calling it a defect.
  let ink = nb.top;
  let culprit = '';
  for (const el of nav.querySelectorAll('*')) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.height < 1 || r.width < 1) continue;
    if (r.bottom > ink) {
      ink = r.bottom;
      culprit = (el.className && String(el.className)) || el.tagName;
    }
  }

  // First real content text below the masthead.
  const vw = document.documentElement.clientWidth;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let firstTop = null, firstText = '';
  while (walker.nextNode()) {
    const n = walker.currentNode;
    if (!n.nodeValue || !n.nodeValue.trim()) continue;
    const el = n.parentElement;
    if (!el || nav.contains(el)) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    if (cs.position === 'fixed') continue;
    const range = document.createRange();
    range.selectNodeContents(n);
    const r = range.getBoundingClientRect();
    if (r.height < 1 || r.right <= 0 || r.left >= vw || r.bottom < 0) continue;
    // Visually-hidden skip links park off-canvas at left:-10000 and are not
    // what a reader sees; counting them reported about.html at -768px.
    if (r.right <= 0 || r.left >= vw) continue;
    firstTop = r.top; firstText = n.nodeValue.trim().slice(0, 40);
    break;
  }

  const brand = nav.querySelector('.nav-brand-text') || nav.querySelector('.nav-brand');
  return {
    navBox: Math.round(nb.height),
    navInk: Math.round(ink),
    spill: Math.round(ink - nb.bottom),          // > 0 = masthead paints past its own bar
    culprit: String(culprit).slice(0, 28),
    brandH: brand ? Math.round(brand.getBoundingClientRect().height) : null,
    firstTop: firstTop === null ? null : Math.round(firstTop),
    firstText,
    clearance: firstTop === null ? null : Math.round(firstTop - ink),
  };
};

(async () => {
  const pages = fs.readFileSync(LIST, 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
  const browser = await webkit.launch({ headless: true });
  const results = [];

  for (const page of pages) {
    const ctx = await browser.newContext({
      viewport: { width: WIDTH, height: 800 }, deviceScaleFactor: 2,
      isMobile: true, hasTouch: true, userAgent: IPHONE_UA,
    });
    const p = await ctx.newPage();
    try {
      await p.goto(`${BASE}/${page}`, { waitUntil: 'domcontentloaded', timeout: 25000 });
      await p.waitForTimeout(400);
      await p.evaluate(() => window.scrollTo(0, 0));
      await p.waitForTimeout(120);
      const r = await p.evaluate(probe);
      results.push({ page, ...r });
      if (r.spill > 0) {
        console.log(`  SPILL   ${String(r.spill).padStart(3)}px  ${page}  <- ${r.culprit}`);
      } else if (r.clearance !== null && r.clearance < 8) {
        console.log(`  TIGHT   ${String(r.clearance).padStart(3)}px  ${page}  "${r.firstText}"`);
      }
    } catch (e) {
      results.push({ page, error: String(e).slice(0, 110) });
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

  const withNav = results.filter(r => !r.noNav);
  const spilled = withNav.filter(r => r.spill > 0);
  const tight = withNav.filter(r => r.clearance !== null && r.clearance < 8);
  console.log(`\nengine             : WebKit (Safari) @ ${WIDTH}px`);
  console.log(`pages scanned      : ${results.length}   with a masthead: ${withNav.length}`);
  console.log(`masthead spills    : ${spilled.length}`);
  console.log(`clearance under 8px: ${tight.length}`);
  console.log(`report             : ${OUT}`);
  await browser.close();
})();
