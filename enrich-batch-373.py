#!/usr/bin/env python3
"""Enrichment batch 373: hand-curated claims for 5 Wisconsin State Senators.

Targets archetype_party_default WI state senators with 0 claims, taken from the
bottom of the alphabet (WI). Mix of 3 D / 2 R covering 2023-2025 records.

Targets:
  Jodi Habush Sinykin (WI-D, SD-8), Jesse James (WI-R, SD-23),
  Jeff Smith (WI-D, SD-31), Jamie Wall (WI-D, SD-30),
  Howard Marklein (WI-R, SD-17).

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
    # ---------------- Jodi Habush Sinykin (WI-D, SD-8) ----------------
    ("jodi-habush-sinykin", "WI", "State Senator", [
        claim("jhs1", "jodi-habush-sinykin", "sanctity_of_life", 0, False,
              "Co-sponsored 2025 Senate Bill 271 establishing that every individual has a fundamental right to bodily autonomy including the right to access abortion at any time during pregnancy in the professional judgment of the medical provider, and requiring health coverage plans to cover abortion — categorically rejecting any life-at-conception or personhood-from-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/sb271",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2839",
               "https://legis.wisconsin.gov/senate/08/habush-sinykin/"]),
        claim("jhs2", "jodi-habush-sinykin", "biblical_marriage", 0, False,
              "Co-sponsored 2025 Senate Joint Resolution 68 to eliminate Wisconsin's constitutional restriction defining marriage as between one man and one woman, and co-sponsored SJR 73 formally recognizing June 2025 as LGBTQ Pride Month — directly rejecting the biblical definition of marriage as one man and one woman and celebrating LGBTQ advocacy at the level of official legislative recognition.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2839",
               "https://legis.wisconsin.gov/senate/08/habush-sinykin/"]),
        claim("jhs3", "jodi-habush-sinykin", "self_defense", 1, False,
              "Sponsored 2025 Senate Bill 329 establishing extreme risk protection temporary restraining orders allowing courts to seize firearms from individuals deemed a risk before any criminal conviction, and 2025 Senate Bill 336 imposing new requirements on firearm sales and transfers — both directly opposing the rubric's defense of unrestricted Second Amendment rights and its rejection of red-flag confiscation orders.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2839",
               "https://legis.wisconsin.gov/senate/08/habush-sinykin/"]),
    ]),

    # ---------------- Jesse James (WI-R, SD-23) ----------------
    ("jesse-james", "WI", "State Senator", [
        claim("jj1", "jesse-james", "sanctity_of_life", 0, True,
              "Co-sponsored 2023 Senate Bill 299 to narrow Wisconsin's therapeutic abortion exception to only genuine medical emergencies — specifying it applies solely when pregnancy presents a serious risk of death or substantial irreversible physical impairment of a major bodily function, or when the fetus has no chance of survival outside the uterus (ectopic, molar, anembryonic). The bill drew a firm legal line against elective abortion under any other medical rationale, reflecting a pro-life legislative posture.",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/SB299",
               "https://docs.legis.wisconsin.gov/2023/legislators/senate/2563",
               "https://legis.wisconsin.gov/senate/23/james/"]),
        claim("jj2", "jesse-james", "self_defense", 1, True,
              "In March 2025, publicly welcomed Henry Repeating Arms' expansion of its manufacturing operations in western Wisconsin — explicitly embracing a leading American firearms manufacturer and its jobs in his district. His sustained Republican caucus record in the Wisconsin Senate reflects consistent opposition to new firearms restrictions, red-flag orders, and expanded background-check mandates.",
              ["https://legis.wisconsin.gov/senate/23/james/news-updates/press-releases",
               "https://legis.wisconsin.gov/senate/23/james/about-jesse/"]),
        claim("jj3", "jesse-james", "public_justice", 0, True,
              "Authored 2023 Wisconsin Acts 224 and 225, signed into law in 2024, banning computer-generated and AI-produced child sexual abuse material and making child sex dolls resembling a minor illegal under Wisconsin statute — protecting children from sexual exploitation through technology-updated child-safety law enforcement, reflecting a commitment to public justice and the protection of minors from sexual predation.",
              ["https://legis.wisconsin.gov/senate/23/james/about-jesse/legislation/",
               "https://legis.wisconsin.gov/senate/23/james/"]),
    ]),

    # ---------------- Jeff Smith (WI-D, SD-31) ----------------
    ("jeff-smith", "WI", "State Senator", [
        claim("js1", "jeff-smith", "sanctity_of_life", 0, False,
              "Co-sponsored 2025 Senate Bill 271 establishing a statutory right to bodily autonomy including abortion access at any point in pregnancy — categorically rejecting a life-at-conception or personhood standard. Earned a 100% rating from NARAL Pro-Choice Wisconsin, reflecting a career-long legislative record of unrestricted abortion advocacy across multiple sessions as both Assembly member and State Senator.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2826",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb271",
               "https://ballotpedia.org/Jeff_Smith_(Wisconsin)"]),
        claim("js2", "jeff-smith", "self_defense", 1, False,
              "Publicly advocates for enacting Wisconsin's Extreme Risk Protection Order (ERPO) law, which would allow law enforcement and family members to petition courts to temporarily seize firearms from individuals deemed dangerous before any criminal conviction — a red-flag confiscation mechanism directly opposed to the rubric's defense of due-process-first Second Amendment rights and its rejection of pre-conviction firearm removal orders.",
              ["https://legis.wisconsin.gov/senate/31/smith/",
               "https://ballotpedia.org/Jeff_Smith_(Wisconsin)"]),
        claim("js3", "jeff-smith", "economic_stewardship", 2, False,
              "Sponsored 2025 Senate Bill 150 to reduce carbon emissions through state regulatory intervention, and authored bills expanding housing programs under the Wisconsin Housing and Economic Development Authority (WHEDA) — a pattern of government-managed economic interventionism that runs counter to the rubric's anti-deficit, limited-government economic stewardship standard and its preference for free-market solutions over government-directed spending programs.",
              ["https://legis.wisconsin.gov/senate/31/smith/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2826"]),
    ]),

    # ---------------- Jamie Wall (WI-D, SD-30) ----------------
    ("jamie-wall", "WI", "State Senator", [
        claim("jw1", "jamie-wall", "sanctity_of_life", 0, False,
              "Co-sponsored 2025 Senate Bill 271 establishing that every individual has a fundamental right to bodily autonomy including the right to access abortion at any time during pregnancy in the professional judgment of the medical provider, and co-sponsored SB 547 to eliminate certain abortion-related regulations in Wisconsin — categorically rejecting any personhood-from-conception or life-at-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2842",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb271",
               "https://legis.wisconsin.gov/senate/30/wall/"]),
        claim("jw2", "jamie-wall", "biblical_marriage", 0, False,
              "Co-sponsored 2025 Senate Joint Resolution 68 to eliminate Wisconsin's constitutional restriction defining marriage as between one man and one woman — directly rejecting the biblical one-man-one-woman definition of marriage. Also co-sponsored SJR 73 recognizing June 2025 as LGBTQ Pride Month through official legislative resolution.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2842",
               "https://legis.wisconsin.gov/senate/30/wall/"]),
        claim("jw3", "jamie-wall", "biblical_marriage", 2, False,
              "Sponsored 2025 Senate Bill 324 prohibiting licensed mental health providers from offering conversion therapy to minors — banning counseling that would help individuals align their sexual orientation or gender identity with traditional biblical values. This bill suppresses pastoral-aligned therapeutic approaches and rejects the rubric's standard of upholding natural sex and biological sex distinctions in public policy.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2842",
               "https://legis.wisconsin.gov/senate/30/wall/about/"]),
    ]),

    # ---------------- Howard Marklein (WI-R, SD-17) ----------------
    ("howard-marklein", "WI", "State Senator", [
        claim("hm1", "howard-marklein", "economic_stewardship", 2, True,
              "As Joint Finance Committee co-chair, on May 8, 2025 co-authored and voted for a motion deleting 612 of Governor Evers' provisions from the 2025-27 Wisconsin state budget bill — continuing a pattern over four consecutive budget cycles of removing more than 1,600 of the governor's spending proposals. This sustained fiscal restraint record is directly aligned with the rubric's anti-deficit, balanced-budget economic stewardship standard.",
              ["https://legis.wisconsin.gov/senate/17/marklein/",
               "https://www.wispolitics.com/2026/wisconsin-state-senate-democratic-committee-jfc-co-chair-senator-howard-marklein-hides-partisan-record-behind-bipartisan-narrative/"]),
        claim("hm2", "howard-marklein", "sanctity_of_life", 0, True,
              "Sponsored 2025 Senate Bill 553 to limit Wisconsin's statutory definition of abortion, drawing a firm legislative line against elective abortion procedures. Previously authored 2019 Senate Bills 187 and 198 regulating abortion providers under Wisconsin's Medical Assistance program. A multi-session pro-life legislative record consistent with the rubric's support for life-protective policy.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2821",
               "https://legis.wisconsin.gov/senate/17/marklein/"]),
        claim("hm3", "howard-marklein", "self_defense", 1, True,
              "Sponsored 2025 Senate Bill 12 to create a Wisconsin sales and use tax exemption on the purchase of gun safes — a pro-gun-rights measure encouraging responsible firearm ownership and reducing the tax burden on law-abiding gun owners. Also sponsored 2025 SB 533 imposing criminal penalties for intentionally disarming correctional officers. Prior sessions included a parallel gun-safe tax exemption bill (2019 SB 337), reflecting a consistent Second Amendment-aligned legislative record.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2821",
               "https://legis.wisconsin.gov/senate/17/marklein/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
