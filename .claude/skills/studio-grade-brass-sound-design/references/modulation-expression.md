# Modulation et expression d'un cuivre

Ce qui bouge dans une note de cuivre, dans l'ordre du temps, et comment le réaliser. Sources : Reid SS25-27 [DOC], patchs d'usine décodés [DOC], presets Surge/Vital lus [DOC], protocole de validation.

| Instant | Phénomène réel | Réalisation | Valeurs de départ |
|---|---|---|---|
| 0–5 ms | coup de langue, bouffée « parp » | attaque d'ampli courte, enveloppe de filtre à quatre étages (montée puis redescente) | ampli A 10–100 ms (plus court fort) ; filtre A 30–600 ms selon stab/tenue, D 300–800 ms, S 50–60 % [DOC forme, HEUR ms] |
| 0–50 ms | installation de l'onde stationnaire, hauteur instable | **growl sur le cutoff** (triangle 80 Hz ou bruit) fondu par une AD ; jamais de modulation périodique de la hauteur ; scoop facultatif minuscule | growl ±10–20 % de cutoff, 50–150 ms [DOC 80 Hz/50 ms, HEUR profondeur] ; scoop −0,3 à −0,5 st sur 30–60 ms [HEUR] ; « rip » de stab trap : −7 st en 80 ms [DOC Vital] |
| 0–200 ms | les harmoniques hauts arrivent après les bas | enveloppe de filtre (ou d'index FM, ou de skew de table) **plus lente que l'ampli** | Minimoog 100 vs 600 ms [DOC] ; Vital Navigator 20 vs 106 ms [DOC] ; DX7 BRASS 1 R1 77 vs 49 [DOC] |
| 0–200 ms | section : l'attaque est plus large et plus haute | enveloppe → détune/nombre de voix d'unisson qui se resserre | Vital 80s Saw Brass : détune max → 0 en 77 ms ; euro brass : +0,25 st et +3 voix pendant 200 ms [DOC] |
| 300 ms → | vibrato des lèvres | LFO sinus 5–6 Hz → pitch, profondeur faible, Delay + Rise ; ou manuel (molette, pitch bend, aftertouch) | 5 Hz [DOC Reid], 6,1 Hz [DOC DX7/STK], < ½ demi-ton [HEUR-extrait] ; delay 300–500 ms, rise 300–600 ms [HEUR] ; Juno-60 delay 0,63–0,67 [DOC] |
| tenue | brillance qui suit le souffle | aftertouch / CC1 / CC11 → cutoff ou index FM ; sur multisample, crossfade de couches | Surge : aftertouch → cutoff +19, molette +42, vélocité +53 [DOC] |
| tenue | gonflement, diminuendo | CC11 ou macro, enveloppe à cinq étages (LFO en mode Env dessiné) | swell A 440–600 ms (Juno-106 A12/A34/A35) [DOC] |
| fin | fall, doit, plop, shake | pitch bend (±2 st pour le réalisme), Env → pitch négatif sur la dernière note, articulations échantillonnées quand la banque les a | fall 200–400 ms ; shake ±60 cents rapide ; plage de bend Kontakt à vérifier [TEST] |
| entre les notes | liaison de pistons vs coup de langue | legato sans retrigger (Mono + Legato, Operator Voices = 1, Analog Legato) vs notes détachées | chevauchement 10–20 ms en legato ; silence ≥ 20 ms pour re-attaquer [HEUR] |
| phrase | respiration | silence toutes les 2–4 mesures, ≥ 1/8 ; phrases de 8–12 s max | [DOC Rimsky : les cuivres respirent comme les bois ; HEUR durées] |

## Cuivre électronique : mouvements en plus
- Tremolo ou chop rythmique (future bass) : LFO carré/dessiné 1/8 ou 1/16 → volume ou cutoff, swing dessiné dans la forme [HEUR].
- Pitch de tout l'accord ±10–50 cents à 1/8–1/16 [HEUR].
- Ouverture progressive vers le drop : macro Brightness automatisée sur 8–16 mesures (`../../live-automation/SKILL.md`).
- Braam : pitch drop −2 à −12 st sur la queue, LP qui se referme sur 1,5 s [DOC synthdef].

## Règles
1. Un mouvement principal fort vaut mieux que cinq modulations : le « wow » du filtre d'abord.
2. Ce qui appartient à la note (growl, vibrato retardé) vit dans le patch ; ce qui appartient à la phrase (dynamique, swell, fall) vit dans le MIDI ; ce qui appartient à la structure (ouverture vers le drop) vit dans l'automation d'arrangement.
3. Vérifier qu'aucune modulation ne sort le son de son registre ni ne change son niveau de plus de 3 dB sans compensation (`validation-protocol.md`).
