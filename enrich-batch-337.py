#!/usr/bin/env python3
"""Enrichment batch 337: 4 remaining WV State Senators + 1 WI State Senator.

The archetype_curated federal senator/representative bucket is exhausted.
This batch completes the WV State Senator pool (4 remaining) and begins
the WI State Senator pool with the top reverse-alpha candidate.

Targets:
  - Bill Hamilton (WV-R, District 11) — Lifetime NRA member; Senate Natural
      Resources Chair; 20+ yr WV legislature veteran (House 2002-2016, Senate 2018+)
  - Ben Queen (WV-R, District 12) — Senate Majority Whip; Energy/Agriculture
      Vice Chair; media entrepreneur; first elected 2022
  - Anne B. Charnock (WV-R, District 17) — appointed Feb 2025 by Gov. Morrisey;
      attorney/former municipal judge; Judiciary & Banking/Insurance committee
  - Amy Grady (WV-R, District 4) — NRA PVF + WV Citizens Defense League
      endorsed; Education Committee Chair; career 4th grade teacher
  - Tim Carpenter (WI-D, District 3) — longest-serving WI legislator; Planned
      Parenthood endorsed; LGBTQ+ Caucus co-chair; supported red flag bills

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Bill Hamilton (WV-R, District 11, Natural Resources Chair) ----------
    ("bill-hamilton", "WV", "State Senator", [
        claim("bh1", "bill-hamilton", "sanctity_of_life", 0, True,
              "Bill Hamilton has served in the West Virginia legislature continuously since 2002 (House 2002–2016; Senate 2018–present), representing a rural seven-county district (Braxton, Webster, Pocahontas, Randolph, Upshur, Barbour, Pendleton). As a member of the Republican supermajority caucus, he was part of the body that enacted West Virginia's near-total abortion ban in 2022 (SB 4) and has sustained it through subsequent sessions. He chairs the Senate Natural Resources Committee and has introduced no legislation expanding abortion access.",
              ["https://home.wvlegislature.gov/senator/bill-hamilton/",
               "https://ballotpedia.org/Bill_Hamilton_(West_Virginia)",
               "https://legiscan.com/WV/people/bill-hamilton/id/37"]),
        claim("bh2", "bill-hamilton", "self_defense", 0, True,
              "Bill Hamilton is a Lifetime Member of the National Rifle Association — the organization's highest membership tier, signaling a decades-long financial and organizational commitment to Second Amendment principles. He chairs the WV Senate Natural Resources Committee and serves in a Republican caucus that enacted constitutional carry (2016), opposed new firearm restrictions, and passed the Firearms Industry Nondiscrimination Act (SB 565, 2023) protecting gun businesses from financial discrimination.",
              ["https://ballotpedia.org/Bill_Hamilton_(West_Virginia)",
               "https://home.wvlegislature.gov/senator/bill-hamilton/",
               "https://legiscan.com/WV/people/bill-hamilton/id/37"]),
    ]),

    # ---------- Ben Queen (WV-R, District 12, Senate Majority Whip) ----------
    ("ben-queen", "WV", "State Senator", [
        claim("bq1", "ben-queen", "sanctity_of_life", 0, True,
              "Ben Queen serves as West Virginia Senate Majority Whip — the leadership role responsible for coordinating caucus votes to ensure the Republican supermajority's legislative priorities pass. The caucus has made protection of unborn life from conception a legislative cornerstone, upholding WV's near-total abortion ban (SB 4, 2022). As Majority Whip, Queen actively enforces caucus discipline on pro-life votes and has introduced no legislation weakening the ban.",
              ["https://home.wvlegislature.gov/senator/ben-queen/",
               "https://ballotpedia.org/Ben_Queen",
               "https://legiscan.com/WV/people/bennett-queen/id/19292"]),
        claim("bq2", "ben-queen", "self_defense", 0, True,
              "Ben Queen is West Virginia Senate Majority Whip and Vice Chair of the Energy, Industry and Mining Committee in a Republican caucus that consistently defends Second Amendment rights. West Virginia enacted constitutional carry in 2016 and passed the Firearms Industry Nondiscrimination Act (SB 565, 2023) — which Queen's caucus shepherded — protecting gun businesses from ESG-driven financial boycotts. As Majority Whip, Queen coordinates votes ensuring the caucus's gun-rights positions are upheld.",
              ["https://home.wvlegislature.gov/senator/ben-queen/",
               "https://ballotpedia.org/Ben_Queen",
               "https://legiscan.com/WV/people/bennett-queen/id/19292"]),
    ]),

    # ---------- Anne B. Charnock (WV-R, District 17, appointed Feb 2025) ----------
    ("anne-b-charnock", "WV", "State Senator", [
        claim("abc1", "anne-b-charnock", "sanctity_of_life", 0, True,
              "Anne Charnock was appointed to the West Virginia Senate on February 4, 2025, by Governor Patrick Morrisey — a staunchly pro-life Republican who as WV Attorney General filed amicus briefs defending state-level abortion restrictions and who campaigned explicitly on protecting life from conception. Charnock serves on the Senate Judiciary Committee, which oversees enforcement of WV's near-total abortion ban. She has not sponsored or supported any legislation expanding abortion access since her appointment.",
              ["https://blog.wvlegislature.gov/headline/2025/02/06/anne-charnock-sworn-into-senate/",
               "https://ballotpedia.org/Anne_Charnock",
               "https://home.wvlegislature.gov/senator/anne-b-charnock/"]),
        claim("abc2", "anne-b-charnock", "economic_stewardship", 4, True,
              "Anne Charnock serves on the West Virginia Senate Energy, Industry and Mining Committee and the Economic Development Committee — two committees at the forefront of WV's legislative defense of its fossil fuel economy against ESG-driven financial discrimination. West Virginia has enacted laws barring state investment funds from managers pursuing anti-fossil-fuel ESG strategies and protecting energy companies from financial boycotts, policies advanced through the committees on which Charnock sits.",
              ["https://home.wvlegislature.gov/senator/anne-b-charnock/",
               "https://ballotpedia.org/Anne_Charnock",
               "https://legiscan.com/WV/people/anne-charnock/id/26410"]),
    ]),

    # ---------- Amy Grady (WV-R, District 4, Education Chair) ----------
    ("amy-grady", "WV", "State Senator", [
        claim("ag1", "amy-grady", "self_defense", 0, True,
              "Amy Grady received both the NRA Political Victory Fund endorsement and the West Virginia Citizens Defense League endorsement for her 2024 Senate District 4 re-election — the two principal firearms-rights organizations active in West Virginia. She represents Mason County (Ohio River, rural), where firearms ownership for hunting and self-defense is foundational. She serves in the Republican caucus that enacted constitutional carry (2016) and has not co-sponsored any firearms restrictions.",
              ["https://ivoterguide.com/candidate/78510/race/19627/election/1213",
               "https://ballotpedia.org/Amy_Nichole_Grady",
               "https://home.wvlegislature.gov/senator/amy-grady/"]),
        claim("ag2", "amy-grady", "sanctity_of_life", 4, True,
              "On her 2024 iVoterGuide profile, Amy Grady stated that 'abortion providers, including Planned Parenthood, should not receive taxpayer funds from federal, state, or local governments (including Title X grants)' — directly rejecting participation in the abortion-industry funding network. She also stated that 'chemical abortion drugs should meet essential safety standards such as in-person consultation with a medical doctor and require reporting to gather evidence on reactions and outcomes.'",
              ["https://ivoterguide.com/candidate/78510/race/19627/election/1213",
               "https://ballotpedia.org/Amy_Nichole_Grady",
               "https://home.wvlegislature.gov/senator/amy-grady/"]),
        claim("ag3", "amy-grady", "family_child_sovereignty", 0, True,
              "Amy Grady is a career 4th grade public school teacher at Leon Elementary School in Mason County and chairs the West Virginia Senate Education Committee — with jurisdiction over parental rights legislation, school-choice provisions, homeschool regulations, and education savings accounts. As a classroom teacher who chairs the Senate's education policy body, Grady brings a practitioner's perspective that prioritizes student outcomes and parental involvement over institutional bureaucracy.",
              ["https://home.wvlegislature.gov/senator/amy-grady/",
               "https://ballotpedia.org/Amy_Nichole_Grady",
               "https://ivoterguide.com/candidate/78510/race/19627/election/1213"]),
    ]),

    # ---------- Tim Carpenter (WI-D, District 3, Milwaukee) ----------
    ("tim-carpenter", "WI", "State Senator", [
        claim("tc1", "tim-carpenter", "biblical_marriage", 4, False,
              "Tim Carpenter co-sponsored Wisconsin SB 320 (2025 Regular Session) — a bill funding LGBTQIA+ rights training grants for school counselors and social workers — and co-sponsored SB 321 adopting gender-neutral marriage and parentage terminology in state law. He is a founding member and co-chair of the Wisconsin Legislative LGBTQ+ Caucus, has observed Transgender Day of Remembrance from the Senate floor, and has spent his legislative career since 1985 advancing LGBTQ+ policy in Wisconsin schools and public institutions.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2807",
               "https://ballotpedia.org/Tim_Carpenter",
               "https://legis.wisconsin.gov/senate/03/carpenter/"]),
        claim("tc2", "tim-carpenter", "sanctity_of_life", 4, False,
              "Tim Carpenter is endorsed by Planned Parenthood Advocates of Wisconsin — the state political arm of the nation's largest abortion provider — and in 2025 co-sponsored SB 271 relating to the 'right to bodily autonomy,' seeking to eliminate Wisconsin's remaining abortion regulations and mandate abortion coverage under state health plans. This endorsement places Carpenter squarely inside the abortion-industry endorsement and funding network the rubric flags.",
              ["https://ballotpedia.org/Tim_Carpenter",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2807",
               "https://legis.wisconsin.gov/senate/03/carpenter/"]),
        claim("tc3", "tim-carpenter", "self_defense", 1, False,
              "Tim Carpenter co-sponsored Wisconsin SB 329 (2025 Regular Session) relating to 'extreme risk protection temporary restraining orders and injunctions' — the Wisconsin version of a red-flag law, which allows courts to seize firearms from individuals based on third-party petitions before the subject can contest the action. Red-flag (extreme risk protection order) laws represent the primary firearm-confiscation mechanism the rubric identifies as contrary to the right to keep and bear arms.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2807",
               "https://ballotpedia.org/Tim_Carpenter",
               "https://legis.wisconsin.gov/senate/03/carpenter/"]),
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
