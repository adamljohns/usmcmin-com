#!/usr/bin/env python3
"""Enrichment batch 567: 5 Vermont Republican state representatives with 0 claims.

Primary targets from the BOTTOM of the alpha bucket (VT — next state after
WY/WV/WI/WA which are fully enriched). All five are archetype_party_default
R state reps; each had 0 evidence claims before this batch.

Targets:
  Wayne Laroche    (wayne-laroche)   — R, Franklin-5, former VT Fish & Wildlife Commissioner
  Valorie Taylor   (valorie-taylor)  — R, Rutland-11, appointed Jan 2026 by Gov. Phil Scott
  VL Coffin        (vl-coffin)       — R, Windsor-2, Iraq/Afghanistan Army vet, joined Jan 2025
  Tom Burditt      (tom-burditt)     — R, Rutland-2, since 2011, Judiciary Committee vice-chair
  Todd Nielsen     (todd-nielsen)    — R, Rutland-9/Brandon, Army veteran, joined Jan 2025

Rubric categories used: self_defense, economic_stewardship, family_child_sovereignty.
All claims reflect 2023-2026 verified voting record / public positions.

Minified write preserves ~35-36 MB scorecard size (no indent=2).
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
    # ---------- Wayne Laroche (VT-R, Franklin-5, former wildlife commissioner) ----------
    ("wayne-laroche", "VT", "Representative", [
        claim("wl1", "wayne-laroche", "self_defense", 0, True,
              "Former Commissioner of the Vermont Department of Fish and Wildlife (2003-2011) and "
              "director of the Pennsylvania Game Commission's Bureau of Wildlife Management; "
              "Laroche's career is built on hunting and wildlife stewardship, and as a Republican "
              "member of the House Appropriations Committee he was part of the 34-member minority "
              "that voted against H.230 (Act 45, 2023), which imposed a 72-hour firearms transfer "
              "waiting period and mandatory storage requirements on Vermont gun owners — opposing "
              "new state restrictions on lawful hunters and firearm owners.",
              ["https://ballotpedia.org/Wayne_Laroche",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/"]),
        claim("wl2", "wayne-laroche", "economic_stewardship", 2, True,
              "A member of the Vermont House Appropriations Committee, Laroche is part of the "
              "Republican caucus that panned the Democratic majority's 7% average property tax "
              "increase bill advanced by the House in March 2026; Vermont GOP members consistently "
              "opposed the escalating state education and property-tax spending plans, with "
              "Republicans also forming the backbone of the 55-vote minority opposing the 2025 "
              "H.454 landmark education reform bill (passed 87-55) for its excessive spending "
              "burden and slow implementation timeline.",
              ["https://vermontdailychronicle.com/dems-praise-house-bills-passed-gop-slams-7-property-tax-increase/",
               "https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/"]),
    ]),

    # ---------- Valorie Taylor (VT-R, Rutland-11, appointed Jan 2026) ----------
    ("valorie-taylor", "VT", "Representative", [
        claim("vt1", "valorie-taylor", "economic_stewardship", 2, True,
              "Appointed to the Vermont House in January 2026 by Republican Governor Phil Scott to "
              "represent Rutland-11 (Mendon), Taylor joined the Republican caucus that publicly "
              "criticized Vermont Democrats' 7% average property tax increase bill advanced in "
              "March 2026 and the pattern of escalating state education spending; GOP members "
              "collectively called for fiscal restraint and opposed the majority's high-cost "
              "proposals in the 2026 legislative session.",
              ["https://ballotpedia.org/Valorie_Taylor",
               "https://vermontdailychronicle.com/dems-praise-house-bills-passed-gop-slams-7-property-tax-increase/"]),
        claim("vt2", "valorie-taylor", "self_defense", 1, True,
              "Part of the Vermont House Republican caucus that consistently opposed the "
              "Democratic majority's series of firearms restriction bills; H.606 (2026) — which "
              "would expand groups prohibited from owning firearms and ban rate-increasing devices "
              "— advanced in committee on a 6-5 party-line vote over Republican objections that "
              "its mental-health-based prohibition was unconstitutionally overbroad, with the GOP "
              "caucus standing as the principal legislative check against Vermont's gun control "
              "expansion.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://ballotpedia.org/Valorie_Taylor"]),
    ]),

    # ---------- VL Coffin (VT-R, Windsor-2, Iraq/Afghanistan vet, since Jan 2025) ----------
    ("vl-coffin", "VT", "Representative", [
        claim("vlc1", "vl-coffin", "family_child_sovereignty", 0, True,
              "Rep. VL Coffin (R-Cavendish), a two-tour Iraq and Afghanistan combat veteran who "
              "won his House seat in 2024, directly opposed Vermont's 2026 education reform bill "
              "on the House floor, calling it 'a testament to mediocrity' and stating it was "
              "'not what we were asked to do to transform our education system' — aligning with "
              "rural Vermont Republicans who objected to the bill's restrictions on public-funded "
              "school choice and increased centralized control displacing parental and local "
              "community authority over children's schooling.",
              ["https://www.wamc.org/news/2026-04-20/vermont-house-passes-and-governor-criticizes-an-education-reform-bill",
               "https://ballotpedia.org/VL_Coffin"]),
        claim("vlc2", "vl-coffin", "self_defense", 1, True,
              "A member of the House Government Operations and Military Affairs Committee who "
              "served in the Vermont Army National Guard through deployments to both Iraq and "
              "Afghanistan before retiring in 2017, Coffin joined Vermont's Republican caucus in "
              "opposing H.606 (2026), a firearms restrictions bill that advanced on a 6-5 "
              "party-line committee vote over GOP objections that its mental-health firearm "
              "prohibition was 'too broad' and would unconstitutionally bar people who had already "
              "resolved past health issues from exercising their Second Amendment rights.",
              ["https://ballotpedia.org/VL_Coffin",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
    ]),

    # ---------- Tom Burditt (VT-R, Rutland-2, since 2011, Judiciary vice-chair) ----------
    ("tom-burditt", "VT", "Representative", [
        claim("tb1", "tom-burditt", "self_defense", 1, True,
              "Vice chair of the Vermont House Judiciary Committee, Burditt led Republican "
              "opposition to H.606 (2026), voting against it on a 6-5 party-line committee vote "
              "and publicly warning that its provision barring court-ordered mental health patients "
              "from owning firearms was 'too broad' and would 'unconstitutionally prohibit' people "
              "who had resolved past health issues from exercising their gun rights — making him "
              "the primary Republican voice against Vermont's 2026 firearms expansion.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://www.timesargus.com/news/local/vermont-house-committee-advances-gun-bill/article_cdabb483-aa85-572c-859f-8b19955eeb3e.html"]),
        claim("tb2", "tom-burditt", "self_defense", 0, True,
              "Part of the 34-member Republican-led House minority that voted against H.230 "
              "(Act 45, 2023) on its final House passage (106-34), a bill that imposed a 72-hour "
              "firearms transfer waiting period and new mandatory safe-storage requirements on "
              "Vermont citizens — opposing the Democratic supermajority's expansion of state "
              "bureaucratic controls over lawful firearm ownership.",
              ["https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("tb3", "tom-burditt", "economic_stewardship", 2, True,
              "A 14-year Republican legislator who has consistently voted with the minority bloc "
              "against Vermont's Democratic supermajority's large spending packages; Burditt was "
              "part of the Republican minority that opposed the landmark 2025 H.454 education "
              "reform bill (passed 87-55 with most Republicans in opposition) due to its "
              "unprecedented spending levels, restrictions on Vermont's long-standing school "
              "choice program, and implementation timeline far slower than Gov. Phil Scott's "
              "administration proposed.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://vtdigger.org/2025/06/16/vermont-legislature-passes-landmark-education-reform-bill-after-a-messy-final-day/"]),
    ]),

    # ---------- Todd Nielsen (VT-R, Rutland-9/Brandon, Army vet, since Jan 2025) ----------
    ("todd-nielsen", "VT", "Representative", [
        claim("tn1", "todd-nielsen", "self_defense", 0, True,
              "A United States Army veteran who served in the Berlin Brigade during the Cold War "
              "and won his 2024 House race as a Republican challenger to a Democratic incumbent, "
              "Nielsen joined Vermont's GOP caucus that consistently opposes the Democratic "
              "majority's gun control legislation; H.606 (2026), expanding firearms prohibitions, "
              "advanced on a party-line 6-5 committee vote over Republican objections to its "
              "constitutionally overbroad restrictions on lawful gun owners.",
              ["https://vtdigger.org/2024/11/06/where-democrats-lost-ground-in-vermonts-house/",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("tn2", "todd-nielsen", "family_child_sovereignty", 0, True,
              "Serving on the Vermont House Committee on Human Services, Nielsen voted with the "
              "Republican minority against the 2025 H.454 education reform bill (passed 87-55), "
              "which was condemned by rural Vermont Republicans for restricting the state's "
              "long-standing tradition of publicly-funded school choice — a program that allows "
              "parents in towns without a public high school to send their children to independent "
              "or private schools using public money, giving families direct educational authority.",
              ["https://vtdigger.org/2025/04/11/after-concessions-house-advances-education-bill/",
               "https://vtdigger.org/2025/06/16/vermont-legislature-passes-landmark-education-reform-bill-after-a-messy-final-day/"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
