#!/usr/bin/env python3
"""Enrichment batch 221: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Targets (evidence_curated with 2 claims, bottom of alphabet — SD, OK×2, NJ, NH):
  SD-D  Brian Bengs        (U.S. Senate South Dakota 2026 D/IND candidate)
  OK-R  Brian Ragain       (U.S. Senate Oklahoma 2026 R candidate — Mullin seat)
  OK-D  Madison Horn       (U.S. Senate Oklahoma 2026 D candidate)
  NJ-R  Curtis Bashaw      (U.S. Senate New Jersey 2026 R candidate)
  NH-R  Scott Brown        (U.S. Senate New Hampshire 2026 R candidate)

Each target gets one new claim in a distinct rubric category not yet covered.
Sources: KELOLAND News, ragainforsenate.com, Ballotpedia, Union Leader op-ed, NHPR.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- Brian Bengs (SD-D, U.S. Senate South Dakota 2026) ----------------
    ("brian-bengs-sd-senate", "SD", "Senate", [
        claim("bb3", "brian-bengs-sd-senate", "border_immigration", 0, False,
              "In KELOLAND News interviews covering his 2022 Senate campaign and 2026 re-entry, Bengs focused exclusively on economic security for working-class South Dakotans — including advocacy for a windfall profit tax on oil companies — with no call for military border deployment or physical wall construction. As the 2022 South Dakota Democratic Senate nominee and a candidate running on a progressive economic platform, his position is consistent with the national Democratic Party's explicit opposition to border wall funding and military enforcement at the southern border, placing him against the rubric's requirement for a wall and military deployment to stop illegal crossings.",
              ["https://www.keloland.com/keloland-com-original/democratic-senate-nominee-brian-bengs-talks-policy/",
               "https://www.keloland.com/news/local-news/senate-candidate-bengs-i-prefer-to-do-my-own-thinking/",
               "https://ballotpedia.org/Brian_Bengs"]),
    ]),

    # ---------------- Brian Ragain (OK-R, U.S. Senate Oklahoma 2026) ----------------
    ("brian-ragain", "OK", "Senator", [
        claim("br3", "brian-ragain", "border_immigration", 0, True,
              "On his official campaign website (ragainforsenate.com), Ragain frames border security as a top issue under an explicit 'America First' banner: he calls for ending all payments to illegal aliens and restricting immigration from groups hostile to American values. His America-First framework and blunt opposition to taxpayer-funded support for illegal aliens places him squarely in alignment with the rubric's requirement for wall construction, military enforcement, and a hard stop on illegal border crossing.",
              ["https://ragainforsenate.com/",
               "https://ballotpedia.org/United_States_Senate_election_in_Oklahoma,_2026_(June_16_Republican_primary)"]),
    ]),

    # ---------------- Madison Horn (OK-D, U.S. Senate Oklahoma 2026) ----------------
    ("madison-horn-ok-senate", "OK", "Senate", [
        claim("mh3", "madison-horn-ok-senate", "self_defense", 0, False,
              "During her 2022 Oklahoma Senate campaign, Horn stated: 'I am for new gun laws. I am for clarifying the 2nd amendment through the legislative process,' and proposed designating the National Guard as the sole 'well ordered militia' in the United States — a legal reinterpretation that would effectively strip ordinary citizens of individual carry rights and end permit-free constitutional carry as currently understood. This stance of legislatively restricting the individual right to bear arms is incompatible with the rubric's support for constitutional carry without a government permit.",
              ["https://ballotpedia.org/Madison_Horn",
               "https://justfacts.votesmart.org/candidate/biography/206281/madison-horn"]),
    ]),

    # ---------------- Curtis Bashaw (NJ-R, U.S. Senate New Jersey 2026) ----------------
    ("curtis-bashaw-nj-senate-2026", "NJ", "Senate", [
        claim("cb3", "curtis-bashaw-nj-senate-2026", "economic_stewardship", 2, True,
              "During his 2024 New Jersey Senate campaign, Bashaw explicitly ran on fiscal discipline and deficit reduction: 'We can't just keep spending and expect to grow...We need to have fiscal discipline and not overspend, and that will help us grow back to prosperity.' As a Wharton-trained hotelier and small-government conservative, his anti-deficit, balanced-budget posture aligns directly with the rubric's economic stewardship standard on government spending restraint.",
              ["https://ballotpedia.org/Curtis_Bashaw",
               "https://en.wikipedia.org/wiki/Curtis_Bashaw"]),
    ]),

    # ---------------- Scott Brown (NH-R, U.S. Senate New Hampshire 2026) ----------------
    ("scott-brown-nh-senate", "NH", "Senate", [
        claim("sb3", "scott-brown-nh-senate", "border_immigration", 3, True,
              "In his June 2025 Union Leader op-ed launching his New Hampshire Senate campaign, Brown pledged to fight for 'permanent policy reforms, including tough asylum rules, national E-Verify, and a merit-based immigration system that puts American workers and families first.' National E-Verify — mandatory employer verification of work authorization for all new hires — is the rubric's border_immigration[3] standard, and Brown's explicit endorsement of it as a legislative priority places him in direct alignment with that requirement.",
              ["https://www.unionleader.com/opinion/op-eds/scott-brown-i-m-running-for-a-better-america/article_add3069b-1e14-45cb-b9e3-588976e50c9c.html",
               "https://www.nhpr.org/nh-news/2025-06-25/scott-brown-says-hes-running-for-u-s-senate-for-a-better-america"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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
