# VA RESOLUTE Sprint — Gaps & Dense-Thin Queue

**Date:** 2026-07-18  
**Inputs:** `data/scorecard.json` inventory + web verification + prior [`va-sprint-2026-07-18-research.md`](va-sprint-2026-07-18-research.md)  
**Citizen Q&A twin:** [`va-q-and-a-2026-07-18.md`](va-q-and-a-2026-07-18.md)  
**Constraint:** Research/write only — **scorecard.json not modified**.

**Dens definition used here:** count of score cells that are strictly `True` or `False`. Strings like `"N/A"` and `None` are **not** dens. (Prior dry-run tables that showed dens=0 for FXBG council while N/A grids were filled match this definition.)

---

## 1. Inventory (all VA slugs)

| Bucket | n |
|--------|--:|
| Total VA (`state == "VA"`) | **296** |
| Active | 285 |
| Lost | 6 |
| Former | 5 |
| Level | state 146 · local 122 · federal 28 |
| Confidence | evidence_curated 155 · evidence_local 119 · evidence_federal 11 · evidence_state 7 · roster_verified 2 · party_default 1 · status_hygiene_only 1 |

### Active dens distribution (True/False only)

| dens | active n | notes |
|-----:|---------:|-------|
| 0 | 9 | all local |
| 1 | 28 | FXBG + Hampton Roads heavy |
| 2 | 17 | |
| 3–5 | 74 | includes most Spotsy/Stafford BoS |
| 6–10 | 59 | |
| 11–15 | 24 | |
| 16–20 | 18 | many House incumbents |
| 21–26 | 7 | top: Walkinshaw 26, Griffith 21, Spanberger 21, Beyer 20… |

**Local thinness:** 91 of 118 active locals have dens ≤ 5; **116/118** have dens ≤ 10.

---

## 2. Q&A answers (research brief)

### 2.1 Sitting statewide trio (2026)

| Office | Who | Slug | dens | Web |
|--------|-----|------|-----:|-----|
| Governor | Abigail Spanberger (D) | `abigail-spanberger` | 21 | https://www.vpm.org/news/2026-01-17/watch-inaugural-interviews-with-abigail-spanberger-ghazala-hashmi-and-jay-jones |
| Lt. Governor | Ghazala Hashmi (D) | `ghazala-hashmi` | 17 | https://www.ltgov.virginia.gov/ |
| Attorney General | Jay Jones (D) | `jay-jones` | 12 | same VPM inaugural package |

Sworn **Jan 17, 2026**. Hashmi first Muslim woman elected statewide (U.S.); Jones first Black VA AG. Losers retained: `winsome-earle-sears` (41), `jason-miyares-ag-2026` (25), `john-reid` (27).

**Gap rank:** Jones dens 12 is the thinnest **sitting** statewide executive — priority for 2026 AG actions / litigation / opinions, not just HD-89 history.

### 2.2 FXBG City Council — full roster vs scorecard

Official: https://www.fredericksburgva.gov/263/Council-Members  

| Seat | Official | Slug | dens | Gap? |
|------|----------|------|-----:|------|
| Mayor At-Large | Kerry P. Devine | `kerry-devine` | 4 | thin |
| Vice Mayor Ward 4 | Charlie L. Frye, Jr. | `charlie-frye-jr` | 4 | thin |
| At-Large | Jannan W. Holmes | `jannan-holmes` | 1 | **very thin** |
| At-Large | Will B. Mackintosh | `will-mackintosh` | 5 | best on council |
| Ward 1 | Matt D. Rowe | `matt-rowe-fxbg` | 1 | new 2026 |
| Ward 2 | Joy Y. Crump | `joy-crump-fxbg` | 1 | new 2026 |
| Ward 3 | Susanna R. Finn | `susanna-finn` | 1 | new 2026 |

**Roster gap: none (7/7).** Evidence gap: **critical** for Crump/Rowe/Finn/Holmes. Do not invent dens from party labels.

FXBG school board is worse: `andy-wolfenbarger` dens **0**; five others dens **1**.

### 2.3 Spotsylvania BoS chair + dens

| Role | Name | Slug | dens |
|------|------|------|-----:|
| **Chair** Lee Hill | Lori Hayes (R) | `lori-hayes` | 6 |
| **Vice Chair** Courtland | Drew Mullins (R) | `drew-mullins` | 4 |
| Battlefield | Chris Yakabouski | `chris-yakabouski` | 4 |
| Berkeley | David Goosman | `david-goosman` | 5 |
| Chancellor | Gerald Childress | `gerald-childress` | 4 |
| Livingston | Jacob Lane | `jacob-lane` | 4 |
| Salem | Deborah Frazier | `deborah-frazier` | 4 |

Chair election coverage: https://www.fxbgadvance.com/p/news-first-spotsylvania-board-of  
County members: https://www.spotsylvania.va.us/1200/Members  

**Gap:** Vice-chair politics (Frazier mentioned in contested VC vote) — re-verify officer titles before citizen copy that names VC. Policy dens uniformly mid-single-digits; CA Mehaffey dens 8 is the thickest Spotsy local.

### 2.4 Stafford BoS key members

Official: https://staffordcountyva.gov/government/elected_and_appointed_officials/board_of_supervisors/index.php  
2026 org news: https://staffordcountyva.gov/news_detail_T5_R1132.php  

| Role | Name | dens |
|------|------|-----:|
| Chair GW | Deuntay Diggs (I) | 5 |
| Vice Chair Aquia | Maya Guy (D) | 4 |
| Falmouth | Kecia Evans (D) | 2 |
| Garrisonville | Pamela Yeung (D) | 6 |
| Griffis-Widewater | Tinesha Allen (D) | 3 |
| Hartwood | Darrell English (R) | 6 |
| Rock Hill | Crystal Vanuch (R) | **11** |

**Gap:** `eric-olsen` (Stafford CA) dens **1** — high-impact office, almost empty rubric. School board dens 1–2 on several seats.

### 2.5 VA U.S. House map (sitting)

