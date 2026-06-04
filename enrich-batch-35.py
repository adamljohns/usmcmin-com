#!/usr/bin/env python3
"""Enrichment batch 35: 4 bottom-of-alphabet federal House candidates with 0 claims.

Targets (all archetype_curated, 0 claims, bottom of reverse-alpha sort):
  Derek Merrin     (OH-09 R) — constitutional carry + voter ID + school choice
  Yvette Herrell   (NM-02 R) — NRA A-rating + border wall support
  Robert Smullen   (NY-21 R) — NYSRPA-endorsed + anti-sanctuary + fiscal sanity
  James Settelmeyer(NV-02 R) — Trump border + anti-tax lawsuit + federal land overreach

All claims cite >=1 reliable public source (2024-2026 positions or documented record).
MINIFIED write preserved (see batch-4 note).
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
    # ---------- Derek Merrin (OH-09, R) ----------
    ("derek-merrin", "OH", "representative", [
        claim("dm1", "derek-merrin", "election_integrity", 0, True,
              "Played a key legislative role in passing Ohio's photo ID voting requirement (enacted January 2023), co-authoring the law that mandates government-issued ID at the polls — consistent with the rubric's voter-ID standard for election integrity.",
              ["https://ballotpedia.org/Derek_Merrin",
               "https://www.ideastream.org/government-politics/2026-05-05/republican-derek-merrin-wins-primary-will-face-longtime-incumbent-kaptur-in-key-rematch"]),
        claim("dm2", "derek-merrin", "self_defense", 0, True,
              "Played a lead role in enacting Ohio's permitless (constitutional) carry law (2022), which allows any law-abiding Ohioan 21+ to carry a concealed handgun without a government license — firmly aligning with the constitutional-carry standard.",
              ["https://ballotpedia.org/Derek_Merrin",
               "https://www.derekmerrin.com/"]),
        claim("dm3", "derek-merrin", "family_child_sovereignty", 0, True,
              "Spearheaded Ohio's universal EdChoice school-voucher expansion in the 2023-24 state budget, opening state-funded school choice to every K-12 student regardless of household income — a direct parental-rights and educational-freedom policy.",
              ["https://ballotpedia.org/Derek_Merrin",
               "https://www.statenews.org/government-politics/2023-05-18/universal-school-vouchers-supporters-seek-ohio-lawmakers-attention-with-statehouse-rally"]),
    ]),

    # ---------- Yvette Herrell (NM-02, R) ----------
    ("yvette-herrell", "NM", "representative", [
        claim("yh1", "yvette-herrell", "self_defense", 0, True,
              "Earned an NRA 'A' rating across both her New Mexico state legislative career and her 2021-2023 congressional term; as a self-described 'proud NRA member,' consistently opposed new federal firearm restrictions, holding a 100% Heritage Action score for the 117th Congress.",
              ["https://ballotpedia.org/Yvette_Herrell",
               "https://www.dailylobo.com/article/2024/10/new-mexicos-2nd-congressional-district-yvette-herrell",
               "https://heritageaction.com/scorecard/members/H001084/117"]),
        claim("yh2", "yvette-herrell", "border_immigration", 0, True,
              "Publicly supports completing Trump's southern border wall, stating 'I support President Trump's efforts to finish building the wall,' and backs full ICE enforcement — opposing blanket amnesty and demanding secure borders as a core 2026 platform position.",
              ["https://www.borderreport.com/regions/new-mexico/views-on-immigration-border-wall-set-new-mexico-congressional-candidates-apart/",
               "https://ballotpedia.org/Yvette_Herrell"]),
    ]),

    # ---------- Robert Smullen (NY-21, R) ----------
    ("robert-smullen", "NY", "representative", [
        claim("rs1", "robert-smullen", "self_defense", 0, True,
              "Endorsed by the New York State Rifle and Pistol Association (NYSRPA), whose president Tom King called him 'a reliable and vocal defender of the Second Amendment for law-abiding gun owners'; stated 'I have never backed down from defending the Second Amendment, and I never will.'",
              ["https://www.dailygazette.com/leader_herald/leader_herald/smullen-herkimer-gun/article_2a96ad88-01ce-47df-8fec-05c3512e83f0.html",
               "https://www.northcountrypublicradio.org/news/story/53175/20260318/ny-s-republican-party-backs-smullen-in-ny-21-race"]),
        claim("rs2", "robert-smullen", "border_immigration", 2, True,
              "In the New York state Assembly, voted against making New York a sanctuary state; pledged to fight sanctuary-city and sanctuary-state policies at the federal level if elected to Congress.",
              ["https://www.wamc.org/news/2026-05-26/ny-21-candidate-questionnaire-republicans-smullen-constantino"]),
        claim("rs3", "robert-smullen", "economic_stewardship", 2, True,
              "Campaign platform centers on 'restoring fiscal sanity' to the federal government, opposing runaway deficit spending, and demanding fiscal accountability — consistent with the anti-deficit and balanced-budget rubric standard.",
              ["https://spectrumlocalnews.com/nys/central-ny/politics/2026/03/19/state-republican-party-chair-backs-robert-smullen-in-ny-21-race",
               "https://www.northcountrypublicradio.org/news/story/53175/20260318/ny-s-republican-party-backs-smullen-in-ny-21-race"]),
    ]),

    # ---------- James Settelmeyer (NV-02, R) ----------
    ("james-settelmeyer", "NV", "representative", [
        claim("js1", "james-settelmeyer", "border_immigration", 0, True,
              "Supports President Trump's border-security effort, stating 'he's done a tremendous job securing the border'; emphasizes enforcement against illegal immigrants with criminal histories and would restore strong border control as a federal priority.",
              ["https://www.kunr.org/local-stories/2026-03-26/meet-james-settelmeyer-republican-candidate-for-nevadas-cd2",
               "https://thenevadaindependent.com/article/james-settelmeyer-is-mr-rural-nevada-is-he-maga-enough-to-win-a-gop-house-primary"]),
        claim("js2", "james-settelmeyer", "economic_stewardship", 2, True,
              "As Nevada State Senate Republican Leader, successfully sued the Democratic majority and won a court ruling blocking a tax increase attempted without the constitutionally required two-thirds supermajority; has campaigned consistently on limited government and low taxes.",
              ["https://www.nevadaappeal.com/news/2026/apr/09/without-trump-endorsement-settelmeyer-running-on-record/",
               "https://www.kunr.org/local-stories/2026-03-26/meet-james-settelmeyer-republican-candidate-for-nevadas-cd2"]),
        claim("js3", "james-settelmeyer", "refuse_federal_overreach", 0, True,
              "As a fourth-generation Nevada rancher, opposes federal overreach in public-land management; seeks a House Natural Resources Committee seat to address Washington's checkerboarded-land policies and return land-management decision-making power to states and local communities.",
              ["https://www.kunr.org/local-stories/2026-03-26/meet-james-settelmeyer-republican-candidate-for-nevadas-cd2",
               "https://thenevadaindependent.com/article/james-settelmeyer-is-mr-rural-nevada-is-he-maga-enough-to-win-a-gop-house-primary"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collision."""
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
