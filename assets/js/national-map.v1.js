/* RESOLUTE Citizen — national score map (national-map.html).
   Reads two precomputed files built by build-national-map.py:
     data/national-map.json           per-state averages, two views
     data/maps/us-states-albers.json  projected state outlines (AK/HI insets)
   Draws a static SVG choropleth; no libraries, no network calls beyond those two.
   Versioned filename: assets are cached immutable, so edits ship as .v2.js. */
(function () {
  'use strict';

  var SVGNS = 'http://www.w3.org/2000/svg';
  var VB = { x: 20, y: 0, w: 960, h: 510 };
  var BINS = [0, 20, 40, 60, 80];                     // lower bounds, 5 classes over 0-100
  var RAMP = {                                        // validated: dataviz validator, ordinal, both surfaces
    light: ['#86b6ef', '#5598e7', '#2a78d6', '#1c5cab', '#0d366b'],
    dark:  ['#184f95', '#2a78d6', '#5598e7', '#86b6ef', '#cde2fb']
  };
  var NODATA = { light: '#e5e7eb', dark: '#2f3237' };
  var NODATA_HATCH = { light: '#9ca3af', dark: '#6b7280' };
  var STROKE = { light: '#ffffff', dark: '#0a0a0a' };
  var CALLOUT_Y0 = 120, CALLOUT_DY = 25, CALLOUT_X = 905;
  var VIEWS = {
    legislature: {
      label: 'State legislature',
      subtitle: "Average score of each state's sitting state legislators who carry an evidence-backed RESOLUTE Citizen scorecard. 0–100; higher means a record closer to the rubric.",
      who: 'state legislators'
    },
    congress: {
      label: 'Congressional delegation',
      subtitle: "Average score of each state's sitting U.S. Senators and U.S. Representatives who carry an evidence-backed RESOLUTE Citizen scorecard. 0–100; higher means a record closer to the rubric.",
      who: 'members of Congress'
    }
  };

  var DATA = null, GEO = null;
  var view = 'legislature';
  var pinned = null;          // state pinned by a touch tap
  var lastPointer = 'mouse';

  var el = function (id) { return document.getElementById(id); };
  function theme() { return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function binOf(v) { var i = BINS.length - 1; while (i > 0 && v < BINS[i]) i--; return i; }
  function fillFor(rec) {
    var t = theme();
    if (!rec || rec.avg == null) return 'url(#nm-hatch-' + t + ')';
    return RAMP[t][binOf(rec.avg)];
  }
  function inkOn(hex) {
    if (!hex || hex.charAt(0) !== '#') return theme() === 'dark' ? '#e5e7eb' : '#1f2937';
    var r = parseInt(hex.substr(1, 2), 16), g = parseInt(hex.substr(3, 2), 16), b = parseInt(hex.substr(5, 2), 16);
    var L = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
    return L > 0.55 ? '#0b1b33' : '#ffffff';
  }
  function fmtDate(iso) {
    if (!iso) return '';
    var p = String(iso).slice(0, 10).split('-');
    var M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return M[(+p[1]) - 1] + ' ' + (+p[2]) + ', ' + p[0];
  }
  function n(x) { return Number(x).toLocaleString('en-US'); }
  function stateHref(st) { return 'state.html?st=' + st; }
  var DETAIL_MAP = { AZ: 1, CA: 1, FL: 1, GA: 1, IL: 1, MI: 1, NJ: 1, NY: 1, NC: 1, OH: 1, PA: 1, TX: 1, VA: 1 };

  // ------------------------------------------------------------------ SVG
  function mk(tag, attrs, parent) {
    var e = document.createElementNS(SVGNS, tag);
    for (var k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }

  function buildSvg() {
    var svg = mk('svg', {
      xmlns: SVGNS, viewBox: VB.x + ' ' + VB.y + ' ' + VB.w + ' ' + VB.h,
      role: 'img', 'aria-labelledby': 'nmTitle nmSub', id: 'nmSvg',
      'font-family': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    });
    var defs = mk('defs', {}, svg);
    ['light', 'dark'].forEach(function (t) {
      var p = mk('pattern', { id: 'nm-hatch-' + t, width: 6, height: 6, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(45)' }, defs);
      mk('rect', { width: 6, height: 6, fill: NODATA[t] }, p);
      mk('line', { x1: 0, y1: 0, x2: 0, y2: 6, stroke: NODATA_HATCH[t], 'stroke-width': 1.6 }, p);
    });
    var gStates = mk('g', { 'class': 'nm-states' }, svg);
    var gLabels = mk('g', { 'class': 'nm-labels', 'pointer-events': 'none' }, svg);
    var gCall = mk('g', { 'class': 'nm-callouts' }, svg);
    // inset frames for AK / HI
    mk('rect', { x: 26, y: 374, width: 226, height: 130, rx: 4, fill: 'none', 'class': 'nm-inset', 'stroke-width': 0.8 }, svg);
    mk('rect', { x: 256, y: 426, width: 104, height: 78, rx: 4, fill: 'none', 'class': 'nm-inset', 'stroke-width': 0.8 }, svg);

    var codes = Object.keys(GEO.states).sort();
    var ci = 0;
    codes.forEach(function (st) {
      var g = GEO.states[st];
      var p = mk('path', { d: g.d, 'data-st': st, 'class': 'nm-state', tabindex: g.callout ? -1 : 0, role: 'link', 'stroke-width': 0.7 }, gStates);
      p.__st = st;
      if (!g.callout) {
        mk('text', { x: g.lx, y: g.ly - 4, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 700, 'class': 'nm-lbl', 'data-st': st }, gLabels).textContent = st;
        mk('text', { x: g.lx, y: g.ly + 8, 'text-anchor': 'middle', 'font-size': 9.5, 'class': 'nm-val', 'data-st': st }, gLabels);
      }
    });
    // callout boxes for the small eastern states, in north-to-south order
    ['VT', 'NH', 'MA', 'RI', 'CT', 'NJ', 'DE', 'MD', 'DC'].forEach(function (st) {
      var g = GEO.states[st];
      var y = CALLOUT_Y0 + ci * CALLOUT_DY; ci++;
      mk('line', { x1: g.lx, y1: g.ly, x2: CALLOUT_X - 2, y2: y + 9, 'class': 'nm-leader', 'stroke-width': 0.6 }, gCall);
      mk('circle', { cx: g.lx, cy: g.ly, r: 1.4, 'class': 'nm-dot' }, gCall);
      var r = mk('rect', { x: CALLOUT_X, y: y, width: 30, height: 18, rx: 3, 'data-st': st, 'class': 'nm-state nm-callout', tabindex: 0, role: 'link', 'stroke-width': 0.7 }, gCall);
      r.__st = st;
      mk('text', { x: CALLOUT_X + 15, y: y + 12.5, 'text-anchor': 'middle', 'font-size': 10, 'font-weight': 700, 'class': 'nm-lbl', 'data-st': st, 'pointer-events': 'none' }, gCall).textContent = st;
      mk('text', { x: CALLOUT_X + 35, y: y + 12.5, 'text-anchor': 'start', 'font-size': 10, 'class': 'nm-val nm-val-out', 'data-st': st, 'pointer-events': 'none' }, gCall);
    });
    return svg;
  }

  function paint() {
    var t = theme(), states = DATA.views[view].states;
    var svg = el('nmSvg');
    var ink = t === 'dark' ? '#e5e7eb' : '#1f2937';
    svg.querySelectorAll('.nm-state').forEach(function (p) {
      var rec = states[p.__st];
      var f = fillFor(rec);
      p.setAttribute('fill', f);
      p.setAttribute('stroke', STROKE[t]);
      p.setAttribute('aria-label', label(p.__st, rec));
    });
    svg.querySelectorAll('.nm-lbl').forEach(function (tx) {
      var rec = states[tx.getAttribute('data-st')];
      var f = fillFor(rec);
      tx.setAttribute('fill', f.charAt(0) === '#' ? inkOn(f) : ink);
    });
    svg.querySelectorAll('.nm-val').forEach(function (tx) {
      var st = tx.getAttribute('data-st'), rec = states[st];
      var f = fillFor(rec);
      var out = tx.classList.contains('nm-val-out');
      tx.textContent = rec && rec.avg != null ? Math.round(rec.avg) : (out ? 'n<' + DATA.min_n : '–');
      tx.setAttribute('fill', out ? ink : (f.charAt(0) === '#' ? inkOn(f) : ink));
    });
    svg.querySelectorAll('.nm-leader, .nm-inset').forEach(function (l) { l.setAttribute('stroke', t === 'dark' ? '#6b7280' : '#9ca3af'); });
    svg.querySelectorAll('.nm-dot').forEach(function (d) { d.setAttribute('fill', t === 'dark' ? '#9ca3af' : '#6b7280'); });
    paintLegend();
  }

  function label(st, rec) {
    var name = GEO.states[st].name;
    if (!rec || rec.avg == null) return name + ': not enough scored (' + (rec ? rec.n : 0) + ' scored)';
    return name + ': average ' + rec.avg.toFixed(1) + ' from ' + rec.n + ' scored ' + VIEWS[view].who;
  }

  // --------------------------------------------------------------- legend
  function legendItems() {
    var t = theme(), items = [];
    BINS.forEach(function (lo, i) {
      var hi = i === BINS.length - 1 ? 100 : BINS[i + 1] - 1;
      items.push({ color: RAMP[t][i], text: lo + '–' + hi });
    });
    items.push({ color: null, text: 'Not enough scored (n < ' + DATA.min_n + ')' });
    return items;
  }
  function paintLegend() {
    var box = el('nmLegend');
    var t = theme();
    var html = '<span class="nm-leg-title">Average score</span>';
    legendItems().forEach(function (it) {
      var sw = it.color
        ? '<span class="nm-sw" style="background:' + it.color + '"></span>'
        : '<span class="nm-sw nm-sw-na" style="background-color:' + NODATA[t] + ';background-image:repeating-linear-gradient(45deg,' + NODATA_HATCH[t] + ' 0 1.5px,transparent 1.5px 5px)"></span>';
      html += '<span class="nm-leg-item">' + sw + esc(it.text) + '</span>';
    });
    box.innerHTML = html;
  }

  // -------------------------------------------------------------- tooltip
  function showTip(st, evt, pin) {
    var tip = el('nmTip'), rec = DATA.views[view].states[st], name = GEO.states[st].name;
    var body;
    if (rec && rec.avg != null) {
      body = '<div class="nm-tip-avg">' + rec.avg.toFixed(1) + '<span> / 100 average</span></div>' +
        '<div class="nm-tip-n">' + n(rec.n) + ' scored ' + VIEWS[view].who + (rec.sitting > rec.n ? ' (of ' + n(rec.sitting) + ' sitting)' : '') + '</div>';
    } else {
      body = '<div class="nm-tip-avg nm-tip-na">Not enough scored</div>' +
        '<div class="nm-tip-n">' + (rec ? n(rec.n) : 0) + ' scored ' + VIEWS[view].who + ' — need ' + DATA.min_n + '+' +
        (st === 'DC' ? (view === 'congress' ? '. D.C. has only a non-voting delegate.' : '. D.C. has no state legislature.') : '') + '</div>';
    }
    var links = '<a href="' + stateHref(st) + '">Open ' + esc(name) + ' scorecards &rarr;</a>';
    if (DETAIL_MAP[st]) links += '<a href="map.html?st=' + st + '">County &amp; district map &rarr;</a>';
    tip.innerHTML = '<div class="nm-tip-name">' + esc(name) + '</div>' + body +
      (pin ? '<div class="nm-tip-links">' + links + '</div>' : '<div class="nm-tip-hint">Click to open state scorecards</div>');
    tip.hidden = false;
    tip.classList.toggle('pinned', !!pin);
    placeTip(evt, st);
  }
  function placeTip(evt, st) {
    var tip = el('nmTip'), wrap = el('nmMapWrap');
    if (getComputedStyle(tip).position !== 'absolute') return;   // docked under the map on phones
    var wr = wrap.getBoundingClientRect();
    var x, y;
    if (evt && evt.clientX != null && !(evt.type === 'focus')) {
      x = evt.clientX - wr.left; y = evt.clientY - wr.top;
    } else {
      var node = el('nmSvg').querySelector('.nm-state[data-st="' + st + '"]');
      var r = node.getBoundingClientRect();
      x = r.left + r.width / 2 - wr.left; y = r.top + r.height / 2 - wr.top;
    }
    var tw = tip.offsetWidth, th = tip.offsetHeight;
    var left = x + 14, top = y + 14;
    if (left + tw > wr.width - 4) left = Math.max(4, x - tw - 14);
    if (top + th > wr.height - 4) top = Math.max(4, y - th - 14);
    tip.style.left = left + 'px';
    tip.style.top = top + 'px';
  }
  function hideTip() { if (pinned) return; el('nmTip').hidden = true; }
  function setHover(st) {
    el('nmSvg').querySelectorAll('.nm-state').forEach(function (p) { p.classList.toggle('hover', p.__st === st); });
  }

  function wire(svg) {
    svg.addEventListener('pointerdown', function (e) { lastPointer = e.pointerType || 'mouse'; });
    svg.addEventListener('pointermove', function (e) {
      if (e.pointerType === 'touch') return;
      var st = e.target.__st;
      if (!st) { if (!pinned) { hideTip(); setHover(null); } return; }
      if (pinned) return;
      setHover(st); showTip(st, e, false);
    });
    svg.addEventListener('pointerleave', function () { if (!pinned) { hideTip(); setHover(null); } });
    svg.addEventListener('click', function (e) {
      var st = e.target.__st;
      if (!st) { pinned = null; el('nmTip').hidden = true; setHover(null); return; }
      if (lastPointer === 'touch' || lastPointer === 'pen') {
        // first tap shows the numbers + links; a second tap on the same state opens it
        if (pinned === st) { window.location.href = stateHref(st); return; }
        pinned = st; setHover(st); showTip(st, e, true);
        return;
      }
      window.location.href = stateHref(st);
    });
    svg.addEventListener('keydown', function (e) {
      var st = e.target.__st;
      if (st && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); window.location.href = stateHref(st); }
    });
    svg.addEventListener('focusin', function (e) { var st = e.target.__st; if (st) { setHover(st); showTip(st, { type: 'focus' }, false); } });
    svg.addEventListener('focusout', function () { if (!pinned) { hideTip(); setHover(null); } });
    document.addEventListener('click', function (e) {
      if (!pinned) return;
      if (el('nmMapWrap').contains(e.target)) return;
      pinned = null; el('nmTip').hidden = true; setHover(null);
    });
  }

  // ------------------------------------------------------------- the rest
  function sourceLine() {
    var v = DATA.views[view];
    return 'Source: RESOLUTE Citizen Scorecard, usmcmin.com · data as of ' + fmtDate(DATA.source_last_updated || DATA.generated) +
      ' · ' + n(v.n_scored) + ' scored ' + VIEWS[view].who;
  }

  function renderText() {
    el('nmSub').textContent = VIEWS[view].subtitle;
    el('nmSource').textContent = sourceLine();
    var v = DATA.views[view];
    el('nmNational').innerHTML = 'National average: <strong>' + (v.national_avg != null ? v.national_avg.toFixed(1) : '—') +
      '</strong> across ' + n(v.n_scored) + ' scored ' + VIEWS[view].who + ' · ' + v.states_shaded + ' of 51 shaded';
    document.querySelectorAll('.nm-tab').forEach(function (b) {
      var on = b.getAttribute('data-view') === view;
      b.classList.toggle('on', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    renderTable();
  }

  function renderTable() {
    var states = DATA.views[view].states;
    var rows = Object.keys(states).map(function (st) { return { st: st, r: states[st] }; });
    rows.sort(function (a, b) {
      var av = a.r.avg, bv = b.r.avg;
      if (av == null && bv == null) return a.st < b.st ? -1 : 1;
      if (av == null) return 1; if (bv == null) return -1;
      return bv - av;
    });
    var html = '';
    rows.forEach(function (row, i) {
      var r = row.r;
      html += '<tr><td>' + (r.avg != null ? i + 1 : '') + '</td><td><a href="' + stateHref(row.st) + '">' + esc(GEO.states[row.st].name) + '</a></td>' +
        '<td class="num">' + (r.avg != null ? r.avg.toFixed(1) : 'not enough scored') + '</td>' +
        '<td class="num">' + n(r.n) + '</td><td class="num">' + n(r.sitting) + '</td></tr>';
    });
    el('nmTableBody').innerHTML = html;
    el('nmTableCap').textContent = VIEWS[view].label + ' — average score by state (' + n(DATA.views[view].n_scored) + ' scored)';
  }

  function setView(v, push) {
    if (!VIEWS[v]) v = 'legislature';
    view = v; pinned = null; el('nmTip').hidden = true;
    renderText(); paint();
    if (push) {
      try { var u = new URL(window.location); u.searchParams.set('view', v); window.history.replaceState({}, '', u); } catch (e) {}
    }
  }

  // ------------------------------------------------------------ share PNG
  function loadImg(src) {
    return new Promise(function (res, rej) { var i = new Image(); i.onload = function () { res(i); }; i.onerror = rej; i.src = src; });
  }
  function wrapText(ctx, text, maxW) {
    var words = text.split(' '), lines = [], cur = '';
    words.forEach(function (w) {
      var t = cur ? cur + ' ' + w : w;
      if (ctx.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t;
    });
    if (cur) lines.push(cur);
    return lines;
  }

  function renderPng() {
    var t = theme();
    var C = t === 'dark'
      ? { bg: '#0a0a0a', card: '#141416', ink: '#f0f0f0', sub: '#b0b8c4', muted: '#9ca3af', rule: '#2a2d35' }
      : { bg: '#ffffff', card: '#f4f5f7', ink: '#1a1a1a', sub: '#374151', muted: '#4b5563', rule: '#d1d5db' };
    var FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif';
    var W = 1600, PAD = 64, mapW = W - PAD * 2, mapH = Math.round(mapW * VB.h / VB.w);
    var clone = el('nmSvg').cloneNode(true);
    clone.setAttribute('width', mapW * 2); clone.setAttribute('height', mapH * 2);
    clone.querySelectorAll('.hover').forEach(function (p) { p.classList.remove('hover'); });
    var xml = new XMLSerializer().serializeToString(clone);
    var svgUrl = URL.createObjectURL(new Blob([xml], { type: 'image/svg+xml;charset=utf-8' }));
    return Promise.all([loadImg(svgUrl), loadImg('assets/icons/shield-map-hires.png')]).then(function (imgs) {
      URL.revokeObjectURL(svgUrl);
      var mapImg = imgs[0], shield = imgs[1];
      var cv = document.createElement('canvas'), ctx = cv.getContext('2d');
      ctx.font = '400 26px ' + FONT;
      var subLines = wrapText(ctx, VIEWS[view].subtitle, W - PAD * 2 - 150);
      var headH = Math.max(130, 64 + 12 + subLines.length * 34);
      var H = PAD + headH + 28 + mapH + 36 + 44 + 30 + 40 + PAD;
      cv.width = W * 2; cv.height = H * 2; ctx.scale(2, 2);
      ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
      // header: shield + title + subtitle
      ctx.drawImage(shield, PAD, PAD, 124, 124);
      var tx = PAD + 150;
      ctx.fillStyle = C.ink; ctx.textBaseline = 'top';
      ctx.font = '800 50px ' + FONT;
      ctx.fillText('RESOLUTE Citizen Score by State', tx, PAD);
      ctx.font = '700 22px ' + FONT; ctx.fillStyle = C.muted;
      ctx.fillText(VIEWS[view].label.toUpperCase(), tx, PAD + 62);
      ctx.font = '400 24px ' + FONT; ctx.fillStyle = C.sub;
      subLines.forEach(function (ln, i) { ctx.fillText(ln, tx, PAD + 96 + i * 32); });
      var y = PAD + headH + 28;
      ctx.drawImage(mapImg, PAD, y, mapW, mapH);
      y += mapH + 36;
      // legend
      ctx.font = '700 22px ' + FONT; ctx.fillStyle = C.ink; ctx.textBaseline = 'middle';
      var lx = PAD; ctx.fillText('Average score', lx, y + 14); lx += ctx.measureText('Average score').width + 26;
      ctx.font = '400 22px ' + FONT;
      legendItems().forEach(function (it) {
        if (it.color) { ctx.fillStyle = it.color; ctx.fillRect(lx, y, 28, 28); }
        else {
          ctx.fillStyle = NODATA[t]; ctx.fillRect(lx, y, 28, 28);
          ctx.save(); ctx.beginPath(); ctx.rect(lx, y, 28, 28); ctx.clip();
          ctx.strokeStyle = NODATA_HATCH[t]; ctx.lineWidth = 2;
          for (var k = -28; k < 56; k += 7) { ctx.beginPath(); ctx.moveTo(lx + k, y + 28); ctx.lineTo(lx + k + 28, y); ctx.stroke(); }
          ctx.restore();
        }
        ctx.strokeStyle = C.rule; ctx.lineWidth = 1; ctx.strokeRect(lx + 0.5, y + 0.5, 27, 27);
        ctx.fillStyle = C.ink; ctx.fillText(it.text, lx + 38, y + 14);
        lx += 38 + ctx.measureText(it.text).width + 30;
      });
      y += 44 + 30;
      ctx.strokeStyle = C.rule; ctx.beginPath(); ctx.moveTo(PAD, y - 14); ctx.lineTo(W - PAD, y - 14); ctx.stroke();
      ctx.font = '400 21px ' + FONT; ctx.fillStyle = C.muted; ctx.textBaseline = 'top';
      ctx.fillText(sourceLine(), PAD, y);
      ctx.font = '700 21px ' + FONT; ctx.fillStyle = C.ink; ctx.textAlign = 'right';
      ctx.fillText('usmcmin.com/national-map', W - PAD, y + 30);
      ctx.textAlign = 'left'; ctx.font = '400 19px ' + FONT; ctx.fillStyle = C.muted;
      ctx.fillText('U.S.M.C. Ministries · Average of each person’s profile score; grey = fewer than ' + DATA.min_n + ' scored.', PAD, y + 30);
      return cv;
    });
  }

  function share() {
    var btn = el('nmShare'), status = el('nmShareStatus');
    btn.disabled = true; status.textContent = 'Rendering…';
    renderPng().then(function (cv) {
      return new Promise(function (res) { cv.toBlob(function (b) { res({ blob: b, cv: cv }); }, 'image/png'); });
    }).then(function (o) {
      var name = 'resolute-national-map-' + view + '.png';
      var file = null;
      try { file = new File([o.blob], name, { type: 'image/png' }); } catch (e) {}
      var touch = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
      if (touch && file && navigator.canShare && navigator.canShare({ files: [file] })) {
        return navigator.share({ files: [file], title: 'RESOLUTE Citizen Score by State' })
          .then(function () { status.textContent = 'Shared.'; })
          .catch(function (err) { if (err && err.name === 'AbortError') { status.textContent = ''; return; } download(o.blob, name); });
      }
      download(o.blob, name);
    }).catch(function (err) {
      status.textContent = 'Could not render the image: ' + (err && err.message ? err.message : err);
    }).then(function () { btn.disabled = false; });
  }
  function download(blob, name) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url; a.download = name; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
    el('nmShareStatus').textContent = 'Saved ' + name;
  }
  // test hook: returns the PNG as a data URL for the current view
  window.__natmapPng = function () { return renderPng().then(function (cv) { return cv.toDataURL('image/png'); }); };

  // ----------------------------------------------------------------- boot
  function boot() {
    Promise.all([
      fetch('data/national-map.json', { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error('national-map.json HTTP ' + r.status); return r.json(); }),
      fetch('data/maps/us-states-albers.json').then(function (r) { if (!r.ok) throw new Error('us-states-albers.json HTTP ' + r.status); return r.json(); })
    ]).then(function (arr) {
      DATA = arr[0]; GEO = arr[1];
      var wrap = el('nmMapWrap');
      var svg = buildSvg();
      wrap.insertBefore(svg, wrap.firstChild);
      wire(svg);
      var q = new URLSearchParams(window.location.search).get('view');
      setView(q === 'congress' ? 'congress' : 'legislature', false);
      document.querySelectorAll('.nm-tab').forEach(function (b) {
        b.addEventListener('click', function () { setView(b.getAttribute('data-view'), true); });
      });
      el('nmShare').addEventListener('click', share);
      el('nmShare').disabled = false;
      // repaint when the site theme toggle flips data-theme
      new MutationObserver(function () { paint(); }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
      document.body.setAttribute('data-natmap', 'ready');
    }).catch(function (err) {
      el('nmMapWrap').innerHTML = '<div class="nm-error">Could not load the map data: ' + esc(err && err.message ? err.message : err) + '</div>';
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
