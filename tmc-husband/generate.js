'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { course } = require('./course.v1.js');
const { renderFieldManual } = require('./render-field-manual.js');

function esc(value) {
  return String(value).replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[character]);
}

function layout({ title, description, body, page = '', noindex = false }) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="${esc(description)}">
  ${noindex ? '<meta name="robots" content="noindex, nofollow">' : ''}
  <title>${esc(title)} | U.S.M.C. Ministries</title>
  <link rel="stylesheet" href="../assets/css/tmc-husband.v1.css">
  <script src="../assets/js/tmc-husband.v1.js" defer></script>
  <link rel="manifest" href="tmc-husband.webmanifest">
  <meta name="theme-color" content="#163047">
  <link rel="apple-touch-icon" href="../assets/icons/apple-touch-icon.png">
</head>
<body data-course-page="${esc(page)}">
  <a class="skip-link" href="#main-content">Skip to course content</a>
  <header class="site-header">
    <a class="brand" href="index.html" aria-label="The Husband Course home">U.S.M.C. <span>Ministries</span></a>
    <nav aria-label="Course navigation">
      <a href="index.html">Course</a>
      <a href="progress.html">Progress <span class="nav-progress" data-progress-short>0/7</span></a>
    </nav>
  </header>
  ${body}
  <footer>
    <p><strong>Local-only course:</strong> no login, upload, or cross-device sync. Progress is saved only in this browser on this device.</p>
    <p>${esc(course.status)}</p>
  </footer>
  <script>if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('sw.js',{scope:'/tmc-husband/'}).catch(function(){});});}</script>
