#!/usr/bin/env python3
"""Enrichment batch 22: hand-curated claims for 5 bottom-of-alphabet federal senate candidates.

Targets archetype_curated senators/candidates with 0 evidence claims, drawn from
the reverse-alphabetical end of the bucket (MT, MN, MI, MS states).

Mix (3 R / 2 D): Kurt Alme (MT-R), Royce White (MN-R), Mike Rogers (MI-R),
Peggy Flanagan (MN-D), Mike Espy (MS-D).
Each claim cites >=1 reliable source and reflects 2024-2026 positions/record.

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
    # ---------------- Kurt Alme (MT-R, 2026 U.S. Senate Candidate) ----------------
    ("kurt-alme", "MT", "Senator", [
        claim("ka1", "kurt-alme", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America (April 22, 2026) as a 'true pro-life champion in the Senate'; SBA cited his character, public-service record, and backing from Senate Pro-Life Caucus founder Steve Daines. He is the Trump-endorsed Republican nominee following the June 2026 primary.",
              ["https://sbaprolife.org/candidate-fund/leading-natl-pro-life-group-endorses-kurt-alme-for-mt-sen",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Montana"]),
        claim("ka2", "kurt-alme", "border_immigration", 1, True,
              "As U.S. Attorney for the District of Montana (2025–2026), Alme drove criminal prosecutions to a 20-year high — including prosecutions for illegal reentry and drug-trafficking cartels — under Operation Take Back America. He calls for keeping the border secure and 'prioritizing prosecuting violent criminals and investigating drug trafficking organizations all the way up to the cartels.'",
              ["https://www.msuexponent.com/news/state/kurt-alme-emphasizes-montana-roots-conservative-cred-in-early-weeks-on-campaign-trail/article_fd36a6f0-7e14-5a8f-9ec4-cb73a779b62a.html",
               "https://www.nbcnews.com/politics/2026-election/trump-backed-kurt-alme-wins-montana-gop-senate-primary-rcna347478"]),
    ]),

    # ---------------- Royce White (MN-R, 2026 U.S. Senate Candidate) ----------------
    ("royce-white", "MN", "Senator", [
        claim("rw1", "royce-white", "sanctity_of_life", 0, True,
              "States that life begins at conception and ran as a pro-life candidate in both his 2024 and 2026 Minnesota Senate campaigns. His campaign platform lists 'pro-life' as a core value and he publicly affirmed this position in the October 2024 debate against Sen. Amy Klobuchar.",
              ["https://roycewhite.us/issues/",
               "https://www.ontheissues.org/2024_MN_Senate.htm"]),
        claim("rw2", "royce-white", "self_defense", 0, True,
              "Declares on his campaign platform that 'The 2nd Amendment is a constitutional right that can never be infringed upon' — an absolute pro-constitutional-carry posture that rejects any legislative infringement on the right to keep and bear arms.",
              ["https://roycewhite.us/issues/",
               "https://ballotpedia.org/Royce_White"]),
    ]),

    # ---------------- Mike Rogers (MI-R, 2026 U.S. Senate Candidate) ----------------
    ("mike-rogers-mi-senate-2026", "MI", "Senator", [
        claim("mr1", "mike-rogers-mi-senate-2026", "sanctity_of_life", 0, True,
              "As a U.S. House member (2001–2015) Rogers voted for the Pain-Capable Unborn Child Protection Act (H.R. 1797, 2013) and co-sponsored four separate bills seeking to define human life as beginning at fertilization — a personhood-at-conception standard — as well as legislation to withdraw FDA approval of the abortion drug mifepristone.",
              ["https://reproductivefreedomforall.org/report/report-the-republican-playbook-republican-candidates-lying-about-abortion/mike-rogers/",
               "https://www.congress.gov/bill/113th-congress/house-bill/1797/history"]),
        claim("mr2", "mike-rogers-mi-senate-2026", "self_defense", 1, True,
              "Holds an A rating from the National Rifle Association and, as a congressman, voted for the Protection of Lawful Commerce in Arms Act (2005) giving firearm manufacturers liability immunity. Rogers opposes new gun restrictions and has said the solution is enforcing existing laws rather than adding new ones.",
              ["https://en.wikipedia.org/wiki/Mike_Rogers_(Michigan_politician)",
               "https://ballotpedia.org/Mike_Rogers_(Michigan)"]),
    ]),

    # ---------------- Peggy Flanagan (MN-D, 2026 U.S. Senate Candidate) ----------------
    ("peggy-flanagan-senate", "MN", "Senate", [
        claim("pf1", "peggy-flanagan-senate", "sanctity_of_life", 0, False,
              "A leading abortion-rights champion who, as Lt. Governor, helped make Minnesota the first state to pass post-Dobbs legislation protecting abortion access. She supports the federal Women's Health Protection Act to codify Roe v. Wade nationwide and vows to 'fight back against Trump and Republicans' attempts to defund Planned Parenthood' — rejecting any life-from-conception legal protection.",
              ["https://peggyflanagan.com/priorities/",
               "https://en.wikipedia.org/wiki/Peggy_Flanagan"]),
        claim("pf2", "peggy-flanagan-senate", "border_immigration", 1, False,
              "Explicitly prioritizes 'ripping ICE apart' as a top Senate goal, framing current immigration enforcement as a broken system to be dismantled — directly opposing the rubric's mandate for mandatory deportation enforcement.",
              ["https://www.thenation.com/article/politics/peggy-flanagan-minnesota-senate/",
               "https://peggyflanagan.com/priorities/"]),
        claim("pf3", "peggy-flanagan-senate", "self_defense", 1, False,
              "As Lt. Governor, championed universal background check legislation for all gun purchases — a gun-control expansion that conflicts with the rubric's opposition to new restrictions on the right to keep and bear arms.",
              ["https://ballotpedia.org/Peggy_Flanagan",
               "https://peggyflanagan.com/priorities/"]),
    ]),

    # ---------------- Mike Espy (MS-D, 2026 U.S. Senate Candidate) ----------------
    ("mike-espy-senate-2026", "MS", "Senate", [
        claim("me1", "mike-espy-senate-2026", "sanctity_of_life", 0, False,
              "Describes himself as 'anti-abortion but pro-choice,' saying 'women should have the basic right to make their own decisions' on reproductive health. He has supported Roe v. Wade and its legal protections throughout his Senate campaigns — rejecting any personhood-from-conception legal standard.",
              ["https://www.ontheissues.org/social/Mike_Espy_Abortion.htm",
               "https://en.wikipedia.org/wiki/Mike_Espy"]),
        claim("me2", "mike-espy-senate-2026", "border_immigration", 0, False,
              "Opposes construction of a border wall, citing excessive cost concerns, and condemned the Trump administration's family-separation border policy as harmful — rejecting both a physical wall/military-border posture and mandatory enforcement doctrine.",
              ["https://en.wikipedia.org/wiki/Mike_Espy",
               "https://ballotpedia.org/Mike_Espy"]),
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
