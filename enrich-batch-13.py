#!/usr/bin/env python3
"""Enrichment batch 13: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators from the bottom of the alphabet (MN–NH)
that had 0 evidence claims.

Mix (2 R / 3 D): Eric Schmitt (MO-R), Cindy Hyde-Smith (MS-R),
Tina Smith (MN-D), Maggie Hassan (NH-D), Jeanne Shaheen (NH-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Eric Schmitt (MO-R, US Senator) ----------------
    ("eric-schmitt", "MO", "Senator", [
        claim("es1", "eric-schmitt", "sanctity_of_life", 0, True,
              "A consistent pro-life legislator who, as Missouri AG, immediately enforced the state's trigger law banning abortion within minutes of the Dobbs decision in June 2022. He holds a 100% pro-life Senate voting record and an A+ rating from SBA Pro-Life America, affirming protection of unborn life from conception.",
              ["https://en.wikipedia.org/wiki/Eric_Schmitt",
               "https://sbaprolife.org/scorecard"]),
        claim("es2", "eric-schmitt", "self_defense", 1, True,
              "Received an A+ rating and endorsement from the NRA Political Victory Fund in his 2022 Senate race and has maintained a consistent anti-restriction posture in the Senate, opposing gun bans, waiting periods, and red-flag proposals.",
              ["https://en.wikipedia.org/wiki/Eric_Schmitt",
               "https://ballotpedia.org/Eric_Schmitt"]),
        claim("es3", "eric-schmitt", "border_immigration", 1, True,
              "As Missouri AG led a multistate coalition that kept Trump's 'Remain in Mexico' (MPP) policy in force; as a Senator he has championed mandatory deportations, declaring he will never 'inhibit law enforcement's ability to execute the deportations the American people voted on in November 2024.'",
              ["https://www.schmitt.senate.gov/media/press-releases/senator-schmitt-on-impending-immigration-enforcement-debate-bring-it-on/",
               "https://en.wikipedia.org/wiki/Eric_Schmitt"]),
    ]),

    # ---------------- Cindy Hyde-Smith (MS-R, US Senator) ----------------
    ("cindy-hyde-smith", "MS", "Senator", [
        claim("chs1", "cindy-hyde-smith", "sanctity_of_life", 0, True,
              "Chairs the Senate Pro-Life Caucus in the 119th Congress (2025-2026) and carries a 100% pro-life voting record per SBA Pro-Life America. She has never voted to fund abortion providers and cosponsored legislation protecting unborn life at every stage of development.",
              ["https://sbaprolife.org/senator/cindy-hyde-smith",
               "https://www.hydesmith.senate.gov/pro-life"]),
        claim("chs2", "cindy-hyde-smith", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (December 2022), which codified federal recognition of same-sex marriages, becoming one of only 36 senators to oppose the bill — reflecting her commitment to the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Cindy_Hyde-Smith",
               "https://ballotpedia.org/Cindy_Hyde-Smith"]),
        claim("chs3", "cindy-hyde-smith", "self_defense", 1, True,
              "In the 119th Congress introduced legislation to prohibit federal funding of state firearm ownership databases, directly opposing the government gun-registry infrastructure the rubric identifies as a threat to Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Cindy_Hyde-Smith",
               "https://ballotpedia.org/Cindy_Hyde-Smith"]),
    ]),

    # ---------------- Tina Smith (MN-D, US Senator) ----------------
    ("tina-smith", "MN", "Senator", [
        claim("ts1", "tina-smith", "sanctity_of_life", 4, False,
              "Served as a Planned Parenthood Vice President from 2003 to 2006 — a direct organizational and financial tie to the nation's largest abortion provider — placing her squarely inside the abortion-industry network the rubric flags at question 4.",
              ["https://en.wikipedia.org/wiki/Tina_Smith",
               "https://ballotpedia.org/Tina_Smith"]),
        claim("ts2", "tina-smith", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (2022) codifying same-sex marriage in federal law, championed LGBTQ diplomatic protections, and co-authored a New York Times op-ed expanding abortion access after Dobbs — consistently rejecting the one-man-one-woman marriage definition and the sanctity-of-life framework.",
              ["https://en.wikipedia.org/wiki/Tina_Smith",
               "https://ballotpedia.org/Tina_Smith"]),
        claim("ts3", "tina-smith", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), which expanded background-check requirements for buyers under 21 and funded state red-flag law implementation, and as a new senator signed a letter calling for federal gun-violence hearings after the 2018 Stoneman Douglas shooting — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Tina_Smith",
               "https://ballotpedia.org/Tina_Smith"]),
    ]),

    # ---------------- Maggie Hassan (NH-D, US Senator) ----------------
    ("maggie-hassan", "NH", "Senator", [
        claim("mh1", "maggie-hassan", "sanctity_of_life", 0, False,
              "A consistent abortion-rights advocate who cosponsored the Women's Health Protection Act to codify abortion access in federal law and who has publicly opposed state restrictions on abortion — rejecting recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Maggie_Hassan",
               "https://ballotpedia.org/Maggie_Hassan"]),
        claim("mh2", "maggie-hassan", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), which expanded background-check requirements for gun buyers under 21 and provided federal grants to implement state red-flag laws — directly opposing the rubric's call to protect unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Maggie_Hassan",
               "https://ballotpedia.org/Maggie_Hassan"]),
        claim("mh3", "maggie-hassan", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan (2021, $1.9T), the Infrastructure Investment and Jobs Act (2021, $1.2T), and the Inflation Reduction Act (2022, ~$750B) — major deficit-increasing packages that the rubric's balanced-budget and fiscal-stewardship standard opposes.",
              ["https://en.wikipedia.org/wiki/Maggie_Hassan",
               "https://ballotpedia.org/Maggie_Hassan"]),
    ]),

    # ---------------- Jeanne Shaheen (NH-D, US Senator) ----------------
    ("jeanne-shaheen", "NH", "Senator", [
        claim("js1", "jeanne-shaheen", "sanctity_of_life", 4, False,
              "Received a perfect 2024 legislative score from Reproductive Freedom for All (the successor organization to NARAL Pro-Choice America), confirming she consistently votes with the abortion-industry endorsement-and-funding network the rubric flags at question 4.",
              ["https://reproductivefreedomforall.org/lawmaker/jeanne-shaheen/",
               "https://en.wikipedia.org/wiki/Jeanne_Shaheen"]),
        claim("js2", "jeanne-shaheen", "self_defense", 1, False,
              "A consistent gun-control advocate who voted for the Bipartisan Safer Communities Act (2022) expanding background checks and funding red-flag laws, and has backed universal background check legislation across multiple Congresses — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Jeanne_Shaheen",
               "https://ballotpedia.org/Jeanne_Shaheen"]),
        claim("js3", "jeanne-shaheen", "foreign_policy_restraint", 1, False,
              "As the senior Democrat on the Senate Foreign Relations Committee, Shaheen was a lead advocate for the $95B Ukraine/Israel/Taiwan aid package passed in February 2024 and has consistently pushed for open-ended U.S. military commitments abroad — opposing the rubric's call to end forever wars and restore Article I war powers.",
              ["https://en.wikipedia.org/wiki/Jeanne_Shaheen",
               "https://ballotpedia.org/Jeanne_Shaheen"]),
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
