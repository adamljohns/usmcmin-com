(function (root, factory) {
  'use strict';
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root) root.TmcHusbandProgress = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const STORAGE_KEY = 'usmcmin:tmc-husband:v1:progress';
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
    storage.setItem(sectionStorageKey(moduleId), JSON.stringify(sections));
  }

  function formatMissionTime(ms) {
    const total = Math.max(0, Math.ceil(ms / 1000));
    const mm = String(Math.floor(total / 60)).padStart(2, '0');
    const ss = String(total % 60).padStart(2, '0');
    return `${mm}:${ss}`;
  }

  function initFieldManual(storage) {
    const root = document.querySelector('[data-field-manual]');
    const hud = document.getElementById('module-mission-hud');
    if (!root) return;

    const moduleId = root.getAttribute('data-field-manual');
    let sections = loadSections(storage, moduleId);
    const sectionNodes = root.querySelectorAll('[data-track-section]');
    const totalSections = sectionNodes.length;

    function updateSectionUI() {
      let done = 0;
      sectionNodes.forEach((node) => {
        const id = node.getAttribute('data-track-section');
        const complete = sections[id] === true;
        node.classList.toggle('is-section-complete', complete);
        const input = node.querySelector(`[data-section-complete="${id}"]`);
        if (input) input.checked = complete;
        if (complete) done += 1;
      });
      const pct = totalSections ? Math.round((done / totalSections) * 100) : 0;
      document.querySelectorAll('[data-section-progress-bar]').forEach((bar) => {
        bar.style.width = `${pct}%`;
      });
      document.querySelectorAll('[data-section-progress-summary]').forEach((node) => {
        node.textContent = `${done} of ${totalSections} sections checked (${pct}%)`;
      });
    }

    root.querySelectorAll('[data-section-complete]').forEach((input) => {
      input.addEventListener('change', () => {
        const id = input.getAttribute('data-section-complete');
        sections[id] = input.checked;
        saveSections(storage, moduleId, sections);
        updateSectionUI();
      });
    });
    updateSectionUI();

    if (!hud) return;

    const minutes = Number(hud.getAttribute('data-mission-minutes')) || 75;
    const display = hud.querySelector('[data-mission-display]');
    const pctNode = hud.querySelector('[data-mission-pct]');
    const startBtn = hud.querySelector('[data-mission-start]');
    const pauseBtn = hud.querySelector('[data-mission-pause]');
    const addBtn = hud.querySelector('[data-mission-add5]');
    let remainingMs = minutes * 60 * 1000;
    let endAt = null;
    let paused = false;
    let timerId = null;

    function renderMission() {
      if (display) display.textContent = formatMissionTime(remainingMs);
      if (pctNode) {
        const pct = Math.round((remainingMs / (minutes * 60 * 1000)) * 100);
        pctNode.textContent = `${pct}%`;
      }
      hud.classList.toggle('mission-urgent', remainingMs <= 5 * 60 * 1000 && remainingMs > 0);
    }

    function tick() {
      if (paused || endAt === null) return;
      remainingMs = endAt - Date.now();
      if (remainingMs <= 0) {
        remainingMs = 0;
        paused = true;
        if (pauseBtn) pauseBtn.hidden = true;
        clearInterval(timerId);
      }
      renderMission();
    }

    function startMission() {
      hud.hidden = false;
      endAt = Date.now() + remainingMs;
      paused = false;
      if (startBtn) startBtn.hidden = true;
      if (pauseBtn) { pauseBtn.hidden = false; pauseBtn.textContent = 'Pause'; }
      clearInterval(timerId);
      timerId = setInterval(tick, 250);
      renderMission();
    }

    startBtn?.addEventListener('click', startMission);
    pauseBtn?.addEventListener('click', () => {
      if (!paused) {
        remainingMs = Math.max(0, endAt - Date.now());
        paused = true;
        pauseBtn.textContent = 'Resume';
      } else {
        endAt = Date.now() + remainingMs;
        paused = false;
        pauseBtn.textContent = 'Pause';
        clearInterval(timerId);
        timerId = setInterval(tick, 250);
      }
      renderMission();
    });
    addBtn?.addEventListener('click', () => {
      remainingMs += 5 * 60 * 1000;
      if (!paused && endAt !== null) endAt += 5 * 60 * 1000;
      renderMission();
    });
    renderMission();
  }

  function initBrowser() {
    const storage = getBrowserStorage();
    let state = loadState(storage);
    updateDocument(state);
    initFieldManual(storage);

    document.querySelectorAll('[data-complete-module]').forEach((button) => {
      button.addEventListener('click', () => {
        const moduleId = button.getAttribute('data-complete-module');
        state = toggleModule(storage, moduleId);
        updateDocument(state);
        const message = document.querySelector(`[data-completion-message="${moduleId}"]`);
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
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initBrowser, { once: true });
    else initBrowser();
  }

  return { STORAGE_KEY, SCHEMA_VERSION, MODULE_KEYS, createDefaultState, normalizeState, loadState, saveState, deriveProgress, toggleModule, resetState };
});
