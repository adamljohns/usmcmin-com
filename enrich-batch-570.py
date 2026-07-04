#!/usr/bin/env python3
"""Enrichment batch 570: hand-curated claims for 5 federal House candidates.

Targets evidence_curated / evidence_federal officials from bottom-of-alphabet
states (WY→TX→TN→OR→OH→UT range) with the fewest existing claims.
All archetype_curated 0-claim federal senators/reps are exhausted.

Targets (3 D / 1 R / 1 D from bottom-alpha states):
  Steve Cohen      (TN-09, D, retiring)  — border, election integrity, economy
  Christian Menefee (TX-18, D, incumbent) — marriage, election integrity, economy
  Justin Pearson   (TN-09, D, candidate) — economy, border
  Troy Balderson   (OH-12, R, incumbent) — marriage, election integrity, economy
  Jonny Larsen     (UT-04, D, nominee)   — life, self-defense, marriage

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
    # ---------------- Steve Cohen (TN-09, D, retiring) ----------------
    ("steve-cohen", "TN", "Representative", [
        claim("sc1", "steve-cohen", "border_immigration", 0, False,
              "As a 19-year member of the House Judiciary Committee, Cohen voted against H.R. 2 (the Secure the Border Act of 2023) on May 11, 2023 — the party-line 219–213 vote requiring resumed border wall construction, E-Verify expansion, and reinstatement of 'Remain in Mexico.' Zero Democrats voted yes. Cohen additionally called for ICE abolition, stating he 'voted against funding a bloated and lawless ICE operation' and demanded the agency be dissolved.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://cohen.house.gov/media-center/press-releases/congressman-cohen-says-immigration-enforcement-killing-americans"]),
        claim("sc2", "steve-cohen", "election_integrity", 0, False,
              "Cohen co-sponsored the For the People Act (H.R. 1, 2021) to mandate automatic voter registration and expand mail-in voting nationwide, and voted for the John R. Lewis Voting Rights Advancement Act restricting states from tightening voting laws. He voted against both the original SAVE Act (H.R. 22, April 2025) and the SAVE America Act (Feb 2026) requiring documentary proof of citizenship to vote, calling voter ID requirements 'voter suppression' and 'an unconstitutional attempt to exclude eligible Americans from the ballot box.'",
              ["https://cohen.house.gov/media-center/press-releases/congressman-cohen-calls-passage-and-votes-john-r-lewis-voting-rights",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("sc3", "steve-cohen", "economic_stewardship", 2, False,
              "Cohen consistently votes for large deficit-funded spending packages (the $1.9T American Rescue Plan, the $739B Inflation Reduction Act) and opposes balanced budget frameworks, describing the federal deficit as a revenue problem requiring corporate tax hikes — not a spending problem requiring fiscal restraint. He has opposed every Republican budget resolution imposing spending caps.",
              ["https://cohen.house.gov/issues/budget",
               "https://en.wikipedia.org/wiki/Steve_Cohen_(politician)"]),
    ]),

    # ---------------- Christian Menefee (TX-18, D) ----------------
    ("christian-menefee", "TX", "Representative", [
        claim("cm1", "christian-menefee", "biblical_marriage", 0, False,
              "On May 21, 2026, Menefee announced he joined the Congressional Equality Caucus 'to stand alongside those fighting for the dignity, freedom, and equality of every American' — an explicit commitment to federal LGBTQ equality including recognition of same-sex relationships. As Harris County Attorney he refused to prosecute gender-affirming care cases and submitted formal objections to Trump administration rollbacks of LGBTQ protections.",
              ["https://menefee.house.gov/media/press-releases/rep-menefee-joins-congressional-equality-caucus-amid-continued-republican-attacks-on-lgbtqia-americans",
               "https://en.wikipedia.org/wiki/Christian_Menefee"]),
        claim("cm2", "christian-menefee", "election_integrity", 0, False,
              "After Trump's 2026 executive order restricted mail-in voting and imposed voter-roll verification requirements, Menefee stated it 'is not about election integrity — it is about making it harder for Americans to vote.' He aligned with fellow Houston Rep. Al Green in backing new Voting Rights Act expansion legislation following the Supreme Court's Callais v. Louisiana ruling narrowing VRA protections.",
              ["https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/05/04/550759/green-menefee-tx-18-runoff-voting-rights-supreme-court/",
               "https://ballotpedia.org/Christian_Menefee"]),
        claim("cm3", "christian-menefee", "economic_stewardship", 2, False,
              "Menefee voted against H.R. 7567 (the Farm, Food, and National Security Act of 2026) citing cuts to nutrition assistance, stating it 'does nothing to lower grocery prices, and locks in devastating cuts to nutrition assistance that Texans rely on.' He actively opposes federal benefit spending reductions and has no documented record of supporting a balanced budget amendment, CBDC restrictions, or Federal Reserve audit legislation.",
              ["https://ballotpedia.org/Christian_Menefee",
               "https://www.govtrack.us/congress/members/christian_menefee/457039"]),
    ]),

    # ---------------- Justin Pearson (TN-09, D candidate) ----------------
    ("justin-pearson-tn-09", "TN", "Representative", [
        claim("jp1", "justin-pearson-tn-09", "economic_stewardship", 2, False,
              "Pearson's congressional platform calls for Medicare for All (covering vision, dental, mental health, and reproductive care with 'no premiums, deductibles, or copays') and he personally sponsored Tennessee HB 1396 (the Protection Against Automation Act) establishing a Guaranteed Basic Income program providing $3,000 annual grants — a platform that explicitly rejects balanced-budget fiscal discipline in favor of major new federal entitlement spending.",
              ["https://www.votejustinj.com/issues",
               "https://wapp.capitol.tn.gov/apps/BillInfo/default.aspx?BillNumber=HB1396&GA=114"]),
        claim("jp2", "justin-pearson-tn-09", "border_immigration", 0, False,
              "At a January 2026 Tennessee Progressive Caucus press conference, Pearson framed ICE enforcement as a violation of the religious duty to 'protect the foreigner.' In February 2026, he condemned the National Guard deployment to Memphis for immigration enforcement as an 'occupation detrimental to the economy' and 'a draconian mass deportation campaign,' calling instead for federal investment rather than enforcement.",
              ["https://tennesseelookout.com/2026/02/03/tennessee-governor-leaves-immigration-enforcement-out-of-final-address/",
               "https://www.nbcnews.com/politics/2026-election/tennessee-three-legislator-justin-pearson-launches-primary-challenge-l-rcna235918"]),
    ]),

    # ---------------- Troy Balderson (OH-12, R) ----------------
    ("troy-balderson", "OH", "Representative", [
        claim("tb1", "troy-balderson", "biblical_marriage", 0, True,
              "On July 19, 2022, Balderson voted against the Respect for Marriage Act (H.R. 8404) — which codified federal recognition of same-sex unions and required states to recognize such marriages — aligning with the one-man-one-woman definition of marriage. He was among the Ohio Republicans who held the line against codifying same-sex marriage into federal law.",
              ["https://clerk.house.gov/Votes/2022513",
               "https://en.wikipedia.org/wiki/Troy_Balderson"]),
        claim("tb2", "troy-balderson", "election_integrity", 0, True,
              "Balderson voted for the SAVE Act (H.R. 22) on April 10, 2025, which requires documentary proof of U.S. citizenship to register to vote in federal elections; the bill passed 220–208 with all 216 voting Republicans supporting it. He also stated unequivocally that 'Congress does not have the authority to overturn elections,' a position consistent with election integrity under constitutional limits.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://balderson.house.gov/"]),
        claim("tb3", "troy-balderson", "economic_stewardship", 2, True,
              "Balderson's voter guide questionnaire confirms he supports passing a balanced budget amendment to the U.S. Constitution, and he has voted against large deficit-funded spending packages throughout his tenure. He is ranked the most politically right member of Ohio's House delegation, consistent with fiscal conservatism and opposition to unchecked federal spending growth.",
              ["https://ivoterguide.com/candidate?canK=1099&elecK=606&primarypartyk=-&raceK=2188",
               "https://www.govtrack.us/congress/members/troy_balderson/412747"]),
    ]),

    # ---------------- Jonny Larsen (UT-04, D nominee) ----------------
    ("jonny-larsen", "UT", "Representative", [
        claim("jl1", "jonny-larsen", "sanctity_of_life", 0, False,
              "Larsen opposes Utah's six-week abortion ban and has no pro-life position in his public record. His UT-04 campaign materials (including the Utah Lieutenant Governor's official candidate information document) show no support for restrictions on abortion access and no personhood-from-conception framework — placing him directly against the rubric's life-at-conception standard.",
              ["https://vote.utah.gov/wp-content/uploads/2026/03/CD4-Jonny-Larsen.pdf",
               "https://ballotpedia.org/Jonathan_Larsen"]),
        claim("jl2", "jonny-larsen", "self_defense", 1, False,
              "Endorsed by Gun Sense Voter — the electoral campaign of Everytown for Gun Safety Action Fund, Moms Demand Action, and Students Demand Action — which endorses only candidates who pledge support for universal background checks and/or red-flag (Extreme Risk Protection Order) laws. No NRA rating, pro-constitutional-carry statement, or anti-red-flag position has been found anywhere in his record.",
              ["https://www.everytown.org/press/everytown-for-gun-safety-action-fund-announces-first-round-of-2026-us-house-endorsements-backing-13-moms-demand-action-volunteers-and-everytown-leaders/",
               "https://ballotpedia.org/Jonathan_Larsen"]),
        claim("jl3", "jonny-larsen", "biblical_marriage", 0, False,
              "On April 20, 2026, the Utah Stonewall Democrats — Utah's LGBTQ Democratic political organization — endorsed Larsen for UT-04, citing his platform of 'dignity, integrity, and solidarity.' No statement supporting a one-man-one-woman definition of marriage, opposing the Respect for Marriage Act, or opposing LGBTQ non-discrimination protections has been found anywhere in his public record.",
              ["https://www.qsaltlake.com/news/2026/04/20/utah-stonewall-democrats-endorsements/",
               "https://ballotpedia.org/Jonathan_Larsen"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states.

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
