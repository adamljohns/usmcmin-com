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

function renderLanding() {
  const cards = course.modules.map((module) => {
    const live = course.publishedModuleIds && course.publishedModuleIds.has(module.id);
    const statusNote = live ? '' : ' <span class="module-draft-tag">Draft</span>';
    return `<li class="module-card${live ? '' : ' module-card-draft'}" data-module-card="${module.id}">
    <p class="eyebrow">Module ${module.number}${statusNote}</p>
    <h2><a href="${module.slug}">${esc(module.title)}</a></h2>
    <p>${esc(module.question)}</p>
    <p class="module-status" data-module-status="${module.id}">Not complete</p>
  </li>`;
  }).join('\n');
  return layout({
    title: course.title,
    description: 'A free, static, seven-module Christian course helping husbands practice faithful, attentive marriage.',
    page: 'landing',
    body: `<main id="main-content">
      <section class="hero">
        <p class="eyebrow">Free · seven modules · no account</p>
        <h1>${esc(course.title)}</h1>
        <p class="lede">${esc(course.subtitle)}</p>
        <p>${esc(course.promise)}</p>
        <div class="button-row"><a class="button" href="module-01.html">Start module 1</a><a class="button secondary" href="progress.html">View progress</a></div>
      </section>
      ${progressPanel()}
      <section aria-labelledby="syllabus-title">
        <p class="review-notice">Modules 1–3 are live with full NotebookLM media rooms. Modules 4–7 are draft placeholders until Adam approves the next wave. Original ministry prose informed by verified research; does not reproduce protected course media or transcripts.</p>
        <h2 id="syllabus-title">Course map</h2>
        <ol class="module-grid">${cards}</ol>
      </section>
      <section class="support-callout" aria-labelledby="before-title">
        <h2 id="before-title">Before you begin</h2>
        <p>This course offers education and practice for a basically safe marriage. It is not counseling or crisis care. If there is fear, coercion, violence, stalking, sexual pressure, active addiction, or immediate danger, prioritize confidential individual support rather than a joint exercise.</p>
      </section>
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
        <section id="resources" aria-labelledby="resources-title"><h2 id="resources-title">Resources</h2><p>No protected Marriage Course media or unverified NotebookLM artifacts are hosted here.</p><ul>${resources}</ul></section>
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
      <section aria-labelledby="module-progress-title"><h2 id="module-progress-title">Module status</h2><ol class="progress-list">${rows}</ol></section>
      <section class="reset-panel" aria-labelledby="reset-title"><h2 id="reset-title">Reset this device</h2><p>This clears all seven completion flags and the last-module pointer from this browser only. It cannot be undone.</p><button class="danger" type="button" data-reset-progress>Reset all course progress</button><p data-reset-message aria-live="polite"></p></section>
    </main>`
  });
}

function renderAll(root = path.resolve(__dirname, '..')) {
  const output = path.join(root, 'tmc-husband');
  fs.mkdirSync(output, { recursive: true });
  fs.writeFileSync(path.join(output, 'index.html'), renderLanding());
  fs.writeFileSync(path.join(output, 'progress.html'), renderProgress());
  for (const module of course.modules) {
    fs.writeFileSync(path.join(output, module.slug), renderModule(module));
  }
}

if (require.main === module) renderAll();

module.exports = { renderAll, renderLanding, renderModule, renderProgress };
