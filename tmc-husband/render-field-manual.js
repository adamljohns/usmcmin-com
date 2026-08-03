'use strict';

const { bibleUrl } = require('./bible-url.js');
const { loadDrills, jsonBlock } = require('./drills.js');

function sectionCheckoff(sectionId, label = 'Done') {
  return `<div class="section-checkoff"><label class="section-checkoff-label"><input type="checkbox" data-section-complete="${sectionId}"> <span>${label}</span></label> <span class="section-tally" data-section-tally aria-live="polite"></span></div>`;
}

// One tracked line item — a Scripture passage, a self-check question, a step.
function checkItem(id, body, extra = '') {
  return `<li class="check-item"><label class="check-item-label"><input type="checkbox" data-item-complete="${id}"> <span class="check-item-body">${body}</span></label>${extra}</li>`;
}

/* The mission clock records time actually spent in the module — hours, minutes,
 * and seconds — rather than counting down from a guess. The ring fills toward
 * the module's time estimate and keeps counting past it.
 */
function missionHud(minutes) {
  return `<div id="module-mission-hud" class="mission-hud" data-mission-minutes="${minutes}" hidden aria-live="polite">
    <div class="mission-hud-inner">
      <div class="mission-timer-ring" data-mission-ring aria-hidden="true"><span class="mission-timer-pct" data-mission-pct>0%</span></div>
      <div class="mission-hud-meta">
        <p class="mission-hud-title">Time on this module <span class="mission-hud-state" data-mission-state>Counting</span></p>
        <p class="mission-hud-time" data-mission-display>0:00:00</p>
        <div class="mission-xp-track" role="progressbar" aria-label="Module checklist progress"><span data-section-progress-bar></span></div>
        <p class="mission-hud-sub"><span data-section-progress-summary>0 of 0 checks complete</span> · target ${minutes} min · course total <strong data-mission-total>0 sec</strong></p>
      </div>
      <div class="mission-hud-controls">
        <button type="button" class="mission-btn" data-mission-pause aria-pressed="false">Pause clock</button>
        <button type="button" class="mission-btn" data-mission-hide aria-pressed="false">Hide clock</button>
        <button type="button" class="mission-btn mission-btn-ghost" data-mission-reset>Reset</button>
        <button type="button" class="mission-btn mission-btn-ghost" data-mission-off>Turn timing off</button>
      </div>
    </div>
    <p class="mission-hud-off">Time tracking is off for this course. <a href="progress.html">Turn it back on</a> whenever you want it.</p>
  </div>`;
}

// A single media artifact rendered INLINE inside the lesson (not the trailing dump).
function inlineArtifact(x, esc, label) {
  if (!x) return '';
  let media = '';
  if (x.mediaType === 'video') {
    media = `<video class="artifact-media" controls preload="metadata" src="${esc(x.href)}"></video>`;
  } else if (x.mediaType === 'audio') {
    media = `<audio class="artifact-media" controls preload="metadata" src="${esc(x.href)}"></audio>`;
  } else if (x.alt) {
    media = `<a href="${esc(x.href)}"><img class="inline-graphic" src="${esc(x.href)}" alt="${esc(x.alt)}" loading="lazy"></a>`;
  }
  const kick = label || (x.mediaType === 'video' ? 'Watch' : x.mediaType === 'audio' ? 'Listen' : 'Field graphic');
  return `<figure class="inline-media inline-media-${esc(x.mediaType || 'graphic')}">
      <figcaption class="inline-media-cap"><span class="inline-media-kick">${esc(kick)}</span> ${esc(x.title)}</figcaption>
      ${media}
      ${x.summary ? `<p class="inline-media-sum">${esc(x.summary)}</p>` : ''}
    </figure>`;
}

