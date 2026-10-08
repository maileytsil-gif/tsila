# Drop bass house en trois couches : sub, mid, growl ou wobble

## Cible
`BASS HOUSE / LA BASSE EST LE HOOK / 126–128 BPM / mi, fa, sol, la mineur / riff sur i, 2 mesures / sub MIDI 28–40, mid et growl +12 à +24`

## Moteur
Serum 2 en une instance (trois oscillateurs, deux filtres, splitter interne) ; ou trois pistes (sub Operator, mid Wavetable, growl Serum 2) groupées dans un bus BASSES.

## Les trois couches
| Couche | Bande | Contenu | Traitement | Preuve |
|---|---|---|---|---|
| **Sub** | LP 90–100 Hz | sinus, mono, unison 1 ; OSC A → **Direct** ; ENV A 4 ms R 30 ms | **aucune saturation, reverb ni LFO** ; −3 dB relatif ; hors du bus traité | `[DOC-2]`, `[COMM JefroB]` |
| **Mid / corps** | HPF sous la note jouée (78 Hz pour F2, 79 Hz Q 0,7), LP 400–500 | saw + carrée ; OSC B → FILTER 1 MG Low 24 480 Hz | saturation chaude ; **même LFO que le growl** | `[DOC-2]` |
| **Growl / caractère** | 500 Hz–2 kHz (HPF 500) ; JefroB 500 Hz–3 kHz | OSC C saws UNISON 3 FINE 17 cents → FILTER 2 1,8 kHz résonant ; WT POS modulée par LFO 10–60 Hz ou stepper 1/16 ; warp Bend 30–50 (nasal) ou FM 15–25 (guttural) | distorsion Diode ou Tube, notch −8 dB à 2,5 kHz Q 4, +3 dB à 600 Hz ; comb ou phaser ; **resample 3–5 passes** | `[DOC-2]`, `[DOC basses.md]` |
| Air (facultatif) | > 2 kHz | | « une quatrième couche = sept sons qui se battent » | `[DOC-2]` |

Règles : toutes les couches jouent **le même rythme** ; LFO identiques (LFO 1 MODE **RETRIG**, ex-« Trig » de Serum 1, RATE 1/8 ou 1/4, SMOOTH 20–50, **HOST** : le comportement ex-« ANCHOR », manuel p. 192–193) ; glue 3–6 dB de réduction sur le bus **sans le sub** ; sidechain sur toutes (« tight ducking » 4–8 dB, attaque 1–5 ms, release 100–150 ms, 8:1 à 10:1) ; mono sous 150 Hz.

## Wobble et rythme timbral
Rate du LFO 1/4, 1/8, 1/8 T (à 126–128, 1/2 est trop lent) ; MATRIX LFO 1 → CUTOFF 40 % + ENV 2 → CUTOFF 60–100 % ; DELAY/RISE du LFO pour un onset en fondu ; **changer le rate toutes les 1–2 mesures, c'est la composition** ; quatre gestes différents par cellule de 2 mesures, le vocabulaire se répète, pas la phrase.

## Serum 2, effets internes
Splitter L/M/H à 120 Hz / 2 kHz : bas propre (ou tape léger), médium = le growl (Distortion Tube puis Hard Clip, « plusieurs étages légers valent mieux qu'un lourd »), haut = Tube ; Compressor MULTIBAND MIX 30–50 % par canal, 15–30 % sur bus ; Utility MONO BASS 120–150 Hz. Presets d'usine de départ : Bass/Hard/**BA - Basilisk**, Bass/Modulated/**MDL - Slippery Snake**, Bass/Hard/**BA - RM Wub Generator** `[DOC]`.

## MIDI (la mineur, pas ; note ; vel ; gate)
1 A1 118 60 % · 4 A1 96 50 % · 7 C2 110 60 % · 9 A1 100 40 % · 11 G1 90 40 % · 13 A2 118 90 % glide → 15 G♯1 80 30 % ; mesure 2 idem sauf 13–16 : E2 tenu 4 pas `[HEUR]`. Glides en mono legato (chevauchement d'un pas) ; chromatismes un demi-ton sous la cible ; ♭2 phrygien pour le sombre.

## Kick
Propre, coupé sous 40 Hz ; couper 80–100 Hz **seulement** s'il se bat avec le sub ; clic 2–6 kHz ; « kick perdu derrière la basse » se règle par sidechain et EQ, pas par le fader (`kick-festival-et-future-rave.md`).

## Erreurs
Sub saturé ou stéréo ; growl pleine bande sans coupe-bas à 100 Hz ; LFO sans RETRIG (chaque note attrape le wobble à une phase différente) ; recettes calées sur 140–150 BPM non retransposées ; percussions qui concurrencent la basse.

## Vérification
Chaque couche seule, puis les trois ; sub seul en mono ; kick audible ; à 0, 50 et 100 % de la macro « growl » ; `kick_bass_check.py` ; niveau du bus relevé par `lom.py meters` avant et après le glue.
