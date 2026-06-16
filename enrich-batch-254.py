#!/usr/bin/env python3
"""Enrichment batch 254: 4 state executives/officials from bottom-of-alphabet states.

archetype_curated federal bucket is now exhausted (0 remaining); pivots to
evidence-backing high-profile state executives and officials from WV / WY / VA.

Targets: Patrick Morrisey (WV Gov), Mark Gordon (WY Gov),
         Elizabeth Guzman (VA Delegate + 2026 congressional candidate),
         Chuck Gray (WY Secretary of State).
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
    # ---------------- Patrick Morrisey (WV, Governor) ----------------
    ("patrick-morrisey", "WV", "Governor", [
        claim("pm1", "patrick-morrisey", "sanctity_of_life", 0, True,
              "As West Virginia Attorney General (2013–2019), Morrisey defended WV's abortion restrictions in court; as Governor from January 2025, he publicly celebrated the 4th Circuit Court of Appeals upholding WV's near-total abortion ban and joined a 12-state coalition filing an amicus brief supporting North Carolina's 20-week limit — affirming a career-long commitment to protecting life from conception.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-releases-statement-pro-life-victory-4th-circuit-court-appeals",
               "https://en.wikipedia.org/wiki/Patrick_Morrisey"]),
        claim("pm2", "patrick-morrisey", "self_defense", 1, True,
              "As Governor, signed three Second Amendment protection bills in 2025: HB 2067 (shielding firearm manufacturers from liability for criminal misuse of their products), HB 3342 (barring state-contracted banks from discriminating against gun businesses), and SB 270 (prohibiting suspension of firearm rights during declared emergencies or disaster responses).",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-legislation-defending-second-amendment-rights",
               "https://en.wikipedia.org/wiki/Patrick_Morrisey"]),
        claim("pm3", "patrick-morrisey", "christian_liberty", 0, True,
              "As Governor, backed a state lawsuit against the West Virginia Board of Education in 2025 for its failure to uphold religious liberty in public schools — defending free exercise of religion against government suppression.",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-backs-lawsuit-against-state-board-education-over-failure-uphold",
               "https://en.wikipedia.org/wiki/Patrick_Morrisey"]),
    ]),

    # ---------------- Mark Gordon (WY, Governor) ----------------
    ("mark-gordon", "WY", "Governor", [
        claim("mg1", "mark-gordon", "family_child_sovereignty", 0, True,
              "Signed legislation in 2025 establishing Wyoming's first universal school-choice program, calling it 'a remarkable achievement for Wyoming' — empowering parents to redirect education funding to schools and curricula of their choosing outside the public system.",
              ["https://en.wikipedia.org/wiki/Governorship_of_Mark_Gordon",
               "https://en.wikipedia.org/wiki/Mark_Gordon"]),
        claim("mg2", "mark-gordon", "biblical_marriage", 2, True,
              "Signed Wyoming law banning puberty blockers, cross-sex hormones, and surgical interventions for minors who identify as transgender — protecting children from irreversible medical transition procedures and rejecting transgender ideology in state policy.",
              ["https://en.wikipedia.org/wiki/Mark_Gordon",
               "https://ballotpedia.org/Mark_Gordon_(Wyoming)"]),
        claim("mg3", "mark-gordon", "self_defense", 0, True,
              "Signed legislation in 2021 extending Wyoming's constitutional (permitless) carry to non-resident U.S. citizens, reinforcing Wyoming as one of the most permissive Second Amendment states and affirming that gun owners from any state can exercise their rights there.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Wyoming",
               "https://ballotpedia.org/Mark_Gordon_(Wyoming)"]),
    ]),

    # ---------------- Elizabeth Guzman (VA, House of Delegates) ----------------
    ("elizabeth-guzman", "VA", "Delegates", [
        claim("eg1", "elizabeth-guzman", "sanctity_of_life", 0, False,
              "Her explicit policy priorities include 'reproductive freedom'; she has supported abortion access legislation throughout her tenure as a Virginia Delegate — rejecting any standard of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Elizabeth_Guzm%C3%A1n",
               "https://ballotpedia.org/Elizabeth_Guzman"]),
        claim("eg2", "elizabeth-guzman", "self_defense", 1, False,
              "Her explicit policy priorities include 'common-sense gun safety reform' — a platform for firearm restrictions that opposes the rubric's defense of unrestricted Second Amendment rights including protections against red-flag laws and assault-weapons bans.",
              ["https://en.wikipedia.org/wiki/Elizabeth_Guzm%C3%A1n",
               "https://ballotpedia.org/Elizabeth_Guzman"]),
        claim("eg3", "elizabeth-guzman", "biblical_marriage", 4, False,
              "Her explicit policy priorities include 'strengthening LGBTQ+ rights' in public policy and law — actively promoting LGBTQ ideology in schools and public life, which the rubric identifies as contrary to a biblical definition of marriage and family.",
              ["https://en.wikipedia.org/wiki/Elizabeth_Guzm%C3%A1n",
               "https://ballotpedia.org/Elizabeth_Guzman"]),
    ]),

    # ---------------- Chuck Gray (WY, Secretary of State) ----------------
    ("chuck-gray", "WY", "Secretary", [
        claim("cg1", "chuck-gray", "election_integrity", 0, True,
              "As a Wyoming state representative, was the lead sponsor of Wyoming's voter ID law (signed into law 2021); as Secretary of State from 2023, advocated for proof-of-citizenship requirements for voter registration, stating he wanted Wyoming to lead 'in the election integrity space' — directly aligned with the rubric's voter-ID standard.",
              ["https://en.wikipedia.org/wiki/Chuck_Gray_(Wyoming_politician)",
               "https://ballotpedia.org/Chuck_Gray_(Wyoming)"]),
        claim("cg2", "chuck-gray", "election_integrity", 2, True,
              "As Secretary of State, publicly advocated for eliminating ballot drop boxes and making ballot harvesting a felony — opposing mass-mail-in and unsecured voting practices the rubric flags as integrity risks; also launched a formal 2024 investigation into ActBlue Wyoming over money-laundering and identity-theft allegations in election finance.",
              ["https://ballotpedia.org/Chuck_Gray_(Wyoming)",
               "https://sos.wyo.gov/Media/2024/SoS_Release_2024-07-30.pdf"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
