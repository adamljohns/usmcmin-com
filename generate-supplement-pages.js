#!/usr/bin/env node
/**
 * generate-supplement-pages.js
 * Builds fitness/supplements/index.html + individual supplement pages
 * from data/supplements.json
 *
 * Usage: node generate-supplement-pages.js
 */

const fs   = require('fs');
const path = require('path');

const data   = JSON.parse(fs.readFileSync(path.join(__dirname,'data/supplements.json'),'utf8'));
const outDir = path.join(__dirname,'fitness','supplements');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

const AMAZON_TAG = 'usmcministrie-20'; // Amazon Associates tracking ID — live 2026-06-10

function escHtml(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;');
}

function amazonUrl(asin) {
  if (!asin) return null;
  const base = `https://www.amazon.com/dp/${asin}`;
  return AMAZON_TAG ? `${base}?tag=${AMAZON_TAG}` : base;
}

// Tagged Amazon SEARCH link for a specific product. Robust: never 404s, always
// lands the reader on the exact product, and the tag earns commission on any
// qualifying purchase in the session. Preferred over /dp/ASIN links (ASINs rot).
function amazonSearchUrl(query) {
  const u = `https://www.amazon.com/s?k=${encodeURIComponent(query)}`;
  return AMAZON_TAG ? `${u}&tag=${AMAZON_TAG}` : u;
}

function tierColor(tier) {
  const map = { core:'var(--gold)', t_stack:'#5a9bd4', workout:'#6abf72', cycling:'var(--gray)', avoid:'#d96666' };
  return map[tier] || 'var(--gold)';
}

function tierBg(tier) {
  const map = { core:'rgba(212,175,55,0.12)', t_stack:'rgba(90,155,212,0.12)', workout:'rgba(106,191,114,0.12)', cycling:'rgba(160,160,160,0.10)', avoid:'rgba(217,102,102,0.12)' };
  return map[tier] || 'rgba(212,175,55,0.12)';
}

function evidenceBadge(e) {
  const map = { A:'#6abf72', B:'var(--gold)', C:'#d4a017', D:'#d96666', 'N/A':'#666' };
  const labels = { A:'Grade A — Strong', B:'Grade B — Good', C:'Grade C — Weak', D:'Grade D — Poor', 'N/A':'N/A' };
  const color = map[e] || '#888';
  return `<span style="background:${color};color:#000;font-size:0.7rem;font-weight:700;padding:2px 7px;border-radius:10px;letter-spacing:0.04em;">${labels[e] || e}</span>`;
}

// Exact site nav, paths adjusted for the fitness/supplements/ depth (../../ to root, ../ to fitness hub)
const NAV = `
<nav>
  <a href="/" class="nav-brand" style="text-decoration:none">
    <img src="../../assets/img/logo.png" alt="U.S.M.C. Ministries" style="object-fit:contain">
    <div class="nav-brand-text">
      <div class="name">U.S.M.C. Ministries</div>
      <div class="tag">Warriors Equipped</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="../../mission.html">Mission</a></li>
    <li><a href="../../shop.html">Shop</a></li>
    <li><a href="../../books.html">Books</a></li>
    <li><a href="../../coaching.html">Coaching</a></li>
    <li><a href="../" class="active">Fitness</a></li>
    <li><a href="../../finance/">Finance</a></li>
    <li><a href="../../about.html">About</a></li>
    <li><a href="https://usmcmin.org" target="_blank">Ministry Site</a></li>
  </ul>
  <a href="../../coaching.html" class="btn nav-cta">Book a Session</a>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme" title="Switch light/dark mode">&#9728;&#65039;</button>
  <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>`;

