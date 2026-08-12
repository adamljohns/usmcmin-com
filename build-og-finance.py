#!/usr/bin/env python3
"""build-og-finance.py — 1200×630 Open Graph cards for finance / giving / shop lanes.

Brand: C5iSR navy + gold on near-black (stewardship desk voice).
Not B&A terracotta; not ministry brain defaults.

Outputs under assets/og/og-finance*.jpg (+ upgraded og-melaleuca.jpg / og-shop.jpg)

Run from repo root:
  python3 build-og-finance.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "og"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630

# C5iSR / stewardship palette (navy + gold, desk-dark)
BG_TOP = (8, 14, 24)
BG_BOTTOM = (14, 28, 48)
NAVY = (11, 46, 79)          # #0b2e4f
NAVY_DEEP = (6, 24, 42)
GOLD = (201, 168, 76)        # #c9a84c
GOLD_SOFT = (232, 214, 160)
CREAM = (247, 245, 240)
WHITE = (245, 246, 248)
MUTED = (160, 172, 186)
SLATE = (90, 104, 120)
GREEN = (0, 112, 60)         # Melaleuca accent
GREEN_LIGHT = (0, 154, 78)

PLAYFAIR = Path("/Users/moop_bot_pro/Library/Fonts/PlayfairDisplay[wght].ttf")
GEORGIA_B = Path("/System/Library/Fonts/Supplemental/Georgia Bold.ttf")
GEORGIA = Path("/System/Library/Fonts/Supplemental/Georgia.ttf")
HELV = Path("/System/Library/Fonts/Helvetica.ttc")
LOGO = ROOT / "assets" / "img" / "logo.png"


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


def vertical_gradient(top=BG_TOP, bottom=BG_BOTTOM) -> Image.Image:
    img = Image.new("RGB", (W, H), top)
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    return img


def brand_footer(draw, left="U.S.M.C. MINISTRIES", right="C5iSR · Stewardship Desk"):
    draw.rectangle((0, H - 72, W, H), fill=NAVY_DEEP)
    draw.rectangle((0, H - 76, W, H - 72), fill=GOLD)
    f_brand = font(PLAYFAIR, 26, weight=600) if PLAYFAIR.exists() else font(GEORGIA_B, 24)
    f_small = font(HELV, 17, index=0)
    draw.text((56, H - 50), left, font=f_brand, fill=CREAM)
    rw = text_width(draw, right, f_small)
    draw.text((W - 56 - rw, H - 44), right, font=f_small, fill=GOLD_SOFT)


def maybe_logo(img: Image.Image, size=54):
    if not LOGO.exists():
        return
    try:
        logo = Image.open(LOGO).convert("RGBA")
        logo.thumbnail((size, size), Image.Resampling.LANCZOS)
        # place bottom-right above footer
        x = W - 56 - logo.width
        y = H - 72 - 18 - logo.height
        # slight dark plate behind
        plate = Image.new("RGBA", (logo.width + 16, logo.height + 16), (0, 0, 0, 90))
        img.paste(plate, (x - 8, y - 8), plate)
        img.paste(logo, (x, y), logo)
    except Exception:
        pass


def render_card(
    kicker: str,
    title: str,
    subtitle: str,
    out_name: str,
    badge: str | None = None,
    accent=GOLD,
    footer_right: str = "C5iSR · Stewardship Desk",
    footer_left: str = "U.S.M.C. MINISTRIES",
):
    base = vertical_gradient()
    # left navy rail + soft gold wash
    wash = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wpx = wash.load()
    for x in range(W):
        t = x / (W - 1)
        a = int(70 * (1 - t) ** 1.4)
        for y in range(H):
            wpx[x, y] = (*NAVY, a)
    composed = Image.alpha_composite(base.convert("RGBA"), wash)
    draw = ImageDraw.Draw(composed, "RGBA")

    # top gold hairline + left accent bar
    draw.rectangle((0, 0, W, 8), fill=(*accent, 255))
    draw.rectangle((0, 0, 12, H), fill=(*accent, 255))

    # subtle right geometric frame
    draw.rectangle((W - 96, 88, W - 56, H - 140), outline=(*accent, 70), width=2)
    draw.line((W - 116, 108, W - 76, 108), fill=(*accent, 110), width=2)

    f_kick = font(HELV, 20, index=0)
    kick = kicker.upper()
    kb = draw.textbbox((0, 0), kick, font=f_kick)
    kw, kh = kb[2] - kb[0], kb[3] - kb[1]
    px, py = 56, 64
    pad_x, pad_y = 16, 10
    draw.rounded_rectangle(
        (px, py, px + kw + pad_x * 2, py + kh + pad_y * 2),
        radius=4,
        fill=(*accent, 230),
    )
    draw.text((px + pad_x, py + pad_y - 1), kick, font=f_kick, fill=NAVY_DEEP)

    if badge:
        f_badge = font(HELV, 16, index=0)
        bb = draw.textbbox((0, 0), badge.upper(), font=f_badge)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        bx, by = W - 56 - bw - 34, 64
        draw.rounded_rectangle(
            (bx, by, bx + bw + 34, by + bh + 18),
            radius=4,
            outline=(*accent, 220),
            width=2,
            fill=(8, 14, 24, 200),
        )
        draw.text((bx + 17, by + 9), badge.upper(), font=f_badge, fill=accent)

    f_title = font(PLAYFAIR, 58, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 54)
    ty = 150
    for line in wrap(draw, title, f_title, W - 160)[:3]:
        draw.text((58, ty + 3), line, font=f_title, fill=(0, 0, 0, 100))
        draw.text((56, ty), line, font=f_title, fill=WHITE)
        ty += 70

    f_sub = font(HELV, 26, index=0)
    sy = ty + 10
    for line in wrap(draw, subtitle, f_sub, W - 180)[:3]:
        draw.text((56, sy), line, font=f_sub, fill=MUTED)
        sy += 34

    brand_footer(draw, left=footer_left, right=footer_right)
    maybe_logo(composed)

    out_path = OUT / out_name
    composed.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}")
    return out_path


def main():
    # Hub + public stewardship lanes
    render_card(
        "Biblical Stewardship",
        "Faithful with what God entrusted.",
        "Money, assets, and opportunity handled with discipline — not fear, not greed.",
        "og-finance.jpg",
        badge="Finance",
    )
    render_card(
        "Digital Assets",
        "Sound money. Sober judgment.",
        "Crypto and digital assets through a Christ-centered stewardship lens.",
        "og-finance-crypto.jpg",
        badge="Crypto",
    )
    render_card(
        "Faithful Investing",
        "Long horizon. Values aligned.",
        "Stewardship over speculation — a written plan you keep when markets get loud.",
        "og-finance-investing.jpg",
        badge="Invest",
    )
    render_card(
        "Household Stewarding",
        "Order in the home first.",
        "Budgeting, debt freedom, and generosity — faithfulness starts at the kitchen table.",
        "og-finance-stewarding.jpg",
        badge="Home",
    )
    render_card(
        "Kingdom Resourcing",
        "Work hard. Give open-handed.",
        "Multiple streams and diligent provision that advance the mission.",
        "og-finance-resourcing.jpg",
        badge="Give",
    )
    render_card(
        "C5iSR Coaching",
        "Christ-centered financial coaching.",
        "Crypto, debt freedom, and family stewardship — without the casino mindset.",
        "og-finance-coaching.jpg",
        badge="Coach",
    )
    render_card(
        "Book a Session",
        "Walk away with a real plan.",
        "Marine, minister, and operator. Free discovery call — then a clear next step.",
        "og-finance-consulting.jpg",
        badge="Book",
    )
    render_card(
        "Coaching Intake",
        "Your stewardship roadmap starts here.",
        "Biblical financial coaching intake — C5iSR LLC with Adam Johns.",
        "og-finance-intake.jpg",
        badge="Intake",
    )
    render_card(
        "Command Center",
        "Family financial command.",
        "Budgets, capital lanes, and provision tracking in one stewardship desk.",
        "og-finance-command.jpg",
        badge="Ops",
    )
    render_card(
        "C5iSR LLC",
        "You bring the problem. We bring the AI.",
        "Agent-backed operating systems for owner-operated businesses — not chatbot demos.",
        "og-finance-c5isr.jpg",
        badge="AI",
        footer_right="C5iSR LLC · Consulting",
    )
    render_card(
        "C5iSR Crypto",
        "Christ-centered crypto intelligence.",
        "Market discipline through a biblical stewardship lens — never a get-rich promise.",
        "og-finance-c5isr-crypto.jpg",
        badge="Markets",
        footer_right="C5iSR · Markets Desk",
    )

    # Shop + Melaleuca (money-adjacent public pages) — upgrade weak existing cards
    render_card(
        "Ministry Shop",
        "Wear the mission.",
        "Faith-forward gear that supports U.S.M.C. Ministries work.",
        "og-shop.jpg",
        badge="Shop",
        footer_right="U.S.M.C. Ministries · Gear",
    )
    render_card(
        "Melaleuca Wellness",
        "Better products. Better lives.",
        "Safer home and wellness choices shipped direct — no inventory pressure.",
        "og-melaleuca.jpg",
        badge="Wellness",
        accent=GREEN_LIGHT,
        footer_right="Preferred Member path",
        footer_left="U.S.M.C. MINISTRIES",
    )

    # Keep a JPEG finance default that replaces the thin PNG when linked
    render_card(
        "Stewardship Desk",
        "C5iSR financial command.",
        "Biblical stewardship tools for households who take provision seriously.",
        "og-financial.jpg",
        badge="Finance",
    )

    print("DONE")


if __name__ == "__main__":
    main()
