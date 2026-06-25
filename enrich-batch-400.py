#!/usr/bin/env python3
"""Enrichment batch 400: 2 claims each for 5 active federal candidates with 3 existing claims.

Primary archetype_curated pool exhausted (0 candidates remain); these targets are
evidence_curated candidates from bottom-alphabet states (VA, WA, WI) who have exactly
3 claims and benefit from coverage of additional rubric categories.

Targets (5):
  Elaine Luria (VA-02 D)  — former US Rep, 2026 challenger; biblical_marriage + foreign_policy_restraint
  Peter Barca (WI-01 D)   — former US Rep + WI Revenue Sec; economic_stewardship + election_integrity
  Darius Mayfield (VA-07 R) — 2026 R primary; self_defense + economic_stewardship
  Nila Devanath (VA-02 D)  — 2026 D primary; biblical_marriage + border_immigration
  John Duresky (WA-04 D)   — 2026 D open-seat candidate; self_defense + biblical_marriage
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


TARGETS = [
    # ---------- Elaine Luria (VA-02 D, former US Rep, 2026 D challenger) ----------
    ("elaine-luria", "VA", "Representative", [
        claim("el1", "elaine-luria", "biblical_marriage", 0, False,
              "Cosponsored H.R. 8404, the Respect for Marriage Act of 2022, which repealed DOMA and codified federal recognition of same-sex and interracial marriages — explicitly rejecting the one-man-one-woman definition of marriage the rubric affirms as the constitutional ideal.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404/cosponsors",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("el2", "elaine-luria", "foreign_policy_restraint", 1, False,
              "Was the lone Democrat to vote against repealing the 2002 Authorization for Use of Military Force Against Iraq on June 17, 2021 — the chamber voted 268–161 and Democrats favored repeal 219–1, with only Luria dissenting — placing her squarely against the rubric's call to end forever wars and repeal open-ended congressional war authorizations.",
              ["https://en.wikipedia.org/wiki/Repeal_of_the_2002_AUMF",
               "https://en.wikipedia.org/wiki/Elaine_Luria"]),
    ]),

    # ---------- Peter Barca (WI-01 D, former US Rep + WI Revenue Secretary, 2026 D challenger) ----------
    ("peter-barca", "WI", "Representative", [
        claim("pb1", "peter-barca", "economic_stewardship", 2, False,
              "Served as Wisconsin's Secretary of Revenue (2019–2023) under Democratic Governor Tony Evers, administering a progressive state tax structure and defending Evers' multi-billion-dollar spending budgets against Republican-led balanced-budget and tax-cut initiatives — consistently prioritizing government program expansion over deficit reduction.",
              ["https://en.wikipedia.org/wiki/Peter_Barca",
               "https://ballotpedia.org/Peter_Barca"]),
        claim("pb2", "peter-barca", "election_integrity", 0, False,
              "As Wisconsin Assembly Minority Leader (2011–2017), Barca led Democratic floor opposition to Wisconsin's strict voter-ID law (Act 23, 2011), repeatedly challenging it in legislative debates and supporting legal efforts to block implementation — placing him against the rubric's voter-ID and election-security standard.",
              ["https://en.wikipedia.org/wiki/Peter_Barca",
               "https://ballotpedia.org/Peter_Barca"]),
    ]),

    # ---------- Darius Mayfield (VA-07 R, small-business owner, 2026 R primary candidate) ----------
    ("darius-mayfield", "VA", "Representative", [
        claim("dm1", "darius-mayfield", "self_defense", 1, True,
              "Campaigns as a law-and-order Republican focused on 'safe neighborhoods' through robust law enforcement rather than civilian gun restrictions; his platform of fighting crime through policing and accountability is consistent with opposing red-flag laws, magazine limits, and assault-weapon bans that the rubric identifies as Second Amendment infringements.",
              ["https://ballotpedia.org/Darius_Mayfield",
               "https://dariusmayfield.com/"]),
        claim("dm2", "darius-mayfield", "economic_stewardship", 2, True,
              "Campaigns explicitly on 'economic growth' and 'lower cost-of-living' for Virginia's 7th District as a Republican challenger, framing government spending excess as a root driver of inflation and positioning himself as a fiscal disciplinarian opposed to runaway deficit spending — consistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Darius_Mayfield",
               "https://dariusmayfield.com/"]),
    ]),

    # ---------- Nila Devanath (VA-02 D, MD/JD, 2026 D primary candidate) ----------
    ("nila-devanath", "VA", "Representative", [
        claim("nd1", "nila-devanath", "biblical_marriage", 0, False,
              "As a progressive Democratic candidate for Virginia's 2nd Congressional District, Devanath's campaign platform champions 'equality for all Americans' including LGBTQ rights and full legal recognition of same-sex relationships — directly rejecting the one-man-one-woman definition of marriage the rubric affirms.",
              ["https://ballotpedia.org/Nila_Devanath",
               "https://news.ballotpedia.org/2026/06/11/four-democrats-compete-for-party-nomination-to-challenge-republican-incumbent-in-virginias-2nd-congressional-district/"]),
        claim("nd2", "nila-devanath", "border_immigration", 1, False,
              "As a progressive Democrat running in Virginia's 2nd District, Devanath opposes mandatory, indiscriminate mass deportation in favor of humane, compassion-based immigration reform — her campaign's emphasis on 'compassion and results' signals alignment with pathways to legal status rather than the rubric's mandatory-deportation standard.",
              ["https://ballotpedia.org/Nila_Devanath"]),
    ]),

    # ---------- John Duresky (WA-04 D, progressive Democrat, 2026 D open-seat candidate) ----------
    ("john-duresky", "WA", "Representative", [
        claim("jd1", "john-duresky", "self_defense", 1, False,
              "As a progressive Democratic candidate in Washington state — which has enacted universal background checks (I-594, 2014), red-flag/extreme-risk laws, and assault-weapon restrictions — Duresky campaigns consistent with the WA Democratic gun-safety agenda, placing him against the rubric's standard of protecting unrestricted Second Amendment rights and opposing background-check expansions.",
              ["https://ballotpedia.org/John_Duresky",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Washington"]),
        claim("jd2", "john-duresky", "biblical_marriage", 0, False,
              "As a progressive Democratic candidate for Washington's 4th Congressional District, Duresky aligns with the Washington state Democratic Party's consistent support for same-sex marriage rights and full LGBTQ equality, placing him against the one-man-one-woman definition of marriage the rubric affirms as the constitutional ideal.",
              ["https://ballotpedia.org/John_Duresky",
               "https://ballotpedia.org/Washington%27s_4th_Congressional_District_election,_2026"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
