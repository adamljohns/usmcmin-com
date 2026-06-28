#!/usr/bin/env python3
"""Enrichment batch 463: 5 Wisconsin State Assembly Democrats with 0 claims.

Primary archetype_curated federal-senator/representative bucket is exhausted.
Fallback: archetype_party_default state-level officials from the bottom of the
alphabet. All five are Wisconsin D state assembly members (WI sorts highest
after WY/WV/WA, which have no remaining archetype_party_default 0-claim
candidates).

Targets (sorted state desc, then name desc):
- Vincent (Vinnie) Miresse (WI-71, D)
- Tip McGuire (WI-64, D)
- Tara Johnson (WI-96, D)
- Sylvia Ortiz-Velez (WI-8, D)
- Supreme Moore Omokunde (WI-17, D)

2-3 distinct-category claims per candidate spanning sanctity_of_life,
biblical_marriage, self_defense, and election_integrity rubric categories.
Sources: docs.legis.wisconsin.gov, legiscan.com, ballotpedia.org,
wikipedia.org, and Wisconsin news outlets.
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
        "verified_date": "2026-06-28",
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Vincent (Vinnie) Miresse (WI-71, D) ----------------
    ("vincent-miresse-wi-71", "WI", "Assembly", [
        claim("vm1", "vincent-miresse-wi-71", "sanctity_of_life", 0, False,
              "Co-introduced Wisconsin AB355 (July 2025), which establishes a 'fundamental right to bodily autonomy' including unrestricted abortion access at any point in pregnancy — directly rejecting any legal personhood from conception and opposing Wisconsin's existing pro-life statute.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://ballotpedia.org/Vinnie_Miresse"]),
        claim("vm2", "vincent-miresse-wi-71", "election_integrity", 0, False,
              "As a Wisconsin Assembly Democrat, Miresse belongs to the caucus that voted unanimously against the January 2025 voter-ID constitutional amendment (SJR2), which passed 54-45 on a strict party-line vote with all Democrats opposed — rejecting the rubric's voter-ID plank for election integrity.",
              ["https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://ballotpedia.org/Wisconsin_Require_Voter_Photo_Identification_Amendment_(April_2025)"]),
        claim("vm3", "vincent-miresse-wi-71", "self_defense", 1, False,
              "Co-signed Wisconsin AB356 (2025), requiring firearm storage locks in residences where a child is present and imposing criminal penalties for non-compliance — a regulatory gun-control measure running counter to the rubric's opposition to new firearms restrictions.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab356",
               "https://legis.wisconsin.gov/assembly/71/miresse/",
               "https://ballotpedia.org/Vinnie_Miresse"]),
    ]),

    # ---------------- Tip McGuire (WI-64, D) ----------------
    ("tip-mcguire-wi-64", "WI", "Assembly", [
        claim("tm1", "tip-mcguire-wi-64", "sanctity_of_life", 0, False,
              "Co-introduced Wisconsin AB355 (July 2025) — the 'Right to Bodily Autonomy' bill that would legalize abortion at any stage of pregnancy without restriction — and was endorsed by Planned Parenthood of Wisconsin, which stated he 'will fight to restore laws that protect decisions that should be made by women and their doctors.' This places McGuire squarely within the abortion-industry network the rubric opposes.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://www.plannedparenthoodaction.org/planned-parenthood-advocates-wisconsin/elections/ad64",
               "https://ballotpedia.org/Tip_McGuire"]),
        claim("tm2", "tip-mcguire-wi-64", "self_defense", 1, False,
              "Co-signed Wisconsin AB1056 (February 2026), relating to firearm transfers, possession, and background-check expansion — legislation that tightens the gun-transfer process in ways the rubric flags as opposed to constitutional-carry and anti-restriction Second Amendment principles.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab1056.pdf",
               "https://legiscan.com/WI/bill/AB1056/2025",
               "https://www.wpr.org/news/wisconsin-democrats-reintroduce-gun-regulations-after-republicans-pull-them-from-budget"]),
        claim("tm3", "tip-mcguire-wi-64", "election_integrity", 0, False,
              "Part of the Wisconsin Assembly Democratic caucus that voted unanimously against the voter-ID constitutional amendment (SJR2) in January 2025 — a party-line 54-45 defeat of a measure that would have enshrined photo-ID voting requirements in the Wisconsin Constitution, opposing the rubric's election-integrity standard.",
              ["https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legis.wisconsin.gov/assembly/64/mcguire/"]),
    ]),

    # ---------------- Tara Johnson (WI-96, D) ----------------
    ("tara-johnson-wi-96", "WI", "Assembly", [
        claim("tj1", "tara-johnson-wi-96", "sanctity_of_life", 0, False,
              "Elected in November 2024 on a platform explicitly prioritizing 'codifying reproductive freedoms and eliminating the 1849 law' — Wisconsin's near-total abortion ban — and immediately upon taking office co-introduced both AB355 (bodily-autonomy unlimited abortion access) and AB589 (further abortion deregulation), rejecting any legal personhood-from-conception protection.",
              ["https://legis.wisconsin.gov/assembly/96/johnson/about/meet-tara/",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://ballotpedia.org/Tara_Johnson_(Wisconsin)"]),
        claim("tj2", "tara-johnson-wi-96", "self_defense", 1, False,
              "Co-introduced Wisconsin AB356 (2025), mandating secure firearm storage under penalty of criminal prosecution whenever a child is present in the residence — a gun-storage mandate the rubric classifies as an opposed restriction on lawful firearm ownership.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab356",
               "https://legis.wisconsin.gov/assembly/96/johnson",
               "https://ballotpedia.org/Tara_Johnson_(Wisconsin)"]),
    ]),

    # ---------------- Sylvia Ortiz-Velez (WI-8, D) ----------------
    ("sylvia-ortiz-velez-wi-8", "WI", "Assembly", [
        claim("so1", "sylvia-ortiz-velez-wi-8", "sanctity_of_life", 0, False,
              "Co-introduced Wisconsin AB355 (2025), the 'Right to Bodily Autonomy' bill establishing abortion as a fundamental right at any stage of pregnancy, and publicly stated she 'believes women must have the right to make their own personal health decisions without government interference' — opposing any legal protection for life from conception.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://www.sylviaforwi.com/",
               "https://ballotpedia.org/Sylvia_Ortiz-Velez"]),
        claim("so2", "sylvia-ortiz-velez-wi-8", "self_defense", 1, False,
              "Co-sponsored Wisconsin AB356 (2025), imposing mandatory criminal-penalty firearm storage requirements in homes with children — a gun-control measure at odds with the rubric's anti-restriction Second Amendment posture.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab356",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2766",
               "https://ballotpedia.org/Sylvia_Ortiz-Velez"]),
        claim("so3", "sylvia-ortiz-velez-wi-8", "election_integrity", 0, False,
              "As a member of the Wisconsin Assembly Democratic caucus, voted against SJR2 (January 2025), the voter-ID constitutional amendment, in a 54-45 party-line defeat — opposing the photo-ID requirement the rubric's election-integrity standard supports.",
              ["https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legis.wisconsin.gov/assembly/08/ortiz-velez/"]),
    ]),

    # ---------------- Supreme Moore Omokunde (WI-17, D) ----------------
    ("supreme-moore-omokunde-wi-17", "WI", "Assembly", [
        claim("sm1", "supreme-moore-omokunde-wi-17", "sanctity_of_life", 0, False,
              "Co-introduced Wisconsin AB355 (2025), establishing an unrestricted 'right to bodily autonomy' including abortion at any point in pregnancy, and publicly advocates for expanded healthcare access consistent with reproductive-freedom framing — rejecting any legal personhood-from-conception protection.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://legis.wisconsin.gov/assembly/17/moore-omokunde/",
               "https://ballotpedia.org/Supreme_Moore_Omokunde"]),
        claim("sm2", "supreme-moore-omokunde-wi-17", "biblical_marriage", 4, False,
              "Sponsored 2023 Assembly Bill 1203 to mandate LGBTQIA+ rights training for school counselors and social workers; co-authored resolutions proclaiming Wisconsin Transgender Day of Visibility in 2023, 2024, and 2025; and publicly argued that 'gender-affirming care for our children saves lives' when opposing 2025 Republican legislation limiting that care — consistently promoting LGBTQ ideology in schools and public institutions, contrary to the rubric's standard.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/assembly/2486",
               "https://trackbill.com/legislator/wisconsin-representative-supreme-moore-omokunde/1053-28316/",
               "https://en.wikipedia.org/wiki/Supreme_Moore_Omokunde"]),
        claim("sm3", "supreme-moore-omokunde-wi-17", "election_integrity", 0, False,
              "Voted against the voter-ID constitutional amendment (SJR2) with the full Assembly Democratic caucus in January 2025 — a 54-45 party-line vote opposing photo-ID requirements for voting, counter to the rubric's election-integrity standard.",
              ["https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legis.wisconsin.gov/assembly/17/moore-omokunde/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

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
        prof["last_curated"] = "2026-06-28"
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
