#!/usr/bin/env python3
"""Enrichment batch 192: hand-curated claims for 5 U.S. House Representatives.

Targets (bottom-of-alphabet protocol, archetype_party_default, 0 claims):
  Dwight Evans (PA-D), Janelle Bynum (OR-D), Shontel Brown (OH-D),
  Marcy Kaptur (OH-D), Joyce Beatty (OH-D).

Sources: govtrack.us, sbaprolife.org, ballotpedia.org, official house.gov
press releases, opb.org, catholicvote.org, reproductivefreedomforall.org.

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
    # ---------------- Dwight Evans (PA-D, US Representative) ----------------
    ("dwight-evans", "PA", "Representative", [
        claim("de1", "dwight-evans", "sanctity_of_life", 4, False,
              "Carries a 100% lifetime pro-choice rating from Reproductive Freedom for All (formerly NARAL), placing him fully inside the abortion-industry endorsement and funding network that the rubric requires candidates to avoid.",
              ["https://reproductivefreedomforall.org/lawmaker/dwight-evans/",
               "https://ballotpedia.org/Dwight_Evans"]),
        claim("de2", "dwight-evans", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (H.R. 8404, Dec. 2022), enshrining federal recognition of same-sex unions and repealing the Defense of Marriage Act's one-man-one-woman definition.",
              ["https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://ballotpedia.org/Dwight_Evans"]),
        claim("de3", "dwight-evans", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022) — the first major federal gun-restriction law in nearly 30 years — which expanded background checks, closed the boyfriend loophole, and imposed new firearm restrictions; Evans publicized the vote as a signature accomplishment.",
              ["https://evans.house.gov/media-center/press-releases/evans-votes-landmark-gun-safety-bill-save-lives",
               "https://www.govtrack.us/congress/votes/117-2022/h299"]),
    ]),

    # ---------------- Janelle Bynum (OR-D, US Representative) ----------------
    ("janelle-bynum", "OR", "Representative", [
        claim("jby1", "janelle-bynum", "sanctity_of_life", 0, False,
              "Made restoring nationwide abortion access one of her top three congressional priorities; stated that 'the right to choose if and when to start a family should be between a woman and her doctor — not politicians,' explicitly rejecting any life-at-conception personhood standard.",
              ["https://www.opb.org/article/2024/10/18/janelle-bynum-democrat-oregon-5th-congressional-district/",
               "https://ballotpedia.org/Janelle_Bynum"]),
        claim("jby2", "janelle-bynum", "self_defense", 1, False,
              "Supports stricter federal gun laws and built her legislative record in the Oregon statehouse around gun-violence prevention; pledged in Congress to enact the full Democratic gun-control agenda including assault-weapons restrictions.",
              ["https://justfacts.votesmart.org/candidate/key-votes/168102/janelle-bynum/37/guns",
               "https://www.koin.com/news/politics/janelle-bynum-on-running-for-oregon-5th-district-top-issues-whats-going-right/"]),
    ]),

    # ---------------- Shontel Brown (OH-D, US Representative) ----------------
    ("shontel-brown", "OH", "Representative", [
        claim("sb1", "shontel-brown", "self_defense", 1, False,
              "Cosponsored the Assault Weapons Ban of 2022 to ban the sale of assault weapons and large-capacity magazines, and introduced legislation tracking implementation of the Bipartisan Safer Communities Act — a consistent record of supporting federal firearm restrictions.",
              ["https://shontelbrown.house.gov/issues/criminal-justice-reform",
               "https://ballotpedia.org/Shontel_Brown"]),
        claim("sb2", "shontel-brown", "sanctity_of_life", 0, False,
              "Cosponsored the EACH Woman Act (mandating federal health insurance coverage of abortion) and serves on the House Pro-Choice Caucus; voted against the Born-Alive Abortion Survivors Protection Act and stated publicly that 'Abortion is healthcare' — rejecting any life-at-conception or personhood standard.",
              ["https://sbaprolife.org/representative/shontel-brown",
               "https://shontelbrown.house.gov/issues/reproductive-rights"]),
    ]),

    # ---------------- Marcy Kaptur (OH-D, US Representative) ----------------
    ("marcy-kaptur", "OH", "Representative", [
        claim("mk1", "marcy-kaptur", "sanctity_of_life", 0, False,
              "Voted against the Born-Alive Abortion Survivors Protection Act (Jan. 2023), opposing federal medical-care requirements for infants who survive abortion procedures; SBA Pro-Life America documents her as consistently voting against protections for the unborn and for children born alive after failed abortions.",
              ["https://sbaprolife.org/representative/marcy-kaptur",
               "https://www.govtrack.us/congress/members/marcy_kaptur/400211"]),
        claim("mk2", "marcy-kaptur", "biblical_marriage", 0, False,
              "Voted YES on the Respect for Marriage Act (2022), codifying federal recognition of same-sex unions — a vote CatholicVote.org flagged, noting she was among the Catholic House members who voted to enshrine same-sex marriage in federal law over the explicit objection of the U.S. Conference of Catholic Bishops.",
              ["https://catholicvote.org/here-are-the-catholic-house-members-who-voted-to-codify-same-sex-marriage/",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
    ]),

    # ---------------- Joyce Beatty (OH-D, US Representative) ----------------
    ("joyce-beatty", "OH", "Representative", [
        claim("jbe1", "joyce-beatty", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (Dec. 2022), repealing the federal Defense of Marriage Act and codifying same-sex unions in federal law; Beatty's own press release declared she voted 'to protect marriage equality amid right-wing threats.'",
              ["https://beatty.house.gov/media-center/press-releases/rep-beatty-votes-to-protect-marriage-equality-amid-right-wing-threats",
               "https://www.govtrack.us/congress/votes/117-2022/h513"]),
        claim("jbe2", "joyce-beatty", "self_defense", 1, False,
              "Publicly called for expanded background checks and a federal assault weapons ban; as Congressional Black Caucus Chair she was a key negotiator in passing the 2022 House gun-safety package that included assault-weapons ban legislation.",
              ["https://beatty.house.gov/media-center/in-the-news/central-ohio-congresswoman-and-dayton-native-joyce-beatty-calls-for-expanded-background-checks-assault-weapons-ban",
               "https://www.nbc4i.com/news/central-ohio-congresswoman-and-dayton-native-joyce-beatty-calls-for-expanded-background-checks-assault-weapons-ban/"]),
        claim("jbe3", "joyce-beatty", "sanctity_of_life", 0, False,
              "SBA Pro-Life America documents Beatty as consistently voting against protections for the unborn and for children born alive after failed abortions throughout her congressional career.",
              ["https://sbaprolife.org/representative/joyce-beatty",
               "https://ballotpedia.org/Joyce_Beatty"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
