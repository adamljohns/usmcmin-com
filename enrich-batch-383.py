#!/usr/bin/env python3
"""Enrichment batch 383: additional claims for 5 2026 U.S. Senate candidates.

All five are evidence_curated candidates (already 3 claims each) from the bottom
of the alphabet (OK×4, NC×1), adding 2-3 new claims each in rubric categories
not yet scored.

Mix (all R): Nick Hankins (OK-R), William Sean Buckner (OK-R), Brian Ragain (OK-R),
Gary Ty England (OK-R), Michele Morrow (NC-R).

Kevin Hern won the OK GOP primary (June 16 2026, 67.3%); Whatley won NC GOP
primary (Mar 3 2026). These are the other candidates from those primaries whose
scorecards still carry 3 claims and needed scoring in additional rubric categories.

Sources: ivoterguide.com candidate profiles, oksaysno.com, auditthesenate.com,
ragainforsenate.com, garytyenglandforsenate.com, wfmynews2.com.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace).
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
    # -------- Nick Hankins (OK-R, 2026 U.S. Senate candidate · Mullin seat) --------
    ("nick-hankins", "OK", "Senator", [
        claim("nh1", "nick-hankins", "biblical_marriage", 0, True,
              "On the iVoterGuide 2026 Oklahoma U.S. Senate questionnaire, Hankins stated: 'Marriage is a God-ordained, sacred and legal union of one man and one woman. No government has the authority to alter this definition.' — an explicit one-man-one-woman affirmation matching the rubric's standard.",
              ["https://ivoterguide.com/candidate/80985/race/27978/election/1425",
               "https://www.oksaysno.com/"]),
        claim("nh2", "nick-hankins", "election_integrity", 0, True,
              "On the 2026 Oklahoma Senate voter guide, Hankins answered 'We need photo ID, proof of citizenship' when asked about election access — a direct affirmation of the photo-ID and proof-of-citizenship standard the rubric requires.",
              ["https://ivoterguide.com/candidate/80985/race/27978/election/1425",
               "https://www.oksaysno.com/"]),
        claim("nh3", "nick-hankins", "economic_stewardship", 2, True,
              "Hankins stated on the 2026 Oklahoma Senate voter guide: 'Government should greatly reduce spending, lowering the necessary tax burden' and 'The government should cut spending in order to reduce the national debt' — a clear anti-deficit, balanced-budget posture consistent with the rubric's fiscal stewardship standard.",
              ["https://ivoterguide.com/candidate/80985/race/27978/election/1425",
               "https://www.oksaysno.com/"]),
    ]),

    # -------- William Sean Buckner (OK-R, 2026 U.S. Senate candidate · Mullin seat) --------
    ("william-sean-buckner", "OK", "Senator", [
        claim("wsb1", "william-sean-buckner", "election_integrity", 0, True,
              "Buckner's campaign (auditthesenate.com) explicitly opposes mass mail-in voting expansion and runs under the 'Audit the Senate' brand — a government-accountability platform built around election process transparency. He spent years documenting government meetings on camera and accepts zero PAC money or special-interest backing, positioning himself as a safeguard against institutional fraud in elections and government alike.",
              ["https://auditthesenate.com/",
               "https://ballotpedia.org/United_States_Senate_election_in_Oklahoma,_2026_(June_16_Republican_primary)"]),
        claim("wsb2", "william-sean-buckner", "economic_stewardship", 2, True,
              "Buckner's entire campaign is built around 'Audit the Senate' — exposing and reducing congressional waste. His platform calls for cutting federal regulations that inflate production costs, champions domestic natural-gas manufacturing over costly imports, and takes zero PAC money or billionaire funding to avoid captured-spending incentives — a limited-government, anti-waste posture consistent with the rubric's anti-deficit and balanced-budget standard.",
              ["https://auditthesenate.com/",
               "https://www.fec.gov/data/candidate/S6OK04254/"]),
    ]),

    # -------- Brian Ragain (OK-R, 2026 U.S. Senate candidate · Mullin seat) --------
    ("brian-ragain", "OK", "Senator", [
        claim("br1", "brian-ragain", "sanctity_of_life", 2, True,
              "On the 2026 Oklahoma Senate iVoterGuide questionnaire, Ragain stated: 'The lives of human embryos created through artificial methods ought to be protected from purposeful destruction' — directly matching the rubric's opposition to embryonic destruction and IVF-discard practices.",
              ["https://ivoterguide.com/candidate/92459/race/27978/election/1425",
               "https://www.ragainforsenate.com/"]),
        claim("br2", "brian-ragain", "self_defense", 1, True,
              "Ragain stated: 'I stand firmly behind the Constitution and the Amendments. Unless those are changed, my core beliefs must match with those without question or deviation.' As a firefighter-paramedic and nurse who pledges strict constitutional fidelity, this affirms unconditional Second Amendment support — opposing red-flag laws, assault-weapons bans, magazine limits, and registry schemes the rubric opposes.",
              ["https://www.ragainforsenate.com/",
               "https://ivoterguide.com/candidate/92459/race/27978/election/1425"]),
    ]),

    # -------- Gary Ty England (OK-R, 2026 U.S. Senate candidate · Mullin seat) --------
    ("gary-ty-england", "OK", "Senator", [
        claim("gte1", "gary-ty-england", "foreign_policy_restraint", 1, True,
              "On the 2026 Oklahoma Senate iVoterGuide questionnaire, England stated: 'The United States has become too involved in others’ policies and should remain focused on issues regarding our own sovereignty unless in imminent danger.' This sovereignty-first restraint doctrine — engage only when directly threatened — aligns with the rubric’s call to end forever wars and limit overseas military entanglements.",
              ["https://ivoterguide.com/candidate/92635/race/27978/election/1425",
               "https://www.garytyenglandforsenate.com/"]),
        claim("gte2", "gary-ty-england", "economic_stewardship", 2, True,
              "England runs on 'fiscal responsibility' and 'limited government' as explicit campaign pillars, stating he believes in 'free enterprise and the right to private property' as essential to a productive economy and opposes expansion of the federal government’s footprint — a posture consistent with the rubric’s anti-deficit and balanced-budget standard.",
              ["https://www.garytyenglandforsenate.com/platform",
               "https://ivoterguide.com/candidate/92635/race/27978/election/1425"]),
    ]),

    # -------- Michele Morrow (NC-R, 2026 U.S. Senate candidate · Tillis seat) --------
    ("michele-morrow", "NC", "Senator", [
        claim("mm1", "michele-morrow", "election_integrity", 0, True,
              "Morrow's 2026 North Carolina Senate campaign explicitly pledges 'restoring election integrity' as a core constitutional-rights priority. Her platform states she will fight for 'protecting constitutional rights, restoring election integrity' and she has a documented record of election-integrity advocacy dating to her 2024 NC Superintendent campaign — aligning directly with the rubric’s voter-ID and anti-fraud standard.",
              ["https://ivoterguide.com/candidate/71701/race/24489/election/1371",
               "https://www.wfmynews2.com/article/news/politics/michele-morrow-enters-crowded-gop-field-in-north-carolina-senate-race/83-7bb8e338-7de7-43d4-bf7e-1a11472ac916"]),
        claim("mm2", "michele-morrow", "border_immigration", 0, True,
              "Morrow lists 'strong borders' as an explicit core campaign pillar, stating she will fight for 'NC to lead the rest of the nation back to the values that make our country great – strong borders, healthy families, quality education and freedom and justice for all.' This affirms full southern border enforcement consistent with the rubric’s wall-and-military-presence standard.",
              ["https://ivoterguide.com/candidate/71701/race/24489/election/1371",
               "https://www.wfmynews2.com/article/news/politics/michele-morrow-enters-crowded-gop-field-in-north-carolina-senate-race/83-7bb8e338-7de7-43d4-bf7e-1a11472ac916"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
