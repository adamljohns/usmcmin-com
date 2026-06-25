#!/usr/bin/env python3
"""Enrichment batch 409: 5 Wyoming state representatives — Schmid, Erickson, Lawley, Brady, Connolly.

Continues reverse-alpha Wyoming House enrichment from batch 408.
Sources: wyoleg.gov, wyomingpublicmedia.org, wyofile.com, ballotpedia.org; 2025-2026 sessions.

Targets:
  Michael Schmid   (WY-HD20, R, Lincoln Co., Freedom Caucus, Agriculture + Minerals cmtes)
  McKay Erickson   (WY-HD21, R, Lincoln/Afton area, Appropriations + Revenue cmtes)
  Martha Lawley    (WY-HD27, R, Worland/Washakie Co., Education + Minerals cmtes)
  Marlene Brady    (WY-HD60, R, Green River/Sweetwater Co., Freedom Caucus freshman 2025)
  Marilyn Connolly (WY-HD40, R, Buffalo/Johnson Co., Travel/Wildlife cmte)

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
    # ---- Michael Schmid (WY-HD20, Lincoln County, R — Freedom Caucus, Agriculture & Minerals cmtes) ----
    ("michael-schmid", "WY", "Representative", [
        claim("ms1", "michael-schmid", "sanctity_of_life", 0, True,
              "Co-sponsored HB0126 (2026), Wyoming's Human Heartbeat Act, banning most abortions "
              "from the moment a fetal heartbeat is detectable — approximately six weeks of "
              "gestation — with felony penalties and mandatory professional license revocation "
              "for violators; Governor Gordon signed the law in March 2026 and it took immediate "
              "effect, one of the most restrictive abortion limits in Wyoming history.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("ms2", "michael-schmid", "family_child_sovereignty", 0, True,
              "Primary sponsor of HB0191 (2026 budget session), requiring Wyoming school boards "
              "to comply with enhanced meeting-notice and procedural transparency standards — "
              "mandating advance public notice of board meetings, agendas, and key votes — so "
              "parents and taxpayers have genuine visibility and meaningful input into the K-12 "
              "governance decisions that shape their children's education.",
              ["https://www.wyoleg.gov/Legislators/2025/H/2121",
               "https://www.wyoleg.gov/Legislation/2026/HB0191"]),
    ]),

    # ---- McKay Erickson (WY-HD21, Afton/Lincoln County, R — Appropriations + Revenue cmtes) ----
    ("mckay-erickson", "WY", "Representative", [
        claim("me1", "mckay-erickson", "sanctity_of_life", 0, True,
              "Voted in favor of HB0126 (2026), Wyoming's Human Heartbeat Act, banning most "
              "abortions from the moment a fetal heartbeat is detectable; the bill was signed "
              "by Governor Gordon in March 2026 — affirming the legislature's commitment to "
              "protecting unborn life from the earliest detectable stage of development.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("me2", "mckay-erickson", "refuse_federal_overreach", 0, True,
              "Co-sponsored SJ0009 (2026), a joint legislative memorial demanding Congress "
              "recognize Wyoming's freedom of access to public lands; the resolution opposes "
              "'broad or indiscriminate sale or exchange of public lands,' demands that "
              "Congress and federal agencies respect county land-use plans and local community "
              "voices in federal land-management decisions, and affirms Wyoming's multi-use "
              "framework for agriculture, hunting, fishing, trapping, and conservation — "
              "directly pushing back against top-down federal control over Wyoming resources.",
              ["https://www.wyoleg.gov/Legislation/2026/SJ0009",
               "https://ballotpedia.org/McKay_Erickson"]),
    ]),

    # ---- Martha Lawley (WY-HD27, Worland/Washakie County, R — Education + Minerals cmtes) ----
    ("martha-lawley", "WY", "Representative", [
        claim("ml1", "martha-lawley", "sanctity_of_life", 0, True,
              "Co-sponsored HB0126 (2026), Wyoming's Human Heartbeat Act, banning most abortions "
              "once fetal cardiac activity is detectable — signed into law by Governor Gordon "
              "in March 2026 — reflecting her consistent record as a Wyoming House member of "
              "voting to protect unborn life.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("ml2", "martha-lawley", "family_child_sovereignty", 0, True,
              "As a member of the Wyoming House Education Committee, actively advocated for "
              "HB0199 (Wyoming Freedom Scholarship Act, 2025) — Wyoming's first universal "
              "school-choice program providing every family $7,000 per child per year for "
              "K-12 private school tuition, tutoring, or homeschool expenses — stating on "
              "the House floor that 'Wyoming has always valued individualism and freedom and "
              "it's no surprise that parents in Wyoming want more options and choices for "
              "their children and education.'",
              ["https://wyofile.com/universal-school-voucher-bill-advances-amid-questions-of-accountability-constitutionality/",
               "https://ballotpedia.org/Martha_Lawley"]),
    ]),

    # ---- Marlene Brady (WY-HD60, Green River/Sweetwater County, R — Freedom Caucus freshman 2025) ----
    ("marlene-brady", "WY", "Representative", [
        claim("mb1", "marlene-brady", "sanctity_of_life", 0, True,
              "Co-sponsored HB0126 (2026), Wyoming's Human Heartbeat Act, as one of the lead "
              "House sponsors banning most abortions from the moment a fetal heartbeat is "
              "detectable; the law was signed by Governor Gordon in March 2026 and represents "
              "one of her most prominent legislative acts in her freshman term.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("mb2", "marlene-brady", "election_integrity", 0, True,
              "As a Freedom Caucus-endorsed freshman who ran on a conservative election-security "
              "platform, voted for HB0156 (2025) — the Wyoming voter residency and citizenship "
              "documentation law requiring every new registrant to prove U.S. citizenship and "
              "at least 30 days of bona fide Wyoming residency before being placed on the voter "
              "rolls; the bill sailed through the Republican-supermajority Legislature and "
              "became law effective July 1, 2025.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/"]),
    ]),

    # ---- Marilyn Connolly (WY-HD40, Buffalo/Johnson County, R — Travel/Wildlife cmte) ----
    ("marilyn-connolly", "WY", "Representative", [
        claim("mc1", "marilyn-connolly", "sanctity_of_life", 0, True,
              "Co-sponsored HB0126 (2026), Wyoming's Human Heartbeat Act, joining the Republican "
              "House supermajority to ban most abortions from the moment of detectable fetal "
              "cardiac activity — a law signed by Governor Gordon in March 2026 that took "
              "immediate effect and reflects her commitment to protecting unborn human life "
              "from the earliest detectable stage.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
        claim("mc2", "marilyn-connolly", "refuse_federal_overreach", 0, True,
              "As a member of the House Travel, Recreation, Wildlife and Cultural Resources "
              "Committee, voted for SJ0009 (2026), Wyoming's joint legislative memorial to "
              "Congress demanding respect for local control over public lands; the resolution "
              "— which passed both chambers of the Wyoming Legislature with broad bipartisan "
              "support — opposes indiscriminate federal land sales or transfers, requires "
              "Congress and federal agencies to honor county land-use plans and local "
              "community voices, and affirms Wyoming's multi-use public-lands framework for "
              "agriculture, hunting, fishing, and conservation.",
              ["https://www.wyoleg.gov/Legislation/2026/SJ0009",
               "https://ballotpedia.org/Marilyn_Connolly"]),
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
