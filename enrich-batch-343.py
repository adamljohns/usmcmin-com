#!/usr/bin/env python3
"""Enrichment batch 343: 5 active U.S. Senate candidates with 2-3 existing claims.

Targets (2 MI + 1 NC + 1 NE + 1 MT):
  Mallory McMorrow (MI-D), Mike Duggan Senate (MI-I),
  Roy Cooper (NC-D), Dan Osborn (NE-I), Monica Tranel (MT-D).

Each target receives 2-3 new claims from distinct rubric categories,
spanning self_defense, border_immigration, sanctity_of_life, and
biblical_marriage, drawn from public statements, Ballotpedia, Wikipedia,
VoteSmart, and candidate campaign sites (2024-2026).

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
    # ---------------- Mallory McMorrow (MI-D, MI State Senator / 2026 US Senate) ----------------
    ("mallory-mcmorrow", "MI", "Senate", [
        claim("mm1", "mallory-mcmorrow", "self_defense", 1, False,
              "As chief Senate sponsor of Michigan's Extreme Risk Protection Order (red-flag) Act "
              "(SB 83, signed May 2023), McMorrow directly authored legislation that allows courts "
              "to remove firearms from individuals without criminal conviction and prior to a hearing. "
              "Her 2026 U.S. Senate campaign explicitly proposes taking Michigan's red-flag regime "
              "nationwide — directly opposing the rubric's opposition to red-flag laws.",
              ["https://senatedems.com/mcmorrow/2025/03/06/red-flag-law/",
               "https://michiganadvance.com/2026/02/05/mcmorrows-gun-violence-prevention-plan-would-take-michigans-red-flag-laws-nationwide/"]),
        claim("mm2", "mallory-mcmorrow", "border_immigration", 2, False,
              "McMorrow has called for ICE to 'get out of communities' and demanded a complete overhaul "
              "of the agency, opposing cooperation between local police and federal immigration "
              "enforcement — a de facto sanctuary stance contrary to the rubric's anti-sanctuary standard. "
              "She has backed requiring ICE officers to wear identifying uniforms and masks, and has "
              "called for denying further funding to the agency absent sweeping reform.",
              ["https://michiganadvance.com/2026/01/25/michigans-u-s-senate-candidates-have-disparate-perspectives-on-dealing-with-ice-overreach/",
               "https://www.mcmorrowformichigan.com/positions-track-record"]),
    ]),

    # ---------------- Mike Duggan Senate (MI-I, Detroit mayor / 2026 US Senate) ----------------
    ("mike-duggan-senate", "MI", "Senate", [
        claim("mds1", "mike-duggan-senate", "sanctity_of_life", 0, False,
              "Duggan declared he is '100 percent behind' the Michigan constitutional amendment that "
              "codifies Roe v. Wade-level protections into state law, explicitly supporting abortion "
              "access 'throughout pregnancy' — a categorical rejection of any life-at-conception or "
              "personhood standard.",
              ["https://www.wlns.com/skubick/mike-duggan-discusses-his-political-stances/",
               "https://en.wikipedia.org/wiki/Mike_Duggan"]),
        claim("mds2", "mike-duggan-senate", "biblical_marriage", 0, False,
              "Duggan has consistently identified as a supporter of LGBTQ rights and same-sex marriage, "
              "publicly noting his long-term support for 'bodily autonomy and LGBTQ rights' as core "
              "campaign principles — rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Mike_Duggan",
               "https://michiganadvance.com/2026/02/14/duggans-inconsistency-on-trifecta-raises-alarms-for-dems-i-really-dont-know-who-mike-duggan-is/"]),
    ]),

    # ---------------- Roy Cooper (NC-D, 2026 US Senate Nominee) ----------------
    # Existing claims: sanctity_of_life-0, biblical_marriage-0, self_defense-1
    ("roy-cooper-nc-senate", "NC", "Senator", [
        claim("rc4", "roy-cooper-nc-senate", "sanctity_of_life", 4, False,
              "Roy Cooper was endorsed by Reproductive Freedom for All (successor to NARAL) following "
              "his 2026 North Carolina Senate primary victory, and his campaign touts his record as "
              "governor defending abortion access against legislative restrictions — placing him firmly "
              "in the abortion-industry endorsement network the rubric scores against.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-roy-coopers-victory-in-north-carolina-primary-race-for-u-s-senate/",
               "https://ballotpedia.org/Roy_Cooper"]),
        claim("rc5", "roy-cooper-nc-senate", "border_immigration", 2, False,
              "As North Carolina governor, Cooper vetoed legislation that would have required county "
              "sheriffs to cooperate with ICE detainer requests for inmates believed to be in the "
              "country unlawfully — an anti-anti-sanctuary veto directly contrary to the rubric's "
              "anti-sanctuary standard.",
              ["https://wlos.com/news/local/roy-cooper-files-us-senate-race-north-carolina-seat-democrat-republican-michael-whatley-novemeber-midterm-election-balance-power-president-donald-trump-crime-economy-immigration",
               "https://ballotpedia.org/Roy_Cooper"]),
    ]),

    # ---------------- Dan Osborn (NE-I, 2026 US Senate Candidate) ----------------
    # Existing claims: sanctity_of_life-0, border_immigration-0, self_defense-1
    ("dan-osborn-senate-2026", "NE", "Senate", [
        claim("do4", "dan-osborn-senate-2026", "economic_stewardship", 2, True,
              "Osborn explicitly campaigns on fiscal restraint, stating 'both parties have spent money "
              "they don't have for decades' and pledging to 'cut waste, end corporate welfare, and "
              "refuse to vote for spending we can't afford' — broadly consistent with the rubric's "
              "anti-deficit/balanced-budget standard.",
              ["https://www.osbornforsenate.com/fairnessplan",
               "https://en.wikipedia.org/wiki/Dan_Osborn"]),
        claim("do5", "dan-osborn-senate-2026", "border_immigration", 3, False,
              "While Osborn supports the border wall, he also calls for legalizing non-criminal "
              "long-term undocumented workers and has backed giving undocumented residents Social "
              "Security cards — opposing mandatory E-Verify enforcement and contradicting the "
              "rubric's E-Verify/anti-amnesty standard.",
              ["https://en.wikipedia.org/wiki/Dan_Osborn",
               "https://ballotpedia.org/Dan_Osborn"]),
    ]),

    # ---------------- Monica Tranel (MT-D, 2026 US Senate Candidate) ----------------
    ("monica-tranel-mt-senate", "MT", "Senate", [
        claim("mtr3", "monica-tranel-mt-senate", "border_immigration", 0, False,
              "Tranel has campaigned on making the border 'safer' and addressing fentanyl flows, "
              "but has not called for physical barrier construction or military deployment; her "
              "broader progressive platform opposes aggressive immigration enforcement and aligns "
              "with expanding pathways for undocumented residents — contrary to the rubric's "
              "wall-and-military-at-the-border standard.",
              ["https://ballotpedia.org/Monica_Tranel",
               "https://en.wikipedia.org/wiki/Monica_Tranel"]),
        claim("mtr4", "monica-tranel-mt-senate", "biblical_marriage", 4, False,
              "Tranel's 2022 and 2024 Montana At-Large campaigns were endorsed by national LGBTQ "
              "advocacy networks, and she explicitly supports anti-discrimination protections based "
              "on sexual orientation and gender identity in schools and public accommodations — "
              "the policy promotion of LGBTQ ideology the rubric opposes.",
              ["https://ballotpedia.org/Monica_Tranel",
               "https://www.mtpr.org/tags/monica-tranel"]),
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
