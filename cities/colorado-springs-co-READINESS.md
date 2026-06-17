# RESOLUTE Local — Readiness: Colorado Springs, CO

**Status:** Research only (J5 scaffold). No code, no profiles, no scorecard data yet.
**Compiled:** 2026-06-17. EXPANSION-PLAN target #5 — the **City of Colorado
Springs, Colorado** (the municipal government — NOT El Paso County).

Colorado Springs has the most *verified* video stack of the set: a live-and-dated
**Granicus** archive (`ViewPublisher.php?view_id=1`, latest video confirmed June 10
2026) that bundles per-meeting video + agenda + minutes in one place. Documents live
on **Granicus Legistar** (`coloradosprings.legistar.com`) — the **same vendor as
Richmond and Nashville** (targets #1 and #4), so the Legistar scraper transfers
again (Legistar is now the most common vendor in the program, 3 of 5 cities). Two
structural firsts for the expansion set: (1) the ingest path is **Granicus VOD, not
YouTube** — the official SpringsTV YouTube channel exists but its posting cadence
could not be verified, so Granicus is the source of record; (2) Colorado Springs
runs a **strong-mayor / mayor-council** government, so the **Mayor is NOT a member
of City Council** — the first separated-executive city in the set.

---

## Meeting broadcaster (video)

- **Primary archive (use this):** **Granicus ViewPublisher** —
  `https://coloradosprings.granicus.com/ViewPublisher.php?view_id=1`
  ("Streaming Media Archive"). Per-meeting rows carry video + agenda + minutes;
  latest confirmed video **June 10, 2026** (2h39m). This is the dated, verified
  ingest source.
- **Granicus live stream:** `https://coloradosprings.granicus.com/MediaPlayer.php?publish_id=1`
  ("Colorado Springs Live Stream" — live + recorded public meetings).
- **Second video path (vendor-side):** council video is also surfaced inline on the
  **Legistar** calendar rows (video present on recent June 2026 meetings), so docs
  and recent video can come from one path.
- **Government-access channel — "SpringsTV":** Comcast **ch. 18** and **880 (HD)**;
  StratusIQ **ch. 99 (streaming)**. SpringsTV programming explicitly includes City
  Council meetings.
- **YouTube:** official channel **"City of Colorado Springs" / "SpringsTV"**, handle
  **`@CityofCOS`**: `https://www.youtube.com/c/SpringsTV`. SpringsTV says it uploads
  council meeting video here — but the posting **cadence could not be verified**
  (the channel JS-rendered empty to the fetcher), so treat YouTube as a likely-but-
  unconfirmed secondary, not the source of record.
- **Vimeo:** `https://vimeo.com/coloradosprings` (listed as a SpringsTV platform).
- **Facebook live:** `https://www.facebook.com/coscitycouncil/` (`@coscitycouncil`).
- **Meeting cadence:** regular City Council meetings are **9:00 a.m. on the 2nd and
  4th Tuesday** monthly, Council Chambers (3rd floor, City Hall); work sessions
  precede them (Mondays, per the Legistar calendar).
- **Note vs. EXPANSION-PLAN spec:** unlike Raleigh/Nashville (clean YouTube VOD),
  the verified ingest path here is the **Granicus VOD** — closest stable, dated
  source. Ingest the **Granicus per-meeting video**; the Legistar embed is a
  fallback.

Sources:
`https://coloradosprings.granicus.com/ViewPublisher.php?view_id=1`,
`https://coloradosprings.gov/springstv`,
`https://coloradosprings.legistar.com/Calendar.aspx`.

## Agenda center (agendas / minutes)

- **Vendor:** **Granicus Legistar** (confirmed — the calendar page loads
  `//webcontent.granicusops.com/content/coloradosprings/` asset paths). The **same
  vendor as Richmond** (`richmondva.legistar.com`) and **Nashville**
  (`nashville.legistar.com`), so the scraper transfers. **Not** BoardDocs (Raleigh),
  **not** CivicClerk (Greenville).
- **Resident-facing portal:** `https://coloradosprings.legistar.com/`
  (main body: `https://coloradosprings.legistar.com/MainBody.aspx`).
- **Calendar / legislation:** `https://coloradosprings.legistar.com/Calendar.aspx`
  — lists City Council, Council Work Session, Planning Commission, Downtown Review
  Board, Historic Preservation Board, etc. Each row exposes Agenda (PDF),
  Accessible Agenda (HTML), Meeting Details, Video, iCalendar export, and
  Minutes/Accessible Minutes.
- **Unified, not split:** agenda PDFs, accessible HTML agendas, and meeting video
  links sit on the same Legistar calendar rows (Granicus underlies both the
  Legistar portal and the video archive). **Minutes lag** — June 2026 meetings
  showed minutes "Not available" at fetch time (minutes post later than
  agendas/video).

Sources:
`https://coloradosprings.legistar.com/`,
`https://coloradosprings.legistar.com/Calendar.aspx`.

## Council roster source

- **Primary (official):** `https://coloradosprings.gov/get-know-your-councilmembers`
  (lists all nine members + titles + the 6-district/3-at-large structure).
- **Cross-check:** Ballotpedia (`https://ballotpedia.org/Colorado_Springs,_Colorado`
  + `https://ballotpedia.org/City_elections_in_Colorado_Springs,_Colorado_(2025)`)
  — both JS-empty to the fetcher; roster below comes from the official city page +
  corroborating local news.

**Form of government:** strong-mayor / **mayor-council**. The **Mayor is a separate
executive and is NOT a member of City Council.** **9 Councilmembers = 6 single-member
Districts + 3 At-Large** (quoted from the city roster page). **4-year terms, 2-
consecutive-term limit. Nonpartisan** elections. **Split election cycle:** the **6
district seats** were last elected **April 1, 2025**; the **Mayor + 3 at-large seats**
are next on **April 6, 2027**.

| Seat | Name | Notes |
|---|---|---|
| Mayor (not on Council) | Yemi Mobolade | Independent; won the May 16 2023 runoff, sworn in **June 6 2023**; announced re-election April 2026 |
| At-Large | Lynette Crow-Iverson | **Council President** |
| At-Large | Brian Risley | **Council President Pro Tem** |
| At-Large | David Leinweber | |
| District 1 | Dave Donelson | Won 2nd term April 2025 (58.1%) |
| District 2 | Ken Casey | **Appointed Apr 6 2026** (5–3 council vote) to fill the Tom Bailey vacancy; serves to the 2027 election |
| District 3 | Brandy Williams | |
| District 4 | Kimberly Gold | |
| District 5 | Nancy Henjum | Re-elected April 2025 |
| District 6 | Roland Rainey (Jr.) | Elected April 2025 |

**District 2 note (resolved conflict):** Tom Bailey won District 2 (uncontested)
Apr 1 2025, then resigned March 2026 amid a successful recall petition; **Ken Casey**
(Army veteran, ex-Planning Commission) was appointed Apr 6 2026 by a 5–3 council vote
to serve until the 2027 election. The current city roster page lists **Ken Casey** —
an earlier stale search snippet showed Tom Bailey; disregard it.

Roster sources: `https://coloradosprings.gov/get-know-your-councilmembers`,
`https://coloradosprings.gov/mayor-yemi-mobolade`,
`https://coloradosprings.gov/election`.

---

## Readiness verdict

**Green — most-verified video stack so far, two structural firsts.** Broadcaster
(**Granicus** archive, dated to 6/10/2026, video+agenda+minutes unified), agenda
center (**Granicus Legistar** — **reuses the Richmond/Nashville scraper**), and
roster source are all sourced and stable. Four things to decide before a build:
(1) ingest the **Granicus per-meeting VOD**, not YouTube — the SpringsTV YouTube
channel exists but its posting cadence is unconfirmed, so Granicus is the source of
record (verify YouTube by hand if a faster MP4 path is wanted); (2) the document
path is **Legistar**, now the program's most common vendor (Richmond + Nashville +
Colorado Springs), so the scraper transfers; (3) the executive model is **mayor-
council** — the **Mayor sits outside Council**, the first separated-executive city
in the set, so the profile build must treat the mayor as its own record, not a
council seat; (4) the **party-label** question is the **same as F1/F2/J2/J4** —
elections are formally **nonpartisan**, so RESOLUTE's party tags would be inferred
from record, not the ballot (Mayor Mobolade runs as an Independent). The
distinguishing wrinkles are the **split election cycle** (districts 2025 / mayor +
at-large 2027) and a **mid-term appointed seat** (District 2, Ken Casey).

