# RESOLUTE Local — Readiness: Oklahoma City, OK

**Status:** Research only (J5 scaffold). No code, no profiles, no scorecard data yet.
**Compiled:** 2026-06-19. EXPANSION-PLAN target #6 — the **City of Oklahoma City,
Oklahoma** (the municipal government — NOT Oklahoma County). First city in a new
state for the program.

Oklahoma City breaks the pattern of the prior five. The agenda/document vendor is
**PrimeGov** (`okc.primegov.com`) — a Granicus product, but **not Legistar**, so the
Richmond/Nashville/Colorado Springs Legistar scraper does **not** transfer; this is a
**new ingest target**. The video path, by contrast, is the cleanest in the set so far:
an official **YouTube channel (`youtube.com/cityofokc`)** that live-streams every
regular Council meeting and archives each one to a dated, per-year playlist — the
**same YouTube-VOD model as Raleigh and Nashville** (targets #2 and #4), so the
YouTube ingest pattern transfers. Two structural notes: (1) OKC runs a
**council-manager** government with a **weak/ceremonial mayor who IS a voting member
of Council** (President of the Council) — the opposite of Colorado Springs'
separated-executive model; (2) the mayor is elected **at-large** while the **8 wards**
elect one member each, for **9 total seats**.

---

## Meeting broadcaster (video)

- **Primary ingest path (use this):** the official **YouTube channel
  `https://www.youtube.com/cityofokc`** (live URL `…/cityofokc/live`). The city's own
  meeting notices state Council meetings broadcast live on **Cox Channel 20**,
  **`youtube.com/cityofokc/live`**, and **okc.gov**, and that **a recording of each
  meeting is then added to the City's YouTube channel** — so YouTube is the dated
  source of record for VOD.
- **Per-year playlists:** meetings are organized into annual playlists — **2026**
  (`youtube.com/playlist?list=PLwFAYTiZB_PLGKFL8G1fnfwFt5KTGQaDx`) and **2025**
  (`…list=PLwFAYTiZB_PK6CREvvQjTZwGzrw0y_Xw8`). Both playlists exist and are active.
- **Most recent confirmed meeting:** a **City Council special meeting dated
  June 17, 2026** is listed on the official okc.gov events directory; regular meetings
  are streamed/recorded to the YouTube channel as above. (See caveat — the per-video
  YouTube date for the most recent *regular* meeting could not be fetch-confirmed
  because the channel JS-rendered empty to the fetcher.)
- **Cable:** **Cox Channel 20** carries the live broadcast.
- **Meeting cadence:** regular City Council meetings are **8:30 a.m. on Tuesdays**
  (roughly every other Tuesday), Council Chamber, 3rd floor, City Hall, **200 N
  Walker Ave.**
- **Note vs. EXPANSION-PLAN spec:** this matches the Raleigh/Nashville **clean
  YouTube VOD** pattern rather than the Granicus-VOD path of Colorado Springs.
  Ingest the **YouTube per-meeting video** from the `cityofokc` channel/playlists;
  the PrimeGov portal also surfaces a per-meeting video/media link as a fallback.

Sources:
`https://www.youtube.com/cityofokc`,
`https://www.youtube.com/playlist?list=PLwFAYTiZB_PLGKFL8G1fnfwFt5KTGQaDx`,
`https://www.okc.gov/Events-directory/City-Council-2026`.

## Agenda center (agendas / minutes)

- **Vendor:** **PrimeGov** (confirmed — the portal loads at `okc.primegov.com` and
  identifies as the PrimeGov Portal; PrimeGov is a **Granicus** product). This is a
  **new vendor for the program** — **not** Legistar (Richmond / Nashville / Colorado
  Springs), **not** BoardDocs (Raleigh), **not** CivicClerk (Greenville). The
  Legistar scraper does **not** transfer; a PrimeGov adapter is required.
- **Resident-facing portal:** `https://okc.primegov.com/public/portal` — sections for
  "Current and Upcoming Meetings" and "Archived Meetings," with per-meeting agenda,
  documents, and meeting-type fields. Individual meetings resolve to
  `okc.primegov.com/Portal/Meeting?...` URLs.
- **City landing pages:** `https://www.okc.gov/Government/Public-Meetings-and-Agendas`
  and its **Public Meeting Calendar** child page link out to the PrimeGov portal as
  the system of record for agendas; the City Clerk page offers archived-meeting search.
- **Structure:** agenda packets (compiled PDFs) and per-meeting media attach to the
  PrimeGov meeting rows. Minutes-vs-agenda lag was not checked at fetch time.

Sources:
`https://okc.primegov.com/public/portal`,
`https://www.okc.gov/Government/Public-Meetings-and-Agendas`,
`https://www.okc.gov/Government/Public-Meetings-and-Agendas/Public-Meeting-Calendar`.

## Council roster source

- **Primary (official):** `https://www.okc.gov/Government/Elected-Officials/City-Council`
  plus the per-ward pages `…/City-Council/Ward-1` through `…/Ward-8` (each member has
  an official city bio page) and the Mayor page under Elected Officials.
- **Cross-check:** Ballotpedia (`https://ballotpedia.org/Oklahoma_City,_Oklahoma`),
  Wikipedia (`https://en.wikipedia.org/wiki/Oklahoma_City_Council`), and local news
  (KFOR / NonDoc / KGOU / The Oklahoman). The official okc.gov pages 403'd to the
  fetcher — roster below is built from okc.gov page *titles/snippets* + Wikipedia +
  news corroboration (see caveats).

**Form of government:** **council-manager**. A professional **City Manager** runs
operations; the **Mayor is a voting member of the City Council** and presides over it
(President of the Council) — a **weak/ceremonial mayor**, the opposite of Colorado
Springs' separated executive. **9 total seats = Mayor (elected at-large) + 8 Ward
members (one per ward).** **4-year terms.** **Nonpartisan** elections (no party label
on the ballot). Elections are staggered (February primary / April runoff cycle); the
**Mayor was re-elected to a third term on February 10, 2026** (~86%).

| Seat | Name | Notes |
|---|---|---|
| Mayor (at-large; on Council) | David Holt | Re-elected to a **3rd term Feb 10 2026** (~86%); presides over Council |
| Ward 1 | Bradley Carter | Re-elected (2025 cycle) |
| Ward 2 | James Cooper | |
| Ward 3 | Katrina Avers | Elected **Feb 11 2025** (~73.9%); appears as "Katrina Bedell Avers" |
| Ward 4 | Todd Stone | Re-elected (2025 cycle) |
| Ward 5 | Matt Hinkle | Won **April 2025 runoff** (succeeded David Greenwell) |
| Ward 6 | JoBeth Hamon | |
| Ward 7 | Camal Pennington | Won **April 1 2025 runoff** for the Ward 7 seat |
| Ward 8 | Mark Stonecipher | |

**Party note:** OKC Council elections are **formally nonpartisan** — no party appears
on the ballot. Wikipedia/news associate members with parties informally; any RESOLUTE
party tag would be **inferred from record, not the ballot**, and must be cited as such.
Do not present these as ballot affiliations.

Roster sources: `https://www.okc.gov/Government/Elected-Officials/City-Council`,
`https://www.okc.gov/Government/Elected-Officials/City-Council/Ward-7`,
`https://www.okc.gov/Government/Elected-Officials/City-Council/Ward-3`,
`https://en.wikipedia.org/wiki/Oklahoma_City_Council`,
`https://ballotpedia.org/Oklahoma_City,_Oklahoma`.

---

## Readiness verdict

**Yellow — clean video, sourced roster, but a brand-new document vendor.** The video
leg is strong (official **YouTube `cityofokc`** with live + dated per-year playlists,
the Raleigh/Nashville pattern that transfers) and the roster is sourced to official
per-ward city pages plus Ballotpedia/Wikipedia/news. The drag is the agenda leg:
**PrimeGov** is confirmed and resident-facing, but it is the **first PrimeGov city in
the program**, so there is no existing scraper to reuse. Four things to decide before
a build: (1) **ingest YouTube** (`cityofokc` channel/playlists) as the video source of
record — the YouTube-VOD pattern transfers from Raleigh/Nashville; (2) **build a
PrimeGov adapter** for `okc.primegov.com` — the Legistar scraper does **not** carry
over, this is net-new vendor work and the main cost of this city; (3) the executive
model is **council-manager with the Mayor ON Council** (President of the Council), so
the profile build treats the Mayor as a council seat **and** flags the City Manager as
the unelected operations head (opposite of Colorado Springs); (4) the **party-label
question** is the same as the nonpartisan cities (F1/F2/J2/J4/Colorado Springs) —
elections are **nonpartisan**, so party tags are inferred-from-record, not the ballot.

## Caveats / unverified

- **okc.gov returned HTTP 403 to the fetcher** on every attempt (Council page, Public
  Meetings page, ward pages). Roster, form-of-government, cadence, and broadcast
  details come from **okc.gov page titles/search snippets + Wikipedia + local news
  (KFOR / KGOU / NonDoc / The Oklahoman / A Better Life OKC)**, not a directly-fetched
  okc.gov render. The official ward bio pages (`…/Ward-1`…`Ward-8`) and Mayor page are
  confirmed to **exist** (appear in search results) but were not fetch-rendered.
- **YouTube channel JS-rendered empty to the fetcher:** the `cityofokc` channel and
  the 2026/2025 playlists are confirmed to exist and to be the city's stated VOD home,
  but the **exact title/date of the most recent regular-meeting video could not be
  fetch-confirmed**. The dated meeting cited (**June 17, 2026 special meeting**) comes
  from the okc.gov events directory snippet, not a fetched YouTube row. Confirm the
  latest regular-meeting VOD date by hand before building.
- **PrimeGov portal rendered as a loading/template state** to the fetcher — vendor
  identity (PrimeGov, a Granicus product) is confirmed from the portal markup and
  search results, but **no specific meeting rows, agenda PDFs, or a most-recent
  PrimeGov meeting date were captured**. Verify the archived-meeting list and agenda
  PDF URLs directly before building the adapter.
- **Party associations are NOT ballot affiliations** — OKC elections are nonpartisan.
  The informal party tags (e.g., from Wikipedia) are inferred-from-record only.
- **Term limits:** OKC mayors/council serve **4-year terms**; search results indicate
  **no hard term limit** (Holt won a 3rd term). Confirm against the City Charter if a
  hard citation is needed.
- **Ward 5 succession:** Matt Hinkle won the April 2025 runoff; an older snippet listed
  **David Greenwell** for Ward 5 — that is stale, disregard it.
- **Confirmed across ≥2 independent sources:** the 8-ward + at-large-mayor structure,
  the council-manager form with the mayor on Council, the 4-year term, the nonpartisan
  ballot, the `cityofokc` YouTube VOD home + Cox Ch. 20, the PrimeGov agenda vendor,
  Holt's Feb 10 2026 third-term win, and the 2025 ward winners (Avers, Hinkle,
  Pennington).
