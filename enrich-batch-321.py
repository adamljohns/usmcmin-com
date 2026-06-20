#!/usr/bin/env python3
"""Enrichment batch 321: third distinct-category claims for 5 WV state senators.

archetype_curated pool is fully exhausted. Continues the reverse-alpha state-senator
pipeline (WV) for evidence_curated candidates with exactly 2 claims.

Candidates:
  Trenton Barnhart (WV R, State Sen D3, appointed Jan 2026) — election_integrity[0]=True
    Co-sponsored WV SJR 9 (2026 citizenship-only voting constitutional amendment);
    Senate adopted 34-0 on March 14, 2026 — WV became the fourth state to place
    such a requirement on the ballot; Barnhart voted AYE on the full 10-bill WV
    election-integrity package signed by Gov. Morrisey in April 2026.

  Rollan A. Roberts (WV R, State Senator) — election_integrity[0]=True
    Co-sponsored WV SJR 9 (2026, Senate 34-0, March 14); voted AYE on WV HB 3016
    (2025, photo voter ID, signed April 30, 2025); part of the Republican supermajority
    enacting WV's 10-bill election-integrity package in 2025-2026.

  Ryan Weld (WV R, State Sen D1, since 2016) — election_integrity[0]=True
    Voted AYE on WV HB 3016 (2025) requiring photo voter ID, signed by Gov. Morrisey
    April 30, 2025; voted AYE on WV SJR 9 (2026 citizenship voting amendment, 34-0).

  Patricia Rucker (WV R, State Sen D16, since 2017) — election_integrity[0]=True
    Co-sponsored WV SJR 9 (2026, Senate 34-0); voted for WV HB 3016 (2025 photo voter
    ID) and the full 10-bill WV election-integrity package enacted 2025-2026.

  Tom Takubo (WV R, State Sen D17, since 2015, Majority Leader 2018-2025) — self_defense[0]=True
    Voted AYE on WV HB 4106 (2026) extending constitutional carry to adults ages 18-20;
    as Majority Leader drove WV's constitutional-carry expansions cementing WV as a
    leading permitless-carry state.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---- Trenton Barnhart (WV-D3, R, appointed Jan 2026) ----
    ("trenton-barnhart", "WV", "State Senator", [
        claim("tb321", "trenton-barnhart", "election_integrity", 0, True,
              "A co-sponsor of West Virginia SJR 9 (2026), the citizenship-only voting constitutional amendment placed on the November 2026 ballot; the Senate adopted the resolution unanimously 34-0 on March 14, 2026, making West Virginia the fourth state to put such a requirement to voters. Barnhart voted AYE on the full 10-bill election-integrity package signed by Governor Morrisey in April 2026.",
              ["https://news.ballotpedia.org/2026/03/19/west-virginia-becomes-the-fourth-state-to-put-a-citizenship-voting-requirement-amendment-on-the-2026-ballot/",
               "https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/"]),
    ]),

    # ---- Rollan A. Roberts (WV, R) ----
    ("rollan-a-roberts", "WV", "State Senator", [
        claim("rar321", "rollan-a-roberts", "election_integrity", 0, True,
              "Co-sponsored WV SJR 9 (2026), the citizenship-only voting constitutional amendment (Senate 34-0, March 14, 2026) placed on the November 2026 ballot. Roberts also voted AYE on WV HB 3016 (2025), requiring government-issued photo identification to vote — signed by Governor Morrisey on April 30, 2025 — as part of WV's comprehensive 10-bill election-integrity package enacted in 2025-2026.",
              ["https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/",
               "https://news.ballotpedia.org/2026/03/19/west-virginia-becomes-the-fourth-state-to-put-a-citizenship-voting-requirement-amendment-on-the-2026-ballot/"]),
    ]),

    # ---- Ryan Weld (WV-D1, R, since 2016) ----
    ("ryan-weld", "WV", "State Senator", [
        claim("rw321", "ryan-weld", "election_integrity", 0, True,
              "Voted AYE on WV HB 3016 (2025), eliminating non-photo ID options and requiring government-issued photo identification to vote — passed the Senate on strict party lines and signed by Governor Morrisey on April 30, 2025. Also voted AYE on WV SJR 9 (2026), the citizenship-only voting constitutional amendment that passed the Senate unanimously 34-0 on March 14, 2026.",
              ["https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/",
               "https://ballotpedia.org/Election_laws_and_legislation_in_West_Virginia"]),
    ]),

    # ---- Patricia Rucker (WV-D16, R, since 2017) ----
    ("patricia-rucker", "WV", "State Senator", [
        claim("pr321", "patricia-rucker", "election_integrity", 0, True,
              "A co-sponsor of WV SJR 9 (2026), the citizenship-only voting constitutional amendment (Senate 34-0, March 14, 2026) placed on the November 2026 ballot. Rucker also voted for WV HB 3016 (2025) requiring photo voter ID (signed April 30, 2025) and the complete 10-bill WV election-integrity package enacted by the Republican supermajority in 2025-2026.",
              ["https://news.ballotpedia.org/2026/03/19/west-virginia-becomes-the-fourth-state-to-put-a-citizenship-voting-requirement-amendment-on-the-2026-ballot/",
               "https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/"]),
    ]),

    # ---- Tom Takubo (WV-D17, R, since 2015, Majority Leader 2018-2025) ----
    ("tom-takubo", "WV", "State Senator", [
        claim("tt321", "tom-takubo", "self_defense", 0, True,
              "Voted AYE on WV HB 4106 (2026), extending West Virginia's constitutional-carry statute to adults ages 18-20 without a government-issued permit. As Senate Majority Leader (2018-January 2025), Takubo consistently drove passage of Second Amendment protections through the WV Senate, reinforcing West Virginia's status as a leading permitless-carry state.",
              ["https://ballotpedia.org/Tom_Takubo",
               "https://home.wvlegislature.gov/senator/tom-takubo/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
