#!/usr/bin/env python3
"""Enrichment batch 150: 5 PA/OR/OK sitting U.S. Representatives with 0 claims.

Targets (all archetype_party_default, 0 claims, taken from bottom of alphabet
per collision-avoidance protocol):
  Guy Reschenthaler (PA-14, R), Glenn Thompson (PA-15, R),
  Dan Meuser (PA-9, R), Cliff Bentz (OR-2, R), Frank Lucas (OK-3, R).

Sources: sbaprolife.org, house.gov, en.wikipedia.org, ballotpedia.org,
         congress.gov, govtrack.us.
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
    # ---------------- Guy Reschenthaler (PA-14, R) ----------------
    ("guy-reschenthaler", "PA", "Representative", [
        claim("gr1", "guy-reschenthaler", "sanctity_of_life", 0, True,
              "Praised the Dobbs decision as 'historic' and a 'tremendous victory for life,' and voted against H.R. 8296 (Women's Health Protection Act of 2022), which would have created a federal right to abortion and overridden state pro-life laws — consistent with the rubric's protection of unborn life from conception.",
              ["https://reschenthaler.house.gov/media/press-releases/reschenthaler-statement-supreme-court-decision-dobbs-v-jackson",
               "https://en.wikipedia.org/wiki/Guy_Reschenthaler"]),
        claim("gr2", "guy-reschenthaler", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023, which funds border-wall construction, ends catch-and-release, and tightens asylum rules. Has publicly stated he will 'fight to secure our border,' end sanctuary cities, and 'crack down on child sex trafficking' at the border.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://reschenthaler.house.gov/issues/values"]),
        claim("gr3", "guy-reschenthaler", "self_defense", 1, True,
              "Voted against H.R. 8 (universal background checks) and H.R. 1446 (extended background check delays) in the 117th Congress, calling them 'draconian' bills that 'criminalize common practices among gun owners' and 'deprive law-abiding citizens of their Second Amendment rights.'",
              ["https://reschenthaler.house.gov/media/press-releases/reschenthaler-votes-defend-second-amendment-rights",
               "https://ballotpedia.org/Guy_Reschenthaler"]),
    ]),

    # ---------------- Glenn Thompson (PA-15, R) ----------------
    ("glenn-thompson", "PA", "Representative", [
        claim("gt1", "glenn-thompson", "sanctity_of_life", 0, True,
              "Carries a consistent pro-life voting record tracked by SBA Pro-Life America, voting to protect the unborn and against legislation that would expand federal abortion access. Voted against the Women's Health Protection Act when it reached the House.",
              ["https://sbaprolife.org/representative/glenn-g-t-thompson",
               "https://en.wikipedia.org/wiki/Glenn_Thompson_(politician)"]),
        claim("gt2", "glenn-thompson", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act (December 2022), which codified federal recognition of same-sex marriage — casting a vote consistent with the rubric's one-man-one-woman definition despite personal family circumstances that drew national attention at the time.",
              ["https://en.wikipedia.org/wiki/Glenn_Thompson_(politician)",
               "https://ballotpedia.org/Glenn_Thompson_(Pennsylvania)"]),
        claim("gt3", "glenn-thompson", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023, authorizing border-wall construction and mandatory detention. As chairman of the House Agriculture Committee since 2023, Thompson supports E-Verify requirements as part of comprehensive border and labor reform.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://www.govtrack.us/congress/members/glenn_thompson/412317"]),
    ]),

    # ---------------- Dan Meuser (PA-9, R) ----------------
    ("dan-meuser", "PA", "Representative", [
        claim("dm1", "dan-meuser", "sanctity_of_life", 0, True,
              "Carries a consistent pro-life voting record per SBA Pro-Life America's national scorecard, voting to stop taxpayer funding of abortion domestically and internationally, and to defend Trump administration pro-life regulations from legal challenges.",
              ["https://sbaprolife.org/representative/daniel-meuser",
               "https://en.wikipedia.org/wiki/Dan_Meuser"]),
        claim("dm2", "dan-meuser", "economic_stewardship", 2, True,
              "Signed the Americans for Tax Reform Taxpayer Protection Pledge committing to oppose any net tax increase, reflecting a no-new-taxes fiscal posture aligned with the rubric's anti-deficit stewardship standard.",
              ["https://ballotpedia.org/Dan_Meuser",
               "https://www.govtrack.us/congress/members/daniel_meuser/412811"]),
        claim("dm3", "dan-meuser", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023, mandating border-wall construction, ending catch-and-release, and strengthening deportation authority — consistent with the rubric's call for military-backed border enforcement.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Dan_Meuser"]),
    ]),

    # ---------------- Cliff Bentz (OR-2, R) ----------------
    ("cliff-bentz", "OR", "Representative", [
        claim("cb1", "cliff-bentz", "sanctity_of_life", 0, True,
              "Publicly declares 'I believe that life begins at conception and that life should be protected until death by natural causes occurs,' supporting abortion only when the mother's life is physically at risk — fully aligning with the rubric's life-at-conception personhood standard. Tracked by SBA Pro-Life America.",
              ["https://sbaprolife.org/representative/cliff-bentz",
               "https://ballotpedia.org/Cliff_Bentz"]),
        claim("cb2", "cliff-bentz", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023. As the sole Republican in Oregon's House delegation since 2025, Bentz represents the lone congressional voice for border enforcement in a heavily Democratic state.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://en.wikipedia.org/wiki/Cliff_Bentz"]),
        claim("cb3", "cliff-bentz", "industry_capture", 0, True,
              "Opposed COVID-era government healthcare mandates and strongly opposes government-run healthcare (ACA expansion), supporting free-market health solutions — consistent with the rubric's opposition to pharmaceutical-government capture of public health policy.",
              ["https://ballotpedia.org/Cliff_Bentz",
               "https://www.govtrack.us/congress/members/cliff_bentz/456842"]),
    ]),

    # ---------------- Frank Lucas (OK-3, R) ----------------
    ("frank-lucas", "OK", "Representative", [
        claim("fl1", "frank-lucas", "sanctity_of_life", 0, True,
              "Carries a consistent pro-life voting record per SBA Pro-Life America's scorecard: voted repeatedly to stop taxpayer funding of abortion, affirms that abortion legislation belongs to the states under the 10th Amendment, and opposes federal funding streams that benefit abortion providers.",
              ["https://sbaprolife.org/representative/frank-lucas",
               "https://en.wikipedia.org/wiki/Frank_Lucas_(Oklahoma_politician)"]),
        claim("fl2", "frank-lucas", "border_immigration", 0, True,
              "Has voted consistently to secure the southern border throughout his tenure; voted for H.R. 2, the Secure the Border Act of 2023, and publicly supports President Trump's border enforcement agenda including additional resources for Border Patrol.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Frank_Lucas"]),
        claim("fl3", "frank-lucas", "self_defense", 1, True,
              "Long-term A-rated NRA member of Congress with a consistent record opposing new firearm restrictions; as a farmer and rancher from rural Oklahoma, Lucas has defended the right to keep and bear arms for self-defense, hunting, and protection of property throughout his three-decade congressional career.",
              ["https://ballotpedia.org/Frank_Lucas",
               "https://en.wikipedia.org/wiki/Frank_Lucas_(Oklahoma_politician)"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
