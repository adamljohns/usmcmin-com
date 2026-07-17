#!/usr/bin/env python3
"""Enrichment batch 731: 4 NV Republican State Senators + 1 NM Republican State Senator, 10 claims.

archetype_curated federal senator/rep buckets exhausted; continuing with
archetype_party_default state senators from the bottom of the reverse-alpha
bucket (NV has 4 remaining unclaimed; NM is next).

Targets:
  John Ellison   (NV SD-19, Elko/northeastern NV, former Assembly member 2010-2022)
  Jeff Stone     (NV SD-20, Henderson/Clark County, former CA State Senator SD-28)
  Ira Hansen     (NV SD-14, Sparks/Washoe, former Assembly Speaker 2015-16)
  Carrie Buck    (NV SD-5, Henderson area, educator/principal, running for CD-1)
  Jay C. Block   (NM SD-12, Rio Rancho, Lt. Col. USAF ret., freshman Jan 2025)

Key sourced votes/positions:
  SB217 (NV 2025, IVF insurance mandate) — final floor vote 18-3; NAY bloc:
    Ellison (R-Elko), Stone (R-Henderson), Titus (R-Wellington). Lombardo vetoed.
    Source: thenevadaindependent.com live session updates.
  SB156 (NV 2025, Special Counsel for Gun Violence appointed by AG) — passed
    Senate on party-line vote with all Republicans opposed; Lombardo vetoed.
    Source: leg.state.nv.us SB156 overview; thenevadaindependent.com session wrap.
  Jeff Stone — advocated for proof-of-citizenship requirement in Nevada's
    DMV automatic-voter-registration program and for statewide voter ID;
    supported Ballot Question 7 (voter ID initiative, Nov 2024).
    Source: thenevadaindependent.com "Freshman Orientation: Jeff Stone."
  Ira Hansen — on record as "100 percent for" rural Nevada sheriffs and
    counties taking a stand against gun control mandates, calling that
    civil disobedience "pretty darn American."
    Source: Las Vegas Review-Journal (Nye County sheriff gun-law story).
  Carrie Buck — publicly backed Ballot Question 7 (voter ID, 2024 general
    election); voted YES on AB383 (2023 NV, "Right to Reproductive Health Care
    Act") alongside Democrats, and supported an out-of-state abortion-seeker
    protection bill — two documented breaks on sanctity-of-life rubric.
    Sources: thenevadaglobe.com; thenevadaindependent.com "On the Record."
  Jay C. Block — publicly condemned HB9 (2025 NM, signed by Gov. Lujan Grisham)
    which bars local govts from contracting with ICE to detain civil immigration
    violators, saying it "killed 1,000 jobs in Torrance, Otero and Cibola
    counties" and gave the 30-day session an F grade because of it.
    Also called NM SB17 (2026, semi-auto rifle ban + dealer restrictions)
    "the worst mockery of the Second Amendment in the state's history";
    voted NAY in 21-17 party-line vote.
    Sources: santafenewmexican.com; sportsmensalliance.org; ballotpedia.org.
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
    # ------- John Ellison (SD-19, Elko/northeastern NV, R, Senate since Nov 2024; Assembly 2010-2022) -------
    ("john-ellison", "NV", "State Senator", [
        claim("je1", "john-ellison", "sanctity_of_life", 2, True,
              "Voted NAY on SB217 (2025 Nevada legislative session), the mandatory IVF "
              "insurance coverage bill authored by Senate Majority Leader Nicole Cannizzaro "
              "that would have required most private insurers and Medicaid to cover IVF "
              "treatments. The bill passed the Senate 18-3 on the final floor vote; the "
              "three NAY votes came from Republican Senators Ellison (Elko), Jeff Stone "
              "(Henderson), and Robin Titus (Wellington). Governor Lombardo subsequently "
              "vetoed the bill. Ellison's opposition aligns with the rubric's anti-embryo-"
              "discard position, since IVF routinely involves the creation and discarding "
              "of surplus embryos.",
              ["https://thenevadaindependent.com/article/live-updates-nevada-legislature-barrels-toward-end-of-session",
               "https://www.leg.state.nv.us/App/NELIS/REL/83rd2025/Bill/12292/Overview",
               "https://thenevadaindependent.com/article/2025-lombardo-veto-tracker-bipartisan-ballot-drop-box-bill-rejected"]),
        claim("je2", "john-ellison", "self_defense", 1, True,
              "Voted with the entire Republican Senate caucus against SB156 (2025 Nevada "
              "legislative session), which would have required the Nevada Attorney General "
              "to appoint a Special Counsel for the Prevention of Gun Violence, authorized "
              "state agencies to cooperate with that official, and established a "
              "state-funded gun-violence-prevention grant program. The bill passed the "
              "Senate on a strict party-line vote with all Republicans opposed. Ellison, "
              "who describes himself publicly as a 'fervent advocate for Second Amendment "
              "rights in Nevada,' was consistent with that record in opposing the measure. "
              "Governor Lombardo vetoed SB156.",
              ["https://www.leg.state.nv.us/App/NELIS/REL/83rd2025/Bill/12137/Overview",
               "https://thenevadaindependent.com/article/collective-bargaining-for-state-workers-major-gun-bill-advance-as-lawmakers-near-end-of-session",
               "https://ballotpedia.org/John_Ellison"]),
    ]),

    # ------- Jeff Stone (SD-20, Henderson/Clark County, R, Senate since Nov 2022; former CA State Senator SD-28) -------
    ("jeff-stone", "NV", "State Senator", [
        claim("jst1", "jeff-stone", "sanctity_of_life", 2, True,
              "Voted NAY on SB217 (2025 Nevada legislative session), the mandatory IVF "
              "insurance coverage bill that would have required most private insurers and "
              "Medicaid to cover in vitro fertilization treatments. The bill passed the "
              "Senate 18-3 on the final floor vote; Stone was one of only three senators "
              "to vote against it, alongside Senators John Ellison (R-Elko) and Robin "
              "Titus (R-Wellington). Governor Lombardo vetoed the bill. Stone's opposition "
              "aligns with the rubric's anti-embryo-discard position, as IVF routinely "
              "results in the creation and destruction of surplus human embryos.",
              ["https://thenevadaindependent.com/article/live-updates-nevada-legislature-barrels-toward-end-of-session",
               "https://www.leg.state.nv.us/App/NELIS/REL/83rd2025/Bill/12292/Overview",
               "https://thenevadaindependent.com/article/2025-lombardo-veto-tracker-bipartisan-ballot-drop-box-bill-rejected"]),
        claim("jst2", "jeff-stone", "election_integrity", 0, True,
              "Advocates for voter ID requirements in Nevada and has pushed for proof of "
              "citizenship to be required in Nevada's DMV automatic voter registration "
              "program. Stone, who served in the California State Senate before moving "
              "to Nevada, stated he is not opposed to motor-voter registration if proof "
              "of citizenship is required but said that without it 'you can't tell the "
              "registrar of voters this person is OK to vote.' He also expressed support "
              "for Ballot Question 7, the voter ID initiative on Nevada's November 2024 "
              "general election ballot, as a means of preventing noncitizens from voting. "
              "His positions align with the rubric's voter-ID and election-integrity "
              "standard.",
              ["https://thenevadaindependent.com/article/freshman-orientation-jeff-stone-has-been-a-senator-in-two-states",
               "https://ballotpedia.org/Jeff_Stone_(Nevada)"]),
    ]),

    # ------- Ira Hansen (SD-14, Sparks/Washoe County, R, Senate since Nov 2018; former Assembly Speaker 2015-16) -------
    ("ira-hansen", "NV", "State Senator", [
        claim("ih1", "ira-hansen", "self_defense", 1, True,
              "Voted with the entire Republican Senate caucus against SB156 (2025 Nevada "
              "legislative session), which would have required the Nevada Attorney General "
              "to appoint a Special Counsel for the Prevention of Gun Violence, authorized "
              "state agencies to cooperate with that official, and created a state-funded "
              "gun-violence-prevention grant program. The bill passed the Senate on a "
              "strict party-line vote with all Republicans opposed. Governor Lombardo "
              "subsequently vetoed SB156. As a longtime gun-rights advocate and talk show "
              "host representing a rural district (Washoe, Nye, Humboldt, Pershing, Lander, "
              "Mineral, and Esmeralda counties), Hansen's party-line opposition to any new "
              "gun-control infrastructure aligns with the rubric's position against "
              "magazine limits, red-flag laws, and related Second Amendment infringements.",
              ["https://www.leg.state.nv.us/App/NELIS/REL/83rd2025/Bill/12137/Overview",
               "https://thenevadaindependent.com/article/collective-bargaining-for-state-workers-major-gun-bill-advance-as-lawmakers-near-end-of-session",
               "https://thenevadaindependent.com/article/2025-lombardo-veto-tracker-bipartisan-ballot-drop-box-bill-rejected"]),
        claim("ih2", "ira-hansen", "self_defense", 0, True,
              "On record as a Second Amendment absolutist who expressed he was '100 percent "
              "for' rural Nevada counties and sheriffs taking a stand against gun control "
              "mandates imposed by the Democrat-controlled legislature, calling that civil "
              "disobedience 'pretty darn American.' Hansen — a longtime talk show host and "
              "columnist at the Sparks Tribune and Elko Daily Free Press, and former Nevada "
              "Assembly Speaker (2015-16 session) — made the remarks in the context of "
              "Nye County's sheriff publicly declaring she would not enforce Nevada's new "
              "background-check law (SB 143, 2019). His position reflects a consistent "
              "belief that Second Amendment rights are non-negotiable and that local law "
              "enforcement has a duty to refuse unconstitutional gun-control mandates — "
              "fully aligning with the rubric's constitutional-carry and pro-Second-"
              "Amendment-enforcement standard.",
              ["https://www.reviewjournal.com/news/politics-and-government/nevada/nye-county-sheriff-says-she-will-not-enforce-new-nevada-gun-law-1613155/",
               "https://ballotpedia.org/Ira_Hansen"]),
    ]),

    # ------- Carrie Buck (SD-5, Henderson/Las Vegas area, R, Senate since Nov 2020; career educator, Pinecrest Foundation) -------
    ("carrie-buck", "NV", "State Senator", [
        claim("cb1", "carrie-buck", "election_integrity", 0, True,
              "Publicly supported Ballot Question 7, the voter ID constitutional amendment "
              "on Nevada's November 2024 general election ballot, stating it would help "
              "prevent noncitizens from voting. When asked about election integrity, Buck "
              "said she would support the voter ID initiative, citing the need to "
              "safeguard elections against noncitizen participation. Ballot Question 7 "
              "would amend the Nevada Constitution to require voters to present photo ID "
              "at the polls, a measure the rubric's election-integrity standard — requiring "
              "voter ID and opposing mass mail-in ballots — directly supports.",
              ["https://thenevadaindependent.com/article/on-the-record-senate-district-5-candidates-carrie-buck-and-jennifer-atlas",
               "https://ballotpedia.org/Carrie_Buck_(Nevada)"]),
        claim("cb2", "carrie-buck", "sanctity_of_life", 0, False,
              "Voted YES on AB383 (2023 Nevada legislative session), the 'Right to "
              "Reproductive Health Care Act,' which enshrined access to 'reproductive "
              "health services, drugs, or devices' in Nevada statute, prohibited any "
              "governmental entity from limiting such access, and expanded Medicaid "
              "coverage for voluntary sterilization. The bill passed 16-5; Buck was one "
              "of the very few Republicans to vote in favor. Conservative groups including "
              "the Nevada Globe publicly condemned her vote, calling it a betrayal of the "
              "Republican platform and noting she was 'aligned with the pro-choice agenda.' "
              "Her support for AB383 places her outside the rubric's life-from-conception "
              "standard, which opposes codifying abortion-adjacent rights into law. Buck "
              "was also one of two Republicans to support a 2023 bill providing legal "
              "protections for individuals who travel to Nevada from other states to "
              "obtain abortions, a second documented break on the sanctity-of-life rubric.",
              ["https://thenevadaglobe.com/articles/senator-carrie-buck-votes-with-dems-on-abortion-bill/",
               "https://thenevadaindependent.com/article/on-the-record-senate-district-5-candidates-carrie-buck-and-jennifer-atlas",
               "https://ballotpedia.org/Carrie_Buck_(Nevada)"]),
    ]),

    # ------- Jay C. Block (NM SD-12, Rio Rancho/Sandoval County, R, Senate since Jan 2025; Lt. Col. USAF ret.) -------
    ("jay-c-block", "NM", "State Senator", [
        claim("jb1", "jay-c-block", "border_immigration", 2, True,
              "Publicly condemned HB9 (2025 New Mexico 30-day legislative session), a bill "
              "signed into law by Governor Michelle Lujan Grisham that prohibits any public "
              "body in New Mexico — including county governments — from entering into or "
              "renewing any intergovernmental services agreement to detain individuals for "
              "federal civil immigration violations, effectively barring local cooperation "
              "with ICE detention operations. Block stated: 'We just killed 1,000 jobs "
              "in Torrance County, Otero County and Cibola County,' referring to the "
              "three counties that house federal immigrant detention facilities that lost "
              "their contracts. He gave the 30-day session a grade of F specifically "
              "because of HB9 and posted the criticism on social media. His opposition "
              "to HB9 directly aligns with the rubric's anti-sanctuary position, which "
              "calls for full federal immigration enforcement cooperation and opposes "
              "policies that shield illegal immigrants from deportation.",
              ["https://www.santafenewmexican.com/news/legislature/the-roundhouse-report-senator-drops-f-bomb-no-not-that-one/article_0baea8a7-6de1-4b73-a098-fa9e9a4c9fb8.html",
               "https://www.nmlegis.gov/Sessions/25%20Regular/bills/house/HB0009.HTML",
               "https://ballotpedia.org/Jay_Block"]),
        claim("jb2", "jay-c-block", "self_defense", 1, True,
              "Called New Mexico SB17 (2026 regular session), which bans the sale of "
              "AK-47s, AR-15s, and other gas-operated semi-automatic rifles and imposes "
              "strict new regulations on firearms retailers, 'the worst mockery of the "
              "Second Amendment in the state's history.' Block stated on the Senate floor: "
              "'Instead of trying to hold violent and repeat criminals accountable, radical "
              "left Democrats are targeting law-abiding New Mexicans and small-business "
              "owners.' He also warned the bill would effectively end gun shows and shut "
              "down independent gun stores across New Mexico. Block voted NAY as part of "
              "a unified Republican opposition bloc (21-17 final vote with all Republicans "
              "opposed). Block is a retired United States Air Force lieutenant colonel "
              "(1989-2016) representing District 12 (Rio Rancho/Sandoval County).",
              ["https://www.santafenewmexican.com/news/local_news/anti-gun-trafficking-bill-would-hold-new-mexico-dealers-accountable/article_cdfda9b2-e3c8-4595-b5f7-90aa01b63d57.html",
               "https://sportsmensalliance.org/news/oppose-nm-sb17-gun-ban/",
               "https://ballotpedia.org/Jay_Block"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
