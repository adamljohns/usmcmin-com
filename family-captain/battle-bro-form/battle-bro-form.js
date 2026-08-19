/**
 * The Family Captain — Battle Brother weekly check-in (standalone)
 * Replaces Google Forms with local memory + FormSubmit relay.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'fc_battle_brother_v1';
  var FORMSUBMIT_URL = 'https://formsubmit.co/ajax/usmcministries2022@gmail.com';

  // Armada theme weeks run Sun–Sat (Wed Armada call sits mid-week).
  // Anchor = Sunday opening a known Sabbath week (Jul 5, 2026).
  // Override anytime with ?week=N or ?theme=key, or by tapping a week chip.
  var ARMADA_ANCHOR = { y: 2026, m: 6, d: 5 }; // month is 0-indexed → Sun Jul 5, 2026
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

  // Canonical Captain habit board (order matters). Users can still add customs below.
  var HABITS_SCHEMA_V = 2;
  var WEEKLY_CHECK_COL = 3; // Wed — single middle check for weekly habits
  var DEFAULT_HABITS = [
    { id: 'creed', name: 'Review Creed', cadence: 'daily', shared: true },
    { id: 'prayer_525', name: '5:25 Prayer', cadence: 'daily', shared: true },
    { id: 'captains_log', name: "Captain's Log", cadence: 'daily', shared: true },
    { id: 'saca', name: 'Complete my SACA', cadence: 'weekly', shared: true },
    { id: 'bb_call', name: 'Battle Brother call / His SACA complete', cadence: 'weekly', shared: true },
    { id: 'armada_call', name: 'Armada call', cadence: 'weekly', shared: true }
  ];
  var LEGACY_DEFAULT_IDS = {
    creed: true, word: true, prayer_525: true, body: true, captains_log: true,
    saca: true, bb_call: true, armada_call: true, family_meeting: true
  };

  var currentMode = 'form';

  function ymd(date) {
    var y = date.getFullYear();
    var m = String(date.getMonth() + 1).padStart(2, '0');
    var d = String(date.getDate()).padStart(2, '0');
    return y + '-' + m + '-' + d;
  }

  function weekDates(ref) {
    var sun = sundayOf(ref || new Date());
    var days = [];
    for (var i = 0; i < 7; i++) {
      var d = new Date(sun.getFullYear(), sun.getMonth(), sun.getDate() + i);
      days.push(d);
    }
    return days;
  }

  function ensureHabits(store) {
    if (!store.habits) store.habits = { items: [], checks: {}, v: 0 };
    if (!Array.isArray(store.habits.items)) store.habits.items = [];
    if (!store.habits.checks || typeof store.habits.checks !== 'object') store.habits.checks = {};
    migrateHabits(store);
    if (!store.habits.items.length) {
      store.habits.items = DEFAULT_HABITS.map(function (h) {
        return Object.assign({}, h);
      });
      store.habits.v = HABITS_SCHEMA_V;
    }
    return store;
  }

  function migrateHabits(store) {
    if ((store.habits.v || 0) >= HABITS_SCHEMA_V) return;

    // Preserve checks when renaming Word / prayer → 5:25 Prayer.
    var checks = store.habits.checks;
    var remapped = {};
    Object.keys(checks).forEach(function (key) {
      if (key.indexOf('word|') === 0) remapped['prayer_525|' + key.slice(5)] = checks[key];
      else remapped[key] = checks[key];
    });
    store.habits.checks = remapped;

    var byId = {};
    store.habits.items.forEach(function (h) {
      if (h && h.id) byId[h.id] = h;
    });
    if (byId.word && !byId.prayer_525) {
      byId.prayer_525 = Object.assign({}, byId.word, { id: 'prayer_525', name: '5:25 Prayer' });
    }

    var custom = store.habits.items.filter(function (h) {
      return h && h.id && !LEGACY_DEFAULT_IDS[h.id];
    });

    store.habits.items = DEFAULT_HABITS.map(function (def) {
      var prev = byId[def.id] || null;
      return {
        id: def.id,
        name: def.name,
        cadence: def.cadence,
        shared: prev && typeof prev.shared === 'boolean' ? prev.shared : def.shared
      };
    }).concat(custom.map(function (h) {
      return Object.assign({}, h);
    }));

    store.habits.v = HABITS_SCHEMA_V;
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
      cursor = sundayOf(cursor);
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
    var labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    head.innerHTML = '<span class="hd-name">Habit</span>' + days.map(function (d, i) {
      var cls = ymd(d) === today ? ' hd-today' : '';
      return '<span class="hd-day' + cls + '"><span class="hd-date">' + d.getDate() + '</span><span class="hd-dow">' + labels[i] + '</span></span>';
    }).join('') + '<span class="hd-share">Share</span>';
  }

  function renderHabitRows(targetId, items, store, opts) {
    var wrap = el(targetId);
    if (!wrap) return;
    opts = opts || {};
    var readonly = !!opts.readonly;
    var days = weekDates(new Date());
    var weekStartKey = ymd(days[0]);
    if (!items.length) {
      wrap.innerHTML = '<p class="habit-empty">' + (opts.empty || 'No habits yet.') + '</p>';
      return;
    }
    wrap.innerHTML = items.map(function (habit) {
      var streak = streakFor(store, habit);
      var isWeekly = habit.cadence === 'weekly';
      var cells;
      if (isWeekly) {
        var on = isChecked(store, habit.id, weekStartKey);
        cells = days.map(function (d, i) {
          if (i === WEEKLY_CHECK_COL) {
            var disabled = readonly ? ' disabled' : '';
            return '<button type="button" class="habit-check' + (on ? ' on' : '') + '" data-habit="' + habit.id + '" data-day="' + weekStartKey + '"' + disabled + ' aria-pressed="' + (on ? 'true' : 'false') + '" aria-label="' + habit.name + ' this week">' + (on ? '✓' : '') + '</button>';
          }
          return '<span class="habit-check weekly-spacer" aria-hidden="true"></span>';
        }).join('');
      } else {
        cells = days.map(function (d) {
          var key = ymd(d);
          var on = isChecked(store, habit.id, key);
          var disabled = readonly ? ' disabled' : '';
          return '<button type="button" class="habit-check' + (on ? ' on' : '') + '" data-habit="' + habit.id + '" data-day="' + key + '"' + disabled + ' aria-pressed="' + (on ? 'true' : 'false') + '" aria-label="' + habit.name + ' ' + key + '">' + (on ? '✓' : '') + '</button>';
        }).join('');
      }
      var shareBtn = readonly
        ? '<span class="habit-share-btn shared">Shared</span>'
        : '<button type="button" class="habit-share-btn' + (habit.shared ? ' shared' : '') + '" data-share="' + habit.id + '">' + (habit.shared ? 'Shared' : 'Private') + '</button>';
      return '<div class="habit-row' + (isWeekly ? ' weekly-row' : '') + '" data-habit-row="' + habit.id + '">' +
        '<div class="hr-meta"><div class="hr-name">' + escapeHtml(habit.name) + '</div>' +
        '<div class="hr-sub">' + (isWeekly ? 'Weekly' : 'Daily') +
        (streak ? ' · <span class="hr-streak">' + streak + (isWeekly ? '-week' : '-day') + ' streak</span>' : '') + '</div></div>' +
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
    var days = weekDates(new Date());
    renderDayHead('habitDayHead', days);
    renderDayHead('brotherDayHead', days);
    renderHabitStats(store);
    renderHabitRows('habitRows', store.habits.items, store, { readonly: false });

    var brother = store.brotherPack || null;
    var hint = el('brotherHabitsHint');
    if (!brother || !brother.items || !brother.items.length) {
      if (hint) hint.textContent = 'No brother pack yet — pair by email above, or import a JSON pack.';
      renderHabitRows('brotherHabitRows', [], store, { empty: 'Pair or import to see the habits he marked Shared.' });
      return;
    }
    if (hint) {
      hint.textContent = (brother.name ? brother.name + ' · ' : '') +
        (brother.live ? 'Live from cloud' : 'Imported') +
        (brother.importedAt ? ' · ' + formatSyncTime(brother.importedAt) : '') +
        '. Read-only Shared habits.';
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
    var weekStart = ymd(sundayOf(new Date(payload.submittedAt || Date.now())));
    if (payload.battleBrotherCall === 'Yes') setChecked(store, 'bb_call', weekStart, true);
    if (payload.armadaCall === 'Yes') setChecked(store, 'armada_call', weekStart, true);
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
    scheduleCloudPush();
  }

  var cloudPushTimer = null;
  var cloudUpdatedAt = null;
  var cloudAvailable = false;
  var lastCloudStatusText = '';
  var lastPushedFingerprint = '';
  var lastBrotherFingerprint = '';

  function formatSyncTime(iso) {
    if (!iso) return '';
    var d = new Date(iso);
    return d.toLocaleDateString() + ', ' + d.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' });
  }

  function cloudStateFingerprint() {
    try {
      return JSON.stringify(cloudStatePayload());
    } catch (e) {
      return '';
    }
  }

  function scheduleCloudPush() {
    if (!window.BBCloud) return;
    var sess = BBCloud.loadSession();
    if (!sess || !sess.sessionToken) return;
    clearTimeout(cloudPushTimer);
    cloudPushTimer = setTimeout(function () {
      var fp = cloudStateFingerprint();
      if (fp && fp === lastPushedFingerprint) return;
      pushCloudState(false);
    }, 2500);
  }

  function cloudStatePayload() {
    var store = loadStore();
    return {
      profile: store.profile || {},
      habits: store.habits || { items: [], checks: {} },
      submissions: (store.submissions || []).slice(0, 52),
      brotherPack: store.brotherPack || null,
    };
  }

  function applyCloudState(state, updatedAt) {
    if (!state || typeof state !== 'object') return;
    var store = loadStore();
    if (state.profile) store.profile = state.profile;
    if (state.habits) store.habits = state.habits;
    if (Array.isArray(state.submissions)) store.submissions = state.submissions.slice(0, 52);
    if (state.brotherPack) store.brotherPack = state.brotherPack;
    ensureHabits(store);
    cloudUpdatedAt = updatedAt || cloudUpdatedAt;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
    } catch (e) {}
    if (store.profile && store.profile.name && !val('reporterName')) {
      setVal('reporterName', store.profile.name);
    }
    renderHistory();
    if (currentMode === 'habits') renderHabitBoard();
  }

  async function pushCloudState(manual) {
    if (!window.BBCloud) return;
    var sess = BBCloud.loadSession();
    if (!sess || !sess.sessionToken) return;
    setCloudStatus(manual ? 'Syncing…' : '');
    try {
      var r = await BBCloud.pushSync(cloudStatePayload(), cloudUpdatedAt);
      if (r.status === 409 && r.data && r.data.state) {
        applyCloudState(r.data.state, r.data.updatedAt);
        setCloudStatus('Server had newer data — loaded from cloud.');
        flash('Cloud had a newer copy — board refreshed.');
        return;
      }
      if (r.ok && r.data && r.data.updatedAt) {
        cloudUpdatedAt = r.data.updatedAt;
        lastPushedFingerprint = cloudStateFingerprint();
        setCloudStatus('Synced · ' + formatSyncTime(cloudUpdatedAt));
        if (manual) flash('Synced to cloud.');
        await refreshBrotherFromCloud();
        return;
      }
      if (r.status === 401) {
        await renderAccountUI();
        setCloudStatus('Session expired — sign in again.');
        return;
      }
      setCloudStatus('Sync failed' + (r.data && r.data.error ? ' (' + r.data.error + ')' : '') + '.');
    } catch (e) {
      setCloudStatus('Sync offline — local save still works.');
    }
  }

  async function pullCloudState(manual) {
    if (!window.BBCloud) return;
    var sess = BBCloud.loadSession();
    if (!sess || !sess.sessionToken) return;
    try {
      var r = await BBCloud.pullSync();
      if (r.ok && r.data && r.data.state) {
        applyCloudState(r.data.state, r.data.updatedAt);
        lastPushedFingerprint = cloudStateFingerprint();
        setCloudStatus('Loaded from cloud' + (cloudUpdatedAt ? ' · ' + formatSyncTime(cloudUpdatedAt) : ''));
        if (manual) flash('Loaded cloud memory.');
      } else if (r.ok && r.data && !r.data.state) {
        // First sign-in — push local up.
        await pushCloudState(manual);
      } else if (r.status === 401) {
        await renderAccountUI();
      }
      await refreshBrotherFromCloud();
    } catch (e) {
      setCloudStatus('Could not reach cloud.');
    }
  }

  async function refreshBrotherFromCloud() {
    if (!window.BBCloud) return;
    var sess = BBCloud.loadSession();
    if (!sess || !sess.sessionToken) return;
    try {
      var r = await BBCloud.fetchBrotherPack();
      if (!r.ok || !r.data) return;
      var store = loadStore();
      if (r.data.pack && r.data.pack.items) {
        var fp = JSON.stringify({
          items: r.data.pack.items,
          checks: r.data.pack.checks || {},
          updatedAt: r.data.updatedAt || '',
        });
        if (fp === lastBrotherFingerprint) return;
        lastBrotherFingerprint = fp;
        store.brotherPack = {
          name: (r.data.brother && (r.data.brother.name || r.data.brother.email)) || r.data.pack.name || 'Battle Brother',
          importedAt: r.data.updatedAt || new Date().toISOString(),
          items: r.data.pack.items,
          checks: r.data.pack.checks || {},
          live: true,
        };
        try { localStorage.setItem(STORAGE_KEY, JSON.stringify(store)); } catch (e) {}
        if (currentMode === 'habits') renderHabitBoard();
      }
    } catch (e) {}
  }

  function setCloudStatus(msg) {
    msg = msg || '';
    if (msg === lastCloudStatusText) return;
    lastCloudStatusText = msg;
    var node = el('cloudStatus');
    if (node) node.textContent = msg;
    var bar = el('memoryBarText');
    if (bar) {
      var sess = window.BBCloud && BBCloud.loadSession();
      bar.textContent = sess && sess.sessionToken
        ? 'Signed in — local + cloud sync.'
        : 'Saved locally — sign in above to sync across devices.';
    }
  }

  function showAuthPanel(panel) {
    ['authSignInPanel', 'authRegisterPanel', 'authResetPanel'].forEach(function (id) {
      var node = el(id);
      if (node) node.hidden = id !== panel;
    });
  }

  async function renderAccountUI() {
    var signedOut = el('accountSignedOut');
    var signedIn = el('accountSignedIn');
    var who = el('accountWho');
    var unlink = el('btnPairUnlink');
    var pairStatus = el('pairStatus');
    var pairWhenUnlinked = el('pairWhenUnlinked');
    var sharePack = el('sharePackSection');
    var hint = el('accountHint');
    if (!window.BBCloud) {
      if (hint) hint.textContent = 'Cloud client missing.';
      return;
    }
    var sess = BBCloud.loadSession();
    if (!sess || !sess.sessionToken) {
      if (signedOut) signedOut.hidden = false;
      if (signedIn) signedIn.hidden = true;
      if (sharePack) sharePack.hidden = false;
      if (hint) hint.textContent = 'Sign in with email + PIN to keep habits on every device. Local save still works offline.';
      setCloudStatus(cloudAvailable ? 'Cloud API reachable — sign in to sync.' : 'Cloud API not deployed yet — local + pack sharing still work.');
      return;
    }
    if (signedOut) signedOut.hidden = true;
    if (signedIn) signedIn.hidden = false;
    var label = (sess.user && (sess.user.name || sess.user.email)) || 'Captain';
    var paired = !!(sess.brother && (sess.brother.email || sess.brother.name));
    if (paired) {
      label += ' · paired with ' + (sess.brother.name || sess.brother.email);
      if (unlink) unlink.hidden = false;
      if (pairWhenUnlinked) pairWhenUnlinked.hidden = true;
      if (pairStatus) pairStatus.textContent = 'Live Shared habits sync with your brother.';
      if (sharePack) sharePack.hidden = true;
    } else {
      if (unlink) unlink.hidden = true;
      if (pairWhenUnlinked) pairWhenUnlinked.hidden = false;
      if (pairStatus) pairStatus.textContent = 'Invite your Battle Brother by email, or accept his code.';
      if (sharePack) sharePack.hidden = false;
    }
    if (who) who.textContent = label;
    if (hint) hint.textContent = 'Signed in. Habits sync to the cloud; Shared habits appear for your paired brother.';
  }

  async function handleSignIn() {
    var email = val('authEmail');
    var pin = val('authPin');
    if (!email || !pin) { flash('Enter email and PIN.'); return; }
    var status = el('authStatus');
    if (status) status.textContent = 'Signing in…';
    try {
      var r = await BBCloud.login(email, pin);
      if (!r.ok) {
        var err = (r.data && (r.data.message || r.data.error)) || 'Sign-in failed';
        if (status) status.textContent = err;
        if (r.data && r.data.error === 'no_pin_set') {
          flash('No PIN yet — use magic link once in a browser, then set a PIN.');
        }
        return;
      }
      await BBCloud.me();
      await renderAccountUI();
      await pullCloudState(false);
      if (status) status.textContent = '';
      flash('Signed in.');
    } catch (e) {
      if (status) status.textContent = 'Cloud API unreachable.';
    }
  }

  async function handleRegister() {
    var email = val('authEmailReg') || val('authEmail');
    var pin = val('authPinReg');
    var name = val('authName') || val('reporterName');
    if (!email || !pin) { flash('Enter email and choose a PIN (6+ characters).'); return; }
    if (pin.length < 6) { flash('PIN must be at least 6 characters.'); return; }
    var status = el('authStatus');
    if (status) status.textContent = 'Creating account…';
    try {
      var r = await BBCloud.register(email, pin, name);
      if (!r.ok) {
        if (status) status.textContent = (r.data && (r.data.message || r.data.error)) || 'Could not create account';
        return;
      }
      await BBCloud.me();
      await renderAccountUI();
      await pushCloudState(true);
      if (status) status.textContent = '';
      flash('Account created — signed in.');
      showAuthPanel('authSignInPanel');
    } catch (e) {
      if (status) status.textContent = 'Cloud API unreachable.';
    }
  }

  async function handleRequestResetCode() {
    var email = val('authEmailReset') || val('authEmail');
    if (!email) { flash('Enter your email.'); return; }
    var status = el('authStatus');
    try {
      var r = await BBCloud.requestPinReset(email);
      if (status) status.textContent = (r.data && r.data.message) || 'Reset code sent if account exists.';
      if (r.data && r.data.devResetCode) {
        setVal('authResetCode', r.data.devResetCode);
        flash('Dev reset code filled in (email not configured).');
      }
    } catch (e) {
      if (status) status.textContent = 'Could not reach cloud API.';
    }
  }

  async function handleConfirmReset() {
    var email = val('authEmailReset') || val('authEmail');
    var code = val('authResetCode');
    var pin = val('authPinReset');
    if (!email || !code || !pin) { flash('Email, reset code, and new PIN required.'); return; }
    if (pin.length < 6) { flash('PIN must be at least 6 characters.'); return; }
    var r = await BBCloud.confirmPinReset(email, code, pin);
    if (r.ok) {
      flash('PIN updated — sign in now.');
      showAuthPanel('authSignInPanel');
      setVal('authEmail', email);
      setVal('authPin', '');
    } else {
      flash((r.data && (r.data.message || r.data.error)) || 'Reset failed.');
    }
  }

  async function handleMagicLinkClick() {
    var email = val('authEmail');
    if (!email) { flash('Enter your email.'); return; }
    var status = el('authStatus');
    if (status) status.textContent = 'Sending magic link…';
    try {
      var r = await BBCloud.requestMagicLink(email);
      if (!r.ok) {
        if (status) status.textContent = 'Could not request link' + (r.data && r.data.error ? ': ' + r.data.error : '');
        return;
      }
      if (r.data && r.data.emailed) {
        if (status) status.textContent = 'Check your email for the sign-in link (expires in 20 minutes).';
        flash('Magic link sent.');
      } else if (r.data && r.data.devMagicUrl) {
        if (status) status.textContent = 'Email not configured on the API yet. Dev link ready — opening…';
        window.location.href = r.data.devMagicUrl;
      } else {
        if (status) status.textContent = r.data && r.data.message ? r.data.message : 'Request sent.';
      }
    } catch (e) {
      if (status) status.textContent = 'Cloud API unreachable. Deploy workers/battle-bro-sync (see README).';
      flash('Cloud API offline.');
    }
  }

  async function completeMagicFromUrl() {
    var params = new URLSearchParams(window.location.search);
    var magic = params.get('magic');
    if (!magic || !window.BBCloud) return;
    flash('Signing in…');
    var r = await BBCloud.verifyMagic(magic, val('reporterName'));
    if (r.ok) {
      // Strip magic from URL
      try {
        params.delete('magic');
        var qs = params.toString();
        window.history.replaceState({}, '', window.location.pathname + (qs ? '?' + qs : '') + window.location.hash);
      } catch (e) {}
      await renderAccountUI();
      await pullCloudState(false);
      flash('Signed in. Cloud sync is on.');
      // Prompt magic-link users to set a PIN for PWA re-login
      if (r.data && r.data.user && !r.data.user.hasPin) {
        setTimeout(function () {
          var pin = window.prompt('Set a PIN (6+ characters) for sign-in on this app — no magic link needed next time:');
          if (pin && pin.length >= 6) {
            BBCloud.setPin(pin).then(function (res) {
              if (res.ok) flash('PIN saved — use email + PIN to sign in.');
            });
          }
        }, 400);
      }
    } else {
      flash('Sign-in link invalid or expired. Request a new one.');
    }
  }

  async function handleInviteFromUrl() {
    var params = new URLSearchParams(window.location.search);
    var invite = params.get('invite');
    if (!invite) return;
    setVal('pairCode', invite);
    setMode('habits');
    var sess = window.BBCloud && BBCloud.loadSession();
    if (sess && sess.sessionToken) {
      // auto-attempt accept
      await handlePairAccept();
    } else {
      flash('Sign in with the invited email, then accept the code.');
    }
  }

  async function handlePairInvite() {
    var email = val('pairEmail');
    if (!email) { flash('Enter your brother\'s email.'); return; }
    var r = await BBCloud.inviteBrother(email);
    var status = el('pairStatus');
    if (r.ok && r.data) {
      if (status) {
        status.textContent = 'Invite code ' + r.data.code + ' — send it to him, or share ' + r.data.acceptUrl;
      }
      flash('Invite created' + (r.data.code ? ': ' + r.data.code : ''));
    } else {
      flash((r.data && r.data.error) || 'Invite failed.');
    }
  }

  async function handlePairAccept() {
    var code = val('pairCode');
    if (!code) { flash('Enter the invite code.'); return; }
    var r = await BBCloud.acceptInvite(code);
    if (r.ok) {
      await BBCloud.me();
      await renderAccountUI();
      await refreshBrotherFromCloud();
      flash('Paired. Shared habits will sync live.');
    } else {
      flash((r.data && r.data.error) || 'Could not accept invite.');
    }
  }

  function themeByWeek(n) {
    return THEMES.find(function (t) { return t.week === n; }) || THEMES[6];
  }

  /** Sunday 00:00 local — start of the Armada theme week (Sun–Sat). */
  function sundayOf(date) {
    var d = new Date(date.getFullYear(), date.getMonth(), date.getDate());
    d.setDate(d.getDate() - d.getDay());
    d.setHours(0, 0, 0, 0);
    return d;
  }

  /**
   * Current Armada week from the calendar (Sun–Sat cycle).
   * Anchored to Sabbath week opening Sun 2026-07-05.
   */
  function calendarWeek(now) {
    var today = now || new Date();
    var thisSun = sundayOf(today);
    var anchor = new Date(ARMADA_ANCHOR.y, ARMADA_ANCHOR.m, ARMADA_ANCHOR.d);
    anchor = sundayOf(anchor);
    var msPerWeek = 7 * 24 * 60 * 60 * 1000;
    var elapsed = Math.floor((thisSun - anchor) / msPerWeek);
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

    // Cloud account wiring
    if (el('btnSignIn')) el('btnSignIn').addEventListener('click', handleSignIn);
    if (el('btnRegister')) el('btnRegister').addEventListener('click', handleRegister);
    if (el('btnShowRegister')) el('btnShowRegister').addEventListener('click', function () { showAuthPanel('authRegisterPanel'); });
    if (el('btnShowSignIn')) el('btnShowSignIn').addEventListener('click', function () { showAuthPanel('authSignInPanel'); });
    if (el('btnShowReset')) el('btnShowReset').addEventListener('click', function () { showAuthPanel('authResetPanel'); });
    if (el('btnResetBack')) el('btnResetBack').addEventListener('click', function () { showAuthPanel('authSignInPanel'); });
    if (el('btnRequestResetCode')) el('btnRequestResetCode').addEventListener('click', handleRequestResetCode);
    if (el('btnConfirmReset')) el('btnConfirmReset').addEventListener('click', handleConfirmReset);
    if (el('authPin')) el('authPin').addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); handleSignIn(); }
    });
    if (el('btnMagicLink')) el('btnMagicLink').addEventListener('click', handleMagicLinkClick);
    if (el('btnLogout')) el('btnLogout').addEventListener('click', async function () {
      await BBCloud.logout();
      await renderAccountUI();
      flash('Signed out. Local memory stays on this device.');
    });
    if (el('btnSyncNow')) el('btnSyncNow').addEventListener('click', async function () {
      await pushCloudState(true);
      await pullCloudState(false);
    });
    if (el('btnPairInvite')) el('btnPairInvite').addEventListener('click', handlePairInvite);
    if (el('btnPairAccept')) el('btnPairAccept').addEventListener('click', handlePairAccept);
    if (el('btnPairUnlink')) el('btnPairUnlink').addEventListener('click', async function () {
      await BBCloud.unlinkBrother();
      await BBCloud.me();
      await renderAccountUI();
      flash('Unlinked.');
    });

    (async function bootCloud() {
      if (!window.BBCloud) return;
      cloudAvailable = await BBCloud.health();
      if (BBCloud.loadSession()) {
        var me = await BBCloud.me();
        if (me.status === 401) BBCloud.saveSession(null);
      }
      await renderAccountUI();
      await completeMagicFromUrl();
      if (BBCloud.loadSession()) await pullCloudState(false);
      await handleInviteFromUrl();
    })();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
