#!/usr/bin/env python3
"""Enrichment batch 339: 5 Virginia state legislators from bottom of evidence_state bucket.

archetype_curated federal senator/representative buckets are fully exhausted;
archetype_party_default federal bucket has no actionable targets. This batch
continues the evidence_state queue from the bottom of the alphabet (VA).

Targets (reverse-alpha top-5):
  Vivian Watts      VA-D, House of Delegates District 14 (Annandale/Fairfax)
  Virgil Thornton Sr VA-D, House of Delegates District 86 (Hampton/York/Poquoson)
  Stella Pekarsky   VA-D, State Senate District 36 (Fairfax)
  Stacey Carroll    VA-D, House of Delegates District 64 (Stafford County)
  Shelly Simonds    VA-D, House of Delegates District 70 (Newport News/Hampton)

Each claim cites >=1 reliable source reflecting 2024-2026 public record/positions.
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
    # ---------- Vivian Watts (VA-D, House of Delegates District 14, Annandale) ----------
    ("vivian-watts", "VA", "House of Delegates", [
        claim("vw1", "vivian-watts", "sanctity_of_life", 0, False,
              "Vivian Watts has served in the Virginia House of Delegates since 1988 and consistently supports abortion access. During the 2024 session she co-sponsored HB 78 — companion to SB 16 — prohibiting law enforcement from subpoenaing menstrual health data stored on third-party apps (a measure aimed at protecting abortion-seekers from prosecution). She voted to prohibit the Board of Medicine from disciplining physicians for performing legal abortion services, rejecting any personhood-from-conception standard. REPRO Rising Virginia, the statewide reproductive-rights lobby, lists her as a key legislative ally.",
              ["https://ballotpedia.org/Vivian_Watts",
               "https://reprorisingva.org/team/delegate-vivian-watts/",
               "https://vadogwood.com/2024/03/13/heres-where-reproductive-rights-bills-stand-in-va-now-that-session-has-ended/"]),
        claim("vw2", "vivian-watts", "self_defense", 1, False,
              "During the 2024 Virginia session, Watts voted to prohibit the public carrying of assault-style weapons in the Commonwealth — a direct restriction on the type of commonly owned semi-automatic firearms the rubric identifies as protected under the Second Amendment. She is identified by the Progressive Voters Guide as a champion of gun violence prevention, consistently supporting legislation restricting firearms in public spaces and expanding background checks.",
              ["https://ballotpedia.org/Vivian_Watts",
               "https://progressivevotersguide.com/virginia/2025/general/vivian-e-watts",
               "https://www.richmondsunlight.com/legislator/vewatts/"]),
    ]),

    # ---------- Virgil Thornton Sr. (VA-D, House of Delegates District 86) ----------
    ("virgil-thornton-sr", "VA", "House of Delegates", [
        claim("vts1", "virgil-thornton-sr", "sanctity_of_life", 0, False,
              "During his successful 2025 campaign for Virginia House District 86, Virgil Thornton Sr. explicitly backed Virginia's in-progress constitutional amendment to protect abortion access and contraception, stating that decisions about pregnancy and contraception 'should be left to women, families, and their doctors.' He cited personal family reasons — daughters of childbearing age — for his commitment to reproductive freedom, rejecting any life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Virgil_Thornton_Sr.",
               "https://virginiaindependentnews.com/elections/meet-the-candidate-virgil-thornton-sr",
               "https://progressivevotersguide.com/virginia/2025/general/virgil-g-thornton-sr"]),
        claim("vts2", "virgil-thornton-sr", "self_defense", 1, False,
              "Gun rights was a key policy dividing line in the 2025 HD-86 race (as reported by the Virginia Mercury), with Thornton running as the progressive Democratic challenger to Republican incumbent A.C. Cordoza; he aligned with the Virginia House Democratic Caucus position supporting gun safety measures over Second Amendment absolutism. He won with 53.4% of the vote and joined a caucus that has passed assault-weapon restrictions, red-flag law enhancements, and Gun Free Zone expansions — all contrary to the rubric's anti-restriction principles.",
              ["https://virginiamercury.com/2025/10/31/education-gun-rights-and-workforce-development-shape-house-district-86-race/",
               "https://ballotpedia.org/Virgil_Thornton_Sr.",
               "https://vahousedems.org/candidates/virgil-thornton-sr/"]),
    ]),

    # ---------- Stella Pekarsky (VA-D, State Senate District 36, Fairfax) ----------
    ("stella-pekarsky", "VA", "State Senate", [
        claim("sp1", "stella-pekarsky", "sanctity_of_life", 0, False,
              "Stella Pekarsky sponsored Virginia's constitutional amendment to recognize Virginians' fundamental right to reproductive freedom — encompassing pre- and post-natal care, contraception, abortion, miscarriage management, and fertility care. She also sponsored legislation prohibiting the extradition of Virginians to other states for abortion services performed legally in Virginia, and a bill prohibiting collection of menstrual health data. Virginia's Choice Tracker rates her explicitly as Pro-Choice.",
              ["https://choicetracker.org/va/people/stella-pekarsky/77201408",
               "https://stellapekarsky.com/issues-stella-pekarsky/",
               "https://ballotpedia.org/Stella_Pekarsky"]),
        claim("sp2", "stella-pekarsky", "self_defense", 1, False,
              "Reducing gun violence is a stated legislative priority for Pekarsky; as part of the January 2025 Fairfax delegation's agenda she co-introduced gun-control legislation alongside abortion and election-reform bills. She votes consistently with the Virginia Senate Democratic caucus on gun restrictions and opposes the constitutional-carry and anti-restriction principles the rubric supports.",
              ["https://www.ffxnow.com/2025/01/09/fairfax-lawmakers-propose-legislation-on-abortion-gun-control-and-election-reform/",
               "https://ballotpedia.org/Stella_Pekarsky",
               "https://legiscan.com/VA/people/stella-pekarsky/id/24983"]),
    ]),

    # ---------- Stacey Carroll (VA-D, House of Delegates District 64, Stafford County) ----------
    ("stacey-carroll", "VA", "House of Delegates", [
        claim("sc1", "stacey-carroll", "sanctity_of_life", 0, False,
              "Stacey Carroll (elected November 2025, sworn January 14, 2026) defeated incumbent Republican Paul Milde III in part on reproductive rights: Milde had voted against Virginia's constitutional amendment to protect abortion access and against a bill protecting contraception access. Carroll campaigned explicitly supporting the constitutional amendment and shared personal reasons for her commitment to reproductive freedom, rejecting any life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Stacey_Carroll",
               "https://virginiaindependentnews.com/elections/2025-house-delegates-district-64-stacey-carroll-paul-milde/",
               "https://staceycarrollforva.com/"]),
        claim("sc2", "stacey-carroll", "self_defense", 1, False,
              "During her 2025 campaign Carroll called it 'a tragedy that gun safety issues remain unresolved,' advocated for 'commonsense solutions to protect kids,' and pledged to push for commonsense gun safety legislation to protect students in schools — actively opposing the constitutional-carry and anti-restriction principles the rubric supports.",
              ["https://virginiaindependentnews.com/elections/2025-house-delegates-district-64-stacey-carroll-paul-milde/",
               "https://ballotpedia.org/Stacey_Carroll",
               "https://vahousedems.org/candidates/stacey-carroll/"]),
    ]),

    # ---------- Shelly Simonds (VA-D, House of Delegates District 70, Newport News) ----------
    ("shelly-simonds", "VA", "House of Delegates", [
        claim("ss1", "shelly-simonds", "sanctity_of_life", 0, False,
              "Shelly Simonds co-sponsored Virginia's constitutional amendment to enshrine abortion rights in the Commonwealth's constitution, voted to establish the right to access FDA-approved contraceptives, and voted to require state health insurance plans to cover all FDA-approved birth control. She publicly stated: 'Access to abortion care is critical life-saving healthcare and is often performed for women experiencing miscarriage or ectopic pregnancies. Access to medical care should not be politicized.' — directly rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Shelly_Simonds",
               "https://simondsfordelegate.com/hd70/",
               "https://progressivevotersguide.com/virginia/2025/general/shelly-simonds"]),
        claim("ss2", "shelly-simonds", "self_defense", 1, False,
              "Simonds co-sponsored legislation establishing Gun Free Zones at Capitol Square and Virginia's public institutions of higher education, and voted to prohibit the manufacture, sale, or possession of assault-style weapons in Virginia — directly opposing the constitutional-carry and anti-assault-weapon-ban principles the rubric supports.",
              ["https://ballotpedia.org/Shelly_Simonds",
               "https://simondsfordelegate.com/hd70/",
               "https://www.vpap.org/legislators/106052-shelly-simonds/"]),
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
