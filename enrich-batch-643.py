#!/usr/bin/env python3
"""Enrichment batch 643: hand-curated claims for 2 Oklahoma State Senators.

Senators: George Burns (SD-5), Grant Green (SD-28).
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
    # --- George Burns (OK SD-5, State Senator — SE Oklahoma, in office since Nov 2020) ---
    ("george-burns", "OK", "State Senator", [
        claim("gb1", "george-burns", "sanctity_of_life", 0, True,
              "Burns voted YEA on SB 918 (2021), Oklahoma's abortion trigger law repealing statutes relating to abortion upon reversal of Roe v. Wade and reactivating the 1910 felony abortion statute (21 O.S. § 861) except for medical necessity; Burns' individual YEA vote is confirmed on the official Oklahoma Legislative Services Bureau roll call; the Senate passed it 38-9 on March 10, 2021, and Gov. Stitt signed it April 27, 2021.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB918_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB918/2021"]),
        claim("gb2", "george-burns", "biblical_marriage", 2, True,
              "Burns was a named co-author of SB 2 (2022), the Save Women's Sports Act, prohibiting biologically male athletes from competing on school athletic teams designated for females at any Oklahoma K-12 school or university; Burns is listed in the enrolled bill's co-author list alongside 14 other senators; the Senate passed it 37-7 on February 22, 2022, and Gov. Stitt signed it March 30, 2022.",
              ["http://webserver1.lsb.state.ok.us/cf_pdf/2021-22%20ENR/SB/SB2%20ENR.PDF",
               "https://legiscan.com/OK/bill/SB2/2022"]),
        claim("gb3", "george-burns", "christian_liberty", 0, True,
              "Burns was the prime sponsor of SB 426 (2024), the Oklahoma Sovereignty and Anti-Mandate Act, prohibiting Oklahoma state agencies, municipalities, and political subdivisions from enforcing any mandate or recommendation issued by the WHO, UN, or WEF — covering masks, vaccines, medical testing, and data collection; the Senate passed it 36-6 on May 29, 2024, and Gov. Stitt signed it June 5, 2024.",
              ["https://oksenate.gov/press-releases/burns-bill-protect-oklahomans-freedoms-passes",
               "https://oklahomavoice.com/briefs/oklahoma-governor-signs-bill-exempting-state-from-who-and-un-mandates/"]),
    ]),

    # --- Grant Green (OK SD-28, State Senator — Wellston/Lincoln County, in office since Nov 2022) ---
    ("grant-green", "OK", "State Senator", [
        claim("gg1", "grant-green", "family_child_sovereignty", 0, True,
              "Green voted YES on SB 613 (2023), the Gender Transition Prevention Act, banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — with civil enforcement and professional license revocation provisions; Green's individual YES vote is confirmed on the official Oklahoma Legislative Services Bureau roll call; the Senate passed it 40-8 on February 15, 2023, and Gov. Stitt signed it May 1, 2023.",
              ["http://webserver1.lsb.state.ok.us/cf/2023-24%20SUPPORT%20DOCUMENTS/votes/Senate/SB613_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB613/2023"]),
        claim("gg2", "grant-green", "self_defense", 0, True,
              "Green voted YEA on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma governmental entities from contracting with companies that discriminate against firearm businesses or associations; Green's individual YEA vote is confirmed on the official Oklahoma Legislature Senate vote record page; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250506/oklahoma-governor-stitt-signs-firearm-industry-non-discrimination-bill"]),
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
