'use strict';

function sectionCheckoff(sectionId) {
  return `<div class="section-checkoff"><label class="section-checkoff-label"><input type="checkbox" data-section-complete="${sectionId}"> <span>Section complete</span></label></div>`;
}

function missionHud(minutes) {
  return `<div id="module-mission-hud" class="mission-hud" data-mission-minutes="${minutes}" hidden aria-live="polite">
    <div class="mission-hud-inner">
      <div class="mission-timer-ring" aria-hidden="true"><span class="mission-timer-pct" data-mission-pct>100%</span></div>
      <div class="mission-hud-meta">
        <p class="mission-hud-title">Module mission clock</p>
        <p class="mission-hud-time" data-mission-display>${minutes}:00</p>
        <div class="mission-xp-track" role="progressbar" aria-label="Module section progress"><span data-section-progress-bar></span></div>
        <p class="mission-hud-sub" data-section-progress-summary>0 sections checked</p>
      </div>
      <div class="mission-hud-controls">
        <button type="button" class="mission-btn" data-mission-start>Start clock</button>
        <button type="button" class="mission-btn" data-mission-pause hidden>Pause</button>
        <button type="button" class="mission-btn mission-btn-ghost" data-mission-add5>+5 min</button>
      </div>
    </div>
  </div>`;
}

