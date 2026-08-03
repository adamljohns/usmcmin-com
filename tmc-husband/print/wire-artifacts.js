'use strict';

/* wire-artifacts.js — one-time wiring of the Notebook by Gemini artifacts for
 * modules 3-7 into their field manuals.
 *
 *   node tmc-husband/print/wire-artifacts.js
 *
 * Modules 4-7 shipped with `artifacts: []` and module 3 still listed its audio
 * and video as `withheld`, so 44 files that were already sitting in the R2
 * bucket were referenced by no page at all. This writes the registry entries,
 * matching the shape modules 1-2 already use, then the normal
 * `node tmc-husband/generate.js` picks them up.
 *
 * Titles come from the artifact filenames (which are Notebook's own titles).
 * Summaries are written to say plainly what the piece is and where it needs
 * reading against the module's caution — the same editorial line modules 1-3
 * already take. Infographic alt text is deliberately structural: these graphics
 * are queued for regeneration (they carry garbled AI-set text), and richer alt
 * text belongs with the replacements.
 *
 * Idempotent: rerunning replaces the artifacts array wholesale.
 */

const fs = require('node:fs');
const path = require('node:path');

const TMC = path.resolve(__dirname, '..');
const base = (n, group, file) => `../assets/media/tmc-husband/m0${n}/${group}/${file}`;

// group → the label a learner taps.
const LINK_LABEL = {
  slides: 'Open slide deck',
  reports: 'Read the report',
  quiz: 'Open the quiz',
  flashcards: 'Open the flashcards'
};

function video(n, file, title, summary) {
  return { slug: `video-${file.replace(/\.mp4$/, '')}`, state: 'local', group: 'video', kind: 'Video', title, summary, href: base(n, 'video', file), mediaType: 'video' };
}
function audio(n, file, title, summary) {
  return { slug: `audio-${file.replace(/\.mp3$/, '')}`, state: 'local', group: 'audio', kind: 'Audio', title, summary, href: base(n, 'audio', file), mediaType: 'audio' };
}
function slides(n, file, title, summary) {
  return { slug: `slides-${file.replace(/\.pdf$/, '')}`, state: 'local', group: 'slides', kind: 'PDF', title, summary, href: base(n, 'slides', file), linkLabel: LINK_LABEL.slides };
}
function graphic(n, file, title, summary, alt) {
  return { slug: `infographic-${file.replace(/\.png$/, '')}`, state: 'local', group: 'infographics', title, summary, href: base(n, 'infographics', file), alt };
}
function report(n, file, title, summary) {
  // The site links the PDF; the Markdown stays as source (see build_reports.py).
  return { slug: `report-${file.replace(/\.md$/, '')}`, state: 'local', group: 'reports', title, summary, href: base(n, 'reports', file.replace(/\.md$/, '.pdf')), linkLabel: LINK_LABEL.reports };
}
function drills(n) {
  return [
    { slug: 'quiz-marriage-quiz', state: 'local', group: 'quiz', title: 'Marriage Quiz', summary: 'Knowledge check over this module.', href: base(n, 'quiz', 'marriage-quiz.html'), linkLabel: LINK_LABEL.quiz },
    { slug: 'flashcards-marriage-flashcards', state: 'local', group: 'flashcards', title: 'Marriage Flashcards', summary: 'Flashcard drill over this module.', href: base(n, 'flashcards', 'marriage-flashcards.html'), linkLabel: LINK_LABEL.flashcards }
  ];
}

const G = (title) => `Illustrated multi-panel field guide titled ${title}.`;

