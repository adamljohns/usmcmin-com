#!/usr/bin/env python3
"""Enrichment batch 766: 5 Vermont R State Representatives (bottom-of-alphabet targets).

Primary archetype_curated federal senator/rep buckets are exhausted; this batch
targets archetype_party_default VT R State Representatives — the next
bottom-of-alphabet state group.

Targets (reversed-alpha VT sweep, selecting those with documentable records):
  James Gregoire     (Franklin-6, serving since 2019)
  Gina Galfetti      (Washington-Orange, since 2023)
  Carolyn Branagan   (Franklin-1, since 2023; prev. 2002-2016)
  Joseph Parsons     (Orange-Caledonia, since 2021)
  Eileen Dickinson   (Franklin-2, serving since 2009)

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- James Gregoire (VT, State Rep Franklin-6, since 2019) ----------
    ("james-gregoire", "VT", "Representative", [
        claim("jg1", "james-gregoire", "family_child_sovereignty", 0, True,
              "Co-sponsored H.173 (2023-2024), 'An act relating to prohibiting manipulating a "
              "child for the purpose of sexual contact'; signed by the governor on June 12, 2024, "
              "becoming Act 172. The legislation creates a new criminal offense for adults who use "
              "coercion, grooming, or psychological pressure to obtain sexual contact with a minor, "
              "filling a gap in Vermont's child-protection statutes.",
              ["https://legislature.vermont.gov/bill/status/2024/H.173",
               "https://trackbill.com/bill/vermont-house-bill-173-an-act-relating-to-prohibiting"
               "-manipulating-a-child-for-the-purpose-of-sexual-contact/2355994/"]),
        claim("jg2", "james-gregoire", "refuse_state_overreach", 0, True,
              "Published an op-ed in the St. Albans Messenger in 2025 opposing S.190, a Vermont "
              "healthcare price-cap mandate, arguing it would harm rural Vermonters and push "
              "Northeast Medical Center into financial crisis through arbitrary price controls for "
              "select groups — cost-shifting, not structural reform. Gregoire, vice chair of the "
              "House Corrections and Institutions Committee, called the pattern of passing costly "
              "mandates rather than fixing structural problems Vermont's persistent policy failure.",
              ["https://www.samessenger.com/opinion/letters_to_editor/letter-to-the-editor-cant-"
               "lower-healthcare-costs-until-vermont-fixes-bad-policy/"
               "article_0d2c3cb9-05de-4167-a74a-2bab75204f3b.html"]),
    ]),

    # ---------- Gina Galfetti (VT, State Rep Washington-Orange, since 2023) ----------
    ("gina-galfetti", "VT", "Representative", [
        claim("gg1", "gina-galfetti", "refuse_state_overreach", 0, True,
              "Co-sponsored H.74 (2023-2024), 'An act relating to repealing the Global Warming "
              "Solutions Act,' which would eliminate Vermont's mandatory greenhouse-gas reduction "
              "requirements and replace them with voluntary goals, repeal the Vermont Climate "
              "Council, and remove the mandate to produce a Climate Action Plan — directly "
              "dismantling the state's regulatory climate-mandate framework.",
              ["https://legislature.vermont.gov/bill/status/2024/H.74",
               "https://www.billtrack50.com/billdetail/1533123"]),
        claim("gg2", "gina-galfetti", "economic_stewardship", 4, True,
              "Member of the American Legislative Exchange Council (ALEC), which develops model "
              "state legislation promoting free markets, limited government, and federalism — "
              "providing a counterweight to ESG, WEF, and globalist regulatory frameworks that "
              "impose compliance burdens on states and businesses. ALEC's model bills directly "
              "oppose the mandatory climate, energy, and ESG mandates that Galfetti has challenged "
              "in Vermont.",
              ["https://alec.org/person/gina-galfetti/"]),
    ]),

    # ---------- Carolyn Branagan (VT, State Rep Franklin-1, since 2023; prev. 2002-2016) ----------
    ("carolyn-branagan", "VT", "Representative", [
        claim("cb1", "carolyn-branagan", "refuse_state_overreach", 0, True,
              "Co-sponsored H.74 (2023-2024), 'An act relating to repealing the Global Warming "
              "Solutions Act,' seeking to eliminate Vermont's mandatory carbon-reduction framework. "
              "Branagan, a long-serving legislator (2002-2016, 2023-present) and Vice Chair of the "
              "House Committee on Ways and Means, has pressed for regulatory rollback as fiscal "
              "relief for Vermont families facing some of the nation's highest energy costs.",
              ["https://legislature.vermont.gov/bill/status/2024/H.74",
               "https://www.billtrack50.com/billdetail/1533123"]),
        claim("cb2", "carolyn-branagan", "economic_stewardship", 2, True,
              "Called Vermont's 2024 education funding crisis an 'old-fashioned taxpayer revolt' "
              "and criticized H.887 for lacking 'structural reform' and 'long-term cost "
              "containment.' As Vice Chair of House Ways and Means, Branagan argued the legislature "
              "should have built lasting structural controls rather than simply passing revenue "
              "increases, and identified rising class-size ratios as a cost-reduction lever the "
              "legislature has failed to use.",
              ["https://www.samessenger.com/news/schools/old-fashioned-taxpayer-revolt-while-vermont"
               "-legislators-talk-education-funding-solutions-school-budgets-fail/"
               "article_6a51ea60-0341-11ef-bac2-035480687da1.html",
               "https://ballotpedia.org/Carolyn_Whitney_Branagan"]),
    ]),

    # ---------- Joseph Parsons (VT, State Rep Orange-Caledonia, since 2021) ----------
    ("joseph-parsons", "VT", "Representative", [
        claim("jp1", "joseph-parsons", "refuse_state_overreach", 0, True,
              "Co-sponsored H.671 (2023-2024), 'An act relating to repealing the Affordable Heat "
              "Act and the Global Warming Solutions Act,' which would repeal the Clean Heat "
              "Standard (enacted as Act 18 of 2023 over the governor's veto), eliminate Vermont's "
              "mandatory carbon-emission targets, and repeal the Vermont Climate Council — directly "
              "unwinding the state's climate regulatory mandates that drive up energy costs for "
              "Vermont consumers and small businesses.",
              ["https://legislature.vermont.gov/bill/status/2024/H.671",
               "https://www.billtrack50.com/billdetail/1659309"]),
        claim("jp2", "joseph-parsons", "economic_stewardship", 4, True,
              "Co-sponsored H.74 (2023-2024), 'An act relating to repealing the Global Warming "
              "Solutions Act,' joining other Vermont Republicans in challenging the state's "
              "ESG-aligned mandatory climate framework. The GWSA imposes non-negotiable compliance "
              "requirements on Vermont's economy that parallel the ESG/WEF regulatory regimes the "
              "rubric identifies as economically destructive.",
              ["https://legislature.vermont.gov/bill/status/2024/H.74",
               "https://www.billtrack50.com/billdetail/1533123"]),
    ]),

    # ---------- Eileen Dickinson (VT, State Rep Franklin-2, since 2009) ----------
    ("eileen-dickinson", "VT", "Representative", [
        claim("ed1", "eileen-dickinson", "self_defense", 1, True,
              "Added an amendment to Vermont's 2018 omnibus gun control bill (S.55, Act 94) "
              "exempting manufacturers from the magazine-capacity limit, specifically protecting "
              "Century Arms, which employs approximately 200 Vermonters. Her amendment allowed "
              "manufacturers to continue importing, exporting, and producing standard-capacity "
              "magazines for out-of-state commerce — a Second Amendment and economic protection "
              "against an anti-gun-rights majority.",
              ["https://vtdigger.org/2018/03/26/amendment-looks-exempt-manufacturers-magazine-limit/"]),
        claim("ed2", "eileen-dickinson", "refuse_state_overreach", 0, True,
              "Earned a 0% score from Vermont Conservation Voters for the 2025-2026 biennium and "
              "a 20% lifetime score, reflecting consistent votes against state environmental and "
              "regulatory mandates across her 15+ year legislative career (serving since 2009). "
              "Dickinson, an Angus cattle farmer from St. Albans Town, has voted against the "
              "regulatory compliance burdens VCV tracks, placing her among Vermont's most "
              "consistent opponents of state-imposed mandates on landowners and businesses.",
              ["https://vermontconservationvoters.com/legislators/eileen-dickinson/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