| Dist | Incumbent | Party | dens | Slug |
|-----:|-----------|-------|-----:|------|
| 1 | Rob Wittman | R | 22 | `rob-wittman` |
| 2 | Jen Kiggans | R | 13 | `jen-kiggans` |
| 3 | Bobby Scott | D | 19 | `bobby-scott` |
| 4 | Jennifer McClellan | D | 9 | `jennifer-mcclellan` |
| 5 | John McGuire | R | 16 | `john-mcguire` |
| 6 | Ben Cline | R | 19 | `ben-cline` |
| 7 | Eugene Vindman | D | 18 | `eugene-vindman` |
| 8 | Don Beyer | D | 20 | `don-beyer` |
| 9 | Morgan Griffith | R | 21 | `morgan-griffith` |
| 10 | Suhas Subramanyam | D | 19 | `suhas-subramanyam-cd10` |
| 11 | James Walkinshaw | D | 26 | `james-walkinshaw` |

Connolly: `gerry-connolly` status **former**, dens 0, hygiene only.

Refs: https://ballotpedia.org/United_States_House_of_Representatives_elections_in_Virginia,_2026 · https://www.vpap.org/elections/us-house/ · https://www.vpap.org/redistricting/2026/

**Gap:** Mid-decade map litigation may reassign “district” labels; challenger hygiene (VA-02/VA-07 withdrawn still active); Tara Durant dual-office VA-07 run (`tara-durant` dens 13).

### 2.6 2026 U.S. Senate

| Fact | Detail | dens / status |
|------|--------|---------------|
| Seat up | **Warner Class 2** | `mark-warner` dens 9 · seeking reelection |
| Not up | **Kaine Class 1** through Jan 2031 | `tim-kaine` dens 11 |
| Hung Cao | **Not a 2026 candidate**; Acting SecNav since Apr 22, 2026 | `hung-cao-senate-2026` dens 2 · `not_running` |
| R primary field (web) | Farington, Mizusawa, Williams (Aug 4, 2026) | **not fully in scorecard as VA challenger set** |
| Independent (web) | Mark Moran | not scored as core record |

Sources:  
https://ballotpedia.org/United_States_Senate_election_in_Virginia,_2026  
https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Virginia  
https://www.vpap.org/elections/us-senate/  
https://www.navy.mil/Leadership/Flag-Officer-Biographies/BioDisplay/Article/4156165/acting-secretary-of-the-navy-hung-cao/  
https://en.wikipedia.org/wiki/Hung_Cao  

**Gap / hygiene:** Slug `hung-cao-senate-2026` is misleading for citizens; office string is correct. Warner dens 9 is thin for a multi-term senator vs House peers at 18–26.

---

## 3. Top 20 thinnest active VA (priority queue)

| # | dens | slug | office | jurisdiction |
|--:|-----:|------|--------|--------------|
| 1 | 0 | andy-wolfenbarger | School Board Ward 1 | Fredericksburg |
| 2 | 0 | ebony-wright | City Council Sleepy Hole | Suffolk |
| 3 | 0 | hope-harper | City Council | Hampton |
| 4 | 0 | leotis-williams | City Council Whaleyville | Suffolk |
| 5 | 0 | marcellus-harris | City Council North | Newport News |
| 6 | 0 | michelle-ferebee | City Council | Hampton |
| 7 | 0 | pat-king | City Council | Chesapeake |
| 8 | 0 | vernon-tillage | City Council | Portsmouth |
| 9 | 0 | william-dodson | City Council | Portsmouth |
| 10 | 1 | amelia-ross-hammond | City Council D4 | Virginia Beach |
| 11 | 1 | annie-langdon | School Board Ward 3 | Fredericksburg |
| 12 | 1 | ella-ward | City Council | Chesapeake |
| 13 | 1 | eric-olsen | Commonwealth’s Attorney | Stafford |
| 14 | 1 | jannan-holmes | City Council At-Large | Fredericksburg |
| 15 | 1 | jarvis-e-bailey | School Board At-Large | Fredericksburg |
| 16 | 1 | jeff-jefferies | City Council | Chesapeake |
| 17 | 1 | jeremy-mcgee | City Council SW6 | Norfolk |
| 18 | 1 | john-paige | City Council Ward 4 | Norfolk |
| 19 | 1 | josh-regan | School Board Aquia | Stafford |
| 20 | 1 | joshua-schulman | City Council D9 | Virginia Beach |

### Remaining active dens = 1 (beyond top 20 cut)

`joy-crump-fxbg` · `kathleen-katie-pomeroy` · `kathryn-bryant` · `lue-ward` · `malvina-rollins-kay` · `matt-rowe-fxbg` · `matthew-hamel` · `molly-mcfadden` · `nicole-jones-rva` · `randy-bowman` · `robert-coleman` · `sarah-abubaker` · `shavonda-fernandez` · `steven-brown` · `susanna-finn` · `wanda-blackwell` · `yolanda-thomas`

**Total active dens ≤ 1: 37** (9 + 28).

---

## 4. Complete list — active dens = 0

| slug | office | jurisdiction | party | conf |
|------|--------|--------------|-------|------|
| `andy-wolfenbarger` | School Board — Ward 1 | City of Fredericksburg | Unknown | evidence_local |
| `ebony-wright` | City Council - Sleepy Hole Borough | City of Suffolk | D | evidence_local |
| `hope-harper` | City Council | City of Hampton | Unknown | evidence_local |
| `leotis-williams` | City Council - Whaleyville Borough | City of Suffolk | I | evidence_local |
| `marcellus-harris` | City Council - North District | City of Newport News | I | evidence_local |
| `michelle-ferebee` | City Council | City of Hampton | Unknown | evidence_local |
| `pat-king` | City Council | City of Chesapeake | D | evidence_local |
| `vernon-tillage` | City Council | City of Portsmouth | I | evidence_local |
| `william-dodson` | City Council | City of Portsmouth | I | evidence_local |

No active federal or statewide dens=0. Connolly dens=0 is **former**.

---

## 5. Ranked unknowns / open questions

