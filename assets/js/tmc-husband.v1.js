(() => {
  "use strict";

  const STORAGE_NAMESPACE = "tmc-husband.lesson-progress";
  const STORAGE_VERSION = 1;
  const LESSON_ID = "lesson-01";
  const button = document.querySelector(`[data-completion="${LESSON_ID}"]`);
  const status = document.querySelector("[data-completion-status]");

  if (!button || !status) return;

  const emptyState = () => ({ version: STORAGE_VERSION, lessons: {} });

  function readState() {
    try {
      const raw = window.localStorage.getItem(STORAGE_NAMESPACE);
      if (!raw) return emptyState();
      const parsed = JSON.parse(raw);
      if (
        !parsed ||
        parsed.version !== STORAGE_VERSION ||
        !parsed.lessons ||
        typeof parsed.lessons !== "object" ||
        Array.isArray(parsed.lessons)
      ) {
        window.localStorage.removeItem(STORAGE_NAMESPACE);
        return emptyState();
      }
      return parsed;
    } catch (error) {
      try {
        window.localStorage.removeItem(STORAGE_NAMESPACE);
      } catch (recoveryError) {
        // Storage may be unavailable; the in-memory default still keeps the control usable.
      }
      return emptyState();
    }
  }

  function writeState(state) {
    try {
      window.localStorage.setItem(STORAGE_NAMESPACE, JSON.stringify(state));
      return true;
    } catch (error) {
      return false;
    }
  }

  function render(completed, persisted = true) {
    button.setAttribute("aria-pressed", String(completed));
    button.querySelector(".completion-button__icon").textContent = completed ? "✓" : "○";
    button.querySelector(".completion-button__text").textContent = completed
      ? "Lesson 1 completed"
      : "Mark Lesson 1 complete";
    status.textContent = completed
      ? persisted
        ? "Completed on this device. Select again to undo."
        : "Completed for this visit, but local storage is unavailable."
      : "Not completed on this device.";
  }

  let state = readState();
  render(Boolean(state.lessons[LESSON_ID]?.completed));

  button.addEventListener("click", () => {
    const completed = !Boolean(state.lessons[LESSON_ID]?.completed);
    state = {
      ...state,
      version: STORAGE_VERSION,
      lessons: {
        ...state.lessons,
        [LESSON_ID]: completed
          ? { completed: true, completedAt: new Date().toISOString() }
          : { completed: false }
      }
    };
    render(completed, writeState(state));
  });
})();
