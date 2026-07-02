#!/usr/bin/env python3
"""Enrichment batch 516: additional claims for 5 U.S. Senate candidates with 3 existing claims.

The archetype_curated 0-claim bucket is fully exhausted. This batch deepens
coverage for the lightest-evidence Senate candidates from bottom-of-alphabet
states (NM, NJ, NH x2, NC), adding 2 claims each in distinct rubric categories
not yet represented in each candidate's profile.

Targets: Mark Ronchetti (NM-R), Curtis Bashaw (NJ-R), Scott Brown (NH-R),
Chris Pappas (NH-D), Wiley Nickel (NC-D).
All claims cite >= 1 reliable source reflecting 2012-2026 public record.
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
    # ---------------- Mark Ronchetti (NM-R, 2026 U.S. Senate candidate) ----------------
    ("mark-ronchetti-senate-2026", "NM", "Senate", [
        claim("mr1", "mark-ronchetti-senate-2026", "election_integrity", 0, True,
              "During his 2020 Senate and 2022 gubernatorial campaigns, Ronchetti committed to requiring photo ID to vote and pledged to push for a statewide voter-ID law in New Mexico. He opposes the automatic mailing of ballots to all registered voters without a request, citing a high number of bad addresses in New Mexico's voter file, and has committed to fighting ballot harvesting. His campaign platform frames the goal as making it 'easy to vote and hard to cheat,' directly aligning with the rubric's voter-ID and anti-mass-mail-in standard.",
              ["https://markronchetti.com/issues/election-integrity/",
               "https://ballotpedia.org/Mark_Ronchetti"]),
        claim("mr2", "mark-ronchetti-senate-2026", "biblical_marriage", 0, True,
              "Ronchetti stated in a faith-based voter guide that 'governments should not discriminate against individuals, organizations, or small businesses because of their belief that marriage is only a union of one man and one woman' and pledged to 'protect the freedom of Christians to share the Gospel and to practice Biblical principles.' He was raised Catholic and his family attends Sagebrush Church in Albuquerque, grounding this position in explicit religious conviction. This directly affirms the rubric's one-man-one-woman definition of marriage.",
              ["https://ivoterguide.com/candidate/52474/race/6821/election/772",
               "https://senate.ontheissues.org/Senate/Mark_Ronchetti.htm"]),
    ]),

    # ---------------- Curtis Bashaw (NJ-R, 2024 nominee / 2026 Senate candidate) ----------------
    ("curtis-bashaw-nj-senate-2026", "NJ", "Senate", [
        claim("cb1", "curtis-bashaw-nj-senate-2026", "election_integrity", 0, True,
              "Bashaw's 2024 Senate campaign platform included a commitment to establishing uniform voter identification laws nationwide, positioning voter ID as a core election security plank and aligning with mainstream Republican election integrity proposals — placing him within the rubric's voter-ID standard.",
              ["https://ballotpedia.org/Curtis_Bashaw",
               "https://www.phillyvoice.com/election-results-new-jersey-primary-republicans-us-senate/"]),
        claim("cb2", "curtis-bashaw-nj-senate-2026", "biblical_marriage", 0, False,
              "Bashaw is an openly gay man who has been married to his husband for over twenty years and is the first openly gay Republican from New Jersey to seek federal office. He has publicly stated 'I'm a gay married man, I'm pro-choice,' and commented that he is 'far less worried about my rights being taken away by Donald Trump or the Republicans than I am about our businesses being crushed by the Democrats.' He does not oppose same-sex marriage and participates in one, directly rejecting the rubric's one-man-one-woman definition of marriage.",
              ["https://www.advocate.com/politics/gay-republican-senate-new-jersey",
               "https://epgn.com/2024/07/31/curtis-bashaw-nj-senate/",
               "https://www.insidernj.com/bashaw-republican-gay-and-pro-choice/"]),
    ]),

    # ---------------- Scott Brown (NH-R, 2026 U.S. Senate candidate) ----------------
    ("scott-brown-nh-senate", "NH", "Senate", [
        claim("sb1", "scott-brown-nh-senate", "self_defense", 1, False,
              "Following the Sandy Hook shooting in December 2012, Brown became the first Republican U.S. Senator to publicly endorse a federal assault weapons ban, as reported contemporaneously by NBC News and The Washington Post. While he later stated that AWBs are 'best left to the states,' he consistently supported Massachusetts' state-level assault weapons ban throughout his Senate tenure and 2014 New Hampshire Senate campaign, and opposed nationwide concealed-carry reciprocity legislation. His 2026 campaign has produced no clear reversal of these positions, placing him in opposition to the rubric's defense of unrestricted semi-automatic rifle ownership.",
              ["https://www.nbcnews.com/id/wbna50261015",
               "https://www.washingtonpost.com/news/the-fix/wp/2012/12/19/scott-brown-supports-federal-assault-weapons-ban/",
               "https://ontheissues.org/Domestic/Scott_Brown_Gun_Control.htm"]),
        claim("sb2", "scott-brown-nh-senate", "economic_stewardship", 2, True,
              "In his 2026 New Hampshire Senate campaign, Brown has identified the national debt and federal deficit as his top issues, stating directly: 'The debt and deficit are my top issues. I support a balanced budget, like we have in our states and we have in our homes.' He also supports a presidential line-item veto as a spending-control mechanism and, in a WKBK Radio interview, called the $40 trillion national debt 'unacceptable,' warning that 'if we don't start paying down our national debt, we're going to be in trouble' — positions that align with the rubric's anti-deficit/balanced-budget standard.",
              ["https://mykeenenow.com/news/219912-scott-brown-talks-border-security-national-debt-and-merrimack-controversy-on-wkbk-radio/",
               "https://townhall.com/tipsheet/amy-curtis/2026/04/13/nh-senate-candidate-scott-brown-talks-fiscal-discipline-but-his-record-tells-a-different-story-n2674381"]),
    ]),

    # ---------------- Chris Pappas (NH-D, 2026 U.S. Senate candidate / sitting U.S. Rep NH-01) ----------------
    ("chris-pappas", "NH", "Senate", [
        claim("cp1", "chris-pappas", "self_defense", 1, False,
              "Pappas voted YES on H.R. 1808, the Assault Weapons Ban of 2022 (passed 217-213 on July 29, 2022), legislation to ban the sale, manufacture, and transfer of certain semi-automatic rifles and high-capacity magazines. He also voted for the Federal Extreme Risk Protection Order Act of 2022 (a national red-flag framework) and the Bipartisan Safer Communities Act — the first major federal gun-control legislation in nearly 30 years. His 2018 campaign platform explicitly called for banning the AR-15, banning high-capacity magazines, and enacting a red-flag law, forming a consistent record directly opposing the rubric's defense of semi-automatic rifle ownership and opposition to red-flag confiscation orders.",
              ["https://pappas.house.gov/media/press-releases/pappas-votes-reinstate-federal-assault-weapon-ban",
               "https://pappas.house.gov/media/press-releases/pappas-helps-pass-gun-violence-protection-legislation"]),
        claim("cp2", "chris-pappas", "election_integrity", 0, False,
              "On July 10, 2024, Pappas voted NO on the Safeguard American Voter Eligibility (SAVE) Act (H.R. 8281), which would have required states to obtain documentary proof of U.S. citizenship when registering voters for federal elections (the bill passed 221-198). In his official statement, Pappas argued the law would impose 'undue burdens' on married women, military families, and seniors and characterized it as unnecessary federal interference in state election procedures. He also publicly advocated for no-excuse vote-by-mail in 2020, placing him in direct opposition to the rubric's voter-ID and anti-mass-mail-in standards.",
              ["https://pappas.house.gov/media/press-releases/pappas-statement-on-the-save-act",
               "https://nhjournal.com/pappas-kuster-vote-no-to-bipartisan-bill-requiring-proof-of-citizenship-to-vote/"]),
    ]),

    # ---------------- Wiley Nickel (NC-D, 2026 U.S. Senate candidate / former U.S. Rep NC-13) ----------------
    ("wiley-nickel-senate", "NC", "Senate", [
        claim("wn1", "wiley-nickel-senate", "self_defense", 1, False,
              "On February 1, 2023, Nickel co-sponsored H.R. 698, the Assault Weapons Ban of 2023, legislation to ban the manufacture, sale, transfer, and possession of semi-automatic assault weapons and large-capacity magazines. He also co-sponsored legislation to ban ghost guns and Ethan's Law requiring mandatory safe storage. He earned an 'F' rating from the NRA and publicly supports universal background checks, red-flag laws, and high-capacity magazine bans — a record of gun restrictions that directly opposes the rubric's defense of unrestricted semi-automatic rifle ownership and opposition to new gun-control legislation.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://www.govtrack.us/congress/bills/118/hr698"]),
        claim("wn2", "wiley-nickel-senate", "biblical_marriage", 4, False,
              "On June 21, 2023, Nickel co-sponsored H.R. 15, the Equality Act, legislation that would extend federal civil rights protections to prohibit discrimination on the basis of sexual orientation and gender identity across employment, housing, public accommodations, and education. He received a 94% score on the Human Rights Campaign Congressional Scorecard for the 118th Congress. These positions reflect active legislative support for institutionalizing LGBTQ identity protections across federal civil-rights law, directly opposing the rubric's standard against government promotion of LGBTQ ideology in schools and public policy.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/15/cosponsors",
               "https://www.hrc.org/resources/congressional-scorecard"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
