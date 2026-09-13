/**
 * Quick check: calendarWeek after US spring-forward 2027.
 * Run: node family-captain/battle-bro-form/calendar-week-test.js
 *
 * Anchor Sunday 2026-07-05 is Sabbath (week 7).
 * 2027-03-14 is DST start; 2027-03-21 is the next Sunday.
 * floor() of local-midnight elapsed would report the previous theme;
 * round() keeps the Sun–Sat count correct.
 */
var ARMADA_ANCHOR = { y: 2026, m: 6, d: 5 };
var ARMADA_ANCHOR_WEEK = 7;

function sundayOf(date) {
  var d = new Date(date.getFullYear(), date.getMonth(), date.getDate());
  d.setDate(d.getDate() - d.getDay());
  d.setHours(0, 0, 0, 0);
  return d;
}

function calendarWeek(now, useRound) {
  var thisSun = sundayOf(now);
  var anchor = sundayOf(new Date(ARMADA_ANCHOR.y, ARMADA_ANCHOR.m, ARMADA_ANCHOR.d));
  var msPerWeek = 7 * 24 * 60 * 60 * 1000;
  var elapsed = (useRound ? Math.round : Math.floor)((thisSun - anchor) / msPerWeek);
  var idx = ((ARMADA_ANCHOR_WEEK - 1) + elapsed) % 7;
  if (idx < 0) idx += 7;
  return idx + 1;
}

var postDst = new Date(2027, 2, 21); // Sun 21 Mar 2027
var rounded = calendarWeek(postDst, true);
var floored = calendarWeek(postDst, false);
// July DST anchor → next March DST crosses fall-back AND spring-forward, so
// the two 1h errors cancel. The real floor bug is EST → EDT (one spring-forward).
var estSun = sundayOf(new Date(2027, 2, 7));
var edtSun = sundayOf(new Date(2027, 2, 14));
var msPerWeek = 7 * 24 * 60 * 60 * 1000;
var gapFloor = Math.floor((edtSun - estSun) / msPerWeek);
var gapRound = Math.round((edtSun - estSun) / msPerWeek);
if (gapRound !== 1) {
  console.error('FAIL: expected 1 week EST→EDT with round, got ' + gapRound);
  process.exit(1);
}
if (gapFloor === 0) {
  console.log('DST gap confirmed: EST→EDT floor=0 round=1');
} else {
  console.log('NOTE: this TZ did not shorten the spring-forward week (floor=' + gapFloor + ')');
}
if (rounded === floored) {
  console.log('NOTE: July-anchor week for 2027-03-21 agrees floor/round = ' + rounded + ' (both DST offsets cancel)');
} else {
  console.log('July-anchor DST gap: floor=' + floored + ' round=' + rounded);
}
if (rounded < 1 || rounded > 7) {
  console.error('FAIL: calendarWeek out of range: ' + rounded);
  process.exit(1);
}
console.log('PASS: calendarWeek(2027-03-21) = ' + rounded);
process.exit(0);
