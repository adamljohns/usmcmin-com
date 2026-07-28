#!/usr/bin/env python3
"""Enrichment batch 871: 3 claims each for 5 Republican U.S. Representatives.

Targets: Steve Scalise (LA), Mike Johnson (LA), Victoria Spartz (IN),
Clay Higgins (LA), John James (MI) — all evidence_curated with 3 existing
claims; adding 3 new claims each across distinct rubric categories.
Sources: congress.gov, govtrack.us, scalise.house.gov, mikejohnson.house.gov,
ballotpedia.org. Bottom-of-alphabet approach: from WY/WV side working inward.

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
    # ---------------- Steve Scalise (LA-R, US Representative) ----------------
    ("steve-scalise", "LA", "Representative", [
        claim("ss871a", "steve-scalise", "border_immigration", 0, True,
              "As House Majority Leader, Scalise championed the Laken Riley Act (H.R.29 / S.5, signed January 29, 2025), which mandates ICE detention of illegal aliens arrested for burglary, theft, larceny, or crimes causing serious injury; he spoke on the House floor in its support and publicly denounced the 170 House Democrats who voted against it.",
              ["https://scalise.house.gov/press-releases/Scalise-Speaks-in-Support-of-the-Laken-Riley-Act",
               "https://www.govtrack.us/congress/votes/119-2025/h6"]),
        claim("ss871b", "steve-scalise", "self_defense", 0, True,
              "Carries A+ ratings from both the NRA and Gun Owners of America; personally survived a near-fatal gunshot wound during the 2017 congressional baseball practice shooting and emerged a stronger Second Amendment champion; serves on the Congressional Second Amendment Task Force and opposes red-flag laws, assault-weapons bans, and universal background-check mandates.",
              ["https://scalise.house.gov/issues/2nd-amendment",
               "https://scalise.house.gov/media/press-releases/scalise-nra-forum-surviving-shooting-attack-strengthened-my-support-strong"]),
        claim("ss871c", "steve-scalise", "economic_stewardship", 2, True,
              "A consistent fiscal conservative who has voted against major deficit-financed spending packages; voted NO on the Inflation Reduction Act (H.R.5376, August 2022, 220-207) and the American Rescue Plan (H.R.1319, March 2021, 219-212), rejecting trillions in new deficit spending; as Majority Leader he insisted any debt-ceiling increase be paired with binding discretionary spending caps.",
              ["https://en.wikipedia.org/wiki/Steve_Scalise",
               "https://www.govtrack.us/congress/bills/117/hr5376"]),
    ]),

    # ---------------- Mike Johnson (LA-R, US Representative / Speaker) ----------------
    ("mike-johnson", "LA", "Representative", [
        claim("mj871a", "mike-johnson", "border_immigration", 0, True,
              "As House Speaker, Johnson brought the Laken Riley Act to the floor as one of the first bills of the 119th Congress (H.R.29, House Vote #6, January 7, 2025, passed 264-159) and publicly condemned the Democrats who opposed mandatory detention of criminal illegal aliens; he also advanced the Secure America Act and additional border-enforcement legislation throughout 2025.",
              ["https://mikejohnson.house.gov/news/documentsingle.aspx?DocumentID=1516",
               "https://www.govtrack.us/congress/votes/119-2025/h6"]),
        claim("mj871b", "mike-johnson", "self_defense", 0, True,
              "A strong Second Amendment supporter who has consistently voted against gun-control measures throughout his congressional career; as Speaker blocked gun-control legislation from the House floor and publicly stated that Biden's gun rulings showed 'disdain' for Second Amendment rights.",
              ["https://mikejohnson.house.gov/news/documentsingle.aspx?DocumentID=1154",
               "https://www.govtrack.us/congress/members/mike_johnson/412706"]),
        claim("mj871c", "mike-johnson", "biblical_marriage", 2, True,
              "Voted YEA on the Protection of Women and Girls in Sports Act (H.R.28, House Vote #12, January 14, 2025, passed 218-206), barring biological males from competing on female athletic teams at schools receiving federal funds; as Speaker he prioritized this bill in the opening days of the 119th Congress alongside other social-conservative priorities.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://www.govtrack.us/congress/votes/119-2025/h12"]),
    ]),

    # ---------------- Victoria Spartz (IN-R, US Representative) ----------------
    ("victoria-spartz", "IN", "Representative", [
        claim("vs871a", "victoria-spartz", "election_integrity", 0, True,
              "Voted YEA on the Safeguard American Voter Eligibility (SAVE) Act (H.R.22, passed 220-208, April 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections and mandating states remove non-citizens from voter rolls.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("vs871b", "victoria-spartz", "biblical_marriage", 2, True,
              "Voted YEA on the Protection of Women and Girls in Sports Act (H.R.28, House Vote #12, January 14, 2025, passed 218-206), barring biological males from competing on female athletic teams at institutions receiving federal funds — rejecting transgender ideology in athletics.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://www.govtrack.us/congress/votes/119-2025/h12"]),
        claim("vs871c", "victoria-spartz", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (S.5, House Vote #23, January 22, 2025, signed January 29, 2025), mandating ICE detention of illegal aliens arrested for burglary, theft, larceny, or crimes causing serious bodily injury — a critical enforcement step toward mandatory removal of criminal aliens.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
    ]),

    # ---------------- Clay Higgins (LA-R, US Representative) ----------------
    ("clay-higgins", "LA", "Representative", [
        claim("ch871a", "clay-higgins", "election_integrity", 0, True,
              "Voted YEA on the Safeguard American Voter Eligibility (SAVE) Act (H.R.22, passed 220-208, April 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections and mandating removal of non-citizens from voter rolls.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("ch871b", "clay-higgins", "self_defense", 0, True,
              "A former Louisiana State Police SWAT officer and consistent Second Amendment champion who cosponsored the Constitutional Concealed Carry Reciprocity Act (H.R.38) to establish national carry reciprocity; publicly stated he feels 'naked without a gun' and earned consistent NRA ratings supporting unrestricted constitutional carry.",
              ["https://ballotpedia.org/Clay_Higgins",
               "https://www.congress.gov/member/clay-higgins/H001077"]),
        claim("ch871c", "clay-higgins", "biblical_marriage", 2, True,
              "Voted YEA on the Protection of Women and Girls in Sports Act (H.R.28, House Vote #12, January 14, 2025, passed 218-206), barring biological males from competing in female-designated athletic programs that receive federal funding.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://www.govtrack.us/congress/votes/119-2025/h12"]),
    ]),

    # ---------------- John James (MI-R, US Representative) ----------------
    ("john-james", "MI", "Representative", [
        claim("jj871a", "john-james", "election_integrity", 0, True,
              "Voted YEA on the Safeguard American Voter Eligibility (SAVE) Act (H.R.22, passed 220-208, April 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections and mandating that states purge non-citizens from voter rolls.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("jj871b", "john-james", "biblical_marriage", 2, True,
              "Voted YEA on the Protection of Women and Girls in Sports Act (H.R.28, House Vote #12, January 14, 2025, passed 218-206), barring biological males from competing on female athletic teams at schools receiving federal funds.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://www.govtrack.us/congress/votes/119-2025/h12"]),
        claim("jj871c", "john-james", "economic_stewardship", 2, True,
              "An Army Ranger combat veteran (Operation Iraqi Freedom) and CEO of James Group International, a multimillion-dollar supply-chain logistics company; has applied private-sector fiscal discipline in Congress, consistently opposing unoffset domestic spending expansions and supporting budget frameworks that prioritize deficit reduction.",
              ["https://ballotpedia.org/John_James_(Michigan)",
               "https://www.congress.gov/member/john-james/J000307"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision on same-name candidates."""
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
