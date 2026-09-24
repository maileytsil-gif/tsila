# Claviers électromécaniques : Rhodes, Wurlitzer, Clavinet, Hammond + Leslie

Ce qui est établi sur le mécanisme, le son et les réglages, d'après les sources lues (miroirs Wikipédia, manuel Live 12, openwurli, setBfree, STK, Synth Secrets 42 et 55-59, patchs DX7) — rapport complet `../../../../corpus/funk-claviers/recherche-funk-axe1-claviers-electromecaniques.md`.

## Rhodes (Mark I / Mark II, Stage / Suitcase)
- Mécanisme : marteau → **tine** (tige) liée à un **tonebar** (résonateur accordé, l'ensemble agit comme un diapason) ; pickup électromagnétique en face du tine ; étouffoir au relâchement [DOC-W, DOC manuel Live]. Tine près du pickup = « bell » [DOC-W].
- Chronologie utile [DOC-W] : 1970 Stage 73 (une sortie jack, pas d'ampli) et Suitcase (ampli + trémolo) ; 1971 pointes de marteau feutre → néoprène ; 1975 harpe alu ; fin 1979 **Mark II = changements cosmétiques** sur les derniers Mark I ; Piano Bass 32 notes E1–B3.
- **Bark** : overtones captés quand l'échappement et la distance tine/pickup sont bien réglés, dosables par la force de jeu [HEUR-extrait] ; quand le tine se rapproche de l'axe du pickup, fondamentale et harmoniques impairs baissent, **la 2e harmonique domine** [HEUR-extrait thèse UCSB] ; « les harmoniques viennent du champ du pickup, pas du métal : la hauteur du pickup re-voice l'instrument, et jouer plus fort grogne au lieu de seulement sonner plus fort » [DOC secondaire epi]. → Le bark est une **non-linéarité de captation dépendante de la vélocité**, pas une saturation d'ampli.
- Suitcase « vibrato » = **trémolo panoramique** entre deux HP, Speed / Intensity, forme triangle [DOC-W, HEUR-extrait] ; fréquence en Hz non documentée → 3–7 Hz [TEST]. Première version mono en carré, stéréo depuis 1969 [HEUR-extrait].
- Dyno-My-Piano : levier qui déplace tines/pickups + préampli 2 bandes (grave, overtones) + stéréo ; son émulé par le « DX7 Rhodes » [DOC-W, HEUR-extrait].
- Chaîne funk : wah (Herbie Hancock [DOC-W]), Echoplex (Hancock [HEUR-extrait]), phaser Small Stone / Phase 90 (« ajouter du corps », un seul bouton Speed sur le Phase 90 [DOC-EXTRAIT fenderrhodes.com]), ampli Fender Twin repiqué SM57 (Breakbot [DOC-EXTRAIT]). Réglages de phaser chiffrés : aucun lu → rate 0,3–0,8 Hz, 4 étages, après le trémolo [HEUR].
- Rhodes « laisse un trou spectral là où se trouve la voix lead » [DOC-W, citation].

## Wurlitzer 200A
- Anche en acier à ressort frappée par un marteau feutré, **pickup électrostatique** polarisé 147 V (200A) ; rapport f2/f1 ≥ 6,27 (spectre inharmonique, « saw-like » sans série harmonique) ; contact marteau/anche ¾ à 1 cycle [DOC openwurli / brevets].
- **Bark** = non-linéarité capacitive 1/(1−y) du pickup ; préampli quasi linéaire ; « anche plus proche = plus fort ET plus dur » ; le gap d'origine n'est documenté nulle part (archives détruites en 1988) [DOC openwurli].
- « Vibrato » = **trémolo de gain**, oscillateur twin-T **≈ 5,56–5,63 Hz fixe**, profondeur 0 / 1,4 / 2,6 / 4,0 / 7,6 dB, **module le gain du préampli** (donc le timbre et la distorsion), asymétrique : dips 2,5 ms, recovery 35 ms (« choppy ») ; **mono** [DOC openwurli].
- 64 notes A1–C7 ; 200 (1968), **200A (1974)**, 200B (1978) [DOC-W].
- « Doux et proche du vibraphone joué doucement, agressif et légèrement overdrivé joué fort » [DOC-W].

## Clavinet D6
- Clavicorde amplifié, Hohner 1964–début 80s ; **60 touches F1–E6 (43,6–1 318,5 Hz)**, 60 cordes en diagonale, pad de caoutchouc qui « frette » la corde (hammer-on), **fil de laine qui étouffe au relâchement**, deux pickups (D6 : six bobines) [DOC-W]. Pads qui se décomposent avec l'âge ; chute de hauteur de **3 demi-tons** au relâchement quand la longueur morte rejoint la corde [DOC secondaire epi].
- Sélecteurs : C = un pickup, D = les deux ; A/B = lequel ou la phase (deux sources se contredisent sur l'étiquetage) ; hors phase = fin et nasal [DOC secondaire / HEUR-extrait] ; Brilliant/Treble = passe-haut, Medium/Soft = passe-bas [HEUR-extrait] ; fréquences réelles non trouvées ; mute mécanique à droite.
- Effets documentés : « Higher Ground » (1973) **à travers un Mu-Tron III** (envelope filter à Vactrol : Gain, Peak, Range Lo/Hi, Mode LP/BP/HP, Direction Up/Down) [DOC-W, DOC secondaire] ; « Superstition » : **plusieurs pistes de Clavinet**, chaîne Margouleff/Cecil « Mutron phaser, wah, distorsions » [HEUR-extrait] ; réglages exacts non trouvés. Presets d'une recréation Mu-Tron [HEUR] : « Higher Ground » Range Hi, BP, Up, gain 6,5, peak 7, attaque 5 ms, release 120 ms ; « Classic Funk » attaque 8 ms, release 180 ms.
- Pourquoi l'auto-wah marche : attaque percussive + decay court + étouffement immédiat → le filtre suit chaque note ; BP + Up = « quack » [HEUR].
- Aucun épisode Synth Secrets sur le Clavinet ; le hard sync est cité (SS43) comme « un des moyens les plus faciles d'imiter une corde frappée ou pincée » [DOC].

## Hammond B-3 + Leslie
- 9 drawbars = harmoniques **1 (16'), 3 (5⅓'), 2 (8'), 4 (4'), 6 (2⅔'), 8 (2'), 10 (1⅗'), 12 (1⅓'), 16 (1')** du 16' ; jamais 5, 7, 9, 11, 13, 14, 15 ; **3 dB par cran** (8 = 0 dB … 1 = −21 dB) ; 83 4211 100 ≈ dent de scie, 00 8030 200 ≈ carré [DOC SS55, DOC secondaire ZOIA]. Pas de vélocité ; 2 × 61 notes, pédalier 25 ; 91 roues phoniques ; fuites (« leakage ») = « qualité rauque » [DOC-W, DOC setBfree, DOC SS].
- **Registrations** (setBfree `default.pgm` [DOC] ; ZOIA/GRAINS [DOC secondaire]) : Jimmy Smith **888 000 000**, perc 3rd soft fast, C3 ; Booker T **888 630 000** perc 2nd ; Green Onions 888 800 000 / 808 800 008 ; Gospel **888 000 008** ; whistle 800 000 008 ; **Funky Comping 688 600 004** ; **Fat 888 000 888** ; Brother Jack 800 000 888 ; Bright Comping 878 000 456 ; Groove Holmes 888 420 080 ; House Bass 880 000 000 (L : 008 080 000). Conseil : baisser les 8 à 7 ou 6 pour s'asseoir dans le mix [HEUR-extrait].
- **Percussion** : 2nd (4') ou 3rd (2⅔') du 8' en accent d'attaque ; **single-trigger** (pas de percussion si une note est déjà tenue) ; Normal/Soft (−6 dB), Fast/Slow (setBfree : **1 s / 4 s**) ; **le 1' est coupé** quand la percussion est active ; la tenue baisse un peu [DOC SS57, DOC setBfree].
- **Vibrato/chorus** : scanner ≈ **7 Hz** ; V1/V2/V3 = profondeurs 1 / 2,5 / 5 ; C = mélange sec + scanner ; « le chorus Hammond ne mélange qu'une seule instance modulée, un ensemble à trois lignes est bien trop luxuriant » [DOC SS57, DOC setBfree].
- **Key click** : bouffée de 0,6–2,9 ms, niveau 0,5 à l'attaque, 0,25 au relâchement [DOC setBfree] ; « défaut de conception devenu signature » [DOC-W].
- **Leslie** [DOC setBfree, DOC SS58-59] : crossover **800 Hz** ; horn **40,3 rpm (0,67 Hz) → 423,4 rpm (7,06 Hz)**, τ accélération 0,161 s, décélération 0,321 s ; tambour **36 rpm (0,60 Hz) → 357,3 rpm (5,96 Hz)**, τ 4,127 s / 1,371 s ; Doppler **±1 %** ; AM à 90° de la FM ; filtres : tambour high-shelf 812 Hz −39 dB, horn LP 4,5 kHz + low-shelf 300 Hz −30 dB ; overdrive avant reverb. Forums : chorale 30–50 rpm, tremolo ≈ 250–400 rpm, horn 1–3 s pour monter [HEUR-extrait].
- Recettes SS55-56 [DOC] : Juno-6 « 888 000 000 » = pulse 33,3 % (supprime un harmonique sur trois) + sub carré −1 octave à fond, VCF résonance 100 % auto-oscillant **19 demi-tons au-dessus du sub** (= le 5⅓'), VCA en gate, clic par une enveloppe de filtre instantanée ; Kawai K3 additif : harmoniques 1, 2, 3 = 31, reste 0. Limite : réaliste pour 888 000 000 seulement.

## Tessitures et registres funk
| Instrument | Tessiture | Registre funk [HEUR] |
|---|---|---|
| Rhodes 73 / 88 | 73 notes (E–E [MÉMOIRE]) / A0–C8 [DOC-W] | accords 4 sons C2–C5, main gauche rarement sous E1 |
| Wurlitzer 200A | 64 notes A1–C7 [DOC-W] | comping C3–C5, bark au médium |
| Clavinet D6 | 60 notes F1–E6 [DOC-W] | riffs F2–C5 (zone guitare), F1–C2 pour doubler la basse |
| Hammond B-3 | 2 × 61 (C–C), pédalier 25 [DOC-W] | comping C3–C5, glissandi à C6, basse main gauche sous C2 |

## Erreurs classiques
Rhodes : vibrato réglé en hauteur ; bark par Saturator ; release trop long ; oublier Stretch. Wurli : même patch que le Rhodes « + drive » ; trémolo sinus lent au lieu de 5,6 Hz choppy sur le gain ; trémolo stéréo. Clav : sustain ; pas de bruit de relâchement ni de chute de 3 st ; envelope filter trop lent ; trop grave. Hammond : vélocité ; attaque en fondu ; percussion retriggée sans couper le 1' ; vibrato = LFO de pitch (« cheesy ») ; Leslie = simple auto-pan ; chorus trop riche ; harmoniques 5, 7, 9 présents.
