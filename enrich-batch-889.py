#!/usr/bin/env python3
"""Enrichment batch 889: hand-curated claims for 5 NC Republican State Senators.

All archetype_curated federal senator/rep buckets exhausted; continuing the
pivot to archetype_party_default NC state senators from the bottom of the
reverse-alphabet name list (following batch 888's Warren Daniel / Alexander /
Sawyer / McInnis / Johnson).

Key NC legislation used as evidence:
  - SB 20 (Care for Women, Children, and Families Act, 2023): 12-week abortion
    limit; Senate voted 30-20 to override Gov. Cooper's veto on May 16, 2023 —
    all 30 Republicans voted yes.
  - SB 49 (Parents' Bill of Rights, 2023): barred K-4 gender/sexuality
    instruction; passed Senate party-line, veto overridden 27-18 Aug 2023.
  - SB 50 (Freedom to Carry NC, 2025): constitutional carry; passed Senate
    26-18 March 2025; Phil Berger, Ralph Hise, and Tim Moffitt are confirmed
    co-sponsors (DavidsonLocal press release / VoteSmart / ncleg.gov).

Targets (NC State Senators, continuing reverse-alpha order from batch 888):
  Timothy D. Moffitt, Steve Jarvis, Ralph Hise, Phil Berger, Norman W. Sanderson

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
    # ------------ Timothy D. Moffitt (NC-R, State Senator SD-48) ------------
    ("timothy-d-moffitt", "NC", "Senator", [
        claim("tm889a", "timothy-d-moffitt", "self_defense", 0, True,
              "Co-sponsored NC Senate Bill 50 ('Freedom to Carry NC'), which passed the Senate "
              "26-18 along party lines in March 2025, removing the permit requirement for "
              "concealed carry and establishing constitutional carry in North Carolina — a "
              "direct legislative push for the rubric's constitutional-carry ideal.",
              ["https://www.davidsonlocal.com/news/press-release-senate-bill-50-filed-to-allow-gun-owners-to-carry-concealed-handguns-without-obtaining-a-permit",
               "https://justfacts.votesmart.org/bill/39472/107404/103082/tim-moffitt-co-sponsored-sb-50-establishes-state-constitutional-concealed-carry"]),
        claim("tm889b", "timothy-d-moffitt", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican caucus to override Gov. Roy "
              "Cooper's veto of NC Senate Bill 20 ('Care for Women, Children, and Families "
              "Act') on May 16, 2023, enacting a 12-week abortion restriction — the Senate "
              "overrode the veto 30-20 on a strict party-line vote. SBA Pro-Life America "
              "hailed the law as 'protecting 3,000+ lives annually.'",
              ["https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://sbaprolife.org/newsroom/press-releases/victory-north-carolina-establishes-law-protecting-3000-lives-annually"]),
    ]),

    # ------------ Steve Jarvis (NC-R, State Senator SD-30) ------------
    ("steve-jarvis", "NC", "Senator", [
        claim("sj889a", "steve-jarvis", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican Senate caucus to override Gov. "
              "Roy Cooper's veto of NC Senate Bill 20 ('Care for Women, Children, and "
              "Families Act') on May 16, 2023, enacting the 12-week abortion restriction "
              "on a strict 30-20 party-line vote. Ballotpedia confirms Jarvis 'opposes "
              "abortion,' consistent with the Republican caucus's uniform pro-life position.",
              ["https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://ballotpedia.org/Steven_Jarvis_(North_Carolina)"]),
        claim("sj889b", "steve-jarvis", "family_child_sovereignty", 0, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') and the Republican "
              "veto override on August 16-17, 2023, requiring schools to notify parents if "
              "a child requests a name or pronoun change and restricting instruction on "
              "gender identity and sexual orientation in kindergarten through 4th grade — "
              "a direct legislative protection of parental authority over children's education.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://spectrumlocalnews.com/nc/charlotte/news/2023/02/07/controversial--parents--bill-of-rights--in-n-c--senate--here-s-what-s-in-the-lgbtq-bill"]),
    ]),

    # ------------ Ralph Hise (NC-R, State Senator SD-47) ------------
    ("ralph-hise", "NC", "Senator", [
        claim("rh889a", "ralph-hise", "self_defense", 0, True,
              "Co-sponsored NC Senate Bill 50 ('Freedom to Carry NC'), which passed the Senate "
              "26-18 along party lines in March 2025, establishing constitutional carry and "
              "removing the permit requirement for concealed handguns in North Carolina.",
              ["https://www.davidsonlocal.com/news/press-release-senate-bill-50-filed-to-allow-gun-owners-to-carry-concealed-handguns-without-obtaining-a-permit",
               "https://legiscan.com/NC/bill/S50/2025"]),
        claim("rh889b", "ralph-hise", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican caucus to override Gov. Roy "
              "Cooper's veto of NC SB 20 ('Care for Women, Children, and Families Act') "
              "on May 16, 2023, enacting a 12-week abortion restriction on a 30-20 party-"
              "line vote and making North Carolina's pro-life law effective July 1, 2023.",
              ["https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://www.ncleg.gov/Sessions/2023/Bills/Senate/PDF/S20v5.pdf"]),
        claim("rh889c", "ralph-hise", "biblical_marriage", 4, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') and the August 2023 "
              "veto override, which bars instruction on gender identity and sexual orientation "
              "in kindergarten through 4th grade — blocking classroom promotion of LGBTQ "
              "ideology in North Carolina's public elementary schools.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://legiscan.com/NC/votes/S49/2023"]),
    ]),

    # ------------ Phil Berger (NC-R, State Senator SD-26, Senate President Pro Tempore) ------------
    ("phil-berger", "NC", "Senator", [
        claim("pb889a", "phil-berger", "self_defense", 0, True,
              "Co-sponsored NC Senate Bill 50 ('Freedom to Carry NC') and publicly championed "
              "it as Senate President Pro Tempore, stating 'It's past time for us to join the "
              "majority of states that recognize Constitutional Carry.' The bill passed the "
              "Senate 26-18 in March 2025, eliminating the permit requirement for concealed "
              "carry in North Carolina.",
              ["https://www.davidsonlocal.com/news/press-release-senate-bill-50-filed-to-allow-gun-owners-to-carry-concealed-handguns-without-obtaining-a-permit",
               "https://northcarolina.concealedcarry.com/2025/06/24/north-carolina-constitutional-carry-vetoed/"]),
        claim("pb889b", "phil-berger", "sanctity_of_life", 0, True,
              "As Senate President Pro Tempore, Phil Berger led the effort to override Gov. "
              "Cooper's veto of NC SB 20 ('Care for Women, Children, and Families Act'), "
              "promising to 'quickly take up the override' after the veto. The Senate voted "
              "30-20 on May 16, 2023, all Republicans voting yes, enacting the 12-week "
              "abortion restriction — SBA Pro-Life America credited NC Republicans for "
              "'protecting 3,000+ lives annually.'",
              ["https://obgyn.duke.edu/news/nc-general-assembly-overrides-gov-roy-coopers-veto-sb20-12-week-abortion-ban",
               "https://sbaprolife.org/newsroom/press-releases/victory-north-carolina-establishes-law-protecting-3000-lives-annually"]),
        claim("pb889c", "phil-berger", "family_child_sovereignty", 0, True,
              "Led the NC Senate's passage of SB 49 ('Parents' Bill of Rights') and the August "
              "2023 veto override as Senate President Pro Tempore, enacting a law requiring "
              "schools to notify parents when a student requests a name or pronoun change and "
              "restricting age-inappropriate gender-and-sexuality instruction in grades K-4.",
              ["https://www.ednc.org/2023-02-07-senate-passes-parents-bill-of-rights/",
               "https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights"]),
    ]),

    # ------------ Norman W. Sanderson (NC-R, State Senator SD-2) ------------
    ("norman-w-sanderson", "NC", "Senator", [
        claim("ns889a", "norman-w-sanderson", "family_child_sovereignty", 0, True,
              "Sponsored NC Senate Bill 49 ('Parents' Bill of Rights'), which passed the Senate "
              "on party lines and was enacted via veto override on August 16-17, 2023. The law "
              "requires schools to notify parents when a child requests a name or pronoun change "
              "and bars instruction on gender identity or sexual orientation in grades K-4 — a "
              "direct statutory protection of parental rights in children's education.",
              ["https://legiscan.com/NC/sponsors/S49/2023",
               "https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights"]),
        claim("ns889b", "norman-w-sanderson", "sanctity_of_life", 0, True,
              "Voted with the unanimous 30-member Republican caucus to override Gov. Roy "
              "Cooper's veto of NC SB 20 ('Care for Women, Children, and Families Act') on "
              "May 16, 2023, enacting a 12-week abortion restriction in a 30-20 party-line "
              "vote — a consistent pro-life legislative record.",
              ["https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://www.ncleg.gov/Sessions/2023/Bills/Senate/PDF/S20v5.pdf"]),
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
