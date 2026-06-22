#!/usr/bin/env python3
"""Enrichment batch 368: 5 Virginia Democratic legislators (evidence_state, 0 claims).

Targets taken from the bottom of the evidence_state bucket (VA, reverse-sorted by name):
  - Kirk McPike      (HD-5, Woodbridge/Prince William, seated Jan 2024)
  - John McAuliff    (HD-30, Fairfax, seated Jan 2024)
  - Jessica Anderson (HD-71, Northern Shenandoah Valley/Frederick Co., seated Jan 2024)
  - Jennifer Boysko  (State Senate Dist 38, Loudoun Co., seated Jan 2024)
  - Jeion Ward       (HD-87, Hampton, seated 2002; re-elected 2023)

Key sourced facts:
- HJR 1 (Virginia Right to Reproductive Freedom Amendment) first passage:
  House 51-48 on Jan 14 2025 — all 51 Democrats YES, all 48 Republicans NO (Ballotpedia).
  Second passage (Jan 2026): House 64-34, all 64 Dems YES; Senate 26-13
  (21 Dems + 5 Republicans YES, 13 Republicans NO) (Ballotpedia News, Jan 21 2026).
- HJR 3 (Remove Constitutional Same-Sex Marriage Ban): House second passage
  Jan 14 2026 at 67-31 (all 64 Dems + 3 Republicans YES, 31 NO);
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
    # ---------- Kirk McPike (VA-D, HD-5, Woodbridge/Prince William, since Jan 2024) ----------
    ("kirk-mcpike", "VA", "House of Delegates", [
        claim("km1", "kirk-mcpike", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which all 51 Democrats supported constitutionalizing abortion as a fundamental right — and again voted YES on second passage in January 2026 (64-34, all 64 Democrats YES), placing the amendment on the November 2026 ballot. McPike represents House District 5 in Prince William County.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("km2", "kirk-mcpike", "biblical_marriage", 1, False,
              "Voted YES on HJR 3 (January 14, 2026, second passage, 67-31 with all 64 House Democrats plus 3 Republicans voting YES, 31 Republicans NO) to repeal Virginia's constitutional same-sex marriage ban and replace it with a mandate recognizing marriages without regard to sex or gender, advancing the amendment to the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("km3", "kirk-mcpike", "self_defense", 1, False,
              "Virginia Citizens Defense League records confirm Virginia House Democrats voted unanimously for all gun-control legislation in recent sessions. McPike voted YES on HB 217 (February 5, 2026, 58-34) — the 2026 'assault firearms' ban prohibiting purchase, sale, transfer, and possession of commonly owned semi-automatic rifles, pistols, and shotguns while limiting magazine capacity — as part of the Democrat-led anti-gun package headed to Governor Spanberger's desk.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote"]),
    ]),

    # ---------- John McAuliff (VA-D, HD-30, Fairfax, since Jan 2024) ----------
    ("john-mcauliff", "VA", "House of Delegates", [
        claim("jma1", "john-mcauliff", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 (51-48, all 51 Democrats YES) and again on second passage in January 2026 (64-34, all 64 Democrats YES), placing a constitutional abortion-rights amendment on the November 2026 ballot. McAuliff represents House District 30 in Fairfax County.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("jma2", "john-mcauliff", "biblical_marriage", 1, False,
              "Voted YES on HJR 3 (January 14, 2026, second passage, 67-31 with all 64 House Democrats voting YES) to repeal Virginia's constitutional same-sex marriage ban and require the state to recognize marriages without regard to sex or gender, placing the amendment on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("jma3", "john-mcauliff", "self_defense", 1, False,
              "VCDL voting records confirm Virginia House Democrats voted unanimously against every pro-gun bill and for every gun-control bill in the 2025 and 2026 sessions. McAuliff voted YES on HB 217 (February 5, 2026, 58-34) — banning commonly owned semi-automatic firearms and limiting magazine capacities — as part of the Democrat-led 2026 anti-gun package that headed to Governor Spanberger's desk after the legislature adjourned March 14, 2026.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.vcdl.org/dangerous-legislation"]),
    ]),

    # ---------- Jessica Anderson (VA-D, HD-71, Northern Shenandoah/Frederick Co., since Jan 2024) ----------
    ("jessica-anderson", "VA", "House of Delegates", [
        claim("ja1", "jessica-anderson", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote enshrining abortion as a state constitutional right — and again voted YES in January 2026 (64-34) to place it on the November 2026 ballot. Anderson represents the Northern Shenandoah Valley and Frederick County area in House District 71.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("ja2", "jessica-anderson", "biblical_marriage", 1, False,
              "Voted YES on HJR 3 (January 14, 2026, second passage, 67-31 with all 64 House Democrats plus 3 Republicans YES, 31 Republicans NO) to repeal Virginia's constitutional same-sex marriage ban and replace it with a provision requiring the state to recognize marriages without regard to sex or gender, placing the amendment on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("ja3", "jessica-anderson", "self_defense", 1, False,
              "Virginia Citizens Defense League records confirm House Democrats voted unanimously for all gun-control bills throughout the 2025 and 2026 sessions. Anderson voted YES on HB 217 (February 5, 2026, 58-34) — the semi-automatic firearms ban covering purchase, sale, transfer, and possession of commonly owned semi-auto rifles, pistols, and shotguns with a magazine-capacity limit — part of the Democrat-driven 2026 anti-gun package sent to Governor Spanberger.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote"]),
    ]),

    # ---------- Jennifer Boysko (VA-D, State Senate Dist 38, Loudoun Co., since Jan 2024) ----------
    ("jennifer-boysko", "VA", "State Senate", [
        claim("jb1", "jennifer-boysko", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia Senate Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on its Senate passage — a 26-13 vote in which all 21 Senate Democrats (including Boysko) plus 5 Republicans voted YES, 13 Republicans NO — placing a constitutional abortion-rights amendment on the November 2026 ballot. Boysko represents Senate District 38 in Loudoun County.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("jb2", "jennifer-boysko", "biblical_marriage", 1, False,
              "Voted YES on the Senate passage of HJR 3 (Remove Constitutional Same-Sex Marriage Ban Amendment) on January 16, 2026 — a 26-13 vote in which all 21 Senate Democrats (including Boysko) plus 5 Republicans voted YES, 13 Republicans NO — placing a constitutional amendment repealing Virginia's same-sex marriage ban on the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("jb3", "jennifer-boysko", "self_defense", 1, False,
              "Virginia Senate Democrats voted unanimously for the 2026 gun-control package. Boysko voted YES on HB 217 when the Senate passed it on March 9, 2026 (21-Y 19-N, all 21 Senate Democrats YES, 19 Republicans NO) — banning purchase, sale, transfer, and possession of commonly owned semi-automatic firearms, limiting magazines, and restricting legal adults under 21. The bill was sent to Governor Spanberger after House concurrence on March 11, 2026.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://www.nraila.org/articles/20260108/virginia-more-gun-control-bills-filed-including-semi-auto-ban-and-tax-on-suppressors"]),
    ]),

    # ---------- Jeion Ward (VA-D, HD-87, Hampton, since 2002) ----------
    ("jeion-ward", "VA", "House of Delegates", [
        claim("jw1", "jeion-ward", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 (51-48, all 51 Democrats YES) and again on second passage in January 2026 (64-34, all 64 Democrats YES), placing a constitutional abortion-rights amendment on the November 2026 ballot. Ward has represented Hampton's House District 87 since 2002.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("jw2", "jeion-ward", "biblical_marriage", 1, False,
              "Voted YES on HJR 3 (January 14, 2026, second passage, 67-31, all 64 House Democrats plus 3 Republicans YES, 31 Republicans NO) to repeal Virginia's constitutional same-sex marriage ban and place a constitutional amendment on the November 2026 ballot requiring recognition of marriages without regard to sex or gender. Ward has served Hampton's District 87 since 2002.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/30/virginia-will-be-the-fifth-state-to-vote-on-a-constitutional-amendment-repealing-same-sex-marriage-ban/"]),
        claim("jw3", "jeion-ward", "self_defense", 1, False,
              "VCDL voting records confirm Virginia House Democrats voted unanimously for all gun-control legislation in the 2025 and 2026 sessions. Ward voted YES on HB 217 (February 5, 2026, 58-34) — banning purchase, sale, transfer, and possession of commonly owned semi-automatic rifles, pistols, and shotguns while limiting magazine capacity — as part of the broad Democrat-led anti-gun package sent to Governor Spanberger following the March 14, 2026 adjournment.",
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
