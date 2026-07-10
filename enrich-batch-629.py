#!/usr/bin/env python3
"""Enrichment batch 629: hand-curated claims for 2 Pennsylvania State Senators.

Senators: Devlin J. Robinson (SD-37), Daniel Laughlin (SD-49).
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
    # --- Devlin J. Robinson (PA SD-37, State Senator) ---
    ("devlin-j-robinson", "PA", "State Senator", [
        claim("djr1", "devlin-j-robinson", "self_defense", 0, True,
              "Robinson co-sponsored both SB 565 (2021-2022) and SB 357 (2025-2026), Pennsylvania constitutional carry bills that would eliminate the permit requirement for law-abiding citizens to carry a concealed firearm.",
              ["https://www.palegis.us/legislation/bills/2025/sb357",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565"]),
        claim("djr2", "devlin-j-robinson", "election_integrity", 0, True,
              "Robinson co-sponsored SB 1 (2023-2024), a joint resolution proposing a constitutional amendment to require valid photo identification at every Pennsylvania election; the bill passed the State Senate 28-20 on January 11, 2023.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://legiscan.com/PA/bill/SB1/2023"]),
    ]),

    # --- Daniel Laughlin (PA SD-49, State Senator) ---
    ("daniel-laughlin", "PA", "State Senator", [
        claim("dl1", "daniel-laughlin", "election_integrity", 0, True,
              "Laughlin was the prime sponsor of Pennsylvania SB 1 (2023-2024), a joint resolution proposing a constitutional amendment requiring voters to present valid identification at the polls; the PA Senate passed it 28-20 on January 11, 2023.",
              ["http://www.politicspa.com/laughlin-introduces-voter-id-legislation-to-amend-pa-constitution/",
               "https://www.senatorlaughlin.com/2023/01/11/senate-approves-constitutional-amendments-for-voter-id-sexual-abuse-victims-regulatory-reform/"]),
        claim("dl2", "daniel-laughlin", "sanctity_of_life", 0, False,
              "Laughlin voted against SB 106 (July 8, 2022), a constitutional amendment declaring no Pennsylvania constitutional right to abortion, stating 'I want to leave our law as it stands — no more or less restrictive' — one of only two Senate Republicans to oppose it in the 28-22 vote.",
              ["https://www.spotlightpa.org/news/2022/07/pa-abortion-restrictions-constitutional-amendment-voter-id/",
               "https://www.inquirer.com/politics/pennsylvania/pa-senate-constitutional-amendments-abortion-elections-voting-20220708.html"]),
        claim("dl3", "daniel-laughlin", "self_defense", 0, True,
              "Laughlin circulated PA Senate Co-Sponsorship Memo 39043 (2023-2024) announcing plans to introduce constitutional carry legislation allowing law-abiding citizens to carry concealed without a government permit, with an optional License to Carry for interstate reciprocity.",
              ["https://www.palegis.us/senate/co-sponsorship/memo?memoID=39043",
               "https://www.alliednews.com/cnhi_network/constitutional-carry-bill-advances-in-pa-senate-on-party-line-vote/article_53d4546f-5ea3-5e5a-b81f-2b2612f2763b.html"]),
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