function renderResourceGroups(m, esc, inlinedSlugs = new Set(), nativeGroups = new Set()) {
  if (!m.resources || !m.artifacts) return '';

  // Anything now rendered natively further down the page (flashcards, quiz) is
  // dropped here so the same drill is not offered twice.
  const remaining = m.artifacts.filter((x) => !inlinedSlugs.has(x.slug) && !nativeGroups.has(x.group));
  const resourceGroups = m.resources.groups.map((group) => {
    const artifacts = remaining.filter((x) => x.group === group.key).map((x) => {
      let media = '';
      if (x.state === 'local' && x.mediaType === 'video') {
        media = `<video class="artifact-media" controls preload="metadata" src="${esc(x.href)}"></video>`;
      } else if (x.state === 'local' && x.mediaType === 'audio') {
        media = `<audio class="artifact-media" controls preload="metadata" src="${esc(x.href)}"></audio>`;
      }
      const defaultLabel = x.linkLabel || (x.mediaType === 'video' ? 'Watch' : x.mediaType === 'audio' ? 'Listen' : x.alt ? 'View graphic' : 'Open');
      const link = x.state === 'local'
        ? `${media}<a class="artifact-link" href="${esc(x.href)}"${['quiz', 'flashcards'].includes(x.group) ? ' target="_blank" rel="noopener noreferrer"' : ''}>${esc(defaultLabel)}</a>`
        : '<span class="artifact-held">Available in your Notebook by Gemini — not hosted here</span>';
      const image = x.alt ? `<a href="${esc(x.href)}"><img src="${esc(x.href)}" alt="${esc(x.alt)}" loading="lazy"></a>` : '';
      return `<article class="artifact-card" data-artifact="${esc(x.slug)}" data-artifact-state="${esc(x.state)}"><p class="eyebrow">${esc(x.kind || group.heading)}</p><h4>${esc(x.title)}</h4>${link}${image}<p>${esc(x.summary)}</p></article>`;
    }).join('\n');
    if (!artifacts) return '';
    return `<section class="resource-group" aria-labelledby="resource-${esc(group.key)}"><h3 id="resource-${esc(group.key)}">${esc(group.heading)}</h3><p>${esc(group.note)}</p><div class="artifact-grid">${artifacts}</div></section>`;
  }).join('\n');

  const withheldBlock = m.resources.withheldNotice
    ? `<aside class="withheld-notice"><h3>Not hosted on this site</h3><p>${esc(m.resources.withheldNotice)}</p></aside>`
    : '';

  const notebookBlock = m.resources.notebook ? `<article><h3>${esc(m.resources.notebook.title)}</h3><p>${esc(m.resources.notebook.body)}</p><a href="${esc(m.resources.notebook.href)}" target="_blank" rel="noopener noreferrer">${esc(m.resources.notebook.label)} <span aria-hidden="true">↗</span></a></article>` : '';
  const journalBlock = m.resources.journal ? `<article><h3>${esc(m.resources.journal.heading)}</h3><p>${esc(m.resources.journal.body)}</p><a href="${esc(m.resources.journal.href)}" target="_blank" rel="noopener noreferrer sponsored">${esc(m.resources.journal.label)} <span aria-hidden="true">↗</span></a><p><small>${esc(m.resources.journal.disclosure)}</small></p></article>` : '';

  // If everything worth showing was already woven into the lesson, skip the trailing section.
  if (!resourceGroups && !withheldBlock && !notebookBlock && !journalBlock) return '';

  return `<section id="resources" aria-labelledby="resources-title" data-track-section="resources">
    <p class="eyebrow">Study library</p>
    <h2 id="resources-title">More study aids</h2>
    <p>Optional extras beyond the media woven into the lesson above — go deeper if you want to.</p>
    ${resourceGroups}
    ${withheldBlock}
    <div class="resource-actions">${notebookBlock}${journalBlock}</div>
    ${sectionCheckoff('resources')}
  </section>`;
}

