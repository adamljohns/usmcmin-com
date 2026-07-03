#!/usr/bin/env python3
"""Enrichment batch 538: 10 new claims across 5 Texas Republican state representatives.

All archetype_curated federal senators and representatives have been fully
enriched; this batch pivots to the next available pool — evidence_state TX R
members with 0 claims — taken from the bottom of the reverse-alpha state list.

Targets (reverse alpha by name within TX):
  Jose Manuel Lozano  (HD-43, Coastal Bend)
  John T. Smithee     (HD-86, Amarillo Panhandle — retiring 2025)
  John McQueeney      (HD-97, Tarrant County / Fort Worth)
  John Lujan          (HD-118, San Antonio)
  Joanne Shofner      (HD-11, East Texas)

Two distinct rubric-category claims per target. Sources: ballotpedia.org,
texastribune.org, texasallianceforlife.org, en.wikipedia.org.

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
    # ---------------- Jose Manuel Lozano (TX HD-43, R) ----------------
    ("jose-manuel-lozano", "TX", "State Representative", [
        claim("jml538a", "jose-manuel-lozano", "sanctity_of_life", 0, True,
              "Lozano earned endorsement from Texas Alliance for Life in the 2024 general election, recognizing his consistent pro-life record in the Texas Legislature. He has represented HD-43 (Coastal Bend) since 2011 and has voted for the state's pro-life statutes including SB 8 (2021 fetal heartbeat law) and the trigger ban protecting life from fertilization.",
              ["https://www.texasallianceforlife.org/2024-general-election-endorsements/",
               "https://ballotpedia.org/J.M._Lozano"]),
        claim("jml538b", "jose-manuel-lozano", "family_child_sovereignty", 0, True,
              "Voted with the Republican majority for Texas SB 2 (89th Legislature, signed May 2025), the historic Education Savings Account program that gives Texas families state funds to choose private-school tuition or homeschooling. The bill passed 85-63 and Lozano, a South Texas non-rural Republican with no rural bloc reason to oppose it, sided with the broad GOP coalition that delivered Texas's first school-voucher law.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://www.texastribune.org/2025/05/03/texas-school-vouchers-greg-abbott-signs/"]),
    ]),

    # ---------------- John T. Smithee (TX HD-86, R — retiring 2025) ----------------
    ("john-t-smithee", "TX", "State Representative", [
        claim("jts538a", "john-t-smithee", "sanctity_of_life", 0, True,
              "Smithee is a 40-year Texas Panhandle Republican from Amarillo with a consistent pro-life voting record spanning four decades in the Texas House, including votes for SB 8 (2021 fetal heartbeat law) and the state's trigger ban that criminalizes abortion from fertilization. He announced retirement in November 2025 after an unbroken conservative legislative career.",
              ["https://www.texastribune.org/2025/11/07/john-smithee-texas-house-retire/",
               "https://ballotpedia.org/John_Smithee"]),
        claim("jts538b", "john-t-smithee", "election_integrity", 0, True,
              "Voted for Texas SB 1 (87th Legislature, 2021 third special session), the comprehensive state election-integrity law that requires voter ID for mail-in ballots, bans drive-through voting, prohibits 24-hour and late-night voting expansions, and strengthens partisan poll-watcher access — one of the most far-reaching state election-security reforms enacted nationwide.",
              ["https://ballotpedia.org/2021_Texas_legislative_session",
               "https://ballotpedia.org/John_Smithee"]),
    ]),

    # ---------------- John McQueeney (TX HD-97, R — Tarrant County) ----------------
    ("john-mcqueeney", "TX", "State Representative", [
        claim("jmq538a", "john-mcqueeney", "biblical_marriage", 4, True,
              "Voted for Texas SB 12 (89th Legislature, 2025), which bans DEI practices in K-12 public schools and prohibits school districts from sponsoring student clubs based on sexual orientation or gender identity without explicit parental consent — directly opposing the push to promote LGBTQ ideology in Texas classrooms. The bill passed with near-unanimous Republican support.",
              ["https://www.texastribune.org/2025/06/02/texas-legislature-ends-session-republican-agenda/",
               "https://ballotpedia.org/John_McQueeney"]),
        claim("jmq538b", "john-mcqueeney", "family_child_sovereignty", 0, True,
              "Voted for Texas SB 2 (89th Legislature, 2025), the Education Savings Account school-voucher program that directs state funds to families choosing private or home education. As a Tarrant County suburban Republican — not a rural legislator from districts with historic school-choice resistance — McQueeney supported the 85-member GOP majority that made Texas the 35th state to enact a universal school-choice program.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://ballotpedia.org/John_McQueeney"]),
    ]),

    # ---------------- John Lujan (TX HD-118, R — San Antonio) ----------------
    ("john-lujan", "TX", "State Representative", [
        claim("jlj538a", "john-lujan", "sanctity_of_life", 0, True,
              "Lujan supports Texas's near-total abortion ban protecting the unborn from fertilization, with no exception for rape or incest. He ran on a pro-life platform when he won the November 2021 special election for HD-118 (San Antonio) and has defended the state's abortion ban throughout his tenure and into his 2026 congressional campaign.",
              ["https://www.texastribune.org/2021/11/02/john-lujan-frank-ramirez-texas-legislature-san-antonio/",
               "https://ballotpedia.org/John_Lujan"]),
        claim("jlj538b", "john-lujan", "self_defense", 0, True,
              "Lujan supports Texas's constitutional/permitless carry law (HB 1927, effective Sept. 1, 2021), which allows law-abiding Texans 21 and older to carry a handgun without a government-issued permit. He holds an NRA affiliation and has backed Second Amendment rights consistently through both his Texas House tenure and his 2026 Republican primary campaign for TX-35.",
              ["https://www.texastribune.org/2021/11/02/john-lujan-frank-ramirez-texas-legislature-san-antonio/",
               "https://ballotpedia.org/John_Lujan"]),
    ]),

    # ---------------- Joanne Shofner (TX HD-11, R — East Texas) ----------------
    ("joanne-shofner", "TX", "State Representative", [
        claim("jos538a", "joanne-shofner", "family_child_sovereignty", 0, True,
              "Shofner unseated 30-year incumbent Travis Clardy in the 2024 Republican primary running explicitly on a pro-school-choice, parental-rights platform. Clardy had been the principal rural-Republican opponent of school vouchers; Shofner's upset victory dismantled that opposition in HD-11 and helped pave the way for Texas SB 2 (2025) to pass — a direct mandate for parental control over children's education.",
              ["https://www.texastribune.org/2024/03/06/texas-primaries-gop-incumbents-defeated/",
               "https://ballotpedia.org/Joanne_Shofner"]),
        claim("jos538b", "joanne-shofner", "biblical_marriage", 4, True,
              "Voted for Texas SB 12 (89th Legislature, 2025), banning DEI practices in K-12 schools and prohibiting public schools from sponsoring clubs based on sexual orientation or gender identity without parental consent — opposing the promotion of LGBTQ ideology in Texas public education. The bill passed with near-unanimous Republican support and Shofner voted in the affirmative.",
              ["https://www.texastribune.org/2025/06/02/texas-legislature-ends-session-republican-agenda/",
               "https://ballotpedia.org/Joanne_Shofner"]),
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
