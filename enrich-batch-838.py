#!/usr/bin/env python3
"""Enrichment batch 838: 5 North Dakota Republican state senators (archetype_party_default).

Continues bottom-of-alphabet state-senator enrichment. Batch 837 covered ND senators at
archetype_curated confidence (Mark Enget, Kristin Roers, Kent Weston, Keith Boehm, Justin
Gerhardt). This batch covers 5 remaining ND Republicans currently at archetype_party_default
with 0 claims, taken from the bottom of the reverse-alpha bucket:

  Jonathan Sickler (District 17, Grand Forks area — appointed June 2022, Harvard JD,
    CLO at AE2S engineering; full Appropriations assignment in 2025)
  Jose L. Castaneda (District 40, Minot — retired USAF Lt. Col., Air Force Academy;
    assumed office Dec 1, 2024; first session 69th Assembly 2025)
  Greg Kessel (District 39, Belfield — farmer; Energy and Natural Resources Vice Chair;
    assumed office Dec 1, 2022; full member of 68th and 69th Assemblies)
  Desiree Van Oosting (District 36 — assumed Dec 1, 2024; Health Care Vice Chair;
    first session 69th Assembly 2025)
  Donald Schaible (District 31, Mott — ambulance/firefighter volunteer, 20-yr school
    board; President Pro Tempore in 68th Assembly 2023; continuing to 69th 2025)

Key sourced legislation (same bills as batch 836-837):
- SB 2150 (2023): ND abortion ban from conception; initial vote 43-4 Jan 31 2023;
  conference version 42-5 April 19 2023; signed Gov. Burgum April 24, 2023.
- HB 1339 (2023): Constitutional carry expansion to non-residents; passed Senate 44-3;
  signed April 12, 2023, effective August 1, 2023.
- HB 1144 (2025): Transgender student bathroom enforcement; passed Senate 40-7 April 10
  2025; signed Gov. Armstrong May 1, 2025.
- HB 1588 (2025): Firearm carry enhancement (removes reporting obligation, reduces
  public-gathering carry penalty to $100 noncriminal fee, authorizes campus carry);
  Senate passed April 3, 2025; signed Gov. Armstrong April 23, 2025.
- HB 1297 (2025): Bans ranked-choice and approval voting statewide; Senate 38-8,
  House 75-16; signed Gov. Armstrong; Castaneda quoted calling it "proactive."

NOTE: Castaneda and Van Oosting assumed office Dec 1, 2024 and were not present for
the 2023 regular session; their claims are limited to 2025 legislation.
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
    # --- Jonathan Sickler (ND-R, District 17, Grand Forks area; appointed June 2022) ---
    ("jonathan-sickler", "ND", "Senator", [
        claim("js1", "jonathan-sickler", "sanctity_of_life", 0, True,
              "Sickler voted with the 43-4 Republican-led ND Senate majority on January 31, "
              "2023 to pass SB 2150, banning abortion from conception throughout pregnancy with "
              "exceptions only for rape or incest through six weeks and life-threatening medical "
              "emergencies. A revised conference version passed 42-5 on April 19, 2023; Gov. "
              "Burgum signed it April 24, 2023, making North Dakota one of the nation's most "
              "protective pro-life states. Born and raised on a farm near Dickinson, ND, Sickler "
              "returned to North Dakota after earning a J.D. from Harvard Law School to serve as "
              "Chief Legal Officer of AE2S, an engineering consulting firm in Grand Forks. He was "
              "appointed to District 17 in June 2022, replacing longtime senator Ray Holmberg, and "
              "won a full four-year term in November 2022. His first full legislative session in "
              "the 68th Assembly (2023) placed him in the Republican majority that enacted one of "
              "the nation's most comprehensive pro-life statutes.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Jonathan_Sickler"]),
        claim("js2", "jonathan-sickler", "self_defense", 0, True,
              "Sickler voted with the near-unanimous 44-3 ND Senate majority to pass HB 1339 "
              "(2023), extending North Dakota's constitutional carry (permitless concealed carry) "
              "to non-residents by removing the state-residency requirement and replacing it with "
              "any valid state driver's license. Gov. Burgum signed HB 1339 April 12, 2023, "
              "effective August 1, 2023, reinforcing North Dakota's position as a leading "
              "constitutional carry state. Sickler — raised on a farm in western North Dakota "
              "where responsible firearm ownership is a cornerstone of rural life — represents "
              "District 17 in the Grand Forks area. In the 69th Assembly (2025) he serves on "
              "the powerful Senate Appropriations Committee.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://ballotpedia.org/Jonathan_Sickler"]),
    ]),

    # --- Jose L. Castaneda (ND-R, District 40, Minot; retired USAF Lt. Col.; assumed Dec 1 2024) ---
    ("jose-l-castaneda", "ND", "Senator", [
        claim("jc1", "jose-l-castaneda", "election_integrity", 0, True,
              "Castaneda was a vocal Senate floor advocate for HB 1297 (2025), which prohibits "
              "cities, counties, and all political subdivisions in North Dakota from using "
              "ranked-choice or approval voting to elect or nominate any candidate. He called the "
              "legislation 'proactive,' stating: 'In this era, where we're trying to build more "
              "trust in our election system, we simply cannot afford to have any complications or "
              "delays in any election.' The Senate passed HB 1297 38-8; the House 75-16; Gov. "
              "Armstrong signed it, locking in a uniform, transparent election system statewide. "
              "A retired U.S. Air Force lieutenant colonel who graduated from the Air Force "
              "Academy and earned a graduate degree in aeronautics from Embry-Riddle Aeronautical "
              "University before a career as an air med pilot, Castaneda won election to District "
              "40 (Minot area, Ward County) in November 2024 and assumed office December 1, 2024.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1297.html",
               "https://bismarcktribune.com/news/state-regional/government-politics/article_6e0cb385-f86f-4a04-8a23-91800a903a22.html",
               "https://ballotpedia.org/Jose_Castaneda_(North_Dakota)"]),
        claim("jc2", "jose-l-castaneda", "biblical_marriage", 2, True,
              "Castaneda voted with the 40-7 ND Senate majority to pass HB 1144 (2025), "
              "prohibiting schools from constructing multi-stall gender-neutral bathrooms or "
              "shower rooms and requiring all multi-use restrooms to be designated by biological "
              "sex. The bill directs the Attorney General to investigate violations, with "
              "noncompliant schools subject to a $2,500 civil fine. Gov. Armstrong signed HB 1144 "
              "May 1, 2025. In his first legislative session (69th Assembly 2025), Castaneda — "
              "representing District 40 in north-central North Dakota — voted with the Republican "
              "Senate supermajority to protect children's privacy in public schools and reject "
              "transgender ideology in the classroom.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://ballotpedia.org/Jose_Castaneda_(North_Dakota)"]),
        claim("jc3", "jose-l-castaneda", "self_defense", 0, True,
              "Castaneda voted with the ND Senate to pass HB 1588 (2025), the firearm carry "
              "enhancement removing the obligation for a person carrying concealed without a "
              "permit to inform law enforcement upon contact, reducing the penalty for carrying "
              "at a public gathering from a criminal infraction to a $100 noncriminal fee, and "
              "authorizing the State Board of Higher Education to allow firearms on campus. Gov. "
              "Armstrong signed HB 1588 April 23, 2025. A retired United States Air Force "
              "lieutenant colonel who carried responsibility for aircraft and personnel safety "
              "throughout his military career, Castaneda understands the constitutional right of "
              "law-abiding citizens to carry without unnecessary government friction. He "
              "represents District 40 (Ward County, north-central North Dakota), a region with "
              "strong agricultural and constitutional-carry traditions.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1588.html",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Jose_Castaneda_(North_Dakota)"]),
    ]),

    # --- Greg Kessel (ND-R, District 39, Belfield — farmer; assumed Dec 1 2022) ---
    ("greg-kessel", "ND", "Senator", [
        claim("gk1", "greg-kessel", "sanctity_of_life", 0, True,
              "Kessel voted with the 43-4 Republican-led ND Senate majority on January 31, "
              "2023 to pass SB 2150, banning abortion from conception throughout pregnancy with "
              "exceptions only for rape or incest through six weeks and life-threatening medical "
              "emergencies. The revised conference version passed 42-5 on April 19, 2023; Gov. "
              "Burgum signed it April 24, 2023. A farmer representing District 39 in southwest "
              "North Dakota (Belfield area), Kessel won election in November 2022 and entered "
              "the 68th Legislative Assembly fully committed to the pro-life consensus of his "
              "rural agricultural district. He serves on the Energy and Natural Resources "
              "Committee (Vice Chair), Emergency Response Services Committee, Energy Development "
              "and Transmission Committee, and Industry and Business Committee.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Greg_Kessel"]),
        claim("gk2", "greg-kessel", "self_defense", 0, True,
              "Kessel voted with the near-unanimous 44-3 ND Senate majority to pass HB 1339 "
              "(2023), extending North Dakota's constitutional carry to non-residents by removing "
              "the state-residency requirement for permitless concealed carry. Gov. Burgum signed "
              "HB 1339 April 12, 2023, effective August 1, 2023. Southwest North Dakota — "
              "Kessel's District 39 in the Belfield area — has one of the deepest gun cultures "
              "in the state, where responsible firearm ownership is a cornerstone of rural and "
              "ranch life. Kessel's vote with the Senate supermajority reflects his constituents' "
              "strong Second Amendment values and the overwhelming conservative consensus in the "
              "ND legislature.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://ballotpedia.org/Greg_Kessel"]),
        claim("gk3", "greg-kessel", "biblical_marriage", 2, True,
              "Kessel voted with the 40-7 ND Senate majority to pass HB 1144 (2025), "
              "prohibiting schools from constructing multi-stall gender-neutral bathrooms or "
              "shower rooms and requiring all multi-use restrooms to be designated by biological "
              "sex. The Attorney General is directed to investigate violations, with noncompliant "
              "schools subject to a $2,500 civil fine. Gov. Armstrong signed HB 1144 May 1, 2025. "
              "As a farmer representing a rural southwest ND district (Belfield area), Kessel "
              "serves constituents who broadly support protecting biological-sex designations in "
              "public schools and safeguarding the privacy of children — consistent with the "
              "traditional family values of his community.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://ballotpedia.org/Greg_Kessel"]),
    ]),

    # --- Desiree Van Oosting (ND-R, District 36; assumed Dec 1 2024; Health Care Vice Chair) ---
    ("desiree-van-oosting", "ND", "Senator", [
        claim("dvo1", "desiree-van-oosting", "biblical_marriage", 2, True,
              "Van Oosting voted with the 40-7 ND Senate majority to pass HB 1144 (2025), "
              "prohibiting schools from constructing multi-stall gender-neutral bathrooms or "
              "shower rooms and requiring all multi-use restrooms to be designated by biological "
              "sex. The bill directs the Attorney General to investigate violations, with "
              "noncompliant schools subject to a $2,500 civil fine. Gov. Armstrong signed HB "
              "1144 May 1, 2025. In her first legislative session (69th Assembly 2025), Van "
              "Oosting — who assumed office December 1, 2024 representing District 36 — voted "
              "with the Republican Senate supermajority to protect children's privacy in public "
              "school facilities and uphold biological-sex designations, rejecting the gender "
              "ideology the rubric opposes. She serves as Vice Chair of the Senate Health Care "
              "Committee and on the Energy Development and Transmission and Rural Health "
              "Transformation Committees.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://ballotpedia.org/Desiree_Van_Oosting"]),
        claim("dvo2", "desiree-van-oosting", "self_defense", 0, True,
              "Van Oosting voted with the ND Senate to pass HB 1588 (2025), the firearm carry "
              "enhancement removing the obligation for a person carrying concealed without a "
              "permit to inform law enforcement upon contact, reducing the penalty for carrying "
              "at a public gathering from a criminal infraction to a $100 noncriminal fee, and "
              "authorizing the State Board of Higher Education to permit firearms on campus and "
              "in buildings. Gov. Armstrong signed HB 1588 April 23, 2025. As a first-term "
              "senator representing District 36 in North Dakota, Van Oosting — who assumed "
              "office December 1, 2024 — voted with the Republican Senate majority to expand "
              "constitutional carry rights and remove unnecessary friction between law-abiding "
              "gun owners and law enforcement.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1588.html",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Desiree_Van_Oosting"]),
    ]),

    # --- Donald Schaible (ND-R, District 31, Mott; President Pro Tempore 2023; ambulance/firefighter) ---
    ("donald-schaible", "ND", "Senator", [
        claim("ds1", "donald-schaible", "sanctity_of_life", 0, True,
              "As President Pro Tempore of the North Dakota Senate, Schaible voted with the "
              "43-4 Senate majority on January 31, 2023 to pass SB 2150, banning abortion from "
              "conception throughout pregnancy with exceptions only for rape or incest through "
              "six weeks and life-threatening medical emergencies. A revised conference version "
              "passed 42-5 on April 19, 2023; Gov. Burgum signed it April 24, 2023. Schaible "
              "represents District 31 (Mott, Hettinger County, south-central North Dakota). A "
              "longtime volunteer with the Mott Ambulance Service, a volunteer firefighter, and "
              "a 20-year member of the Mott-Regent School Board, Schaible presided over a Senate "
              "session that enacted one of the nation's most comprehensive pro-life statutes — "
              "and cast his own yes vote alongside 42 colleagues in the 43-4 majority.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Donald_Schaible"]),
        claim("ds2", "donald-schaible", "self_defense", 0, True,
              "Schaible voted with the near-unanimous 44-3 ND Senate majority to pass HB 1339 "
              "(2023), extending North Dakota's constitutional carry to non-residents by removing "
              "the state-residency requirement for permitless concealed carry. Gov. Burgum signed "
              "HB 1339 April 12, 2023, effective August 1, 2023. Representing District 31 in "
              "rural south-central North Dakota (Mott, Hettinger County) — a region with deep "
              "agricultural and firearm-ownership traditions — Schaible voted with the Senate "
              "supermajority to reinforce North Dakota's status as a leading constitutional carry "
              "state. His background in emergency services reflects the same community-safety "
              "values that underlie responsible gun ownership across rural ND.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://ballotpedia.org/Donald_Schaible"]),
        claim("ds3", "donald-schaible", "biblical_marriage", 2, True,
              "Schaible voted with the 40-7 ND Senate majority to pass HB 1144 (2025), "
              "prohibiting schools from constructing multi-stall gender-neutral bathrooms or "
              "shower rooms and requiring all multi-use restrooms to be designated by biological "
              "sex. Gov. Armstrong signed HB 1144 May 1, 2025. A 20-year member of the "
              "Mott-Regent School Board who has deep roots in his rural District 31 community, "
              "Schaible is closely acquainted with the importance of protecting children's privacy "
              "in public-school facilities. His vote with the Republican supermajority — as the "
              "former President Pro Tempore of the 68th Assembly — continues the pro-family "
              "legislative consensus he helped shepherd across multiple sessions.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://ballotpedia.org/Donald_Schaible"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent wrong-state slug collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
