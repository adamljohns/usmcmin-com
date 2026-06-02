#!/usr/bin/env python3
"""Enrichment batch 10: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims, taken from
the BOTTOM of the alphabet (OR, NV, NM, NM, NJ) to avoid collision with the
top-of-alphabet agent loop.

Mix (0 R / 5 D): Jeff Merkley (OR-D), Catherine Cortez Masto (NV-D),
Martin Heinrich (NM-D), Ben Ray Lujan (NM-D), Andy Kim (NJ-D).
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
    # ---------------- Jeff Merkley (OR-D, US Senator) ----------------
    ("jeff-merkley", "OR", "Senator", [
        claim("jm1", "jeff-merkley", "sanctity_of_life", 0, False,
              "A consistent pro-abortion-access senator who joined the full Senate Democratic caucus in introducing the Women's Health Protection Act of 2025 to guarantee a federal right to abortion nationwide, and championed legislation to repeal the Comstock Act — rejecting any personhood-from-conception standard.",
              ["https://www.merkley.senate.gov/on-3rd-anniversary-of-roe-being-overturned-merkley-and-wyden-join-bill-to-restore-abortion-access-nationwide/",
               "https://www.merkley.senate.gov/merkley-champions-legislation-to-repeal-the-comstock-act/"]),
        claim("jm2", "jeff-merkley", "biblical_marriage", 4, False,
              "Signed a joint letter with 40+ Senate colleagues demanding that no anti-LGBTQ+ provisions appear in must-pass government funding legislation, actively opposing any policy limits on LGBTQ+ promotion — the opposite of the rubric's standard.",
              ["https://www.merkley.senate.gov/merkley-baldwin-booker-40-senators-no-new-anti-lgbtq-anti-abortion-provisions-in-must-pass-government-funding-bills/",
               "https://en.wikipedia.org/wiki/Jeff_Merkley"]),
        claim("jm3", "jeff-merkley", "self_defense", 1, False,
              "A gun-control advocate who supports universal background checks and restrictions on semi-automatic weapons; GovTrack's 2024 analysis ranked him among the most politically-left senators overall, consistent with his F-rated gun policy record.",
              ["https://en.wikipedia.org/wiki/Jeff_Merkley",
               "https://www.govtrack.us/congress/members/jeff_merkley/412325/report-card/2024"]),
    ]),

    # ---------------- Catherine Cortez Masto (NV-D, US Senator) ----------------
    ("catherine-cortez-masto", "NV", "Senator", [
        claim("ccm1", "catherine-cortez-masto", "self_defense", 1, False,
              "Carries an 'F' grade from the NRA Political Victory Fund. Cosponsored the Keep Americans Safe Act to ban magazines over ten rounds, cosponsored the Background Check Expansion Act for universal gun-sale checks, and backed an extreme-risk/red-flag-law grant program — opposing every element of the rubric's Second Amendment standard.",
              ["https://www.cortezmasto.senate.gov/news/press-releases/cortez-masto-cosponsors-bill-to-ban-high-capacity-gun-magazines/",
               "https://www.cortezmasto.senate.gov/news/press-releases/cortez-masto-colleagues-reintroduce-background-check-expansion-act-to-reduce-gun-violence-/"]),
        claim("ccm2", "catherine-cortez-masto", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act to codify a federal right to abortion and is publicly pro-choice, committing to protect abortion access in Nevada and nationally — rejecting any recognition of life from conception.",
              ["https://en.wikipedia.org/wiki/Catherine_Cortez_Masto",
               "https://ballotpedia.org/Catherine_Cortez_Masto"]),
        claim("ccm3", "catherine-cortez-masto", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (2022), which federally codified same-sex marriage and required all states to recognize same-sex unions — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Catherine_Cortez_Masto",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ---------------- Martin Heinrich (NM-D, US Senator) ----------------
    ("martin-heinrich", "NM", "Senator", [
        claim("mh1", "martin-heinrich", "sanctity_of_life", 0, False,
              "Co-announced legislation with Sen. Luján to 'restore abortion access nationwide' and vowed publicly 'I will not stop fighting until we federally protect women's reproductive freedoms, including restoring abortion access nationally' — rejecting any personhood-from-conception standard.",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/heinrich-lujan-announce-introduction-of-legislation-to-restore-abortion-access-nationwide",
               "https://www.heinrich.senate.gov/newsroom/press-releases/heinrich-i-will-not-stop-fighting-until-we-federally-protect-womens-reproductive-freedoms-including-restoring-abortion-access-nationally"]),
        claim("mh2", "martin-heinrich", "self_defense", 1, False,
              "Supports expanded background checks, bump-stock bans, and prohibiting sales to anyone on the federal no-fly list; backed the Bipartisan Safer Communities Act (2022) which funds crisis-intervention red-flag programs — counter to the rubric's opposition to red-flag laws and firearm restrictions.",
              ["https://en.wikipedia.org/wiki/Martin_Heinrich",
               "https://ballotpedia.org/Martin_Heinrich"]),
        claim("mh3", "martin-heinrich", "border_immigration", 0, False,
              "Supports a pathway to citizenship for Dreamers and opposes enforcement-only immigration approaches; his official platform emphasizes legal pathways rather than wall construction or military deployment — rejecting the rubric's wall-and-military-enforcement standard.",
              ["https://www.heinrich.senate.gov/priorities/issues/immigration",
               "https://en.wikipedia.org/wiki/Martin_Heinrich"]),
    ]),

    # ---------------- Ben Ray Lujan (NM-D, US Senator) ----------------
    ("ben-ray-lujan", "NM", "Senator", [
        claim("brl1", "ben-ray-lujan", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (November 2022), which federally codified same-sex marriage and compelled all states to recognize same-sex unions, stating 'Love is love' — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.lujan.senate.gov/newsroom/press-releases/lujan-statement-on-senate-passage-of-the-respect-for-marriage-act/",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("brl2", "ben-ray-lujan", "self_defense", 1, False,
              "Praised the Bipartisan Safer Communities Act (2022) as 'the most significant gun safety legislation to pass Congress in nearly three decades,' which funds crisis-intervention red-flag programs and expands background checks — opposing the rubric's standard against red-flag laws and firearm restrictions.",
              ["https://www.lujan.senate.gov/newsroom/press-releases/lujan-statement-on-the-senate-passage-of-bipartisan-safer-communities-act/",
               "https://en.wikipedia.org/wiki/Ben_Ray_Luj%C3%A1n"]),
        claim("brl3", "ben-ray-lujan", "sanctity_of_life", 0, False,
              "Co-introduced legislation with Sen. Heinrich to restore nationwide abortion access; described by his own office as 'an unwavering supporter of women's rights' who fights to protect reproductive freedom — rejecting personhood from conception.",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/heinrich-lujan-announce-introduction-of-legislation-to-restore-abortion-access-nationwide",
               "https://en.wikipedia.org/wiki/Ben_Ray_Luj%C3%A1n"]),
    ]),

    # ---------------- Andy Kim (NJ-D, US Senator) ----------------
    ("andy-kim", "NJ", "Senator", [
        claim("ak1", "andy-kim", "sanctity_of_life", 0, False,
              "Self-described 'proudly pro-choice' senator endorsed by Reproductive Freedom for All (formerly NARAL) for his 2024 Senate race; called the Dobbs decision an 'injustice' and pledged to codify reproductive rights into federal law, calling reproductive healthcare an 'essential human right' — rejecting personhood from conception.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-andy-kim-for-u-s-senate-in-new-jersey/",
               "https://en.wikipedia.org/wiki/Andy_Kim"]),
        claim("ak2", "andy-kim", "self_defense", 1, False,
              "Rated 'F' by the NRA Political Victory Fund; supports an assault weapons ban and universal background checks, previously voting against the House Secure the Border Act and stating 'Making progress on gun violence prevention isn't inevitable, but inaction is unacceptable' — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Andy_Kim",
               "https://ballotpedia.org/Andrew_Kim_(New_Jersey)"]),
        claim("ak3", "andy-kim", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (2022) as a U.S. Representative, codifying federal recognition of same-sex unions; co-sponsored the Equality Act to extend LGBTQ anti-discrimination protections into schools and public accommodations.",
              ["https://en.wikipedia.org/wiki/Andy_Kim",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
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
