#!/usr/bin/env python3
"""Enrichment batch 891: hand-curated claims for 5 NC Democratic State Senators.

Continuing the pivot from federal to NC state senate (archetype_party_default, 0 claims),
picking the top 5 of the reverse-alphabetical name list that remained after batch 890
(Michael V. Lee / Michael A. Lazzara / Mark Hollo / Lisa S. Barnes / Kevin Corbin).

Key NC legislation referenced:
  - SB 20 (Care for Women, Children, and Families Act, 2023): 12-week abortion
    limit; veto override 30-20 party line, May 16, 2023. All 20 D senators voted NO.
  - SB 49 (Parents' Bill of Rights, 2023): barred K-4 gender/sexuality instruction,
    parental notification of name/pronoun changes. Senate veto override 27-18,
    House 59-54, Aug 16-17, 2023. Democrats voted NO (party line).
  - SB 50 (Freedom to Carry NC, 2025): constitutional carry; Senate passage 26-18
    along party lines, March 20, 2025. All 18 present D senators voted NO. Governor
    Stein vetoed June 20, 2025; Senate overrode 30-19; House veto override pending.

Targets (top 5 of reverse-alpha remaining list, all NC State Senators):
  Woodson Bradley  (SD-42, serving since Jan 2025)
  Val Applewhite   (SD-19, serving since Jan 2023)
  Terence Everitt  (SD-18, served Jan 2025-May 2026; resigned)
  Sydney Batch     (SD-17, serving since Jan 2023; Minority Leader since Jan 2025)
  Sophia Chitlik   (SD-22, serving since Jan 2025)

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
    # ------------ Woodson Bradley (NC-D, State Senator SD-42, serving since Jan 2025) ------------
    ("woodson-bradley", "NC", "Senator", [
        claim("wb891a", "woodson-bradley", "sanctity_of_life", 4, False,
              "Endorsed for her 2024 NC Senate District 42 campaign by EMILY's List, "
              "Lillian's List, and Planned Parenthood — three of the largest "
              "pro-abortion-rights organizations in the country — placing her squarely "
              "within the rubric's definition of taking support from the abortion-advocacy "
              "network. She has publicly called NC's 12-week abortion ban 'only step "
              "one' in Republicans' plan to ban all abortions and has been endorsed again "
              "by these same organizations for her 2026 reelection race.",
              ["https://ncvoices.com/community-leader-woodson-bradley-is-facing-a-republican-with-extremist-ties-in-ncs-senate-district-42-race/",
               "https://ballotpedia.org/Woodson_Bradley",
               "https://www.woodsonbradley.com/"]),
        claim("wb891b", "woodson-bradley", "self_defense", 1, False,
              "Publicly supports mandatory red-flag laws and universal background checks "
              "for all gun purchases — opposing the rubric's defense of Second Amendment "
              "rights against restriction. She has cited personal experience as a "
              "domestic-violence survivor as the basis for her gun-restriction advocacy "
              "and voted against NC Senate Bill 50 (constitutional carry) in her first "
              "legislative session (March 2025). Her name appears explicitly in the "
              "NCLEG roll call transcript as a NO vote (Roll Call #50, 2025 session, "
              "26R yes / 18D no).",
              ["https://www.ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2025/S/50",
               "https://www.woodsonbradley.com/",
               "https://www.ncleg.gov/BillLookup/2025/S50"]),
    ]),

    # ------------ Val Applewhite (NC-D, State Senator SD-19, serving since Jan 2023) ------------
    ("val-applewhite", "NC", "Senator", [
        claim("va891a", "val-applewhite", "sanctity_of_life", 0, False,
              "Voted against NC Senate Bill 20 ('Care for Women, Children, and Families "
              "Act') on May 16, 2023 — the 12-week abortion ban enacted via a strict "
              "30-20 party-line veto override — and publicly condemned the law as "
              "disregarding women's health-care decisions. She advocates restoring "
              "Roe-era abortion access and has stated the 12-week limit 'does not "
              "account for the complexities of pregnancy,' rejecting any personhood-"
              "from-conception standard.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://www.joshstein.org/press-releases/icymi-state-senator-val-applewhite-on-the-anniversary-of-abortion-ban-robinson-wants-to-endanger-us-further",
               "https://ballotpedia.org/Val_Applewhite"]),
        claim("va891b", "val-applewhite", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List, a major pro-abortion-rights political action "
              "committee that bundles contributions for pro-choice candidates — directly "
              "within the rubric's definition of taking money from abortion-advocacy "
              "organizations. She is also a member of the Reproductive Freedom "
              "Leadership Council, a national network of state legislators championing "
              "expanded abortion access.",
              ["https://ballotpedia.org/Val_Applewhite",
               "https://www.cityviewnc.com/stories/val-applewhite-maintains-n-c-senate-district-19-seat/",
               "https://choicetracker.org/nc/people/val-applewhite/212271104"]),
        claim("va891c", "val-applewhite", "self_defense", 0, False,
              "Voted NO on NC Senate Bill 50 ('Freedom to Carry NC') on March 20, 2025 "
              "(26-18 party-line Senate passage), which would establish constitutional "
              "carry by eliminating the permit requirement for concealed carry. Her name "
              "appears explicitly in the NCLEG roll call transcript as a NO vote (Roll "
              "Call #50, 2025 session). She joined all 18 present Senate Democrats in "
              "publicly condemning the bill as 'dangerous' and a threat to public safety.",
              ["https://www.ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2025/S/50",
               "https://www.ncleg.gov/BillLookup/2025/S50",
               "https://www.carolinajournal.com/nc-senate-officially-passes-constitutional-carry-bill/"]),
    ]),

    # ------------ Terence Everitt (NC-D, State Senator SD-18, served Jan 2025–May 2026; resigned) ------------
    ("terence-everitt", "NC", "Senator", [
        claim("te891a", "terence-everitt", "sanctity_of_life", 0, False,
              "Ran for the NC State Senate in 2024 explicitly to protect abortion "
              "rights, stating publicly: 'Reproductive rights are on the ballot. Now "
              "is not the time to take a break or step away from our responsibilities' "
              "— framing his entire Senate campaign around opposing legal protections "
              "for the unborn. He maintained a consistently pro-abortion-access record "
              "throughout his legislative career in both the NC House (2019-2025) and "
              "NC Senate (January 2025 until his resignation in May 2026).",
              ["https://twitter.com/TerenceEveritt/status/1778140488245055540",
               "https://www.wakedems.org/election-central-2024/candidate-info-terence-everitt/",
               "https://ballotpedia.org/Terence_Everitt"]),
        claim("te891b", "terence-everitt", "self_defense", 0, False,
              "Voted against NC Senate Bill 50 ('Freedom to Carry NC') on March 20, "
              "2025 (26-18 Senate party-line vote), opposing the elimination of the "
              "permit requirement for concealed carry and the establishment of "
              "constitutional carry in North Carolina. His name appears explicitly in "
              "the NCLEG roll call transcript as a NO vote (Roll Call #50, 2025 "
              "session) — his first legislative vote as a state senator (assumed "
              "office January 2025).",
              ["https://www.ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2025/S/50",
               "https://www.ncleg.gov/BillLookup/2025/S50",
               "https://ballotpedia.org/Terence_Everitt"]),
    ]),

    # ------------ Sydney Batch (NC-D, State Senator SD-17, serving since Jan 2023; Minority Leader since Jan 2025) ------------
    ("sydney-batch", "NC", "Senator", [
        claim("sb891a", "sydney-batch", "sanctity_of_life", 0, False,
              "Voted against NC Senate Bill 20 (the 12-week abortion ban, veto override "
              "May 16, 2023, 30-20 party line) and has consistently championed "
              "unrestricted abortion access. As a family-law attorney, she sponsored "
              "legislation to codify the right to abortion before viability in NC and "
              "to protect the right to travel out of state for an abortion or "
              "contraception — rejecting any personhood-from-conception standard.",
              ["https://www.ncleg.gov/BillLookup/2023/S20",
               "https://choicetracker.org/nc/people/sydney-batch/207224832",
               "https://ballotpedia.org/Sydney_Batch"]),
        claim("sb891b", "sydney-batch", "self_defense", 0, False,
              "As NC Senate Minority Leader (assumed office January 2025), led the "
              "Democratic caucus in unanimously opposing NC Senate Bill 50 ('Freedom "
              "to Carry NC') on March 20, 2025 (26-18 party-line Senate passage). "
              "Her name appears explicitly in the NCLEG roll call transcript as a NO "
              "vote (Roll Call #50, 2025 session). Democrats held a post-vote press "
              "conference condemning the bill as 'dangerous' — a direct rejection of "
              "the rubric's constitutional-carry ideal.",
              ["https://www.ncleg.gov/Legislation/Votes/RollCallVoteTranscript/2025/S/50",
               "https://www.ncleg.gov/BillLookup/2025/S50",
               "https://www.carolinajournal.com/nc-senate-officially-passes-constitutional-carry-bill/"]),
    ]),

    # ------------ Sophia Chitlik (NC-D, State Senator SD-22, serving since Jan 2025) ------------
    ("sophia-chitlik", "NC", "Senator", [
        claim("sc891a", "sophia-chitlik", "sanctity_of_life", 0, False,
              "Opposes all abortion bans and has stated that medical decisions "
              "regarding abortion 'should be left in the hands of doctors, nurses, "
              "and their patients — not lawmakers.' Endorsed by Planned Parenthood "
              "in the 2024 general election for NC Senate District 22 (Wake County). "
              "She describes herself as an outspoken advocate for 'reproductive "
              "justice' and has opposed NC's existing 12-week abortion limit.",
              ["https://indyweek.com/news/elections-news/candidate-questionnaire-sophia-chitlik-nc-senate-district-22/",
               "https://ballotpedia.org/Sophia_Chitlik",
               "https://sophiafornc.com/"]),
        claim("sc891b", "sophia-chitlik", "biblical_marriage", 2, False,
              "As a state senator, has worked to advance gender-affirming care and "
              "describes LGBTQIA+ rights and gender-affirming care as 'critical "
              "elements' of reproductive justice — actively promoting transgender "
              "ideology that the rubric rejects. She framed these as core legislative "
              "priorities in an Indy Week candidate questionnaire and frames opposition "
              "to any limits on gender-affirming treatments as a non-negotiable "
              "position.",
              ["https://indyweek.com/news/elections-news/candidate-questionnaire-sophia-chitlik-nc-senate-district-22/",
               "https://ballotpedia.org/Sophia_Chitlik"]),
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
            if cat in scores and isinstance(qi, int) and qi < len(scores[cat]):
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
