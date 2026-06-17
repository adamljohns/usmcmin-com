# RESOLUTE Local — Readiness: Greenville, SC

**Status:** Research only (J3 scaffold). No code, no profiles, no scorecard data yet.
**Compiled:** 2026-06-17. EXPANSION-PLAN target #3 (City of Greenville, SC — the
municipal government, **not** Greenville County).

Greenville is a clean expansion candidate on the video side: the city posts every
City Council meeting to an **official YouTube channel** (its own stated "official
site for publication and archiving of all digital media"), recordings up within
~24 hours. The live-viewing layer is **Cisco Webex** (per-meeting links, not a
stable ingest source) — so target the YouTube archive, not Webex. Documents live
on **CivicClerk (CivicPlus)** — a different vendor from Fredericksburg's stack and
from Raleigh's BoardDocs, so plan a distinct document scraper.

---

## Meeting broadcaster (video)

- **Live layer:** **Cisco Webex** — the city streams Council (plus Planning
  Commission, Design Review Board, Historic Review Board, Board of Zoning Appeals)
  live via Webex. Webex links are per-meeting, posted on the council/meeting page
  shortly before each meeting — **no single static live URL**, so not a clean
  ingest source.
- **Archive (use this):** official **YouTube channel — "City of Greenville,
  South Carolina"**:
  `https://www.youtube.com/channel/UCpADd24B_DBqM04drOaX-Ig`
  The city describes this channel as "the official site for publication and
  archiving of all digital media"; Council recordings post to a City Council
  playlist on it, typically **within ~24 hours** of the meeting.
- **Meeting cadence:** **2nd and 4th Mondays** monthly — Work Session 3:30 PM,
  Formal Meeting 5:30 PM.
- **No Vimeo** channel and **no dedicated GTV/cable government-access** archive
  surfaced as the primary source.
- **Note vs. EXPANSION-PLAN spec:** Greenville satisfies the YouTube path (like
  Raleigh), but its live layer is Webex (unlike Raleigh's parallel YouTube Live).
  The recap pipeline should ingest the **YouTube per-meeting VOD**, not Webex.

Sources:
`https://www.greenvillesc.gov/283/City-Council`,
`https://www.youtube.com/channel/UCpADd24B_DBqM04drOaX-Ig`,
`https://www.simplecivicsgreenvillecounty.org/blog/everything-you-need-to-know-about-greenville-city-council-meetings`.

## Agenda center (agendas / minutes)

- **Vendor:** **CivicClerk** (the CivicPlus agenda/meeting product) — **not**
  Legistar, **not** BoardDocs, **not** Granicus.
- **Resident-facing portal** (search by meeting date, calendar/list view, filter
  by board): `https://greenvillesc.portal.civicclerk.com/`
- **City page that points to it:**
  `https://www.greenvillesc.gov/129/Meeting-Agendas-Minutes`
  (also linked from the City Council page and the meeting-schedule page).
- **Split-vendor note:** documents (CivicClerk) and video (YouTube/Webex) live on
  separate platforms — two ingest paths, like Raleigh.

Sources:
`https://greenvillesc.portal.civicclerk.com/`,
`https://www.greenvillesc.gov/129/Meeting-Agendas-Minutes`,
`https://www.greenvillesc.gov/575/City-Council-Meeting-Schedule`.

## Council roster source

- **Primary (official):** `https://www.greenvillesc.gov/283/City-Council`
- **Cross-check:** Ballotpedia (`https://ballotpedia.org/Greenville,_South_Carolina`)
  + 2025 results via Greenville Journal
  (`https://greenvillejournal.com/government/tina-belge-lillian-brock-flemming-win-contested-greenville-sc-city-council-races/`).

**7 members = Mayor + 2 At-Large + 4 single-member Districts (1–4).** Four-year
terms, **staggered** with elections every two years in **odd years**. Mayor is
elected citywide.

| Seat / District | Name | Notes |
|---|---|---|
| Mayor | Knox H. White | In office since Dec 11 1995 (34th mayor); last elected 2023, next 2027 |
| At-Large | Dorothy Dowe | Vice Mayor Pro Tem; first elected 2019, re-elected 2023, next 2027 |
| At-Large | Tina Belge | Won Nov 4 2025 (D, 6,126 vs Matt Alexander R 4,188); replaced Russell Stall; next 2029 |
| District 1 | John DeWorken | Unopposed 2023; next 2027 |
| District 2 | Lillian Brock Flemming | Re-elected Nov 4 2025 (61.8% vs Mike Kilgore); next 2029 |
| District 3 | Ken Gibson | Unopposed 2023; next 2027 |
| District 4 | Wil Brasington | Held seat since 2017 (R); ran unopposed 2025; next 2029 |

Roster source: `https://www.greenvillesc.gov/283/City-Council`
(seat label cross-check: `https://www.greenvillesc.gov/1186/Dorothy-Dowe---At-Large`).

**Term window:** four-year staggered terms. The 2025 cycle (Belge At-Large,
Flemming D2, Brasington D4) runs **2025–2029**; the Mayor, Dowe (At-Large),
DeWorken (D1), and Gibson (D3) are on the **2023–2027** cycle. Sources:
`https://greenvillejournal.com/government/election-results-2025-greenville-county/`,
`https://www.greenvillesc.gov/283/City-Council`.

**Partisan → nonpartisan (TIME-SENSITIVE):** Greenville city elections are
**currently PARTISAN** — candidates run with party labels (Belge ran as a
Democrat, Alexander as a Republican in Nov 2025; the council currently sits at a
**4–3 Democratic majority**). A **state law passed May 2026 requires SC cities
over 39,000 population (Greenville and Florence) to hold NONPARTISAN city
elections starting in 2027.** So party labels are accurate only **through the
2025 cycle**; from 2027 on, Greenville joins the nonpartisan-ballot states
(Fredericksburg / Richmond / Raleigh). Source:
`https://www.postandcourier.com/greenville/news/greenville-nonpartisan-elections-change-city-politics/article_194ef61e-6ac9-4e3a-862d-dd71c4d0a321.html`.

---

## Readiness verdict

**Green, with one ingest caveat and one reconciliation twist.** Broadcaster
(YouTube archive + Webex live), agenda center (CivicClerk), and roster are all
sourced and stable. Three things to decide before a build: (1) ingest the
**YouTube per-meeting VOD** (Webex has no stable live URL — confirm the City
Council playlist on the channel before wiring the pipeline); (2) the document
path is **CivicClerk (CivicPlus)** — a third distinct vendor (Fredericksburg's
stack, Raleigh's BoardDocs, now CivicClerk), so a separate scraper; (3) the
party-label question is the **inverse** of F1/F2/J2 — Greenville is currently
*partisan* (4–3 D) and converts to *nonpartisan* only with the 2027 cycle, so
RESOLUTE's party tags can use the real 2025 labels for now but must drop them
after 2027. No code written here.

## Caveats / unverified

- **Webex live URL not captured:** Webex links are per-meeting and posted shortly
  before each meeting; there is no single static live URL. For ingest rely on the
  YouTube channel/playlist, not Webex.
- **YouTube "City Council" playlist URL not captured:** only the channel
  (`UCpADd24B_DBqM04drOaX-Ig`) is confirmed. Verify the specific council playlist
  on the channel before wiring the pipeline.
- **Ballotpedia main page:** `ballotpedia.org/Greenville,_South_Carolina` and
  several greenvillesc.gov pages render via JavaScript and returned empty to
  automated fetch — the URLs are valid and are the right cross-checks, but a human
  should open them to visually confirm the roster table. Ballotpedia's stronger
  Greenville coverage is on its county/election pages; roster facts here are
  anchored to the authoritative official city site.
- **Mayor White's 2023 election year is inferred** from the staggered-term
  schedule + 2023 coverage; the city roster page does not print his term dates.
  His long tenure (since Dec 11 1995) is confirmed.
- **Some party labels unprinted:** Dowe's and Flemming's party affiliations were
  not explicitly stated in every source; Belge (D), Alexander (R), and Brasington
  (R) are explicitly labeled. Party labels become moot for the 2027+ cycle.
- **Belge vote-total minor discrepancy:** 6,127 (WSPA/aggregate) vs 6,126
  (Greenville Journal, 31 of 34 precincts) — a precinct-reporting rounding
  difference, not a conflict on the outcome.
- **Agenda vendor confirmed CivicClerk only:** no Legistar/BoardDocs/Granicus
  instance surfaced for this city; treat those as not in use unless a future check
  shows otherwise.
