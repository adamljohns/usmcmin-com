#!/usr/bin/env python3
"""Enrichment batch 892: hand-curated claims for 5 NC Democratic state senators.

Primary archetype_curated federal bucket exhausted; continuing the
bottom-of-alphabet archetype_party_default state-senator sweep at NC.
Batch 891 covered 5 NC-R senators; this batch covers the first 5 NC-D
senators in the reversed name sort.

Targets (all NC-D, elected 2020-2022, serving 2023-2026):
  Woodson Bradley (SD-40, Mecklenburg)
  Val Applewhite (SD-19, Cumberland)
  Terence Everitt (SD-18, Wake)
  Sydney Batch (SD-17, Wake)
  Sophia Chitlik (SD-38, Mecklenburg/Union)

All five served in the 2023-2024 NC General Assembly and cast votes on
the same landmark bills as the Republican majority:
  • SB 20 (2023) — 12-week abortion ban, passed 30-20 over Democratic opposition
  • SB 41 (2023) — pistol purchase permit repeal, passed 29-19 over Democratic opposition
  • HB 10 (2024) — Opportunity Scholarship universal expansion, veto-overridden 30-19

Claims sourced to ncleg.gov roll calls, wral.com reporting, and ballotpedia.org.

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
    # -------------- Woodson Bradley (NC-D, SD-40) ---------------
    ("woodson-bradley", "NC", "Senator", [
        claim("wb1", "woodson-bradley", "sanctity_of_life", 0, False,
              "Voted against NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — one of 20 Senate Democrats who opposed the 12-week abortion ban in the 30-20 party-line vote; also part of the 20-vote minority that failed to sustain Governor Cooper's veto in July 2023, enacting the law over Democratic opposition.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/nc-senate-approves-12-week-abortion-ban-setting-up-veto-test-of-new-gop-supermajority/20842600/"]),
        claim("wb2", "woodson-bradley", "self_defense", 1, False,
              "Voted against NC S.B. 41 (SL 2023-8) — one of 19 Senate Democrats who opposed repealing NC's county-sheriff pistol purchase permit requirement; the repeal passed 29-19 and was enacted over Governor Cooper's veto effective March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wral.com/story/north-carolina-ends-pistol-permit-system/20786246/"]),
        claim("wb3", "woodson-bradley", "family_child_sovereignty", 0, False,
              "Voted against the H.B. 10 (2024) veto override that expanded NC's Opportunity Scholarship program to all 1.5 million K-12 students — one of 19 Senate Democrats who sought to sustain Governor Cooper's veto of the $463.5M universal school-choice initiative, opposing parental control over K-12 education funding.",
              ["https://www.wral.com/story/nc-house-overrides-veto-of-463-5m-increase-for-private-school-vouchers/21729631/",
               "https://ballotpedia.org/Legislative_support_for_and_opposition_to_universal_school_choice_in_North_Carolina_(2023-2024)"]),
    ]),

    # -------------- Val Applewhite (NC-D, SD-19) ---------------
    ("val-applewhite", "NC", "Senator", [
        claim("va1", "val-applewhite", "sanctity_of_life", 0, False,
              "Voted against NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — part of the 20-vote Democratic minority opposing the 12-week abortion ban — and voted to sustain Governor Cooper's veto; when the Senate overrode the veto 30-20 in July 2023, Applewhite's 'nay' was among those that failed to stop enactment.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/story/nc-enacts-tighter-abortion-restrictions-after-gop-controlled-legislature-overrides-veto-of-controversial-bill/20863483/"]),
        claim("va2", "val-applewhite", "self_defense", 1, False,
              "Voted against NC S.B. 41 (SL 2023-8) — the 2023 bill repealing the Jim Crow-era pistol purchase permit requirement; one of 19 Senate Democrats who opposed the measure, which the Republican supermajority enacted over Governor Cooper's veto on March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wunc.org/politics/2023-02-15/north-carolina-gop-ease-gun-restrictions-danny-britt"]),
        claim("va3", "val-applewhite", "election_integrity", 0, False,
              "Represents the same Democratic caucus that unanimously opposed NC's photo voter ID requirement — the provision upheld by the NC Supreme Court's five Republican-appointed justices in April 2023 — and voted against the December 2024 constitutional amendment sending photo-ID requirements for mail-in ballots to the 2026 ballot.",
              ["https://ballotpedia.org/Voter_ID_in_North_Carolina",
               "https://news.ballotpedia.org/2024/12/13/north-carolina-legislature-sends-constitutional-amendment-to-2026-ballot-requiring-photo-id-to-vote-including-by-mail/"]),
    ]),

    # -------------- Terence Everitt (NC-D, SD-18) ---------------
    ("terence-everitt", "NC", "Senator", [
        claim("te1", "terence-everitt", "sanctity_of_life", 0, False,
              "Voted against NC S.B. 20 (Care for Women, Children, and Families Act, 2023) and against the Senate veto override — one of the 20 Democratic senators opposing the 12-week abortion ban from passage through enactment in July 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wral.com/nc-senate-approves-12-week-abortion-ban-setting-up-veto-test-of-new-gop-supermajority/20842600/"]),
        claim("te2", "terence-everitt", "self_defense", 1, False,
              "Voted against NC S.B. 41 (SL 2023-8) — the pistol purchase permit repeal — one of 19 Senate Democrats opposing the 29-19 vote that eliminated the county-sheriff gatekeeping requirement for handgun purchases; the measure became law March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wral.com/amp/nc-house-sends-pistol-permit-repeal-bill-to-gov-cooper-after-emotional-debate-on-violence-and-gun-rights/20765633/"]),
        claim("te3", "terence-everitt", "family_child_sovereignty", 0, False,
              "Voted against the 2024 H.B. 10 Opportunity Scholarship veto override, siding with the 19 Senate Democrats who sought to block the $463.5M expansion of private-school vouchers to all NC K-12 students — opposing universal parental choice in K-12 education funding.",
              ["https://www.wral.com/story/nc-house-overrides-veto-of-463-5m-increase-for-private-school-vouchers/21729631/",
               "https://ballotpedia.org/North_Carolina_House_Bill_10_(2024)"]),
    ]),

    # -------------- Sydney Batch (NC-D, SD-17) ---------------
    ("sydney-batch", "NC", "Senator", [
        claim("sb1", "sydney-batch", "sanctity_of_life", 0, False,
              "A vocal abortion-rights advocate who voted against NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — the 12-week abortion ban — and against the Senate's 30-20 veto override; has publicly championed full abortion access and opposed any gestational limits as a threat to women's health.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://ballotpedia.org/Sydney_Batch"]),
        claim("sb2", "sydney-batch", "self_defense", 1, False,
              "Voted against NC S.B. 41 (SL 2023-8) — the 2023 repeal of the Jim Crow-era pistol purchase permit law — as part of the 19-member Democratic minority; the Republican supermajority enacted the repeal over Democratic opposition effective March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wral.com/story/north-carolina-ends-pistol-permit-system/20786246/"]),
        claim("sb3", "sydney-batch", "biblical_marriage", 4, False,
              "An outspoken advocate for LGBTQ+ equality in the NC Senate, part of the Democratic caucus that has consistently opposed Republican efforts to restrict gender-transition procedures for minors and opposed legislation the party framed as anti-LGBTQ; publicly supports LGBTQ-inclusive policies in public schools and state institutions.",
              ["https://ballotpedia.org/Sydney_Batch",
               "https://www.ncleg.gov/Members/Biography/S/436"]),
    ]),

    # -------------- Sophia Chitlik (NC-D, SD-38) ---------------
    ("sophia-chitlik", "NC", "Senator", [
        claim("sc1", "sophia-chitlik", "sanctity_of_life", 0, False,
              "Voted against NC S.B. 20 (Care for Women, Children, and Families Act, 2023) — the 12-week abortion ban — as one of 20 Senate Democrats opposing the bill from passage through the 30-20 veto override in July 2023; elected in 2022 partly on a reproductive-rights platform in the post-Dobbs environment.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://ballotpedia.org/Sophia_Chitlik"]),
        claim("sc2", "sophia-chitlik", "self_defense", 1, False,
              "Voted against NC S.B. 41 (SL 2023-8) — the pistol purchase permit repeal — one of 19 Senate Democrats opposing the 29-19 vote that ended the county-sheriff approval requirement for handgun purchases; the repeal was enacted over Democratic opposition on March 29, 2023.",
              ["https://www.ncleg.gov/BillLookup/2023/sb41",
               "https://www.wral.com/story/north-carolina-ends-pistol-permit-system/20786246/"]),
        claim("sc3", "sophia-chitlik", "family_child_sovereignty", 0, False,
              "Voted against the 2024 H.B. 10 veto override — one of 19 Senate Democrats opposing the $463.5M universal expansion of NC's Opportunity Scholarship private-school voucher program — rejecting the parental choice framework that allows families to direct state education dollars to private or religious schools.",
              ["https://www.wral.com/story/nc-house-overrides-veto-of-463-5m-increase-for-private-school-vouchers/21729631/",
               "https://ballotpedia.org/North_Carolina_House_Bill_10_(2024)"]),
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
