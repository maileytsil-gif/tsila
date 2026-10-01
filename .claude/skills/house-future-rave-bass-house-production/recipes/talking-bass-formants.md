# Talking bass : filtre formant et voyelles

## Cible
`BASS HOUSE / BASSE MID « qui parle » / 126–128 BPM / sur sub séparé / morph entre deux voyelles sur 2–4 mesures`

## Moteur
Serum 2 : FILTER 1 type **Formant I, II ou III** (« le cutoff morphe entre voyelles », VAR = FORMNT), FILTER 2 MG Low 24 en série pour la brillance ; ou deux filtres Band 12 aux fréquences F1 et F2. Preset d'usine de départ : Vox/**VOX - I Talk** `[DOC-2 DUBFORGE]`. Natif : Vocoder d'Ableton avec bruit en porteuse ; Auto Filter n'a pas de formant.

## Formants (Hz)
| Voyelle | F1 / F2 (amen) | F1 / F2 « adaptés à la basse » (DUBFORGE) |
|---|---|---|
| ee / I | 270 / 2290 | 390 / 1990 |
| eh / E | 530 / 1840 | 660 / 1720 |
| **ah / A** | 730 / 1090 | 730 / 1090 |
| **oh / O** | 570 / 840 | 570 / 840 |
| oo / U | 300 / 870 | 440 / 1020 |
F3 fixe 2500–3000 Hz « pour le réalisme ». Les deux tables coïncident sur ah et oh, les voyelles les plus utiles pour une basse.

## Patch
| Étage | Valeur | Preuve |
|---|---|---|
| Source | saw, growl (`drop-bass-house-trois-couches.md`) ou wavetable de voix (« custom wavetables from vocals — the formants survive ») | `[DOC-2]` |
| FILTER 1 | Formant I ; CUTOFF = position entre voyelles ; RES 20–40 (les voyelles restent définies) ; VAR (FORMNT) = décalage global | `[DOC]`, `[DOC-2]` |
| Mouvement | « de oh à ah c'est un tout petit mouvement de bouton ; balayer toute la course donne une démo de filtre, pas une voix » : trouver deux positions, moduler lentement entre elles (LFO 2–4 mesures ou macro), sans delay d'abord | `[DOC-EXTRAIT]` |
| Le « parler » | LFO 1 Mode Trig, 1/8, petite plage sur CUTOFF, combiné au morph lent | `[DOC-2]` |
| FILTER 2 | MG Low 24 3–5 kHz, en série, pour retirer le fizz | `[HEUR]` |

## Chaîne
Splitter L/M/H : < 120 Hz propre, 120 Hz–2 kHz waveshaping lourd (Tube puis Hard Clip), > 2 kHz Tube ; Compressor MULTIBAND ; coupe-bas 100 Hz ; **sub séparé**, Direct.

## Erreurs
Course entière du filtre ; résonance trop haute (sifflement) ; delay et reverb posés avant d'avoir deux voyelles nettes ; sub dans le même chemin que le formant.

## Vérification
Deux voyelles identifiables à l'oreille sur la boucle du drop ; mono ; kick audible ; à 0, 50 et 100 % de la macro « voyelle ».
