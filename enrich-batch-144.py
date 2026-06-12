#!/usr/bin/env python3
"""Enrichment batch 144: 5 sitting U.S. House members — Connecticut delegation.

Targets from the evidence_federal / 0-claim bucket, reverse-sorted by state.
VA bucket candidates lacked publishable positions (2026 challengers only);
CT has 5 long-serving sitting members with clear, sourced records.

  Rosa DeLauro   (CT-03, D) — 17-term Ranking Member Appropriations
  Jim Himes      (CT-04, D) — 9-term, fmr Ranking Member Intelligence
  Jahana Hayes   (CT-05, D) — 4th term, fmr National Teacher of the Year
  Joe Courtney   (CT-02, D) — 10-term, Armed Services / submarine focus
  John Larson    (CT-01, D) — 13-term, Caucus Chair emeritus

Sources: en.wikipedia.org, ballotpedia.org, govtrack.us, congress.gov,
         sbaprolife.org, reproductivefreedomforall.org,
         delauro.house.gov, himes.house.gov, hayes.house.gov,
         courtney.house.gov, larson.house.gov
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
    # ---------------- Rosa DeLauro (CT-03, D) ----------------
    ("rosa-delauro", "CT", "Representative", [
        claim("rd1", "rosa-delauro", "sanctity_of_life", 0, False,
              "Voted YES on HR 8296, the Women's Health Protection Act of 2022, which would have codified abortion access as a federal statutory right beyond what Roe v. Wade required and preempted state restrictions — rejecting any recognition of fetal personhood from conception.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8296",
               "https://www.govtrack.us/congress/members/rosa_delauro/400103"]),
        claim("rd2", "rosa-delauro", "self_defense", 1, False,
              "Voted YES on S.2938, the Bipartisan Safer Communities Act (June 24, 2022), which expanded background-check requirements for gun buyers under 21, funded state red-flag (extreme risk protection order) programs, and broadened the definition of a federally licensed dealer — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938"]),
        claim("rd3", "rosa-delauro", "biblical_marriage", 0, False,
              "Voted YES on HR 8404, the Respect for Marriage Act (July 19, 2022 and final passage December 2022), which repealed the Defense of Marriage Act and required federal and state recognition of same-sex civil marriages — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
    ]),

    # ---------------- Jim Himes (CT-04, D) ----------------
    ("jim-himes", "CT", "Representative", [
        claim("jh1", "jim-himes", "sanctity_of_life", 4, False,
              "Carries a 100% score from Reproductive Freedom for All (successor to NARAL Pro-Choice America) and has consistently voted against any restrictions on abortion funding or access throughout his tenure, placing him firmly within the pro-abortion-industry endorsement network.",
              ["https://reproductivefreedomforall.org/lawmaker/jim-himes/",
               "https://en.wikipedia.org/wiki/Jim_Himes"]),
        claim("jh2", "jim-himes", "biblical_marriage", 0, False,
              "Voted YES on HR 8404, the Respect for Marriage Act (July 19, 2022), repealing the Defense of Marriage Act and federally codifying same-sex marriage recognition — rejecting the one-man-one-woman definition.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://ballotpedia.org/Jim_Himes"]),
        claim("jh3", "jim-himes", "self_defense", 1, False,
              "Voted YES on S.2938, the Bipartisan Safer Communities Act (June 24, 2022), funding state red-flag laws and tightening background checks — opposing the rubric's position that red-flag laws and registry expansions violate Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938"]),
    ]),

    # ---------------- Jahana Hayes (CT-05, D) ----------------
    ("jahana-hayes", "CT", "Representative", [
        claim("jha1", "jahana-hayes", "sanctity_of_life", 0, False,
              "Rated 100% by Planned Parenthood Action Fund and voted YES on HR 8296, the Women's Health Protection Act of 2022, which would have created a federal right to abortion beyond Roe and struck down state-level gestational limits — rejecting personhood from conception.",
              ["https://ballotpedia.org/Jahana_Hayes",
               "https://www.congress.gov/bill/117th-congress/house-bill/8296"]),
        claim("jha2", "jahana-hayes", "self_defense", 1, False,
              "Voted YES on S.2938, the Bipartisan Safer Communities Act (June 24, 2022), which funded state extreme-risk protection order (red-flag) programs and expanded background-check requirements for firearm buyers under 21 — directly opposing constitutional-carry and anti-red-flag rubric standards.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://www.govtrack.us/congress/members/jahana_hayes/412763"]),
        claim("jha3", "jahana-hayes", "border_immigration", 1, False,
              "Voted NO on HR 2, the Secure the Border Act of 2023 (May 11, 2023), which would have funded border-wall construction, reinstated remain-in-Mexico protocols, and tightened asylum standards — opposing mandatory deportation and militarized border enforcement.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://www.govtrack.us/congress/members/jahana_hayes/412763"]),
    ]),

    # ---------------- Joe Courtney (CT-02, D) ----------------
    ("joe-courtney", "CT", "Representative", [
        claim("jc1", "joe-courtney", "biblical_marriage", 0, False,
              "Voted YES on HR 8404, the Respect for Marriage Act (July 19, 2022), repealing the Defense of Marriage Act and requiring federal recognition of same-sex marriages — rejecting the one-man-one-woman definition.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://ballotpedia.org/Joe_Courtney"]),
        claim("jc2", "joe-courtney", "sanctity_of_life", 0, False,
              "Rated 100% by Planned Parenthood Action Fund; voted YES on the Women's Health Protection Act of 2022 (HR 8296) to codify abortion access into federal law, and has publicly stated the Supreme Court's Dobbs ruling was 'a stunning step backward' requiring federal statutory reversal.",
              ["https://ballotpedia.org/Joe_Courtney",
               "https://www.congress.gov/bill/117th-congress/house-bill/8296"]),
        claim("jc3", "joe-courtney", "self_defense", 1, False,
              "Voted YES on S.2938, the Bipartisan Safer Communities Act (June 24, 2022), which funded state red-flag (extreme risk protection order) laws and expanded background-check mandates for firearm purchases — opposing the rubric's anti-red-flag and anti-registry positions.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938"]),
    ]),

    # ---------------- John Larson (CT-01, D) ----------------
    ("john-larson", "CT", "Representative", [
        claim("jl1", "john-larson", "sanctity_of_life", 0, False,
              "Has maintained a consistent pro-choice voting record throughout his 25-year House career; voted YES on HR 8296, the Women's Health Protection Act of 2022, to codify abortion access beyond Roe v. Wade and preempt state personhood protections.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8296",
               "https://ballotpedia.org/John_Larson"]),
        claim("jl2", "john-larson", "biblical_marriage", 0, False,
              "Voted YES on HR 8404, the Respect for Marriage Act (July 19, 2022), repealing DOMA and codifying federal recognition of same-sex marriages — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://en.wikipedia.org/wiki/John_Larson_(politician)"]),
        claim("jl3", "john-larson", "self_defense", 1, False,
              "Voted YES on S.2938, the Bipartisan Safer Communities Act (June 24, 2022), which funded state red-flag law programs and expanded background-check requirements for under-21 firearm buyers — opposing the rubric's position against red-flag laws and background-check expansions.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/John_Larson"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
