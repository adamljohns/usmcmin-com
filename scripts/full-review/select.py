#!/usr/bin/env python3
"""Full-review selector (--full-review mode of the scorecard grind).

Selection order (ticket): (a) Fredericksburg and Virginia officials; (b) federal delegation and
2026 competitive races; (c) records with fewer than 3 cited cells or no headline letter, oldest
first; (d) the rest. Every tier is ordered never-reviewed first, then oldest full review, then
oldest last_refined.

A batch is filled by quota so one round touches every tier (default for 25: a=10, b=8, c=5, d=2);
any unused share falls through to the next tier in order. Inside tier (a) Fredericksburg leads and
the batch then rotates Virginia federal / state / local so a round is not all one city.

Reads data/scorecard.json read-only. Writes only the batch file.

Usage: select.py OUT.json [--batch 25] [--quota a:10,b:8,c:5,d:2] [--slugs s@ST,s2@ST]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fr_lib as L  # noqa: E402

LIVE = {"active", "lame_duck", None, ""}


def key(c):
    return f"{c['slug']}@{(c.get('state') or '').upper()}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--batch", type=int, default=25)
    ap.add_argument("--quota", default="")
    ap.add_argument("--slugs", default="")
    a = ap.parse_args()
    n = max(1, min(60, a.batch))
    sc = json.load(open(L.SCORECARD))
    cats = sc["categories"]
    C = sc["candidates"]
    ledger = L.load_json(os.path.join(L.STATE_HOME, "ledger.json"), {}) or {}

    def order(c):
        led = ledger.get(key(c)) or {}
        return (1 if led else 0, led.get("last_round") or "", (c.get("profile") or {}).get("last_refined") or "0000",
                c.get("slug"))

    if a.slugs:
        want = [s.strip() for s in a.slugs.split(",") if s.strip()]
        by = {key(c): c for c in C}
        picked = [(by[w], "explicit") for w in want if w in by]
    else:
        live = [c for c in C if c.get("status") in LIVE]
        fx = sorted([c for c in live if L.is_fxbg(c)], key=order)
        va = [c for c in live if L.is_fxbg_or_va(c) and not L.is_fxbg(c)]
        va_fed = sorted([c for c in va if L.tier_of(c) == "federal"], key=order)
        va_state = sorted([c for c in va if L.tier_of(c) == "state"], key=order)
        va_local = sorted([c for c in va if L.tier_of(c) == "local"], key=order)
        # Fredericksburg leads every cycle (two slots), then one each of VA federal / state / local
        tier_a, i, fi = [], 0, 0
        while fi < len(fx) or any(len(g) > i for g in (va_fed, va_state, va_local)):
            tier_a += fx[fi:fi + 2]
            fi += 2
            for g in (va_fed, va_state, va_local):
                if i < len(g):
                    tier_a.append(g[i])
            i += 1
        seen = {key(c) for c in tier_a}

        def sitting_fed(c):
            o = (c.get("office") or "").lower()
            return L.tier_of(c) == "federal" and ("u.s. house" in o or "u.s. senat" in o or "u.s. rep" in o
                                                   or "united states" in o) and "candidate" not in o
        b1 = [c for c in live if key(c) not in seen and sitting_fed(c)]
        b2 = [c for c in live if key(c) not in seen and not sitting_fed(c) and c.get("race_id")]
        tier_b = sorted(b1, key=order) + sorted(b2, key=order)
        seen |= {key(c) for c in tier_b}

        def thin(c):
            h = L.headline(c, cats)
            return h["backed"] < 3 or h["letter"] is None
        rest = [c for c in live if key(c) not in seen]
        tier_c = sorted([c for c in rest if thin(c)], key=order)
        tier_d = sorted([c for c in rest if not thin(c)], key=order)
        tiers = {"a": tier_a, "b": tier_b, "c": tier_c, "d": tier_d}
        quota = {"a": round(n * .40), "b": round(n * .32), "c": round(n * .20)}
        quota["d"] = n - sum(quota.values())
        for part in filter(None, a.quota.split(",")):
            t, v = part.split(":")
            quota[t.strip()] = int(v)
        picked, carry = [], 0
        for t in "abcd":
            want = quota.get(t, 0) + carry
            got = tiers[t][:want]
            picked += [(c, t) for c in got]
            carry = want - len(got)
        picked = picked[:n]

    batch = []
    for c, t in picked:
        p = c.get("profile") or {}
        batch.append({"key": key(c), "slug": c["slug"], "state": c.get("state"), "name": c.get("name"),
                      "office": c.get("office"), "level": c.get("level"), "tier": L.tier_of(c),
                      "selection_tier": t, "fxbg": L.is_fxbg(c), "va": L.is_fxbg_or_va(c),
                      "website": c.get("website"), "campaign_website": p.get("campaign_website"),
                      "records_website": p.get("records_website"), "last_refined": p.get("last_refined")})
    L.dump_json(a.out, batch)
    from collections import Counter
    print(f"selected {len(batch)} -> {a.out}  tiers={dict(Counter(b['selection_tier'] for b in batch))}  "
          f"fxbg/va={sum(b['va'] for b in batch)} federal={sum(b['tier'] == 'federal' for b in batch)}")


if __name__ == "__main__":
    main()
