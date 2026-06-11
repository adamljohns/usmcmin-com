#!/usr/bin/env python3
"""Enrichment batch 143: 5 evidence_federal U.S. House members (bottom-of-alphabet states).

Targets from the evidence_federal / 0-claim bucket, reverse-sorted by state:
  Randy Feenstra  (IA-04, R) — lame duck, lost 2026 IA Gov primary
  Jesus "Chuy" Garcia (IL-04, D) — retiring member
  Jesse Watts     (NV-02, R) — 2026 primary candidate, former Eureka Co. Sheriff
  Nikema Williams (GA-05, D) — sitting member
  Lucy McBath     (GA-07, D) — sitting member

Sources: feenstra.house.gov, govtrack.us, congress.gov, votesmart.org,
         thenevadaindependent.com, thecentersquare.com, en.wikipedia.org,
         ballotpedia.org
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
    # ---------------- Randy Feenstra (IA-04, R) ----------------
    ("randy-feenstra", "IA", "Representative", [
        claim("rf1", "randy-feenstra", "sanctity_of_life", 0, True,
              "Voted YES on HR 26, the Born-Alive Abortion Survivors Protection Act (Jan 11, 2023), which requires immediate medical care for infants who survive abortion procedures — affirming the sanctity of life after birth.",
              ["https://feenstra.house.gov/media/press-releases/feenstra-votes-provide-babies-who-survive-botched-abortions-immediate-high",
               "https://www.govtrack.us/congress/votes/118-2023/h29"]),
        claim("rf2", "randy-feenstra", "border_immigration", 0, True,
              "Voted YES on HR 2, the Secure the Border Act of 2023, specifically to fund completion of border-wall construction, maintain Title 42, and fully staff Border Patrol — matching the rubric's wall-plus-military standard.",
              ["https://feenstra.house.gov/media/press-releases/feenstra-votes-secure-border-finish-construction-border-wall",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
        claim("rf3", "randy-feenstra", "self_defense", 1, True,
              "Voted NO on the Bipartisan Safer Communities Act (S.2938, June 2022) citing constitutional concerns with its expanded background-check and red-flag provisions; introduced the PROTECT the Second Amendment Act to bar landlords from restricting tenants' firearm rights.",
              ["https://feenstra.house.gov/media/press-releases/feenstra-issues-statement-after-voting-against-overreaching-gun-control",
               "https://www.nraila.org/articles/20250422/rep-feenstra-reintroduces-legislation-to-second-amendment-rights-of-tenants"]),
    ]),

    # ---------------- Jesus "Chuy" Garcia (IL-04, D) ----------------
    ("jesus-garcia", "IL", "Representative", [
        claim("jg1", "jesus-garcia", "border_immigration", 0, False,
              "Publicly opposed HR 2, the Secure the Border Act of 2023, calling it the 'child deportation act' and declaring that 'seeking asylum is a human right because we are a nation of immigrants' — rejecting border-wall completion and enhanced enforcement.",
              ["https://justfacts.votesmart.org/public-statement/1649719/secure-the-border-act-of-2023",
               "https://www.govtrack.us/congress/members/jesus_garcia/412774"]),
        claim("jg2", "jesus-garcia", "sanctity_of_life", 0, False,
              "Voted NAY on HR 26, the Born-Alive Abortion Survivors Protection Act (Jan 11, 2023), in line with the House Democratic caucus majority (220–210 final); rejects legal recognition of personhood from conception.",
              ["https://www.govtrack.us/congress/votes/118-2023/h29",
               "https://ballotpedia.org/Jesus_Garcia"]),
        claim("jg3", "jesus-garcia", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S.2938, June 2022), a gun-control package that expanded background checks, added red-flag-law incentives, and tightened dealer licensing — opposing the rubric's call to block new firearms restrictions.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://www.govtrack.us/congress/members/jesus_garcia/412774"]),
    ]),

    # ---------------- Jesse Watts (NV-02, R) ----------------
    ("jesse-watts", "NV", "Representative", [
        claim("jw1", "jesse-watts", "self_defense", 1, True,
              "As Eureka County Sheriff, wrote a public letter to Governor Steve Sisolak pledging to resist Nevada's red-flag law (AB291), stating he would fight the legislation 'until there is no fight left in me' — directly opposing red-flag confiscation orders.",
              ["https://thenevadaindependent.com/article/eureka-sheriff-writes-letter-to-sisolak-says-hell-resist-new-red-flag-gun-law-until-there-is-no-fight-left-in-me"]),
        claim("jw2", "jesse-watts", "border_immigration", 0, True,
              "Signed a letter with Nevada rural-county sheriffs urging border-wall construction and adoption of Trump-era border policies, blaming Biden's open-border approach for increased criminal activity from illegal immigration.",
              ["https://www.thecentersquare.com/nevada/nevada-sheriffs-express-second-amendment-sanctuary-sentiment-non-compliance-with-gun-registration-law/article_b6c50eee-49ac-11e9-abfd-d39cec23c07b.html",
               "https://www.kunr.org/local-stories/2026-03-25/meet-jesse-watts-republican-candidate-for-nevadas-cd2"]),
    ]),

    # ---------------- Nikema Williams (GA-05, D) ----------------
    ("nikema-williams", "GA", "Representative", [
        claim("nw1", "nikema-williams", "self_defense", 1, False,
              "Cosponsored HR 1361, the Safer Neighborhoods Gun Buyback Act of 2023, which would establish a federal voluntary gun-buyback program — a measure the rubric's self-defense standard opposes.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/1361/cosponsors",
               "https://www.govtrack.us/congress/members/nikema_williams/456811"]),
        claim("nw2", "nikema-williams", "sanctity_of_life", 0, False,
              "Voted NAY on HR 26, the Born-Alive Abortion Survivors Protection Act (Jan 11, 2023), consistent with her pro-choice record and party-line Democratic vote; does not recognize personhood from conception.",
              ["https://www.govtrack.us/congress/votes/118-2023/h29",
               "https://ballotpedia.org/Nikema_Williams"]),
    ]),

    # ---------------- Lucy McBath (GA-07, D) ----------------
    ("lucy-mcbath", "GA", "Representative", [
        claim("lm1", "lucy-mcbath", "self_defense", 1, False,
              "Served as a national spokeswoman for Moms Demand Action for Gun Sense in America and Everytown for Gun Safety before running for Congress; explicitly supports red-flag laws, universal background checks, and assault-weapons bans — the gun-control agenda the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Lucy_McBath",
               "https://ballotpedia.org/Lucy_McBath"]),
        claim("lm2", "lucy-mcbath", "sanctity_of_life", 0, False,
              "Publicly states support for abortion rights and condemned the Dobbs v. Jackson ruling, saying 'without Roe, all reproductive care is on the line' — rejecting any recognition of life from conception.",
              ["https://justfacts.votesmart.org/candidate/key-votes/178538/lucy-mcbath/2/abortion",
               "https://en.wikipedia.org/wiki/Lucy_McBath"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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
