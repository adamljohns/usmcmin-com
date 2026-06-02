#!/usr/bin/env python3
"""Enrichment batch 8: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators from the bottom of the alphabet with
0 evidence claims. Mix (3 R / 2 D): Tim Scott (SC-R), Jack Reed (RI-D),
Sheldon Whitehouse (RI-D), Dave McCormick (PA-R), James Lankford (OK-R).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record
/ public positions.

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
    # ---------------- Tim Scott (SC-R, US Senator) ----------------
    ("tim-scott", "SC", "Senator", [
        claim("ts1", "tim-scott", "sanctity_of_life", 0, True,
              "Carries an A+ rating from SBA Pro-Life America and a 100% pro-life Senate voting record; affirms that human life must be protected from conception, consistently votes to defund Planned Parenthood, and introduced legislation to reverse Biden-era rules stripping TANF funds from pregnancy resource centers.",
              ["https://sbaprolife.org/senator/tim-scott",
               "https://en.wikipedia.org/wiki/Tim_Scott"]),
        claim("ts2", "tim-scott", "border_immigration", 0, True,
              "Called for completing the southern border wall and reinstating Title 42 expulsion authority; framed the fentanyl crisis as making every U.S. county a border county and has voted consistently for hard-enforcement immigration measures.",
              ["https://ballotpedia.org/Tim_Scott",
               "https://en.wikipedia.org/wiki/Tim_Scott"]),
        claim("ts3", "tim-scott", "self_defense", 1, True,
              "Holds a high NRA rating and voted against the 2022 Bipartisan Safer Communities Act — opposing its red-flag law incentive grants, juvenile background-check expansions, and other new restrictions on firearms — maintaining a consistent pro-Second Amendment record.",
              ["https://en.wikipedia.org/wiki/Tim_Scott",
               "https://ballotpedia.org/Tim_Scott"]),
    ]),

    # ---------------- Jack Reed (RI-D, US Senator) ----------------
    ("jack-reed", "RI", "Senator", [
        claim("jr1", "jack-reed", "sanctity_of_life", 0, False,
              "Strongly pro-choice, opposing all legislative restrictions on abortion including proposals to limit late-term procedures, bar abortion services on military installations, and restrict minors' ability to cross state lines to obtain abortions — rejecting any recognition of life at conception.",
              ["https://en.wikipedia.org/wiki/Jack_Reed_(Rhode_Island_politician)",
               "https://ballotpedia.org/Jack_Reed"]),
        claim("jr2", "jack-reed", "foreign_policy_restraint", 1, False,
              "As senior Democrat on the Senate Armed Services Committee, championed the $95 billion Ukraine/Israel/Taiwan supplemental aid package in 2024 and has consistently supported sustaining U.S. military commitments abroad — opposing the rubric's call to end open-ended foreign engagements.",
              ["https://en.wikipedia.org/wiki/Jack_Reed_(Rhode_Island_politician)",
               "https://www.reed.senate.gov/"]),
        claim("jr3", "jack-reed", "self_defense", 1, False,
              "A persistent gun-control advocate who has voted for and cosponsored legislation expanding background checks, restricting semi-automatic firearms, and funding red-flag laws — consistently opposing unrestricted Second Amendment rights.",
              ["https://www.reed.senate.gov/news/videos/reed-discusses-gun-control-and-foreign-policy-on-cnn",
               "https://ballotpedia.org/Jack_Reed"]),
    ]),

    # ---------------- Sheldon Whitehouse (RI-D, US Senator) ----------------
    ("sheldon-whitehouse", "RI", "Senator", [
        claim("sw1", "sheldon-whitehouse", "biblical_marriage", 0, False,
              "Cosponsored and championed the Respect for Marriage Act (signed 2022), which repealed the federal Defense of Marriage Act and enshrined federal recognition of same-sex unions; Whitehouse hailed its passage as landmark legislation — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.whitehouse.senate.gov/news/release/sen-whitehouse-hails-passage-of-same-sex-marriage-law/",
               "https://en.wikipedia.org/wiki/Sheldon_Whitehouse"]),
        claim("sw2", "sheldon-whitehouse", "sanctity_of_life", 4, False,
              "A consistent ally of Planned Parenthood and abortion-rights groups; among the senators who declared that Democratic control of Congress would make passage of a national abortion statute 'virtually certain,' and has never broken from the abortion-rights donor-and-endorsement network.",
              ["https://en.wikipedia.org/wiki/Sheldon_Whitehouse",
               "https://ballotpedia.org/Sheldon_Whitehouse"]),
        claim("sw3", "sheldon-whitehouse", "self_defense", 1, False,
              "Voted for the 2022 Bipartisan Safer Communities Act and supports further gun-control measures including expanded background checks, assault-weapons restrictions, and red-flag law funding — consistently opposing unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Sheldon_Whitehouse",
               "https://ballotpedia.org/Sheldon_Whitehouse"]),
    ]),

    # ---------------- Dave McCormick (PA-R, US Senator) ----------------
    ("dave-mccormick", "PA", "Senator", [
        claim("dm1", "dave-mccormick", "border_immigration", 0, True,
              "An original cosponsor of the Laken Riley Act — the first bill signed into law in the 119th Congress, requiring mandatory detention of undocumented immigrants charged with violent crimes — and supports completing the southern border wall to secure the U.S.-Mexico border.",
              ["https://www.mccormick.senate.gov/news/press-releases/senator-dave-mccormick-begins-to-deliver-on-stronger-borders/",
               "https://en.wikipedia.org/wiki/Dave_McCormick"]),
        claim("dm2", "dave-mccormick", "sanctity_of_life", 0, True,
              "Earned an SBA Pro-Life America endorsement during his 2024 Senate campaign on a pro-life platform; voted with Senate Republicans for legislation protecting born-alive infant survivors of abortion and against Democratic measures to codify Roe v. Wade.",
              ["https://en.wikipedia.org/wiki/Dave_McCormick",
               "https://ballotpedia.org/David_McCormick_(Pennsylvania)"]),
        claim("dm3", "dave-mccormick", "self_defense", 1, True,
              "Ran a strongly pro-Second Amendment Senate campaign in 2024, emphasizing opposition to new gun restrictions and magazine limits; has voted with the Republican majority against additional firearm-control legislation since taking office in January 2025.",
              ["https://en.wikipedia.org/wiki/Dave_McCormick",
               "https://ballotpedia.org/David_McCormick_(Pennsylvania)"]),
    ]),

    # ---------------- James Lankford (OK-R, US Senator) ----------------
    ("james-lankford", "OK", "Senator", [
        claim("jl1", "james-lankford", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America; affirms Congress should recognize life at the moment of fertilization and has championed the Born-Alive Abortion Survivors Protection Act, the Down Syndrome Discrimination by Abortion Prohibition Act, the Conscience Protection Act, and the Dismemberment Abortion Ban Act.",
              ["https://sbaprolife.org/senator/james-lankford",
               "https://www.lankford.senate.gov/news/press-releases/lankford-receives-a-rating-on-his-pro-life-leadership/"]),
        claim("jl2", "james-lankford", "self_defense", 1, True,
              "Awarded an A+ rating by the NRA for strong Second Amendment leadership; applauded the Bruen decision restoring public-carry rights and filed an amicus brief defending the NRA against New York's attempt to financially blacklist gun-rights organizations via regulatory pressure.",
              ["https://www.lankford.senate.gov/news/press-releases/lankford-given-a-rating-for-his-strong-support-of-the-second-amendment/",
               "https://en.wikipedia.org/wiki/James_Lankford"]),
        claim("jl3", "james-lankford", "christian_liberty", 0, True,
              "A Baptist minister before entering politics, Lankford is the Senate's most consistent defender of the Religious Freedom Restoration Act; testified against the Equality Act specifically because it would exclude RFRA protections for the first time since 1993, and successfully secured changes to DHS guidance to protect religious exercise.",
              ["https://www.lankford.senate.gov/news/press-releases/lankford-continues-to-stand-for-americans-right-to-freely-live-their-faith/",
               "https://en.wikipedia.org/wiki/James_Lankford"]),
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
