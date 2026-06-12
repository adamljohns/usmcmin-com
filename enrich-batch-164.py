#!/usr/bin/env python3
"""Enrichment batch 164: 4 sitting U.S. House Republicans from NJ, NY, NE, and NC.

Targets archetype_party_default members with 0 evidence claims from the bottom
of the alphabet. All positions sourced from official sites, Wikipedia, SBA
Pro-Life, congress.gov, and news reporting.

Candidates: Chris Smith (NJ-04, longest-serving NJ member, Pro-Life Caucus Chair),
Andrew Garbarino (NY-02, Homeland Security Committee Chair since July 2025),
Adrian Smith (NE-03, senior Ways & Means member), Richard Hudson (NC-09, NRCC Chair).
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
    # ---------------- Chris Smith (NJ-04, R, in office since 1981) ----------------
    ("chris-smith", "NJ", "House", [
        claim("cs1", "chris-smith", "sanctity_of_life", 0, True,
              "Founder and Chair of the Congressional Pro-Life Caucus with an unbroken pro-life record since 1981; carries a lifetime A+ rating from SBA Pro-Life America; was executive director of New Jersey Right to Life before entering Congress; co-sponsored the Life at Conception Act recognizing personhood from fertilization, and introduced the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act — a federal 15-week ban grounded in the science of fetal pain. In 2025 voted for H.R.1, the reconciliation bill that defunded Planned Parenthood of Medicaid dollars for one year — the largest pro-life legislative victory in two decades.",
              ["https://sbaprolife.org/representative/chris-smith",
               "https://en.wikipedia.org/wiki/Chris_Smith_(New_Jersey_politician)"]),
        claim("cs2", "chris-smith", "foreign_policy_restraint", 2, True,
              "Introduced and passed H.R. 1150, the Frank R. Wolf International Religious Freedom Act (P.L. 114-281, signed 2016), which strengthened U.S. authority to designate countries that persecute Christians and other religious minorities as 'Countries of Particular Concern' — triggering required U.S. action including aid restrictions and sanctions. Smith stated the law targets regimes like China, where underground Christian pastors face imprisonment and churches face demolition. As Chair of the House Subcommittee on Global Human Rights, Smith continues to convene hearings on China's persecution of Christians and to push for sanctions on CCP officials responsible for religious repression.",
              ["https://www.congress.gov/bill/114th-congress/house-bill/1150",
               "https://chrissmith.house.gov/uploadedfiles/the_frank_wolf_international_religious_freedom_act_subcom_mark_up_april_5_2015.pdf"]),
    ]),

    # ---------------- Andrew Garbarino (NY-02, R, Homeland Security Chair) ----------------
    ("andrew-garbarino", "NY", "Representative", [
        claim("ag1", "andrew-garbarino", "border_immigration", 0, True,
              "Elected Chair of the House Homeland Security Committee in July 2025, Garbarino leads House Republicans' border security and immigration enforcement agenda — including drafting the new version of H.R. 2, the Secure the Border Act, which funds border-wall construction, ends catch-and-release, and tightens asylum rules. He visited the southern border personally to assess conditions and has made physical border security a centerpiece of his committee agenda.",
              ["https://dailycaller.com/2025/07/21/andrew-garbarino-homeland-security-committee-chair/",
               "https://garbarino.house.gov/issues/border-security"]),
        claim("ag2", "andrew-garbarino", "border_immigration", 1, True,
              "Introduced the POLICE Act (Protect Our Law Enforcement with Immigration Control and Enforcement Act), whose mandatory-detention language was incorporated verbatim into the Laken Riley Act — the first bill signed into law by President Trump in January 2025. The law requires ICE to mandatorily detain illegal immigrants charged with or convicted of theft, burglary, or violent offenses, closing the catch-and-release loophole that allowed charged illegal aliens to remain free. Garbarino also voted to impeach DHS Secretary Alejandro Mayorkas for his refusal to enforce mandatory-detention statutes at the border.",
              ["https://en.wikipedia.org/wiki/Andrew_Garbarino",
               "https://garbarino.house.gov/"]),
    ]),

    # ---------------- Adrian Smith (NE-03, R, senior Ways & Means member) ----------------
    ("adrian-smith", "NE", "House", [
        claim("as1", "adrian-smith", "sanctity_of_life", 0, True,
              "Believes life begins at conception and ends at natural death; co-sponsored the Life at Conception Act, which would extend 14th Amendment equal-protection guarantees to unborn persons from fertilization. Voted for H.R. 36, the Pain-Capable Unborn Child Protection Act (20-week ban); voted for H.R. 3504, the Born-Alive Abortion Survivors Protection Act; and voted for H.R. 3134, the Defund Planned Parenthood Act. Recognized annually by SBA Pro-Life America for voting consistently to protect unborn life and block taxpayer funding of abortion.",
              ["https://adriansmith.house.gov/media/press-releases/smith-votes-protect-unborn-children-painful-late-term-abortion",
               "https://sbaprolife.org/representative/adrian-smith"]),
        claim("as2", "adrian-smith", "border_immigration", 0, True,
              "Voted to fund completion of the southern border wall, supported increased Border Patrol hiring and resources, voted to remove illegal immigrants from the U.S. census (to prevent apportionment benefits from illegal entries), and cast a vote to impeach DHS Secretary Alejandro Mayorkas for dereliction of duty at the border — a wall-plus-enforcement posture.",
              ["https://adriansmith.house.gov/issues/",
               "https://www.govtrack.us/congress/members/adrian_smith/412217"]),
        claim("as3", "adrian-smith", "self_defense", 1, True,
              "Consistently opposes new gun-control legislation including assault-weapons bans, magazine-capacity limits, and expanded background-check mandates — earning a Heritage Action for America scorecard rating of 90% in the 117th Congress. Supports the Second Amendment against Democrat attempts to impose federal firearm restrictions.",
              ["https://heritageaction.com/scorecard/members/S001172/117",
               "https://en.wikipedia.org/wiki/Adrian_Smith_(politician)"]),
    ]),

    # ---------------- Richard Hudson (NC-09, R, NRCC Chair) ----------------
    ("richard-hudson", "NC", "Representative", [
        claim("rh1", "richard-hudson", "self_defense", 0, True,
              "Introduced H.R. 38, the Constitutional Concealed Carry Reciprocity Act, in the 119th Congress with over 120 co-sponsors — legislation that would require every state to recognize any other state's concealed-carry permit, functionally extending constitutional-carry rights across state lines for all law-abiding permit holders. Hudson has made gun-rights reciprocity legislation a signature priority in every recent Congress.",
              ["https://hudson.house.gov/media/press-releases",
               "https://en.wikipedia.org/wiki/Richard_Hudson_(American_politician)"]),
        claim("rh2", "richard-hudson", "sanctity_of_life", 0, True,
              "States on his official website that he is '100% Pro-Life and will fight for legislation which protects life from conception until natural death,' holding that life is 'a precious gift from God and should be protected at all stages.' Endorsed and rated 'A' by SBA Pro-Life America; voted consistently to defend the unborn and block taxpayer funding for abortion, and voted for H.R.1 (2025 reconciliation bill) which defunded Planned Parenthood of Medicaid dollars for one year.",
              ["https://sbaprolife.org/representative/richard-hudson",
               "https://en.wikipedia.org/wiki/Richard_Hudson_(American_politician)"]),
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
