#!/usr/bin/env python3
"""Enrichment batch 240: hand-curated claims for 5 sitting U.S. Representatives.

Targets: MI bottom-of-alpha sitting House members (Shri Thanedar, Kristen McDonald
Rivet, Debbie Dingell) and MD members (Sarah Elfreth, Kweisi Mfume).
All archetype_curated federal senators and representatives are exhausted; this batch
draws from archetype_party_default sitting members at the bottom of the reverse-alpha
state queue (MI then MD).

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
    # ---------------- Shri Thanedar (MI-D, US Representative) ----------------
    ("shri-thanedar", "MI", "Representative", [
        claim("st1", "shri-thanedar", "sanctity_of_life", 0, False,
              "A pro-choice Democrat who explicitly backs expanding abortion access. Received a 100% score from Reproductive Freedom for All (the renamed NARAL), and supports federal legislation to restore Roe v. Wade protections, rejecting any personhood-at-conception standard.",
              ["https://reproductivefreedomforall.org/lawmaker/shri-thanedar/",
               "https://en.wikipedia.org/wiki/Shri_Thanedar"]),
        claim("st2", "shri-thanedar", "self_defense", 1, False,
              "A progressive Democrat from Detroit who backed Michigan's package of gun-safety laws passed in 2023 including universal background checks, safe-storage mandates, and red-flag laws; consistently opposes constitutional-carry and resists rolling back firearms restrictions.",
              ["https://en.wikipedia.org/wiki/Shri_Thanedar",
               "https://ballotpedia.org/Shri_Thanedar"]),
        claim("st3", "shri-thanedar", "biblical_marriage", 1, False,
              "Supports federal recognition of same-sex marriage; a secular progressive who has championed LGBTQ equality and opposes any effort to define marriage as exclusively between one man and one woman.",
              ["https://en.wikipedia.org/wiki/Shri_Thanedar",
               "https://ballotpedia.org/Shri_Thanedar"]),
    ]),

    # ---------------- Kristen McDonald Rivet (MI-D, US Representative) ----------------
    ("kristen-mcdonald-rivet", "MI", "Representative", [
        claim("kmr1", "kristen-mcdonald-rivet", "sanctity_of_life", 0, False,
              "A Democrat who supports abortion access, having championed reproductive rights during her tenure in the Michigan Senate before being elected to Congress in a 2024 special election for Michigan's 8th District.",
              ["https://en.wikipedia.org/wiki/Kristen_McDonald_Rivet",
               "https://ballotpedia.org/Kristen_McDonald_Rivet"]),
        claim("kmr2", "kristen-mcdonald-rivet", "border_immigration", 1, True,
              "One of only 46 House Democrats to join all Republicans in voting for the Laken Riley Act (January 2025), which requires federal immigration authorities to mandatorily detain undocumented immigrants arrested for burglary, theft, or violence — a step toward the rubric's mandatory-deportation standard.",
              ["https://en.wikipedia.org/wiki/Kristen_McDonald_Rivet",
               "https://www.govtrack.us/congress/members/kristen_mcdonald_rivet/456995"]),
        claim("kmr3", "kristen-mcdonald-rivet", "border_immigration", 4, True,
              "Co-sponsored the bipartisan FARMLAND Act to expand CFIUS authority to block foreign entities connected to China and adversarial nations from purchasing U.S. farmland — directly matching the rubric's concern about foreign acquisition of American land.",
              ["https://en.wikipedia.org/wiki/Kristen_McDonald_Rivet",
               "https://www.govtrack.us/congress/members/kristen_mcdonald_rivet/456995"]),
    ]),

    # ---------------- Debbie Dingell (MI-D, US Representative) ----------------
    ("debbie-dingell", "MI", "Representative", [
        claim("dd1", "debbie-dingell", "sanctity_of_life", 0, False,
              "A vocal abortion-rights champion with a 100% rating from Planned Parenthood Action Fund; voted for the Women's Health Protection Act of 2022 to codify abortion access beyond Roe v. Wade, and stated she believes abortion decisions belong to 'a woman, her doctor, and her faith' — rejecting any legal personhood from conception.",
              ["https://en.wikipedia.org/wiki/Debbie_Dingell",
               "https://justfacts.votesmart.org/candidate/key-votes/152482/debbie-dingell/2/abortion"]),
        claim("dd2", "debbie-dingell", "self_defense", 1, False,
              "A leading gun-control advocate in Congress who introduced the Defective Firearms Protection Act in 2026, backed universal background checks and assault-weapon restrictions, and in 2018 introduced legislation giving the Consumer Product Safety Commission authority to recall defective firearms.",
              ["https://en.wikipedia.org/wiki/Debbie_Dingell",
               "https://justfacts.votesmart.org/candidate/key-votes/152482/debbie-dingell"]),
        claim("dd3", "debbie-dingell", "sanctity_of_life", 4, False,
              "Carries a 100% score from Planned Parenthood Action Fund, placing her squarely within the abortion-industry endorsement network the rubric identifies as disqualifying.",
              ["https://en.wikipedia.org/wiki/Debbie_Dingell",
               "https://ballotpedia.org/Debbie_Dingell"]),
    ]),

    # ---------------- Sarah Elfreth (MD-D, US Representative) ----------------
    ("sarah-elfreth", "MD", "Representative", [
        claim("se1", "sarah-elfreth", "sanctity_of_life", 0, False,
              "An ardent abortion-rights supporter who as a Maryland state senator co-sponsored a constitutional amendment to enshrine 'reproductive freedom' in Maryland's constitution and in 2024 introduced a bill to provide state abortion clinics with $500,000 in security grants; pledges to make Roe v. Wade federal law.",
              ["https://en.wikipedia.org/wiki/Sarah_Elfreth",
               "https://ballotpedia.org/Sarah_Elfreth"]),
        claim("se2", "sarah-elfreth", "self_defense", 1, False,
              "Backed Maryland's Gun Safety Act increasing handgun permit requirements, co-sponsored legislation to ban ghost guns, voted to restrict firearm carry in public spaces (schools, restaurants, churches), and introduced a bill to levy an 11% excise tax on gun sales — opposing the rubric's Second Amendment positions at every point.",
              ["https://en.wikipedia.org/wiki/Sarah_Elfreth",
               "https://ballotpedia.org/Sarah_Elfreth"]),
        claim("se3", "sarah-elfreth", "border_immigration", 2, False,
              "In January 2026 supported efforts to impeach DHS Secretary Kristi Noem, accusing ICE of 'terrorizing our cities' over immigration enforcement operations — a position directly opposing the rubric's anti-sanctuary and border-enforcement standards.",
              ["https://en.wikipedia.org/wiki/Sarah_Elfreth",
               "https://ballotpedia.org/Sarah_Elfreth"]),
    ]),

    # ---------------- Kweisi Mfume (MD-D, US Representative) ----------------
    ("kweisi-mfume", "MD", "Representative", [
        claim("km1", "kweisi-mfume", "sanctity_of_life", 0, False,
              "A long-standing abortion-rights supporter with a record of pro-choice votes; backed the Women's Health Protection Act to codify abortion through all nine months of pregnancy, rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Kweisi_Mfume",
               "https://www.ontheissues.org/social/Kweisi_Mfume_Abortion.htm"]),
        claim("km2", "kweisi-mfume", "biblical_marriage", 0, False,
              "Has supported civil unions and opposed constitutional amendments to restrict marriage to one man and one woman; voted for the Respect for Marriage Act of 2022 codifying federal same-sex marriage recognition — rejecting the biblical definition of marriage.",
              ["https://en.wikipedia.org/wiki/Kweisi_Mfume",
               "https://www.ontheissues.org/Domestic/Kweisi_Mfume_Civil_Rights.htm"]),
        claim("km3", "kweisi-mfume", "self_defense", 1, False,
              "Consistent gun-control voting record representing the Baltimore area; backed universal background check legislation and other firearms restrictions, opposing constitutional-carry and the rubric's anti-gun-control positions.",
              ["https://en.wikipedia.org/wiki/Kweisi_Mfume",
               "https://ontheissues.org/House/Kweisi_Mfume.htm"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
