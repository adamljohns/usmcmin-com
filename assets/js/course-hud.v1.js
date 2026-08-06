/*
 * course-hud.v1.js — per-page progress HUD for the Watchman's Course
 * (ai-mission-week-*.html) and the Family Captain AI Boot Camp
 * (ai-boot-camp-*.html).
 *
 * Both courses already track completion, but only on their voyage/log page.
 * Open week 7 and there was nothing: no percentage, no time, no sense of
 * where you are in a twelve-week course. This puts the same numbers on every
 * page, reading the SAME localStorage keys the voyage page writes, so the two
 * can never disagree — this file adds no new source of truth for completion.
 *
 * What it adds that did not exist anywhere: a session timer. The Husband
 * Course logs time across modules ("course total 0 sec"); these two logged
 * none. Time accrues only while the tab is visible, so leaving a tab open
 * overnight does not credit eight hours of study.
 *
 * Local-only, like the rest of both courses: no account, no sync, no network.
 */
(function () {
  'use strict';

  var COURSES = {
    watchman: {
      label: "The Watchman's Course",
      progressKey: 'watchman_mission_progress_v1',
      notesKey: 'watchman_mission_notes_v1',
      timeKey: 'watchman_mission_time_v1',
      total: 36,
      units: 12,
      voyage: 'ai-mission-voyage.html',
      unitHref: function (n) { return 'ai-mission-week-' + n + '.html'; },
      unitWord: 'Week'
    },
    'family-captain': {
      label: 'Family Captain AI Boot Camp',
      progressKey: 'usmc_voyage_progress_v1',
      notesKey: 'fc_voyage_notes_v1',
      timeKey: 'fc_voyage_time_v1',
      total: 15,
      units: 5,
      voyage: 'ai-boot-camp-voyage.html',
      unitHref: null,
      unitWord: 'Stage'
    }
  };

  function readJSON(key) {
    try { return JSON.parse(localStorage.getItem(key)) || {}; } catch (e) { return {}; }
  }
  function writeJSON(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) { /* private mode */ }
  }

  function countTrue(obj) {
    var n = 0;
    for (var k in obj) { if (Object.prototype.hasOwnProperty.call(obj, k) && obj[k]) n++; }
    return n;
  }

  // Notes are stored as an id -> string map; blank textareas should not count
  // as work done, so only non-empty values are tallied.
  function countNotes(obj) {
    var n = 0;
    for (var k in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, k)) {
        var v = obj[k];
        if (typeof v === 'string' && v.trim()) n++;
      }
    }
    return n;
  }

  function fmtTime(sec) {
    sec = Math.max(0, Math.round(sec));
    if (sec < 60) return sec + ' sec';
    var m = Math.round(sec / 60);
    if (m < 60) return m + ' min';
    var h = Math.floor(m / 60);
    return h + 'h ' + (m % 60) + 'm';
  }

  function build(host, cfg) {
    host.classList.add('course-hud');
    host.innerHTML =
      '<div class="course-hud-ring" aria-hidden="true"><span data-hud-pct>0%</span></div>' +
      '<div class="course-hud-body">' +
        '<div class="course-hud-title">' + cfg.label + '</div>' +
        '<div class="course-hud-bar" role="progressbar" aria-label="Course progress"' +
          ' aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" data-hud-barwrap>' +
          '<span data-hud-bar></span></div>' +
        '<div class="course-hud-sub">' +
          '<span data-hud-summary>0 of ' + cfg.total + ' complete</span>' +
          ' &middot; <span data-hud-notes>0 notes</span>' +
          ' &middot; <span data-hud-time>0 sec</span> logged' +
        '</div>' +
      '</div>' +
      '<a class="course-hud-link" href="' + cfg.voyage + '">Field notes &rarr;</a>';
    return {
      pct: host.querySelector('[data-hud-pct]'),
      bar: host.querySelector('[data-hud-bar]'),
      barWrap: host.querySelector('[data-hud-barwrap]'),
      summary: host.querySelector('[data-hud-summary]'),
      notes: host.querySelector('[data-hud-notes]'),
      time: host.querySelector('[data-hud-time]')
    };
  }

  // Both courses put a position:fixed nav at the top of the document and let
  // the hero clear it with its own padding. The HUD sits ABOVE the hero, so it
  // has to clear that nav itself or it renders underneath it — which is
  // exactly what happened on first deploy. Measure rather than hardcode 70px,
  // so this keeps working if the nav height ever changes.
  function clearFixedHeader(host) {
    var tallest = 0;
    var candidates = document.querySelectorAll('nav, header, .site-header, .navbar');
    for (var i = 0; i < candidates.length; i++) {
      var el = candidates[i];
      var cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      var r = el.getBoundingClientRect();
      if (r.top <= 2 && r.height > tallest) tallest = r.height;
    }
    host.style.setProperty('--hud-clear', Math.round(tallest) + 'px');
  }

  function init() {
    var host = document.querySelector('[data-course-hud]');
    if (!host) return;
    var cfg = COURSES[host.getAttribute('data-course-hud')];
    if (!cfg) return;

    var el = build(host, cfg);
    clearFixedHeader(host);
    window.addEventListener('resize', function () { clearFixedHeader(host); });

    // ---- session timer -----------------------------------------------------
    // Only counts visible time, flushed on a short interval and on unload so a
    // closed tab still records what it earned.
    var accrued = 0;
    try { accrued = Number(localStorage.getItem(cfg.timeKey)) || 0; } catch (e) { accrued = 0; }
    var session = 0;
    var last = Date.now();

    function tick() {
      var now = Date.now();
      if (!document.hidden) {
        var delta = (now - last) / 1000;
        // A delta far larger than the interval means the machine slept or the
        // tab was throttled; credit the interval, not the gap.
        session += delta > 30 ? 5 : delta;
      }
      last = now;
      paint();
    }

    function flush() {
      try { localStorage.setItem(cfg.timeKey, String(accrued + session)); } catch (e) { /* ignore */ }
    }

    function paint() {
      var done = countTrue(readJSON(cfg.progressKey));
      var pct = cfg.total ? Math.round((done / cfg.total) * 100) : 0;
      if (pct > 100) pct = 100;
      el.pct.textContent = pct + '%';
      el.bar.style.width = pct + '%';
      el.barWrap.setAttribute('aria-valuenow', String(pct));
      host.style.setProperty('--hud-pct', pct);
      el.summary.textContent = done + ' of ' + cfg.total + ' complete';
      var notes = countNotes(readJSON(cfg.notesKey));
      el.notes.textContent = notes + (notes === 1 ? ' note' : ' notes');
      el.time.textContent = fmtTime(accrued + session);
    }

    paint();
    setInterval(tick, 5000);
    setInterval(flush, 15000);
    document.addEventListener('visibilitychange', function () { last = Date.now(); flush(); });
    window.addEventListener('pagehide', flush);
    window.addEventListener('beforeunload', flush);

    // Another tab (typically the voyage page) ticking a task should update
    // this HUD live rather than showing a stale count.
    window.addEventListener('storage', function (e) {
      if (!e.key || e.key === cfg.progressKey || e.key === cfg.notesKey) paint();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
