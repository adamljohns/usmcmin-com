#!/usr/bin/env python3
"""Enrichment batch 215: 2nd-round claims for 5 sitting U.S. Senators (NC x2, NE x2, NJ).

archetype_curated bucket exhausted; targets are evidence_curated senators from
the bottom of the alphabet (NC, NE, NJ) with 2-3 existing claims.

Candidates: Thom Tillis (NC-R), Ted Budd (NC-R), Deb Fischer (NE-R),
Pete Ricketts (NE-R), Cory Booker (NJ-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions across rubric categories not yet covered for each senator.

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
    # ---------------- Thom Tillis (NC-R, US Senator) ----------------
    ("thom-tillis", "NC", "Senator", [
        claim("tt3", "thom-tillis", "sanctity_of_life", 0, True,
              "A consistent pro-life vote in the Senate who in January 2025 co-introduced the Born-Alive Abortion Survivors Protection Act, requiring medical care for any infant born alive during an attempted abortion. Has called himself a protector of life 'before and after birth' and backed legislation restricting abortion funding.",
              ["https://www.tillis.senate.gov/2025/1/tillis-introduces-bill-to-protect-babies-born-after-failed-abortions",
               "https://www.tillis.senate.gov/2021/1/tillis-reaffirms-commitment-to-protecting-life",
               "https://en.wikipedia.org/wiki/Thom_Tillis"]),
        claim("tt4", "thom-tillis", "self_defense", 0, True,
              "NRA-endorsed senator who in January 2025 introduced the Constitutional Concealed Carry Reciprocity Act, allowing law-abiding permit holders to carry concealed across state lines. Has also fought Biden administration gun-control rules that threatened to reclassify lawful owners as felons, and has consistently backed Second Amendment rights in the Senate.",
              ["https://www.tillis.senate.gov/2025/1/tillis-colleagues-introduce-concealed-carry-reciprocity-bill",
               "https://www.tillis.senate.gov/2023/3/tillis-colleagues-fight-to-stop-biden-administration-from-turning-lawful-gun-owners-into-felons",
               "https://www.nrapvf.org/articles/20140908/nra-endorses-thom-tillis-for-us-senate-in-north-carolina"]),
    ]),

    # ---------------- Ted Budd (NC-R, US Senator) ----------------
    ("ted-budd", "NC", "Senator", [
        claim("tb4", "ted-budd", "economic_stewardship", 2, True,
              "Co-sponsored the Balanced Budget Amendment to the U.S. Constitution in February 2023, which would require the President and Congress to produce a balanced federal budget each year. States the national debt is 'unsustainable and unacceptable' and that a constitutional amendment is necessary to force fiscal discipline on both parties.",
              ["https://www.budd.senate.gov/2023/02/10/budd-sponsors-balanced-budget-amendment/",
               "https://www.budd.senate.gov/priority-issues/controlling-government-spending/"]),
        claim("tb5", "ted-budd", "economic_stewardship", 0, True,
              "Co-sponsored Senator Ted Cruz's legislation to block the Federal Reserve from issuing a central bank digital currency (CBDC), opposing a government-controlled surveillance-capable digital dollar — directly aligning with the rubric's anti-CBDC position.",
              ["https://www.budd.senate.gov/category/government-spending/",
               "https://www.cruz.senate.gov/newsroom/press-releases/sen-cruz-introduces-bill-to-block-federal-reserve-from-issuing-central-bank-digital-currency"]),
    ]),

    # ---------------- Deb Fischer (NE-R, US Senator) ----------------
    ("deb-fischer", "NE", "Senator", [
        claim("df4", "deb-fischer", "self_defense", 1, True,
              "Opposed the Bipartisan Safer Communities Act in June 2022, stating she had 'serious concerns about legislation that would infringe upon law-abiding citizens' Second Amendment rights and limit due process,' and pledged to use all legislative tools to oppose gun-control measures. Maintains a consistent pro-Second Amendment voting record.",
              ["https://www.fischer.senate.gov/public/index.cfm/2022/6/fischer-statement-on-gun-legislation",
               "https://ballotpedia.org/Deb_Fischer"]),
        claim("df5", "deb-fischer", "border_immigration", 0, True,
              "A strong border-security advocate who criticized President Biden for rescinding Remain in Mexico, border-wall construction, and other Trump-era enforcement policies on his first day in office, writing in a June 2024 column that 'political reaction, not good policy, motivated these changes' and calling for a return to proven enforcement measures.",
              ["https://www.fischer.senate.gov/public/index.cfm/2024/6/politics-yield-bad-border-policy",
               "https://ballotpedia.org/Deb_Fischer"]),
    ]),

    # ---------------- Pete Ricketts (NE-R, US Senator) ----------------
    ("pete-ricketts", "NE", "Senator", [
        claim("pr4", "pete-ricketts", "biblical_marriage", 0, True,
              "Ran for governor and Senate on a conservative platform opposing same-sex marriage and abortion. Was not in the Senate for the November 2022 Respect for Marriage Act vote (appointed January 2023); has not supported federal recognition of same-sex marriage, consistent with a one-man-one-woman definition. His first three co-sponsored bills as senator were legislation to ban federal abortion funding.",
              ["https://en.wikipedia.org/wiki/Pete_Ricketts",
               "https://ballotpedia.org/Pete_Ricketts",
               "https://www.govtrack.us/congress/members/pete_ricketts/456952"]),
        claim("pr5", "pete-ricketts", "economic_stewardship", 2, True,
              "As Nebraska governor delivered over $12.7 billion in tax relief and held state budget growth to an average of 2.8% annually — well below inflation. In the Senate voted against the Fiscal Responsibility Act of 2023 as insufficiently hawkish, and supports balanced-budget discipline. A consistent opponent of unsustainable deficit spending.",
              ["https://www.ricketts.senate.gov/about/",
               "https://en.wikipedia.org/wiki/Pete_Ricketts",
               "https://ballotpedia.org/Pete_Ricketts"]),
    ]),

    # ---------------- Cory Booker (NJ-D, US Senator) ----------------
    ("cory-booker", "NJ", "Senator", [
        claim("cb4", "cory-booker", "self_defense", 1, False,
              "A leading Senate gun-control advocate who introduced the Federal Firearm Licensing Act (requiring DOJ licenses before any firearm purchase), co-introduced the Assault Weapons Ban of 2017, backed red-flag 'extreme risk protection order' legislation, and praised President Biden's executive orders expanding gun-control measures — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.booker.senate.gov/news/press/booker-introduces-federal-firearm-licensing-act-as-senate-reconvenes-from-august-recess",
               "https://www.booker.senate.gov/?p=press_release&id=696",
               "https://en.wikipedia.org/wiki/Political_positions_of_Cory_Booker"]),
        claim("cb5", "cory-booker", "border_immigration", 0, False,
              "Has consistently opposed border-wall construction and stricter deportation enforcement. In February 2024 he voted to advance the bipartisan border deal while publicly opposing several of its provisions as violating 'Americans' shared values' by excluding asylum seekers fleeing violence. Opposes military-backed border enforcement and mandatory deportation.",
              ["https://www.booker.senate.gov/news/press/booker-statement-on-senate-border-bill",
               "https://en.wikipedia.org/wiki/Political_positions_of_Cory_Booker"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