const REGISTRY = {
  3: [
    video(3, 'resolving-conflict.mp4', 'Resolving Conflict', 'Session video on working a disagreement without making the marriage the battlefield.'),
    video(3, 'navigating-conflict.mp4', 'Navigating Conflict', 'How couples move from position-trading to shared problem-solving.'),
    video(3, 'how-to-externalize-marriage-conflict.mp4', 'How to Externalise a Conflict', 'Putting the problem on the table instead of across from you.'),
    audio(3, 'why-your-partner-is-not-the-problem.mp3', 'Why Your Partner Is Not the Problem', 'Deep-dive audio on separating the person from the problem.'),
    audio(3, 'when-good-marriage-advice-goes-wrong.mp3', 'When Good Marriage Advice Goes Wrong', 'Critical audio on where conflict advice misfires. Read against the module caution.'),
    audio(3, 'when-marriage-tools-become-dangerous-weapons.mp3', 'When Marriage Tools Become Dangerous Weapons', 'Safety inversion: how a fair-fighting rule becomes a control tactic.'),
    slides(3, 'the-marriage-blueprint.pdf', 'The Marriage Blueprint', 'Session overview deck.'),
    slides(3, 'marital-conflict-blueprint.pdf', 'Marital Conflict Blueprint', 'Four principles through five steps.'),
    slides(3, 'engineering-us.pdf', 'Engineering Us', 'Systems view of marriage maintenance.'),
    graphic(3, 'marriage-conflict-resolution-field-guide.png', 'Marriage Conflict Resolution Field Guide', 'Navigating the Waves Together — includes a red-flag panel.', 'Illustrated field guide titled Navigating the Waves Together with panels on teamwork, appreciation, and the five-step protocol.'),
    graphic(3, 'marriage-conflict-and-teamwork-guide.png', 'Marriage Conflict and Teamwork Guide', 'Navigating the Storm — includes a safety overlay.', 'Illustrated guide titled Navigating the Storm with a conflict toolkit and a seven-day action plan.'),
    graphic(3, 'marriage-teamwork-guide.png', 'Marriage Teamwork Guide', 'Five cards on appreciation, differences, timing, and support.', 'Illustrated guide titled From Conflict to Connection showing five teamwork cards.'),
    report(3, 'conflict-resolution-and-partnership-briefing.md', 'Conflict Resolution and Partnership', 'Executive briefing — best starting point.'),
    report(3, 'from-clashing-oars-to-gliding-boats.md', 'From Clashing Oars to Gliding Boats', 'Systems-flavoured treatment of the rowing metaphor.'),
    report(3, 'why-your-biggest-disagreements-secret-weapon.md', 'Why Your Biggest Disagreements Might Be Your Secret Weapon', 'Popular-article register — the headline overclaims; read against the caution.'),
    ...drills(3)
  ],
  4: [
    video(4, 'healing-hurt-and-forgiveness.mp4', 'Healing Hurt and Forgiveness', 'Session video on naming a hurt and making a specific repair.'),
    video(4, 'navigating-marital-conflict.mp4', 'Navigating Marital Conflict', 'Where unresolved anger goes when nobody addresses it.'),
    audio(4, 'the-danger-of-forgiving-rhinos-and-hedgehogs.mp3', 'The Danger of Forgiving: Rhinos and Hedgehogs', 'Deep-dive audio on the two anger styles and where the model stops applying.'),
    audio(4, 'when-marriage-advice-becomes-ammunition.mp3', 'When Marriage Advice Becomes Ammunition', 'Safety inversion: how repair language gets weaponised. Read against the module caution.'),
    slides(4, 'marital-repair-blueprint.pdf', 'Marital Repair Blueprint', 'The three-step repair, start to finish.'),
    slides(4, 'the-topography-of-repair.pdf', 'The Topography of Repair', 'Mapping how deep a given hurt actually runs.'),
    graphic(4, 'marriage-healing-and-forgiveness-guide.png', 'The Path to Healing', 'Anger as signal, the three-step repair, and a red-flag panel on when to seek help.', 'Illustrated field guide titled The Path to Healing: Navigating Hurt and Forgiveness in Marriage, with panels on anger as an alarm, the rhino and hedgehog styles, a three-step repair, a safety filter, and a seven-day plan.'),
    graphic(4, 'marriage-conflict-and-forgiveness-guide.png', 'Marriage Conflict and Forgiveness Guide', 'Companion guide on repair sequence and boundaries.', G('Marriage Conflict and Forgiveness Guide')),
    report(4, 'episode-4-the-marriage-course-healing-hurt-and-anger.md', 'Healing Hurt and Anger', 'Executive briefing — best starting point for this module.'),
    report(4, 'beyond-the-apple-throw-navigating-anger-and-healing-in-marriage.md', 'Beyond the Apple Throw', 'Longer treatment of anger, repair, and what forgiveness does not mean.'),
    report(4, 'rhinos-hedgehogs-and-the-buried-alive-rule-5-surprising-lessons-for-a-healthier-marriage.md', 'Rhinos, Hedgehogs, and the Buried-Alive Rule', 'Popular-article register — use as a prompt, not as proof.'),
    ...drills(4)
  ],
  5: [
    video(5, 'family-impact-past-and-present.mp4', 'The Impact of Family: Past and Present', 'Session video on the family you brought into the marriage.'),
    video(5, 'family-dynamics-in-marriage.mp4', 'Family Dynamics in Marriage', 'How inherited patterns show up in a marriage nobody planned them for.'),
    audio(5, 'trauma-informed-forgiveness-and-cultural-marriage-boundaries.mp3', 'Trauma-Informed Forgiveness and Boundaries', 'Deep-dive audio on forgiveness that does not require unsafe contact.'),
    audio(5, 'why-ai-flagged-the-marriage-course-trauma.mp3', 'Where This Session Needs Care', 'Critical audio on the limits of a formation course around trauma. Read against the module caution.'),
    slides(5, 'navigating-family-legacies.pdf', 'Navigating Family Legacies', 'Leaving, cleaving, and the new centre of gravity.'),
    slides(5, 'the-marital-blueprint.pdf', 'The Marital Blueprint', 'Session overview deck.'),
    graphic(5, 'navigating-the-family-tree-guide.png', 'Navigating the Family Tree', 'Leaving as an emotional shift, inherited conflict styles, and a critical panel on when advice is not enough.', 'Illustrated field guide titled Navigating the Family Tree: A Field Guide for Married Couples, with panels on creating a new centre of gravity, inherited conflict styles, evaluating your roots, a healing action plan, and a red-flag note to seek professional help.'),
    graphic(5, 'navigating-family-patterns-in-marriage.png', 'Navigating Family Patterns in Marriage', 'Companion guide on inherited patterns and boundaries.', G('Navigating Family Patterns in Marriage')),
    report(5, 'episode-5-the-marriage-course-the-impact-of-family-past-and-present.md', 'The Impact of Family: Past and Present', 'Executive briefing — best starting point for this module.'),
    report(5, 'the-ghost-at-the-dinner-table-navigating-family-baggage-and-in-law-dynamics.md', 'The Ghost at the Dinner Table', 'Longer treatment of in-law dynamics and inherited expectations.'),
    report(5, 'why-your-in-laws-are-secretly-living-in-your-marriage-5-radical-shifts-for-every-couple.md', 'Why Your In-Laws Are Living in Your Marriage', 'Popular-article register — the headline overclaims; use as a prompt.'),
    ...drills(5)
  ],
  6: [
    video(6, 'keeping-the-spark-alive.mp4', 'Keeping the Spark Alive', 'Session video on friendship, attention, and desire over years.'),
    video(6, 'the-engine-of-intimacy.mp4', 'The Engine of Intimacy', 'Why emotional connection and physical intimacy feed each other.'),
    video(6, 'restoring-the-spark.mp4', 'Restoring the Spark', 'What to do when the connection has gone quiet.'),
    video(6, 'the-7-day-intimacy-reset.mp4', 'The Seven-Day Intimacy Reset', 'A week of small, non-pressuring moves.'),
    audio(6, 'the-best-sex-starts-at-breakfast.mp3', 'It Starts Long Before the Bedroom', 'Deep-dive audio on intimacy as the whole day, not the last hour of it.'),
    audio(6, 'why-responsive-desire-fuels-the-marital-spark.mp3', 'Responsive Desire', 'Deep-dive audio on desire that answers rather than initiates.'),
    audio(6, 'modernizing-the-psychology-of-marital-intimacy.mp3', 'Modernising the Psychology of Intimacy', 'Critical audio on where the session dates. Read against the module caution.'),
    slides(6, 'the-intimacy-blueprint.pdf', 'The Intimacy Blueprint', 'Session overview deck.'),
    slides(6, 'the-intimacy-blueprint-2.pdf', 'The Intimacy Blueprint (Part Two)', 'Second half of the blueprint deck.'),
    slides(6, 'relational-circuitry.pdf', 'Relational Circuitry', 'How connection, safety, and desire wire together.'),
    graphic(6, 'the-spark-and-the-flame.png', 'The Spark and the Flame', 'Friendship, attention, and desire over a long marriage.', G('The Spark and the Flame')),
    graphic(6, 'keeping-the-spark-alive.png', 'Keeping the Spark Alive', 'Habits that protect intimacy in an ordinary week.', G('Keeping the Spark Alive')),
    graphic(6, 'five-secrets-of-sexual-intimacy.png', 'Five Secrets of Sexual Intimacy', 'Five practices, with a consent and safety panel.', G('Five Secrets of Sexual Intimacy')),
    report(6, 'briefing-document-the-marriage-course-episode-6-sexual-intimacy.md', 'Sexual Intimacy: Session Briefing', 'Executive briefing — best starting point for this module.'),
    report(6, 'beyond-the-bedroom-reclaiming-the-spark-in-your-marriage.md', 'Beyond the Bedroom', 'Longer treatment of intimacy as friendship, safety, and attention.'),
    report(6, 'good-luck-mr-gorsky-5-surprising-truths-about-keeping-the-spark-alive.md', 'Five Surprising Truths About Keeping the Spark Alive', 'Popular-article register — use as a prompt, not as proof.'),
    ...drills(6)
  ],
  7: [
    video(7, 'love-in-action.mp4', 'Love in Action', 'Session video on love as something you do on purpose.'),
    video(7, '5-languages-of-marriage.mp4', 'The Five Languages of Marriage', 'Giving love in the currency your wife actually receives.'),
    audio(7, 'giving-love-in-your-partner-s-currency.mp3', 'Giving Love in Her Currency', 'Deep-dive audio on paying attention to what actually lands.'),
    audio(7, 'why-love-languages-need-emotional-safety.mp3', 'Why Love Languages Need Safety First', 'Critical audio: the framework assumes a safe marriage. Read against the module caution.'),
    slides(7, 'the-love-language-manual.pdf', 'The Love Language Manual', 'The five languages, applied.'),
    slides(7, 'marriage-field-manual.pdf', 'Marriage Field Manual', 'Session overview deck.'),
    slides(7, 'marriage-systems-manual.pdf', 'Marriage Systems Manual', 'Keeping the habits running after the course ends.'),
    graphic(7, 'love-in-action-relationship-guide.png', 'Love in Action Relationship Guide', 'The five languages with a practice plan.', G('Love in Action Relationship Guide')),
    graphic(7, 'marriage-maintenance-storyboard-field-guide.png', 'Marriage Maintenance Storyboard', 'The whole course as one maintenance rhythm.', G('Marriage Maintenance Storyboard Field Guide')),
    report(7, 'love-in-action-insights-from-the-marriage-course-episode-7.md', 'Love in Action: Session Insights', 'Executive briefing — best starting point for this module.'),
    report(7, 'the-architecture-of-intimacy-why-lasting-love-is-a-learned-language-not-a-reflex.md', 'The Architecture of Intimacy', 'Longer treatment of love as a learned practice rather than a reflex.'),
    report(7, 'love-in-action-beyond-the-spontaneous-myth-and-into-the-five-languages.md', 'Beyond the Spontaneous Myth', 'Popular-article register — use as a prompt, not as proof.'),
    ...drills(7)
  ]
};

function render(entries) {
  const lines = entries.map((entry) => {
    const parts = Object.entries(entry).map(([k, v]) => `${k}: ${JSON.stringify(v)}`);
    return `    { ${parts.join(', ')} }`;
  });
  return `  artifacts: [\n${lines.join(',\n')}\n  ]`;
}

let total = 0;
for (const [number, entries] of Object.entries(REGISTRY)) {
  const file = path.join(TMC, `module-0${number}.field-manual.js`);
  let source = fs.readFileSync(file, 'utf8');
  const start = source.indexOf('  artifacts: [');
  if (start === -1) throw new Error(`no artifacts array in ${file}`);
  // Find the matching close bracket for this array.
  let depth = 0;
  let end = -1;
  for (let i = source.indexOf('[', start); i < source.length; i += 1) {
    if (source[i] === '[') depth += 1;
    else if (source[i] === ']') {
      depth -= 1;
      if (depth === 0) { end = i + 1; break; }
    }
  }
  source = source.slice(0, start) + render(entries) + source.slice(end);
  fs.writeFileSync(file, source);
  total += entries.length;
  console.log(`m0${number}: ${entries.length} artifacts wired`);
}
console.log(`${total} artifacts written across ${Object.keys(REGISTRY).length} modules.`);
