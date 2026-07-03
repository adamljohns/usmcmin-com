#!/usr/bin/env python3
"""Enrichment batch 546: hand-curated claims for 5 Tennessee State Senators.

All archetype_curated federal senators/reps are exhausted; this batch moves
to the archetype_party_default state-senator tier, taking the first 5 entries
from the reverse-alpha (WY→TX→TN) bucket.

Targets (all TN R State Senators, 0 prior claims):
  Tom Hatcher (SD-2), Shane Reeves (SD-14), Rusty Crowe (SD-3),
  Richard Briggs (SD-7), Paul Rose (SD-32).

Sources: ballotpedia.org, en.wikipedia.org, legiscan.com, tn.gov,
tnreportcard.org, tennesseelookout.com, paulroseforsenate.com, axios.com,
justfacts.votesmart.org.

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
    # ---------------- Tom Hatcher (TN-2, State Senator, R) ----------------
    ("tom-hatcher", "TN", "State Senator", [
        claim("th1", "tom-hatcher", "sanctity_of_life", 0, False,
              "In the 2025 session of the 114th Tennessee General Assembly, Hatcher voted in favor of a bill that expanded medical exceptions to Tennessee's near-total abortion ban — a vote scored by the TN Legislative Report Card (TLRC) as 'weakening Tennessee's pro-life protections,' departing from a strict life-from-conception standard.",
              ["https://tnreportcard.org/senators/tn-sd2-hatcher/",
               "https://tennesseelookout.com/2025/02/25/tennessee-republicans-sponsor-abortion-ban-exception-bill/"]),
        claim("th2", "tom-hatcher", "self_defense", 0, True,
              "A Republican state senator representing Blount County (District 2), East Tennessee's most conservative region; as a member of the TN Senate Republican supermajority he carries forward the caucus's unanimous support for the state's 2021 permitless-carry law (HB786/SB765), which removed the permit requirement for eligible adults to carry handguns.",
              ["https://ballotpedia.org/Tom_Hatcher",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
    ]),

    # ---------------- Shane Reeves (TN-14, State Senator, R) ----------------
    ("shane-reeves", "TN", "State Senator", [
        claim("sr1", "shane-reeves", "biblical_marriage", 2, True,
              "Voted for Tennessee SB1 (February 13, 2023, passed 26-6), the first state law banning gender-affirming medical care — puberty blockers, cross-sex hormones, and surgeries — for minors under 18. The law was later the subject of United States v. Skrmetti (2025), upheld by the U.S. Supreme Court.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/bill/SB0001/2023",
               "https://en.wikipedia.org/wiki/United_States_v._Skrmetti"]),
        claim("sr2", "shane-reeves", "biblical_marriage", 4, True,
              "Voted for SB1440/HB0239 (2023), which codified 'sex' in Tennessee law as 'a person's immutable biological sex as determined by anatomy and genetics existing at the time of birth,' barring transgender individuals from changing sex markers on government IDs — opposed by the Human Rights Campaign as codifying discrimination.",
              ["https://www.axios.com/2023/03/14/tennessee-senate-bill-transgender-identity",
               "https://www.hrc.org/press-releases/breaking-tennessee-senate-passes-bill-to-codify-discrimination-against-lgbtq-people-into-law"]),
        claim("sr3", "shane-reeves", "biblical_marriage", 0, True,
              "Opposes same-sex marriage as a matter of policy, per the 2024 Tennessee Lookout voter guide for State Senate District 14.",
              ["https://tennesseelookout.com/race-details/state-senate-district-14/",
               "https://ballotpedia.org/Shane_Reeves"]),
    ]),

    # ---------------- Rusty Crowe (TN-3, State Senator, R) ----------------
    ("rusty-crowe", "TN", "State Senator", [
        claim("rc1", "rusty-crowe", "self_defense", 0, True,
              "A longtime advocate of gun rights who supports allowing citizens to carry concealed firearms without a government permit (per Project Vote Smart). Served during Tennessee's passage of HB786/SB765 (2021), the permitless carry law allowing eligible adults to carry handguns without a permit — signed by Governor Lee April 2021.",
              ["https://justfacts.votesmart.org/candidate/24342/rusty-crowe",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
        claim("rc2", "rusty-crowe", "christian_liberty", 0, True,
              "Project Vote Smart records that Crowe supports the public display of the Ten Commandments in public schools, reflecting a commitment to religious expression in civic institutions — consistent with the christian liberty rubric.",
              ["https://justfacts.votesmart.org/candidate/24342/rusty-crowe",
               "https://ballotpedia.org/Rusty_Crowe"]),
        claim("rc3", "rusty-crowe", "sanctity_of_life", 0, True,
              "Voted for SB600 (March 13, 2023, passed 27-6 in the Tennessee Senate), prohibiting local governments from expending funds to assist any person in obtaining a criminal abortion, reinforcing Tennessee's statewide near-total abortion ban enacted through the Human Life Protection Act.",
              ["https://tnreportcard.org/senators/tn-sd03-crowe/",
               "https://legiscan.com/TN/people/rusty-crowe/id/7282"]),
    ]),

    # ---------------- Richard Briggs (TN-7, State Senator, R) ----------------
    ("richard-briggs", "TN", "State Senator", [
        claim("rb1", "richard-briggs", "sanctity_of_life", 0, True,
              "Voted for Tennessee's Human Life Protection Act (2022), which enacted a near-total statewide abortion ban effective August 25, 2022, thirty days after Roe v. Wade was overturned — passing the Senate with all 27 Republican members voting yes.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Tennessee",
               "https://ballotpedia.org/Richard_Briggs_(Tennessee)"]),
        claim("rb2", "richard-briggs", "biblical_marriage", 2, True,
              "Voted for Tennessee SB1 (February 13, 2023, passed 26-6 in the Senate), banning gender-affirming medical care for minors under 18, a major rejection of transgender ideology in public health policy.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/bill/SB0001/2023"]),
    ]),

    # ---------------- Paul Rose (TN-32, State Senator, R) ----------------
    ("paul-rose", "TN", "State Senator", [
        claim("pr1", "paul-rose", "family_child_sovereignty", 0, True,
              "Sponsored SB1971 (2024, 113th GA), signed into law July 1, 2024: criminalizes recruiting, harboring, or transporting an un-emancipated pregnant minor to obtain an abortion without written notarized parental consent. Rose said the bill protects parents' 'God-given rights to protect their minors.'",
              ["https://legiscan.com/TN/bill/SB1971/2023",
               "https://tennesseelookout.com/2024/04/11/senate-passes-bill-making-it-a-crime-to-aid-a-minor-seeking-an-abortion/"]),
        claim("pr2", "paul-rose", "sanctity_of_life", 0, True,
              "Sponsored the 'Every Mom Matters Act' (SB1222/HB1425, 112th GA, 2021-2022), requiring abortion providers to counsel patients on available anti-poverty resources and state assistance programs as alternatives before proceeding — a pro-life measure aimed at reducing abortion demand.",
              ["https://legiscan.com/TN/bill/SB1222/2021",
               "https://legiscan.com/TN/people/paul-rose/id/21328"]),
        claim("pr3", "paul-rose", "self_defense", 0, True,
              "Describes himself on his official campaign platform as 'a strong believer in less government and a staunch defender of our 2nd Amendment.' Voted with his caucus for Tennessee's 2021 permitless carry law (HB786/SB765), removing the permit requirement for eligible adults to carry handguns.",
              ["https://www.paulroseforsenate.com/about/",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
