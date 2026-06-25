#!/usr/bin/env python3
"""Enrichment batch 411: 5 Wyoming state representatives — Pendergraft, Clouston, Fornstrom, Jarvis, Webb.

Continues reverse-alpha Wyoming House enrichment from batch 410.
Sources: wyoleg.gov, legiscan.com, wyomingpublicmedia.org, wyofile.com; 2025-2026 sessions.

Targets:
  Ken Pendergraft  (WY-HD29, R, Goshen County, serving since 2023)
  Ken Clouston     (WY-HD32, R, Laramie County, serving since 2023)
  Justin Fornstrom (WY-HD10, R, Laramie County, freshman Dec 2025 special election)
  Julie Jarvis     (WY-HD57, R, Natrona County, serving since 2023)
  Joseph Webb      (WY-HD19, R, Washakie/Hot Springs County, freshman Jan 2025)

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
    # ---- Ken Pendergraft (WY-HD29, Goshen County, R — serving since 2023) ----
    ("ken-pendergraft", "WY", "Representative", [
        claim("kp1", "ken-pendergraft", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable — approximately six weeks of gestation — "
              "with exceptions only for life-threatening medical emergencies and no rape or incest "
              "exception. The House passed it 47–7 on March 5, 2026; Governor Gordon signed it "
              "March 9, 2026, making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
        claim("kp2", "ken-pendergraft", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency "
              "before being placed on the voter rolls, and explicitly prohibits registration using "
              "documents showing non-citizen status. The bill passed the Republican-supermajority "
              "Wyoming House 54–3 on February 28, 2025, and became law March 21, 2025 (Chapter 172) "
              "after Governor Gordon allowed it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- Ken Clouston (WY-HD32, Laramie County, R — serving since 2023) ----
    ("ken-clouston", "WY", "Representative", [
        claim("kc1", "ken-clouston", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. The House passed "
              "it 47–7 on March 5, 2026; Governor Gordon signed it March 9, 2026, making "
              "Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
        claim("kc2", "ken-clouston", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, requiring all new voter registrants to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency, "
              "and explicitly prohibiting registration using documents showing non-citizen status. "
              "The 54–3 House passage on February 28, 2025, reflected near-unanimous Republican "
              "support; the bill became law March 21, 2025 (Chapter 172) after Governor Gordon "
              "allowed it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
    ]),

    # ---- Justin Fornstrom (WY-HD10, Laramie County, R — farmer/rancher, freshman Dec 2025 special election) ----
    ("justin-fornstrom", "WY", "Representative", [
        claim("jf1", "justin-fornstrom", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies and no rape or incest "
              "exception. Fornstrom was sworn in December 16, 2025 (filling the vacancy left by "
              "the late Rep. John Eklund), and joined the 47–7 House majority to pass the bill "
              "on March 5, 2026; Governor Gordon signed it March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/politics-government/2025-12-16/fornstrom-sworn-in-to-wyoming-legislature-replacing-the-late-rep-john-eklund"]),
        claim("jf2", "justin-fornstrom", "self_defense", 1, True,
              "Voted YES on HB0096 (2026), which lowered Wyoming's minimum age to obtain a "
              "concealed-carry permit from 21 to 18, removing an age-based restriction on "
              "young adults' Second Amendment rights. The bill passed the House 58–3 on "
              "February 21, 2026, and was signed by Governor Gordon, taking effect July 1, 2026. "
              "The lopsided vote reflected strong Republican consensus — only 3 members dissented — "
              "and the bill was reported as one of the notable new Wyoming laws of 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0096",
               "https://www.wyomingpublicmedia.org/politics-government/2026-03-10/new-laws-concealed-carry-at-18-professional-wildfire-fighters-and-hand-counting-ballots"]),
    ]),

    # ---- Julie Jarvis (WY-HD57, Natrona County, R — serving since 2023) ----
    ("julie-jarvis", "WY", "Representative", [
        claim("jj1", "julie-jarvis", "sanctity_of_life", 0, False,
              "Voted NO on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation). "
              "Jarvis was one of only 7 House members to vote against the bill on March 5, 2026 "
              "(the others were Democrats and one dissident Republican), joining opponents Byron, "
              "Campbell (E), Chestek, Provenza, Storer, and Yin. Governor Gordon signed the "
              "bill March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("jj2", "julie-jarvis", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide "
              "documentary proof of U.S. citizenship and at least 30 days of bona fide Wyoming "
              "residency, and explicitly prohibits registration using documents showing non-citizen "
              "status. Jarvis joined the 54–3 House majority on February 28, 2025; the bill "
              "became law March 21, 2025 (Chapter 172) after Governor Gordon allowed it to "
              "take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
    ]),

    # ---- Joseph Webb (WY-HD19, Washakie/Hot Springs County, R — freshman Jan 2025) ----
    ("joseph-webb", "WY", "Representative", [
        claim("jw1", "joseph-webb", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Webb joined the "
              "47–7 House majority on March 5, 2026; Governor Gordon signed it March 9, 2026, "
              "making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
        claim("jw2", "joseph-webb", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, requiring all new voter registrants to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency, "
              "and explicitly prohibiting registration using documents showing non-citizen status. "
              "Webb was among the 54 House members (out of 57 voting) to support the bill on "
              "February 28, 2025; it became law March 21, 2025 (Chapter 172) after Governor "
              "Gordon allowed it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
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
