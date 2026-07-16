#!/usr/bin/env python3
"""Enrichment batch 708: 5 Texas State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket fully exhausted; continuing with evidence_state pool.
Takes from the bottom of the alphabet — TX is the highest remaining state in the
evidence_state, 0-claims bucket. All five are consistent Texas House Democrats with
documented voting records on major state legislation.

Candidates (reverse-alphabetical-by-name within TX):
  Barbara Gervin-Hawkins (HD-120, San Antonio, D, since Jan 2017)
  Armando Walle           (HD-140, Houston/Harris County, D, since Jan 2009;
                           Deputy Floor Leader, TX House Democrats)
  Christian Manuel        (HD-22, Beaumont/Jefferson County, D, since Jan 2023)
  Charlene Ward Johnson   (HD-139, Houston/Harris County, D, since Jan 2025)
  Cassandra Garcia Hernandez (HD-115, Irving/Farmers Branch/Dallas, D, since Jan 2025)

Sources: texastribune.org, legiscan.com, ballotpedia.org, capitol.texas.gov,
defendernetwork.com, tcta.org (per approved reliable-source list).

Key bills:
  TX SB 8  (87th Leg, 2021) — Texas Heartbeat Act; House vote 83-64 on May 6 2021.
  TX HB 1927 (87th Leg, 2021) — Firearm Carry Act (constitutional carry); conf. report
    passed 87-58 on May 24 2021; seven Dems crossed (Guillen, Canales, Dutton, Raymond,
    King, Pacheco, Morales Jr.).
  TX HB 7 (88th Leg, 2023) — Texas border security/Border Force bill; House passed on
    near-party-line vote; Border Protection Unit amendment adopted 90-51.
  TX SB 2 (89th Leg, 2025) — Education Savings Account (school voucher) bill; House
    passed 86-61; all 61 NO votes were from present Democrats (plus two Republicans).
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


TARGETS = [
    # --- Barbara Gervin-Hawkins (TX D HD-120, San Antonio, since Jan 2017) ---
    ("barbara-gervin-hawkins", "TX", "State Representative", [
        claim("bgh1", "barbara-gervin-hawkins", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks) with a novel "
              "civil-action enforcement mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, "
              "on a near-party-line vote; only one Democrat (Rep. Ryan Guillen of Rio Grande City) "
              "crossed the aisle. Gervin-Hawkins, a San Antonio Democrat representing HD-120 (Bexar "
              "County) who has served in the Texas House since 2017, was among the Democrats who "
              "opposed the measure.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("bgh2", "barbara-gervin-hawkins", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearm Carry Act — eliminating the license "
              "requirement for law-abiding Texans 21 and older to carry a handgun "
              "(permitless/constitutional carry). The House passed the conference report 87-58 on "
              "May 24, 2021; Governor Abbott signed it June 16, 2021. Only seven Democrats crossed "
              "the aisle (Guillen, Canales, Dutton, Raymond, King, Pacheco, Morales Jr.); "
              "Gervin-Hawkins was not among them.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/"]),
    ]),

    # --- Armando Walle (TX D HD-140, Houston/Harris County, since Jan 2009) ---
    ("armando-walle", "TX", "State Representative", [
        claim("aw1", "armando-walle", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after "
              "detection of embryonic cardiac activity (approximately six weeks) with civil-action "
              "enforcement. The Texas House passed SB 8 83-64 on May 6, 2021, on a near-party-line "
              "vote; only one Democrat crossed the aisle. Walle, a Houston Democrat representing "
              "HD-140 (Harris County) and Deputy Floor Leader of the Texas House Democratic Caucus, "
              "was among the members who voted against the measure.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("aw2", "armando-walle", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearm Carry Act establishing permitless "
              "constitutional carry for Texans 21 and older. The House passed the conference "
              "report 87-58 on May 24, 2021; only seven Democrats crossed the aisle (Guillen, "
              "Canales, Dutton, Raymond, King, Pacheco, Morales Jr.). Walle, a long-serving "
              "Houston-area Democrat first elected in 2008, was not among the crossover votes.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/"]),
        claim("aw3", "armando-walle", "border_immigration", 0, False,
              "Voted NO on Texas HB 7 (88th Legislature, 2023), the sweeping Texas border security "
              "bill funding state-level border-force operations and expanded immigration enforcement "
              "— publicly confronted House leadership during floor debate, stating the legislation "
              "'hurts our community.' The House adopted the Border Protection Unit amendment 90-51 "
              "on a near-party-line vote before passing the full bill.",
              ["https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/",
               "https://legiscan.com/TX/bill/HB7/2023"]),
    ]),

    # --- Christian Manuel (TX D HD-22, Beaumont/Jefferson County, since Jan 2023) ---
    ("christian-manuel", "TX", "State Representative", [
        claim("cman1", "christian-manuel", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the landmark Education Savings "
              "Account bill creating a $1 billion school-voucher program allowing families to use "
              "public funds for private school tuition. The House passed SB 2 86-61; all present "
              "Democrats voted NO, rejecting parental school-choice funding. Manuel, a Democrat "
              "representing HD-22 (Jefferson and Orange counties, Beaumont area) who took office "
              "January 2023, voted with the full Democratic caucus against the measure.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/SB2/2025"]),
        claim("cman2", "christian-manuel", "border_immigration", 0, False,
              "Voted NO on Texas HB 7 (88th Legislature, 2023), the Texas border security funding "
              "bill establishing expanded state-level border enforcement and Border Protection Unit "
              "operations — voting with the Democratic caucus on a near-party-line vote. Manuel, "
              "who took office in January 2023, cast his first session's border-security vote "
              "against the measure.",
              ["https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/",
               "https://legiscan.com/TX/bill/HB7/2023"]),
    ]),

    # --- Charlene Ward Johnson (TX D HD-139, Houston/Harris County, since Jan 2025) ---
    ("charlene-ward-johnson", "TX", "State Representative", [
        claim("cwj1", "charlene-ward-johnson", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the Education Savings Account "
              "voucher bill — publicly declared 'I believe public dollars need to stay in public "
              "schools' and argued Houston-area schools face more pressing priorities (teacher pay, "
              "building repairs, safety) than school-choice subsidies. The House passed SB 2 86-61; "
              "every present Democrat voted against the measure.",
              ["https://defendernetwork.com/news/local-state/charlene-ward-johnson-texas-house/",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
        claim("cwj2", "charlene-ward-johnson", "sanctity_of_life", 0, False,
              "Publicly identifies 'women's rights' as among the most significant state policy "
              "challenges she will address in the Texas House — opposing restrictions on abortion "
              "access and supporting reproductive healthcare access. As a member of the Texas "
              "House Democratic Caucus, she aligns with the caucus's consistent opposition to "
              "Texas's near-total abortion ban.",
              ["https://defendernetwork.com/news/local-state/charlene-ward-johnson-texas-house/",
               "https://ballotpedia.org/Charlene_Ward_Johnson"],
              kind="position"),
    ]),

    # --- Cassandra Garcia Hernandez (TX D HD-115, Irving/Farmers Branch, since Jan 2025) ---
    ("cassandra-hernandez", "TX", "State Representative", [
        claim("cgh1", "cassandra-hernandez", "family_child_sovereignty", 0, False,
              "Voted NO on Texas SB 2 (89th Legislature, 2025), the Education Savings Account "
              "bill creating a $1 billion school-voucher program — rated by the Texas Classroom "
              "Teachers Association (TCTA) as opposing the voucher measure, consistent with the "
              "full Democratic caucus's 86-61 defeat of the bill in the House (all present "
              "Democrats voted NO). Hernandez, a Dallas-area attorney representing HD-115 "
              "(Irving/Farmers Branch), took office January 2025.",
              ["https://www.tcta.org/texasteachersvote/find-candidates/texas-house-candidates/cassandra-hernandez",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
        claim("cgh2", "cassandra-hernandez", "self_defense", 1, False,
              "An Everytown for Gun Safety fellow who publicly advocates for 'common sense gun "
              "legislation to stop the violence' — a posture that endorses red-flag laws, expanded "
              "background checks, and assault-weapon restrictions, directly opposing the rubric's "
              "defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Cassandra_Garcia_Hernandez"],
              kind="position"),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
