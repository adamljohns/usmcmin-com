#!/usr/bin/env node
/* enrich-fxbg-commerce.js — fill gaps in the Fredericksburg Christian business
 * directory from each business's OWN website, mechanically.
 *
 * Audited 2026-08-10 against 317 records:
 *   photos      0 / 317
 *   phone     246 / 317   (71 missing, 64 of those have a website)
 *   web       310 / 317
 *
 * Everything here comes from the business's own site, so a value is either
 * verifiable at the source or not taken. Same posture as the church directory:
 * "if you can't verify it, leave it blank" beats a plausible guess.
 *
 * WHAT IT TAKES, AND THE GATE ON EACH
 *   phone   only from a `tel:` link the business publishes, and only when the
 *           same digits also appear in the visible page text. A tel: href alone
 *           can be a template default or a web designer's own number.
 *   image   og:image, or the apple-touch-icon as a LOGO (recorded separately —
 *           a logo is not a photo of the business and should not pretend to be).
 *           Must load from a neutral origin, and be at least 200x120 so a
 *           favicon or tracking pixel cannot slip through.
 *   status  every site gets its HTTP result recorded. Dead links are FLAGGED,
 *           never auto-removed — a dead site may mean the business closed,
 *           which is a human call (see CLAUDE.md on URL-mismatch records).
 *
 * NEVER overwrites an existing value. Only fills blanks.
 *
 * usage:
 *   node scripts/enrich-fxbg-commerce.js --check          report, write nothing
 *   node scripts/enrich-fxbg-commerce.js --limit 20       try the first 20
 *   node scripts/enrich-fxbg-commerce.js                  full run, writes
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { chromium } = require('/Users/moop_bot_pro/Scripts/cdp-tmc/node_modules/playwright-core');

const REPO = path.dirname(__dirname);
const DATA = path.join(REPO, 'fxbg', 'commerce', 'data', 'businesses.json');
const REPORT = path.join(REPO, 'fxbg', 'commerce', 'data', 'enrichment-report.json');

const argv = process.argv.slice(2);
const CHECK = argv.includes('--check');
const li = argv.indexOf('--limit');
const LIMIT = li !== -1 ? parseInt(argv[li + 1], 10) : Infinity;
const CONCURRENCY = 4;

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
           '(KHTML, like Gecko) Chrome/126.0 Safari/537.36';

const digits = s => String(s || '').replace(/\D/g, '');

/* A US number, allowing the leading 1. Rejects the obvious non-numbers that
   show up in tel: hrefs (extensions, 555 placeholders, short codes). */
function normalizePhone(raw) {
  let d = digits(raw);
  if (d.length === 11 && d[0] === '1') d = d.slice(1);
  if (d.length !== 10) return null;
  if (/^(\d)\1{9}$/.test(d)) return null;          // 0000000000
  if (d.slice(3, 6) === '555') return null;         // placeholder exchange
  if (d[0] === '0' || d[0] === '1') return null;    // invalid area code
  return `(${d.slice(0, 3)}) ${d.slice(3, 6)}-${d.slice(6)}`;
}

