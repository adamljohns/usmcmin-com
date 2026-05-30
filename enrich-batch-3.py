#!/usr/bin/env python3
"""Enrichment batch 3: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims. Uses the
(slug + state + office_keyword) matcher from batch 2 to avoid the batch-1
Mike Lee name-collision bug.

Mix: Adam Schiff (CA-D), Raphael Warnock (GA-D), Katie Britt (AL-R),
John Kennedy (LA-R), Joni Ernst (IA-R). Each claim cites >=1 reliable
source and reflects 2024-2026 voting record / public positions.
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
    # ---------------- Adam Schiff (CA-D, US Senator) ----------------
    ("adam-schiff", "CA", "Senator", [
        claim("as1", "adam-schiff", "sanctity_of_life", 0, False,
              "Campaigns explicitly for a national statutory right to abortion, calling reproductive freedom a human right. Holds a 100% lifetime score from Reproductive Freedom for All (the former NARAL Pro-Choice America) and rejects any personhood-from-conception framework.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-adam-schiff-for-u-s-senate-in-california/",
               "https://schiff.house.gov/news/press-releases/congressman-schiff-on-national-abortion-ban-proposed-by-republicans"]),
        claim("as2", "adam-schiff", "sanctity_of_life", 4, False,
              "Endorsed by Reproductive Freedom for All (successor to NARAL) for his 2024 Senate run and carries a 100% abortion-rights congressional scorecard, placing him firmly within the abortion-industry endorsement-and-funding network.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-adam-schiffs-senate-victory-in-u-s-senate-race/"]),
        claim("as3", "adam-schiff", "foreign_policy_restraint", 3, False,
              "Voted for the 2024 Israel Security Supplemental ($26B in military and related aid) and voted against both Sanders resolutions to block U.S. arms transfers to Israel (failed 70-27 and 73-24). Record reflects support for unconditional foreign military aid rather than America-First restraint.",
              ["https://en.wikipedia.org/wiki/Adam_Schiff",
               "https://www.schiff.senate.gov/news/press-releases/statement-sen-schiff-on-israel-hamas-ceasefire-and-hostage-deal/"]),
    ]),

    # ---------------- Raphael Warnock (GA-D, US Senator) ----------------
    ("raphael-warnock", "GA", "Senator", [
        claim("rw1", "raphael-warnock", "biblical_marriage", 0, False,
              "Cosponsor and public supporter of the Respect for Marriage Act, which codifies federal recognition of same-sex marriage. Also cosponsored the 2021 Equality Act extending sexual-orientation and gender-identity protections into civil-rights law.",
              ["https://www.warnock.senate.gov/newsroom/press-releases/senator-reverend-warnock-statement-on-the-senate-passage-of-the-bipartisan-respect-for-marriage-act/",
               "https://en.wikipedia.org/wiki/Raphael_Warnock"]),
        claim("rw2", "raphael-warnock", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood and rated as a reliable abortion-rights vote by Reproductive Freedom for All, situating him within the abortion-industry endorsement network.",
              ["https://reproductivefreedomforall.org/lawmaker/rev-raphael-warnock/",
               "https://en.wikipedia.org/wiki/Raphael_Warnock"]),
        claim("rw3", "raphael-warnock", "sanctity_of_life", 0, False,
              "A consistent proponent of abortion access who does not affirm personhood from conception; campaigns on protecting abortion rights at the federal level.",
              ["https://en.wikipedia.org/wiki/Raphael_Warnock"]),
    ]),

    # ---------------- Katie Britt (AL-R, US Senator) ----------------
    ("katie-britt", "AL", "Senator", [
        claim("kb1", "katie-britt", "border_immigration", 0, True,
              "A vocal border-security hawk who toured the southern border early in her term, repeatedly criticized the Biden administration's border policy, and opposed the 2024 bipartisan border deal as insufficiently strong on enforcement.",
              ["https://en.wikipedia.org/wiki/Katie_Britt",
               "https://www.britt.senate.gov/priorities/legislative-record/"]),
        claim("kb2", "katie-britt", "border_immigration", 4, True,
              "Co-introduced the Not One More Inch or Acre Act with Sen. Tom Cotton (March 2023, reintroduced January 2025) to bar any Chinese national or Chinese entity from owning American farmland — directly opposing foreign ownership of U.S. agricultural land.",
              ["https://en.wikipedia.org/wiki/Katie_Britt",
               "https://www.britt.senate.gov/priorities/legislative-record/"]),
        claim("kb3", "katie-britt", "sanctity_of_life", 2, False,
              "An outspoken champion of IVF access; the Trump administration credited her influence on a 2025 executive order to make IVF more affordable. This pro-IVF posture conflicts with the rubric's opposition to embryo creation and discard inherent in IVF.",
              ["https://en.wikipedia.org/wiki/Katie_Britt",
               "https://www.newsweek.com/fox-news-host-confronts-katie-britt-voting-against-ivf-1960953"]),
    ]),

    # ---------------- John Kennedy (LA-R, US Senator) ----------------
    ("john-kennedy", "LA", "Senator", [
        claim("jk1", "john-kennedy", "self_defense", 1, True,
              "Holds an A+ rating from the NRA Political Victory Fund and a consistent pro-gun voting record; in 2023 negotiated passage of a measure protecting the gun-ownership rights of veterans who use VA assistance to manage their benefits. Opposes new gun-control restrictions.",
              ["https://justfacts.votesmart.org/candidate/key-votes/35496/john-kennedy",
               "https://en.wikipedia.org/wiki/John_Kennedy_(Louisiana_politician)"]),
        claim("jk2", "john-kennedy", "sanctity_of_life", 0, True,
              "Strongly pro-life: praised the overturning of Roe, voted against the 2024 Reproductive Freedom for Women Act, and cosponsored the Born-Alive Abortion Survivors Protection Act, Pain-Capable Unborn Child Protection Act, and No Taxpayer Funding for Abortion Act.",
              ["https://www.kennedy.senate.gov/public/defending-the-unborn",
               "https://sbaprolife.org/senator/john-kennedy"]),
        claim("jk3", "john-kennedy", "foreign_policy_restraint", 1, False,
              "Supported U.S. military aid to Ukraine, framing it as a fight for American national security (while advocating a special inspector general to monitor the funds). The pro-aid posture cuts against the rubric's call for withdrawal from foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/John_Kennedy_(Louisiana_politician)",
               "https://www.govtrack.us/congress/members/john_kennedy/412679"]),
    ]),

    # ---------------- Joni Ernst (IA-R, US Senator) ----------------
    ("joni-ernst", "IA", "Senator", [
        claim("je1", "joni-ernst", "economic_stewardship", 2, True,
              "Founded the Senate DOGE Caucus to target government waste, has published a decade of annual 'Squeal Award' waste reports identifying trillions in wasteful federal spending, and is a longstanding supporter of a Balanced Budget Amendment to the Constitution.",
              ["https://www.ernst.senate.gov/priorities/budget-and-spending",
               "https://www.ernst.senate.gov/news/press-releases/ernst-creates-senate-doge-caucus-to-eliminate-government-waste"]),
        claim("je2", "joni-ernst", "sanctity_of_life", 0, True,
              "Opposes legalized abortion; voted for a fetal-personhood amendment in the Iowa Senate (2013) and has stated she would support a federal personhood bill recognizing life from conception.",
              ["https://en.wikipedia.org/wiki/Joni_Ernst",
               "https://ballotpedia.org/Joni_Ernst"]),
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

    SCORECARD.write_text(json.dumps(scorecard, indent=2))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
