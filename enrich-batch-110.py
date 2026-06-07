#!/usr/bin/env python3
"""Enrichment batch 110: hand-curated claims for 5 bottom-of-alphabet candidates.

Targets archetype_curated candidates with 0 evidence claims taken from the
reverse-alphabetical tail of the bucket:
  Kay Ivey (AL-R, Governor), Lew Burdette (AL-R, Gov candidate),
  Bert Reeves (GA-R, LtGov candidate), Marc Morial (GA-D, Gov candidate),
  Bill Walker (AK-I, Gov candidate 2026).

Each claim cites >=1 reliable source and reflects 2018-2026 legislative record
or publicly documented positions.

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
    # ---------------- Kay Ivey (AL-R, Governor) ----------------
    ("kay-ivey", "AL", "Governor", [
        claim("ki1", "kay-ivey", "sanctity_of_life", 0, True,
              "Signed the Human Life Protection Act (HB 314) on May 15, 2019 — Alabama's near-total abortion ban that criminalizes performing an abortion at any stage of pregnancy (Class A felony for physicians), with no rape or incest exceptions, directly affirming legal protection of unborn life from conception.",
              ["https://governor.alabama.gov/newsroom/2019/05/governor-ivey-issues-statement-after-signing-the-alabama-human-life-protection-act/",
               "https://en.wikipedia.org/wiki/Human_Life_Protection_Act"]),
        claim("ki2", "kay-ivey", "self_defense", 0, True,
              "Signed constitutional carry into law (HB 272, March 10, 2022), eliminating Alabama's requirement for law-abiding citizens to obtain a permit to carry a concealed pistol, making Alabama the 22nd constitutional carry state. Declared: 'Alabama is reaffirming our commitment to defending our Second Amendment rights.'",
              ["https://governor.alabama.gov/newsroom/2022/03/governor-ivey-defends-alabamians-second-amendment-rights-signs-constitutional-carry-bill-into-law/",
               "https://en.wikipedia.org/wiki/Kay_Ivey"]),
        claim("ki3", "kay-ivey", "election_integrity", 0, True,
              "Signed 2021 legislation (HB 167) making it a crime to vote in the same election in both Alabama and another state — a concrete voter-fraud deterrent aligned with the rubric's demand for clean, accountable elections.",
              ["https://en.wikipedia.org/wiki/Kay_Ivey"]),
    ]),

    # ---------------- Lew Burdette (AL-R, Gov candidate) ----------------
    ("lew-burdette-gov", "AL", "Governor", [
        claim("lb1", "lew-burdette-gov", "sanctity_of_life", 0, True,
              "Affirms that life begins at conception and that all human life is sacred, pledging to 'stand firm' on pro-life positions without wavering, citing his deeply held Christian faith as the foundation of his commitment to protecting the unborn.",
              ["https://ivoterguide.com/candidate/60587/race/13254/election/867",
               "https://birminghamwatch.org/lew-burdette-governor-republican/"]),
        claim("lb2", "lew-burdette-gov", "sanctity_of_life", 4, True,
              "Explicitly opposes any federal, state, or local government funding for abortion providers including Planned Parenthood, calling for full defunding of organizations that perform abortions.",
              ["https://birminghamwatch.org/lew-burdette-governor-republican/",
               "https://www.wsfa.com/2022/05/12/alabamas-us-gubernatorial-candidate-profiles-lew-burdette/"]),
        claim("lb3", "lew-burdette-gov", "self_defense", 0, True,
              "Identifies as a strong supporter of the Second Amendment and gun rights throughout his gubernatorial campaigns, opposing new restrictions on law-abiding firearms owners.",
              ["https://birminghamwatch.org/lew-burdette-governor-republican/"]),
    ]),

    # ---------------- Bert Reeves (GA-R, LtGov candidate) ----------------
    ("bert-reeves-ltgov", "GA", "Lieutenant Governor", [
        claim("br1", "bert-reeves-ltgov", "family_child_sovereignty", 0, True,
              "As a Georgia state representative, sponsored HB 159, a comprehensive 100-page adoption code reform — the first major rewrite of Georgia adoption law since 1990 — that strengthened parental rights in surrender processes and updated interstate and foreign adoption recognition. Passed the House 168-0 and Senate 53-2; signed by Governor Deal in March 2018.",
              ["https://www.wsav.com/news/gov-deal-signs-hb-159-adoption-bill/",
               "https://www.albanyherald.com/news/local/georgia-updates-adoption-code-with-signing-of-hb/article_11fb20a4-cda6-5538-88c8-2d9697261c84.html"]),
        claim("br2", "bert-reeves-ltgov", "family_child_sovereignty", 2, True,
              "Championed HB 912 to reduce DFCS bureaucratic barriers for foster families, allowing foster parents to take brief out-of-town trips without first putting childcare providers through the full DFCS approval process — a direct rollback of state overreach into foster family daily life.",
              ["https://trackbill.com/legislator/georgia-representative-bert-reeves/610-13497/",
               "https://www.georgiapol.com/2017/04/03/rep-bert-reeves-pulls-no-punches-senates-failure-pass-adoption-bill/"]),
    ]),

    # ---------------- Marc Morial (GA-D, Gov candidate) ----------------
    ("marc-morial-gov", "GA", "Governor", [
        claim("mm1", "marc-morial-gov", "sanctity_of_life", 0, False,
              "Characterized the Supreme Court's Dobbs ruling as 'the first time the Supreme Court has taken away people's rights,' framing abortion access as a woman's individual constitutional right over her own body — rejecting any life-at-conception standard or legal protection for the unborn.",
              ["https://www.washingtoninformer.com/national-urban-leagues-ceo-marc-morial-tackles-tough-issues/",
               "https://nul.org/marc-h-morial"]),
        claim("mm2", "marc-morial-gov", "election_integrity", 0, False,
              "As National Urban League president, led successful advocacy for reauthorization of the Voting Rights Act and testified before the House Judiciary Committee to expand federal oversight of state election procedures — opposing the state-level voter-ID, ballot-security, and anti-mass-mail-in reforms the rubric requires.",
              ["https://nul.org/marc-h-morial",
               "https://veritenews.org/2024/07/19/marc-morial-national-urban-league-conference-2024-election/"]),
        claim("mm3", "marc-morial-gov", "refuse_federal_overreach", 0, False,
              "Called for repeal of the One Big Beautiful Bill Act in June 2025, opposing federal spending reductions on social programs — a posture that favors a large federal government role in welfare and healthcare rather than limiting federal overreach into states and families.",
              ["https://www.kut.org/life-arts/2025-06-10/the-national-urban-league-with-president-and-ceo-marc-h-morial"]),
    ]),

    # ---------------- Bill Walker (AK-I, Gov candidate 2026) ----------------
    ("bill-walker-gov-2026", "AK", "Governor", [
        claim("bw1", "bill-walker-gov-2026", "sanctity_of_life", 0, False,
              "Co-authored a July 2022 op-ed pledging to 'rebuild Alaska, not take away reproductive rights,' committing to protect abortion access under Alaska's constitutional privacy clause and to veto any legislation restricting a woman's right to an abortion — a direct rejection of the life-at-conception standard.",
              ["https://www.adn.com/opinions/2022/07/12/opinion-we-will-uphold-womens-constitutional-reproductive-rights/",
               "https://alaskabeacon.com/2022/05/11/after-u-s-supreme-court-opinion-leaks-alaska-governor-candidates-share-their-thoughts/"]),
        claim("bw2", "bill-walker-gov-2026", "economic_stewardship", 2, False,
              "As Alaska governor (2015-2018), proposed a new Alaska state income tax to address the state budget deficit — introducing a new tax burden on residents and businesses rather than cutting spending, contrary to the rubric's anti-deficit, no-new-taxes posture.",
              ["https://en.wikipedia.org/wiki/Bill_Walker_(American_politician)",
               "https://alaskapublic.org/2022/08/10/candidate-qa-governor-bill-walker/"]),
        claim("bw3", "bill-walker-gov-2026", "refuse_federal_overreach", 0, False,
              "Signed Alaska's Medicaid expansion under the Affordable Care Act as governor in 2015, extending a major federal healthcare program into the state rather than exercising the option to opt out and limit federal overreach.",
              ["https://en.wikipedia.org/wiki/Bill_Walker_(American_politician)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
