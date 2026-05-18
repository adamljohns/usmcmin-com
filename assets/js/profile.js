/* RESOLUTE Citizen Scorecard — profile-page client-side scripts.
 *
 * All five DOM-side concerns that don't need per-candidate template
 * variables, bundled here so the browser caches them once and reuses
 * across every profile-to-profile navigation:
 *   1. Page-view counter (Goatcounter API call)
 *   2. Keyboard prev/next (left/right arrow keys -> a.prof-nav-btn)
 *   3. Jump-to dropdown + Prev/Next sort override (reads data-state attr)
 *   4. Mobile nav-toggle hamburger
 *   5. Light/dark theme toggle
 *
 * Originally inlined into every profile.html via generate-profiles.py
 * (~8 KB × ~8,670 profiles = ~70 MB of duplicated JS). Extracted on
 * 2026-04-29 alongside profile.css.
 *
 * EDIT THIS FILE DIRECTLY. Profile HTML regen does NOT regenerate this
 * JS — generate-profiles.py just emits a <script src> to it.
 */

(function(){
  var p = window.location.pathname;
  fetch('https://usmcmin.goatcounter.com/counter/' + encodeURIComponent(p) + '.json')
    .then(function(r){ return r.json(); })
    .then(function(d){
      var el = document.getElementById('pageViews');
      if (el && d && typeof d.count !== 'undefined') el.textContent = d.count + ' views';
    })
    .catch(function(){});
})();

(function(){
  document.addEventListener('keydown', function(e){
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    var dir = e.key === 'ArrowLeft' ? 'prev' : 'next';
    var btn = document.querySelector('a.prof-nav-btn[data-direction="' + dir + '"]');
    if (btn && btn.href) { window.location.href = btn.href; }
  });
})();

