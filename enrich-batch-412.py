#!/usr/bin/env python3
"""Enrichment batch 412: 5 Wyoming state representatives — Storer, Chestek, Provenza, Winter, Guggenmos.

Continues reverse-alpha Wyoming House enrichment from batch 411.
Sources: wyoleg.gov, legiscan.com, wyomingpublicmedia.org; 2025-2026 sessions.

Targets:
  Liz Storer      (WY-HD23, D, Albany County, re-elected 2024)
  Ken Chestek     (WY-HD13, D, Albany County, re-elected 2024)
  Karlee Provenza (WY-HD45, D, Albany County, re-elected 2024 over Paul Crouch)
  John Winter     (WY-HD28, R, Crook County, serving since 2018, re-elected 2024)
  Joel Guggenmos  (WY-HD55, R, Natrona County, freshman Jan 2025 — defeated incumbent Ember Oakley in Aug 2024 primary)

Key bill reference (established in prior batches):
  HB0126 (2026) – Human Heartbeat Act: final 3rd-reading vote 47–7, March 5 2026.
    7 NO votes: Byron, Campbell (E), Chestek, Provenza, Storer, Yin, Jarvis.
    Winter and Guggenmos (R) were in the 47-member YES majority.
  HB0156 (2025) – Proof of Voter Residency: 54 Ayes, 3 Nays (Chestek, Provenza, Sherwood), 5 Excused.
    Storer voted YES; Chestek and Provenza voted NO.
  HB0096 (2026) – Concealed Carry at 18: 58-3-1. R majority voted YES.

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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---- Liz Storer (WY-HD23, Albany County, D — re-elected 2024) ----
    ("liz-storer", "WY", "Representative", [
        claim("ls1", "liz-storer", "sanctity_of_life", 0, False,
              "Voted NO on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Storer was one of "
              "only 7 House members to vote against the bill on March 5, 2026 — joining fellow "
              "Democrats Byron, Chestek, Provenza, and Yin, plus dissident Republicans Campbell "
              "(E) and Jarvis. Governor Gordon signed it March 9, 2026, making Wyoming the 5th "
              "state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("ls2", "liz-storer", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. "
              "The bill passed the House 54–3 on February 28, 2025 (only Chestek, Provenza, and "
              "Sherwood dissented); it became law March 21, 2025 (Chapter 172) after Governor "
              "Gordon allowed it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- Ken Chestek (WY-HD13, Albany County, D — re-elected 2024) ----
    ("ken-chestek", "WY", "Representative", [
        claim("kc1", "ken-chestek", "sanctity_of_life", 0, False,
              "Voted NO on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation). "
              "Chestek was one of only 7 House members to vote against the bill on March 5, 2026 "
              "— alongside Democrats Byron, Provenza, Storer, and Yin, plus Republicans Campbell "
              "(E) and Jarvis. Governor Gordon signed it March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("kc2", "ken-chestek", "election_integrity", 0, False,
              "Voted NO on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires documentary proof of U.S. citizenship and at "
              "least 30 days of bona fide Wyoming residency before voter registration. Chestek "
              "was one of only 3 House members (with Provenza and Sherwood) to vote against the "
              "bill on February 28, 2025 (54–3); it became law March 21, 2025 (Chapter 172) "
              "after Governor Gordon allowed it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
    ]),

    # ---- Karlee Provenza (WY-HD45, Albany County, D — re-elected 2024 over Paul Crouch) ----
    ("karlee-provenza", "WY", "Representative", [
        claim("kp1", "karlee-provenza", "sanctity_of_life", 0, False,
              "Voted NO on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation). "
              "Provenza was one of only 7 House members to vote against the bill on March 5, 2026 "
              "— alongside Democrats Byron, Chestek, Storer, and Yin, plus Republicans Campbell "
              "(E) and Jarvis. Governor Gordon signed it March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("kp2", "karlee-provenza", "election_integrity", 0, False,
              "Voted NO on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires documentary proof of U.S. citizenship and at "
              "least 30 days of bona fide Wyoming residency before voter registration. Provenza "
              "was one of only 3 House members (with Chestek and Sherwood) to vote against the "
              "bill on February 28, 2025 (54–3); it became law March 21, 2025 (Chapter 172) "
              "after Governor Gordon allowed it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
    ]),

    # ---- John Winter (WY-HD28, Crook County, R — serving since 2018, re-elected 2024) ----
    ("john-winter", "WY", "Representative", [
        claim("jw1", "john-winter", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Winter joined the "
              "47-member House majority (against only 7 NO votes) on March 5, 2026; Governor "
              "Gordon signed the bill March 9, 2026, making Wyoming the 5th state to enact a "
              "heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("jw2", "john-winter", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, requiring all new voter registrants to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. "
              "Winter joined the 54-member House majority on February 28, 2025 (54–3; only "
              "Chestek, Provenza, and Sherwood dissented); the bill became law March 21, 2025 "
              "(Chapter 172) after Governor Gordon allowed it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- Joel Guggenmos (WY-HD55, Natrona County, R — freshman Jan 2025, defeated incumbent Ember Oakley in Aug 2024 R primary) ----
    ("joel-guggenmos", "WY", "Representative", [
        claim("jg1", "joel-guggenmos", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Guggenmos joined "
              "the 47-member House majority on March 5, 2026 (against only 7 NO votes); Governor "
              "Gordon signed the bill March 9, 2026, making Wyoming the 5th state to enact a "
              "heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("jg2", "joel-guggenmos", "self_defense", 1, True,
              "Voted YES on HB0096 (2026), which lowered Wyoming's minimum age to obtain a "
              "concealed-carry permit from 21 to 18, removing an age-based restriction on "
              "young adults' Second Amendment rights. The bill passed the House 58–3 on "
              "February 21, 2026 — with only 3 dissents in the Republican-supermajority chamber "
              "— and was signed by Governor Gordon, taking effect July 1, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0096",
               "https://www.wyomingpublicmedia.org/politics-government/2026-03-10/new-laws-concealed-carry-at-18-professional-wildfire-fighters-and-hand-counting-ballots"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states."""
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
