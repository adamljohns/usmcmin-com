'use strict';

const { bibleUrl } = require('./bible-url.js');

function sectionCheckoff(sectionId, label = 'Done') {
  return `<div class="section-checkoff"><label class="section-checkoff-label"><input type="checkbox" data-section-complete="${sectionId}"> <span>${label}</span></label></div>`;
}

function missionHud(minutes) {
  return `<div id="module-mission-hud" class="mission-hud" data-mission-minutes="${minutes}" hidden aria-live="polite">
    <div class="mission-hud-inner">
      <div class="mission-timer-ring" aria-hidden="true"><span class="mission-timer-pct" data-mission-pct>100%</span></div>
      <div class="mission-hud-meta">
        <p class="mission-hud-title">Module mission clock</p>
        <p class="mission-hud-time" data-mission-display>${minutes}:00</p>
        <div class="mission-xp-track" role="progressbar" aria-label="Module task progress"><span data-section-progress-bar></span></div>
        <p class="mission-hud-sub" data-section-progress-summary>0 tasks checked</p>
      </div>
      <div class="mission-hud-controls">
        <button type="button" class="mission-btn" data-mission-start>Start clock</button>
        <button type="button" class="mission-btn" data-mission-pause hidden>Pause</button>
        <button type="button" class="mission-btn mission-btn-ghost" data-mission-add5>+5 min</button>
      </div>
    </div>
  </div>`;
}

