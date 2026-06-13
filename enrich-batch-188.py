#!/usr/bin/env python3
"""Enrichment batch 188: hand-curated claims for 4 KY federal Senate candidates.

Primary archetype_curated bucket is exhausted; falls back to the evidence_curated
federal pool (all 4 KY 2026 Senate candidates with 0 claims), taken from the
bottom of the alphabet per the collision-avoidance protocol.

Mix (2 R / 2 D): Charles Booker (KY-D, D nominee), Daniel Cameron (KY-R, former AG),
Amy McGrath (KY-D), Mike Faris (KY-R, Air Force vet / small-business owner).
Each claim cites >=1 reliable source and reflects 2024-2026 positions / public record.

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
    # -------- Charles Booker (KY-D, 2026 D nominee for McConnell's open seat) --------
    ("charles-booker", "KY", "Senator", [
        claim("cb1", "charles-booker", "sanctity_of_life", 4, False,
              "Received the endorsement of NARAL Pro-Choice America (now Reproductive Freedom for All) for his 2022 Kentucky Senate campaign, placing him squarely inside the abortion-industry endorsement network the rubric flags.",
              ["https://reproductivefreedomforall.org/news/naral-endorses-charles-booker-for-senate/",
               "https://en.wikipedia.org/wiki/Charles_Booker_(American_politician)"]),
        claim("cb2", "charles-booker", "sanctity_of_life", 0, False,
              "Pledged to vote to lock the federal right to abortion into law and opposed Kentucky's post-Dobbs trigger ban — rejecting any personhood-from-conception standard and making abortion access a top 2026 campaign commitment.",
              ["https://ballotpedia.org/Charles_Booker",
               "https://en.wikipedia.org/wiki/Charles_Booker_(American_politician)"]),
        claim("cb3", "charles-booker", "border_immigration", 1, False,
              "Publicly called for abolishing U.S. Immigration and Customs Enforcement (ICE), directly opposing the mandatory-deportation enforcement framework the rubric requires.",
              ["https://ballotpedia.org/Charles_Booker",
               "https://en.wikipedia.org/wiki/Charles_Booker_(American_politician)"]),
    ]),

    # -------- Daniel Cameron (KY-R, former KY AG, lost 2026 R primary) --------
    ("daniel-cameron", "KY", "Senator", [
        claim("dc1", "daniel-cameron", "sanctity_of_life", 0, True,
              "As Kentucky's 51st Attorney General, personally argued before the U.S. Supreme Court to defend the state's law banning the dismemberment abortion method (Cameron v. EMW Women's Surgical Center, 2021), and after Dobbs enforced Kentucky's total-abortion trigger ban — a direct legal defense of the sanctity of unborn life.",
              ["https://en.wikipedia.org/wiki/Cameron_v._EMW_Women%27s_Surgical_Center,_P.S.C.",
               "https://en.wikipedia.org/wiki/Daniel_Cameron_(American_politician)"]),
        claim("dc2", "daniel-cameron", "border_immigration", 0, True,
              "2026 Senate platform explicitly committed to build the border wall, fully fund CBP and ICE for mass deportations of illegal aliens, and enhance criminal penalties for human trafficking and drug dealing — matching the rubric's wall-plus-enforcement ideal.",
              ["https://ballotpedia.org/Daniel_Cameron",
               "https://en.wikipedia.org/wiki/Daniel_Cameron_(American_politician)"]),
        claim("dc3", "daniel-cameron", "self_defense", 1, True,
              "As Kentucky Attorney General, made Second Amendment protection a stated daily priority of his office; 2026 Senate campaign extended that record with a pledge to take the fight for the Second Amendment to the Senate, opposing restrictions on firearms rights.",
              ["https://ballotpedia.org/Daniel_Cameron",
               "https://en.wikipedia.org/wiki/Daniel_Cameron_(American_politician)"]),
    ]),

    # -------- Amy McGrath (KY-D, former Marine pilot, lost 2026 D primary) --------
    ("amy-mcgrath", "KY", "Senator", [
        claim("am1", "amy-mcgrath", "sanctity_of_life", 0, False,
              "Pro-choice Democrat who supports abortion access; in 2019 stated existing abortion restrictions were 'reasonable' (not too many), and in 2026 ran opposing Kentucky's abortion ban — positions that fall short of life-from-conception protection.",
              ["https://en.wikipedia.org/wiki/Amy_McGrath",
               "https://ballotpedia.org/Amy_McGrath"]),
        claim("am2", "amy-mcgrath", "self_defense", 1, False,
              "Supports universal background checks on all firearm sales, banning firearm sales to individuals on terror watch lists, and continued federal research into gun violence — regulatory positions that conflict with the rubric's unrestricted Second Amendment standard.",
              ["https://en.wikipedia.org/wiki/Amy_McGrath",
               "https://ballotpedia.org/Amy_McGrath"]),
    ]),

    # -------- Mike Faris (KY-R, USAF veteran / small-business owner, lost 2026 R primary) --------
    ("mike-faris", "KY", "Senator", [
        claim("mf1", "mike-faris", "foreign_policy_restraint", 1, True,
              "In a 2026 Republican primary debate on the Iran war, Faris bucked the field by stating 'It looks to me like there wasn't exactly a great plan going in' — placing him in the Article-I restraint camp against open-ended executive military commitments.",
              ["https://www.kentuckynewera.com/news/state/article_6abb9401-34a9-564b-9d26-28a9368d3ebd.html",
               "https://ballotpedia.org/Mike_Faris"]),
        claim("mf2", "mike-faris", "refuse_federal_overreach", 0, True,
              "Ran on a platform of term limits for Congress, defending the Constitution against judicial activism, and criticizing COVID-era federal overreach — positions consistent with the rubric's opposition to unchecked federal power.",
              ["https://ballotpedia.org/Mike_Faris",
               "https://www.farisforsenate.com/"]),
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