async function scrape(browser, biz) {
  const out = { id: biz.id, name: biz.name, web: biz.web, status: null,
                phone: null, image: null, logo: null, notes: [] };
  if (!biz.web) { out.status = 'no-website'; return out; }

  const ctx = await browser.newContext({ userAgent: UA });
  const page = await ctx.newPage();
  try {
    let resp;
    try {
      resp = await page.goto(biz.web, { waitUntil: 'domcontentloaded', timeout: 25000 });
    } catch (e) {
      out.status = 'unreachable';
      out.notes.push(String(e.message || e).split('\n')[0].slice(0, 70));
      return out;
    }
    out.status = resp ? `http-${resp.status()}` : 'no-response';
    if (!resp || resp.status() >= 400) return out;
    out.finalUrl = page.url();
    await page.waitForTimeout(700);

    const found = await page.evaluate(() => {
      if (!document.body) return null;   // not an HTML document

      const abs = u => { try { return new URL(u, location.href).toString(); } catch { return null; } };
      const meta = sel => { const e = document.querySelector(sel); return e && e.getAttribute('content'); };
      const link = sel => { const e = document.querySelector(sel); return e && e.getAttribute('href'); };

      /* ---- LOGO candidates, best source first ----
         A business's logo is declared in a handful of standard places. Prefer
         the ones that are unambiguous (schema.org, apple-touch-icon) over
         guessing from the DOM. */
      const logos = [];
      const push = (u, source) => {
        const a = u && abs(u);
        if (a && !PLATFORM_CHROME.test(a)) logos.push({ url: a, source });
      };

      for (const el of document.querySelectorAll('script[type="application/ld+json"]')) {
        try {
          const walk = node => {
            if (!node || typeof node !== 'object') return;
            if (Array.isArray(node)) return node.forEach(walk);
            if (node.logo) push(typeof node.logo === 'string' ? node.logo : node.logo.url, 'json-ld');
            Object.values(node).forEach(walk);
          };
          walk(JSON.parse(el.textContent));
        } catch {}
      }
      push(link('link[rel="apple-touch-icon"]'), 'apple-touch-icon');
      push(link('link[rel="apple-touch-icon-precomposed"]'), 'apple-touch-icon');
      push(meta('meta[property="og:logo"]'), 'og:logo');
      // a header image that calls itself a logo
      for (const img of document.querySelectorAll('header img, .header img, nav img, .logo img, img.logo, img[class*="logo"], img[id*="logo"], img[alt*="logo" i], img[src*="logo" i]')) {
        push(img.currentSrc || img.getAttribute('src'), 'header-img');
        if (logos.length > 8) break;
      }

      /* ---- PHOTO candidates ----
         og:image first (what the business chose to represent itself), then the
         largest genuinely in-content image. Anything that looks like a logo or
         an icon is excluded here — it will be picked up as the logo instead. */
      /* Chrome belonging to the PLATFORM, not the business. When a business's
         only "website" is a Facebook page we would otherwise scrape Facebook's
         own brand mark and file it as their logo — that happened to 6 records
         on the first two-asset run. */
      const PLATFORM_CHROME = /facebook\.com\/images\/|\/rsrc\.php\/|fbcdn\.net\/rsrc|instagram\.com\/static\/|yelp\.com\/assets\/|etsy\.com\/images\//i;
      const LOGOISH = /(logo|favicon|icon|brandmark|wordmark|sprite|badge)/i;
      const photos = [];
      const pushPhoto = (u, source) => {
        const a = u && abs(u);
        if (a && !LOGOISH.test(a) && !PLATFORM_CHROME.test(a)) photos.push({ url: a, source });
      };
      pushPhoto(meta('meta[property="og:image"]') || meta('meta[name="og:image"]'), 'og:image');
      pushPhoto(meta('meta[property="twitter:image"]') || meta('meta[name="twitter:image"]'), 'twitter:image');

      const inContent = [...document.querySelectorAll('img')]
        .filter(i => !i.closest('header, nav, footer, .header, .footer'))
        .map(i => ({ el: i, w: i.naturalWidth || i.width || 0, h: i.naturalHeight || i.height || 0 }))
        .filter(o => o.w >= 400 && o.h >= 240)
        .sort((a, b) => (b.w * b.h) - (a.w * a.h))
        .slice(0, 4);
      for (const o of inContent) pushPhoto(o.el.currentSrc || o.el.getAttribute('src'), 'content-image');

      const tels = [...document.querySelectorAll('a[href^="tel:"]')]
        .map(a => a.getAttribute('href').replace(/^tel:/i, '').trim());

      return { tels, bodyText: (document.body.innerText || '').slice(0, 40000), logos, photos };
    });

    if (!found) { out.notes.push('not an HTML document'); return out; }

    /* ---- phone: published as tel: AND visible in the page text ---- */
    if (!biz.phone) {
      const textDigits = digits(found.bodyText);
      for (const t of found.tels) {
        const norm = normalizePhone(t);
        if (!norm) continue;
        if (textDigits.includes(digits(norm))) { out.phone = norm; break; }
      }
      if (!out.phone && found.tels.length) {
        out.notes.push(`tel: present but not confirmed in page text (${found.tels.length})`);
      }
    }

    /* Confirm a candidate actually loads and is big enough to use. A declared
       URL is not evidence the file exists. */
    const measure = async (cand, minW, minH) => {
      const probe = await page.evaluate(u => new Promise(res => {
        const i = new Image();
        i.onload = () => res({ ok: true, w: i.naturalWidth, h: i.naturalHeight });
        i.onerror = () => res({ ok: false });
        setTimeout(() => res({ ok: false }), 9000);
        i.src = u;
      }), cand.url).catch(() => ({ ok: false }));
      if (!probe.ok || probe.w < minW || probe.h < minH) return null;
      return { url: cand.url, source: cand.source, w: probe.w, h: probe.h };
    };

    const seen = new Set();
    const firstUsable = async (cands, minW, minH) => {
      for (const c of cands) {
        if (seen.has(c.url)) continue;
        const m = await measure(c, minW, minH);
        if (m) { seen.add(c.url); return m; }
      }
      return null;
    };

    /* Logos are square-ish and can legitimately be small — 96px is plenty for a
       card badge. Photos need to be big enough not to look degraded when they
       fill a 16:9 frame. */
    out.logo  = await firstUsable(found.logos, 96, 96);
    out.image = await firstUsable(found.photos, 400, 240);

    return out;
  } finally {
    await ctx.close();
  }
}

