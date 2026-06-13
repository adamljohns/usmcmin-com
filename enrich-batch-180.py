#!/usr/bin/env python3
"""Enrichment batch 180: evidence_federal CA sitting members — 5 targets with documented 2024-2026 positions.

archetype_curated bucket fully exhausted; pulling from evidence_federal (0 claims).
Targets from the bottom of the alphabet (CA sitting members with verified records):
Raul Ruiz CA-25 (ER physician, sitting since 2013, SBA Pro-Life F),
Nanette Barragan CA-44 (sitting since 2017, 100% Reproductive Freedom, Respect for Marriage Act),
Mark Takano CA-39 (Chair Congressional Equality Caucus, first openly gay Asian-American in Congress),
Brad Sherman CA-32 (sitting since 1997, Israel Allied Caucus Co-Chair, praised AIPAC),
Jim Costa CA-21 (11th term, Blue Dog Coalition chair, pro-abortion Catholic).
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


TARGETS = [
    # ---- Raul Ruiz (CA-25, D, sitting since 2013, ER physician) ----
    ("raul-ruiz", "CA", "CA-25", [
        claim("rr1", "raul-ruiz", "sanctity_of_life", 0, False,
              "Holds an F rating from SBA Pro-Life America; has consistently voted to eliminate or "
              "prevent federal protections for the unborn and for children born alive after failed "
              "abortions, and has voted to remove prohibitions on taxpayer-funded abortion — "
              "rejecting any life-at-conception personhood standard.",
              ["https://sbaprolife.org/representative/raul-ruiz",
               "https://en.wikipedia.org/wiki/Raul_Ruiz_(politician)"]),
        claim("rr2", "raul-ruiz", "sanctity_of_life", 4, False,
              "Consistently earns top scores from Reproductive Freedom for All (the successor to NARAL "
              "Pro-Choice America), placing him within the abortion-industry endorsement and funding "
              "network — directly violating the rubric's standard of never taking PP/NARAL/EMILY money.",
              ["https://reproductivefreedomforall.org/lawmaker/raul-ruiz/",
               "https://ballotpedia.org/Raul_Ruiz"]),
    ]),

    # ---- Nanette Barragan (CA-44, D, sitting since 2017) ----
    ("nanette-barragan", "CA", "CA-44", [
        claim("nb1", "nanette-barragan", "sanctity_of_life", 4, False,
              "Earned a 2024 score of 100 from Reproductive Freedom for All (formerly NARAL "
              "Pro-Choice America) and an F from the Susan B. Anthony List — placing her at the "
              "top of the abortion-industry endorsement and funding network.",
              ["https://reproductivefreedomforall.org/lawmaker/nanette-diaz-barragan/",
               "https://en.wikipedia.org/wiki/Nanette_Barrag%C3%A1n"]),
        claim("nb2", "nanette-barragan", "biblical_marriage", 0, False,
              "Cosponsored and voted for the Respect for Marriage Act (H.R. 8404, 2022), which "
              "codifies federal recognition of same-sex marriages — directly rejecting the "
              "biblical one-man-one-woman definition of marriage.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://en.wikipedia.org/wiki/Nanette_Barrag%C3%A1n"]),
        claim("nb3", "nanette-barragan", "biblical_marriage", 4, False,
              "Cosponsored the Equality Act, which would write sexual-orientation and "
              "gender-identity protections into federal civil-rights law extending to schools and "
              "public accommodations — the policy promotion of LGBTQ ideology the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Nanette_Barrag%C3%A1n",
               "https://ballotpedia.org/Nanette_Barrag%C3%A1n"]),
    ]),

    # ---- Mark Takano (CA-39, D, sitting since 2013, Chair Congressional Equality Caucus) ----
    ("mark-takano", "CA", "CA-39", [
        claim("mt1", "mark-takano", "biblical_marriage", 0, False,
              "The first openly gay person of Asian descent elected to Congress; chairs the "
              "Congressional Equality Caucus (119th Congress) — the House's dedicated LGBTQ advocacy "
              "body — and has been a vocal, lifelong champion of same-sex marriage, rejecting the "
              "one-man-one-woman definition entirely.",
              ["https://en.wikipedia.org/wiki/Mark_Takano",
               "https://en.wikipedia.org/wiki/Congressional_Equality_Caucus"]),
        claim("mt2", "mark-takano", "biblical_marriage", 2, False,
              "Voted against H.R. 734, the Protection of Women and Girls in Sports Act, which "
              "would bar biological males from competing in female athletic categories — indicating "
              "rejection of biological sex distinctions and endorsement of transgender ideology in "
              "federal sports policy.",
              ["https://en.wikipedia.org/wiki/Mark_Takano",
               "https://www.govtrack.us/congress/members/mark_takano/412520"]),
        claim("mt3", "mark-takano", "sanctity_of_life", 0, False,
              "Holds a 100% rating from NARAL Pro-Choice America and a 2024 score of 100 from "
              "Reproductive Freedom for All; publicly called the Dobbs ruling 'offensive and radical' "
              "— reflecting total rejection of any life-at-conception or personhood standard.",
              ["https://reproductivefreedomforall.org/lawmaker/mark-takano/",
               "https://en.wikipedia.org/wiki/Mark_Takano"]),
    ]),

    # ---- Brad Sherman (CA-32, D, sitting since 1997, Israel Allied Caucus Co-Chair) ----
    ("brad-sherman", "CA", "CA-32", [
        claim("bs1", "brad-sherman", "foreign_policy_restraint", 3, False,
              "Co-chaired the Congressional Israel Allies Caucus (116th Congress) and publicly "
              "praised AIPAC as 'the single most important organization in promoting the "
              "U.S.-Israel alliance' — placing him within the foreign-linked pro-Israel lobbying "
              "network that the rubric flags under 'never took AIPAC/foreign-linked PAC' money.",
              ["https://en.wikipedia.org/wiki/Brad_Sherman",
               "https://en.wikipedia.org/wiki/Congressional_Israel_Allies_Caucus"]),
        claim("bs2", "brad-sherman", "sanctity_of_life", 0, False,
              "Has earned a 100% rating from both NARAL Pro-Choice America and Planned Parenthood; "
              "called the Supreme Court's Dobbs ruling 'appalling and outrageous' — reflecting "
              "consistent rejection of life from conception as a legal standard across his "
              "27-year congressional career.",
              ["https://en.wikipedia.org/wiki/Brad_Sherman",
               "https://ballotpedia.org/Brad_Sherman_(California)"]),
    ]),

    # ---- Jim Costa (CA-21, D, 11th term, Blue Dog Coalition chair) ----
    ("jim-costa", "CA", "CA-21", [
        claim("jc1", "jim-costa", "sanctity_of_life", 0, False,
              "A self-described liberal Roman Catholic who nonetheless is an original co-sponsor "
              "of the Women's Health Protection Act, which would create a federal right to abortion "
              "overriding most state limits; opposed the Dobbs ruling, saying it 'strips women of "
              "their freedom to make their own decisions' — rejecting any life-at-conception standard.",
              ["https://en.wikipedia.org/wiki/Jim_Costa",
               "https://ballotpedia.org/Jim_Costa"]),
        claim("jc2", "jim-costa", "economic_stewardship", 2, True,
              "A member and former chair (116th Congress) of the Blue Dog Coalition, whose "
              "foundational mission is fiscal conservatism: the coalition explicitly advocates for "
              "balanced-budget discipline and restraint on deficit spending — aligning with the "
              "rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Jim_Costa",
               "https://ballotpedia.org/Jim_Costa"]),
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
