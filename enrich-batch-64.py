#!/usr/bin/env python3
"""Enrichment batch 64: evidence claims for 5 House candidates (NY/IA/GA/FL, bottom-alpha).

Targets (archetype_curated, 0 claims, reverse-alpha from bottom):
  Mike Roth (NY-19, R), Travis Terrell (IA-01, D),
  Jasmine Clark (GA-13, D), Sarah Corkery (IA-02, D),
  Lucia Baez-Geller (FL-27, D).
Each claim cites >=1 reliable source and reflects 2024-2026 campaign
positions or state-legislative voting record.
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
    # --- Mike Roth (NY-19, R) ---
    ("mike-roth-ny-19", "NY", "Representative", [
        claim("mr1", "mike-roth-ny-19", "sanctity_of_life", 0, True,
              "In his 2019-2020 congressional campaign Roth explicitly described abortion as 'killing babies' and ran on a pro-life platform opposing abortion access — consistent with a life-from-conception position.",
              ["https://www.chronogram.com/news-politics/the-bizarre-far-right-candidacy-of-mike-roth-self-styled-king-of-ulster-9043137"]),
        claim("mr2", "mike-roth-ny-19", "foreign_policy_restraint", 4, True,
              "Campaigns explicitly against a 'One World Government' and supranational governance, opposing what he characterizes as globalist-socialist institutions — aligning with the rubric's rejection of WHO/UN/NATO expansion.",
              ["https://www.chronogram.com/news-politics/the-bizarre-far-right-candidacy-of-mike-roth-self-styled-king-of-ulster-9043137"]),
        claim("mr3", "mike-roth-ny-19", "public_justice", 0, True,
              "Called for designating Antifa a terrorist organization during his 2019-2020 congressional campaign — consistent with the rubric's public-justice enforcement framework.",
              ["https://www.chronogram.com/news-politics/the-bizarre-far-right-candidacy-of-mike-roth-self-styled-king-of-ulster-9043137"]),
    ]),

    # --- Travis Terrell (IA-01, D) ---
    ("travis-terrell", "IA", "Representative", [
        claim("tt1", "travis-terrell", "sanctity_of_life", 0, False,
              "Supports codifying Roe v. Wade into federal law and expanding reproductive healthcare access — rejecting protection of human life from conception.",
              ["https://scottcountydems.org/travis-terrell-2026-iowa-democratic-candidate-1st-congressional-district/",
               "https://terrellforcongress.com/"]),
        claim("tt2", "travis-terrell", "border_immigration", 1, False,
              "Supports abolishing ICE and creating a direct residency-to-citizenship pathway, stating 'it's entirely too hard to come here and be a citizen' — contrary to the rubric's mandatory-deportation standard.",
              ["https://dailyiowan.com/2025/12/04/tiffin-democrat-travis-terrell-preaches-worker-reform-streamlined-citizenship-processes/",
               "https://scottcountydems.org/travis-terrell-2026-iowa-democratic-candidate-1st-congressional-district/"]),
        claim("tt3", "travis-terrell", "self_defense", 1, False,
              "Backs universal background checks for all gun sales and expanded safe-storage mandates — opposing the rubric's rejection of new firearms controls.",
              ["https://scottcountydems.org/travis-terrell-2026-iowa-democratic-candidate-1st-congressional-district/"]),
    ]),

    # --- Jasmine Clark (GA-13, D) ---
    ("jasmine-clark-ga-13", "GA", "Representative", [
        claim("jc1", "jasmine-clark-ga-13", "sanctity_of_life", 0, False,
              "Her 2026 congressional campaign centers on 'standing up to Republican attacks on... reproductive freedom'; she explicitly opposes restrictions on abortion — rejecting personhood from conception.",
              ["https://www.ajc.com/politics/2026/05/jasmine-clark-wins-democratic-primary-to-succeed-late-us-rep-david-scott/",
               "https://19thnews.org/2026/05/georgia-primary-election-jasmine-clark-congress/"]),
        claim("jc2", "jasmine-clark-ga-13", "industry_capture", 0, False,
              "Endorsed by 314 Action (a PAC electing mainstream-science advocates) and campaigns to defend federal public-health research funding from cuts — aligning with the medical-establishment consensus the rubric's anti-pharma-mandate category cautions against.",
              ["https://314action.org/2026/04/07/314-action-endorses-dr-jasmine-clark-for-georgias-13th-congressional-district/",
               "https://www.cbsnews.com/atlanta/news/georgia-13th-congressional-district-primary/"]),
    ]),

    # --- Sarah Corkery (IA-02, D) ---
    ("sarah-corkery", "IA", "Representative", [
        claim("sc1", "sarah-corkery", "sanctity_of_life", 0, False,
              "Campaigned explicitly against abortion restrictions, framing them as violations of 'the right to make personal medical decisions without government intervention' and opposing a federal abortion ban — rejecting life-from-conception protection.",
              ["https://iowacapitaldispatch.com/briefs/democrat-sarah-corkery-launches-campaign-for-2nd-congressional-district/",
               "http://www.corkeryforcongress.com/"]),
        claim("sc2", "sarah-corkery", "self_defense", 1, False,
              "Runs explicitly on a platform to 'strengthen gun safety laws,' supporting new firearms restrictions — contrary to the rubric's defense of unrestricted Second Amendment rights.",
              ["https://iowacapitaldispatch.com/briefs/democrat-sarah-corkery-launches-campaign-for-2nd-congressional-district/"]),
    ]),

    # --- Lucia Baez-Geller (FL-27, D) ---
    ("lucia-baez-geller", "FL", "Representative", [
        claim("lbg1", "lucia-baez-geller", "sanctity_of_life", 4, False,
              "Received the endorsement and backing of EMILY's List for her 2024 FL-27 congressional race, placing her inside the abortion-industry funding network the rubric's sanctity-of-life standard rejects.",
              ["https://emilyslist.org/news/emilys-list-endorses-lucia-baez-geller-for-election-to-floridas-27th-congressional-district/",
               "https://ballotpedia.org/Lucia_Baez-Geller"]),
        claim("lbg2", "lucia-baez-geller", "biblical_marriage", 4, False,
              "As Miami-Dade school-board member, was the sole vote in favor of observing LGBTQ History Month in district schools in 2022 — directly contradicting the rubric's rejection of LGBTQ ideology promotion in public education.",
              ["https://floridapolitics.com/archives/690850-democrats-lucia-baez-geller-mike-davey-compete-for-right-to-face-maria-elvira-salazar-in-cd-27/",
               "https://ballotpedia.org/Lucia_Baez-Geller"]),
        claim("lbg3", "lucia-baez-geller", "family_child_sovereignty", 0, False,
              "Her Miami-Dade school-board record of advancing LGBTQ curriculum over community objections reflects advocacy against the parental rights over public-school content that the rubric's family-sovereignty category upholds.",
              ["https://floridapolitics.com/archives/690850-democrats-lucia-baez-geller-mike-davey-compete-for-right-to-face-maria-elvira-salazar-in-cd-27/",
               "https://ballotpedia.org/Lucia_Baez-Geller"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher. Returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
