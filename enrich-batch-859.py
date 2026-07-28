#!/usr/bin/env python3
"""Enrichment batch 859: 3 Virginia 2026 congressional candidates (2-claim tier).

The archetype_curated federal pool is fully exhausted (all promoted to
evidence_curated). This batch adds a third documented claim to three Virginia
House candidates who each had exactly 2 claims, drawn from the bottom of the
evidence_curated 2-claim list (VA = bottom-of-alphabet target states).

Targets (all Republican, VA, 2026 primary):
  Tony Sabio    — VA-08, R  (+1 claim: christian_liberty)
  Arthur Purves — VA-11, R  (+2 claims: christian_liberty, self_defense)
  Julie Perry   — VA-10, R  (+2 claims: family_child_sovereignty, economic_stewardship)

All claims sourced from candidate campaign sites and verifiable news coverage
(2025-2026). Minified write preserved — see enrich-batch-4.py docstring.
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
    # -------- Tony Sabio (VA-08, R) — CIA/Navy veteran, 2026 R nominee --------
    ("tony-sabio", "VA", "Representative", [
        claim("ts1", "tony-sabio", "christian_liberty", 0, True,
              "Sabio's campaign platform at sabioforcongress.com/tonys-vision asserts that 'our rights come from God—not from government—and that those rights must never be compromised by political agendas,' and lists 'defending religious liberty' as an explicit constitutional-freedom pillar alongside the First and Second Amendments. He appeared at the Faith and Freedom Coalition Road to Majority Conference (Washington D.C., June 2025) and stated that faith 'guides everything I do. Everything comes from servant leadership.'",
              ["https://sabioforcongress.com/tonys-vision",
               "https://www.washingtonexaminer.com/videos/3457259/conservative-leaders-role-faith-politics-road-to-majority-conference/"]),
    ]),

    # -------- Arthur Purves (VA-11, R) — Fairfax County Taxpayers Alliance president --------
    ("arthur-purves", "VA", "Representative", [
        claim("ap1", "arthur-purves", "christian_liberty", 0, True,
              "Purves states on his campaign website that 'while the First Amendment prohibits a state church, the Founders expected government to foster Christianity,' and calls for reversing Supreme Court decisions (Engel v. Vitale; Abington School District v. Schempp) that removed the Lord's Prayer, Bible reading, and the Ten Commandments from public schools — arguing those rulings 'resulted in a deterioration of marriage and family' and are a root cause of gun violence and higher taxes.",
              ["https://votepurves.org/",
               "https://ballotpedia.org/Arthur_Purves"]),
        claim("ap2", "arthur-purves", "self_defense", 1, True,
              "Purves opposes gun-control legislation on cultural grounds, writing on his campaign website that 'complex gun laws turn law-abiding citizens into inadvertent felons' and that 'Fathers are the best form of gun control, and the Ten Commandments are the only gun control laws that ever worked.' He locates the cause of gun violence in absentee fatherhood and moral decline, not firearms access — rejecting new restrictions as misdiagnosing the problem.",
              ["https://votepurves.org/",
               "https://www.insidenova.com/news/election/taxpayer-advocate-to-square-off-against-veteran-legislator-in-november/article_029d8da6-91d7-11e9-b9fa-6b56f408b357.html"]),
    ]),

    # -------- Julie Perry (VA-10, R) — former HS teacher, 3-time R candidate --------
    ("julie-perry", "VA", "Representative", [
        claim("jp1", "julie-perry", "family_child_sovereignty", 0, True,
              "In her June 2026 Patch candidate questionnaire, Perry stated she would have voted FOR H.R. 2616 (Stopping Indoctrination and Protecting Kids Act — requires parental consent before schools may change a student's gender markers or pronouns on school forms, and prohibits using federal education funds to teach gender ideology), and attacked her opponent for voting NO. Her platform states: 'Parents have the right to participate and decide what content, to include criteria such as age appropriateness, is being taught to their children.'",
              ["https://patch.com/virginia/ashburn/julie-perry-running-gop-va-10-primary-candidate-questionnaire",
               "https://www.congress.gov/bill/119th-congress/house-bill/2616"]),
        claim("jp2", "julie-perry", "economic_stewardship", 2, True,
              "In her June 2026 Patch questionnaire Perry pledged to 'push for fiscal responsibility, oppose reckless spending, and support policies who bring down inflation so families can afford to live, work, and raise children.' She criticizes federal 'administrative bloat, DEI programs, and overspending on lawyers' as examples of wasteful spending that she will target — a consistent anti-deficit, limited-government fiscal posture.",
              ["https://patch.com/virginia/ashburn/julie-perry-running-gop-va-10-primary-candidate-questionnaire",
               "https://www.fauquiernow.com/news/government_politics/three-way-race-to-determine-gop-challenger-for-subramanyam-s-10th-district-seat/article_a450efad-cf7e-5fc1-af99-44eaf2fd19d0.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents same-slug/different-state collisions."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see enrich-batch-4.py docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
