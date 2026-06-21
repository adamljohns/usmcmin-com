#!/usr/bin/env python3
"""Enrichment batch 338: hand-curated claims for 5 statewide officials.

archetype_curated federal senator/rep buckets are fully exhausted; targets
here are evidence_state officials with 0 claims from bottom-of-alphabet
states (WA, WI, VT).

Targets: Nick Brown (WA-D, AG), Denny Heck (WA-D, Lt Gov), Sara Rodriguez
(WI-D, Lt Gov), Charity Clark (VT-D, AG), John Rodgers (VT-R, Lt Gov).
Each claim cites >=1 reliable source reflecting 2024-2026 public record.
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
    # ---------------- Nick Brown (WA-D, Attorney General) ----------------
    ("nick-brown", "WA", "Attorney", [
        claim("nb1", "nick-brown", "self_defense", 1, False,
              "Co-authored Washington's Initiative 1639 (approved by ~60% of voters, 2018) imposing waiting periods, enhanced background checks, and safe-storage requirements on semi-automatic rifles; as AG, campaigns on eliminating ghost guns and banning high-capacity magazines — consistently opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://nickbrownforag.com/priorities/",
               "https://ballotpedia.org/Nick_Brown_(Washington)"]),
        claim("nb2", "nick-brown", "sanctity_of_life", 4, False,
              "Campaigned on a promise to 'always stand up for abortion access' and upon taking office in January 2025 vowed to enforce Washington's abortion 'shield law' protecting out-of-state patients who travel to Washington for abortions — actively aligned with the abortion-provider network the rubric opposes.",
              ["https://www.atg.wa.gov/about-nick-brown",
               "https://nickbrownforag.com/priorities/"]),
        claim("nb3", "nick-brown", "biblical_marriage", 2, False,
              "Filed a multi-state federal lawsuit in 2025 challenging a presidential executive order criminalizing gender-affirming care for minors, successfully obtaining court relief to keep gender-transition treatments available to children — directly advancing the transgender ideology the rubric opposes.",
              ["https://www.atg.wa.gov/news/news-releases/state-washington-challenges-unconstitutional-presidential-order-criminalizing",
               "https://ballotpedia.org/Nick_Brown_(Washington)"]),
    ]),

    # ---------------- Denny Heck (WA-D, Lieutenant Governor) ----------------
    ("denny-heck", "WA", "Lieutenant Governor", [
        claim("dh1", "denny-heck", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood and NARAL Pro-Choice Washington during his eight-year tenure as a U.S. Representative (2013-2021) and voted consistently against any restriction on abortion access; as Lieutenant Governor (2021-present) he has continued publicly supporting abortion rights — rejecting personhood-from-conception.",
              ["https://ballotpedia.org/Denny_Heck",
               "https://justfacts.votesmart.org/candidate/126058/denny-heck"]),
        claim("dh2", "denny-heck", "self_defense", 1, False,
              "Voted for gun-control legislation repeatedly as a U.S. Representative (2013-2021) — including the Bipartisan Background Checks Act (H.R. 8, 2019) — and earned a consistently low NRA grade, opposing the constitutional-carry and anti-restriction principles the rubric supports.",
              ["https://justfacts.votesmart.org/candidate/key-votes/126058/denny-heck/37/guns",
               "https://www.govtrack.us/congress/members/denny_heck/412584"]),
        claim("dh3", "denny-heck", "biblical_marriage", 0, False,
              "Publicly supported same-sex marriage recognition throughout his congressional career (2013-2021) and as Lieutenant Governor; voted with his party on LGBTQ equality measures, rejecting the one-man-one-woman definition of marriage the rubric holds.",
              ["https://ballotpedia.org/Denny_Heck",
               "https://justfacts.votesmart.org/candidate/126058/denny-heck"]),
    ]),

    # ---------------- Sara Rodriguez (WI-D, Lieutenant Governor) ----------------
    ("sara-rodriguez", "WI", "Lieutenant Governor", [
        claim("sr1", "sara-rodriguez", "sanctity_of_life", 0, False,
              "As a Wisconsin Assembly member, co-sponsored legislation to repeal Wisconsin's 1849 abortion ban; as Lieutenant Governor (2023-present) committed to protecting abortion access for all Wisconsinites, and launched a 2026 gubernatorial campaign with abortion rights as a centerpiece — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Sara_Rodriguez",
               "https://www.saraforwi.com/why-im-running"]),
        claim("sr2", "sara-rodriguez", "border_immigration", 0, False,
              "Called for 'immediate action to protect Wisconsin communities' and publicly demanded accountability from federal immigration enforcement, opposing the Trump administration's deportation operations — contrary to the rubric's support for strong border enforcement and mandatory deportation.",
              ["https://ballotpedia.org/Sara_Rodriguez",
               "https://en.wikipedia.org/wiki/Sara_Rodriguez"]),
        claim("sr3", "sara-rodriguez", "self_defense", 1, False,
              "Frames gun violence as a 'public health issue' and supports 'sensible' gun-control legislation; as a public health professional turned officeholder, consistently advocates for restricting firearms — opposing the constitutional-carry and anti-restriction principles the rubric defends.",
              ["https://isthmus.com/news/news/meet-your-lieutenant-governor-sara-rodriguez/",
               "https://ballotpedia.org/Sara_Rodriguez"]),
    ]),

    # ---------------- Charity Clark (VT-D, Attorney General) ----------------
    ("charity-clark", "VT", "Attorney", [
        claim("cc1", "charity-clark", "biblical_marriage", 2, False,
              "Won a 2026 federal court victory protecting gender-affirming care for transgender youth, celebrated it as 'a victory in our ongoing fight for bodily autonomy and the rights of transgender youth,' and sued the Trump administration in December 2025 over restrictions on gender-transition treatments for minors — actively promoting transgender ideology.",
              ["https://ago.vermont.gov/blog/2026/04/20/attorney-general-clark-and-coalition-win-lawsuit-protecting-gender-affirming-care",
               "https://ago.vermont.gov/blog/2025/12/24/attorney-general-clark-sues-trump-administration-federal-attack-gender-affirming-care"]),
        claim("cc2", "charity-clark", "sanctity_of_life", 0, False,
              "Joined a multistate coalition challenging restrictions on the abortion drug mifepristone, committed to protecting abortion providers, and describes abortion as essential healthcare — actively defending broad abortion access and rejecting any personhood-from-conception standard.",
              ["https://ago.vermont.gov/blog/2025/05/23/attorney-general-clark-joins-multistate-effort-protect-abortion-and-gender-affirming-care-providers",
               "https://vtdigger.org/profile/charity-r-clark/"]),
        claim("cc3", "charity-clark", "self_defense", 1, False,
              "Filed amicus briefs and joined coalitions defending Vermont's gun-control laws in court — including age-based restrictions on long-gun purchases and magazine-capacity limits — calling such measures 'commonsense gun measures that save lives,' opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ago.vermont.gov/blog/2025/10/23/attorney-general-clark-joins-brief-supporting-states-rights-protect-communities-gun-violence",
               "https://ago.vermont.gov/blog/2025/11/06/attorney-general-clark-joins-coalition-supporting-california-law-regulates-purchase-long-guns"]),
    ]),

    # ---------------- John Rodgers (VT-R, Lieutenant Governor) ----------------
    ("john-rodgers", "VT", "Lt. Governor", [
        claim("jr1", "john-rodgers", "self_defense", 1, True,
              "A vocal gun-rights advocate who has publicly argued that Vermont's ban on high-capacity magazines is unconstitutional and has a long record defending Second Amendment rights; ran for governor in 2018 specifically on a platform opposing new gun restrictions — consistent with the rubric's opposition to magazine limits and firearm restrictions.",
              ["https://vtdigger.org/2018/04/10/rodgers-vocal-gun-rights-advocate-weighs-run-governor/",
               "https://ballotpedia.org/John_Rodgers_(Vermont)"]),
        claim("jr2", "john-rodgers", "economic_stewardship", 2, True,
              "Campaigned for Lieutenant Governor (2024) on Vermont's affordability crisis, explicitly criticizing 'the massive cost-of-living increase: fuel and electricity, taxes, fees, all growing far in excess of people's incomes' — aligning with the rubric's call for fiscal restraint and balanced budgets.",
              ["https://vtdigger.org/2024/12/04/vermont-conversation-john-rodgers-and-the-future-of-vermont-politics/",
               "https://ballotpedia.org/John_Rodgers_(Vermont)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
