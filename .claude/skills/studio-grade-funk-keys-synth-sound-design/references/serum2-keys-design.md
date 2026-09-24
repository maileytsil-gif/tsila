# Serum 2 pour les claviers et synthés funk

Faits : corpus mesuré des 626 presets d'usine (2.0.11-2.0.15) [DOC-mesure], manuel dépouillé localement (`../../sound-designer-serum/references/`), manuel Serum 1.0.1 lu (voicing et LFO identiques), site Xfer en extraits. Serum 2 n'expose rien à l'API de Live sans configuration : réglages par clics et captures (`../../vst-sound-design/references/serum2.md` : boutons MONO (1058,627), LEGATO (1058,653), PORTA (1081,720)).

## Quand Serum 2 plutôt que le natif
- **Synth bass mono** (Flash Light, Thriller, Chameleon, Chromeo, G-funk lead) : MONO + LEGATO, `PortamentoTime` (jusqu'à 2,6 s), `PortaAlways` (glisse même sans legato), `PortaScaled` (temps proportionnel à l'intervalle), courbe de portamento [DOC-mesure] ; filtres ladder **MG Low 6/12/18/24, LadderMg, LadderAcid, LadderEMS, DirtyMg** [DOC-mesure] ; FAT dans la résonance [DOC]. Le Minimoog = MG Low 24 ; l'Odyssey = un 12 dB.
- **Rhodes / Wurli échantillonnés** : Multisample d'usine **`Keys/Elec.Piano Suitcase.sfz`** (aussi Baby Grand Piano, RDE88) [DOC-mesure] ; `TimbreShift`, `VelTrack`, enveloppe AHDSR propre, warps FM/PD/RM/AM et distorsions Tube/TapeSat/StompBox/Diode/SoftClip sur le multisample [DOC-mesure]. Les points de boucle embarqués dans les WAV ne sont pas importés [DOC-EXTRAIT forum Xfer].
- **Basse échantillonnée** : samples d'usine `Bass/` : « Alu Slap », « Clean 808 », « JB Fingerstyle », « PB Fingerstyle », « Round Comforting », « Samo Op » [DOC-mesure] — le « JB/PB » = Jazz/Precision Bass pour un doublage à la Jamiroquai ou la couche « réaliste » de Don't Start Now.
- **FM DX7** : Warp **FM from B** Linear (garde la hauteur) [DOC] ; pas de feedback d'opérateur documenté → B en scie ou distorsion sur B ; pour E.PIANO 1 (ratio 14) : B à +3 octaves + 2 st (ratio 14 ≈ 3 octaves + 2,4 st, à caler à l'oreille [TEST]) ; l'Operator de Live reste plus direct (`dx7-fm-keys-bass.md`).
- **Talkbox** : filtre à formants (la page Xfer parle d'un « formant filter … contrary-motion mirror-image harmonics » [DOC-EXTRAIT]) ; nom exact dans 2.1.5 à relever [TEST] ; sinon `CombP`, `Combs`, `Allpasses`, `Phase24P`, `PZ_SVF` (filtre dessinable) [DOC-mesure] ; table de formants d'homme (SS23) : « oo » 300/870/2250, « a » 660/1700/2400, « ee » 270/2300/3000 Hz [DOC].
- **Poly analogique** : unison 2–16, `UnisonStack` (octaves, quinte, Center-12), `UnisonStereo`, `UnisonTrigPattern` [DOC-mesure] ; Chorus 4 voix, Phaser (POLES), Flanger, Hyper/Dimension [DOC].
- **Grain SP-303 / bande** : Distortion 13 types ; Compressor SINGLE/MULTIBAND avec mode Limit [DOC] ; pas de réducteur de bits documenté → Redux natif après Serum.

## Réglages par famille [HEUR sauf mention]
| Famille | OSC | Filtre | Enveloppes | Voicing | FX |
|---|---|---|---|---|---|
| P-Funk bass (Flash Light) | A scie −12 st (32'), B scie ou pulse 25–40 % (16'), fine ±10 cents, Sub pour la « 3e unité » | MG Low 24, 120–800 Hz, rés 25–35 % | Env 2 → cutoff +60–80 %, A 0, D 80–600 ms, S 0 (pluck) ou plein (« ouvert », joué au bend) ; Env 1 A 0–2 ms, R 15–20 ms | MONO LEGATO, porta 45 ms, bend ±12 | Distortion Tube léger ; Compressor opto-like en Live |
| Chameleon (Odyssey) | 2 scies fine ±5–8 cents | **12 dB**, 150–250 Hz, rés 70–85 %, FAT/drive | Env 2 → cutoff +50–70 %, D 80–150 ms, S faible ; Env 1 AR court | MONO LEGATO | drive doux avant filtre |
| Juno bass (Chromeo) | Sub + scie +12 st | MG Low 24, 300–600 Hz | « à goût » | MONO ou poly | Chorus I |
| G-funk lead | A scie +24, B carré +24 fine +5–8, C ou Sub −12 à 60–70 % | LP 24 ouvert, rés 20–30 %, pas d'env | A 5–10 ms, R 100–200 ms | MONO LEGATO, porta 60–120 ms | LFO 5–6 Hz → pitch ±10–20 cents à la molette, delay en envoi |
| Rhodes Multisample | Elec.Piano Suitcase | LP doux si besoin | env du multisample | poly 8 | Chorus 4 voix, Phaser, Compressor |
| Talkbox | A scie (ou scie + pulse 30 %) | Formant/PZ_SVF morphé par macro ou LFO | — | MONO LEGATO porta 30–80 ms | Distortion douce, EQ coupe-haut 5–6 kHz |

## Macros et bridge
Voir `macro-bridge-schema.md` ; pour Serum 2, mapper les macros avant de compter sur l'automation de Live (`../../sound-designer-serum/references/serum2-automation-et-migration.md`).
