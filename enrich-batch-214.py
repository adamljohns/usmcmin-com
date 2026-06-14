#!/usr/bin/env python3
"""Enrichment batch 214: 4th claims for 5 sitting U.S. Senators (AL, GA x2, KY, PA).

Targets evidence_curated senators from the bottom of the alphabet with 3 existing
claims; adds 3 new claims each spanning distinct rubric categories.

Mix (3 R / 2 D): Tommy Tuberville (AL-R), Raphael Warnock (GA-D),
Jon Ossoff (GA-D), Rand Paul (KY-R), Dave McCormick (PA-R).

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
    # ---------------- Tommy Tuberville (AL-R, US Senator) ----------------
    ("tommy-tuberville", "AL", "Senator", [
        claim("tt4", "tommy-tuberville", "self_defense", 0, True,
              "An avid sportsman who believes law-abiding citizens should never have their constitutional rights infringed. Tuberville co-sponsored the Constitutional Concealed Carry Reciprocity Act (endorsed by the NRA, NSSF, and Gun Owners of America), which would allow individuals with home-state carry privileges to exercise them in any other state permitting concealed carry — expanding constitutional carry nationally.",
              ["https://www.tuberville.senate.gov/issues/second-amendment/",
               "https://www.tuberville.senate.gov/newsroom/press-releases/tuberville-fights-for-second-amendment-rights/"]),
        claim("tt5", "tommy-tuberville", "self_defense", 1, True,
              "Voted against the 2022 Bipartisan Safer Communities Act, stating the legislation raised serious due-process concerns over how states would implement red flag laws; separately co-sponsored a Congressional Review Act resolution to block the Biden-era ATF pistol-brace rule he called unlawful federal overreach into Second Amendment rights.",
              ["https://www.tuberville.senate.gov/newsroom/press-releases/tuberville-statement-on-gun-legislation/",
               "https://www.tuberville.senate.gov/newsroom/press-releases/tuberville-pushes-to-block-unlawful-atf-rule/"]),
        claim("tt6", "tommy-tuberville", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who voted against deficit-expanding spending packages and, with Senate Republican colleagues, refused to support any debt-ceiling increase without significant spending cuts. Tuberville co-sponsored the Prevent Government Shutdowns Act of 2023 to force Congress to pass responsible, fiscally conservative budgets on time, and his Senate website lists fiscal responsibility as a core issue.",
              ["https://www.tuberville.senate.gov/issues/economy-fiscal-responsibility/",
               "https://www.tuberville.senate.gov/newsroom/press-releases/tuberville-gop-colleagues-urge-biden-to-negotiate-on-debt-limit/"]),
    ]),

    # ---------------- Raphael Warnock (GA-D, US Senator) ----------------
    ("raphael-warnock", "GA", "Senator", [
        claim("rw4", "raphael-warnock", "self_defense", 1, False,
              "A vocal gun-control advocate who voted for the 2022 Bipartisan Safer Communities Act — the first major federal gun legislation in three decades — and has pushed for an assault-weapons ban, universal background checks, red flag laws, and safe-storage requirements, framing gun violence as a public health crisis and explicitly rejecting broad constitutional carry.",
              ["https://www.warnock.senate.gov/newsroom/press-releases/its-past-time-the-senate-got-something-done-senator-reverend-warnock-votes-in-favor-of-bipartisan-legislation-to-help-keep-georgians-safe-from-gun-violence/",
               "https://en.wikipedia.org/wiki/Raphael_Warnock"]),
        claim("rw5", "raphael-warnock", "biblical_marriage", 4, False,
              "A leading Senate advocate for the Equality Act, which would write sexual-orientation and gender-identity protections into federal civil-rights law and extend them into schools, workplaces, and public accommodations — the policy promotion of LGBTQ ideology the rubric opposes. Warnock has called LGBTQ rights non-negotiable and voted for the Respect for Marriage Act (2022) codifying same-sex marriage federally.",
              ["https://en.wikipedia.org/wiki/Raphael_Warnock",
               "https://ballotpedia.org/Raphael_Warnock"]),
        claim("rw6", "raphael-warnock", "foreign_policy_restraint", 1, False,
              "Voted for the February 2024 $95 billion Ukraine/Israel/Taiwan supplemental foreign-aid package and has consistently supported ongoing U.S. military assistance and foreign entanglements rather than the rubric's call to end forever wars and wind down foreign military commitments.",
              ["https://en.wikipedia.org/wiki/Raphael_Warnock",
               "https://www.govtrack.us/congress/members/raphael_warnock/456858"]),
    ]),

    # ---------------- Jon Ossoff (GA-D, US Senator) ----------------
    ("jon-ossoff", "GA", "Senator", [
        claim("jo4", "jon-ossoff", "biblical_marriage", 0, False,
              "Voted yes on the Respect for Marriage Act (2022) federally codifying same-sex marriage; calls his commitment to LGBTQ equality 'unwavering' and supports the Equality Act to extend federal civil-rights protections to sexual orientation and gender identity — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/Jon_Ossoff",
               "https://ballotpedia.org/Jon_Ossoff"]),
        claim("jo5", "jon-ossoff", "self_defense", 1, False,
              "Supports an assault-weapons ban, universal background checks, closing the gun-show loophole, and red flag laws; voted for the 2022 Bipartisan Safer Communities Act. Ossoff has called for expanded gun safety legislation to address what he describes as an epidemic of gun violence — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.ossoff.senate.gov/press-releases/sen-ossoff-statement-on-bipartisan-action-to-prevent-gun-violence/",
               "https://www.ontheissues.org/Domestic/Jon_Ossoff_Gun_Control.htm"]),
        claim("jo6", "jon-ossoff", "foreign_policy_restraint", 1, False,
              "Voted for the February 2024 $95 billion Ukraine/Israel/Taiwan supplemental package and maintains broad support for U.S. foreign military commitments and aid to regional allies, including voting against resolutions that would have withheld weapons sales to Israel (April 2025) — a posture at odds with the rubric's call to end forever wars and rein in foreign entanglements.",
              ["https://en.wikipedia.org/wiki/Jon_Ossoff",
               "https://www.govtrack.us/congress/members/jon_ossoff/456857"]),
    ]),

    # ---------------- Rand Paul (KY-R, US Senator) ----------------
    ("rand-paul", "KY", "Senator", [
        claim("rp4", "rand-paul", "self_defense", 0, True,
              "Maintains a dedicated 'Protecting Gun Rights' page on his Senate website and consistently opposes all new federal firearms regulations. Paul opposed the UN Arms Trade Treaty, warning it offered only a weak non-binding reference to lawful firearms ownership and failed to recognize individual self-defense as a fundamental right — protecting Americans' constitutional carry rights from international erosion.",
              ["https://www.paul.senate.gov/issues/protecting-gun-rights/",
               "https://en.wikipedia.org/wiki/Political_positions_of_Rand_Paul"]),
        claim("rp5", "rand-paul", "economic_stewardship", 2, True,
              "A perennial champion of a balanced budget amendment and the Penny Plan Budget Act (which would balance the federal budget in five years by cutting spending by one penny per dollar). Paul has objected to multi-trillion-dollar deficit-spending bills from both parties, forced Senate floor votes on spending reductions, and has stated the national debt is the single greatest threat to American security.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Rand_Paul",
               "https://www.paul.senate.gov/issues/"]),
        claim("rp6", "rand-paul", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (2022), which federally codified same-sex marriage — he was not among the 12 Senate Republicans who crossed over to support the bill. Paul has held that civil marriage definitions should be left to the states and has not endorsed federal redefinition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022",
               "https://en.wikipedia.org/wiki/Political_positions_of_Rand_Paul"]),
    ]),

    # ---------------- Dave McCormick (PA-R, US Senator) ----------------
    ("dave-mccormick", "PA", "Senator", [
        claim("dm4", "dave-mccormick", "biblical_marriage", 0, False,
              "In 2013, McCormick joined 131 other Republicans in signing an amicus brief filed at the U.S. Supreme Court supporting the legalization of gay marriage — a formal legal position that does not affirm the one-man-one-woman definition of civil marriage that the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Dave_McCormick",
               "https://ballotpedia.org/David_McCormick_(Pennsylvania)"]),
        claim("dm5", "dave-mccormick", "foreign_policy_restraint", 4, True,
              "Has stated publicly that he does not support Ukraine's membership in NATO, opposing further eastward expansion of the alliance — aligning with the rubric's anti-NATO-expansion position and reflecting skepticism of open-ended security commitments that could entangle the U.S. in additional foreign conflicts.",
              ["https://en.wikipedia.org/wiki/Dave_McCormick",
               "https://www.ontheissues.org/Senate/David_McCormick.htm"]),
        claim("dm6", "dave-mccormick", "border_immigration", 1, True,
              "Campaigned on and supports the Trump administration's mass-deportation and interior-enforcement agenda; as a senator confirmed in the 119th Congress and Armed Services Committee member, McCormick backed using military resources for border security and mandatory removal of illegal immigrants in alignment with the administration's strict enforcement priorities.",
              ["https://ballotpedia.org/David_McCormick_(Pennsylvania)",
               "https://www.ontheissues.org/Senate/David_McCormick.htm"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
