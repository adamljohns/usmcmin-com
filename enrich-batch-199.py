#!/usr/bin/env python3
"""Enrichment batch 199: 5 federal candidates from AK + AZ with 0 claims.

Targets evidence_federal House/Senate candidates from the bottom of the
alphabet bucket (AK → AZ), reverse-sorted. archetype_curated federal bucket
exhausted; this batch moves into evidence_federal pool.

Mix: 3D / 2R.
  Mary Peltola (AK-D, former US Rep / 2026 Senate candidate)
  Daniel Keenan (AZ-05-R, 2026 open-seat R candidate)
  Marlene Galán-Woods (AZ-01-D, DCCC Red-to-Blue / EMILY's List)
  Amish Shah (AZ-01-D, former AZ state rep / Giffords-endorsed)
  JoAnna Mendoza (AZ-06-D, USMC Gunnery Sgt / J Street PAC)

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
    # ---- Mary Peltola (AK-D, former US Rep AK-AL; 2026 U.S. Senate candidate) ----
    ("mary-peltola", "AK", "Representative", [
        claim("mp1", "mary-peltola", "sanctity_of_life", 4, False,
              "NARAL Pro-Choice America (now Reproductive Freedom for All) endorsed Peltola for her 2024 reelection, citing her commitment to 'locking protections for reproductive health care into federal law' — placing her inside the abortion-industry endorsement network the rubric identifies as disqualifying.",
              ["https://reproductivefreedomforall.org/news/naral-endorses-ak-rep-peltola-reelection/",
               "https://ballotpedia.org/Mary_Peltola"]),
        claim("mp2", "mary-peltola", "self_defense", 1, True,
              "Earned the NRA's endorsement in her 2024 reelection campaign — making her the only Democrat in Congress to receive an NRA endorsement that cycle — citing her defense of Alaskans' right to own firearms for subsistence hunting and stating 'guns are a part of Alaska's culture and a core tool of a subsistence lifestyle,' opposing sweeping federal gun-control restrictions.",
              ["https://ballotpedia.org/Mary_Peltola",
               "https://en.wikipedia.org/wiki/Mary_Peltola"]),
        claim("mp3", "mary-peltola", "border_immigration", 1, True,
              "During her 2022–2024 House term, Peltola crossed party lines to vote for Republican-backed legislation to deport undocumented migrants who assault police officers, and voted to condemn the Biden administration's handling of the southern border — a harder-than-average Democratic stance on immigration enforcement.",
              ["https://ballotpedia.org/Mary_Peltola",
               "https://www.govtrack.us/congress/members/mary_peltola/456870"]),
    ]),

    # ---- Daniel Keenan (AZ-05, R, 2026 open-seat primary candidate) ----
    ("daniel-keenan", "AZ", "Representative", [
        claim("dk1", "daniel-keenan", "sanctity_of_life", 0, True,
              "Keenan campaigns on an explicitly pro-life platform, opposing taxpayer-funded abortions and upholding strong pro-life policies — aligning with the rubric's core principle of protecting the unborn.",
              ["https://ballotpedia.org/Daniel_Keenan"]),
        claim("dk2", "daniel-keenan", "self_defense", 1, True,
              "Pledges to defend Second Amendment rights 'without compromise,' opposing red-flag laws, assault-weapons bans, and other restrictions on civilian firearms access — matching the rubric's standard of uninfringed Second Amendment rights.",
              ["https://ballotpedia.org/Daniel_Keenan"]),
        claim("dk3", "daniel-keenan", "border_immigration", 4, True,
              "Immigration platform calls for ending birthright citizenship and mandating nationwide E-Verify employment verification — two policies that directly align with the rubric's call to eliminate pull-factors for illegal entry and enforce immigration law at the workplace.",
              ["https://ballotpedia.org/Daniel_Keenan"]),
    ]),

    # ---- Marlene Galán-Woods (AZ-01, D, 2026 primary candidate) ----
    ("marlene-galan-woods", "AZ", "Representative", [
        claim("mgw1", "marlene-galan-woods", "sanctity_of_life", 0, False,
              "Describes herself as a 'lifelong supporter of reproductive freedom' who entered the 2024 race specifically because she was 'alarmed by Arizona Republicans' efforts to roll back reproductive rights' — explicitly rejecting any legal protection of the unborn from conception.",
              ["https://ballotpedia.org/Marlene_Gal%C3%A1n-Woods",
               "https://emilyslist.org/candidate/marlene-galan-woods-2/"]),
        claim("mgw2", "marlene-galan-woods", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List as an 'Majority Maker' and chosen for the DCCC's Red-to-Blue program — placing her inside the flagship abortion-advocacy funding network the rubric identifies as disqualifying; EMILY's List calls her 'a fierce defender of reproductive freedom.'",
              ["https://emilyslist.org/news/emilys-list-endorses-marlene-galan-woods-for-election-to-arizonas-1st-congressional-district-2/",
               "https://ballotpedia.org/Marlene_Gal%C3%A1n-Woods"]),
    ]),

    # ---- Amish Shah (AZ-01, D, 2026 primary candidate / former AZ state rep) ----
    ("amish-shah-az-01", "AZ", "Representative", [
        claim("as1", "amish-shah-az-01", "sanctity_of_life", 0, False,
              "Pledges in Congress to 'fight for abortion rights' and as an Arizona State House member from 2019 to 2024 consistently voted against pro-life restrictions, committing to protect reproductive access at every level of government — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Amish_Shah",
               "https://en.wikipedia.org/wiki/Amish_Shah"]),
        claim("as2", "amish-shah-az-01", "self_defense", 1, False,
              "Endorsed by the Giffords Law Center to Prevent Gun Violence, which commits Shah in Congress to expand background checks to all gun sales, fund community violence intervention programs, and strengthen mandatory safe-storage requirements — directly opposing the rubric's standard of uninfringed Second Amendment rights.",
              ["https://giffords.org/candidates/amish-shah/",
               "https://ballotpedia.org/Amish_Shah"]),
    ]),

    # ---- JoAnna Mendoza (AZ-06, D, 2026 D nominee / USMC Gunnery Sgt) ----
    ("joanna-mendoza", "AZ", "Representative", [
        claim("jm1", "joanna-mendoza", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List — the flagship fundraising vehicle for candidates committed to protecting abortion access — which designates her a reproductive-rights champion in the 2026 AZ-06 race, placing her inside the abortion-industry endorsement network the rubric identifies as disqualifying.",
              ["https://emilyslist.org/candidate/joanna-mendoza/",
               "https://ballotpedia.org/JoAnna_Mendoza"]),
        claim("jm2", "joanna-mendoza", "biblical_marriage", 4, False,
              "Endorsed by LGBT Equality PAC — an organization that explicitly recruits and backs candidates who will advance LGBTQ rights and representation in federal policy — indicating she will promote LGBTQ ideology in public policy, which the rubric opposes.",
              ["https://lgbtequalitypac.org/candidates/joanna-mendoza/",
               "https://ballotpedia.org/JoAnna_Mendoza"]),
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
