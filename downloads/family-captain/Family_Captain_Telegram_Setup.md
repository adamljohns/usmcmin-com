# Family Captain Boot Camp — Telegram Setup Guide

**Decision (2026-05-08):** Bootcamp pivots from Mighty Networks to **Telegram**. Rationale: most men already have Telegram or can install in 60 seconds; no second-app friction; free; supports the channel + comments shape we want.

This guide is **operational** — do these steps in order. ~20 minutes total.

---

## The Shape (read once, then build)

You're creating two linked things:

1. **A public Channel** — Adam-only posting. The bootcamp index, the 15 task posts, the heartbeat posts, the materials all live here as broadcast posts. Captains read.
2. **A linked Discussion Group** — auto-created by Telegram when you "Add Discussion" to the Channel. This is where comments on Channel posts land. Captains discuss.

When a captain joins the Channel and clicks **Comments** on any post, Telegram auto-joins them to the linked Group transparently. They never see "join two things" — they just see the channel.

**Progress tracking model (no bot needed):**
- Captain ships Task W1.T1.
- He **reacts ✓** on the W1.T1 channel post.
- He **drops a one-line comment**: "shipped — wrote 5 lines, posted one in the comments."
- That's the cohort signal. Reactions roll up automatically; comments are the iron-on-iron.

---

## Step 1 — Create the Channel (5 min)

1. Open Telegram (mobile or desktop).
2. Tap the pencil/new-chat icon → **New Channel**.
3. **Channel name:** `Family Captain Boot Camp` (or `USMC Family Captain` — your call)
4. **Description (paste):**
   > 5 weeks. 15 tasks. One captain. Christ-centered AI use for husbands, fathers, and leaders. Claude and Cowork primary. AI on the bridge as a trusted aide — not the autopilot. Run by U.S.M.C. Ministries.
5. **Channel type:** Public (so captains can find it via link).
6. **Public link:** try `t.me/FamilyCaptainBootCamp` or `t.me/USMCFamilyCaptain` — Telegram will tell you if it's taken.
7. Upload your channel **photo** (the USMC logo from `assets/img/logo.png` works).

## Step 2 — Add the Discussion Group (3 min)

