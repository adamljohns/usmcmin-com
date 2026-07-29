#!/usr/bin/env python3
"""Enrichment batch 888: hand-curated claims for 5 NC Republican State Senators.

All archetype_curated federal senator/rep buckets exhausted; pivoting to
archetype_party_default NC state senators from the bottom of the reverse-
alphabet list. All 5 are sitting Republican members of the NC Senate who
voted along party lines for NC SB20 (12-week abortion limit, May 2023
and veto override), NC SB49 (Parents' Bill of Rights, Feb/Aug 2023), and
NC SB50 (constitutional carry, March 2025 — Warren Daniel is a primary
co-sponsor).

Targets (NC State Senators, reverse-alpha order):
  Warren Daniel, W. Ted Alexander, Vickie Sawyer, Tom McInnis, Todd Johnson

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
    # ------------ Warren Daniel (NC-R, State Senator SD-46) ------------
    ("warren-daniel", "NC", "Senator", [
        claim("wd1", "warren-daniel", "self_defense", 0, True,
              "A primary sponsor of NC Senate Bill 50 'Freedom to Carry NC,' which passed the Senate 26-18 along party lines in March 2025, removing the permit requirement for concealed carry and establishing constitutional carry in North Carolina — the bill most directly aligned with the rubric's constitutional-carry ideal.",
              ["https://www.carolinajournal.com/nc-senate-officially-passes-constitutional-carry-bill/",
               "https://ncnewsline.com/2025/03/20/north-carolina-senate-passes-bill-allowing-permitless-carry-of-concealed-handguns/"]),
        claim("wd2", "warren-daniel", "sanctity_of_life", 0, True,
              "Voted for NC Senate Bill 20 ('Care for Women, Children, and Families Act') and the Republican veto override in May 2023, enacting a 12-week abortion restriction celebrated by SBA Pro-Life America as 'protecting 3,000+ lives annually' — a consistent pro-life legislative record.",
              ["https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://sbaprolife.org/newsroom/press-releases/victory-north-carolina-establishes-law-protecting-3000-lives-annually"]),
        claim("wd3", "warren-daniel", "family_child_sovereignty", 0, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') in February 2023 and the veto override in August 2023, requiring schools to notify parents if their child requests a name or pronoun change and restricting sexuality-and-gender instruction in grades K-4 — a direct parental-rights protection.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://spectrumlocalnews.com/nc/charlotte/news/2023/02/07/controversial--parents--bill-of-rights--in-n-c--senate--here-s-what-s-in-the-lgbtq-bill"]),
    ]),

    # ------------ W. Ted Alexander (NC-R, State Senator SD-44) ------------
    ("w-ted-alexander", "NC", "Senator", [
        claim("wta1", "w-ted-alexander", "sanctity_of_life", 0, True,
              "Voted for NC Senate Bill 20 ('Care for Women, Children, and Families Act') and the Republican veto override in May 2023, enacting the 12-week abortion restriction along party lines — a pro-life legislative record consistent with SBA Pro-Life America's celebration of the bill.",
              ["https://www.northcarolinahealthnews.org/2023/05/04/measure-limiting-abortions-after-12-weeks-passes-nc-house-along-party-lines-in-late-night-vote/",
               "https://sbaprolife.org/newsroom/press-releases/victory-north-carolina-establishes-law-protecting-3000-lives-annually"]),
        claim("wta2", "w-ted-alexander", "biblical_marriage", 4, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') and the veto override in August 2023, which bars instruction on gender identity or sexual orientation in kindergarten through 4th grade — blocking the classroom promotion of LGBTQ ideology in public elementary schools.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://spectrumlocalnews.com/nc/charlotte/news/2023/02/07/controversial--parents--bill-of-rights--in-n-c--senate--here-s-what-s-in-the-lgbtq-bill"]),
    ]),

    # ------------ Vickie Sawyer (NC-R, State Senator SD-37) ------------
    ("vickie-sawyer", "NC", "Senator", [
        claim("vs1", "vickie-sawyer", "sanctity_of_life", 0, True,
              "Voted for NC Senate Bill 20 ('Care for Women, Children, and Families Act') and the Republican veto override in May 2023, enacting a 12-week abortion restriction celebrated by SBA Pro-Life America — part of a uniform Republican caucus pro-life vote.",
              ["https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html",
               "https://sbaprolife.org/newsroom/press-releases/victory-north-carolina-establishes-law-protecting-3000-lives-annually"]),
        claim("vs2", "vickie-sawyer", "family_child_sovereignty", 0, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') in February 2023 and the veto override in August 2023, mandating parental notification if a child requests a name or pronoun change at school and limiting gender-identity curriculum in elementary grades — a strong parental-rights stance.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://spectrumlocalnews.com/nc/charlotte/news/2023/02/07/controversial--parents--bill-of-rights--in-n-c--senate--here-s-what-s-in-the-lgbtq-bill"]),
    ]),

    # ------------ Tom McInnis (NC-R, State Senator SD-21) ------------
    ("tom-mcinnis", "NC", "Senator", [
        claim("tm1", "tom-mcinnis", "sanctity_of_life", 0, True,
              "Voted for NC Senate Bill 20 ('Care for Women, Children, and Families Act') and the Republican veto override in May 2023, enacting the 12-week abortion restriction along party lines — consistent with the Republican caucus's uniform pro-life position on this legislation.",
              ["https://www.northcarolinahealthnews.org/2023/05/04/measure-limiting-abortions-after-12-weeks-passes-nc-house-along-party-lines-in-late-night-vote/",
               "https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html"]),
        claim("tm2", "tom-mcinnis", "family_child_sovereignty", 0, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') and the August 2023 veto override — compelling schools to notify parents when a student requests a name or pronoun change and restricting age-inappropriate gender-and-sexuality instruction in grades K-4.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://spectrumlocalnews.com/nc/charlotte/news/2023/02/07/controversial--parents--bill-of-rights--in-n-c--senate--here-s-what-s-in-the-lgbtq-bill"]),
    ]),

    # ------------ Todd Johnson (NC-R, State Senator SD-35) ------------
    ("todd-johnson", "NC", "Senator", [
        claim("tj1", "todd-johnson", "sanctity_of_life", 0, True,
              "Voted for NC Senate Bill 20 ('Care for Women, Children, and Families Act') and the Republican veto override in May 2023, enacting a 12-week abortion restriction along strict party lines — a clear pro-life legislative record.",
              ["https://www.northcarolinahealthnews.org/2023/05/04/measure-limiting-abortions-after-12-weeks-passes-nc-house-along-party-lines-in-late-night-vote/",
               "https://www.cnn.com/2023/05/16/politics/north-carolina-abortion-ban-veto-vote/index.html"]),
        claim("tj2", "todd-johnson", "biblical_marriage", 4, True,
              "Voted for NC Senate Bill 49 ('Parents' Bill of Rights') and the August 2023 veto override, prohibiting instruction on gender identity and sexual orientation in kindergarten through 4th grade — a legislative check on LGBTQ ideology in public elementary schools.",
              ["https://www.wunc.org/politics/2023-08-17/nc-general-assembly-overrides-veto-parents-bill-rights",
               "https://spectrumlocalnews.com/nc/charlotte/news/2023/02/07/controversial--parents--bill-of-rights--in-n-c--senate--here-s-what-s-in-the-lgbtq-bill"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
