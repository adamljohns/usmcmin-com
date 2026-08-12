#!/usr/bin/env python3
"""build-og-citizen.py — 1200×630 Open Graph cards for RESOLUTE Citizen.

Gold bar: match Bow & Arrow polish (branded share cards, not ministry defaults,
not raw photo dumps). RESOLUTE silver / gold civic palette + Playfair titles.

Outputs under assets/og/og-citizen*.jpg

Run from repo root:
  python3 build-og-citizen.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "og"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630

# RESOLUTE silver-tier palette (site brand) elevated to B&A card structure
BG_TOP = (8, 10, 14)
BG_BOTTOM = (22, 28, 38)
PANEL = (16, 20, 28)
SILVER = (200, 207, 217)
SILVER_DIM = (138, 148, 162)
SILVER_BRIGHT = (230, 234, 240)
GOLD = (201, 168, 76)
GOLD_DIM = (168, 138, 58)
WHITE = (245, 246, 248)
MUTED = (120, 130, 142)
NAVY_LINE = (48, 58, 74)
GOD_PILL_BG = (36, 42, 54)
AMERICA_PILL_BG = (48, 40, 24)
STATE_PILL_BG = (28, 44, 40)
LOCAL_PILL_BG = (34, 40, 52)

PLAYFAIR = Path("/Users/moop_bot_pro/Library/Fonts/PlayfairDisplay[wght].ttf")
GEORGIA_B = Path("/System/Library/Fonts/Supplemental/Georgia Bold.ttf")
GEORGIA = Path("/System/Library/Fonts/Supplemental/Georgia.ttf")
HELV = Path("/System/Library/Fonts/Helvetica.ttc")


def font(path: Path, size: int, weight: int | None = None, index: int = 0):
    try:
        if path.suffix == ".ttf" and "[" in path.name:
            f = ImageFont.truetype(str(path), size)
            if weight is not None:
                try:
                    f.set_variation_by_axes([weight])
                except Exception:
                    pass
            return f
        return ImageFont.truetype(str(path), size, index=index)
    except Exception:
        return ImageFont.load_default()


def text_width(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0]


def text_height(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[3] - b[1]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_width(draw, trial, fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def vertical_gradient() -> Image.Image:
    img = Image.new("RGB", (W, H), BG_TOP)
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        for x in range(W):
            # subtle left vignette for depth
            edge = min(1.0, x / 90.0)
            shade = 0.92 + 0.08 * edge
            px[x, y] = tuple(min(255, int(c[i] * shade)) for i in range(3))
    return img


def brand_chrome(draw: ImageDraw.ImageDraw, accent=SILVER):
    # Top accent bar + left spine (B&A structure, RESOLUTE colors)
    draw.rectangle((0, 0, W, 8), fill=accent)
    draw.rectangle((0, 0, 12, H), fill=accent)
    # Bottom brand bar
    draw.rectangle((0, H - 78, W, H), fill=(14, 16, 22))
    draw.rectangle((0, H - 82, W, H - 78), fill=accent)
    f_brand = font(PLAYFAIR, 30, weight=600) if PLAYFAIR.exists() else font(GEORGIA_B, 28)
    f_small = font(HELV, 18, index=0)
    draw.text((48, H - 54), "RESOLUTE Citizen", font=f_brand, fill=SILVER_BRIGHT)
    right = "USMCMIN.COM  ·  Christian voter scorecard"
    rw = text_width(draw, right, f_small)
    draw.text((W - 48 - rw, H - 48), right, font=f_small, fill=SILVER_DIM)


def pill(draw, x, y, text, fill_bg, outline, fill_text):
    f_kick = font(HELV, 18, index=1)
    kick = text.upper()
    kb = draw.textbbox((0, 0), kick, font=f_kick)
    kw, kh = kb[2] - kb[0], kb[3] - kb[1]
    pad_x, pad_y = 18, 10
    draw.rounded_rectangle(
        (x, y, x + kw + pad_x * 2, y + kh + pad_y * 2),
        radius=4,
        fill=(*fill_bg, 235),
        outline=outline,
        width=2,
    )
    draw.text((x + pad_x, y + pad_y - 1), kick, font=f_kick, fill=fill_text)
    return y + kh + pad_y * 2


def render_hub_card(
    kicker: str,
    title: str,
    subtitle: str,
    out_name: str,
    *,
    badge: str | None = None,
    accent=SILVER,
    kicker_bg=GOD_PILL_BG,
):
    img = vertical_gradient()
    draw = ImageDraw.Draw(img, "RGBA")
    brand_chrome(draw, accent=accent)

    # Soft panel behind title block
    draw.rounded_rectangle((36, 48, W - 36, H - 110), radius=10, fill=(*PANEL, 110))

    bottom = pill(draw, 56, 72, kicker, kicker_bg, accent, accent)

    if badge:
        f_badge = font(HELV, 16, index=1)
        bb = draw.textbbox((0, 0), badge.upper(), font=f_badge)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        bx, by = W - 56 - bw - 36, 72
        draw.rounded_rectangle(
            (bx, by, bx + bw + 36, by + bh + 18),
            radius=4,
            outline=GOLD,
            width=2,
            fill=(*AMERICA_PILL_BG, 230),
        )
        draw.text((bx + 18, by + 9), badge.upper(), font=f_badge, fill=GOLD)

    f_title = font(PLAYFAIR, 58, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 54)
    ty = max(bottom + 28, 150)
    for line in wrap(draw, title, f_title, W - 140)[:3]:
        # soft shadow
        draw.text((58, ty + 3), line, font=f_title, fill=(0, 0, 0, 110))
        draw.text((56, ty), line, font=f_title, fill=WHITE)
        ty += 68

    f_sub = font(HELV, 26, index=0)
    sy = ty + 10
    for line in wrap(draw, subtitle, f_sub, W - 160)[:3]:
        draw.text((56, sy), line, font=f_sub, fill=SILVER_DIM)
        sy += 34

    # thin rule under copy
    draw.rectangle((56, min(sy + 8, H - 120), 56 + 120, min(sy + 12, H - 116)), fill=accent)

    out_path = OUT / out_name
    img.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}  ({out_path.stat().st_size/1024:.0f} KB)")
    return out_path


def render_category_card(
    num: int,
    label: str,
    tagline: str,
    tier: str,
    out_name: str,
):
    if tier == "god_first":
        accent = SILVER
        pill_bg = GOD_PILL_BG
        tier_label = "✝  GOD FIRST"
    elif tier == "america_first":
        accent = GOLD
        pill_bg = AMERICA_PILL_BG
        tier_label = "★  AMERICA FIRST"
    elif tier == "state_first":
        accent = (120, 188, 160)
        pill_bg = STATE_PILL_BG
        tier_label = "⬡  STATE FIRST"
    else:  # local_first
        accent = (150, 170, 210)
        pill_bg = LOCAL_PILL_BG
        tier_label = "⌂  LOCAL FIRST"

    img = vertical_gradient()
    draw = ImageDraw.Draw(img, "RGBA")
    brand_chrome(draw, accent=accent)
    draw.rounded_rectangle((36, 48, W - 36, H - 110), radius=10, fill=(*PANEL, 120))

    pill(draw, 56, 72, tier_label, pill_bg, accent, accent)

    # Ghost category number (B&A-style depth, not plain Helvetica dump)
    f_num = font(PLAYFAIR, 200, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 180)
    num_text = str(num)
    nw = text_width(draw, num_text, f_num)
    draw.text((W - nw - 70, 40), num_text, font=f_num, fill=(*accent, 38))

    f_title = font(PLAYFAIR, 56, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 52)
    ty = 180
    for line in wrap(draw, label, f_title, W - 160)[:3]:
        draw.text((58, ty + 3), line, font=f_title, fill=(0, 0, 0, 110))
        draw.text((56, ty), line, font=f_title, fill=WHITE)
        ty += 66

    f_sub = font(HELV, 26, index=0)
    sy = ty + 8
    for line in wrap(draw, tagline, f_sub, W - 180)[:2]:
        draw.text((56, sy), line, font=f_sub, fill=SILVER_DIM)
        sy += 34

    f_meta = font(HELV, 18, index=0)
    draw.text((56, H - 118), "Category deep-dive  ·  scored questions + bills tracked", font=f_meta, fill=MUTED)

    out_path = OUT / out_name
    img.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}  ({out_path.stat().st_size/1024:.0f} KB)")
    return out_path


# Category set — Rush final share-copy 2026-08-12 (RSA-0812-OG1)
CATEGORIES = [('sanctity-of-life', 'Sanctity of Life', 'Personhood from conception. No carve-outs.', 'god_first', 1),
 ('biblical-marriage', 'Biblical Marriage', 'One man, one woman, for life — no redefinition of sex.', 'god_first', 2),
 ('family-child-sovereignty',
  'Family & Child Sovereignty',
  'Parents over the state. Predators off the platform.',
  'god_first',
  3),
 ('christian-liberty', 'Christian Liberty', 'Freedom to profess Christ — and freedom to disagree.', 'god_first', 4),
 ('economic-stewardship', 'Economic Stewardship', 'Sound money. No CBDC. No debt-slavery.', 'god_first', 5),
 ('election-integrity', 'Election Integrity', 'Paper. Hand-counted. Single-day. Citizen-only.', 'god_first', 6),
 ('border-immigration', 'Border & Immigration', 'No border enforcement, no nation.', 'america_first', 7),
 ('self-defense-2a', 'Self-Defense & 2A', 'God-given right to protect household and neighbor.', 'america_first', 8),
 ('foreign-policy-restraint',
  'Foreign Policy Restraint',
  'Article I war powers. No forever wars. No foreign-lobby owners.',
  'america_first',
  9),
 ('industry-capture', 'Industry Capture', 'Anti-Pharma. Anti-Big-Ag. Anti-MIC. Anti-cartel.', 'america_first', 10),
 ('public-justice',
  'Public Justice & Law/Order',
  'Magistrate bears the sword — punish evil, protect the innocent.',
  'god_first',
  11),
 ('refuse-federal-overreach',
  'Refuse Federal Overreach',
  '10th Amendment. Nullify unlawful federal mandates.',
  'state_first',
  12),
 ('refuse-state-overreach',
  'Refuse State Overreach',
  'Subsidiarity — local control beats unlawful state mandates.',
  'local_first',
  13)]

# Hub / tool / civic pages — Rush final titles/kickers 2026-08-12
HUB_CARDS = [('og-citizen.jpg',
  'RESOLUTE Citizen',
  "Know who you're voting for.",
  '8,900+ officials. Cited scores. Tap-to-call.',
  '100-PT',
  'silver'),
 ('og-citizen-hub.jpg',
  'Christian Voter Scorecard',
  'Vote with a clear record.',
  '10 categories. Cited sources. Contact on every card.',
  'HUB',
  'silver'),
 ('og-citizen-how-to-use.jpg',
  '5-Minute Tour',
  'How to use RESOLUTE Citizen.',
  'Look up officials, find your reps, watch council.',
  'GUIDE',
  'silver'),
 ('og-citizen-scoring-system.jpg',
  'Methodology · v5.0',
  'How the scorecard actually works.',
  'Federal 60/40. State & local 70/30 God First. Cited rubric.',
  'RUBRIC',
  'gold'),
 ('og-citizen-find-my-reps.jpg',
  'Your Ballot Starts Here',
  'Find every official over you.',
  'ZIP, city, or county → photos, scores, call links.',
  'LOOKUP',
  'silver'),
 ('og-citizen-rankings.jpg',
  'Live A–F Grades',
  "Who scores — and who doesn't.",
  'Filter 8,900+ officeholders by office, party, tier.',
  'LIST',
  'gold'),
 ('og-citizen-formers.jpg',
  'Archive · Still Scored',
  'Left office. Lost. Still on record.',
  'Grades stay live if they run again.',
  'ARCHIVE',
  'silver'),
 ('og-citizen-issues.jpg',
  'Before You Vote',
  "What's actually on the ballot.",
  'Measures, amendments, races — plain English + sources.',
  '2026',
  'gold'),
 ('og-citizen-table.jpg',
  'Table View',
  'Score the field at a glance.',
  'Sortable rows — scores, photos, contact. Primary sources.',
  'DATA',
  'silver'),
 ('og-citizen-compare.jpg',
  'Side-by-Side',
  'Compare candidates in the same race.',
  'Same scorecard. Cited profiles. No vibes.',
  'VS',
  'silver'),
 ('og-citizen-map.jpg',
  'VA · FL · TX',
  'Maps that show coverage, not slogans.',
  'Counties, cities, House districts — candidate overlays.',
  'MAP',
  'silver'),
 ('og-citizen-state.jpg',
  'State Desk',
  'State officials, scored.',
  'Governors, AGs, legislators, statewide races.',
  'STATE',
  'gold'),
 ('og-citizen-races.jpg',
  '2026 Races',
  'Key races on the scorecard.',
  'Senate, House, governor — RESOLUTE grades in the mix.',
  '2026',
  'gold'),
 ('og-citizen-methodology-foreign-influence.jpg',
  'Methodology',
  'Foreign-lobby money is not neutral.',
  'How foreign influence adjusts the score — method only.',
  'NOTE',
  'gold'),
 ('og-citizen-petition.jpg',
  'Petition',
  'Send a clear message upstream.',
  'Primary-source framing. Deliver with a spine.',
  'ACTION',
  'silver'),
 ('og-citizen-fredericksburg.jpg',
  'Fredericksburg, VA',
  'Know your council. Watch the meeting.',
  'Local votes hit families first — agendas, rules, scores.',
  'WARD 4',
  'local'),
 ('og-citizen-council-notes.jpg',
  'Council Notes',
  'What council actually did.',
  'What moved — and what still needs a citizen voice.',
  'LOCAL',
  'local')]


def accent_for(key: str):
    if key == "gold":
        return GOLD, AMERICA_PILL_BG
    if key == "local":
        return (150, 170, 210), LOCAL_PILL_BG
    return SILVER, GOD_PILL_BG


def main():
    print("=== RESOLUTE Citizen OG cards (B&A quality bar) ===")
    for out_name, kicker, title, subtitle, badge, akey in HUB_CARDS:
        accent, kbg = accent_for(akey)
        render_hub_card(
            kicker,
            title,
            subtitle,
            out_name,
            badge=badge,
            accent=accent,
            kicker_bg=kbg,
        )

    print("=== Category deep-dives ===")
    for slug, label, tagline, tier, num in CATEGORIES:
        render_category_card(num, label, tagline, tier, f"og-citizen-{slug}.jpg")

    print("DONE")


if __name__ == "__main__":
    main()
