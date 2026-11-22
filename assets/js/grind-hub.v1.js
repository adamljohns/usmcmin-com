/* Grind Hub — live counters for the three local grinds.
   Church numbers come only from the live verified stats file on usmcmin.org
   (data/grind-stats.json; that Worker sends access-control-allow-origin for
   https://usmcmin.com on that one key). Citizen and commerce read usmcmin.com
   same-origin. Versioned filename: the Worker caches js as immutable. */
(function () {
  'use strict';
  var CHURCH_STATS = 'https://usmcmin.org/data/grind-stats.json';

  function $(id) { return document.getElementById(id); }
  function num(v) { var x = Number(v); return isFinite(x) ? x : 0; }
  function fmt(v) { return num(v).toLocaleString('en-US'); }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function stat(label, value, delta, sub) {
    return '<div class="gh-stat"><div class="gh-label">' + esc(label) + '</div>' +
      '<div class="gh-value">' + esc(value) + '</div>' +
      (delta ? '<div class="gh-delta">' + esc(delta) + '</div>' : '') +
      (sub ? '<div class="gh-sub">' + esc(sub) + '</div>' : '') + '</div>';
  }
  function ago(date) {
    if (!date || isNaN(date)) return 'time unknown';
    var hours = (Date.now() - date.getTime()) / 36e5;
    if (hours < 1) return Math.max(1, Math.round(hours * 60)) + ' min ago';
    if (hours < 48) { var h = Math.round(hours); return h + (h === 1 ? ' hour ago' : ' hours ago'); }
    return Math.floor(hours / 24) + ' days ago';
  }
  function day(date) {
    return isNaN(date) ? '' : date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'America/New_York' });
  }
  // Church rows are written in UTC without a zone suffix (grind-report.html
  // labels the column "When (UTC)"); parse them as UTC, not local time.
  function utc(ts) { return ts ? new Date(String(ts).replace(' ', 'T') + (/[zZ]|[+-]\d\d:?\d\d$/.test(ts) ? '' : 'Z')) : new Date(NaN); }
  function getJSON(url) {
    return fetch(url, { cache: 'no-store' }).then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    });
  }
  function fail(prefix, message) {
    var el = $(prefix + '-status');
    el.className = 'gh-status is-error';
    el.textContent = message;
    $(prefix + '-stats').innerHTML = '';
  }

  // Church directory (usmcmin.org)
  getJSON(CHURCH_STATS).then(function (stats) {
    var s = (stats && stats.series) || [];
    // Zero-content hops are folded in as pending stubs with no totals; only
    // full rows carry the verified pastor and social counts.
    var full = s.filter(function (r) { return r && r.real_pastors != null && !r.pending; });
    if (!full.length) { fail('church', 'No verified church rounds are published yet.'); return; }
    var base = full[0], last = full[full.length - 1];
    var newest = s[s.length - 1] || last;
    var since = day(utc(base.ts));
    var attempted = 0, found = 0, applied = 0, updated = 0;
    s.forEach(function (r) {
      attempted += num(r.attempted); found += num(r.found);
      applied += num(r.applied); updated += num(r.records_updated);
    });
    $('church-status').textContent = 'Last round ' + ago(utc(newest.ts)) + ' · ' + fmt(s.length) +
      ' rounds on the board since ' + since + ' · ' + fmt(last.us_total) + ' U.S. churches listed';
    $('church-stats').innerHTML = [
      stat('Verified pastors', fmt(last.real_pastors), '+' + fmt(num(last.real_pastors) - num(base.real_pastors)) + ' since ' + since, fmt(last.rosters) + ' multi-pastor rosters'),
      stat('Churches with socials', fmt(last.socials_any), '+' + fmt(num(last.socials_any) - num(base.socials_any)) + ' since ' + since, 'of ' + fmt(last.total_churches) + ' churches on file'),
      stat('Fields applied', fmt(applied), '', fmt(updated) + ' profile records updated'),
      stat('Pastor hit rate', attempted ? Math.round(100 * found / attempted) + '%' : '—', '', fmt(found) + ' pastors landed of ' + fmt(attempted) + ' attempted')
    ].join('');
  }).catch(function () {
    fail('church', 'Live church numbers did not load. The full report on usmcmin.org has them.');
  });

  // RESOLUTE Citizen scorecard (usmcmin.com)
  Promise.all([getJSON('/data/stats.json'), getJSON('/data/coverage-by-state.json')]).then(function (res) {
    var stats = res[0] || {}, cov = res[1] || {};
    var totals = stats.totals || {}, conf = stats.scoring_confidence || {}, nat = cov.national || {};
    var meta = stats._meta || {};
    var built = new Date(meta.generated);
    $('citizen-status').textContent = 'Stats built ' + day(built) + ' (' + ago(built) + ') from scorecard v' +
      (meta.scorecard_version || '?') + '. They change only when a round lands new evidence.';
    $('citizen-stats').innerHTML = [
      stat('Evidence-scored', fmt(nat.evidence_scored), (nat.pct != null ? nat.pct + '%' : '—') + ' of ' + fmt(nat.total), fmt(num(nat.total) - num(nat.evidence_scored)) + ' candidates still to score'),
      stat('Verified claims', fmt(totals.verified_claims), '', fmt(totals.total_claims) + ' claims on file · ' + fmt(totals.disputed_claims) + ' disputed'),
      stat('Still unreviewed', fmt(conf.unreviewed), '', fmt(conf.legacy_reviewed) + ' legacy-reviewed · ' + fmt(conf.party_default) + ' party default'),
      stat('Citation coverage', (totals.bias_citation_coverage_pct != null ? totals.bias_citation_coverage_pct + '%' : '—'), '', fmt(totals.unique_cited_domains) + ' unique domains cited')
    ].join('');
  }).catch(function () {
    fail('citizen', 'Live scorecard numbers did not load. Try the full report below.');
  });

  // Fredericksburg commerce directory (usmcmin.com)
  getJSON('/fxbg/commerce/data/stats.json').then(function (stats) {
    var total = num(stats.total), o = stats.overall || {};
    var prog = stats.progress || {}, target = (stats.target || {}).total;
    var scored = total - num(o.gray);
    $('commerce-status').textContent = 'Updated ' + (stats.updated || 'date unknown') + ' · ' + fmt(total) + ' listings in ' + fmt(stats.categories) + ' categories';
    $('commerce-stats').innerHTML = [
      stat('Listings', fmt(total), target ? (prog.listed_pct != null ? prog.listed_pct : Math.round(100 * total / target)) + '% of ' + fmt(target) + ' target' : '', fmt(stats.with_sources) + ' with cited sources'),
      stat('Rated green', fmt(o.green), '', fmt(o.red) + ' red'),
      stat('Rated yellow', fmt(o.yellow), '', 'rubric v' + (stats.rubric_version || '?')),
      stat('Still gray', fmt(o.gray), total ? Math.round(100 * scored / total) + '% rated' : '', fmt(scored) + ' listings rated so far')
    ].join('');
  }).catch(function () {
    fail('commerce', 'Live commerce numbers did not load. The directory itself is still up.');
  });
})();
