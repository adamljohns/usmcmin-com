/* RESOLUTE Citizen — Virginia local score map.
   Reads data/va-local-map.json and data/maps/va-counties.geojson.
   Same letter-grade fills as national-map.v2.js. Grey hatch = fewer than 3 scored. */
(function () {
  'use strict';
  var SVGNS = 'http://www.w3.org/2000/svg';
  var BANDS = [
    { lo: 0, hi: 19, fill: '#C4501A', ink: '#ffffff', letter: 'F' },
    { lo: 20, hi: 39, fill: '#E8641E', ink: '#111111', letter: 'F' },
    { lo: 40, hi: 59, fill: '#F28C28', ink: '#111111', letter: 'F' },
    { lo: 60, hi: 69, fill: '#F5A623', ink: '#111111', letter: 'D' },
    { lo: 70, hi: 79, fill: '#F2D13A', ink: '#111111', letter: 'C' },
    { lo: 80, hi: 89, fill: '#9CCC3C', ink: '#111111', letter: 'B' },
    { lo: 90, hi: 100, fill: '#2E9E4F', ink: '#111111', letter: 'A' }
  ];
  var DATA, GEO, pinned = null;
  function theme() { return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'; }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      if (c === '&') return '&' + 'amp;';
      if (c === '<') return '&' + 'lt;';
      if (c === '>') return '&' + 'gt;';
      if (c === '"') return '&' + 'quot;';
      return '&' + '#39;';
    });
  }

  function bandOf(v) { var r = Math.round(v), i = BANDS.length - 1; while (i > 0 && r < BANDS[i].lo) i--; return BANDS[i]; }
  function keyOf(name, lsad) { return name + '|' + lsad; }
  function recFor(name, lsad) {
    if (!DATA) return null;
    for (var i = 0; i < DATA.areas.length; i++) {
      var a = DATA.areas[i];
      if (a.name === name && a.lsad === lsad) return a;
    }
    return null;
  }
  function fillFor(rec) {
    if (!rec || rec.avg == null) return theme() === 'dark' ? '#2f3237' : '#e5e7eb';
    return bandOf(rec.avg).fill;
  }
  function project(lon, lat, b) {
    var x = (lon - b.minLon) / (b.maxLon - b.minLon) * 760 + 20;
    var y = (b.maxLat - lat) / (b.maxLat - b.minLat) * 380 + 16;
    return [x, y];
  }
  function ringPath(ring, b) {
    var d = '';
    for (var i = 0; i < ring.length; i++) {
      var p = project(ring[i][0], ring[i][1], b);
      d += (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1);
    }
    return d + 'Z';
  }
  function geomPath(geom, b) {
    var polys = geom.type === 'Polygon' ? [geom.coordinates] : geom.coordinates;
    var d = '';
    polys.forEach(function (poly) { poly.forEach(function (ring) { d += ringPath(ring, b); }); });
    return d;
  }
  function bounds() {
    var minLon = 180, maxLon = -180, minLat = 90, maxLat = -90;
    GEO.features.forEach(function (f) {
      var polys = f.geometry.type === 'Polygon' ? [f.geometry.coordinates] : f.geometry.coordinates;
      polys.forEach(function (poly) {
        poly[0].forEach(function (pt) {
          if (pt[0] < minLon) minLon = pt[0];
          if (pt[0] > maxLon) maxLon = pt[0];
          if (pt[1] < minLat) minLat = pt[1];
          if (pt[1] > maxLat) maxLat = pt[1];
        });
      });
    });
    return { minLon: minLon, maxLon: maxLon, minLat: minLat, maxLat: maxLat };
  }
  function tipHtml(rec, name, lsad) {
    var label = name + (lsad === 'city' ? ' city' : ' County');
    if (!rec) return '<div class="nm-tip-name">' + esc(label) + '</div><div class="nm-tip-n">No local officials on file.</div>';
    var avg = rec.avg == null ? 'Not enough scored' : rec.avg;
    var body = '<div class="nm-tip-name">' + esc(label) + '</div><div class="nm-tip-avg">' + esc(avg) + '</div>';
    body += '<div class="nm-tip-n">' + rec.scored + ' scored of ' + rec.sitting + ' sitting</div>';
    (rec.people || []).slice(0, 6).forEach(function (p) {
      var score = p.score == null ? '—' : p.score;
      body += '<a href="candidates/va/' + encodeURIComponent(p.slug) + '.html">' + esc(p.name) + ' · ' + score + '</a>';
    });
    if ((rec.people || []).length > 6) body += '<div class="nm-tip-hint">+' + (rec.people.length - 6) + ' more on the scorecard</div>';
    return body;
  }
  function draw() {
    var wrap = document.getElementById('vlMap');
    wrap.innerHTML = '';
    var b = bounds();
    var svg = document.createElementNS(SVGNS, 'svg');
    svg.setAttribute('viewBox', '0 0 800 420');
    svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', 'Virginia counties and independent cities shaded by local RESOLUTE scores');
    var tip = document.createElement('div');
    tip.className = 'nm-tip';
    tip.hidden = true;
    GEO.features.forEach(function (f) {
      var name = f.properties.NAME;
      var lsad = f.properties.LSAD;
      var rec = recFor(name, lsad);
      var path = document.createElementNS(SVGNS, 'path');
      path.setAttribute('d', geomPath(f.geometry, b));
      path.setAttribute('class', 'vl-place');
      path.setAttribute('fill', fillFor(rec));
      path.setAttribute('stroke', theme() === 'dark' ? '#0a0a0a' : '#ffffff');
      path.setAttribute('stroke-width', '0.6');
      path.setAttribute('tabindex', '0');
      path.setAttribute('aria-label', name + ' ' + lsad);
      function show(ev) {
        tip.hidden = false;
        tip.classList.toggle('pinned', !!pinned);
        tip.innerHTML = tipHtml(rec, name, lsad);
        if (ev && ev.clientX) {
          var box = wrap.getBoundingClientRect();
          tip.style.left = Math.min(box.width - 200, Math.max(8, ev.clientX - box.left + 8)) + 'px';
          tip.style.top = Math.max(8, ev.clientY - box.top + 8) + 'px';
        }
      }
      path.addEventListener('mouseenter', show);
      path.addEventListener('mousemove', function (ev) { if (!pinned) show(ev); });
      path.addEventListener('mouseleave', function () { if (!pinned) tip.hidden = true; });
      path.addEventListener('click', function (ev) { pinned = keyOf(name, lsad); show(ev); });
      svg.appendChild(path);
    });
    wrap.appendChild(svg);
    wrap.appendChild(tip);
    var legend = document.getElementById('vlLegend');
    legend.innerHTML = BANDS.map(function (b) {
      return '<span><i class="nm-sw" style="background:' + b.fill + '"></i>' + b.letter + ' ' + b.lo + '–' + b.hi + '</span>';
    }).join('') + '<span><i class="nm-sw" style="background:#e5e7eb"></i>Fewer than 3 scored</span>';
    document.getElementById('vlNational').textContent =
      'Virginia local average ' + DATA.national_avg + ' across ' + DATA.n_scored + ' scored of ' + DATA.n_sitting + ' sitting officials. ' + DATA.places_shaded + ' places have enough scores to shade. Scorecard as of ' + String(DATA.source_last_updated || '').slice(0, 10) + '.';
    var rows = DATA.areas.filter(function (a) { return a.avg != null; }).sort(function (a, b) { return b.avg - a.avg; });
    document.getElementById('vlTable').innerHTML = rows.map(function (a) {
      return '<tr><td>' + esc(a.name) + (a.lsad === 'city' ? ' city' : ' County') + '</td><td class="num">' + a.avg + '</td><td class="num">' + a.scored + '</td><td class="num">' + a.sitting + '</td></tr>';
    }).join('');
  }
  Promise.all([
    fetch('data/va-local-map.json').then(function (r) { return r.json(); }),
    fetch('data/maps/va-counties.geojson').then(function (r) { return r.json(); })
  ]).then(function (pair) {
    DATA = pair[0];
    GEO = pair[1];
    draw();
    document.getElementById('themeToggle') && document.getElementById('themeToggle').addEventListener('click', function () {
      setTimeout(draw, 30);
    });
  }).catch(function () {
    document.getElementById('vlMap').textContent = 'The map data did not load.';
  });
})();