// Native site footer, paths adjusted for fitness/supplements/ depth
const FOOTER = `
<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="name">U.S.M.C. Ministries</div>
        <div class="tag">Warriors Equipped. Kingdom Advancing.</div>
        <p>Helping men become better husbands, fathers, and citizens as they follow Jesus. Based in Fredericksburg, VA.</p>
      </div>
      <div class="footer-col">
        <h4>Fitness</h4>
        <ul>
          <li><a href="../">Fitness Overview</a></li>
          <li><a href="./">Supplement Stack</a></li>
          <li><a href="../fitness-intake.html">Coaching Intake</a></li>
          <li><a href="../trainer.html">About the Trainer</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Resources</h4>
        <ul>
          <li><a href="../../shop.html">Ministry Shop</a></li>
          <li><a href="../../books.html">Books &amp; Devos</a></li>
          <li><a href="../../coaching.html">Coaching</a></li>
          <li><a href="../../finance/">C5iSR Finance</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Ministry</h4>
        <ul>
          <li><a href="../../about.html">About Adam</a></li>
          <li><a href="https://usmcmin.org" target="_blank">usmcmin.org</a></li>
          <li><a href="mailto:usmcministries2022@gmail.com">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div style="color:var(--gray);font-size:0.8rem">© 2026 U.S.M.C. Ministries. All rights reserved. &nbsp;|&nbsp; MOOP's Supplement Stack v${escHtml(data.meta.version)} · updated ${escHtml(data.meta.updated)}</div>
    </div>
  </div>
</footer>`;

// Theme toggle + mobile nav + analytics — matches the rest of the site
const CHROME_SCRIPTS = `
<script>
(function(){var t=document.querySelector('.nav-toggle'),l=document.querySelector('.nav-links');if(t&&l){t.addEventListener('click',function(){l.classList.toggle('open');});}})();
</script>
<script>
(function(){var tg=document.getElementById('themeToggle');if(!tg)return;var s=localStorage.getItem('usmc-theme');if(s!=='light'){document.documentElement.setAttribute('data-theme','dark');tg.textContent='\\u2600\\uFE0F';}tg.addEventListener('click',function(){var d=document.documentElement.getAttribute('data-theme')==='dark';if(d){document.documentElement.removeAttribute('data-theme');localStorage.setItem('usmc-theme','light');tg.textContent='\\uD83C\\uDF19';}else{document.documentElement.setAttribute('data-theme','dark');localStorage.setItem('usmc-theme','dark');tg.textContent='\\u2600\\uFE0F';}});})();
</script>
<script data-goatcounter="https://usmcmin.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>`;

const supplementNav = () => NAV;

/* ────────────────────────────────────────────────────────────────────────────
   INDEX PAGE
   ──────────────────────────────────────────────────────────────────────────── */

const active = data.supplements.filter(s => s.status === 'active');
const avoid  = data.supplements.filter(s => s.status === 'avoid');

// Daily stack order for the timeline hero
const dailyStack = [
  { time:'AM Core', color:'var(--gold)', items: active.filter(s => s.tier === 'core' && s.tags && s.tags.includes('morning')) },
  { time:'Workout Days (Tue/Fri)', color:'#6abf72', items: active.filter(s => s.tier === 'workout') },
  { time:'T-Stack (Mon/Tue/Thu/Fri/Sat)', color:'#5a9bd4', items: active.filter(s => s.tier === 't_stack') },
  { time:'PM', color:'#b07dd4', items: active.filter(s => s.tags && s.tags.includes('evening')) },
  { time:'Cycling / Rotating', color:'#888', items: active.filter(s => s.tier === 'cycling') },
];

function supCard(s, relPath='') {
  const tc = tierColor(s.tier);
  const tb = tierBg(s.tier);
  const tierLabel = (data.tiers[s.tier] || {}).label || s.tier;
  const hasMela = s.brands && s.brands.some(b => b.type === 'melaleuca');
  const hasAmz  = s.amazon_asin;
  return `
<a href="${relPath}${escHtml(s.id)}.html" class="sup-card" data-tier="${s.tier}" data-goals="${(s.goals||[]).join(' ')}" style="text-decoration:none;display:block;">
  <div style="border-left:3px solid ${tc};background:${tb};border-radius:6px;padding:14px 16px;margin-bottom:10px;transition:opacity .15s;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;">
      <span style="color:${tc};font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">${escHtml(tierLabel)}</span>
      ${evidenceBadge(s.evidence)}
    </div>
    <div style="color:#f0f0f0;font-weight:700;font-size:0.97rem;margin-bottom:5px;">${escHtml(s.name)}</div>
    <div style="color:var(--gray);font-size:0.82rem;line-height:1.5;margin-bottom:8px;">${escHtml((s.why_i_take_it||s.why_i_avoid_it||'').slice(0,120))}${(s.why_i_take_it||s.why_i_avoid_it||'').length > 120 ? '…' : ''}</div>
    <div style="display:flex;gap:6px;flex-wrap:wrap;">
      ${hasMela ? `<span style="background:rgba(0,140,120,0.18);color:#4ecdc4;font-size:0.68rem;font-weight:600;padding:2px 7px;border-radius:10px;">Melaleuca</span>` : ''}
      ${hasAmz  ? `<span style="background:rgba(255,153,0,0.15);color:#ffa500;font-size:0.68rem;font-weight:600;padding:2px 7px;border-radius:10px;">Amazon</span>` : ''}
      ${(s.tags||[]).slice(0,3).map(t=>`<span style="background:rgba(255,255,255,0.05);color:#888;font-size:0.65rem;padding:2px 6px;border-radius:8px;">${escHtml(t)}</span>`).join('')}
    </div>
  </div>
</a>`;
}