(function(){
  var sel = document.getElementById('profJumpSelect');
  if (!sel) return;
  var st = (sel.getAttribute('data-state') || 'VA').toLowerCase();
  var currentSlug = sel.getAttribute('data-current-slug') || '';

  // ---- Score helpers (mirror server-side, no categories needed) ----
  // Per-state JSONs do not include the categories array, so we compute the
  // total directly by walking the keys of candidate.scores.
  var POINTS_PER_TRUE = 2;
  function calcTotal(scores){
    if (!scores) return 0;
    var t = 0;
    for (var k in scores) {
      if (!Object.prototype.hasOwnProperty.call(scores, k)) continue;
      var arr = scores[k] || [];
      for (var i = 0; i < arr.length; i++) {
        if (arr[i] === true) t += POINTS_PER_TRUE;
      }
    }
    return t;
  }

  var LEVEL_RANK = { executive: 1, judicial: 2, federal: 3, state: 4, local: 5 };
  var PARTY_RANK = { R: 1, D: 2, I: 3 };

  function makeComparator(sortKey){
    function totalOf(c){ return calcTotal(c.scores); }
    function nameTie(a, b){ return (a.name||'').toLowerCase().localeCompare((b.name||'').toLowerCase()); }
    switch (sortKey) {
      case 'score-asc':
        return function(a, b){ return (totalOf(a) - totalOf(b)) || nameTie(a, b); };
      case 'name':
        return nameTie;
      case 'level-score':
        return function(a, b){
          return ((LEVEL_RANK[a.level]||6) - (LEVEL_RANK[b.level]||6))
              || (totalOf(b) - totalOf(a))
              || nameTie(a, b);
        };
      case 'jurisdiction-score':
        return function(a, b){
          return ((a.jurisdiction||'').toLowerCase().localeCompare((b.jurisdiction||'').toLowerCase()))
              || (totalOf(b) - totalOf(a))
              || nameTie(a, b);
        };
      case 'party-score':
        return function(a, b){
          return ((PARTY_RANK[a.party]||4) - (PARTY_RANK[b.party]||4))
              || (totalOf(b) - totalOf(a))
              || nameTie(a, b);
        };
      case 'score-desc':
      default:
        return function(a, b){ return (totalOf(b) - totalOf(a)) || nameTie(a, b); };
    }
  }

  var SORT_LABELS = {
    'score-desc': 'Score High → Low',
    'score-asc': 'Score Low → High',
    'name': 'Name A → Z',
    'level-score': 'Level + Score',
    'jurisdiction-score': 'Jurisdiction + Score',
    'party-score': 'Party + Score'
  };

  function activeSort(){
    var fromUrl = null;
    try { fromUrl = new URL(window.location).searchParams.get('sort'); } catch(e) {}
    var fromStorage = null;
    try { fromStorage = localStorage.getItem('rc-sort'); } catch(e) {}
    var v = fromUrl || fromStorage;
    return SORT_LABELS[v] ? v : null; // null = no override, keep static order
  }

  function buildNavBtnHtml(neighbor, direction, arrow){
    if (!neighbor) {
      return '<span class="prof-nav-btn prof-nav-disabled">' + arrow + '</span>';
    }
    var name = (neighbor.name || '').replace(/[<>]/g, '');
    var office = (neighbor.office || '').replace(/[<>]/g, '');
    var href = (neighbor.slug || '') + '.html';
    return '<a class="prof-nav-btn" href="' + href + '" data-direction="' + direction + '">'
      + '<span class="prof-nav-arrow">' + arrow + '</span>'
      + '<span class="prof-nav-text"><span class="prof-nav-name">' + name + '</span>'
      + '<span class="prof-nav-office">' + office + '</span></span></a>';
  }

  function rerenderNav(prev, next, position, total, sortLabel){
    var bars = document.querySelectorAll('.prof-nav-bar');
    var prevHtml = buildNavBtnHtml(prev, 'prev', '← Prev');
    var nextHtml = buildNavBtnHtml(next, 'next', 'Next →');
    var posHtml = '<div class="prof-nav-position">' + position + ' of ' + total
                + (sortLabel ? ' &middot; ' + sortLabel : '') + '</div>';
    bars.forEach(function(bar){
      bar.innerHTML = prevHtml + posHtml + nextHtml;
    });
  }

  fetch('../../data/states/' + st + '.json')
    .then(function(r){ return r.json(); })
    .then(function(data){
      var cands = (data && data.candidates) || [];

      // ---- Jump-to dropdown (alphabetical within jurisdiction groups) ----
      var groups = {};
      cands.forEach(function(c){
        var j = c.jurisdiction || 'Other';
        if (!groups[j]) groups[j] = [];
        groups[j].push(c);
      });
      var groupNames = Object.keys(groups).sort();
      sel.innerHTML = '<option value="">Jump to another official…</option>';
      groupNames.forEach(function(g){
        var og = document.createElement('optgroup');
        og.label = g + ' (' + groups[g].length + ')';
        groups[g].sort(function(a, b){
          return (a.name || '').localeCompare(b.name || '');
        });
        groups[g].forEach(function(c){
          var opt = document.createElement('option');
          opt.value = c.slug + '.html';
          opt.textContent = c.name + (c.office ? ' — ' + c.office : '');
          if (c.slug === currentSlug) {
            opt.selected = true;
            opt.textContent = '★ ' + opt.textContent + ' (current)';
          }
          og.appendChild(opt);
        });
        sel.appendChild(og);
      });
      sel.addEventListener('change', function(){
        if (sel.value) window.location.href = sel.value;
      });

      // ---- Prev/Next sort override ----
      // If no sort is active, leave the baked-in static order alone.
      var sortKey = activeSort();
      if (!sortKey) return;
      var sorted = cands.slice().sort(makeComparator(sortKey));
      var idx = -1;
      for (var i = 0; i < sorted.length; i++) {
        if (sorted[i].slug === currentSlug) { idx = i; break; }
      }
      if (idx === -1) return;
      var prev = idx > 0 ? sorted[idx - 1] : null;
      var next = idx < sorted.length - 1 ? sorted[idx + 1] : null;
      rerenderNav(prev, next, idx + 1, sorted.length, SORT_LABELS[sortKey]);
    })
    .catch(function(){
      sel.innerHTML = '<option value="">Could not load officials list</option>';
    });
})();

