#!/usr/bin/env node
/* enrich-wire-images.js — fill in real article images on the RESOLUTE Wire.
 *
 * The desk sets `image` to the site's own OG art (`image_source: brand_fallback`)
 * whenever it cannot get a picture from the source. On the 2026-08-08 edition
 * that was 6 of 11 items, and wire.html rendered a column of identical
 * placeholders — which is what Adam photographed.
 *
 * Most of those were recoverable. Heritage and USNI both publish an `og:image`,
 * but they answer a plain server-side fetch with 403; only a real browser gets
 * through. So this opens each link in headless Chromium and reads the meta tag
 * the publisher themselves put there for sharing.
 *
 * Honesty rules, because a wrong picture on a news card is worse than none:
 *   - never overwrite an image the desk already resolved from the source
 *   - the URL must return 200 AND the image must actually load as an image
 *   - anything that is not an HTML page (agenda PDFs, DocumentCenter downloads)
 *     is skipped rather than guessed at
 *   - failures leave the item exactly as it was; a card with no picture is fine
 *
 * usage:
 *   node scripts/enrich-wire-images.js --check      report only, writes nothing
 *   node scripts/enrich-wire-images.js              resolve and write back
 *   node scripts/enrich-wire-images.js --file <p>   a specific edition
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { chromium } = require('/Users/moop_bot_pro/Scripts/cdp-tmc/node_modules/playwright-core');

const REPO = path.dirname(__dirname);
const argv = process.argv.slice(2);
const CHECK = argv.includes('--check');
const fileArg = argv.indexOf('--file');
const DATA = fileArg !== -1 ? argv[fileArg + 1] : path.join(REPO, 'data', 'wire-latest.json');

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
           '(KHTML, like Gecko) Chrome/126.0 Safari/537.36';

// The feed's own share art. Present in `image` means "the desk had nothing".
const GENERIC = /\/assets\/og\/og-[a-z0-9-]+\.(jpe?g|png|webp)(\?|$)/i;
// Links that are downloads, not pages — nothing to scrape.
const NOT_A_PAGE = /\.(pdf|docx?|xlsx?|pptx?|zip)(\?|$)|\/DocumentCenter\/View\//i;

function collect(doc) {
  const out = [];
  if (doc.lead) out.push({ rail: 'lead', item: doc.lead });
  for (const [rail, arr] of Object.entries(doc.rails || {})) {
    if (Array.isArray(arr)) arr.forEach(item => out.push({ rail, item }));
  }
  return out;
}

const needsImage = it =>
  !it.image || GENERIC.test(String(it.image));

async function resolveImage(browser, url) {
  const ctx = await browser.newContext({ userAgent: UA });
  const page = await ctx.newPage();
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    if (!resp || resp.status() !== 200) {
      return { ok: false, why: `page HTTP ${resp ? resp.status() : 'none'}` };
    }
    const title = await page.title();
    if (/not found|404|page unavailable/i.test(title)) {
      return { ok: false, why: `soft-404 ("${title.slice(0, 40)}")` };
    }
    const src = await page.evaluate(() => {
      const g = sel => { const e = document.querySelector(sel); return e && e.getAttribute('content'); };
      return g('meta[property="og:image"]') || g('meta[name="og:image"]') ||
             g('meta[property="twitter:image"]') || g('meta[name="twitter:image"]') || null;
    });
    if (!src) return { ok: false, why: 'publisher declares no og:image' };

    const abs = new URL(src, url).toString();
    // The tag existing is not enough — confirm the file is really there and
    // really an image, from the same browser context so referrer checks pass.
    const probe = await page.evaluate(u => new Promise(res => {
      const img = new Image();
      img.onload = () => res({ ok: true, w: img.naturalWidth, h: img.naturalHeight });
      img.onerror = () => res({ ok: false });
      img.src = u;
      setTimeout(() => res({ ok: false, timeout: true }), 12000);
    }), abs);

    if (!probe.ok) return { ok: false, why: 'og:image declared but will not load' };
    if (probe.w < 200 || probe.h < 120) {
      // Sites return a logo or a 1x1 when they have no real art.
      return { ok: false, why: `og:image too small (${probe.w}x${probe.h}) — likely a logo` };
    }
    return { ok: true, url: abs, w: probe.w, h: probe.h };
  } catch (e) {
    return { ok: false, why: String(e.message || e).slice(0, 60) };
  } finally {
    await ctx.close();
  }
}

(async () => {
  const doc = JSON.parse(fs.readFileSync(DATA, 'utf8'));
  const all = collect(doc);
  const targets = all.filter(({ item }) => needsImage(item));

  console.log(`edition : ${doc.cid || '(no cid)'}  ${doc.board_date || ''}`);
  console.log(`items   : ${all.length}   already have a source image: ${all.length - targets.length}`);
  console.log(`to try  : ${targets.length}\n`);

  if (!targets.length) { console.log('Nothing to do.'); return; }

  const browser = await chromium.launch({ headless: true });
  let filled = 0, skipped = 0, failed = 0;

  for (const { rail, item } of targets) {
    const label = `${rail}/${(item.source || '?').slice(0, 22)}`;
    if (!item.url) { skipped++; console.log(`  SKIP  ${label} — no url`); continue; }
    if (NOT_A_PAGE.test(item.url)) {
      skipped++; console.log(`  SKIP  ${label} — download, not a page`); continue;
    }
    const r = await resolveImage(browser, item.url);
    if (r.ok) {
      filled++;
      console.log(`  FILL  ${label} — ${r.w}x${r.h}  ${r.url.slice(0, 58)}`);
      if (!CHECK) { item.image = r.url; item.image_source = 'og-browser'; }
    } else {
      failed++;
      console.log(`  KEEP  ${label} — ${r.why}`);
    }
  }

  await browser.close();

  console.log(`\nfilled ${filled}   skipped ${skipped}   left as-is ${failed}`);
  if (CHECK) { console.log('\n--check: nothing written.'); return; }
  if (filled) {
    fs.writeFileSync(DATA, JSON.stringify(doc, null, 2) + '\n');
    console.log(`wrote ${path.relative(REPO, DATA)}`);
  } else {
    console.log('No changes to write.');
  }
})();
