#!/usr/bin/env python3
"""Enrichment batch 202: 3 bottom-of-alphabet candidates with documented records.

archetype_curated + evidence_federal federal buckets exhausted; working archetype_party_default
and low_evidence pools from the bottom of the alphabet (WY → MO direction).

Targets:
  Wes Climer       (SC State Senator → SC-05 R nominee, uncontested primary June 9 2026)
  Anthony Constantino (NY-21 R candidate · Trump-endorsed frontrunner · CEO/self-funded)
  Jim Ingram       (MO-06 R candidate · Army vet · balanced-budget/election-integrity platform)

MINIFIED write — see enrich-batch-4.py module docstring for rationale.
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
    # ---------------- Wes Climer (SC State Senator → SC-05 R nominee) ----------------
    ("wes-climer", "SC", "senator", [
        claim("wc1", "wes-climer", "sanctity_of_life", 0, True,
              "Co-sponsored SC S.1, the Fetal Heartbeat Protection from Abortion Act (passed Feb 18, 2021), and on the floor proposed an amendment tightening it further — allowing abortion only in cases of 'imminent risk' to the mother's life — consistent with a life-at-conception standard that rejects permissive exceptions.",
              ["https://www.scstatehouse.gov/sess124_2021-2022/bills/1.htm",
               "https://legiscan.com/SC/rollcall/S0001/id/991303"]),
        claim("wc2", "wes-climer", "self_defense", 0, True,
              "As SC Senate Judiciary Committee Chairman, championed and steered constitutional carry legislation to final passage; Gov. McMaster signed it in March 2024, making South Carolina the 29th constitutional carry state. The NRA publicly credited Climer's 'tireless efforts' as 'instrumental in advancing the right to self-defense in South Carolina,' and Climer himself declared every law-abiding South Carolinian can now carry 'without the need for a permission slip from the government.'",
              ["https://www.nraila.org/articles/20240306/south-carolina-constitutional-carry-headed-to-gov-mcmasters-desk-for-his-signature",
               "https://www.foxnews.com/politics/south-carolina-becomes-29th-state-nation-constitutional-carry-law"]),
        claim("wc3", "wes-climer", "border_immigration", 0, True,
              "Launched his SC-05 congressional campaign pledging to 'maintain a secure border' and fully back Trump's America First agenda — which includes border wall construction and military deployment — as a top legislative priority.",
              ["https://scdailygazette.com/2025/07/31/rock-hill-state-senator-launches-bid-for-scs-5th-congressional-district/",
               "https://wesclimer.com/"]),
    ]),

    # ---------------- Anthony Constantino (NY-21 R candidate, Trump-endorsed) ----------------
    ("anthony-constantino", "NY", "representative", [
        claim("ac1", "anthony-constantino", "self_defense", 0, True,
              "Pledges to 'pass Concealed Carry Reciprocity or National Constitutional Carry Legislation,' stating the Second Amendment is 'a RIGHT, not a privilege' and condemning 'anti-gun politicians' for imposing unconstitutional permit requirements — especially in New York.",
              ["https://www.vote4anthony.com/blog/makingthe-second-amendment-great-again/"]),
        claim("ac2", "anthony-constantino", "self_defense", 1, True,
              "Explicitly commits to 'repeal federal gun control' and 'slash unconstitutional regulations imposed by rogue agencies like the ATF,' directly opposing assault weapons bans, magazine restrictions, and federal registry schemes that the rubric treats as Second Amendment violations.",
              ["https://www.vote4anthony.com/blog/makingthe-second-amendment-great-again/"]),
        claim("ac3", "anthony-constantino", "border_immigration", 1, True,
              "Agrees with Trump's immigration crackdown and says he wants to 'eliminate what Republicans call illegal immigration,' supporting deportation enforcement as the primary tool; running entirely self-funded (no donors) to remain free of any interest group influence on this or any other issue.",
              ["https://www.wamc.org/news/2026-05-26/ny-21-candidate-questionnaire-republicans-smullen-constantino"]),
    ]),

    # ---------------- Jim Ingram (MO-06 R candidate) ----------------
    ("jim-ingram-mo-06", "MO", "representative", [
        claim("ji1", "jim-ingram-mo-06", "economic_stewardship", 2, True,
              "Calls for a constitutional amendment mandating a 'balanced budget except in times of war,' making fiscal discipline — not deficit spending — the default position of the federal government; frames it as one of the most urgent reforms Congress must enact.",
              ["https://ballotpedia.org/Jim_Ingram"]),
        claim("ji2", "jim-ingram-mo-06", "election_integrity", 0, True,
              "Advocates 'Uniform Election Laws' and 'States running all elections' as a constitutional change — opposing the patchwork of mass-mail-in rules, inconsistent ID requirements, and federal election administration schemes that undermine ballot integrity.",
              ["https://ballotpedia.org/Jim_Ingram"]),
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
