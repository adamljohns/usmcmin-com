#!/usr/bin/env python3
"""Enrichment batch 529: 12 new claims across 5 sitting U.S. Senators.

Targets: Eric Schmitt (MO-R), John Kennedy (LA-R), Dave McCormick (PA-R),
Jerry Moran (KS-R), Mitch McConnell (KY-R) — bottom-of-alphabet states
with evidence_curated confidence and 5-6 existing claims. Adds 2-3 distinct
new-category claims per target drawn from 2022-2026 voting records and
public statements.

Sources: govtrack.us, congress.gov, kennedy.senate.gov, schmitt.senate.gov,
mccormick.senate.gov, moran.senate.gov, thehill.com, ballotpedia.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ---------------- Eric Schmitt (MO-R, US Senator) ----------------
    ("eric-schmitt", "MO", "Senator", [
        claim("es3", "eric-schmitt", "election_integrity", 0, True,
              "Schmitt has been a persistent champion of the SAVE America Act, appearing on Fox News multiple times calling for its passage and releasing press releases titled 'Senator Schmitt Blasts Democrats' Voter ID Hypocrisy' and 'Calls for Passage of the SAVE America Act.' The bill requires documentary proof of U.S. citizenship and photo ID to register and vote in federal elections. In 2026, Schmitt introduced a substitute amendment to the SAVE America Act citing Trump priorities — proof of citizenship, keeping men out of women's sports, and banning gender surgeries on minors — and stated that over 80 percent of Americans support voter ID, including more than 70 percent of Democrats.",
              ["https://www.schmitt.senate.gov/media/press-releases/senator-schmitt-blasts-democrats-voter-id-hypocrisy-calls-for-passage-of-the-save-america-act-on-fox-news/",
               "https://www.schmitt.senate.gov/media/press-releases/schmitt-to-introduce-amendment-to-save-america-act-following-through-on-trump-priorities/"]),
        claim("es4", "eric-schmitt", "foreign_policy_restraint", 1, True,
              "Schmitt voted NAY on H.R.815, the $95 billion National Security Supplemental (Senate Vote #154, April 23, 2024, 79-18), which included approximately $61 billion in military and security assistance for Ukraine. He was among 18 senators voting No. Schmitt spoke on the Senate floor 'at length against funding Ukraine without securing the border,' and issued a formal statement that he opposed 'spending billions defending the Ukrainian border while nothing is done to secure America's own border.' He also called for each foreign-aid funding request to be separated and voted on individually.",
              ["https://www.schmitt.senate.gov/media/press-releases/senator-schmitt-statement-on-foreign-aid-supplemental-vote/",
               "https://www.govtrack.us/congress/votes/118-2024/s154"]),
        claim("es5", "eric-schmitt", "biblical_marriage", 2, True,
              "Schmitt introduced a substitute amendment to the SAVE America Act in 2026 that explicitly included provisions protecting women's sports from biological males and banning transgender surgeries on minors. He stated on the record: 'we think men should not be able to compete in women's sports, and we should stop and ban the transgender mutilation of our kids.' As Missouri Attorney General, Schmitt also participated in a multistate coalition of Republican AGs suing the Biden administration's Department of Education over its LGBTQ+ guidance mandating pro-transgender policies in schools.",
              ["https://www.schmitt.senate.gov/media/press-releases/schmitt-to-introduce-amendment-to-save-america-act-following-through-on-trump-priorities/",
               "https://ballotpedia.org/Eric_Schmitt"]),
    ]),

    # ---------------- John Kennedy (LA-R, US Senator) ----------------
    ("john-kennedy", "LA", "Senator", [
        claim("jk6", "john-kennedy", "election_integrity", 0, True,
              "Kennedy co-introduced legislation with Sen. Mike Lee in January 2025 requiring documentary proof of U.S. citizenship when registering to vote in federal elections and ordering removal of non-citizens from voter rolls. In March 2026, Kennedy reaffirmed support for the SAVE America Act 'unconditionally' in a Senate floor speech and forced a vote during the reconciliation debate to insert SAVE Act voter-ID and proof-of-citizenship provisions into the DHS funding bill. Kennedy's amendment failed 48-50, but he called it 'a basic requirement' of legitimate self-government.",
              ["https://www.kennedy.senate.gov/public/2025/1/kennedy-lee-lead-bill-to-require-proof-of-citizenship-when-registering-voters-remove-foreign-nationals-from-voter-rolls",
               "https://www.kennedy.senate.gov/public/2026/3/washington-sen-john-kennedy-r-la-today-reaffirmed-his-support-for-the-save-america-act-and-called-for-the-use-of-another-reconciliation-bill-to-pass-the-legislation-in-a-speech-on-the-u-s-senate-floor-key-excerpts-of-the-speech-are-below-mr-president-i-would-like-to-talk-for-a-few-mi"]),
        claim("jk7", "john-kennedy", "family_child_sovereignty", 0, True,
              "Kennedy wrote an op-ed in the Daily Advertiser (March 2024) titled 'Congress must support parents who protect their children from irreversible gender procedures,' condemning activists who pressure parents to approve 'harmful drugs and surgeries' on gender-confused minors. He co-sponsored the Families' Rights and Responsibilities Act, which empowers parents to defend themselves legally when government bureaucrats push cross-sex medical interventions on their children. Kennedy commended the Louisiana legislature for outlawing gender procedures on minors and urged Congress to follow.",
              ["https://www.kennedy.senate.gov/public/2024/3/congress-must-support-parents-who-protect-their-children-from-irreversible-gender-procedures",
               "https://www.kennedy.senate.gov/public/press-releases?id=C7CC5C64-AA0A-4463-8250-B8386791F1DE"]),
        claim("jk8", "john-kennedy", "biblical_marriage", 2, True,
              "Kennedy has been an outspoken opponent of transgender ideology. In February 2024, he delivered Senate remarks titled 'Kennedy speaks out against radical transgender activism: We know this agenda is dangerous,' calling transgender ideology a direct threat to children and families. He earned the Family Research Council's 'True Blue' award with a perfect 100% scorecard rating for both 2020 and 2021, reflecting an unblemished record on faith, family, and freedom issues including opposition to LGBTQ ideological mandates.",
              ["https://www.kennedy.senate.gov/public/2024/2/kennedy-speaks-out-against-radical-transgender-activism-we-know-this-agenda-is-dangerous",
               "https://www.kennedy.senate.gov/public/2022/4/kennedy-scores-100-percent-on-family-research-council-s-2020-and-2021-score-cards"]),
    ]),

    # ---------------- Dave McCormick (PA-R, US Senator) ----------------
    ("dave-mccormick", "PA", "Senator", [
        claim("dm3", "dave-mccormick", "election_integrity", 0, True,
              "McCormick gave two Senate floor speeches urging passage of the SAVE America Act in 2026, citing his own 950-vote loss in the 2022 Pennsylvania Senate race as evidence for why only verified citizens should cast ballots. He called for documentary proof of citizenship and photo ID, stating that 'Voter ID is an 80-20 issue,' with Pew Research showing 95 percent of Republicans and 71 percent of Democrats in support. He cited the indictment of an illegal immigrant named Mahady Sacko for voting in seven federal elections, including 2024, as a case study for why the bill was needed.",
              ["https://www.mccormick.senate.gov/news/remarks/save-america-speech-by-u-s-senator-david-h-mccormick-r-pa/",
               "https://www.mccormick.senate.gov/news/remarks/second-save-america-speech-by-u-s-senator-david-h-mccormick-r-pa/"]),
        claim("dm4", "dave-mccormick", "economic_stewardship", 2, False,
              "Despite publicly stating that 'the federal government is too big and spends too much, and the debt and deficit must be reined in,' McCormick voted YES on the One Big Beautiful Bill Act (Senate 51-50 with Vice President J.D. Vance casting the tie-breaking vote, July 1, 2025), signed into law July 4, 2025. The CBO scored the bill as adding approximately $3.3 trillion to the national debt over 10 years, making it among the largest deficit increases in recent history. McCormick praised the bill as preventing 'the largest tax increase in American history' and delivering 'continued tax relief to millions of Pennsylvania families.'",
              ["https://www.mccormick.senate.gov/press-releases/senator-dave-mccormick-statement-on-senate-passage-of-the-one-big-beautiful-bill-act/",
               "https://ballotpedia.org/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---------------- Jerry Moran (KS-R, US Senator) ----------------
    ("jerry-moran", "KS", "Senator", [
        claim("jm3", "jerry-moran", "foreign_policy_restraint", 1, False,
              "Moran voted YES on H.R.815, the $95 billion National Security Supplemental (Senate Vote #154, April 23, 2024, 79-18), which included approximately $61 billion in military and security assistance for Ukraine. Moran spoke on the Senate floor in support, arguing: 'It would be naive to send aid to Israel but take a pass on supporting Ukraine, Taiwan or our other allies,' and stated that 'there is no path forward for Ukraine, there is no path forward for Israel or for Taiwan if the United States of America disengages in the world.' His remarks endorsed open-ended U.S. military support for overseas conflicts not authorized under Article I war powers.",
              ["https://www.moran.senate.gov/public/index.cfm/2024/4/sen-moran-speaks-on-the-senate-floor-regarding-the-national-security-supplemental",
               "https://www.govtrack.us/congress/votes/118-2024/s154"]),
        claim("jm4", "jerry-moran", "border_immigration", 1, True,
              "Moran voted YES on S.5, the Laken Riley Act (Senate Vote #7, January 20, 2025, passed 64-35), the first bill signed into law in the 119th Congress (January 29, 2025). The act requires DHS to mandatorily detain and initiate removal proceedings against illegal immigrants arrested for burglary, theft, larceny, shoplifting, assault of a law enforcement officer, or any crime resulting in death or serious bodily injury. It also authorizes state attorneys general to sue the federal government for failures to enforce immigration law.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Mitch McConnell (KY-R, US Senator) ----------------
    ("mitch-mcconnell", "KY", "Senator", [
        claim("mm3", "mitch-mcconnell", "border_immigration", 1, True,
              "McConnell voted YES on S.5, the Laken Riley Act (Senate Vote #7, January 20, 2025, passed 64-35), signed into law January 29, 2025. The law requires ICE to mandatorily detain and initiate removal proceedings against undocumented immigrants arrested for theft, burglary, larceny, shoplifting, assault of a law enforcement officer, or crimes resulting in death or serious bodily injury — and grants state AGs standing to sue the federal government for immigration enforcement failures.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
        claim("mm4", "mitch-mcconnell", "biblical_marriage", 1, True,
              "McConnell voted NAY on H.R.8404, the Respect for Marriage Act (Senate Vote #362, November 29, 2022, passed 61-36), which repealed the Defense of Marriage Act and codified federal recognition of same-sex and interracial marriages. McConnell was among the 36 senators — all Republicans — who voted against the bill, opposing federal recognition of same-sex marriage and the repeal of DOMA. The 12 Republicans who voted yes included Collins, Portman, Tillis, Romney, Murkowski, and Blunt; McConnell was not among them.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022"]),
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
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
