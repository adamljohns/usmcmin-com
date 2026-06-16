#!/usr/bin/env python3
"""Enrichment batch 245: 5 federal House members from bottom of alphabet.

Targets archetype_party_default House reps with 0 claims.
States: MA×4, LA×1 (bottom of alphabet, avoiding top-side collision agent).

Mix (0 R / 5 D): Richard Neal (MA-D), Lori Trahan (MA-D),
Jake Auchincloss (MA-D), Bill Keating (MA-D), Troy Carter (LA-D).
Each claim cites >=1 reliable source and reflects voting record /
public positions through 2024-2026.

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
    # ---------------- Richard Neal (MA-D, US Representative) ----------------
    ("richard-neal", "MA", "Representative", [
        claim("rn1", "richard-neal", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act (H.R. 8296, July 2022), which would have federally overridden state abortion restrictions and protected abortion access through all nine months of pregnancy — directly opposing personhood-from-conception standards.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Richard_Neal"]),
        claim("rn2", "richard-neal", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 2022), which expanded background-check requirements and closed the 'boyfriend loophole' on firearm purchases — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Richard_Neal"]),
        claim("rn3", "richard-neal", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 11, 2023), which would have resumed border-wall construction and tightened asylum eligibility — opposing a secure physical border and enforcement-first immigration policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Richard_Neal"]),
    ]),

    # ---------------- Lori Trahan (MA-D, US Representative) ----------------
    ("lori-trahan", "MA", "Representative", [
        claim("lt1", "lori-trahan", "sanctity_of_life", 0, False,
              "Cosponsored H.Res.1285 expressing support for mifepristone access and voted YES on the Women's Health Protection Act (H.R. 8296, July 2022), endorsing a federal right to abortion that would override state life-protecting laws.",
              ["https://ballotpedia.org/Lori_Trahan",
               "https://www.govtrack.us/congress/votes/117-2022/h360"]),
        claim("lt2", "lori-trahan", "self_defense", 1, False,
              "Voted YES on the Assault Weapons Ban of 2022 (H.R. 1808) and YES on the Bipartisan Safer Communities Act (S. 2938, June 2022), supporting restrictions on commonly-owned semi-automatic rifles and expanded background-check mandates.",
              ["https://ballotpedia.org/Lori_Trahan",
               "https://www.govtrack.us/congress/votes/117-2022/h299"]),
        claim("lt3", "lori-trahan", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 2023), opposing border-wall construction, mandatory deportation, and tightened asylum rules that would secure the southern border.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Lori_Trahan"]),
    ]),

    # ---------------- Jake Auchincloss (MA-D, US Representative) ----------------
    ("jake-auchincloss", "MA", "Representative", [
        claim("ja1", "jake-auchincloss", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act (H.R. 8296, July 2022), which would have federally codified abortion access and preempted state personhood and heartbeat laws.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Jake_Auchincloss"]),
        claim("ja2", "jake-auchincloss", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 2022) and publicly advocates for universal background checks and an assault weapons ban — opposing the rubric's constitutional-carry and anti-restriction standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://auchincloss.house.gov/media/in-the-news/auchincloss-reflects-on-2022-sets-goals-for-2023"]),
        claim("ja3", "jake-auchincloss", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 2023), opposing border-wall resumption and mandatory deportation enforcement prioritized by the rubric.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Jake_Auchincloss"]),
    ]),

    # ---------------- Bill Keating (MA-D, US Representative) ----------------
    ("bill-keating", "MA", "Representative", [
        claim("bk1", "bill-keating", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act (H.R. 3755, Sept. 2021) and pledged to vote for it again, stating women should have access to abortion and contraceptives federally protected — rejecting personhood-from-conception standards.",
              ["https://ballotpedia.org/Bill_Keating",
               "https://newbedfordlight.org/for-congress-u-s-rep-bill-keating-faces-challenger-dan-sullivan-a-working-nurse/"]),
        claim("bk2", "bill-keating", "self_defense", 1, False,
              "Endorsed by Moms Demand Action for gun safety; voted YES on the Bipartisan Safer Communities Act (S. 2938, June 2022), supporting expanded background checks and gun purchase restrictions.",
              ["https://ballotpedia.org/Bill_Keating",
               "https://www.govtrack.us/congress/votes/117-2022/h299"]),
        claim("bk3", "bill-keating", "border_immigration", 0, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 2023), opposing border-wall construction, asylum restrictions, and mandatory-deportation enforcement provisions.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Bill_Keating"]),
    ]),

    # ---------------- Troy Carter (LA-D, US Representative) ----------------
    ("troy-carter", "LA", "Representative", [
        claim("tc1", "troy-carter", "sanctity_of_life", 0, False,
              "Earned a 100/100 score from Reproductive Freedom for All (formerly NARAL) in 2024 and a 0% rating from SBA Pro-Life America; voted YES on the Women's Health Protection Act (H.R. 8296, July 2022), opposing any legal recognition of the unborn.",
              ["https://reproductivefreedomforall.org/lawmaker/troy-a-carter-sr/",
               "https://sbaprolife.org/representative/troy-carter",
               "https://www.govtrack.us/congress/votes/117-2022/h360"]),
        claim("tc2", "troy-carter", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 2022), supporting expanded background-check requirements and restrictions on firearm access for those under 21.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Troy_Carter"]),
        claim("tc3", "troy-carter", "border_immigration", 1, False,
              "Voted NO on H.R. 2 Secure the Border Act of 2023 (May 2023) and publicly spoke against Trump-era immigration enforcement raids, opposing mandatory deportation and border enforcement priorities.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Troy_Carter"]),
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
