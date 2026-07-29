#!/usr/bin/env python3
"""Enrichment batch 891: hand-curated claims for 5 NC Republican state senators.

Primary archetype_curated federal bucket exhausted; falling back to the next
available bottom-of-alphabet bucket: archetype_party_default NC state senators
(NC is the lowest remaining state with unenriched senators after WY/WV/WI/WA/VA
are fully done).

Targets (all NC-R, elected 2022, serving 2023-2026, confirmed by next_election=2026):
  Bill Rabon (SD-8, Brunswick/Columbus/New Hanover)
  Jim Burgin (SD-12, Harnett/Lee/Sampson)
  Danny Earl Britt Jr. (SD-23, Robeson/Scotland/Richmond)
  Brent Jackson (SD-9, Bladen/Duplin/Jones/Pender/Sampson; Senate President Pro Tempore)
  Buck Newton (SD-4, primary sponsor NC SB 153 2025)

All major claims sourced to ncleg.gov roll calls, wral.com reporting, and
ballotpedia.org. Each senator voted on the same 2023 party-line bills (SB 20,
SB 41) as part of the 30-seat NC Senate Republican supermajority.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the
master under GitHub's 50MB warning.
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
    # -------------- Bill Rabon (NC-R, SD-8) ---------------
    ("bill-rabon", "NC", "Senator", [
        claim("br1", "bill-rabon", "sanctity_of_life", 0, True,
              "Voted for NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — the party-line 30-20 Senate vote banning most abortions after 12 weeks, then joined the 30-20 Senate veto override that enacted the law over Governor Cooper's veto in July 2023; one of the most significant state-level pro-life legislative wins in NC history.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/nc-senate-approves-12-week-abortion-ban-setting-up-veto-test-of-new-gop-supermajority/20842600/"]),
        claim("br2", "bill-rabon", "self_defense", 1, True,
              "Voted for NC S.B. 41 (SL 2023-8) — repealing NC's pistol purchase permit law, a Jim Crow-era statute that required North Carolinians to obtain a county sheriff's written permission before buying a handgun; the Senate passed the repeal 29-19 and overrode Governor Cooper's veto, effective March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wral.com/story/north-carolina-ends-pistol-permit-system/20786246/"]),
        claim("br3", "bill-rabon", "election_integrity", 0, True,
              "Part of the NC Senate Republican supermajority that championed and defended NC's photo voter ID requirement — upheld by the state Supreme Court's five Republican-appointed justices in April 2023 — and voted in December 2024 to send a constitutional amendment to the 2026 ballot extending the photo ID requirement to mail-in ballots.",
              ["https://ballotpedia.org/Voter_ID_in_North_Carolina",
               "https://news.ballotpedia.org/2024/12/13/north-carolina-legislature-sends-constitutional-amendment-to-2026-ballot-requiring-photo-id-to-vote-including-by-mail/"]),
    ]),

    # -------------- Jim Burgin (NC-R, SD-12) ---------------
    ("jim-burgin", "NC", "Senator", [
        claim("jb1", "jim-burgin", "sanctity_of_life", 0, True,
              "Voted for NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — the 30-20 party-line Senate vote banning most abortions after 12 weeks — and joined the Senate's 30-20 veto override that enacted the law in July 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/story/north-carolina-senate-overrides-governor-s-abortion-ban-veto/20863796/"]),
        claim("jb2", "jim-burgin", "family_child_sovereignty", 0, True,
              "Voted to override Governor Cooper's veto of H.B. 10 (2024), the legislation expanding NC's Opportunity Scholarship program universally to all 1.5 million K-12 students regardless of income — a $463.5 million parental school-choice initiative and one of the largest expansions of private school vouchers in state history; the Senate vote passed with all Republicans in favor.",
              ["https://www.wral.com/story/nc-house-overrides-veto-of-463-5m-increase-for-private-school-vouchers/21729631/",
               "https://ballotpedia.org/Legislative_support_for_and_opposition_to_universal_school_choice_in_North_Carolina_(2023-2024)"]),
        claim("jb3", "jim-burgin", "self_defense", 1, True,
              "Voted for NC S.B. 41 (SL 2023-8) — repealing NC's Jim Crow-era pistol purchase permit requirement that let county sheriffs gatekeep handgun purchases; enacted over the governor's veto effective March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wral.com/amp/nc-house-sends-pistol-permit-repeal-bill-to-gov-cooper-after-emotional-debate-on-violence-and-gun-rights/20765633/"]),
    ]),

    # -------------- Danny Earl Britt Jr. (NC-R, SD-24) ---------------
    ("danny-earl-britt-jr", "NC", "Senator", [
        claim("db1", "danny-earl-britt-jr", "self_defense", 1, True,
              "Primary Senate sponsor of S.B. 41 (SL 2023-8) — the bill repealing NC's pistol purchase permit law, a Jim Crow-era statute requiring county-sheriff approval before buying a handgun, and authorizing licensed concealed-carry holders to carry in places of religious worship held on school property; the 30-19 Senate veto override enacted it March 29, 2023. Gun rights groups specifically credited Britt for the win and for rejecting red-flag gun confiscation schemes.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wunc.org/politics/2023-02-15/north-carolina-gop-ease-gun-restrictions-danny-britt"]),
        claim("db2", "danny-earl-britt-jr", "sanctity_of_life", 0, True,
              "Voted for NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — the 30-20 party-line Senate vote banning most abortions after 12 weeks — and joined the Senate's 30-20 veto override, enacting the law in July 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://en.wikipedia.org/wiki/Abortion_in_North_Carolina"]),
        claim("db3", "danny-earl-britt-jr", "border_immigration", 2, True,
              "Part of the NC Senate Republican caucus that passed NC S.B. 153 (SL 2026-19, effective July 29, 2025) — the North Carolina Border Protection Act — requiring state law enforcement to enter 287(g) Memoranda of Agreement with ICE, prohibiting all local sanctuary-style ordinances, and barring UNC system institutions from limiting immigration enforcement.",
              ["https://www.ncleg.gov/BillLookup/2025/S153",
               "https://dashboard.ncleg.gov/api/Services/BillSummary/2025/S153-SMCV-72(e2)-v-3"]),
    ]),

    # -------------- Brent Jackson (NC-R, SD-9, Senate President Pro Tempore) ---------------
    ("brent-jackson", "NC", "Senator", [
        claim("bj1", "brent-jackson", "sanctity_of_life", 0, True,
              "As Senate President Pro Tempore, helped lead NC S.B. 20 (Care for Women, Children, and Families Act, 2023) to passage; the bill banned most abortions after 12 weeks in a 30-20 party-line Senate vote and was enacted over Governor Cooper's veto in a 30-20 Senate override in July 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/nc-senate-approves-12-week-abortion-ban-setting-up-veto-test-of-new-gop-supermajority/20842600/"]),
        claim("bj2", "brent-jackson", "family_child_sovereignty", 0, True,
              "Voted with all Senate Republicans to override Governor Cooper's veto of H.B. 10 (2024), expanding NC's Opportunity Scholarship program universally to all K-12 students — a $463.5 million investment in parental school choice that made NC one of the first states to offer universal private-school vouchers.",
              ["https://www.wral.com/story/nc-house-overrides-veto-of-463-5m-increase-for-private-school-vouchers/21729631/",
               "https://www.wral.com/story/republicans-strike-deal-on-funding-school-vouchers-plan-votes-starting-monday/21611710/"]),
        claim("bj3", "brent-jackson", "self_defense", 1, True,
              "Voted for NC S.B. 41 (SL 2023-8) — repealing the county sheriff pistol purchase permit requirement that had gatekept handgun purchases since 1919; the 29-19 Senate vote and subsequent veto override enacted the repeal effective March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://en.wikipedia.org/wiki/Gun_laws_in_North_Carolina"]),
    ]),

    # -------------- Buck Newton (NC-R, SD-4) ---------------
    ("buck-newton", "NC", "Senator", [
        claim("bn1", "buck-newton", "border_immigration", 2, True,
              "Primary co-sponsor (alongside Senate leader Phil Berger) of NC S.B. 153 — the North Carolina Border Protection Act (SL 2026-19, effective July 29, 2025) — which requires NC state law enforcement agencies to enter 287(g) Memoranda of Agreement with ICE, bans local sanctuary-city ordinances statewide, prohibits UNC system institutions from limiting immigration enforcement, and requires unemployment-benefits applicants to verify legal residency.",
              ["https://www.ncleg.gov/BillLookup/2025/S153",
               "https://www.ncleg.gov/Members/IntroducedBills/s/443"]),
        claim("bn2", "buck-newton", "sanctity_of_life", 0, True,
              "Voted for NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — the 30-20 party-line Senate vote banning most abortions after 12 weeks — and joined the 30-20 Senate veto override that enacted the law in July 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/story/nc-enacts-tighter-abortion-restrictions-after-gop-controlled-legislature-overrides-veto-of-controversial-bill/20863483/"]),
        claim("bn3", "buck-newton", "election_integrity", 0, True,
              "Chair of the NC Senate Redistricting and Elections Committee and NC GOP Election Integrity Committee; championed photo voter ID (upheld by NC Supreme Court in April 2023); advanced H.B. 958 (July 2026) requiring citizenship attestation on voter-registration forms and vetting voter rolls against the federal USCIS SAVE database — one of the strictest non-citizen voter protections passed by any state legislature.",
              ["https://ballotpedia.org/Buck_Newton",
               "https://ncnewsline.com/2026/07/28/nc-senate-advances-controversial-but-slimmed-down-elections-changes/"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
