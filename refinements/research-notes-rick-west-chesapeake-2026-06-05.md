# Rick West (Mayor of Chesapeake, VA) — research notes preserved for next batch

**Reason held back from 2026-06-05 batch-42:** slug `rick-west` collides with a second `level=state` Oklahoma House Rep candidate. `refine-records.py` builds `by_slug` as a flat dict and matches the later (Oklahoma) record. Adam should rename the OK record (e.g. to `rick-west-ok-hd3`) before re-running this dossier so the Chesapeake mayor record can be refined cleanly.

When the slug is disambiguated, paste the block below into the next dossier under `records`:

```json
"rick-west": {
  "set": {"status": "active", "party": "R"},
  "profile": {
    "confidence": "evidence_local",
    "background": "Dr. Richard Wayne 'Rick' West. Mayor of City of Chesapeake, VA since November 14, 2017 (initially appointed when prior mayor stepped down; won 2018 special election 57.81%, re-elected 2020 with 65.99%, re-elected November 5, 2024). Current term ends January 1, 2029. Public-school administrator in Chesapeake Public Schools for 20+ years (holds doctorate); served 10 years on Chesapeake City Council before becoming mayor. Born and raised in rural Chesapeake; father served U.S. Navy."
  },
  "sources_add": [
    "https://www.cityofchesapeake.net/1893/City-Council-Members",
    "https://ballotpedia.org/Richard_West_(Virginia)",
    "https://www.13newsnow.com/article/news/local/mycity/chesapeake/chesapeake-mayor-proclaims-june-pride-month-1st-time-city-history-local-lgbt-org/291-a18dfda2-8552-4559-9331-213337719e43",
    "https://www.wtkr.com/2019/12/10/massive-crowd-of-second-amendment-sanctuary-supporters-turn-out-to-chesapeake-city-council-meeting",
    "https://www.wavy.com/news/local-news/chesapeake/chesapeake-to-vote-on-second-amendment-sanctuary-resolution-at-tuesday-night-meeting/",
    "https://www.wavy.com/news/local-news/chesapeake/chesapeake-fy25-budget-keeps-real-estate-tax-rate-funds-raises-for-city-employees-teachers/",
    "https://www.whro.org/local-government/2024-08-15/chesapeake-mayor-asked-city-attorney-to-look-into-stepbrothers-personal-legal-issue"
  ],
  "notes_set": "Mayor of Chesapeake, VA (R) since Nov 2017; re-elected Nov 5, 2024 (term to Jan 1, 2029). [2026-06 RESOLUTE refinement] HARD evidence: (a) presided over Dec 10 2019 unanimous Chesapeake City Council adoption of a 'Second Amendment Constitutional City' resolution and personally pledged 'we will not just tell you to go to Richmond, we will go to Richmond with you' to constituents opposing Northam-era state gun bills (self_defense q0/q1 TRUE); (b) issued Chesapeake's FIRST-EVER Pride Month proclamation in June 2024 from the dais ('I Richard West, Mayor of the City of Chesapeake, do hereby proclaim the month of June as PRIDE MONTH') (biblical_marriage q4 FALSE); (c) FY25 budget held real-estate tax rate flat at $1.01/$100 and FY26 proposed rate increase was 'no longer being considered' after public pushback (economic_stewardship q2 TRUE on nominal rate; rising assessments yielded effective-rate growth but the rate itself was held). NO EVIDENCE on abortion, family/school, Christian liberty, election administration, COVID-mandate resistance, ESG, or immigration at the mayoral level — those cells null. Affirmative public 'Back the Blue' advocacy not located — public_justice q0 null (routine budget funding alone does not clear the rubric's high bar). Religion / church affiliation not publicly stated. Flag: August 2024 WHRO report that West asked city attorney to 'look into' a personal legal matter for his stepbrother (Georgia property dispute) drew an ethics-flag and a councilman's resignation call — noted as governance-conduct context, not a rubric-scoring event.",
  "evidence": {
    "biblical_marriage": {
      "4": {"v": false, "src": ["https://www.13newsnow.com/article/news/local/mycity/chesapeake/chesapeake-mayor-proclaims-june-pride-month-1st-time-city-history-local-lgbt-org/291-a18dfda2-8552-4559-9331-213337719e43"], "note": "Mayor West personally issued Chesapeake's first-ever Pride Month proclamation, June 2024, from the dais at a city council meeting."}
    },
    "economic_stewardship": {
      "2": {"v": true, "src": ["https://www.wavy.com/news/local-news/chesapeake/chesapeake-fy25-budget-keeps-real-estate-tax-rate-funds-raises-for-city-employees-teachers/"], "note": "FY25 budget held real-estate tax rate flat at $1.01/$100; FY26 proposed rate increase was withdrawn after public pushback."}
    },
    "self_defense": {
      "0": {"v": true, "src": ["https://www.wtkr.com/2019/12/10/massive-crowd-of-second-amendment-sanctuary-supporters-turn-out-to-chesapeake-city-council-meeting"], "note": "Presided over Dec 10 2019 unanimous Chesapeake City Council adoption of a Second Amendment 'Constitutional City' resolution; pledged 'we will not just tell you to go to Richmond, we will go to Richmond with you.'"},
      "1": {"v": true, "src": ["https://www.wavy.com/news/local-news/chesapeake/chesapeake-to-vote-on-second-amendment-sanctuary-resolution-at-tuesday-night-meeting/"], "note": "Same 2019 2A-sanctuary resolution opposing Northam-era state red-flag / AWB / magazine-limit bills; mayor publicly led the local-control pushback."}
    }
  }
}
```

Note that `refuse_state_overreach[0]` evidence was also found (same 2019 2A resolution) but is **tier=state** per `applicable_at` in the rubric, so engine ignores it — leave it out of the dossier or it'll log a warning.
