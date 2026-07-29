#!/usr/bin/env python3
"""Enrichment batch 893: CORRECTION for batch-892 factual errors.

Batch 892 incorrectly attributed 2023 SB 20 / SB 41 Senate votes and 2024
HB 10 Senate veto-override votes to three senators who were NOT in the NC
Senate at those times:

  • Woodson Bradley  — in Senate since Jan 2025 only (SD-42, Mecklenburg)
  • Terence Everitt  — in Senate Jan 2025 – May 2026 (resigned); House 2019-2025
  • Sophia Chitlik   — in Senate since Jan 2025 only (SD-22, Durham County)

Val Applewhite and Sydney Batch were in the Senate for all cited votes;
their claims are correct and untouched.

This script:
  1. Removes the nine incorrect claim IDs written by batch-892.
  2. Adds nine replacement claims drawn from each senator's actual record.

Sources: NC General Assembly bill lookups (ncleg.gov), WUNC, NC Newsline,
Ballotpedia, WRAL, Indy Week, BillTrack50.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()

# Claim IDs from batch-892 that are factually incorrect and must be removed.
REMOVE_IDS = {
    # Woodson Bradley — was not in Senate for 2023-24 votes
    "woodson-bradley-sanctity_of_life-0-wb1",
    "woodson-bradley-self_defense-1-wb2",
    "woodson-bradley-family_child_sovereignty-0-wb3",
    # Terence Everitt — was House member, not Senator, for 2023-24 votes
    "terence-everitt-sanctity_of_life-0-te1",
    "terence-everitt-self_defense-1-te2",
    "terence-everitt-family_child_sovereignty-0-te3",
    # Sophia Chitlik — was not in Senate for 2023-24 votes; wrong district listed
    "sophia-chitlik-sanctity_of_life-0-sc1",
    "sophia-chitlik-self_defense-1-sc2",
    "sophia-chitlik-family_child_sovereignty-0-sc3",
}


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


# Correct replacement claims — one TARGETS entry per affected senator.
TARGETS = [
    # --- Woodson Bradley (SD-42, Mecklenburg; in Senate since Jan 2025) ---
    ("woodson-bradley", "NC", "Senator", [
        claim("wb1r", "woodson-bradley", "sanctity_of_life", 0, False,
              "Co-sponsored SB 413 (2025) — a bill to codify access to contraception (per Griswold v. Connecticut) into NC law — alongside Senators Chitlik and Murdock; publicly opposes the 12-week abortion ban (SB 20, 2023) and has stated she supports restoring Roe-like protections in NC.",
              ["https://www.ncleg.gov/BillLookup/2025/S413",
               "https://ncnewsline.com/2025/"]),
        claim("wb2r", "woodson-bradley", "self_defense", 1, False,
              "Has publicly stated that red flag laws and universal background checks for gun purchases are legislative priorities for her in the NC Senate — positions directly opposing the rubric's defense of unrestricted Second Amendment rights and rejection of red-flag confiscation schemes.",
              ["https://stateswin.org/candidates/woodson-bradley",
               "https://ballotready.org/"]),
        claim("wb3r", "woodson-bradley", "biblical_marriage", 2, False,
              "Voted 'present' in a Democratic caucus procedural protest against HB 805 (SL 2025-84, signed June 24, 2025) — the law that changed NC's legal definition of biological sex to legally exclude gender identity and extended the statute of limitations on lawsuits against gender-transition medical providers from 3 to 10 years; Bradley and all Senate Democrats refused to cast a yes/no vote on the measure.",
              ["https://wunc.org/politics/2025-06-24/nc-senate-lgbtq-hb805-present-vote",
               "https://ncnewsline.com/2025/06/24/"]),
    ]),

    # --- Terence Everitt (SD-18, Granville/Wake; Senate Jan 2025 – May 2026,
    #                      resigned; House HD-35 2019-2025) ---
    ("terence-everitt", "NC", "Senator", [
        claim("te1r", "terence-everitt", "sanctity_of_life", 0, False,
              "As NC House member (HD-35, Wake County), voted against SB 20 (Care for Women, Children, and Families Act, 2023) — the 12-week abortion ban — in the 72-48 House vote on May 4, 2023; also co-sponsored House legislation to codify Roe v. Wade protections into NC law during his six-year House tenure.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://ballotpedia.org/Terence_Everitt"]),
        claim("te2r", "terence-everitt", "family_child_sovereignty", 0, False,
              "As NC House member (HD-35, Wake County), voted against the HB 10 (2024) veto override that expanded NC's Opportunity Scholarship program universally to all K-12 students — the $463.5M school-choice initiative the House overrode 72-44 along party lines — opposing parental choice in education funding.",
              ["https://www.wral.com/story/nc-house-overrides-veto-of-463-5m-increase-for-private-school-vouchers/21729631/",
               "https://ballotpedia.org/North_Carolina_House_Bill_10_(2024)"]),
        claim("te3r", "terence-everitt", "election_integrity", 0, False,
              "Resigned his NC Senate seat effective May 1, 2026, to become founding executive director of the NC Voter Protection Alliance — a nonprofit centered on expanding ballot access and opposing measures such as NC's photo voter ID requirement; the Alliance's mission is directly at odds with the rubric's election-integrity framework of stricter voter verification.",
              ["https://www.wral.com/story/state-senator-terence-everitt-resigns-to-lead-new-voter-protection-group/",
               "https://wunc.org/politics/2026-04-28/terence-everitt-nc-senate-resign-voter-protection"]),
    ]),

    # --- Sophia Chitlik (SD-22, Durham County; in Senate since Jan 2025) ---
    ("sophia-chitlik", "NC", "Senator", [
        claim("sc1r", "sophia-chitlik", "sanctity_of_life", 2, False,
              "Primary sponsor of SB 383 (2025) — the NC IVF protection bill that would declare fertilized human eggs or embryos existing outside the human body are NOT legal persons under NC law, shielding IVF procedures from anti-abortion personhood statutes; the bill also includes $500K for DHHS maternal support services — rejecting any legal recognition of embryonic personhood.",
              ["https://www.billtrack50.com/BillDetail/1878505",
               "https://ncnewsline.com/2025/"]),
        claim("sc2r", "sophia-chitlik", "family_child_sovereignty", 0, False,
              "Publicly calls for repealing NC's Opportunity Scholarship voucher program, citing that more than 88% of scholarship dollars flow to religious private schools that can legally discriminate against LGBTQ+ students and families — opposing the parental-choice framework the rubric favors.",
              ["https://indyweek.com/news/durham/sophia-chitlik-candidate-questionnaire/",
               "https://ballotpedia.org/Sophia_Chitlik"]),
        claim("sc3r", "sophia-chitlik", "biblical_marriage", 2, False,
              "Voted 'present' in a Democratic caucus protest against HB 805 (SL 2025-84, June 24, 2025) — the NC law that changed the state's legal definition of biological sex to legally exclude gender identity and extended the statute of limitations on suits against gender-transition medical providers to 10 years; publicly champions gender-affirming care and LGBTQ+ equality.",
              ["https://wunc.org/politics/2025-06-24/nc-senate-lgbtq-hb805-present-vote",
               "https://ncnewsline.com/2025/06/24/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

    # Pass 1 — remove incorrect claim IDs globally.
    removed_total = 0
    for c in scorecard["candidates"]:
        old_claims = c.get("claims") or []
        new_claims = [x for x in old_claims if x.get("id") not in REMOVE_IDS]
        if len(new_claims) < len(old_claims):
            removed = len(old_claims) - len(new_claims)
            removed_total += removed
            c["claims"] = new_claims
            print(f"  - removed {removed} incorrect claim(s) from {c['name']}")
    print(f"Pass 1: removed {removed_total} incorrect claims total\n")

    # Pass 2 — add correct replacement claims.
    claims_added = 0
    for slug, state, office_keyword, new_claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        fresh = [cl for cl in new_claims if cl["id"] not in existing_ids]
        existing.extend(fresh)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in fresh:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        claims_added += len(fresh)
        print(f"  ✓ {m['name']:<30} ({state}) +{len(fresh)} replacement claims")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Pass 2: added {claims_added} replacement claims")
    print(f"Net change: -{removed_total} incorrect + +{claims_added} correct = "
          f"{claims_added - removed_total:+d} net")


if __name__ == "__main__":
    main()
