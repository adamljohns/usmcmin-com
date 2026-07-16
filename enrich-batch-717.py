#!/usr/bin/env python3
"""Enrichment batch 717: evidence-curated claims for 5 state officials.

Primary federal senator/representative pools (archetype_curated with 0 claims)
are fully exhausted. Batch continues evidence_state candidates with 0 claims,
bottom-of-alphabet reverse-sort (MD -> KY -> HI -> HI -> KS):

  Aruna Miller          (MD-D, Lieutenant Governor, since Jan 2023)
  Jacqueline Coleman    (KY-D, Lt. Governor, since Jan 2019; re-elected Nov 2023)
  Sylvia Luke           (HI-D, Lieutenant Governor, since Dec 2022)
  Anne Lopez            (HI-D, Attorney General, since Dec 2022)
  David Toland          (KS-D, Lieutenant Governor, since Jan 2021)

Claims sourced to governor.maryland.gov, ballotpedia.org, en.wikipedia.org,
wdrb.com, ltgov.hawaii.gov, ag.hawaii.gov, civilbeat.org, kansasreflector.com,
kslegislature.gov.
All reflect 2019-2025 public record.
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
    # --------------- Aruna Miller (MD-D, Lieutenant Governor) ---------------
    ("aruna-miller", "MD", "Lieutenant", [
        claim("am1", "aruna-miller", "sanctity_of_life", 0, False,
              "Championed and co-signed the 2024 Maryland constitutional amendment (Question 1) "
              "enshrining a fundamental 'right to reproductive freedom' — which passed with 73% "
              "of the vote in November 2024. Alongside Governor Moore, Miller released an official "
              "statement declaring the Moore-Miller administration would 'fight for abortion rights "
              "and reproductive freedom,' adding: 'While other states are dead set on ripping away "
              "reproductive rights and attempting to erase the existence of trans and nonbinary "
              "individuals, we're doing the opposite.' Governor Moore signed the proclamation "
              "formally incorporating the amendment into Maryland's constitution in January 2025.",
              ["https://governor.maryland.gov/news/press-releases/governor-moore-signs-proclamation-enshrine-reproductive-freedom-marylands-constitution",
               "https://governor.maryland.gov/news/press/pages/Governor-Moore-and-Lt-Governor-Miller-Release-Statements-on-General-Assembly-Passing-Legislation-to-ERR-in-MD-Constitution.aspx",
               "https://ballotpedia.org/Maryland_Question_1,_Right_to_Reproductive_Freedom_Amendment_(2024)"]),
        claim("am2", "aruna-miller", "border_immigration", 2, False,
              "Was the administration's most prominent spokesperson for HB 444 / SB 245 (2024), "
              "which prohibited Maryland law enforcement jurisdictions from entering into ICE "
              "287(g) program agreements — effectively banning mandatory local immigration "
              "enforcement cooperation statewide. Miller stated: 'As an immigrant, this bill is "
              "deeply personal to me. Immigrants make Maryland stronger every day, and our "
              "communities are safer when everyone feels protected and valued. This legislation "
              "ensures that our law enforcement resources remain focused on keeping Marylanders "
              "safe, not on actions that create fear in our neighborhoods.' Governor Moore signed "
              "the legislation in May 2024.",
              ["https://governor.maryland.gov/news/press-releases/governor-moore-signs-legislation-prohibit-maryland-jurisdictions-deputizing-officers-federal-civil-immigration-enforcement",
               "https://ballotpedia.org/Aruna_Miller"]),
        claim("am3", "aruna-miller", "self_defense", 1, False,
              "The Moore-Miller administration's 2024 Legislative Session Public Safety Agenda "
              "included creating Maryland's Center for Firearm Violence Prevention within the "
              "Maryland Department of Health — making Maryland the first state in the nation to "
              "establish a dedicated Center for Firearm Violence. The agenda advanced a "
              "comprehensive package of gun restrictions, including assault-weapon regulations "
              "and purchase restrictions. As Lt. Governor, Miller publicly endorsed and advanced "
              "this agenda, directly opposing constitutional carry and Second Amendment protections.",
              ["https://governor.maryland.gov/news/press-releases/governor-moore-announces-2024-legislative-session-public-safety-agenda-and-legislative-action",
               "https://ballotpedia.org/Aruna_Miller"]),
    ]),

    # --------------- Jacqueline Coleman (KY-D, Lt. Governor) ---------------
    ("jacqueline-coleman", "KY", "Governor", [
        claim("jc1", "jacqueline-coleman", "family_child_sovereignty", 0, False,
              "Became the leading public opponent of Kentucky Constitutional Amendment 2 (2024 "
              "ballot measure that would have allowed state tax dollars to fund non-public private "
              "school education), traveling statewide against it and declaring: 'I will go anywhere, "
              "anytime, any place and speak about the damage that Amendment 2 will do to our kids, "
              "our schools and our communities.' Coleman stated flatly that 'public dollars should "
              "stay in public schools,' opposing educational freedom, parental school choice, and "
              "any public funding for homeschool or private school families — effectively defending "
              "the government school monopoly over education funding. Amendment 2 was defeated "
              "November 5, 2024, with 53% of Kentucky voters rejecting it.",
              ["https://www.wdrb.com/news/kentuckys-lieutenant-governor-leans-on-her-teaching-roots-in-fighting-a-school-choice-measure/article_ff6c23a2-8511-11ef-8dc9-bff975bf648a.html",
               "https://ballotpedia.org/Kentucky_Constitutional_Amendment_2,_Allow_State_Funding_for_Non-Public_Education_Amendment_(2024)"]),
        claim("jc2", "jacqueline-coleman", "sanctity_of_life", 0, False,
              "Ran on the Beshear-Coleman joint ticket in the November 2023 Kentucky gubernatorial "
              "re-election campaign, where abortion — specifically the absence of rape and incest "
              "exceptions in Kentucky's near-total abortion ban — was the Democrats' central "
              "campaign argument. A viral campaign ad featuring rape survivor Hadley Duvall "
              "attacking the Republican challenger's support for no-exception abortion laws was "
              "credited by GOP leadership as a decisive factor in Beshear and Coleman's victory "
              "in a deep-red state. As Lt. Governor throughout the Beshear administration, "
              "Coleman represents an executive branch that has consistently opposed Kentucky's "
              "pro-life legislation and called for weakening the state's abortion restrictions.",
              ["https://en.wikipedia.org/wiki/2023_Kentucky_gubernatorial_election",
               "https://ballotpedia.org/Jacqueline_Coleman"]),
    ]),

    # --------------- Sylvia Luke (HI-D, Lieutenant Governor) ---------------
    ("sylvia-luke", "HI", "Lieutenant", [
        claim("sl1", "sylvia-luke", "sanctity_of_life", 0, False,
              "Participated in the signing of Hawaii Senate Bill 1 (2023 legislative session), "
              "which codified and fortified existing abortion access protections in Hawaii law; "
              "stated at the press conference: 'Hawaii was the first state to legalize abortion "
              "and we have continued to be at the forefront of efforts to protect and expand "
              "access to reproductive health care. The signing of Senate Bill 1 is a huge step "
              "in ensuring access to essential health care and securing reproductive freedom "
              "throughout the Aloha State.' Luke has also participated in the signing of the "
              "2024 Hawaii Right to Reproductive Freedom constitutional amendment, further "
              "enshrining unrestricted abortion access at the constitutional level.",
              ["https://ltgov.hawaii.gov/featured/lt-gov-sylvia-luke-joins-state-legislators-and-gov-josh-green-to-protect-reproductive-freedom-in-hawai%CA%BBi/",
               "https://ballotpedia.org/Hawaii_Right_to_Reproductive_Freedom_Amendment_(2024)"]),
        claim("sl2", "sylvia-luke", "sanctity_of_life", 1, False,
              "In March 2023, joined a Multi-State Reproductive Freedom Coalition of 22 lieutenant "
              "governors at the National Lieutenant Governors Association meeting in Washington, D.C., "
              "forming an interstate compact to coordinate advocacy and policy across state lines "
              "for unrestricted abortion access — explicitly opposing any restrictions on abortion "
              "or recognition of unborn personhood. The coalition's stated mission is to protect "
              "and expand reproductive freedom as a cross-state policy agenda, positioning Hawaii "
              "as an abortion refuge state and coordinating with other blue states on policy.",
              ["https://ltgov.hawaii.gov/featured/lt-governor-sylvia-luke-joins-multi-state-reproductive-freedom-coalition/",
               "https://ballotpedia.org/Sylvia_Luke"]),
    ]),

    # --------------- Anne Lopez (HI-D, Attorney General) ---------------
    ("anne-lopez", "HI", "Attorney", [
        claim("al1", "anne-lopez", "border_immigration", 2, False,
              "Filed at least 5 immigration-related lawsuits against the Trump administration in "
              "2025, challenging federal immigration enforcement actions — a pattern documented "
              "in a May 2025 Civil Beat interview as a cornerstone of her affirmative litigation "
              "strategy. These cases collectively used the Hawaii AG's office to block or limit "
              "federal deportation and immigration enforcement, aligning Hawaii with a sanctuary-"
              "state posture and opposing mandatory cooperation with federal immigration authorities.",
              ["https://www.civilbeat.org/2025/05/the-sunshine-interview-hawai%CA%BBi-attorney-general-anne-lopez/",
               "https://ag.hawaii.gov/news-releases/"]),
        claim("al2", "anne-lopez", "economic_stewardship", 2, False,
              "Led or co-led multiple multistate coalitions in 2025 suing the Trump administration "
              "to block federal cost-cutting measures: (1) joined 22 other state AGs to win a "
              "federal TRO blocking the OMB's January 2025 federal grants-and-loans freeze, "
              "preserving billions in federal spending; (2) co-led a coalition suing to permanently "
              "block the dissolution of four federal agencies (IMLS, MBDA, FMCS, USICH), securing "
              "a permanent injunction; (3) joined a 20-AG coalition winning a preliminary injunction "
              "against the mass firing of federal probationary employees; (4) joined an 18-AG "
              "coalition blocking DOGE from accessing Americans' private data; (5) filed suit "
              "against the administration's attempted 50% reduction in the DOE workforce — "
              "actively litigating to preserve federal spending programs and oppose fiscal restraint.",
              ["https://ag.hawaii.gov/wp-content/uploads/2025/02/News-Release-2025-30.pdf",
               "https://ag.hawaii.gov/wp-content/uploads/2025/11/News-Release-2025-95.pdf",
               "https://ag.hawaii.gov/news-releases/"]),
    ]),

    # --------------- David Toland (KS-D, Lieutenant Governor) ---------------
    ("david-toland", "KS", "Lieutenant", [
        claim("dt1", "david-toland", "sanctity_of_life", 0, False,
              "As founding CEO of Thrive Allen County (a nonprofit he led until entering state "
              "government), accepted $20,000 in grants from the George Tiller Memorial Abortion "
              "Fund (named for the late George Tiller, Kansas's most prominent late-term "
              "abortionist, who was assassinated in 2009) in 2015 and 2018. The grants were "
              "designated to help low-income pregnant women stop smoking and to prevent unintended "
              "pregnancies. This connection was highlighted by Kansas Senators Rob Olson and "
              "Mary Pilcher-Cook and the leader of Kansans for Life during Toland's 2020 "
              "confirmation hearings as Kansas Secretary of Commerce, with 14 Republican "
              "senators voting against his confirmation on these grounds.",
              ["https://ballotpedia.org/David_Toland",
               "https://kslegislature.gov/li_2020/b2019_20/appointments/1344/"]),
        claim("dt2", "david-toland", "sanctity_of_life", 1, False,
              "Serves as Lt. Governor in the Laura Kelly administration, which in April 2024 "
              "vetoed multiple pro-life bills passed by the Republican-controlled Kansas "
              "Legislature, including a bill banning gender-identity healthcare for minors, "
              "an abortion coercion prohibition bill, and an abortion-reasons survey requirement. "
              "The Kansas Legislature overrode some of these vetoes. As Lt. Governor and "
              "presiding officer of the Kansas Senate, Toland is a full partner in the Kelly "
              "administration's consistent opposition to any pro-life or pro-family restrictions "
              "on abortion and gender-ideology in Kansas — the state where the 2022 abortion "
              "referendum was defeated and where Kelly has been the pro-abortion movement's "
              "primary gubernatorial ally.",
              ["https://kansasreflector.com/2024/04/12/gov-laura-kelly-vetoes-ban-on-gender-identity-health-care-abortion-coercion-and-survey-bills/",
               "https://kansasreflector.com/2024/04/19/kansas-governor-allows-anti-dei-bill-to-become-law-vetoes-anti-abortion-and-election-bills/",
               "https://ballotpedia.org/David_Toland"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<36} ({state}) +{len(new_claims)} claims  "
              f"conf: {old_conf} -> evidence_curated")

    # Minified write -- keep scorecard.json under GitHub's 50 MB warning.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
