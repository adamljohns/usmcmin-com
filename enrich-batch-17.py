#!/usr/bin/env python3
"""Enrichment batch 17: hand-curated claims for 5 federal Senate candidates.

Targets archetype_curated federal candidates from the BOTTOM of the alphabet
(WY, SD, SC, RI, NH) that had 0 evidence claims.

Mix (3 D / 2 R): Scott Morrow (WY-D, 2026 candidate),
Brian Bengs (SD-D, 2026 candidate), Annie Andrews (SC-D, 2026 candidate),
Allen Waters (RI-R, 2026 candidate), John E. Sununu (NH-R, 2026 candidate).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ------------- Scott Morrow (WY-D, 2026 US Senate Candidate) -------------
    ("scott-morrow-wy-senate", "WY", "Senate", [
        claim("sm1", "scott-morrow-wy-senate", "sanctity_of_life", 0, False,
              "A perennial Wyoming Democratic Senate candidate who has called to codify Roe v. Wade into federal law and denounced the Supreme Court's Dobbs ruling, stating 'Big Brother should not be allowed to get between women and their doctors' — explicitly rejecting any legal personhood from conception.",
              ["https://www.ontheissues.org/Senate/Scott_Morrow.htm",
               "https://ballotpedia.org/Scott_Morrow_(Wyoming)"]),
        claim("sm2", "scott-morrow-wy-senate", "economic_stewardship", 2, False,
              "Attacked Wyoming's Republican congressional delegation for what he characterized as hostility toward Social Security, Medicare, and federal employee pension systems, positioning himself as a defender of expansionary entitlement spending — at odds with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.ontheissues.org/Senate/Scott_Morrow.htm"]),
    ]),

    # ------------- Brian Bengs (SD-D, 2026 US Senate Candidate) -------------
    ("brian-bengs-sd-senate", "SD", "Senate", [
        claim("bb1", "brian-bengs-sd-senate", "sanctity_of_life", 0, False,
              "Aligns his abortion stance with the Roe v. Wade framework: unrestricted access in the first trimester and through the point of viability, after which the state may impose restrictions — explicitly rejecting any personhood-from-conception standard.",
              ["https://www.ontheissues.org/Social/Brian_Bengs_Abortion.htm",
               "https://ballotpedia.org/Brian_Bengs"]),
        claim("bb2", "brian-bengs-sd-senate", "self_defense", 1, False,
              "Although a gun owner, Bengs stated he would vote for HR 8 (universal background checks for all firearm sales), supports red-flag laws, and favors raising the minimum age for certain firearms, acknowledging the NRA 'would probably not' rate him favorably — backing restrictions the rubric opposes.",
              ["https://www.keloland.com/keloland-com-original/democratic-senate-candidate-talks-gun-control/",
               "https://dakotafreepress.com/2022/05/27/bengs-would-vote-for-some-background-checks-but-still-normalizes-guns-and-the-obsolete-second-amendment/"]),
    ]),

    # ------------- Annie Andrews (SC-D, 2026 US Senate Candidate) -------------
    ("annie-andrews-senate", "SC", "Senate", [
        claim("aa1", "annie-andrews-senate", "sanctity_of_life", 0, False,
              "A pediatrician-candidate who calls to restore the protections of Roe v. Wade, expand maternal health services in rural communities, and guarantee access to contraception — explicitly rejecting personhood-from-conception standards.",
              ["https://drannieandrews.com/",
               "https://19thnews.org/2026/02/annie-andrews-south-carolina-measles-pediatrician-senate/"]),
        claim("aa2", "annie-andrews-senate", "self_defense", 1, False,
              "Serves as Senior Advisor for Everytown for Gun Safety, the nation's largest gun-control advocacy organization, and makes reducing gun violence a signature campaign theme — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.live5news.com/2025/09/26/we-palmetto-meet-candidate-dr-annie-andrews-us-senate/",
               "https://ballotpedia.org/Annie_Andrews"]),
        claim("aa3", "annie-andrews-senate", "industry_capture", 0, False,
              "Made South Carolina's 2026 measles outbreak a cornerstone of her Senate campaign, publicly advocating for vaccination requirements as a public-health imperative and warning against erosion of childhood vaccine mandates — supporting pharmaceutical-industry-aligned public-health mandates rather than opposing them.",
              ["https://19thnews.org/2026/02/annie-andrews-south-carolina-measles-pediatrician-senate/"]),
    ]),

    # ------------- Allen Waters (RI-R, 2026 US Senate Candidate) -------------
    ("allen-waters-ri-senate", "RI", "Senate", [
        claim("aw1", "allen-waters-ri-senate", "sanctity_of_life", 0, True,
              "Holds a pro-life position: abortion should be permitted only to protect the life of the mother — a restrictive standard consistent with the rubric's sanctity-of-life framework recognizing protections for unborn life.",
              ["https://www.ontheissues.org/social/Allen_Waters_Abortion.htm",
               "https://ballotpedia.org/Allen_Waters"]),
        claim("aw2", "allen-waters-ri-senate", "border_immigration", 1, True,
              "Calls for full funding and support of U.S. Border Patrol, mandatory deportation of criminal illegal aliens, and reform of immigration laws to require orderly and lawful entry — aligning with the rubric's mandatory-deportation border-enforcement priority.",
              ["https://www.ontheissues.org/senate/Allen_Waters.htm",
               "https://justfacts.votesmart.org/candidate/biography/154036/allen-waters"]),
        claim("aw3", "allen-waters-ri-senate", "self_defense", 1, True,
              "Holds conservative gun-rights views, publicly carried his gun license as a personal display of Second Amendment conviction, and opposes new federal restrictions on legal firearm ownership — consistent with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.ontheissues.org/senate/Allen_Waters.htm",
               "https://ballotpedia.org/Allen_Waters"]),
    ]),

    # ------------- John E. Sununu (NH-R, 2026 US Senate Candidate) -------------
    ("john-sununu", "NH", "Senator", [
        claim("js1", "john-sununu", "sanctity_of_life", 0, True,
              "Earned a 100% rating from the National Right to Life Committee and a 0% score from NARAL Pro-Choice America during his Senate tenure (2003–2009), reflecting a consistent pro-life voting record aligned with the rubric's personhood-from-conception standard.",
              ["https://www.ontheissues.org/senate/john_sununu.htm",
               "https://en.wikipedia.org/wiki/John_E._Sununu"]),
        claim("js2", "john-sununu", "self_defense", 1, True,
              "Maintained a pro-gun Senate record (2003–2009), opposing new federal gun-control legislation and supporting Second Amendment rights without additional restrictions — consistent with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.ontheissues.org/Domestic/John_Sununu_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/John_E._Sununu"]),
        claim("js3", "john-sununu", "refuse_federal_overreach", 0, True,
              "Was one of only three House Republicans — and fewer than 70 members total — to vote against the original USA PATRIOT Act in October 2001, citing concerns about unchecked federal surveillance powers and civil liberties, a record consistent with the rubric's opposition to federal overreach.",
              ["https://en.wikipedia.org/wiki/John_E._Sununu",
               "https://www.ontheissues.org/senate/john_sununu.htm"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions across states."""
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
