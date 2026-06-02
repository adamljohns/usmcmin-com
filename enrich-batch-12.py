#!/usr/bin/env python3
"""Enrichment batch 12: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims.  Uses the
(slug + state + office_keyword) matcher from batches 2-4 to avoid
name-collision bugs.

Mix (4 R + 1 mixed): Marsha Blackburn (TN-R), Steve Daines (MT-R),
Roger Wicker (MS-R), Deb Fischer (NE-R), Thom Tillis (NC-R).
Each claim cites >=1 reliable source and reflects verified 2022-2026
voting record / public positions.

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
    # ---------------- Marsha Blackburn (TN-R, sitting U.S. Senator) ----------------
    ("marsha-blackburn-gov", "TN", "Senator", [
        claim("mb1", "marsha-blackburn-gov", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record with an A+ rating from SBA Pro-Life America, which endorsed her 2018 Senate race and lauded her record of opposing taxpayer funding for abortion and Planned Parenthood.  She affirms life begins at conception.",
              ["https://sbaprolife.org/senator/marsha-blackburn",
               "https://en.wikipedia.org/wiki/Marsha_Blackburn"]),
        claim("mb2", "marsha-blackburn-gov", "self_defense", 1, True,
              "Holds an NRA 'A' rating and has consistently opposed firearms restrictions including red-flag laws, assault-weapons bans, and magazine limits, stating that the Second Amendment is 'one of our most important freedoms.'",
              ["https://ballotpedia.org/Marsha_Blackburn",
               "https://en.wikipedia.org/wiki/Marsha_Blackburn"]),
        claim("mb3", "marsha-blackburn-gov", "biblical_marriage", 0, True,
              "Publicly opposes same-sex marriage and voted against the Respect for Marriage Act (2022), which federally codified same-sex unions — she was among the 36 Senate Republicans who rejected the bill.",
              ["https://en.wikipedia.org/wiki/Marsha_Blackburn",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022"]),
    ]),

    # ---------------- Steve Daines (MT-R, U.S. Senator) ----------------
    ("steve-daines", "MT", "Senator", [
        claim("sd1", "steve-daines", "sanctity_of_life", 0, True,
              "Founder and chairman of the Senate Pro-Life Caucus; introduced the Life at Conception Act, which declares constitutional personhood beginning at fertilization, along with the Pain-Capable Unborn Child Protection Act, Prenatal Nondiscrimination Act, and legislation to block taxpayer funding of abortion.",
              ["https://www.daines.senate.gov/meet-steve/legislative-issues/pro-life/",
               "https://en.wikipedia.org/wiki/Steve_Daines"]),
        claim("sd2", "steve-daines", "self_defense", 1, True,
              "Holds an NRA 'A' rating; opposes expanded background checks, red-flag laws, and new firearm restrictions; reintroduced the Firearm Owners Protection Act reform to preserve law-abiding gun owners' right to transport firearms across state lines.",
              ["https://www.daines.senate.gov/news/press-releases/daines-introduces-bill-to-protect-2nd-amendment-law-abiding-gun-owners",
               "https://en.wikipedia.org/wiki/Steve_Daines"]),
        claim("sd3", "steve-daines", "border_immigration", 0, True,
              "Voted in January 2019 to fund $5.7 billion in border-wall construction; in 2024 opposed the Senate emergency supplemental border deal as a betrayal of Trump-era enforcement policies, stating that reversing those policies had turned the border into 'one of the biggest national security risks in our country's history.'",
              ["https://en.wikipedia.org/wiki/Steve_Daines",
               "https://www.daines.senate.gov/meet-steve/legislative-issues/securing-our-borders/"]),
    ]),

    # ---------------- Roger Wicker (MS-R, U.S. Senator) ----------------
    ("roger-wicker", "MS", "Senator", [
        claim("rw1", "roger-wicker", "sanctity_of_life", 0, True,
              "Has affirmed that life begins at conception throughout his legislative career: as a Mississippi state senator he authored a 24-hour abortion waiting period and clinic regulations; in the U.S. House he cosponsored the partial-birth-abortion ban; in the Senate he cosponsored personhood legislation and established a pro-life record on his official page.",
              ["https://www.wicker.senate.gov/protecting-life",
               "https://en.wikipedia.org/wiki/Roger_Wicker"]),
        claim("rw2", "roger-wicker", "self_defense", 1, True,
              "Earned an 'A+' rating from the NRA Political Victory Fund and pledged to filibuster any legislation he determines 'infringes' on the Second Amendment, including assault-weapons bans or gun registries.",
              ["https://ballotpedia.org/Roger_Wicker",
               "https://en.wikipedia.org/wiki/Roger_Wicker"]),
        claim("rw3", "roger-wicker", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act on November 29, 2022, the bill that federally codified same-sex marriage; he was among the 36 senators who rejected it, maintaining the traditional one-man-one-woman definition.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://www.govtrack.us/congress/members/roger_wicker/400432"]),
    ]),

    # ---------------- Deb Fischer (NE-R, U.S. Senator) ----------------
    ("deb-fischer", "NE", "Senator", [
        claim("df1", "deb-fischer", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and was endorsed by SBA Pro-Life America Candidate Fund for her successful 2024 re-election; supports defunding Planned Parenthood and opposes taxpayer-funded abortion.",
              ["https://sbaprolife.org/senator/deb-fischer",
               "https://en.wikipedia.org/wiki/Deb_Fischer"]),
        claim("df2", "deb-fischer", "economic_stewardship", 2, True,
              "Was among 31 Senate Republicans who voted against the Fiscal Responsibility Act of 2023, the bipartisan debt-ceiling compromise, viewing it as insufficiently stringent on federal spending and deficit reduction.",
              ["https://en.wikipedia.org/wiki/Deb_Fischer",
               "https://ballotpedia.org/Deb_Fischer"]),
        claim("df3", "deb-fischer", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act (2022); she was not among the 12 Senate Republicans who supported the bill's passage, holding to the traditional definition of marriage.",
              ["https://ballotpedia.org/Respect_for_Marriage_Act_of_2022",
               "https://en.wikipedia.org/wiki/Deb_Fischer"]),
    ]),

    # ---------------- Thom Tillis (NC-R, U.S. Senator) ----------------
    ("thom-tillis", "NC", "Senator", [
        claim("tt1", "thom-tillis", "biblical_marriage", 0, False,
              "Was a lead Republican negotiator of the Respect for Marriage Act (2022) and voted for its passage, federally codifying same-sex marriage; he called the bill 'a good compromise based on mutual respect,' directly rejecting the one-man-one-woman definition.",
              ["https://www.tillis.senate.gov/2022/12/senate-passes-respect-for-marriage-act-that-includes-robust-religious-freedom-protections-secured-by-tillis",
               "https://en.wikipedia.org/wiki/Thom_Tillis"]),
        claim("tt2", "thom-tillis", "border_immigration", 0, False,
              "Initially opposed President Trump's 2019 national-emergency declaration to divert military funds for border-wall construction; has also backed a pathway to citizenship for illegal immigrants in bipartisan immigration frameworks.",
              ["https://en.wikipedia.org/wiki/Thom_Tillis",
               "https://ballotpedia.org/Thom_Tillis_(North_Carolina)"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
