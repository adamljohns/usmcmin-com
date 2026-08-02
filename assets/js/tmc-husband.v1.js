(function (root, factory) {
  'use strict';
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root) root.TmcHusbandProgress = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const STORAGE_KEY = 'usmcmin:tmc-husband:v1:progress';
  const TIME_KEY = 'usmcmin:tmc-husband:v1:time';
  const SCHEMA_VERSION = 1;
  const MODULE_KEYS = Object.freeze(['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07']);

  function createDefaultState() {
    return {
      schemaVersion: SCHEMA_VERSION,
      modules: Object.fromEntries(MODULE_KEYS.map((key) => [key, false])),
      lastModule: null
    };
  }

  function saveState(storage, state) {
    const normalized = normalizeState(state);
    storage.setItem(STORAGE_KEY, JSON.stringify(normalized));
    return normalized;
  }

  function normalizeState(value) {
    if (!value || Array.isArray(value) || typeof value !== 'object' || value.schemaVersion !== SCHEMA_VERSION) {
      return createDefaultState();
    }
    const state = createDefaultState();
    if (value.modules && !Array.isArray(value.modules) && typeof value.modules === 'object') {
      for (const key of MODULE_KEYS) state.modules[key] = value.modules[key] === true;
    }
    state.lastModule = MODULE_KEYS.includes(value.lastModule) ? value.lastModule : null;
    return state;
  }

  function loadState(storage) {
    let parsed;
    try {
      const raw = storage.getItem(STORAGE_KEY);
      parsed = raw === null ? createDefaultState() : JSON.parse(raw);
    } catch (_error) {
      parsed = createDefaultState();
    }
    const normalized = normalizeState(parsed);
    try { storage.setItem(STORAGE_KEY, JSON.stringify(normalized)); } catch (_error) { /* local-only UI still works in memory */ }
    return normalized;
  }

  function deriveProgress(state) {
    const safe = normalizeState(state);
    const completed = MODULE_KEYS.filter((key) => safe.modules[key]).length;
    return {
      completed,
      total: MODULE_KEYS.length,
      percent: Math.round((completed / MODULE_KEYS.length) * 100),
      isComplete: completed === MODULE_KEYS.length
    };
  }

  // Rank ladder — dignified Captain voice, no hype. Indexed by modules completed (0–7).
  const RANKS = Object.freeze([
    { rank: 'Ashore', milestone: 'Not yet under way. Begin Module 1 when you are ready.' },
    { rank: 'Deckhand', milestone: 'First action shipped. The hardest step is behind you.' },
    { rank: 'Mate', milestone: 'Two modules down. A rhythm is forming.' },
    { rank: 'Bosun', milestone: 'Halfway to the charter. Steady steaming.' },
    { rank: 'Watch Officer', milestone: 'Four modules in. The habits are taking hold.' },
    { rank: 'First Officer', milestone: 'Five complete. The commission is in sight.' },
    { rank: 'Executive Officer', milestone: 'One module from commissioned. Finish the tour.' },
    { rank: 'Captain of the Home', milestone: 'All seven shipped. You have completed the course — commissioned.' }
  ]);

  function deriveRank(completed) {
    const index = Math.max(0, Math.min(RANKS.length - 1, Number(completed) || 0));
    return Object.assign({ index }, RANKS[index]);
  }

  // Badge id -> earned condition, given progress + state. 9 badges total.
  function deriveBadges(state) {
    const safe = normalizeState(state);
    const completed = MODULE_KEYS.filter((key) => safe.modules[key]).length;
    const earned = {
      first: completed >= 1,
      commissioned: completed === MODULE_KEYS.length
    };
    for (const key of MODULE_KEYS) earned[key] = safe.modules[key] === true;
    return earned;
  }

  function toggleModule(storage, moduleId) {
    if (!MODULE_KEYS.includes(moduleId)) throw new Error(`Unknown module: ${moduleId}`);
    const state = loadState(storage);
    state.modules[moduleId] = !state.modules[moduleId];
    state.lastModule = moduleId;
    return saveState(storage, state);
  }

  function resetState(storage) {
    return saveState(storage, createDefaultState());
  }

  function getBrowserStorage() {
    try {
      const storage = window.localStorage;
      const probe = `${STORAGE_KEY}:probe`;
      storage.setItem(probe, '1');
      storage.removeItem(probe);
      return storage;
    } catch (_error) {
      const memory = new Map();
      return {
        getItem: (key) => memory.has(key) ? memory.get(key) : null,
        setItem: (key, value) => memory.set(key, String(value)),
        removeItem: (key) => memory.delete(key)
      };
    }
  }

  /* ── Time on task ──────────────────────────────────────────────────────────
   * Wall-clock seconds actually spent with a module page open and the reader
   * awake — not a countdown, and not a guess. Persisted per module; the course
   * total is the sum. Ticks only while the tab is visible and the reader has
   * interacted within IDLE_LIMIT_MS, so a page left open overnight does not
   * inflate the record.
   */
  const IDLE_LIMIT_MS = 3 * 60 * 1000;

  function loadTime(storage) {
    let parsed = {};
    try {
      const raw = storage.getItem(TIME_KEY);
      parsed = raw ? JSON.parse(raw) : {};
    } catch (_error) {
      parsed = {};
    }
    const out = {};
    for (const key of MODULE_KEYS) {
      const value = parsed && typeof parsed === 'object' ? Number(parsed[key]) : 0;
      out[key] = Number.isFinite(value) && value > 0 ? Math.floor(value) : 0;
    }
    return out;
  }

  function saveTime(storage, table) {
    try { storage.setItem(TIME_KEY, JSON.stringify(table)); } catch (_error) { /* memory fallback */ }
    return table;
  }

  function totalTime(table) {
    return MODULE_KEYS.reduce((sum, key) => sum + (Number(table[key]) || 0), 0);
  }

  // 0:04:12 under an hour, 1:22:05 over. Hours, minutes, and seconds — always.
  function formatClock(seconds) {
    const total = Math.max(0, Math.floor(Number(seconds) || 0));
    const h = Math.floor(total / 3600);
    const m = Math.floor((total % 3600) / 60);
    const s = total % 60;
    return `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }

  // "2 h 14 min" / "46 min" / "38 sec" — for prose lines, not the HUD readout.
  function formatDuration(seconds) {
    const total = Math.max(0, Math.floor(Number(seconds) || 0));
    if (total < 60) return `${total} sec`;
    const h = Math.floor(total / 3600);
    const m = Math.floor((total % 3600) / 60);
    if (!h) return `${m} min`;
    return m ? `${h} h ${m} min` : `${h} h`;
  }

  function updateDocument(state) {
    const progress = deriveProgress(state);
    document.querySelectorAll('[data-progress-summary]').forEach((node) => {
      node.textContent = `${progress.completed} of ${progress.total} modules complete (${progress.percent}%).`;
    });
    document.querySelectorAll('[data-progress-short]').forEach((node) => {
      node.textContent = `${progress.completed}/${progress.total}`;
    });
    document.querySelectorAll('[role="progressbar"]').forEach((node) => {
      node.setAttribute('aria-valuenow', String(progress.completed));
      node.setAttribute('aria-valuetext', `${progress.percent}% complete`);
    });
    document.querySelectorAll('[data-progress-bar]').forEach((node) => {
      node.style.setProperty('--progress', `${progress.percent}%`);
    });

    // Rank + milestone copy (only affects pages that opt in with these hooks).
    const rank = deriveRank(progress.completed);
    document.querySelectorAll('[data-rank]').forEach((node) => { node.textContent = rank.rank; });
    document.querySelectorAll('[data-rank-step]').forEach((node) => {
      node.textContent = `Rank ${rank.index} of ${RANKS.length - 1}`;
    });
    document.querySelectorAll('[data-milestone]').forEach((node) => { node.textContent = rank.milestone; });

    // Badges + commission ceremony.
    const earned = deriveBadges(state);
    const totalEarned = Object.values(earned).filter(Boolean).length;
    document.querySelectorAll('[data-badge]').forEach((node) => {
      const id = node.getAttribute('data-badge');
      const isEarned = earned[id] === true;
      node.classList.toggle('earned', isEarned);
      node.classList.toggle('locked', !isEarned);
      node.setAttribute('aria-pressed', String(isEarned));
      const status = node.querySelector('[data-badge-state]');
      if (status) status.textContent = isEarned ? 'Earned' : 'Locked';
    });
    document.querySelectorAll('[data-badge-count]').forEach((node) => {
      node.textContent = `${totalEarned} of 9 earned`;
    });
    document.querySelectorAll('[data-commission]').forEach((node) => {
      node.classList.toggle('unlocked', progress.isComplete);
      node.setAttribute('aria-hidden', String(!progress.isComplete));
    });

    for (const key of MODULE_KEYS) {
      const complete = state.modules[key];
      document.querySelectorAll(`[data-module-status="${key}"]`).forEach((node) => {
        node.textContent = complete ? 'Complete' : 'Not complete';
      });
      document.querySelectorAll(`[data-progress-module="${key}"]`).forEach((node) => {
        node.classList.toggle('is-complete', complete);
        const check = node.querySelector('[data-progress-check]');
        if (check) check.textContent = complete ? '✓' : '○';
      });
      document.querySelectorAll(`[data-module-card="${key}"]`).forEach((node) => {
        node.classList.toggle('is-complete', complete);
      });
      document.querySelectorAll(`[data-complete-module="${key}"]`).forEach((button) => {
        button.setAttribute('aria-pressed', String(complete));
        const number = Number(key.slice(1));
        button.textContent = complete ? `Module ${number} complete — undo` : `Mark module ${number} complete`;
      });
    }
  }

  function sectionStorageKey(moduleId) {
    return `usmcmin:tmc-husband:v1:sections:${moduleId}`;
  }

  function drillStorageKey(moduleId) {
    return `usmcmin:tmc-husband:v1:drills:${moduleId}`;
  }

  function loadSections(storage, moduleId) {
    try {
      const raw = storage.getItem(sectionStorageKey(moduleId));
      const parsed = raw ? JSON.parse(raw) : {};
      return parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed : {};
    } catch (_error) {
      return {};
    }
  }

  function saveSections(storage, moduleId, sections) {
    try { storage.setItem(sectionStorageKey(moduleId), JSON.stringify(sections)); } catch (_error) { /* memory fallback */ }
  }

  function loadDrills(storage, moduleId) {
    try {
      const raw = storage.getItem(drillStorageKey(moduleId));
      const parsed = raw ? JSON.parse(raw) : {};
      if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) return { cards: {}, quiz: {} };
      return {
        cards: parsed.cards && typeof parsed.cards === 'object' ? parsed.cards : {},
        quiz: parsed.quiz && typeof parsed.quiz === 'object' ? parsed.quiz : {}
      };
    } catch (_error) {
      return { cards: {}, quiz: {} };
    }
  }

  function saveDrills(storage, moduleId, drills) {
    try { storage.setItem(drillStorageKey(moduleId), JSON.stringify(drills)); } catch (_error) { /* memory fallback */ }
  }

  // Every tracked checkbox on a module page, in document order. One list — the
  // section check-offs and the per-item checks all count toward the same bar.
  function trackedInputs(root) {
    return Array.from(root.querySelectorAll('[data-section-complete], [data-item-complete]'));
  }

  function inputId(input) {
    return input.getAttribute('data-section-complete') || input.getAttribute('data-item-complete');
  }

  function initModulePage(storage) {
    const root = document.querySelector('[data-field-manual]');
    if (!root) return null;

    const moduleId = root.getAttribute('data-field-manual');
    const sections = loadSections(storage, moduleId);
    const inputs = trackedInputs(root);
    const total = inputs.length;

    function checkedCount() {
      return inputs.filter((input) => sections[inputId(input)] === true).length;
    }

    function updateChecklistUI() {
      const done = checkedCount();
      const pct = total ? Math.round((done / total) * 100) : 0;

      inputs.forEach((input) => {
        const id = inputId(input);
        const complete = sections[id] === true;
        input.checked = complete;
        const holder = input.closest('[data-track-section], .check-item, .task-block');
        if (holder) holder.classList.toggle('is-section-complete', complete);
      });

      // Section-level roll-up: a section shows complete when every check inside it is.
      root.querySelectorAll('[data-track-section]').forEach((node) => {
        const own = trackedInputs(node);
        const allDone = own.length > 0 && own.every((input) => sections[inputId(input)] === true);
        node.classList.toggle('is-section-complete', allDone);
        const tally = node.querySelector('[data-section-tally]');
        if (tally) {
          const sub = own.filter((input) => sections[inputId(input)] === true).length;
          tally.textContent = own.length > 1 ? `${sub} of ${own.length} checked` : (allDone ? 'Checked' : 'Not checked');
        }
      });

      document.querySelectorAll('[data-section-progress-bar]').forEach((bar) => {
        bar.style.width = `${pct}%`;
      });
      document.querySelectorAll('[data-section-progress-summary]').forEach((node) => {
        node.textContent = `${done} of ${total} checks complete (${pct}%)`;
      });
      document.querySelectorAll('[data-section-progress-pct]').forEach((node) => {
        node.textContent = `${pct}%`;
      });
      return { done, total, pct };
    }

    root.addEventListener('change', (event) => {
      const input = event.target;
      if (!input || !input.matches || !input.matches('[data-section-complete], [data-item-complete]')) return;
      sections[inputId(input)] = input.checked;
      saveSections(storage, moduleId, sections);
      updateChecklistUI();
    });

    updateChecklistUI();
    return { moduleId, sections, updateChecklistUI, checkedCount, total };
  }

  /* ── Mission clock ─────────────────────────────────────────────────────── */
  function initMissionClock(storage, moduleId) {
    const hud = document.getElementById('module-mission-hud');
    if (!hud || !moduleId) return null;

    const targetMinutes = Number(hud.getAttribute('data-mission-minutes')) || 60;
    const targetSeconds = targetMinutes * 60;
    const display = hud.querySelector('[data-mission-display]');
    const ring = hud.querySelector('[data-mission-ring]');
    const pctNode = hud.querySelector('[data-mission-pct]');
    const stateNode = hud.querySelector('[data-mission-state]');
    const totalNode = hud.querySelector('[data-mission-total]');
    const pauseBtn = hud.querySelector('[data-mission-pause]');
    const resetBtn = hud.querySelector('[data-mission-reset]');

    const table = loadTime(storage);
    let elapsed = table[moduleId] || 0;
    let manuallyPaused = false;
    let lastActivity = Date.now();
    let sinceSave = 0;

    function awake() {
      return !manuallyPaused && document.visibilityState === 'visible' && (Date.now() - lastActivity) < IDLE_LIMIT_MS;
    }

    function render() {
      const pct = Math.min(100, Math.round((elapsed / targetSeconds) * 100));
      if (display) display.textContent = formatClock(elapsed);
      if (pctNode) pctNode.textContent = `${pct}%`;
      if (ring) ring.style.setProperty('--ring', `${pct}%`);
      if (totalNode) totalNode.textContent = formatDuration(totalTime(Object.assign({}, table, { [moduleId]: elapsed })));
      if (stateNode) {
        stateNode.textContent = manuallyPaused
          ? 'Paused'
          : document.visibilityState !== 'visible'
            ? 'Away'
            : (Date.now() - lastActivity) >= IDLE_LIMIT_MS
              ? 'Idle'
              : elapsed >= targetSeconds ? 'Past target' : 'Counting';
      }
      hud.classList.toggle('is-paused', !awake());
      hud.classList.toggle('is-past-target', elapsed >= targetSeconds);
    }

    function persist() {
      table[moduleId] = elapsed;
      saveTime(storage, table);
      sinceSave = 0;
    }

    function tick() {
      if (!awake()) { render(); return; }
      elapsed += 1;
      sinceSave += 1;
      if (sinceSave >= 10) persist();
      render();
    }

    ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach((type) => {
      window.addEventListener(type, () => { lastActivity = Date.now(); }, { passive: true });
    });
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'visible') lastActivity = Date.now();
      else persist();
      render();
    });
    window.addEventListener('pagehide', persist);
    window.addEventListener('beforeunload', persist);

    pauseBtn?.addEventListener('click', () => {
      manuallyPaused = !manuallyPaused;
      if (!manuallyPaused) lastActivity = Date.now();
      pauseBtn.textContent = manuallyPaused ? 'Resume clock' : 'Pause clock';
      pauseBtn.setAttribute('aria-pressed', String(manuallyPaused));
      persist();
      render();
    });

    resetBtn?.addEventListener('click', () => {
      const label = `Reset the clock for this module? ${formatDuration(elapsed)} of recorded time will be cleared. This cannot be undone.`;
      if (!window.confirm(label)) return;
      elapsed = 0;
      persist();
      render();
    });

    hud.hidden = false;
    render();
    setInterval(tick, 1000);
    return { persist };
  }

  /* ── Flashcard drill ───────────────────────────────────────────────────── */
  function initFlashcards(storage, moduleId, drills, onChange) {
    const deck = document.querySelector('[data-flashcards]');
    if (!deck) return;

    let cards = [];
    try {
      const raw = document.getElementById('tmc-flashcard-data');
      cards = raw ? JSON.parse(raw.textContent) : [];
    } catch (_error) {
      cards = [];
    }
    if (!Array.isArray(cards) || !cards.length) return;

    const face = deck.querySelector('[data-card-face]');
    const back = deck.querySelector('[data-card-back]');
    const counter = deck.querySelector('[data-card-counter]');
    const tally = deck.querySelector('[data-card-tally]');
    const bar = deck.querySelector('[data-card-bar]');
    const flipBtn = deck.querySelector('[data-card-flip]');
    const knownBtn = deck.querySelector('[data-card-known]');
    const prevBtn = deck.querySelector('[data-card-prev]');
    const nextBtn = deck.querySelector('[data-card-next]');
    const resetBtn = deck.querySelector('[data-card-reset]');
    const inner = deck.querySelector('[data-card-inner]');

    let index = 0;
    let flipped = false;

    function knownCount() {
      return cards.reduce((sum, _card, i) => sum + (drills.cards[i] === true ? 1 : 0), 0);
    }

    function render() {
      const card = cards[index];
      if (face) face.textContent = card.f;
      if (back) back.textContent = card.b;
      if (counter) counter.textContent = `Card ${index + 1} of ${cards.length}`;
      if (inner) inner.classList.toggle('is-flipped', flipped);
      if (flipBtn) flipBtn.textContent = flipped ? 'Hide answer' : 'Show answer';
      const known = drills.cards[index] === true;
      if (knownBtn) {
        knownBtn.setAttribute('aria-pressed', String(known));
        knownBtn.textContent = known ? 'Known — undo' : 'Mark known';
      }
      deck.classList.toggle('is-known', known);
      const done = knownCount();
      const pct = Math.round((done / cards.length) * 100);
      if (tally) tally.textContent = `${done} of ${cards.length} marked known (${pct}%)`;
      if (bar) bar.style.width = `${pct}%`;
      const checkbox = document.querySelector('[data-item-complete="flashcards"]');
      if (checkbox && done === cards.length && !checkbox.checked) {
        checkbox.checked = true;
        checkbox.dispatchEvent(new Event('change', { bubbles: true }));
      }
      if (typeof onChange === 'function') onChange();
    }

    function move(step) {
      index = (index + step + cards.length) % cards.length;
      flipped = false;
      render();
    }

    flipBtn?.addEventListener('click', () => { flipped = !flipped; render(); });
    inner?.addEventListener('click', () => { flipped = !flipped; render(); });
    prevBtn?.addEventListener('click', () => move(-1));
    nextBtn?.addEventListener('click', () => move(1));
    knownBtn?.addEventListener('click', () => {
      drills.cards[index] = drills.cards[index] !== true;
      saveDrills(storage, moduleId, drills);
      render();
      if (drills.cards[index]) move(1);
    });
    resetBtn?.addEventListener('click', () => {
      if (!window.confirm('Clear every "known" mark on this deck?')) return;
      drills.cards = {};
      saveDrills(storage, moduleId, drills);
      index = 0;
      flipped = false;
      render();
    });

    deck.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowRight') { move(1); event.preventDefault(); }
      if (event.key === 'ArrowLeft') { move(-1); event.preventDefault(); }
      if (event.key === ' ' || event.key === 'Enter') {
        if (event.target === inner) { flipped = !flipped; render(); event.preventDefault(); }
      }
    });

    render();
  }

  /* ── Knowledge check ───────────────────────────────────────────────────── */
  function initQuiz(storage, moduleId, drills, onChange) {
    const panel = document.querySelector('[data-quiz]');
    if (!panel) return;

    let questions = [];
    try {
      const raw = document.getElementById('tmc-quiz-data');
      questions = raw ? JSON.parse(raw.textContent) : [];
    } catch (_error) {
      questions = [];
    }
    if (!Array.isArray(questions) || !questions.length) return;

    const list = panel.querySelector('[data-quiz-list]');
    const scoreNode = panel.querySelector('[data-quiz-score]');
    const bar = panel.querySelector('[data-quiz-bar]');
    const resetBtn = panel.querySelector('[data-quiz-reset]');
    const answers = drills.quiz.answers && typeof drills.quiz.answers === 'object' ? drills.quiz.answers : (drills.quiz.answers = {});

    function correctIndex(question) {
      return question.answerOptions.findIndex((option) => option.isCorrect === true);
    }

    function build() {
      list.innerHTML = '';
      questions.forEach((question, qi) => {
        const item = document.createElement('li');
        item.className = 'quiz-item';
        item.setAttribute('data-quiz-item', String(qi));

        const prompt = document.createElement('p');
        prompt.className = 'quiz-question';
        prompt.textContent = `${qi + 1}. ${question.question}`;
        item.appendChild(prompt);

        const options = document.createElement('div');
        options.className = 'quiz-options';
        options.setAttribute('role', 'group');
        options.setAttribute('aria-label', `Question ${qi + 1}`);
        question.answerOptions.forEach((option, oi) => {
          const label = document.createElement('label');
          label.className = 'quiz-option';
          const input = document.createElement('input');
          input.type = 'radio';
          input.name = `q-${moduleId}-${qi}`;
          input.value = String(oi);
          input.addEventListener('change', () => {
            answers[qi] = oi;
            drills.quiz.answers = answers;
            saveDrills(storage, moduleId, drills);
            paint();
          });
          const text = document.createElement('span');
          text.textContent = option.text;
          label.appendChild(input);
          label.appendChild(text);
          options.appendChild(label);
        });
        item.appendChild(options);

        const feedback = document.createElement('p');
        feedback.className = 'quiz-feedback';
        feedback.setAttribute('data-quiz-feedback', String(qi));
        feedback.hidden = true;
        item.appendChild(feedback);

        list.appendChild(item);
      });
    }

    function paint() {
      let answered = 0;
      let correct = 0;
      questions.forEach((question, qi) => {
        const chosen = answers[qi];
        const item = list.querySelector(`[data-quiz-item="${qi}"]`);
        const feedback = item.querySelector(`[data-quiz-feedback="${qi}"]`);
        item.querySelectorAll('.quiz-option').forEach((label, oi) => {
          const input = label.querySelector('input');
          const isChosen = chosen === oi;
          input.checked = isChosen;
          label.classList.toggle('is-chosen', isChosen);
          label.classList.toggle('is-correct', chosen !== undefined && question.answerOptions[oi].isCorrect === true);
          label.classList.toggle('is-wrong', isChosen && question.answerOptions[oi].isCorrect !== true);
        });
        if (chosen === undefined) {
          feedback.hidden = true;
          feedback.textContent = '';
          item.classList.remove('is-right', 'is-wrong');
          return;
        }
        answered += 1;
        const option = question.answerOptions[chosen];
        const right = option.isCorrect === true;
        if (right) correct += 1;
        item.classList.toggle('is-right', right);
        item.classList.toggle('is-wrong', !right);
        feedback.hidden = false;
        const rationale = option.rationale || question.answerOptions[correctIndex(question)]?.rationale || '';
        feedback.textContent = right ? `Correct. ${rationale}` : `Not quite. ${rationale}`;
      });

      const pct = Math.round((answered / questions.length) * 100);
      if (bar) bar.style.width = `${pct}%`;
      if (scoreNode) {
        scoreNode.textContent = answered
          ? `${correct} of ${answered} correct · ${answered} of ${questions.length} answered`
          : `0 of ${questions.length} answered`;
      }
      drills.quiz.answered = answered;
      drills.quiz.correct = correct;
      saveDrills(storage, moduleId, drills);

      const checkbox = document.querySelector('[data-item-complete="quiz"]');
      if (checkbox && answered === questions.length && !checkbox.checked) {
        checkbox.checked = true;
        checkbox.dispatchEvent(new Event('change', { bubbles: true }));
      }
      if (typeof onChange === 'function') onChange();
    }

    resetBtn?.addEventListener('click', () => {
      if (!window.confirm('Clear your answers and retake this knowledge check?')) return;
      drills.quiz.answers = {};
      saveDrills(storage, moduleId, drills);
      build();
      Object.keys(answers).forEach((key) => { delete answers[key]; });
      paint();
    });

    build();
    paint();
  }

  /* ── Course-wide time readouts (landing + progress pages) ──────────────── */
  function renderTimeReadouts(storage) {
    const table = loadTime(storage);
    const total = totalTime(table);
    document.querySelectorAll('[data-time-total]').forEach((node) => { node.textContent = formatClock(total); });
    document.querySelectorAll('[data-time-total-words]').forEach((node) => { node.textContent = formatDuration(total); });
    for (const key of MODULE_KEYS) {
      document.querySelectorAll(`[data-time-module="${key}"]`).forEach((node) => {
        const seconds = table[key] || 0;
        node.textContent = seconds ? formatDuration(seconds) : 'Not started';
      });
    }
    document.querySelectorAll('[data-time-detail]').forEach((node) => {
      const started = MODULE_KEYS.filter((key) => (table[key] || 0) > 0).length;
      node.textContent = started
        ? `Across ${started} of 7 modules, on this device only.`
        : 'No time recorded on this device yet.';
    });
  }

  // Per-module checklist percent for the landing + progress pages.
  function renderChecklistReadouts(storage) {
    for (const key of MODULE_KEYS) {
      const nodes = document.querySelectorAll(`[data-checks-module="${key}"]`);
      if (!nodes.length) continue;
      const sections = loadSections(storage, key);
      const done = Object.values(sections).filter((value) => value === true).length;
      const total = Number(nodes[0].getAttribute('data-checks-total')) || 0;
      nodes.forEach((node) => {
        node.textContent = total ? `${done} of ${total} checks` : `${done} checks`;
      });
      document.querySelectorAll(`[data-checks-bar="${key}"]`).forEach((bar) => {
        bar.style.width = total ? `${Math.min(100, Math.round((done / total) * 100))}%` : '0%';
      });
    }
  }

  function initBrowser() {
    const storage = getBrowserStorage();
    let state = loadState(storage);
    updateDocument(state);

    const page = initModulePage(storage);
    renderTimeReadouts(storage);
    renderChecklistReadouts(storage);

    if (page) {
      initMissionClock(storage, page.moduleId);
      const drills = loadDrills(storage, page.moduleId);
      initFlashcards(storage, page.moduleId, drills, page.updateChecklistUI);
      initQuiz(storage, page.moduleId, drills, page.updateChecklistUI);
    }

    document.querySelectorAll('[data-complete-module]').forEach((button) => {
      button.addEventListener('click', () => {
        const moduleId = button.getAttribute('data-complete-module');
        const root = document.querySelector(`[data-field-manual="${moduleId}"]`);
        const message = document.querySelector(`[data-completion-message="${moduleId}"]`);

        if (root && !state.modules[moduleId]) {
          const sections = loadSections(storage, moduleId);
          const missing = [];
          if (!sections['field-action']) missing.push('field action');
          if (root.querySelector('[data-item-complete="quiz"]') && !sections.quiz) missing.push('knowledge check');
          if (missing.length) {
            const proceed = window.confirm(
              `You have not checked off: ${missing.join(' and ')}.\n\nMark complete anyway? Only do this if the finish line is actually done.`
            );
            if (!proceed) {
              if (message) message.textContent = `Not marked complete — finish the ${missing.join(' and ')} first, or confirm to override.`;
              return;
            }
          }
        }

        state = toggleModule(storage, moduleId);
        updateDocument(state);
        if (message) message.textContent = state.modules[moduleId]
          ? 'Saved on this device. This module is complete.'
          : 'Saved on this device. This module is not complete.';
      });
    });

    document.querySelectorAll('[data-reset-progress]').forEach((button) => {
      button.addEventListener('click', () => {
        if (!window.confirm('Reset all seven module flags on this device? This cannot be undone.')) return;
        state = resetState(storage);
        updateDocument(state);
        const message = document.querySelector('[data-reset-message]');
        if (message) message.textContent = 'All local course progress has been reset.';
      });
    });

    document.querySelectorAll('[data-reset-time]').forEach((button) => {
      button.addEventListener('click', () => {
        if (!window.confirm('Clear every recorded minute on this device? Module completion is not affected.')) return;
        saveTime(storage, Object.fromEntries(MODULE_KEYS.map((key) => [key, 0])));
        renderTimeReadouts(storage);
        const message = document.querySelector('[data-reset-message]');
        if (message) message.textContent = 'Time on task has been cleared for this device.';
      });
    });
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initBrowser, { once: true });
    else initBrowser();
  }

  return {
    STORAGE_KEY, TIME_KEY, SCHEMA_VERSION, MODULE_KEYS, RANKS,
    createDefaultState, normalizeState, loadState, saveState,
    deriveProgress, deriveRank, deriveBadges, toggleModule, resetState,
    loadTime, saveTime, totalTime, formatClock, formatDuration
  };
});
