#!/usr/bin/env python3
"""Enrichment batch 203: 5 sitting U.S. Representatives, bottom-of-alphabet states.

Targets archetype_party_default House members with 0 evidence claims.
States: NY (Riley, Mannion), NC (Adams), MI (Scholten), ME (Pingree).
All have active House terms as of 2025-2026.

Writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ------------ Josh Riley (NY-19, D) ------------
    ("josh-riley", "NY", "Representative", [
        claim("jr1", "josh-riley", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (H.R. 29, Jan 7 2025), mandating ICE detention "
              "of undocumented immigrants charged with theft, burglary, or violent crimes — one "
              "of 48 Democrats who crossed the aisle in the 263–156 House passage.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://clerk.house.gov/Votes/20256",
               "https://ballotpedia.org/Josh_Riley"]),
        claim("jr2", "josh-riley", "biblical_marriage", 2, False,
              "Voted NO on the Protection of Women and Girls in Sports Act (H.R. 28, Jan 2025), "
              "which would have prohibited transgender athletes from competing in female sports "
              "categories — rejecting the statutory exclusion of biological males from women's athletics.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://ballotpedia.org/Josh_Riley"]),
    ]),

    # ------------ John Mannion (NY-22, D) ------------
    ("john-mannion", "NY", "Representative", [
        claim("jm1", "john-mannion", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act (H.R. 12, 119th Congress, 2025), "
              "which would federally codify abortion access through all stages of pregnancy with "
              "no gestational limits, overriding state restrictions — rejecting any life-at-conception "
              "or personhood standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/12",
               "https://www.mannionforny.com/on-the-issues/reproductive-rights-freedoms/"]),
        claim("jm2", "john-mannion", "sanctity_of_life", 4, False,
              "Earned a 100% rating from Planned Parenthood across prior electoral cycles, "
              "and committed to passing the Women's Health Protection Act in Congress — placing "
              "him squarely within the abortion-industry endorsement and funding network the rubric "
              "flags at sanctity_of_life[4].",
              ["https://reproductivefreedomforall.org/lawmaker/john-mannion/",
               "https://centralcurrent.org/do-sarah-klee-hood-and-john-mannion-have-different-views-on-abortion-rights/"]),
    ]),

    # ------------ Alma Adams (NC-12, D) ------------
    ("alma-adams", "NC", "Representative", [
        claim("aa1", "alma-adams", "sanctity_of_life", 4, False,
              "Received a 100% score from Reproductive Freedom for All (successor to NARAL "
              "Pro-Choice America) in 2024, reflecting consistent support for abortion-access "
              "legislation and acceptance of endorsements from the abortion-industry funding "
              "network.",
              ["https://reproductivefreedomforall.org/lawmaker/alma-adams/",
               "https://ballotpedia.org/Alma_Adams"]),
        claim("aa2", "alma-adams", "self_defense", 1, False,
              "Voted YES on the Protecting Our Kids Act (H.R. 7910, June 2022), raising the "
              "federal rifle-purchase age from 18 to 21, creating a new ban on 'ghost guns,' "
              "and authorizing grants for state red-flag (extreme-risk protection order) laws — "
              "directly opposing constitutional-carry and Second Amendment protections.",
              ["https://adams.house.gov/media-center/press-releases/adams-votes-life-saving-gun-violence-prevention-legislation",
               "https://www.congress.gov/bill/117th-congress/house-bill/7910"]),
    ]),

    # ------------ Hillary Scholten (MI-03, D) ------------
    ("hillary-scholten", "MI", "Representative", [
        claim("hs1", "hillary-scholten", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (H.R. 29, Jan 7 2025), requiring mandatory ICE "
              "detention of undocumented immigrants charged with theft, burglary, or violent crimes — "
              "one of a handful of Democrats to cross the aisle, citing a 'common sense approach' "
              "to immigration enforcement.",
              ["https://www.wzzm13.com/article/news/politics/michigan-politics/immigration-debate-continues-in-michigan-as-laken-riley-act-receives-w-mich-democrat-support/69-ec95b769-2df7-44f3-878a-90d7bdf10d5c",
               "https://clerk.house.gov/Votes/20256"]),
        claim("hs2", "hillary-scholten", "sanctity_of_life", 0, False,
              "Voted NO on the Born-Alive Abortion Survivors Protection Act (H.R. 26, Jan 2023) "
              "and has voted to eliminate prohibitions on taxpayer funding for abortion travel; "
              "SBA Pro-Life America gives her a 0% lifetime score — rejecting all born-alive and "
              "life-at-conception protections.",
              ["https://sbaprolife.org/representative/hillary-scholten",
               "https://scholten.house.gov/media/in-the-news/representative-hillary-scholten-addresses-her-position-hr-26-and-h-con-res-3"]),
    ]),

    # ------------ Chellie Pingree (ME-01, D) ------------
    ("chellie-pingree", "ME", "Representative", [
        claim("cp1", "chellie-pingree", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act in both 2021 and 2022 (H.R. 3755 / "
              "H.R. 8296) to federally codify abortion access with no gestational limits, and "
              "cosponsored the 2025 reintroduction (H.R. 12) — repeatedly rejecting any "
              "life-at-conception or fetal-personhood standard.",
              ["https://pingree.house.gov/news/documentsingle.aspx?DocumentID=4242",
               "https://www.congress.gov/bill/117th-congress/house-bill/8296"]),
        claim("cp2", "chellie-pingree", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 2022), which "
              "provides federal grant funding to states implementing red-flag (extreme-risk "
              "protection order) laws — opposing the rubric's opposition to red-flag frameworks "
              "that allow firearm seizure without due process.",
              ["https://pingree.house.gov/issues/issue/?IssueID=14922",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states."""
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
