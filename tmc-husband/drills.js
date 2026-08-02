'use strict';

/* Flashcard + quiz decks for each module.
 *
 * Source of truth is `drills/<moduleId>.json`, extracted from the Notebook by
 * Gemini exports with `extract-drills.js` so the cards render natively in the
 * course (on-brand, tracked, offline) instead of loading a 1.3 MB Google iframe.
 * A module with no JSON simply renders no drill sections.
 */

const fs = require('node:fs');
const path = require('node:path');

const DRILL_DIR = path.join(__dirname, 'drills');

function loadDrills(moduleId) {
  const file = path.join(DRILL_DIR, `${moduleId}.json`);
  if (!fs.existsSync(file)) return { flashcards: [], quiz: [] };
  let parsed;
  try {
    parsed = JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    throw new Error(`Unreadable drill deck ${file}: ${error.message}`);
  }
  const flashcards = Array.isArray(parsed.flashcards)
    ? parsed.flashcards.filter((card) => card && card.f && card.b).map((card) => ({ f: String(card.f), b: String(card.b) }))
    : [];
  const quiz = Array.isArray(parsed.quiz)
    ? parsed.quiz.filter((item) => item && item.question && Array.isArray(item.answerOptions) && item.answerOptions.some((o) => o.isCorrect))
      .map((item) => ({
        question: String(item.question),
        answerOptions: item.answerOptions.map((option) => ({
          text: String(option.text),
          isCorrect: option.isCorrect === true,
          rationale: option.rationale ? String(option.rationale) : ''
        }))
      }))
    : [];
  return { flashcards, quiz };
}

// JSON safe to drop inside a <script type="application/json"> block.
function jsonBlock(value) {
  return JSON.stringify(value).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026');
}

module.exports = { loadDrills, jsonBlock, DRILL_DIR };
