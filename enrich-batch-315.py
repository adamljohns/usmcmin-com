#!/usr/bin/env python3
"""Enrichment batch 315: 3rd distinct-category claims for 5 bottom-of-alphabet WY state senators.

Pipeline continues evidence_curated state-level candidates at exactly 2 claims,
reverse-sorted by state then name — WY senators at the top of that reversed list.
Picks up where batch 314 left off (Stacy Jones, Ogden Driskill, Mike Gierau,
Lynn Hutchings, Laura Taliaferro Pearson done).

Targets (WY senators, reverse-alpha by name within WY):
  John Kolb             — border_immigration[2]=True  (co-sponsored SF0124 2025,
                           immigration-enforcement bill requiring law enforcement to
                           inquire about immigration status; anti-sanctuary stance)
  Jared Olsen           — family_child_sovereignty[0]=True  (voted for HB199 2025,
                           Wyoming Freedom Scholarship Act — $7K universal school-
                           choice vouchers; parental education rights)
  James Lee Anderson    — sanctity_of_life[0]=True  (voted for HB0126 2026,
                           Human Heartbeat Act banning abortion after detectable
                           fetal heartbeat; 27-4 Senate passage, signed by Gordon)
  Gary Crum             — self_defense[0]=True  (voted aye in Senate Judiciary
                           Committee to advance HB0172 2025, gun-free zone repeal;
                           bill passed Senate 25-6 and became law)
  Evie Brennan          — family_child_sovereignty[0]=True  (voted for HB199 2025
                           in Senate Education Committee and proposed/passed amendment
                           to preserve universal school-choice program; Senate 20-11)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- John Kolb (WY, State Senator, R) ----------------
    ("john-kolb", "WY", "State Senator", [
        claim("jk1", "john-kolb", "border_immigration", 2, True,
              "Co-sponsored Wyoming Senate File 124 (2025), 'Illegal Immigration — Identify, Report, Detain and Deport,' a sweeping immigration-enforcement bill that would prohibit Wyoming law enforcement agencies from banning officers from inquiring about a person's immigration status upon reasonable, articulable suspicion that the person is in the country unlawfully. Kolb joined co-sponsors Sen. Lynn Hutchings and Sen. Cheri Steinmetz as original Senate sponsors, directly demonstrating an anti-sanctuary-city stance consistent with the rubric's border_immigration[2] standard.",
              ["https://wyoleg.gov/Legislation/2025/SF0124",
               "https://wyofile.com/sweeping-state-immigration-crackdown-to-get-wyoming-committee-hearing/"]),
    ]),

    # ---------------- Jared Olsen (WY, State Senator, R) ----------------
    ("jared-olsen", "WY", "State Senator", [
        claim("jo1", "jared-olsen", "family_child_sovereignty", 0, True,
              "Voted for Wyoming House Bill 199 (2025), 'The Wyoming Freedom Scholarship Act,' which creates a universal school-choice program providing up to $7,000 per child to any Wyoming family — regardless of income — for private-school tuition and related educational expenses for pre-K through high-school students. Olsen additionally carried an amendment on the Senate floor reinstating statewide assessment requirements, demonstrating active involvement in shaping the bill. The Senate passed HB 199 on third reading 20-11, enacting what advocates called a landmark expansion of parental authority over children's education consistent with the rubric's family_child_sovereignty[0] standard.",
              ["https://wyofile.com/universal-school-vouchers-clear-senate-with-notable-addition-of-pre-k-funding/",
               "https://cowboystatedaily.com/2025/02/12/bill-to-give-parents-more-school-choice-7k-per-kid-vouchers-advances-barely/"]),
    ]),

    # ---------------- James Lee Anderson (WY, State Senator, R) ----------------
    ("james-lee-anderson", "WY", "State Senator", [
        claim("jla1", "james-lee-anderson", "sanctity_of_life", 0, True,
              "Voted for Wyoming House Bill 126 (2026), the 'Human Heartbeat Act,' which prohibits abortion in Wyoming after a fetal heartbeat is detectable — as early as six weeks of pregnancy. The Wyoming Senate passed HB 126 on third reading on March 4, 2026 by a vote of 27 in favor and 4 opposed, and Governor Mark Gordon signed it into law on March 9, 2026. Anderson's affirmative vote aligns with the rubric's sanctity_of_life[0] life-at-conception/personhood standard.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2026/03/09/gordon-signs-heartbeat-act-abortion-ban-despite-concerns-its-not-enough-for-courts/"]),
    ]),

    # ---------------- Gary Crum (WY, State Senator, R) ----------------
    ("gary-crum", "WY", "State Senator", [
        claim("gc1", "gary-crum", "self_defense", 0, True,
              "As a member of the Senate Judiciary Committee, voted 'aye' to advance Wyoming House Bill 172 (2025), 'Repeal Gun Free Zones and Preemption Amendments,' out of committee in February 2025, along with Sens. Barry Crago, Larry Hicks, and John Kolb. The bill, which would allow concealed carry in schools, government buildings, and most other previously restricted public spaces, subsequently passed the full Senate 25-6 and became law after Governor Mark Gordon allowed it to take effect without his signature. Crum's committee vote demonstrates a constitutional-carry stance consistent with the rubric's self_defense[0] standard.",
              ["https://wyofile.com/majority-speak-against-gun-free-zone-bill-but-panel-poised-to-advance-it/",
               "https://cowboystatedaily.com/2025/02/18/repeal-of-wyomings-gun-free-zones-clear-major-hurdle-headed-to-senate/"]),
    ]),

    # ---------------- Evie Brennan (WY, State Senator, R) ----------------
    ("evie-brennan", "WY", "State Senator", [
        claim("eb1", "evie-brennan", "family_child_sovereignty", 0, True,
              "Voted in favor of Wyoming House Bill 199 (2025), 'The Wyoming Freedom Scholarship Act,' in the Senate Education Committee, and on the Senate floor proposed an amendment to restore the bill's universal coverage after it had been narrowed — her amendment passed, preserving the program's full scope. The Senate ultimately passed HB 199 on third reading 20-11, creating a universal school-choice program that provides up to $7,000 per child to any Wyoming family for private educational expenses from pre-K through 12th grade. Brennan's sustained advocacy for the most expansive form of the program reflects the rubric's family_child_sovereignty[0] parental-rights standard.",
              ["https://wyofile.com/universal-school-vouchers-clear-senate-with-notable-addition-of-pre-k-funding/",
               "https://cowboystatedaily.com/2025/02/12/bill-to-give-parents-more-school-choice-7k-per-kid-vouchers-advances-barely/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
