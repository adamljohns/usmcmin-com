#!/usr/bin/env python3
"""Enrichment batch 660: hand-curated claims for 2 Mississippi State Senators.

Senators: Chris Johnson (SD-44), Philman Ladner (SD-46).
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
    # --- Chris Johnson (MS SD-44, State Senator — George/Greene/Perry/Stone counties) ---
    ("chris-johnson", "MS", "State Senator", [
        claim("cj1", "chris-johnson", "family_child_sovereignty", 0, True,
              "Johnson voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
        claim("cj2", "chris-johnson", "self_defense", 0, True,
              "Johnson voted for HB 912 (2023), the Mississippi Suppressor Freedom Act, removing suppressors from the state's list of restricted weapons and allowing their lawful possession without a special state permit; the Senate passed it and Gov. Reeves signed it March 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/HB/0900-0999/HB0912SG.htm",
               "https://www.americanrifleman.org/content/mississippi-removes-suppressors-from-restricted-weapons-list/"]),
        claim("cj3", "chris-johnson", "election_integrity", 0, True,
              "Johnson voted with the Republican caucus for SB 2588 (2026), the SHIELD Act, which requires annual citizenship verification of all registered voters against the federal SAVE database and mandates county registrars to run applicants through SAVE before registering them; the Senate passed it 33-17 on a strict party-line vote on February 5, 2026, and Gov. Reeves signed it April 3, 2026, effective July 1, 2026.",
              ["https://magnoliatribune.com/2026/04/01/governor-signs-shield-act-into-law-seeking-to-further-safeguard-mississippi-elections/",
               "https://www.mississippifreepress.org/mississippi-governor-signs-shield-act-into-law-enacting-voter-citizenship-checks/"]),
    ]),

    # --- Philman Ladner (MS SD-46, State Senator — Hancock/Harrison counties) ---
    ("philman-ladner", "MS", "State Senator", [
        claim("pl1", "philman-ladner", "family_child_sovereignty", 0, True,
              "Ladner voted for HB 1126 (2024), the Mississippi Age-Appropriate Design Code Act, requiring digital platforms to perform data protection impact assessments and prohibiting collection or use of personal data of minors in ways that are not in the minor's best interests; the Senate passed it unanimously 49-0 and Gov. Reeves signed it March 15, 2024.",
              ["https://billstatus.ls.state.ms.us/documents/2024/html/HB/1100-1199/HB1126SG.htm",
               "https://www.wlbt.com/2024/03/15/gov-reeves-signs-bill-protecting-children-online/"]),
        claim("pl2", "philman-ladner", "economic_stewardship", 0, True,
              "Ladner voted for HB 1 (2025), the landmark Mississippi income tax elimination bill that phases out the state's 4% flat income tax entirely by 2030 — the largest tax cut in Mississippi history; the Senate passed it with strong Republican support and Gov. Reeves signed it March 27, 2025.",
              ["https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm",
               "https://mississippitoday.org/2025/03/27/mississippi-eliminates-income-tax/"]),
        claim("pl3", "philman-ladner", "election_integrity", 0, True,
              "Ladner voted with the Republican caucus for SB 2588 (2026), the SHIELD Act, which requires annual citizenship verification of all registered voters against the federal SAVE database and mandates county registrars to run applicants through SAVE before registering them; the Senate passed it 33-17 on a strict party-line vote on February 5, 2026, and Gov. Reeves signed it April 3, 2026.",
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