| Priority | Unknown | Why it matters | Suggested next action |
|---------:|---------|----------------|------------------------|
| P0 | Jones / Hashmi / Spanberger 2026 session actions | Statewide power; dens lag office | Bill signatures, AG letters, LG statements → refine only with HARD URLs |
| P0 | dens=0 nine locals | Profiles publish empty policy grids | Meeting minutes + votes; or mark confidence down if roster-only |
| P1 | FXBG school board dens 0–1 | Parent/citizen local impact | Board agendas 2024–2026 |
| P1 | Stafford CA dens 1 | Prosecutor power | Case policy, endorsements, Soros/reform links if any |
| P1 | 2026 Senate R primary not in scorecard | Citizen “who challenges Warner?” incomplete | Add Farington / Mizusawa / Williams as federal primary_candidate records when ready |
| P2 | VA-02/07 withdrawn still active | Noise in digests & search | candidacy_status hygiene batch |
| P2 | Redistricting map status | District labels may go stale | Track VPAP / SCOVA; don’t re-slug until map final |
| P2 | Warner dens 9 / McClellan dens 9 | Federal thin relative to peers | Federal vote backfill (Heritage / floor votes already partially sourced) |
| P3 | Party=Unknown on FXBG SB / Hampton | Citizen trust | Nonpartisan vs ballot party cleanup |
| P3 | Spotsy VC title edge case | Conflicting press color | Re-scrape county officer list |
| P3 | hung-cao slug naming | Confuses “2026 Senate” | Rename only via careful slug migration (out of scope for this sprint) |

---

## 6. Coverage checklist (this sprint’s asked topics)

| Topic | Scorecard solid? | Web verified? | Residual gap |
|-------|------------------|---------------|--------------|
| Sitting Gov/LG/AG | Yes | Yes | Jones dens thin for AG |
| FXBG council full roster | Yes 7/7 | Official page | dens 1–5 |
| Spotsy chair + dens | Yes | FXBG Advance + county | VC nuance |
| Stafford key members | Yes 7/7 | County site | CA dens 1 |
| VA House map | Yes 11 incumbents | Ballotpedia/VPAP | map litigation |
| 2026 Senate (Warner/Kaine/Cao) | Warner/Kaine/Cao yes | Yes | R primary field missing |
| Top 20 thinnest | Computed | n/a | research queue |
| dens=0 active list | Complete (9) | n/a | fill or hygiene |
| Unknowns | Listed | partial | ongoing |

---

## 7. Complete VA slug inventory (296)

### Full table

Generated from `data/scorecard.json` on 2026-07-18. dens = True/False cells only.

