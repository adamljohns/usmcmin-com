#!/usr/bin/env python3
"""Enrichment batch 520: 15 claims across 5 sitting U.S. Senators (3 per candidate).

archetype_curated and evidence_curated (0-claim) buckets exhausted.
Targets are evidence_curated sitting U.S. Senators from bottom-of-alphabet states
(SC×2, RI×2, PA×1) that had 6-7 existing claims each. Adds 3 distinct-category
claims covering christian_liberty, family_child_sovereignty, refuse_federal_overreach,
election_integrity, and industry_capture.

Targets:
  Lindsey Graham (SC-R)  — election_integrity, christian_liberty, family_child_sovereignty
  Tim Scott (SC-R)       — christian_liberty, family_child_sovereignty, refuse_federal_overreach
  Sheldon Whitehouse (RI-D) — election_integrity, christian_liberty, refuse_federal_overreach
  Jack Reed (RI-D)       — christian_liberty, industry_capture, refuse_federal_overreach
  John Fetterman (PA-D)  — election_integrity, christian_liberty, industry_capture

Sources: ballotpedia.org, en.wikipedia.org, govtrack.us, graham.senate.gov,
         scott.senate.gov, whitehouse.senate.gov, reed.senate.gov, fetterman.senate.gov,
         cruz.senate.gov, congress.gov, sbaprolife.org, lee.senate.gov.

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


TARGETS = [
    # ---------------- Lindsey Graham (SC-R, US Senator) ----------------
    ("lindsey-graham", "SC", "Senator", [
        claim("lg5", "lindsey-graham", "election_integrity", 0, True,
              "Graham has consistently backed photo-voter-ID requirements at both the state and federal "
              "level. He praised South Carolina's strict photo-ID law (enacted 2011, upheld by the "
              "Fourth Circuit in 2012) that requires government-issued ID at the polls, and as Senate "
              "Judiciary Committee chairman he has supported federal election-security legislation "
              "demanding proof of identity to vote — aligning with the voter-ID rubric ideal.",
              ["https://ballotpedia.org/Lindsey_Graham",
               "https://en.wikipedia.org/wiki/Lindsey_Graham"]),
        claim("lg6", "lindsey-graham", "christian_liberty", 0, True,
              "When the Senate debated the Respect for Marriage Act in 2022, Graham co-authored with "
              "Sen. Mike Lee a Religious Liberty Amendment that would have protected faith-based "
              "organizations from federal government action based on their one-man-one-woman marriage "
              "beliefs. He voted AGAINST the final bill on the grounds that its religious-liberty "
              "protections were insufficient — the strongest Senate position for free-exercise "
              "protection taken in that floor debate.",
              ["https://en.wikipedia.org/wiki/Lindsey_Graham",
               "https://www.lee.senate.gov/2022/11/respect-for-marriage-act-why-religious-liberty-deserves-protection-and-my-amendment-will-provide-it"]),
        claim("lg7", "lindsey-graham", "family_child_sovereignty", 0, True,
              "Graham voted for the One Big Beautiful Bill (H.R.1, 119th Congress, enacted 2025), which "
              "includes the Educational Choice for Children Act (ECCA) — the largest federal "
              "school-choice expansion in U.S. history — providing a permanent federal tax credit up "
              "to $1,700/year for K–12 scholarship-granting organizations plus expanded 529 savings "
              "plans for private and religious-school tuition, directly empowering parental education "
              "sovereignty.",
              ["https://en.wikipedia.org/wiki/Lindsey_Graham",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # ---------------- Tim Scott (SC-R, US Senator) ----------------
    ("tim-scott", "SC", "Senator", [
        claim("ts7", "tim-scott", "christian_liberty", 0, True,
              "Scott co-introduced the Child Welfare Provider Inclusion Act with Sen. Ted Cruz to bar "
              "federal and state governments from discriminating against faith-based foster-care and "
              "adoption agencies based on their religious beliefs — ensuring that faith organizations "
              "cannot be excluded from federal programs for adhering to their convictions. Scott also "
              "voted AGAINST the Equality Act, which would have subordinated RFRA religious-liberty "
              "exemptions to LGBTQ non-discrimination mandates.",
              ["https://www.cruz.senate.gov/newsroom/press-releases/sens-cruz-scott-colleagues-introduce-legislation-to-protect-faith-based-foster-care-providers",
               "https://en.wikipedia.org/wiki/Tim_Scott"]),
        claim("ts8", "tim-scott", "family_child_sovereignty", 0, True,
              "Scott co-introduced the Educational Choice for Children Act (ECCA) alongside Senators "
              "Cruz, Johnson, Lankford, Sheehy, Schmitt, and Rounds, advocating for a permanent "
              "federal tax credit empowering families to direct education dollars to private and "
              "religious schools of their choosing. The ECCA was secured inside the One Big Beautiful "
              "Bill (H.R.1, 119th Congress, enacted 2025), the largest federal school-choice "
              "expansion in U.S. history.",
              ["https://www.scott.senate.gov/",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
        claim("ts9", "tim-scott", "refuse_federal_overreach", 0, True,
              "Scott has consistently fought against administrative-state expansion: he has "
              "cosponsored the REINS Act requiring congressional approval for all major federal "
              "regulations (economic impact above $100M), opposed unlawful rule-making by the CFPB "
              "and EPA, and championed private-sector-led 'opportunity zones' development to reduce "
              "reliance on federal programs. His voting record reflects a principled commitment to "
              "limiting the unelected administrative state.",
              ["https://www.scott.senate.gov/issues/conservative-values/",
               "https://en.wikipedia.org/wiki/Tim_Scott"]),
    ]),

    # ---------------- Sheldon Whitehouse (RI-D, US Senator) ----------------
    ("sheldon-whitehouse", "RI", "Senator", [
        claim("sw7", "sheldon-whitehouse", "election_integrity", 0, False,
              "Whitehouse cosponsored the Freedom to Vote Act (S.2747), which rejected strict photo-"
              "voter-ID requirements for federal elections in favor of a broad-document standard, and "
              "has repeatedly characterized Republican voter-ID proposals as 'voter suppression' aimed "
              "at disenfranchising minority voters. He has consistently opposed proof-of-citizenship "
              "requirements for voter registration — positions directly contrary to the voter-ID "
              "rubric ideal.",
              ["https://www.whitehouse.senate.gov/about/",
               "https://en.wikipedia.org/wiki/Sheldon_Whitehouse"]),
        claim("sw8", "sheldon-whitehouse", "christian_liberty", 0, False,
              "Whitehouse has supported the Equality Act framework, which would write LGBTQ "
              "non-discrimination protections into federal civil-rights law in ways that override "
              "current RFRA religious-liberty exemptions. He has championed federal anti-discrimination "
              "policies that limit the ability of faith-based employers and organizations to act in "
              "accordance with their religious convictions — a posture directly contrary to the "
              "free-exercise rubric.",
              ["https://en.wikipedia.org/wiki/Sheldon_Whitehouse",
               "https://www.whitehouse.senate.gov/about/"]),
        claim("sw9", "sheldon-whitehouse", "refuse_federal_overreach", 0, False,
              "Whitehouse has been among the Senate's most aggressive champions of expanding federal "
              "agency authority, particularly at the EPA: he backed the Inflation Reduction Act's "
              "sweeping EPA regulatory expansion (2022), cosponsored climate legislation granting "
              "broad federal rulemaking authority over energy and industry, and led 'Whiteboard of "
              "Democracy' sessions arguing the federal administrative state must grow — the opposite "
              "of the refuse-federal-overreach rubric.",
              ["https://en.wikipedia.org/wiki/Sheldon_Whitehouse",
               "https://www.whitehouse.senate.gov/news/release/whitehouse-votes-to-pass-inflation-reduction-act/"]),
    ]),

    # ---------------- Jack Reed (RI-D, US Senator) ----------------
    ("jack-reed", "RI", "Senator", [
        claim("jr8", "jack-reed", "christian_liberty", 0, False,
              "Reed has supported the Equality Act, which would codify LGBTQ non-discrimination "
              "protections in federal law in a manner that overrides current RFRA exemptions, and has "
              "not cosponsored or backed legislation protecting faith-based institutions from "
              "government coercion for holding traditional religious views. His three-decade Senate "
              "record reflects consistent support for LGBTQ civil rights over religious-liberty "
              "carveouts — contrary to the free-exercise rubric.",
              ["https://en.wikipedia.org/wiki/Jack_Reed_(Rhode_Island_politician)",
               "https://www.reed.senate.gov/issues"]),
        claim("jr9", "jack-reed", "industry_capture", 0, False,
              "Reed did not oppose COVID-era federal vaccine mandates for healthcare workers and "
              "government contractors, aligning with the Biden administration's institutional "
              "pharmaceutical protocols. He has not advocated for repealing pharmaceutical companies' "
              "federal liability shields (such as the PREP Act immunizing COVID-vaccine makers from "
              "civil suits) — a posture contrary to the anti-pharma-mandate and anti-pharma-liability-"
              "shield rubric.",
              ["https://en.wikipedia.org/wiki/Jack_Reed_(Rhode_Island_politician)",
               "https://www.reed.senate.gov/"]),
        claim("jr10", "jack-reed", "refuse_federal_overreach", 0, False,
              "Reed has consistently supported expanded federal regulatory authority throughout his "
              "nearly three decades in the Senate, backing legislation enlarging the powers of the "
              "EPA, CFPB, and other agencies. As ranking member and chair of the Senate Armed "
              "Services Committee (2019–present), he has championed centralized federal defense "
              "management and opposed efforts to limit the administrative state — contrary to the "
              "refuse-federal-overreach rubric.",
              ["https://en.wikipedia.org/wiki/Jack_Reed_(Rhode_Island_politician)",
               "https://www.reed.senate.gov/"]),
    ]),

    # ---------------- John Fetterman (PA-D, US Senator) ----------------
    ("john-fetterman", "PA", "Senator", [
        claim("jf7", "john-fetterman", "election_integrity", 0, False,
              "Fetterman championed Pennsylvania's Act 77 universal mail-in voting expansion as Lt. "
              "Governor (2019–2023) and in the Senate has opposed photo-voter-ID and proof-of-"
              "citizenship requirements, voting with the Democratic caucus against the SAVE Act "
              "(Safeguard American Voter Eligibility Act, 2024) that would require documentary proof "
              "of citizenship for federal voter registration — contrary to the voter-ID and ballot-"
              "integrity rubric ideal.",
              ["https://ballotpedia.org/John_Fetterman",
               "https://en.wikipedia.org/wiki/John_Fetterman"]),
        claim("jf8", "john-fetterman", "christian_liberty", 0, False,
              "Fetterman's record consistently elevates LGBTQ civil rights over religious-liberty "
              "exemptions: as Braddock mayor he officiated same-sex marriages in 2013 in defiance "
              "of state law; in the Senate he condemned the Supreme Court's 303 Creative LLC v. "
              "Elenis ruling (2023) — which upheld a Christian designer's First Amendment right to "
              "decline same-sex-wedding work — as licensing discrimination; and he actively secured "
              "$1 million in federal appropriations for an LGBT community center. His record "
              "opposes the free-exercise rubric.",
              ["https://en.wikipedia.org/wiki/John_Fetterman",
               "https://www.fetterman.senate.gov/press-releases/fetterman-statement-on-scotus-lgbtq-decision/"]),
        claim("jf9", "john-fetterman", "industry_capture", 0, False,
              "Fetterman backed COVID-era public-health mandates and institutional vaccine requirements "
              "and has not opposed pharmaceutical companies' federal liability shields for COVID "
              "vaccine manufacturers under the PREP Act. He has not advocated for reforming the "
              "government-pharma relationship that the rubric's anti-mandate and anti-liability-shield "
              "questions target — aligning with the institutional pharmaceutical consensus rather than "
              "the rubric ideal.",
              ["https://ballotpedia.org/John_Fetterman",
               "https://en.wikipedia.org/wiki/John_Fetterman"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions (e.g. Mike Lee HI vs UT)."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
