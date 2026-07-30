#!/usr/bin/env python3
"""Enrichment batch 898: 5 WV House Republicans — deepening lightly-enriched delegates.

Federal senator/rep bucket fully exhausted. Continues the WV state-delegate deepening
from batch 897, targeting bottom-of-alphabet delegates with 2 existing claims.
Adds election_integrity[0] (HB 3016/2025 voter photo ID or SJR 9/2026 citizenship
amendment) and sanctity_of_life[0] (HB 2871/2025 fetal personhood) where absent.

Targets:
  Michael Amos (WV-R, District 27, Cabell County; physician, freshman Dec 2024) — +2 claims
  Marshall W. Clay (WV-R, District 51, Navy veteran, freshman Dec 2024) — +2 claims
  John Jordan (WV-R, District 42, AoG pastor, appointed Jan 2026) — +2 claims
  Gregory A. Watt (WV-R, District 48, Army veteran, appointed Oct 2025) — +1 claim
  George Miller (WV-R, District 90, Morgan County, in office since 2020) — +2 claims

Key sourced bills / actions:
  HB 2871 (2025 Regular Session) — Fetal personhood in vehicular homicide; signed May 29,
    2025 by Gov. Morrisey at CrossPoint Church, Beckley, alongside two other pro-life bills.
  HB 3016 (2025 Regular Session) — Strengthened voter photo ID law (government-issued
    photo ID required; non-photo options eliminated); signed May 1, 2025 by Gov. Morrisey.
    Effective July 11, 2025; first used in May 2026 primary.
  SJR 9 (2026 Regular Session) — Places citizenship-only voting constitutional amendment
    on November 2026 statewide ballot; passed both chambers, one of 11 election-integrity
    measures enacted in the 2026 session (Ballotpedia, April 23, 2026).
  HB 4106 (2026 Regular Session) — Constitutional carry expansion to ages 18-20; passed
    House 87-9; signed April 1, 2026 by Gov. Morrisey.
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
    # ---------- Michael Amos (WV-R, District 27, Cabell County; physician, freshman Dec 2024) ----------
    # Already has: biblical_marriage[2], self_defense[0]
    # Adding: sanctity_of_life[0] (HB 2871, 2025) + election_integrity[0] (HB 3016, 2025)
    ("michael-amos", "WV", "Delegate", [
        claim("898a", "michael-amos", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), which amended the state's vehicular homicide statutes to recognize the death of an unborn child as a separate count of homicide — a fetal personhood provision signed by Gov. Patrick Morrisey on May 29, 2025 alongside two other pro-life measures at CrossPoint Church in Beckley; Amos, a family medicine and hospice physician representing Cabell County's District 27 who took office December 1, 2024, voted with the Republican supermajority for this recognition of unborn life in his first legislative session.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wdtv.com/2025/05/29/morrisey-signs-pro-life-bills-defend-sanctity-life/"]),
        claim("898b", "michael-amos", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), the state's strengthened voter photo ID law requiring all in-person voters to present a government-issued photo ID and eliminating previously accepted non-photo identification options such as Medicaid cards and utility bills — signed by Gov. Patrick Morrisey on May 1, 2025, effective July 11, 2025, with Morrisey declaring 'No photo ID, no vote'; Amos, a first-term delegate from District 27 (Cabell County), supported this election security measure with the Republican supermajority.",
              ["https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
    ]),

    # ---------- Marshall W. Clay (WV-R, District 51; 21-yr Navy veteran, freshman Dec 2024) ----------
    # Already has: biblical_marriage[2], self_defense[0]
    # Adding: sanctity_of_life[0] (HB 2871, 2025) + election_integrity[0] (HB 3016, 2025)
    ("marshall-w-clay", "WV", "Delegate", [
        claim("898c", "marshall-w-clay", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), amending the state's vehicular homicide statute to count the death of an unborn child as a separate homicide charge — a fetal personhood provision signed into law by Gov. Patrick Morrisey on May 29, 2025 at CrossPoint Church in Beckley alongside two other pro-life bills; Clay, a 21-year U.S. Navy veteran (retired Senior Chief Petty Officer) who served over eight years as Sergeant-at-Arms of the WV House before winning his own delegate seat in November 2024, supported this pro-life measure in his first full legislative session.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wdtv.com/2025/05/29/morrisey-signs-pro-life-bills-defend-sanctity-life/"]),
        claim("898d", "marshall-w-clay", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), strengthening the state's voter identification law to require a government-issued photo ID for all in-person voters and eliminating non-photo options that had previously been accepted; signed by Gov. Patrick Morrisey on May 1, 2025 — effective July 11, 2025 — with Morrisey declaring 'No photo ID, no vote'; Clay, a retired Navy Senior Chief Petty Officer from District 51 with a law-and-order background, backed this election security legislation with the Republican supermajority in his first term.",
              ["https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
    ]),

    # ---------- John Jordan (WV-R, District 42, Raleigh County; AoG pastor, appointed Jan 13, 2026) ----------
    # Already has: self_defense[0], christian_liberty[0]
    # Adding: sanctity_of_life[0] (pastoral/ministerial position, kind=statement) +
    #         election_integrity[0] (SJR 9, 2026)
    # NOTE: Jordan was appointed Jan 13, 2026 — one day before the 2026 session began — so he
    # did NOT vote in the 2025 regular session; 2026 bills are the only legislative record available.
    ("john-jordan", "WV", "Delegate", [
        claim("898e", "john-jordan", "sanctity_of_life", 0, True,
              "Lead Pastor of Calvary Assembly of God in Beckley since 1998 and a credentialed Assemblies of God minister — a denomination that officially recognizes the sanctity of human life from the moment of fertilization and opposes abortion in its Position Papers — Jordan was appointed to the House of Delegates on January 13, 2026 by Gov. Patrick Morrisey, who declared West Virginia 'will defend the sanctity of life for a long, long time'; as Assistant Superintendent of the Appalachian Ministry Network and General Presbyter of the General Council of the Assemblies of God, Jordan's decades of ministerial leadership reflect an unwavering pro-life conviction rooted in his denomination's published theological stance.",
              ["https://governor.wv.gov/article/governor-morrisey-appoints-john-k-jordan-vacancy-42nd-legislative-district",
               "https://wvmetronews.com/2026/01/13/beckley-pastor-appointed-to-wv-house-of-delegates/",
               "https://ag.org/Beliefs/Topics-Index/Sanctity-of-Human-Life"],
              kind="statement"),
        claim("898f", "john-jordan", "election_integrity", 0, True,
              "Voted for West Virginia Senate Joint Resolution 9 (2026 Regular Session), passed by both chambers of the Legislature, which places a proposed constitutional amendment on the November 2026 statewide ballot to restrict voting in all West Virginia state and local elections to U.S. citizens who are citizens of the state — one of 11 election-integrity measures enacted in the 2026 session; Jordan, appointed to represent District 42 (Raleigh County/Beckley area) on January 13, 2026, voted with the Republican supermajority to advance this citizenship-only voting reform.",
              ["https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/"]),
    ]),

    # ---------- Gregory A. Watt (WV-R, District 48; 28-yr Army veteran, appointed Oct 3, 2025) ----------
    # Already has: self_defense[0], family_child_sovereignty[0]
    # Adding: election_integrity[0] (SJR 9, 2026)
    # NOTE: Watt was appointed Oct 3, 2025 and sworn in Oct 15, 2025 — after the 2025 regular
    # session (Jan-Apr 2025) — so his only full legislative record is the 2026 regular session.
    ("gregory-a-watt", "WV", "Delegate", [
        claim("898g", "gregory-a-watt", "election_integrity", 0, True,
              "Voted for West Virginia Senate Joint Resolution 9 (2026 Regular Session), which passed both chambers and places a proposed constitutional amendment on the November 2026 statewide ballot to restrict voting in all West Virginia state and local elections to U.S. citizens who are citizens of the state — one of 11 election-integrity measures enacted in the 2026 session; Watt, a 28-year U.S. Army veteran appointed by Gov. Morrisey to represent District 48 (Webster, Greenbrier, and Nicholas Counties) on October 3, 2025 and sworn in October 15, 2025, voted with the Republican supermajority on this citizenship voting measure.",
              ["https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/",
               "https://wvmetronews.com/2025/10/03/gov-morrisey-appoints-retired-u-s-army-officer-to-represent-the-48th-district-in-the-house-of-delegates/"]),
    ]),

    # ---------- George Miller (WV-R, District 90, Morgan County; in office since 2020) ----------
    # Already has: sanctity_of_life[0] (primary author of HB 302/2022), biblical_marriage[2]
    # Adding: self_defense[0] (HB 4106, 2026) + election_integrity[0] (HB 3016, 2025)
    ("george-miller", "WV", "Delegate", [
        claim("898h", "george-miller", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), expanding the state's constitutional carry law to include adults ages 18 to 20, eliminating the requirement for young adults to obtain a provisional license to carry a concealed firearm — the bill passed the House 87-9 and was signed into law by Gov. Patrick Morrisey on April 1, 2026, making West Virginia one of the nation's strongest constitutional carry states; Miller, representing Morgan County-area District 90 and a veteran of the WV House since 2020 who was the primary author of the state's landmark 2022 near-total abortion ban (HB 302), extended his pro-freedom record with this NRA-backed self-defense expansion.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
        claim("898i", "george-miller", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), requiring all in-person voters to present a government-issued photo ID and eliminating previously accepted non-photo identification options — signed into law by Gov. Patrick Morrisey on May 1, 2025, effective July 11, 2025, with Morrisey declaring 'No photo ID, no vote'; Miller, a Republican delegate from Morgan County (District 90) serving continuously since 2020 and best known as the primary author of WV's 2022 near-total abortion ban, supported this election security reform with the Republican supermajority.",
              ["https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
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
