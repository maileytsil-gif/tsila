# Risers, impacts, downlifters, vocal risers : les FX de transition

## Cible
`Toute famille / FX / 8 ou 16 mesures avant le drop (4 pour une transition courte) / trois à cinq dispositifs par couture, deux vrais silences par morceau`

## Riser de bruit (Serum 2, patch chiffré)
| Étage | Valeur | Preuve |
|---|---|---|
| OSC A | NOISE White 100 %, UNISON 4, DETUNE 12 cents | `[DOC-EXTRAIT SoundBridge]` |
| OSC B | sinus OCT −1, WARP FM from OSC A 30 % | idem |
| FILTER 1 | Comb, MIX 100 %, RES 60 %, CUTOFF automatisé **100 Hz → 12 kHz sur 4 mesures** (8 ou 16 pour un drop) | idem |
| ENV 1 | A 0 · D 1,2 s · S 0 · R 0 (une seule note tenue) ; ou ENV en mode **BPM** (A = 8 bars) | idem ; `[DOC]` |
| LFO 1 | 1/8 triangle 70 % → CUTOFF et PAN | idem |
| Version simple | bruit blanc passe-bande **200 Hz → 8 kHz** exponentiel, RES 30 %, volume −∞ → 0 dB sur 8 mesures, +1 octave sur les 4 dernières (option), pas de pitch 1/8 ou 1/16 (« stepped riser ») | `[DOC-2 amen, Fearvox]` |

## Riser tonal et Shepard
Saw ou carrée montant **1–3 octaves**, LP qui s'ouvre, vibrato croissant, finir sur une note **hors** de l'accord du drop (demi-ton sous la tonique) ; Shepard : 4–6 copies à l'octave, volume en cloche ; LFO Mode **Env** pour un balayage one-shot.

## Filtre de bus pendant le build
LP 300–500 Hz → 16 kHz sur les 8 mesures avant le drop, RES 10–15 % ; puis HP du mix 20 → 400–800 Hz sur les 4 dernières mesures (la basse disparaît) ; automatiser **sur un bus** (`../../live-automation/SKILL.md`).

## Fin de build et premier temps
Coupure nette au temps 1 ; reverb « cut dead at the drop » ; dernier temps vide ; **impact** = grave sinus 60 → 30 Hz decay 1–2 s + **sub-drop** 80 → 25 Hz sur 0,5–2 temps saturé + burst médium + clic + crash, crêtes alignées au début, quasi mono, queue de reverb inversée avant ; impact + crash + sub-drop + mix complet **sur le même échantillon**.

## Downlifter et tape stop
Même source que le riser, pitch **−12 à −24 st** sur 1 mesure, LP qui se ferme, send de reverb qui monte, posé sur le **premier temps** de la nouvelle section ; riser et downlifter se croisent sur la dernière mesure ; tape stop 200–600 ms ; Serum 2 : LFO Mode Env → CRS −24 st, ENV BPM 1 bar, NOISE Brown pour le grondement.

## Vocal riser
Délier pitch et timbre ; pas de pitch alignés sur le chop (−quinte, +quinte, retour sur les mesures 2–4) puis montée continue ; delay 1/4 feedback 30 % (les répétitions héritent du pitch) ; second pitch-shifter descendant sur la queue de reverb `[DOC-2 Attack]`.

## Budget
Snare roll 1/8 → 1/16 → 1/32 → 1/64 + riser + HP du mix + reverb send + crowd = une couture ; « un riser sur chaque transition cesse de fonctionner » ; deux vrais silences par morceau.

## Vérification
Le riser ne masque pas la basse filtrée ; rien ne bave sur la mesure 1 ; impact en mono ; à −6 à −10 LU sous le drop en breakdown.
