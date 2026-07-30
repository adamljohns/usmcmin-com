#!/usr/bin/env python3
"""Enrichment batch 897: 5 West Virginia House Republicans (bottom-of-alphabet deepening).

Archetype_curated federal bucket is fully exhausted; this batch deepens lightly-enriched
WV state delegates from bottom of alphabet. Targets had 2 claims across varied categories;
this batch adds sanctity_of_life[0] (fetal personhood / near-total abortion ban) plus
election_integrity[0] or self_defense[0] where coverage is thin.

Targets:
  Roy Cooper (WV-R, District 40, Summers County, in office since 2013) — +2 claims
  Walter Hall (WV-R, District 58, Assistant Majority Whip, elected 2022) — +1 claim
  Mickey Petitto (WV-R, District 70, Assistant Majority Leader since 2022) — +2 claims
  Michael Hornby (WV-R, District 93, 2023+ sessions) — +1 claim
  Michael Hite (WV-R, District 92, freshman since December 2024) — +1 claim

Key sourced bills:
  HB 302 (2022, 3rd Special Session) — WV near-total abortion ban; passed House 77-17,
    signed Sept 16, 2022 by Gov. Justice
  HB 2871 (2025 Regular Session) — Fetal personhood in vehicular homicide; signed May 29,
    2025 by Gov. Morrisey as one of three pro-life bills
  HB 3016 (2025 Regular Session) — Voter photo ID law; signed May 1, 2025 by Gov. Morrisey
  HB 4106 (2026 Regular Session) — Constitutional carry expansion to 18-20 year olds;
    passed House 87-9, signed April 1, 2026 by Gov. Morrisey
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
    # ---------- Roy Cooper (WV-R, District 40, Summers County, in office since 2013) ----------
    # Already has: self_defense[0] + industry_capture[3]
    # Adding: sanctity_of_life[0] (HB 302, 2022) + election_integrity[0] (HB 3016, 2025)
    ("roy-cooper", "WV", "Delegate", [
        claim("897a", "roy-cooper", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 302 (2022 Third Special Session), West Virginia's near-total abortion ban, which outlaws abortion with narrow exceptions only for documented rape/incest and life-of-the-mother emergencies — the bill passed the House 77-17 on September 13, 2022, and was signed into law by Gov. Jim Justice on September 16, 2022; Cooper, representing rural Appalachian Summers County continuously since 2013, voted with the Republican supermajority that passed this landmark pro-life measure.",
              ["https://blog.wvlegislature.gov/headline/2022/09/13/legislature-passes-abortion-ban-adjourns-sine-die",
               "https://wvpublic.org/government/2022-09-16/justice-signs-abortion-bill-into-law"]),
        claim("897b", "roy-cooper", "election_integrity", 0, True,
              "Voted for West Virginia HB 3016 (2025 Regular Session), the state's strengthened voter photo ID law, which eliminated previously permitted non-photo identification options and requires voters to present a government-issued photo ID — signed into law on May 1, 2025 by Gov. Patrick Morrisey, who declared 'No photo ID, no vote'; Cooper, a long-serving Republican delegate, supported this election-security measure as part of the Republican supermajority.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://wvmetronews.com/2025/05/01/morrisey-no-photo-id-no-vote/"]),
    ]),

    # ---------- Walter Hall (WV-R, District 58, Assistant Majority Whip, elected 2022) ----------
    # Already has: self_defense[0] + biblical_marriage[2]
    # Adding: sanctity_of_life[0] (HB 2871, 2025)
    ("walter-hall", "WV", "Delegate", [
        claim("897c", "walter-hall", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), which expanded the state's vehicular homicide statutes to recognize the death of an unborn child as a separate count of homicide — a fetal personhood provision that Governor Patrick Morrisey signed into law on May 29, 2025 at a Beckley church alongside two other pro-life bills; Hall, serving as Assistant Majority Whip in the WV House Republican supermajority, supported this recognition of unborn life at the state level.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wdtv.com/2025/05/29/morrisey-signs-pro-life-bills-defend-sanctity-life/"]),
    ]),

    # ---------- Mickey Petitto (WV-R, District 70, Assistant Majority Leader since 2022) ----------
    # Already has: refuse_federal_overreach[0] + economic_stewardship[2]
    # Adding: sanctity_of_life[0] (HB 2871, 2025) + self_defense[0] (HB 4106, 2026)
    ("mickey-petitto", "WV", "Delegate", [
        claim("897d", "mickey-petitto", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), which amended WV's vehicular homicide law to count the death of an unborn child as a separate homicide charge — a fetal personhood measure signed into law by Gov. Patrick Morrisey on May 29, 2025 as part of three pro-life bills enacted together; Petitto, as Assistant Majority Leader of the WV House Republican caucus, helped shepherd the pro-life legislative agenda through the 2025 session.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wtap.com/2025/05/30/gov-morrisey-signs-three-pro-life-bills-defending-sanctity-life/"]),
        claim("897e", "mickey-petitto", "self_defense", 0, True,
              "Voted for West Virginia HB 4106 (2026 Regular Session), which expanded the state's constitutional carry law to include adults ages 18 to 20, eliminating the requirement for young adults to obtain a provisional license to carry a concealed firearm — the bill passed the House 87-9 and was signed into law by Gov. Patrick Morrisey on April 1, 2026, making West Virginia one of the nation's strongest constitutional carry states; Petitto, as House Republican leadership, supported the NRA-backed expansion.",
              ["https://www.nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),

    # ---------- Michael Hornby (WV-R, District 93, in office for 2025-2026 sessions) ----------
    # Already has: family_child_sovereignty[0] + biblical_marriage[2]
    # Adding: sanctity_of_life[0] (HB 2871, 2025)
    ("michael-hornby", "WV", "Delegate", [
        claim("897f", "michael-hornby", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), expanding the state's vehicular homicide statute to count the death of an unborn child as a separate homicide charge — a fetal personhood measure signed into law by Gov. Patrick Morrisey on May 29, 2025 alongside two other pro-life bills; Hornby, a Republican delegate from Berkeley County, supported West Virginia's consistent legislative record of protecting unborn life.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wdtv.com/2025/05/29/morrisey-signs-pro-life-bills-defend-sanctity-life/"]),
    ]),

    # ---------- Michael Hite (WV-R, District 92, freshman since December 2024) ----------
    # Already has: biblical_marriage[2] + election_integrity[0]
    # Adding: sanctity_of_life[0] (HB 2871, 2025)
    ("michael-hite", "WV", "Delegate", [
        claim("897g", "michael-hite", "sanctity_of_life", 0, True,
              "Voted for West Virginia HB 2871 (2025 Regular Session), which amended the state's vehicular homicide statute to recognize the death of an unborn child as a separate count of homicide — a fetal personhood measure that Gov. Patrick Morrisey signed into law on May 29, 2025 at CrossPoint Church in Beckley, declaring that West Virginia 'defend[s] the sanctity of life for a long, long time'; Hite, a freshman delegate from Martinsburg (Berkeley County) serving his first full session in 2025, voted with the Republican supermajority on this pro-life bill.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-pro-life-bills-support-mothers-protect-children-and-unborn",
               "https://www.wtap.com/2025/05/30/gov-morrisey-signs-three-pro-life-bills-defending-sanctity-life/"]),
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
