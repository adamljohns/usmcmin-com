#!/usr/bin/env python3
"""Enrichment (judicial batch 2): completes the U.S. Supreme Court.

The remaining 4 sitting justices not covered by enrich-judicial-1.py:
  John G. Roberts Jr. (Chief Justice) — Obergefell dissent, Bruen join,
    303 Creative join. NOTE: Roberts only concurred in the *judgment* in Dobbs
    (would discard the viability line but not fully overrule Roe), so no clean
    sanctity_of_life claim is asserted for him.
  Brett M. Kavanaugh — Dobbs majority join, Bruen join + concurrence,
    Kennedy v. Bremerton join.
  Amy Coney Barrett  — Dobbs majority join, Bruen join, Kennedy v. Bremerton join.
  Ketanji Brown Jackson — post-Dobbs abortion-access alignment (Moyle, 2024),
    303 Creative dissent join, declined to define "woman" at 2022 confirmation
    (NEGATIVE on biblical_marriage).

Named enrich-judicial-2.py to stay clear of the hourly cloud routine's
enrich-batch-N.py sequence. Writes scorecard.json MINIFIED (see judicial-1).
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()

DOBBS = "https://en.wikipedia.org/wiki/Dobbs_v._Jackson_Women%27s_Health_Organization"
BRUEN = "https://en.wikipedia.org/wiki/New_York_State_Rifle_%26_Pistol_Association,_Inc._v._Bruen"
OBERGEFELL = "https://en.wikipedia.org/wiki/Obergefell_v._Hodges"
KENNEDY = "https://en.wikipedia.org/wiki/Kennedy_v._Bremerton_School_District"
THREE03 = "https://en.wikipedia.org/wiki/303_Creative_LLC_v._Elenis"
MOYLE = "https://en.wikipedia.org/wiki/Moyle_v._United_States"
KBJ = "https://en.wikipedia.org/wiki/Ketanji_Brown_Jackson"
ACB = "https://en.wikipedia.org/wiki/Amy_Coney_Barrett"
WOMAN_NR = "https://www.nationalreview.com/news/judge-jackson-refuses-to-define-woman-during-confirmation-hearing-im-not-a-biologist/"
WOMAN_SEN = "https://www.blackburn.senate.gov/2022/3/video-release-judge-jackson-cannot-define-woman-during-blackburn-scotus-day-two-hearing-remarks"


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
    # ---------------- John G. Roberts Jr. (US, Chief Justice) ----------------
    ("john-g-roberts-jr", "US", "Justice", [
        claim("rb1", "john-g-roberts-jr", "biblical_marriage", 0, True,
              "Dissented in Obergefell v. Hodges (2015), rejecting a constitutional right to same-sex marriage, writing that the majority's decision 'has nothing to do with the Constitution' and that the definition of marriage belongs to the people of the states — famously asking, 'Just who do we think we are?'",
              [OBERGEFELL]),
        claim("rb2", "john-g-roberts-jr", "self_defense", 1, True,
              "Joined the 6-3 majority in New York State Rifle & Pistol Assn. v. Bruen (2022), recognizing a right to carry firearms in public and striking New York's discretionary 'proper-cause' permit regime under the text-history-and-tradition test.",
              [BRUEN]),
        claim("rb3", "john-g-roberts-jr", "christian_liberty", 2, True,
              "Joined the 6-3 majority in 303 Creative v. Elenis (2023), holding the First Amendment forbids compelling a Christian website designer to create messages celebrating same-sex weddings against her religious convictions — a ruling against compelled speech.",
              [THREE03]),
    ]),

    # ---------------- Brett M. Kavanaugh (US, Associate Justice) ----------------
    ("brett-m-kavanaugh", "US", "Justice", [
        claim("kv1", "brett-m-kavanaugh", "sanctity_of_life", 0, True,
              "Joined the five-justice majority in Dobbs v. Jackson Women's Health Organization (2022) overruling Roe v. Wade and Casey, and wrote a concurrence emphasizing that the Constitution is neutral on abortion and the issue was being returned to the people and their elected representatives.",
              [DOBBS]),
        claim("kv2", "brett-m-kavanaugh", "self_defense", 1, True,
              "Joined the Bruen majority (2022) and wrote a concurrence (with the Chief Justice) confirming the right to carry in public while clarifying that objective shall-issue permitting survives — rejecting New York's discretionary restrictions.",
              [BRUEN]),
        claim("kv3", "brett-m-kavanaugh", "christian_liberty", 3, True,
              "Joined the 6-3 majority in Kennedy v. Bremerton School District (2022), upholding a public-school football coach's right to pray at midfield and discarding the Lemon test.",
              [KENNEDY]),
    ]),

    # ---------------- Amy Coney Barrett (US, Associate Justice) ----------------
    ("amy-coney-barrett", "US", "Justice", [
        claim("ab1", "amy-coney-barrett", "sanctity_of_life", 0, True,
              "Joined the Dobbs majority (2022) overruling Roe v. Wade and Casey and holding the Constitution confers no right to abortion; a longtime scholarly critic of Roe's reasoning.",
              [DOBBS, ACB]),
        claim("ab2", "amy-coney-barrett", "self_defense", 1, True,
              "Joined the Bruen majority (2022) recognizing the right to carry firearms in public under the text-history-and-tradition standard and rejecting discretionary 'proper-cause' permitting.",
              [BRUEN]),
        claim("ab3", "amy-coney-barrett", "christian_liberty", 3, True,
              "Joined the 6-3 majority in Kennedy v. Bremerton (2022), protecting a public-school coach's personal prayer in the public square and discarding the Lemon test.",
              [KENNEDY]),
    ]),

    # ---------------- Ketanji Brown Jackson (US, Associate Justice) ----------------
    ("ketanji-brown-jackson", "US", "Justice", [
        claim("kbj1", "ketanji-brown-jackson", "sanctity_of_life", 0, False,
              "Sworn in days after Dobbs, has aligned with the Court's liberal justices in favor of abortion access in post-Dobbs disputes; in Moyle v. United States (2024) she would have decided the EMTALA case on the merits and protested that the Court's dismissal left 'pregnant people experiencing emergency medical conditions' unprotected — rejecting any personhood-from-conception standard.",
              [MOYLE, KBJ]),
        claim("kbj2", "ketanji-brown-jackson", "biblical_marriage", 1, False,
              "Joined Justice Sotomayor's dissent in 303 Creative v. Elenis (2023), which would have required a Christian website designer to create same-sex-wedding content; votes consistently with the Court's liberal bloc on LGBTQ legal claims.",
              [THREE03]),
        claim("kbj3", "ketanji-brown-jackson", "biblical_marriage", 2, False,
              "At her March 2022 Senate confirmation hearing, when Sen. Blackburn asked her to define the word 'woman,' she declined, answering 'I can't ... I'm not a biologist' — declining to affirm a fixed biological definition of sex, contrary to the rubric's affirmation of immutable, God-given biological sex.",
              [WOMAN_NR, WOMAN_SEN]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            cat, qi, si = cl["category"], cl["question_idx"], cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                before = scores[cat][qi]
                scores[cat][qi] = si
                scores_set += 1
                if before != si:
                    print(f"      delta {m['name']}: scores[{cat}][{qi}] {before} -> {si}")
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ok {m['name']:<24} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} justices, added {claims_added} claims, set {scores_set} per-question scores")


if __name__ == "__main__":
    main()
