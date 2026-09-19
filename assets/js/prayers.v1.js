/* U.S.M.C. Ministries — Prayer Lists engine (PJG-0919-PRAY1)
 *
 * Renders a prayer list from /prayers/data/<slug>.json, substitutes the man's
 * own names into the text, and hands him a print-to-PDF booklet.
 *
 * Deliberately has no backend and no PDF library. The names never leave the
 * phone: they live in localStorage and nowhere else, which matters when a man
 * is typing his wife's and children's names into a ministry site. The "PDF" is
 * the browser's own print-to-PDF driving the @media print block in
 * prayers.v1.css — that path exists on every platform, including iOS, where
 * Share -> Print -> Save to Files produces a real file.
 */
(function () {
  'use strict';

  var LS = 'usmc.prayers.names.v1';
  var root = document.getElementById('pr-app');
  if (!root) return;
  var slug = root.getAttribute('data-slug');

  function load() {
    try { return JSON.parse(localStorage.getItem(LS)) || {}; } catch (e) { return {}; }
  }
  function save(n) {
    try { localStorage.setItem(LS, JSON.stringify(n)); } catch (e) {}
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c];
    });
  }
  // "Gideon, Boaz" -> ["Gideon","Boaz"]
  function list(s) {
    return String(s || '').split(',').map(function (x) { return x.trim(); })
      .filter(function (x) { return x.length; });
  }

  var names = load();
  var state = { child: null, data: null };

  function fill(text) {
    var wife = names.wife || 'my wife';
    var me = names.me || '';
    var child = state.child || (slug === 'daughters' ? 'my daughter' : 'my son');
    return text.replace(/\{\{wife\}\}/g, wife)
               .replace(/\{\{child\}\}/g, child)
               .replace(/\{\{me\}\}/g, me);
  }

  function kidsFor() {
    return slug === 'sons' ? list(names.sons)
         : slug === 'daughters' ? list(names.daughters) : [];
  }

  function coverTitle() {
    var d = state.data;
    if (slug === 'wife') {
      return names.wife ? 'Prayers for ' + names.wife : d.title;
    }
    return state.child ? (slug === 'daughters' ? 'Petitions for ' : 'Requests for ') + state.child : d.title;
  }

  function render() {
    var d = state.data;
    var kids = kidsFor();
    if (kids.length && (!state.child || kids.indexOf(state.child) === -1)) state.child = kids[0];
    if (!kids.length) state.child = null;

    var h = '';

    // Print-only cover page.
    h += '<div class="pr-cover">' +
           '<div class="ct">' + esc(coverTitle()) + '</div>' +
           '<div class="cs">' + esc(d.items.length) + ' prayers &middot; U.S.M.C. Ministries</div>' +
           (names.me ? '<div class="cf">Prayed by ' + esc(names.me) + '</div>' : '') +
         '</div>';

    h += '<div class="pr-kicker">' + esc(d.kicker) + '</div>';
    h += '<h1>' + esc(d.title) + '</h1>';
    h += '<p class="pr-lede">' + esc(d.lede) + '</p>';

    // Personalisation panel.
    h += '<section class="pr-panel pr-noprint">';
    h += '<h2>Make it yours</h2>';
    h += '<p class="hint">Type the names and they drop straight into every prayer below. ' +
         'They stay on this device &mdash; nothing is uploaded, and we never see them.</p>';
    h += '<div class="pr-fields">';
    h += field('me', 'Your name', 'Adam');
    if (slug === 'wife') h += field('wife', "Your wife's name", 'Maria');
    if (slug === 'sons') h += field('sons', "Your sons (comma separated)", 'Gideon, Boaz');
    if (slug === 'daughters') h += field('daughters', 'Your daughters (comma separated)', 'Shiloh');
    h += '</div>';
    if (slug !== 'wife') {
      if (kids.length) {
        h += '<div class="pr-kids" role="group" aria-label="Choose who to pray for">';
        kids.forEach(function (k) {
          h += '<button type="button" class="pr-kid" data-kid="' + esc(k) + '" aria-pressed="' +
               (k === state.child) + '">' + esc(k) + '</button>';
        });
        h += '</div>';
      }
    }
    h += '<div class="pr-actions">' +
           '<button type="button" class="pr-btn pr-go" id="pr-print">Make my PDF</button>' +
           '<button type="button" class="pr-btn" id="pr-clear">Clear names</button>' +
           '<span class="pr-saved" id="pr-saved"></span>' +
         '</div>';
    h += '</section>';

    // The prayers.
    d.items.forEach(function (p, i) {
      h += '<article class="pr-item">' +
             '<div class="pr-num">' + (i + 1) + ' of ' + d.items.length + '</div>' +
             '<h3>' + esc(fill(p.title)) + '</h3>' +
             '<div class="pr-ref"><a href="' + esc(p.bte) + '" target="_blank" rel="noopener">' +
               esc(p.ref) + '</a></div>' +
             '<p class="pr-body">' + esc(fill(p.body)) + '</p>' +
           '</article>';
    });

    root.innerHTML = h;
    wire();
  }

  function field(key, label, ph) {
    return '<div class="pr-field"><label for="f-' + key + '">' + esc(label) + '</label>' +
      '<input id="f-' + key + '" data-key="' + key + '" type="text" autocomplete="off" ' +
      'placeholder="' + esc(ph) + '" value="' + esc(names[key] || '') + '"></div>';
  }

  function wire() {
    Array.prototype.forEach.call(root.querySelectorAll('.pr-field input'), function (inp) {
      inp.addEventListener('input', function () {
        names[inp.getAttribute('data-key')] = inp.value;
        save(names);
        note('Saved on this device');
        redrawText();
      });
      // Re-render only on blur for the comma lists, so the chips do not
      // rebuild under the man's fingers while he is still typing.
      inp.addEventListener('blur', function () {
        var k = inp.getAttribute('data-key');
        if (k === 'sons' || k === 'daughters') render();
      });
    });
    Array.prototype.forEach.call(root.querySelectorAll('.pr-kid'), function (b) {
      b.addEventListener('click', function () {
        state.child = b.getAttribute('data-kid');
        render();
      });
    });
    var pb = document.getElementById('pr-print');
    if (pb) pb.addEventListener('click', function () {
      document.title = coverTitle() + ' — U.S.M.C. Ministries';
      window.print();
    });
    var cb = document.getElementById('pr-clear');
    if (cb) cb.addEventListener('click', function () {
      names = {}; state.child = null; save(names); render();
    });
  }

  // Cheap path: swap the text without rebuilding the panel, so focus and the
  // caret stay put while he types.
  function redrawText() {
    var d = state.data;
    var items = root.querySelectorAll('.pr-item');
    for (var i = 0; i < items.length && i < d.items.length; i++) {
      items[i].querySelector('h3').textContent = fill(d.items[i].title);
      items[i].querySelector('.pr-body').textContent = fill(d.items[i].body);
    }
    var ct = root.querySelector('.pr-cover .ct');
    if (ct) ct.textContent = coverTitle();
    var cf = root.querySelector('.pr-cover .cf');
    if (cf) cf.textContent = names.me ? 'Prayed by ' + names.me : '';
  }

  var noteTimer = null;
  function note(msg) {
    var el = document.getElementById('pr-saved');
    if (!el) return;
    el.textContent = msg;
    clearTimeout(noteTimer);
    noteTimer = setTimeout(function () { el.textContent = ''; }, 1800);
  }

  fetch('/prayers/data/' + slug + '.json')
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (d) { state.data = d; render(); })
    .catch(function (e) {
      root.innerHTML = '<p>Sorry — this list could not load (' + esc(e.message) +
        '). Try a refresh.</p>';
    });
})();
