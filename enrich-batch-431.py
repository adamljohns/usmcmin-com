#!/usr/bin/env python3
"""Enrichment batch 431: 5 West Virginia state delegates (bottom-of-alpha, unset → evidence_curated).

Federal senator/representative archetype_curated buckets are exhausted (all 0 remain);
pivoting to unset-confidence WV R state delegates with 0 evidence claims, reverse-sorted
by (state, name): Tresa Howell HD-52, S. Chris Anders HD-97, Scot C. Heckert HD-13,
Sarah Drennan HD-20, Stanley Adkins HD-49.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ---------- Tresa Howell (WV HD-52, R) ----------
    ("tresa-howell", "WV", "Delegate", [
        claim("th1", "tresa-howell", "sanctity_of_life", 0, True,
              "An openly pro-life Republican endorsed by West Virginians for Life and the West Virginia Freedom Caucus; her campaign describes life as a cornerstone priority and she runs on an unapologetically pro-life platform consistent with West Virginia's Unborn Child Protection Act.",
              ["https://ballotpedia.org/Tresa_Howell",
               "https://keepwvgreat.com/endorsements-1"]),
        claim("th2", "tresa-howell", "self_defense", 1, True,
              "Carries a National Rifle Association (NRA) endorsement; her campaign website describes her as 'unapologetically' pro-Second Amendment, opposing new firearms restrictions including red-flag laws and assault-weapons bans.",
              ["https://keepwvgreat.com/endorsements-1",
               "https://ballotpedia.org/Tresa_Howell"]),
    ]),

    # ---------- S. Chris Anders (WV HD-97, R) ----------
    ("s-chris-anders", "WV", "Delegate", [
        claim("sca1", "s-chris-anders", "sanctity_of_life", 0, True,
              "Has spent 18 years working alongside Students for Life; states that 'any government that claims to be moral or just must protect the most innocent,' affirming life-at-conception as a governing duty and his primary campaign priority.",
              ["https://berkeleycountygop.com/2024/02/s-chris-anders/",
               "https://ballotpedia.org/S._Chris_Anders"]),
        claim("sca2", "s-chris-anders", "self_defense", 1, True,
              "Worked 18 years alongside the National Association of Gun Rights (NAGR), the hardline anti-restriction group that explicitly opposes red-flag laws, assault-weapons bans, magazine limits, and registries; campaigns to 'preserve the 2nd Amendment and the entire Bill of Rights.'",
              ["https://berkeleycountygop.com/2024/02/s-chris-anders/",
               "https://ballotpedia.org/S._Chris_Anders"]),
        claim("sca3", "s-chris-anders", "family_child_sovereignty", 0, True,
              "Campaigns for 'full and complete school choice to restore parental freedom in education,' explicitly framing the issue as restoring parental sovereignty over children's schooling against institutional control.",
              ["https://berkeleycountygop.com/2024/02/s-chris-anders/",
               "https://ballotpedia.org/S._Chris_Anders"]),
    ]),

    # ---------- Scot C. Heckert (WV HD-13, R) ----------
    ("scot-c-heckert", "WV", "Delegate", [
        claim("sch1", "scot-c-heckert", "sanctity_of_life", 0, True,
              "Publicly anti-abortion; campaigns on protecting unborn life and upholding West Virginia's abortion restrictions, affirming his support for the state's Unborn Child Protection Act framework.",
              ["https://en.wikipedia.org/wiki/Scot_Heckert",
               "https://www.spiritofjefferson.com/news/article_40f6ab90-91fa-11ef-8d97-c3adf4ca3e7b.html"]),
        claim("sch2", "scot-c-heckert", "self_defense", 0, True,
              "Campaigns on protecting gun-ownership rights in Jefferson County; supports West Virginia's constitutional carry (permitless carry) law and opposes new firearms restrictions.",
              ["https://www.spiritofjefferson.com/news/article_40f6ab90-91fa-11ef-8d97-c3adf4ca3e7b.html",
               "https://ballotpedia.org/Scot_Heckert"]),
    ]),

    # ---------- Sarah Drennan (WV HD-20, R) ----------
    ("sarah-drennan", "WV", "Delegate", [
        claim("sd1", "sarah-drennan", "family_child_sovereignty", 0, True,
              "Campaigns on 'prioritizing children's education over current social issues in schools,' opposing ideological agendas in classrooms; draws on over a decade of volunteering in the school system as a concerned parent.",
              ["https://ballotpedia.org/Sarah_Drennan",
               "https://www.wvgazettemail.com/elections/candidate-profile-sarah-drennan-house-of-delegates-district-20/article_282e63d3-417f-57f3-95d6-61dd5164748f.html"]),
        claim("sd2", "sarah-drennan", "sanctity_of_life", 0, True,
              "Stated in a 2024 voter-guide survey that chemical abortion drugs should meet essential safety standards (including in-person physician consultation) and that abortion providers including Planned Parenthood should not receive taxpayer funds from any level of government.",
              ["https://ivoterguide.com/candidate/79242/race/19543/election/1100",
               "https://ballotpedia.org/Sarah_Drennan"]),
    ]),

    # ---------- Stanley Adkins (WV HD-49, R) ----------
    ("stanley-adkins", "WV", "Delegate", [
        claim("sa1", "stanley-adkins", "sanctity_of_life", 0, True,
              "States 'I am pro life. I do not think doctors should murder children,' making his opposition to abortion an unambiguous stated commitment on the campaign trail.",
              ["https://mountainstatespotlight.org/2024/08/15/49th-house-district-candidates-wv/"]),
        claim("sa2", "stanley-adkins", "self_defense", 0, False,
              "Cast the only Republican vote against a 2026 West Virginia House bill (passed 93-1) expanding constitutional carry (permitless carry) to adults aged 18-20, departing from his party's near-unanimous support for broadening Second Amendment carry rights.",
              ["https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents slug collisions across states."""
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

    # Minified write — preserve no-whitespace master (keeps file ~35-36 MB, under GitHub's 50 MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
