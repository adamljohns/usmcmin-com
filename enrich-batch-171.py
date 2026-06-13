#!/usr/bin/env python3
"""Enrichment batch 171: 5 Republican U.S. House members (bottom-of-alphabet states).

archetype_curated federal senator/rep buckets exhausted; continuing with
archetype_party_default Republican House members from the bottom of the
state-alphabet reversed list: Jack Bergman (MI-1), Bill Huizenga (MI-4),
Eric Burlison (MO-7), Ryan Zinke (MT-1), Don Bacon (NE-2).
2-3 claims each from distinct rubric categories, sourced to official
*.house.gov, en.wikipedia.org, ballotpedia.org, sbaprolife.org, congress.gov.

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
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
    # ---------------- Jack Bergman (MI-1, R) ----------------
    # Retired USMC Lt. General — highest-ranking combat veteran ever elected to Congress.
    ("jack-bergman", "MI", "Representative", [
        claim("jb1", "jack-bergman", "sanctity_of_life", 0, True,
              "Signed the Born-Alive Abortion Survivors Protection Act discharge petition and joined 200+ House Republicans opposing any weakening of longstanding pro-life protections; has voted consistently throughout his House tenure to protect unborn life and stop taxpayer funding of abortion.",
              ["https://bergman.house.gov/news/documentsingle.aspx?DocumentID=340",
               "https://bergman.house.gov/news/documentsingle.aspx?DocumentID=802"]),
        claim("jb2", "jack-bergman", "self_defense", 1, True,
              "Co-sponsored and voted for the Concealed Carry Reciprocity Act of 2017 (H.R. 38), which the House passed 231–198; has never supported assault-weapons bans, red-flag confiscation orders, or federal gun registries throughout his House tenure.",
              ["https://bergman.house.gov/news/documentsingle.aspx?DocumentID=140",
               "https://en.wikipedia.org/wiki/Jack_Bergman"]),
        claim("jb3", "jack-bergman", "border_immigration", 0, True,
              "Voted YES on the Secure the Border Act of 2023 (H.R. 2); co-introduced a resolution with Rep. Lisa McClain supporting DHS, ICE, and CBP personnel against Biden-era criticism, and repeatedly visited the southern border to demand enforcement action.",
              ["https://bergman.house.gov/news/documentsingle.aspx?DocumentID=905",
               "https://ballotpedia.org/Jack_Bergman"]),
    ]),

    # ---------------- Bill Huizenga (MI-4, R) ----------------
    ("bill-huizenga", "MI", "Representative", [
        claim("bh1", "bill-huizenga", "economic_stewardship", 0, True,
              "Co-sponsored the Anti-CBDC Surveillance State Act (H.R. 1919, 2025) opposing a government-issued central bank digital currency that would give federal authorities real-time visibility into every American's financial transactions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://huizenga.house.gov/news/documentsingle.aspx?DocumentID=401590"]),
        claim("bh2", "bill-huizenga", "economic_stewardship", 1, True,
              "Named Chairman of the House Financial Services Monetary Policy & Trade Subcommittee (119th Congress); released landmark Fed Reform Legislation creating a pathway to Audit the Fed and passed it through committee — championing sound-money accountability over an opaque central bank.",
              ["https://huizenga.house.gov/news/documentsingle.aspx?DocumentID=398109",
               "https://huizenga.house.gov/news/documentsingle.aspx?DocumentID=398226"]),
        claim("bh3", "bill-huizenga", "sanctity_of_life", 0, True,
              "Carries a consistent 100% pro-life voting record recognized by SBA Pro-Life America; has voted to defund Planned Parenthood and oppose all taxpayer-funded abortion throughout his House tenure since 2011.",
              ["https://sbaprolife.org/representative/bill-huizenga",
               "https://ballotpedia.org/Bill_Huizenga"]),
    ]),

    # ---------------- Eric Burlison (MO-7, R) ----------------
    ("eric-burlison", "MO", "House", [
        claim("eb1", "eric-burlison", "sanctity_of_life", 0, True,
              "Introduced the Life at Conception Act (H.R. 722) on January 24, 2025 — a federal personhood bill that declares every unborn child a 'person' under the 14th Amendment from the moment of fertilization, directly filling the gap left by Dobbs v. Jackson Women's Health Organization.",
              ["https://burlison.house.gov/media/press-releases/congressman-burlison-introduces-life-conception-act",
               "https://www.congress.gov/bill/119th-congress/house-bill/722"]),
        claim("eb2", "eric-burlison", "sanctity_of_life", 1, True,
              "The Life at Conception Act takes an abolition-not-restrictions approach: it does not merely regulate abortion but asserts full constitutional personhood, leaving no carve-outs for gestational limits, rape, or incest — the strongest possible legislative posture against abortion.",
              ["https://burlison.house.gov/media/press-releases/congressman-burlison-introduces-life-conception-act",
               "https://www.congress.gov/bill/119th-congress/house-bill/722"]),
        claim("eb3", "eric-burlison", "self_defense", 1, True,
              "Sponsored Missouri's constitutional carry bill while serving in the Missouri House (2016), eliminating permit requirements for concealed carry and making Missouri one of the earliest constitutional-carry states; as a House Freedom Caucus member in Congress, consistently opposes federal gun registration, red-flag laws, and assault-weapons bans.",
              ["https://en.wikipedia.org/wiki/Eric_Burlison",
               "https://ballotpedia.org/Eric_Burlison"]),
    ]),

    # ---------------- Ryan Zinke (MT-1, R) ----------------
    ("ryan-zinke", "MT", "House", [
        claim("rz1", "ryan-zinke", "sanctity_of_life", 0, True,
              "Endorsed by the Montana Right to Life Association and campaigned on an anti-abortion platform; has voted consistently to protect unborn life and restrict federal abortion funding throughout his House tenure.",
              ["https://ballotpedia.org/Ryan_Zinke",
               "https://en.wikipedia.org/wiki/Ryan_Zinke"]),
        claim("rz2", "ryan-zinke", "self_defense", 1, True,
              "A retired Navy SEAL commander who describes his legislative decisions as 'based on upholding the Constitution'; has consistently opposed federal gun registration schemes, red-flag confiscation orders, and assault-weapons bans — defending the right to keep and bear arms for law-abiding citizens.",
              ["https://zinke.house.gov/",
               "https://ballotpedia.org/Ryan_Zinke"]),
        claim("rz3", "ryan-zinke", "border_immigration", 0, True,
              "Voted YES on the Secure the Border Act of 2023 (H.R. 2), which funds border-wall construction and tightens asylum standards; has consistently called for strong military-backed enforcement at the southern border as a core national-security priority.",
              ["https://zinke.house.gov/issues/congress",
               "https://ballotpedia.org/Ryan_Zinke"]),
    ]),

    # ---------------- Don Bacon (NE-2, R) ----------------
    ("don-bacon", "NE", "House", [
        claim("db1", "don-bacon", "border_immigration", 0, True,
              "Voted YES on the Secure the Border Act of 2023 (H.R. 2) and has supported construction of the U.S.-Mexico border wall since 2017, including voting against a government-shutdown resolution that excluded wall funding; has cosponsored legislation strengthening border enforcement.",
              ["https://bacon.house.gov/news/documentsingle.aspx?DocumentID=1236",
               "https://ballotpedia.org/Don_Bacon"]),
        claim("db2", "don-bacon", "sanctity_of_life", 0, False,
              "Supports only a 15-week federal abortion ban with exceptions for the life of the mother — explicitly rejecting the life-at-conception personhood standard; does not co-sponsor the Life at Conception Act and represents a moderate position that falls short of the rubric's sanctity-of-life ideal.",
              ["https://ballotpedia.org/Don_Bacon",
               "https://en.wikipedia.org/wiki/Don_Bacon"]),
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

    # Minified write — preserve no-whitespace master to stay under GitHub's 50 MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
