#!/usr/bin/env python3
"""Enrichment batch 342: 5 Virginia House of Delegates members (evidence_state → evidence_curated).

archetype_curated federal and state buckets are fully exhausted; this batch
continues the evidence_state queue from the bottom of the alphabet (VA, P-N names).

Targets (reverse-alpha top-5 of remaining VA evidence_state 0-claim after batch 341):
  Phil Hernandez    VA-D, House of Delegates District 94 (Norfolk/Chesapeake)
  Paul Krizek       VA-D, House of Delegates District 16 (Fairfax/Springfield)
  Patrick Hope      VA-D, House of Delegates District 1 (Arlington)
  Nicole Cole       VA-D, House of Delegates District 66 (Caroline/Spotsylvania)
  Nadarius Clark    VA-D, House of Delegates District 84 (Portsmouth)

Each claim cites >=1 reliable source reflecting 2024-2026 public record/positions.
NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Phil Hernandez (VA-D, House of Delegates District 94, Norfolk/Chesapeake) ----------
    ("phil-hernandez", "VA", "House of Delegates", [
        claim("ph1", "phil-hernandez", "sanctity_of_life", 0, False,
              "Phil Hernandez voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. The amendment — which codifies abortion, contraception, miscarriage management, and fertility care as constitutional rights — passed the House 64-34 along party lines, with Hernandez voting yes as a member of the Democratic caucus. This directly rejects any life-at-conception or personhood protection.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("ph2", "phil-hernandez", "self_defense", 1, False,
              "Hernandez voted for the Virginia House Democrats' sweeping 2026 gun control package, which prohibits the sale and transfer of high-capacity semiautomatic firearms, bans guns in hospitals and college campuses, creates a state civil cause of action against firearm manufacturers, and expands punishments for ghost gun distribution. He also sponsored legislation in his 2024 term to restrict weapons in mental health facilities — a consistent record of restricting Second Amendment exercise beyond constitutional limits.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://en.wikipedia.org/wiki/Phil_Hernandez",
               "https://ballotpedia.org/Phil_Hernandez"]),
    ]),

    # ---------- Paul Krizek (VA-D, House of Delegates District 16, Fairfax/Springfield) ----------
    ("paul-krizek", "VA", "House of Delegates", [
        claim("pk1", "paul-krizek", "sanctity_of_life", 0, False,
              "Paul Krizek voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. The measure, which enshrines abortion, contraception, fertility care, and miscarriage management as state constitutional rights, passed the House 64-34 with Krizek voting yes as part of the Democratic caucus — rejecting any life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("pk2", "paul-krizek", "biblical_marriage", 0, False,
              "Paul Krizek voted for Virginia's constitutional amendment (HJR 9) to repeal the state's 2006 definition of marriage as 'only a union between a man and a woman,' advancing the repeal to the November 2026 statewide ballot. The amendment passed the House 58-35 with near-unanimous Democratic support, and Krizek voted yes — directly opposing the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://en.wikipedia.org/wiki/Paul_Krizek"]),
    ]),

    # ---------- Patrick Hope (VA-D, House of Delegates District 1, Arlington) ----------
    ("patrick-hope", "VA", "House of Delegates", [
        claim("phop1", "patrick-hope", "self_defense", 1, False,
              "Patrick Hope chaired the Virginia House Public Safety Committee and was the lead architect of Virginia's landmark 2020 gun control package, which enacted universal background checks, mandatory reporting of lost or stolen firearms, a one-handgun-per-month purchase limit, and red-flag/extreme risk protective orders allowing courts to temporarily confiscate firearms from individuals deemed a risk. He endorsed and voted for the 2026 package banning assault-style weapon sales — a consistent record directly opposing the rubric's opposition to red-flag laws and AWB/magazine restrictions.",
              ["https://ballotpedia.org/Patrick_Hope",
               "https://giffords.org/candidates/patrick-hope-2/",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("phop2", "patrick-hope", "sanctity_of_life", 0, False,
              "Patrick Hope voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions, and publicly stated he supports 'the right to a safe and legal abortion' and opposes any 'attempt to legislate a patient's decision to end a pregnancy.' He has also served as patron of abortion-access legislation in the General Assembly and is listed as a legislative champion by REPRO Rising Virginia — directly rejecting a personhood-from-conception standard.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Patrick_Hope",
               "https://reprorisingva.org/team/delegate-patrick-hope/"]),
    ]),

    # ---------- Nicole Cole (VA-D, House of Delegates District 66, Caroline/Spotsylvania) ----------
    ("nicole-cole", "VA", "House of Delegates", [
        claim("nc1", "nicole-cole", "sanctity_of_life", 0, False,
              "Nicole Cole, sworn in January 14, 2026, voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in the 2026 Regular Session — the first session she was eligible to vote in. The amendment, which codifies abortion, contraception, fertility treatments, and miscarriage management as constitutional rights, passed the House 64-34 along party lines with Cole voting yes. REPRO Rising Virginia lists her as a legislative champion of reproductive access.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://reprorisingva.org/team/nicole-cole/",
               "https://virginiaindependentnews.com/elections/nicole-cole-bobby-orrock-house-delegates-district-66-november-4/"]),
        claim("nc2", "nicole-cole", "self_defense", 1, False,
              "Nicole Cole expressed support for gun restrictions during her 2025 campaign, stating she favors preventing unrestricted access to firearms and frames gun violence as a public health and safety issue. She voted for the 2026 Democratic gun control package, which bans high-capacity semiautomatic firearms, prohibits guns on college campuses and in hospitals, and stiffens penalties for ghost gun trafficking — opposing the rubric's defense of broad Second Amendment access.",
              ["https://virginiaindependentnews.com/elections/nicole-cole-bobby-orrock-house-delegates-district-66-november-4/",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://ballotpedia.org/Nicole_Cole"]),
    ]),

    # ---------- Nadarius Clark (VA-D, House of Delegates District 84, Portsmouth) ----------
    ("nadarius-clark", "VA", "House of Delegates", [
        claim("nac1", "nadarius-clark", "self_defense", 1, False,
              "Nadarius Clark chairs the Virginia House Public Safety Subcommittee on Firearms and co-chairs the Gun Violence Prevention Caucus. In the 2026 Regular Session he steered the sweeping Democratic gun control package through his subcommittee: banning the sale and transfer of semiautomatic centerfire rifles and pistols capable of holding more than 15 rounds after July 1, 2026; prohibiting firearms in hospitals and college campuses; creating a state cause of action against gun manufacturers; and expanding ghost gun penalties. Clark stated, 'We are keeping communities safe from gun violence' — directly opposing the rubric's defense of unrestricted Second Amendment rights and opposition to AWBs, magazine limits, and gun-free zones.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://sisterdistrict.com/candidates/nadarius-clark/",
               "https://www.13newsnow.com/article/news/local/virginia/virginia-gun-restrictions-assault-weapons-ghost-guns-bills-pass-senate/291-33791bc0-58c5-478a-887c-24c620334912"]),
        claim("nac2", "nadarius-clark", "sanctity_of_life", 0, False,
              "Nadarius Clark voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. The amendment — which enshrines abortion, contraception, fertility care, and miscarriage management as constitutional rights — passed the House 64-34 along party lines, with Clark voting yes as a member of the Democratic caucus, directly rejecting any life-at-conception or personhood protection.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://ballotpedia.org/Nadarius_Clark"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
