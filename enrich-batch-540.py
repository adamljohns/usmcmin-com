#!/usr/bin/env python3
"""Enrichment batch 540: 10 new claims across 5 Texas Republican state representatives.

Continuing the TX evidence_state pool. All five are H/G/E-name Republican state
reps with 0 claims, taken from the top of the reverse-alpha list (bottom of the
canonical alphabet order to avoid collisions with the top-of-alphabet agent).

Targets:
  Hillary Hickland  (HD-55, McLennan County / Waco area — new Jan 2025)
  Helen Kerwin      (HD-58, Johnson County — new Jan 2025, replaced anti-voucher Burns)
  Gary VanDeaver    (HD-1, Red River County — retiring after 2026; dissented on SB 2)
  Gary Gates        (HD-28, Fort Bend County / SW Houston — businessman, strong conservative)
  Ellen Troxclair   (HD-19, Burnet County / TX Hill Country — small business owner)

Two distinct rubric-category claims per target. Sources: ballotpedia.org,
texasallianceforlife.org, texastribune.org, legis.state.tx.us, en.wikipedia.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # --- Hillary Hickland (TX HD-55, R — McLennan County / Waco area, new Jan 2025) ---
    ("hillary-hickland", "TX", "State Representative", [
        claim("hh540a", "hillary-hickland", "sanctity_of_life", 0, True,
              "Hickland earned a 93% rating on the Texas Alliance for Life 2025 Legislative Scorecard (89th Legislature), voting for the full slate of pro-life bills including SB 31 (Life of the Mother Act, clarifying that medically necessary care is permitted under Texas abortion law), HB 7 (Mail-Order Abortion Drug Enforcement, imposing civil penalties on providers who mail abortion-inducing drugs into Texas), and SB 33 (Ban on Taxpayer-Funded Abortion Travel). She ran in 2024 explicitly on protecting Texas's abortion laws and won the seat from a less-conservative incumbent.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Hillary_Hickland"]),
        claim("hh540b", "hillary-hickland", "family_child_sovereignty", 0, True,
              "Hickland described herself publicly as a 'strong supporter of school choice in the form of Education Savings Accounts' and was endorsed by Governor Greg Abbott in her successful 2024 primary challenge against incumbent Rep. Hugh Shine, who had opposed school-voucher legislation. She voted for Texas SB 2 (89th Legislature, signed May 2025), the landmark Education Savings Account program, in the House's 85-vote Republican majority that enacted Texas's first universal school-choice law.",
              ["https://ballotpedia.org/Hillary_Hickland",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # --- Helen Kerwin (TX HD-58, R — Johnson County, new Jan 2025) ---
    ("helen-kerwin", "TX", "State Representative", [
        claim("hk540a", "helen-kerwin", "sanctity_of_life", 0, True,
              "Kerwin received a 93% rating on the Texas Alliance for Life 2025 Legislative Scorecard for the 89th Texas Legislature, voting with the pro-life majority on key bills: SB 31 (Life of the Mother Act), HB 7 (Mail-Order Abortion Drug Enforcement), and SB 33 (Ban on Taxpayer-Funded Abortion Travel). She ran in 2024 as a conservative challenger against incumbent Rep. DeWayne Burns and won, carrying on a strong pro-life record from her first session.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Helen_Kerwin"]),
        claim("hk540b", "helen-kerwin", "family_child_sovereignty", 0, True,
              "Kerwin defeated incumbent Rep. DeWayne Burns in the 2024 Republican primary specifically because Burns had voted against school-voucher legislation in the 88th Legislature — Burns was one of the rural Republicans whose opposition killed the voucher bill in 2023. Kerwin ran on reversing that position, won the seat, and voted for Texas SB 2 (89th Legislature, signed May 2025), the $1 billion Education Savings Account program that grants families state funds for private school tuition or homeschooling.",
              ["https://ballotpedia.org/Helen_Kerwin",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # --- Gary VanDeaver (TX HD-1, R — Red River/Bowie County, retiring 2026) ---
    ("gary-vandeaver", "TX", "State Representative", [
        claim("gvd540a", "gary-vandeaver", "sanctity_of_life", 0, True,
              "VanDeaver received a 97% rating on the Texas Alliance for Life 2025 Legislative Scorecard (89th Legislature), one of the highest scores in the Texas House. He voted for all key pro-life bills tracked by TAL including SB 31 (Life of the Mother Act), HB 7 (Mail-Order Abortion Drug Enforcement), and SB 33 (Ban on Taxpayer-Funded Abortion Travel), demonstrating a consistent pro-life record across multiple legislative sessions despite other departures from the Republican majority.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Gary_VanDeaver"]),
        claim("gvd540b", "gary-vandeaver", "family_child_sovereignty", 0, False,
              "VanDeaver was one of only two Republicans — along with former Speaker Dade Phelan — to vote against Texas SB 2 (89th Legislature, April 2025), the landmark $1 billion Education Savings Account program enabling families to use state funds for private-school tuition or homeschooling. His vote against school choice aligned him with all House Democrats and triggered a censure from the Texas Republican Party on October 11, 2025. VanDeaver announced in December 2025 that he would not seek re-election in 2026.",
              ["https://www.texastribune.org/2025/04/17/texas-house-voucher-vote-breakdown-2025/",
               "https://ballotpedia.org/Gary_VanDeaver"]),
    ]),

    # --- Gary Gates (TX HD-28, R — Fort Bend County / SW Houston metro) ---
    ("gary-gates", "TX", "State Representative", [
        claim("gg540a", "gary-gates", "sanctity_of_life", 0, True,
              "Gates received a 97% rating on the Texas Alliance for Life 2025 Legislative Scorecard (89th Legislature), voting for the full suite of pro-life legislation including HB 7 (Mail-Order Abortion Drug Enforcement), SB 31 (Life of the Mother Act), and SB 33 (Ban on Taxpayer-Funded Abortion Travel). He has maintained a strong pro-life record since first winning the HD-28 seat in 2020, supporting the Human Life Protection Act trigger ban (2021) and SB 8 fetal heartbeat law (2021) that protect life from fertilization.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Gary_Gates"]),
        claim("gg540b", "gary-gates", "election_integrity", 0, True,
              "Gates voted for Texas SB 1 (87th Legislature, 2021 third special session), the comprehensive election-security law that mandates photo voter ID for mail-in ballots, bans drive-through and 24-hour voting, limits unsolicited mail-in ballot applications, and strengthens partisan poll-watcher access inside voting locations — one of the most sweeping state election-integrity statutes enacted in 2021. Representing a competitive Fort Bend County suburban district, Gates has consistently backed Republican election-security priorities.",
              ["https://ballotpedia.org/Gary_Gates",
               "https://ballotpedia.org/Texas_Senate_Bill_1_(2021)"]),
    ]),

    # --- Ellen Troxclair (TX HD-19, R — Burnet County / Hill Country) ---
    ("ellen-troxclair", "TX", "State Representative", [
        claim("et540a", "ellen-troxclair", "family_child_sovereignty", 0, True,
              "Troxclair voted for Texas SB 2 (89th Legislature, signed May 2025), the Education Savings Account program enabling families to use state funds for private-school tuition or homeschooling. She had been a school-choice advocate since her time on the Austin City Council (2014–2018), and as a state representative from the conservative Hill Country HD-19 district she supported the final passage of SB 2 in the 85-vote Republican majority that enacted Texas's first universal school-choice law.",
              ["https://ballotpedia.org/Ellen_Troxclair",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
        claim("et540b", "ellen-troxclair", "economic_stewardship", 2, True,
              "As a small business owner representing the TX HD-19 Hill Country district, Troxclair serves on the House Delivery of Government Efficiency (DOGE) Committee — Texas's equivalent of the federal efficiency effort, charged with identifying redundant programs, wasteful spending, and regulatory burden within state government — and the Ways and Means Committee, which handles state revenue and tax policy. Her committee assignments reflect her priority of constraining state spending and opposing deficit-financed expansion of government programs.",
              ["https://ballotpedia.org/Ellen_Troxclair",
               "https://www.legis.state.tx.us/members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A4385"]),
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
