#!/usr/bin/env python3
"""Enrichment batch 291: hand-curated claims for 5 Wyoming state senators.

Targets archetype_party_default WY state senators from the bottom of the
alphabet with 0 evidence claims (continuing from batch 290).

Targets: Stephan Pappas (WY-R SD-7), Stacy Jones (WY-R SD-13),
Ogden Driskill (WY-R SD-1, Senate President), Mike Gierau (WY-D SD-17),
Laura Taliaferro Pearson (WY-R SD-14).

All five senators' votes on HB0126 (Wyoming Human Heartbeat Act, 2026)
confirmed via wyoleg.gov roll call — 27 Ayes, 4 Nays. Governor Gordon
signed the act March 9, 2026. Additional individual claims sourced from
ballotpedia.org, cowboystatedaily.com, and wyomingnews.com.

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
    # ---------- Stephan Pappas (WY-R, State Senator SD-7) ----------
    ("stephan-pappas", "WY", "State Senator", [
        claim("sp1", "stephan-pappas", "sanctity_of_life", 0, True,
              "Publicly declared 'I believe that abortion is not a legal and morally valid choice. The life of a new human being starts at fertilization; a scientific fact.' Voted AYE on HB0126 (Wyoming Human Heartbeat Act, 2026), one of 27 senators who passed the bill 27-4; Governor Gordon signed it March 9, 2026, prohibiting abortion after fetal heartbeat detection.",
              ["https://cowboystatedaily.com/2022/09/28/democrat-marcie-kindred-trying-to-unseat-gop-sen-stephan-pappas-in-cheyenne-senate-seat/",
               "https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2026/03/09/gordon-signs-heartbeat-act-abortion-ban-despite-concerns-its-not-enough-for-courts/"]),
        claim("sp2", "stephan-pappas", "refuse_federal_overreach", 0, False,
              "A 'fervent supporter of Medicaid expansion and the state's mental health services' who is, unlike many other Republican legislators, 'not opposed to accepting federal money' — importing federal matching funds and federal program requirements into Wyoming's health system in a manner inconsistent with limiting federal government reach.",
              ["https://cowboystatedaily.com/2022/09/28/democrat-marcie-kindred-trying-to-unseat-gop-sen-stephan-pappas-in-cheyenne-senate-seat/"]),
    ]),

    # ---------- Stacy Jones (WY-R, State Senator SD-13) ----------
    ("stacy-jones", "WY", "State Senator", [
        claim("sj1", "stacy-jones", "sanctity_of_life", 0, True,
              "Voted AYE on HB0126 (Wyoming Human Heartbeat Act, 2026), part of the 27-4 senate majority that banned abortions after fetal heartbeat detection; Governor Gordon signed the act into law March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2026/03/09/gordon-signs-heartbeat-act-abortion-ban-despite-concerns-its-not-enough-for-courts/"]),
        claim("sj2", "stacy-jones", "self_defense", 0, True,
              "A lifetime member of the National Rifle Association (NRA) and member of the Gun Owners of America (GOA); a gun owner who campaigned as a defender of Second Amendment rights representing a rural southwest Wyoming district (Rock Springs) where constitutional-carry is the baseline expectation.",
              ["https://www.wyomingnews.com/wyomingbusinessreport/industry_news/government_and_politics/women-in-politics-local-businesswoman-runs-for-senate-district-no-13/article_fdf78ae6-fd66-11ec-accb-2b9666f4abdf.html",
               "https://ballotpedia.org/Stacy_Jones"]),
    ]),

    # ---------- Ogden Driskill (WY-R, State Senator SD-1, Senate President) ----------
    ("ogden-driskill", "WY", "State Senator", [
        claim("od1", "ogden-driskill", "sanctity_of_life", 0, True,
              "Voted AYE on HB0126 (Wyoming Human Heartbeat Act, 2026) as part of the 27-4 senate majority; the act prohibits abortion after fetal heartbeat detection and was signed by Governor Gordon on March 9, 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2026/03/09/gordon-signs-heartbeat-act-abortion-ban-despite-concerns-its-not-enough-for-courts/"]),
        claim("od2", "ogden-driskill", "sanctity_of_life", 1, False,
              "Voted against introduction of SJ 7 (2026 anti-abortion constitutional amendment) alongside eight other Republicans, blocking the measure by one vote from the required two-thirds majority; as Senate President representing the traditional-wing caucus, he prefers incremental statutory restrictions over a constitutional prohibition, declining to support the abolition-first approach the amendment represented.",
              ["https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/",
               "https://ballotpedia.org/Ogden_Driskill"]),
    ]),

    # ---------- Mike Gierau (WY-D, State Senator SD-17) ----------
    ("mike-gierau", "WY", "State Senator", [
        claim("mg1", "mike-gierau", "sanctity_of_life", 0, False,
              "Voted NAY on HB0126 (Wyoming Human Heartbeat Act, 2026), one of only four senators to oppose the bill that bans abortion after fetal heartbeat detection; as Teton County's Democratic senator he has sponsored and supported legislation expanding abortion access, including a Reproductive Freedom Act relating to abortion and reproductive rights.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2025/02/18/mike-gierau-is-the-ultimate-wyoming-political-underdog-a-democrat-from-jackson/"]),
        claim("mg2", "mike-gierau", "self_defense", 0, True,
              "Despite serving as one of Wyoming's two Democratic state senators, explicitly identifies as a gun owner and states he 'supports the right to bear arms' — an unusual bipartisan alignment on Second Amendment rights that reflects the gun-culture norms of his state even as his party generally moves the opposite direction.",
              ["https://cowboystatedaily.com/2025/02/18/mike-gierau-is-the-ultimate-wyoming-political-underdog-a-democrat-from-jackson/"]),
    ]),

    # ---------- Laura Taliaferro Pearson (WY-R, State Senator SD-14) ----------
    ("laura-taliaferro-pearson", "WY", "State Senator", [
        claim("lp1", "laura-taliaferro-pearson", "sanctity_of_life", 0, True,
              "Voted AYE on HB0126 (Wyoming Human Heartbeat Act, 2026, 27-4 vote signed by Governor Gordon); voted to override Governor Gordon's veto of HB0239 (2025 ultrasound bill requiring ultrasound viewing before dispensing abortion pills), arguing it 'protects mothers and babies'; also ultimately voted AYE on SJ 7 (2026 anti-abortion constitutional amendment) after initially wavering — a consistent, multi-front pro-life voting record in her first session.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://cowboystatedaily.com/2025/03/05/legislature-overrides-governors-veto-of-ultrasound-abortion-bill/",
               "https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/"]),
        claim("lp2", "laura-taliaferro-pearson", "family_child_sovereignty", 0, True,
              "One of only two Wyoming Freedom Caucus-endorsed senators in 2024; defeated Wyoming House Speaker Albert Sommers in the Republican primary, delivering a parental-rights and state-sovereignty mandate from rural southwest Wyoming; entered the legislature stating her core mission is 'to protect our state' from federal and bureaucratic overreach, aligning with the Freedom Caucus's parental rights and anti-federal-control platform.",
              ["https://www.wyomingnews.com/rocketminer/to-protect-our-state-pearson-prepares-for-new-role-in-wyoming-legislature/article_da10c222-bd81-11ef-962d-db19e6055383.html",
               "https://www.wyomingnews.com/laramieboomerang/laramieboomerang/news/will-the-wyoming-freedom-caucus-win-control-of-the-senate/article_ed650e6e-2195-4019-9f7b-8e5d7f152f9d.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