/* Flashcards come before the quiz: drill the material, then test it. */
function renderFlashcards(cards, esc, moduleNumber) {
  if (!cards.length) return '';
  return `<section id="flashcards" class="drill-panel" aria-labelledby="flashcards-title" data-track-section="flashcards" data-flashcards>
      <p class="eyebrow">Drill first</p>
      <h2 id="flashcards-title">Flashcards</h2>
      <p>${cards.length} cards from the Module ${moduleNumber} study material. Read the prompt, answer it in your head, then reveal. Mark a card known when you can answer it without help — the deck remembers on this device.</p>
      <div class="flashcard-progress"><span class="flashcard-bar-track"><span class="flashcard-bar" data-card-bar></span></span> <span class="flashcard-tally" data-card-tally aria-live="polite">0 of ${cards.length} marked known (0%)</span></div>
      <div class="flashcard-stage">
        <div class="flashcard" data-card-inner tabindex="0" role="button" aria-label="Flashcard — activate to reveal the answer">
          <p class="flashcard-face" data-card-face></p>
          <p class="flashcard-back" data-card-back></p>
        </div>
      </div>
      <p class="flashcard-counter" data-card-counter aria-live="polite">Card 1 of ${cards.length}</p>
      <div class="drill-controls">
        <button type="button" class="mission-btn" data-card-prev aria-label="Previous card">&larr; Previous</button>
        <button type="button" class="mission-btn" data-card-flip>Show answer</button>
        <button type="button" class="mission-btn" data-card-known aria-pressed="false">Mark known</button>
        <button type="button" class="mission-btn" data-card-next aria-label="Next card">Next &rarr;</button>
        <button type="button" class="mission-btn mission-btn-ghost" data-card-reset>Clear deck</button>
      </div>
      <script type="application/json" id="tmc-flashcard-data">${jsonBlock(cards)}</script>
      <div class="section-checkoff"><label class="section-checkoff-label"><input type="checkbox" data-item-complete="flashcards"> <span>Flashcard drill done</span></label></div>
    </section>`;
}

/* The knowledge check is the last thing in the module before you mark it complete. */
function renderQuiz(questions, esc, moduleNumber, intro) {
  if (!questions.length) return '';
  return `<section id="quiz" class="drill-panel assessment-panel" aria-labelledby="quiz-title" data-track-section="quiz" data-quiz>
      <p class="eyebrow">Last step before you close the module</p>
      <h2 id="quiz-title">Knowledge check</h2>
      <p>${esc(intro || `Take this after the tasks, the field action, and the flashcards. ${questions.length} questions — each answer explains itself, right or wrong. Your answers stay on this device.`)}</p>
      <div class="flashcard-progress"><span class="flashcard-bar-track"><span class="flashcard-bar" data-quiz-bar></span></span> <span class="flashcard-tally" data-quiz-score aria-live="polite">0 of ${questions.length} answered</span></div>
      <ol class="quiz-list" data-quiz-list></ol>
      <div class="drill-controls"><button type="button" class="mission-btn mission-btn-ghost" data-quiz-reset>Clear answers and retake</button></div>
      <script type="application/json" id="tmc-quiz-data">${jsonBlock(questions)}</script>
      <div class="section-checkoff"><label class="section-checkoff-label"><input type="checkbox" data-item-complete="quiz"> <span>Knowledge check done</span></label></div>
    </section>`;
}

