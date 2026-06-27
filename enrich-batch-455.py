#!/usr/bin/env python3
"""Enrichment batch 455: 5 Texas state representatives — evidence_state → evidence_curated.

Bottom-of-alphabet targets (evidence_state confidence, 0 claims, reverse-sorted from TX):
  - Terry Wilson  (TX-R, HD-20) — authored Border Protection Unit HB 20 (2023); 94% TVA
  - Stan Gerdes   (TX-R, HD-17) — 93% TVA Faith & Family Champion 2025; gun-carry legislation
  - Shelley Luther(TX-R, HD-62) — defied COVID salon closures 2020; voted for school vouchers 2025
  - Stan Kitzman  (TX-R, HD-85) — border security champion; NRA affiliate; Freedom Index scorecard
  - Todd Ames Hunter (TX-R, HD-32) — Calendars Chair who scheduled constitutional carry HB 1927 (2021)

All federal buckets (archetype_curated senators and reps with 0 claims) are exhausted as of this
batch; pipeline now works through evidence_state Republican state legislators from the bottom of
the alphabet.
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
    # ---------- Terry Wilson (TX-R, HD-20) ----------
    ("terry-wilson", "TX", "State Representative", [
        claim("tw1", "terry-wilson", "border_immigration", 0, True,
              "Authored HB 20 (88th Legislature, 2023) creating the Border Protection Unit within the "
              "Governor's Office — state officers empowered to 'arrest, apprehend, or detain persons "
              "crossing the Texas-Mexico border unlawfully.' The bill's core language was absorbed into "
              "HB 7, which passed the House and committed nearly $100 million to border enforcement, "
              "detention centers, and border-area courts.",
              ["https://www.texastribune.org/2023/04/13/texas-house-border-protection-unit/",
               "https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/",
               "https://ballotpedia.org/Terry_Wilson_(Texas)"]),
        claim("tw2", "terry-wilson", "family_child_sovereignty", 0, True,
              "Earned a 94% 'Faith & Family Champion' rating from Texas Values Action for his 2023 "
              "session votes, spanning parental rights, education content, family protection, and "
              "religious-liberty legislation. Has publicly pushed back against critical race theory "
              "and DEI programming in public schools, calling for parents to have a direct say in "
              "K-12 curriculum content.",
              ["https://txvaluesaction.org/legislator/terry-wilson/",
               "https://ballotpedia.org/Terry_Wilson_(Texas)"]),
        claim("tw3", "terry-wilson", "self_defense", 1, True,
              "A National Rifle Association affiliate and 32-year Army veteran (1983-2015) who served "
              "as Chairman of the Defense & Veterans' Affairs Committee (2023-2024); has consistently "
              "backed Texas's Second Amendment legislative agenda, opposing new firearms restrictions "
              "on law-abiding gun owners.",
              ["https://ballotpedia.org/Terry_Wilson_(Texas)",
               "https://txvaluesaction.org/legislator/terry-wilson/"]),
    ]),

    # ---------- Stan Gerdes (TX-R, HD-17) ----------
    ("stan-gerdes", "TX", "State Representative", [
        claim("sg1", "stan-gerdes", "family_child_sovereignty", 0, True,
              "Earned a 93% 'Faith & Family Champion' rating from Texas Values Action for his 2025 "
              "session votes — among the highest scores in the 89th Legislature — covering parental "
              "rights, education content, religious liberty, and family-protection measures.",
              ["https://txvaluesaction.org/legislator/stan-gerdes/",
               "https://ballotpedia.org/Stan_Gerdes"]),
        claim("sg2", "stan-gerdes", "self_defense", 1, True,
              "Authored legislation (88th Legislature, 2023) refining where Texas handgun license "
              "holders may lawfully carry; has supported the constitutional carry framework and "
              "broader Second Amendment freedoms consistent with his conservative Fayette-County "
              "(Smithville) district.",
              ["https://ballotpedia.org/Stan_Gerdes",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A4195"]),
    ]),

    # ---------- Shelley Luther (TX-R, HD-62) ----------
    ("shelley-luther", "TX", "State Representative", [
        claim("sl1", "shelley-luther", "industry_capture", 0, True,
              "Nationally recognized for openly defying Texas pandemic-closure orders in May 2020: "
              "kept her Dallas hair salon open despite government mandates, was cited for contempt, "
              "and was sentenced to seven days in jail before the Texas Supreme Court voided the "
              "jailing order in April 2021. Her public stand — challenging COVID restrictions as "
              "a violation of small-business and individual liberty — became a national symbol "
              "of resistance to government-mandated lockdowns and health-authority overreach.",
              ["https://www.texastribune.org/2020/05/05/dallas-salon-owner-jail-sentence-reopening-shelley-luther-coronavirus/",
               "https://www.texastribune.org/2021/04/09/shelley-luther-supreme-court/",
               "https://en.wikipedia.org/wiki/Shelley_Luther"]),
        claim("sl2", "shelley-luther", "family_child_sovereignty", 0, True,
              "Defeated the anti-school-voucher Republican incumbent in the 2024 primary and then "
              "voted for the 2025 Texas school choice program (SB 2) — directing up to $10,000 "
              "per child to private and home-school expenses. Named in U.S. Senator Ted Cruz's "
              "pro-voucher ad campaign as a champion of parental educational freedom, stating she "
              "would be honored to 'fight alongside' Governor Abbott to deliver parental-choice "
              "legislation.",
              ["https://www.texastribune.org/2025/03/20/ted-cruz-voucher-ads/",
               "https://ballotpedia.org/Shelley_Luther",
               "https://en.wikipedia.org/wiki/Shelley_Luther"]),
    ]),

    # ---------- Stan Kitzman (TX-R, HD-85) ----------
    ("stan-kitzman", "TX", "State Representative", [
        claim("sk1", "stan-kitzman", "border_immigration", 0, True,
              "Made securing the Texas border his top campaign priority, stating 'With the Texas "
              "Border being left wide open, it is time to end the crisis at our border and put "
              "the safety of Texans first.' As a member of the 88th Legislature (2023), his "
              "priorities aligned with the Republican-led passage of the Texas border security "
              "package (HB 7), which created the Border Protection Unit and directed nearly "
              "$100 million to border infrastructure.",
              ["https://kitzmanfortexas.com/",
               "https://ballotpedia.org/Stan_Kitzman",
               "https://www.texastribune.org/2023/05/10/texas-legislature-border-funding/"]),
        claim("sk2", "stan-kitzman", "self_defense", 1, True,
              "An NRA-affiliated legislator representing Washington County whose campaign bio "
              "emphasizes 'A Texan's right to protect life and property is a basic human right.' "
              "Served on conference committees for SB 1 and SB 2155 during the 89th Legislature "
              "(2025) and has opposed firearms restrictions inconsistent with constitutional "
              "carry rights throughout his House tenure (2023-2026).",
              ["https://ballotpedia.org/Stan_Kitzman",
               "https://thefreedomindex.org/tx/legislator/24088/"]),
    ]),

    # ---------- Todd Ames Hunter (TX-R, HD-32) ----------
    ("todd-ames-hunter", "TX", "State Representative", [
        claim("tah1", "todd-ames-hunter", "self_defense", 0, True,
              "As House Calendars Committee Chairman — a role Hunter has held repeatedly since at "
              "least 2011 — he determines which legislation reaches the House floor for a vote. "
              "During the 87th Legislature (2021), his committee scheduled Texas HB 1927, the "
              "constitutional carry bill eliminating the handgun license requirement for "
              "law-abiding Texans; the measure passed 87-58 with 80 of 83 Republicans voting "
              "in favor. Hunter has served the Corpus Christi area (District 32) since 2009, "
              "winning re-election in November 2024 over Democratic challenger Cathy McAuliffe.",
              ["https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://www.texastribune.org/2021/05/05/constitutional-carry-guns-texas-legislature/",
               "https://ballotpedia.org/Todd_Hunter"]),
        claim("tah2", "todd-ames-hunter", "refuse_federal_overreach", 0, True,
              "Authored the 2025 Texas congressional redistricting legislation, asserting the "
              "state legislature's constitutional authority over electoral map-drawing. Texas "
              "redistricting has been the subject of repeated federal judicial challenges and "
              "DOJ interventions; Hunter's authorship of the 2025 plan continues Texas's "
              "long-running defense of state sovereignty over its own electoral geography.",
              ["https://en.wikipedia.org/wiki/Todd_Ames_Hunter",
               "https://ballotpedia.org/Todd_Hunter"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: slug + state + office_keyword must all match."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master to stay under GitHub's 50 MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
