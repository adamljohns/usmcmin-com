'use strict';

/* export-course.js — hand the course to the Python print builders.
 *
 *   node tmc-father/print/export-course.js
 *
 * The course content lives in JS (course.v1.js + module-0N.field-manual.js) and
 * the drill payloads in tmc-father/drills/*.json. The printables are drawn with
 * reportlab in Python. Rather than duplicate any of that content, this writes a
 * single export the builders read, so the PDFs can never drift from the site:
 * fix a typo in the field manual, rebuild, and every sheet follows.
 *
 * Writes tmc-father/print/course-export.json (derived — do not hand-edit).
 */

const fs = require('node:fs');
const path = require('node:path');
const { course } = require('../course.v1.js');

const HERE = __dirname;
const TMC = path.resolve(HERE, '..');

function drillsFor(moduleId) {
  const file = path.join(TMC, 'drills', `${moduleId}.json`);
  if (!fs.existsSync(file)) return { flashcards: 0, quiz: [] };
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  const cards = data.flashcards || data.cards || [];
  const questions = data.quiz || data.questions || [];
  return {
    flashcards: cards.length,
    // The prompt, how many options, and the answer — the insert asks the reader
    // to write from memory, then prints the key on its own page at the back so
    // he can mark himself without leaving the sheet.
    quiz: questions.map((q, i) => {
      const opts = q.answerOptions || q.options || [];
      const right = opts.find((o) => o && o.isCorrect === true);
      return {
        number: i + 1,
        question: q.question || q.prompt || '',
        options: opts.length,
        answer: (right && (right.text || right.answer)) || '',
        rationale: (right && right.rationale) || ''
      };
    })
  };
}

const modules = course.modules.map((module) => {
  const fm = module.fieldManual ? require(`../module-${String(module.number).padStart(2, '0')}.field-manual.js`).fieldManual : null;
  const artifacts = (fm && fm.artifacts) || [];
  const byGroup = (group) => artifacts
    .filter((a) => a.group === group)
    .map((a) => ({
      slug: a.slug,
      title: a.title,
      summary: a.summary || '',
      href: a.href,
      kind: a.kind || '',
      // The file basename is what the report-PDF builder keys on.
      file: a.href ? a.href.split('/').pop() : ''
    }));

  return {
    id: module.id,
    number: module.number,
    title: module.title,
    question: module.question,
    fieldActionSummary: module.fieldActionSummary || '',
    timeEstimate: (fm && fm.timeEstimate) || module.timeEstimate || '',
    finishLineHero: (fm && fm.finishLineHero) || '',
    opening: (fm && fm.opening) || module.missionBrief || [],
    scripture: (fm && fm.scripture) || module.scripture || [],
    tasks: (fm && fm.tasks) || [],
    selfCheck: (fm && fm.selfCheck) || module.selfCheck || [],
    fieldAction: (fm && fm.fieldAction) || module.fieldAction || {},
    conversation: (fm && fm.conversation) || module.conversation || [],
    caution: (fm && fm.caution) || module.caution || '',
    support: (fm && fm.support) || module.support || '',
    media: {
      video: byGroup('video'),
      audio: byGroup('audio'),
      slides: byGroup('slides'),
      infographics: byGroup('infographics'),
      reports: byGroup('reports')
    },
    drills: drillsFor(module.id)
  };
});

const out = {
  generatedFrom: 'tmc-father/course.v1.js + module-*.field-manual.js + drills/*.json',
  title: course.title,
  subtitle: course.subtitle,
  promise: course.promise,
  howItWorks: course.howItWorks || [],
  modules
};

const target = path.join(HERE, 'course-export.json');
fs.writeFileSync(target, JSON.stringify(out, null, 2));
console.log(`Wrote ${path.relative(process.cwd(), target)} — ${modules.length} modules, ` +
  `${modules.reduce((n, m) => n + m.tasks.length, 0)} tasks, ` +
  `${modules.reduce((n, m) => n + m.media.reports.length, 0)} reports, ` +
  `${modules.reduce((n, m) => n + m.drills.quiz.length, 0)} quiz questions.`);
