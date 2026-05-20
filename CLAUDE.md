# usmcmin.com — Working Notes for Claude

## Brand voice
- Captain voice: direct, calm, plain. Talk to one operator, not a crowd.
- NO hype. No "revolutionary/game-changing/unlock/supercharge."
  No exclamation-point enthusiasm. Honesty over salesmanship —
  the "Captain's Call" recs tell people what to SKIP, and that's the brand.

## Visual rules
- Palette: muted golds + navy. Soft sage + light gray accents.
- TFC private track uses bronze #CE8E31 (text-bronze #8B5A1F, deeper button bronze #B07320)
  + slate #1E293B. USMC public track uses USMC navy + gold.
- No neon. No animations. No hover-jiggles. Static, calm, scannable.
- WCAG AA contrast minimum. Never encode meaning in hue alone — pair color with a
  letter, label, or shape.

## Tier system (S/A/B/C)
- S = START HERE (10–15%). A = CORE (30–40%). B = DEPTH (30–40%). C = OPTIONAL (15–20%).
- If everything is S, nothing is. Hold the distribution line.
- Visual: bronze S, slate A, sage B, gray C. Letter in white on a 32px circle, top-left
  of every task/tool card. Card border (2px) matches tier. C-tier cards at 80% opacity.
- Filter chip "Show S+A only" on Compass + Sovereign filter rows.

## Two-track architecture
- TRACK=usmc → 5-week public (Watchman lexicon, AI Mission branding).
- TRACK=fc   → 7-week private (Captain lexicon, TFC visual identity, Armada order:
  Vision → Body → Spiritual → Husbanding → Fathering → Finance → Sabbath).
- One `build/site_pages.py` source. `fc_track_builder.py` + `watchman_track_builder.py`
  are post-processors. Per-week pages emit only on TRACK=fc.

## Out of scope unless asked
- Don't touch the Heartbeat Posts page.
- Don't rewrite task/tool content (it's been through 6 iterations).
- Don't build wizards/quizzes.

## Before any page is "done"
- Open it in a browser. Verify at ~390px width.
- Type-checking ≠ feature-checking — actually look at it.
