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

  var DEFAULT_HABITS = [
    { id: 'creed', name: 'Read Creed', cadence: 'daily', shared: true },
    { id: 'word', name: 'Word / prayer', cadence: 'daily', shared: true },
    { id: 'body', name: 'Body line', cadence: 'daily', shared: false },
    { id: 'saca', name: 'Complete my SACA', cadence: 'weekly', shared: true },
    { id: 'bb_call', name: 'Battle Brother call', cadence: 'weekly', shared: true },
    { id: 'armada_call', name: 'Armada call', cadence: 'weekly', shared: true },
    { id: 'family_meeting', name: 'Family meeting', cadence: 'weekly', shared: false }
  ];

  var currentMode = 'form';

  function ymd(date) {
    var y = date.getFullYear();
    var m = String(date.getMonth() + 1).padStart(2, '0');
    var d = String(date.getDate()).padStart(2, '0');
    return y + '-' + m + '-' + d;
  }

  function weekDates(ref) {
    var mon = mondayOf(ref || new Date());
    var days = [];
    for (var i = 0; i < 7; i++) {
      var d = new Date(mon.getFullYear(), mon.getMonth(), mon.getDate() + i);
      days.push(d);
    }
    return days;
  }

  function ensureHabits(store) {
    if (!store.habits) store.habits = { items: [], checks: {} };
    if (!Array.isArray(store.habits.items)) store.habits.items = [];
    if (!store.habits.checks || typeof store.habits.checks !== 'object') store.habits.checks = {};
    if (!store.habits.items.length) {
      store.habits.items = DEFAULT_HABITS.map(function (h) {
        return Object.assign({}, h);
      });
    }
    return store;
  }

  function habitCheckKey(habitId, dateStr) {
    return habitId + '|' + dateStr;
  }

  function isChecked(store, habitId, dateStr) {
    return !!(store.habits && store.habits.checks && store.habits.checks[habitCheckKey(habitId, dateStr)]);
  }

  function setChecked(store, habitId, dateStr, on) {
    ensureHabits(store);
    var key = habitCheckKey(habitId, dateStr);
    if (on) store.habits.checks[key] = true;
    else delete store.habits.checks[key];
  }

  function streakFor(store, habit) {
    ensureHabits(store);
    var streak = 0;
    var cursor = new Date();
    cursor.setHours(0, 0, 0, 0);
    if (habit.cadence === 'weekly') {
      cursor = mondayOf(cursor);
      while (streak < 520) {
        if (!isChecked(store, habit.id, ymd(cursor))) break;
        streak += 1;
        cursor.setDate(cursor.getDate() - 7);
      }
      return streak;
    }
    while (streak < 800) {
      if (!isChecked(store, habit.id, ymd(cursor))) break;
      streak += 1;
      cursor.setDate(cursor.getDate() - 1);
    }
    return streak;
  }

  function weekHitRate(store) {
    ensureHabits(store);
    var days = weekDates(new Date());
    var today = ymd(new Date());
    var due = 0;
    var hit = 0;
    store.habits.items.forEach(function (habit) {
      if (habit.cadence === 'weekly') {
        due += 1;
        if (isChecked(store, habit.id, ymd(days[0]))) hit += 1;
      } else {
        days.forEach(function (d) {
          var key = ymd(d);
          if (key > today) return;
          due += 1;
          if (isChecked(store, habit.id, key)) hit += 1;
        });
      }
    });
    return { due: due, hit: hit, pct: due ? Math.round((hit / due) * 100) : 0 };
  }

  function longestSharedStreak(store) {
    ensureHabits(store);
    var best = 0;
    store.habits.items.forEach(function (h) {
      if (!h.shared) return;
      best = Math.max(best, streakFor(store, h));
    });
    return best;
  }

  function setMode(mode) {
    currentMode = mode === 'habits' ? 'habits' : 'form';
    var formBtn = el('modeForm');
    var habitBtn = el('modeHabits');
    if (formBtn) {
      formBtn.classList.toggle('active', currentMode === 'form');
      formBtn.setAttribute('aria-selected', currentMode === 'form' ? 'true' : 'false');
    }
    if (habitBtn) {
      habitBtn.classList.toggle('active', currentMode === 'habits');
      habitBtn.setAttribute('aria-selected', currentMode === 'habits' ? 'true' : 'false');
    }
    var habitShell = el('habitShell');
    var formShell = el('formShell');
    var doneShell = el('doneShell');
    var historyPanel = el('historyPanel');
    if (habitShell) habitShell.hidden = currentMode !== 'habits';
    if (currentMode === 'habits') {
      if (formShell) formShell.hidden = true;
      if (doneShell) doneShell.hidden = true;
      if (historyPanel) historyPanel.hidden = true;
      renderHabitBoard();
    } else {
      if (formShell) formShell.hidden = false;
      if (doneShell) doneShell.hidden = true;
      renderHistory();
    }
    try {
      var url = new URL(window.location.href);
      if (currentMode === 'habits') url.searchParams.set('mode', 'habits');
      else url.searchParams.delete('mode');
      window.history.replaceState({}, '', url.pathname + url.search + url.hash);
    } catch (e) {}
  }

  function renderDayHead(targetId, days) {
    var head = el(targetId);
    if (!head) return;
    var today = ymd(new Date());
    var labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    head.innerHTML = '<span class="hd-name">Habit</span>' + days.map(function (d, i) {
      var cls = ymd(d) === today ? ' hd-today' : '';
      return '<span class="' + cls.trim() + '">' + labels[i] + '</span>';
    }).join('') + '<span>Share</span>';
  }

  function renderHabitRows(targetId, items, store, opts) {
    var wrap = el(targetId);
    if (!wrap) return;
    opts = opts || {};
    var readonly = !!opts.readonly;
    var days = weekDates(new Date());
    var monKey = ymd(days[0]);
    if (!items.length) {
      wrap.innerHTML = '<p class="habit-empty">' + (opts.empty || 'No habits yet.') + '</p>';
      return;
    }
    wrap.innerHTML = items.map(function (habit) {
      var streak = streakFor(store, habit);
      var cells = days.map(function (d) {
        var key = ymd(d);
        var activeKey = habit.cadence === 'weekly' ? monKey : key;
        var on = isChecked(store, habit.id, activeKey);
        var isWeeklyCell = habit.cadence === 'weekly' && key !== monKey;
        if (isWeeklyCell) {
          return '<button type="button" class="habit-check weekly-slot' + (on ? ' on' : '') + '" disabled aria-hidden="true">' + (on ? '✓' : '') + '</button>';
        }
        var disabled = readonly ? ' disabled' : '';
        return '<button type="button" class="habit-check' + (on ? ' on' : '') + '" data-habit="' + habit.id + '" data-day="' + activeKey + '"' + disabled + ' aria-pressed="' + (on ? 'true' : 'false') + '" aria-label="' + habit.name + ' ' + activeKey + '">' + (on ? '✓' : '') + '</button>';
      }).join('');
      var shareBtn = readonly
        ? '<span class="habit-share-btn shared">Shared</span>'
        : '<button type="button" class="habit-share-btn' + (habit.shared ? ' shared' : '') + '" data-share="' + habit.id + '">' + (habit.shared ? 'Shared' : 'Private') + '</button>';
      return '<div class="habit-row" data-habit-row="' + habit.id + '">' +
        '<div class="hr-meta"><div class="hr-name">' + escapeHtml(habit.name) + '</div>' +
        '<div class="hr-sub">' + (habit.cadence === 'weekly' ? 'Weekly' : 'Daily') +
        (streak ? ' · <span class="hr-streak">' + streak + (habit.cadence === 'weekly' ? '-week' : '-day') + ' streak</span>' : '') + '</div></div>' +
        cells + shareBtn + '</div>';
    }).join('');

    if (!readonly) {
      wrap.querySelectorAll('.habit-check[data-habit]').forEach(function (btn) {
        btn.addEventListener('click', function () {
          var s = ensureHabits(loadStore());
          var id = btn.dataset.habit;
          var day = btn.dataset.day;
          setChecked(s, id, day, !isChecked(s, id, day));
          saveStore(s);
          renderHabitBoard();
        });
      });
      wrap.querySelectorAll('.habit-share-btn[data-share]').forEach(function (btn) {
        btn.addEventListener('click', function () {
          var s = ensureHabits(loadStore());
          var hit = s.habits.items.find(function (h) { return h.id === btn.dataset.share; });
          if (!hit) return;
          hit.shared = !hit.shared;
          saveStore(s);
          renderHabitBoard();
        });
      });
    }
  }

  function escapeHtml(str) {
    return String(str || '').replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  function renderHabitStats(store) {
    var box = el('habitStats');
    if (!box) return;
    var rate = weekHitRate(store);
    var shared = store.habits.items.filter(function (h) { return h.shared; }).length;
    var best = longestSharedStreak(store);
    box.innerHTML =
      '<div class="habit-stat"><span class="hs-label">This week</span><span class="hs-value">' + rate.pct + '%</span></div>' +
      '<div class="habit-stat"><span class="hs-label">Shared habits</span><span class="hs-value">' + shared + '</span></div>' +
      '<div class="habit-stat"><span class="hs-label">Best shared streak</span><span class="hs-value">' + best + '</span></div>';
  }

  function renderHabitBoard() {
    var store = ensureHabits(loadStore());
    saveStore(store);
    var days = weekDates(new Date());
    renderDayHead('habitDayHead', days);
    renderDayHead('brotherDayHead', days);
    renderHabitStats(store);
    renderHabitRows('habitRows', store.habits.items, store, { readonly: false });

    var brother = store.brotherPack || null;
    var hint = el('brotherHabitsHint');
    if (!brother || !brother.items || !brother.items.length) {
      if (hint) hint.textContent = 'No brother pack imported yet.';
      renderHabitRows('brotherHabitRows', [], store, { empty: 'Import his share pack to see the habits he marked Shared.' });
      return;
    }
    if (hint) {
      hint.textContent = (brother.name ? brother.name + ' · ' : '') +
        'Imported ' + (brother.importedAt ? new Date(brother.importedAt).toLocaleDateString() : 'recently') +
        '. Read-only — his checks as of the pack he sent.';
    }
    var brotherStore = {
      habits: {
        items: brother.items,
        checks: brother.checks || {}
      }
    };
    renderHabitRows('brotherHabitRows', brother.items, brotherStore, { readonly: true });
  }

  function buildSharePack() {
    var store = ensureHabits(loadStore());
    var sharedItems = store.habits.items.filter(function (h) { return h.shared; });
    var checks = {};
    Object.keys(store.habits.checks).forEach(function (key) {
      var habitId = key.split('|')[0];
      if (sharedItems.some(function (h) { return h.id === habitId; })) {
        checks[key] = true;
      }
    });
    return {
      v: 1,
      type: 'fc_battle_brother_share',
      name: (store.profile && store.profile.name) || val('reporterName') || '',
      exportedAt: new Date().toISOString(),
      week: calendarWeek(),
      theme: themeByWeek(calendarWeek()).title,
      items: sharedItems,
      checks: checks
    };
  }

  function sharePackOrWarn() {
    var pack = buildSharePack();
    if (!pack.items.length) {
      flash('Mark at least one habit Shared before sending a pack.');
      return null;
    }
    return pack;
  }

  function syncHabitsFromSubmission(payload) {
    var store = ensureHabits(loadStore());
    var mon = ymd(mondayOf(new Date(payload.submittedAt || Date.now())));
    if (payload.battleBrotherCall === 'Yes') setChecked(store, 'bb_call', mon, true);
    if (payload.armadaCall === 'Yes') setChecked(store, 'armada_call', mon, true);
    saveStore(store);
  }

  function addHabit() {
    var name = val('newHabitName');
    if (!name) { flash('Name the habit first.'); return; }
    var cadence = val('newHabitCadence') === 'weekly' ? 'weekly' : 'daily';
    var store = ensureHabits(loadStore());
    var id = 'h_' + Date.now().toString(36);
    store.habits.items.push({ id: id, name: name, cadence: cadence, shared: false });
    saveStore(store);
    setVal('newHabitName', '');
    renderHabitBoard();
    flash('Habit added.');
  }

  function copySharePack() {
    var pack = sharePackOrWarn();
    if (!pack) return;
    var text = JSON.stringify(pack, null, 2);
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        flash('Share pack copied — text/email it to your Battle Brother.');
      }).catch(function () {
        el('importSharePack').value = text;
        flash('Copy failed — pack pasted into the import box so you can select it.');
      });
    } else {
      el('importSharePack').value = text;
      flash('Clipboard unavailable — pack pasted into the import box.');
    }
  }

  function downloadSharePack() {
    var pack = sharePackOrWarn();
    if (!pack) return;
    var blob = new Blob([JSON.stringify(pack, null, 2)], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'battle-brother-share-pack.json';
    a.click();
    URL.revokeObjectURL(a.href);
    flash('Share pack downloaded.');
  }

  function nativeSharePack() {
    var pack = sharePackOrWarn();
    if (!pack) return;
    var text = JSON.stringify(pack, null, 2);
    var title = 'Battle Brother share pack — ' + (pack.name || 'Captain');
    if (navigator.share) {
      var sharePromise;
      if (navigator.canShare) {
        try {
          var file = new File([text], 'battle-brother-share-pack.json', { type: 'application/json' });
          var withFile = { title: title, text: 'My Shared captain habits for this Armada week.', files: [file] };
          if (navigator.canShare(withFile)) {
            sharePromise = navigator.share(withFile);
          }
        } catch (e) {}
      }
      if (!sharePromise) {
        sharePromise = navigator.share({
          title: title,
          text: 'Battle Brother share pack (paste into Habit Board → Import):\n\n' + text
        });
      }
      sharePromise.then(function () {
        flash('Share sheet sent.');
      }).catch(function () {
        copySharePack();
      });
      return;
    }
    copySharePack();
  }

  function importSharePack() {
    var raw = val('importSharePack');
    if (!raw) { flash('Paste a share pack first.'); return; }
    try {
      var pack = JSON.parse(raw);
      if (!pack || pack.type !== 'fc_battle_brother_share' || !Array.isArray(pack.items)) {
        flash('That does not look like a Battle Brother share pack.');
        return;
      }
      var store = loadStore();
      store.brotherPack = {
        name: pack.name || 'Battle Brother',
        importedAt: new Date().toISOString(),
        items: pack.items,
        checks: pack.checks || {}
      };
      saveStore(store);
      setVal('importSharePack', '');
      renderHabitBoard();
      flash('Brother pack imported — his Shared habits are below.');
    } catch (e) {
      flash('Could not parse that pack — check the JSON.');
    }
  }

  function clearBrotherPack() {
    var store = loadStore();
    delete store.brotherPack;
    saveStore(store);
    renderHabitBoard();
    flash('Brother board cleared.');
  }

  function openHabitsShare() {
    setMode('habits');
    setTimeout(function () {
      var section = el('sharePackSection');
      if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 60);
  }

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
    syncHabitsFromSubmission(payload);
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
    ensureHabits(loadStore());
    renderHistory();
    showStep(currentStep);

    el('modeForm').addEventListener('click', function () { setMode('form'); });
    el('modeHabits').addEventListener('click', function () { setMode('habits'); });
    el('btnAddHabit').addEventListener('click', addHabit);
    el('newHabitName').addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); addHabit(); }
    });
    el('btnCopySharePack').addEventListener('click', copySharePack);
    el('btnDownloadSharePack').addEventListener('click', downloadSharePack);
    el('btnNativeSharePack').addEventListener('click', nativeSharePack);
    el('btnImportSharePack').addEventListener('click', importSharePack);
    el('btnClearBrotherPack').addEventListener('click', clearBrotherPack);
    var goHabits = el('btnGoHabits');
    if (goHabits) goHabits.addEventListener('click', openHabitsShare);

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

    var params = new URLSearchParams(window.location.search);
    var mode = (params.get('mode') || '').toLowerCase();
    if (mode === 'habits' || mode === 'share' || params.get('share') === '1') {
      if (params.get('share') === '1' || mode === 'share') openHabitsShare();
      else setMode('habits');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
