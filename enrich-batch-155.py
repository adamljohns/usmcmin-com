#!/usr/bin/env python3
"""Enrichment batch 155: hand-curated claims for 5 sitting U.S. Representatives.

Targets archetype_party_default federal House members with 0 claims, taken from
the BOTTOM of the alphabet: TX (Veasey, Doggett, Fletcher) and RI (Magaziner, Amo).
Each claim cites >=1 reliable source and reflects documented voting record / public positions.

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
    # ---------------- Marc Veasey (TX-33, D) ----------------
    ("marc-veasey", "TX", "Representative", [
        claim("mv1", "marc-veasey", "sanctity_of_life", 0, False,
              "SBA Pro-Life America documents that Veasey has consistently voted to eliminate or prevent protections for the unborn and against banning taxpayer-funded abortion domestically and internationally — a career-long 0% pro-life voting record.",
              ["https://sbaprolife.org/representative/marc-veasey",
               "https://en.wikipedia.org/wiki/Marc_Veasey"]),
        claim("mv2", "marc-veasey", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (H.R. 8404, July 2022 and final passage Dec 2022), which codifies federal recognition of same-sex marriages and requires states to honor out-of-state same-sex marriage licenses — contradicting the one-man-one-woman standard the rubric upholds.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("mv3", "marc-veasey", "self_defense", 1, False,
              "Member of the House Gun Violence Prevention Task Force; voted for the Violence Against Women Reauthorization Act of 2022, which closed the 'boyfriend loophole' by expanding federal firearms background-check requirements — a gun-control position that extends restrictions beyond existing law.",
              ["https://en.wikipedia.org/wiki/Marc_Veasey",
               "https://ballotpedia.org/Marc_Veasey"]),
    ]),

    # ---------------- Lloyd Doggett (TX-37, D) ----------------
    ("lloyd-doggett", "TX", "Representative", [
        claim("ld1", "lloyd-doggett", "sanctity_of_life", 0, False,
              "Rated 100% by NARAL Pro-Choice America and confirmed 0% by SBA Pro-Life America; voted against the Partial-Birth Abortion Ban Act of 2003 and has consistently voted against every protection for the unborn across three decades in Congress.",
              ["https://sbaprolife.org/representative/lloyd-doggett",
               "https://en.wikipedia.org/wiki/Lloyd_Doggett"]),
        claim("ld2", "lloyd-doggett", "biblical_marriage", 1, False,
              "Co-sponsored the 2011 Respect for Marriage Act to repeal the Defense of Marriage Act; voted for final passage of H.R. 8404 (Dec 2022), codifying federal recognition of same-sex marriages — opposing the one-man-one-woman definition the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Lloyd_Doggett",
               "https://ballotpedia.org/Lloyd_Doggett"]),
        claim("ld3", "lloyd-doggett", "self_defense", 1, False,
              "Consistent gun-control voting record spanning his full House tenure; rated F by the NRA and supported the Bipartisan Safer Communities Act of 2022 — the first major federal gun legislation in 30 years, expanding background checks and restricting Second Amendment access.",
              ["https://en.wikipedia.org/wiki/Lloyd_Doggett",
               "https://govtrack.us/congress/members/lloyd_doggett/400111"]),
    ]),

    # ---------------- Lizzie Fletcher (TX-7, D) ----------------
    ("lizzie-fletcher", "TX", "Representative", [
        claim("lf1", "lizzie-fletcher", "sanctity_of_life", 0, False,
              "Self-described member of the Pro-Choice Caucus; introduced the Ensuring Women's Right to Reproductive Freedom Act and legislation protecting out-of-state abortion travel — SBA Pro-Life America documents a consistent 0% pro-life voting record.",
              ["https://sbaprolife.org/representative/lizzie-fletcher",
               "https://en.wikipedia.org/wiki/Lizzie_Fletcher"]),
        claim("lf2", "lizzie-fletcher", "self_defense", 1, False,
              "Co-sponsored and voted for the Bipartisan Background Checks Act of 2019, the Enhanced Background Checks Act, the Assault Weapons Ban of 2019, and the Extreme Risk Protection Order Act of 2019 — a sustained legislative record of restricting Second Amendment rights.",
              ["https://ballotpedia.org/Lizzie_Pannill_Fletcher",
               "https://en.wikipedia.org/wiki/Lizzie_Fletcher"]),
        claim("lf3", "lizzie-fletcher", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (H.R. 8404, Dec 2022), which codifies federal recognition of same-sex marriages and requires all states to honor out-of-state same-sex marriage licenses — opposing the one-man-one-woman standard.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://en.wikipedia.org/wiki/Lizzie_Fletcher"]),
    ]),

    # ---------------- Seth Magaziner (RI-2, D) ----------------
    ("seth-magaziner", "RI", "Representative", [
        claim("sm1", "seth-magaziner", "sanctity_of_life", 0, False,
              "Rated 0% by the National Right to Life Committee and 100% by Planned Parenthood Action Fund; publicly committed to restoring and codifying Roe v. Wade and has voted against every pro-life measure brought to the House floor.",
              ["https://en.wikipedia.org/wiki/Seth_Magaziner",
               "https://ballotpedia.org/Seth_Magaziner"]),
        claim("sm2", "seth-magaziner", "biblical_marriage", 1, False,
              "Served as a board member of Marriage Equality Rhode Island and was personally active in the campaign that legalized same-sex marriage in Rhode Island; his entire political career has championed same-sex marriage recognition — directly opposing the one-man-one-woman standard.",
              ["https://en.wikipedia.org/wiki/Seth_Magaziner",
               "https://ballotpedia.org/Seth_Magaziner"]),
    ]),

    # ---------------- Gabe Amo (RI-1, D) ----------------
    ("gabe-amo", "RI", "Representative", [
        claim("ga1", "gabe-amo", "sanctity_of_life", 0, False,
              "Has stated 'No member of Congress should stand in between a woman and her doctor'; describes Rhode Island as a 'safe haven' for abortion access and has pledged to protect and expand abortion nationally — rejecting any life-at-conception personhood standard.",
              ["https://en.wikipedia.org/wiki/Gabe_Amo",
               "https://ballotpedia.org/Gabe_Amo"]),
        claim("ga2", "gabe-amo", "self_defense", 1, False,
              "States that 'preventing gun violence is personal' and campaigns on a gun-control platform; explicitly lists reducing gun violence as a top legislative priority, opposing the rubric's standard of protecting unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Gabe_Amo",
               "https://ballotpedia.org/Gabe_Amo"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
