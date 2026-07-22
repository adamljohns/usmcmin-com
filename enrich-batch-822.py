#!/usr/bin/env python3
"""Enrichment batch 822: 5 Florida Republican State Representatives (evidence_state → evidence_curated).

The archetype_curated pool is fully exhausted. This batch continues the evidence_state
Florida state-rep series, covering:
  Peggy Gossett-Seidman (FL HD-91, Palm Beach Co.; voted NO on 6-week ban HB 7B,
    YES on Constitutional Carry HB 543; sponsored voter registration protection CS/HB 135),
  Nathan Boyles (FL HD-3, Okaloosa Co.; attorney; homeschool dad; special election June 2025;
    pro-life iVoterGuide; co-sponsored HB 641 anti-gender-ideology workplace act),
  Omar Blanco (FL HD-115, Miami-Dade; elected Nov 2024; FL Right to Life endorsed;
    Christian Family Coalition 2025 recognition; voted yes HB 1517 unborn wrongful death),
  Monique Miller (FL HD-33, Brevard/Palm Bay; FL Right to Life dual endorsement;
    sponsored HB 6025 repealing emergency firearm ban, signed law; Moms for Liberty founder),
  Mike Redondo (FL HD-118, Miami-Dade; FL Right to Life endorsed; sponsored HB 757
    AI deepfake child exploitation felony, signed law Ch.2025-99; Speaker-designate 2030).

Research covers 2023-2026 voting records, endorsements, sponsored legislation, and
iVoterGuide questionnaire responses from FL Right to Life, NRA-ILA, Christian Family
Coalition, Ballotpedia, Florida Politics, Florida Phoenix, FL House official records.
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
    # --- Peggy Gossett-Seidman (FL HD-91, R; Palm Beach Co.; first elected Nov 2022; re-elected Nov 2024) ---
    ("peggy-gossett-seidman", "FL", "State Representative", [
        claim("pgs1", "peggy-gossett-seidman", "sanctity_of_life", 0, False,
              "Voted NO on HB 7B (Florida's Heartbeat Protection Act, 6-week abortion ban) on "
              "April 13, 2023 — one of approximately nine Republicans to break with the party "
              "caucus on the measure, which passed 70-40 and was signed by Gov. DeSantis. "
              "Gossett-Seidman stated publicly: 'It's just not the right vote, and I think "
              "everyone does their best and tries their hardest, and that was my decision on "
              "behalf of the district.' Her opposition to the 6-week threshold places her "
              "outside the rubric's standard for lawmakers who affirm full legal protection "
              "from conception.",
              ["https://choicetracker.org/fl/people/peggy-gossett-seidman/200540160",
               "https://news.yahoo.com/vote-three-palm-beach-county-090641822.html"]),
        claim("pgs2", "peggy-gossett-seidman", "self_defense", 0, True,
              "Voted YES on HB 543, Florida's Constitutional Carry bill, on March 24, 2023. "
              "The bill passed the House 76-32 and was signed by Gov. DeSantis on April 3, "
              "2023, making Florida the 26th permitless-carry state — allowing law-abiding "
              "citizens to carry a concealed firearm without a government-issued permit.",
              ["https://fastdemocracy.com/bill-search/fl/2023/bills/FLB00028080/",
               "https://spacecoastdaily.com/2023/03/florida-house-passes-constitutional-carry-house-bill-543-with-76-32-vote-senate-version-ready-for-consideration/"]),
        claim("pgs3", "peggy-gossett-seidman", "election_integrity", 0, True,
              "Sponsored and passed CS/HB 135 (2024), signed into law as Chapter 2024-78, "
              "which prevents the Florida Dept. of Highway Safety & Motor Vehicles from "
              "changing a voter's party affiliation without the voter's written consent — "
              "a direct election-integrity protection against administrative party-affiliation "
              "manipulation. Gossett-Seidman represents FL House District 91 (Palm Beach Co.).",
              ["https://myfloridahouse.gov/Sections/Bills/billsdetail.aspx?BillId=78726",
               "https://flvoicenews.com/gossett-seidman-passes-four-bills-secures-state-funding-following-legislative-session/"]),
    ]),

    # --- Nathan Boyles (FL HD-3, R; Okaloosa Co.; attorney; homeschool dad; special election June 10, 2025) ---
    ("nathan-boyles", "FL", "State Representative", [
        claim("nb1", "nathan-boyles", "sanctity_of_life", 0, True,
              "Stated on his iVoterGuide questionnaire that 'human life begins at conception "
              "and deserves legal protection at every stage until natural death,' and that "
              "abortion providers including Planned Parenthood should receive zero taxpayer "
              "funds (federal, state, local, including Title X). He also supports requiring "
              "in-person medical consultation and outcome reporting for chemical abortion drugs. "
              "Boyles lists 'pro-life principles' as a top campaign priority. He represents "
              "Okaloosa County in the Florida Panhandle, winning a special election on "
              "June 10, 2025.",
              ["https://ivoterguide.com/candidate/87326/race/22895/election/1275",
               "https://midbaynews.com/post/nathan-boyles-election"],
              kind="statement"),
        claim("nb2", "nathan-boyles", "self_defense", 0, True,
              "Stated publicly: 'We have to defend our Second Amendment and ensure that no "
              "politician passes laws to restrict law-abiding citizens' access to their gun "
              "rights.' He lists Second Amendment defense as a core campaign pillar and "
              "confirmed on his iVoterGuide questionnaire full alignment with constitutional "
              "gun rights. As a licensed Florida attorney (FSU J.D.) and former Okaloosa "
              "County Commissioner (2012-2024), Boyles campaigned explicitly on preventing "
              "government infringement on firearms rights.",
              ["https://www.votenathanboyles.com/",
               "https://ivoterguide.com/candidate/87326/race/22895/election/1275"],
              kind="statement"),
        claim("nb3", "nathan-boyles", "biblical_marriage", 2, True,
              "Co-sponsored HB 641 (2026), the 'Freedom of Conscience in the Workplace Act,' "
              "which prohibits employers from compelling employees to use pronouns inconsistent "
              "with their biological sex and bans adverse personnel action based on gender "
              "ideology. The bill passed all three House committees before dying on the Second "
              "Reading Calendar (last action March 13, 2026). On his iVoterGuide questionnaire "
              "Boyles also affirmed: 'Marriage is a God-ordained, sacred and legal union of "
              "one man and one woman, and no government has the authority to alter this "
              "definition,' and stated he opposes compelling individuals or businesses to "
              "provide services that violate their moral or religious beliefs.",
              ["https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=83253",
               "https://ivoterguide.com/candidate/87326/race/22895/election/1275"]),
    ]),

    # --- Omar Blanco (FL HD-115, R; Miami-Dade; elected Nov 2024; pro-life; CFC recognized) ---
    ("omar-blanco", "FL", "State Representative", [
        claim("ob1", "omar-blanco", "sanctity_of_life", 0, True,
              "Florida Right to Life endorsed Omar Blanco in the November 2024 general "
              "election for HD-115. He stated on his iVoterGuide questionnaire: 'Human life "
              "begins at conception and deserves legal protection at every stage until natural "
              "death.' He also endorsed the Born Alive Abortion Survivors Protection Act and "
              "opposed all taxpayer funding for abortion providers including Planned Parenthood. "
              "Blanco, the son of Cuban exiles, represents parts of Miami, Hialeah, and Doral "
              "in Miami-Dade County.",
              ["https://frtl.org/2024-general-election-endorsements/",
               "https://ivoterguide.com/candidate/52458/race/1317/election/715"],
              kind="statement"),
        claim("ob2", "omar-blanco", "family_child_sovereignty", 0, True,
              "The Christian Family Coalition Florida — a leading pro-family, pro-religious-liberty "
              "advocacy group — named Blanco among honored GOP lawmakers at their 2025 "
              "Legislative Victory Breakfast at Trump National Doral (August 2025), citing his "
              "support for CFC-backed legislation during the 2025 session including expanded "
              "parental rights measures and HB 1205 (election integrity reform). Blanco "
              "campaigned explicitly on 'further protect[ing] parental rights in education' "
              "and stated on iVoterGuide: 'Parents should have the right to make decisions "
              "for their minor children.'",
              ["https://floridapolitics.com/archives/750444-christian-family-coalition-florida-to-celebrate-2025-session-victories-with-gop-lawmakers-at-trump-doral/",
               "https://ivoterguide.com/candidate/52458/race/1317/election/715"],
              kind="endorsement"),
        claim("ob3", "omar-blanco", "election_integrity", 0, True,
              "Supported HB 1205 (2025), Florida's citizen initiative petition reform bill, "
              "described by the Republican Party of Florida as an 'election integrity' measure "
              "and celebrated by the Christian Family Coalition as a 2025 session victory. "
              "The bill reformed Florida's constitutional initiative amendment process. The "
              "RPOF described the bill as protecting election integrity by tightening rules "
              "on petition-driven ballot initiatives. Blanco's recognition by CFC for 2025 "
              "session votes confirms his support for the legislation.",
              ["https://florida.gop/republican-party-of-florida-moves-to-intervene-in-federal-lawsuits-to-defend-hb-1205s-election-integrity-reforms-to-floridas-citizen-initiative-constitutional-amendment-process/",
               "https://floridapolitics.com/archives/750444-christian-family-coalition-florida-to-celebrate-2025-session-victories-with-gop-lawmakers-at-trump-doral/"]),
    ]),

    # --- Monique Miller (FL HD-33, R; Brevard Co./Palm Bay; elected Nov 2024; Moms for Liberty founder) ---
    ("monique-miller", "FL", "State Representative", [
        claim("mm1", "monique-miller", "sanctity_of_life", 0, True,
              "Florida Right to Life endorsed Monique Miller in both the August 2024 Republican "
              "primary and the November 2024 general election for HD-33 — one of the few "
              "candidates to receive both a primary and general FRTL endorsement. Her iVoterGuide "
              "questionnaire states: 'Human life begins at conception and deserves legal "
              "protection at every stage until natural death.' Her campaign platform includes "
              "the explicit goal to 'Foster a culture of LIFE.' Miller succeeded Rep. Randy "
              "Fine in HD-33 (Brevard County / Palm Bay area) and is seeking re-election in "
              "the August 18, 2026 primary.",
              ["https://frtl.org/2024-primary-endorsements/",
               "https://frtl.org/2024-general-election-endorsements/",
               "https://ivoterguide.com/candidate/31737/race/5151/election/1170"],
              kind="statement"),
        claim("mm2", "monique-miller", "self_defense", 1, True,
              "Sponsored HB 6025 (2025), which repealed Florida's statutory ban on the sale "
              "and possession of firearms and ammunition during declared states of emergency — "
              "a ban that had carried up to 60 days in jail for violation. The bill passed the "
              "House 86-28 and was signed into law by Gov. DeSantis on May 28, 2025 "
              "(Chapter 2025-103). NRA-ILA specifically highlighted the signing and cited "
              "Miller's sponsorship as protecting Second Amendment rights during emergencies, "
              "when law-abiding citizens may most need access to self-defense tools.",
              ["https://www.nraila.org/articles/20250529/florida-governor-desantis-signs-legislation-to-remove-2a-restrictions-during-emergencies",
               "https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=81483"]),
        claim("mm3", "monique-miller", "family_child_sovereignty", 0, True,
              "A founding advisory board member of Moms for Liberty, the national parental-rights-in-education "
              "organization. Miller entered the legislature directly from parental rights activism, "
              "citing her children and grandchildren as motivation. Her iVoterGuide responses "
              "state 'Parents should have the right to make decisions for their minor children' "
              "and 'our rights are derived from God, rather than government.' She supported "
              "Florida's Parental Rights in Education law and also sponsored HB 491 (2025) "
              "to prohibit AI-powered camera surveillance of concealed firearms in spaces "
              "where citizens have a privacy expectation.",
              ["https://floridapolitics.com/archives/613756-moms-for-liberty-activist-monique-miller-running-to-succeed-randy-fine/",
               "https://ivoterguide.com/candidate/31737/race/5151/election/1170"],
              kind="statement"),
    ]),

    # --- Mike Redondo (FL HD-118, R; Miami-Dade; special election Dec 2023; Speaker-designate 2030) ---
    ("mike-redondo", "FL", "State Representative", [
        claim("mr1", "mike-redondo", "sanctity_of_life", 0, True,
              "Florida Right to Life endorsed Mike Redondo in the November 2024 general "
              "election for HD-118. Redondo, a Catholic personal injury attorney and son of "
              "Cuban exiles, represents west Miami-Dade County (near Zoo Miami / Kendall). "
              "He first won his seat via special election on December 5, 2023, and was "
              "re-elected in November 2024 with 68.3% of the vote. He was subsequently "
              "elected Speaker-designate for the 2030 Florida House term by unanimous vote "
              "of all 22 GOP freshmen, making him a key future figure in Florida Republican "
              "leadership.",
              ["https://frtl.org/2024-general-election-endorsements/",
               "https://ballotpedia.org/Mike_Redondo"],
              kind="endorsement"),
        claim("mr2", "mike-redondo", "public_justice", 0, True,
              "Sponsored HB 757 (2025), signed into law as Chapter 2025-99 (effective "
              "October 1, 2025), making it a felony to create, possess, or distribute "
              "AI-generated or deepfake non-consensual sexual images — including of minors "
              "(3rd-degree felony for soliciting or viewing; 2nd-degree for intent to "
              "distribute). The bill passed the Florida Legislature and was signed by "
              "Governor DeSantis, establishing criminal penalties for digital sexual "
              "exploitation that protects children and women from AI-generated abuse.",
              ["https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=81383",
               "https://cbs12.com/news/local/florida-makes-deepfake-ai-porn-a-felony-as-teen-victim-shares-her-story-south-florida-palm-beach-county-new-laws-october-1-2025"]),
        claim("mr3", "mike-redondo", "family_child_sovereignty", 0, True,
              "Co-sponsored HB 1505 (2025), expanding parental consent requirements for "
              "minors' healthcare — including STI treatment, surveys, biofeedback, and DNA "
              "records — and strengthening parents' right to be involved in their minor "
              "children's medical decisions. Redondo's campaign platform states he stands "
              "with 'President Trump and the America First movement' and lists parental "
              "involvement and constitutional defense as core priorities. He self-identifies "
              "as Catholic and describes his Cuban exile family background as central to "
              "his conviction that government must not supplant parental and family authority.",
              ["https://mikeredondo.com",
               "https://floridapolitics.com/archives/745799-the-honor-of-a-lifetime-mike-redondo-wins-race-to-be-house-speaker-for-2030-term/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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
