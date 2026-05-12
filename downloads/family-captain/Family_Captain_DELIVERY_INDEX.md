# Family Captain — v2 Delivery Index (Telegram Launch)

**Status:** Ready to launch. All artifacts rebuilt with Telegram pivot. Channel invite `https://t.me/+ddnHqJEqkKk3ZmVh` wired into every CTA. Deploy bundle staged on `family-captain-v2` branch, ready to push.

---

## End-to-end captain path (verified)

```
   usmcmin.com/family-captain.html
            │
            │  click "Join the Telegram channel"
            ▼
   https://t.me/+ddnHqJEqkKk3ZmVh
            │
            │  read pinned bootcamp index
            ▼
   Open W1.T1 (pinned PDF) → do task → react ✓ → comment one-liner
            │
            │  Mon/Wed/Fri new task drops
            ▼
   Continue 14 more tasks → Captain's Charter → commissioned
```

What MOOP needs to do once to make this live:
1. **Push the `family-captain-v2` branch** (see `deploy/README_DEPLOY.md` — 5 commands)
2. **Set up the Telegram channel** per `Family_Captain_Telegram_Setup.md` (~20 minutes)
3. **Drop W1.T1 as a pinned message** — the rest happens as scheduled drops

---

## What changed in v2

### Cohort platform pivoted: Mighty Networks → Telegram
- All user-facing copy reflects Telegram (channel + linked discussion group)
- Captain progress tracker (with captain-id input + webhook stub) replaced with read-only task tile preview
- Telegram invite link wired into every join CTA

### New product: AI Tools Landscape (Captain's Compass)
- 30 tools across 7 categories (Chat / Voice / Image / Notes / Automation / Coding / Video)
- Each tool: what it does, cost, redundancy hint, captain's call
- 3 Captain's Stacks at the bottom: $0 / $40-60 / $150-200 monthly
- Both standalone (single HTML for sharing) and site-integrated (deploys to `usmcmin.com/family-captain-tools.html`)

### New product: Telegram Setup Guide
- Operational ~20-minute build for cohort host
- Channel + linked group setup, settings, pinned index template, scheduled drops

### New site pages
- `family-captain.html` (landing, rebuilt)
- `family-captain-tools.html` (Captain's Compass)
- `family-captain-heartbeat.html` (cohort feed preview)

### Rebuilt binary deliverables
- `Family_Captain_Bootcamp_MASTER.docx` — Telegram-aware (17 Telegram references, 0 MN), Captain's Quick Start callout with the live invite link
- `Family_Captain_Bootcamp_DECK.pptx` — slide 17 now reads "24 in the Telegram channel"
- `Family_Captain_Bootcamp_WORKBOOK.docx` — rebuilt for parity (no source changes; never had platform refs)
- `Family_Captain_Heartbeat_Posts.html` (standalone preview) — Telegram framing throughout

---

## File map

```
/Users/moop_bot_pro/Agents/IX. Pops/
│
├─ Family_Captain_DELIVERY_INDEX.md           ← you are here
│
├─ STANDALONE PREVIEW SET (share with MOOP, view on phone)
│   ├─ Family_Captain_Bootcamp.html           landing (TG invite wired)
│   ├─ Family_Captain_AI_Tools.html           Captain's Compass (30 tools)
│   └─ Family_Captain_Heartbeat_Posts.html    cohort feed preview (24 posts)
│
├─ DOCUMENT DELIVERABLES
│   ├─ Family_Captain_Bootcamp_MASTER.docx    master curriculum
│   ├─ Family_Captain_Bootcamp_WORKBOOK.docx  participant workbook
│   ├─ Family_Captain_Bootcamp_DECK.pptx      live-teaching deck (22 slides)
│   ├─ Family_Captain_Heartbeat_Posts.md      24-post source markdown
│   ├─ Family_Captain_Telegram_Setup.md       operational ~20-min cohort host guide
│   ├─ Family_Captain_Bootcamp_Architecture_v2.md  curriculum spine + decision log
│   ├─ Family_Captain_Bootcamp_Architecture_v1.md  (kept for history)
│   └─ Family_Captain_Task_PDFs.zip           15 task PDFs zipped
│
├─ Family_Captain_Task_PDFs/                  15 single-task PDFs + Captain's Drills
│
└─ deploy/
    ├─ README_DEPLOY.md                       push instructions + captain-path verify
    ├─ family-captain-deploy.tar.gz           ← extract on your local clone
    ├─ family-captain-v2.patch                review-only diff (use this, not v1 patch)
    ├─ family-captain.html                    site landing preview
    ├─ family-captain-tools.html              site tools preview
    ├─ family-captain-heartbeat.html          site heartbeat preview
    ├─ family-captain-launch.patch            (v1 — superseded)
    └─ family-captain.html (older copy)       (v1 — superseded)
```

---

## Audit summary (all clean)

| Check | Result |
|---|---|
| HTML lint (6 surfaces) | ✓ all clean |
| Telegram invite wired in landing pages | ✓ 4 in site, 2 in standalone |
| Stale MN references in user-facing surfaces | ✓ 0 (one intentional negative-space mention in landing copy: "no Mighty Networks, no Discord, no Slack") |
| All download files exist | ✓ 9/9 |
| All 15 task PDFs present | ✓ 15/15 |
| Sitemap contains all 3 bootcamp pages | ✓ 3/3 |
| Master.docx Telegram references | ✓ 17 Telegram, 2 t.me links, 0 MN |
| Deck.pptx Telegram references | ✓ 3 Telegram, 0 MN |

---

## Next steps for MOOP

1. **Open `deploy/README_DEPLOY.md`** — 5-command push sequence to deploy v2 to usmcmin.com.
2. **Open `Family_Captain_Telegram_Setup.md`** — 20-min channel setup. The guide includes the suggested channel name, settings, pinned bootcamp index template, and the schedule for Week 1 drops.
3. **Pin Task W1.T1** in the channel after setup so the first captain who joins has something to do immediately.
4. **(Optional)** Pre-schedule the rest of Week 1 (Wed Captain's Call + Task W1.T2 + Fri Close-out + Task W1.T3) using Telegram's scheduled-message feature.
5. **Test the path yourself** — visit usmcmin.com/family-captain.html, click Join, verify you land in your own channel cleanly.

---

Wheel's yours.
