---
titre: "sergree/whatbpm — README + extrait de latest.json : BPM, fondamentale et tonalité les plus fréquents par genre Beatport (Top 100 : Tech House, Bass House, Mainstage, House, Progressive, Deep House…)"
source: https://raw.githubusercontent.com/sergree/whatbpm/main/README.md (+ https://raw.githubusercontent.com/sergree/whatbpm/gh-pages/latest.json)
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: théorie spécifique (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Dépôt du site WhatBPM (Beatport Top 100 analysé quotidiennement, > 3000 titres) [DOC]. Le README est copié intégralement ; l'annexe est un extrait tabulé du fichier de données `latest.json` (branche gh-pages) calculé localement.

# README.md (texte intégral)

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://pip.me/sergree)

# ![WhatBPM Logo](https://raw.githubusercontent.com/sergree/whatbpm/main/images/whatbpm_logo.png)

[![crates.io](https://img.shields.io/crates/v/whatbpm)](https://crates.io/crates/whatbpm)
[![License](https://img.shields.io/crates/l/whatbpm)](https://crates.io/crates/whatbpm)
[![Mentioned in Awesome Rust](https://awesome.re/mentioned-badge.svg)](https://github.com/rust-unofficial/awesome-rust)
[![CI](https://github.com/sergree/whatbpm/actions/workflows/website_build_deploy.yml/badge.svg)](https://github.com/sergree/whatbpm/actions)

## 💓 Today's Trending Values for EDM Production 

This is the repository for the [WhatBPM] website.

[WhatBPM] is a daily updated information resource for [EDM] producers, answering questions such as
what [BPM] / [root note] / [key] / [track length] to use for a new production, what [labels][label] to look at, what [EDM] genres are the most trending, and so on.

Watch [the video][Video]:

[![WhatBPM Promo Video](https://raw.githubusercontent.com/sergree/whatbpm/main/images/yt_thumbnail.png)][Video]

- 🦀 Made with [Rust]
- 🧑‍🍳 Backed by [GitHub Actions]
- 🍽️ Served by [GitHub Pages]

# About

Please follow the [FAQ] section. There is an in-depth description of the project and its features.

If you would like to learn **how WhatBPM was made**, please read [this Habr article](https://habr.com/ru/post/714538/).

## Press

We are mentioned in the press.

- [**KVR**: *Sergree releases WhatBPM - Free Information Tool for EDM Producers*](https://www.kvraudio.com/news/sergree-releases-whatbpm---free-information-tool-for-edm-producers-56575)
- [**SAMESOUND**: *Российский программист запустил сервис WhatBPM - с ним можно изучить текущие тренды в жанре EDM*](https://samesound.ru/soft/168555-rossijskij-programmist-zapustil-servis-whatbpm-s-nim-mozhno-uznat-temp-kompozicii-i-izuchit-tekushhie-trendy-v-zhanre-edm)

Thanks, guys!

## For Developers

You can freely use [WhatBPM] data in your applications. We also provide historical data. Follow the [For Developers] section for details.

# Backers

Our project is supported by these wonderful people.

- [**nanobii**: *Found this on /r/edmproduction and it's a pretty neat resource*](https://twitter.com/nanobii/status/1596434980540153856)
- [**SLAVA BASYUL**: *Hi) Respect for WhatBPM and Matchering!👍🏻*](https://www.youtube.com/channel/UCsbS60o4lEjXcicQiMi912A)

Thank you!

## A Coffee

If our website saved your time or money, you may:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://pip.me/sergree)

**Thank you!**

## JetBrains

**WhatBPM** was made using [WebStorm] by [JetBrains].

![WebStorm](https://resources.jetbrains.com/storage/products/company/brand/logos/WebStorm.png)

Thank you for the [Open Source Development License]!

[WhatBPM]: https://sergree.github.io/whatbpm/
[EDM]: https://en.wikipedia.org/wiki/Electronic_dance_music
[BPM]: https://en.wikipedia.org/wiki/Tempo
[root note]: https://en.wikipedia.org/wiki/Tonic_(music)
[key]: https://en.wikipedia.org/wiki/Key_(music)
[track length]: https://en.wikipedia.org/wiki/Duration_(music)
[label]: https://en.wikipedia.org/wiki/Record_label
[Video]: https://www.youtube.com/watch?v=dc8o9dlAjnA "WhatBPM - Best BPM / Key / Root Note for Your EDM Production"
[Rust]: https://www.rust-lang.org/
[GitHub Actions]: https://github.com/features/actions
[GitHub Pages]: https://pages.github.com/
[FAQ]: https://github.com/sergree/whatbpm/wiki/FAQ
[For Developers]: https://github.com/sergree/whatbpm/wiki/For-Developers
[WebStorm]: https://www.jetbrains.com/webstorm/
[JetBrains]: https://www.jetbrains.com/
[Open Source Development License]:  https://jb.gg/OpenSourceSupport


# Annexe (calcul local, mode synthese) : extrait de `latest.json` (branche gh-pages, données du 2023-07-11, Beatport Top 100 par genre, valeurs « standard » pondérées par la position dans le chart)

Lecture : `n` = nombre de titres du Top 100 portant la valeur ; les trois à cinq valeurs les plus fréquentes sont listées. « root » = fondamentale (tonique) toutes modalités confondues ; « key » = tonalité avec mode. Beatport annote les tonalités automatiquement (voir GiantSteps : ~30 % d'accord avec l'annotation manuelle), donc les fréquences de tonalités sont indicatives.

| Genre Beatport | Durée moy. (s) | BPM (n) | Fondamentales (n) | Tonalités (n) |
|---|---|---|---|---|
| Tous genres (Top 100 global) | 342 | 128 (16) · 126 (15) · 127 (13) · 124 (12) · 125 (8) | D# / Eb (12) · F (12) · E (11) · A# / Bb (10) · G# / Ab (10) | A min (9) · E min (7) · Bb min (7) · F min (7) · Eb maj (6) · Eb min (6) |
| 140 / Deep Dubstep / Grime | 242 | 140 (54) · 105 (7) · 138 (4) · 142 (3) · 150 (2) | D (18) · A (12) · F (10) · G (10) · E (10) | A min (10) · D maj (10) · D min (8) · E maj (7) · F# min (6) · G min (6) |
| Afro House | 381 | 122 (23) · 120 (21) · 123 (18) · 124 (14) · 121 (10) | G (15) · F (13) · A (12) · E (12) · C# / Db (10) | G min (12) · A min (9) · C# min (7) · F min (7) · Bb min (7) · C min (6) |
| Amapiano | 366 | 113 (42) · 112 (41) · 116 (4) · 111 (4) · 114 (3) | A (17) · E (13) · G# / Ab (9) · A# / Bb (9) · G (8) | A min (12) · E maj (7) · E min (6) · Bb min (6) · F# min (5) · A maj (5) |
| Bass / Club | 279 | 130 (11) · 140 (9) · 134 (7) · 160 (6) · 155 (4) | A (13) · C# / Db (11) · D (10) · F (10) · E (10) | A min (9) · C# min (9) · E min (8) · F# min (7) · D min (7) · C min (7) |
| Bass House | 248 | 126 (29) · 128 (27) · 125 (17) · 127 (13) · 130 (6) | E (14) · F# / Gb (13) · F (12) · D# / Eb (11) · G# / Ab (9) | E min (8) · F maj (7) · Eb min (7) · F# min (7) · F# maj (6) · E maj (6) |
| Breaks / Breakbeat / UK Bass | 277 | 130 (17) · 132 (16) · 128 (12) · 134 (12) · 136 (7) | F (17) · C (11) · E (11) · F# / Gb (9) · D (8) | F min (11) · G min (7) · E min (7) · C maj (6) · F maj (6) · F# min (6) |
| Dance / Electro Pop | 285 | 128 (18) · 126 (18) · 130 (9) · 125 (9) · 124 (6) | C (19) · A (12) · D (10) · F# / Gb (9) · F (9) | C min (12) · A min (10) · D min (9) · C maj (7) · G min (6) · C# min (5) |
| Deep House | 393 | 126 (17) · 124 (15) · 122 (13) · 125 (11) · 128 (11) | F (15) · G# / Ab (12) · A# / Bb (11) · F# / Gb (10) · G (9) | F min (13) · G# min (9) · Bb min (8) · F# min (7) · E min (6) · G min (6) |
| Drum & Bass | 231 | 174 (58) · 176 (16) · 172 (8) · 131 (5) · 103 (3) | F (25) · D (12) · D# / Eb (12) · E (11) · C (9) | F min (15) · F maj (10) · Eb min (10) · D min (9) · C min (9) · E min (6) |
| Dubstep | 208 | 150 (17) · 145 (17) · 140 (16) · 144 (8) · 146 (6) | D# / Eb (25) · D (21) · E (12) · G (7) · C# / Db (7) | Eb maj (13) · D maj (12) · Eb min (12) · E min (11) · D min (9) · G min (6) |
| Electro (Classic / Detroit / Modern) | 318 | 130 (16) · 134 (10) · 132 (10) · 125 (7) · 126 (5) | F (18) · G (16) · D (11) · D# / Eb (8) · B (8) | F min (10) · G maj (9) · Eb min (8) · B min (8) · F maj (8) · D min (8) |
| Electronica | 331 | 128 (9) · 126 (8) · 122 (8) · 120 (7) · 130 (6) | G (15) · C (13) · E (12) · D (10) · A# / Bb (9) | C min (9) · G min (8) · D min (8) · F min (7) · G maj (7) · E maj (7) |
| Funky House | 306 | 126 (26) · 125 (18) · 124 (17) · 128 (14) · 123 (12) | G (12) · A (12) · F# / Gb (10) · E (9) · C (9) | C min (8) · A min (8) · G min (7) · F# min (5) · E maj (5) · G# min (5) |
| Hard Dance / Hardcore | 265 | 160 (29) · 155 (16) · 150 (13) · 138 (5) · 161 (4) | F# / Gb (15) · G (13) · G# / Ab (12) · F (11) · C# / Db (8) | F# min (9) · G# min (7) · G min (7) · F# maj (6) · G maj (6) · F min (6) |
| Hard Techno | 341 | 150 (28) · 155 (17) · 152 (12) · 154 (7) · 153 (7) | A (18) · G (13) · E (10) · A# / Bb (8) · F (8) | A min (13) · G maj (9) · Bb min (7) · E min (7) · F maj (6) · C maj (5) |
| House | 362 | 127 (20) · 125 (15) · 124 (14) · 128 (13) · 126 (13) | D (17) · D# / Eb (11) · C (11) · A (10) · C# / Db (10) | D min (10) · C min (10) · A min (8) · Eb min (8) · C# min (8) · D maj (7) |
| Indie Dance | 380 | 122 (22) · 124 (19) · 125 (16) · 120 (11) · 128 (10) | F (15) · A (15) · C (14) · G (12) · D (12) | F maj (9) · G maj (9) · A maj (9) · C min (7) · C maj (7) · D maj (7) |
| Jackin House | 361 | 124 (20) · 126 (20) · 125 (18) · 128 (13) · 127 (11) | G (15) · A (15) · F (12) · C (11) · E (10) | A min (13) · G min (12) · E min (9) · D min (8) · C min (8) · F min (8) |
| Mainstage | 272 | 128 (21) · 130 (15) · 126 (12) · 135 (8) · 140 (6) | A (13) · E (12) · D# / Eb (12) · F# / Gb (12) · F (10) | A min (10) · E min (8) · F# maj (7) · F min (7) · Eb min (6) · G maj (6) |
| Melodic House & Techno | 399 | 124 (29) · 125 (15) · 122 (13) · 126 (10) · 123 (8) | A (13) · E (12) · C (12) · D (12) · F (11) | E maj (8) · D maj (8) · C maj (7) · A min (7) · A maj (6) · F min (6) |
| Minimal / Deep Tech | 379 | 128 (33) · 129 (22) · 130 (18) · 131 (8) · 127 (7) | G (17) · A (13) · E (10) · D (10) · D# / Eb (9) | G min (13) · A min (9) · E min (7) · D min (7) · F# min (7) · C min (5) |
| Nu Disco / Disco | 345 | 124 (20) · 122 (20) · 123 (16) · 120 (10) · 125 (7) | A (17) · D (13) · G (13) · C (12) · F (11) | A min (13) · D min (11) · G min (11) · C min (9) · F maj (6) · F min (5) |
| Organic House / Downtempo | 437 | 122 (37) · 120 (21) · 121 (11) · 123 (9) · 124 (8) | C (18) · D (14) · A (13) · F (13) · G (11) | C maj (10) · A min (9) · D min (9) · C min (8) · F maj (7) · G min (6) |
| Progressive House | 423 | 124 (30) · 122 (20) · 125 (12) · 121 (10) · 123 (10) | E (15) · C (12) · A (12) · D (10) · G (9) | E min (10) · F min (7) · C min (7) · G maj (7) · A maj (7) · B min (6) |
| Psy-Trance | 448 | 140 (10) · 144 (10) · 138 (9) · 145 (8) · 146 (7) | G# / Ab (17) · D# / Eb (15) · G (12) · F (11) · E (11) | Ab maj (14) · Eb maj (11) · A maj (9) · G maj (9) · E maj (8) · F# maj (7) |
| Tech House | 330 | 128 (40) · 126 (19) · 125 (11) · 127 (11) · 129 (7) | G (16) · D# / Eb (13) · F (13) · E (12) · G# / Ab (8) | G maj (10) · F min (9) · Eb min (9) · E min (7) · G min (6) · C min (5) |
| Techno (Peak Time / Driving) | 380 | 132 (15) · 135 (13) · 130 (10) · 138 (9) · 134 (9) | G (15) · F (12) · E (12) · C (11) · A# / Bb (10) | G maj (9) · F maj (8) · E maj (7) · F# maj (7) · Bb maj (7) · Ab maj (6) |
| Techno (Raw / Deep / Hypnotic) | 344 | 140 (18) · 138 (15) · 136 (10) · 145 (8) · 135 (8) | G (13) · G# / Ab (12) · D (11) · B (10) · E (10) | G min (8) · B min (7) · D min (7) · Eb min (6) · E min (6) · G# min (6) |
| Trance (Main Floor) | 378 | 140 (27) · 138 (21) · 130 (7) · 132 (6) · 145 (4) | D (12) · F# / Gb (12) · F (12) · G (12) · G# / Ab (11) | F min (8) · F# min (7) · G min (7) · D min (6) · D maj (6) · G# min (6) |
| Trance (Raw / Deep / Hypnotic) | 413 | 124 (11) · 128 (8) · 145 (8) · 134 (7) · 130 (6) | C (15) · D (12) · A (12) · F (10) · E (9) | A maj (8) · C maj (8) · F maj (8) · C min (7) · D maj (6) · D min (6) |
| Trap / Wave | 203 | 150 (14) · 140 (12) · 130 (8) · 145 (5) · 174 (5) | D# / Eb (16) · F (14) · C (13) · D (11) · C# / Db (9) | F min (13) · C min (9) · Eb min (9) · C# min (8) · G min (8) · D maj (8) |
| UK Garage / Bassline | 283 | 132 (16) · 135 (14) · 130 (13) · 134 (9) · 136 (8) | G (16) · D (14) · D# / Eb (11) · B (10) · A# / Bb (9) | D min (11) · G min (11) · B min (9) · C min (8) · E min (7) · Bb min (7) |

Sources : FAQ https://github.com/sergree/whatbpm/wiki/FAQ ; For Developers https://github.com/sergree/whatbpm/wiki/For-Developers ; historique https://sergree.github.io/whatbpm/history/AAAA-MM-JJ.json.
