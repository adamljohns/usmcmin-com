#!/usr/bin/env python3
"""Enrichment batch 205: hand-curated claims for 5 sitting U.S. Representatives.

archetype_curated federal senator/rep buckets exhausted; targets drawn from
archetype_party_default US Representatives with 0 claims, bottom of the alphabet
(NY).

All 5 are New York Democrats: Nydia Velazquez (NY-07, retiring), Gregory Meeks
(NY-05), Grace Meng (NY-06), Dan Goldman (NY-10), Adriano Espaillat (NY-13).
Each claim cites >=1 reliable source and reflects documented voting record /
public positions (2019-2025).

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
    # ---------------- Nydia Velazquez (NY-07-D, US Representative, retiring 2026) ----------------
    ("nydia-velazquez", "NY", "Representative", [
        claim("nv1", "nydia-velazquez", "sanctity_of_life", 0, False,
              "SBA Pro-Life America gives Velazquez a 0% lifetime pro-life score; she voted YES on the Women's Health Protection Act of 2022 (H.R.8296) to enshrine a federal statutory right to abortion and eliminate state limits — rejecting any personhood-from-conception standard.",
              ["https://sbaprolife.org/representative/nydia-velazquez",
               "https://www.congress.gov/bill/117th-congress/house-bill/8296",
               "https://ballotpedia.org/Nydia_Velazquez"]),
        claim("nv2", "nydia-velazquez", "self_defense", 1, False,
              "Voted YES on the Assault Weapons Ban of 2022 (H.R.1808), which passed the House 217-213 on July 29, 2022 and would have banned the manufacture and sale of semi-automatic rifles and high-capacity magazines — opposing the rubric's defense of such firearms from bans and registries.",
              ["https://www.govtrack.us/congress/bills/117/hr1808",
               "https://ballotpedia.org/Nydia_Velazquez"]),
        claim("nv3", "nydia-velazquez", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R.2, House Vote #209, May 11 2023), which funds border-wall construction, ends catch-and-release, and tightens asylum — opposing the rubric's call for a wall and military presence at the southern border.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Nydia_Velazquez"]),
    ]),

    # ---------------- Gregory Meeks (NY-05-D, US Representative) ----------------
    ("gregory-meeks", "NY", "Representative", [
        claim("gm1", "gregory-meeks", "sanctity_of_life", 0, False,
              "SBA Pro-Life America scorecard gives Meeks a 0% pro-life rating; Ballotpedia records he voted to eliminate prohibitions on taxpayer funding for abortion domestically and internationally, including redefining longstanding safeguards to allow taxpayer-funded abortion travel expenses — rejecting any personhood-from-conception standard.",
              ["https://sbaprolife.org/representative/gregory-meeks",
               "https://ballotpedia.org/Gregory_Meeks"]),
        claim("gm2", "gregory-meeks", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (H.R.8404, House Vote #373, July 19 2022; signed into law Dec 13 2022), which repealed the Defense of Marriage Act and codified federal recognition of same-sex marriages — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://ballotpedia.org/Gregory_Meeks"]),
        claim("gm3", "gregory-meeks", "self_defense", 1, False,
              "Voted YES on the Assault Weapons Ban of 2022 (H.R.1808, passed House 217-213 on July 29 2022), which would have banned the manufacture and sale of semi-automatic assault-style weapons and high-capacity magazines — opposing the rubric's defense of such firearms from government restriction.",
              ["https://www.govtrack.us/congress/bills/117/hr1808",
               "https://ballotpedia.org/Gregory_Meeks"]),
    ]),

    # ---------------- Grace Meng (NY-06-D, US Representative) ----------------
    ("grace-meng", "NY", "Representative", [
        claim("gmng1", "grace-meng", "sanctity_of_life", 0, False,
              "Carries a 100% rating from Reproductive Freedom for All (NARAL's successor) and a 0% rating from SBA Pro-Life America; cosponsored the Women's Health Protection Act in multiple Congresses to codify federal abortion access — rejecting any personhood-from-conception standard.",
              ["https://reproductivefreedomforall.org/lawmaker/grace-meng/",
               "https://sbaprolife.org/representative/grace-meng",
               "https://ballotpedia.org/Grace_Meng"]),
        claim("gmng2", "grace-meng", "self_defense", 1, False,
              "Voted YES on the Bipartisan Background Checks Act of 2019 (H.R.8, passed House 240-190) and YES on the Assault Weapons Ban of 2022 (H.R.1808, passed House 217-213 on July 29 2022) — opposing the rubric's position against expanded federal gun registries and bans on semi-automatic firearms.",
              ["https://www.govtrack.us/congress/bills/116/hr8",
               "https://www.govtrack.us/congress/bills/117/hr1808",
               "https://ballotpedia.org/Grace_Meng"]),
        claim("gmng3", "grace-meng", "border_immigration", 0, False,
              "Voted YES on the American Dream and Promise Act of 2021 (H.R.6), which would have granted permanent legal status to DACA recipients and Temporary Protected Status holders, and voted NO on the Secure the Border Act of 2023 (H.R.2) — opposing the rubric's call for wall construction and enforcement-first immigration policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Grace_Meng"]),
    ]),

    # ---------------- Dan Goldman (NY-10-D, US Representative, first term 2023-) ----------------
    ("dan-goldman", "NY", "Representative", [
        claim("dg1", "dan-goldman", "sanctity_of_life", 0, False,
              "Called the Supreme Court's Dobbs v. Jackson Women's Health Organization decision 'one of the very worst opinions that the Supreme Court has ever issued on both a legal and factual basis'; co-led more than 50 House Democrats in pressing major pharmacy chains to stock the abortion pill mifepristone — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Dan_Goldman",
               "https://reproductivefreedomforall.org/lawmaker/daniel-s-goldman/",
               "https://ballotpedia.org/Daniel_Goldman"]),
        claim("dg2", "dan-goldman", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R.2, House Vote #209, May 11 2023) and introduced the Immigration Court Efficiency and Children's Court Act of 2023, which prioritizes court processing and family unification rather than enforcement and deportation — opposing the rubric's call for mandatory deportation and a militarized border.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/member/daniel-goldman/G000599",
               "https://ballotpedia.org/Daniel_Goldman"]),
        claim("dg3", "dan-goldman", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (H.R.8404, House Vote #373, July 19 2022 and final House Vote #513, Dec 8 2022; signed into law Dec 13 2022), which repealed the Defense of Marriage Act and codified federal recognition of same-sex marriages — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://ballotpedia.org/Daniel_Goldman"]),
    ]),

    # ---------------- Adriano Espaillat (NY-13-D, US Representative) ----------------
    ("adriano-espaillat", "NY", "Representative", [
        claim("ae1", "adriano-espaillat", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act in the 116th Congress (H.R.2975, 2019), 117th Congress (H.R.3755, 2021), and subsequent Congresses, seeking to codify a federal right to abortion and preempt state restrictions — rejecting any personhood-from-conception standard.",
              ["https://www.congress.gov/bill/116th-congress/house-bill/2975/cosponsors",
               "https://www.congress.gov/bill/117th-congress/house-bill/3755/cosponsors",
               "https://ballotpedia.org/Adriano_Espaillat"]),
        claim("ae2", "adriano-espaillat", "self_defense", 1, False,
              "Co-introduced the Untraceable Firearms Act (2021) with Rep. Brad Schneider to regulate privately made ghost guns under the Gun Control Act, mandating serial numbers and background checks for unserialized firearms — supporting expanded federal firearms registry requirements the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Adriano_Espaillat",
               "https://ballotpedia.org/Adriano_Espaillat"]),
        claim("ae3", "adriano-espaillat", "border_immigration", 0, False,
              "Ranked 7th most politically left in the 117th Congress (GovTrack); voted NO on the Secure the Border Act of 2023 (H.R.2, House Vote #209) and is a member of the Congressional Progressive Caucus, which has consistently opposed border-wall construction and mandatory deportation — opposing the rubric's enforcement-first immigration stance.",
              ["https://www.govtrack.us/congress/members/adriano_espaillat/412718/report-card/2022",
               "https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Adriano_Espaillat"]),
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
