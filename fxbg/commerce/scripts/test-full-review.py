#!/usr/bin/env python3
"""Offline tests for the commerce full-review gates. No network, no data writes.

  python3 fxbg/commerce/scripts/test-full-review.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import full_review_common as fr  # noqa: E402

spec = importlib.util.spec_from_file_location("bp", HERE / "full-review-build-patch.py")
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

fails = 0


def check(name, cond):
    global fails
    print(("PASS " if cond else "FAIL ") + name)
    fails += 0 if cond else 1


# hours: compared as sets of day+time tokens; structured output
p = fr.parse_hours("Monday - Friday: 7:00am - 8:00pm · Saturday 8am-2pm · Sunday Closed")
check("hours parse full week", p["complete"] and not p["inferred"])
check("hours lines structured", fr.hours_lines(p) == ["Mon–Fri: 7:00 AM–8:00 PM", "Sat: 8:00 AM–2:00 PM", "Sun: Closed"])
stored = fr.parse_hours(" · ".join(["Mon–Fri: 7:00 AM–8:00 PM", "Sat: 8:00 AM–2:00 PM", "Sun: Closed"]))
check("stored vs page token sets equal", set(fr.hours_tokens(stored)) == set(fr.hours_tokens(p)))
check("osm hours parse", fr.hours_lines(fr.parse_hours(fr.osm_hours_text("Mo-Fr 08:00-18:00; Sa 08:00-17:00; Su off")))
      == ["Mon–Fri: 8:00 AM–6:00 PM", "Sat: 8:00 AM–5:00 PM", "Sun: Closed"])
check("am/pm missing -> inferred", fr.parse_hours("Mon-Fri 9-5")["inferred"])
check("phone number is not hours", not fr.parse_hours("Call 540-373-9049 Mon")["ok"])
check("holiday closure after hours is not a day closure",
      fr.hours_lines(fr.parse_hours("Sat 9am-1pm. Closed on major holidays")) == ["Sat: 9:00 AM–1:00 PM"])

# socials: html_link vs site-config; junk skipped
f = {}
fr.harvest_socials('<html xmlns:fb="http://www.facebook.com/2008/fbml"><a class="x" href="https://www.facebook.com/joesplumbing/">FB</a>'
                   '<script>var c={"ig":"https://www.instagram.com/joes_plumb"}</script>', "https://joes.example/", f)
check("facebook.com/2008 skipped, real FB kept", f.get("facebook", {}).get("url") == "https://www.facebook.com/joesplumbing")
check("FB typed html_link with exact tag", f["facebook"]["kind"] == "html_link" and f["facebook"]["quote"].startswith("<a "))
check("config-only IG typed site-config", f.get("instagram", {}).get("kind") == "site-config")
f2 = {}
fr.harvest_socials('<a href="https://www.facebook.com/profile.php">x</a>', "u", f2)
check("bare profile.php skipped", "facebook" not in f2)

# methodology rules are printed on the page
try:
    rules = fr.check_rules()
    check("every cited rule text is on methodology.html", len(rules) == len(fr.RULES))
except SystemExit as e:
    check(f"every cited rule text is on methodology.html ({e})", False)

# scope gate
biz = {"slug": "t", "name": "Joe's Plumbing", "address": "100 Main St", "zip": "22401", "phone": "(540) 555-0100",
       "category": "plumbing", "scores": {}, "sources": []}
page = {"url": "https://joes.example/", "kind": "home", "text": "Joe's Plumbing · 100 Main St Fredericksburg, VA 22401 · (540) 555-0100 · "
        "We proudly sponsor the Little League. Our Richmond, VA location opened in 2019.",
        "identity": ["street:100 Main", "zip:22401", "phone"]}
obs = {"slug": "t", "status": "reviewed", "pages": [page], "site_identity": page["identity"], "site": {}}
b = bp.Builder("r", biz, obs, {"t": biz}, {})
check("in-scope local quote passes", b.quote_scope("100 Main St Fredericksburg, VA 22401", page["url"])[0])
check("sponsor passage dropped", not b.quote_scope("We proudly sponsor the Little League.", page["url"])[0])
check("other-town passage dropped", not b.quote_scope("Our Richmond, VA location opened in 2019.", page["url"])[0])
check("identity hits", fr.identity_hits(biz, page["text"]) == ["street:100 Main", "zip:22401", "phone"])

# a quote that is not on the page never becomes a change
b.add("phone", "fill", "", "(540) 555-0199", "Call (540) 555-0199", page["url"], "high", True, [])
check("unverifiable quote -> no change", not b.changes and b.dropped_unverifiable == 1)

# ── verify round 1 fixes (VERIFY-commerce-full-review.md: NK Floors, BIM, All Air) ──
NK = ("Business Hours · NK Floors Selection Center 10042 Southpoint Parkway Fredericksburg, VA 22407 · Monday 10am-4pm · "
      "Tuesday 10am - 4pm · Wednesday 10am - 4pm · Thursday 10am - 4pm · Friday 10am-4pm · Saturday Open by Appointment Only · "
      "NK Floors Builder Showroom 210 Freedom Court, Unit 112 Fredericksburg, VA 22408 · Monday-Friday 8am-4pm · Closed on Saturdays")
runs = [NK[a:b] for a, b in fr.hours_runs(NK)]
check("one-day-per-line runs split at the second address", len(runs) == 2)
check("Selection Center hours parsed", fr.hours_lines(fr.parse_hours(runs[0])) == ["Mon–Fri: 10:00 AM–4:00 PM", "Sat: By appointment"])
check("'Closed on Saturdays' parsed", fr.hours_lines(fr.parse_hours(runs[1])) == ["Mon–Fri: 8:00 AM–4:00 PM", "Sat: Closed"])
nkbiz = {"address": "10042 Southpoint Pkwy"}
check("Selection Center block is this location's section", fr.own_location(nkbiz, NK, runs[0]) == "own-section")
check("Builder Showroom block is not", fr.own_location(nkbiz, NK, runs[1]) is None)
check("'2 Locations:' header -> multi-location",
      bool(fr.detect_multi([{"url": "u", "text": "Free Estimate · 2 Locations: NK Floors Selection Center & NK Floors Builder Showroom"}])))
check("widget 'up to 3 locations' is not multi-location",
      fr.detect_multi([{"url": "u", "text": "up to 3 locations or up to 10,000 locations, depending on the plan"}]) is None)
check("two street+ZIP addresses -> multi-location", bool(fr.detect_multi([{"url": "u", "text": NK}])))
check("'Sunday Closed · Available 24/7' keeps Sunday closed",
      fr.hours_lines(fr.parse_hours("Mon - Sat 7:00 am - 7:00 pm · Sunday Closed · Available 24/7")) == ["Mon–Sat: 7:00 AM–7:00 PM", "Sun: Closed"])
check("partial listing that agrees is not a conflict",
      not fr.hours_disagree(fr.parse_hours("Mon.-Fri. 8am-5pm"), fr.parse_hours("Monday to Friday, 8:00 AM to 5:00 PM Saturday and Sunday: Closed")))
check("different hours on the same days are a conflict",
      fr.hours_disagree(fr.parse_hours(runs[0]), fr.parse_hours("Mon - Fri: 9AM - 6PM · Sat: 10AM - 2PM · Sun: Closed"))[:1] == ["Mon"])
check("bare '#2705069928' in a footer is a licence number",
      [x["number"] for x in fr.license_numbers("4934 Trade Center Dr · Fredericksburg, VA 22408 · (540) 317-0727 · #2705069928 · Areas")] == ["2705069928"])
check("a phone is not a licence number", fr.license_numbers("Call 540-271-2345 today") == [])

# location gate: a page printing only the (shared) phone can never carry an auto change
biz2 = {"slug": "nk", "name": "NK Floors", "address": "10042 Southpoint Pkwy", "zip": "22407", "phone": "(540) 582-4000",
        "category": "flooring", "scores": {}, "sources": []}
pop = {"url": "https://nk.example/store/", "kind": "inner", "identity": ["phone"],
       "text": "Call (540) 582-4000 · Business Hours · Mon - Fri: 9AM - 6PM · Sat: 10AM - 2PM · Sun: Closed"}
b2 = bp.Builder("r", biz2, {"slug": "nk", "pages": [pop], "site_identity": ["phone"], "site": {}}, {"nk": biz2}, {})
b2.add("hours", "fill", [], ["x"], "Mon - Fri: 9AM - 6PM", pop["url"], "high", True, [])
check("phone-only page -> hold, never auto", bool(b2.changes) and b2.changes[0]["gate"] == "hold"
      and any("location gate" in r for r in b2.changes[0]["hold_reasons"]))

print(f"\n{'ALL PASS' if not fails else f'{fails} FAIL'}")
sys.exit(1 if fails else 0)
