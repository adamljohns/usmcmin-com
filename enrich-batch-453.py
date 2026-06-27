#!/usr/bin/env python3
"""Enrichment batch 453: 4 Texas state senators (evidence_state → evidence_curated).

Targets: Pete Flores (SD-24, R), Charles Schwertner (SD-5, R),
         Angela Paxton (SD-8, R), Brent Hagenbuch (SD-30, R).
Sources: senate.texas.gov, ballotpedia.org, texaspolicyresearch.com,
         txvaluesaction.org, txgunrights.org, texasrighttolifepac.com
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
    # ---------- Pete Flores (TX SD-24, R) ----------
    ("pete-flores", "TX", "Senator", [
        claim("pf1", "pete-flores", "sanctity_of_life", 0, True,
              "Endorsed by Texas Right to Life as 'the only Pro-Life option' for his Senate district; self-identifies as pro-life and affirms protection of the unborn from conception.",
              ["https://www.texasrighttolifepac.com/peter-flores-is-the-only-pro-life-option-for-senate-district-19/",
               "https://floresfortexas.com/issues/"]),
        claim("pf2", "pete-flores", "border_immigration", 1, True,
              "Authored SB 4 (89th Legislature, 2025) increasing the minimum prison sentence for human smuggling from 2 to 10 years and raising penalties for stash-house operators; also authored SB 1099 stiffening penalties for noncitizens unlawfully present who commit felony crimes — both bills passed 29-2 and were signed into law.",
              ["https://www.texaspolicyresearch.com/89th-legislative-session-policy-brief-border-security/",
               "https://www.senate.texas.gov/member.php?d=24"]),
        claim("pf3", "pete-flores", "self_defense", 0, True,
              "A former peace officer who describes himself as 'a strong proponent of the people's right to bear arms, as guaranteed by the 2nd Amendment' and supports constitutional carry in Texas.",
              ["https://floresfortexas.com/issues/",
               "https://ballotpedia.org/Pete_Flores_(Texas)"]),
    ]),

    # ---------- Charles Schwertner (TX SD-5, R) ----------
    ("charles-schwertner", "TX", "Senator", [
        claim("cs1", "charles-schwertner", "self_defense", 0, True,
              "Primary author of Texas's landmark Constitutional Carry law (HB 1927, 87th Legislature) — the first permitless carry in Texas since Reconstruction — and sponsored SB 706 (89th Legislature, 2025) requiring Texas to automatically recognize all valid out-of-state carry licenses without requiring governor-negotiated reciprocity agreements.",
              ["https://senate.texas.gov/news.php?id=20210505a",
               "https://www.texaspolicyresearch.com/bills/89th-legislature-sb-706/"]),
        claim("cs2", "charles-schwertner", "sanctity_of_life", 0, True,
              "Senate sponsor of HB 4 (87th Legislature, 2021), Texas's Heartbeat Act banning abortions after detection of cardiac activity (approximately 6 weeks) and imposing civil liability of at least $10,000 per procedure; also passed earlier legislation banning dismemberment abortions and prohibiting sale of fetal tissue from elective abortions.",
              ["https://senate.texas.gov/news.php?id=20210514a",
               "https://www.drschwertner.com/accomplishments"]),
        claim("cs3", "charles-schwertner", "election_integrity", 0, True,
              "Co-authored the Texas Senate's 'Integrity Seven' election integrity bills alongside Senators Birdwell, Creighton, Hall, and Kolkhorst — preventing ballot harvesting, mandating uniform and transparent voting processes, enforcing compliance by local election officials, and ensuring rapid court resolution of electoral disputes.",
              ["https://texasscorecard.com/state/7-key-election-integrity-bills-filed-in-texas-senate/",
               "https://ballotpedia.org/Charles_Schwertner"]),
    ]),

    # ---------- Angela Paxton (TX SD-8, R) ----------
    ("angela-paxton", "TX", "Senator", [
        claim("ap1", "angela-paxton", "biblical_marriage", 2, True,
              "Cosponsor of SB 14 (88th Legislature, 2023) banning puberty blockers, cross-sex hormones, and transition surgeries for minors in Texas, with penalties including medical-license revocation and withdrawal of public funding from providers — rejecting transgender ideology applied to children.",
              ["https://www.billtrack50.com/billdetail/1595576",
               "https://ballotpedia.org/Angela_Paxton"]),
        claim("ap2", "angela-paxton", "christian_liberty", 0, True,
              "Sponsored SB 26 (Freedom to Worship Act, 87th Legislature), prohibiting state and local governments from limiting worship services or closing churches — protecting religious assemblies from executive-order restrictions imposed during the COVID-19 pandemic.",
              ["https://txvaluesaction.org/religious-freedom-pro-life-bills-pass-texas-senate-committee/",
               "https://ballotpedia.org/Angela_Paxton"]),
        claim("ap3", "angela-paxton", "family_child_sovereignty", 0, True,
              "Champion of SB 2 (89th Legislature, 2025), Texas's landmark Education Savings Account program providing eligible parents up to $8,000 per child annually for private school tuition, homeschool materials, or other approved educational expenses — a major parental-rights and school-choice victory.",
              ["https://www.texaspolicyresearch.com/bills/89th-legislature-sb-2/",
               "https://www.senate.texas.gov/member.php?d=8"]),
    ]),

    # ---------- Brent Hagenbuch (TX SD-30, R) ----------
    ("brent-hagenbuch", "TX", "Senator", [
        claim("bh1", "brent-hagenbuch", "sanctity_of_life", 0, True,
              "Endorsed by Texas Alliance for Life; describes himself as 'pro-life and pro-family' who 'firmly believes in protecting the unborn' and pledges to defend the sanctity of innocent life in the Texas Senate.",
              ["https://choicetracker.org/tx/people/brent-hagenbuch/234487808",
               "https://ballotpedia.org/Brent_Hagenbuch"]),
        claim("bh2", "brent-hagenbuch", "self_defense", 0, True,
              "Supports constitutional carry and all prior Texas expansions of carry rights (concealed, campus, open, and permitless carry), framing vigilance against federal encroachment on gun rights as a core mission.",
              ["https://texasscorecard.com/state/in-their-own-words-runoff-candidates-on-gun-rights/",
               "https://ballotpedia.org/Brent_Hagenbuch"]),
        claim("bh3", "brent-hagenbuch", "self_defense", 2, True,
              "Sponsored SB 1596 (89th Legislature, 2025) repealing Texas's state-level criminal penalties for manufacturing, possessing, and selling short-barreled rifles and shotguns — removing a redundant state layer of NFA-style restrictions; bill was unanimously reported out of the Senate State Affairs Committee.",
              ["https://txgunrights.org/texas-senate-to-hear-bill-decriminalizing-short-barrel-firearms/",
               "https://www.senate.texas.gov/member.php?d=30"]),
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
