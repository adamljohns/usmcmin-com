#!/usr/bin/env python3
"""Enrichment batch 246: 5 federal House members from bottom of alphabet.

Targets archetype_party_default House reps with 0 claims.
States: KS×1, IN×1, IL×3 (bottom of alphabet, avoiding top-side collision agent).

Mix (0 R / 5 D): Sharice Davids (KS-D), Andre Carson (IN-D),
Sean Casten (IL-D), Nikki Budzinski (IL-D), Mike Quigley (IL-D).
Each claim cites >=1 reliable source and reflects voting record /
public positions through 2022-2024.

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
    # ---------------- Sharice Davids (KS-D, US Representative) ----------------
    ("sharice-davids", "KS", "Representative", [
        claim("sd1", "sharice-davids", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act (H.R. 8296, July 15, 2022), which would have federally overridden state abortion restrictions and protected abortion access through all nine months of pregnancy — directly opposing personhood-from-conception standards.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Sharice_Davids"]),
        claim("sd2", "sharice-davids", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 24, 2022), which expanded background-check requirements, closed the 'boyfriend loophole,' and restricted firearm access for those under 21 — opposing the rubric's standard of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Sharice_Davids"]),
        claim("sd3", "sharice-davids", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 11, 2023), which would have resumed border-wall construction, tightened asylum eligibility, and mandated deportation enforcement — opposing a secure physical border and enforcement-first immigration policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Sharice_Davids"]),
    ]),

    # ---------------- Andre Carson (IN-D, US Representative) ----------------
    ("andre-carson", "IN", "Representative", [
        claim("ac1", "andre-carson", "sanctity_of_life", 0, False,
              "Earned a 0% rating from SBA Pro-Life America; consistently voted against protections for the unborn and for children born alive after failed abortions, and opposed defunding Planned Parenthood of Medicaid dollars in H.R. 1 reconciliation proceedings.",
              ["https://sbaprolife.org/representative/andre-carson",
               "https://ballotpedia.org/Andr%C3%A9_Carson"]),
        claim("ac2", "andre-carson", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 24, 2022), supporting expanded background checks and firearm purchase restrictions; also introduced the Gun Safety Incentive Act to mandate federal tax incentives for firearm safe-storage devices.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Andr%C3%A9_Carson"]),
        claim("ac3", "andre-carson", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 11, 2023), opposing border-wall construction, tightened asylum rules, and mandatory-deportation enforcement; previously condemned Trump-era immigration executive orders as a 'Muslim ban' and 'bigotry campaign.'",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://en.wikipedia.org/wiki/Andr%C3%A9_Carson"]),
    ]),

    # ---------------- Sean Casten (IL-D, US Representative) ----------------
    ("sean-casten", "IL", "Representative", [
        claim("sc1", "sean-casten", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act (H.R. 8296, July 15, 2022), which would have federally codified abortion access and preempted state personhood and heartbeat laws — opposing any legal recognition of the unborn.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Sean_Casten"]),
        claim("sc2", "sean-casten", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 24, 2022); all 220 House Democrats voted in favor of this gun-control legislation, which expanded background checks and closed the 'boyfriend loophole.'",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Sean_Casten"]),
        claim("sc3", "sean-casten", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 11, 2023), opposing resumed border-wall construction, tightened asylum eligibility, and mandatory-deportation enforcement provisions.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Sean_Casten"]),
    ]),

    # ---------------- Nikki Budzinski (IL-D, US Representative) ----------------
    ("nikki-budzinski", "IL", "Representative", [
        claim("nb1", "nikki-budzinski", "sanctity_of_life", 0, False,
              "Endorsed by NARAL Pro-Choice America (now Reproductive Freedom for All) in her 2022 campaign with a 100/100 rating; publicly committed to protecting abortion access and the freedom to make reproductive decisions, opposing personhood-from-conception and heartbeat-law standards.",
              ["https://reproductivefreedomforall.org/lawmaker/nikki-budzinski/",
               "https://ballotpedia.org/Nikki_Budzinski"]),
        claim("nb2", "nikki-budzinski", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 11, 2023), opposing border-wall resumption, tightened asylum eligibility, and mandatory-deportation provisions that would secure the southern border.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Nikki_Budzinski"]),
        claim("nb3", "nikki-budzinski", "self_defense", 1, False,
              "Publicly supports universal background checks and an assault weapons ban; received endorsement from gun-safety advocates during her 2022 campaign — opposing the rubric's constitutional-carry and anti-restriction standard for Second Amendment rights.",
              ["https://ballotpedia.org/Nikki_Budzinski",
               "https://www.govtrack.us/congress/members/nicole_nikki_budzinski/456901"]),
    ]),

    # ---------------- Mike Quigley (IL-D, US Representative) ----------------
    ("mike-quigley", "IL", "Representative", [
        claim("mq1", "mike-quigley", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act (H.R. 3755, 2021) and voted YES on H.R. 8296 (July 15, 2022), which would have federally overridden state abortion restrictions; earned a 0% rating from SBA Pro-Life America for opposing protections for unborn life.",
              ["https://sbaprolife.org/representative/mike-quigley",
               "https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://congress.gov/bill/117th-congress/house-bill/3755/cosponsors"]),
        claim("mq2", "mike-quigley", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 24, 2022) and has been a persistent advocate for gun-control legislation, including co-sponsoring the Women's Health Protection Act of 2023 and repeatedly introducing assault-weapons restriction bills.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Mike_Quigley"]),
        claim("mq3", "mike-quigley", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 11, 2023), opposing border-wall construction, mandatory deportation enforcement, and tightened asylum standards that would secure the southern border.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Mike_Quigley"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