const timelineHtml = dailyStack.filter(g=>g.items.length).map(g=>`
<div style="margin-bottom:28px;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
    <div style="width:12px;height:12px;border-radius:50%;background:${g.color};flex-shrink:0;"></div>
    <span style="color:${g.color};font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;">${escHtml(g.time)}</span>
  </div>
  <div style="padding-left:22px;border-left:1px solid rgba(255,255,255,0.07);">
    ${g.items.map(s=>`
    <a href="${escHtml(s.id)}.html" style="display:flex;align-items:center;gap:10px;padding:8px 0;text-decoration:none;border-bottom:1px solid rgba(255,255,255,0.04);">
      <span style="color:#f0f0f0;font-size:0.9rem;font-weight:600;flex:1;">${escHtml(s.name)}</span>
      <span style="color:var(--gray);font-size:0.78rem;">${escHtml(s.dose ? s.dose.split('.')[0].slice(0,40) : '')}</span>
    </a>`).join('')}
  </div>
</div>`).join('');

const indexHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://usmcmin.com/fitness/supplements/">
  <title>MOOP's Supplement Stack — What I Actually Take | U.S.M.C. Ministries Fitness</title>
  <meta name="description" content="The supplement protocol I use as a 47-year-old Marine veteran, NASM-certified trainer, and Melaleuca wellness advocate — what I take, why, and what I stopped wasting money on.">
  <meta property="og:title" content="MOOP's Supplement Stack — Real Protocols from a Marine Veteran Trainer">
  <meta property="og:description" content="Not a generic supplement guide. This is the stack I actually use — seeded from years of NASM education, real lab work, and trial and error.">
  <meta property="og:url" content="https://usmcmin.com/fitness/supplements/">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../../assets/css/main.min.css">
  <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="../../assets/icons/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/icons/apple-touch-icon.png">
  <style>
    .sup-hero{text-align:center;padding:80px 1.25rem 48px;border-bottom:1px solid var(--border);background:radial-gradient(ellipse at center top,rgba(212,175,55,0.12) 0%,transparent 65%);}
    .sup-hero .eyebrow{display:inline-block;font-size:0.72rem;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold);padding:0.3rem 0.9rem;border:1px solid rgba(212,175,55,0.35);border-radius:20px;margin-bottom:20px;}
    .sup-hero h1{font-size:clamp(1.6rem,5vw,2.8rem);font-weight:700;line-height:1.15;margin:0 0 14px;}
    .sup-hero p{color:var(--gray);font-size:0.95rem;max-width:560px;margin:0 auto 24px;line-height:1.7;}
    .filter-bar{display:flex;gap:8px;flex-wrap:wrap;padding:16px 20px;border-bottom:1px solid var(--border);background:var(--bg-card,#111);position:sticky;top:56px;z-index:9;}
    .filter-btn{background:var(--bg,#0a0a0a);border:1px solid var(--border);color:var(--gray);font-size:0.78rem;font-weight:600;padding:5px 13px;border-radius:20px;cursor:pointer;transition:all .15s;}
    .filter-btn.active,.filter-btn:hover{border-color:var(--gold);color:var(--gold);}
    .sup-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:4px;padding:20px;}
    .section-divider{padding:20px 20px 8px;border-top:1px solid var(--border);margin-top:12px;}
    .section-divider h2{font-size:1rem;font-weight:700;color:var(--gold);margin:0;}
    .section-divider p{color:var(--gray);font-size:0.82rem;margin:4px 0 0;}
    .disclaimer-box{background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:8px;padding:16px 20px;margin:24px 20px;font-size:0.78rem;color:#888;line-height:1.6;}
    .disclaimer-box strong{color:#aaa;}
    .stack-timeline{background:var(--bg-card,#111);border:1px solid var(--border);border-radius:10px;padding:20px 20px 8px;margin:16px 20px;}
    .stack-timeline h2{color:var(--gold);font-size:0.9rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin:0 0 16px;}
    .moop-quote{background:rgba(212,175,55,0.08);border-left:3px solid var(--gold);border-radius:0 8px 8px 0;padding:14px 18px;margin:0 20px 16px;font-style:italic;color:#ccc;font-size:0.92rem;line-height:1.65;}
    .stat-row{display:flex;gap:12px;flex-wrap:wrap;padding:0 20px 20px;}
    .stat-box{flex:1;min-width:100px;background:var(--bg-card,#111);border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center;}
    .stat-box .val{color:var(--gold);font-size:1.5rem;font-weight:700;}
    .stat-box .lbl{color:var(--gray);font-size:0.72rem;margin-top:4px;}
  </style>
</head>
<body>
${supplementNav('index')}

<main>
  <div class="sup-hero">
    <span class="eyebrow">MOOP's Personal Protocol</span>
    <h1>What I Actually Take —<br>And What I Stopped Wasting Money On</h1>
    <p>Not a generic supplement guide written by a copywriter. This is the stack I use as a 47-year-old Marine veteran, NASM-certified nutrition coach, and Melaleuca wellness advocate — grounded in real lab work and NASM education.</p>
  </div>

  <!-- Stats bar -->
  <div class="stat-row" style="padding-top:20px;">
    <div class="stat-box"><div class="val">${active.length}</div><div class="lbl">Active supplements</div></div>
    <div class="stat-box"><div class="val">${active.filter(s=>s.tier==='core').length}</div><div class="lbl">Daily non-negotiables</div></div>
    <div class="stat-box"><div class="val">${avoid.length}</div><div class="lbl">Dropped / avoid</div></div>
    <div class="stat-box"><div class="val">47</div><div class="lbl">Age (DOB 1978)</div></div>
  </div>

  <!-- MOOP's quote -->
  <div class="moop-quote">
    "Your body is a temple — 1 Corinthians 6:19. Stewardship means being intentional about what you put in it. Not obsessive, not vain. Intentional. This stack took years of NASM coursework, bad purchases, and real blood work to develop. I'm sharing it so you don't have to start from zero."
    <div style="margin-top:8px;font-style:normal;font-size:0.78rem;color:var(--gold);">— Adam "MOOP" Johns, NASM CPT/CNC/WLS/PES</div>
  </div>

  <!-- Daily Stack Timeline -->
  <div class="stack-timeline">
    <h2>📋 My Daily Stack At a Glance</h2>
    ${timelineHtml}
  </div>

  <!-- Filter bar -->
  <div class="filter-bar">
    <button class="filter-btn active" onclick="filterSups('all',this)">All Active</button>
    <button class="filter-btn" onclick="filterSups('core',this)">Core Daily</button>
    <button class="filter-btn" onclick="filterSups('t_stack',this)">T-Stack</button>
    <button class="filter-btn" onclick="filterSups('workout',this)">Workout Days</button>
    <button class="filter-btn" onclick="filterSups('cycling',this)">Cycling</button>
    <button class="filter-btn" onclick="filterSups('avoid',this)">Don't Bother</button>
  </div>

  <!-- Active supplements -->
  <div id="active-section">
    <div class="section-divider">
      <h2>Active Stack</h2>
      <p>${active.length} supplements currently in rotation</p>
    </div>
    <div class="sup-grid" id="sup-grid">
      ${active.map(s=>supCard(s)).join('')}
    </div>
  </div>

  <!-- Avoid section -->
  <div id="avoid-section">
    <div class="section-divider" style="border-top-color:#d96666;margin-top:24px;">
      <h2 style="color:#d96666;">🚫 Don't Waste Your Money</h2>
      <p>${avoid.length} things I tried, researched thoroughly, and cut. Honesty is part of the protocol.</p>
    </div>
    <div class="sup-grid">
      ${avoid.map(s=>supCard(s)).join('')}
    </div>
  </div>

  <!-- Disclaimer -->
  <div class="disclaimer-box">
    <strong>Disclaimer:</strong> ${escHtml(data.meta.disclaimer)}<br><br>
    <strong>Affiliate Disclosure:</strong> ${escHtml(data.meta.affiliate_disclosure)}<br><br>
    <strong>About these recommendations:</strong> Adam Johns is a NASM Certified Nutrition Coach (CNC) and Personal Trainer (CPT). These are his personal supplement choices documented for educational purposes. Individual needs vary significantly — consult a healthcare provider before beginning any supplement regimen.
  </div>
</main>

${FOOTER}

<script>
function filterSups(tier, btn) {
  document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  const cards = document.querySelectorAll('#sup-grid .sup-card');
  const avoidSection = document.getElementById('avoid-section');
  if (tier === 'all') {
    cards.forEach(c=>c.style.display='');
    avoidSection.style.display = '';
    return;
  }
  if (tier === 'avoid') {
    cards.forEach(c=>c.style.display='none');
    avoidSection.style.display = '';
    return;
  }
  avoidSection.style.display = 'none';
  cards.forEach(c=>{
    c.style.display = c.dataset.tier === tier ? '' : 'none';
  });
}
</script>
${CHROME_SCRIPTS}
</body>
</html>`;

fs.writeFileSync(path.join(outDir,'index.html'), indexHtml, 'utf8');
console.log('✅ fitness/supplements/index.html');

/* ────────────────────────────────────────────────────────────────────────────
   PER-SUPPLEMENT DETAIL PAGES
   ──────────────────────────────────────────────────────────────────────────── */

for (const s of data.supplements) {
  const tc = tierColor(s.tier);
  const tb = tierBg(s.tier);
  const tierLabel = (data.tiers[s.tier] || {}).label || s.tier;
  const tierDesc  = (data.tiers[s.tier] || {}).description || '';
  const isAvoid   = s.status === 'avoid';
  const amzUrl    = amazonUrl(s.amazon_asin);

  const brandsHtml = (s.brands||[]).map(b => {
    let link = '';
    let icon = '';
    if (b.type === 'melaleuca' && s.melaleuca_link) {
      link = s.melaleuca_link;
      icon = `<span style="background:rgba(0,140,120,0.18);color:#4ecdc4;font-size:0.68rem;font-weight:600;padding:2px 6px;border-radius:8px;">Melaleuca</span>`;
    } else if (b.type === 'amazon') {
      link = amazonSearchUrl(b.search || b.name);
      icon = `<span style="background:rgba(255,153,0,0.15);color:#ffa500;font-size:0.68rem;font-weight:600;padding:2px 6px;border-radius:8px;">Amazon</span>`;
    }
    return `
<div style="background:var(--bg,#0a0a0a);border:1px solid var(--border);border-radius:8px;padding:14px 16px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;">
  <div>
    <div style="color:#f0f0f0;font-weight:600;font-size:0.9rem;">${escHtml(b.name)}</div>
    <div style="color:var(--gray);font-size:0.8rem;margin-top:3px;">${escHtml(b.note||'')}</div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;">
    ${icon}
    ${link ? `<a href="${escHtml(link)}" target="_blank" rel="noopener sponsored" style="color:var(--gold);font-size:0.82rem;font-weight:600;text-decoration:none;border:1px solid rgba(212,175,55,0.4);padding:4px 10px;border-radius:6px;">Shop →</a>` : ''}
  </div>
</div>`;
  }).join('');

  const populationLabels = { adult:'Adults', '50plus':'50+ / Veteran', youth:'Youth / Young Adult' };
  const goalLabels = {
    testosterone:'Testosterone', sleep:'Sleep & Recovery', strength:'Strength', lean_mass:'Lean Mass',
    fat_loss:'Fat Loss', joints:'Joint Health', heart_health:'Heart Health', cognition:'Cognitive',
    gut_health:'Gut Health', immunity:'Immunity', hormones:'Hormones', stress:'Stress Management',
    general_wellness:'General Wellness', performance:'Performance', blood_flow:'Blood Flow',
    inflammation:'Anti-Inflammatory', anti_aging:'Anti-Aging', bone_health:'Bone Health',
    libido:'Libido', energy:'Energy', focus:'Focus', memory:'Memory', mood:'Mood',
    micronutrients:'Micronutrients', endurance:'Endurance', absorption:'Absorption', alkalinity:'Alkalinity'
  };

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://usmcmin.com/fitness/supplements/${escHtml(s.id)}.html">
  <title>${escHtml(s.name)} — MOOP's Supplement Stack | U.S.M.C. Ministries</title>
  <meta name="description" content="${escHtml((s.why_i_take_it||s.why_i_avoid_it||'').slice(0,155))}">
  <meta property="og:title" content="${escHtml(s.name)} — MOOP's Supplement Protocol">
  <meta property="og:url" content="https://usmcmin.com/fitness/supplements/${escHtml(s.id)}.html">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../../assets/css/main.min.css">
  <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="../../assets/icons/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/icons/apple-touch-icon.png">
  <style>
    .back-bar{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-bottom:1px solid var(--border);background:var(--bg-card,#111);}
    .back-bar a{color:var(--gold);text-decoration:none;font-size:0.85rem;font-weight:600;}
    .sup-hero{padding:36px 20px 28px;border-bottom:1px solid var(--border);background:${tb};}
    .sup-tier-badge{display:inline-block;background:${tc};color:#000;font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:3px 10px;border-radius:12px;margin-bottom:12px;}
    .sup-name{font-size:clamp(1.3rem,5vw,2rem);font-weight:700;line-height:1.2;margin:0 0 10px;}
    .moop-take{background:rgba(212,175,55,0.08);border-left:3px solid ${tc};border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;font-style:italic;color:#ccc;font-size:0.93rem;line-height:1.7;}
    .moop-take .moop-label{font-style:normal;color:${tc};font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;}
    .detail-card{background:var(--bg-card,#111);border:1px solid var(--border);border-radius:8px;padding:16px 18px;margin-bottom:10px;}
    .detail-card h3{color:var(--gold);font-size:0.82rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin:0 0 8px;}
    .detail-card p{color:#d0d0d0;font-size:0.88rem;line-height:1.7;margin:0;}
    .protocol-box{background:var(--bg,#0a0a0a);border:2px solid ${tc};border-radius:10px;padding:18px 20px;margin:16px 0;}
    .protocol-box h3{color:${tc};font-size:0.8rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;margin:0 0 8px;}
    .protocol-row{display:flex;justify-content:space-between;align-items:flex-start;padding:7px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:0.85rem;}
    .protocol-row:last-child{border-bottom:none;}
    .protocol-label{color:#888;min-width:90px;font-size:0.78rem;}
    .protocol-val{color:#e8e8e8;flex:1;text-align:right;line-height:1.5;}
    .advisor-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0;}
    @media(max-width:480px){.advisor-grid{grid-template-columns:1fr;}}
    .advisor-card{background:var(--bg,#0a0a0a);border:1px solid var(--border);border-radius:8px;padding:14px;}
    .advisor-name{font-size:0.72rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;}
    .advisor-text{font-size:0.84rem;font-style:italic;color:#ccc;line-height:1.6;}
    .avoid-warning{background:rgba(217,102,102,0.12);border:1px solid rgba(217,102,102,0.4);border-radius:8px;padding:16px 18px;margin:14px 0;}
    .avoid-warning h3{color:#d96666;font-size:0.82rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin:0 0 6px;}
    .tag-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px;}
    .tag{background:rgba(255,255,255,0.05);color:#888;font-size:0.68rem;padding:2px 8px;border-radius:8px;}
    .disclaimer-mini{font-size:0.73rem;color:#555;line-height:1.6;padding:14px 18px;border-top:1px solid var(--border);margin-top:20px;}
    .pop-badge{display:inline-block;background:rgba(255,255,255,0.06);color:#999;font-size:0.7rem;padding:2px 8px;border-radius:10px;margin:0 3px 4px 0;}
    .goal-badge{display:inline-block;background:rgba(212,175,55,0.1);color:#c8a84b;font-size:0.7rem;padding:2px 8px;border-radius:10px;margin:0 3px 4px 0;}
  </style>
</head>
<body>
${supplementNav('')}

<div class="back-bar">
  <a href="./">← Supplement Directory</a>
  <a href="/fitness/">Fitness Hub</a>
</div>

<main>
  <div class="sup-hero">
    <span class="sup-tier-badge">${escHtml(tierLabel)}</span>
    <h1 class="sup-name">${escHtml(s.name)}</h1>
    <div style="color:var(--gray);font-size:0.82rem;margin-bottom:10px;">${escHtml(s.category)}</div>
    <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:6px;">
      ${(s.populations||[]).map(p=>`<span class="pop-badge">${escHtml(populationLabels[p]||p)}</span>`).join('')}
    </div>
    <div>
      ${evidenceBadge(s.evidence)}
      <span style="color:#666;font-size:0.7rem;margin-left:8px;">Evidence Grade</span>
    </div>
  </div>

  <div style="padding:0 20px;">

    <!-- MOOP's take -->
    <div class="moop-take" style="margin-top:20px;">
      <div class="moop-label">MOOP's Take</div>
      ${escHtml(isAvoid ? (s.why_i_avoid_it||s.my_protocol||'') : (s.why_i_take_it||s.my_protocol||''))}
    </div>

    ${isAvoid ? `
    <!-- Avoid warning -->
    <div class="avoid-warning">
      <h3>⚠️ Why I Don't Recommend This</h3>
      <p style="color:#e0a0a0;font-size:0.88rem;line-height:1.65;margin:0;">${escHtml(s.avoid_reason||'')}</p>
    </div>` : ''}

    ${!isAvoid ? `
    <!-- Protocol box -->
    <div class="protocol-box">
      <h3>My Protocol</h3>
      ${s.timing ? `<div class="protocol-row"><span class="protocol-label">Timing</span><span class="protocol-val">${escHtml(s.timing)}</span></div>` : ''}
      ${s.dose ? `<div class="protocol-row"><span class="protocol-label">Dose</span><span class="protocol-val">${escHtml(s.dose)}</span></div>` : ''}
      ${s.my_protocol ? `<div class="protocol-row" style="flex-direction:column;gap:4px;"><span class="protocol-label" style="margin-bottom:4px;">Notes</span><span class="protocol-val" style="text-align:left;">${escHtml(s.my_protocol)}</span></div>` : ''}
    </div>` : ''}

    <!-- Goals/populations -->
    ${(s.goals||[]).length ? `
    <div class="detail-card">
      <h3>What It's For</h3>
      <div style="margin-top:4px;">${(s.goals||[]).map(g=>`<span class="goal-badge">${escHtml(goalLabels[g]||g)}</span>`).join('')}</div>
    </div>` : ''}

    <!-- Coach + Doc notes -->
    ${(s.coach_note || s.doc_note) ? `
    <div class="advisor-grid">
      ${s.coach_note ? `<div class="advisor-card"><div class="advisor-name" style="color:#6abf72;">💪 Coach Arnie</div><div class="advisor-text">${escHtml(s.coach_note)}</div></div>` : ''}
      ${s.doc_note ? `<div class="advisor-card"><div class="advisor-name" style="color:#5a9bd4;">🩺 Doc Hartley</div><div class="advisor-text">${escHtml(s.doc_note)}</div></div>` : ''}
    </div>` : ''}

    <!-- Buy links -->
    ${brandsHtml ? `
    <div class="detail-card">
      <h3>Where I Buy It</h3>
      ${brandsHtml}
    </div>` : ''}

    <!-- Cost note -->
    ${s.cost_vs_generic ? `
    <div class="detail-card">
      <h3>Cost & Value</h3>
      <p>${escHtml(s.cost_vs_generic)}</p>
    </div>` : ''}

    <!-- Tags -->
    <div class="tag-row">
      ${(s.tags||[]).map(t=>`<span class="tag">${escHtml(t)}</span>`).join('')}
    </div>

    <div class="disclaimer-mini">
      ${escHtml(data.meta.disclaimer)}<br>
      ${escHtml(data.meta.affiliate_disclosure)}
    </div>
  </div>
</main>

${FOOTER}
${CHROME_SCRIPTS}
</body>
</html>`;

  fs.writeFileSync(path.join(outDir,`${s.id}.html`), html, 'utf8');
  console.log(`✅ supplements/${s.id}.html`);
}

console.log(`\n🎉 Generated ${data.supplements.length} supplement pages + index`);