(function() {
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function() { navLinks.classList.toggle('open'); });
  }
})();

// ─── Share button (X / email / SMS / copy-link) ──────────────────────────
// Pre-fills text mentioning the candidate's name + RESOLUTE Citizen
// branding. URL is built from window.location so it works on local +
// production. Copy-link triggers a 1.5s "Copied!" feedback.
(function() {
  var menu = document.querySelector('.prof-share-menu');
  if (!menu) return;
  menu.addEventListener('click', function(e) {
    var btn = e.target.closest('.prof-share-opt');
    if (!btn) return;
    var kind = btn.getAttribute('data-share');
    var name = btn.getAttribute('data-name') || 'this candidate';
    var url = window.location.href.split('#')[0];
    var msg = 'RESOLUTE Citizen Scorecard: ' + name + ' — see the full record';
    var encoded = encodeURIComponent(msg + ' ' + url);
    if (kind === 'x') {
      window.open('https://twitter.com/intent/tweet?text=' + encoded, '_blank', 'noopener');
    } else if (kind === 'email') {
      window.location.href = 'mailto:?subject=' + encodeURIComponent('RESOLUTE Citizen Scorecard: ' + name)
        + '&body=' + encodeURIComponent(msg + '\n\n' + url + '\n\nFrom USMC Ministries.');
    } else if (kind === 'sms') {
      window.location.href = 'sms:?&body=' + encoded;
    } else if (kind === 'copy') {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function() {
          btn.classList.add('copied');
          var prev = btn.textContent;
          btn.textContent = 'Copied!';
          setTimeout(function() {
            btn.classList.remove('copied');
            btn.textContent = prev;
          }, 1500);
        });
      } else {
        var ta = document.createElement('textarea');
        ta.value = url;
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); } catch (err) {}
        document.body.removeChild(ta);
        btn.classList.add('copied');
        setTimeout(function() { btn.classList.remove('copied'); }, 1500);
      }
    }
    if (kind !== 'copy') {
      var details = btn.closest('details');
      if (details) details.open = false;
    }
  });
  document.addEventListener('click', function(e) {
    var details = document.querySelector('.prof-share');
    if (details && details.open && !details.contains(e.target)) {
      details.open = false;
    }
  });
})();

// ─── Sticky TOC: highlight the currently-visible section ──────────────────
// Uses IntersectionObserver — simple, no scroll-listener perf cost. Section
// with the highest intersection ratio wins the .active class.
(function() {
  var tocLinks = document.querySelectorAll('.prof-toc-link');
  if (!tocLinks.length) return;
  var byTarget = {};
  tocLinks.forEach(function(l) { byTarget[l.getAttribute('data-target')] = l; });

  var activeId = null;
  function setActive(id) {
    if (id === activeId) return;
    activeId = id;
    tocLinks.forEach(function(l) {
      l.classList.toggle('active', l.getAttribute('data-target') === id);
    });
  }

  var visible = new Map();
  var io = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) visible.set(e.target.id, e.intersectionRatio);
      else visible.delete(e.target.id);
    });
    if (visible.size === 0) return;
    var ids = Array.from(visible.keys());
    var ratios = Array.from(visible.values());
    var maxR = Math.max.apply(null, ratios);
    var winner = ids[ratios.indexOf(maxR)];
    setActive(winner);
  }, { rootMargin: '-80px 0px -50% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] });

  Object.keys(byTarget).forEach(function(id) {
    var el = document.getElementById(id);
    if (el) io.observe(el);
  });
})();

(function() {
  var toggle = document.getElementById('themeToggle');
  var saved = localStorage.getItem('usmc-theme');
  if (saved !== 'light') {
    document.documentElement.setAttribute('data-theme', 'dark');
    toggle.textContent = '\u2600\uFE0F';
  }
  toggle.addEventListener('click', function() {
    var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDark) {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('usmc-theme', 'light');
      toggle.textContent = '\uD83C\uDF19';
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('usmc-theme', 'dark');
      toggle.textContent = '\u2600\uFE0F';
    }
  });
})();

