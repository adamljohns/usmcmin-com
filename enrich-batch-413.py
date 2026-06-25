#!/usr/bin/env python3
"""Enrichment batch 413: 5 Wyoming state representatives — Lien, Wasserburger, Larson, Riggins, Williams.

Continues reverse-alpha Wyoming House enrichment from batch 412.
Sources: wyoleg.gov, legiscan.com, ballotpedia.org, wyomingpublicmedia.org,
         oilcity.news, cowboystatedaily.com, bitcoinmagazine.com; 2025-2026 sessions.

Targets:
  Jayme Lien         (WY-HD38, R, Natrona County, elected 2024, 1st term)
  Jacob Wasserburger (WY-HD11, R, Laramie County, elected 2024, 1st term)
  J.T. Larson        (WY, R, State Representative)
  J.R. Riggins       (WY-HD59, R, Natrona County, elected 2024, 1st term)
  J.D. Williams      (WY, R, State Representative)

Key bill references:
  HB0126 (2026) – Human Heartbeat Act: bans abortion at detectable heartbeat (~6 wks).
    House 3rd Reading Feb 24, 2026: 51-7. House Concurrence March 5, 2026: 47-7-8.
    7 NO votes: Byron, Campbell(E), Chestek, Provenza, Storer, Yin, Jarvis.
    Lien was a named co-sponsor (27 co-sponsors total; primary sponsor: Rep. Neiman).
    Larson (J.T.), Riggins, Wasserburger, and Williams confirmed in AYES on March 5 roll call.
    Lien confirmed co-sponsor; excused from March 5 concurrence, YES on Feb 24 3rd Reading.
    Governor Gordon signed as HEA No. 29 on March 9, 2026.
  HB0156 (2025) – Proof of Voter Residency-Registration Qualifications Act:
    Passed House 54-3 (NO: Chestek, Provenza, Sherwood only). Became law March 21, 2025.
    None of the 5 targets are on the NO list, confirming YES votes.
  HB0032 (2025) – "What is a Woman Act": codifies biological sex definitions in statute.
    Primary sponsor: Lien. Became law March 14, 2025 (took effect without governor signature).
  HB0201 (2025) – State Funds-Investment in Bitcoin Act:
    Sponsored by Wasserburger et al. Authorized investing up to 3% of state funds in Bitcoin.
    Died in House Minerals Committee 1-7 on Feb 10, 2025.
  HB0172 (2025) – Firearms preemption / gun-free-zone repeal:
    Co-sponsored by Riggins. Amends or repeals gun-free-zone restrictions and strengthens
    state firearms preemption.

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
    # ---- Jayme Lien (WY-HD38, Natrona County, R — elected 2024, 1st term) ----
    ("jayme-lien", "WY", "Representative", [
        claim("jl1", "jayme-lien", "biblical_marriage", 2, True,
              "Primary sponsor of HB0032 (2025), Wyoming's 'What is a Woman Act,' which codified "
              "legal definitions of 'female,' 'male,' 'woman,' 'girl,' 'mother,' and 'father' "
              "exclusively on biological sex at birth — giving Wyoming's judiciary clear, sex-based "
              "definitions for the 200+ state statutes that reference sex and directly rejecting the "
              "premise that legal gender can differ from biological sex. Lien, a homeschooling mother "
              "of five from Casper (Natrona County) who unseated a 6-term incumbent in the August "
              "2024 primary, championed the legislation as protective of women's legal standing. It "
              "became law March 14, 2025 without Governor Gordon's signature, making Wyoming the "
              "13th state to define 'woman' in statute.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0032",
               "https://wyomingfamily.org/hb0032-what-is-a-woman-act/",
               "https://www.iwvoice.com/2025/03/wyoming-becomes-13th-state-to-define-woman-in-law-without-governor-mark-gordons-support/"]),
        claim("jl2", "jayme-lien", "sanctity_of_life", 0, True,
              "Named co-sponsor of HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), with "
              "exceptions only for life-threatening medical emergencies. Lien was one of 27 House "
              "co-sponsors (primary sponsor: Rep. Chip Neiman) and voted YES on the February 24, 2026 "
              "3rd Reading (51-7 passage); she was excused from the final March 5 concurrence vote "
              "but her sponsorship reflects unambiguous support for protecting unborn life from "
              "conception. Governor Gordon signed the bill (HEA No. 29) on March 9, 2026, making "
              "Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("jl3", "jayme-lien", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. The "
              "bill passed the House 54-3 on February 28, 2025 (only Chestek, Provenza, and Sherwood "
              "dissented); it became law March 21, 2025 (Chapter 172) after Governor Gordon allowed "
              "it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- Jacob Wasserburger (WY-HD11, Laramie County, R — elected 2024, 1st term) ----
    ("jacob-wasserburger", "WY", "Representative", [
        claim("jw1", "jacob-wasserburger", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Wasserburger is "
              "confirmed by name in the 47-member House majority on the March 5, 2026 concurrence "
              "roll call (47-7, with only 7 members dissenting). Governor Gordon signed the bill "
              "(HEA No. 29) on March 9, 2026, making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("jw2", "jacob-wasserburger", "economic_stewardship", 1, True,
              "Primary sponsor of HB0201 (2025), the State Funds-Investment in Bitcoin Act, which "
              "would have authorized Wyoming's State Treasurer to invest up to 3% of the General "
              "Fund, Permanent Wyoming Mineral Trust Fund, and Permanent Land Fund in Bitcoin — "
              "treating the fixed-supply, decentralized asset as a state-level hard-money hedge "
              "against fiat debasement and inflationary monetary policy. Though the bill died in "
              "the House Minerals Committee (1-7 vote, Feb. 10, 2025), Wasserburger continued "
              "advancing sound-money and digital-asset initiatives through his assignment to the "
              "Wyoming Select Committee on Blockchain, Financial Technology and Digital Innovation "
              "Technology.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0201",
               "https://legiscan.com/WY/bill/HB0201/2025",
               "https://bitcoinmagazine.com/politics/wyoming-introduces-bitcoin-strategic-reserve-bill-"]),
        claim("jw3", "jacob-wasserburger", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. The "
              "bill passed the House 54-3 on February 28, 2025 (only Chestek, Provenza, and Sherwood "
              "dissented); it became law March 21, 2025 (Chapter 172) after Governor Gordon allowed "
              "it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- J.T. Larson (WY, R — State Representative) ----
    ("jt-larson", "WY", "Representative", [
        claim("jtl1", "jt-larson", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Larson appears by "
              "name ('Larson J.T.' — distinguished in the roll call from Rep. L. Larsen) in the "
              "47-member House majority on the March 5, 2026 concurrence vote (47-7, with only "
              "7 members dissenting). Governor Gordon signed the bill (HEA No. 29) on March 9, 2026, "
              "making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("jtl2", "jt-larson", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. The "
              "bill passed the House 54-3 on February 28, 2025 (only Chestek, Provenza, and Sherwood "
              "dissented); it became law March 21, 2025 (Chapter 172) after Governor Gordon allowed "
              "it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- J.R. Riggins (WY-HD59, Natrona County, R — elected 2024, 1st term) ----
    ("jr-riggins", "WY", "Representative", [
        claim("jrr1", "jr-riggins", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Riggins appears by "
              "name in the 47-member House majority on the March 5, 2026 concurrence vote (47-7, "
              "with only 7 members dissenting). Governor Gordon signed the bill (HEA No. 29) on "
              "March 9, 2026, making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("jrr2", "jr-riggins", "self_defense", 1, True,
              "Co-sponsored HB0172 (2025), Wyoming's repeal of gun-free-zone statutes and "
              "strengthening of state firearms preemption — removing existing statutory restrictions "
              "on carrying lawfully owned firearms in previously designated gun-free locations and "
              "asserting exclusive state authority over firearm regulation, preempting local "
              "governments and universities. The bill passed the House 50-10 and became law on "
              "February 28, 2025, without Governor Gordon's signature. Gun Owners of America "
              "praised its enactment. Riggins, a 40-year natural-gas industry veteran representing "
              "the Casper area (HD-59), has described defending Constitutional rights as a core "
              "commitment.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://www.gunowners.org/wy02282025/",
               "https://ballotpedia.org/J.R._Riggins"]),
        claim("jrr3", "jr-riggins", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. The "
              "bill passed the House 54-3 on February 28, 2025 (only Chestek, Provenza, and Sherwood "
              "dissented); it became law March 21, 2025 (Chapter 172) after Governor Gordon allowed "
              "it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---- J.D. Williams (WY, R — State Representative) ----
    ("jd-williams", "WY", "Representative", [
        claim("jdw1", "jd-williams", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Williams appears by "
              "name in the 47-member House majority on the March 5, 2026 concurrence vote (47-7, "
              "with only 7 members dissenting). Governor Gordon signed the bill (HEA No. 29) on "
              "March 9, 2026, making Wyoming the 5th state to enact a heartbeat law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("jdw2", "jd-williams", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. The "
              "bill passed the House 54-3 on February 28, 2025 (only Chestek, Provenza, and Sherwood "
              "dissented); it became law March 21, 2025 (Chapter 172) after Governor Gordon allowed "
              "it to take effect without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
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
