#!/usr/bin/env python3
"""Enrichment batch 846: 6 claims for 4 bottom-of-alphabet 2026 U.S. House candidates.

Targets: Niina Threlfall-Baum (WI-07 R), John Duresky (WA-04 D),
         Rebecca Cooke (WI-03 D), Philip Harding (VA-07 R).
All archetype_curated senator/rep buckets exhausted; these are the bottom-of-alphabet
active federal candidates with fewest existing claims (4-5 each).

Sources verified via WebSearch (2026-07-23). Minified write preserves ~35-36 MB master.
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
    # ---- Niina Threlfall-Baum (WI-R, WI-07 open seat, Tiffany seat) ----
    ("niina-threlfall-baum", "WI", "WI-07", [
        claim("ntb2", "niina-threlfall-baum", "border_immigration", 1, False,
              "At her February 2026 campaign launch and in a WSAW interview, Threlfall-Baum explicitly stated that immigrants are 'essential in Wisconsin' and called for creating 'a functional legal pathway' for agricultural and rural workers — directly rejecting mandatory deportation and standing apart from the America First enforcement platform the rubric requires.",
              ["https://www.wsaw.com/2026/02/25/moderate-republican-baum-wants-more-unity-warns-ai-data-centers-7th-congressional/",
               "https://www.weau.com/2026/02/04/moderate-republican-niina-baum-running-7th-congressional-district/"]),
    ]),

    # ---- John Duresky (WA-D, WA-04 open seat, Newhouse seat) ----
    ("john-duresky", "WA", "WA-04", [
        claim("jd4", "john-duresky", "foreign_policy_restraint", 3, True,
              "Pledged from the outset of his 2026 congressional campaign not to accept AIPAC or corporate PAC money, placing himself outside the foreign-lobbying fundraising infrastructure the rubric identifies as a disqualifying entanglement.",
              ["https://dominickb.substack.com/p/meet-the-democrat-running-for-dan"]),
        claim("jd5", "john-duresky", "border_immigration", 0, False,
              "Characterized Trump's border-enforcement operations as 'immoral and un-American,' specifically criticizing ICE for detaining people going to immigration appointments and work rather than criminal actors, and opposing wall-based and military-force approaches to immigration control.",
              ["https://www.yakimaherald.com/news/local/government/elections/immigration-a-key-issue-in-4th-district-congressional-race-in-central-wa/article_f9d5881b-02f3-43aa-b3ea-39bb1edfe01f.html",
               "https://columbiabasinherald.com/news/2026/jul/09/fourth-congressional-district-candidates-share-immigration-policy-opinions/"]),
    ]),

    # ---- Rebecca Cooke (WI-D, WI-03 2026 D Candidate) ----
    ("rebecca-cooke", "WI", "WI-03", [
        claim("rc6", "rebecca-cooke", "border_immigration", 2, False,
              "Headlined a 2026 campaign fundraiser with former Chicago Mayor Rahm Emanuel, widely documented as the architect of Chicago's sanctuary-city policies; and publicly touted an endorsement from AFSCME, whose Wisconsin chapter filed suit to protect CDL driving privileges for illegal immigrants — signaling opposition to anti-sanctuary enforcement.",
              ["https://www.vanordenforcongress.com/cooke-campaigns-off-the-architect-of-sanctuary-cities/",
               "https://www.wispolitics.com/2026/van-orden-campaign-rebecca-cooke-celebrates-endorsement-from-union-suing-to-protect-cdls-for-illegal-aliens/"]),
        claim("rc7", "rebecca-cooke", "biblical_marriage", 4, False,
              "Publicly welcomed and highlighted her endorsement from the Wisconsin Education Association Council (WEAC), which the NRCC characterized as an organization supporting gender-transition curriculum for minors in public schools; by touting the endorsement Cooke aligned herself with LGBTQ promotion in school policy that the rubric opposes.",
              ["https://nrcc.org/2026/06/22/radical-rebecca-cooke-endorsed-by-group-that-supports-sex-changes-for-kids/",
               "https://www.wizmnews.com/2026/05/19/us-house-candidates-cooke-and-berge-debate-in-la-crosse/"]),
    ]),

    # ---- Philip Harding (VA-R, VA-07 2026 R Candidate) ----
    ("philip-harding", "VA", "VA-07", [
        claim("ph1", "philip-harding", "self_defense", 0, True,
              "At the June 17, 2026 Republican primary forum in Fredericksburg, Harding joined all three GOP candidates in endorsing national concealed carry reciprocity and specifically 'emphasized self-defense and lawful carry,' affirming his support for expanding constitutional carry rights.",
              ["https://www.potomaclocal.com/2026/06/19/republican-candidates-outline-priorities-on-energy-data-centers-and-parental-rights-at-fredericksburg-forum/",
               "https://virginiamercury.com/2026/07/06/affordability-jobs-election-integrity-take-center-stage-in-va-s-7th-congressional-district-race/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
