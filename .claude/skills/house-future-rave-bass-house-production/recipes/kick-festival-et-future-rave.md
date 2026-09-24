# Kick de festival et de future rave : trois couches, accord, clipper

## Cible
`FUTURE RAVE, BIG ROOM, BASS HOUSE, TECH HOUSE / KICK / 126–128 BPM / accordé sur la tonique ou la quinte (≥ Mi1 41 Hz) / 4/4`

## Moteur
Drum Rack de samples en couches (voie par défaut, `../../drums-signature/SKILL.md`) ; synthèse : Serum 2, Operator, Ableton Kick (Drum Synths) ; Kick 2 cité par le cours Sonic Academy « Future Rave with Protoculture » `[DOC-EXTRAIT]`.

## Trois couches
| Couche | Bande | Réglage | Preuve |
|---|---|---|---|
| Sub | 30–80 Hz (fondamentale 50–60 future rave et big room, 50–70 tech house) | sinus accordé ; big room : court, < 100 ms en renfort ; techno-house : long, decay 300–700 ms, saturé | `[DOC-2]`, `[COMM]` |
| Corps / punch | 100–150 Hz (techno : 100–200) | decay 80–150 ms, saturation ; enveloppe de pitch 150–220 → 50–55 Hz en **15–30 ms** (909) ; SOS dit 200–500 ms pour la 909 : contradiction, à trancher à l'oreille | `[DOC-2]` |
| Clic | 2–6 kHz | 5–15 ms ; transitoire seul en seconde couche ; tech house : « pas assez de clic » est l'erreur classique | `[DOC-2]`, `[COMM]` |

Big room `[DOC-EXTRAIT Attack]` : 909 sous forte compression et saturation, mêlé à un 808 plus profond, couche de caractère 707 / LinnDrum / DMX, kick long accordé à la tonalité, grave du kick snappy coupé sous 150–250 Hz. Bass house : sub 40–80 Hz avec pitch 200 → 50 Hz en 100 ms + corps 909 80–200 + clic 2–8 kHz à −15 dB, alignés à l'échantillon.

## Serum 2 (synthèse)
OSC A sinus, Pitch track off ; ENV 2 → CRS **+24 à +36 st**, decay 20–40 ms ; ENV 1 A 0 · D 250–500 ms ; NOISE one-shot decay 5 ms + FILTER 2 HP 2 kHz pour le clic ; Distortion Tube ; Utility MONO BASS. Sub synthé une octave sous le sample si on superpose (27,5 Hz sous 55 Hz), **phase 0° à chaque trigger** (RAND 0 %).

## Accord et alignement
- Accorder le kick **en dernier, contre la basse** ; 808 natif 49,5 Hz = Sol1 ; descendre à Ré1 coûte −11,8 dB ; rester ≥ Mi1 ; tonique ou quinte, ou hors de la bande de la basse : arbitrage, pas règle (`../../kick-bass-equilibre/SKILL.md`).
- Départs des formes d'onde dans le même sens, sinon inverser la polarité ; nudge par pas de 0,1–1 ms ; 5 ms à 100 Hz = annulation complète ; corrélation +1 visée en 30–80 Hz (`kick_bass_check.py`).
- Queue du kick contre le release du sidechain : un demi-temps = 234 ms à 128 ; un kick de 800 ms interdit un sub actif.

## Chaîne
EQ correctif (HPF 30 ; creux 200–400 ; boost 50–60 et 3–5 kHz) → **clipper dur à 0 dB** sur le kick, puis sur le groupe kick + clap (Saturator interdit : J37 en entrée forte, L4 Clip) → transient (attaque 5–10 ms) → compression → EQ de couleur → mono. Facteur de crête du bus batterie 12–16 dB avant master ; glue ≈ 4 dB attaque rapide.

## Toms de rave `[HEUR, aucune source]`
Tom 909 (deux triangles à la quinte) ou Simmons (triangle + bruit, chute de pitch 200–400 ms) accordé sur tonique ou quinte, decay 300–600 ms, ENV → CRS +12 st sur 50–100 ms, saturation, grave creusé pour lire « tom » et non « kick » ; en fills de doubles sur le dernier temps de chaque 8 mesures.

## Vérification
Kick seul puis avec le sub et la basse : qui tient la fondamentale est écrit ; corrélation positive ; kick plus fort que la basse dans le sub ; en mono identique ; niveau relevé par `lom.py meters`.