</body>
</html>
`;
}

function progressPanel() {
  return `<aside class="progress-panel" aria-labelledby="course-progress-title">
    <div>
      <h2 id="course-progress-title">Your local progress</h2>
      <p data-progress-summary aria-live="polite">0 of 7 modules complete (0%).</p>
    </div>
    <div class="progress-track" role="progressbar" aria-label="Course progress" aria-valuemin="0" aria-valuemax="7" aria-valuenow="0">
      <span data-progress-bar></span>
    </div>
    <p class="local-status">Saved only on this device. Clearing browser storage removes this progress.</p>
  </aside>`;
}

// Nine ribbons (badges): first action, one per module (themed to its virtue), and commissioned.
const BADGES = [
  { id: 'first', name: 'First Action', desc: 'Shipped your first field action.', glyph: '★' },
  { id: 'm01', name: 'Foundation', desc: 'Built the foundation.', glyph: '1' },
  { id: 'm02', name: 'Understanding', desc: 'Listened to understand.', glyph: '2' },
  { id: 'm03', name: 'Peacemaker', desc: 'Fought the problem, not each other.', glyph: '3' },
  { id: 'm04', name: 'Repair', desc: 'Made a specific, safe repair.', glyph: '4' },
  { id: 'm05', name: 'Roots', desc: 'Faced the family you brought in.', glyph: '5' },
  { id: 'm06', name: 'Friendship', desc: 'Guarded friendship and intimacy.', glyph: '6' },
  { id: 'm07', name: 'Faithfulness', desc: 'Put love into action for seven days.', glyph: '7' },
  { id: 'commissioned', name: 'Commissioned', desc: 'Completed all seven modules.', glyph: '⚓' }
];

function rankBanner() {
  return `<section class="rank-banner" aria-labelledby="rank-title">
    <div class="rank-medallion" aria-hidden="true"><span>⚓</span></div>
    <div class="rank-copy">
      <p class="eyebrow" data-rank-step>Rank 0 of 7</p>
      <h2 id="rank-title" data-rank>Ashore</h2>
      <p class="rank-milestone" data-milestone aria-live="polite">Not yet under way. Begin Module 1 when you are ready.</p>
    </div>
  </section>`;
}

function badgeGrid() {
  const items = BADGES.map((badge) => `<li class="badge locked" data-badge="${badge.id}" aria-pressed="false">
      <span class="badge-icon" aria-hidden="true">${esc(badge.glyph)}</span>
      <span class="badge-name">${esc(badge.name)}</span>
      <span class="badge-desc">${esc(badge.desc)}</span>
      <span class="badge-state" data-badge-state>Locked</span>
    </li>`).join('\n');
  return `<section class="badges" aria-labelledby="badges-title">
    <div class="badges-head"><h2 id="badges-title">Ribbons</h2><p class="badge-count" data-badge-count>0 of 9 earned</p></div>
    <p class="section-intro">Earned quietly, as you ship each field action. Nothing is shared or uploaded.</p>
    <ul class="badge-grid">${items}</ul>
  </section>`;
}

function commissionCard() {
  return `<section class="commission-card" data-commission aria-hidden="true" aria-labelledby="commission-title">
    <p class="eyebrow">Charter complete</p>
    <h2 id="commission-title">Commissioned — Captain of the Home</h2>
    <p>You completed all seven modules and shipped every field action — quietly, and for the long haul. That is a real thing you did. Well done.</p>
  </section>`;
}

function renderLanding() {
  const published = course.publishedModuleIds || new Set();
  const howSteps = (course.howItWorks || []).map((step, index) => `<li class="how-step">
    <h3><span class="how-step-num" aria-hidden="true">${index + 1}</span> ${esc(step.title)}</h3>
    <p>${esc(step.body)}</p>
  </li>`).join('\n');
  const cards = course.modules.map((module) => {
    const isPublished = published.has(module.id);
    const badge = isPublished ? '' : 'Draft';
    const fieldLine = module.fieldActionSummary
      ? `<p class="module-field-action"><strong>This week:</strong> ${esc(module.fieldActionSummary)}</p>`
      : '';
    const timeLine = module.timeEstimate ? `<p class="module-time">${esc(module.timeEstimate)}</p>` : '';
    return `<li class="module-card${isPublished ? '' : ' module-card-draft'}" data-module-card="${module.id}">
    <p class="eyebrow">Module ${module.number}${badge ? ' · ' + esc(badge) : ''}</p>
    <h2><a href="${module.slug}">${esc(module.title)}</a></h2>
    <p class="module-question">${esc(module.question)}</p>
    ${fieldLine}
    ${timeLine}
    <p class="module-status" data-module-status="${module.id}">Not complete</p>
  </li>`;
  }).join('\n');
  return layout({
    title: course.title,
    description: 'A free, static, seven-module Christian course helping husbands practice faithful, attentive marriage.',
    page: 'landing',
    body: `<main id="main-content">
      <section class="hero">
        <p class="eyebrow">Free · seven modules · no account · local progress</p>
        <h1>${esc(course.title)}</h1>
        <p class="lede">${esc(course.subtitle)}</p>
        <p>${esc(course.promise)}</p>
        <div class="button-row"><a class="button" href="module-01.html">Start module 1</a><a class="button secondary" href="progress.html">View progress</a></div>
      </section>
      ${progressPanel()}
      ${rankBanner()}
      <section aria-labelledby="how-title" class="how-it-works">
        <h2 id="how-title">How it works</h2>
        <ul class="how-steps">${howSteps}</ul>
      </section>
      <section aria-labelledby="syllabus-title">
        <h2 id="syllabus-title">Course map</h2>
        <p class="section-intro">Seven modules. Each ends with one husband-owned field action with a finish line your wife could notice.</p>
        <ol class="module-grid">${cards}</ol>
      </section>
      <section class="support-callout" aria-labelledby="before-title">
        <h2 id="before-title">Before you begin</h2>
        <p>This course offers education and practice for a basically safe marriage. It is not counseling or crisis care. If there is fear, coercion, violence, stalking, sexual pressure, active addiction, or immediate danger, prioritize confidential individual support rather than a joint exercise.</p>
        <p><a href="about.html">How this course was made</a> · Original ministry prose; does not reproduce protected course media or transcripts.</p>
      </section>
    </main>`
  });
}

function renderAbout() {
  return layout({
    title: 'About This Course',
    description: 'How The Husband Course was made, what it includes, and what it is not.',
    page: 'about',
    noindex: true,
    body: `<main id="main-content">
      <header class="page-header">
        <p class="eyebrow">Background</p>
        <h1>About The Husband Course</h1>
        <p class="lede">Method, boundaries, and what you will — and will not — find inside.</p>
      </header>
      <article>
        <section aria-labelledby="what-title"><h2 id="what-title">What this is</h2>
          <p>A free, static, seven-module Christian formation course for husbands. Each module gives you a short lesson, numbered tasks with observable finish lines, one required field action, optional conversation prompts, and local progress tracking in your browser.</p>
          <p>Modules 1–3 include optional study aids (audio, video, slides, reports, quizzes) generated through <strong>Notebook by Gemini</strong> from thematically related public research. Modules 4–7 are original ministry prose without a media room.</p>
        </section>
        <section aria-labelledby="method-title"><h2 id="method-title">How it was made</h2>
          <p>Content was developed by U.S.M.C. Ministries using thematic research informed by marriage-formation literature, pastoral review, Scripture framing, and multi-model editorial critique. That research pipeline informed the teaching; it is not reproduced inside the learner path.</p>
          <p>The site is generated from source files in this repository (<code>tmc-husband/course.v1.js</code> and <code>module-*.field-manual.js</code>) via <code>node tmc-husband/generate.js</code>. Progress is stored only in <code>localStorage</code> on your device — no account, no sync.</p>
        </section>
        <section aria-labelledby="not-title"><h2 id="not-title">What this is not</h2>
          <ul>
            <li>Not a copy of The Marriage Course — no protected video, audio, transcripts, slides, or workbooks are hosted here.</li>
            <li>Not crisis care, clinical treatment, addiction recovery, or trauma therapy.</li>
            <li>Not an endorsement by The Marriage Course, Alpha, Google, or Gemini.</li>
            <li>Not deployed publicly until the principal approves — this is a local content-complete build.</li>
          </ul>
        </section>
        <section aria-labelledby="rights-title"><h2 id="rights-title">Rights and study aids</h2>
          <p>Scripture quotations follow the ministry site’s established translation practices. Notebook by Gemini artifacts are optional study aids requiring human editorial review before any public deployment. Each hosted artifact needs a documented rights basis.</p>
        </section>
        <section id="safety" aria-labelledby="safety-title"><h2 id="safety-title">Safety guidance</h2>
          <p>Every module assumes a basically safe marriage unless stated otherwise. This course is formation and practice — not counseling, crisis care, clinical treatment, addiction recovery, or trauma therapy. Abuse, coercion, threats, violence, active addiction, serious betrayal, or fear of retaliation require confidential individual help first — not a joint course exercise. A husband must never use Scripture, forgiveness, headship, money, children, or course completion to demand access, silence concern, or prevent help.</p>
          <ul>
            <li><strong>Immediate danger:</strong> Call or text <strong>911</strong> (United States), or your local emergency service.</li>
            <li><strong>Abuse or coercive control:</strong> National Domestic Violence Hotline — <strong>1-800-799-7233</strong>, or text <strong>START</strong> to <strong>88788</strong> (confidential, 24/7).</li>
            <li><strong>Where fear is present:</strong> seek confidential individual support before any joint exercise in this course.</li>
          </ul>
        </section>
      </article>
      <p class="button-row"><a class="button" href="index.html">← Back to course</a></p>
    </main>`
  });
}

function renderModule(module) {
  const prev = module.number > 1 ? `<a href="module-${String(module.number - 1).padStart(2, '0')}.html">← Module ${module.number - 1}</a>` : '<a href="index.html">← Course home</a>';
  const next = module.number < 7 ? `<a href="module-${String(module.number + 1).padStart(2, '0')}.html">Module ${module.number + 1} →</a>` : '<a href="progress.html">Progress →</a>';
  const published = course.publishedModuleIds && course.publishedModuleIds.has(module.id);
  if (module.fieldManual) {
    return renderFieldManual({ module, course, layout, progressPanel, esc, prev, next });
  }
  const paragraphs = module.missionBrief.map((paragraph) => `<p>${esc(paragraph)}</p>`).join('\n');
  const scripture = module.scripture.map((item) => `<li><h3>${esc(item.reference)}</h3><p>${esc(item.note)}</p></li>`).join('\n');
  const checks = module.selfCheck.map((item) => `<li>${esc(item)}</li>`).join('\n');
  const actionSteps = module.fieldAction.steps.map((item) => `<li>${esc(item)}</li>`).join('\n');
  const conversation = module.conversation.map((item) => `<li>${esc(item)}</li>`).join('\n');
  const resources = module.resources.map((item) => `<li><a href="${esc(item.href)}" target="_blank" rel="noopener noreferrer">${esc(item.label)} <span aria-hidden="true">↗</span></a></li>`).join('\n');

  return layout({
    title: `Module ${module.number}: ${module.title}`,
    description: module.question,
    page: module.id,
    noindex: !published,
    body: `<main id="main-content" class="lesson">
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
      <header class="lesson-header">
        <p class="eyebrow">Module ${module.number} of 7${published ? '' : ' · Draft'}</p>
        <h1>${esc(module.title)}</h1>
        <p class="lede">${esc(module.question)}</p>
        ${published ? '' : `<p class="review-notice">${esc(course.status)}</p>`}
      </header>
      ${progressPanel()}
      <article>
        <section id="mission-brief" aria-labelledby="mission-title"><h2 id="mission-title">Mission brief</h2>${paragraphs}</section>
        <section id="scripture-frame" aria-labelledby="scripture-title"><h2 id="scripture-title">Scripture frame</h2><p>Read each passage in its wider context before applying it.</p><ul class="scripture-list">${scripture}</ul></section>
        <section id="fair-insight" aria-labelledby="insight-title"><h2 id="insight-title">What the source gets right</h2><p>${esc(module.fairInsight)}</p></section>
        <section id="caution-boundary" class="caution" aria-labelledby="caution-title"><h2 id="caution-title">Where caution is required</h2><p>${esc(module.caution)}</p></section>
        <section id="self-check" aria-labelledby="check-title"><h2 id="check-title">Husband’s self-check</h2><p>Reflect privately. Do not use these prompts to diagnose or score your wife.</p><ul class="check-list">${checks}</ul></section>
        <section id="field-action" class="field-action" aria-labelledby="action-title"><p class="eyebrow">Required field action</p><h2 id="action-title">${esc(module.fieldAction.title)}</h2><ol>${actionSteps}</ol><p><strong>Observable finish line:</strong> ${esc(module.fieldAction.finishLine)}</p></section>
        <section id="conversation-guide" aria-labelledby="conversation-title"><h2 id="conversation-title">Optional conversation guide</h2><p>Invite; do not assign. Your wife may decline, stop, or suggest another format without penalty.</p><ul>${conversation}</ul></section>
        <section id="support-boundary" class="support-callout" aria-labelledby="support-title"><h2 id="support-title">Support and safety boundary</h2><p>${esc(module.support)}</p></section>
        <section id="resources" aria-labelledby="resources-title"><h2 id="resources-title">Resources</h2><p>No protected Marriage Course media or unverified Notebook by Gemini artifacts are hosted here.</p><ul>${resources}</ul></section>
        <section id="completion" class="completion" aria-labelledby="completion-title"><h2 id="completion-title">Complete module ${module.number}</h2><p>Mark complete only after the observable field-action finish line. You can change this status later.</p><button type="button" data-complete-module="${module.id}" aria-pressed="false">Mark module ${module.number} complete</button><p data-completion-message="${module.id}" aria-live="polite"></p></section>
      </article>
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
    </main>`
  });
}

function renderProgress() {
  const rows = course.modules.map((module) => `<li data-progress-module="${module.id}">
      <span data-progress-check aria-hidden="true">○</span>
      <div><a href="${module.slug}">Module ${module.number}: ${esc(module.title)}</a><p data-module-status="${module.id}">Not complete</p></div>
    </li>`).join('\n');
  return layout({
    title: 'Course Progress',
    description: 'Review and reset local progress for The Husband Course.',
    page: 'progress',
    body: `<main id="main-content">
      <header class="page-header"><p class="eyebrow">The Husband Course</p><h1>Your progress</h1><p class="lede">Seven field actions. One honest local record.</p></header>
      ${progressPanel()}
      ${rankBanner()}
      ${commissionCard()}
      ${badgeGrid()}
      <section aria-labelledby="module-progress-title"><h2 id="module-progress-title">Module status</h2><ol class="progress-list">${rows}</ol></section>
      <section class="reset-panel" aria-labelledby="reset-title"><h2 id="reset-title">Reset this device</h2><p>This clears all seven completion flags and the last-module pointer from this browser only. It cannot be undone.</p><button class="danger" type="button" data-reset-progress>Reset all course progress</button><p data-reset-message aria-live="polite"></p></section>
    </main>`
  });
}

function renderAll(root = path.resolve(__dirname, '..')) {
  const output = path.join(root, 'tmc-husband');
  fs.mkdirSync(output, { recursive: true });
  fs.writeFileSync(path.join(output, 'index.html'), renderLanding());
  fs.writeFileSync(path.join(output, 'about.html'), renderAbout());
  fs.writeFileSync(path.join(output, 'progress.html'), renderProgress());
  for (const module of course.modules) {
    fs.writeFileSync(path.join(output, module.slug), renderModule(module));
  }
}

if (require.main === module) renderAll();

module.exports = { renderAll, renderLanding, renderAbout, renderModule, renderProgress };