| slug | dens | status | candidacy_status | level | party | office | jurisdiction |
|------|-----:|--------|------------------|-------|-------|--------|--------------|
| `aaron-rouse` | 7 | active | incumbent | state | D | State Senate — District 22 | Virginia State Senate |
| `abigail-spanberger` | 21 | active | won | state | D | Governor (sitting · sworn Jan 17, 2026) | Commonwealth of Virginia |
| `adele-mcclure` | 9 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 2 | Virginia House of Delegates |
| `alex-askew` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 95 | Virginia House of Delegates |
| `alfonso-lopez` | 19 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 3 | Virginia House of Delegates |
| `amanda-newins` | 3 | active | — | local | R | City Council | City of Chesapeake |
| `amelia-ross-hammond` | 1 | active | general_candidate | local | I | City Council - District 4 | City of Virginia Beach |
| `amy-laufer` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 55 | Virginia House of Delegates |
| `andrew-breton` | 3 | active | incumbent_seeking_reelection | local | D | City Council — District 1 (West End) | City of Richmond |
| `andrew-rice` | 3 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 98 | Virginia House of Delegates |
| `andy-wolfenbarger` | 0 | active | — | local | Unknown | School Board — Ward 1 | City of Fredericksburg |
| `angelia-williams-graves` | 6 | active | incumbent_seeking_reelection | state | D | State Senate — District 21 | Virginia State Senate |
| `anne-ferrell-tata` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 99 | Virginia House of Delegates |
| `anne-holton` | 8 | active | general_candidate | local | D | School Board — District 6 | City of Richmond |
| `annie-langdon` | 1 | active | — | local | Unknown | School Board — Ward 3 | City of Fredericksburg |
| `anton-bell` | 6 | active | — | local | D | Commonwealth's Attorney | City of Hampton |
| `atoosa-reaser` | 8 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 27 | Virginia House of Delegates |
| `barbara-favola` | 12 | active | incumbent | state | D | State Senate — District 40 | Virginia State Senate |
| `barbara-henley` | 3 | active | incumbent_seeking_reelection | local | I | City Council - District 2 | City of Virginia Beach |
| `belen-rodas` | 2 | active | incumbent | local | D | School Board — Chancellor | Spotsylvania County |
| `ben-cline` | 19 | active | incumbent_seeking_reelection | federal | R | U.S. House — District 6 | United States House of Representatives |
| `betsy-b-carr` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 78 | Virginia House of Delegates |
| `bill-desteph` | 8 | active | incumbent_seeking_reelection | state | R | State Senate — District 20 | Virginia State Senate |
| `bill-stanley` | 8 | active | incumbent_seeking_reelection | state | R | State Senate — District 7 (sitting) | Virginia State Senate |
| `bill-wiley` | 6 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 32 | Virginia House of Delegates |
| `bobby-dyer` | 12 | active | won | local | R | Mayor | City of Virginia Beach |
| `bobby-scott` | 19 | active | incumbent_seeking_reelection | federal | D | U.S. House — District 3 | United States House of Representatives |
| `bonita-anthony` | 4 | active | incumbent | state | D | House of Delegates — District 92 | Virginia House of Delegates |
| `briana-sewell` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 25 | Virginia House of Delegates |
| `bryce-reeves` | 8 | active | incumbent_seeking_reelection | state | R | State Senate — District 28 | Virginia State Senate |
| `buddy-fowler` | 9 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 59 | Virginia House of Delegates |
| `buta-biberaj` | 11 | former | — | local | D | Former Commonwealth's Attorney (Loudoun County) | Loudoun County, Virginia |
| `cal-jackson-green` | 4 | active | won | local | R | City Council - District 7 | City of Virginia Beach |
| `carlos-clanton` | 7 | active | — | local | I | City Council - Superward 7 | City of Norfolk |
| `carol-medawar` | 4 | active | incumbent | local | D | School Board — Courtland | Spotsylvania County |
| `carolyn-campbell` | 2 | active | — | local | Unknown | City Council | City of Hampton |
| `charlie-frye-jr` | 4 | active | — | local | D | Vice Mayor, Ward 4 | City of Fredericksburg |
| `charlie-schmidt` | 8 | active | incumbent | state | D | House of Delegates — District 77 | Virginia House of Delegates |
| `charniele-herring` | 8 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 4 | Virginia House of Delegates |
| `chris-head` | 5 | active | incumbent_seeking_reelection | state | R | State Senate — District 3 | Virginia State Senate |
| `chris-runion` | 11 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 35 | Virginia House of Delegates |
| `chris-yakabouski` | 4 | active | incumbent | local | R | County Board of Supervisors — Battlefield District | Spotsylvania County |
| `christie-new-craig` | 11 | active | incumbent_seeking_reelection | state | R | State Senate — District 19 | Virginia State Senate |
| `cleon-long` | 2 | active | — | local | I | City Council - Central District | City of Newport News |
| `cliff-hayes-jr` | 8 | active | incumbent | state | D | House of Delegates — District 91 | Virginia House of Delegates |
| `colette-mceachin` | 5 | active | incumbent_seeking_reelection | local | D | Commonwealth's Attorney | City of Richmond |
| `colin-stolle` | 5 | active | won | local | R | Commonwealth's Attorney | City of Virginia Beach |
| `courtney-doyle` | 5 | active | incumbent_seeking_reelection | local | I | City Council - Ward 2 | City of Norfolk |
| `creigh-deeds` | 14 | active | incumbent_seeking_reelection | state | D | State Senate — District 11 | Virginia State Senate |
| `crystal-vanuch` | 11 | active | incumbent | local | R | County Board of Supervisors — Rock Hill District | Stafford County |
| `curtis-bethany` | 2 | active | — | local | I | Vice Mayor / City Council - North District | City of Newport News |
| `cynthia-newbille` | 8 | active | incumbent_seeking_reelection | local | D | City Council — District 7 (East End) | City of Richmond |
| `dan-helmer` | 3 | active | running_higher_office | state | D | House of Delegates — District 10 | Virginia House of Delegates |
| `danica-roem` | 8 | active | incumbent_seeking_reelection | state | D | State Senate — District 30 | Virginia State Senate |
| `daniel-whitaker` | 3 | active | — | local | Unknown | City Council | City of Chesapeake |
| `danny-avula` | 9 | active | incumbent_seeking_reelection | local | D | Mayor of Richmond | City of Richmond |
| `danny-diggs` | 8 | active | incumbent_seeking_reelection | state | R | State Senate — District 24 | Virginia State Senate |
| `darius-mayfield` | 17 | active | primary_candidate | federal | R | U.S. Representative VA-07 (2026 R Candidate · 2x prior NJ-12 nominee · small-business owner) | United States House of Representatives |
| `darrell-english` | 6 | active | incumbent | local | R | County Board of Supervisors — Hartwood District | Stafford County |
| `dave-marsden` | 8 | active | incumbent_seeking_reelection | state | D | State Senate — District 35 | Virginia State Senate |
| `david-goosman` | 5 | active | incumbent | local | R | County Board of Supervisors — Berkeley District | Spotsylvania County |
| `david-reid` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 28 | Virginia House of Delegates |
| `david-suetterlein` | 7 | active | incumbent_seeking_reelection | state | R | State Senate — District 4 | Virginia State Senate |
| `debbie-ritter` | 6 | active | — | local | R | Vice Mayor / City Council (At-Large) | City of Chesapeake |
| `deborah-frazier` | 4 | active | incumbent | local | D | County Board of Supervisors — Salem District | Spotsylvania County |
| `debra-gardner` | 5 | active | incumbent | state | D | House of Delegates — District 76 | Virginia House of Delegates |
| `delores-mcquinn` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 81 | Virginia House of Delegates |
| `delores-riley-oates` | 17 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 31 | Virginia House of Delegates |
| `destiny-levere-bolling` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 80 | Virginia House of Delegates |
| `deuntay-diggs` | 5 | active | incumbent | local | I | County Board of Supervisors — George Washington District (Chairman) | Stafford County |
| `don-beyer` | 20 | active | incumbent_seeking_reelection | federal | D | U.S. House — District 8 | United States House of Representatives |
| `don-scott` | 5 | active | incumbent | state | D | Speaker of the Virginia House of Delegates (District 88) | Virginia House of Delegates |
| `douglas-ollivant` | 9 | active | primary_candidate | federal | R | U.S. Representative VA-07 (2026 R Candidate · former NSC Director for Iraq) | United States House of Representatives |
| `drew-mullins` | 4 | active | incumbent | local | R | County Board of Supervisors — Courtland District (Vice Chairman) | Spotsylvania County |
| `ebony-wright` | 0 | active | incumbent | local | D | City Council - Sleepy Hole Borough | City of Suffolk |
| `elaine-luria` | 12 | active | primary_candidate | federal | D | U.S. Representative VA-02 (2026 D Candidate · former US Rep VA-02 · seeking rematch with Kiggans) | United States House of Representatives |
| `elizabeth-bennett-parker` | 11 | active | incumbent | state | D | State Senate — District 39 (special-election winner, sworn Feb 18, 2026; prior House of Delegates HD-5, 2022-2026) | Virginia State Senate |
| `elizabeth-guzman` | 8 | active | running_higher_office | state | D | House of Delegates — District 22 (sitting; 2026 candidate for Congress, VA-07) | Virginia House of Delegates |
| `elizabeth-warner` | 5 | active | incumbent | local | D | School Board — Griffis-Widewater (Chair 2026) | Stafford County |
| `ella-ward` | 1 | active | — | local | D | City Council | City of Chesapeake |
| `ellen-mclaughlin` | 4 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 36 | Virginia House of Delegates |
| `ellen-robertson` | 4 | active | incumbent | local | D | City Council — District 6 (Gateway) | City of Richmond |
| `emily-jordan` | 14 | active | incumbent_seeking_reelection | state | R | State Senate — District 17 | Virginia State Senate |
| `eric-olsen` | 1 | active | incumbent | local | R | Commonwealth's Attorney | Stafford County |
| `eric-phillips` | 12 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 48 | Virginia House of Delegates |
| `eric-zehr` | 9 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 51 | Virginia House of Delegates |
| `eugene-vindman` | 18 | active | incumbent_seeking_reelection | federal | D | U.S. House — District 7 | United States House of Representatives |
| `garrett-mcguire` | 4 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 17 | Virginia House of Delegates |
| `gerald-childress` | 4 | active | incumbent | local | R | County Board of Supervisors — Chancellor District | Spotsylvania County |
| `gerry-connolly` | 0 | former | deceased | federal | D | U.S. Representative · (died in office · seat filled by special election) | United States House of Representatives |
| `ghazala-hashmi` | 17 | active | won | state | D | Lt. Governor (sitting · sworn Jan 17, 2026) | Commonwealth of Virginia |
| `glen-sturtevant` | 9 | active | incumbent_seeking_reelection | state | R | State Senate — District 12 | Virginia State Senate |
| `gretchen-bulova` | 5 | active | incumbent | state | D | House of Delegates — District 11 | Virginia House of Delegates |
| `hillary-pugh-kent` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 67 | Virginia House of Delegates |
| `holly-seibold` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 12 | Virginia House of Delegates |
| `hope-harper` | 0 | active | — | local | Unknown | City Council | City of Hampton |
| `howard-gwynn` | 1 | lost | lost | local | D | Commonwealth's Attorney | City of Newport News |
| `hung-cao-senate-2026` | 2 | active | not_running | federal | R | Acting U.S. Secretary of the Navy (assumed Apr 22, 2026 · former 2024 VA Senate nominee · not a 2026 Senate candidate) | United States Senate |
| `hutch-hutcheson` | 2 | active | won | local | I | City Council - District 1 | City of Virginia Beach |
| `irene-shin` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 8 | Virginia House of Delegates |
| `israel-o'quinn` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 44 | Virginia House of Delegates |
| `jackie-glass` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 93 | Virginia House of Delegates |
| `jacob-lane` | 4 | active | incumbent | local | R | County Board of Supervisors — Livingston District | Spotsylvania County |
| `james-osyf` | 4 | active | not_running | federal | D | U.S. House VA-02 (2026 D candidate · SUSPENDED Dec 2025) | United States House of Representatives |
| `james-walkinshaw` | 26 | active | incumbent_seeking_reelection | federal | D | U.S. House — District 11 | United States House of Representatives |
| `jannan-holmes` | 1 | active | — | local | D | City Council, At-Large | City of Fredericksburg |
| `jarvis-e-bailey` | 1 | active | — | local | Unknown | School Board — At-Large | City of Fredericksburg |
| `jas-jeet-singh` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 26 | Virginia House of Delegates |
| `jason-ballard` | 4 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 42 | Virginia House of Delegates |
| `jason-graham` | 0 | former | — | local | Unknown | City Council, Ward 1 (Former) | City of Fredericksburg |
| `jason-miyares-ag-2026` | 25 | lost | lost | state | R | Attorney General of Virginia (former · lost 2025 to Jay Jones) | Commonwealth of Virginia |
| `jay-jones` | 12 | active | won | state | D | Attorney General (sitting · sworn Jan 17, 2026) | Commonwealth of Virginia |
| `jay-leftwich` | 12 | active | incumbent | state | R | House of Delegates — District 90 | Virginia House of Delegates |
| `jeff-bunn` | 4 | active | — | local | Unknown | City Council | City of Chesapeake |
| `jeff-jefferies` | 1 | active | — | local | Unknown | City Council | City of Chesapeake |
| `jeion-ward` | 13 | active | incumbent | state | D | House of Delegates — District 87 | Virginia House of Delegates |
| `jen-kiggans` | 13 | active | incumbent_seeking_reelection | federal | R | U.S. House — District 2 | United States House of Representatives |
| `jennifer-boysko` | 11 | active | incumbent | state | D | State Senate — District 38 | Virginia State Senate |
| `jennifer-carroll-foy` | 12 | active | incumbent_seeking_reelection | state | D | State Senate — District 33 | Virginia State Senate |
| `jennifer-craig-ford` | 4 | active | incumbent | local | I | School Board — Battlefield | Spotsylvania County |
| `jennifer-mcclellan` | 9 | active | incumbent_seeking_reelection | federal | D | U.S. House — District 4 | United States House of Representatives |
| `jennifer-rouse` | 2 | active | incumbent_seeking_reelection | local | I | City Council - District 10 | City of Virginia Beach |
| `jeremy-mcgee` | 1 | active | incumbent | local | I | City Council - Superward 6 | City of Norfolk |
| `jeremy-mcpike` | 8 | active | incumbent_seeking_reelection | state | D | State Senate — District 29 | Virginia State Senate |
| `jessica-anderson` | 4 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 71 | Virginia House of Delegates |
| `jimmy-gray` | 2 | active | — | local | Unknown | Mayor | City of Hampton |
| `joe-mcnamara` | 8 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 40 | Virginia House of Delegates |
| `john-eley` | 2 | active | — | local | I | City Council - South District | City of Newport News |
| `john-gray-va-07` | 4 | active | not_running | federal | R | U.S. Representative VA-07 (WITHDREW 2026 R primary · former 2023 VA HD-25 nominee · Vietnam-era USMC vet, CPA) | United States House of Representatives |
| `john-mcauliff` | 4 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 30 | Virginia House of Delegates |
| `john-mcguire` | 16 | active | incumbent_seeking_reelection | federal | R | U.S. House — District 5 | United States House of Representatives |
| `john-paige` | 1 | active | general_candidate | local | I | City Council - Ward 4 | City of Norfolk |
| `john-reid` | 27 | lost | lost | state | R | Lt. Governor (2025 R Candidate · lost) | Commonwealth of Virginia |
| `john-stringfellow` | 4 | lost | not_running | federal | D | U.S. Representative VA-02 (2026 D candidate — did NOT make the Aug 4 primary ballot) | United States House of Representatives |
| `jonathan-gerlach` | 0 | former | — | local | Unknown | Former — City Council, Ward 2 | City of Fredericksburg |
| `josh-regan` | 1 | active | incumbent | local | D | School Board — Aquia | Stafford County |
| `josh-thomas` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 21 | Virginia House of Delegates |
| `joshua-cole` | 15 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 65 | Virginia House of Delegates |
| `joshua-schulman` | 1 | active | incumbent_seeking_reelection | local | I | City Council - District 9 | City of Virginia Beach |
| `joy-crump-fxbg` | 1 | active | — | local | D | City Council, Ward 2 | City of Fredericksburg |
| `justin-pence` | 5 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 33 | Virginia House of Delegates |
| `kacey-carnegie` | 8 | active | incumbent | state | D | House of Delegates — District 89 | Virginia House of Delegates |
| `kannan-srinivasan` | 7 | active | incumbent_seeking_reelection | state | D | State Senate — District 32 | Virginia State Senate |
| `karen-hamilton` | 5 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 62 | Virginia House of Delegates |
| `karen-keys-gamarra` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 7 | Virginia House of Delegates |
| `karrie-delaney` | 8 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 9 | Virginia House of Delegates |
| `katherine-jordan-rva` | 4 | active | incumbent | local | D | City Council — District 2 (North Central) | City of Richmond |
| `kathleen-katie-pomeroy` | 1 | active | — | local | Unknown | School Board — Ward 2 | City of Fredericksburg |
| `kathryn-bryant` | 1 | active | incumbent | local | I | City Council | City of Portsmouth |
| `kathy-tran` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 18 | Virginia House of Delegates |
| `katrina-callsen` | 12 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 54 | Virginia House of Delegates |
| `kecia-evans` | 2 | active | incumbent | local | D | County Board of Supervisors — Falmouth District | Stafford County |
| `keith-hodges` | 9 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 68 | Virginia House of Delegates |
| `kelly-convirs-fowler` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 96 | Virginia House of Delegates |
| `kenny-alexander` | 3 | active | — | local | D | Mayor | City of Norfolk |
| `kenya-gibson` | 6 | active | incumbent | local | D | City Council — District 3 (Northside) | City of Richmond |
| `kerry-devine` | 4 | active | — | local | D | Mayor, At-Large | City of Fredericksburg |
| `kimberly-pope-adams` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 82 | Virginia House of Delegates |
| `kirk-mcpike` | 9 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 5 | Virginia House of Delegates |
| `l-louise-lucas` | 13 | active | incumbent_seeking_reelection | state | D | State Senate — District 18 | Virginia State Senate |
| `lamont-bagby` | 10 | active | incumbent_seeking_reelection | state | D | State Senate — District 14 | Virginia State Senate |
| `lashrecse-aird` | 9 | active | incumbent_seeking_reelection | state | D | State Senate — District 13 | Virginia State Senate |
| `laura-jane-cohen` | 9 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 15 | Virginia House of Delegates |
| `lawrence-a-dibella-iii` | 3 | active | incumbent | local | R | School Board — Berkeley | Spotsylvania County |
| `lee-ware` | 6 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 72 | Virginia House of Delegates |
| `leotis-williams` | 0 | active | won | local | I | City Council - Whaleyville Borough | City of Suffolk |
| `leroy-bennett` | 4 | active | general_candidate | local | I | City Council - Cypress Borough | City of Suffolk |
| `les-smith` | 3 | active | — | local | D | City Council | City of Chesapeake |
| `leslie-mehta` | 12 | active | incumbent | state | D | House of Delegates — District 73 | Virginia House of Delegates |
| `libby-humphries` | 3 | active | — | local | D | Commonwealth's Attorney | City of Fredericksburg |
| `lily-franklin` | 3 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 41 | Virginia House of Delegates |
| `lindsey-dougherty` | 6 | active | incumbent | state | D | House of Delegates — District 75 | Virginia House of Delegates |
| `lori-hayes` | 6 | active | incumbent | local | R | County Board of Supervisors — Lee Hill District (Chairman) | Spotsylvania County |
| `lorita-c-daniels` | 6 | active | running_higher_office | local | D | School Board — Salem | Spotsylvania County |
| `lue-ward` | 1 | active | — | local | I | Vice Mayor / City Council - Nansemond Borough | City of Suffolk |
| `luke-torian` | 11 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 24 (Chair, House Appropriations Committee) | Virginia House of Delegates |
| `luther-cifers` | 4 | active | incumbent_seeking_reelection | state | R | State Senate — District 10 (sitting · sworn Jan 15 2025) | Virginia State Senate |
| `madison-whittle` | 13 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 49 | Virginia House of Delegates |
| `malvina-rollins-kay` | 1 | active | — | local | Unknown | School Board — Ward 4 | City of Fredericksburg |
| `mamie-johnson` | 2 | active | — | local | I | City Council - Ward 3 | City of Norfolk |
| `mamie-locke` | 5 | active | incumbent_seeking_reelection | state | D | State Senate — District 23 | Virginia State Senate |
| `marcellus-harris` | 0 | active | — | local | I | City Council - North District | City of Newport News |
| `marcia-price` | 9 | active | incumbent | state | D | House of Delegates — District 85 | Virginia House of Delegates |
| `marcus-simon` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 13 | Virginia House of Delegates |
| `margaret-franklin` | 4 | active | incumbent | state | D | House of Delegates — District 23 | Virginia House of Delegates |
| `mark-downey` | 4 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 69 | Virginia House of Delegates |
| `mark-hugel` | 3 | active | incumbent_seeking_reelection | local | I | City Council | City of Portsmouth |
| `mark-obenshain` | 11 | active | incumbent_seeking_reelection | state | R | State Senate — District 2 | Virginia State Senate |
| `mark-peake` | 6 | active | incumbent_seeking_reelection | state | R | State Senate — District 8 (sitting) | Virginia State Senate |
| `mark-warner` | 9 | active | incumbent_seeking_reelection | federal | D | U.S. Senator (Class 2 · seeking 4th term 2026) | United States Senate |
| `martin-thomas-jr` | 2 | active | incumbent_seeking_reelection | local | I | Vice Mayor / City Council - Ward 1 | City of Norfolk |
| `marty-martinez` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 29 | Virginia House of Delegates |
| `matt-rowe-fxbg` | 1 | active | — | local | D | City Council, Ward 1 | City of Fredericksburg |
| `matt-strickler` | 4 | active | not_running | federal | D | U.S. House VA-02 (2026 D candidate · WITHDREW Apr 2026) | United States House of Representatives |
| `matthew-hamel` | 1 | active | — | local | D | Commonwealth's Attorney | City of Chesapeake |
| `matthew-percival` | 5 | active | incumbent | local | I | School Board Vice Chair — District 1 | City of Richmond |
| `may-nivar` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 57 | Virginia House of Delegates |
| `maya-guy` | 4 | active | incumbent | local | D | County Board of Supervisors — Aquia District (Vice Chair) | Stafford County |
| `megan-jackson` | 6 | active | incumbent | local | D | School Board — Livingston (Chair) | Spotsylvania County |
| `michael-berlucchi` | 6 | active | won | local | R | City Council - District 3 | City of Virginia Beach |
| `michael-feggans` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 97 | Virginia House of Delegates |
| `michael-jones` | 9 | active | incumbent_seeking_reelection | state | D | State Senate — District 15 | Virginia State Senate |
| `michael-webert` | 4 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 61 | Virginia House of Delegates |
| `michelle-ferebee` | 0 | active | — | local | Unknown | City Council | City of Hampton |
| `michelle-maldonado` | 8 | former | resigned | state | D | House of Delegates — District 20 (resigned eff. 2026-05-31) | Virginia House of Delegates |
| `mike-cherry` | 6 | active | incumbent | state | R | House of Delegates — District 74 | Virginia House of Delegates |
| `mike-duman` | 8 | active | general_candidate | local | I | Mayor | City of Suffolk |
| `missy-cotter-smasal` | 7 | active | lost | federal | D | U.S. House VA-02 (2024 D nominee · lost to Kiggans · 2026 run unconfirmed) | United States House of Representatives |
| `mitchell-cornett` | 6 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 46 | Virginia House of Delegates |
| `molly-mcfadden` | 1 | active | — | local | Unknown | School Board — At-Large | City of Fredericksburg |
| `morgan-griffith` | 21 | active | incumbent_seeking_reelection | federal | R | U.S. House — District 9 | United States House of Representatives |
| `nadarius-clark` | 8 | active | incumbent | state | D | House of Delegates — District 84 | Virginia House of Delegates |
| `narendra-pleas` | 3 | active | — | local | D | Commonwealth's Attorney | City of Suffolk |
| `nicolaus-sleister` | 2 | lost | not_running | federal | D | U.S. Representative VA-02 (2026 D candidate — did NOT make the Aug 4 primary ballot) | United States House of Representatives |
| `nicole-cole` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 66 | Virginia House of Delegates |
| `nicole-jones-rva` | 1 | active | incumbent | local | I | City Council — District 9 (South Central) | City of Richmond |
| `nila-devanath` | 10 | active | primary_candidate | federal | D | U.S. Representative VA-02 (2026 D Candidate · challenger · Kiggans challenger) | United States House of Representatives |
| `otto-wachsmann` | 9 | active | incumbent | state | R | House of Delegates — District 83 | Virginia House of Delegates |
| `pamela-yeung` | 6 | active | incumbent | local | D | County Board of Supervisors — Garrisonville District | Stafford County |
| `parisa-dehghani-tafti` | 9 | active | — | local | D | Commonwealth's Attorney (Arlington County) | Arlington County, Virginia |
| `pat-king` | 0 | active | — | local | D | City Council | City of Chesapeake |
| `patricia-healy` | 6 | active | incumbent | local | R | School Board — Rock Hill | Stafford County |
| `patrick-hope` | 6 | active | incumbent | state | D | House of Delegates — District 1 | Virginia House of Delegates |
| `patrick-mosolf` | 7 | active | primary_candidate | federal | D | U.S. Representative VA-02 (2026 D Candidate · challenger · Kiggans challenger) | United States House of Representatives |
| `paul-krizek` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 16 | Virginia House of Delegates |
| `phil-hernandez` | 5 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 94 | Virginia House of Delegates |
| `phillip-jones` | 6 | active | — | local | D | Mayor | City of Newport News |
| `phillip-scott` | 4 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 63 | Virginia House of Delegates |
| `rae-cousins` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 79 | Virginia House of Delegates |
| `ramin-fatehi` | 7 | active | — | local | D | Commonwealth's Attorney | City of Norfolk |
| `randy-bowman` | 1 | active | — | local | Unknown | City Council | City of Hampton |
| `reva-trammell` | 5 | active | incumbent | local | D | City Council — District 8 (Southside) | City of Richmond |
| `richard-j-rich-lieberman` | 6 | active | incumbent | local | I | School Board — Lee Hill | Spotsylvania County |
| `richard-stuart` | 5 | active | incumbent_seeking_reelection | state | R | State Senate — District 25 | Virginia State Senate |
| `rick-west-chesapeake` | 4 | active | — | local | R | Mayor | City of Chesapeake |
| `rip-sullivan` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 6 | Virginia House of Delegates |
| `rob-wittman` | 22 | active | incumbent_seeking_reelection | federal | R | U.S. House — District 1 | United States House of Representatives |
| `robert-bloxom-jr` | 9 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 100 | Virginia House of Delegates |
| `robert-coleman` | 1 | active | — | local | I | City Council - Central District | City of Newport News |
| `rodney-willett` | 9 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 58 | Virginia House of Delegates |
| `rosemary-wilson` | 3 | active | won | local | R | Vice Mayor / City Council - District 5 | City of Virginia Beach |
| `rozia-henson` | 7 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 19 | Virginia House of Delegates |
| `russet-perry` | 9 | active | incumbent_seeking_reelection | state | D | State Senate — District 31 | Virginia State Senate |
| `ryan-mcdougle` | 9 | active | incumbent_seeking_reelection | state | R | State Senate — District 26 | Virginia State Senate |
| `ryan-mehaffey` | 8 | active | incumbent | local | R | Commonwealth's Attorney | Spotsylvania County |
| `saddam-azlan-salim` | 9 | active | incumbent | state | D | State Senate — District 37 | Virginia State Senate |
| `sam-rasoul` | 13 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 38 | Virginia House of Delegates |
| `sarah-abubaker` | 1 | active | incumbent | local | I | City Council — District 4 (Southwest) | City of Richmond |
| `sarah-chase` | 5 | active | incumbent | local | D | School Board — Falmouth (Vice Chair 2026) | Stafford County |
| `schuyler-vanvalkenburg` | 12 | active | incumbent_seeking_reelection | state | D | State Senate — District 16 | Virginia State Senate |
| `scott-surovell` | 13 | active | incumbent_seeking_reelection | state | D | State Senate — District 34 (Senate Majority Leader) | Virginia State Senate |
| `scott-wyatt` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 60 | Virginia House of Delegates |
| `shannon-fingerholz` | 2 | active | incumbent | local | D | School Board — Hartwood | Stafford County |
| `shannon-glover` | 3 | active | — | local | D | Mayor | City of Portsmouth |
| `shavonda-fernandez` | 1 | active | incumbent | local | Unknown | School Board Chair — District 9 | City of Richmond |
| `shelley-butler-barlow` | 6 | active | general_candidate | local | I | City Council - Chuckatuck Borough | City of Suffolk |
| `shelly-simonds` | 6 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 70 | Virginia House of Delegates |
| `stacey-carroll` | 10 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 64 | Virginia House of Delegates |
| `stella-pekarsky` | 14 | active | incumbent_seeking_reelection | state | D | State Senate — District 36 | Virginia State Senate |
| `stephanie-lynch` | 6 | active | incumbent | local | D | City Council — District 5 (Central) | City of Richmond |
| `stephanie-morales` | 6 | active | — | local | D | Commonwealth's Attorney | City of Portsmouth |
| `steve-descano` | 6 | active | incumbent | local | D | Commonwealth's Attorney (Fairfax County) | Fairfax County, Virginia |
| `steven-brown` | 1 | active | — | local | Unknown | Vice Mayor / City Council | City of Hampton |
| `suhas-subramanyam-cd10` | 19 | active | incumbent_seeking_reelection | federal | D | U.S. House — District 10 | United States House of Representatives |
| `susan-randall` | 2 | active | incumbent | local | R | School Board — George Washington | Stafford County |
| `susanna-finn` | 1 | active | — | local | I | City Council, Ward 3 | City of Fredericksburg |
| `tammy-brankley-mulchi` | 7 | active | incumbent_seeking_reelection | state | R | State Senate — District 9 (sitting · sworn Jan 2024) | Virginia State Senate |
| `tara-durant` | 13 | active | running_higher_office | state | R | State Senator, District 27 (sitting · 2026 candidate for Congress, VA-7) | Commonwealth of Virginia |
| `terry-austin` | 4 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 37 | Virginia House of Delegates |
| `terry-kilgore` | 6 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 45 | Virginia House of Delegates |
| `tim-griffin` | 14 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 53 | Virginia House of Delegates |
| `tim-kaine` | 11 | active | incumbent | federal | D | U.S. Senator (Class 1 · term through Jan 2031) | United States Senate |
| `timmy-french` | 5 | active | incumbent_seeking_reelection | state | R | State Senate — District 1 | Virginia State Senate |
| `tina-vick` | 2 | active | — | local | I | City Council - South District | City of Newport News |
| `tinesha-allen` | 3 | active | incumbent | local | D | County Board of Supervisors — Griffis-Widewater District | Stafford County |
| `todd-pillion` | 5 | active | incumbent_seeking_reelection | state | R | State Senate — District 6 (sitting) | Virginia State Senate |
| `tom-garrett` | 12 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 56 | Virginia House of Delegates |
| `tommy-wright` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 50 | Virginia House of Delegates |
| `tony-wilt` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 34 | Virginia House of Delegates |
| `travis-hackworth` | 9 | active | incumbent_seeking_reelection | state | R | State Senate — District 5 | Virginia State Senate |
| `vernon-tillage` | 0 | active | general_candidate | local | I | City Council | City of Portsmouth |
| `virgil-thornton-sr` | 9 | active | incumbent | state | D | House of Delegates — District 86 | Virginia House of Delegates |
| `vivian-watts` | 9 | active | incumbent_seeking_reelection | state | D | House of Delegates — District 14 | Virginia House of Delegates |
| `wanda-blackwell` | 1 | active | incumbent | local | D | School Board — Garrisonville | Stafford County |
| `waverly-washington` | 2 | active | not_running | federal | R | U.S. House VA-07 (WITHDREW from 2026 R primary · West Point grad, combat vet, former Tuberville Defense Fellow) | United States House of Representatives |
| `wendell-walker` | 7 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 52 | Virginia House of Delegates |
| `will-davis` | 6 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 39 | Virginia House of Delegates |
| `will-mackintosh` | 5 | active | — | local | D | City Council, At-Large | City of Fredericksburg |
| `will-morefield` | 5 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 43 | Virginia House of Delegates |
| `william-dodson` | 0 | active | — | local | I | City Council | City of Portsmouth |
| `william-moody` | 6 | active | general_candidate | local | I | Vice Mayor / City Council | City of Portsmouth |
| `winsome-earle-sears` | 41 | lost | lost | state | R | Lt. Governor (former) · Failed 2025 gubernatorial candidate | Commonwealth of Virginia |
| `worth-remick` | 2 | active | incumbent_seeking_reelection | local | Unknown | City Council - District 6 | City of Virginia Beach |
| `wren-williams` | 12 | active | incumbent_seeking_reelection | state | R | House of Delegates — District 47 | Virginia House of Delegates |
| `yesli-vega` | 16 | active | not_running | federal | R | U.S. Representative VA-07 (NOT running 2026 — sitting Prince William Co. Supervisor / 2022 + 2024 R nominee) | United States House of Representatives |
| `yolanda-thomas` | 1 | active | — | local | I | City Council | City of Portsmouth |

