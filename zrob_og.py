#!/usr/bin/env python3
"""Obrazek do udostępniania (Open Graph / Twitter) — img/og.png 1200×630.

Po co: bez `og:image` link do strony wklejony w mailu, na Messengerze czy
Slacku pokazuje się jako szara ramka bez podglądu, a to jedyny kanał
dystrybucji tej strony.

Kompozycja powtarza hero: granat marki, delikatna siatka, błękitna poświata
i monogram produktu. Krój: Avenir Next (geometryczny, najbliższy Sorze
z fontów systemowych — Sora jest tylko w woff2, którego PIL nie czyta).

    python3 zrob_og.py
"""
import pathlib

from PIL import Image, ImageDraw, ImageFont

BASE = pathlib.Path(__file__).resolve().parent
MONOGRAM = BASE.parent / "app/assets/icon/logo_monogram_t.png"
WYNIK = BASE / "img/og.png"

W, H = 1200, 630
GRANAT = (11, 19, 32)
NIEBIESKI = (35, 124, 253)
POMARANCZ = (240, 140, 0)
BIALY = (255, 255, 255)
STONOWANY = (176, 198, 219)

KROJ = "/System/Library/Fonts/Avenir Next.ttc"
tytul = ImageFont.truetype(KROJ, 78, index=0)      # Bold
podtytul = ImageFont.truetype(KROJ, 34, index=5)   # Medium
nadtytul = ImageFont.truetype(KROJ, 22, index=2)   # Demi Bold


def poswiata(im, cx, cy, r, kolor, moc):
    """Radialny gradient jak `radial-gradient` w hero — rysowany pierścieniami,
    bo PIL nie ma gradientów."""
    warstwa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(warstwa)
    krokow = 90
    for i in range(krokow, 0, -1):
        pr = r * i / krokow
        a = int(moc * (1 - i / krokow) ** 2)
        d.ellipse((cx - pr, cy - pr, cx + pr, cy + pr), fill=(*kolor, a))
    return Image.alpha_composite(im.convert("RGBA"), warstwa)


im = Image.new("RGB", (W, H), GRANAT)
d = ImageDraw.Draw(im)
# siatka 64 px, jak `.hero::before`
for x in range(0, W, 64):
    d.line([(x, 0), (x, H)], fill=(20, 30, 46))
for y in range(0, H, 64):
    d.line([(0, y), (W, y)], fill=(20, 30, 46))
im = poswiata(im, 1120, -40, 620, NIEBIESKI, 150).convert("RGB")
d = ImageDraw.Draw(im)

mono = Image.open(MONOGRAM).convert("RGBA")
mono = mono.resize((190, 190), Image.LANCZOS)
im.paste(mono, (84, 96), mono)

d.text((84, 320), "APLIKACJA MOBILNA DO NOVICLOUD", font=nadtytul,
       fill=(120, 180, 235))
d.text((84, 356), "NoviCloud GO", font=tytul, fill=BIALY)
d.text((84, 456), "Twój NoviCloud w kieszeni —", font=podtytul, fill=STONOWANY)
d.text((84, 498), "sprzedaż, raporty i towary na telefonie.", font=podtytul,
       fill=STONOWANY)
d.rectangle((84, 566, 164, 572), fill=POMARANCZ)

WYNIK.parent.mkdir(exist_ok=True)
im.save(WYNIK, optimize=True)
print(f"{WYNIK}  {im.size}  {WYNIK.stat().st_size // 1024} KB")

# Ikona dla „dodaj do ekranu początkowego” na iOS — Safari nie używa SVG
# z `rel=icon`, więc bez tego skrót dostaje zrzut strony zamiast logo.
IKONA = BASE / "img/ikona-180.png"
ik = Image.new("RGB", (180, 180), GRANAT)
znak = Image.open(MONOGRAM).convert("RGBA").resize((132, 132), Image.LANCZOS)
ik.paste(znak, (24, 26), znak)
ik.save(IKONA, optimize=True)
print(f"{IKONA}  {ik.size}  {IKONA.stat().st_size // 1024} KB")
