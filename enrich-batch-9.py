#!/usr/bin/env python3
"""Enrichment batch 9: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators with 0 evidence claims, taken from the
BOTTOM of the alphabet (OR, OH, NY, NV) to avoid collision with the
parallel top-of-alphabet enrichment loop.

Mix (2 R / 3 D): Ron Wyden (OR-D), Bernie Moreno (OH-R),
Jon Husted (OH-R), Kirsten Gillibrand (NY-D), Jacky Rosen (NV-D).
Each claim cites >=1 reliable source and reflects 2022-2026 voting
record / public positions.

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
    # ---------------- Ron Wyden (OR-D, US Senator) ----------------
    ("ron-wyden", "OR", "Senator", [
        claim("rw1", "ron-wyden", "sanctity_of_life", 4, False,
              "Holds a career 100% rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America) and personally blocked a Senate floor vote to defund Planned Parenthood — placing him squarely inside the abortion-industry endorsement and funding network the rubric rejects.",
              ["https://www.wyden.senate.gov/news/videos/watch/on-senate-floor-wyden-blocks-republican-bill-to-defund-planned-parenthood",
               "https://en.wikipedia.org/wiki/Ron_Wyden"]),
        claim("rw2", "ron-wyden", "biblical_marriage", 1, False,
              "Voted for and publicly applauded the Senate passage of the Respect for Marriage Act (S. 4651, Nov. 29, 2022), which codifies federal recognition of same-sex marriages — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.wyden.senate.gov/news/press-releases/wyden-applauds-senate-passage-of-the-respect-for-marriage-act",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("rw3", "ron-wyden", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (S. 2938, June 2022), which enhances background checks for gun buyers under 21, provides federal grants to fund state red-flag law implementation, and tightens gun-trafficking rules — opposing the rubric's commitment to unrestricted firearms rights.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/2938",
               "https://en.wikipedia.org/wiki/Ron_Wyden"]),
    ]),

    # ---------------- Bernie Moreno (OH-R, US Senator) ----------------
    ("bernie-moreno", "OH", "Senator", [
        claim("bm1", "bernie-moreno", "sanctity_of_life", 0, True,
              "Describes himself as 'absolute pro-life, no exceptions' and in 2025 voted for H.R.1 (the reconciliation bill) defunding Planned Parenthood and abortion providers through the federal Medicaid system — affirming the life-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Bernie_Moreno",
               "https://www.moreno.senate.gov/press-releases/moreno-recaps-first-year-successes-for-ohio/"]),
        claim("bm2", "bernie-moreno", "border_immigration", 1, True,
              "Introduced the RULES Act to prohibit asylum claims by prior illegal entrants, has repeatedly called for mandatory deportation of illegal aliens, and applauded the 2025 SCOTUS decision clearing mass deportation of 500,000 illegal immigrants — directly aligning with the rubric's mandatory-deportation standard.",
              ["https://www.moreno.senate.gov/press-releases/new-moreno-bill-to-crack-down-on-asylum/",
               "https://www.moreno.senate.gov/press-releases/moreno-applauds-scotus-decision-allowing-trump-to-deport-500000-illegal-aliens-from-u-s/"]),
    ]),

    # ---------------- Jon Husted (OH-R, US Senator) ----------------
    ("jon-husted", "OH", "Senator", [
        claim("jh1", "jon-husted", "election_integrity", 0, True,
              "As Ohio Secretary of State, prevailed in Husted v. Philip Randolph Institute (2018), the landmark Supreme Court ruling that set the national standard for maintaining accurate voter rolls — a cornerstone reinforcement of election integrity.",
              ["https://en.wikipedia.org/wiki/Jon_Husted",
               "https://www.husted.senate.gov/about/"]),
        claim("jh2", "jon-husted", "border_immigration", 0, True,
              "As senator, secured millions of dollars in law enforcement funding and backed the Senate Republicans' 2025 budget bill strengthening southern and northern border security — consistent with the rubric's border-wall and military-enforcement standard.",
              ["https://www.husted.senate.gov/contact/newsletters/making-ohio-safer/",
               "https://www.husted.senate.gov/about/"]),
        claim("jh3", "jon-husted", "sanctity_of_life", 0, True,
              "His official Senate biography highlights his 'track record of defending the rights of women, children, and the unborn'; as a Republican senator he backed the 2025 reconciliation package (H.R.1) that defunded abortion providers through the federal Medicaid system.",
              ["https://www.husted.senate.gov/about/",
               "https://en.wikipedia.org/wiki/Jon_Husted"]),
    ]),

    # ---------------- Kirsten Gillibrand (NY-D, US Senator) ----------------
    ("kirsten-gillibrand", "NY", "Senator", [
        claim("kg1", "kirsten-gillibrand", "sanctity_of_life", 4, False,
              "Holds a career 100% rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America), supports federal funding for Planned Parenthood, and cosponsored the Women's Health Protection Act to codify a national abortion right — firmly inside the abortion-industry endorsement and funding network.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Kirsten_Gillibrand",
               "https://justfacts.votesmart.org/candidate/key-votes/65147/kirsten-gillibrand/2/abortion"]),
        claim("kg2", "kirsten-gillibrand", "biblical_marriage", 1, False,
              "Became the first New York senator to publicly support same-sex marriage (2010) and voted for the Respect for Marriage Act (Nov. 29, 2022) codifying federal recognition of same-sex unions — explicitly rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Kirsten_Gillibrand",
               "https://www.gillibrand.senate.gov/news/press/release/gillibrand-statement-on-senate-passage-of-the-respect-for-marriage-act/"]),
        claim("kg3", "kirsten-gillibrand", "self_defense", 1, False,
              "After holding a 100% NRA rating in the House, reversed course in the Senate and now advocates for an assault-weapons ban, universal background checks, waiting periods, and red-flag laws — abandoning the pro-gun record the rubric values.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Kirsten_Gillibrand"]),
    ]),

    # ---------------- Jacky Rosen (NV-D, US Senator) ----------------
    ("jacky-rosen", "NV", "Senator", [
        claim("jr1", "jacky-rosen", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice America and Planned Parenthood; backed federal funding for Planned Parenthood and cosponsored the Women's Health Protection Act to codify a national abortion right — placing her inside the abortion-industry endorsement and funding network.",
              ["https://en.wikipedia.org/wiki/Jacky_Rosen",
               "https://ballotpedia.org/Jacky_Rosen"]),
        claim("jr2", "jacky-rosen", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (Senate vote #362, Nov. 29, 2022), codifying federal recognition of same-sex marriages, and cosponsored the Equality Act to extend LGBTQ protections in federal civil-rights law — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/Jacky_Rosen"]),
        claim("jr3", "jacky-rosen", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (S. 2938, June 2022), which enhances firearm background checks for buyers under 21 and provides federal funding for states to implement red-flag laws — supporting gun restrictions the rubric opposes.",
              ["https://www.rosen.senate.gov/2022/06/24/rosen-votes-to-pass-historic-bipartisan-gun-reform-and-mental-health-legislation-bill-advances-out-of-senate/",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938"]),
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
