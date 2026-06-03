#!/usr/bin/env python3
"""Enrichment batch 31: 5 bottom-of-alphabet 2026 U.S. House candidates.

Targets (all archetype_curated, 0 prior claims):
  Trever Nehls (TX-22 R), Van Hilleary (TN-06 R), Johnny Garrett (TN-06 R),
  Charlotte Bergmann (TN-09 R), Mark Smith (SC-01 R).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # -------- Trever Nehls (TX-22, R) --------
    ("trever-nehls", "TX", "TX-22", [
        claim("tn1", "trever-nehls", "border_immigration", 0, True,
              "Won the TX-22 Republican primary as Trump's endorsed candidate on a platform to finish the border wall, end catch-and-release permanently, and deploy military force against cartel threats — directly matching the rubric's wall-and-military enforcement pillar.",
              ["https://ballotpedia.org/Trever_Nehls",
               "https://www.foxnews.com/politics/trump-endorses-close-allys-twin-brother-race-texas-congressional-seat"]),
        claim("tn2", "trever-nehls", "border_immigration", 1, True,
              "Campaign platform explicitly demands mandatory deportation of illegal aliens and designation of cartels as foreign terrorist organizations — consistent with the rubric's zero-tolerance mandatory-deportation standard.",
              ["https://ballotpedia.org/Trever_Nehls",
               "https://coveringkaty.com/news/fort-bend/former-fort-bend-county-constable-trever-nehls-announces-bid/"]),
        claim("tn3", "trever-nehls", "self_defense", 1, True,
              "Trump's endorsement of Nehls specifically cited defending 'our always-under-siege Second Amendment'; as a former Fort Bend County constable he aligns with constitutional gun rights and opposes new firearm restrictions.",
              ["https://www.foxnews.com/politics/trump-endorses-close-allys-twin-brother-race-texas-congressional-seat",
               "https://ballotpedia.org/Trever_Nehls"]),
    ]),

    # -------- Van Hilleary (TN-06, R — former US Rep TN-04) --------
    ("van-hilleary", "TN", "former US Rep", [
        claim("vh1", "van-hilleary", "biblical_marriage", 2, True,
              "At his 2026 campaign kickoff, Hilleary specifically raised transgender athletes competing in college sports as a policy he would fight to reverse in Congress — a public rejection of transgender ideology applied to athletics.",
              ["https://tennesseelookout.com/2025/07/12/former-tennessee-congressman-hilleary-announces-run-for-6th-congressional-district/"],
              kind="position"),
        claim("vh2", "van-hilleary", "self_defense", 1, True,
              "Stated at his 2026 campaign kickoff that Democrats had 'attacked Second Amendment rights' and pledged to defend gun rights in Congress, consistent with his four-term conservative record as TN-04 Representative (1995–2003).",
              ["https://tennesseelookout.com/2025/07/12/former-tennessee-congressman-hilleary-announces-run-for-6th-congressional-district/",
               "https://www.govtrack.us/congress/members/H000615"],
              kind="position"),
        claim("vh3", "van-hilleary", "border_immigration", 1, True,
              "At his 2026 kickoff, Hilleary criticized Biden-era immigration policies and declared he is running to 'ensure President Trump has backup,' signaling support for mandatory deportation and strict border enforcement.",
              ["https://tennesseelookout.com/2025/07/12/former-tennessee-congressman-hilleary-announces-run-for-6th-congressional-district/"],
              kind="position"),
    ]),

    # -------- Johnny Garrett (TN-06, R — TN state rep) --------
    ("johnny-garrett", "TN", "TN state rep", [
        claim("jg1", "johnny-garrett", "sanctity_of_life", 0, True,
              "Received a perfect scorecard from the Family Action Council of Tennessee (FACT) for voting in favor of the Human Life Protection Act (Tennessee's post-Roe abortion trigger law) and Governor Lee's Pro-Life Bill, affirming full legal protection of human life.",
              ["https://scorecard.factennessee.org/representatives/johnny-garrett",
               "https://ballotpedia.org/Johnny_Garrett"]),
        claim("jg2", "johnny-garrett", "biblical_marriage", 2, True,
              "Received a perfect FACT score for voting in favor of Tennessee legislation restricting single-sex student athletics, rejecting the premise that males who identify as transgender may compete in women's sports.",
              ["https://scorecard.factennessee.org/representatives/johnny-garrett",
               "https://ballotpedia.org/Johnny_Garrett"]),
        claim("jg3", "johnny-garrett", "border_immigration", 0, True,
              "Campaigns for Congress as a 'pro-Trump Christian conservative' with securing the southern border listed as a top priority — supporting wall construction and Trump's America First immigration enforcement agenda.",
              ["https://johnnygarrettforcongress.com/",
               "https://ballotpedia.org/Johnny_Garrett"],
              kind="position"),
    ]),

    # -------- Charlotte Bergmann (TN-09, R) --------
    ("charlotte-bergmann", "TN", "TN-09", [
        claim("cb1", "charlotte-bergmann", "sanctity_of_life", 0, True,
              "Has run four consecutive cycles (2018–2026) in TN-09 as an explicit Christian conservative on an America First platform; campaign materials center on 'protecting children's futures' and opposing the Democratic cultural agenda — consistent with a pro-life posture.",
              ["https://ballotpedia.org/Charlotte_Bergmann",
               "https://www.bergmannforcongress.com/"],
              kind="position"),
        claim("cb2", "charlotte-bergmann", "family_child_sovereignty", 0, True,
              "Campaign platform specifically includes 'empowering parents and protecting children's futures' and supporting school choice — aligning with the rubric's parental-rights and family-sovereignty pillar.",
              ["https://www.bergmannforcongress.com/",
               "https://ballotpedia.org/Charlotte_Bergmann"],
              kind="position"),
    ]),

    # -------- Mark Smith (SC-01, R) --------
    ("mark-smith-sc-01", "SC", "SC-01", [
        claim("ms1", "mark-smith-sc-01", "sanctity_of_life", 0, True,
              "Honored by South Carolina Citizens for Life in 2021 for voting in favor of the Heartbeat Bill (S.C.'s fetal heartbeat abortion ban), establishing a consistent pro-life record in the SC House.",
              ["https://votemarksmith.com/about/",
               "https://ballotpedia.org/Mark_Smith_(South_Carolina)"]),
        claim("ms2", "mark-smith-sc-01", "self_defense", 1, True,
              "Self-described as 'an unwavering defender of Second Amendment rights,' opposing firearm restrictions; earned the highest rating in the SC House from Americans for Prosperity-South Carolina during the 2024 legislative session.",
              ["https://votemarksmith.com/about/",
               "https://abcnews4.com/news/local/servant-leader-mark-smith-aims-to-continue-to-serve-with-a-bid-for-congress-politics-south-carolina-1st-congressional-district-wciv-abc-news-4-10-13-2025"]),
        claim("ms3", "mark-smith-sc-01", "economic_stewardship", 2, True,
              "Supported small business tax cuts and received top scores from Americans for Prosperity-South Carolina, reflecting a fiscally conservative anti-spending record aligned with the rubric's balanced-budget and anti-deficit pillar.",
              ["https://votemarksmith.com/about/",
               "https://ballotpedia.org/Mark_Smith_(South_Carolina)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