function renderFieldManual({ module, course, layout, progressPanel, esc, prev, next }) {
  const m = module.fieldManual;
  const ps = (items) => items.map((x) => `<p>${esc(x)}</p>`).join('\n');

  const scripture = m.scripture.map((item, index) => {
    const href = item.href || bibleUrl(item.reference);
    const body = `<h3><a href="${esc(href)}" target="_blank" rel="noopener noreferrer">${esc(item.reference)}</a></h3><p>${esc(item.note)}</p>`;
    return checkItem(`scripture-${index + 1}`, body);
  }).join('\n');

  const tasks = m.tasks.map((task) => {
    const actions = task.actions.map((a) => `<li>${esc(a)}</li>`).join('');
    const callout = task.callout
      ? `<div class="task-callout"><p class="task-callout-label">${esc(task.callout.label)}</p><p>${esc(task.callout.body)}</p></div>`
      : '';
    return `<article class="task-block" id="task-${esc(task.number)}" data-track-section="task-${esc(task.number)}">
      <p class="task-kicker">Task ${esc(task.number)}</p>
      <h3 class="task-title">${esc(task.title)}</h3>
      ${task.tagline ? `<p class="task-tagline">${esc(task.tagline)}</p>` : ''}
      ${task.setup ? `<p class="task-setup">${esc(task.setup)}</p>` : ''}
      <p class="task-actions-label">Actions</p>
      <ol class="task-actions">${actions}</ol>
      ${callout}
      ${sectionCheckoff(`task-${task.number}`, 'Task complete')}
    </article>`;
  }).join('\n');

  const actionSteps = m.fieldAction.steps
    .map((item, index) => checkItem(`action-step-${index + 1}`, esc(item)))
    .join('\n');
  const conversationItems = m.conversation.items
    .map((item, index) => checkItem(`conversation-${index + 1}`, esc(item)))
    .join('\n');
  const selfCheckItems = (m.selfCheck || [])
    .map((item, index) => checkItem(`self-check-${index + 1}`, esc(item)))
    .join('\n');

  // Weave the primary media into the lesson flow (not the trailing dump).
  const arts = m.artifacts || [];
  const firstOf = (grp) => arts.find((a) => a.group === grp && a.state === 'local' && (a.mediaType || a.alt));
  const openingVideo = firstOf('video');
  const tasksGraphic = firstOf('infographics');
  const reflectAudio = firstOf('audio');
  const inlinedSlugs = new Set([openingVideo, tasksGraphic, reflectAudio].filter(Boolean).map((a) => a.slug));

  const drills = loadDrills(module.id);
  const nativeGroups = new Set([
    drills.flashcards.length ? 'flashcards' : null,
    drills.quiz.length ? 'quiz' : null
  ].filter(Boolean));

  const flashcardsSection = renderFlashcards(drills.flashcards, esc, module.number);
  const quizSection = renderQuiz(drills.quiz, esc, module.number, m.assessment && m.assessment.intro);

  // The paper track. Every module has a fillable insert; the whole course has a
  // workbook. Built by tmc-husband/print/*.py.
  const pad = String(module.number).padStart(2, '0');
  const insertLink = `<aside class="module-print" aria-labelledby="print-${module.number}-title">
      <p class="eyebrow">Work it on paper</p>
      <h2 id="print-${module.number}-title">Module ${module.number} study insert</h2>
      <p>A fillable PDF for this module: a note block for each video and audio briefing, reading notes on every study report, and this module&rsquo;s knowledge check laid out so you can grade yourself. Type into it, or print it and use a pen.</p>
      <p class="button-row"><a class="button" href="/downloads/tmc-husband/The_Husband_Course_Module_${pad}_INSERT.pdf">Download the module ${module.number} insert (PDF)</a></p>
      <p class="module-print-alt">Taking the whole course on paper? <a href="/downloads/tmc-husband/The_Husband_Course_FIELD_WORKBOOK.pdf">The Husband&rsquo;s Field Workbook</a> carries all seven modules.</p>
    </aside>`;

  const hasResources = (m.artifacts && m.artifacts.length > 0) || (m.resources?.groups && m.resources.groups.length > 0);
  const resourcesSection = hasResources ? renderResourceGroups(m, esc, inlinedSlugs, nativeGroups) : '';
  const missionMinutes = m.missionDurationMinutes || 60;
  const published = course.publishedModuleIds && course.publishedModuleIds.has(module.id);

  return layout({
    title: `Module ${module.number}: ${module.title}`,
    description: module.question,
    page: module.id,
    noindex: !published,
    body: `${missionHud(missionMinutes)}
    <main id="main-content" class="lesson field-manual" data-field-manual="${module.id}">
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
      <header class="lesson-header module-hero">
        <span class="course-badge">Module ${module.number} &middot; The Husband Course</span>
        <p class="eyebrow">Module ${module.number} of 7 · ${esc(m.timeEstimate)}${published ? '' : ' · Draft'}</p>
        <h1>${esc(module.title)}</h1>
        <p class="lede">${esc(module.question)}</p>
        ${m.finishLineHero ? `<p class="finish-line-hero"><strong>This week&apos;s finish line:</strong> ${esc(m.finishLineHero)}</p>` : ''}
        ${published ? '' : `<p class="review-notice">${esc(course.status)}</p>`}
      </header>
      <article>
        <section id="opening" aria-labelledby="opening-title" data-track-section="opening">
          <p class="eyebrow">Opening</p>
          <h2 id="opening-title">Why this matters now</h2>
          ${ps(m.opening)}
          ${openingVideo ? inlineArtifact(openingVideo, esc, 'Watch first') : ''}
          ${sectionCheckoff('opening')}
        </section>
        <section id="scripture-frame" aria-labelledby="scripture-title" data-track-section="scripture">
          <p class="eyebrow">Scripture anchor</p>
          <h2 id="scripture-title">Ground your work in Scripture</h2>
          <p>Read each passage in its wider context before applying it. Check each one as you read it.</p>
          <ul class="scripture-list check-list">${scripture}</ul>
        </section>
        <section id="tasks" aria-labelledby="tasks-title">
          <p class="eyebrow">This week</p>
          <h2 id="tasks-title">Your tasks</h2>
          <p>Work through these in order. Each task has an observable finish line.</p>
          ${tasksGraphic ? inlineArtifact(tasksGraphic, esc, "This week's field guide") : ''}
          ${tasks}
        </section>
        ${selfCheckItems ? `<section id="self-check" aria-labelledby="check-title" data-track-section="self-check"><h2 id="check-title">Private self-check</h2><p>Reflect alone, then check each one off. Do not use these to diagnose or score your wife.</p><ul class="check-list">${selfCheckItems}</ul>${reflectAudio ? inlineArtifact(reflectAudio, esc, 'Listen while you reflect') : ''}</section>` : ''}
        <section id="field-action" class="field-action" aria-labelledby="action-title" data-track-section="field-action">
          <p class="eyebrow">Required field action</p>
          <h2 id="action-title">${esc(m.fieldAction.title)}</h2>
          <ul class="check-list">${actionSteps}</ul>
          <p><strong>Observable finish line:</strong> ${esc(m.fieldAction.finishLine)}</p>
          ${sectionCheckoff('field-action', 'Field action complete')}
        </section>
        <section id="conversation-guide" aria-labelledby="conversation-title" data-track-section="conversation">
          <h2 id="conversation-title">Optional conversation guide</h2>
          <p>${esc(m.conversation.intro)}</p>
          <ul class="check-list">${conversationItems}</ul>
        </section>
        <aside id="safety" class="module-safety" aria-labelledby="safety-title">
          <h2 id="safety-title">Safety for this module</h2>
          <p>${esc(m.caution)}</p>
          <p class="module-safety-link"><a href="about.html#safety">Full safety guidance, boundaries, and where to find confidential help &rarr;</a></p>
        </aside>
        ${resourcesSection}
        ${insertLink}
        ${flashcardsSection}
        ${quizSection}
        <section id="completion" class="completion" aria-labelledby="completion-title" data-track-section="completion">
          <h2 id="completion-title">Complete module ${module.number}</h2>
          <p>Mark complete only after the field-action finish line. You can change this later.</p>
          <p class="completion-tally"><span data-section-progress-summary>0 of 0 checks complete</span> · <span data-mission-total>0 sec</span> logged across the course.</p>
          <button type="button" data-complete-module="${module.id}" aria-pressed="false">Mark module ${module.number} complete</button>
          <p data-completion-message="${module.id}" aria-live="polite"></p>
        </section>
      </article>
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
    </main>`
  });
}

module.exports = { renderFieldManual, sectionCheckoff, missionHud, checkItem };
