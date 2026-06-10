#!/usr/bin/env python3
"""Enrichment batch 121: hand-curated claims for 5 sitting U.S. Representatives
(bottom of reverse-alpha pool: VA-02, VA-06, FL-17, FL-18, CO-04).

archetype_curated federal senator bucket is down to 1 perennial candidate
(Joe Mazzola, MA) with no findable sourced positions; reps bucket is empty.
Next sourced targets taken from evidence_federal 0-claims pool, reverse-alpha.

Targets: Jen Kiggans (VA-02 R), Ben Cline (VA-06 R), Greg Steube (FL-17 R),
Scott Franklin (FL-18 R), Lauren Boebert (CO-04 R). Each claim cites >=1
reliable source and reflects 2024-2026 voting record / public positions.

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
    # ---------------- Jen Kiggans (VA-02, R, U.S. House District 2) ----------------
    ("jen-kiggans", "VA", "House", [
        claim("jk1", "jen-kiggans", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America for her 2022 and 2024 campaigns; has voted consistently to defend the lives of the unborn and infants in Congress, opposing taxpayer funding for abortion domestically and internationally, and affirmed the Dobbs ruling overturning Roe v. Wade — aligning with the rubric's life-at-conception and pro-life standard.",
              ["https://sbaprolife.org/representative/jennifer-kiggans",
               "https://en.wikipedia.org/wiki/Jen_Kiggans"]),
        claim("jk2", "jen-kiggans", "border_immigration", 1, False,
              "Co-sponsored the DIGNIDAD Act (H.R.4393, 119th Congress, joined Feb 3 2026) — a bill proposing a pathway to legal status for up to 12 million undocumented immigrants, representing a legalization framework rather than the mandatory deportation and enforcement-first standard the rubric requires.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/4393/cosponsors",
               "https://en.wikipedia.org/wiki/Jen_Kiggans"]),
    ]),

    # ---------------- Ben Cline (VA-06, R, U.S. House District 6) ----------------
    ("ben-cline", "VA", "House", [
        claim("bc1", "ben-cline", "sanctity_of_life", 0, True,
              "Established a 16-year staunchly anti-abortion record in the Virginia House of Delegates before Congress; in the House voted consistently to stop taxpayer dollars from funding abortion domestically and internationally, cosponsored the Pain-Capable Unborn Children from Late-Term Abortions Act, and pushed back on Biden-era pro-abortion executive actions — matching the rubric's life-at-conception and protection-of-the-unborn standard.",
              ["https://en.wikipedia.org/wiki/Ben_Cline",
               "https://sbaprolife.org/representative/ben-cline"]),
        claim("bc2", "ben-cline", "border_immigration", 0, True,
              "Voted for H.R.2, the Secure the Border Act of 2023, which funds border-wall construction, tightens asylum standards, and expands enforcement capacity; has repeatedly called Biden's open-border policies a national crisis and stated that 'every town' in Virginia has become a border town due to fentanyl, human trafficking, and illegal immigration.",
              ["https://cline.house.gov/news/documentsingle.aspx?DocumentID=1222",
               "https://en.wikipedia.org/wiki/Ben_Cline"]),
        claim("bc3", "ben-cline", "self_defense", 1, True,
              "Cosponsored legislation demanding the FBI and DOJ purge firearms-related records on individuals who were coerced or unduly pressured into waiving their gun rights — a pro-Second Amendment position consistent with the rubric's rejection of background-check overreach and firearm registries.",
              ["https://cline.house.gov/news/documentsingle.aspx?DocumentID=808",
               "https://en.wikipedia.org/wiki/Ben_Cline"]),
    ]),

    # ---------------- Greg Steube (FL-17, R, US Representative) ----------------
    ("greg-steube", "FL", "Representative", [
        claim("gs1", "greg-steube", "sanctity_of_life", 0, True,
              "Tracked by SBA Pro-Life America with a consistent pro-life voting record; cosponsored the Pain-Capable Unborn Children from Late-Term Abortions Act; voted against federal abortion funding and spoke against Florida's all-trimester abortion ballot amendment — affirming protection of the unborn aligned with the rubric's life-at-conception standard.",
              ["https://sbaprolife.org/representative/greg-steube",
               "https://steube.house.gov/issues/life-and-values/"]),
        claim("gs2", "greg-steube", "self_defense", 1, True,
              "Voted against H.R.8 (expanded universal background checks) and H.R.1446 (which would allow FBI to delay firearm transfers indefinitely); formally opposed H.R.2377, the Federal Extreme Risk Protection Order Act (red-flag law), in the House Judiciary Committee — directly matching the rubric's rejection of background-check expansions, red-flag laws, and magazine restrictions.",
              ["https://steube.house.gov/press-releases/steube-stands-up-for-second-amendment-opposes-red-flag-laws/",
               "https://en.wikipedia.org/wiki/Greg_Steube"]),
    ]),

    # ---------------- Scott Franklin (FL-18, R, US Representative) ----------------
    ("scott-franklin", "FL", "Representative", [
        claim("sf1", "scott-franklin", "sanctity_of_life", 0, True,
              "Requested unanimous consent in the House for H.R.18, the No Taxpayer Funding for Abortion and Abortion Insurance Full Disclosure Act (to make the Hyde Amendment permanent); introduced H.R.7798, the Prohibiting Abortion Industry's Lucrative Loopholes Act; SBA Pro-Life America tracks his consistent record of votes defending unborn life and opposing abortion financing — aligning with the rubric's life-at-conception and protection-of-the-unborn standard.",
              ["https://sbaprolife.org/representative/scott-franklin",
               "https://en.wikipedia.org/wiki/Scott_Franklin_(politician)"]),
        claim("sf2", "scott-franklin", "election_integrity", 0, True,
              "On January 6, 2021, voted to object to the certification of Arizona and Pennsylvania electoral votes on grounds of election-integrity concerns, aligning with the rubric's election-integrity pillar.",
              ["https://en.wikipedia.org/wiki/Scott_Franklin_(politician)",
               "https://ballotpedia.org/Scott_Franklin"]),
    ]),

    # ---------------- Lauren Boebert (CO-04, R, US Representative) ----------------
    ("lauren-boebert", "CO", "Representative", [
        claim("lb1", "lauren-boebert", "self_defense", 1, True,
              "A founding member of the House Second Amendment Caucus and the most prominent gun-rights advocate in Congress; voted against H.R.8 (expanded background checks) and H.R.1446 (FBI delay authority), and has publicly carried a firearm while campaigning — embodying the rubric's rejection of any assault-weapons ban, magazine restriction, background-check expansion, or red-flag legislation.",
              ["https://en.wikipedia.org/wiki/Lauren_Boebert",
               "https://ballotpedia.org/Lauren_Boebert"]),
        claim("lb2", "lauren-boebert", "sanctity_of_life", 0, True,
              "Received high marks from SBA Pro-Life America with an impeccable record of standing and voting for life; stated she would support national restrictions on abortion access — aligning with the rubric's life-at-conception and protection-of-the-unborn standard.",
              ["https://sbaprolife.org/representative/lauren-boebert",
               "https://en.wikipedia.org/wiki/Lauren_Boebert"]),
        claim("lb3", "lauren-boebert", "border_immigration", 0, True,
              "Was the first Republican in 24 years to initiate impeachment proceedings — against President Biden — citing his dereliction of duty at the Southern border; has been a relentless advocate for wall funding, military deployment, and full border enforcement throughout her congressional career.",
              ["https://en.wikipedia.org/wiki/Lauren_Boebert",
               "https://ballotpedia.org/Lauren_Boebert"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
