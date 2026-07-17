#!/usr/bin/env python3
"""Enrichment batch 722: hand-curated claims for 5 NY Republican State Senators.

archetype_curated federal senator/rep buckets fully exhausted; continuing the
state-level pivot. Targets five New York Republican State Senators with 0 claims
(archetype_party_default), taken from the bottom of the alphabet:
  Rob Ortt (SD-62), George Borrello (SD-57), Tom O'Mara (SD-58),
  Patrick M. Gallivan (SD-60), Jim Tedisco (SD-44).

Each claim cites >=1 reliable source and reflects documented voting record /
public positions on the God-First/America-First rubric categories.
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
    # --- Rob Ortt (NY, State Senator SD-62; Senate Republican Minority Leader) ---
    ("rob-ortt", "NY", "State Senator", [
        claim("ro1", "rob-ortt", "self_defense", 1, True,
              "Introduced legislation (2017) that would repeal the NY SAFE Act in every county outside New York City — striking assault-weapon classifications, magazine limits, and the handgun registry imposed by the 2013 law — and created an online petition demanding full repeal, calling the SAFE Act 'unconstitutional' and harmful to law-abiding gun owners.",
              ["https://www.nysenate.gov/newsroom/in-the-news/2017/robert-g-ortt/new-law-would-repeal-safe-act-upstate-ny-everywhere-nyc",
               "https://en.wikipedia.org/wiki/Rob_Ortt"]),
        claim("ro2", "rob-ortt", "sanctity_of_life", 0, True,
              "Voted against the Reproductive Health Act (January 2019), which eliminated criminal penalties for late-term abortions and removed all references to the unborn from New York's penal code — affirming his opposition to unrestricted abortion and his support for legal protections for life from conception.",
              ["https://en.wikipedia.org/wiki/Rob_Ortt",
               "https://ballotpedia.org/Robert_Ortt"]),
    ]),

    # --- George Borrello (NY, State Senator SD-57) ---
    ("george-borrello", "NY", "State Senator", [
        claim("gb1", "george-borrello", "refuse_state_overreach", 0, True,
              "Was a named co-plaintiff in the lawsuit challenging Governor Hochul's DOH Rule 2.13 (isolation and quarantine procedures), which had been adopted administratively without a vote of the Legislature. On July 11, 2022, Judge Ronald Ploetz ruled in favor of the plaintiffs, finding the rule violated constitutional due process — a ruling Borrello called a 'win for all New Yorkers.'",
              ["https://www.nysenate.gov/newsroom/press-releases/2023/george-borrello/statement-senator-george-borrello-and-fellow",
               "https://ballotpedia.org/George_Borrello"]),
        claim("gb2", "george-borrello", "sanctity_of_life", 0, True,
              "Publicly condemned the 2019 Reproductive Health Act as 'radical,' objecting that it eliminated all legal protections for the unborn and allowed abortion through the moment of birth — a position consistent with defending the right to life from conception.",
              ["https://ballotpedia.org/George_Borrello",
               "https://www.nysenate.gov/senators/george-m-borrello/about"]),
    ]),

    # --- Tom O'Mara (NY, State Senator SD-58) ---
    ("tom-omara", "NY", "State Senator", [
        claim("to1", "tom-omara", "self_defense", 1, True,
              "Voted against the NY SAFE Act in January 2013, issuing a statement criticizing the rushed process and warning that the law 'goes too far to infringe upon the Second Amendment rights' of law-abiding citizens — opposing its assault-weapon ban, magazine limit, and registration requirements.",
              ["https://www.nysenate.gov/newsroom/press-releases/2013/thomas-f-omara/omara-criticizes-legislative-process-lack-public-input",
               "https://ballotpedia.org/Thomas_O'Mara"]),
        claim("to2", "tom-omara", "biblical_marriage", 0, True,
              "Voted against the Marriage Equality Act in June 2011, which passed the New York State Senate 33–29 legalizing same-sex marriage — affirming the traditional one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Tom_O%27Mara",
               "https://ballotpedia.org/Thomas_O'Mara"]),
    ]),

    # --- Patrick M. Gallivan (NY, State Senator SD-60) ---
    ("patrick-m-gallivan", "NY", "State Senator", [
        claim("pg1", "patrick-m-gallivan", "self_defense", 1, True,
              "Voted Nay on the NY SAFE Act (S2230, January 2013) — a 43–18 Senate vote — opposing the law's assault-weapon ban, 7-round magazine limit, and expanded firearms registry. Gallivan, a former Erie County Sheriff and retired State Trooper, has consistently defended Second Amendment rights and sportsmen across his district.",
              ["https://justfacts.votesmart.org/candidate/key-votes/127657/patrick-gallivan",
               "https://ballotpedia.org/Patrick_Gallivan"]),
        claim("pg2", "patrick-m-gallivan", "sanctity_of_life", 0, True,
              "Voted against the Reproductive Health Act (January 2019), which passed 38–24, removing all criminal protections for the unborn in New York's penal code and legalizing abortion up to birth — a documented vote consistent with protecting life from conception.",
              ["https://www.nysenate.gov/newsroom/video/patrick-m-gallivan/senator-gallivan-votes-against-reproductive-health-act",
               "https://ballotpedia.org/Patrick_Gallivan"]),
    ]),

    # --- Jim Tedisco (NY, State Senator SD-44) ---
    ("jim-tedisco", "NY", "State Senator", [
        claim("jt1", "jim-tedisco", "self_defense", 1, True,
              "Voted against the NY SAFE Act in January 2013, opposing its assault-weapon ban, magazine limit, and firearms registry. Tedisco also believes that safety or childproof mechanisms do not need to be incorporated into the design of firearms — a position consistent with defending the right to keep and bear arms without burdensome mandates.",
              ["https://en.wikipedia.org/wiki/Jim_Tedisco",
               "https://justfacts.votesmart.org/candidate/key-votes/4401/jim-tedisco"]),
        claim("jt2", "jim-tedisco", "sanctity_of_life", 0, True,
              "Voted against the Reproductive Health Act (January 2019) and has affirmed he opposes abortion except in cases of rape, incest, or when the mother's life is at risk — rejecting unrestricted abortion and declining to accept the political position promoted by the abortion industry's advocacy organizations.",
              ["https://en.wikipedia.org/wiki/Jim_Tedisco",
               "https://justfacts.votesmart.org/candidate/4401/james-tedisco"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
