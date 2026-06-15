#!/usr/bin/env python3
"""Enrichment batch 224: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Targets evidence_curated candidates with exactly 2 claims (archetype_curated 0-claim bucket
is exhausted). Selected from the bottom of the alphabet (VA, TX, TN, OR). Mix: 3 D / 2 (1D+1R).

Candidates:
  Missy Cotter Smasal (VA-D, VA-02 D nominee 2024) – EMILY's List endorsement / sanctity_of_life
  Darius Mayfield (VA-R, VA-07 2026 candidate) – anti-abortion statement / sanctity_of_life
  Frederick D. Haynes III (TX-D, TX-30 2026 nominee) – ICE abolition / border_immigration
  Justin Pearson (TN-D, TN-09 2026 candidate) – Planned Parenthood endorsement / sanctity_of_life
  Suzanne Bonamici (OR-D, sitting U.S. Rep OR-01) – gun-control voting record / self_defense

Each claim cites >=1 reliable source and reflects documented 2023-2026 voting
record / public positions.

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


TARGETS = [
    # --- Missy Cotter Smasal (VA-D, U.S. House VA-02 2024 nominee) ---
    ("missy-cotter-smasal", "VA", "House", [
        claim("mcs3", "missy-cotter-smasal", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List — which exclusively backs pro-choice Democratic women and "
              "requires a firm commitment to abortion access as a condition of its endorsement and "
              "financial support — for her 2024 run in Virginia's 2nd Congressional District. The "
              "EMILY's List endorsement press release described Smasal as a 'pro-choice champion' "
              "committed to stopping a Republican national abortion ban. EMILY's List is classified "
              "by the rubric as an abortion-industry funding network alongside NARAL and Planned "
              "Parenthood; receiving its endorsement and associated fundraising support places "
              "Smasal squarely within the abortion-industry donor network the rubric's fourth "
              "sanctity-of-life question asks candidates to reject.",
              ["https://emilyslist.org/news/emilys-list-endorses-missy-cotter-smasal-for-election-to-virginias-2nd-congressional-district/",
               "https://ballotpedia.org/Missy_Cotter_Smasal"]),
    ]),

    # --- Darius Mayfield (VA-R, U.S. Representative VA-07 2026 candidate) ---
    ("darius-mayfield", "VA", "Representative", [
        claim("dm3", "darius-mayfield", "sanctity_of_life", 0, True,
              "Has publicly declared that 'abortion is unconstitutional,' rejecting abortion access "
              "as a matter of constitutional law and affirming the unborn's right to life from "
              "conception. He has additionally stated that abortion providers — including Planned "
              "Parenthood — should not receive taxpayer funds from federal, state, or local "
              "governments. Mayfield, a small-business owner and two-time Republican congressional "
              "nominee (NJ-12 2020 and 2022, VA-07 2026), has held this position consistently "
              "across multiple campaigns, placing him in alignment with the rubric's life-at-"
              "conception and anti-abortion-industry-funding standard.",
              ["https://www.facebook.com/dariusmayfieldforamerica/photos/a.110264104384048/116818383728620/?type=3",
               "https://www.isidewith.com/candidates/darius-mayfield/policies/social/abortion"]),
    ]),

    # --- Frederick D. Haynes III (TX-D, U.S. Representative TX-30 2026 nominee) ---
    ("frederick-d-haynes-iii", "TX", "Representative", [
        claim("fdh3", "frederick-d-haynes-iii", "border_immigration", 1, False,
              "At his January 2026 campaign kickoff event in Dallas, Rev. Haynes explicitly called "
              "for 'dismantling Immigration and Customs Enforcement' — the federal agency that "
              "carries out deportation operations — as a core plank of his immigration platform. "
              "Abolishing ICE, the primary enforcement mechanism for mandatory removal of "
              "undocumented immigrants, directly contradicts the rubric's mandatory-deportation "
              "standard. Haynes has framed ICE abolition as part of a broader 'overhaul of the "
              "immigration system' and supports comprehensive immigration reform, signaling "
              "consistent opposition to the enforcement-first, mandatory-removal model the rubric "
              "requires. He won the TX-30 Democratic primary in March 2026 running on this platform "
              "and is endorsed by Justice Democrats.",
              ["https://www.keranews.org/politics/2026-01-12/frederick-haynes-friendship-west-baptist-congress-district-30-jasmine-crockett",
               "https://www.wfaa.com/article/news/politics/elections/dallas-pastor-frederick-haynes-iii-running-us-house-of-represenatatives/287-eb6f183d-2a58-4707-9301-16988d6af3b4"]),
    ]),

    # --- Justin Pearson (TN-D, U.S. Representative TN-09 2026 candidate) ---
    ("justin-pearson-tn-09", "TN", "Representative", [
        claim("jp3", "justin-pearson-tn-09", "sanctity_of_life", 0, False,
              "Endorsed by Tennessee Advocates for Planned Parenthood in 2024, which exclusively "
              "endorses candidates who support abortion access and reproductive healthcare. Pearson "
              "is a Justice Democrats-endorsed progressive who openly supports abortion rights, "
              "consistent with his broader platform of 'bodily autonomy' and reproductive justice. "
              "His campaign website (votejustinj.com) and Justice Democrats endorsement both "
              "reflect a pro-choice stance that rejects any legal recognition of fetal personhood "
              "from conception — directly opposing the rubric's life-at-conception standard. As a "
              "Tennessee state representative, Pearson has been a vocal opponent of the state's "
              "post-Dobbs abortion ban, framing it as an attack on women's fundamental rights.",
              ["https://www.plannedparenthoodaction.org/tennessee-advocates-planned-parenthood/blog/2024-candidate-endorsements",
               "https://en.wikipedia.org/wiki/Justin_J._Pearson"]),
    ]),

    # --- Suzanne Bonamici (OR-D, sitting U.S. Rep OR-01) ---
    ("suzanne-bonamici", "OR", "Representative", [
        claim("sb3", "suzanne-bonamici", "self_defense", 1, False,
              "A member of the House Gun Violence Prevention Task Force with a documented record of "
              "backing sweeping gun-control legislation: supported the Bipartisan Background Checks "
              "Act (H.R. 8) and Enhanced Background Checks Act (H.R. 1446) to mandate universal "
              "background checks; co-sponsored the Federal Extreme Risk Protection Order Act (red-"
              "flag law) authorizing courts to remove firearms from individuals deemed a danger; "
              "backed legislation to ban high-capacity magazines, raise the minimum age to purchase "
              "semi-automatic weapons to 21, require safe storage of firearms, and close the bump-"
              "stock loophole. Her official press releases from her House office confirm each of "
              "these votes and co-sponsorships. This comprehensive gun-restriction record directly "
              "opposes the rubric's anti-red-flag / anti-AWB / anti-mag-limit / anti-registry "
              "standard.",
              ["https://bonamici.house.gov/media/press-releases/house-passes-bonamici-backed-bills-prevent-gun-violence-schools-communities",
               "https://bonamici.house.gov/media/press-releases/bonamici-helps-pass-gun-violence-prevention-bills"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
