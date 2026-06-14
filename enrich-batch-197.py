#!/usr/bin/env python3
"""Enrichment batch 197: evidence_federal House members from the bottom of the alphabet.

Targets evidence_federal candidates with 0 claims, sorted reverse-alpha by state.
Mix: 2R + 3D. Darrell Issa (CA-48-R, retiring sitting), Jimmy Panetta (CA-19-D,
sitting), Jimmy Gomez (CA-34-D, sitting), Kevin Lincoln II (CA-13-R, 2026
Trump-endorsed), Adam Gray (CA-13-D, sitting since Jan 2025).

MINIFIED write — see enrich-batch-4.py module docstring for rationale.
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
    # ---- Darrell Issa (CA-48, R, retiring sitting member) ----
    ("darrell-issa", "CA", "Representative", [
        claim("di1", "darrell-issa", "sanctity_of_life", 0, True,
              "Received an A+ rating from SBA Pro-Life America and earned the Susan B. Anthony List endorsement for his consistent record defending the unborn, blocking taxpayer funding for abortion travel, and pushing back on Biden-era abortion executive orders.",
              ["https://sbaprolife.org/representative/darrell-issa",
               "https://issa.house.gov/media/press-releases/issa-earns-pro-life-rating-susan-b-anthony-list"]),
        claim("di2", "darrell-issa", "border_immigration", 2, True,
              "Reintroduced the Sanctuary City Accountability Act to hold sanctuary jurisdictions liable for crimes committed by illegal immigrants they shield from ICE, and has stated publicly: 'We must build the wall. We can't keep our country safe if we don't secure the border.'",
              ["https://issa.house.gov/issues/immigration",
               "https://ballotpedia.org/Darrell_Issa"]),
        claim("di3", "darrell-issa", "self_defense", 1, True,
              "Introduced the Freedom from Unfair Gun Taxes Act (H.R. 2442) with Rep. Hudson and Sen. Risch to prohibit states from levying excise taxes on firearms and ammunition to fund gun-control programs — blocking a backdoor mechanism to burden law-abiding gun owners.",
              ["https://issa.house.gov/media/press-releases/issa-hudson-risch-block-attack-second-amendment-rights-introduce-bill-prohibit",
               "https://issa.house.gov/media/press-releases/reps-issa-hudson-and-senator-risch-introduce-bicameral-legislation-stop"]),
    ]),

    # ---- Jimmy Panetta (CA-19, D, sitting since Jan 2017) ----
    ("jimmy-panetta", "CA", "Representative", [
        claim("jp1", "jimmy-panetta", "sanctity_of_life", 0, False,
              "Holds a 100% rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America) and an F grade from SBA Pro-Life America; sits on the Pro-Choice Caucus and has committed to protecting abortion access at every stage, rejecting any recognition of personhood from conception.",
              ["https://reproductivefreedomforall.org/resources/2024-congressional-record-on-reproductive-freedom/",
               "https://ballotpedia.org/Jimmy_Panetta"]),
        claim("jp2", "jimmy-panetta", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice America / Reproductive Freedom for All — the core of the abortion-advocacy endorsement-and-funding network the rubric identifies as disqualifying.",
              ["https://reproductivefreedomforall.org/resources/2024-congressional-record-on-reproductive-freedom/",
               "https://en.wikipedia.org/wiki/Jimmy_Panetta"]),
        claim("jp3", "jimmy-panetta", "self_defense", 1, False,
              "Voted for H.R. 8, the Bipartisan Background Checks Act of 2021, extending federal background-check requirements to include private firearm transfers — expanding the federal gatekeeping apparatus the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Bipartisan_Background_Checks_Act",
               "https://ballotpedia.org/Jimmy_Panetta"]),
    ]),

    # ---- Jimmy Gomez (CA-34, D, sitting since June 2017) ----
    ("jimmy-gomez", "CA", "Representative", [
        claim("jg1", "jimmy-gomez", "sanctity_of_life", 0, False,
              "Holds a 100% rating from Reproductive Freedom for All (NARAL) and an F grade from SBA Pro-Life America; cosponsored and voted to pass the Women's Health Protection Act to codify abortion-on-demand through viability into federal law, rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Jimmy_Gomez",
               "https://ballotpedia.org/Jimmy_Gomez"]),
        claim("jg2", "jimmy-gomez", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (H.R. 8404, July 19, 2022), codifying federal recognition of same-sex marriages and repealing the Defense of Marriage Act — directly rejecting the one-man-one-woman standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("jg3", "jimmy-gomez", "self_defense", 1, False,
              "Congressional Progressive Caucus member who voted for H.R. 8, the Bipartisan Background Checks Act of 2021, expanding background-check mandates to private firearm transfers and has consistently supported gun-control legislation.",
              ["https://ballotpedia.org/Jimmy_Gomez",
               "https://www.govtrack.us/congress/members/jimmy_gomez/412739"]),
    ]),

    # ---- Kevin Lincoln II (CA-13, R, 2026 Trump-endorsed candidate) ----
    ("kevin-lincoln-ii", "CA", "Representative", [
        claim("kl1", "kevin-lincoln-ii", "border_immigration", 0, True,
              "Received President Trump's 'Complete and Total Endorsement' in December 2025 on the explicit basis of border security and conservative values; has stated border security is among his top campaign priorities and publicly supports Trump's border-wall and immigration-enforcement agenda.",
              ["https://www.abc10.com/video/news/local/stockton/trump-endorses-kevin-lincoln-for-ca-13/103-14d83b39-4551-4f51-93aa-5adb39441e10",
               "https://stocktonia.org/news/politics/2025/12/20/former-stockton-mayor-kevin-lincoln-honored-by-president-trumps-endorsement-in-race-against-rep-adam-gray/"]),
        claim("kl2", "kevin-lincoln-ii", "border_immigration", 1, True,
              "Publicly aligned with President Trump's mass deportation and immigration enforcement agenda, supporting aggressive enforcement as part of his stated platform for CA-13.",
              ["https://www.yourcentralvalley.com/election-2026/california-13th-congressional-race-2/",
               "https://ballotpedia.org/Kevin_Lincoln_II"]),
    ]),

    # ---- Adam Gray (CA-13, D, sitting since Jan 2025) ----
    ("adam-gray", "CA", "Representative", [
        claim("ag1", "adam-gray", "border_immigration", 1, True,
              "Voted for the Laken Riley Act of 2025 — mandating ICE detention of illegal immigrants charged with or convicted of crimes — one of only 46 House Democrats to cross party lines and support the immigration enforcement measure alongside all Republicans.",
              ["https://en.wikipedia.org/wiki/Adam_Gray",
               "https://ballotpedia.org/Adam_Gray"]),
        claim("ag2", "adam-gray", "sanctity_of_life", 0, False,
              "As a California Assemblymember, voted for SCA 10 enshrining abortion access in the California Constitution and for SB 1142 establishing the Abortion Practical Support Fund — establishing a consistent pro-choice public record that rejects personhood from conception.",
              ["https://ballotpedia.org/Adam_Gray",
               "https://justfacts.votesmart.org/candidate/key-votes/138552/adam-gray"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; slug uniqueness prevents collisions here."""
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