function renderResourceGroups(m, esc) {
  if (!m.resources || !m.artifacts) return '';

  const resourceGroups = m.resources.groups.map((group) => {
    const artifacts = m.artifacts.filter((x) => x.group === group.key).map((x) => {
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
    return `<section class="resource-group" aria-labelledby="resource-${esc(group.key)}"><h3 id="resource-${esc(group.key)}">${esc(group.heading)}</h3><p>${esc(group.note)}</p><div class="artifact-grid">${artifacts}</div></section>`;
  }).join('\n');

  const withheldBlock = m.resources.withheldNotice
    ? `<aside class="withheld-notice"><h3>Not hosted on this site</h3><p>${esc(m.resources.withheldNotice)}</p></aside>`
    : '';

  const notebookBlock = m.resources.notebook ? `<article><h3>${esc(m.resources.notebook.title)}</h3><p>${esc(m.resources.notebook.body)}</p><a href="${esc(m.resources.notebook.href)}" target="_blank" rel="noopener noreferrer">${esc(m.resources.notebook.label)} <span aria-hidden="true">↗</span></a></article>` : '';
  const journalBlock = m.resources.journal ? `<article><h3>${esc(m.resources.journal.heading)}</h3><p>${esc(m.resources.journal.body)}</p><a href="${esc(m.resources.journal.href)}" target="_blank" rel="noopener noreferrer sponsored">${esc(m.resources.journal.label)} <span aria-hidden="true">↗</span></a><p><small>${esc(m.resources.journal.disclosure)}</small></p></article>` : '';

  return `<section id="resources" aria-labelledby="resources-title" data-track-section="resources">
    <p class="eyebrow">Resource room</p>
    <h2 id="resources-title">Study aids</h2>
    <p>${esc(m.resources.intro)}</p>
    ${resourceGroups}
    ${withheldBlock}
    <div class="resource-actions">${notebookBlock}${journalBlock}</div>
    ${sectionCheckoff('resources')}
  </section>`;
}

function renderFieldManual({ module, course, layout, progressPanel, esc, prev, next }) {
  const m = module.fieldManual;
  const ps = (items) => items.map((x) => `<p>${esc(x)}</p>`).join('\n');
  const lis = (items) => items.map((x) => `<li>${esc(x)}</li>`).join('\n');

  const scripture = m.scripture.map((item) => {
    const href = item.href || bibleUrl(item.reference);
    return `<li><h3><a href="${esc(href)}" target="_blank" rel="noopener noreferrer">${esc(item.reference)}</a></h3><p>${esc(item.note)}</p></li>`;
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

  const actionSteps = m.fieldAction.steps.map((item) => `<li>${esc(item)}</li>`).join('\n');
  const conversationItems = m.conversation.items.map((item) => `<li>${esc(item)}</li>`).join('\n');
  const selfCheckItems = (m.selfCheck || []).map((item) => `<li>${esc(item)}</li>`).join('\n');
  const referrals = m.support.referrals.map((x) => `<li><h3>${esc(x.label)}</h3><p>${esc(x.body)}${x.href ? ` <a href="${esc(x.href)}" target="_blank" rel="noopener noreferrer">${esc(x.linkLabel || x.label)} <span aria-hidden="true">↗</span></a>` : ''}</p></li>`).join('\n');

  let assessmentSection = '';
  if (m.assessment) {
    assessmentSection = `<section id="assessment" class="assessment-panel" aria-labelledby="assessment-title" data-track-section="assessment">
      <h2 id="assessment-title">Knowledge check</h2>
      <p>${esc(m.assessment.intro || 'Complete the quiz after working through the module tasks.')}</p>
      <h3>Quiz</h3>
      <iframe class="assessment-frame" title="${esc(m.assessment.quizTitle)}" src="${esc(m.assessment.quizHref)}" loading="lazy"></iframe>
      <p><a href="${esc(m.assessment.quizHref)}" target="_blank" rel="noopener noreferrer">Open quiz full-screen <span aria-hidden="true">↗</span></a></p>
      ${m.assessment.flashcardsHref ? `<h3>Flashcards</h3><iframe class="assessment-frame" title="${esc(m.assessment.flashcardsTitle)}" src="${esc(m.assessment.flashcardsHref)}" loading="lazy"></iframe><p><a href="${esc(m.assessment.flashcardsHref)}" target="_blank" rel="noopener noreferrer">Open flashcards full-screen <span aria-hidden="true">↗</span></a></p>` : ''}
      ${sectionCheckoff('assessment')}
    </section>`;
  }

  const hasResources = (m.artifacts && m.artifacts.length > 0) || (m.resources?.groups && m.resources.groups.length > 0);
  const resourcesSection = hasResources ? renderResourceGroups(m, esc) : '';
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
          ${sectionCheckoff('opening')}
        </section>
        <section id="scripture-frame" aria-labelledby="scripture-title" data-track-section="scripture">
          <p class="eyebrow">Scripture anchor</p>
          <h2 id="scripture-title">Ground your work in Scripture</h2>
          <p>Read each passage in its wider context before applying it.</p>
          <ul class="scripture-list">${scripture}</ul>
          ${sectionCheckoff('scripture')}
        </section>
        <section id="tasks" aria-labelledby="tasks-title">
          <p class="eyebrow">This week</p>
          <h2 id="tasks-title">Your tasks</h2>
          <p>Work through these in order. Each task has an observable finish line.</p>
          ${tasks}
        </section>
        ${selfCheckItems ? `<section id="self-check" aria-labelledby="check-title" data-track-section="self-check"><h2 id="check-title">Private self-check</h2><p>Reflect alone. Do not use these to diagnose or score your wife.</p><ul class="check-list">${selfCheckItems}</ul>${sectionCheckoff('self-check')}</section>` : ''}
        <section id="field-action" class="field-action" aria-labelledby="action-title" data-track-section="field-action">
          <p class="eyebrow">Required field action</p>
          <h2 id="action-title">${esc(m.fieldAction.title)}</h2>
          <ol>${actionSteps}</ol>
          <p><strong>Observable finish line:</strong> ${esc(m.fieldAction.finishLine)}</p>
          ${sectionCheckoff('field-action', 'Field action complete')}
        </section>
        <section id="conversation-guide" aria-labelledby="conversation-title" data-track-section="conversation">
          <h2 id="conversation-title">Optional conversation guide</h2>
          <p>${esc(m.conversation.intro)}</p>
          <ul>${conversationItems}</ul>
          ${sectionCheckoff('conversation')}
        </section>
        <section id="caution-boundary" class="caution" aria-labelledby="caution-title" data-track-section="caution">
          <h2 id="caution-title">Read before you proceed</h2>
          <p>${esc(m.caution)}</p>
          ${sectionCheckoff('caution')}
        </section>
        <section id="support-boundary" class="support-callout" aria-labelledby="support-title" data-track-section="support">
          <h2 id="support-title">Support and safety</h2>
          <p>${esc(m.support.lead)}</p>
          <ul>${referrals}</ul>
          <p>${esc(m.support.close)}</p>
          ${sectionCheckoff('support')}
        </section>
        ${resourcesSection}
        ${assessmentSection}
        <section id="completion" class="completion" aria-labelledby="completion-title" data-track-section="completion">
          <h2 id="completion-title">Complete module ${module.number}</h2>
          <p>Mark complete only after the field-action finish line. You can change this later.</p>
          <button type="button" data-complete-module="${module.id}" aria-pressed="false">Mark module ${module.number} complete</button>
          <p data-completion-message="${module.id}" aria-live="polite"></p>
        </section>
      </article>
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
    </main>`
  });
}

module.exports = { renderFieldManual, sectionCheckoff, missionHud };
