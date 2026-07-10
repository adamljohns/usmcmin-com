#!/usr/bin/env python3
"""Enrichment batch 611: additional claims for 5 active 2026 federal House candidates.

archetype_curated bucket is fully exhausted; batch targets evidence_curated
candidates with only 3 prior claims, adding 2 new claims each in DISTINCT
rubric categories. Bottom-of-alphabet states: VA, TX, TN, SC, TN.

Candidates (1D/1D-TX/1R-TN/1R-SC/1R-TN):
  Patrick Mosolf     (VA-02, D) — USAID veteran, 2026 D challenger to Kiggans
  Marquette Greene-Scott (TX-22, D) — 2026 D Nominee, won March primary
  Jon Henry          (TN-06, R) — USMC colonel (ret.), 2026 R candidate open Rose seat
  Sam McCown         (SC-01, R) — physician, 2026 R candidate open Mace seat (lost primary)
  Jay Reedy          (TN-07, R) — TN state rep dist-74, 2026 R candidate open TN-07

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ----------- Patrick Mosolf (VA-02, D) -----------
    ("patrick-mosolf", "VA", "VA-02", [
        claim("pm1", "patrick-mosolf", "economic_stewardship", 2, False,
              "Opposes 'irrational tariffs' as harmful to Americans and campaigns for expanding Affordable Care Act subsidies, opening new public-option healthcare pathways, and more aggressively regulating the insurance and pharmaceutical industry — a government-expansion posture that conflicts with the rubric's balanced-budget and anti-deficit standard.",
              ["https://www.patrickmosolf.com/issues"]),
        claim("pm2", "patrick-mosolf", "border_immigration", 1, False,
              "A former senior USAID official married to a naturalized immigrant, Mosolf has not called for mandatory deportation or mass removal of those in the country unlawfully; his platform centers on restoring democratic governance and legal immigration pathways rather than the deportation-first enforcement the rubric favors.",
              ["https://www.patrickmosolf.com/about",
               "https://ballotpedia.org/Patrick_Mosolf"]),
    ]),

    # ----------- Marquette Greene-Scott (TX-22, D) -----------
    ("marquette-greene-scott", "TX", "TX-22", [
        claim("mgs1", "marquette-greene-scott", "self_defense", 1, False,
              "Endorsed by Moms Demand Action, which campaigns for universal background checks, red-flag laws, and bans on semi-automatic rifles, branding Greene-Scott a 'gun sense candidate' — positioning her in opposition to the constitutional carry and anti-restriction posture the rubric requires.",
              ["https://ballotpedia.org/Marquette_Greene-Scott"]),
        claim("mgs2", "marquette-greene-scott", "economic_stewardship", 2, False,
              "Advocates expanding federal spending on infrastructure, job training, healthcare, and childcare, citing public demand for government investment to address the 'affordability crisis' — a government-growth orientation that conflicts with the rubric's deficit-reduction and balanced-budget requirement.",
              ["https://marquettegreenescott.com/issues/"]),
    ]),

    # ----------- Jon Henry (TN-06, R) -----------
    ("jon-henry-tn-06", "TN", "TN-06", [
        claim("jh1", "jon-henry-tn-06", "refuse_federal_overreach", 0, True,
              "Pledges to 'fight the weaponization of government, whether it's the IRS, the DOJ, or any agency used to punish political opponents,' and signed the U.S. Term Limits congressional pledge — committing to rein in the federal bureaucratic footprint the rubric marks against career-politician overreach.",
              ["https://www.jhenryforcongress.com/issues",
               "https://termlimits.com/jon-henry-pledges-to-support-congressional-term-limits/"]),
        claim("jh2", "jon-henry-tn-06", "industry_capture", 2, True,
              "Made foreign takeover of American food production a flagship issue, pledging to 'take action on the TN land grab, double standard of processing of our food, and help eliminate the foreign takeover of our food availability and security' — directly opposing the agribusiness and foreign-ownership capture the rubric's anti-Big Ag criterion targets.",
              ["https://www.jhenryforcongress.com/issues"]),
    ]),

    # ----------- Sam McCown (SC-01, R) -----------
    ("sam-mccown", "SC", "SC-01", [
        claim("sm1", "sam-mccown", "sanctity_of_life", 0, True,
              "A physician who is 'proudly pro-life': supports protecting the life of the unborn, opposes taxpayer funding for abortion, and preserves religious freedom for medical providers — a record aligned with the rubric's life-from-conception standard, anchored in his medical ethics background.",
              ["https://sammccown.com/issues/",
               "https://abcnews4.com/news/local/republican-physician-announces-run-for-lowcountrys-us-house-seat-wciv-abc-news-4-charleston-sc-south-carolina-sam-mccown"]),
        claim("sm2", "sam-mccown", "self_defense", 1, True,
              "Explicitly identifies as a 'defender of the Second Amendment' who supports the right to bear arms for all law-abiding Americans and opposes new restrictions on firearms — a clean anti-restriction record aligned with the rubric's opposition to red-flag laws, assault-weapon bans, and magazine limits.",
              ["https://sammccown.com/issues/"]),
    ]),

    # ----------- Jay Reedy (TN-07, R) -----------
    ("jay-reedy", "TN", "TN-07", [
        claim("jr1", "jay-reedy", "sanctity_of_life", 0, True,
              "As a Tennessee state representative (District 74 since 2015), Reedy compiled a strong pro-life record tracked by the Family Action Council of Tennessee (FACT): voted for measures prohibiting county and municipal abortion funding and supported Tennessee's near-total abortion ban after Dobbs (2022) — consistent with the rubric's life-from-conception standard.",
              ["https://scorecard.factennessee.org/representatives/jay-reedy",
               "https://ballotpedia.org/Jay_Reedy"]),
        claim("jr2", "jay-reedy", "self_defense", 0, True,
              "An NRA Life Member since 1986, Reedy has pledged 'I will oppose any limitations or constraints on our rights as citizens to keep and bear arms' and voted in the Tennessee state house for 2023 legislation authorizing trained school faculty and staff to carry concealed firearms on campus — expanding lawful carry rather than adding restrictions.",
              ["https://ballotpedia.org/Jay_Reedy",
               "https://scorecard.factennessee.org/representatives/jay-reedy"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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
