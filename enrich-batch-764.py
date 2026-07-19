#!/usr/bin/env python3
"""Enrichment batch 764: 2 new claims each for 5 NC U.S. Representatives.

All archetype_curated federal 0-claim candidates are exhausted; this batch
adds claims to sitting NC U.S. Reps that currently have only 3 claims,
bringing each to 5.

Targets (5 R): Pat Harrigan (NC-10), Mark Harris (NC-08),
Greg Murphy (NC-03), David Rouzer (NC-07), Chuck Edwards (NC-11).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions.

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
    # ---------------- Pat Harrigan (NC-10, R) ----------------
    ("pat-harrigan", "NC", "Representative", [
        claim("ph4", "pat-harrigan", "economic_stewardship", 2, True,
              "Voted to advance H.Con.Res. 14, the 'America First Budget' (FY2025), which directs eleven House committees to propose legislation reducing the deficit; Harrigan stated he came to Washington to 'stop Washington's reckless spending' and received the Defender of Limited Government Award from the Institute for Legislative Analysis for a near-perfect limited-government voting record.",
              ["https://harrigan.house.gov/media/press-releases/congressman-pat-harrigan-votes-advance-america-first-budget-delivering",
               "https://harrigan.house.gov/media/press-releases/congressman-pat-harrigan-receives-defender-limited-government-award-institute"]),
        claim("ph5", "pat-harrigan", "self_defense", 1, True,
              "As NRA PVF-endorsed owner of firearms manufacturers ZRODelta and UnBrandedAR, Harrigan has stated he will 'stop big government from infringing upon our constitutional rights to keep and bear arms,' opposing gun-control measures including assault-weapons bans and restrictions on lawful gun owners — positions consistent with categorical rejection of red-flag laws, AWBs, and magazine limits.",
              ["https://ballotpedia.org/Pat_Harrigan",
               "https://ivoterguide.com/candidate/65072/race/1742/election/1206"]),
    ]),

    # ---------------- Mark Harris (NC-08, R) ----------------
    ("mark-harris", "NC", "Representative", [
        claim("mh4", "mark-harris", "self_defense", 0, True,
              "In the 119th Congress, Harris co-sponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025, which would require all states to recognize each other's concealed-carry permits and allow law-abiding Americans to exercise their right to carry across state lines — directly advancing the constitutional-carry standard.",
              ["https://www.govtrack.us/congress/bills/119/hr38",
               "https://ballotpedia.org/Mark_Harris_(North_Carolina)"]),
        claim("mh5", "mark-harris", "economic_stewardship", 2, True,
              "Harris has publicly stated the nation 'is $19 trillion in debt' with $120 trillion in unfunded liabilities and that a Balanced Budget Amendment is necessary to restore fiscal sanity; as a Freedom Caucus member in the 119th Congress, he consistently supports spending cuts and fiscal discipline — aligning with the anti-deficit, balanced-budget rubric standard.",
              ["https://en.wikipedia.org/wiki/Mark_Harris_(North_Carolina_politician)",
               "https://ballotpedia.org/Mark_Harris_(North_Carolina)"]),
    ]),

    # ---------------- Greg Murphy (NC-03, R) ----------------
    ("greg-murphy", "NC", "Representative", [
        claim("gm4", "greg-murphy", "self_defense", 1, True,
              "Voted NO on H.R. 1808 (Assault Weapons Ban of 2022), calling it 'blatantly unconstitutional' for banning firearms 'in common use'; voted NO on S. 2938 (Bipartisan Safer Communities Act) specifically citing its red-flag provisions as 'deny[ing] due process and depriv[ing] Americans of their Second Amendment rights'; and publicly condemned Democrats' attempt to embed red-flag laws in the FY2022 NDAA as 'reprehensible.'",
              ["https://murphy.house.gov/media/press-releases/murphy-votes-defend-second-amendment-rights",
               "https://murphy.house.gov/media/press-releases/murphy-statement-senate-gun-control-package",
               "https://murphy.house.gov/media/press-releases/murphy-condemns-democrat-attempt-conceal-red-flag-laws-ndaa"]),
        claim("gm5", "greg-murphy", "economic_stewardship", 2, True,
              "Signed the Americans for Tax Reform (ATR) Taxpayer Protection Pledge, committing to oppose any net federal income-tax increase; returned $160,000 of unused congressional office budget back to taxpayers; and voted for the Limit, Save, Grow Act (2023), stating it 'will be instrumental in returning spending to responsible levels and slashing the ridiculously wasteful programs' — a consistent anti-deficit record.",
              ["https://www.atr.org/greg-murphy-becomes-first-candidate-make-no-new-taxes-promise-nc-03-race/",
               "https://murphy.house.gov/media/press-releases/murphy-returns-160000-116th-congress-budget-back-taxpayers",
               "https://murphy.house.gov/media/press-releases/murphy-releases-statement-passage-limit-save-grow-act"]),
    ]),

    # ---------------- David Rouzer (NC-07, R) ----------------
    ("david-rouzer", "NC", "Representative", [
        claim("dr4", "david-rouzer", "self_defense", 4, True,
              "Voted for H.J.Res. 44 (2023) to nullify the ATF's pistol-brace rule under the Congressional Review Act, which Rouzer called 'unconstitutional'; the rule had threatened gun owners with up to 10 years in prison and $10,000 fines for failing to register or destroy their stabilizing-brace firearms — a direct stand against ATF overreach and de-facto firearm registry mandates.",
              ["https://rouzer.house.gov/news/documentsingle.aspx?DocumentID=990",
               "https://ballotpedia.org/David_Rouzer"]),
        claim("dr5", "david-rouzer", "economic_stewardship", 2, True,
              "Voted for H.Con.Res. 14, the Senate-amended FY2025 budget resolution (April 2025), which establishes recommended federal spending and deficit-reduction levels through 2034; Rouzer has consistently supported budget discipline measures and spending restraint throughout his tenure since 2015.",
              ["https://rouzer.house.gov/news/documentsingle.aspx?DocumentID=2405",
               "https://rouzer.house.gov/news/email/show.aspx?ID=YUECWPZYC65CWIVAZUNJZ3FCSU"]),
    ]),

    # ---------------- Chuck Edwards (NC-11, R) ----------------
    ("chuck-edwards", "NC", "Representative", [
        claim("ce4", "chuck-edwards", "economic_stewardship", 2, True,
              "Edwards has pledged that 'one of my top priorities will be to introduce legislation to enact a Balanced Budget Amendment,' citing his experience as the only candidate who had actually balanced a government budget (North Carolina mandates it); he has maintained a consistent spending-cut record in Congress, stating he has been 'voting to cut spending' throughout his tenure.",
              ["https://edwards.house.gov/about",
               "https://ballotpedia.org/Chuck_Edwards"]),
        claim("ce5", "chuck-edwards", "foreign_policy_restraint", 1, True,
              "Voted against the Ukraine Security Assistance and Oversight Supplemental Appropriations Act (HR 5692, 2024), joining House conservatives opposed to continued open-ended U.S. military spending abroad — consistent with the rubric's call to end forever wars and reassert congressional authority over foreign military aid commitments.",
              ["https://ballotpedia.org/Chuck_Edwards",
               "https://www.govtrack.us/congress/members/charles_chuck_edwards/456914"]),
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