## Caveats / unverified

- **YouTube `@CityofCOS` JS-empty to the fetcher:** channel existence + "uploads
  council meetings" comes from the official SpringsTV page text and search snippets;
  VOD upload cadence, recent titles/dates, and whether *every* meeting is mirrored
  could **not** be confirmed. Use Granicus (dated, verified) as the ingest source.
- **Ballotpedia pages returned empty via the fetcher** (both the city page and the
  2025 city-elections page): roster + structure facts come from the official city
  pages + corroborating local news (KOAA / CPR / Gazette / KRDO / Axios), not a
  fetched Ballotpedia render.
- **Governance mechanics (4-yr term / 2-term limit / nonpartisan) not quoted from a
  directly-fetched official page:** these come from search snippets citing the City
  Charter — high-confidence but worth confirming against the City Charter/Code if a
  hard citation is needed.
- **StratusIQ cable channel:** the official SpringsTV page says **ch. 99**; one
  snippet also said "76/99" — treat 76 as unverified.
- **Granicus archive references Windows Media Player format** — may complicate clean
  automated MP4 extraction; check the actual per-meeting media URLs before building.
- **Confirmed by ≥1 official coloradosprings.gov source:** the 9-member
  (6 district + 3 at-large) structure, all 9 current members + their titles, the
  mayor-council form, Mayor Mobolade's June 6 2023 swearing-in, and the
  April 6 2027 Mayor + at-large election date.
