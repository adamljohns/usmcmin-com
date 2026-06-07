#!/usr/bin/env python3
"""Enrichment batch 103: hand-curated claims for 4 sitting U.S. House members.

Targets archetype_party_default U.S. Representatives (2025-2026), taken from
the bottom of the alphabet (WV, WI). All are sitting members of Congress with
documented voting records from reliable public sources.

Mix (4 R): Riley Moore (WV-02), Carol Miller (WV-01),
Glenn Grothman (WI-06), Tom Tiffany (WI-07).
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
    # ------------- Riley Moore (WV-02, first-term Rep since Jan 2025) -------------
    ("riley-moore", "WV", "Representative", [
        claim("rm1", "riley-moore", "sanctity_of_life", 0, True,
              "SBA Pro-Life America's Candidate Fund endorsed Moore's 2024 congressional campaign, stating 'In Congress he will be a rock-solid vote to advance the cause of life.' Moore consistently affirms protection of unborn life from conception and has cast pro-life votes since taking office in January 2025.",
              ["https://sbaprolife.org/candidate/riley-moore",
               "https://sbaprolife.org/uncategorized/sba-pro-life-americas-candidate-fund-endorses-riley-moore-for-congress-in-wv-02"]),
        claim("rm2", "riley-moore", "election_integrity", 0, True,
              "Voted for the SAVE America Act (Safeguard American Voter Eligibility Act) requiring proof of U.S. citizenship to register to vote in federal elections — a foundational voter-integrity measure combating non-citizen registration and closing vulnerabilities in mass-mail-in-ballot systems.",
              ["https://www.mooreforwv.com/about",
               "https://www.congress.gov/member/riley-moore/M001235"]),
        claim("rm3", "riley-moore", "foreign_policy_restraint", 2, True,
              "Introduced the Stop CCP VISAs Act (March 2025) to ban all Chinese nationals from receiving U.S. student visas, citing PRC government espionage and systematic intellectual property theft through American universities — treating the CCP-governed People's Republic of China as a hostile foreign power that must be denied privileged access to U.S. institutions.",
              ["https://rileymoore.house.gov/media/press-releases/congressman-moore-introduces-stop-ccp-visas-act",
               "https://thehill.com/homenews/house/5195480-riley-moore-chinese-students-visas-bill/"]),
    ]),

    # ------------- Carol Miller (WV-01, Ways and Means Committee) -------------
    ("carol-miller", "WV", "Representative", [
        claim("cm1", "carol-miller", "sanctity_of_life", 0, True,
              "A consistent pro-life advocate: delivered a House floor speech in support of the Born Alive Abortion Survivors Protection Act demanding care for infants surviving abortion procedures; introduced H.R. 7045, the Pregnancy Center Support Act (2024), creating a federal tax credit to fund pregnancy centers offering alternatives to abortion. Rates as pro-life on SBA Pro-Life America's National Scorecard.",
              ["https://miller.house.gov/media/press-releases/icymi-congresswoman-carol-miller-house-floor-speech-born-alive-abortion",
               "https://sbaprolife.org/representative/carol-miller"]),
        claim("cm2", "carol-miller", "self_defense", 0, True,
              "Publicly identifies as 'pro-Second Amendment' as a foundational campaign and legislative position; has voted consistently against federal gun-control measures and lists Second Amendment protection among her top issues, opposing restrictions that would burden law-abiding gun owners.",
              ["https://miller.house.gov/issues",
               "https://www.electcarolmiller.com/"]),
        claim("cm3", "carol-miller", "border_immigration", 1, True,
              "In April 2025 Miller traveled to El Salvador to tour the CECOT (Centro de Confinamiento del Terrorismo) detention facility holding deportees removed from the United States under the Trump administration's mass-enforcement program — publicly demonstrating support for mandatory deportation and aggressive immigration enforcement as legitimate national-security policy.",
              ["https://en.wikipedia.org/wiki/Carol_Miller_(politician)",
               "https://miller.house.gov/issues"]),
    ]),

    # ------------- Glenn Grothman (WI-06, 6-term conservative veteran) -------------
    ("glenn-grothman", "WI", "House", [
        claim("gg1", "glenn-grothman", "sanctity_of_life", 0, True,
              "States publicly: 'I am committed to protecting life from conception to natural death. We have a moral and civic duty to protect those who are voiceless and defenseless, including unborn children and individuals with disabilities.' Has voted consistently to block taxpayer funding of abortion and holds a strong score on SBA Pro-Life America's National Scorecard.",
              ["https://grothman.house.gov/issues",
               "https://sbaprolife.org/representative/glenn-grothman"]),
        claim("gg2", "glenn-grothman", "self_defense", 1, True,
              "NRA-endorsed concealed-carry license holder who states: 'As a Wisconsin Concealed Carry License holder, I will support legislation that protects your 2nd Amendment rights.' Has a documented record of opposing federal gun-control proposals including red-flag-law precursors, assault-weapons bans, and magazine restrictions across multiple Congresses.",
              ["https://www.nrapvf.org/emails/2020/wisconsin/glenn-grothman-wi-06-general/",
               "https://grothman.house.gov/issues/issue/?IssueID=14905"]),
        claim("gg3", "glenn-grothman", "economic_stewardship", 2, True,
              "A veteran fiscal hawk who states 'I will work to cut spending, root out waste and balance the federal budget'; earned a 92% Heritage Action scorecard in the 116th Congress. Has repeatedly voted against continuing resolutions that add to the deficit without spending cuts, and frames a balanced budget as a non-negotiable fiscal obligation — objecting to multi-trillion-dollar spending packages regardless of party origin.",
              ["https://grothman.house.gov/issues/issue/?IssueID=14887",
               "https://heritageaction.com/scorecard/members/G000576/116"]),
    ]),

    # ------------- Tom Tiffany (WI-07, Freedom Caucus, 2026 WI Gov candidate) -------------
    ("tom-tiffany", "WI", "House", [
        claim("tt1", "tom-tiffany", "sanctity_of_life", 0, True,
              "Holds a pro-life record documented on SBA Pro-Life America's National Scorecard; as a Wisconsin state legislator voted for a 20-week abortion-protection law that was signed, and in Congress has advocated for a six-week fetal-heartbeat standard — consistently rejecting any framework that does not legally protect unborn life from early stages of development.",
              ["https://sbaprolife.org/representative/tom-tiffany",
               "https://en.wikipedia.org/wiki/Tom_Tiffany"]),
        claim("tt2", "tom-tiffany", "foreign_policy_restraint", 1, True,
              "Voted against the April 2024 $95 billion Ukraine/Israel foreign-aid package, stating '$95 billion in FOREIGN aid with NOTHING to stop the FOREIGN invasion of our own country' and that 'America's border security should come FIRST.' In July 2023 also supported an amendment to cut off all U.S. military aid to Ukraine — a consistent vote against open-ended foreign military entanglements.",
              ["https://tiffany.house.gov/media/newsletters/tiffany-telegram-april-19-2024",
               "https://www.northernnewsnow.com/2023/07/15/northland-reps-stauber-tiffany-vote-cut-off-aid-ukraine/"]),
        claim("tt3", "tom-tiffany", "border_immigration", 4, True,
              "Introduced H.R. 7780, the One Nation, One Visa Policy Act (March 2026), to close the loophole that allows Chinese nationals to exploit birthright citizenship by entering U.S. territories (Northern Mariana Islands, Guam) visa-free and bearing children who automatically receive U.S. citizenship — directly targeting the birthright-citizenship loophole that enables chain migration from hostile nations.",
              ["https://tiffany.house.gov/media/press-releases/rep-tiffany-introduces-one-nation-one-visa-policy-act-end-obama-era-program",
               "https://www.breitbart.com/politics/2026/03/04/exclusive-tom-tiffany-issues-one-nation-one-visa-bill-shut-down-chinas-exploitation-birthright-citizenship-u-s/"]),
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
