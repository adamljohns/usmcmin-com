# RESOLUTE Local — Readiness: Nashville, TN

**Status:** Research only (J4 scaffold). No code, no profiles, no scorecard data yet.
**Compiled:** 2026-06-17. EXPANSION-PLAN target #4 — the **Metropolitan Government
of Nashville and Davidson County** ("Metro Nashville"), a consolidated city-county
government.

Nashville is the strongest video candidate yet: the city streams and archives
Metro Council meetings on an **official YouTube channel** (@MetroNashvilleNetwork)
with posting "within 1 business day," backed by a government-access cable network
(Metro Nashville Network) and a Roku app. Documents live on **Granicus Legistar**
(`nashville.legistar.com`) — the **same vendor as Richmond** (J/F2 target #1), so
the Legistar scraper planned for Richmond should largely transfer. The one scale
caveat: Metro Council has **40 members** (35 district + 5 at-large), the third-
largest city council in the U.S., so the roster build is bigger than any prior
target.

---

## Meeting broadcaster (video)

- **Government-access network:** **Metro Nashville Network (MNN)**, run by the
  Information Technology Services Department, gives "gavel-to-gavel coverage" of
  the Metropolitan Council and many boards/commissions. A second online-only
  channel (MNN2) carries overlapping meetings.
- **Cable:** Comcast/Xfinity ch. 3; AT&T U-verse ch. 99.
- **Roku:** dedicated MNN streaming app (launched April 2026).
- **Archive (use this):** official **YouTube channel — "Metro Nashville Network,"
  handle `@MetroNashvilleNetwork`**:
  `https://www.youtube.com/@MetroNashvilleNetwork`
  (also reachable at `https://www.youtube.com/MetroNashville`). Meetings stream
  live on YouTube and post on-demand **within 1 business day** of taping.
- **Online watch page (Cablecast):** `https://nashville.cablecast.tv/watch-now?site=1`
- **Meeting cadence:** regular Metro Council meetings are the **1st and 3rd
  Tuesdays** monthly at **6:30 PM**, David Scobey Council Chamber, Historic Metro
  Courthouse, One Public Square.
- **Second video path (vendor-side):** council video from **Oct 2020 onward** is
  also embedded in the Legistar portal; pre-Oct-2020 video lives on YouTube.
- **No Vimeo** presence found.
- **Note vs. EXPANSION-PLAN spec:** Nashville fully satisfies the YouTube path
  (like Raleigh, and unlike Greenville's Webex live layer) — ingest the
  **YouTube per-meeting VOD** off `@MetroNashvilleNetwork`.

Sources:
`https://www.nashville.gov/departments/information-technology-services/cable-television-services/metro-nashville-network/live`,
`https://www.nashville.gov/departments/information-technology-services/cable-television-services/metro-nashville-network`,
`https://www.youtube.com/@MetroNashvilleNetwork`,
`https://www.nashville.gov/departments/council/metro-council-meetings`,
`https://www.nashville.gov/departments/mayor/news/metro-nashville-network-launches-new-streaming-app-across-major-platforms`.

## Agenda center (agendas / minutes)

- **Vendor:** **Granicus Legistar** (confirmed via granicusops.com asset paths on
  the portal) — the **same vendor as Richmond** (`richmondva.legistar.com`), so the
  scraper transfers. **Not** BoardDocs (Raleigh), **not** CivicClerk (Greenville).
- **Resident-facing portal:** `https://nashville.legistar.com/` — the "Metro
  Government Legislative Information Center," run by the Metropolitan Clerk's
  Office (legislation from 1998 on, meeting records, agendas, minutes, and video
  Oct 2020+). Calendar: `https://nashville.legistar.com/Calendar.aspx`
- **nashville.gov pages that point to it:**
  `https://www.nashville.gov/departments/metro-clerk/legislative/minutes` (minutes
  archive); `https://www.nashville.gov/departments/council/boards/metro-council/meetings`
  (meeting browser).
- **"InSite" branding:** a Metro news release calls the post-2021 legislative site
  "InSite" (auto-updating agendas, minutes, packets, video). Appears to be the same
  Granicus/Legistar-backed system; exact front-end relationship unconfirmed.
- **Split-vendor note:** unlike Richmond, Nashville's Legistar portal *also* embeds
  the council video (Oct 2020+), so docs and recent video can come from one path —
  but YouTube remains the cleaner, faster VOD source.

Sources:
`https://nashville.legistar.com/`,
`https://nashville.legistar.com/Calendar.aspx`,
`https://www.nashville.gov/departments/metro-clerk/legislative/minutes`,
`https://www.nashville.gov/departments/council/news/metro-government-makes-broad-enhancements-legislative-process`.

## Council roster source

- **Primary (official):** `https://www.nashville.gov/departments/council`
  (includes a downloadable "Council Member Roster 2023-2027" PDF, a member lookup,
  and a district map).
- **Cross-check:** Ballotpedia (`https://ballotpedia.org/Nashville,_Tennessee`)
  + Wikipedia (`https://en.wikipedia.org/wiki/Metropolitan_Council_of_Nashville_and_Davidson_County`).

**40 members = 35 single-member Districts + 5 At-Large.** Third-largest city
council in the U.S. (behind Chicago and New York). Four-year terms, 2-consecutive-
term limit. **Nonpartisan** ballot (no party labels). Last general election
**Aug 1, 2023**; current term **2023–2027**. The popularly elected **Vice Mayor**
presides over Council and votes only to break ties.

| Seat | Name | Notes |
|---|---|---|
| Mayor | Freddie O'Connell | 10th Mayor; took office Sept 25 2023; term 2023–2027 (announced May 2026 he'll seek a 2nd term) |
| Vice Mayor (presides) | Angie Henderson | Popularly elected; took office Sept 1 2023; votes only to break ties |
| At-Large | Zulfat Suara | President pro tempore |
| At-Large | Delishia Porterfield | |
| At-Large | Quin Evans Segall | |
| At-Large | Burkley Allen | |
| At-Large | Olivia Hill | |
| Districts 1–35 | (see official roster PDF) | Full district list cross-checked below against Wikipedia; verify against the official lookup before ingest |

**Districts 1–35 (per Wikipedia — verify against the official roster PDF):**
1 Joy Kimbrough · 2 Kyonztè Toombs · 3 Jennifer Gamble · 4 Mike Cortese ·
5 Sean Parker · 6 Clay Capp · 7 Emily Benedict · 8 Deonte Harrell ·
9 Tonya Hancock · 10 Jennifer Frensley Webb · 11 Jeff Eslick · 12 Erin Evans ·
13 Russ Bradford · 14 Jordan Huffman · 15 Jeff Gregg · 16 Ginny Welsch ·
17 Terry Vo · 18 Tom Cash · 19 Jacob Kupin · 20 Rollin Horton ·
21 Brandon Taylor · 22 Sheri Weiner · 23 Thom Druffel · 24 Brenda Gadd ·
25 Jeff Preptit · 26 Courtney Johnston · 27 Robert Nash · 28 David Benton ·
29 Tasha Ellis · 30 Sandra Sepulveda · 31 John Rutherford · 32 Joy Styles ·
33 Antoinette Lee · 34 Sandy Ewing · 35 Jason Spain.

Roster sources: `https://www.nashville.gov/departments/council`,
`https://www.nashville.gov/departments/council/districts/vice-mayor`,
`https://www.nashville.gov/departments/mayor/people/freddie-oconnell`,
`https://en.wikipedia.org/wiki/Metropolitan_Council_of_Nashville_and_Davidson_County`.

---

## Readiness verdict

**Green — strongest video stack so far, one scale caveat.** Broadcaster (YouTube
`@MetroNashvilleNetwork`, ~1-business-day posting + cable + Roku + Cablecast),
agenda center (Granicus Legistar — **reuses the Richmond scraper**), and roster
source are all sourced and stable. Three things to decide before a build:
(1) ingest the **YouTube per-meeting VOD** (Legistar also embeds Oct-2020+ video,
but YouTube is faster/cleaner); (2) the document path is **Legistar**, the first
*repeat* vendor across the expansion set (Richmond), so the scraper transfers
rather than needing a new one; (3) the party-label question is the **same as
F1/F2/J2** (not the inverse like Greenville) — Nashville elections are formally
**nonpartisan**, so RESOLUTE's party tags would be inferred from record, not from
the ballot. The distinguishing factor is **scale**: a **40-member** council (35
district + 5 at-large) is the largest roster in the program — budget for that in
the profile build.

## Caveats / unverified

- **MNN landing page 403'd to the fetcher:** the main
  `.../metro-nashville-network` page returned HTTP 403; broadcaster details were
  reconstructed from its `/live` subpage, search snippets of the same page, and the
  YouTube channel. The "within 1 business day" posting claim comes from a snippet of
  the 403'd page — high-confidence but not retrieved in full.
- **`stream.nashville.gov` not confirmed:** referenced in some snippets as a live
  URL but did **not** appear on the directly-fetched `/live` page (which gave the
  Cablecast URL). Rely on the Cablecast watch page + YouTube, not `stream.nashville.gov`.
- **35-district list is from Wikipedia, not the official PDF:** the official
  "Council Member Roster 2023-2027" PDF is linked from
  `nashville.gov/departments/council` but its direct file URL was not captured;
  the live member lookup on that page is the authoritative source. Cross-check each
  district name against it before ingest — and note district seats can change
  mid-term (resignations / special elections); the Wikipedia list reflects the 2023
  outcome.
- **"InSite" vs. Legistar relationship unconfirmed:** the directly-fetched Legistar
  page showed no "InSite" branding; "InSite" is only named in a nashville.gov news
  release. They appear to be the same Granicus/Legistar system, but the exact
  front-end relationship was not definitively confirmed.
- **Confirmed by ≥1 official nashville.gov source + Wikipedia:** Mayor, Vice Mayor,
  President pro tempore, all 5 at-large members, the 40-member structure, the
  nonpartisan ballot, and the 2023–2027 term window.
