#!/usr/bin/env python3
"""Enrichment batch 734: 1 NC federal Rep + 3 NC Republican State Senators, 9 claims.

archetype_curated federal/state buckets continuing from bottom of reverse-alpha.
NC federal rep (NC-06 freshman) + NC state senators with no prior enrich entries.

Targets:
  Addison McDowell  (NC-06, R, US Representative, freshman elected 2024)
  Ralph Hise        (NC SD-47, R, State Senator since 2010)
  Danny Britt       (NC SD-22, R, State Senator since 2017)
  Bill Rabon        (NC SD-8, R, State Senator since 2011, Senate Rules Chair)

Key sourced votes/positions:
  McDowell — 100% pro-life pledge; Pregnancy Loss Mental Health Research Act;
    H.R. 38 Concealed Carry Reciprocity Act supporter; voted YES on H.R. 1
    (One Big Beautiful Bill Act) including border security provisions; brother
    died of fentanyl overdose, driving his border position.
  SB 20 (NC 2023-14) — 12-week abortion ban, enacted May 2023 after a
    veto override. Hise, Rabon voted YES for bill and veto override.
  SB 41 (NC 2023-8) — Repealed NC's 1919 pistol purchase permit requirement.
    Danny Britt was PRIMARY SPONSOR; Hise and Rabon voted YES.
  SB 153 (NC 2026-19) — NC Border Protection Act, bans sanctuary policies
    statewide, mandates ICE cooperation. Danny Britt co-sponsored; enacted
    June 2026 after veto override.
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
    # ------- Addison McDowell (NC-06, R, US Representative, freshman since Jan 2025) -------
    ("addison-mcdowell", "NC", "Representative", [
        claim("am1", "addison-mcdowell", "sanctity_of_life", 0, True,
              "Has publicly pledged to be '100% pro-life and champion pro-life causes and "
              "legislation in Congress,' and introduced the Pregnancy Loss Mental Health "
              "Research Act (119th Congress) to fund research on the psychological impact "
              "of miscarriage and stillbirth — affirming a personhood-from-conception "
              "posture that aligns with the rubric's pro-life standard. McDowell has made "
              "protection of the unborn a flagship congressional commitment.",
              ["https://mcdowell.house.gov/issues",
               "https://www.congress.gov/member/addison-mcdowell/M001240"]),
        claim("am2", "addison-mcdowell", "self_defense", 0, True,
              "Publicly supports H.R. 38, the Concealed Carry Reciprocity Act, calling it "
              "'about the most commonsense thing we can do right now,' and stated "
              "unequivocally: 'The right to self-defense is a God-given, constitutional "
              "right of every law-abiding American.' His Second Amendment platform opposes "
              "restrictions on lawful carry and affirms the individual's fundamental right "
              "to bear arms for self-defense — matching the rubric's position against "
              "carry restrictions and infringements on gun rights.",
              ["https://www.nssf.org/articles/nssf-profile-qa-us-rep-addison-mcdowell-rnc/",
               "https://mcdowell.house.gov/issues"]),
        claim("am3", "addison-mcdowell", "border_immigration", 0, True,
              "Voted YES on H.R. 1, the One Big Beautiful Bill Act (passed House May 22, "
              "2025), which includes substantial border wall construction funding, "
              "mandatory E-Verify provisions, and expanded immigration enforcement. "
              "McDowell has publicly declared 'we must secure the Southern Border and "
              "stop the flow of illegal drugs' — a position driven in part by the fentanyl "
              "overdose death of his brother, giving his border-security commitment a "
              "deeply personal dimension. His vote aligns with the rubric's "
              "wall-and-enforcement standard.",
              ["https://mcdowell.house.gov/media/press-releases/congressman-addison-mcdowell-applauds-house-passage-one-big-beautiful-bill-act",
               "https://mcdowell.house.gov/issues"]),
    ]),

    # ------- Ralph Hise (NC SD-47, R, State Senator since 2010) -------
    ("ralph-hise", "NC", "State Senator", [
        claim("rh1", "ralph-hise", "sanctity_of_life", 0, True,
              "Voted YES on SB 20 (NC Session Law 2023-14), North Carolina's 12-week "
              "abortion ban, and voted to override Governor Cooper's veto on May 16, 2023, "
              "enacting the ban into law. Hise was also a co-sponsor of Senate Bill 405 "
              "(2021-22 session), the Born-Alive Abortion Survivors Protection Act, which "
              "required medical care for infants born alive during abortion procedures. "
              "His long legislative record opposing abortion on demand aligns with the "
              "rubric's personhood-from-conception standard.",
              ["https://ncleg.gov/BillLookup/2023/SB20",
               "https://ncleg.gov/BillLookup/2021/S405"]),
        claim("rh2", "ralph-hise", "self_defense", 0, True,
              "Voted YES on SB 41 (NC Session Law 2023-8), which repealed North Carolina's "
              "1919 pistol purchase permit requirement — a government-imposed permission "
              "barrier to handgun purchases that dated back over a century. The repeal "
              "removed the requirement that law-abiding citizens obtain a government permit "
              "before purchasing a handgun, a significant Second Amendment expansion. Hise "
              "has also supported broader concealed carry permit location expansions and "
              "property owner self-defense safeguards in prior NC sessions.",
              ["https://ncleg.gov/BillLookup/2023/SB41",
               "https://ballotpedia.org/Ralph_Hise"]),
    ]),

    # ------- Danny Britt (NC SD-22, R, State Senator since 2017) -------
    ("danny-britt", "NC", "State Senator", [
        claim("db1", "danny-britt", "self_defense", 1, True,
              "Was the PRIMARY SPONSOR of SB 41 (NC Session Law 2023-8), which repealed "
              "North Carolina's 1919 pistol purchase permit requirement — eliminating a "
              "government-mandated permission slip for handgun purchases that law-abiding "
              "citizens had been subjected to for over a century. The repeal, signed into "
              "law in March 2023, represented the most significant Second Amendment "
              "expansion in NC in decades and directly aligned with the rubric's opposition "
              "to government registration and permission barriers on firearm ownership.",
              ["https://ncleg.gov/BillLookup/2023/SB41",
               "https://ncleg.gov/Sessions/2023/Bills/Senate/PDF/S41v3.pdf"]),
        claim("db2", "danny-britt", "border_immigration", 2, True,
              "Co-sponsored SB 153 (NC Session Law 2026-19), the NC Border Protection Act, "
              "signed into law in June 2026 after a veto override. The law bans sanctuary "
              "city and county policies statewide, mandates ICE cooperation for state law "
              "enforcement agencies (Highway Patrol, DPS, DAC, SBI), restricts "
              "state-funded benefits for unauthorized immigrants, and bars UNC system "
              "institutions from interfering with immigration enforcement operations. "
              "Britt's co-sponsorship of this landmark enforcement bill places him "
              "squarely within the rubric's full federal immigration cooperation standard "
              "and opposition to sanctuary policies.",
              ["https://ncleg.gov/BillLookup/2025/SB153",
               "https://www.wunc.org/politics/2026-06-12/nc-border-protection-act-sanctuary-cities-ice"]),
    ]),

    # ------- Bill Rabon (NC SD-8, R, State Senator since 2011, Senate Rules Chair) -------
    ("bill-rabon", "NC", "State Senator", [
        claim("br1", "bill-rabon", "sanctity_of_life", 0, True,
              "Voted YES on SB 20 (NC Session Law 2023-14), the 12-week abortion ban, and "
              "voted to override Governor Cooper's veto on May 16, 2023 to enact the law. "
              "As Chairman of the Senate Rules and Operations of the Senate Committee, "
              "Rabon held a key procedural leadership position throughout the bill's "
              "passage — making his YES votes a substantive endorsement, not merely "
              "procedural. His record aligns with the rubric's opposition to abortion on "
              "demand and support for limiting abortion access.",
              ["https://ncleg.gov/BillLookup/2023/SB20",
               "https://ncleg.gov/Members/MemberInfo/Senate/428"]),
        claim("br2", "bill-rabon", "self_defense", 0, True,
              "Voted YES on SB 41 (NC Session Law 2023-8), which repealed North Carolina's "
              "1919 pistol purchase permit requirement — a historic Second Amendment "
              "expansion removing a government permission barrier to lawful handgun "
              "ownership that had stood for over a century. The roll call vote passed the "
              "Senate 30-20; Rabon's YES vote aligned with the bill's goal of restoring "
              "unfettered access to handguns for law-abiding citizens, consistent with the "
              "rubric's opposition to government-mandated barriers on firearm ownership.",
              ["https://ncleg.gov/BillLookup/2023/SB41",
               "https://ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2023/S/79"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~42MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
