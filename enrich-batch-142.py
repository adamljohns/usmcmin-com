#!/usr/bin/env python3
"""Enrichment batch 142: 5 federal House members (GA x3, FL x2, DE x1).

Bottom-of-alphabet pick from evidence_federal candidates with 0 claims.
Targets: Clay Fuller (GA-14, R), Mike Haridopolos (FL-08, R),
Daniel Webster (FL-11, R, retiring), Sanford Bishop (GA-02, D),
Sarah McBride (DE-AL, D).

Each target gets 2 claims spanning distinct rubric categories drawn from
confirmed 2024-2026 voting records, public statements, and official sources.
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
    # ---------------- Clay Fuller (GA-14, R — special election April 2026, succeeded MTG) ----------------
    ("clay-fuller", "GA", "Representative", [
        claim("cf1", "clay-fuller", "self_defense", 1, True,
              "During his 2026 special-election campaign, Fuller explicitly vowed to 'fight back against the radical left as they try to limit our Constitutional freedoms, most importantly those enshrined in our 1st and 2nd Amendments' — directly opposing any assault-weapons ban, magazine-limit, or registry proposal.",
              ["https://ballotpedia.org/Clayton_Fuller",
               "https://en.wikipedia.org/wiki/Clay_Fuller"]),
        claim("cf2", "clay-fuller", "border_immigration", 1, True,
              "Stated he supported 'all efforts to empower the Trump Administration as they seek to remove the millions of illegal immigrants who do not have permission to be in this country' — aligning with the rubric's mandatory-deportation plank.",
              ["https://ballotpedia.org/Clayton_Fuller",
               "https://en.wikipedia.org/wiki/Clay_Fuller"]),
    ]),

    # ---------------- Mike Haridopolos (FL-08, R — sitting since Jan 2025, former FL Senate President) ----------------
    ("mike-haridopolos", "FL", "Representative", [
        claim("mh1", "mike-haridopolos", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America, which credited him with having 'consistently advocated for innocent babies, their mothers & the taxpayers' throughout his legislative career — a multi-cycle pro-life record aligning with the rubric's life-from-conception standard.",
              ["https://sbaprolife.org/candidate/mike-haridopolos",
               "https://ballotpedia.org/Mike_Haridopolos"]),
        claim("mh2", "mike-haridopolos", "self_defense", 1, True,
              "Carried an NRA 'A' rating during his tenure in the Florida Legislature and is described as 'a staunch defender of our Second Amendment rights' — opposing restrictions on firearms consistent with the rubric's self-defense plank.",
              ["https://ballotpedia.org/Mike_Haridopolos",
               "https://en.wikipedia.org/wiki/Mike_Haridopolos"]),
    ]),

    # ---------------- Daniel Webster (FL-11, R — sitting since 2017, retiring 2026) ----------------
    ("daniel-webster", "FL", "Representative", [
        claim("dw1", "daniel-webster", "sanctity_of_life", 0, True,
              "Webster publicly opposes abortion under all circumstances — the most restrictive pro-life position and a clear affirmation of unborn personhood from conception.",
              ["https://en.wikipedia.org/wiki/Daniel_Webster_(Florida_politician)",
               "https://ballotpedia.org/Daniel_Webster_(Florida)"]),
        claim("dw2", "daniel-webster", "self_defense", 1, True,
              "Long-standing NRA-supported legislator who voted YES on H.J.Res.40 (2017) to block the Obama-era rule restricting Social Security recipients with mental impairments from buying firearms, and voted YES for national concealed-carry reciprocity — a consistent record defending unrestricted gun rights.",
              ["https://en.wikipedia.org/wiki/Daniel_Webster_(Florida_politician)",
               "https://www.govtrack.us/congress/members/daniel_webster/412410"]),
    ]),

    # ---------------- Sanford Bishop (GA-02, D — sitting since 1993, Blue Dog Coalition) ----------------
    ("sanford-bishop", "GA", "Representative", [
        claim("sb1", "sanford-bishop", "border_immigration", 1, True,
              "Was one of only 46 House Democrats who joined all Republicans in passing the Laken Riley Act (2025), which requires mandatory ICE detention of undocumented immigrants who commit crimes — a border-enforcement vote sharply at odds with the Democratic mainstream.",
              ["https://en.wikipedia.org/wiki/Sanford_Bishop",
               "https://www.govtrack.us/congress/members/sanford_bishop/400030"]),
        claim("sb2", "sanford-bishop", "industry_capture", 2, False,
              "Has for decades championed federal price-support programs and crop subsidies for his southwest Georgia agriculture district, calling preservation of Big Ag subsidy structures a top legislative priority — aligning with the crony-agriculture model the rubric opposes.",
              ["https://ballotpedia.org/Sanford_Bishop_Jr.",
               "https://en.wikipedia.org/wiki/Sanford_Bishop"]),
    ]),

    # ---------------- Sarah McBride (DE-AL, D — first transgender U.S. Representative, since Jan 2025) ----------------
    ("sarah-mcbride", "DE", "Representative", [
        claim("smb1", "sarah-mcbride", "sanctity_of_life", 0, False,
              "Campaigned on and in Congress has sponsored legislation to ensure affordable abortion coverage, limit restrictions on the provision of abortion services, prohibit interference with interstate abortion access, and revise regulations banning medication-abortion drugs by mail — rejecting any protection of unborn personhood from conception.",
              ["https://en.wikipedia.org/wiki/Sarah_McBride",
               "https://ballotpedia.org/Sarah_McBride"]),
        claim("smb2", "sarah-mcbride", "biblical_marriage", 2, False,
              "The first openly transgender member of Congress; actively opposed the 2025 presidential executive order banning transgender service members from the U.S. military and sponsored legislation prohibiting discrimination against LGBTQ servicemembers — advancing the transgender ideology the rubric explicitly opposes.",
              ["https://en.wikipedia.org/wiki/Sarah_McBride",
               "https://www.govtrack.us/congress/members/sarah_mcbride/456985"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
