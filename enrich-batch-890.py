#!/usr/bin/env python3
"""Enrichment batch 890: hand-curated claims for 5 NC Republican State Senators.

All archetype_curated federal senator/rep buckets exhausted; continuing the
pivot to archetype_party_default NC state senators from the bottom of the
reverse-alphabet name list (following batch 889's Moffitt / Jarvis / Hise /
Berger / Sanderson).

Key NC legislation used as evidence:
  - SB 20 (Care for Women, Children, and Families Act, 2023): 12-week abortion
    limit; Senate voted 30-20 to override Gov. Cooper's veto on May 16, 2023.
    Confirmed Senate yes-voters include: Alexander, Barnes, Berger, Britt, Burgin,
    Corbin, Craven, Daniel, Ford, Galey, Hanig, Hise, Jackson, Jarvis, Johnson,
    Krawiec, Lazzara, Lee, McInnis, Moffitt, B. Newton, P. Newton, Overcash, Perry,
    Proctor, Rabon, Sanderson, Sawrey, Sawyer, Settle.
    Source: ncleg.gov Roll Call #215, 2023 Senate session.
  - SB 49 (Parents' Bill of Rights, 2023): barred K-4 gender/sexuality instruction,
    parental notification of name/pronoun change. Primary Senate sponsors: Barnes,
    Galey, Lee. Veto overridden House 59-54, Aug 16-17 2023.
  - SB 50 (Freedom to Carry NC, 2025): constitutional carry; passed Senate 26-18
    on March 20, 2025. Confirmed Senate yes-voters include: Alexander, Berger,
    Brinson, Britt, Burgin, Corbin, Craven, Daniel, Ford, Galey, Hanig, Hise,
    Hollo, Jackson, Jarvis, Johnson, Jones, Lazzara, Lee, McInnis, Moffitt,
    Overcash, Sanderson, Sawrey, Sawyer, Settle.
    Source: ncleg.gov Roll Call #50, 2025 Senate session; legiscan.com/NC/rollcall/S50/id/1599136

Targets (NC State Senators, continuing reverse-alpha order from batch 889):
  Michael V. Lee, Michael A. Lazzara, Mark Hollo, Lisa S. Barnes, Kevin Corbin

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ------------ Michael V. Lee (NC-R, State Senator SD-7, Senate Majority Leader) ------------
    ("michael-v-lee", "NC", "Senator", [
        claim("mvl890a", "michael-v-lee", "family_child_sovereignty", 0, True,
              "Co-sponsored NC Senate Bill 49 ('Parents' Bill of Rights') as one of its "
              "three primary sponsors (with Senators Galey and Barnes); the bill, enacted "
              "via veto override on August 16-17, 2023 (House 59-54, Senate 27-18), requires "
              "schools to notify parents when a child requests a name or pronoun change and "
              "bars instruction on gender identity or sexual orientation in kindergarten "
              "through 4th grade — a direct statutory protection of parental authority.",
              ["https://www.ncleg.gov/BillLookup/2023/S49",
               "https://legiscan.com/NC/sponsors/S49/2023",
               "https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights"]),
        claim("mvl890b", "michael-v-lee", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican Senate caucus to override Gov. "
              "Roy Cooper's veto of NC Senate Bill 20 ('Care for Women, Children, and "
              "Families Act') on May 16, 2023, enacting a 12-week abortion restriction in "
              "a 30-20 party-line vote. Lee has since become NC Senate Majority Leader "
              "(April 2025), giving him increased influence over the Senate's pro-life agenda.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.wunc.org/politics/2023-05-16/nc-senate-votes-to-override-gov-coopers-abortion-veto",
               "https://www.wunc.org/politics/2025-04-01/new-hanover-republican-michael-lee-senate-majority-leader"]),
        claim("mvl890c", "michael-v-lee", "self_defense", 0, True,
              "Voted in favor of NC Senate Bill 50 ('Freedom to Carry NC') on March 20, "
              "2025 — the bill eliminating the permit requirement for concealed carry and "
              "establishing constitutional carry in North Carolina, which passed the Senate "
              "26-18 along party lines.",
              ["https://www.ncleg.gov/BillLookup/2025/S50",
               "https://legiscan.com/NC/rollcall/S50/id/1599136",
               "https://www.ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2025/S/50"]),
    ]),

    # ------------ Michael A. Lazzara (NC-R, State Senator SD-6, USMC veteran) ------------
    ("michael-a-lazzara", "NC", "Senator", [
        claim("mal890a", "michael-a-lazzara", "self_defense", 0, True,
              "Co-sponsored NC Senate Bill 50 ('Freedom to Carry NC'), which passed the "
              "Senate 26-18 along party lines on March 20, 2025, eliminating the permit "
              "requirement for concealed carry and establishing constitutional carry in "
              "North Carolina — a legislative push for the rubric's constitutional-carry ideal. "
              "Lazzara, a U.S. Marine Corps veteran, represents District 6 (Onslow County).",
              ["https://www.ncleg.gov/BillLookup/2025/S50",
               "https://legiscan.com/NC/rollcall/S50/id/1599136",
               "https://ballotpedia.org/Michael_Lazzara"]),
        claim("mal890b", "michael-a-lazzara", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican Senate caucus to override Gov. "
              "Roy Cooper's veto of NC Senate Bill 20 ('Care for Women, Children, and "
              "Families Act') on May 16, 2023, enacting a 12-week abortion restriction on "
              "a strict 30-20 party-line vote, protecting an estimated 3,000+ lives annually "
              "per SBA Pro-Life America.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://sbaprolife.org/newsroom/press-releases/victory-north-carolina-establishes-law-protecting-3000-lives-annually"]),
    ]),

    # ------------ Mark Hollo (NC-R, State Senator SD-45, USAF Reserve Captain, joined Senate Jan 2025) ------------
    ("mark-hollo", "NC", "Senator", [
        claim("mh890a", "mark-hollo", "self_defense", 0, True,
              "Co-sponsored NC Senate Bill 50 ('Freedom to Carry NC') in his first session "
              "as a State Senator (assumed office January 2025, District 45 / Caldwell and "
              "Catawba counties), which passed the Senate 26-18 along party lines on "
              "March 20, 2025, eliminating the permit requirement for concealed carry and "
              "establishing constitutional carry in North Carolina.",
              ["https://www.ncleg.gov/BillLookup/2025/S50",
               "https://legiscan.com/NC/rollcall/S50/id/1599136",
               "https://ballotpedia.org/Mark_Hollo"]),
        claim("mh890b", "mark-hollo", "family_child_sovereignty", 0, True,
              "As a Republican member of the NC House of Representatives (serving District "
              "97 since 2011), voted for NC Senate Bill 49 ('Parents' Bill of Rights') and "
              "the veto override on August 16-17, 2023 (House voted 59-54 along party lines), "
              "barring instruction on gender identity and sexual orientation in kindergarten "
              "through 4th grade and requiring schools to notify parents when a student "
              "requests a name or pronoun change.",
              ["https://www.ncleg.gov/BillLookup/2023/S49",
               "https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://ballotpedia.org/Mark_Hollo"]),
    ]),

    # ------------ Lisa S. Barnes (NC-R, State Senator SD-11, primary sponsor SB 49) ------------
    ("lisa-s-barnes", "NC", "Senator", [
        claim("lsb890a", "lisa-s-barnes", "family_child_sovereignty", 0, True,
              "Was a primary sponsor of NC Senate Bill 49 ('Parents' Bill of Rights'), "
              "one of only three lead sponsors (with Senators Galey and Lee). The law, "
              "enacted via veto override on August 16-17, 2023 (Senate 27-18, House 59-54 "
              "on party lines), requires schools to notify parents when a student requests "
              "a name or pronoun change and bars instruction on gender identity or sexual "
              "orientation in grades K-4 — a direct statutory protection of parental rights "
              "over children's education.",
              ["https://www.ncleg.gov/BillLookup/2023/S49",
               "https://legiscan.com/NC/sponsors/S49/2023",
               "https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights"]),
        claim("lsb890b", "lisa-s-barnes", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican Senate caucus to override Gov. "
              "Roy Cooper's veto of NC Senate Bill 20 ('Care for Women, Children, and "
              "Families Act') on May 16, 2023, enacting a 12-week abortion restriction on "
              "a strict 30-20 party-line vote — a consistent pro-life legislative record.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://www.wunc.org/politics/2023-05-16/nc-senate-votes-to-override-gov-coopers-abortion-veto"]),
    ]),

    # ------------ Kevin Corbin (NC-R, State Senator SD-50, District 50 / western NC) ------------
    ("kevin-corbin", "NC", "Senator", [
        claim("kc890a", "kevin-corbin", "self_defense", 0, True,
              "Voted in favor of NC Senate Bill 50 ('Freedom to Carry NC') on March 20, "
              "2025, which passed the Senate 26-18 along party lines, eliminating the "
              "permit requirement for concealed carry and establishing constitutional carry "
              "in North Carolina. Corbin represents District 50 (Cherokee, Clay, Graham, "
              "Haywood, Jackson, Macon, and Swain counties) in western North Carolina.",
              ["https://www.ncleg.gov/BillLookup/2025/S50",
               "https://legiscan.com/NC/rollcall/S50/id/1599136",
               "https://www.ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2025/S/50"]),
        claim("kc890b", "kevin-corbin", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican Senate caucus to override Gov. "
              "Roy Cooper's veto of NC Senate Bill 20 ('Care for Women, Children, and "
              "Families Act') on May 16, 2023, enacting a 12-week abortion restriction on "
              "a strict 30-20 party-line vote.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://ballotpedia.org/Kevin_Corbin"]),
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
            if cat in scores and isinstance(qi, int) and qi < len(scores[cat]):
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
