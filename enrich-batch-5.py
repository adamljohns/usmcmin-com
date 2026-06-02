#!/usr/bin/env python3
"""Enrichment batch 5: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims. Uses the
(slug + state + office_keyword) matcher from batches 2-4 to avoid
name-collision bugs.

Mix (3 R / 2 D): John Barrasso (WY-R), Shelley Moore Capito (WV-R),
Jim Justice (WV-R), Patty Murray (WA-D), Maria Cantwell (WA-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- John Barrasso (WY-R, US Senator) ----------------
    ("john-barrasso", "WY", "Senator", [
        claim("jb1", "john-barrasso", "sanctity_of_life", 0, True,
              "Listed on the SBA Pro-Life America National Scorecard with a consistent pro-life voting record; has voted to stop all taxpayer funding of abortion domestically and internationally and to protect conscience rights for pro-life healthcare providers. Stated at his 2007 Senate appointment that he had 'sponsored legislation to protect the sanctity of life' — affirming protection of unborn life from conception.",
              ["https://sbaprolife.org/senator/john-barrasso",
               "https://www.barrasso.senate.gov/newsroom-news-releases-barrasso-votes-to-protect-life/"]),
        claim("jb2", "john-barrasso", "border_immigration", 0, True,
              "A leading Senate border-security hawk who introduced the Build The Wall Act and a 2024 bill funding southern-border wall construction with unused COVID-19 appropriations; praised the 2025 'Big Beautiful Bill' for its $75 billion border enforcement appropriation and completion of the physical wall — describing Biden-era border policy as 'the deadliest, most destructive, and most disastrous in American history.'",
              ["https://www.barrasso.senate.gov/newsroom-news-releases-democrats-block-barrassos-build-the-wall-act/",
               "https://www.barrasso.senate.gov/public/index.cfm/2024/5/barrasso-bill-funds-southern-border-wall-with-unused-covid-19-funds",
               "https://www.barrasso.senate.gov/barrasso-the-big-beautiful-bill-secures-the-border-and-makes-communities-safer/"]),
        claim("jb3", "john-barrasso", "self_defense", 1, True,
              "A steadfast Second Amendment defender who voted against a 2013 background-check expansion bill and cosponsored a suite of Second Amendment protection bills with Sen. Lummis in 2023, opposing all legislation restricting law-abiding citizens' firearm access — calling the Second Amendment 'freedom's safeguard.'",
              ["https://www.barrasso.senate.gov/public/index.cfm/2023/2/barrasso-lummis-introduce-suite-of-bills-to-safeguard-second-amendment-rights",
               "https://www.barrasso.senate.gov/newsroom-news-releases-barrasso-the-second-amendment-is-freedoms-safeguard/",
               "https://en.wikipedia.org/wiki/John_Barrasso"]),
    ]),

    # ---------------- Shelley Moore Capito (WV-R, US Senator) ----------------
    ("shelley-moore-capito", "WV", "Senator", [
        claim("smc1", "shelley-moore-capito", "sanctity_of_life", 0, True,
              "Listed on the SBA Pro-Life America National Scorecard; has voted to stop taxpayer funding of abortion and protect conscience rights for pro-life providers. After previously identifying as 'pro-choice,' reversed position in 2022 to support states' rights to restrict abortion post-Dobbs, and issued a formal statement affirming her pro-life votes.",
              ["https://sbaprolife.org/senator/shelley-moore-capito",
               "https://www.capito.senate.gov/news/press-releases/capito-statement-on-pro-life-votes-",
               "https://en.wikipedia.org/wiki/Shelley_Moore_Capito"]),
        claim("smc2", "shelley-moore-capito", "self_defense", 1, False,
              "In June 2022, was one of only 15 Republican senators to vote for the Bipartisan Safer Communities Act, which expanded background checks for firearm buyers under age 21 and closed the 'boyfriend loophole' — a gun-control departure from the rubric's opposition to new firearm restrictions. Her NRA rating is 92%, reflecting a generally pro-Second Amendment record with this notable exception.",
              ["https://en.wikipedia.org/wiki/Shelley_Moore_Capito",
               "https://www.capito.senate.gov/news/press-releases/capito-statement-on-vote-to-consider-legislation-addressing-gun-violence",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("smc3", "shelley-moore-capito", "election_integrity", 0, True,
              "Expressed support for the Safeguard American Voter Eligibility (SAVE) Act, which requires proof of citizenship to register to vote in federal elections — backing the rubric's voter-verification standard.",
              ["https://www.capito.senate.gov/news/in-the-news/capito-expresses-support-for-trump-elections-bill-calls-for-homeland-security-funding"]),
    ]),

    # ---------------- Jim Justice (WV-R, US Senator) ----------------
    ("jim-justice", "WV", "Senator", [
        claim("jj1", "jim-justice", "sanctity_of_life", 0, True,
              "As West Virginia governor, signed into law a near-total abortion ban following the Supreme Court's 2022 Dobbs decision overturning Roe v. Wade, making West Virginia one of the first states to enact such a prohibition. Justice publicly stated he stood 'rock solid for life,' affirming legal protection for the unborn.",
              ["https://en.wikipedia.org/wiki/Jim_Justice",
               "https://en.wikipedia.org/wiki/Abortion_in_West_Virginia"]),
        claim("jj2", "jim-justice", "self_defense", 1, True,
              "As West Virginia governor, signed permitless (constitutional) carry legislation allowing law-abiding gun owners to carry concealed firearms without a government permit, and separately signed campus carry legislation — expanding Second Amendment exercise in line with the rubric's opposition to permit requirements.",
              ["https://en.wikipedia.org/wiki/Jim_Justice",
               "https://ballotpedia.org/Jim_Justice"]),
    ]),

    # ---------------- Patty Murray (WA-D, US Senator) ----------------
    ("patty-murray", "WA", "Senator", [
        claim("pm1", "patty-murray", "sanctity_of_life", 0, False,
              "A leading Senate champion of unrestricted abortion access who introduced the Reproductive Freedom for Women Act to codify abortion rights nationally and who cosponsored the Women's Health Protection Act, repeatedly arguing that legislators — not government — should make pregnancy decisions including late-term abortions. She opposes any personhood-from-conception framework.",
              ["https://www.murray.senate.gov/ahead-of-senate-vote-on-her-reproductive-freedom-for-women-act-murray-speaks-on-dystopian-post-dobbs-horror-stories-how-americans-will-not-be-fooled-by-dishonest-republican-spin-on-abortion/",
               "https://www.murray.senate.gov/murray-leads-senate-democratic-women-in-the-fight-to-protect-the-right-to-abortion-pass-whpa/",
               "https://en.wikipedia.org/wiki/Patty_Murray"]),
        claim("pm2", "patty-murray", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), which expanded background checks for under-21 firearm buyers and closed the 'boyfriend loophole,' and has consistently backed gun-control legislation throughout her Senate career — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Patty_Murray",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("pm3", "patty-murray", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (2022), which codified federal recognition of same-sex marriage and requires all states to honor lawful same-sex marriages from other states — rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Patty_Murray",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ---------------- Maria Cantwell (WA-D, US Senator) ----------------
    ("maria-cantwell", "WA", "Senator", [
        claim("mc1", "maria-cantwell", "sanctity_of_life", 0, False,
              "Co-introduced with Sen. Patty Murray bicameral legislation to guarantee women's right to choose abortion nationwide, and received a 2024 score of 100 from Reproductive Freedom for All (formerly NARAL Pro-Choice America) — affirming consistent support for unrestricted abortion access and rejecting any personhood-from-conception standard.",
              ["https://www.cantwell.senate.gov/news/press-releases/cantwell-murray-introduce-bicameral-legislation-guaranteeing-womens-right-to-choose-nationwide",
               "https://reproductivefreedomforall.org/lawmaker/maria-cantwell/"]),
        claim("mc2", "maria-cantwell", "election_integrity", 0, False,
              "Took to the Senate floor to defend Washington State's universal vote-by-mail system, calling it a model for the nation while debating voting rights legislation — opposing the voter-ID and anti-mass-mail-in requirements the rubric supports.",
              ["https://www.cantwell.senate.gov/news/press-releases/cantwell-defends-voting-rights-on-the-senate-floor-highlights-success-of-washington-state-vote-by-mail-business-leader-support"]),
        claim("mc3", "maria-cantwell", "border_immigration", 1, False,
              "In 2025, co-signed a letter to ICE Director Todd Lyons citing explicit concerns about the treatment of immigrants detained at the Tacoma, WA immigration detention center — opposing the mandatory detention and deportation enforcement posture the rubric supports.",
              ["https://en.wikipedia.org/wiki/Maria_Cantwell"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
