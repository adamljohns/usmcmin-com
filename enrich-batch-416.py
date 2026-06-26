#!/usr/bin/env python3
"""Enrichment batch 416: evidence_federal U.S. House candidates (0 claims, bottom-alphabet).

Targets: Rebecca Clark (TX-22, R, lost primary), Ty Jensen (UT-04, R, lost convention),
Eric Garcia (CA-22, D, lost primary), Rudy Salas (CA-22, D, withdrew before primary).

Sources: rebeccaclark4congress.com, ballotpedia.org, termlimits.com, giffords.org,
justfacts.votesmart.org, ericgarciaforcongress.com, ivoterguide.com, rudysalas.com.
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
    # ---------------- Rebecca Clark (TX-22, R, lost primary 2026-03-03) ----------------
    ("rebecca-clark-tx-22", "TX", "Representative", [
        claim("rc1", "rebecca-clark-tx-22", "border_immigration", 0, True,
              "Her platform calls to 'properly maintain and modernize our physical and technological defenses while ensuring the consistent enforcement of national immigration laws,' explicitly pairing physical border infrastructure with enforcement — aligning with the rubric's wall-plus-military standard.",
              ["https://rebeccaclark4congress.com/",
               "https://ballotpedia.org/Rebecca_Clark_(Texas)"]),
        claim("rc2", "rebecca-clark-tx-22", "self_defense", 0, True,
              "Explicitly lists defending 'the Constitution, life, the Second Amendment, and our heritage' as a campaign pillar — 'the foundation of freedom, opportunity, and prosperity for Texas and the nation' — reflecting a constitutional-carry, pro-Second-Amendment posture.",
              ["https://rebeccaclark4congress.com/"]),
        claim("rc3", "rebecca-clark-tx-22", "economic_stewardship", 2, True,
              "Advocates zero-based budgeting — 'requiring every agency to account for every dollar' — describing the federal budget as 'lawless' with 'hundreds of unauthorized programs spending billions on autopilot.' Calls for a disciplined anti-deficit approach rooted in her geophysics/data background.",
              ["https://rebeccaclark4congress.com/",
               "https://rebeccaclark4congress.com/experience"]),
    ]),

    # ---------------- Ty Jensen (UT-04, R, lost GOP convention 1.4%) ----------------
    ("ty-jensen", "UT", "Representative", [
        claim("tj1", "ty-jensen", "border_immigration", 1, True,
              "His top campaign priority — stated verbatim in his Ballotpedia Candidate Connection Survey — was 'Passing a new comprehensive take on Kate's Law and also deal with the Immigration Issues.' Kate's Law mandates enhanced criminal penalties for illegal reentry of previously deported felons, directly aligning with mandatory-deportation enforcement standards.",
              ["https://ballotpedia.org/Ty_Jensen"]),
        claim("tj2", "ty-jensen", "self_defense", 0, True,
              "Called for legislation to fund school safety officers and 'at least Concealed Carry for designated teachers that are willing' (verbatim from his Ballotpedia Candidate Connection Survey) — affirming a pro-Second-Amendment, concealed-carry-expansion position consistent with the rubric's constitutional-carry standard.",
              ["https://ballotpedia.org/Ty_Jensen"]),
        claim("tj3", "ty-jensen", "refuse_federal_overreach", 0, True,
              "Signed the U.S. Term Limits pledge to support a constitutional amendment imposing term limits on Congress — a structural check on entrenched federal power and career politicians.",
              ["https://termlimits.com/ty-jensen-pledges-to-support-term-limits-on-congress/",
               "https://ballotpedia.org/Ty_Jensen"]),
    ]),

    # ---------------- Eric Garcia (CA-22, D, lost primary 2026-06-02) ----------------
    ("eric-garcia-ca-22", "CA", "Representative", [
        claim("eg1", "eric-garcia-ca-22", "border_immigration", 0, False,
              "His campaign website calls for 'a pathway to citizenship for the 11 million immigrants living in the United States without legal status,' protection for DREAMers, keeping families together, and streamlining the visa and green-card process — a legalization-first stance directly opposed to the rubric's enforcement-and-wall standard.",
              ["https://www.ericgarciaforcongress.com/issues",
               "https://ballotpedia.org/Eric_Garcia"]),
        claim("eg2", "eric-garcia-ca-22", "self_defense", 1, False,
              "His 2026 voter guide responses support allowing gun violence victims to sue firearms dealers and manufacturers — effectively repealing the PLCAA-style liability shield for the firearms industry — signaling support for expanded gun regulations the rubric opposes.",
              ["https://ivoterguide.com/candidate/48916/race/16202/election/924",
               "https://ballotpedia.org/Eric_Garcia"]),
    ]),

    # ---------------- Rudy Salas (CA-22, D, withdrew before 2026-06-02 primary) ----------------
    ("rudy-salas", "CA", "Representative", [
        claim("rs1", "rudy-salas", "sanctity_of_life", 0, False,
              "Received a 100% rating from Planned Parenthood Affiliates of California across his ten-year Assembly tenure (2012–2022) and campaigned for Congress on the position that 'the government shouldn't interfere in a woman's healthcare decisions' — directly opposing any life-at-conception or personhood standard.",
              ["https://justfacts.votesmart.org/candidate/evaluations/129492/rudy-salas-jr",
               "https://www.rudysalas.com/"]),
        claim("rs2", "rudy-salas", "self_defense", 1, False,
              "Endorsed by Giffords as their 'gun safety champion' for CA-22; his congressional platform calls for 'commonsense gun safety legislation to expand background checks to all gun sales' — supporting the kind of expanded firearm restrictions that the rubric opposes.",
              ["https://giffords.org/candidates/rudy-salas/",
               "https://www.rudysalas.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents wrong-state same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