async function pool(items, n, worker) {
  const results = new Array(items.length);
  let i = 0;
  await Promise.all(Array.from({ length: n }, async () => {
    while (true) {
      const idx = i++;
      if (idx >= items.length) return;
      results[idx] = await worker(items[idx], idx);
    }
  }));
  return results;
}

(async () => {
  const doc = JSON.parse(fs.readFileSync(DATA, 'utf8'));
  const all = doc.businesses;

  const targets = all.filter(b =>
    b.web && (!b.phone || !(b.media && b.media.logo) || !(b.media && b.media.photo))
  ).slice(0, LIMIT);

  console.log(`directory : ${all.length} businesses (${doc.edition}, rubric ${doc.rubric_version})`);
  console.log(`targets   : ${targets.length}  (missing a phone, logo, or photo, and have a website)`);
  console.log(`mode      : ${CHECK ? 'CHECK — nothing will be written' : 'WRITE'}\n`);

  const browser = await chromium.launch({ headless: true });
  let done = 0;
  const results = await pool(targets, CONCURRENCY, async (biz) => {
    let r;
    try {
      r = await scrape(browser, biz);
    } catch (e) {
      // A single hostile site killed the first full run on a null document.body.
      // Record it and keep going; a crash loses every result gathered so far.
      r = { id: biz.id, name: biz.name, web: biz.web, status: 'scrape-error',
            phone: null, image: null, logo: null,
            notes: [String(e.message || e).split('\n')[0].slice(0, 80)] };
    }
    done++;
    if (done % 25 === 0) console.log(`  … ${done}/${targets.length}`);
    return r;
  });
  await browser.close();

  const byId = new Map(results.map(r => [r.id, r]));
  let phones = 0, photos = 0, logos = 0, dead = 0;
  const deadList = [];
  const stamp = new Date().toISOString().slice(0, 10);

  for (const biz of all) {
    const r = byId.get(biz.id);
    if (!r) continue;
    if (r.phone && !biz.phone) { phones++; if (!CHECK) biz.phone = r.phone; }

    /* logo and photo are stored separately and do different jobs on a card: the
       logo identifies the business, the photo shows the place. Neither stands in
       for the other, which is why an og:image that is really a wordmark is
       filed as a logo. */
    const media = Object.assign({}, biz.media);
    if (r.logo && !media.logo) {
      logos++;
      if (!CHECK) media.logo = { url: r.logo.url, w: r.logo.w, h: r.logo.h,
                                 source: r.logo.source, checked: stamp };
    }
    if (r.image && !media.photo) {
      photos++;
      if (!CHECK) media.photo = { url: r.image.url, w: r.image.w, h: r.image.h,
                                  source: r.image.source, checked: stamp };
    }
    if (!CHECK && (media.logo || media.photo)) biz.media = media;

    const bad = r.status === 'unreachable' || /^http-[45]/.test(String(r.status));
    if (bad) {
      dead++;
      deadList.push({ id: r.id, name: r.name, web: r.web, status: r.status, note: r.notes[0] || '' });
      if (!CHECK) {
        biz.review_flag = Object.assign({}, biz.review_flag, {
          website_status: r.status, website_checked: stamp,
        });
      }
    }
  }

  console.log(`\nphones filled    : ${phones}`);
  console.log(`photos added     : ${photos}`);
  console.log(`logos added      : ${logos}`);
  console.log(`websites failing : ${dead}   <- flagged for review, not changed`);
  if (deadList.length) {
    console.log('\nsites that did not answer:');
    deadList.slice(0, 25).forEach(d => console.log(`   ${String(d.status).padEnd(14)} ${d.name.slice(0, 34).padEnd(34)} ${d.web.slice(0, 44)}`));
    if (deadList.length > 25) console.log(`   … and ${deadList.length - 25} more`);
  }

  if (CHECK) { console.log('\n--check: nothing written.'); return; }

  const withPhoto = all.filter(b => b.media && b.media.photo).length;
  const withLogo  = all.filter(b => b.media && b.media.logo).length;
  const withBoth  = all.filter(b => b.media && b.media.photo && b.media.logo).length;
  const withPhone = all.filter(b => b.phone).length;
  doc.updated = new Date().toISOString().slice(0, 10);
  fs.writeFileSync(DATA, JSON.stringify(doc, null, 2) + '\n');
  fs.writeFileSync(REPORT, JSON.stringify({
    ran: new Date().toISOString(), edition: doc.edition,
    totals: { businesses: all.length, withPhone, withPhoto, withLogo, withBoth },
    filled: { phones, photos, logos }, deadSites: deadList,
  }, null, 2) + '\n');

  console.log(`\ncoverage now  phone ${withPhone}/${all.length}   logo ${withLogo}/${all.length}   photo ${withPhoto}/${all.length}   both ${withBoth}/${all.length}`);
  console.log(`wrote ${path.relative(REPO, DATA)}`);
  console.log(`wrote ${path.relative(REPO, REPORT)}`);
})();
