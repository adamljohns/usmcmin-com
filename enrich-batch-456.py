#!/usr/bin/env python3
"""Enrichment batch 456: 5 Virginia House of Delegates members with 0 claims.

Archetype_curated federal buckets fully exhausted after 455 batches.
Pivoting to evidence_state Virginia delegates from the bottom of the alphabet
(VA = near-bottom), all seated members with verifiable 2025-2026 voting records.

Targets (all D, evidence_state, 0 claims):
  - Jackie Glass        (HOD-93, Norfolk)         — seated Jan 10 2024
  - Holly Seibold       (HOD-12)                  — seated Jan 10 2024
  - JJ Singh            (HOD-26)                  — seated Jan 13 2025
  - Gretchen Bulova     (HOD-11, Fairfax)         — seated Jan 13 2026
  - Garrett McGuire     (HOD-17, Fairfax)         — seated Jan 21 2026

Key 2025-2026 VA session votes cited:
  HJR 1 (2025): Reproductive Freedom Amendment, House 51-48 party-line Jan 14 2025
  HJR 9 (2025): Repeal same-sex marriage ban, House 58-35 party-line Jan 14 2025
  HJR 1 (2026): Second passage 64-34 party-line, Jan 16 2026
  HJ3  (2026): Same-sex marriage second passage, Jan 16 2026 party-line
  HB 217 (2026): Assault weapons ban, House 58-34 party-line, Feb 5 2026 (signed by Gov. Spanberger)
  HB1524 (2026): McGuire-sponsored ban on public carry of assault-style firearms (enacted)

NOTE: Gretchen Bulova (seated Jan 13 2026) was present for the Jan 16 2026
constitutional amendment votes. Garrett McGuire (seated Jan 21 2026) missed those
votes; his claims are limited to the Feb 2026 gun control package + HB1524 sponsorship.

Minified write preserves the ~35-36 MB master under GitHub's 50 MB limit.
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
    # ---------------- Jackie Glass (VA-D, HOD-93, Norfolk) ----------------
    ("jackie-glass", "VA", "Delegates", [
        claim("jg1", "jackie-glass", "sanctity_of_life", 0, False,
              "Voted YES on HJR 1 (2025), Virginia's constitutional amendment establishing a fundamental right to reproductive freedom including abortion care. The House passed it 51-48 on a strict party-line vote on Jan. 14, 2025, with every Democrat — including Glass — in support. The amendment cleared both the 2025 and 2026 sessions and appears on the Nov. 2026 ballot.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("jg2", "jackie-glass", "biblical_marriage", 0, False,
              "Voted YES on HJR 9 (2025) to repeal Virginia's constitutional provision defining marriage as only between one man and one woman and replace it with language requiring the state to recognize marriages regardless of the parties' sex or gender. The House passed HJR 9 58-35 on Jan. 14, 2025, on a strict party-line vote.",
              ["https://lis.virginia.gov/bill-details/20251/HJ9",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)"]),
        claim("jg3", "jackie-glass", "self_defense", 1, False,
              "Voted YES on HB 217 (2026), Virginia's sweeping assault-style weapons ban that prohibits the importation, sale, manufacture, purchase, and transfer of assault firearms and large-capacity magazines. The House passed it 58-34 on a party-line vote on Feb. 5, 2026; Governor Spanberger signed it into law.",
              ["https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
    ]),

    # ---------------- Holly Seibold (VA-D, HOD-12) ----------------
    ("holly-seibold", "VA", "Delegates", [
        claim("hs1", "holly-seibold", "sanctity_of_life", 0, False,
              "Voted YES on HJR 1 (2025), the Virginia constitutional amendment to enshrine a right to reproductive freedom including abortion care, passing the House 51-48 on a party-line vote on Jan. 14, 2025. Seibold has publicly stated that protecting abortion rights from Gov. Youngkin and Republican restrictions is her \"top priority.\"",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://ballotpedia.org/Holly_Seibold"]),
        claim("hs2", "holly-seibold", "self_defense", 1, False,
              "Explicitly committed to \"keep pushing to ban assault weapons\" and voted YES on HB 217 (2026), Virginia's assault-style weapons ban passing the House 58-34 on a party-line vote on Feb. 5, 2026, and signed into law by Gov. Spanberger. She has also stated she will protect Virginia's gun-reform progress.",
              ["https://ballotpedia.org/Holly_Seibold",
               "https://lis.virginia.gov/bill-details/20261/HB217"]),
        claim("hs3", "holly-seibold", "biblical_marriage", 0, False,
              "Voted YES on HJR 9 (2025) to repeal Virginia's constitutional one-man-one-woman marriage definition and replace it with language mandating state recognition of marriages regardless of the parties' sex or gender — passing the House 58-35 in a party-line vote on Jan. 14, 2025.",
              ["https://lis.virginia.gov/bill-details/20251/HJ9",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)"]),
    ]),

    # ---------------- JJ Singh (VA-D, HOD-26) ----------------
    ("jas-jeet-singh", "VA", "Delegates", [
        claim("jjs1", "jas-jeet-singh", "sanctity_of_life", 0, False,
              "Voted YES on HJR 1's second passage in the 2026 Virginia General Assembly (64-34, strict party-line), placing a constitutional right to reproductive freedom including abortion care on the Nov. 2026 ballot. Singh had been in office since his Jan. 13, 2025 swearing-in following a special election and was present for both the 2025 and 2026 passages.",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("jjs2", "jas-jeet-singh", "biblical_marriage", 0, False,
              "Voted YES on HJ3 (2026), the second General Assembly passage of the constitutional amendment repealing Virginia's one-man-one-woman marriage clause and requiring recognition of marriages without regard to sex or gender — passed the House on a party-line vote on Jan. 16, 2026.",
              ["https://lis.virginia.gov/bill-details/20261/HJ3",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)"]),
        claim("jjs3", "jas-jeet-singh", "self_defense", 1, False,
              "Voted YES on HB 217 (2026), Virginia's assault-style weapons ban prohibiting the future sale, manufacture, purchase, and transfer of assault firearms and large-capacity magazines, passed 58-34 on a party-line vote on Feb. 5, 2026, and signed by Gov. Spanberger.",
              ["https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
    ]),

    # ---------------- Gretchen Bulova (VA-D, HOD-11, Fairfax) ----------------
    ("gretchen-bulova", "VA", "Delegates", [
        claim("gb1", "gretchen-bulova", "sanctity_of_life", 0, False,
              "Voted YES on HJR 1's second passage (64-34, party-line) in the 2026 Virginia General Assembly, placing a constitutional right to reproductive freedom including abortion care on the Nov. 2026 ballot. Bulova was sworn in Jan. 13, 2026, following a special election, and was present for the Jan. 16, 2026 House vote.",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("gb2", "gretchen-bulova", "biblical_marriage", 0, False,
              "Voted YES on HJ3 (2026), the second passage of the constitutional amendment repealing Virginia's one-man-one-woman marriage definition and requiring the state to recognize marriages without regard to sex or gender — passed the House on a party-line vote Jan. 16, 2026.",
              ["https://lis.virginia.gov/bill-details/20261/HJ3",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)"]),
        claim("gb3", "gretchen-bulova", "self_defense", 1, False,
              "Voted YES on HB 217 (2026), Virginia's assault-style weapons ban (58-34 party-line, Feb. 5, 2026) prohibiting the sale, manufacture, purchase, and transfer of assault firearms and large-capacity magazines; signed into law by Gov. Spanberger.",
              ["https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
    ]),

    # ---------------- Garrett McGuire (VA-D, HOD-17, Fairfax) ----------------
    # Note: seated Jan 21 2026 — missed the Jan 16 constitutional amendment votes.
    # Claims draw on the Feb 2026 gun control package + his own sponsored legislation.
    ("garrett-mcguire", "VA", "Delegates", [
        claim("gm1", "garrett-mcguire", "self_defense", 1, False,
              "Voted YES on HB 217 (2026), Virginia's assault-style weapons ban prohibiting the future sale, manufacture, purchase, and transfer of assault firearms and large-capacity magazines — passed the House 58-34 on a party-line vote on Feb. 5, 2026, and signed by Gov. Spanberger. McGuire was seated Jan. 21, 2026 and was present for this vote.",
              ["https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("gm2", "garrett-mcguire", "self_defense", 0, False,
              "Sponsored and helped enact HB1524 (2026), which prohibits carrying any semi-automatic center-fire rifle, pistol, or shotgun — or any firearm modified to operate as an assault firearm — on public streets, sidewalks, parks, or other public places in Virginia, directly undermining constitutional-carry and open-carry rights. The bill was signed into law.",
              ["https://www.vpap.org/bills/90284/HB1524/",
               "https://lis.virginia.gov/session-details/20261/member-information/H0405/member-details"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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
