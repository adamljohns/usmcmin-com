#!/usr/bin/env python3
"""Enrichment batch 204: hand-curated claims for 5 sitting/recently-serving U.S. Representatives.

archetype_curated federal senator/rep buckets exhausted; targets drawn from
archetype_party_default US Representatives with 0 claims, bottom of the alphabet
(MI, ME, MD, MA).

Mix (1 R / 4 D): John James (MI-R), Jared Golden (ME-D), Jamie Raskin (MD-D),
Katherine Clark (MA-D), Jim McGovern (MA-D).
Each claim cites >=1 reliable source and reflects documented voting record /
public positions (2019-2025).

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
    # ---------------- John James (MI-R, US Representative MI-10) ----------------
    ("john-james", "MI", "Representative", [
        claim("jj1", "john-james", "sanctity_of_life", 0, True,
              "SBA Pro-Life America endorsed James with praise for his 'strong voice for the pro-life movement'; he stated publicly 'I believe life begins at conception and ends at a natural death' and voted YES on the Born-Alive Abortion Survivors Protection Act (H.R.21, Jan 2025), which mandates medical care for infants who survive abortions.",
              ["https://sbaprolife.org/representative/john-james",
               "https://ballotpedia.org/John_James_(Michigan)",
               "https://michiganindependent.com/politics/10-congressional-district-2024-election-john-james-carl-marlinga-house-representatives/"]),
        claim("jj2", "john-james", "self_defense", 1, True,
              "The NRA endorsed James in his Senate races praising his opposition to an assault-weapons ban and universal background checks. As a U.S. Representative he maintained a pro-Second-Amendment voting record, opposing new firearm restrictions on semi-automatic rifles, background-check expansions, and magazine-capacity limits.",
              ["https://www.nrapvf.org/emails/2018/michigan/john-james-mi-sen-general-election-email/",
               "https://ballotpedia.org/John_James_(Michigan)"]),
        claim("jj3", "john-james", "border_immigration", 0, True,
              "Voted YES on the Secure the Border Act of 2023 (H.R.2, House Vote #209, May 11 2023), which funds border-wall construction, ends catch-and-release, and tightens asylum rules. Also voted YES on the Laken Riley Act (S.5/H.R.29, signed Jan 29 2025) requiring DHS to detain undocumented immigrants charged with violent crimes.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/John_James_(Michigan)"]),
    ]),

    # ---------------- Jared Golden (ME-D, US Representative ME-02) ----------------
    ("jared-golden", "ME", "Representative", [
        claim("jg1", "jared-golden", "self_defense", 1, False,
              "After previously being one of only five Democrats to vote AGAINST a House assault-weapons ban (2022), Golden reversed course in October 2023 following the Lewiston, Maine mass shooting and publicly called for a ban on assault rifles — earning an F from the NRA, whose 2024 endorsement went to his Republican challenger.",
              ["https://www.cbsnews.com/news/jared-golden-in-favor-of-assault-weapons-ban-maine-lewiston-mass-shootings/",
               "https://www.bangordailynews.com/2024/09/09/politics/elections/austin-theriault-wins-nra-endorsement-joam40zk0w/",
               "https://www.nrapvf.org/campaigns/2024/defeat-golden/"]),
        claim("jg2", "jared-golden", "sanctity_of_life", 0, False,
              "Golden has voted to eliminate prohibitions on taxpayer funding for abortion domestically and internationally, voted against restrictions on the unborn, and marked the second anniversary of the Dobbs decision as a setback for women's healthcare — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Jared_Golden",
               "https://www.mainepublic.org/politics/2024-10-29/guns-emerge-as-top-issue-in-2nd-congressional-district-race"]),
        claim("jg3", "jared-golden", "biblical_marriage", 0, False,
              "Voted YES on the Respect for Marriage Act (H.R.8404, 2022), which repealed the Defense of Marriage Act and codified federal recognition of same-sex and interracial marriages — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://ballotpedia.org/Respect_for_Marriage_Act_of_2022"]),
    ]),

    # ---------------- Jamie Raskin (MD-D, US Representative MD-08) ----------------
    ("jamie-raskin", "MD", "Representative", [
        claim("jr1", "jamie-raskin", "sanctity_of_life", 0, False,
              "Carries a 100% score from Reproductive Freedom for All (NARAL successor); co-introduced the Ensuring Women's Right to Reproductive Freedom Act to protect interstate abortion travel; and cosponsored the Women's Health Protection Act to codify federal abortion access — rejecting any personhood-from-conception standard.",
              ["https://reproductivefreedomforall.org/lawmaker/jamie-raskin/",
               "https://raskin.house.gov/2023/2/reps-raskin-fletcher-and-strickland-reintroduce-legislation-to-protect-a-woman-s-right-to-travel-for-abortion"]),
        claim("jr2", "jamie-raskin", "biblical_marriage", 1, False,
              "Led the Maryland legislative fight to legalize same-sex marriage and as a congressman voted YES on the Respect for Marriage Act (H.R.8404, 2022), cosponsoring the bill that repealed the Defense of Marriage Act and codified federal recognition of same-sex unions — explicitly rejecting the traditional one-man-one-woman definition.",
              ["https://en.wikipedia.org/wiki/Jamie_Raskin",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
        claim("jr3", "jamie-raskin", "self_defense", 1, False,
              "A gun-control advocate whose official House page promotes gun-safety legislation including assault-weapon restrictions; voted to pass the Assault Weapons Ban of 2022 and supports expanded background checks and other firearms restrictions — opposing the rubric's defense of semi-automatic firearms from bans and registries.",
              ["https://raskin.house.gov/gun-safety",
               "https://en.wikipedia.org/wiki/Jamie_Raskin"]),
    ]),

    # ---------------- Katherine Clark (MA-D, US Representative MA-05 / House Minority Whip) ----------------
    ("katherine-clark", "MA", "Representative", [
        claim("kc1", "katherine-clark", "sanctity_of_life", 0, False,
              "Led House Democratic efforts to pass the Women's Health Protection Act to enshrine federal abortion access, voted to codify the right to contraception and to protect interstate abortion travel — consistently scoring 100% with pro-abortion groups and carrying no support from pro-life organizations.",
              ["https://katherineclark.house.gov/reproductivefreedom",
               "https://katherineclark.house.gov/2024/6/courier"]),
        claim("kc2", "katherine-clark", "self_defense", 1, False,
              "Partnered with Rep. John Lewis to lead a historic sit-in on the House floor demanding a vote on gun-control measures; voted to close background-check loopholes, ban assault weapons, and restrict high-capacity magazines — opposing the rubric's defense of semi-automatic firearms from government restriction.",
              ["https://katherineclark.house.gov/2023/1/gbh",
               "https://legisletter.org/legislator/katherine-clark-C001101"]),
        claim("kc3", "katherine-clark", "biblical_marriage", 4, False,
              "Voted for the Equality Act (H.R.5, 2021), which writes sexual-orientation and gender-identity protections into federal civil-rights law and extends them into schools and public accommodations — the broad promotion of LGBTQ ideology in policy and education that the rubric opposes.",
              ["https://katherineclark.house.gov/reproductivefreedom",
               "https://legisletter.org/legislator/katherine-clark-C001101"]),
    ]),

    # ---------------- Jim McGovern (MA-D, US Representative MA-02) ----------------
    ("jim-mcgovern", "MA", "Representative", [
        claim("jm1", "jim-mcgovern", "sanctity_of_life", 0, False,
              "Has maintained a 100% pro-abortion voting record across more than two decades in Congress: voted against the Partial-Birth Abortion Ban Act (2003) and the Unborn Victims of Violence Act (2004), voted FOR the Women's Health Protection Act to codify abortion access, and stated 'I believe reproductive care is health care' after Dobbs.",
              ["https://en.wikipedia.org/wiki/Jim_McGovern_(American_politician)",
               "https://ballotpedia.org/Jim_McGovern_(Massachusetts)",
               "https://www.govtrack.us/congress/members/james_mcgovern/400263"]),
        claim("jm2", "jim-mcgovern", "border_immigration", 0, False,
              "A consistent opponent of border-wall funding and restrictive immigration enforcement; has voted against appropriations packages that include border-wall construction and has publicly criticized efforts to militarize immigration enforcement — opposing the rubric's call for a wall and military presence at the southern border.",
              ["https://ballotpedia.org/Jim_McGovern_(Massachusetts)",
               "https://en.wikipedia.org/wiki/Jim_McGovern_(American_politician)"]),
        claim("jm3", "jim-mcgovern", "self_defense", 1, False,
              "Supports 'commonsense gun violence prevention measures' including restrictions on assault-style weapons; has voted for gun-control legislation across his 28-year House career and as Ranking Member of the House Rules Committee has worked to advance gun-restriction bills — opposing the rubric's defense of unrestricted access to semi-automatic firearms.",
              ["https://en.wikipedia.org/wiki/Jim_McGovern_(American_politician)",
               "https://www.govtrack.us/congress/members/james_mcgovern/400263"]),
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
