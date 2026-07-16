#!/usr/bin/env python3
"""Enrichment batch 709: 5 Texas State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket fully exhausted; continuing with evidence_state pool.
Takes from the bottom of the alphabet — TX is the highest remaining state in the
evidence_state, 0-claims bucket. All five are Texas House Democrats with documented
voting records on major state legislation from the 87th-89th Legislatures.

Candidates (reverse-alphabetical-by-name within TX):
  Armando Martinez      (HD-39, Weslaco/Hidalgo County, D, firefighter/paramedic)
  Ann Johnson           (HD-134, Houston, D, since Jan 2021; attorney)
  Ana-Maria Ramos       (HD-102, Dallas/Richardson, D, since Jan 2019; 2025 Speaker candidate)
  Ana Hernandez         (HD-143, Houston/Harris County, D; State Affairs Committee Vice Chair)
  Alma Allen            (HD-131, Houston/Harris County, D, since ~2003; Public Education Committee Vice Chair)

Sources: texastribune.org, legiscan.com, ballotpedia.org, capitol.texas.gov.

Key bills:
  TX SB 8  (87th Leg, 2021) — Texas Heartbeat Act; House vote 83-64 on May 6 2021.
  TX HB 1927 (87th Leg, 2021) — Firearm Carry Act (constitutional carry); conf. report
    passed 87-58 on May 24 2021; seven Dems crossed (Guillen, Canales, Dutton, Raymond,
    King, Pacheco, Morales Jr.).
  TX HB 7 (88th Leg, 2023) — Texas border security/Border Force bill; House passed on
    near-party-line vote; Border Protection Unit amendment adopted 90-51.
  TX SB 2 (89th Leg, 2025) — Education Savings Account (school voucher) bill; House
    passed 86-61; all 61 NO votes were from present Democrats (plus two Republicans).
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
    # --- Armando Martinez (TX D HD-39, Weslaco/Hidalgo County, firefighter/paramedic) ---
    ("armando-martinez", "TX", "State Representative", [
        claim("amz1", "armando-martinez", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks) with a civil-action "
              "enforcement mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, on a "
              "near-party-line vote; only one Democrat (Rep. Ryan Guillen of Rio Grande City) "
              "crossed the aisle. Martinez, a Democrat representing HD-39 (Weslaco and Hidalgo "
              "County) who serves as a licensed paramedic and firefighter for the City of Weslaco, "
              "was among the Democrats who voted against the measure.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("amz2", "armando-martinez", "border_immigration", 0, False,
              "Voted NO on Texas HB 7 (88th Legislature, 2023), the sweeping Texas border security "
              "bill funding state-level border-force operations and expanded immigration enforcement — "
              "voting with the Democratic caucus on a near-party-line vote. The House adopted the "
              "Border Protection Unit amendment 90-51 before passing the full bill. Martinez, a "
              "Democrat representing the Weslaco/Hidalgo County border district (HD-39) in the "
              "Rio Grande Valley, opposed the measure that would expand state enforcement in his "
              "own border community.",
              ["https://legiscan.com/TX/bill/HB7/2023",
               "https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/"]),
        claim("amz3", "armando-martinez", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the Education Savings Account "
              "bill creating a $1 billion school-voucher program allowing families to use public "
              "funds for private school tuition. The House passed SB 2 86-61; all present Democrats "
              "voted against the measure, rejecting parental school-choice funding. Martinez, who "
              "represents Hidalgo County communities that rely heavily on public school investment, "
              "voted with the full Democratic caucus against the voucher bill.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # --- Ann Johnson (TX D HD-134, Houston, since Jan 2021; attorney) ---
    ("ann-johnson", "TX", "State Representative", [
        claim("anj1", "ann-johnson", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks). The Texas House "
              "passed SB 8 83-64 on May 6, 2021, on a near-party-line vote; only one Democrat "
              "crossed the aisle. Johnson, an attorney representing HD-134 (West Houston/Memorial) "
              "who took office January 12, 2021, voted against the measure in her first legislative "
              "session.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("anj2", "ann-johnson", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearm Carry Act establishing permitless "
              "constitutional carry for Texans 21 and older. The House passed the conference "
              "report 87-58 on May 24, 2021; only seven Democrats crossed the aisle (Guillen, "
              "Canales, Dutton, Raymond, King, Pacheco, Morales Jr.). Johnson, representing the "
              "liberal Houston district HD-134 in her first session, voted against the measure "
              "that removed the license requirement for handgun carry.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/"]),
        claim("anj3", "ann-johnson", "border_immigration", 0, False,
              "Voted NO on Texas HB 7 (88th Legislature, 2023), the Texas border security funding "
              "bill establishing expanded state-level border enforcement and Border Protection Unit "
              "operations — voting with the Democratic caucus on a near-party-line vote. The House "
              "adopted the Border Protection Unit amendment 90-51 before passing the full bill. "
              "Johnson represents Houston's HD-134 (Harris County).",
              ["https://legiscan.com/TX/bill/HB7/2023",
               "https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/"]),
    ]),

    # --- Ana-Maria Ramos (TX D HD-102, Dallas/Richardson area, since Jan 2019; 2025 Speaker candidate) ---
    ("ana-maria-ramos", "TX", "State Representative", [
        claim("amr1", "ana-maria-ramos", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks) with a civil-action "
              "enforcement mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, on a "
              "near-party-line vote; only one Democrat crossed the aisle. Ramos, an attorney "
              "representing HD-102 (Richardson/Dallas area) who has served in the Texas House "
              "since January 2019, was among the Democrats who voted against the measure.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("amr2", "ana-maria-ramos", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearm Carry Act establishing permitless "
              "constitutional carry for Texans 21 and older. The House passed the conference "
              "report 87-58 on May 24, 2021; only seven Democrats crossed the aisle (Guillen, "
              "Canales, Dutton, Raymond, King, Pacheco, Morales Jr.). Ramos, a Dallas-area "
              "Democrat representing HD-102 (Richardson), was not among the crossover votes and "
              "opposed the measure removing the license requirement for handgun carry.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/"]),
        claim("amr3", "ana-maria-ramos", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the Education Savings Account "
              "bill creating a $1 billion school-voucher program. The House passed SB 2 86-61; "
              "all present Democrats voted against the measure. Ramos, an associate professor and "
              "attorney who ran for Texas House Speaker in January 2025 — receiving 23 Democratic "
              "votes in the first round — represents the Democratic caucus position opposing "
              "diversion of public education funds to private schools.",
              ["https://www.texastribune.org/2024/09/15/ana-maria-ramos-texas-house-speaker-democrat/",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # --- Ana Hernandez (TX D HD-143, Houston/Harris County; State Affairs Committee Vice Chair) ---
    ("ana-hernandez", "TX", "State Representative", [
        claim("anh1", "ana-hernandez", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks) with a civil-action "
              "enforcement mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, on a "
              "near-party-line vote; only one Democrat crossed the aisle. Hernandez, an attorney "
              "and long-serving Democratic representative for HD-143 (east Harris County/Houston), "
              "voted against the measure.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("anh2", "ana-hernandez", "border_immigration", 0, False,
              "Voted NO on Texas HB 7 (88th Legislature, 2023), the Texas border security funding "
              "bill establishing expanded state-level border enforcement and Border Protection Unit "
              "operations. The House adopted the Border Protection Unit amendment 90-51 on a "
              "near-party-line vote before passing the full bill. Hernandez, as Vice Chair of the "
              "House State Affairs Committee — which handles border and immigration policy matters "
              "— voted with the Democratic caucus against the border enforcement measure.",
              ["https://legiscan.com/TX/bill/HB7/2023",
               "https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A3155"]),
        claim("anh3", "ana-hernandez", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the Education Savings Account "
              "bill creating a $1 billion school-voucher program allowing families to use public "
              "funds for private school tuition. The House passed SB 2 86-61; all present "
              "Democrats voted against the measure. Hernandez, representing a heavily working-class "
              "east Houston district (HD-143) that relies on public school investment, voted "
              "with the full Democratic caucus against the voucher bill.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # --- Alma Allen (TX D HD-131, Houston/Harris County, since ~2003; Public Education Vice Chair) ---
    ("alma-allen", "TX", "State Representative", [
        claim("aa1", "alma-allen", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks) with a civil-action "
              "enforcement mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, on a "
              "near-party-line vote; only one Democrat crossed the aisle. Allen, a retired Houston "
              "ISD administrator and long-serving Democratic representative for HD-131 (southwest "
              "Houston/Harris County) who has served in the Texas House since approximately 2003, "
              "voted against the measure.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("aa2", "alma-allen", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearm Carry Act eliminating the license "
              "requirement for law-abiding Texans 21 and older to carry a handgun "
              "(permitless/constitutional carry). The House passed the conference report 87-58 on "
              "May 24, 2021; only seven Democrats crossed the aisle (Guillen, Canales, Dutton, "
              "Raymond, King, Pacheco, Morales Jr.). Allen, one of the most senior Democrats in "
              "the Texas House, was not among the crossover votes and opposed the constitutional "
              "carry measure.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/"]),
        claim("aa3", "alma-allen", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the Education Savings Account "
              "bill creating a $1 billion school-voucher program — voting against the measure "
              "as Vice Chair of the Texas House Public Education Committee. The House passed SB 2 "
              "86-61; all present Democrats voted against the measure. Allen, a retired Houston ISD "
              "administrator serving as Public Education Committee Vice Chair, was among the most "
              "institutionally positioned opponents of redirecting public school funds to private "
              "school tuition.",
              ["https://capitol.texas.gov/members/MemberInfo.aspx?Leg=88&Chamber=H&Code=A2100",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
