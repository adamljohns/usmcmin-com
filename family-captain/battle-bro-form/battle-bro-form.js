/**
 * The Family Captain — Battle Brother weekly check-in (standalone)
 * Replaces Google Forms with local memory + FormSubmit relay.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'fc_battle_brother_v1';
  var FORMSUBMIT_URL = 'https://formsubmit.co/ajax/usmcministries2022@gmail.com';

  // Armada weeks run Mon–Sun. Anchor = Monday of a known Sabbath week
  // (Finance was the week before: Mon 2026-06-29). After Sabbath the
  // cycle rolls to Vision and repeats. Override anytime with ?week=N
  // or ?theme=key, or by tapping a week chip.
  var ARMADA_ANCHOR = { y: 2026, m: 6, d: 6 }; // month is 0-indexed → Jul 6, 2026
  var ARMADA_ANCHOR_WEEK = 7; // Sabbath

  var THEMES = [
    { week: 1, key: 'vision', title: 'Vision', icon: '🗺️', color: '#B85042' },
    { week: 2, key: 'body', title: 'Body', icon: '💪', color: '#E89B47' },
    { week: 3, key: 'spiritual', title: 'Spiritual', icon: '✝️', color: '#6BA368' },
    { week: 4, key: 'husbanding', title: 'Husbanding', icon: '💍', color: '#4A7BA6' },
    { week: 5, key: 'fathering', title: 'Fathering', icon: '🏡', color: '#8B5FBF' },
    { week: 6, key: 'finance', title: 'Finance', icon: '💰', color: '#D4A574' },
    { week: 7, key: 'sabbath', title: 'Sabbath', icon: '🌅', color: '#557C99' }
  ];

  var STEPS = ['checkin', 'brother', 'armada', 'comments'];
  var currentStep = 0;
  var selectedWeek = 7;
  var weekFromOverride = false;
  var editingId = null;

  var form = {
    reporterName: '',
    lastWeekSaca: '',
    sacaPassFail: '',
    thisWeekSaca: '',
    battleBrotherCall: '',
    threeQuestionsAsked: '',
    armadaCall: '',
    armadaRating: 0,
    confidentialComments: ''
  };

  function loadStore() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function saveStore(store) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
    } catch (e) {}
  }

  function themeByWeek(n) {
    return THEMES.find(function (t) { return t.week === n; }) || THEMES[6];
  }

  /** Monday 00:00 local of the calendar week containing `date`. */
  function mondayOf(date) {
    var d = new Date(date.getFullYear(), date.getMonth(), date.getDate());
    var day = d.getDay(); // 0=Sun … 6=Sat
    var offset = day === 0 ? -6 : 1 - day;
    d.setDate(d.getDate() + offset);
    d.setHours(0, 0, 0, 0);
    return d;
  }

  /**
   * Current Armada week from the calendar (Mon–Sun cycle).
   * Anchored to the known Sabbath week starting Mon 2026-07-06.
   */
  function calendarWeek(now) {
    var today = now || new Date();
    var thisMon = mondayOf(today);
    var anchor = new Date(ARMADA_ANCHOR.y, ARMADA_ANCHOR.m, ARMADA_ANCHOR.d);
    anchor = mondayOf(anchor);
    var msPerWeek = 7 * 24 * 60 * 60 * 1000;
    var elapsed = Math.floor((thisMon - anchor) / msPerWeek);
    var idx = ((ARMADA_ANCHOR_WEEK - 1) + elapsed) % 7;
    if (idx < 0) idx += 7;
    return idx + 1;
  }

  function weekFromUrl() {
    var params = new URLSearchParams(window.location.search);
    var w = parseInt(params.get('week'), 10);
    if (w >= 1 && w <= 7) {
      weekFromOverride = true;
      return w;
    }
    var key = (params.get('theme') || '').toLowerCase();
    var hit = THEMES.find(function (t) { return t.key === key; });
    if (hit) {
      weekFromOverride = true;
      return hit.week;
    }
    weekFromOverride = false;
    return calendarWeek();
  }

  function syncWeekToUrl(week) {
    try {
      var url = new URL(window.location.href);
      var t = themeByWeek(week);
      url.searchParams.set('week', String(week));
      url.searchParams.set('theme', t.key);
      window.history.replaceState({}, '', url.pathname + url.search + url.hash);
    } catch (e) {}
  }

  function el(id) { return document.getElementById(id); }

  function val(id) {
    var node = el(id);
    return node ? (node.value || '').trim() : '';
  }

  function setVal(id, v) {
    var node = el(id);
    if (node) node.value = v || '';
  }

  function flash(msg) {
    var bar = el('bbFlash');
    if (!bar) return;
    bar.textContent = msg;
    bar.hidden = false;
    clearTimeout(flash._t);
    flash._t = setTimeout(function () { bar.hidden = true; }, 3200);
  }

  function readForm() {
    form.reporterName = val('reporterName');
    form.lastWeekSaca = val('lastWeekSaca');
    form.sacaPassFail = val('sacaPassFail');
    form.thisWeekSaca = val('thisWeekSaca');
    form.battleBrotherCall = val('battleBrotherCall');
    form.threeQuestionsAsked = val('threeQuestionsAsked');
    form.armadaCall = val('armadaCall');
    form.armadaRating = parseInt(val('armadaRating'), 10) || 0;
    form.confidentialComments = val('confidentialComments');
  }

  function writeForm(data) {
    if (!data) return;
    setVal('reporterName', data.reporterName);
    setVal('lastWeekSaca', data.lastWeekSaca);
    setVal('sacaPassFail', data.sacaPassFail);
    setVal('thisWeekSaca', data.thisWeekSaca);
    setVal('battleBrotherCall', data.battleBrotherCall);
    setVal('threeQuestionsAsked', data.threeQuestionsAsked);
    setVal('armadaCall', data.armadaCall);
    setVal('confidentialComments', data.confidentialComments);
    setStar(data.armadaRating || 0);
  }

  function saveDraft() {
    readForm();
    var store = loadStore();
    store.draft = {
      week: selectedWeek,
      step: currentStep,
      data: Object.assign({}, form),
      updatedAt: new Date().toISOString()
    };
    saveStore(store);
  }

  function restoreProfile() {
    var store = loadStore();
    if (store.profile && store.profile.name && !val('reporterName')) {
      setVal('reporterName', store.profile.name);
    }
    if (store.draft && store.draft.week === selectedWeek && store.draft.data) {
      writeForm(store.draft.data);
      if (typeof store.draft.step === 'number') currentStep = store.draft.step;
    }
    prefillLastSaca();
  }

  function prefillLastSaca() {
    var store = loadStore();
    if (val('lastWeekSaca')) return;
    var subs = store.submissions || [];
    if (!subs.length) return;
    var prev = subs.find(function (s) { return s.week < selectedWeek; }) || subs[0];
    if (prev && prev.data && prev.data.thisWeekSaca) {
      setVal('lastWeekSaca', prev.data.thisWeekSaca);
    }
  }

  function renderWeekPicker() {
    var wrap = el('weekPicker');
    if (!wrap) return;
    var cal = calendarWeek();
    wrap.innerHTML = THEMES.map(function (t) {
      var active = t.week === selectedWeek ? ' active' : '';
      var mark = t.week === cal ? ' <span class="wc-now" title="Current Armada week">· now</span>' : '';
      return '<button type="button" class="week-chip' + active + '" data-week="' + t.week + '" style="--chip-color:' + t.color + '">' +
        '<span class="wc-icon">' + t.icon + '</span>' +
        '<span class="wc-label">Wk ' + t.week + ' · ' + t.title + mark + '</span></button>';
    }).join('');
    wrap.querySelectorAll('.week-chip').forEach(function (btn) {
      btn.addEventListener('click', function () {
        selectedWeek = parseInt(btn.dataset.week, 10);
        weekFromOverride = selectedWeek !== calendarWeek();
        syncWeekToUrl(selectedWeek);
        renderWeekPicker();
        updateThemeBanner();
        prefillLastSaca();
        saveDraft();
      });
    });
  }

  function updateThemeBanner() {
    var t = themeByWeek(selectedWeek);
    var banner = el('themeBanner');
    if (banner) {
      banner.style.setProperty('--theme-color', t.color);
      var kicker = weekFromOverride && selectedWeek !== calendarWeek()
        ? 'Armada theme (manual pick)'
        : 'This week&rsquo;s Armada theme';
      banner.innerHTML = '<span class="tb-kicker">' + kicker + '</span>' +
        '<span class="tb-title">' + t.icon + ' Week ' + t.week + ' — ' + t.title + '</span>';
    }
    document.title = 'Battle Brother Form · Week ' + t.week + ' ' + t.title + ' — The Family Captain';
  }

  function showStep(n) {
    currentStep = Math.max(0, Math.min(STEPS.length - 1, n));
    STEPS.forEach(function (key, i) {
      var sec = el('step-' + key);
      if (sec) sec.classList.toggle('active', i === currentStep);
    });
    var pct = Math.round(((currentStep + 1) / STEPS.length) * 100);
    var fill = el('progressFill');
    var text = el('progressText');
    if (fill) fill.style.width = pct + '%';
    if (text) text.textContent = 'Step ' + (currentStep + 1) + ' of ' + STEPS.length;
    var back = el('btnBack');
    var next = el('btnNext');
    var submit = el('btnSubmit');
    if (back) back.style.visibility = currentStep === 0 ? 'hidden' : 'visible';
    if (next) next.hidden = currentStep === STEPS.length - 1;
    if (submit) submit.hidden = currentStep !== STEPS.length - 1;
    saveDraft();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function validateStep() {
    readForm();
    if (currentStep === 0) {
      if (!form.reporterName) return 'Enter your name (first and last).';
      if (!form.lastWeekSaca) return "What was your Battle Brother's SACA for last week?";
      if (!form.sacaPassFail) return 'Did he complete his SACA? (Pass/Fail)';
      if (!form.thisWeekSaca) return "What is your Battle Brother's SACA for this week?";
    }
    if (currentStep === 1) {
      if (!form.battleBrotherCall) return 'Did you have your Battle Brother call?';
      if (!form.threeQuestionsAsked) return 'Did your Battle Brother ask the required 3 questions?';
    }
    if (currentStep === 2) {
      if (!form.armadaCall) return 'Did you have your Armada call?';
      if (!form.armadaRating) return 'Rate the Armada call (1–5 stars).';
    }
    if (currentStep === 3) {
      if (!form.confidentialComments) return 'Any additional comments? (required — even a short prayer counts)';
    }
    return '';
  }

  function setStar(n) {
    form.armadaRating = n;
    setVal('armadaRating', n ? String(n) : '');
    document.querySelectorAll('.star-btn').forEach(function (btn) {
      var v = parseInt(btn.dataset.value, 10);
      btn.classList.toggle('selected', v <= n);
      btn.setAttribute('aria-pressed', v <= n ? 'true' : 'false');
    });
    var hint = el('ratingHint');
    if (hint) hint.textContent = n ? 'Selected: ' + n + ' / 5' : '';
  }

  function bindStars() {
    document.querySelectorAll('.star-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        setStar(parseInt(btn.dataset.value, 10));
        saveDraft();
      });
    });
    var clear = el('clearRating');
    if (clear) clear.addEventListener('click', function (e) {
      e.preventDefault();
      setStar(0);
      saveDraft();
    });
  }

  function buildPayload() {
    readForm();
    var t = themeByWeek(selectedWeek);
    return {
      _subject: 'Battle Brother Form — Wk ' + t.week + ' ' + t.title + ' — ' + form.reporterName,
      _template: 'table',
      _captcha: 'false',
      submittedAt: new Date().toISOString(),
      week: t.week,
      theme: t.title,
      reporterName: form.reporterName,
      lastWeekSaca: form.lastWeekSaca,
      sacaPassFail: form.sacaPassFail,
      thisWeekSaca: form.thisWeekSaca,
      battleBrotherCall: form.battleBrotherCall,
      threeQuestionsAsked: form.threeQuestionsAsked,
      armadaCall: form.armadaCall,
      armadaRating: form.armadaRating,
      armadaRatingLabel: ratingLabel(form.armadaRating),
      confidentialComments: form.confidentialComments
    };
  }

  function ratingLabel(n) {
    var labels = {
      1: '1 — Wasted Time',
      2: '2 — Surface-Level',
      3: '3 — Solid',
      4: '4 — High Impact',
      5: '5 — Transformational'
    };
    return labels[n] || '';
  }

  function persistSubmission(payload) {
    var store = loadStore();
    store.profile = { name: form.reporterName };
    store.submissions = store.submissions || [];
    var entry = {
      id: editingId || ('bb_' + Date.now()),
      week: selectedWeek,
      theme: themeByWeek(selectedWeek).title,
      submittedAt: payload.submittedAt,
      data: Object.assign({}, form)
    };
    if (editingId) {
      store.submissions = store.submissions.map(function (s) {
        return s.id === editingId ? entry : s;
      });
    } else {
      store.submissions.unshift(entry);
    }
    store.submissions = store.submissions.slice(0, 52);
    delete store.draft;
    saveStore(store);
    renderHistory();
    return entry.id;
  }

  function emailPayload(payload) {
    fetch(FORMSUBMIT_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(payload)
    }).catch(function () {});
  }

  function submitForm() {
    var err = validateStep();
    if (err) { flash(err); return; }
    var payload = buildPayload();
    persistSubmission(payload);
    emailPayload(payload);
    el('formShell').hidden = true;
    el('doneShell').hidden = false;
    el('doneWeek').textContent = 'Week ' + payload.week + ' · ' + payload.theme;
    el('doneName').textContent = payload.reporterName;
    window.scrollTo(0, 0);
  }

  function renderHistory() {
    var list = el('historyList');
    var wrap = el('historyPanel');
    if (!list || !wrap) return;
    var store = loadStore();
    var subs = store.submissions || [];
    if (!subs.length) {
      wrap.hidden = true;
      return;
    }
    wrap.hidden = false;
    list.innerHTML = subs.slice(0, 12).map(function (s) {
      var d = new Date(s.submittedAt);
      var when = d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' });
      return '<div class="hist-row">' +
        '<div><strong>Wk ' + s.week + ' · ' + s.theme + '</strong><br><span class="hist-meta">' + when + ' — ' + (s.data.reporterName || '') + '</span></div>' +
        '<button type="button" class="hist-edit" data-id="' + s.id + '">Edit</button></div>';
    }).join('');
    list.querySelectorAll('.hist-edit').forEach(function (btn) {
      btn.addEventListener('click', function () { loadSubmission(btn.dataset.id); });
    });
  }

  function loadSubmission(id) {
    var store = loadStore();
    var hit = (store.submissions || []).find(function (s) { return s.id === id; });
    if (!hit) return;
    editingId = id;
    selectedWeek = hit.week;
    writeForm(hit.data);
    renderWeekPicker();
    updateThemeBanner();
    el('formShell').hidden = false;
    el('doneShell').hidden = true;
    showStep(0);
    flash('Loaded submission for editing.');
  }

  function resetForm() {
    editingId = null;
    form = {
      reporterName: val('reporterName'),
      lastWeekSaca: '',
      sacaPassFail: '',
      thisWeekSaca: '',
      battleBrotherCall: '',
      threeQuestionsAsked: '',
      armadaCall: '',
      armadaRating: 0,
      confidentialComments: ''
    };
    writeForm(form);
    prefillLastSaca();
    el('formShell').hidden = false;
    el('doneShell').hidden = true;
    showStep(0);
  }

  function bindInputs() {
    ['reporterName', 'lastWeekSaca', 'sacaPassFail', 'thisWeekSaca',
      'battleBrotherCall', 'threeQuestionsAsked', 'armadaCall', 'confidentialComments'
    ].forEach(function (id) {
      var node = el(id);
      if (!node) return;
      node.addEventListener('input', saveDraft);
      node.addEventListener('change', saveDraft);
      if (id === 'reporterName') node.addEventListener('blur', function () {
        var store = loadStore();
        store.profile = { name: val('reporterName') };
        saveStore(store);
      });
    });
  }

  function init() {
    selectedWeek = weekFromUrl();
    if (!weekFromOverride) syncWeekToUrl(selectedWeek);
    renderWeekPicker();
    updateThemeBanner();
    restoreProfile();
    bindStars();
    bindInputs();
    renderHistory();
    showStep(currentStep);

    el('btnNext').addEventListener('click', function () {
      var err = validateStep();
      if (err) { flash(err); return; }
      showStep(currentStep + 1);
    });
    el('btnBack').addEventListener('click', function () { showStep(currentStep - 1); });
    el('btnSubmit').addEventListener('click', submitForm);
    el('btnAnother').addEventListener('click', resetForm);
    el('btnClearDraft').addEventListener('click', function () {
      var store = loadStore();
      delete store.draft;
      saveStore(store);
      resetForm();
      flash('Draft cleared.');
    });
    el('btnExport').addEventListener('click', function () {
      var blob = new Blob([JSON.stringify(loadStore(), null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'battle-brother-memory.json';
      a.click();
      URL.revokeObjectURL(a.href);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
