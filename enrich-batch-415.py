#!/usr/bin/env python3
"""Enrichment batch 415: evidence_federal U.S. House candidates (0 claims, bottom-alphabet).

Targets: David Jones (TN-07-D), Jack Ellison (SC-01-R, withdrew),
Jay Vaingankar (NJ-12-D, lost primary), Brad Cohen (NJ-12-D, lost primary).

Sourced from campaign websites, WHYY voter guide, Daily Princetonian, and
ABC News 4 coverage. Covers distinct rubric categories per candidate.
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
    # ---------------- David Jones (TN-07, D, 2026 primary challenger) ----------------
    ("david-jones-tn-07", "TN", "Representative", [
        claim("dj1", "david-jones-tn-07", "self_defense", 0, True,
              "His campaign website explicitly lists 'gun rights' among the core individual rights he pledges to 'uphold for all Tennesseans,' alongside freedom of speech and medical freedom — reflecting a constitutional-carry, pro-Second-Amendment posture.",
              ["https://www.davidjonesfortn.com/issues/"]),
        claim("dj2", "david-jones-tn-07", "foreign_policy_restraint", 1, True,
              "Campaigns on 'avoiding entangling alliances' and limits the U.S. military mission to homeland defense: 'strong, appropriately sized armed forces that are properly prepared to defend homes from immediate attacks' — directly aligning with the call to end open-ended overseas military engagements.",
              ["https://www.davidjonesfortn.com/issues/"]),
        claim("dj3", "david-jones-tn-07", "economic_stewardship", 2, True,
              "Cites runaway national debt as a critical concern and pledges to keep 'the federal government out of citizens' lives and pocketbooks,' reflecting a balanced-budget, anti-deficit posture — his 2022 campaign page quantified the debt burden at $250,000 per taxpayer.",
              ["https://www.davidjonesfortn.com/issues/",
               "https://ballotpedia.org/David_Jones_(Tennessee_congressional_candidate)"]),
    ]),

    # ---------------- Jack Ellison (SC-01, R, withdrew 3/25/2026) ----------------
    ("jack-ellison", "SC", "Representative", [
        claim("je1", "jack-ellison", "economic_stewardship", 2, True,
              "Before withdrawing to finish his MUSC doctorate, pledged to 'demand fiscal responsibility including a balanced budget delivered on time' and 'a reduction in federal spending of 5% per department per year,' calling the national debt 'a security threat, an unsustainable burden, and totally unnecessary.'",
              ["https://crowdblue.com/candidates/019635a60b5e721cb05688e2606c6973/jack-ellison",
               "https://abcnews4.com/news/lowcountry-and-state-politics/lowcountry-native-veteran-jack-ellison-enters-race-for-scs-1st-congressional-district-south-carolina-politics-one-on-one-interview"]),
        claim("je2", "jack-ellison", "refuse_federal_overreach", 0, True,
              "Ran on 'limited government, fiscal responsibility, and a strong national defense' as his three-pillar platform, consistently framing the federal government as too large and campaigning on rolling back its footprint across departments.",
              ["https://abcnews4.com/news/lowcountry-and-state-politics/lowcountry-native-veteran-jack-ellison-enters-race-for-scs-1st-congressional-district-south-carolina-politics-one-on-one-interview",
               "https://scdailygazette.com/2026/01/12/14-candidates-are-running-to-replace-rep-nancy-mace-in-congress/"]),
    ]),

    # ---------------- Jay Vaingankar (NJ-12, D, lost June 2026 primary) ----------------
    ("jay-vaingankar", "NJ", "House", [
        claim("jv1", "jay-vaingankar", "border_immigration", 2, False,
              "Campaigned explicitly on abolishing ICE — the enforcement agency whose elimination would effectively create sanctuary conditions nationwide — directly opposing the rubric's anti-sanctuary, enforcement-first immigration standard.",
              ["https://www.dailyprincetonian.com/article/2026/02/news-adpol-jay-vaingankar-former-dept-energy-official-runs-nj-12-democratic-nomination",
               "https://whyy.org/articles/new-jersey-election-2026-primary-12th-congressional-district/"]),
        claim("jv2", "jay-vaingankar", "self_defense", 1, False,
              "Received a 2026 Moms Demand Action 'Gun Sense Voter' co-endorsement and ran on strict gun-control measures, signaling support for the expanded firearm regulations (red-flag laws, assault-weapons restrictions) the rubric opposes.",
              ["https://whyy.org/articles/new-jersey-election-2026-primary-12th-congressional-district/",
               "https://www.jayvaingankar.com/press/release-qualified-debate"]),
        claim("jv3", "jay-vaingankar", "foreign_policy_restraint", 1, True,
              "Included 'putting an end to forever wars' as a core campaign commitment, aligning with the rubric's call to wind down open-ended overseas military engagements and repeal the blank-check AUMFs that authorize them.",
              ["https://www.jayvaingankar.com/",
               "https://newjerseyglobe.com/congress/the-final-list-of-whos-running-for-congress-in-new-jersey-in-2026/"]),
    ]),

    # ---------------- Brad Cohen (NJ-12, D, lost June 2026 primary) ----------------
    ("brad-cohen", "NJ", "House", [
        claim("bc1", "brad-cohen", "sanctity_of_life", 0, False,
              "An OBGYN and East Brunswick mayor who ran explicitly on abortion-rights advocacy, warning that 'women today have fewer rights than when I started practice' and that abortion restrictions would cause women to die from self-induced procedures — rejecting any life-from-conception or personhood standard.",
              ["https://www.dailyprincetonian.com/article/2026/04/princeton-news-broadfocus-brad-cohen-nj-12-democratic-nomination-mayor-east-brunswick-obgyn",
               "https://bradcohenforcongress.com/"]),
        claim("bc2", "brad-cohen", "self_defense", 1, False,
              "Received the 2026 Moms Demand Action 'Gun Sense Candidate' Distinction, signaling active support for expanded gun regulations — the opposite of the rubric's demand for an end to red-flag laws, assault-weapons bans, and magazine-capacity limits.",
              ["https://www.dailyprincetonian.com/article/2026/04/princeton-news-broadfocus-brad-cohen-nj-12-democratic-nomination-mayor-east-brunswick-obgyn",
               "https://bradcohenforcongress.com/"]),
        claim("bc3", "brad-cohen", "foreign_policy_restraint", 1, False,
              "Set himself apart from most NJ-12 competitors at the Rider University debate by openly defending continued American military funding for Israel when other candidates called for cuts — contrary to the rubric's non-entanglement standard of ending open-ended foreign military commitments.",
              ["https://www.dailyprincetonian.com/article/2026/04/princeton-news-broadfocus-nj12-candidates-debate-at-rider-university"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents wrong-state same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
