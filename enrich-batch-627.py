#!/usr/bin/env python3
"""Enrichment batch 627: hand-curated claims for 2 Pennsylvania State Senators.

Senators: Jarrett Coleman (SD-16), Lynda Schlegel Culver (SD-27).
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
    # --- Jarrett Coleman (PA SD-16, State Senator) ---
    ("jarrett-coleman", "PA", "State Senator", [
        claim("jc1", "jarrett-coleman", "election_integrity", 0, True,
              "Coleman co-sponsored PA SB 1 (2023-2024), a joint resolution for a constitutional amendment requiring voters to present valid identification at every election; it passed the PA Senate 28-20 on January 11, 2023.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://legiscan.com/PA/bill/SB1/2023"]),
        claim("jc2", "jarrett-coleman", "election_integrity", 3, True,
              "Coleman introduced SB 130 (2023 session), a proposed constitutional amendment mandating the Pennsylvania Office of Auditor General conduct routine post-election audits of results, citing lack of public confidence in the electoral system.",
              ["https://www.meadvilletribune.com/news/pa-senate-committee-moves-forward-on-constitutional-amendments-on-voter-id-election-audits-regulatory-reform/article_593df8b8-9083-11ed-ada2-9f7e1770b66a.html",
               "https://www.pasenategop.com/news/coleman-appointed-to-pa-election-law-advisory-board/"]),
        claim("jc3", "jarrett-coleman", "self_defense", 0, True,
              "Coleman co-sponsored SB 357 (2025-2026), Pennsylvania's constitutional carry bill allowing law-abiding adults to carry concealed without a government permit, and scored 100% on the 2022 Gun Owners of America candidate survey, earning their endorsement.",
              ["https://pennsylvania.gunowners.org/goa-endorses-jarrett-coleman-for-state-senate/",
               "https://www.palegis.us/legislation/bills/2025/sb357"]),
    ]),

    # --- Lynda Schlegel Culver (PA SD-27, State Senator) ---
    ("lynda-schlegel-culver", "PA", "State Senator", [
        claim("lsc1", "lynda-schlegel-culver", "sanctity_of_life", 0, True,
              "As a PA House member, Culver voted yes on SB 106 (July 8, 2022), a joint resolution proposing a constitutional amendment declaring the PA Constitution provides no right to abortion and that state policy is to protect every unborn child from conception to birth; the bill passed the House 107-92.",
              ["https://legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=106",
               "https://ballotpedia.org/Pennsylvania_No_State_Constitutional_Right_to_Abortion_Amendment_(2024)"]),
        claim("lsc2", "lynda-schlegel-culver", "family_child_sovereignty", 0, True,
              "As a PA Senator, Culver voted for SB 7 (October 24, 2023), requiring schools to notify parents and obtain parental consent before students access instructional materials or books containing sexually explicit content; the bill passed 29-21 with all 28 Republican senators voting yes.",
              ["https://www.palegis.us/legislation/bills/2023/sb7",
               "https://www.pasenategop.com/news/senate-passes-bill-to-settle-issue-of-sexually-explicit-content-in-school/"]),
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
