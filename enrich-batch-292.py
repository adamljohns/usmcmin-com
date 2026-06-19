#!/usr/bin/env python3
"""Enrichment batch 292: hand-curated claims for 5 West Virginia state senators.

archetype_curated federal bucket exhausted; batch continues the state-senator
protocol from batch 291 (WY), now taking the next bottom-of-alphabet state: WV.
Reverse-sorted WV archetype_party_default state senators with 0 claims; first 5.

Targets: Zack Maynard (WV-R SD-7), Vince Deeds (WV-R SD-10),
T. Kevan Bartlett (WV-R SD-8), Scott Fuller (WV-R SD-5),
Rollan A. Roberts (WV-R SD-9).

Key sourced votes:
  WV SB 456 (2025 Riley Gaines Act) — defining biological sex, passed 32-1,
  signed by Gov. Morrisey March 12, 2025.
  WV HB 4106 (2026) — constitutional carry expansion to 18-20 year olds,
  Senate 31-3, signed by Gov. Morrisey April 1, 2026.
  WV HB 302 (2022 special session) — near-total abortion ban, Senate 22-7,
  signed by Gov. Justice Sept 16, 2022 (Roberts was in Senate since 2018).

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{slug}-{category}-{q_idx}-{cid}",
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
    # ---------- Zack Maynard (WV-R, State Senator SD-7, appointed Oct 30 2025) ----------
    ("zack-maynard", "WV", "State Senator", [
        claim("zm1", "zack-maynard", "self_defense", 0, True,
              "Voted AYE on WV HB 4106 (2026), expanding constitutional carry to adults ages 18-20, making permitless concealed carry universal for all legal adults in West Virginia; the Senate passed the bill 31-3 on March 14, 2026, and Governor Patrick Morrisey signed it April 1, 2026. As a WV House delegate (2016-2022), Maynard carried a 100% NRA voting rating throughout his six-year House tenure before his October 2025 Senate appointment.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "http://www.wvlegislature.gov/legisdocs/2026/RS/votes/senate/03-14-0701.pdf",
               "https://www.wvgazettemail.com/news/politics/maynard-appointed-to-wv-senate-district-for-southern-kanawha-coalfield-counties/article_0cf8f9a2-c30c-40c0-9f49-58be60dd8a62.html"]),
        claim("zm2", "zack-maynard", "sanctity_of_life", 0, True,
              "Carried a 100% voting record with West Virginians for Life — the state's principal right-to-life organization — throughout his six years serving in the West Virginia House of Delegates (2016-2022). Was appointed to the WV State Senate in October 2025 by Governor Patrick Morrisey, himself a staunch pro-life executive who has signed multiple pro-life measures into law, affirming Maynard's alignment with a life-at-conception worldview.",
              ["https://www.wvgazettemail.com/news/politics/maynard-appointed-to-wv-senate-district-for-southern-kanawha-coalfield-counties/article_0cf8f9a2-c30c-40c0-9f49-58be60dd8a62.html",
               "https://ballotpedia.org/Zack_Maynard"]),
    ]),

    # ---------- Vince Deeds (WV-R, State Senator SD-10, since Dec 1 2022) ----------
    ("vince-deeds", "WV", "State Senator", [
        claim("vd1", "vince-deeds", "biblical_marriage", 2, True,
              "Voted AYE on WV SB 456 (2025, Riley Gaines Act), which defines 'sex,' 'male,' and 'female' in West Virginia state law as biological at birth and explicitly protects single-sex spaces (restrooms, changing rooms, overnight sleeping quarters) in public schools, shelters, and correctional facilities from biological males who identify as female. The bill passed the Senate 32-1 — with only one Democrat dissenting — and was signed by Governor Morrisey on March 12, 2025.",
              ["https://blog.wvlegislature.gov/headline/2025/03/03/senate-passes-bill-defining-male-and-female",
               "https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("vd2", "vince-deeds", "self_defense", 0, True,
              "Voted AYE on WV HB 4106 (2026), extending constitutional (permitless) carry to all legal adults ages 18-20 in West Virginia — the final step to making WV's Second Amendment protections age-neutral for adults. The Senate passed the bill 31-3 on March 14, 2026; Governor Morrisey signed it April 1, 2026. Deeds, a retired WV State Police lieutenant colonel who spent 25 years in law enforcement, consistently supports robust Second Amendment rights.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "http://www.wvlegislature.gov/legisdocs/2026/RS/votes/senate/03-14-0701.pdf",
               "https://ballotpedia.org/Vince_Deeds"]),
    ]),

    # ---------- T. Kevan Bartlett (WV-R, State Senator SD-8, appointed Jan 30 2025) ----------
    ("t-kevan-bartlett", "WV", "State Senator", [
        claim("tkb1", "t-kevan-bartlett", "biblical_marriage", 2, True,
              "Voted AYE on WV SB 456 (2025, Riley Gaines Act), codifying biological sex definitions in state law and preserving single-sex spaces across public schools, domestic violence shelters, and correctional facilities; the Senate passed the bill 32-1 on March 3, 2025, and Governor Morrisey signed it March 12, 2025. Bartlett had been appointed to District 8 by Governor Morrisey on January 30, 2025, and cast this vote shortly after being sworn in.",
              ["https://blog.wvlegislature.gov/headline/2025/03/03/senate-passes-bill-defining-male-and-female",
               "https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://ballotpedia.org/T._Kevan_Bartlett"]),
        claim("tkb2", "t-kevan-bartlett", "self_defense", 0, True,
              "Voted AYE on WV HB 4106 (2026), expanding constitutional carry to adults ages 18-20, completing West Virginia's transition to full permitless carry for all adults. The Senate passed the bill 31-3 on March 14, 2026; Governor Morrisey signed it April 1, 2026.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "http://www.wvlegislature.gov/legisdocs/2026/RS/votes/senate/03-14-0701.pdf"]),
    ]),

    # ---------- Scott Fuller (WV-R, State Senator SD-5, since Dec 1 2024) ----------
    ("scott-fuller", "WV", "State Senator", [
        claim("sf1", "scott-fuller", "biblical_marriage", 2, True,
              "Voted AYE on WV SB 456 (2025, Riley Gaines Act), defining sex in state law as biological and protecting single-sex facilities in schools, shelters, and correctional facilities from intrusion by members of the opposite biological sex. The bill passed 32-1 in the WV Senate on March 3, 2025, and was signed by Governor Morrisey March 12, 2025. Fuller, a former SVU detective with the Huntington Police Department and U.S. Navy veteran, joined the Senate in December 2024.",
              ["https://blog.wvlegislature.gov/headline/2025/03/03/senate-passes-bill-defining-male-and-female",
               "https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://ballotpedia.org/Scott_Fuller_(West_Virginia)"]),
        claim("sf2", "scott-fuller", "self_defense", 0, True,
              "Voted AYE on WV HB 4106 (2026), extending constitutional carry rights to adults ages 18-20 and eliminating the age gap in West Virginia's permitless carry law; the Senate passed the bill 31-3 on March 14, 2026, and Governor Morrisey signed it April 1, 2026. Fuller's background as a decorated U.S. Navy veteran, West Virginia National Guard soldier, and career law enforcement detective informs his consistent Second Amendment advocacy.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "http://www.wvlegislature.gov/legisdocs/2026/RS/votes/senate/03-14-0701.pdf",
               "https://ballotpedia.org/Scott_Fuller_(West_Virginia)"]),
    ]),

    # ---------- Rollan A. Roberts (WV-R, State Senator SD-9, since Dec 1 2018) ----------
    ("rollan-a-roberts", "WV", "State Senator", [
        claim("rar1", "rollan-a-roberts", "sanctity_of_life", 0, True,
              "Voted AYE on WV HB 302 (September 2022 special session), West Virginia's near-total abortion ban; the Senate passed the bill 22-7 and Governor Jim Justice signed it September 16, 2022. As Senior Pastor of Victory Baptist Church (since 1988) and administrator of Victory Baptist Academy, Roberts has maintained a consistently pro-life legislative record aligned with his pastoral convictions throughout his Senate service since 2018.",
              ["https://wvpublic.org/west-virginia-legislature-outlaws-abortion/",
               "https://blog.wvlegislature.gov/headline/2022/09/13/legislature-passes-abortion-ban-adjourns-sine-die/",
               "https://ballotpedia.org/Rollan_Roberts_(West_Virginia)"]),
        claim("rar2", "rollan-a-roberts", "family_child_sovereignty", 0, True,
              "A consistent champion of parental rights and educational freedom: voted to advance West Virginia's Hope Scholarship (ESA) in the 2021 legislative session, which created education savings accounts allowing parents to direct per-pupil state funds to private schools, homeschool co-ops, and other educational providers. Prior to passage, Roberts voted three times in 2019 to advance an earlier ESA bill and three times to defeat amendments that would have gutted the program — despite WV Gazette-Mail reporting a potential conflict of interest because his own Victory Baptist Academy stood to benefit.",
              ["https://www.wvpublic.org/section/education/2021-03-10/w-va-senate-moves-forward-on-hope-scholarship-jumpstart-savings-programs",
               "https://www.wvgazettemail.com/news/education/wv-senator-voted-to-send-public-money-to-private-religious-schools-like-his/article_b10360c4-1b12-5eba-89df-8044e7387915.html",
               "https://ballotpedia.org/Rollan_Roberts_(West_Virginia)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
