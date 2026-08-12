#!/usr/bin/env python3
"""build-og-bow-arrow.py — 1200×630 Open Graph cards for Bow & Arrow pages.

Brand: terracotta / cream / warm brown (Maria's B&A system).
Outputs under assets/og/og-bow-arrow*.jpg

Run from repo root:
  python3 build-og-bow-arrow.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "og"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630

CREAM = (250, 247, 242)
LINEN = (243, 236, 228)
TERRACOTTA = (196, 131, 90)
TERRACOTTA_DARK = (169, 107, 66)
BLUSH = (212, 166, 140)
WARM_BROWN = (107, 74, 58)
DARK_BROWN = (61, 43, 34)

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


def cover_crop(src: Image.Image, tw: int, th: int) -> Image.Image:
    sw, sh = src.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale + 0.5), int(sh * scale + 0.5)
    im = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = max(0, (nh - th) // 3)
    return im.crop((left, top, left + tw, top + th))


def gradient_overlay(base: Image.Image, left_alpha=225, right_alpha=70) -> Image.Image:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    px = overlay.load()
    for x in range(W):
        t = x / (W - 1)
        a = int(left_alpha * (1 - t) + right_alpha * t)
        for y in range(H):
            yb = y / (H - 1)
            aa = min(255, int(a + 40 * yb))
            r = int(DARK_BROWN[0] * 0.55 + WARM_BROWN[0] * 0.45)
            g = int(DARK_BROWN[1] * 0.55 + WARM_BROWN[1] * 0.45)
            b = int(DARK_BROWN[2] * 0.55 + WARM_BROWN[2] * 0.45)
            px[x, y] = (r, g, b, aa)
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def cream_card() -> Image.Image:
    img = Image.new("RGB", (W, H), CREAM)
    wash = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wpx = wash.load()
    for y in range(H):
        t = y / H
        a = int(28 * (1 - t))
        for x in range(W):
            wpx[x, y] = (*TERRACOTTA, a)
    img = Image.alpha_composite(img.convert("RGBA"), wash).convert("RGB")
    draw = ImageDraw.Draw(img, "RGBA")
    draw.rectangle((0, 0, 14, H), fill=TERRACOTTA)
    draw.rectangle((0, 0, W, 6), fill=TERRACOTTA)
    draw.rectangle((0, H - 70, W, H), fill=WARM_BROWN)
    return img


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


def brand_footer(draw):
    f_small = font(HELV, 18, index=0)
    f_brand = font(PLAYFAIR, 28, weight=600) if PLAYFAIR.exists() else font(GEORGIA_B, 28)
    label = "BOW & ARROW STUDIO"
    place = "Historic Fredericksburg, Virginia"
    draw.text((48, H - 52), label, font=f_brand, fill=CREAM)
    pw = text_width(draw, place, f_small)
    draw.text((W - 48 - pw, H - 46), place, font=f_small, fill=BLUSH)


def render_photo_card(photo_path: Path, kicker: str, title: str, subtitle: str, out_name: str):
    src = Image.open(photo_path).convert("RGB")
    src = ImageEnhance.Color(src).enhance(1.05)
    src = ImageEnhance.Contrast(src).enhance(1.05)
    base = cover_crop(src, W, H)
    composed = gradient_overlay(base)
    draw = ImageDraw.Draw(composed, "RGBA")

    draw.rectangle((0, 0, W, 8), fill=(*TERRACOTTA, 255))

    f_kick = font(HELV, 20, index=0)
    kick = kicker.upper()
    kb = draw.textbbox((0, 0), kick, font=f_kick)
    kw, kh = kb[2] - kb[0], kb[3] - kb[1]
    px, py = 56, 70
    pad_x, pad_y = 18, 10
    draw.rounded_rectangle(
        (px, py, px + kw + pad_x * 2, py + kh + pad_y * 2),
        radius=4,
        fill=(*TERRACOTTA, 235),
    )
    draw.text((px + pad_x, py + pad_y - 1), kick, font=f_kick, fill=CREAM)

    f_title = font(PLAYFAIR, 64, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 60)
    ty = 160
    for line in wrap(draw, title, f_title, W - 120)[:3]:
        draw.text((58, ty + 3), line, font=f_title, fill=(0, 0, 0, 90))
        draw.text((56, ty), line, font=f_title, fill=CREAM)
        ty += 74

    f_sub = font(HELV, 28, index=0)
    sy = ty + 8
    for line in wrap(draw, subtitle, f_sub, W - 140)[:2]:
        draw.text((56, sy), line, font=f_sub, fill=BLUSH)
        sy += 36

    draw.rectangle((0, H - 78, W, H), fill=(*WARM_BROWN, 235))
    f_brand = font(PLAYFAIR, 30, weight=600) if PLAYFAIR.exists() else font(GEORGIA_B, 28)
    f_small = font(HELV, 18, index=0)
    draw.text((56, H - 54), "Bow & Arrow Studio", font=f_brand, fill=CREAM)
    place = "Historic Fredericksburg, VA"
    pw = text_width(draw, place, f_small)
    draw.text((W - 56 - pw, H - 48), place, font=f_small, fill=BLUSH)
    draw.rectangle((0, H - 82, W, H - 78), fill=(*TERRACOTTA, 255))

    out_path = OUT / out_name
    composed.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}")
    return out_path


def render_ops_card(kicker: str, title: str, subtitle: str, out_name: str, badge: str | None = None):
    img = cream_card()
    draw = ImageDraw.Draw(img, "RGBA")

    f_kick = font(HELV, 20, index=0)
    kick = kicker.upper()
    draw.text((56, 70), kick, font=f_kick, fill=TERRACOTTA_DARK)
    kw = text_width(draw, kick, f_kick)
    draw.rectangle((56, 100, 56 + min(kw, 220), 104), fill=TERRACOTTA)

    f_title = font(PLAYFAIR, 58, weight=700) if PLAYFAIR.exists() else font(GEORGIA_B, 54)
    ty = 150
    for line in wrap(draw, title, f_title, W - 140)[:3]:
        draw.text((56, ty), line, font=f_title, fill=DARK_BROWN)
        ty += 70

    f_sub = font(HELV, 26, index=0)
    sy = ty + 12
    for line in wrap(draw, subtitle, f_sub, W - 160)[:3]:
        draw.text((56, sy), line, font=f_sub, fill=WARM_BROWN)
        sy += 34

    if badge:
        f_badge = font(HELV, 18, index=0)
        bb = draw.textbbox((0, 0), badge, font=f_badge)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        bx, by = W - 56 - bw - 36, 64
        draw.rounded_rectangle(
            (bx, by, bx + bw + 36, by + bh + 20),
            radius=4,
            outline=TERRACOTTA,
            width=2,
            fill=(*LINEN, 255),
        )
        draw.text((bx + 18, by + 10), badge, font=f_badge, fill=TERRACOTTA_DARK)

    draw.rectangle((W - 90, H - 160, W - 56, H - 90), outline=BLUSH, width=2)
    brand_footer(draw)

    out_path = OUT / out_name
    img.convert("RGB").save(out_path, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"wrote {out_path}")
    return out_path


def main():
    props = ROOT / "assets" / "img" / "properties"

    render_photo_card(
        props / "hanover-combined.jpg",
        "Photography & Hospitality",
        "Bow & Arrow Studios",
        "Boutique photography + family-run stays in historic Fredericksburg.",
        "og-bow-arrow.jpg",
    )
    render_photo_card(
        props / "apt-7.jpg",
        "Book Direct · Save 15–20%",
        "Stay Downtown. Book Direct.",
        "Skip platform fees. Historic-district apartments, personal host care.",
        "og-bow-arrow-direct.jpg",
    )
    render_photo_card(
        props / "apt-6.jpg",
        "House Rules",
        "A warm stay starts with clear house rules.",
        "Read and acknowledge before check-in — same standards for every stay.",
        "og-bow-arrow-house-rules.jpg",
    )
    render_photo_card(
        props / "apt-8.jpg",
        "Guest Guide",
        "Everything you need for your stay.",
        "Check-in, parking, Wi‑Fi, and local notes — ready when you arrive.",
        "og-bow-arrow-guests.jpg",
    )
    render_photo_card(
        props / "apt-7.jpg",
        "Book Your Stay",
        "Reserve direct with Bow & Arrow.",
        "Five-star rated apartments in the heart of Fredericksburg, VA.",
        "og-bow-arrow-booking.jpg",
    )

    ops = [
        ("Operations", "Dashboard", "Property command center for Bow & Arrow Studio.", "og-bow-arrow-dashboard.jpg", "OPS"),
        ("Operations", "Financials", "Revenue, expenses, and property performance snapshot.", "og-bow-arrow-financials.jpg", "FINANCE"),
        ("Operations", "Booking Calendar", "Reservation calendar across downtown apartments.", "og-bow-arrow-calendar.jpg", "OPS"),
        ("Operations", "Cleaning Management", "Turnover schedule and cleaner coordination.", "og-bow-arrow-cleaning.jpg", "OPS"),
        ("Operations", "Guest Communications", "Message log and host communication history.", "og-bow-arrow-comms.jpg", "OPS"),
        ("Operations", "Maintenance Tracker", "Open work orders and property upkeep status.", "og-bow-arrow-maintenance.jpg", "OPS"),
        ("Operations", "Staff Portal", "Sign in to the Bow & Arrow operations desk.", "og-bow-arrow-login.jpg", "STAFF"),
    ]
    for kick, title, sub, name, badge in ops:
        render_ops_card(kick, title, sub, name, badge=badge)

    print("DONE")


if __name__ == "__main__":
    main()
