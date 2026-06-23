#!/usr/bin/env python3
"""Enrichment batch 392: hand-curated claims for 5 Virginia state legislators.

Targets: VA state legislators with 0 evidence claims.
Mix (5 D): Dave Marsden (VA SD-35), Don Scott (VA HOD-88/Speaker),
Dan Helmer (VA HOD-10), Irene Shin (VA HOD-8), Gretchen Bulova (VA HOD-11).

Key source: HJR1 (2025 Regular Session) — Virginia Right to Reproductive
Freedom constitutional amendment, passed House 51-48 (Jan 14 2025) and
Senate 21-19 (Jan 21 2025) on party-line votes.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace).
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
    # ---------------- Dave Marsden (VA-D, State Senate District 35) ----------------
    ("dave-marsden", "VA", "District 35", [
        claim("dm1", "dave-marsden", "sanctity_of_life", 0, False,
              "Co-sponsored and voted for SJR 247, the Virginia Right to Reproductive Freedom constitutional amendment (Senate 21-19, January 21, 2025), which would enshrine a right to abortion in the Virginia constitution — directly rejecting any personhood-from-conception standard. All 21 Senate Democrats were co-patrons of the resolution.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("dm2", "dave-marsden", "self_defense", 1, False,
              "Sponsored and passed SB 496 (2026), which requires handguns left in unattended vehicles to be stored in a locked container — signed into law as Chapter 561 of the 2026 Acts of Assembly despite opposition from the NRA, VCDL, and Gun Owners of America, who lobbied against it as a restriction on Second Amendment rights.",
              ["https://lis.virginia.gov/bill-details/20261/SB496",
               "https://legiscan.com/VA/text/SB496/id/3332228"]),
    ]),

    # ---------------- Don Scott (VA-D, Speaker, House of Delegates District 88) ----------------
    ("don-scott", "VA", "District 88", [
        claim("ds1", "don-scott", "sanctity_of_life", 0, False,
              "As Speaker of the Virginia House of Delegates, presided over and organized passage of HJR 1 (51-48, January 14, 2025), the Right to Reproductive Freedom constitutional amendment — placing abortion access in the Virginia constitution and directly opposing any recognition of the unborn from conception.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("ds2", "don-scott", "self_defense", 1, False,
              "Voted for HB 1607 (2025), the Virginia assault-firearms and magazine-capacity ban (House 50-48, February 4, 2025), which would have criminalized the sale and transfer of assault rifles and banned magazines over 10 rounds — directly opposing unrestricted Second Amendment rights.",
              ["https://lis.virginia.gov/bill-details/20251/HB1607",
               "https://legiscan.com/VA/votes/HB1607/2025"]),
    ]),

    # ---------------- Dan Helmer (VA-D, House of Delegates District 10) ----------------
    ("dan-helmer", "VA", "District 10", [
        claim("dh1", "dan-helmer", "sanctity_of_life", 0, False,
              "Voted for HJR 1 (51-48, January 14, 2025), the Virginia Right to Reproductive Freedom constitutional amendment, and is a named supporter of the 2026 ballot referendum — rejecting any protection of the unborn from conception.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("dh2", "dan-helmer", "self_defense", 1, False,
              "Was the chief patron (primary sponsor) of HB 1607 (2025), Virginia's assault-firearms and magazine-capacity ban (House 50-48, February 4, 2025), which would have criminalized the import, sale, and transfer of assault rifles and banned magazines over 10 rounds — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://lis.virginia.gov/bill-details/20251/HB1607",
               "https://legiscan.com/VA/votes/HB1607/2025"]),
    ]),

    # ---------------- Irene Shin (VA-D, House of Delegates District 8) ----------------
    ("irene-shin", "VA", "District 8", [
        claim("is1", "irene-shin", "sanctity_of_life", 0, False,
              "Voted against HB 2183 (Born Alive Infant Protection Act), which would have required the same standard of medical care for infants born alive after a failed abortion as any other live-born infant. The bill passed 52-47 (February 7, 2025) on a party-line vote; all Democrats including Shin voted no — rejecting protections for the born alive and any personhood standard.",
              ["https://lis.virginia.gov/bill-details/20251/HB2183",
               "https://legiscan.com/VA/research/HB2183/2025"]),
        claim("is2", "irene-shin", "biblical_marriage", 0, False,
              "Voted for HJ 9 (58-35, January 14, 2025), the Virginia constitutional amendment to repeal the state's same-sex marriage ban and enshrine marriage equality for two adults regardless of sex or gender — rejecting the one-man-one-woman definition of marriage the rubric defends.",
              ["https://lis.virginia.gov/bill-details/20251/HJ9",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)"]),
    ]),

    # ---------------- Gretchen Bulova (VA-D, House of Delegates District 11) ----------------
    ("gretchen-bulova", "VA", "District 11", [
        claim("gb1", "gretchen-bulova", "sanctity_of_life", 0, False,
              "Voted against HB 2183 (Born Alive Infant Protection Act), which would have required equal medical care for infants born alive after a failed abortion. The bill passed 52-47 (February 7, 2025) on a strict party-line vote; all House Democrats including Bulova voted no — rejecting any born-alive protection and personhood-from-conception standard.",
              ["https://lis.virginia.gov/bill-details/20251/HB2183",
               "https://legiscan.com/VA/research/HB2183/2025"]),
        claim("gb2", "gretchen-bulova", "self_defense", 1, False,
              "Voted for HB 1607 (2025), the Virginia assault-firearms and magazine-capacity ban (House 50-48, February 4, 2025), which would have criminalized the sale and transfer of assault rifles and restricted magazines to 10 rounds — directly opposing unrestricted Second Amendment rights.",
              ["https://lis.virginia.gov/bill-details/20251/HB1607",
               "https://legiscan.com/VA/votes/HB1607/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
