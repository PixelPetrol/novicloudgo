# NoviCloud GO — strona produktowa (GitHub Pages)

Ten folder jest wystawiany jako **osobne, publiczne** repozytorium, dzięki czemu
strona i instrukcja mają publiczny adres, a repozytorium kodu zostaje prywatne.
Ten sam wzorzec co `privacy-site/` (polityka prywatności).

Adres: **https://pixelpetrol.github.io/novicloudgo/**
· instrukcja: `…/novicloudgo/instrukcja/`

> **Strona TYMCZASOWA** — hostowana na koncie osobistym autora, do prezentacji
> aplikacji. Docelowo treść trafi na domenę firmową Novitusa; wtedy warto
> zostawić tu przekierowanie (link może już krążyć w mailach).

## Zawartość

| Ścieżka | Co to |
|---|---|
| `index.html` | strona produktowa (funkcje, prywatność, jak zacząć) — jeden samodzielny plik |
| `img/` | zrzuty użyte na stronie + logo i monogram (SVG) |
| `instrukcja/` | KOPIA instrukcji obsługi z `docs/instrukcja/` (index.html + `zrzuty/`) |

## Aktualizacja po zmianach w aplikacji

1. Odśwież instrukcję w repo kodu (`docs/instrukcja/` — patrz README tam).
2. Skopiuj ją tutaj i podmień zrzuty użyte na stronie głównej:
   ```bash
   cd ..                      # katalog novilink/
   cp docs/instrukcja/index.html site/instrukcja/
   cp docs/instrukcja/zrzuty/*.webp site/instrukcja/zrzuty/
   for f in 07-pulpit 12-raport-dnia 15-raport-kasjerski 20-skaner 21-doradca-ai \
            58-tablet-pulpit-pionowo; do
     cp docs/instrukcja/zrzuty/$f.webp site/img/
   done
   # UWAGA: kopiujemy TYLKO .webp — źródłowe PNG (~11 MB) nie wchodzą
   # do publicznego repo strony (strona odwołuje się wyłącznie do .webp).
   ```
3. W `site/`: `git add -A && git commit -m "…" && git push` — GitHub Pages
   przebuduje stronę w ciągu ~1 minuty.

## Uwagi

- Wszystkie zrzuty pochodzą z konta demonstracyjnego `wtest`, więc nadają się
  do publikacji (kwoty i nazwy towarów są przykładowe).
- Strona nie używa zewnętrznych czcionek ani skryptów — działa offline
  i nie ustawia żadnych ciasteczek, więc nie wymaga banera zgód.
- Polityka prywatności ZOSTAJE pod starym adresem
  (`pixelpetrol.github.io/novilink-privacy/`), bo ten URL jest zaszyty
  w wydanych wersjach aplikacji — nie przenosimy go bez przekierowania.
