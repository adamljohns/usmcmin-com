#!/usr/bin/env python3
"""Enrichment batch 532: hand-curated claims for 5 state senators (2 UT, 3 TN).

Targets archetype_party_default state senators from bottom-of-alphabet states
(UT, TN) with 0 evidence claims, taken from the reverse-alphabetical
collision-avoidance bucket (top loop takes AK–AL; this loop takes WY–UT).

Candidates:
  Ann Millner (UT-R) — Utah Senate Majority Whip, SD-5
  Cal Musselman (UT-R) — Utah Senate District 4 (seated Jan 2025)
  Adam Lowe (TN-R) — Tennessee Senate District 1
  Bo Watson (TN-R) — Tennessee Senate District 11, Finance Chair
  Becky Duncan Massey (TN-R) — Tennessee Senate District 6

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50MB limit.
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
    # ---------------- Ann Millner (UT-R, Utah Senate Majority Whip) ----------------
    ("ann-millner", "UT", "State Senator", [
        claim("am1", "ann-millner", "sanctity_of_life", 0, True,
              "Co-sponsored 2022 Utah legislation with Rep. Karianne Lisonbee requiring the state's online abortion informed-consent module to include video of fetal development and audio of a fetal heartbeat — embedding recognition of fetal humanity into required pre-abortion state disclosures.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-action-council-utah-inc/policy/2022-leg-summary"]),
        claim("am2", "ann-millner", "election_integrity", 0, True,
              "As Utah Senate Majority Whip, backed HB300 (2025) requiring voters to write the last four digits of their ID on mail-ballot return envelopes beginning in 2026 and phasing out Utah's automatic universal mail-voting system by January 2029; the Senate passed the bill 19-10.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/"]),
    ]),

    # ---------------- Cal Musselman (UT-R, Utah Senate SD-4) ----------------
    ("cal-musselman", "UT", "State Senator", [
        claim("cm1", "cal-musselman", "border_immigration", 1, True,
              "Sponsored Utah SB90 (2025), Mandatory Jail Sentence Amendments — passed the Senate unanimously — requiring mandatory minimum sentences (90 days to full felony term) for illegal reentrants convicted of further crimes in Utah and barring federal deportation transfer until the complete mandatory sentence is served.",
              ["https://www.deseret.com/politics/2025/03/01/utah-senate-lawmakers-vote-on-immigration-law-enforcement-bills/",
               "https://utahnewsdispatch.com/2025/03/07/utah-legislature-passes-immigration-law-to-support-deportations/"]),
        claim("cm2", "cal-musselman", "sanctity_of_life", 0, True,
              "Voted for Utah HB0467 (2023) as a Utah House member — the Abortion Changes Act requiring abortions to be performed in licensed hospitals with limited exceptions and prohibiting the licensing of new abortion clinics in Utah after May 2, 2023 — extending pro-life clinic restrictions post-Dobbs.",
              ["https://le.utah.gov/~2023/bills/static/HB0467.html",
               "https://www.billsponsor.com/bills/417509/utah-house-bill-467-session-2023"]),
    ]),

    # ---------------- Adam Lowe (TN-R, Tennessee Senate SD-1) ----------------
    ("adam-lowe", "TN", "State Senator", [
        claim("al1", "adam-lowe", "biblical_marriage", 2, True,
              "Sponsored Tennessee SB1/HB1 (signed March 2, 2023), the state's ban on gender-affirming surgeries and puberty blockers for minors — one of the nation's earliest and broadest legislative rejections of transgender medical interventions for children.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://www.aclu-tn.org/legislation/sb-1hb-1-ban-healthcare-trans-youth/"]),
        claim("al2", "adam-lowe", "self_defense", 1, True,
              "Voted to restrict Tennessee cities and counties from enacting emergency risk protection orders (ERPO / red-flag-style authority), blocking local governments from imposing gun-seizure orders that bypass standard judicial due process; tracked by the Tennessee Legislative Report Card.",
              ["https://tnreportcard.org/senators/tn-sd01-lowe/"]),
        claim("al3", "adam-lowe", "sanctity_of_life", 0, True,
              "Voted to prohibit Tennessee counties and municipalities from using taxpayer funds to pay for employee abortions, extending pro-life public-spending restrictions to local government payrolls.",
              ["https://tnreportcard.org/senators/tn-sd01-lowe/"]),
    ]),

    # ---------------- Bo Watson (TN-R, Tennessee Senate SD-11, Finance Chair) ----------------
    ("bo-watson", "TN", "State Senator", [
        claim("bw1", "bo-watson", "self_defense", 0, True,
              "Voted for and, as Senate Finance Committee Chairman, advanced Tennessee's permitless-carry law (SB765/HB786, signed April 8, 2021), eliminating the permit requirement for law-abiding adults 21+ to carry a handgun openly or concealed — the bill cleared his Finance Committee on its path to passage.",
              ["https://www.ammoland.com/2021/03/tennessee-on-the-move-toward-constitutional-carry-hb0786-sb0765/",
               "https://tennesseefirearms.com/2021/03/permitless-carry-bill-clears-another-hurdle-in-tennessee-senate/"]),
        claim("bw2", "bo-watson", "sanctity_of_life", 0, True,
              "A Tennessee Republican senator since 2007, Watson was part of the 23-5 Senate majority that enacted the Human Life Protection Act (SB1257/HB1029, 2019 trigger law), Tennessee's near-total abortion ban that took effect upon the Dobbs ruling in June 2022.",
              ["https://scorecard.factennessee.org/bills/sb-1257hb-1029-human-life-protection-act",
               "https://www.tn.gov/attorneygeneral/news/2022/6/28/pr22-21.html"]),
    ]),

    # ---------------- Becky Duncan Massey (TN-R, Tennessee Senate SD-6) ----------------
    ("becky-duncan-massey", "TN", "State Senator", [
        claim("bdm1", "becky-duncan-massey", "sanctity_of_life", 1, False,
              "Co-sponsored legislation to add rape and incest exceptions to Tennessee's near-total abortion ban — signaling support for restrictions-with-exceptions rather than the full-abolition standard; this stance drew primary opposition in 2024 from anti-abortion activists who argued exceptions contradict life-at-conception principles.",
              ["https://nashvillebanner.com/2024/09/17/tn-reproductive-rights-elections/",
               "https://compassknox.com/2024/10/15/election-2024-state-senate-district-6/"]),
        claim("bdm2", "becky-duncan-massey", "family_child_sovereignty", 0, True,
              "Sponsored Tennessee law requiring law enforcement to immediately notify the Department of Children's Services (DCS) when taking a minor into custody on trafficking-related charges, strengthening state intervention pathways for sexually exploited children.",
              ["https://www.tngopsenate.com/category/becky-massey/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to avoid wrong-state slug collisions."""
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
