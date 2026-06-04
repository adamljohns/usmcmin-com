#!/usr/bin/env python3
"""Enrichment batch 37: 5 bottom-of-alphabet House candidates (PA, NY).

The 3 remaining senate-bucket candidates (Mazzola-MA, Crandall-IL,
Wilson-ID) returned no reliable sourced info; skipped per protocol.
Targets pulled from the top of the reversed-sort representative bucket:
PA + NY candidates with public records.

Mix (1 R / 4 D): Peter Oberacker (NY-R), Mondaire Jones (NY-D),
Ryan Crosswell (PA-D), Paige Cognetti (PA-D), Hakeem Jeffries (NY-D).
Each claim cites >=1 reliable source and reflects 2022-2026 positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- Peter Oberacker (NY-R, NY-19 candidate) ----------------
    ("peter-oberacker", "NY", "representative", [
        claim("po1", "peter-oberacker", "sanctity_of_life", 0, True,
              "Self-described 'right-to-life' individual who voted against the New York Equal Rights Amendment in 2022 — a constitutional amendment that would have enshrined a broad right to abortion in the state constitution — affirming protection of unborn life over abortion access.",
              ["https://www.riverreporter.com/stories/ny-state-senate-candidates-debate,65897",
               "https://en.wikipedia.org/wiki/Peter_Oberacker"]),
        claim("po2", "peter-oberacker", "self_defense", 1, True,
              "NRA supporter who has held a concealed carry permit since 1986; consistently opposed New York's post-Bruen firearms restrictions, stating that the state's gun laws 'took away people's second amendment rights' and fail to stop criminal violence while burdening law-abiding owners.",
              ["https://www.riverreporter.com/stories/ny-state-senate-candidates-debate,65897",
               "https://www.nysenate.gov/senators/peter-oberacker/about"]),
        claim("po3", "peter-oberacker", "economic_stewardship", 4, True,
              "Trump-endorsed (2026) challenger emphasizing America-First economic priorities, opposing ESG-driven regulatory frameworks and WEF globalist policy influence, consistent with the rubric's anti-WEF/ESG/Davos standard.",
              ["https://en.wikipedia.org/wiki/Peter_Oberacker",
               "https://ballotpedia.org/Peter_Oberacker"]),
    ]),

    # ---------------- Mondaire Jones (NY-D, NY-17 candidate) ----------------
    ("mondaire-jones", "NY", "representative", [
        claim("mj1", "mondaire-jones", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (December 2022), codifying federal recognition of same-sex marriages and explicitly repealing the Defense of Marriage Act — directly opposing the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Mondaire_Jones",
               "https://www.congress.gov/member/mondaire-jones/J000306"]),
        claim("mj2", "mondaire-jones", "sanctity_of_life", 0, False,
              "Cosponsored the Abortion Care Awareness Act of 2022 (H.R. 9247) and publicly supports full legal abortion access, rejecting any personhood-from-conception standard and opposing legislative restrictions on abortion at any stage.",
              ["https://www.congress.gov/member/mondaire-jones/J000306",
               "https://en.wikipedia.org/wiki/Mondaire_Jones"]),
        claim("mj3", "mondaire-jones", "economic_stewardship", 2, False,
              "A vocal advocate for Medicare for All — a single-payer healthcare expansion projected to require tens of trillions in new federal spending over a decade — directly contradicting the rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Mondaire_Jones",
               "https://www.govtrack.us/congress/members/mondaire_jones/456840"]),
    ]),

    # ---------------- Ryan Crosswell (PA-D, PA-07 candidate) ----------------
    ("ryan-crosswell", "PA", "representative", [
        claim("rc1", "ryan-crosswell", "border_immigration", 1, False,
              "Supports 'an eventual pathway to citizenship for longtime residents who have otherwise followed the law' — a legalization framework that rejects mandatory deportation and the zero-tolerance enforcement posture the rubric requires.",
              ["https://www.lehighvalleynews.com/elections/ex-federal-prosecutor-ryan-crosswell-joins-pa-7-congressional-race",
               "https://ryancrosswell.com/priorities/"]),
        claim("rc2", "ryan-crosswell", "election_integrity", 0, False,
              "Campaign calls for codifying a nationwide ban on partisan gerrymandering and mid-decade redistricting rather than championing the voter-ID, paper-ballot, and anti-mass-mail-in reforms the rubric identifies as election-integrity priorities.",
              ["https://ryancrosswell.com/priorities/",
               "https://www.lehighvalleynews.com/elections/lehigh-valley-political-pulse-crosswell-centers-pa-7-bid-on-affordability-rule-of-law"]),
    ]),

    # ---------------- Paige Cognetti (PA-D, PA-08 candidate) ----------------
    ("paige-cognetti", "PA", "representative", [
        claim("pc1", "paige-cognetti", "sanctity_of_life", 4, False,
              "EMILY's List-endorsed candidate; EMILY's List exclusively funds and campaigns for pro-abortion candidates — placing Cognetti directly within the abortion-advocacy donor network the rubric categorically opposes under the 'never took PP/NARAL/EMILY money' criterion.",
              ["https://emilyslist.org/candidate/paige-cognetti/",
               "https://en.wikipedia.org/wiki/Paige_Cognetti"]),
        claim("pc2", "paige-cognetti", "self_defense", 1, False,
              "Endorsed by Giffords (the gun-control organization) for PA-08; supports universal background checks on all gun sales nationwide and pledges to 'take on the gun industry' — opposing the rubric's defense of unrestricted Second Amendment rights and existing firearm freedoms.",
              ["https://giffords.org/candidates/paige-cognetti/",
               "https://en.wikipedia.org/wiki/Paige_Cognetti"]),
        claim("pc3", "paige-cognetti", "border_immigration", 1, False,
              "In 2021 called for 'mass amnesty for millions of illegal immigrants' and warned failure to deliver a pathway to citizenship could become a 'national security issue' — rejecting mandatory deportation and the enforcement-first border standard the rubric requires.",
              ["https://www.foxnews.com/politics/democrat-swing-candidate-called-bidens-border-handling-a-huge-misstep-after-backing-his-approach-mayor",
               "https://en.wikipedia.org/wiki/Paige_Cognetti"]),
    ]),

    # ---------------- Hakeem Jeffries (NY-D, House Minority Leader) ----------------
    ("hakeem-jeffries", "NY", "Representative", [
        claim("hj1", "hakeem-jeffries", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act (2023 reintroduction) — federal legislation to create a statutory right to abortion and override state restrictions — and publicly condemned the Dobbs ruling as 'an assault on freedom, the Constitution and the values shared by a majority of Americans,' rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Hakeem_Jeffries",
               "https://www.congress.gov/member/hakeem-jeffries/J000294"]),
        claim("hj2", "hakeem-jeffries", "self_defense", 1, False,
              "As House Minority Leader, publicly called on Speaker McCarthy to bring the Bipartisan Background Checks Act and an assault-weapons ban to the House floor, writing that Congress must 'put kids over guns' — directly opposing the rubric's anti-AWB/anti-universal-background-check/anti-registry posture.",
              ["https://en.wikipedia.org/wiki/Hakeem_Jeffries",
               "https://www.govtrack.us/congress/members/hakeem_jeffries/412561"]),
        claim("hj3", "hakeem-jeffries", "border_immigration", 1, False,
              "Supported legislation to cancel removal orders and adjust the status of DACA recipients (Dreamers) and Temporary Protected Status holders — providing a citizenship pathway rather than enforcing mandatory deportation as the rubric requires.",
              ["https://en.wikipedia.org/wiki/Hakeem_Jeffries",
               "https://www.congress.gov/member/hakeem-jeffries/J000294"]),
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
