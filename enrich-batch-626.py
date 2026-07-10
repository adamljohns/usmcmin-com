#!/usr/bin/env python3
"""Enrichment batch 626: hand-curated claims for 2 Pennsylvania State Senators.

Senators: Gene Yaw (SD-23), Kristin Phillips-Hill (SD-28).
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
    # --- Gene Yaw (PA SD-23, State Senator) ---
    ("gene-yaw", "PA", "State Senator", [
        claim("gy1", "gene-yaw", "self_defense", 0, True,
              "Yaw co-sponsored SB 565 (2021-2022) and SB 357 (2023-2024), both permitless-carry bills that would eliminate Pennsylvania's requirement to obtain a license to carry a concealed firearm; SB 565 passed the Senate but was vetoed by Gov. Wolf.",
              ["https://www.palegis.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565",
               "https://www.palegis.us/legislation/bills/2023/sb357"]),
        claim("gy2", "gene-yaw", "sanctity_of_life", 0, True,
              "Yaw voted in favor of SB 106 (July 8, 2022), a joint resolution to place a constitutional amendment on the ballot declaring the Pennsylvania Constitution provides no right to abortion or taxpayer-funded abortion; it passed the Senate 28-22.",
              ["https://www.inquirer.com/politics/pennsylvania/pennsylvania-abortion-law-bills-constitutional-amendment-20220708.html",
               "https://choicetracker.org/pa/people/gene-yaw/53477376"]),
        claim("gy3", "gene-yaw", "election_integrity", 3, False,
              "In August 2021, Yaw publicly opposed conducting a post-election audit of the 2020 presidential race, stating it 'will not be a productive undertaking' and warning that every audit action would be met with legal challenges — breaking with his Senate Republican caucus majority that was pushing for a forensic audit.",
              ["https://www.senatorgeneyaw.com/2021/08/19/senator-yaws-response-on-election-audit/",
               "https://talkwilliamsport.com/senator-yaws-response-on-election-audit/"]),
    ]),

    # --- Kristin Phillips-Hill (PA SD-28, State Senator) ---
    ("kristin-phillips-hill", "PA", "State Senator", [
        claim("kph1", "kristin-phillips-hill", "self_defense", 0, True,
              "Phillips-Hill co-sponsored SB 565 (2021-2022), the Pennsylvania Constitutional Carry Act eliminating the permit requirement to carry a concealed firearm statewide; it passed the Senate but was vetoed by Governor Wolf in December 2021.",
              ["https://pennsylvania.gunowners.org/goa-endorses-kristin-phillips-hill-for-state-senate/",
               "https://blog.tenthamendmentcenter.com/2021/11/pennsylvania-senate-passes-constitutional-carry-bill/"]),
        claim("kph2", "kristin-phillips-hill", "election_integrity", 3, True,
              "Phillips-Hill co-sponsored SB 982 (2021-2022), which banned third-party private funding (so-called 'Zuckerbucks') of Pennsylvania election administration; it passed the Senate 37-12 with bipartisan support and was signed into law as Act 88 of 2022.",
              ["https://senatorkristin.com/2022/04/13/senate-votes-to-ban-unsecured-ballot-drop-boxes-and-private-funding-of-election-operations/",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=982"]),
        claim("kph3", "kristin-phillips-hill", "sanctity_of_life", 0, True,
              "Phillips-Hill co-sponsored SB 106 (2021-2022), a proposed Pennsylvania constitutional amendment explicitly stating there is no state constitutional right to abortion or to taxpayer-funded abortion.",
              ["https://www.palegis.us/legislation/bills/2021/sb0106",
               "https://choicetracker.org/legislator/s28phillips-hill"]),
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
