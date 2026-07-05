#!/usr/bin/env python3
"""select-scorecard-batch.py — pick the next batch for the local grind.

Civic twin of select-enrichment-batch.js. Chooses ACTIVE, not-yet-evidence-scored
candidates that have a fetchable source (own website or campaign site — the extractor
also tries Ballotpedia), prioritized by civic impact: Virginia/DMV first, then large
swing-state legislatures (the ~7k-record frontier), then everyone else.

Usage: select-scorecard-batch.py [N] [OUT.json]
"""
import json, sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/scorecard-local-batch.json"

# Impact order: home turf + battlegrounds first; New-England citizen-legislatures last.
HIGH = ["VA", "MD", "DC", "TX", "FL", "GA", "NC", "PA", "AZ", "WI", "MI", "OH", "NV", "MN"]
DEFER = ["NH", "MA", "CT", "ME", "VT", "RI"]


def evid(c):
    return ((c.get("profile", {}) or {}).get("confidence", "") or "").startswith("evidence")


def active(c):
    return (c.get("status") or "active") not in ("lost", "former", "deceased", "withdrew", "not_running")


def website(c):
    return c.get("website") or (c.get("profile") or {}).get("campaign_website")


def rank(c):
    st = c.get("state") or "ZZ"
    tier = 0 if st in HIGH else (2 if st in DEFER else 1)
    hi = HIGH.index(st) if st in HIGH else 99
    return (tier, hi, st, c.get("slug") or "")


def main():
    C = json.load(open("data/scorecard.json"))["candidates"]
    pool = [c for c in C if active(c) and not evid(c) and website(c)]
    pool.sort(key=rank)
    batch = [{
        "slug": c["slug"], "name": c.get("name"), "state": c.get("state"),
        "level": c.get("level"), "party": c.get("party"), "office": c.get("office"),
        "website": c.get("website"),
        "campaign_website": (c.get("profile") or {}).get("campaign_website"),
    } for c in pool[:N]]
    json.dump(batch, open(OUT, "w"), indent=1)
    print(f"selected {len(batch)} of {len(pool)} eligible (unscored + fetchable) -> {OUT}")
    # eligible-with-website is the fetchable frontier; the website-less remainder waits on Brave discovery.


if __name__ == "__main__":
    main()
