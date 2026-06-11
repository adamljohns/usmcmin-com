#!/usr/bin/env python3
"""Enrichment batch 130: hand-curated claims for 5 sitting U.S. Senators.

Targets sitting senators with unset confidence and 0 claims, drawn from the
bottom of the alphabet (ME, IN, IA, AZ, AK) — the complement of the top-of-
alphabet loop running concurrently.

Mix: Dan Sullivan (AK-R), Chuck Grassley (IA-R), Todd Young (IN-R),
     Angus King (ME-I), Ruben Gallego (AZ-D).
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


TARGETS = [
    # ---------------- Dan Sullivan (AK-R, US Senator) ----------------
    ("dan-sullivan", "AK", "Senator", [
        claim("ds1", "dan-sullivan", "sanctity_of_life", 0, True,
              "SBA Pro-Life America endorsed Sullivan for his 2026 re-election on the strength of his 100% pro-life voting record; he co-sponsored both the Pain-Capable Unborn Child Protection Act and the Born-Alive Abortion Survivors Protection Act, affirming protection of human life from conception.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-lists-candidate-fund-pac-endorses-u-s-senator-dan-sullivan-re-election",
               "https://en.wikipedia.org/wiki/Dan_Sullivan_(U.S._senator)"]),
        claim("ds2", "dan-sullivan", "self_defense", 1, True,
              "Voted against Senate gun-control legislation; his office issued a press release titled 'Sullivan Votes to Protect Second Amendment Rights of Alaskans,' affirming his consistent opposition to new firearm restrictions.",
              ["https://www.sullivan.senate.gov/newsroom/press-releases/sullivan-votes-to-protect-second-amendment-rights-of-alaskans",
               "https://en.wikipedia.org/wiki/Dan_Sullivan_(U.S._senator)"]),
        claim("ds3", "dan-sullivan", "border_immigration", 1, True,
              "Joined 53 Senate colleagues in co-introducing the Laken Riley Act (2025) requiring mandatory detention of illegal aliens charged with theft or violent crimes; has consistently backed border-wall funding and enforcement-first immigration measures and opposed the 2024 bipartisan border deal as too weak.",
              ["https://www.sullivan.senate.gov/newsroom/press-releases/sen-sullivan-joins-53-senate-colleagues-in-introducing-laken-riley-act",
               "https://www.sullivan.senate.gov/newsroom/press-releases/senator-sullivan-statement-on-senate-border-legislation"]),
    ]),

    # ---------------- Chuck Grassley (IA-R, US Senator) ----------------
    ("chuck-grassley", "IA", "Senator", [
        claim("cg1", "chuck-grassley", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America for a decades-long career of pro-life Senate votes; has publicly denounced the Women's Health Protection Act, pressed nominees on late-term abortion, and introduced legislation blocking taxpayer funding for abortion travel for undocumented minors.",
              ["https://sbaprolife.org/senator/chuck-grassley",
               "https://en.wikipedia.org/wiki/Chuck_Grassley"]),
        claim("cg2", "chuck-grassley", "self_defense", 1, True,
              "Co-authored the Protecting Communities and Preserving the Second Amendment Act (with Sen. Cruz) to improve the National Instant Criminal Background Check System targeting criminals — without expanding restrictions on law-abiding gun owners — and has opposed broad gun-control measures throughout his Senate tenure.",
              ["https://www.grassley.senate.gov/news/news-releases/grassley-cruz-work-to-safeguard-second-amendment-rights-protect-communities-from-gun-violence",
               "https://en.wikipedia.org/wiki/Chuck_Grassley"]),
        claim("cg3", "chuck-grassley", "economic_stewardship", 2, True,
              "Consistent fiscal hawk who has stalled large spending packages from both parties and listed 'curbing wasteful spending' and deficit reduction as top 2024 legislative priorities; has cast more than 11,000 Senate votes with a near-perfect attendance record, building a long record of opposing unauthorized deficit expenditures.",
              ["https://www.grassley.senate.gov/news/news-releases/grassley-shares-2024-policy-oversight-achievements",
               "https://www.grassley.senate.gov/news/news-releases/grassley-has-cast-11000-votes-us-senate"]),
    ]),

    # ---------------- Todd Young (IN-R, US Senator) ----------------
    ("todd-young", "IN", "Senator", [
        claim("ty1", "todd-young", "sanctity_of_life", 0, True,
              "Earned a 100% lifetime rating from the National Right to Life Committee and a 0% score from both NARAL Pro-Choice America and Planned Parenthood; has consistently voted against pro-abortion legislation throughout his Senate tenure.",
              ["https://en.wikipedia.org/wiki/Todd_Young",
               "https://ballotpedia.org/Todd_Young"]),
        claim("ty2", "todd-young", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (June 2022), which created new federal funding streams for state red-flag laws and imposed enhanced background-check requirements on firearm purchasers under age 21 — contradicting the rubric's opposition to red-flag legislation.",
              ["https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act",
               "https://en.wikipedia.org/wiki/Todd_Young"]),
        claim("ty3", "todd-young", "border_immigration", 1, True,
              "Opposes amnesty pathways for undocumented immigrants including the DREAM Act; has stated that the U.S. immigration system should be based on merit and job skills rather than chain migration or illegal-entry rewarding.",
              ["https://en.wikipedia.org/wiki/Todd_Young",
               "https://ballotpedia.org/Todd_Young"]),
    ]),

    # ---------------- Angus King (ME-I, US Senator) ----------------
    ("angus-king", "ME", "Senator", [
        claim("ak1", "angus-king", "sanctity_of_life", 0, False,
              "Supports unrestricted abortion access; publicly called the Supreme Court's Dobbs v. Jackson ruling 'a dangerous, blatantly political ruling' and has voted consistently with Senate Democrats against any restrictions on abortion — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Angus_King",
               "https://ballotpedia.org/Angus_King"]),
        claim("ak2", "angus-king", "biblical_marriage", 1, False,
              "A cosponsor and affirmative voter on the Respect for Marriage Act (2022), which federally codifies same-sex marriage; stated publicly that 'the government should have no say' in who people choose to marry — explicitly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.king.senate.gov/newsroom/press-releases/king-statement-after-senate-passes-protections-for-marriage-equality",
               "https://en.wikipedia.org/wiki/Angus_King"]),
        claim("ak3", "angus-king", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), a gun-control bill that funded state red-flag laws and expanded background-check requirements — consistent with his broader support for firearms restrictions and contrary to the rubric's opposition to red-flag legislation.",
              ["https://en.wikipedia.org/wiki/Angus_King",
               "https://ballotpedia.org/Angus_King"]),
    ]),

    # ---------------- Ruben Gallego (AZ-D, US Senator) ----------------
    ("ruben-gallego", "AZ", "Senator", [
        claim("rg1", "ruben-gallego", "sanctity_of_life", 0, False,
              "Supports abortion rights as a near-absolute constitutional guarantee; opposed the Dobbs v. Jackson ruling and endorsed Arizona Proposition 139 (2024) enshrining abortion rights in the state constitution; carries a 100% rating from Reproductive Freedom for All (formerly NARAL).",
              ["https://en.wikipedia.org/wiki/Ruben_Gallego",
               "https://ballotpedia.org/Ruben_Gallego"]),
        claim("rg2", "ruben-gallego", "self_defense", 1, False,
              "Advocates breaking the Senate filibuster to pass federal gun-control legislation; has called for an assault-weapons ban and supported background-check expansions — consistently opposing Second Amendment protections throughout his House and Senate career.",
              ["https://en.wikipedia.org/wiki/Ruben_Gallego",
               "https://ballotpedia.org/Ruben_Gallego"]),
        claim("rg3", "ruben-gallego", "border_immigration", 1, True,
              "Broke with the Senate Democratic caucus in 2025 to vote for the Laken Riley Act, which mandates detention of illegal aliens charged with theft or violent crimes; said his party is 'largely out of touch' with average voters on border enforcement.",
              ["https://en.wikipedia.org/wiki/Ruben_Gallego",
               "https://ballotpedia.org/Ruben_Gallego"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
