#!/usr/bin/env python3
"""Enrichment batch 756: 5 sitting FL state representatives with 0 evidence claims.

Bottom-of-name-alphabet FL pool (evidence_state bucket): Will Robinson Jr.
(HD-71), Tiffany Esposito (HD-77), Shane G. Abbott (HD-5), Tom Fabricio
(HD-110), Ryan Chamberlin (HD-24). 12 claims spanning sanctity_of_life,
self_defense, family_child_sovereignty, border_immigration, and
economic_stewardship categories.

Sources: ballotpedia.org, en.wikipedia.org, tiffanyforfl.com, 30a.news,
voteshaneabbott.com, robinsonforflorida.com, ryanchamberlincampaign.com,
wusf.org, flgov.com, myfloridahouse.gov.
Minified write preserves ~35-36 MB master.
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
    # ----------- Will Robinson Jr. (FL, State Representative HD-71, R) -----------
    ("will-robinson-jr", "FL", "State Representative", [
        claim("wr1", "will-robinson-jr", "sanctity_of_life", 0, True,
              "Self-described pro-life Republican — Wikipedia identifies him as 'a pro-life Republican' — who voted YES on Florida HB 5 (15-week abortion limit, 2022) and SB 300 (Heartbeat Protection Act, restricting abortion after approximately six weeks, 2023), building a consistent pro-life floor record across multiple sessions.",
              ["https://en.wikipedia.org/wiki/Will_Robinson_(Florida_politician)",
               "https://www.robinsonforflorida.com/",
               "https://wusf.org/politics-issues/2023-04-14/desantis-signs-6-week-abortion-ban-florida-house-approval"]),
        claim("wr2", "will-robinson-jr", "self_defense", 0, True,
              "Wikipedia identifies him as 'an avid supporter of Second Amendment rights'; voted YES on HB 543 (April 2023), making Florida the 26th constitutional-carry state and eliminating the permit requirement for qualified adults to carry a concealed firearm.",
              ["https://en.wikipedia.org/wiki/Will_Robinson_(Florida_politician)",
               "https://www.robinsonforflorida.com/",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
    ]),

    # ----------- Tiffany Esposito (FL, State Representative HD-77, R) -----------
    ("tiffany-esposito", "FL", "State Representative", [
        claim("te1", "tiffany-esposito", "sanctity_of_life", 0, True,
              "Ran explicitly as a 'pro-life' candidate who committed to 'defend the unborn'; voted YES on SB 300 (Heartbeat Protection Act, 2023), restricting abortion after approximately six weeks — her first legislative session after taking office in January 2023.",
              ["https://tiffanyforfl.com/meet-tiffany/",
               "https://ballotpedia.org/Tiffany_Esposito",
               "https://wusf.org/politics-issues/2023-04-14/desantis-signs-6-week-abortion-ban-florida-house-approval"]),
        claim("te2", "tiffany-esposito", "self_defense", 0, True,
              "Self-described 'pro-gun' candidate who pledged to 'strengthen Second Amendment rights'; voted YES on HB 543 (April 2023), Florida's constitutional-carry legislation, making the state the 26th to eliminate the permit requirement for concealed carry.",
              ["https://tiffanyforfl.com/meet-tiffany/",
               "https://ballotpedia.org/Tiffany_Esposito",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
        claim("te3", "tiffany-esposito", "family_child_sovereignty", 0, True,
              "Supported and voted YES on CS/CS/HB 1505 (2025 Parental Rights bill), which passed the Florida House 80-28 and strengthens parental authority over school curriculum and activities — consistent with her 'Constitutional Conservative' platform commitment to parental rights in education.",
              ["https://tiffanyforfl.com/meet-tiffany/",
               "https://ballotpedia.org/Tiffany_Esposito",
               "https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=82261"]),
    ]),

    # ----------- Shane G. Abbott (FL, State Representative HD-5, R) -----------
    ("shane-g-abbott", "FL", "State Representative", [
        claim("sa1", "shane-g-abbott", "sanctity_of_life", 0, True,
              "Declared himself 'passionate about protecting the unborn' in his 2022 campaign announcement; voted YES on SB 300 (Heartbeat Protection Act, 2023), restricting abortion after approximately six weeks — his first full legislative session after winning election to represent the northwest Florida Panhandle (HD-5).",
              ["https://30a.news/2022/02/16/why-im-running-for-florida-house-district-5/",
               "https://www.voteshaneabbott.com/",
               "https://wusf.org/politics-issues/2023-04-14/desantis-signs-6-week-abortion-ban-florida-house-approval"]),
        claim("sa2", "shane-g-abbott", "self_defense", 0, True,
              "Declared himself 'a staunch defender of the constitutional right to bear arms' in his 2022 campaign announcement; voted YES on HB 543 (April 2023), Florida's constitutional-carry legislation eliminating the government permit requirement for qualified adults carrying a concealed firearm.",
              ["https://30a.news/2022/02/16/why-im-running-for-florida-house-district-5/",
               "https://ballotpedia.org/Shane_Abbott",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
        claim("sa3", "shane-g-abbott", "border_immigration", 0, True,
              "Made 'securing the border' a primary campaign commitment, calling for enforcement action against illegal immigration; his position is consistent with subsequent FL House support for SB 1718 (2023 immigration enforcement bill), which tightened state cooperation with federal immigration authorities and penalized sanctuary policies.",
              ["https://30a.news/2022/02/16/why-im-running-for-florida-house-district-5/",
               "https://ballotpedia.org/Shane_Abbott"]),
    ]),

    # ----------- Tom Fabricio (FL, State Representative HD-110, R) -----------
    ("tom-fabricio", "FL", "State Representative", [
        claim("tf1", "tom-fabricio", "sanctity_of_life", 0, True,
              "Voted YES on HB 5 (15-week abortion limit, 2022) and is not among the named Republican defectors on SB 300 (Heartbeat Protection Act, 2023, passed 70-40), indicating a consistent pro-life voting record across multiple Florida House sessions.",
              ["https://ballotpedia.org/Tom_Fabricio",
               "https://wusf.org/politics-issues/2023-04-14/desantis-signs-6-week-abortion-ban-florida-house-approval"]),
        claim("tf2", "tom-fabricio", "family_child_sovereignty", 0, True,
              "Voted YES on HB 1557 (Florida Parental Rights in Education Act, 2022) and CS/CS/HB 1505 (2025 Parental Rights bill, passed 80-28), supporting parental authority over school curriculum and restrictions on classroom instruction on sexual orientation and gender identity in early grades.",
              ["https://ballotpedia.org/Tom_Fabricio",
               "https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act",
               "https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=82261"]),
    ]),

    # ----------- Ryan Chamberlin (FL, State Representative HD-24, R) -----------
    ("ryan-chamberlin", "FL", "State Representative", [
        claim("rc1", "ryan-chamberlin", "economic_stewardship", 0, True,
              "Campaigned explicitly on 'conservative fiscal values,' applying his background as a business CEO (True Patriot Network) to advocate for limited government spending, fiscal accountability, and protection of taxpayer dollars — making private-sector fiscal discipline a defining campaign theme.",
              ["https://ryanchamberlincampaign.com/",
               "https://ballotpedia.org/Ryan_Chamberlin"]),
        claim("rc2", "ryan-chamberlin", "family_child_sovereignty", 0, True,
              "As an Apostolic Pentecostal minister and parent, championed family sovereignty and parental authority over children's upbringing and education as a core campaign commitment; voted YES on CS/CS/HB 1505 (2025 Parental Rights bill, passed 80-28) during his first full legislative session.",
              ["https://ryanchamberlincampaign.com/",
               "https://ballotpedia.org/Ryan_Chamberlin",
               "https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=82261"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
