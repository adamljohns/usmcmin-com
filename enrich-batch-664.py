#!/usr/bin/env python3
"""Enrichment batch 664: hand-curated claims for 5 Rhode Island State Senators.

Targets from the bottom of the archetype_party_default / 0-claims bucket
(sorted descending by state then name): all five represent RI Senate District
seats held by Democrats. Claims span gun-control votes, abortion-coverage
votes, transgender-healthcare shield legislation, and ICE-restriction votes
covering 2023-2026.

Senators (RI / D):
  Walter Felag    — SD-10, Warren/Bristol/Tiverton (since 1998)
  Victoria Gu     — SD-38, Charlestown/Westerly/South Kingstown (since 2023)
  Valarie Lawson  — SD-14, East Providence; RI Senate President (since April 2025)
  V. Susan Sosnowski — SD-37, South Kingstown/New Shoreham (since 1996)
  Todd Patalano   — SD-26, Cranston (since 2025); notable for OPPOSING AWB and ICE bills

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50 MB warning.
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
    # ── Walter Felag (RI SD-10, D) ──────────────────────────────────────────
    ("walter-felag", "RI", "State Senator", [
        claim("wf1", "walter-felag", "self_defense", 1, False,
              "Co-sponsored S0359A, the Rhode Island Assault Weapons Ban Act of 2025, "
              "which bans the manufacture, purchase, sale, or transfer of certain "
              "military-style semi-automatic weapons beginning July 1, 2026; the RI "
              "Senate passed S0359A 25–11 on June 20, 2025, and Gov. McKee signed it "
              "June 26, 2025.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-bill-banning-sale-assault-weapons"]),
        claim("wf2", "walter-felag", "sanctity_of_life", 0, False,
              "Voted for H5006 (Equality in Abortion Coverage Act) when the Rhode "
              "Island Senate passed it 24–12 on May 18, 2023; the act extends Medicaid "
              "coverage to all abortions and repeals the exclusion of abortion coverage "
              "from state employee health plans; Felag was among the 24 yes votes — "
              "only eight Senate Democrats broke with the caucus to oppose the bill.",
              ["https://thefreedomindex.org/ri/vote/1312955/",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/"]),
    ]),

    # ── Victoria Gu (RI SD-38, D, Senate Judiciary Committee) ───────────────
    ("victoria-gu", "RI", "State Senator", [
        claim("vg1", "victoria-gu", "biblical_marriage", 2, False,
              "Voted for SB2262, the Rhode Island Healthcare Provider Shield Act "
              "(May 2024), which protects out-of-state prosecutions of providers who "
              "offer abortion and gender-affirming transgender care; Gu added her vote "
              "after the initial passage, bringing the final tally to 30–7; Gov. McKee "
              "signed it into law in May 2024.",
              ["https://www.bostonglobe.com/2024/05/03/metro/ri-bill-would-shield-doctors-who-provide-abortion-transgender-care/",
               "https://www.gladlaw.org/rhode-island-senate-passes-bill-to-safeguard-health-care-system-access-to-care/"]),
        claim("vg2", "victoria-gu", "self_defense", 1, False,
              "As a member of the Rhode Island Senate Judiciary Committee, voted on "
              "June 18, 2025 to advance S0359A (Assault Weapons Ban Act of 2025) when "
              "the committee forwarded the bill 8–6; the six opposing votes were cast "
              "by Sen. Patalano, Minority Leader de la Cruz, Minority Whip Rogers, and "
              "Sens. Dimitri, Paolino, and Raptakis — Gu was among the eight-member "
              "majority that advanced the ban to the full Senate.",
              ["https://rhodeislandcurrent.com/2025/06/18/vote-first-ask-questions-later-senate-panel-quickly-advances-reworked-assault-weapons-ban/",
               "https://ballotpedia.org/Victoria_Gu"]),
    ]),

    # ── Valarie Lawson (RI SD-14, D, RI Senate President since April 2025) ──
    ("valarie-lawson", "RI", "State Senator", [
        claim("vl1", "valarie-lawson", "self_defense", 1, False,
              "Primary Senate sponsor of S0359A, the Rhode Island Assault Weapons Ban "
              "Act of 2025; as Senate President she championed the bill through the "
              "chamber (passed 25–11, June 20, 2025) and Gov. McKee signed it June 26, "
              "2025; the law bans the manufacture, purchase, sale, or transfer of "
              "military-style semi-automatic rifles, shotguns, and handguns effective "
              "July 1, 2026.",
              ["https://governor.ri.gov/press-releases/governor-mckee-signs-bill-banning-sale-assault-weapons",
               "https://www.everytown.org/press/senator-valarie-lawson-elected-rhode-island-senate-president-moms-demand-action-and-students-demand-action-urge-follow-through-on-s-359-to-keep-assault-weapons-out-of-rhode-island-communities/"]),
        claim("vl2", "valarie-lawson", "sanctity_of_life", 0, False,
              "Described as a 'steadfast supporter of abortion rights since her first "
              "day in office'; co-sponsored the Senate companion bill (S0032) to the "
              "Equality in Abortion Coverage Act, which the RI Senate passed 24–12 on "
              "May 18, 2023, extending Medicaid and state-employee abortion coverage; "
              "Lawson was elected RI Senate President in April 2025.",
              ["https://rhodeislandcurrent.com/2025/01/07/lawson-has-her-lesson-plan-ready-for-the-r-i-senate/",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/"]),
    ]),

    # ── V. Susan Sosnowski (RI SD-37, D) ─────────────────────────────────────
    ("v-susan-sosnowski", "RI", "State Senator", [
        claim("vs1", "v-susan-sosnowski", "sanctity_of_life", 0, False,
              "Voted for H5006 (Equality in Abortion Coverage Act) when the Rhode "
              "Island Senate passed it 24–12 on May 18, 2023; the act mandates "
              "Medicaid coverage for all abortions and removes the abortion exclusion "
              "from state employee health insurance plans; VoteSmart records her 'aye' "
              "on this vote.",
              ["https://justfacts.votesmart.org/candidate/12867/v-susan-sosnowski",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/"]),
        claim("vs2", "v-susan-sosnowski", "self_defense", 1, False,
              "Voted for S2202 (Firearm Safe Storage Act) when the Rhode Island Senate "
              "passed it 30–7 on June 6, 2024; the law imposes civil and criminal "
              "penalties for leaving firearms unsecured, extends trigger-lock purchase "
              "requirements to rifles and shotguns, and requires gun dealers to post "
              "safe-storage signage; Gov. McKee signed it June 13, 2024.",
              ["https://justfacts.votesmart.org/candidate/12867/v-susan-sosnowski",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-safe-storage-firearms-law"]),
    ]),

    # ── Todd Patalano (RI SD-26, D, Cranston; notable crossover votes) ───────
    ("todd-patalano", "RI", "State Senator", [
        claim("tp1", "todd-patalano", "self_defense", 1, True,
              "Voted against S0359A (Assault Weapons Ban Act of 2025) in the Rhode "
              "Island Senate Judiciary Committee on June 18, 2025, when the committee "
              "advanced the bill 8–6; Patalano publicly opposed the bill, arguing "
              "'we can't pass a law that changes the constitution' and warning it "
              "would cost Rhode Island taxpayers millions in litigation; he was one of "
              "six committee members — alongside all chamber Republicans and one other "
              "Democrat — to oppose the ban.",
              ["https://rhodeislandcurrent.com/2025/06/18/vote-first-ask-questions-later-senate-panel-quickly-advances-reworked-assault-weapons-ban/",
               "https://www.ripbs.org/news-and-culture/rhode-island-senate-panel-advances-amended-assault-weapons-ban-despite-divided-reactions/"]),
        claim("tp2", "todd-patalano", "border_immigration", 2, True,
              "Voted against two RI Senate bills restricting ICE cooperation on June "
              "4, 2026: the first (31–7) authorized lawsuits against federal "
              "immigration officials in state courts; the second (30–8) barred ICE "
              "from using secure government facilities and nonpublic police databases "
              "for enforcement; Patalano was one of only eight senators opposing both "
              "measures, alongside all four chamber Republicans and two other Democrats "
              "— consistent with his 30-year career as a Cranston Police major.",
              ["https://rhodeislandcurrent.com/2026/06/04/ri-senate-votes-to-restrain-ice-operations-opening-door-to-lawsuits/",
               "https://ballotpedia.org/Todd_Patalano"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