1. Open the channel → tap channel name (header) → **Edit** → **Discussion**.
2. Tap **Create Group** (Telegram auto-creates one linked to this channel).
3. **Group name:** `Family Captain — Captains' Mess` (or just `Family Captain Discussion`).
4. **Permissions** (group settings → Manage Group → Permissions):
   - Send Messages: ✅ (captains comment)
   - Send Photos / Videos / Files: ✅ (captains share screenshots of charters, fridges, etc.)
   - Polls: ✅ (you'll use these for weekly check-ins)
   - Pin Messages: ❌ (admin only)
   - Add Members: ❌ (channel-driven membership only)

## Step 3 — Channel Settings (2 min)

In the channel → **Edit** → **Channel Settings**:
- **Sign Messages**: ✅ (so posts read as "Adam 'MOOP' Johns" instead of just "Channel")
- **Reactions**: enabled, allow custom emoji
- **Slow Mode** in Discussion Group: 15 seconds (prevents spam without killing flow)

## Step 4 — Drop the Bootcamp Index Post (PINNED)

Post this in the channel, then long-press → **Pin**.

```
🛡️ FAMILY CAPTAIN AI BOOT CAMP

5 weeks. 15 tasks. One captain. Christ at the center.

WHAT TO EXPECT
• Tasks drop Mon / Wed / Fri (3 per week × 5 weeks).
• Each task = 20-30 min. Imperfect actions count.
• React ✓ on a task post when you ship it.
• Drop a one-line "what shipped, what slipped" in the comments.
• Heartbeat posts run alongside — Monday Kickoff, Wed Captain's Call, Fri Close-out.
• Optional: 35 Captain's Drills (90-second daily micro-prompts).

THE 5 WEEKS
1. Foundations: The Captain's Mindset
2. Personal OS: Daily Rhythm with AI
3. At Home: Husband, Father, Brother
4. Business / Ministry: Where Leverage Lives
5. Mastery & Multiplication: Train the Next Captain

Materials are pinned below. Tap, read, ship.

— Adam "MOOP" Johns
```

## Step 5 — Upload the Bootcamp Materials (5 min)

In the channel, attach each file as a **Document** (paperclip icon → File). Telegram allows up to 2GB per file; our largest (the deck) is under 500KB so we're fine.

Upload these one at a time, each with a short caption:

| File | Caption |
|---|---|
| `Family_Captain_Bootcamp_MASTER.docx` | "Master curriculum — full week + task breakdown, Captain's Drills, Charter template." |
| `Family_Captain_Bootcamp_WORKBOOK.docx` | "Participant workbook — print-friendly. One page per task." |
| `Family_Captain_Task_PDFs.zip` | "All 15 task PDFs in one zip. Or wait for them to drop one at a time below." |
| `Family_Captain_Bootcamp_DECK.pptx` | "Live-teaching deck — for cohort hosts who want to teach this in person or on video." |
| `Captains_Drills_35.pdf` | "Optional: 35 ninety-second Captain's Drills. Skip without guilt." |

After uploading the deck, **pin** the master and workbook (long-press → Pin). The bootcamp index from Step 4 stays pinned as the top message.

## Step 6 — Schedule the Cohort Drops (10 min)

Telegram supports **scheduled messages** (long-press the send button → Schedule). Pre-schedule the bootcamp launch sequence so you don't have to remember:

**Week 0 — pre-launch**
- Day -7: pin "Doors open Day 1. Start when you're ready."

**Week 1 launch (Monday Day 1)**
- 0700 — Heartbeat: Monday Kickoff (W1.M from `Family_Captain_Heartbeat_Posts.md`)
- 0800 — Task W1.T1: attach `W1_T1_Write_Your_AI_Charter.pdf` with caption "Task 1: Write your AI charter. 5 lines. 25 minutes. Post one line in the comments when you ship."

**Week 1 — rest of week**
- Wed 0700 — Heartbeat: Captain's Call (W1.W)
- Wed 0800 — Task W1.T2: attach the W1_T2 PDF
- Fri 0700 — Heartbeat: Close-out (W1.F)
- Fri 0800 — Task W1.T3: attach the W1_T3 PDF

Repeat the pattern for Weeks 2-5. Scripture Anchors (5) drop pinned as each week opens. Bonus Drops (4) fire whenever the cohort needs them.

**The 24 heartbeat posts are already drafted in:** `Family_Captain_Heartbeat_Posts.md` (and styled HTML preview at `Family_Captain_Heartbeat_Posts.html`). Copy/paste into the channel as scheduled posts.

## Step 7 — Comment / Reaction Conventions (post pinned in Discussion Group)

In the **Discussion Group**, post and pin this:

```
COHORT CONVENTIONS

When you ship a task:
✅ React with ✓ on the task post in the channel
💬 Drop a one-liner here: what shipped, what slipped, what surprised you

Voice: brotherly, captain-to-captain. Be honest. Don't perform.

When in doubt, take the imperfect action and post about it.
```

---

## Formatting Cheat Sheet (Telegram Markdown)

Telegram's mobile app uses a slightly different markdown than typical:

- **Bold:** `*bold*` (single asterisks) — note: NOT double asterisks like in standard Markdown
- **Italic:** `_italic_`
- **Strikethrough:** `~strikethrough~`
- **Code:** `` `code` `` (single backticks) or ```` ``` ```` for blocks
- **Link:** `[text](https://url)` — works the same as standard MD
- **Custom emoji & reactions:** add via the emoji picker; premium users can use animated

For the heartbeat posts, the existing `**bold**` from the .md source needs to be converted to `*bold*` for Telegram. **Quick conversion script** if you want to batch-convert:

```bash
# In your Family_Captain_Heartbeat_Posts.md folder:
sed 's/\*\*\([^*]*\)\*\*/*\1*/g' Family_Captain_Heartbeat_Posts.md > Heartbeat_Telegram.md
```

Or paste each post into Telegram and manually edit the bold markers. ~30 seconds per post.

---

## File-Size Reality Check

- Telegram caps single uploads at **2 GB per file** (4 GB for Premium senders).
- Our entire bundle including the deck is well under 1 GB.
- Captains downloading on phones: PDFs open in-app; .docx / .pptx open in their phone's Office app or Google Docs.

## Channel Privacy Posture

For **soft launch**: Channel public (so guys can find via link), Discussion Group **private** but linked (only channel followers can comment, no random outsiders).

When you're ready to hard-launch: keep it the same. Just promote the link more publicly.

To **gate by invitation only** later: switch the Channel to **Private** with an invite link you control (Edit → Channel Type → Private). Comments still flow through the linked group; non-members can't see the channel at all.

---

## What the Captain's Day-1 Experience Looks Like

1. Adam shares the channel link via DM, email, or in person.
2. Captain taps the link, hits **Join**, sees the pinned bootcamp index.
3. Scrolls down — sees the master curriculum (.docx), workbook (.docx), and Task W1.T1 (PDF) already posted.
4. Taps the W1.T1 PDF, reads it, does the task in his own time.
5. Comes back, taps the W1.T1 post in the channel, hits ✓ reaction, taps **Comments**, drops his one-liner.
6. Telegram auto-joins him to the discussion group. He sees other captains' one-liners. Iron sharpens iron.
7. Wednesday morning, he gets a notification: heartbeat post + Task W1.T2 just dropped.

That's it. No second app. No funnel. No download.

---

## What Changes vs. The Mighty Networks Plan

| Was | Now |
|---|---|
| MN bootcamp post + comments | Telegram channel index post (pinned) + linked discussion group |
| MN feed of heartbeat posts | Telegram channel posts, scheduled in advance |
| MN comments per post | Comments on each Channel post (auto-route to linked group) |
| MN custom reactions | Telegram reactions (✅, 🔥, 💯, custom emoji) |
| MN's "captains" tag | @username mentions in the discussion group |
| Web progress tracker (your `family-captain.html` page) | Stays as-is on usmcmin.com — captains can use it as a personal log; no webhook to MN required |

The bootcamp curriculum itself doesn't change. The platform under it does.

---

## What To Do Once This is Live

1. Send Adam (you) a test message from a second account to verify the channel + comments flow works end-to-end.
2. Pre-schedule Week 1's content (heartbeat + 3 tasks).
3. Invite **2-3 trusted brothers** as a private pilot before opening the link wider.
4. Confirm `usmcmin.com/ai-boot-camp.html` is live and the "Join the Telegram channel" button routes to your invite link (`https://t.me/+ddnHqJEqkKk3ZmVh`).

---

## Bot Setup — MoopBotPro (Adam's Openclaw agent in the channel)

If you've added a bot like **MoopBotPro** to the channel + linked discussion group, it can serve as a 24/7 study partner for captains: answer questions, recall the curriculum, surface scripture, gently nudge accountability. Three settings decide whether it actually *works* — and one mindset decides whether it should.

### Three settings (do these on day one)

**1. Turn off Privacy Mode** (so the bot can see all group messages, not just commands).

By default, Telegram bots in groups only see (a) commands starting with `/`, (b) @mentions, and (c) replies to their own messages. For natural-language Q&A — "MoopBotPro, what was Task W2.T3 again?" — the bot needs to see everything. Turn this off:

- DM `@BotFather` in Telegram
- `/mybots` → select **MoopBotPro** → **Bot Settings** → **Group Privacy** → **Turn off**
- BotFather will confirm: *"Privacy mode is disabled."*

**2. Add MoopBotPro as a group Administrator** (so it can post replies cleanly and read history).

- In the linked Discussion Group → tap group name → **Administrators** → **Add Administrator**
- Search "MoopBotPro" → add
- **Grant:** Send Messages, Pin Messages (optional), Delete Messages (optional)
- **Don't grant:** Add New Admins, Change Group Info, Ban Users — those decisions belong to a human captain

**3. Set the bot's command list** (so the in-app `/` menu surfaces what captains can do).

In `@BotFather`: `/mybots` → MoopBotPro → **Edit Bot** → **Edit Commands** — paste:

```
start - Get oriented in the bootcamp
task - Open the current week's task PDF
drill - Today's optional 90-second Captain's Drill
scripture - Today's Scripture anchor
ask - Ask MoopBotPro a question
help - How to use this bot
```

The commands appear in the menu; behavior is wired in your Openclaw backend.

### Pinned "intro the bot" post (paste in the discussion group)

```
🛡️ MEET MoopBotPro

He's not Adam. He's an AI adjutant on the bridge —
trained on the bootcamp materials, the scriptures we
use, and the captain's voice.

WAYS TO TALK TO HIM
• Just type a question in the channel. He listens.
• Tap his name to DM him privately.
• Try: /task, /drill, /scripture, /ask, /help

WHAT HE IS / ISN'T
• He IS: a 24/7 study partner, prompt scratch pad,
  task-explainer, accountability nudge.
• He ISN'T: a substitute for the Spirit, the Word,
  your wife, or your brothers in this channel.

If MoopBotPro says something off — flag it in the
chat. He's an aide on the bridge, not the captain.

— Adam "MOOP" Johns
```

### What NOT to do

- **Don't auto-post task PDFs from the bot in the first cohort.** Drop them yourself the first time so you see the room react. Automate from cohort #2.
- **Don't grant the bot moderation powers** (Add New Admins, Ban Users). A misfired bot decision is hard to undo and erodes trust fast.
- **Don't connect the bot's brain to a model that can browse arbitrary URLs from the channel.** Captains share private things — charters, family-policy screenshots, screenshots of texts. Keep the bot's reach scoped to your own corpus.

### The tiered-autonomy reminder (now with a bot in the room)

The bootcamp's whole framework — informational / contextual / sensitive — applies to MoopBotPro the same way it applies to Claude in Cowork:

- **Informational** (let the bot answer): "What's Task W3.T2?" / "Show me Proverbs 3:5–6 in context." / "Summarize today's drill."
- **Contextual** (bot drafts, captain decides): "Help me draft a one-line ship comment for W1.T1." / "What's a Scripture anchor for the week I'm having?"
- **Sensitive** (bot stays out): Marriage conflict. Discipline questions. Anything moving money. Prayer. Discipline. Discernment. The bot is a study partner, not a counselor.

Captains who treat the bot like a counselor will get bad outcomes. Captains who treat it like the smartest brother in the channel — one who's always around, always remembers the materials, and never gets tired — will get good ones. Make sure the cohort knows the difference.

---

That's the build. Captain on the bridge. Bot on watch.
