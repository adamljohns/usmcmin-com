#!/usr/bin/env python3
"""Enrichment batch 216: second-round claims for 5 sitting U.S. Representatives.

Primary archetype_curated bucket exhausted; targets are evidence_curated
sitting federal representatives from the bottom of the alphabet with only
2 existing claims each.

Targets (TX x2, TN x2, PA x1):
  Vicente Gonzalez (TX-34, D), Beth Van Duyne (TX-24, R),
  Scott DesJarlais (TN-04, R), David Kustoff (TN-08, R),
  Mike Kelly (PA-16, R).

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
    # ---------------- Vicente Gonzalez (TX-34, D, US Representative) ----------------
    ("vicente-gonzalez", "TX", "Representative", [
        claim("vg3", "vicente-gonzalez", "border_immigration", 1, True,
              "One of 48 House Democrats to vote Yea on H.R. 29, the Laken Riley Act (January 7, 2025), requiring ICE to detain illegal aliens arrested for theft, burglary, or larceny — crossing party lines to support mandatory immigration enforcement from his South Texas border district.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act"]),
        claim("vg4", "vicente-gonzalez", "economic_stewardship", 2, True,
              "Co-chairs the fiscally conservative Blue Dog Coalition, which demands pay-as-you-go budget rules and deficit reduction; has broken with House Democratic leadership to oppose deficit-expanding spending packages and back balanced-budget principles.",
              ["https://en.wikipedia.org/wiki/Vicente_Gonzalez_(American_politician)",
               "https://bluedogcaucus.house.gov/"]),
    ]),

    # ---------------- Beth Van Duyne (TX-24, R, US Representative) ----------------
    ("beth-van-duyne", "TX", "Representative", [
        claim("bvd3", "beth-van-duyne", "economic_stewardship", 2, True,
              "Voted against the Fiscal Responsibility Act of 2023, arguing it did not cut spending enough; publicly called for 'return to pre-pandemic spending levels' and championed a 13%+ top-line cut including a 39% EPA reduction and a 28% Commerce-Justice cut — a firm anti-deficit stance.",
              ["https://ballotpedia.org/Beth_Van_Duyne",
               "https://www.govtrack.us/congress/members/beth_van_duyne/456850"]),
        claim("bvd4", "beth-van-duyne", "self_defense", 1, True,
              "Voted against the Assault Weapons Ban of 2022 (H.R. 1808) and has pledged to 'Protect the Second Amendment' as a core legislative priority, opposing new restrictions on semi-automatic firearms, magazine limits, and red-flag laws.",
              ["https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://ballotpedia.org/Beth_Van_Duyne"]),
    ]),

    # ---------------- Scott DesJarlais (TN-04, R, US Representative) ----------------
    ("scott-desjarlais", "TN", "Representative", [
        claim("sdj3", "scott-desjarlais", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record with the National Right to Life Committee; as a physician, believes all human life should be 'cherished and protected' and has voted consistently to stop taxpayer funding of abortion domestically and internationally.",
              ["https://sbaprolife.org/representative/scott-desjarlais",
               "https://ballotpedia.org/Scott_DesJarlais"]),
        claim("sdj4", "scott-desjarlais", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023 (May 11, 2023), which mandated border-wall construction, tightened asylum eligibility, and required DHS to detain illegal border crossers — supporting full physical-barrier and enforcement measures.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Scott_DesJarlais"]),
        claim("sdj5", "scott-desjarlais", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who has stated that 'hard working, law abiding citizens have to live within their means each year and they should expect their government to do the same'; opposed deficit-expanding legislation and demanded balanced-budget discipline throughout his tenure.",
              ["https://ballotpedia.org/Scott_DesJarlais",
               "https://www.govtrack.us/congress/members/scott_desjarlais/412477"]),
    ]),

    # ---------------- David Kustoff (TN-08, R, US Representative) ----------------
    ("david-kustoff", "TN", "Representative", [
        claim("dk3", "david-kustoff", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (H.R. 8404) on December 8, 2022, one of 169 House Republicans opposing the bill that would require all states to recognize same-sex marriages — maintaining the traditional one-man-one-woman definition in his legislative record.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://www.govtrack.us/congress/votes/117-2022/h513"]),
        claim("dk4", "david-kustoff", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023, to resume border-wall construction and tighten asylum; rated 92% by the Federation for American Immigration Reform (FAIR) for his pro-enforcement record; publicly called out the 'Biden Border Crisis' as jeopardizing national security.",
              ["https://ballotpedia.org/David_Kustoff",
               "https://www.govtrack.us/congress/votes/118-2023/h209"]),
        claim("dk5", "david-kustoff", "economic_stewardship", 2, True,
              "Signed the Taxpayer Protection Pledge with Americans for Tax Reform; rated 100% by FreedomWorks and 97% by Club for Growth; championed the 2017 Tax Cuts and Jobs Act as returning money to hard-working Americans and has consistently opposed deficit-expanding legislation.",
              ["https://ballotpedia.org/David_Kustoff",
               "https://justfacts.votesmart.org/candidate/48997/david-kustoff"]),
    ]),

    # ---------------- Mike Kelly (PA-16, R, US Representative) ----------------
    ("mike-kelly", "PA", "Representative", [
        claim("mk3", "mike-kelly", "election_integrity", 0, True,
              "Filed a September 2024 lawsuit demanding photo-ID verification for overseas and military absentee ballots in Pennsylvania; earlier joined a Supreme Court case seeking to scrutinize mail-in ballot procedures in GA, MI, PA, and WI — a consistent advocate for ballot-integrity enforcement measures.",
              ["https://ballotpedia.org/Mike_Kelly_(Pennsylvania)",
               "https://en.wikipedia.org/wiki/Mike_Kelly_(Pennsylvania_politician)"]),
        claim("mk4", "mike-kelly", "border_immigration", 0, True,
              "Praised and voted for H.R. 2, the Secure the Border Act of 2023 (supporting border-wall construction); and backed the Laken Riley Act (signed January 2025) requiring ICE to detain illegal aliens who commit theft or burglary, citing the need to 'protect American communities.'",
              ["https://kelly.house.gov/media/press-releases/kelly-praises-house-passage-secure-border-act",
               "https://kelly.house.gov/media/press-releases/kelly-backs-laken-riley-act-bill-goes-president-trump-signature"]),
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
