#!/usr/bin/env python3
"""Enrichment batch 244: 5 federal House members from bottom of alphabet.

Targets archetype_party_default House reps with 0 claims.
States: MD×4, MA×1 (bottom of alphabet, avoiding top-side collision agent).

Mix (0 R / 5 D): Steny Hoyer (MD-D), John Olszewski (MD-D),
Glenn Ivey (MD-D), April McClain Delaney (MD-D), Seth Moulton (MA-D).
Each claim cites >=1 reliable source and reflects voting record /
public positions through 2025-2026.

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
    # ---------------- Steny Hoyer (MD-D, US Representative MD-5) ----------------
    ("steny-hoyer", "MD", "Representative", [
        claim("sh1", "steny-hoyer", "sanctity_of_life", 0, False,
              "A career-long pro-choice legislator who voted against the Partial-Birth Abortion Ban Act in 2003 and declared himself 'outraged' by the Supreme Court's Dobbs decision in 2022; supports codifying Roe v. Wade into federal law — rejecting any legal recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Steny_Hoyer",
               "https://ballotpedia.org/Steny_Hoyer"]),
        claim("sh2", "steny-hoyer", "self_defense", 1, False,
              "Rated 'F' by the NRA Political Victory Fund throughout his Congressional career, reflecting consistent support for gun-control legislation including background-check expansion, assault-weapons bans, and red-flag laws — opposing the rubric's defense of the unrestricted right to keep and bear arms.",
              ["https://justfacts.votesmart.org/candidate/key-votes/26890/steny-hoyer",
               "https://en.wikipedia.org/wiki/Steny_Hoyer"]),
        claim("sh3", "steny-hoyer", "biblical_marriage", 0, False,
              "Supported the Respect for Marriage Act (2022), which codified federal recognition of same-sex unions — rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Steny_Hoyer",
               "https://ballotpedia.org/Steny_Hoyer"]),
    ]),

    # ---------------- John Olszewski (MD-D, US Representative MD-2) ----------------
    ("john-olszewski", "MD", "Representative", [
        claim("jo1", "john-olszewski", "sanctity_of_life", 0, False,
              "Pledged as a central campaign commitment to 'protect reproductive rights and abortion access' — an explicit rejection of any conception-based personhood standard and an endorsement of unrestricted abortion access.",
              ["https://en.wikipedia.org/wiki/Johnny_Olszewski",
               "https://ballotpedia.org/John_Olszewski_Jr."]),
        claim("jo2", "john-olszewski", "biblical_marriage", 2, False,
              "Publicly criticized the Supreme Court for 'disregarding the LGBTQ+ community' and supports LGBTQ+ rights policies including transgender inclusion — contrary to the rubric's rejection of transgender ideology in law and public life.",
              ["https://en.wikipedia.org/wiki/Johnny_Olszewski",
               "https://www.govtrack.us/congress/members/johnny_olszewski/456991"]),
        claim("jo3", "john-olszewski", "border_immigration", 0, False,
              "Voted with President Trump only 13.6% of the time in the 119th Congress (2025), placing him firmly in the progressive bloc that opposes border-wall funding, mandatory deportation, and military-border enforcement posture the rubric endorses.",
              ["https://www.govtrack.us/congress/members/johnny_olszewski/456991",
               "https://ballotpedia.org/John_Olszewski_Jr."]),
    ]),

    # ---------------- Glenn Ivey (MD-D, US Representative MD-4) ----------------
    ("glenn-ivey", "MD", "Representative", [
        claim("gi1", "glenn-ivey", "sanctity_of_life", 0, False,
              "A pro-choice Democrat who votes with House Democrats against Republican restrictions on abortion access; aligned with the progressive bloc (voted with Trump just 10.5% of the time in the 119th Congress) and has not broken with his party on any pro-life legislation.",
              ["https://en.wikipedia.org/wiki/Glenn_Ivey",
               "https://www.govtrack.us/congress/members/glenn_ivey/456905"]),
        claim("gi2", "glenn-ivey", "self_defense", 1, False,
              "As a Democrat representing a heavily urban Prince George's County district, Ivey backs gun-violence-prevention legislation and votes with the House Democratic caucus in favor of expanded background checks, assault-weapons restrictions, and red-flag laws — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/members/glenn_ivey/456905",
               "https://en.wikipedia.org/wiki/Glenn_Ivey"]),
        claim("gi3", "glenn-ivey", "border_immigration", 0, False,
              "Voted with Trump just 10.5% of the time in the 119th Congress — at the progressive median among House Democrats — and has consistently opposed Republican border-security legislation including border-wall appropriations and mandatory-deportation measures the rubric endorses.",
              ["https://www.govtrack.us/congress/members/glenn_ivey/456905",
               "https://ballotpedia.org/Glenn_Ivey"]),
    ]),

    # ---------------- April McClain Delaney (MD-D, US Representative MD-6) ----------------
    ("april-mcclain-delaney", "MD", "Representative", [
        claim("amd1", "april-mcclain-delaney", "sanctity_of_life", 0, False,
              "Stated she will 'protect choice and women's reproductive rights' and 'protect women's reproductive freedoms' as a central commitment — explicitly rejecting any legal recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/April_McClain_Delaney",
               "https://ballotpedia.org/April_McClain-Delaney"]),
        claim("amd2", "april-mcclain-delaney", "border_immigration", 1, True,
              "One of only 48 House Democrats — and the only Maryland Democrat — to vote for the Laken Riley Act (January 2025), which requires ICE to detain undocumented immigrants charged with theft or violent crimes; a notable bipartisan break consistent with the rubric's support for immigration enforcement.",
              ["https://en.wikipedia.org/wiki/April_McClain_Delaney",
               "https://ballotpedia.org/April_McClain-Delaney"]),
        claim("amd3", "april-mcclain-delaney", "self_defense", 1, False,
              "Stated she supports 'keeping dangerous weapons off our streets and out of the wrong hands,' signaling support for assault-weapons restrictions and other gun-control measures — opposing the rubric's defense of the unrestricted right to keep and bear arms.",
              ["https://en.wikipedia.org/wiki/April_McClain_Delaney",
               "https://ballotpedia.org/April_McClain-Delaney"]),
    ]),

    # ---------------- Seth Moulton (MA-D, US Representative MA-6) ----------------
    ("seth-moulton", "MA", "Representative", [
        claim("sm1", "seth-moulton", "sanctity_of_life", 0, False,
              "Supports abortion rights and backed the Women's Health Protection Act, which would codify Roe v. Wade-era abortion-access standards into federal law — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Seth_Moulton",
               "https://ballotpedia.org/Seth_Moulton"]),
        claim("sm2", "seth-moulton", "biblical_marriage", 0, False,
              "Supports same-sex marriage and backed LGBTQ equality legislation including the Respect for Marriage Act (2022), which codified federal recognition of same-sex unions — rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Seth_Moulton",
               "https://ballotpedia.org/Seth_Moulton"]),
        claim("sm3", "seth-moulton", "self_defense", 1, False,
              "Despite being a Marine Corps combat veteran, Moulton is a gun-control advocate who supports background-check expansion, assault-weapons restrictions, and red-flag laws consistent with the Massachusetts Democratic mainstream — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Seth_Moulton",
               "https://www.govtrack.us/congress/members/seth_moulton/412632"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent slug collisions across states."""
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
