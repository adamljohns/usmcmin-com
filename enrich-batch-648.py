#!/usr/bin/env python3
"""Enrichment batch 648: hand-curated claims for 2 Mississippi State Senators.

Senators: Rita Potts Parks (SD-4), Daniel Sparks (SD-5).
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
    # --- Rita Potts Parks (MS SD-4, State Senator — Alcorn/Tippah counties, in office since Jan 2012) ---
    ("rita-potts-parks", "MS", "State Senator", [
        claim("rpp1", "rita-potts-parks", "sanctity_of_life", 0, True,
              "Parks was a named co-sponsor of SB 2116 (2019), the Mississippi Fetal Heartbeat Protection Act, which prohibited abortion of any unborn individual with a detectable heartbeat except to prevent the mother's death or serious bodily impairment; Parks is listed by name in the official bill introduction text alongside Senators Hill, Fillingane, Watson, McDaniel, and others; the Senate passed it 34-14 on February 13, 2019, and Gov. Bryant signed it March 21, 2019.",
              ["https://billstatus.ls.state.ms.us/documents/2019/html/SB/2100-2199/SB2116IN.htm",
               "https://wreg.com/news/mississippi-senate-oks-ban-on-abortion-after-fetal-heartbeat/"]),
        claim("rpp2", "rita-potts-parks", "biblical_marriage", 2, True,
              "Parks was formally recognized as a named co-author of SB 2536 (2021), the Mississippi Fairness Act, which became the first such law in the nation when signed on March 11, 2021; the bill requires all public schools and NCAA/NAIA/MHSAA member institutions to designate athletic teams by biological sex, blocking male-born athletes who identify as female from women's sports; the Senate passed it 34-9 on February 11, 2021.",
              ["https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/",
               "https://billstatus.ls.state.ms.us/documents/2021/html/SB/2500-2599/SB2536SG.htm"]),
        claim("rpp3", "rita-potts-parks", "family_child_sovereignty", 0, True,
              "Parks voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning puberty blockers, cross-sex hormones, and gender transition surgeries for minors under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, with all 15 no-votes coming from Democrats, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
    ]),

    # --- Daniel Sparks (MS SD-5, State Senator — Itawamba/Prentiss/Tishomingo counties, in office since Jan 2020) ---
    ("daniel-sparks", "MS", "State Senator", [
        claim("ds1", "daniel-sparks", "sanctity_of_life", 0, True,
              "Sparks served as one of six Senate conference committee members who drafted the final language of HB 1613 (2026), which amends Mississippi drug trafficking law to classify distribution of abortion-inducing drugs — including mifepristone and misoprostol — as a felony carrying up to 10 years in prison; Sparks is directly and repeatedly quoted stating: 'The state of Mississippi has been pretty clear about their pro-life position. If people are circumventing that through the mail or other mechanisms, then we're trying to be consistent with what the law is'; the House passed it 77-39 and the Senate 37-15; Gov. Reeves signed it April 8, 2026.",
              ["https://mississippitoday.org/2026/04/01/mississippi-abortion-medication/",
               "https://www.mississippifreepress.org/bill-criminalizing-mail-order-abortion-pills-as-drug-trafficking-heads-to-mississippi-governors-desk/"]),
        claim("ds2", "daniel-sparks", "biblical_marriage", 2, True,
              "Sparks was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, which mandates that public schools and universities designate athletic teams by biological sex, explicitly rejecting transgender ideology in women's sports — co-authoring in his second year in office; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://billstatus.ls.state.ms.us/documents/2021/html/SB/2500-2599/SB2536SG.htm"]),
        claim("ds3", "daniel-sparks", "election_integrity", 0, True,
              "Sparks voted with the Republican caucus for SB 2588 (2026), the SHIELD Act, which requires annual citizenship verification of all registered voters against the federal SAVE database and mandates county registrars to run applicants through SAVE before registering them; the Senate passed it 33-17 on February 5, 2026, on a strict party-line vote, and Gov. Reeves signed it April 3, 2026, effective July 1, 2026.",
              ["https://magnoliatribune.com/2026/04/01/governor-signs-shield-act-into-law-seeking-to-further-safeguard-mississippi-elections/",
               "https://www.mississippifreepress.org/mississippi-governor-signs-shield-act-into-law-enacting-voter-citizenship-checks/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
