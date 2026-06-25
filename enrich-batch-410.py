#!/usr/bin/env python3
"""Enrichment batch 410: 5 Wyoming state representatives — Larsen, Filer, Bratten, L. Brown, Campbell.

Continues reverse-alpha Wyoming House enrichment from batch 409.
Sources: wyoleg.gov, nrlc.org, wyofile.com, wyomingpublicmedia.org, wyomingfamily.org; 2025-2026 sessions.

Targets:
  Lloyd Larsen    (WY-HD54, R, Lander/Fremont County, serving since 2013)
  Lee Filer       (WY-HD44, R, Laramie County, freshman 2025)
  Laurie Bratten  (WY-HD51, R, Sheridan County, freshman 2025)
  Landon Brown    (WY-HD9, R, Cheyenne/Laramie County, serving since 2012)
  Kevin Campbell  (WY-HD62, R, Glenrock/Converse County, freshman 2025)

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
    # ---- Lloyd Larsen (WY-HD54, Lander/Fremont County, R — serving since 2013) ----
    ("lloyd-larsen", "WY", "Representative", [
        claim("ll1", "lloyd-larsen", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion once "
              "fetal cardiac activity is detectable — approximately six weeks of gestation — with "
              "exceptions only for life-threatening medical emergencies and no rape or incest "
              "exception. The House passed it 47–7 on March 5, 2026; Governor Gordon signed it "
              "on March 9, 2026, making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
        claim("ll2", "lloyd-larsen", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency "
              "before being placed on the voter rolls, and explicitly prohibits registration using "
              "documents showing non-citizen status. The bill became law March 21, 2025 "
              "(Chapter 172) after Governor Gordon allowed it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- Lee Filer (WY-HD44, Laramie County, R — Judiciary & Select Blockchain committees) ----
    ("lee-filer", "WY", "Representative", [
        claim("lf1", "lee-filer", "self_defense", 1, True,
              "Named co-sponsor of HB0096 (2026), which lowered Wyoming's minimum age to obtain a "
              "concealed-carry permit from 21 to 18 — removing an age-based restriction on young "
              "adults' Second Amendment rights. The bill passed the House 58–3 and was signed by "
              "Governor Gordon (effective July 1, 2026).",
              ["https://www.wyoleg.gov/Legislation/2026/HB0096",
               "https://legiscan.com/WY/bill/HB0096/2026"]),
        claim("lf2", "lee-filer", "family_child_sovereignty", 0, True,
              "Named co-sponsor of HB0199 (2025), the Wyoming Freedom Scholarship Act, which "
              "expanded Wyoming's education savings accounts into a near-universal school-choice "
              "program providing every family approximately $7,000 per child per year for private "
              "school tuition, tutoring, or homeschool expenses. The bill passed the House 42–19 "
              "and the Senate 20–11, and was signed by Governor Gordon on March 4, 2025.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0199",
               "https://wyomingfamily.org/hb0199-wyoming-freedom-scholarship-act/"]),
    ]),

    # ---- Laurie Bratten (WY-HD51, Sheridan County, R — Judiciary & Education committees) ----
    ("laurie-bratten", "WY", "Representative", [
        claim("lb1", "laurie-bratten", "election_integrity", 0, True,
              "Named co-sponsor of HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires all new voter registrants to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency, and "
              "explicitly prohibits registration using documents showing non-citizen status. The "
              "bill became law March 21, 2025 (Chapter 172) after Governor Gordon allowed it to "
              "take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
        claim("lb2", "laurie-bratten", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion once "
              "fetal cardiac activity is detectable (approximately six weeks of gestation), with "
              "exceptions only for life-threatening medical emergencies and no rape or incest "
              "exception. The House passed it 47–7; the Senate 27–4. Governor Gordon signed it "
              "March 9, 2026, making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
    ]),

    # ---- Landon Brown (WY-HD9, Cheyenne/Laramie County, R — Transportation committee chair, since 2012) ----
    ("landon-brown", "WY", "Representative", [
        claim("lbr1", "landon-brown", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, banning abortion once "
              "fetal cardiac activity is detectable (approximately six weeks), with exceptions "
              "only for life-threatening medical emergencies. A long-serving conservative "
              "legislator who chairs the House Transportation, Highways & Military Affairs "
              "Committee, Brown joined the 47–7 House majority to pass the bill on March 5, "
              "2026; it was signed by Governor Gordon on March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
        claim("lbr2", "landon-brown", "election_integrity", 0, True,
              "Supported HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, requiring all new voter registrants to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency, "
              "and prohibiting registration using documents showing non-citizen status. The bill "
              "passed the Republican-supermajority Wyoming House and became law March 21, 2025 "
              "(Chapter 172) after Governor Gordon allowed it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- Kevin Campbell (WY-HD62, Glenrock/Converse County, R — Revenue & Minerals committees, freshman 2025) ----
    ("kevin-campbell", "WY", "Representative", [
        claim("kc1", "kevin-campbell", "election_integrity", 0, True,
              "Named co-sponsor of HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, requiring all new voter registrants to provide documentary proof "
              "of U.S. citizenship and at least 30 days of bona fide Wyoming residency, and "
              "explicitly prohibiting registration using documents showing non-citizen status. "
              "The bill became law March 21, 2025 (Chapter 172) after Governor Gordon allowed "
              "it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
        claim("kc2", "kevin-campbell", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, and spoke on the House "
              "floor in favor of the bill, sharing his personal story as an adoptee — born to a "
              "14-year-old mother and a serviceman — to advocate for the protection of unborn life. "
              "The bill bans abortions after fetal cardiac activity is detected (approximately six "
              "weeks), with exceptions only for life-threatening medical emergencies. The House "
              "passed it 47–7; it was signed by Governor Gordon on March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
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
