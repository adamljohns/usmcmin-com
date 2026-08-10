# Field graphics — regeneration brief

**Status:** ready to run. Nothing here is wired into the site yet; the current
graphics stay live until replacements are approved.

## Why we are redoing these

Two reasons, and the first one is not cosmetic.

**1. The current graphics contain garbled text.** They were generated whole —
art and lettering together — by an image model, which cannot spell reliably.
Real examples from files that are live on usmcmin.com right now:

| File | Garbled text |
|---|---|
| `m01/marriage-vineyard-field-guide.png` | "share future **hepes**", "Barriers includes **viuunions**", "**affectting** employment" |
| `m04/marriage-healing-and-forgiveness-guide.png` | "**Chorge** and attack", "**Faar**", "**Ure the.** Ask your partner", "**unomodorated** disclosure", "expect an apology to **fis** everything" |
| `m05/navigating-the-family-tree-guide.png` | "We decide together **firat**" |

A man printing a marriage guide with misspelled words on it does not think
"AI artifact." He thinks the ministry does not proofread. On a course about
paying attention, that is the wrong first impression.

**2. No U.S.M.C. Ministries branding.** Every one carries a NotebookLM
watermark in the corner and nothing of ours.

## The method that fixes the spelling

Do **not** ask an image model to render the words. Ask it for the artwork with
**no text at all** (or with clearly marked empty label plates), then set the
type afterward in Canva/Affinity/Figma — or hand the art back and let me
composite the type, which guarantees the words match the module exactly.

If you do let the model set type, keep every label under four words and
proofread every single word at full zoom before accepting. Long sentences
inside a generated image is where the garbling always happens.

## Brand spec

- **Palette:** USMC navy `#1E3A5F` for headers and rules. One module accent per
  graphic, from the course palette — module 1 bronze `#8C5A1F`, 2 harbor
  `#2C6E8A`, 3 olive `#4C6B2F`, 4 clay `#9B4A3F`, 5 slate violet `#5B5A8C`,
  6 deep rose `#8A3F62`, 7 navy blue `#1E4E6B`. Neutrals: white, `#F4F5F7`
  panels, `#D1D5DB` borders.
- **Type:** Playfair Display for headings, a clean humanist sans for body.
  Static instances live in `tmc-husband/print/fonts/`.
- **Mark:** the U.S.M.C. Ministries shield, bottom right, at about 8% of the
  height, with "U.S.M.C. MINISTRIES · WARRIORS EQUIPPED" set small beside it.
  Remove the NotebookLM watermark.
- **Tone:** muted and calm. No neon, no gradients doing the work of hierarchy,
  no emoji. Illustration style: warm, realistic, non-cartoonish, mixed ages and
  builds, ordinary homes rather than showrooms.
- **Format:** PNG, 1536 × 2752 or larger, ≥ 2× the print size.

## Safety panel — non-negotiable

Every graphic that touches conflict, anger, forgiveness, family, or intimacy
keeps a visible red-flag panel that says, in plain words: this material assumes
a basically safe marriage; abuse, coercive control, addiction, or fear call for
confidential individual help first. The current graphics do carry this. Do not
lose it in the redesign.

## The twelve graphics

Prompts below assume "illustrated single-page field guide, portrait, panel
grid, no lettering — leave blank plates where labels go."

**Module 1 — bronze**
1. `marriage-connection-roadmap.png` — a roadmap of connection habits: protected
   weekly time, naming emotional needs, the four vineyard tasks.
2. `marriage-vineyard-field-guide.png` — a vineyard across four seasons of work:
   adjusting, pruning, supporting, renewing; end panel on the limits.

**Module 2 — harbor blue**
3. `mastering-marriage-communication.png` — three levels of conversation, from
   logistics to feeling; a listening posture panel.
4. `art-of-effective-communication.png` — the listen-back loop: hear, reflect,
   check, respond.

**Module 3 — olive**
5. `marriage-conflict-resolution-field-guide.png` — two people rowing the same
   boat against the problem; the five-step protocol; red-flag panel.
6. `marriage-conflict-and-teamwork-guide.png` — weathering a storm together; a
   conflict toolkit; a seven-day plan.
7. `marriage-teamwork-guide.png` — five cards: appreciation, differences,
   timing, support, repair.

