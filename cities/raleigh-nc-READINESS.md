# RESOLUTE Local — Readiness: Raleigh, NC

**Status:** Research only (J2 scaffold). No code, no profiles, no scorecard data yet.
**Compiled:** 2026-06-17. EXPANSION-PLAN target #2 (Raleigh, NC).

Raleigh is a strong expansion candidate: it splits **video** (Granicus/RTN +
an official YouTube Live feed) from **documents** (BoardDocs), and both halves
are public and stable. The YouTube feed is a closer match to the EXPANSION-PLAN
spec than Richmond's Granicus-only stack, but the document side uses a different
vendor (BoardDocs, not Legistar/CivicPlus) — plan two ingest paths, not one.

---

## Meeting broadcaster (video)

- **Vendor:** Granicus (city portal `raleigh.granicus.com`), branded publicly as
  **RTN — Raleigh Television Network (cable Channel 11)**. An official
  **YouTube Live** feed runs in parallel as a backup.
- **Live stream:** three concurrent options —
  - Granicus player (click the "RTN 11 / In Progress" link when a meeting is in
    session): `https://raleigh.granicus.com/ViewPublisher.php?view_id=24`
  - YouTube Live (official City of Raleigh channel):
    `https://www.youtube.com/c/cityofraleigh/live`
  - Cable: RTN Channel 11.
- **On-demand archive:** the same Granicus "Streaming Video" portal lists prior
  City Council, Planning Commission, Board of Adjustment, and other meetings:
  `https://raleigh.granicus.com/ViewPublisher.php?view_id=24`
- **TV/cable notes:** RTN-11 runs continuously (live meetings when in session,
  recent recordings otherwise). The city offers YouTube as a backup live feed and
  explicitly disclaims YouTube's post-meeting recommended videos/ads.
- **Note vs. EXPANSION-PLAN spec:** Raleigh satisfies the YouTube path **and** has
  a Granicus archive. The recap pipeline can target either the YouTube Live VOD or
  the Granicus clip portal; the YouTube channel is the cleaner ingest source.

Sources:
`https://raleighnc.gov/engage-city/services/watch-city-council-and-select-meetings-live`,
`https://raleighnc.gov/engage-city/services/watch-rtn-live-or-demand-videos`,
`https://raleighnc.gov/raleigh-television-network-rtn-and-video-services`.

## Agenda center (agendas / minutes)

- **Vendor:** **BoardDocs** (Diligent BoardDocs Plus) — **not** Legistar/CivicPlus.
- **Agenda / minutes URL:** `https://go.boarddocs.com/nc/raleigh/Board.nsf/Public`
  (the public portal returns HTTP 403 to automated fetches, but it is the live
  link the city directs residents to).
- **What it provides:** City Council (plus boards/commissions) agendas and minutes
  organized by meeting date. Meeting **video** links live separately on the
  Granicus portal — Raleigh splits documents (BoardDocs) from video (Granicus/RTN).
- **City page that points to it:**
  `https://raleighnc.gov/government/services/city-council-boards-and-commissions-agendas-and-minutes`

## Council roster source

- **Primary (official):** `https://raleighnc.gov/city-council`
  and `https://raleighnc.gov/government/services/council-meetings/council-contacts`
- **Cross-check:** Ballotpedia (`https://ballotpedia.org/Raleigh,_North_Carolina`);
  mayor page `https://ballotpedia.org/Janet_Cowell`; 2024 city elections
  `https://ballotpedia.org/City_elections_in_Raleigh,_North_Carolina_(2024)`.

**8 members = Mayor + 2 At-Large + 5 District (A–E).** Seats are formally
**nonpartisan** (like Fredericksburg + Richmond) — expect the same party-label
reconciliation question the F1 audit flagged.

| Seat / District | Name | Notes |
|---|---|---|
| Mayor | Janet Cowell | Citywide; elected Nov 5 2024, sworn in Dec 2 2024 |
| At-Large | Stormie D. Forte | Citywide at-large seat |
| At-Large | Jonathan Lambert-Melton | Citywide at-large seat |
| District A | Mitchell Silver | |
| District B | Megan Patton | |
| District C | Corey Branch | |
| District D | Jane Harrison | Mayor Pro Tem |
| District E | Christina Jones | |

Roster source: `https://raleighnc.gov/city-council` and
`https://raleighnc.gov/government/services/council-meetings/council-contacts`.

**Term window:** current members were elected **Nov 5 2024**, sworn in
**Dec 2 2024**, to **two-year terms** (2024–2026). Last election Nov 5 2024; next
election **Nov 3 2026** with a nonpartisan **primary Mar 3 2026**. Sources:
`https://raleighnc.gov/government/news/city-council-swearing-ceremony-dec-2`,
`https://raleighnc.gov/engage-city/news/city-council-moves-four-year-terms-staggered-elections`.

**Term-structure change (2026 onward):** City Ordinance (2024) 627 moves Raleigh
to **four-year staggered terms** starting with the 2026 election — in 2026 the
Mayor, the top at-large vote-getter, and Districts A and B get four-year terms;
the other at-large seat and Districts C/D/E get two-year terms, converting to
four-year in 2028. Source:
`https://raleighnc.gov/engage-city/news/city-council-moves-four-year-terms-staggered-elections`.

---

## Readiness verdict

**Green, with one ingest caveat.** Broadcaster (Granicus/RTN + YouTube Live),
agenda center (BoardDocs), and roster all sourced and stable. Three things to
decide before a build: (1) the recap pipeline can use the **YouTube Live VOD**
(cleaner than Granicus) — confirm the channel publishes per-meeting VODs;
(2) the document path is **BoardDocs**, a different vendor from Fredericksburg's
stack — a separate scraper from the video path; (3) reconcile the formally
**nonpartisan** city labels against RESOLUTE's party tags (same open question as
F1/F2). No code written here.

## Caveats / unverified

- **District-letter conflict (resolved):** a Dec 2024 swearing-in recap
  (enlacelatinonc.org) labeled seats differently (calling Silver "at-large" and
  shifting the district letters, listing only 7 members). The two **current
  official raleighnc.gov pages** both independently give Silver=A, Patton=B,
  Branch=C, Harrison=D, Jones=E with Forte + Lambert-Melton at-large — those are
  treated as authoritative here; the news recap appears garbled/outdated.
- **Ballotpedia main page:** `ballotpedia.org/Raleigh,_North_Carolina` would not
  return content to automated fetch; the URL is valid and is the right cross-check.
  Roster facts were confirmed via the Cowell + 2024-city-elections Ballotpedia
  pages instead. A human should open the main page to visually confirm the table.
- **BoardDocs 403:** the portal blocks bots, so its contents could not be
  machine-read — multiple city pages confirm it as the agenda/minutes host.
- **Name spelling:** official pages render District C as **Corey Branch** (one
  secondary source spelled it "Cory Branch") — use the raleighnc.gov spelling.
- **"3 at-large" phrasing:** some secondary sources count the mayor as one of
  "3 at-large." Functionally there are 2 council at-large seats plus the
  separately elected mayor (8 total).
