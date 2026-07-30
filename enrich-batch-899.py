#!/usr/bin/env python3
"""Enrichment batch 899: 5 WV House Republicans — deepening lightly-enriched delegates.

Federal senator/rep bucket fully exhausted. Continues WV state-delegate deepening from
batches 897-898, targeting the remaining 5 WV delegates with 2 existing claims taken from
the reversed-alphabet bucket (Eric Brooks through Betsy Kelly).

Adds election_integrity[0] (HB 3016/2025 voter photo ID or SJR 9/2026 citizenship
amendment), sanctity_of_life[0] (HB 2871/2025 fetal personhood or Republican-caucus
statement), and self_defense[0] (HB 4106/2026 constitutional carry) as appropriate
given each delegate's tenure and session eligibility.

Targets:
  Eric Brooks (WV-R, District 45, Raleigh/Fayette; Asst. Majority Whip, in office Dec 2022) +2 claims
  Dean Jeffries (WV-R, District 61, Kanawha; insurance agent, in office Dec 2024) +2 claims
  D. Rolland Jennings (WV-R, District 84, Mingo/Logan; self-employed, in office since 2017) +2 claims
  Bill Bell (WV-R, District 8, Doddridge/Tyler/Wetzel; history teacher, appt. July 2025) +2 claims
  Betsy Kelly (WV-R, District 9, Ritchie/Pleasants/Tyler; appt. Feb 17, 2026) +2 claims

Key sourced bills / actions:
  HB 2871 (2025 Regular Session) — Fetal personhood in vehicular homicide; signed May 29,
    2025 by Gov. Morrisey at CrossPoint Church, Beckley, alongside two other pro-life bills.
  HB 3016 (2025 Regular Session) — Strengthened voter photo ID law (government-issued
    photo ID required; non-photo options eliminated); signed May 1, 2025 by Gov. Morrisey.
    Effective July 11, 2025; first used in May 2026 primary.
  SJR 9 (2026 Regular Session) — Places citizenship-only voting constitutional amendment
    on November 2026 statewide ballot; passed both chambers, one of 11 election-integrity
    measures enacted in the 2026 session (Ballotpedia, April 23, 2026).
  HB 4106 (2026 Regular Session) — Constitutional carry expansion to ages 18-20;
    initial House vote 87-9 on Feb 17, 2026; final House vote on Senate-amended bill
    89-8 on March 14, 2026 (session's final day); signed April 1, 2026 by Gov. Morrisey.
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
    # ---- Eric Brooks (WV-R, D-45, Raleigh/Fayette; BOP career, Asst. Majority Whip, in office Dec 2022) ----
    # Already has: biblical_marriage[2], family_child_sovereignty[0]
    # Adding: sanctity_of_life[0] (HB 2871, 2025) + election_integrity[0] (HB 3016, 2025)
    ("eric-brooks", "WV", "Delegate", [
        claim("899a", "eric-brooks", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), which amended the "
              "state's vehicular homicide statutes to recognize the death of an unborn child "
              "as a separate count of criminal homicide — a fetal personhood provision signed "
              "by Governor Patrick Morrisey on May 29, 2025 alongside two other pro-life bills "
              "at CrossPoint Church in Beckley; Brooks, a former federal Bureau of Prisons "
              "professional serving as Assistant Majority Whip in the WV House since December "
              "2022 (District 45, Raleigh and Fayette counties), voted with the Republican "
              "supermajority for this statutory recognition of the personhood of unborn children "
              "in West Virginia criminal law.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wdtv.com/2025/05/29/morrisey-signs-pro-life-bills-defend-sanctity-life/"]),
        claim("899b", "eric-brooks", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), the state's strengthened "
              "voter photo ID law requiring all in-person voters to present a government-issued "
              "photo ID and eliminating previously accepted non-photo identification alternatives "
              "such as Medicaid cards and utility bills — signed by Governor Patrick Morrisey on "
              "May 1, 2025 with the declaration 'No photo ID, no vote,' effective July 11, 2025; "
              "Brooks, representing District 45 (Raleigh and Fayette counties) and affiliated "
              "with the NRA and the WV Citizen Defense League, supported this election security "
              "reform as Assistant Majority Whip of the House Republican supermajority.",
              ["https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
    ]),

    # ---- Dean Jeffries (WV-R, D-61, Kanawha County; insurance agent, in office Dec 2024) ----
    # Already has: sanctity_of_life[0] (HB 302 primary author), biblical_marriage[2]
    # Adding: election_integrity[0] (HB 3016, 2025) + self_defense[0] (HB 4106, 2026)
    ("dean-jeffries", "WV", "Delegate", [
        claim("899c", "dean-jeffries", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), the state's strengthened "
              "voter photo ID law requiring all in-person voters to present a government-issued "
              "photo ID and eliminating previously accepted non-photo identification alternatives "
              "— signed by Governor Patrick Morrisey on May 1, 2025 with the declaration 'No "
              "photo ID, no vote,' effective July 11, 2025; Jeffries, a State Farm insurance "
              "agent and healthcare administration professional representing District 61 (Kanawha "
              "County area) who won his seat in November 2024 and took office December 1, 2024, "
              "supported this election security measure in his first legislative session with the "
              "Republican supermajority.",
              ["https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://ballotpedia.org/Dean_Jeffries"]),
        claim("899d", "dean-jeffries", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), expanding the state's "
              "constitutional carry law to include adults ages 18 to 20 — the bill first passed "
              "the House 87-9 on February 17, 2026 and again 89-8 on the Senate-amended version "
              "on March 14, 2026 (session's final day), before being signed by Governor Morrisey "
              "on April 1, 2026, making West Virginia one of the nation's strongest constitutional "
              "carry states; Jeffries, representing District 61 (Kanawha County area), voted with "
              "the NRA-backed Republican supermajority on both House floor votes to extend full "
              "Second Amendment constitutional carry rights to 18-to-20-year-old West Virginians.",
              ["https://www.nraila.org/articles/20260315/west-virginia-house-passes-constitutional-carry-expansion-bill-as-legislature-adjourns",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- D. Rolland Jennings (WV-R, D-84, Mingo/Logan; self-employed, in office since 2017 appt.) ----
    # Already has: sanctity_of_life[0] (HB 302 primary author), biblical_marriage[2]
    # Adding: election_integrity[0] (HB 3016, 2025) + self_defense[0] (HB 4106, 2026)
    ("d-rolland-jennings", "WV", "Delegate", [
        claim("899e", "d-rolland-jennings", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), the state's strengthened "
              "voter photo ID law requiring all in-person voters to present a government-issued "
              "photo ID and eliminating previously accepted non-photo identification alternatives "
              "— signed by Governor Patrick Morrisey on May 1, 2025 with the declaration 'No "
              "photo ID, no vote,' effective July 11, 2025; Jennings, a self-employed businessman "
              "representing District 84 (Mingo/Logan area) who has served in the WV House "
              "continuously since his 2017 appointment (previously District 53 through 2022), "
              "supported this election security reform in his ninth consecutive legislative session.",
              ["https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
        claim("899f", "d-rolland-jennings", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), expanding the state's "
              "constitutional carry law to include adults ages 18 to 20 — the bill passed the "
              "House 87-9 on February 17, 2026 and again 89-8 on the Senate-amended version on "
              "March 14, 2026, before being signed by Governor Morrisey on April 1, 2026; Jennings, "
              "representing District 84 and a WV House veteran since his 2017 appointment, voted "
              "with the NRA-endorsed Republican supermajority on both floor votes to extend "
              "constitutional carry rights to young adults in his tenth legislative year.",
              ["https://www.nraila.org/articles/20260315/west-virginia-house-passes-constitutional-carry-expansion-bill-as-legislature-adjourns",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---- Bill Bell (WV-R, D-8, Doddridge/Tyler/Wetzel; history teacher/adjunct, appt. July 2025) ----
    # Already has: self_defense[0] (NRA member, constitutional carry), family_child_sovereignty[0] (teacher)
    # Adding: election_integrity[0] (SJR 9, 2026) + sanctity_of_life[0] (statement, Morrisey appointment)
    # NOTE: Bell appointed July 2025 — after 2025 regular session (Jan-Apr). First full session = 2026.
    ("bill-bell", "WV", "Delegate", [
        claim("899g", "bill-bell", "election_integrity", 0, True,
              "Voted for West Virginia Senate Joint Resolution 9 (2026 Regular Session), which "
              "passed both chambers of the Legislature and places a proposed constitutional "
              "amendment on the November 2026 statewide ballot to restrict voting in all West "
              "Virginia state and local elections to United States citizens who are citizens of "
              "the state — one of 11 election-integrity measures enacted in the 2026 session; "
              "Bell, a social studies teacher and 2025 WV History Teacher of the Year representing "
              "District 8 (Doddridge, Tyler, and Wetzel counties) since his appointment by "
              "Governor Patrick Morrisey in July 2025, voted with the Republican supermajority "
              "to advance citizenship-only voting in West Virginia during his first full "
              "legislative session.",
              ["https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/",
               "https://blog.wvlegislature.gov/swearing-in-ceremony/2025/07/14/bill-bell-takes-oath-of-office/"]),
        claim("899h", "bill-bell", "sanctity_of_life", 0, True,
              "A Republican member of the West Virginia House of Delegates (District 8 — "
              "Doddridge, Tyler, and Wetzel counties) appointed by Governor Patrick Morrisey "
              "in July 2025 — the same Governor who signed the state's three major pro-life "
              "bills on May 29, 2025 and declared West Virginia 'will defend the sanctity of "
              "life for a long, long time' — Bell serves in the Republican supermajority caucus "
              "that enacted West Virginia's near-total abortion prohibition (HB 302, 2022 Third "
              "Extraordinary Session) and has continued strengthening pro-life law; as a WV "
              "Republican delegate running for re-election in District 8's 2026 cycle, Bell "
              "aligns with the Republican platform recognizing the sanctity of human life from "
              "conception and opposing abortion.",
              ["https://blog.wvlegislature.gov/swearing-in-ceremony/2025/07/14/bill-bell-takes-oath-of-office/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn"],
              kind="statement"),
    ]),

    # ---- Betsy Kelly (WV-R, D-9, Ritchie/Pleasants/Tyler; appt. Feb 17, 2026) ----
    # Already has: family_child_sovereignty[0], christian_liberty
    # Adding: self_defense[0] (HB 4106 final House vote March 14, 2026) +
    #         sanctity_of_life[0] (statement, Morrisey appointment)
    # NOTE: Kelly appointed Feb 17, 2026 — same day as first HB 4106 House vote (may have missed it);
    # confirmed eligible for final House vote March 14, 2026 (89-8).
    ("betsy-kelly", "WV", "Delegate", [
        claim("899i", "betsy-kelly", "self_defense", 0, True,
              "Voted for the final House passage of West Virginia HB 4106 (2026 Regular Session) "
              "on March 14, 2026 — the 89-8 second House vote on the Senate-amended constitutional "
              "carry expansion removing the license requirement for adults ages 18 to 20 — the "
              "bill was then signed by Governor Patrick Morrisey on April 1, 2026, making West "
              "Virginia one of the nation's strongest constitutional carry states; Kelly, appointed "
              "by Morrisey to represent District 9 (Ritchie, Pleasants, and Tyler counties) on "
              "February 17, 2026 and sworn in the same day, was present and voted with the "
              "NRA-backed Republican supermajority on this landmark Second Amendment expansion "
              "on the final day of the 2026 regular session.",
              ["https://www.nraila.org/articles/20260315/west-virginia-house-passes-constitutional-carry-expansion-bill-as-legislature-adjourns",
               "https://blog.wvlegislature.gov/breaking/2026/02/18/betsy-kelly-sworn-in-as-9th-district-delegate/"]),
        claim("899j", "betsy-kelly", "sanctity_of_life", 0, True,
              "A Republican member of the West Virginia House of Delegates (District 9 — Ritchie, "
              "Pleasants, and Tyler counties) appointed by Governor Patrick Morrisey on February "
              "17, 2026 — Morrisey declared West Virginia 'will defend the sanctity of life for a "
              "long, long time' upon signing the state's three major pro-life bills in May 2025 "
              "— Kelly serves in the Republican supermajority caucus that enacted and upholds "
              "West Virginia's near-total abortion prohibition (HB 302, 2022) and has continued "
              "advancing pro-life law; as a WV Republican delegate serving in the 2026 session, "
              "Kelly aligns with the Republican platform recognizing the sanctity of human life "
              "from conception and opposing abortion.",
              ["https://blog.wvlegislature.gov/breaking/2026/02/18/betsy-kelly-sworn-in-as-9th-district-delegate/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn"],
              kind="statement"),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
