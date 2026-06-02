#!/usr/bin/env python3
"""Enrichment (judicial batch 1): hand-curated claims for 5 sitting U.S. Supreme
Court Justices.

First JUDICIAL-branch batch. Named enrich-judicial-1 (not enrich-batch-N) to
avoid colliding with the hourly CLOUD routine, which owns the enrich-batch-N.py
sequence (currently through batch 12, all U.S. Senators).

Targets archetype_curated SCOTUS justices that had 0 evidence claims, all
state="US", office "Associate Justice, U.S. Supreme Court". Uses the
(slug + state + office_keyword) matcher from the senator batches.

Mix (3 conservative / 2 liberal), every claim tied to a landmark opinion:
  Samuel A. Alito Jr. — Dobbs (author), Hobby Lobby (author), Obergefell dissent
  Clarence Thomas     — Bruen (author), Dobbs (concurrence), Kennedy v. Bremerton (join)
  Neil M. Gorsuch     — Kennedy v. Bremerton (author), Bostock (author, NEGATIVE), Bruen (join)
  Sonia Sotomayor     — Dobbs dissent, Bruen dissent, Obergefell/303 Creative (NEGATIVE)
  Elena Kagan         — Dobbs dissent, Kennedy v. Bremerton dissent, Obergefell (NEGATIVE)

Scores are legislator-framed; for justices we map each claim to the closest
scored question and let the per-question score_impact reflect the actual judicial
record (user wants negative scores visible, not just total-score docking). Only
the four scored categories present on these records are touched:
sanctity_of_life, biblical_marriage, christian_liberty, self_defense.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the
master under GitHub's 50MB warning. build-data.py only re-minifies the master
when meta changes; the enrich step preserves minification itself.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()

# Frequently reused source URLs
DOBBS = "https://en.wikipedia.org/wiki/Dobbs_v._Jackson_Women%27s_Health_Organization"
DOBBS_PDF = "https://www.supremecourt.gov/opinions/21pdf/19-1392_6j37.pdf"
BRUEN = "https://en.wikipedia.org/wiki/New_York_State_Rifle_%26_Pistol_Association,_Inc._v._Bruen"
HOBBY = "https://en.wikipedia.org/wiki/Burwell_v._Hobby_Lobby_Stores,_Inc."
OBERGEFELL = "https://en.wikipedia.org/wiki/Obergefell_v._Hodges"
BOSTOCK = "https://en.wikipedia.org/wiki/Bostock_v._Clayton_County"
KENNEDY = "https://en.wikipedia.org/wiki/Kennedy_v._Bremerton_School_District"
THREE03 = "https://en.wikipedia.org/wiki/303_Creative_LLC_v._Elenis"


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
    # ---------------- Samuel A. Alito Jr. (US, Associate Justice) ----------------
    ("samuel-a-alito-jr", "US", "Justice", [
        claim("sa1", "samuel-a-alito-jr", "sanctity_of_life", 0, True,
              "Authored the majority opinion in Dobbs v. Jackson Women's Health Organization (2022), overruling Roe v. Wade and Planned Parenthood v. Casey, holding that the Constitution confers no right to abortion and returning the question to the people and their elected representatives — the most consequential pro-life ruling in fifty years.",
              [DOBBS, DOBBS_PDF]),
        claim("sa2", "samuel-a-alito-jr", "christian_liberty", 1, True,
              "Authored Burwell v. Hobby Lobby Stores (2014), holding under the Religious Freedom Restoration Act that closely held, family-owned corporations cannot be forced to fund insurance coverage for contraceptives that violate their owners' sincere religious convictions — a landmark conscience exemption for religious business owners.",
              [HOBBY]),
        claim("sa3", "samuel-a-alito-jr", "biblical_marriage", 0, True,
              "Dissented in Obergefell v. Hodges (2015), rejecting a constitutional right to same-sex marriage, arguing the Constitution is silent on marriage and its definition belongs to the people of the states, and warning the decision would be used to stigmatize Americans who hold the man-woman view of marriage.",
              [OBERGEFELL]),
    ]),

    # ---------------- Clarence Thomas (US, Associate Justice) ----------------
    ("clarence-thomas", "US", "Justice", [
        claim("ct1", "clarence-thomas", "self_defense", 1, True,
              "Authored New York State Rifle & Pistol Assn. v. Bruen (2022), striking down New York's discretionary 'proper-cause' carry-permit regime and establishing the text-history-and-tradition test for Second Amendment cases — the most significant expansion of gun rights since Heller and a rejection of discretionary firearm restrictions.",
              [BRUEN]),
        claim("ct2", "clarence-thomas", "sanctity_of_life", 0, True,
              "Joined the Dobbs majority (2022) ending the constitutional right to abortion and wrote a concurrence urging the Court to reconsider its substantive-due-process line of cases; a consistent originalist opponent of a judicially created abortion right across more than three decades on the bench.",
              [DOBBS, "https://en.wikipedia.org/wiki/Clarence_Thomas"]),
        claim("ct3", "clarence-thomas", "christian_liberty", 3, True,
              "Joined the 6-3 majority in Kennedy v. Bremerton School District (2022), upholding a public-school football coach's right to pray at midfield after games and discarding the Lemon test — a major protection for prayer and religious expression by public officials in the public square.",
              [KENNEDY]),
    ]),

    # ---------------- Neil M. Gorsuch (US, Associate Justice) ----------------
    ("neil-m-gorsuch", "US", "Justice", [
        claim("ng1", "neil-m-gorsuch", "christian_liberty", 3, True,
              "Authored Kennedy v. Bremerton School District (2022), holding that a public-school football coach had a First Amendment right to kneel in personal prayer at the 50-yard line, and formally abandoning the Lemon test in favor of a historical-practices analysis — a landmark win for public religious expression.",
              [KENNEDY]),
        claim("ng2", "neil-m-gorsuch", "biblical_marriage", 2, False,
              "Authored the 6-3 majority in Bostock v. Clayton County (2020), holding that Title VII's ban on sex discrimination necessarily covers sexual orientation and gender identity — the most consequential federal LGBTQ employment ruling to date, contrary to the rubric's affirmation of immutable, God-given biological sex.",
              [BOSTOCK]),
        claim("ng3", "neil-m-gorsuch", "self_defense", 1, True,
              "Joined the Bruen majority (2022) expanding the right to carry firearms in public and adopting the text-history-and-tradition standard; a consistent vote against discretionary gun-control restrictions.",
              [BRUEN]),
    ]),

    # ---------------- Sonia Sotomayor (US, Associate Justice) ----------------
    ("sonia-sotomayor", "US", "Justice", [
        claim("ss1", "sonia-sotomayor", "sanctity_of_life", 0, False,
              "Joined the joint dissent in Dobbs (2022) defending the constitutional abortion right established by Roe and Casey and condemning its elimination; a reliable vote for abortion rights, rejecting any personhood-from-conception standard.",
              [DOBBS]),
        claim("ss2", "sonia-sotomayor", "self_defense", 1, False,
              "Dissented in Bruen (2022), arguing that states must retain authority to enact public-carry licensing and other firearm restrictions to address gun violence — opposing the rubric's defense of unrestricted Second Amendment rights.",
              [BRUEN]),
        claim("ss3", "sonia-sotomayor", "biblical_marriage", 1, False,
              "Joined the Obergefell v. Hodges majority (2015) establishing a nationwide right to same-sex marriage and authored the dissent in 303 Creative v. Elenis (2023) that would have compelled a Christian website designer to create same-sex-wedding content — consistently favoring LGBTQ legal claims over the man-woman definition of marriage and conscience protections.",
              [OBERGEFELL, THREE03]),
    ]),

    # ---------------- Elena Kagan (US, Associate Justice) ----------------
    ("elena-kagan", "US", "Justice", [
        claim("ek1", "elena-kagan", "sanctity_of_life", 0, False,
              "Joined the joint dissent in Dobbs (2022) defending the constitutional abortion right; a consistent vote for abortion access.",
              [DOBBS]),
        claim("ek2", "elena-kagan", "christian_liberty", 3, False,
              "Joined Justice Sotomayor's dissent in Kennedy v. Bremerton School District (2022), arguing the coach's midfield prayer amounted to coercive government endorsement of religion — opposing the rubric's support for prayer by public officials in the public square.",
              [KENNEDY]),
        claim("ek3", "elena-kagan", "biblical_marriage", 1, False,
              "Joined the Obergefell majority (2015) establishing same-sex marriage nationwide and joined the 303 Creative (2023) dissent; a consistent vote for same-sex marriage in law over conscience-based objections.",
              [OBERGEFELL, THREE03]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
    scores_set = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
                before = scores[cat][qi]
                scores[cat][qi] = si
                scores_set += 1
                if before != si:
                    print(f"      delta {m['name']}: scores[{cat}][{qi}] {before} -> {si}")
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ok {m['name']:<22} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} justices, added {claims_added} claims, set {scores_set} per-question scores")


if __name__ == "__main__":
    main()