function renderFieldManual({ module, course, layout, progressPanel, esc, prev, next }) {
  const m = module.fieldManual;
  const ps = (items) => items.map((x) => `<p>${esc(x)}</p>`).join('\n');
  const lis = (items) => items.map((x) => `<li>${esc(x)}</li>`).join('\n');
  const labelled = (label, heading, items) => `<div class="provenance-block"><p class="provenance-label">${esc(label)}</p><h3>${esc(heading)}</h3>${ps(items)}</div>`;

  const sectionNav = m.sectionNav.map((x) => `<a href="${esc(x.href)}">${esc(x.label)}</a>`).join('');
  const counts = m.inventory.counts.map((x) => `<li><strong>${esc(x.value)}</strong><span>${esc(x.label)}</span><small>${esc(x.detail)}</small></li>`).join('');
  const sources = m.sources.map((x) => `<li data-source="${esc(x.slug)}"><p class="eyebrow">${esc(x.lane)}</p><h3>${esc(x.title)}</h3><p>${esc(x.note)}</p></li>`).join('\n');
  const scripture = m.scripture.entries.map((x) => `<li><h3>${esc(x.reference)}</h3><p><strong>Original source teaching:</strong> ${esc(x.teaching)}</p><p><strong>U.S.M.C. Ministries analysis:</strong> ${esc(x.caveat)}</p></li>`).join('\n');
  const slogans = m.caution.slogans.map((x) => `<li><blockquote>${esc(x.line)}</blockquote><p class="source-stamp">${esc(x.stamp)}</p><p>${esc(x.qualification)}</p></li>`).join('\n');
  const days = m.fieldExercise.days.map((x) => `<li><p class="eyebrow">${esc(x.day)}</p><h3>${esc(x.title)}</h3><p>${esc(x.body)}</p></li>`).join('\n');
  const referrals = m.referral.referrals.map((x) => `<li><h3>${esc(x.label)}</h3><p>${esc(x.body)}${x.href ? ` <a href="${esc(x.href)}" target="_blank" rel="noopener noreferrer">${esc(x.linkLabel)} <span aria-hidden="true">↗</span></a>` : ''}</p></li>`).join('\n');

  let frameworkSection = '';
  if (m.vineyardFramework) {
    const tasks = m.vineyardFramework.tasks.map((x) => `<li class="principle-card"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.name)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.husbandMove)}</p><p class="guardrail"><strong>Guardrail:</strong> ${esc(x.guardrail)}</p></li>`).join('\n');
    const practices = m.vineyardFramework.practices.items.map((x) => `<li><h4>${esc(x.name)}</h4><p>${esc(x.body)}</p></li>`).join('\n');
    frameworkSection = `<section id="vineyard-framework" aria-labelledby="framework-title" data-track-section="vineyard-framework"><p class="eyebrow">Vineyard framework</p><h2 id="framework-title">${esc(m.vineyardFramework.heading)}</h2><p>${esc(m.vineyardFramework.lead)}</p><ol class="principle-grid">${tasks}</ol><h3>${esc(m.vineyardFramework.practices.heading)}</h3><ul class="posture-grid">${practices}</ul>${sectionCheckoff('vineyard-framework')}</section>`;
  } else if (m.communicationFramework) {
    const levels = m.communicationFramework.levels.map((x) => `<li class="principle-card"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.name)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.husbandMove)}</p><p class="guardrail"><strong>Guardrail:</strong> ${esc(x.guardrail)}</p></li>`).join('\n');
    const habits = m.communicationFramework.habits.map((x) => `<li class="principle-card"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.name)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.husbandMove)}</p><p class="guardrail"><strong>Failure mode:</strong> ${esc(x.failureMode)}</p></li>`).join('\n');
    frameworkSection = `<section id="communication-framework" aria-labelledby="framework-title" data-track-section="communication-framework"><p class="eyebrow">Communication framework</p><h2 id="framework-title">${esc(m.communicationFramework.heading)}</h2><p>${esc(m.communicationFramework.lead)}</p><h3>Three levels of communication</h3><ol class="principle-grid">${levels}</ol><h3>Five bad listening habits</h3><ol class="principle-grid">${habits}</ol>${sectionCheckoff('communication-framework')}</section>`;
  } else if (m.coreFramework) {
    const principles = m.coreFramework.principles.map((x) => `<li class="principle-card"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.name)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.husbandMove)}</p><p class="guardrail"><strong>Guardrail:</strong> ${esc(x.guardrail)}</p></li>`).join('\n');
    const postures = m.coreFramework.postures.items.map((x) => `<li><h4>${esc(x.name)}</h4><p>${esc(x.looksLike)}</p><p><strong>Cost:</strong> ${esc(x.cost)}</p></li>`).join('\n');
    frameworkSection = `<section id="core-framework" aria-labelledby="framework-title" data-track-section="core-framework"><p class="eyebrow">Core conflict framework</p><h2 id="framework-title">${esc(m.coreFramework.heading)}</h2><p>${esc(m.coreFramework.lead)}</p><ol class="principle-grid">${principles}</ol><h3>${esc(m.coreFramework.postures.heading)}</h3><p>${esc(m.coreFramework.postures.note)}</p><ul class="posture-grid">${postures}</ul><div class="externalise-panel"><h3>${esc(m.coreFramework.externalise.heading)}</h3><p><strong>Original source teaching:</strong> ${esc(m.coreFramework.externalise.teaching)}</p><p><strong>U.S.M.C. Ministries analysis:</strong> ${esc(m.coreFramework.externalise.analysis)}</p><p class="guardrail"><strong>Critical guardrail:</strong> ${esc(m.coreFramework.externalise.criticalNote)}</p></div>${sectionCheckoff('core-framework')}</section>`;
  }

  const pauseSection = m.pauseProtocol ? `<section id="pause-protocol" aria-labelledby="pause-title" data-track-section="pause-protocol"><p class="eyebrow">Pause and return</p><h2 id="pause-title">${esc(m.pauseProtocol.heading)}</h2>${labelled('Original source teaching', m.pauseProtocol.teaching.heading, m.pauseProtocol.teaching.paragraphs)}<div class="provenance-block"><p class="provenance-label">U.S.M.C. Ministries analysis &amp; application</p><h3>${esc(m.pauseProtocol.analysis.heading)}</h3><p>${esc(m.pauseProtocol.analysis.lead)}</p><ol>${lis(m.pauseProtocol.analysis.rules)}</ol><h4>This is not a pause</h4><ul>${lis(m.pauseProtocol.analysis.notAPause)}</ul></div><p class="safety-line">${esc(m.pauseProtocol.safetyLine)}</p>${sectionCheckoff('pause-protocol')}</section>` : '';

  const fiveStepsSection = m.fiveSteps ? (() => {
    const steps = m.fiveSteps.steps.map((x) => `<li class="protocol-step"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.step)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.execution)}</p><p class="guardrail"><strong>Failure mode:</strong> ${esc(x.failureMode)}</p></li>`).join('\n');
    return `<section id="five-steps" aria-labelledby="steps-title" data-track-section="five-steps"><p class="eyebrow">Five-step protocol</p><h2 id="steps-title">${esc(m.fiveSteps.heading)}</h2><p>${esc(m.fiveSteps.intro)}</p><h3>Preconditions</h3><ul>${lis(m.fiveSteps.preconditions)}</ul><ol class="protocol-list">${steps}</ol><p>${esc(m.fiveSteps.close)}</p>${sectionCheckoff('five-steps')}</section>`;
  })() : '';

  const conversationSection = m.conversationGuide ? (() => {
    const guide = m.conversationGuide.steps.map((x) => `<li><strong>${esc(x.label)}:</strong> ${esc(x.body)}</li>`).join('\n');
    return `<section id="conversation-guide" aria-labelledby="conversation-title" data-track-section="conversation-guide"><h2 id="conversation-title">${esc(m.conversationGuide.heading)}</h2><p>${esc(m.conversationGuide.intro)}</p><ol>${guide}</ol><p class="guardrail">${esc(m.conversationGuide.pauseSignal)}</p>${sectionCheckoff('conversation-guide')}</section>`;
  })() : '';

  const resourceGroups = m.resources.groups.map((group) => {
    const artifacts = m.artifacts.filter((x) => x.group === group.key).map((x) => {
      let media = '';
      if (x.state === 'local' && x.mediaType === 'video') {
        media = `<video class="artifact-media" controls preload="metadata" src="${esc(x.href)}"></video>`;
      } else if (x.state === 'local' && x.mediaType === 'audio') {
        media = `<audio class="artifact-media" controls preload="metadata" src="${esc(x.href)}"></audio>`;
      }
      const defaultLabel = x.linkLabel || (x.mediaType === 'video' ? 'Open video file' : x.mediaType === 'audio' ? 'Open audio file' : x.alt ? 'Open full-size graphic' : 'Open file');
      const link = x.state === 'local'
        ? `${media}<a class="artifact-link" href="${esc(x.href)}"${['quiz', 'flashcards'].includes(x.group) ? ' target="_blank" rel="noopener noreferrer"' : ''}>${esc(defaultLabel)}</a>`
        : '<span class="artifact-held">Named for review · not published</span>';
      const image = x.alt ? `<a href="${esc(x.href)}"><img src="${esc(x.href)}" alt="${esc(x.alt)}" loading="lazy"></a>` : '';
      return `<article class="artifact-card" data-artifact="${esc(x.slug)}" data-artifact-state="${esc(x.state)}"><p class="eyebrow">${esc(x.kind || (x.state === 'withheld' ? 'Held media' : group.heading))}</p><h4>${esc(x.title)}</h4>${link}${image}<p>${esc(x.summary)}</p></article>`;
    }).join('\n');
    return `<section class="resource-group" aria-labelledby="resource-${esc(group.key)}"><h3 id="resource-${esc(group.key)}">${esc(group.heading)} <span>${esc(group.count)}</span></h3><p>${esc(group.note)}</p><div class="artifact-grid">${artifacts}</div></section>`;
  }).join('\n');

  const withheldBlock = m.resources.withheldNotice
    ? `<aside class="withheld-notice"><h3>Publication gate for held artifacts</h3><p>${esc(m.resources.withheldNotice)}</p></aside>`
    : '';

  const assessmentSection = m.assessment ? `<section id="assessment" class="assessment-panel" aria-labelledby="assessment-title" data-track-section="assessment"><h2 id="assessment-title">${esc(m.assessment.heading)}</h2><p>${esc(m.assessment.intro)}</p><h3>Quiz</h3><iframe class="assessment-frame" title="${esc(m.assessment.quizTitle)}" src="${esc(m.assessment.quizHref)}" loading="lazy"></iframe><p><a href="${esc(m.assessment.quizHref)}" target="_blank" rel="noopener noreferrer">Open quiz full-screen <span aria-hidden="true">↗</span></a></p>${m.assessment.flashcardsHref ? `<h3>Flashcards</h3><iframe class="assessment-frame" title="${esc(m.assessment.flashcardsTitle)}" src="${esc(m.assessment.flashcardsHref)}" loading="lazy"></iframe><p><a href="${esc(m.assessment.flashcardsHref)}" target="_blank" rel="noopener noreferrer">Open flashcards full-screen <span aria-hidden="true">↗</span></a></p>` : ''}${sectionCheckoff('assessment')}</section>` : '';

  const missionMinutes = m.missionDurationMinutes || 75;
  const published = course.publishedModuleIds && course.publishedModuleIds.has(module.id);
  const prototypeBanner = published
    ? ''
    : `<div class="prototype-banner" role="status"><strong>Local prototype.</strong> ${esc(course.status)}</div>`;
  const reviewNotice = published ? '' : `<p class="review-notice">${esc(course.status)}</p>`;

  return layout({
    title: `Module ${module.number}: ${module.title}`,
    description: module.question,
    page: module.id,
    noindex: !published,
    body: `${prototypeBanner}
    ${missionHud(missionMinutes)}
    <main id="main-content" class="lesson field-manual" data-field-manual="${module.id}">
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
      <header class="lesson-header field-manual-header">
        <p class="eyebrow">Module ${module.number} of 7 · ${esc(m.reviewStatus)}</p>
        <h1>${esc(module.title)}</h1><p class="lede">${esc(module.question)}</p>
        <dl class="brief-meta"><div><dt>Classification</dt><dd>${esc(m.classification)}</dd></div><div><dt>Objective</dt><dd>${esc(m.objective)}</dd></div><div><dt>Source base</dt><dd>${esc(m.sourceBase)}</dd></div></dl>
        ${reviewNotice}
      </header>
      ${progressPanel()}
      <nav class="section-nav" aria-label="Module ${module.number} sections">${sectionNav}</nav>
      <article>
        <section class="inventory-panel" aria-labelledby="inventory-title" data-track-section="inventory"><h2 id="inventory-title">${esc(m.inventory.heading)}</h2><p>${esc(m.inventory.summary)}</p><ul class="inventory-counts">${counts}</ul><ol class="source-ledger">${sources}</ol>${sectionCheckoff('inventory')}</section>
        <section id="mission-brief" aria-labelledby="mission-title" data-track-section="mission-brief"><p class="eyebrow">Mission brief</p><h2 id="mission-title">${esc(m.missionBrief.heading)}</h2>${labelled('Original source teaching', m.missionBrief.teaching.heading, m.missionBrief.teaching.paragraphs)}<p class="source-stamp">${esc(m.missionBrief.teaching.map)}</p>${labelled('U.S.M.C. Ministries analysis & application', m.missionBrief.analysis.heading, m.missionBrief.analysis.paragraphs)}<p class="end-state"><strong>End state:</strong> ${esc(m.missionBrief.endState)}</p>${sectionCheckoff('mission-brief')}</section>
        <section id="scripture-frame" aria-labelledby="scripture-title" data-track-section="scripture-frame"><p class="eyebrow">Scripture frame</p><h2 id="scripture-title">${esc(m.scripture.heading)}</h2><blockquote><p>${esc(m.scripture.quote.text)}</p><cite>${esc(m.scripture.quote.cite)}</cite></blockquote><p>${esc(m.scripture.intro)}</p><ul class="scripture-list">${scripture}</ul><p class="scripture-links"><a href="https://usmcmin.org/bible.html">Read in the MOOP Bible on usmcmin.org</a></p>${sectionCheckoff('scripture-frame')}</section>
        ${frameworkSection}
        <section id="fair-insight" aria-labelledby="insight-title" data-track-section="fair-insight"><h2 id="insight-title">${esc(m.fairInsight.heading)}</h2>${ps(m.fairInsight.paragraphs)}${sectionCheckoff('fair-insight')}</section>
        <section id="caution-boundary" class="caution" aria-labelledby="caution-title" data-track-section="caution-boundary"><h2 id="caution-title">${esc(m.caution.heading)}</h2>${ps(m.caution.paragraphs)}<ul class="slogan-list">${slogans}</ul><ul>${lis(m.caution.additional)}</ul>${sectionCheckoff('caution-boundary')}</section>
        <section id="self-check" aria-labelledby="check-title" data-track-section="self-check"><h2 id="check-title">${esc(m.selfCheck.heading)}</h2><p>${esc(m.selfCheck.intro)}</p><ul class="check-list">${lis(m.selfCheck.items)}</ul>${sectionCheckoff('self-check')}</section>
        ${pauseSection}
        ${fiveStepsSection}
        <section id="field-action" class="field-action" aria-labelledby="action-title" data-track-section="field-action"><p class="eyebrow">Required field action</p><h2 id="action-title">${esc(m.fieldExercise.heading)}</h2><p>${esc(m.fieldExercise.intro)}</p><ol class="day-grid">${days}</ol><p><strong>Observable finish line:</strong> ${esc(m.fieldExercise.finishLine)}</p>${sectionCheckoff('field-action')}</section>
        <section id="discussion-prompts" aria-labelledby="prompts-title" data-track-section="discussion-prompts"><h2 id="prompts-title">${esc(m.discussionPrompts.heading)}</h2><p>${esc(m.discussionPrompts.intro)}</p><ul>${lis(m.discussionPrompts.items)}</ul>${sectionCheckoff('discussion-prompts')}</section>
        ${conversationSection}
        <section id="support-boundary" class="support-callout" aria-labelledby="support-title" data-track-section="support-boundary"><h2 id="support-title">${esc(m.referral.heading)}</h2><p>${esc(m.referral.lead)}</p><p><strong>${esc(m.referral.distinction)}</strong></p><ul>${referrals}</ul><p>${esc(m.referral.close)}</p>${sectionCheckoff('support-boundary')}</section>
        <section id="verification-notes" aria-labelledby="verification-title" data-track-section="verification-notes"><h2 id="verification-title">${esc(m.verification.heading)}</h2><p>${esc(m.verification.intro)}</p><ul>${lis(m.verification.items)}</ul>${sectionCheckoff('verification-notes')}</section>
        <section id="resources" aria-labelledby="resources-title" data-track-section="resources"><h2 id="resources-title">${esc(m.resources.heading)}</h2><p>${esc(m.resources.intro)}</p>${resourceGroups}${withheldBlock}<div class="resource-actions"><article><h3>${esc(m.resources.notebook.title)}</h3><p>${esc(m.resources.notebook.body)}</p><a href="${esc(m.resources.notebook.href)}" target="_blank" rel="noopener noreferrer">${esc(m.resources.notebook.label)} <span aria-hidden="true">↗</span></a></article><article><h3>${esc(m.resources.journal.heading)}</h3><p>${esc(m.resources.journal.body)}</p><a href="${esc(m.resources.journal.href)}" target="_blank" rel="noopener noreferrer sponsored">${esc(m.resources.journal.label)} <span aria-hidden="true">↗</span></a><p><small>${esc(m.resources.journal.disclosure)}</small></p></article></div>${sectionCheckoff('resources')}</section>
        ${assessmentSection}
        <section id="completion" class="completion" aria-labelledby="completion-title" data-track-section="completion"><h2 id="completion-title">Complete module ${module.number}</h2><p>Mark complete only after the observable field-action finish line. You can change this status later.</p><button type="button" data-complete-module="${module.id}" aria-pressed="false">Mark module ${module.number} complete</button><p data-completion-message="${module.id}" aria-live="polite"></p></section>
      </article>
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
    </main>`
  });
}

module.exports = { renderFieldManual, sectionCheckoff, missionHud };
