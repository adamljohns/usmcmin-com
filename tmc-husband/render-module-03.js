'use strict';

function renderModule03({ module, course, layout, progressPanel, esc, prev, next }) {
  const m = module.fieldManual;
  const ps = (items) => items.map((x) => `<p>${esc(x)}</p>`).join('\n');
  const lis = (items) => items.map((x) => `<li>${esc(x)}</li>`).join('\n');
  const labelled = (label, heading, items) => `<div class="provenance-block"><p class="provenance-label">${esc(label)}</p><h3>${esc(heading)}</h3>${ps(items)}</div>`;

  const sectionNav = m.sectionNav.map((x) => `<a href="${esc(x.href)}">${esc(x.label)}</a>`).join('');
  const counts = m.inventory.counts.map((x) => `<li><strong>${esc(x.value)}</strong><span>${esc(x.label)}</span><small>${esc(x.detail)}</small></li>`).join('');
  const sources = m.sources.map((x) => `<li data-source="${esc(x.slug)}"><p class="eyebrow">${esc(x.lane)}</p><h3>${esc(x.title)}</h3><p>${esc(x.note)}</p></li>`).join('\n');
  const scripture = m.scripture.entries.map((x) => `<li><h3>${esc(x.reference)}</h3><p><strong>Original source teaching:</strong> ${esc(x.teaching)}</p><p><strong>U.S.M.C. Ministries analysis:</strong> ${esc(x.caveat)}</p></li>`).join('\n');
  const principles = m.coreFramework.principles.map((x) => `<li class="principle-card"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.name)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.husbandMove)}</p><p class="guardrail"><strong>Guardrail:</strong> ${esc(x.guardrail)}</p></li>`).join('\n');
  const postures = m.coreFramework.postures.items.map((x) => `<li><h4>${esc(x.name)}</h4><p>${esc(x.looksLike)}</p><p><strong>Cost:</strong> ${esc(x.cost)}</p></li>`).join('\n');
  const slogans = m.caution.slogans.map((x) => `<li><blockquote>${esc(x.line)}</blockquote><p class="source-stamp">${esc(x.stamp)}</p><p>${esc(x.qualification)}</p></li>`).join('\n');
  const steps = m.fiveSteps.steps.map((x) => `<li class="protocol-step"><p class="principle-number">${esc(x.number)}</p><h3>${esc(x.step)}</h3><p><strong>Original source teaching:</strong> ${esc(x.source)}</p><p><strong>U.S.M.C. Ministries analysis &amp; application:</strong> ${esc(x.execution)}</p><p class="guardrail"><strong>Failure mode:</strong> ${esc(x.failureMode)}</p></li>`).join('\n');
  const days = m.fieldExercise.days.map((x) => `<li><p class="eyebrow">${esc(x.day)}</p><h3>${esc(x.title)}</h3><p>${esc(x.body)}</p></li>`).join('\n');
  const guide = m.conversationGuide.steps.map((x) => `<li><strong>${esc(x.label)}:</strong> ${esc(x.body)}</li>`).join('\n');
  const referrals = m.referral.referrals.map((x) => `<li><h3>${esc(x.label)}</h3><p>${esc(x.body)}${x.href ? ` <a href="${esc(x.href)}" target="_blank" rel="noopener noreferrer">${esc(x.linkLabel)} <span aria-hidden="true">↗</span></a>` : ''}</p></li>`).join('\n');

  const resourceGroups = m.resources.groups.map((group) => {
    const artifacts = m.artifacts.filter((x) => x.group === group.key).map((x) => {
      const link = x.state === 'local'
        ? `<a class="artifact-link" href="${esc(x.href)}"${['quiz', 'flashcards'].includes(x.group) ? ' target="_blank" rel="noopener noreferrer"' : ''}>${esc(x.linkLabel || 'Open full-size graphic')}</a>`
        : '<span class="artifact-held">Named for review · not published</span>';
      const image = x.alt ? `<a href="${esc(x.href)}"><img src="${esc(x.href)}" alt="${esc(x.alt)}" loading="lazy"></a>` : '';
      return `<article class="artifact-card" data-artifact="${esc(x.slug)}" data-artifact-state="${esc(x.state)}"><p class="eyebrow">${esc(x.kind || (x.state === 'withheld' ? 'Held media' : group.heading))}</p><h4>${esc(x.title)}</h4>${link}${image}<p>${esc(x.summary)}</p></article>`;
    }).join('\n');
    return `<section class="resource-group" aria-labelledby="resource-${esc(group.key)}"><h3 id="resource-${esc(group.key)}">${esc(group.heading)} <span>${esc(group.count)}</span></h3><p>${esc(group.note)}</p><div class="artifact-grid">${artifacts}</div></section>`;
  }).join('\n');

  return layout({
    title: `Module ${module.number}: ${module.title}`,
    description: module.question,
    page: module.id,
    noindex: true,
    body: `<div class="prototype-banner" role="status"><strong>Local prototype.</strong> ${esc(course.status)}</div>
    <main id="main-content" class="lesson field-manual">
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
      <header class="lesson-header field-manual-header">
        <p class="eyebrow">Module ${module.number} of 7 · ${esc(m.reviewStatus)}</p>
        <h1>${esc(module.title)}</h1><p class="lede">${esc(module.question)}</p>
        <dl class="brief-meta"><div><dt>Classification</dt><dd>${esc(m.classification)}</dd></div><div><dt>Objective</dt><dd>${esc(m.objective)}</dd></div><div><dt>Source base</dt><dd>${esc(m.sourceBase)}</dd></div></dl>
        <p class="review-notice">${esc(course.status)}</p>
      </header>
      ${progressPanel()}
      <nav class="section-nav" aria-label="Module 3 sections">${sectionNav}</nav>
      <article>
        <section class="inventory-panel" aria-labelledby="inventory-title"><h2 id="inventory-title">${esc(m.inventory.heading)}</h2><p>${esc(m.inventory.summary)}</p><ul class="inventory-counts">${counts}</ul><ol class="source-ledger">${sources}</ol></section>
        <section id="mission-brief" aria-labelledby="mission-title"><p class="eyebrow">Mission brief</p><h2 id="mission-title">${esc(m.missionBrief.heading)}</h2>${labelled('Original source teaching', m.missionBrief.teaching.heading, m.missionBrief.teaching.paragraphs)}<p class="source-stamp">${esc(m.missionBrief.teaching.map)}</p>${labelled('U.S.M.C. Ministries analysis & application', m.missionBrief.analysis.heading, m.missionBrief.analysis.paragraphs)}<p class="end-state"><strong>End state:</strong> ${esc(m.missionBrief.endState)}</p></section>
        <section id="scripture-frame" aria-labelledby="scripture-title"><p class="eyebrow">Scripture frame</p><h2 id="scripture-title">${esc(m.scripture.heading)}</h2><blockquote><p>${esc(m.scripture.quote.text)}</p><cite>${esc(m.scripture.quote.cite)}</cite></blockquote><p>${esc(m.scripture.intro)}</p><ul class="scripture-list">${scripture}</ul></section>
        <section id="core-framework" aria-labelledby="framework-title"><p class="eyebrow">Core conflict framework</p><h2 id="framework-title">${esc(m.coreFramework.heading)}</h2><p>${esc(m.coreFramework.lead)}</p><ol class="principle-grid">${principles}</ol><h3>${esc(m.coreFramework.postures.heading)}</h3><p>${esc(m.coreFramework.postures.note)}</p><ul class="posture-grid">${postures}</ul><div class="externalise-panel"><h3>${esc(m.coreFramework.externalise.heading)}</h3><p><strong>Original source teaching:</strong> ${esc(m.coreFramework.externalise.teaching)}</p><p><strong>U.S.M.C. Ministries analysis:</strong> ${esc(m.coreFramework.externalise.analysis)}</p><p class="guardrail"><strong>Critical guardrail:</strong> ${esc(m.coreFramework.externalise.criticalNote)}</p></div></section>
        <section id="fair-insight" aria-labelledby="insight-title"><h2 id="insight-title">${esc(m.fairInsight.heading)}</h2>${ps(m.fairInsight.paragraphs)}</section>
        <section id="caution-boundary" class="caution" aria-labelledby="caution-title"><h2 id="caution-title">${esc(m.caution.heading)}</h2>${ps(m.caution.paragraphs)}<ul class="slogan-list">${slogans}</ul><ul>${lis(m.caution.additional)}</ul></section>
        <section id="self-check" aria-labelledby="check-title"><h2 id="check-title">${esc(m.selfCheck.heading)}</h2><p>${esc(m.selfCheck.intro)}</p><ul class="check-list">${lis(m.selfCheck.items)}</ul></section>
        <section id="pause-protocol" aria-labelledby="pause-title"><p class="eyebrow">Pause and return</p><h2 id="pause-title">${esc(m.pauseProtocol.heading)}</h2>${labelled('Original source teaching', m.pauseProtocol.teaching.heading, m.pauseProtocol.teaching.paragraphs)}<div class="provenance-block"><p class="provenance-label">U.S.M.C. Ministries analysis &amp; application</p><h3>${esc(m.pauseProtocol.analysis.heading)}</h3><p>${esc(m.pauseProtocol.analysis.lead)}</p><ol>${lis(m.pauseProtocol.analysis.rules)}</ol><h4>This is not a pause</h4><ul>${lis(m.pauseProtocol.analysis.notAPause)}</ul></div><p class="safety-line">${esc(m.pauseProtocol.safetyLine)}</p></section>
        <section id="five-steps" aria-labelledby="steps-title"><p class="eyebrow">Five-step protocol</p><h2 id="steps-title">${esc(m.fiveSteps.heading)}</h2><p>${esc(m.fiveSteps.intro)}</p><h3>Preconditions</h3><ul>${lis(m.fiveSteps.preconditions)}</ul><ol class="protocol-list">${steps}</ol><p>${esc(m.fiveSteps.close)}</p></section>
        <section id="field-action" class="field-action" aria-labelledby="action-title"><p class="eyebrow">Required field action</p><h2 id="action-title">${esc(m.fieldExercise.heading)}</h2><p>${esc(m.fieldExercise.intro)}</p><ol class="day-grid">${days}</ol><p><strong>Observable finish line:</strong> ${esc(m.fieldExercise.finishLine)}</p></section>
        <section id="discussion-prompts" aria-labelledby="prompts-title"><h2 id="prompts-title">${esc(m.discussionPrompts.heading)}</h2><p>${esc(m.discussionPrompts.intro)}</p><ul>${lis(m.discussionPrompts.items)}</ul></section>
        <section id="conversation-guide" aria-labelledby="conversation-title"><h2 id="conversation-title">${esc(m.conversationGuide.heading)}</h2><p>${esc(m.conversationGuide.intro)}</p><ol>${guide}</ol><p class="guardrail">${esc(m.conversationGuide.pauseSignal)}</p></section>
        <section id="support-boundary" class="support-callout" aria-labelledby="support-title"><h2 id="support-title">${esc(m.referral.heading)}</h2><p>${esc(m.referral.lead)}</p><p><strong>${esc(m.referral.distinction)}</strong></p><ul>${referrals}</ul><p>${esc(m.referral.close)}</p></section>
        <section id="verification-notes" aria-labelledby="verification-title"><h2 id="verification-title">${esc(m.verification.heading)}</h2><p>${esc(m.verification.intro)}</p><ul>${lis(m.verification.items)}</ul></section>
        <section id="resources" aria-labelledby="resources-title"><h2 id="resources-title">${esc(m.resources.heading)}</h2><p>${esc(m.resources.intro)}</p>${resourceGroups}<aside class="withheld-notice"><h3>Publication gate for six held artifacts</h3><p>${esc(m.resources.withheldNotice)}</p></aside><div class="resource-actions"><article><h3>${esc(m.resources.notebook.title)}</h3><p>${esc(m.resources.notebook.body)}</p><a href="${esc(m.resources.notebook.href)}" target="_blank" rel="noopener noreferrer">${esc(m.resources.notebook.label)} <span aria-hidden="true">↗</span></a></article><article><h3>${esc(m.resources.journal.heading)}</h3><p>${esc(m.resources.journal.body)}</p><a href="${esc(m.resources.journal.href)}" target="_blank" rel="noopener noreferrer sponsored">${esc(m.resources.journal.label)} <span aria-hidden="true">↗</span></a><p><small>${esc(m.resources.journal.disclosure)}</small></p></article></div></section>
        <section id="completion" class="completion" aria-labelledby="completion-title"><h2 id="completion-title">Complete module ${module.number}</h2><p>Mark complete only after the observable finish line. You can change this status later.</p><button type="button" data-complete-module="${module.id}" aria-pressed="false">Mark module ${module.number} complete</button><p data-completion-message="${module.id}" aria-live="polite"></p></section>
      </article>
      <nav class="module-nav" aria-label="Previous and next modules">${prev}${next}</nav>
    </main>`
  });
}

module.exports = { renderModule03 };
