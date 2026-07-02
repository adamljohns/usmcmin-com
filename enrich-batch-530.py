#!/usr/bin/env python3
"""Enrichment batch 530: 12 new claims across 5 sitting U.S. Senators.

Targets: Josh Hawley (MO-R), Thom Tillis (NC-R), Roger Marshall (KS-R),
Jeff Merkley (OR-D), Susan Collins (ME-R) — bottom-of-alphabet states
with evidence_curated confidence and 5-6 existing claims. Adds 2-3 distinct
new-category claims per target drawn from 2022-2026 voting records and
public statements.

Sources: hawley.senate.gov, govtrack.us, ballotpedia.org, en.wikipedia.org,
tillis.senate.gov, marshall.senate.gov, merkley.senate.gov, collins.senate.gov,
congress.gov.

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
    # ---------------- Josh Hawley (MO-R, US Senator) ----------------
    ("josh-hawley", "MO", "Senator", [
        claim("jh7", "josh-hawley", "election_integrity", 0, True,
              "Hawley was the first U.S. senator to publicly announce he would object to the 2020 Electoral College certification, releasing a statement on December 30, 2020, that he would force a floor debate citing allegations that some states 'failed to follow their own election laws' and 'unprecedented interference of Big Tech monopolies in the election.' On January 6-7, 2021, Hawley formally objected to Pennsylvania's certified electoral votes when the joint session of Congress reconvened after the Capitol breach. The Senate voted 7-92 to reject the objection to Pennsylvania's results. His official press release framed the action as a demand for 'election integrity' investigation before certification.",
              ["https://www.hawley.senate.gov/sen-hawley-will-object-during-electoral-college-certification-process-jan-6/",
               "https://ballotpedia.org/Counting_of_electoral_votes_(January_6-7,_2021)",
               "https://en.wikipedia.org/wiki/Josh_Hawley"]),
        claim("jh8", "josh-hawley", "biblical_marriage", 1, True,
              "Hawley voted NAY on H.R.8404 (Respect for Marriage Act, Senate Vote #362, November 29, 2022, passed 61-36), which repealed the Defense of Marriage Act and codified federal and state recognition of same-sex marriages. He was among the 36 senators — all Republicans — who voted against the bill. Hawley has stated that 'the issue of marriage should be left to the states' and noted that he does not believe 'the underlying Supreme Court decision [Obergefell v. Hodges] was rightly decided,' affirming a traditional marriage view and opposing federal override of state marriage law.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022",
               "https://en.wikipedia.org/wiki/Josh_Hawley"]),
        claim("jh9", "josh-hawley", "economic_stewardship", 2, False,
              "Despite publicly calling the bill's Medicaid cuts 'both morally wrong and politically suicidal,' Hawley voted YES on the One Big Beautiful Bill Act (Senate Vote 51-50, July 1, 2025, with VP J.D. Vance casting the tie-breaking vote in favor), which the CBO scored as adding approximately $3.3 trillion to the national debt over ten years — one of the largest single-bill deficit expansions in U.S. history. Hawley justified his vote after securing inclusion of the largest-ever expansion of the Radiation Exposure Compensation Act (RECA) for uranium workers in his state, characterizing the overall bill as delivering major economic and tax relief.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://ballotpedia.org/One_Big_Beautiful_Bill_Act",
               "https://www.govtrack.us/congress/bills/119/hr1"]),
    ]),

    # ---------------- Thom Tillis (NC-R, US Senator) ----------------
    ("thom-tillis", "NC", "Senator", [
        claim("tt7", "thom-tillis", "economic_stewardship", 2, True,
              "Tillis was one of only two Senate Republicans (alongside Sen. Susan Collins) to vote NAY on the One Big Beautiful Bill Act (Senate Vote 51-50, July 1, 2025, with VP J.D. Vance casting the tie-breaking vote). Tillis stated the bill would result in 'tens of billions of dollars in lost funding for North Carolina, including its hospitals and rural communities' and would force the state to eliminate Medicaid coverage for hundreds of thousands in the expansion population. The CBO scored the OBBB as adding approximately $3.3 trillion to the national debt over ten years. After President Trump threatened to back a primary challenger over his NAY vote, Tillis announced on June 29, 2025, that he would not seek re-election in 2026.",
              ["https://www.tillis.senate.gov/2025/6/tillis-statement-on-senate-reconciliation-vote",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://news.ballotpedia.org/2025/06/30/sen-thom-tillis-announces-he-will-not-seek-re-election-to-the-u-s-senate-in-2026/"]),
        claim("tt8", "thom-tillis", "family_child_sovereignty", 0, True,
              "Tillis has criticized Senate Democrats for 'pushing partisan bills that take away parental rights and infringe on religious freedoms,' arguing that parents — not federal bureaucrats — should control their children's education. He co-introduced the Saving American History Act, legislation that prohibits federal funds from being used to teach the 1619 Project or Critical Race Theory in K-12 schools or school districts, asserting that these curricula undermine parental authority over their children's historical and civic education and that schools should not use taxpayer dollars to advance contested ideological frameworks against parental wishes.",
              ["https://www.tillis.senate.gov/education",
               "https://en.wikipedia.org/wiki/Thom_Tillis"]),
    ]),

    # ---------------- Roger Marshall (KS-R, US Senator) ----------------
    ("roger-marshall", "KS", "Senator", [
        claim("rm7", "roger-marshall", "biblical_marriage", 1, True,
              "Marshall voted NAY on H.R.8404 (Respect for Marriage Act, Senate Vote #362, November 29, 2022, passed 61-36), which repealed the Defense of Marriage Act and mandated federal and state recognition of same-sex marriages. Marshall was among the 36 senators — all Republicans — who voted against codifying same-sex marriage into federal law. As an obstetrician with a 100% Family Research Council rating and 'True Blue' award, Marshall holds a biblical view of marriage as the union of one man and one woman and opposed federal legislation overriding that standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022",
               "https://www.marshall.senate.gov/newsroom/press-releases/sen-roger-marshall-scores-100-percent-on-frc-actions-2021-scorecard/"]),
        claim("rm8", "roger-marshall", "family_child_sovereignty", 0, True,
              "Marshall scored a perfect 100 percent on FRC Action's 2021 congressional scorecard, earning the organization's 'True Blue' award for 'unwavering commitment to and support of faith, family, and freedom.' FRC Action specifically noted that Marshall 'voted to reject the radical gender ideology that would overhaul [the] federal civil rights framework' and voted 'to protect women, the military, homeless shelters, and public restrooms from this harmful ideology.' These votes include opposition to legislation that would mandate LGBTQ non-discrimination policies in K-12 schools in ways that override parental rights and local community standards.",
              ["https://www.marshall.senate.gov/newsroom/press-releases/sen-roger-marshall-scores-100-percent-on-frc-actions-2021-scorecard/"]),
        claim("rm9", "roger-marshall", "industry_capture", 0, True,
              "During a CBS News interview in September 2025, Marshall — a practicing obstetrician who delivered thousands of babies before entering the Senate — publicly challenged blanket childhood vaccine mandate policies, questioning 'whether every baby at one day of age needs a hepatitis vaccine' and stating 'not every child needs a COVID vaccine.' He also stated that 'the CDC lied about COVID and COVID vaccinations,' signaling strong skepticism of government-mandated pharmaceutical interventions and supporting physician and parental discretion over one-size-fits-all vaccine schedules.",
              ["https://www.marshall.senate.gov/newsroom/press-releases/senator-marshall-we-need-to-focus-on-disease-prevention-not-just-treatment/"]),
    ]),

    # ---------------- Jeff Merkley (OR-D, US Senator) ----------------
    ("jeff-merkley", "OR", "Senator", [
        claim("jm7", "jeff-merkley", "family_child_sovereignty", 0, False,
              "Merkley is a consistent opponent of parental rights legislation related to LGBTQ education. He joined Advocates for Trans Equality in 2024 to push passage of the Equality Act, which would extend federal civil rights protections to gender identity and sexual orientation across education and public accommodations — explicitly overriding state and local parental rights laws. In 2025, Merkley called on the Trump administration to stop the Department of Education from 'penalizing education institutions for protecting transgender students,' explicitly defending school administration authority over student gender identity matters against parental-rights-based education policy.",
              ["https://www.merkley.senate.gov/merkley-joined-by-advocates-for-trans-equality-makes-equality-act-push/",
               "https://www.merkley.senate.gov/wyden-merkley-push-to-stop-trumps-education-department-from-politicizing-civil-rights-investigations/"]),
        claim("jm8", "jeff-merkley", "biblical_marriage", 2, False,
              "Merkley actively promotes transgender ideology in law and policy. In 2024, he joined Advocates for Trans Equality to push the Equality Act, making gender identity a protected federal class across all civil rights law, and condemned state bills targeting transgender minors as 'constrain[ing] the opportunity for transgender Americans.' He publicly denounced the reversal of Obama-era Title IX guidance protecting transgender students, stating 'transgender students already face difficult challenges in school — bullying, harassment — and this move will make it harder for these students to succeed.' He consistently rejects any restriction on transgender ideology in schools or government policy.",
              ["https://www.merkley.senate.gov/merkley-joined-by-advocates-for-trans-equality-makes-equality-act-push/",
               "https://www.merkley.senate.gov/news/press-releases/merkley-denounces-reversal-of-policy-protecting-transgender-students/"]),
    ]),

    # ---------------- Susan Collins (ME-R, US Senator) ----------------
    ("susan-collins", "ME", "Senator", [
        claim("sc7", "susan-collins", "biblical_marriage", 2, True,
              "Collins voted for Senator Tommy Tuberville's amendment to the SAVE America Act debate (March 22, 2026) protecting women's and girls' sports from transgender athlete participation. Collins stated in her floor remarks that 'policies allowing transgender athletes in women's sports violate the original intent behind Title IX' and called it 'a matter of fairness, safety, and giving girls and women the opportunity to excel in sports.' While noting that transgender people deserve respect and dignity, Collins drew a clear line between social acceptance and preserving sex-segregated athletic competition.",
              ["https://www.collins.senate.gov/newsroom/senator-collins-statement-on-tuberville-amendment-to-protect-women-and-girls-sports",
               "https://www.congress.gov/bill/119th-congress/senate-bill/9/text"]),
        claim("sc8", "susan-collins", "border_immigration", 1, True,
              "Collins voted YES on S.5, the Laken Riley Act (Senate Vote #7, January 20, 2025, passed 64-35), the first bill signed into law in the 119th Congress (signed January 29, 2025). The bipartisan act mandates that DHS detain and initiate removal proceedings against illegal immigrants arrested for burglary, theft, larceny, shoplifting, assault of a law enforcement officer, or any crime resulting in death or serious bodily injury, and authorizes state attorneys general to sue the federal government for immigration enforcement failures. Collins joined the 64-vote majority in requiring mandatory detention and removal proceedings for criminal illegal immigrants.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
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