### Focus cluster indexes

**Federal Senate-related:** `mark-warner` · `tim-kaine` · `hung-cao-senate-2026`  
**Federal House incumbents:** `rob-wittman` · `jen-kiggans` · `bobby-scott` · `jennifer-mcclellan` · `john-mcguire` · `ben-cline` · `eugene-vindman` · `don-beyer` · `morgan-griffith` · `suhas-subramanyam-cd10` · `james-walkinshaw`  
**Statewide exec:** `abigail-spanberger` · `ghazala-hashmi` · `jay-jones` · `winsome-earle-sears` · `jason-miyares-ag-2026` · `john-reid`  
**FXBG council:** `kerry-devine` · `charlie-frye-jr` · `jannan-holmes` · `will-mackintosh` · `matt-rowe-fxbg` · `joy-crump-fxbg` · `susanna-finn`  
**Spotsy BoS:** `lori-hayes` · `drew-mullins` · `chris-yakabouski` · `david-goosman` · `gerald-childress` · `jacob-lane` · `deborah-frazier`  
**Stafford BoS:** `deuntay-diggs` · `maya-guy` · `kecia-evans` · `pamela-yeung` · `tinesha-allen` · `darrell-english` · `crystal-vanuch`

## 8. Method notes

- Cardinal rule remains: **web-verified before any future score change**.  
- This file and the Q&A digest **do not** apply refinements.  
- Prior sprint dry-run (same day) refined 23 records with **0 evidence cells set** — dens tables there used the same True/False dens concept.  
- Avoid treating `"N/A"`-heavy local grids as “dense”; dens=1 with 35 N/As is still a **thin** record.

---

*End gaps digest · 2026-07-18 · scorecard untouched*
