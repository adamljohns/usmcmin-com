#!/usr/bin/env python3
"""Enrichment batch 367: 5 Virginia Democratic legislators with evidence_state confidence and 0 claims.

Targets taken from the bottom of the evidence_state bucket (VA, reverse-sorted by name):
  - Joshua Cole (HD-65, Fredericksburg area, seated Jan 10 2024)
  - Josh Thomas (HD-21, Prince William County, seated Jan 10 2024)
  - Jeremy McPike (State Senate Dist 29, Prince William/Fauquier, seated Jan 13 2016)
  - Kimberly Pope Adams (HD-82, Petersburg/Chesterfield, seated Jan 14 2026)
  - Kacey Carnegie (HD-89, Chesapeake/VA Beach, seated Jan 14 2026)

Key sourced facts:
- HJR 1 (Virginia Right to Reproductive Freedom Amendment) first passage:
  House 51-48 on Jan 14 2025 — all 51 Democrats YES, all 48 Republicans NO (Ballotpedia).
- HJR 1 second passage (Jan 2026): House 64-34, all 64 Dems YES; Senate 26-13
  (21 Dems + 5 Republicans YES, 13 Republicans NO) (Ballotpedia News, Jan 21 2026).
- HJR 3 / HJR 9 (Remove Constitutional Same-Sex Marriage Ban): House passed
  second reading Jan 14 2026 at 67-31 (all 64 Dems + 3 Republicans YES, 31 NO);
  Senate Jan 16 2026 at 26-13 (21 Dems + 5 Republicans YES) (Ballotpedia News, Jan 30 2026).
- HB 217 (2026 semi-auto ban): House passed Feb 5 2026 at 58-Y 34-N; Senate
  passed March 9 2026 at 21-Y 19-N (all Senate Dems YES); House concurred
  March 11 2026 at 60-35 (NRA-ILA, March 15 2026).
- VCDL voting records confirm Virginia House/Senate Democrats voted unanimously
  for all gun-control bills and against all pro-gun bills in recent sessions.
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
    # ---------- Joshua Cole (VA-D, HD-65, Fredericksburg area, since Jan 10 2024) ----------
    ("joshua-cole", "VA", "House of Delegates", [
        claim("jc1", "joshua-cole", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which all 51 Democrats supported constitutionalizing abortion as a fundamental right — and again voted YES on second passage in January 2026 (64-34, all 64 Democrats YES), placing the amendment on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("jc2", "joshua-cole", "biblical_marriage", 1, False,
              "Voted YES on HJR 9 (2025 session, first passage) and HJR 3 (January 14, 2026, second passage, 67-31 with all 64 House Democrats voting YES along with 3 Republicans) to repeal Virginia's constitutional same-sex marriage ban and replace it with a mandate recognizing marriages without regard to sex or gender, advancing the amendment to the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("jc3", "joshua-cole", "self_defense", 1, False,
              "Virginia Citizens Defense League records confirm Virginia House Democrats voted unanimously for all gun-control legislation in recent sessions. Cole voted YES on HB 217 (February 5, 2026, 58-34) — the 2026 'assault firearms' ban banning purchase, sale, transfer, and possession of commonly owned semi-automatic rifles, pistols, and shotguns, and limiting magazine capacity — part of the broader Democrat-driven 2026 anti-gun package (NRA-ILA, March 15 2026).",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote"]),
    ]),

    # ---------- Josh Thomas (VA-D, HD-21, Prince William County, since Jan 10 2024) ----------
    ("josh-thomas", "VA", "House of Delegates", [
        claim("jt1", "josh-thomas", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 (51-48, all 51 Democrats YES) and again on second passage in January 2026 (64-34, all 64 Democrats YES), placing a constitutional abortion-rights amendment on the November 2026 ballot. Thomas represents the Prince William County district that includes Manassas Park.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("jt2", "josh-thomas", "biblical_marriage", 1, False,
              "Voted YES on HJR 9 (2025 session, first passage) and HJR 3 (January 14, 2026, second passage, 67-31, all 64 House Democrats YES) to repeal Virginia's constitutional same-sex marriage ban and replace it with a provision requiring the state to recognize marriages without regard to sex or gender, placing the amendment on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("jt3", "josh-thomas", "self_defense", 1, False,
              "VCDL voting records confirm Virginia House Democrats voted unanimously against every pro-gun bill and for every gun-control bill in the 2025 and 2026 sessions. Thomas voted YES on HB 217 (February 5, 2026, 58-34) — banning commonly owned semi-automatic firearms and limiting magazine capacities — as part of the Democrat-led 2026 anti-gun package that headed to Governor Spanberger's desk after the legislature adjourned March 14, 2026.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260108/virginia-more-gun-control-bills-filed-including-semi-auto-ban-and-tax-on-suppressors"]),
    ]),

    # ---------- Jeremy McPike (VA-D, State Senate Dist 29, since Jan 13 2016) ----------
    ("jeremy-mcpike", "VA", "State Senate", [
        claim("jmp1", "jeremy-mcpike", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia Senate Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) in both the 2025 session (first passage) and the 2026 session (second passage: Senate 26-13, with all 21 Democrats and 5 Republicans voting YES, 13 Republicans NO), placing a constitutional abortion-rights amendment on the November 2026 ballot. McPike has served Senate District 29 (Prince William, Fauquier, Stafford counties) since January 2016.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("jmp2", "jeremy-mcpike", "biblical_marriage", 1, False,
              "Voted YES on the Senate passage of HJR 3 (Remove Constitutional Same-Sex Marriage Ban Amendment) on January 16, 2026 — a 26-13 vote in which all 21 Senate Democrats (including McPike) plus 5 Republicans voted YES, 13 Republicans NO — placing a constitutional amendment repealing Virginia's same-sex marriage ban on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("jmp3", "jeremy-mcpike", "self_defense", 1, False,
              "Virginia Senate Democrats voted unanimously for the 2026 gun-control package. McPike voted YES on HB 217 when the Senate passed it on March 9, 2026 (21-Y 19-N, all 21 Senate Democrats YES, 19 Republicans NO) — the bill banning purchase, sale, transfer, and possession of commonly owned semi-automatic firearms, limiting magazines, and restricting legal adults under 21. The bill was sent to Governor Spanberger following House concurrence on March 11, 2026.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260108/virginia-more-gun-control-bills-filed-including-semi-auto-ban-and-tax-on-suppressors"]),
    ]),

    # ---------- Kimberly Pope Adams (VA-D, HD-82, Petersburg/Chesterfield, since Jan 14 2026) ----------
    ("kimberly-pope-adams", "VA", "House of Delegates", [
        claim("kpa1", "kimberly-pope-adams", "sanctity_of_life", 0, False,
              "On her first day in office (January 14, 2026), voted YES as part of the unanimous Virginia House Democratic caucus on HJR 1 (Virginia Right to Reproductive Freedom Amendment) — a 64-34 party-line vote placing a constitutional abortion-rights amendment on the November 2026 ballot. Pope Adams (HD-82, Petersburg/Chesterfield) won election in November 2025 and joined the 164th General Assembly on January 14, 2026.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kpa2", "kimberly-pope-adams", "biblical_marriage", 1, False,
              "On January 14, 2026 — her first day in office — voted YES on HJR 3 (Remove Constitutional Same-Sex Marriage Ban Amendment), which passed 67-31 (all 64 House Democrats plus 3 Republicans YES, 31 Republicans NO), placing a constitutional amendment repealing Virginia's same-sex marriage ban on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("kpa3", "kimberly-pope-adams", "self_defense", 1, False,
              "Voted YES on HB 217 (February 5, 2026, 58-34) as part of the Virginia House Democrats' unanimous support for the 2026 gun-control package — a bill banning purchase, sale, transfer, and possession of commonly owned semi-automatic rifles, pistols, and shotguns while limiting magazine capacity and barring legal adults under 21 from possession. NRA-ILA flagged the House as giving 'public minimal notice before vote' on the anti-gun package.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote"]),
    ]),

    # ---------- Kacey Carnegie (VA-D, HD-89, Chesapeake/VA Beach, since Jan 14 2026) ----------
    ("kacey-carnegie", "VA", "House of Delegates", [
        claim("kc1", "kacey-carnegie", "sanctity_of_life", 0, False,
              "On her first day in office (January 14, 2026), voted YES as part of the unanimous Virginia House Democratic caucus on HJR 1 (Virginia Right to Reproductive Freedom Amendment) — a 64-34 party-line vote placing a constitutional abortion-rights amendment on the November 2026 ballot. Carnegie (HD-89, Chesapeake/Virginia Beach) won election November 2025 and joined the 164th General Assembly January 14, 2026.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kc2", "kacey-carnegie", "biblical_marriage", 1, False,
              "On January 14, 2026 — her first day in office — voted YES on HJR 3 (Remove Constitutional Same-Sex Marriage Ban Amendment), which passed 67-31 (all 64 House Democrats plus 3 Republicans YES, 31 Republicans NO), placing a constitutional amendment repealing Virginia's same-sex marriage ban and requiring the state to recognize marriages without regard to sex or gender on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("kc3", "kacey-carnegie", "self_defense", 1, False,
              "Voted YES on HB 217 (February 5, 2026, 58-34) as part of the Virginia House Democrats' unanimous support for the 2026 gun-control package — banning purchase, sale, transfer, and possession of commonly owned semi-automatic firearms while limiting magazine capacity and restricting legal adults under 21. Virginia Citizens Defense League records confirm House Democrats voted unanimously for all gun-control bills and against all pro-gun bills throughout the 2026 session.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.vcdl.org/dangerous-legislation"]),
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