**Module 4 — clay**
8. `marriage-healing-and-forgiveness-guide.png` — anger as an alarm bell, not a
   sin; two anger styles; the three-step repair; safety filter; seven-day plan.
9. `marriage-conflict-and-forgiveness-guide.png` — what forgiveness is and is
   not; boundaries alongside forgiveness; trust rebuilt over time.

**Module 5 — slate violet**
10. `navigating-the-family-tree-guide.png` — leaving as an emotional shift, not
    a move; inherited patterns; a secure base; when to get help.
11. `navigating-family-patterns-in-marriage.png` — mapping family closeness and
    distance; holiday and money boundaries decided together.

**Modules 6 and 7 — deep rose, navy blue**
12. Consolidate the current five (`the-spark-and-the-flame`,
    `keeping-the-spark-alive`, `five-secrets-of-sexual-intimacy`,
    `love-in-action-relationship-guide`,
    `marriage-maintenance-storyboard-field-guide`) into **two** guides — one on
    friendship, safety, and desire over a long marriage; one on love expressed
    in the currency your wife actually receives. The current five overlap
    heavily; two better ones beat five thin ones.

## Acceptance checklist

- [ ] Every word proofread at full zoom. Zero garbled text.
- [ ] Module accent used, USMC shield present, NotebookLM watermark gone.
- [ ] Safety / red-flag panel intact where the topic calls for it.
- [ ] Legible on a phone at full width and on a printed sheet.
- [ ] Alt text written for each one (the site currently carries structural
      placeholder alt text for the graphics regenerated here).

When the files land, drop them in `assets/media/tmc-husband/mNN/infographics/`
with the same filenames, run `tmc-husband/print/sync-media.sh --apply`, and
tell me — I will rewrite the alt text and the registry summaries to match.

---

## Addendum 2026-08-05 — TWO STYLES ARE MIXED ACROSS THE SET

Adam's note: *"towards the end of our modules, we lost all the color… the
Vineyard of Marriage / Field Guide to Lifelong Connection looked pretty good
and they're not too cartoony."*

Measured across all 16 infographics, then checked by eye on a contact sheet.
The problem is **not** saturation — it is that two incompatible illustration
styles shipped in the same course.

**STYLE A — illustrated field guide (the standard; keep and match).**
Painterly scenes with real people in real environments, depth, and seasonal
range. Navy panel headers, warm skin tones, a red accent for warnings.
Representative: `m01/marriage-vineyard-field-guide.png` — a vineyard through
four seasons, snow in Phase 3, sunset in Phase 4.

**STYLE B — flat corporate infographic (the regression; redo).**
Monochrome navy line-art icons on white, numbered lists, no scenes, no depth.
`m07/love-in-action-relationship-guide.png` is the clearest case: three
distinct hues in the whole poster against twelve in the Vineyard guide.

### Redo list — 7 of 16, to be brought onto Style A

| Module | File | Note |
|---|---|---|
| m02 | `art-of-effective-communication.png` | flat panels |
| m02 | `mastering-marriage-communication.png` | flat icon rows |
| m03 | `marriage-teamwork-guide.png` | text-heavy, sparse art |
| m05 | `navigating-family-patterns-in-marriage.png` | flat diagram |
| m06 | `five-secrets-of-sexual-intimacy.png` | numbered list + icons |
| m06 | `keeping-the-spark-alive.png` | numbered list + icons |
| m07 | `love-in-action-relationship-guide.png` | **worst — pure line art** |

### Keep as reference (already Style A)

`m01` both · `m03` conflict-and-teamwork + conflict-resolution ·
`m04` both · `m05` family-tree · `m06` the-spark-and-the-flame ·
`m07` marriage-maintenance-storyboard

### Correction to the "late modules" reading

The drift is not purely late. **m02 carries two Style B graphics**, and m07
still has one good Style A piece (`marriage-maintenance-storyboard`). The
trend is real — m06 is 2-of-3 flat — but any redo pass has to be driven by
this list rather than by module number.

Reproduce the measurement: mean HLS saturation plus a count of distinct
10-degree hue buckets over pixels with 0.08 < lightness < 0.94, which ignores
the white background. Style B lands at 3–6 hues; Style A at 8–20.
