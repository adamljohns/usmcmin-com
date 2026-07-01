#!/usr/bin/env python3
"""Enrichment batch 510: 5 Wisconsin Republican State Assembly Members with 0 claims.

archetype_curated federal bucket fully exhausted; archetype_party_default state
legislators (WI — bottom of alphabet) are the target tier, continuing from batch 509.

Targets (all WI Assembly, all Republican, all with 0 prior claims):
  Barbara Dittrich  (barbara-dittrich-wi-99) — WI AD-99 Waukesha Co.; introduced
                                               transgender sports ban (AB 100, 2025)
                                               and parental pronoun-consent bill
                                               (AB 103, 2025); parental rights in
                                               library materials and curriculum
                                               transparency bills

  Calvin Callahan   (calvin-callahan-wi-35)  — WI AD-35 Lincoln Co.; authored Lincoln
                                               County 2nd Amendment Sanctuary resolution
                                               (passed Dec 2022); NRA member; former
                                               Lincoln County Board Supervisor 2018-2023

  Bob Donovan       (bob-donovan-wi-61)      — WI AD-61 Milwaukee / Greenfield area;
                                               20 years on Milwaukee Common Council;
                                               2016 and 2022 Milwaukee mayoral candidate;
                                               anti-crime platform; supported AB 357 and
                                               AB 975 (14-week abortion restriction)

  Brent Jacobson    (brent-jacobson-wi-87)   — WI AD-87 Marathon Co. (Mosinee); attorney
                                               (WVU Law 2009); former Mayor of Mosinee
                                               2015-2024; voted for AB 24 (ICE-sheriff
                                               cooperation, March 2025); authored
                                               Bradyn's Law (AB 201, signed Dec 2025)

  Benjamin Franklin (benjamin-franklin-wi-88) — WI AD-88 Marathon Co.; Air Force Reserve
                                               (2008-); Director of Operations, Papa
                                               Johns; first elected Nov 2024; Vice Chair
                                               Veterans and Military Affairs; co-authored
                                               AB 912 (child testimony protection, 2025)
                                               and AB 913 (Guard/Reserve income tax
                                               exemption, 2025)

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Barbara Dittrich (WI AD-99, Waukesha County) ----
    # Transgender sports ban, parental rights in education bills
    ("barbara-dittrich-wi-99", "WI", "Assembly", [
        claim("bd1", "barbara-dittrich-wi-99", "biblical_marriage", 2, True,
              "Repeatedly introduced legislation rejecting transgender ideology in Wisconsin schools: 2025 Assembly Bill 100 bans biological males from competing on girls' sports teams and from using girls' locker rooms and showers; 2025 AB 103 requires parental written consent before school staff address a student by a name or pronoun inconsistent with their biological sex. Governor Evers vetoed a nearly identical sports-and-pronouns bill in 2024, confirming Dittrich's sustained legislative opposition to transgender ideology in public schools.",
              ["https://www.wispolitics.com/2025/dittrich-reintroduces-transgender-sports-ban-bills/",
               "https://www.wpr.org/news/public-hearing-transgender-students-wisconsin-assembly",
               "https://en.wikipedia.org/wiki/Barbara_Dittrich"]),
        claim("bd2", "barbara-dittrich-wi-99", "family_child_sovereignty", 0, True,
              "Authored multiple parental-rights bills in the Wisconsin Assembly: legislation requiring school boards to post curricula and instructional materials online for parental inspection; a parental-notification bill ensuring parents are informed when public library materials contain content flagged for minors; and AB 103 (2025) establishing that school personnel must obtain parental written consent before using a name or pronouns inconsistent with a student's biological sex — protecting parental sovereignty over a child's upbringing and education.",
              ["https://ballotpedia.org/Barbara_Dittrich",
               "https://legis.wisconsin.gov/assembly/99/dittrich/",
               "https://en.wikipedia.org/wiki/Barbara_Dittrich"]),
    ]),

    # ---- Calvin Callahan (WI AD-35, Lincoln County) ----
    # 2A sanctuary county author, NRA member
    ("calvin-callahan-wi-35", "WI", "Assembly", [
        claim("cc1", "calvin-callahan-wi-35", "self_defense", 0, True,
              "As Lincoln County Board Supervisor (2018-2023), authored and championed the county's Second Amendment Sanctuary resolution, which passed December 2022, declaring that Lincoln County will not use taxpayer funds to enforce unconstitutional gun restrictions and will not aid in limiting citizens' Second Amendment rights. Callahan stated: 'We will uphold the Second Amendment rights of the citizens of Lincoln County and will not use taxpayer dollars to restrict Second Amendment rights.' He is a documented NRA member.",
              ["https://tomahawkleader.com/2022/12/22/supervisors-approve-resolution-declaring-lincoln-county-second-amendment-sanctuary/",
               "https://ballotpedia.org/Calvin_Callahan",
               "https://justfacts.votesmart.org/candidate/193887/calvin-callahan"]),
        claim("cc2", "calvin-callahan-wi-35", "self_defense", 1, True,
              "The Second Amendment Sanctuary resolution Callahan authored explicitly commits Lincoln County to refuse enforcement of any 'unconstitutional restriction' on firearms — including federal mandates. This posture aligns with opposition to red-flag confiscation laws, assault-weapon bans, magazine-capacity limits, and gun-owner registries. Callahan's NRA membership and his role as a county-level champion of 2A nullification place him squarely against the federal gun-control agenda.",
              ["https://tomahawkleader.com/2022/12/22/supervisors-approve-resolution-declaring-lincoln-county-second-amendment-sanctuary/",
               "https://justfacts.votesmart.org/candidate/193887/calvin-callahan"]),
    ]),

    # ---- Bob Donovan (WI AD-61, Milwaukee / Greenfield area) ----
    # Pro-life votes (AB 357, AB 975); anti-crime Milwaukee conservative
    ("bob-donovan-wi-61", "WI", "Assembly", [
        claim("bdx1", "bob-donovan-wi-61", "sanctity_of_life", 0, True,
              "Supported 2023 Wisconsin Assembly Bill 357, which tightened the legal definition of abortion in state law, and backed AB 975, which would limit abortion to 14 weeks gestational age — a measure the Assembly passed 53-46 in January 2024. Donovan, a Milwaukee-area Republican who served 20 years on the Common Council before returning to the Assembly, has maintained a consistent record of pro-life votes protecting the unborn.",
              ["https://ballotpedia.org/Robert_G._Donovan_(Wisconsin)",
               "https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://en.wikipedia.org/wiki/Bob_Donovan"]),
        claim("bdx2", "bob-donovan-wi-61", "public_justice", 0, True,
              "A longtime Milwaukee conservative whose entire political identity centers on law and order: as a 20-year Milwaukee Common Council member and two-time mayoral candidate (2016, 2022), Donovan built his platform on more police officers, tougher criminal penalties, and community safety — a rare conservative voice for public order in a heavily Democratic city. His anti-crime record predates and persists through his current Assembly service.",
              ["https://en.wikipedia.org/wiki/Bob_Donovan",
               "https://ballotpedia.org/Robert_G._Donovan_(Wisconsin)",
               "https://legis.wisconsin.gov/assembly/61/donovan/about-bob/meet-bob/"]),
    ]),

    # ---- Brent Jacobson (WI AD-87, Marathon County / Mosinee) ----
    # ICE cooperation vote (AB 24, 2025); Bradyn's Law (AB 201, signed Dec 2025)
    ("brent-jacobson-wi-87", "WI", "Assembly", [
        claim("bj1", "brent-jacobson-wi-87", "border_immigration", 2, True,
              "Voted for and publicly championed 2025 Wisconsin Assembly Bill 24, requiring sheriffs to cooperate with ICE when arresting a noncitizen for a felony — a direct rejection of sanctuary-city-style policies. Jacobson stated: 'The bill which I proudly voted for today should not be controversial' and praised the eight Wisconsin sheriff departments that had already signed ICE cooperation agreements to detain and deport noncitizen felons.",
              ["https://www.wispolitics.com/2025/rep-jacobson-republicans-crack-down-on-dangerous-illegal-aliens/",
               "https://legis.wisconsin.gov/assembly/87/jacobson/media/rawj5r2h/3182025_pr_jacobson_republicans_crack_down_on_dangerous_illegal_aliens.pdf"]),
        claim("bj2", "brent-jacobson-wi-87", "family_child_sovereignty", 0, True,
              "Authored 'Bradyn's Law' (2025 Wisconsin Assembly Bill 201, signed into law December 2025), named for DC Everest High School student Bradyn Bohn who took his own life after being targeted by an organized sexual extortion ring. The law establishes sextortion as a new crime with severe penalties for perpetrators who prey on minors, expanding legal protections for children against online sexual predators and providing stronger tools for public justice on behalf of victimized families.",
              ["https://legis.wisconsin.gov/assembly/87/jacobson/media/ddedyly2/61825_pr_jacobson_bradyns_law_passes_assembly.pdf",
               "https://legis.wisconsin.gov/assembly/87/jacobson/media/surlrq0b/12825_pr_jacobson_bradyns_law_signed.pdf",
               "https://ballotpedia.org/Brent_Jacobson_(Wisconsin)"]),
    ]),

    # ---- Benjamin Franklin (WI AD-88, Marathon County) ----
    # Air Force Reserve; AB 912 (child testimony); AB 913 (Guard income tax exemption)
    ("benjamin-franklin-wi-88", "WI", "Assembly", [
        claim("bf1", "benjamin-franklin-wi-88", "family_child_sovereignty", 0, True,
              "Co-authored 2025 Wisconsin Assembly Bill 912, updating state evidentiary law to allow audiovisual recordings of child witness testimony for abuse and exploitation victims up to age 18 (raised from 16), with eligibility determined by the child's age at the time of recording rather than at trial. The change reduces re-traumatization of child victims who would otherwise be required to testify repeatedly in person, strengthening the state's capacity to prosecute predators while protecting the child's wellbeing.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2900",
               "https://ballotpedia.org/Benjamin_Franklin_(Wisconsin)",
               "https://legis.wisconsin.gov/assembly/88/franklin/"]),
        claim("bf2", "benjamin-franklin-wi-88", "refuse_state_overreach", 0, True,
              "Authored 2025 Wisconsin Assembly Bill 913, exempting income earned by Wisconsin National Guard and Air Force Reserve members for inactive duty service performed in Wisconsin from state income tax — restoring more of their earned compensation to military families and reducing the tax burden the state imposes on men and women who sacrifice time with family for training obligations. Franklin, himself an active-duty Air Force Reserve member since 2008 and Vice Chair of the Assembly Veterans and Military Affairs Committee, sponsored the measure from direct personal experience.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2900",
               "https://ballotpedia.org/Benjamin_Franklin_(Wisconsin)",
               "https://legis.wisconsin.gov/assembly/88/franklin/about/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
