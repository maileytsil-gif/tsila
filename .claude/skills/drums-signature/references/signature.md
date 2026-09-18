# Registre de signature sonore (lisible) — données dans `scripts/signature.json`

## Palette « deep chill minimal house » (validée 14 sept. 2026, 120 BPM, fa mineur)
| famille | son | source | réglages | chaîne |
|---|---|---|---|---|
| Kick | Serum 2 « DR - Kick Minimal » (2 sinus, decay 294 ms) | preset factory | note C1 (suit la hauteur), ≈ −3 dB avant fader | EQ HP 28 / LP 9 k → Saturator |
| Clap / Rim | Clap 808 Light Quick (−5 dB) · Rim 808 (−2 dB, pan 7R) | Core Library one-shots | pads C1/D1 | REQ 6 HP 180, creux 650 |
| Hats | Hihat Closed Kaninchen (+2) · Hihat Open RKTD (+2, 6L) | Core Library | F#1/A#1, swing 16e 0,03 | Auto Filter (automatisé), REQ 6 HP 400 |
| Percs | Cabasa Short Mid (11L) · Conga Acoustified Low (13R) · Conga Soft (6L) | Core Library | C1/D1/E1 | REQ 6 HP 200 |
| Sub | Serum 2 sinus mono+legato, release 90 ms | patch maison | F0 | Utility mono → EQ 24–130 → SC kick |
Bus batterie : bx_glue 4:1 (3 ms, auto, −13, +1,5, SC HP 60) → API-2500 parallèle 30 % → REQ 6.

## Comment garder la signature sur un nouveau morceau
1. Recharger la palette (`kit_builder.py` → `ppal-create-device` par famille) et la chaîne bus.
2. Changer au plus deux pièces (ex. hats plus brillants, un perc de plus) — trouvées avec `findSimilar` sur le son remplacé.
3. Accorder le kick/sub à la nouvelle tonalité ; garder les niveaux relatifs (kick −3, clap −6, hats −12, percs −14).
4. Noter dans `historique` ce qui a changé et pourquoi ; une pièce nouvelle validée à l'écoute rejoint la palette.
