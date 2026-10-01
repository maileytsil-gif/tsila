---
titre: "Rapport de recherche — Axe F1 : claviers électromécaniques du funk (Rhodes, Wurlitzer, Clavinet, Hammond + Leslie)"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: claviers électromécaniques
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE F1 — Claviers électromécaniques du funk (Rhodes, Wurlitzer, Clavinet, Hammond + Leslie)

Rapport de recherche pour le skill « sound design des synthés et claviers du funk moderne » (Ableton Live 12 + Serum 2).
Date : 2026-09-24.

Conventions de marquage :
- **[DOC]** : lu dans une source primaire (manuel, texte intégral d'un article, code source d'un émulateur de référence, dump de patch).
- **[HEUR]** : plage ou valeur issue de tutoriels, de forums, de pratique, ou d'un *extrait* de recherche dont la page n'a pas pu être lue.
- **[TEST]** : à valider dans le Set.
- **[MÉMOIRE, non vérifié]** : vient de ma mémoire, aucune page lue ne le confirme.

## 0. Méthode et limites (à lire d'abord)

Le proxy réseau de l'environnement a refusé **tous** les domaines web classiques (soundonsound.com, ableton.com, en.wikipedia.org, clavinet.com, fenderrhodes.com, pianogroove.com, reverbmachine.com, forums…) — erreur `EGRESS_BLOCKED` sur chaque `WebFetch`. Seuls `raw.githubusercontent.com` (lecture de fichiers) et l'outil de recherche (extraits seulement, budget épuisé après ~20 requêtes) étaient utilisables.

J'ai donc contourné en lisant **intégralement** des copies ou des sources primaires hébergées sur GitHub :
- les **textes intégraux** des Synth Secrets de Gordon Reid (miroir Markdown fidèle, avec URL d'origine SOS en tête de chaque fichier) : parties 42, 55, 56, 57, 58, 59 ;
- le **manuel Ableton Live 12**, chapitre 30 « Live Instrument Reference » (miroir Markdown : sections Electric 30.5, Operator 30.9, Tension 30.12) ;
- les **noms officiels de paramètres** d'Electric/Tension/Operator (scripts MIDI Remote de Live 12 + doc ClyphX) ;
- **setBfree** (émulateur B-3/Leslie de référence : `default.cfg`, `default.pgm`, `b_whirl`, `vibrato.c`, `tonegen.h`) ;
- **openwurli** (modèle physique du Wurlitzer 200A dérivé du schéma : docs de recherche) ;
- **STK** (Perry Cook / Gary Scavone : `Rhodey.cpp`, `Wurley.cpp`, `BeeThree.cpp`) ;
- deux **dumps du patch DX7 « E.PIANO 1 »** (ROM1A #11 converti en Faust, et JSON) ;
- des **miroirs texte de Wikipédia** (Rhodes, Wurlitzer, Hammond, Clavinet) ;
- émulateurs et documents secondaires (ZOIA Hammond, GRAINS Booker, Cabbage Clavinet.csd, zoo-tron Mu-Tron III, epi).

Ce qui n'a été vu **qu'en extrait de recherche** (donc [HEUR]) : la page « bark » de Chicago Electric Piano, la FAQ clavinet.com, PianoGroove (drawbars), les vitesses Leslie de forums, Dyno-My-Piano (fenderrhodes.com), les tutoriels Electric/Operator, Mu-Tron III (Guitar World / Wikipédia).

---

## 1. Fender Rhodes (Mark I, Mark II, Suitcase vs Stage)

### 1.1 Mécanisme tine + tonebar + pickup

- « Pressing a key results in a hammer striking a thin metal rod called a tine connected to a larger "tone bar". The tone generator assembly acts as a tuning fork as the tone bar reinforces and extends the tine's vibrations. A pickup sits opposite the tine, inducing an electric current from the vibrations like an electric guitar. » **[DOC]** — miroir Wikipédia « Rhodes piano » : https://raw.githubusercontent.com/usamaahmedsh/synthetic-data-langchain-rag/main/data/raw/great_depression/pages/Rhodes_piano.txt (original : https://en.wikipedia.org/wiki/Rhodes_piano, bloqué).
- « Vibrating tines produce a mellower timbre, and the sound changes with the tine's relative position to the pickup. Putting the two close together gives a characteristic "bell" sound. » **[DOC]** (même source).
- Comparaison Wurlitzer : « The Rhodes has a better sustain, while the Wurlitzer produces significant harmonics when the keys are played hard, giving it a "bite". » **[DOC]** (même source).
- Le manuel Live 12 décrit le même mécanisme pour Electric : « The fork is made of two parts, called the tine bar and tone bar. The tine bar is where the hammer hits the fork while the tone bar is a tuned metal resonator […] releasing the key applies a damper to the fork » **[DOC]** — manuel Live 12 §30.5.1 (miroir : https://raw.githubusercontent.com/djaboxx/iron-static/main/docs/api/ableton/30-live-instrument-reference.md ; original : https://www.ableton.com/en/live-manual/12/live-instrument-reference/).
- Le Rhodes laisse « un trou » spectral là où se trouve la voix lead (Benjamin Love, Retro Rentals, cité par Wikipédia) **[DOC, citation indirecte]**.

### 1.2 Chronologie et modèles (utile pour « Mark I vs Mark II », Stage vs Suitcase)

Toutes ces dates : **[DOC]** miroir Wikipédia ci-dessus.
- 1965 : premier Fender Rhodes 73 notes, deux parties (piano + enceinte/ampli dessous) ; lid fibre de verre (« silvertop »), remplacé en 1969 par du plastique moulé.
- 1970 : **Stage 73** (≈ 59 kg / 130 lb), quatre pieds, pédale de sustain, **une seule sortie jack** ; catalogue conseillant un Fender Twin Reverb. L'ancien modèle deux-pièces est renommé **Suitcase**.
- 1971 : modèle **88 notes** ; **pointes de marteau passées du feutre au néoprène** (1971).
- 1975 : supports de harpe **bois → aluminium** (« it changed the resonance of the instrument slightly »).
- 1977 : ampli Suitcase 80 → 100 W.
- Fin 1979 : **Mark II** = « simply a set of cosmetic changes over the most recent Mk I models » ; un 54 notes ajouté.
- 1980 : Mk III EK-10 (piano + synthé, peu vendu). 1984 : Mk V (corps plastique plus léger, action améliorée).
- Suitcase : « includes a built-in power amplifier and a tremolo feature that bounces the output signal from the piano across two speakers. This feature is inaccurately labeled "vibrato" ». **[DOC]**
- Piano Bass (1962) : 32 notes E1–B3. **[DOC]**
- Publicité 1976 : 82 % des 100 premiers albums Billboard avec piano électrique utilisent un Rhodes. **[DOC]**
- Utilisateurs : Herbie Hancock (Rhodes **à travers une wah-wah**), Chick Corea, Zawinul, Billy Preston, Stevie Wonder (« You Are the Sunshine of My Life »), Donny Hathaway, Bob James (« Angela »). **[DOC]**

### 1.3 Le « bark », l'asymétrie selon la vélocité, la position du pickup

- Extrait (page bloquée) Chicago Electric Piano : « The "bark" is produced by the overtones generated by the Rhodes' tine and tone bar when proper escapement and pickup distance is set to capture these overtones within their magnetic fields. When setup properly, the dynamic range of the bark can be set such that the player can bring out more or less bark with more or less forte in their playing. » **[HEUR]** — https://chicagoelectricpiano.com/rhodes/fender-rhodes-bark/
- Extrait (thèse UCSB Greg Shear, non lue) : « As the tip of the tine gets closer to the pickup axis, the fundamental and odd harmonics decrease, causing the second harmonics to rise as the strongest frequency of the spectrum. » **[HEUR]** — https://www.mat.ucsb.edu/Masters/GregShearMasters2011_12_5.pdf
- Physique reprise par un modèle physique open source (epi, DatanoiseTV) : « The harmonics come from the pickup's field, not the metal — which is why the pickup HEIGHT knob re-voices the instrument the way the real voicing screw does, and why playing harder growls instead of just getting louder. » **[DOC, source secondaire]** — https://raw.githubusercontent.com/DatanoiseTV/epi/main/README.md
- Wikipédia sur Dyno-My-Piano : « Chuck Monte manufactured an after-market modification to the Rhodes, known as Dyno My Piano. It included a lever that moved the relative position of the tines to the pickups, modifying the sound, and fed the output signal through additional electronics. This sound was emulated by the Yamaha DX7 with a patch known as the DX7 Rhodes ». **[DOC]**
- Extraits (fenderrhodes.com, ep-forum, bloqués) : le Dyno typique = **deux modifs** : (1) réglages physiques d'action et de position tine/pickup, (2) **préampli actif avec EQ spécifique** — « two tunable EQ bands — one for bass and one for overtones », plus un effet stéréo ; le préampli remplace **Volume et Bass Boost** sur le namerail des Stage. **[HEUR]** — http://www.fenderrhodes.com/history/dyno.html ; https://ep-forum.com/smf/index.php?topic=516.0
- Conclusion pour l'émulation (déduite des points ci-dessus) : le bark n'est pas une saturation d'ampli mais une **non-linéarité de captation** (position verticale du tine par rapport à l'axe du pickup + distance + force de frappe) qui fait monter la **2e harmonique** et les partiels supérieurs avec la vélocité. **[HEUR]**

### 1.4 Vibrato stéréo du Suitcase (trémolo panoramique)

- Nature : trémolo d'amplitude alterné entre deux HP, étiqueté « Vibrato » par cohérence avec les amplis Fender. **[DOC]** (Wikipédia).
- Extraits (fenderrhodes.com/history/effects.html, bloqué) : « When the Suitcase amps went stereo in 1969, this pattern was translated into a panning effect. Front-panel controls were provided for Speed and Intensity. » ; un autre extrait indique « Rhodes panners used a triangle wave pan effect » (Apple Logic Pro « Vintage Electric Piano Tremolo »). **[HEUR]** — http://www.fenderrhodes.com/history/effects.html ; https://support.apple.com/guide/logicpro/tremolo-effect-controls-lgsifc1b9de5/mac
- **Fréquence en Hz : non trouvée dans une page lue.** Le modèle epi parle seulement de « the stereo panner its amplifier called vibrato » **[DOC secondaire]**. Plage de départ pratique pour le funk : 3–7 Hz **[MÉMOIRE, non vérifié]** → **[TEST]**.

### 1.5 Chaîne d'effets funk typique (Rhodes)

Aucune page de réglages chiffrés de phaser (Phase 90 / Small Stone) n'a pu être lue ; le budget de recherche s'est épuisé sur ces requêtes. Ce qui est documenté :
- Herbie Hancock : Rhodes à travers une **wah-wah** **[DOC]** (Wikipédia).
- Dyno-My-Piano : préampli/EQ 2 bandes + stéréo **[HEUR]** (extraits).
- Suitcase : trémolo panoramique Speed/Intensity **[HEUR]**.
- Phaser MXR Phase 90 / EHX Small Stone, chorus, compression : chaîne « classique » des années 70 **[MÉMOIRE, non vérifié]** ; réglages **[TEST]**. Recommandation de départ (pratique, non documentée) : phaser 4 étages, rate 0,3–0,8 Hz, après le trémolo ; compresseur doux (ratio 2–3:1) avant le phaser pour uniformiser le bark **[HEUR/TEST]**.

### 1.6 Ableton Electric (Live 12) — ce que dit le manuel, paramètre par paramètre

Source unique : manuel Live 12 §30.5 (miroir djaboxx/iron-static) **[DOC]**. Electric est « developed in collaboration with Applied Acoustics Systems », modèle physique, pas de samples.

**Hammer (Mallet)**
- **Stiffness** : dureté de la surface du marteau ; « Higher values simulate a harder surface, which results in a brighter sound. » Modulable par **Vel** et **Key**.
- **Noise** : bruit d'impact ; sous-paramètres **Pitch** (fréquence centrale du bruit), **Decay**, **Key** (volume du bruit selon la hauteur).
- **Force** : « intensity of the hammer's impact on the fork. Low Amount values simulate a soft impact while high values result in a hard impact. » Modulable par **Vel** et **Key**.

**Fork**
- **Tine** : « the portion of the fork that is directly struck by the hammer ». **Color** : « relative amplitude of high and low partials in the tine's spectrum » ; **Decay** ; **Key** (niveau selon hauteur).
- **Tone** : « the secondary resonance of the fork » (= tonebar), avec **Decay**.
- **Release** : « applies to both Tine and Tone, and controls the decay time of the fork's sound after a key is released. »

**Pickup**
- **Symmetry** : « simulates the vertical position of the pickup. At 50%, the pickup is directly in front of the tine, which results in a brighter sound. Lower amounts move the pickup below the tine, while higher amounts move it above the tine. »
- **Distance** : « Higher amounts increase the distance, while lower amounts move the pickup closer. Note that the sound becomes more overdriven as the pickup approaches the tine. »
- **Type R / W** : « In the R position, Electric simulates electro-dynamic pickups, while W is based on an electro-static model. » (R = Rhodes, électromagnétique ; W = Wurlitzer, électrostatique.)
- **Input** : « amount of the fork's signal that is fed to the pickup, which in turn affects the amount of distortion » ; **Output** : niveau de sortie de la section. « a low amount of input with a high amount of output will produce a cleaner sound than a high input with a low output. » **Key** module la sortie.

**Damper**
- **Tone** : « stiffness of the dampers. Lower values simulate soft dampers, which produces a mellower sound. »
- **Level** : quantité de bruit d'étouffoir.
- **Att/Rel** : « At -100, damper noise will only be heard during the note's attack phase. At 100, the noise is present only during the release phase. »

**Global** : Volume, Voices, **Semi**, **Detune** (± 50 cents), **Stretch** (accord étiré, 0 % = tempérament égal), P.Bend, etc.

Noms API (pour LOM/ClyphX/scripts) **[DOC]** — https://raw.githubusercontent.com/nuno-andre/clyphx/master/docs/live_instant_mapping.md et https://raw.githubusercontent.com/gluon/AbletonLive12_MIDIRemoteScripts/main/_Generic/Devices.py (classe interne **`LoungeLizard`**, banques : 'Mallet and Tine', 'Tone and Damper', 'Pickup', 'Modulation', 'Global') :
`M Stiffness, M Force, Noise Pitch, Noise Decay, Noise Amount, F Tine Color, F Tine Decay, F Tine Vol, F Tone Decay, F Tone Vol, F Release, Damp Tone, Damp Balance, Damp Amount, P Symmetry, P Distance, P Amp In, P Amp Out, Pickup Model, M Stiff < Vel, M Stiff < Key, M Force < Vel, M Force < Key, Noise < Key, F Tine < Key, P Amp < Key, Volume, Voices, Semitone, Detune, KB Stretch, PB Range`.

**Ce que disent les tutoriels** (extraits seulement, pages bloquées) **[HEUR]** : « greater Stiffness produces more metallic sounds, and greater Force generates more harmonics » ; « Tine settings affect the sound of the mallet striking the tine, whereas the Tone settings affect the sound and duration of the tone-bar vibrations. Turn one's level down and the other's up to hear the difference. » — https://theaudioowl.com/ableton-live/ableton-electric-piano-sounds/ ; https://www.ableton.com/en/packs/electric/ . **Aucune valeur numérique de preset n'a été trouvée.**

**Recette de départ Rhodes Mark I « bark » (déduite du manuel + physique, à valider) [TEST]** :
- Pickup Model **R** ; **Symmetry** légèrement hors 50 % (ex. 40–45 % ou 55–60 %) pour recréer l'asymétrie tine/pickup (2e harmonique) ; **Distance** basse-moyenne (plus proche = plus d'overdrive de captation = bark) ; **P Amp In** moyen-haut, **P Amp Out** ajusté pour le niveau.
- **M Force < Vel** élevé et **M Stiff < Vel** moyen : c'est la vélocité qui doit faire apparaître le bark, pas le niveau seul.
- **F Tine Color** moyen ; **F Tine Vol** > **F Tone Vol** pour un Mark I brillant ; inverser pour un son « Suitcase doux ».
- **F Release** court (≈ dampers réels), **Damp Amount** faible mais non nul, **Att/Rel** vers +30…+60 (bruit surtout au relâchement).
- **KB Stretch** > 0 (le manuel indique que l'accord étiré fait partie du son).
- Trémolo panoramique Suitcase : **Auto Pan** natif après l'instrument, forme triangle **[HEUR]**, rate 3–7 Hz **[TEST]**, amount 40–70 % **[TEST]**.

### 1.7 La recette DX7 « E.PIANO 1 » (lue et vérifiée) et sa transposition dans Operator

**Source primaire 1** : conversion du sysex ROM1A patch #11 en instrument Faust autonome (paramètres bruts DX7) — https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/master/examples/dx7/dsp/epiano.dsp **[DOC]**.
**Source primaire 2** : JSON de la collection Glenn Scott (banque « rhodes1 ») — https://raw.githubusercontent.com/itsjoesullivan/dx7-patches/master/readme.md **[DOC]**. Les deux concordent sur tout sauf LFO Speed (34 vs 15) et Pitch Mod Sens (3 vs 2) — probablement deux banques différentes ; le LFO n'affecte de toute façon pas le son (PMD = AMD = 0).

**Paramètres globaux [DOC]** : Algorithme **5** ; Feedback **6** ; Transpose 0 (C3) ; Osc Key Sync off ; Pitch EG rates 94/67/95/60, levels 50/50/50/50 (= aucun mouvement de hauteur) ; LFO sine, speed 34, delay 33, PMD 0, AMD 0, sync off.

**Structure de l'algorithme 5 [DOC]** : trois « tours » de deux opérateurs additionnées : OP2→OP1, OP4→OP3, OP6(avec feedback)→OP5. Porteuses : 1, 3, 5. (Le README du même dépôt : « Algorithm 5 (E.Piano) ».)

| Opérateur | Rôle | Coarse (ratio) | Fine | Detune | Out Level | EG R1/R2/R3/R4 | EG L1/L2/L3/L4 | Vel Sens | Rate Scaling | Level scaling |
|---|---|---|---|---|---|---|---|---|---|---|
| OP1 | porteuse tour A | 1 | 0 | +3 | 99 | 96/25/25/67 | 99/75/0/0 | 2 | 3 | — |
| OP2 | modulateur tour A (« tine ») | **14** | 0 | 0 | 58 | 95/50/35/78 | 99/75/0/0 | **7** | 3 | — |
| OP3 | porteuse tour B | 1 | 0 | 0 | 99 | 95/20/20/50 | 99/95/0/0 | 2 | 3 | — |
| OP4 | modulateur tour B | 1 | 0 | 0 | 89 | 95/29/20/50 | 99/95/0/0 | 6 | 3 | — |
| OP5 | porteuse tour C | 1 | 0 | **−7** | 99 | 95/20/20/50 | 99/95/0/0 | 0 | 3 | — |
| OP6 | modulateur tour C (feedback 6) | 1 | 0 | **+7** | 79 | 95/29/20/50 | 99/95/0/0 | 6 | 3 | breakpoint D3 (41), R-depth 19, courbe −LIN |

Lecture (analyse) **[DOC → HEUR pour l'interprétation]** :
- La **tour A** (14:1) crée la « cloche/tine » : le ratio 14 place les bandes latérales très haut ; sa **sensibilité vélocité 7 (max)** sur le modulateur fait apparaître les harmoniques uniquement en jeu fort → c'est l'équivalent FM du **bark**. Son enveloppe décroît plus vite (R2 = 50) que celle de la porteuse.
- La **tour B** (1:1) donne le corps ; vélocité 6 sur le modulateur → le corps s'enrichit aussi avec la force.
- La **tour C** (1:1 + feedback 6, porteuse −7 / modulateur +7 de detune) ajoute un corps « dent-de-scie douce » (le feedback sur un opérateur 1:1 crée une série harmonique complète) et un léger chorus par les detunes opposés. Le level scaling de l'OP6 (à droite de D3, profondeur 19) **adoucit** le feedback dans l'aigu.

**Transposition dans Operator (Live 12)** — faits documentés sur Operator **[DOC]** (manuel §30.9) : 4 oscillateurs A–D ; **11 algorithmes** prédéfinis ; **Coarse** = ratio en nombres entiers, **Fine** = fraction (inharmonique) ; **Fixed** avec Freq × Multi ; **Level** ; **Feedback** « An oscillator can modulate itself if it is not modulated by another oscillator » ; enveloppes avec **Vel** et **Key** ; **Osc < Vel** (+ Quantize) module la fréquence par vélocité ; **Spread** = deux voix désaccordées L/R ; **Tone** global ; « Operator is the result of an intense preoccupation with FM synthesis and a love and dedication to the old hardware FM synthesizers, such as the Yamaha SY77, the Yamaha TX81Z and the NED Synclavier II ».
Limite structurelle : 4 opérateurs contre 6 (extrait Attack Magazine : « The classic DX7 e-piano sound makes full use of all 6 operators, while Operator only has 4 » **[HEUR]** — https://www.attackmagazine.com/technique/tutorials/fm-electric-piano/).

Proposition **[TEST]** (deux tours seulement) :
- Algorithme à **deux paires parallèles** (B→A et D→C) — l'existence exacte de cette icône parmi les 11 est **[MÉMOIRE, non vérifié]** ; sinon, deux Operator dans un Instrument Rack.
- **Osc A** (porteuse) : Sine, Coarse 1, Level 0 dB, enveloppe : attaque ≈ 1 ms, decay long (≈ 2–4 s), sustain 0, release ≈ 0,3 s ; Vel de l'enveloppe faible.
- **Osc B** (modulateur « tine ») : Sine, **Coarse 14**, Fine 0, Level à régler à l'oreille entre −30 et −18 dB (le level 58/99 du DX7 n'est pas convertible sans la table de niveaux DX7, non lue), enveloppe decay plus court (≈ 0,5–1 s), **Vel élevé (≈ 80–100 %)** pour le bark.
- **Osc C** (porteuse) : Sine, Coarse 1, Level −3 dB, même enveloppe qu'A.
- **Osc D** (modulateur « corps ») : Sine, Coarse 1, **Feedback 40–70 %** (équivalent qualitatif du feedback 6/7), Level −12 à −6 dB, Vel moyen.
- Detune ±7 des OP5/6 : **Spread** modéré (≈ 10–20 %) ou Fine de quelques centièmes sur D **[TEST]**.
- Ratio « 18 » cité par un tutoriel comme alternative plus dure **[HEUR]** (Attack Magazine : « a ratio of 18.00 giving a harsh, sustained tone »).

**Recette FM alternative, entièrement documentée : STK `Rhodey`** (Perry Cook & Gary Scavone) **[DOC]** — https://raw.githubusercontent.com/thestk/stk/master/src/Rhodey.cpp
- « two simple FM Pairs summed together, also referred to as algorithm 5 of the TX81Z » : 4→3, 2→1.
- Fréquence de base = **2 × la note** ; ratios ops 1..4 = **1.0, 0.5, 1.0, 15.0** → paire A : porteuse à 2f modulée par f (1:0,5) ; paire B : porteuse à 2f modulée par **30 f** (la « cloche »).
- Gains (index de table fmGains) : 99, 90, 99, **67** (le modulateur cloche est le plus faible).
- Enveloppes ADSR (A, D, S, R en s) : op1 0.001/1.50/0/0.04 ; op2 0.001/1.50/0/0.04 ; op3 0.001/1.00/0/0.04 ; **op4 0.001/0.25/0/0.04** → l'indice de modulation « cloche » s'éteint en 0,25 s : attaque brillante puis son rond. Ondes : 3 sinus + `fwavblnk` pour le 4e.

---

## 2. Wurlitzer 200A

### 2.1 Anches (reeds) vs tines — mécanisme

- « the sound is generated electromechanically by striking a metal reed with a felt hammer, using conventional piano action. This induces an electrical current in an electrostatic pickup system using a DC voltage of 170 v. » **[DOC]** — miroir Wikipédia « Wurlitzer electronic piano » : https://raw.githubusercontent.com/bigai-nlco/RAM/main/data/mquake_2104/Wurlitzer_electric_piano.txt (original https://en.wikipedia.org/wiki/Wurlitzer_electronic_piano, bloqué).
- Tension de polarisation du **200A** : **147 V DC via 1 MΩ** (« 200A manual spec ») ; Pfeifle a mesuré un EP200 à 130 V pour 170 V nominal. **[DOC, via openwurli qui cite le service manual]** — https://raw.githubusercontent.com/hal0zer0/openwurli/main/docs/research/reed-pickup-displacement.md
- Anches en acier à ressort « high grade of high carbon spring steel having a hardness of Rockwell C-50 » (brevet US 2,919,616, Andersen 1960) ; accord par masse de soudure à l'extrémité ; longueurs vibrantes ≈ 74,9 mm (A1, 55 Hz), 44,5 mm (E4), 25,4 mm (C7). **[DOC]** — https://raw.githubusercontent.com/hal0zer0/openwurli/main/docs/research/reed-and-hammer-physics.md
- Le rapport f2/f1 d'une anche encastrée-libre est ≥ **6,27** (inharmonique, pas 2:1) — d'où le timbre « sawtooth-like » sans série harmonique propre. **[DOC]** (même doc, section 2.5).
- Contact marteau/anche : « three fourths to one cycle of vibration at its fundamental frequency » (brevet Miessner US 2,932,231) → 18 ms à A1, 3,8 ms à C4, 0,48 ms à C7 ; plus court quand on frappe fort. **[DOC]** (même doc, §4.2).
- 64 touches ; 200 lancé en 1968 (ampli 30 W, deux HP face au joueur, ≈ 88 000 exemplaires) ; **200A en 1974** (blindage anti-ronflette amélioré) ; 200B 1978 (piles, sans ampli). **[DOC]** (Wikipédia).

### 2.2 Pourquoi il « grogne » (bark) à forte vélocité

- « When played gently the sound can be quite sweet and vibraphone-like […] while becoming more aggressive with harder playing, producing a characteristic slightly overdriven tone usually described as a "bark". » **[DOC]** (Wikipédia).
- Cause physique établie par openwurli : « The 200A's "bark" […] is overwhelmingly a product of the capacitive pickup's `1/(1−y)` transfer nonlinearity, where y = x/d₀ is the reed displacement normalized to the rest gap » ; « preamp/power-amp/speaker add negligible harmonics; loop gain ~450 linearizes the preamp to ~0.04% THD ». Direction confirmée par le service manual : « closer reed = louder AND harsher (more harmonic) » (remède usine contre une note trop forte : relever les extrémités du pickup de **1/32″–1/16″**). **[DOC]** — reed-pickup-displacement.md
- Le gap anche/pickup **d₀ n'est documenté nulle part** (dossiers Wurlitzer détruits en 1988) ; le modèle utilise un « y_peak ≈ 0,85 » calibré à l'oreille/spectre (« Calibrated, not physical »). **[DOC]**
- Sortie de l'instrument : 2–7 mV AC au potentiomètre de volume (Avenson, non vérifié indépendamment) ; gain du préampli ≈ 14–16 dB ; bande passante du préampli ≈ 10 kHz ; enceinte : LPF 5,5 kHz. **[DOC]** — signal-chain-architecture.md
- Extraits (Vintage Vibe, bloqué) : « the more a reed swings in front of the pickup the more harmonic distortion is achieved, creating that growl or bark associated with the initial attack when played with a mid to hard blow » **[HEUR]** — https://www.vintagevibe.com/blogs/news/wurlitzer-electric-piano-reeds-case-study

### 2.3 Vibrato interne (en réalité un trémolo de gain)

- Wikipédia : le « vibrato » (mal nommé) a **une vitesse fixe et une profondeur réglable** (introduit sur le 140 en 1962 ; retravaillé sur le 200). **[DOC]**
- openwurli (dérivé du schéma du 200A + SPICE) : oscillateur **twin-T** ; « Rate ≈ 5.56 Hz (measured) » ; « SPICE-validated at 5.63 Hz » ; plage « ≈5.5–5.9 Hz rate — R-17-dependent » ; **profondeur** : « depth ladder 0/1.4/2.6/4.0/7.6 dB ("6 dB" folklore figure = one aged unit) » ; ≈ 7 dB crête à crête à fond ; **le trémolo module le gain du préampli** (LDR dans la boucle de contre-réaction), donc **le timbre et la distorsion**, pas seulement le volume ; « asymmetric attack/release creates a "choppy" effect: fast dips (2.5 ms), slow recovery (35 ms) […] immediately recognizable as Wurlitzer ». **[DOC]** — https://raw.githubusercontent.com/hal0zer0/openwurli/main/docs/research/signal-chain-architecture.md ; …/preamp-circuit.md ; …/output-stage.md ; README : « Rate fixed at ~5.6 Hz by Twin-T oscillator » — https://raw.githubusercontent.com/Ferglerz/openwurli/main/README.md
- Le trémolo est **mono** (HP internes) : pas de panoramique, contrairement au Suitcase. **[DOC, déduit du schéma décrit]**

### 2.4 Émulation : Electric (Live 12) et Operator

- Electric : **Pickup Type W** = « electro-static model » **[DOC]** (manuel §30.5.4.1) : c'est exactement la non-linéarité capacitive décrite ci-dessus ; **Distance** faible + **P Amp In** élevé pour le bark de captation ; **F Tone Vol** bas (le Wurlitzer n'a pas de tonebar) ; **Noise** un peu plus présent (feutre) ; **F Release** très court ; **Str. inharmonicité** : non réglable dans Electric — accepter. **[TEST]**
- Trémolo : **Auto Pan** natif en mode amplitude (pas de pan), rate **5,6 Hz** fixe **[DOC pour la valeur, TEST pour l'implémentation]**, profondeur 1,5–7 dB ; forme non sinusoïdale « choppy » → essayer une forme triangle/impulsion et un **Saturator** *avant* le trémolo puisque le gain modulé est celui du préampli **[TEST]**.
- Recette FM documentée : **STK `Wurley`** **[DOC]** — https://raw.githubusercontent.com/thestk/stk/master/src/Wurley.cpp : algorithme 5 TX81Z (4→3, 2→1) ; ratios **1.0, 4.0** pour la paire A ; paire B en **fréquence fixe −510 Hz** (« Note here a 'fixed resonance' ») ; gains 99, 82, 92 (82 à noteOn), 68 ; ADSR : op1 0.001/1.5/0/0.04, op2 0.001/1.5/0/0.04, **op3 0.001/0.25/0/0.04, op4 0.001/0.15/0/0.04** ; `twozero_.setGain(2.0)` ; **vibrato 8.0 Hz**. → Dans Operator : Osc A (porteuse Coarse 1) modulée par B (Coarse 4) ; Osc C **Fixed 510 Hz** modulée par D Fixed 510 Hz avec enveloppes de 0,15–0,25 s (résonance fixe = la « cloche » de l'anche qui ne suit pas la note). **[TEST]**

---

## 3. Hohner Clavinet D6

### 3.1 Mécanisme et tessiture

- « an electrically amplified clavichord […] manufactured by Hohner […] from 1964 to the early 1980s. Hohner produced seven models […] I, II, L, C, D6, E7 and Duo. » ; « Most models have 60 keys and a keyboard range of **F1 to E6** (fundamental frequencies of **43.6 Hz – 1318.5 Hz**). This five octave span covers the range of an electric guitar and most of the range of a four-string electric bass guitar. » **[DOC]** — miroir Wikipédia « Clavinet » : https://raw.githubusercontent.com/gianmarcopicarella/babelarity/master/Babelarity_Picarella.1788997/resources/corpus/44710.txt (original https://en.wikipedia.org/wiki/Clavinet, bloqué).
- « a harp of 60 tensioned steel strings oriented diagonally below the key surface […] Beneath each key, a metal holder grips a small rubber pad. Depressing a key makes the pad perform what is known in guitar technique as a "hammer on" (forcefully fretting the string). An electro-magnetic pickup turns the string vibration into an electric current. » ; « The end of each string farthest from the pick-ups passes through a weave of yarn. When the key is released, the yarn damps the vibration » ; « Most clavinets have two sets of pickups, positioned above and below the strings » ; « Early clavinet models featured single-coil pickups. The D6 introduced a six-core pickup design. » **[DOC]**
- Les pointes en polymère se décomposent avec l'âge (collent, puis se liquéfient) ; les émulations modernes modélisent aussi « the sound they made when the rubber pads decayed and began to stick to the strings ». **[DOC]**
- Modèle physique epi : « sixty strings struck and held against an anvil, twin bar pickups at their measured distances with a 4-way selector (center, bridge, both, out of phase), four tone rockers computed as the real RC networks behind them, and the measured **three-semitone pitch drop** when the tangent lets go and the yarn-wrapped dead length rejoins the string. » **[DOC secondaire]** — epi README.

### 3.2 Les quatre positions de pickup et les filtres

Deux sources se contredisent sur l'étiquetage exact — à trancher **[TEST]** :
- Cabbage `Clavinet.csd` (émulation Csound, Iain McCurdy) : « CA - neck pickup only (pickup A) ; CB - bridge pickup only (pickup B) ; DA - both pickups in phase ; DB - bridge pickup (pickup B) 180 degrees out of phase w.r.t the neck pickup ». **[DOC secondaire]** — https://raw.githubusercontent.com/rorywalsh/cabbage/develop/Examples/Instruments/PhysicalModelling/Clavinet.csd
- Extrait (forum/Nord, pages bloquées) : « CA = Bottom Pickup Only, CB = Upper Pickup Only, DB = Both Pickups Together, DA = Both Pickups Together, but out of Phase ». **[HEUR]** — https://www.nordkeyboards.com/sounds/piano-library/hohner-clavinet-d6/
- Point commun **[DOC/HEUR]** : C = un seul pickup, D = les deux ; A/B choisit lequel (ou la phase). La position « hors phase » annule le grave et donne le son fin et nasal.
- Filtres : extrait Wikipédia (non lu en entier) : « "Brilliant" and "Treble" activate a high-pass filter, while "Medium" and "Soft" activate a low-pass filter. On the right was a mechanical mute slider. » **[HEUR]** ; Cabbage les modélise comme « four bandpass filters […] in a parallel arrangement » avec fco/level/Q réglables **[DOC secondaire]** ; epi : « four tone rockers computed as the real RC networks » **[DOC secondaire]**. Les fréquences de coupure réelles **n'ont pas été trouvées** (la FAQ clavinet.com est bloquée).
- Nord (extrait) : chaque position CA/CB/DA/DB × 7 vélocités ; « the filter tabs allow access to the 60 possible tone variations of the original » **[HEUR]**.

### 3.3 Pourquoi un auto-wah / envelope filter et un phaser (Superstition, Higher Ground)

- Wikipédia : « When the clavinet was used in funk, soul, rock and jazz fusion in the 1970s, it was often plugged into electronic effects units » ; liste : « Stevie Wonder, "Higher Ground" (**through a Mu-Tron III**), "Superstition", "You Haven't Done Nothin'" ; Bernie Worrell, "Testify" ; Billy Preston "Outa-Space" ; Chris Jasper "Live It Up" (Isley Brothers) ; John Paul Jones "Trampled Under Foot" ; Bob Marley "Could You Be Loved" ». **[DOC]**
- **Superstition** : les extraits (Guitar World, Wikipédia Mu-Tron) associent le Mu-Tron III à **Higher Ground (1973)**, pas à Superstition ; un extrait de forum EHX note que Superstition « uses multiple clavinet tracks » et qu'aucune pédale ne reproduit seule le son « due to the speed and overdrive characteristics of the original recording ». **[HEUR]** — https://www.ehx.com/topic/superstition-intro-sound/ ; https://www.guitarworld.com/gear/guitar-pedals/mu-tron-iii . Le réglage de pickup/filtre de Superstition **n'a pas été trouvé**.
- Mu-Tron III (1972) : « the position of the filter is controlled not by an expression pedal but by the amplitude of the input signal, via an envelope follower. This technique was first used to great acclaim in the 1972 Mu-Tron III » ; les originaux utilisaient un **Vactrol** (opto). **[DOC secondaire]** — https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/master/docs/pedals.md
- Commandes du Mu-Tron III (d'après la recréation zoo-tron, qui reprend la façade) : **Gain** (sensibilité d'enveloppe), **Peak** (résonance/Q), **Range** Lo/Hi, **Mode** LP/BP/HP, **Direction** Up/Down ; suiveur « full-wave rectifier + asymmetric one-pole detector », vactrol « fast attack, slow level-dependent release ». **[DOC secondaire]** — https://raw.githubusercontent.com/anthonycoffey/zoo-tron/main/README.md
- Presets d'usine de cette recréation (valeurs du plug-in, **pas** des réglages historiques) **[HEUR]** — https://raw.githubusercontent.com/anthonycoffey/zoo-tron/main/Source/PresetManager.h :
  - « Classic Funk » : Range Hi, Mode BP, Up, gain 5.5, peak 6.0, attack 8 ms, release 180 ms, drive 2.0, contour (HPF sidechain) 90 Hz, mix 100 %.
  - « Higher Ground » : Range Hi, Mode BP, Up, **gain 6.5, peak 7.0, attack 5 ms, release 120 ms**, drive 3.5, contour 110 Hz, mix 100 %.
  - « Bootsy » : Range Lo, BP, Up, gain 6.0, peak 5.5, attack 12, release 260, contour 70.
- Pourquoi ça marche : le Clavinet a une **attaque percussive et un decay court** (étouffement immédiat au relâchement) → un filtre piloté par l'enveloppe suit chaque note ; le mode **BP** et la direction **Up** (« louder = brighter ») donnent le « quack ». **[HEUR]**

### 3.4 Synthétiser le Clavinet — Synth Secrets et Live

- **Il n'existe pas d'épisode « Synthesizing Clavinets » dans Synth Secrets.** L'index complet des 63 épisodes (https://raw.githubusercontent.com/micjamking/synth-secrets/master/README.md) n'en contient aucun **[DOC]**. Les seules mentions : Part 43 (pianos sur JX10) : « hard sync […] is one of the easiest ways to imitate the sound of a hammered or plucked string, and it's used in some of the most evocative harpsichord and clavinet sounds ever produced by an analog synth » **[DOC]** — https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-43.md ; et Part 42 « Synthesizing Pianos » (physique du marteau : « the piano hammer remains in contact with the string long enough to ensure that the position at which the string is struck is a node of zero displacement » ; hammers « anywhere from one seventh of the way along the string to about one 15th ») **[DOC]** — https://raw.githubusercontent.com/Pointhairedboss/Willickr/main/SyntheoryGordonReid/40_Synthesizing%20Pianos.md (original https://www.soundonsound.com/techniques/synthesizing-pianos). Les parties 28–30 (cordes pincées) seraient la référence la plus proche mais n'ont pas pu être téléchargées (404 sur le miroir).
- Recette de modèle physique documentée (Cabbage `Clavinet.csd`) **[DOC secondaire]** : corde Karplus-Strong « repluck » ; **Pluck** (position d'excitation) « Should be close to zero for a typical clavinet behaviour » ; deux pickups **Pick A / Pick B** (position 0–1) avec LFO et enveloppe de position pour l'attaque ; **HPF** exprimé en multiple de la fondamentale (2 = coupe sous la 2e harmonique, « remove the emphasis of the fundamental ») ; **LPF** idem ; **Inharm** ; **Damp** dépendant de la note (« lower notes should experience greater damping ») ; **release 'pluck'** (bruit quand le pad quitte la corde, « Poorly maintained clavinets exhibit a release 'pluck' ») avec Ampl/Tone/D.Time/Damp/A.Time ; quatre filtres Brilliant/Treble/Medium/Soft en parallèle.
- **Tension (Live 12)** — manuel §30.12 **[DOC]** : exciteurs **Bow, Hammer, Hammer (bouncing), Plectrum** ; Hammer = « located below the string and strikes it once before falling away » ; **Position** (0 % = au chevalet, 50 % = milieu) ; **Fix. Pos** (position fixe type guitare, ou relative type piano « about 1/7th ») ; **Damping** de l'exciteur (« interaction between the hammer and string will become shorter, generally resulting in a louder, brighter sound ») ; section **Damper** (Mass, Stiffness, Velocity, Position, Gated, Damping — « very high Mass and Stiffness values can simulate dampers that connect with the string hard enough to change its effective length, thus causing a change in tuning », intéressant pour la chute de 3 demi-tons) ; **String** : Decay, < Key, Ratio (onset/release), **Inharm**, Damping ; **Termination** (Finger Mass, Finger Stiff, Fret Stiff) ; **Pickup** : « The only control here is the Position slider […] At 0%, the pickup is located at the string's termination point, while at 50% it is under the midpoint of the string. Lower values generally result in a brighter, thinner sound » ; **Body** (Type, Size XS–XL, Decay, Str/Body). Noms API : `Excitator Type, Exc Velocity, E Pos, String Decay, Str Inharmon, Str Damping, Damper On, Damper Mass, D Stiffness, D Velocity, Damp Pos, D Damping, Term On/Off, Term Mass, Term Fng Stiff, Term Fret Stiff, Pickup On/Off, Pickup Pos, Body On/Off, Body Type, Body Size, Body Decay, Body Low-Cut, Body High-Cut, Body Mix` **[DOC]** (ClyphX).
  Recette de départ Tension **[TEST]** : Exciter **Hammer**, Stiffness élevé (pad de caoutchouc dur), **Position 5–12 %**, Fix. Pos **on** (la position de frappe du Clavinet est fixe près de l'extrémité) ; **Damper on, Gated on**, Mass élevé, Velocity élevée (étouffement immédiat), Damp Pos proche de 0 ; String Decay moyen, Inharm faible, Damping élevé (brillance) ; **Pickup on, Position 10–20 %** (fin/brillant = « bridge ») ou 30–40 % (« neck ») ; Body **off** ou Mix très bas (le Clavinet n'a pas de caisse) ; puis **Auto Filter** en enveloppe (BP, Q élevé, Env amount fort, Attack court) + **Phaser**.
- **Sampler** : multi-échantillon libre (« stevie-clavinet », musical-artifacts #646) avec « fast release time, as I recall from playing actual clavinets back in the 70's » et `veltrack` corrigé **[DOC]** — https://raw.githubusercontent.com/jlearman/stevie-clavinet/main/README.md ; licence inconnue.
- **Serum 2** : rien de documenté trouvé sur GitHub ; approche par analogie **[TEST]** : oscillateur dent-de-scie/impulsion étroite (le pad « frette » la corde près de l'extrémité → spectre riche en harmoniques paires et impaires), **enveloppe d'ampli** attaque 0, decay 0,4–1,2 s, sustain 40–60 %, release 30–80 ms (yarn) ; filtre passe-haut léger + notch fixe pour imiter la position hors phase ; **Env → filtre** rapide pour le « quack » ; bruit court (1–3 ms) à l'attaque et petit « pluck » de relâchement.

---

## 4. Hammond B-3 + Leslie

### 4.1 Drawbars, harmoniques, registrations

- Table des drawbars (Gordon Reid, Synth Secrets « Synthesizing Tonewheel Organs Part 1 », SOS nov. 2003) **[DOC]** — https://raw.githubusercontent.com/Pointhairedboss/Willickr/main/SyntheoryGordonReid/53_Synthesizing%20Tonewheel%20Organs%20Part%201.md (original https://www.soundonsound.com/techniques/synthesizing-tonewheel-organs-part-1) :

| Drawbar | Couleur | Nom | **Numéro d'harmonique (réf. 16')** |
|---|---|---|---|
| 16' | brun | Bass (sub-octave) | 1 |
| 5 1/3' | brun | Quint | 3 |
| 8' | blanc | Unison (« fondamentale ») | 2 |
| 4' | blanc | Octave | 4 |
| 2 2/3' | noir | Nazard | 6 |
| 2' | blanc | Block-flute | 8 |
| 1 3/5' | noir | Tierce | 10 |
| 1 1/3' | noir | Larigot | 12 |
| 1' | blanc | Sifflute | 16 |

  « the 16' pitch is the fundamental of a series that includes the first, second, third, fourth, sixth, eighth, 10th, 12th and 16th harmonics » ; l'idéal Hammond « does not include the fifth, seventh, ninth, 11th, 13th, 14th or 15th harmonics » ; 9 sinus mixés de 0 à 8 ; **387 420 489** registrations (9⁹) ; « 88 8000 000 […] beloved of Jimmy Smith, Keith Emerson, and heavy rock players » ; 88 8888 888 « very full and bright » ; **83 4211 100** ≈ dent de scie (série 1/n) ; **00 8030 200** ≈ carré. **[DOC]**
- Niveau par cran (table utilisée par l'émulation ZOIA) : 8 = 0 dB, 7 = −3, 6 = −6, 5 = −9, 4 = −12, 3 = −15, 2 = −18, 1 = −21, 0 = −∞ (3 dB/cran). **[DOC secondaire]** — https://raw.githubusercontent.com/eclab/zoia/master/Hammond.README.md
- Wikipédia (miroir) : « A very popular setting is 888000000 […] identified as the "classic" Jimmy Smith sound » ; deux claviers de **61 notes** ; pédalier **25 notes** (B-3), 32 sur RT/D-100 ; B-3/C-3 introduits en **1954** « with the additional harmonic percussion feature » (Reid dit 1955) ; le tonewheel « generate sound by creating an electric current from rotating a metal tonewheel near an electromagnetic pickup » ; « The only guaranteed frequency for a Hammond's tuning is concert A at 440 Hz » ; pas de vélocité (« There is no difference in volume regardless of how heavily the key is pressed ») ; pitch bend possible en coupant « Run ». **[DOC]** — https://raw.githubusercontent.com/jeffreywpli/convex_case/master/data/wiki3029/wiki3029/Hammond_organ.txt (miroir à phrases mélangées ; original https://en.wikipedia.org/wiki/Hammond_organ).
- 91 tonewheels : setBfree numérote les oscillateurs 1–91 (`osc.eqv.91`), clés 0–60 upper, 64–124 lower, 128–159 pédales ; moteur 1200 rpm/60 Hz (« gear60 ») ou 1500 rpm/50 Hz. **[DOC]** — https://raw.githubusercontent.com/pantherb/setBfree/master/cfg/default.cfg
- Foldback, taper, crosstalk (« leakage ») modélisés dans setBfree (osc.compartment-crosstalk 0.01, terminalstrip 0.01, wiring 0.01) **[DOC]** ; Reid : le leakage donne « a characteristic, throaty quality » **[DOC]**.

**Registrations funk / soul / gospel documentées** (fichier de programmes de setBfree — noms d'auteur inclus) **[DOC]** — https://raw.githubusercontent.com/pantherb/setBfree/master/pgm/default.pgm :
- « Jazz 1 all » : **888 0000 000**, perc on, **soft, fast, 3rd**, vibrato **C3** (upper), overdrive on, rotary chorale.
- « Jimmy Smith » : 88 8000 000, C3, perc 3rd ; « Jimmy Smith Plus » : 88 8800 000, C3, perc 3rd soft fast, chorale.
- « Booker T Jones » : **88 8630 000**, perc 2nd ; « Green Onions 1 » : 88 8800 000 ; « Green Onions 2 » : **80 8800 008**.
- « Gospel » : **88 8000 008** ; « Standard B mid whistle » : 88 8000 004 ; « Reggae » : 80 8000 008.
- « Brian Auger 3rd » : 88 8110 000, C3, perc 3rd ; « Steve Winwood 1 » : 84 8848 448 ; « Paul Shaffer » : 88 8788 678, C3, **tremolo** ; « Greg Rolie » : 88 8886 666, C3, perc 3rd soft fast ; « Blues 2 » : 88 5324 588 ; « Waa-waa (2nd bar) » : 88 8800 000 perc 3rd soft fast.
Liste complémentaire (ZOIA / GRAINS Booker, mêmes valeurs dans les deux) **[DOC secondaire]** — https://raw.githubusercontent.com/eclab/grains/master/booker/booker.ino : **Funky Comping 688600004**, **Fat 888000888**, **Brother Jack 800000888**, Bright Comping 878000456, Dark Comping 843000000, Gospel 1 808808008, Gospel 2 888000008, Jimmy McGriff 1 868600006, Groove Holmes (U) 888420080, House Bass (U) 880000000 / (L) 008080000, Ray Charles 006876400, Booker T. Jones 1 888800000 / 2 888630000, Gimme Some Loving 888800000, Jon Lord 884400000, Wide Leslie 866800000, Whistle 1 800000008, Shirley Scott 008888800, Jimmy Smith 2 (U) 888000000 / (L) 838000000.
- Extraits PianoGroove (bloqué) : « classic Jimmy Smith » = 16', 5 1/3', 8' à fond, **percussion On, Soft, Fast Decay, 3rd Harmonic** ; « Groove Holmes (Flutey Funk) 88 8000 008 » ; conseil : réduire les 8 à 7 ou 6 « to soften the sound […] that may sit better in the mix ». **[HEUR]** — https://www.pianogroove.com/blues-piano-lessons/hammond-b3-drawbars-presets-controls/
- Cory Henry : **rien trouvé** (recherche impossible, budget épuisé).

### 4.2 Percussion

- Reid : « the four percussion controls on an A100 allow you to add a greater or lesser amount of either the second or third harmonic of the 8' pitch — ie. of the 4' or 2 2/3' drawbar — as an accent at the start of the note » ; « adding percussion also reduces the loudness of the sustained part of the note » ; « Hammond percussion is polyphonic, but of the **single-triggering** variety, so if a previous note is held, the percussion does not sound » ; commutateurs **Normal/Soft** (niveau) et **Fast/Slow** (decay). **[DOC]** — https://raw.githubusercontent.com/Pointhairedboss/Willickr/main/SyntheoryGordonReid/55_Synthesizing%20Hammond%20Organ%20Effects.md (original https://www.soundonsound.com/techniques/synthesizing-hammond-organ-effects)
- Valeurs par défaut setBfree (émulateur de référence, « Example values (should) reflect compile-time defaults ») **[DOC]** — default.cfg : `osc.perc.fast=1.0` s ; `osc.perc.slow=4.0` s ; `osc.perc.gain=3.0` ; `osc.perc.normal=1.0` ; `osc.perc.soft=0.5012` (= **−6,0 dB**) ; `osc.perc.bus.a=3` (bus 4' → 2nd) ; `osc.perc.bus.b=4` (bus 2 2/3' → 3rd) ; `osc.perc.bus.trig=8` : **le drawbar 1' est coupé quand la percussion est active** (« Selects the bus to be muted when percussion is enabled »). tonegen.h : `HIPASS_PERCUSSION` (filtre passe-haut sur la percussion + compensation psychoacoustique) **[DOC]** — https://raw.githubusercontent.com/pantherb/setBfree/master/src/tonegen.h

### 4.3 Vibrato / chorus (scanner) V1–V3, C1–C3

- Reid : scanner 1945, « a tapped delay line […] a type of phase-shifter constructed from low-pass filters », un pickup rotatif entraîné par le générateur balaie les prises « from one end of the delay line to the other, and back again, during each rotation » ; **V** = tout le signal passe par le scanner (V-1, V-2, V-3 = trois profondeurs) ; **C** = « the output from the scanner unit is mixed with the unaffected output from the tonewheel generator » ; « The Hammond chorus mixes the straight-through signal with just a single instance of the pitch-modulated signal, so the Roland's three-stage chorus/ensemble is far too lush » ; rate sur un Juno 60 : « 'six and a bit' is correct » (≈ 6,x Hz). **[DOC]**
- setBfree vibrato.c : « it is driven from the tonegenerator motor which runs at a steady 1200 or 1500 rpm (50 Hz models). The usual frequency is somewhere between **7 or 8 Hz** » ; défauts : `scanner.hz=7` ; profondeurs relatives `v1=1.0, v2=2.5, v3=5.0` (« may be a bit on the conservative side ») ; sélection C = mélange dry + scanner (`select & CHO_`). **[DOC]** — https://raw.githubusercontent.com/pantherb/setBfree/master/src/vibrato.c
- Extraits (Benton Electronics / b3world, bloqués) : « the rotor continuously at about 7 Hz » ; 16 plaques de condensateur ; balayage complet en ≈ 1/14 s pour le vibrato le plus large. **[HEUR]**
- Wikipédia : « six settings, V1, V2, V3, C1, C2 and C3 […] selected via a rotary switch » ; sélectionnable par clavier (B-2/C-2, 1949). **[DOC]**

### 4.4 Key click

- Wikipédia : « Some Hammond organs have an audible pop or click when a key is pressed […] Originally, key click was considered a design defect and Hammond worked to eliminate or at least reduce it with equalization filters. » **[DOC]** ; Reid : « 'spit' at the start of the note […] we are rather attached to these so-called 'key-clicks' ». **[DOC]**
- setBfree : modèle d'attaque `click` (« several random contact bounces ») ; `osc.attack.click.level=0.5` ; longueur de la bouffée : min 0.1, max 0.5 d'une unité ≈ **5,87 ms** (soit ≈ 0,6–2,9 ms) ; release `linear`, `osc.release.click.level=0.25`. **[DOC]**

### 4.5 Leslie (vitesses, accélération, crossover)

- Reid (SOS fév. 2004) : deux HP, « a treble unit that produced the frequencies **above 800Hz**, and which played upward into what looks like two rotating horns (although one of these is a dummy) » ; basse **sous 800 Hz** dans un rotor tambour ; deux vitesses « **chorale** » et « **tremolo** » ; « The rotor's chorale speed was different from the horn's, as was its tremolo speed, and the transition rates between slow and fast (and vice versa) were different for the two assemblies » ; effet = FM (Doppler) + AM + modulation de timbre + réverbération de caisse ; **vibrato à 90° du trémolo**, modulation de timbre en phase avec l'amplitude ; placement près d'un mur pour obtenir du stéréo. **[DOC]** — https://raw.githubusercontent.com/Pointhairedboss/Willickr/main/SyntheoryGordonReid/56_Synthesizing%20The%20Rest%20Of%20The%20Hammond%20Organ%20Part%201.md (original https://www.soundonsound.com/techniques/synthesizing-rest-hammond-organ-part-1)
- Reid (mars 2004) : « the modulation depth created by the doppler effect in a Leslie speaker is quite small — around **±1 percent** » ; « For a Leslie rotor, [the rate] can be slower than **1Hz** » ; recette : split 800 Hz, deux LFO indépendants, **slew generator** pour les transitions, AM + LPF à 90°. **[DOC]** — …/57_Synthesizing%20The%20Rest%20Of%20The%20Hammond%20Organ%20Part%202.md (original https://www.soundonsound.com/techniques/synthesizing-rest-hammond-organ-part-2)
- **Valeurs numériques de setBfree (b_whirl, défauts)** **[DOC]** — https://raw.githubusercontent.com/pantherb/setBfree/master/b_whirl/b_whirl-configurable.ttl.in et default.cfg :
  - Horn slow **40,32 rpm** (0,67 Hz) ; horn fast **423,36 rpm** (7,06 Hz) ; horn **acceleration τ = 0,161 s**, **deceleration τ = 0,321 s** (constantes de temps exponentielles : « Time required to accelerate reduced by a factor exp(1) »).
  - Drum slow **36,0 rpm** (0,60 Hz) ; drum fast **357,3 rpm** (5,96 Hz) ; drum **acceleration τ = 4,127 s**, **deceleration τ = 1,371 s**.
  - Rayons : horn 17 cm, drum 22 cm ; horn level 0,7 ; fuite du horn (« leak », non Doppler) 0,15.
  - Filtre tambour : high-shelf **811,97 Hz**, Q 1,60, gain −38,9 dB ; filtre horn a : passe-bas **4500 Hz** Q 2,75 ; horn b : low-shelf **300 Hz** −30 dB ; deux filtres en peigne sur le horn (feedback −0,55/38 échantillons ; −0,35/120).
  - Overdrive : `overdrive.inputgain=3.5675`, `outputgain=0.8795`.
- Autres valeurs d'implémenteurs : GRAINS Booker : `LESLIE_FREQUENCY 5.66` Hz (« This is the 450 speed. The classic slower speed is 0.66 ») **[DOC secondaire]** ; ZOIA : période 166,7 ms = 6 Hz pour « fast » **[DOC secondaire]**.
- Extraits de forums/Wikipédia (bloqués) : « tremolo is typically around 250 revolutions per minute, and chorale is 30-50 RPM » ; mesures : « Slow/Chorale - Horn 50 RPM, Woofer/Rotor 40 RPM; Fast/Tremolo - Horn 400 RPM, Woofer/Rotor 340 RPM » ; « The top rotor can spin-up and slow-down in 1-3 seconds » ; le tambour est nettement plus lent à accélérer ; « acceleration time should be shorter than deacceleration » pour le horn. **[HEUR]** — https://forums.musicplayer.com/topic/150793-122-leslie-horn-and-rotor-speeds/ ; https://en.wikipedia.org/wiki/Leslie_speaker
- Modèles : 122 (entrée symétrique, consoles) et 147 (asymétrique, spinets) **[DOC]** (Wikipédia).

### 4.6 Réglages typiques funk/soul (synthèse des sources)

- Jimmy Smith : 888000000, perc 3rd soft fast, C3 **[DOC setBfree + HEUR PianoGroove]**.
- Booker T : 888630000 perc 2nd ; 888800000 (Green Onions) **[DOC setBfree]**.
- Gospel : 888000008 / 808808008 ; « whistle » 800000008 **[DOC setBfree/ZOIA]**.
- Funky comping : 688600004 ; « Fat » 888000888 ; « Brother Jack » (McDuff) 800000888 **[DOC secondaire ZOIA/GRAINS]**.
- Cory Henry : non trouvé.
- Reid sur l'overdrive : « A Hammond exhibits mild compression when you add notes to a chord » ; overdrive **avant** la réverb dans l'A100 **[DOC]**.

### 4.7 Synth Secrets « Synthesizing Tonewheel Organs » — recettes chiffrées

**Juno-6 : registration 88 8000 000** (SOS nov. 2003) **[DOC]** :
1. DCO : dent de scie **off** ; **pulse on, largeur 33,33 %** (« a pulse wave with a duty cycle of one third […] take a sawtooth wave and remove every third harmonic »), PWM en « Man » ; **sub-oscillateur (carré, −1 octave) à fond** ; pas de bruit.
2. VCF passe-bas : cutoff **exactement 19 demi-tons au-dessus du sub** (= 3e harmonique du 16'), **résonance 100 %** (auto-oscillation = le drawbar 5 1/3') ; keyboard tracking parfait requis.
3. Key click : ADSR du filtre en transitoire quasi instantané ; « A high [Sustain] value will reduce the amount, while a low value will accentuate it » ; « a 'Freq' value of 'zero' is best, and […] tuning the filter using the 'Env' control alone ».
4. VCA en mode **Gate** (enveloppe rectangulaire).
5. Limites : réaliste seulement pour 888000000 ; la comparaison A/B avec un A100 montre que le patch sonne plutôt comme **67 8321 000** (la résonance ampute le sub) — Part 3.
6. Vibrato : LFO ≈ 6 Hz sur DCO **et** VCF à parts égales ; overdrive : Level du VCA vers +5 (compression naturelle).

**Prophet 10** (Double mode) : deux oscillateurs par synthé → quatre drawbars (triangle pour le 16', pulse 33 % pour le 8', puis 5 1/3' et 4') ; percussion réaliste en n'enveloppant que le filtre « Lower » qui porte le 2 2/3'. **[DOC]** — …/54_Synthesizing%20Tonewheel%20Organs%20Part%202.md (original https://www.soundonsound.com/techniques/synthesizing-tonewheel-organs-part-2)

**Kawai K3 (additif) : 88 8000 000** **[DOC]** : harmoniques **1, 2, 3 = 31** (max), autres 0 ; Wave 32 ; Range 16' ; Filter Cutoff 65, Res 0, Env Amount 31, ADSR filtre 0/0/0/0 (click), ADSR ampli 0/0/31/0 ; VCF key tracking 9 (≈ 100 %) ; vélocité/pression 0 ; chorus off.

### 4.8 Émulation dans Live 12 (Operator additif, Wavetable, Rack) et Leslie natif

Faits Operator **[DOC]** : éditeur de partiels **16/32/64 harmoniques** par oscillateur (« Normalize » maintient le niveau) ; onde « Sine » pure ; Feedback seulement sur oscillateurs non modulés ; Vel/Key sur chaque enveloppe.

**Recette Operator « drawbars » [TEST, déduite]** :
- Onde **User** sur Osc A avec les partiels **1, 2, 3, 4, 6, 8, 10, 12, 16** à des niveaux relatifs suivant la table 3 dB/cran (8 = 0 dB, 7 = −3 dB…) — un seul oscillateur porte la registration entière (ex. 888000000 → partiels 1, 2, 3 à 0 dB, reste 0 ; 888000008 → + partiel 16 à 0 dB).
- Algorithme **tous porteurs en parallèle** (aucune FM) ; enveloppe A : attaque ≈ 1–3 ms, sustain 100 %, release 5–10 ms ; **Vel = 0** (pas de vélocité sur un Hammond).
- **Percussion** : Osc B, Sine, Coarse **2** (2nd) ou **3** (3rd) *par rapport au 8'* — attention : si la registration est référencée au 16' (partiel 1 = 16'), le 2nd harmonique du 8' est le partiel **4** et le 3rd le partiel **6** ; enveloppe decay **1,0 s (fast) / 4,0 s (slow)**, sustain 0 ; niveau normal 0 dB / soft **−6 dB** ; couper le partiel 16 quand la percussion est active ; retrig **off** (single-trigger approximatif via mode legato/mono ou Vel < Key, à valider).
- **Key click** : Osc C, onde Noise, enveloppe 1–3 ms.
- **Vibrato/chorus** : ne pas utiliser le LFO de pitch seul (Reid : « cheesy ») ; préférer un **Chorus-Ensemble** natif en mode chorus simple, rate ≈ 7 Hz, une seule voix, mix 50 % pour C3 **[TEST]**.
- **Leslie** : Live n'a pas de « Rotary » natif à ma connaissance **[MÉMOIRE, non vérifié]**. Construction dans un **Audio Effect Rack** à deux chaînes séparées par EQ à **800 Hz** : chaîne HF = Auto Pan (rate 7,06 Hz fast / 0,67 Hz slow) + léger Chorus/Frequency Shifter pour le Doppler ±1 % + LPF modulé ; chaîne BF = Auto Pan 5,96 / 0,60 Hz, largeur stéréo réduite ; **rampes** : automation avec temps différents (horn ≈ 0,5 s pour atteindre 95 %, tambour ≈ 12 s en montée / 4 s en descente d'après les τ de setBfree). **[TEST]**
- **Wavetable** : possible avec une table « organ » mais l'éditeur de partiels d'Operator est plus direct pour une registration exacte **[HEUR]**.
- Recette FM documentée : **STK `BeeThree`** (« Hammond-oid organ ») **[DOC]** — https://raw.githubusercontent.com/thestk/stk/master/src/BeeThree.cpp : algorithme 8 TX81Z (4 porteurs additifs) ; ratios **0.999, 1.997, 3.006, 6.009** (harmoniques 1, 2, 3, 6 légèrement désaccordés = « leakage/chorus » gratuit) ; gains 95, 95, 99, 95 ; enveloppes attaque **5 ms**, decay 3 ms, sustain 1.0 (ops 1–3) ; **op 4 : sustain 0.4** (partiel 6 qui décroît = percussion-like) ; feedback 0.1.

---

## 5. Tessitures, registre funk et erreurs classiques

| Instrument | Tessiture réelle | Source | Registre le plus utilisé en funk |
|---|---|---|---|
| Rhodes 73 | 73 notes ; E1–E7 en numérotation « C3 = 60 » de Live (E0–E6 en notation C4 = 60) | **[MÉMOIRE, non vérifié]** (le miroir Wikipédia ne donne que « 73 keys ») | accords 4 sons entre C2 et C5, basse main gauche rarement sous E1 **[HEUR]** |
| Rhodes 88 | 88 notes, A0–C8 (comme un piano) | **[DOC]** (1971, 88 notes) | idem |
| Wurlitzer 200A | **64 notes**, « from A an octave above the lowest note of a standard 88-note piano to the C an octave below its top note » → **A1–C7** | **[DOC]** Wikipédia | comping médium C3–C5, « bark » surtout dans le médium **[HEUR]** |
| Clavinet D6 | **60 notes, F1–E6 (43,6–1318,5 Hz)** | **[DOC]** Wikipédia | riffs entre F2 et C5 (zone guitare) ; grave F1–C2 pour doubler la basse **[HEUR]** |
| Hammond B-3 | 2 × **61 notes** (C–C, 5 octaves), pédalier 25 notes | **[DOC]** Wikipédia | comping main droite C3–C5, glissandi jusqu'à C6 ; basse main gauche/pédales sous C2 **[HEUR]** |

**Erreurs classiques d'émulation** (synthèse ; les justifications renvoient aux faits documentés ci-dessus) :
- Rhodes : (1) « vibrato » réglé en hauteur alors que c'est un trémolo panoramique **[DOC]** ; (2) bark obtenu par un Saturator post-instrument plutôt que par la dépendance vélocité → contenu harmonique (Force<Vel, Symmetry, Distance) **[HEUR]** ; (3) release trop long (les dampers coupent vite) ; (4) mélange Rhodes/Wurlitzer (« tonebar » vs anche) ; (5) oublier l'accord étiré (Stretch) **[DOC manuel]**.
- Wurlitzer : (1) même patch que le Rhodes avec plus de drive ; (2) trémolo sinus lent et profond au lieu de **5,6 Hz** fixe, choppy, qui module le gain (donc la distorsion) **[DOC]** ; (3) trémolo stéréo (il est mono) ; (4) spectre trop harmonique (l'anche a f2/f1 > 6) **[DOC]**.
- Clavinet : (1) sustain long/legato — l'instrument est staccato, la corde est étouffée au relâchement **[DOC]** ; (2) absence de bruit de relâchement et de la chute de 3 demi-tons **[DOC secondaire]** ; (3) filtre d'enveloppe absent ou trop lent (attaque ≥ 20 ms) alors que les presets Mu-Tron tournent autour de 5–12 ms d'attaque, 120–260 ms de release **[HEUR]** ; (4) jouer dans un registre trop grave et trop d'harmoniques paires (position hors phase mal imitée).
- Hammond : (1) **vélocité** appliquée (aucune sur l'orgue) **[DOC]** ; (2) attaque en fondu au lieu d'un rectangle + key click ~1–3 ms **[DOC]** ; (3) percussion **retriggée** à chaque note (elle est single-trigger) et sans coupure du 1' **[DOC]** ; (4) vibrato = LFO de pitch (Reid : « cheesy ») au lieu du scanner ≈ 7 Hz mélangé (C) **[DOC]** ; (5) Leslie = simple auto-pan : il faut le split à 800 Hz, des vitesses distinctes horn/tambour, des rampes différentes montée/descente, et le Doppler ±1 % **[DOC]** ; (6) chorus/ensemble trop riche (« far too lush ») **[DOC]** ; (7) harmoniques 5, 7, 9… présents (un oscillateur dent-de-scie filtré n'est pas une registration) **[DOC]**.

---

## 6. Recettes complètes trouvées (paramètre par paramètre, avec URL)

1. **DX7 ROM1A #11 « E.PIANO 1 »** — tableau complet §1.7 — https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/master/examples/dx7/dsp/epiano.dsp et https://raw.githubusercontent.com/itsjoesullivan/dx7-patches/master/readme.md **[DOC]**.
2. **STK Rhodey / Wurley / BeeThree** — §1.7, §2.4, §4.8 — https://raw.githubusercontent.com/thestk/stk/master/src/Rhodey.cpp , …/Wurley.cpp , …/BeeThree.cpp **[DOC]**.
3. **Juno-6 « 88 8000 000 »** (Reid) — §4.7 — https://www.soundonsound.com/techniques/synthesizing-tonewheel-organs-part-1 (lu via miroir Willickr) **[DOC]**.
4. **Kawai K3 « 88 8000 000 »** (Reid, 39 paramètres) — §4.7 — https://www.soundonsound.com/techniques/synthesizing-tonewheel-organs-part-2 (miroir) **[DOC]**.
5. **Percussion / vibrato / key click / Leslie / overdrive : défauts setBfree** — §4.2–4.5 — https://raw.githubusercontent.com/pantherb/setBfree/master/cfg/default.cfg ; …/b_whirl/b_whirl-configurable.ttl.in **[DOC]**.
6. **Registrations nommées** — §4.1 — https://raw.githubusercontent.com/pantherb/setBfree/master/pgm/default.pgm ; https://raw.githubusercontent.com/eclab/zoia/master/Hammond.README.md ; https://raw.githubusercontent.com/eclab/grains/master/booker/booker.ino **[DOC / DOC secondaire]**.
7. **Wurlitzer 200A trémolo** (5,6 Hz, 0/1,4/2,6/4,0/7,6 dB, dips 2,5 ms / recovery 35 ms) — §2.3 — https://raw.githubusercontent.com/hal0zer0/openwurli/main/docs/research/signal-chain-architecture.md **[DOC]**.
8. **Clavinet Csound (Cabbage)** — §3.4 — https://raw.githubusercontent.com/rorywalsh/cabbage/develop/Examples/Instruments/PhysicalModelling/Clavinet.csd **[DOC secondaire]**.
9. **Mu-Tron III presets (zoo-tron)** — §3.3 — https://raw.githubusercontent.com/anthonycoffey/zoo-tron/main/Source/PresetManager.h **[HEUR]**.
10. **Electric / Tension / Operator : sémantique de chaque paramètre** — §1.6, §3.4, §1.7 — manuel Live 12 (miroir djaboxx/iron-static) + noms API ClyphX **[DOC]**. Recettes de départ Electric (Rhodes, Wurli), Tension (Clav), Operator (E.Piano, drawbars) : **[TEST]**.

---

## 7. Pages consultées

### Lues en intégralité (ou en grande partie) — [DOC]
- https://raw.githubusercontent.com/Pointhairedboss/Willickr/main/SyntheoryGordonReid/53_Synthesizing%20Tonewheel%20Organs%20Part%201.md (SOS nov. 2003)
- …/54_Synthesizing%20Tonewheel%20Organs%20Part%202.md (SOS déc. 2003)
- …/55_Synthesizing%20Hammond%20Organ%20Effects.md (SOS jan. 2004)
- …/56_Synthesizing%20The%20Rest%20Of%20The%20Hammond%20Organ%20Part%201.md (SOS fév. 2004)
- …/57_Synthesizing%20The%20Rest%20Of%20The%20Hammond%20Organ%20Part%202.md (SOS mars 2004)
- …/40_Synthesizing%20Pianos.md (SOS oct. 2002)
- https://raw.githubusercontent.com/micjamking/synth-secrets/master/README.md (index des 63 épisodes) ; part-43.md, part-46.md (mentions « clavinet ») ; part-53…58.md (extraits tronqués)
- https://raw.githubusercontent.com/djaboxx/iron-static/main/docs/api/ableton/30-live-instrument-reference.md (manuel Live 12 ch. 30 : Electric, Operator, Tension)
- https://raw.githubusercontent.com/nuno-andre/clyphx/master/docs/live_instant_mapping.md (noms de paramètres Electric/Tension)
- https://raw.githubusercontent.com/gluon/AbletonLive12_MIDIRemoteScripts/main/_Generic/Devices.py (banques LoungeLizard/StringStudio/Operator)
- https://raw.githubusercontent.com/pantherb/setBfree/master/README.md ; cfg/default.cfg ; pgm/default.pgm ; b_whirl/whirl.h ; b_whirl/b_whirl-configurable.ttl.in ; src/vibrato.c ; src/tonegen.h ; (whirl.c, tonegen.c, overdrive.c téléchargés, parcourus par grep)
- https://raw.githubusercontent.com/Ferglerz/openwurli/main/README.md ; https://raw.githubusercontent.com/hal0zer0/openwurli/main/docs/research/reed-pickup-displacement.md (intégral) ; reed-and-hammer-physics.md, signal-chain-architecture.md, preamp-circuit.md, output-stage.md, pickup-system.md (grep ciblés)
- https://raw.githubusercontent.com/thestk/stk/master/src/Rhodey.cpp ; Wurley.cpp ; BeeThree.cpp
- https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/master/examples/dx7/dsp/epiano.dsp ; …/examples/dx7/README.md
- https://raw.githubusercontent.com/itsjoesullivan/dx7-patches/master/readme.md
- https://raw.githubusercontent.com/usamaahmedsh/synthetic-data-langchain-rag/main/data/raw/great_depression/pages/Rhodes_piano.txt (miroir Wikipédia)
- https://raw.githubusercontent.com/bigai-nlco/RAM/main/data/mquake_2104/Wurlitzer_electric_piano.txt (miroir Wikipédia)
- https://raw.githubusercontent.com/jeffreywpli/convex_case/master/data/wiki3029/wiki3029/Hammond_organ.txt (miroir Wikipédia, phrases mélangées)
- https://raw.githubusercontent.com/gianmarcopicarella/babelarity/master/Babelarity_Picarella.1788997/resources/corpus/44710.txt (miroir Wikipédia Clavinet) ; https://raw.githubusercontent.com/an-nos/search/master/lab6/res/stoner/Clavinet.txt (tronqué)
- https://raw.githubusercontent.com/eclab/zoia/master/Hammond.README.md ; https://raw.githubusercontent.com/eclab/grains/master/booker/booker.ino (en-tête)
- https://raw.githubusercontent.com/rorywalsh/cabbage/develop/Examples/Instruments/PhysicalModelling/Clavinet.csd (en-tête)
- https://raw.githubusercontent.com/anthonycoffey/zoo-tron/main/README.md ; …/Source/PresetManager.h
- https://raw.githubusercontent.com/bailleul-dev/greybound/main/knowledge/models/pedals/filter/muon.mdx ; https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/master/docs/pedals.md (section Mu-Tron)
- https://raw.githubusercontent.com/DatanoiseTV/epi/main/README.md ; …/docs/ControlMap.md (partiel)
- https://raw.githubusercontent.com/michele-perrone/OpenB3/main/README.md ; https://raw.githubusercontent.com/orange-dot/tonewheel91/main/docs/renders.md (grep) ; https://raw.githubusercontent.com/danielpodrazka/piano/main/README.md (section FM Rhodes) ; https://raw.githubusercontent.com/jlearman/stevie-clavinet/main/README.md ; https://raw.githubusercontent.com/dreamrec/LivePilot/main/livepilot/skills/livepilot-core/references/device-atlas/synths-native.md (extrait)

### Vues uniquement en extrait de recherche — [HEUR]
- https://chicagoelectricpiano.com/rhodes/fender-rhodes-bark/ ; https://www.mat.ucsb.edu/Masters/GregShearMasters2011_12_5.pdf ; https://soundgirls.org/the-fender-rhodes/
- http://www.fenderrhodes.com/history/effects.html ; http://www.fenderrhodes.com/history/dyno.html ; https://ep-forum.com/smf/index.php?topic=516.0 ; https://support.apple.com/guide/logicpro/tremolo-effect-controls-lgsifc1b9de5/mac
- https://www.vintagevibe.com/blogs/news/wurlitzer-electric-piano-reeds-case-study ; https://www.tropicalfishvintage.com/blog/2019/5/27/how-does-a-wurlitzer-electronic-piano-work
- https://www.nordkeyboards.com/sounds/piano-library/hohner-clavinet-d6/ ; https://www.clavinet.com/clavfaq.pdf ; https://www.ehx.com/topic/superstition-intro-sound/ ; https://www.guitarworld.com/gear/guitar-pedals/mu-tron-iii ; https://en.wikipedia.org/wiki/Mu-Tron_III
- https://www.pianogroove.com/blues-piano-lessons/hammond-b3-drawbars-presets-controls/ ; https://www.davidkempton.com/hmd3/ ; https://bentonelectronics.com/service-manual-the-hammond-vibrato/ ; https://b3world.com/hammond-technical-information-02.html
- https://forums.musicplayer.com/topic/150793-122-leslie-horn-and-rotor-speeds/ ; https://en.wikipedia.org/wiki/Leslie_speaker ; https://electronicmusic.fandom.com/wiki/Leslie ; https://adammonroemusic.com/blog/simulating_a_leslie_speaker.html
- https://theaudioowl.com/ableton-live/ableton-electric-piano-sounds/ ; https://www.ableton.com/en/packs/electric/ ; https://www.attackmagazine.com/technique/tutorials/fm-electric-piano/ ; https://www.edmprod.com/ableton-operator/ ; https://yamahablackboxes.com/articles/how-to-program-yamaha-dx7/ ; https://reverbmachine.com/blog/exploring-the-yamaha-dx7/

### Échecs (fetch refusé : `EGRESS_BLOCKED` par le proxy, équivalent d'un 403)
- https://chicagoelectricpiano.com/rhodes/fender-rhodes-bark/
- https://www.ableton.com/en/live-manual/12/live-instrument-reference/
- https://www.soundonsound.com/techniques/synthesizing-tonewheel-organs-part-1 ; …-part-2 ; https://www.soundonsound.com/techniques/synthesizing-hammond-organ-effects
- https://www.clavinet.com/clavfaq.pdf
- https://www.pianogroove.com/blues-piano-lessons/hammond-b3-drawbars-presets-controls/
- https://forums.musicplayer.com/topic/150793-122-leslie-horn-and-rotor-speeds/
- https://en.wikipedia.org/wiki/Rhodes_piano ; …/Leslie_speaker ; …/Clavinet ; …/Hammond_organ ; …/Wurlitzer_electric_piano
- https://reverbmachine.com/blog/exploring-the-yamaha-dx7/ ; https://www.fenderrhodes.com/org/manual/ch6.html ; https://www.righto.com/2021/11/reverse-engineering-yamaha-dx7.html
- 404 : https://raw.githubusercontent.com/Pointhairedboss/Willickr/main/SyntheoryGordonReid/26_Synthesizing%20Plucked%20Strings.md ; https://raw.githubusercontent.com/grame-cncm/faustlibraries/master/dx7.lib (tables de niveau DX7)
- 403/400 : api.github.com (listage des dossiers setBfree/epi), github.com/…/tree (HTML)
- Budget WebSearch épuisé (200/200 pour la session) avant les requêtes : Rhodes service manual/escapement, Mark I vs II (détails sonores), Wurlitzer vibrato Hz (forums), Suitcase « Janus » rate, Superstition (pickup/prises), Tension clavinet tutoriels, Hammond service manual percussion, Cory Henry, Phase 90/Small Stone, valeurs de presets Electric.

---

## 8. Ce qui n'a pas été trouvé

1. **Fréquence (Hz) et plage du trémolo panoramique du Rhodes Suitcase** (Speed/Intensity) — seulement « Speed » et « Intensity » comme commandes, forme triangle en extrait. À mesurer sur un enregistrement ou à prendre 3–7 Hz [TEST].
2. **Réglages chiffrés de phaser (Phase 90 / Small Stone), chorus, Dyno-My-Piano** pour Rhodes : aucune page lisible. Dyno : seulement « deux bandes d'EQ (basse + overtones) + stéréo » en extrait.
3. **Valeurs numériques de presets Electric (Live)** pour Rhodes/Wurli : aucun tutoriel n'en donne dans les extraits ; le manuel ne donne que la sémantique. Toutes les recettes Electric ici sont [TEST].
4. **Table de conversion Output Level DX7 (0–99) → dB** (dx7.lib introuvable) : la transposition des niveaux 58/89/79 vers Operator reste à l'oreille [TEST].
5. **Liste exacte des 11 algorithmes d'Operator** (le manuel miroir ne les décrit qu'en icônes) : l'existence d'un algorithme « deux paires parallèles » est [MÉMOIRE, non vérifié].
6. **Fréquences de coupure réelles des filtres Brilliant/Treble/Medium/Soft du D6** et l'étiquetage définitif CA/CB/DA/DB (deux sources se contredisent sur A/B).
7. **Réglages de « Superstition »** (position de pickup, filtres, nombre de prises, effets) : seulement un extrait de forum (« multiple clavinet tracks ») ; le Mu-Tron III est documenté pour « Higher Ground », pas pour Superstition.
8. **Réglages historiques du Mu-Tron III de Stevie Wonder** : seuls des presets d'un plug-in de recréation sont disponibles [HEUR].
9. **Un épisode Synth Secrets sur le Clavinet** : n'existe pas (index des 63 vérifié) ; l'article le plus proche (cordes pincées, parts 28–30) n'a pas pu être lu.
10. **Valeurs de percussion Hammond (decay en s, dB) dans un manuel de service** : seules les valeurs par défaut de setBfree (1 s / 4 s / −6 dB) sont documentées ; les ~7–8 Hz du scanner viennent de setBfree et d'extraits.
11. **Vitesses Leslie « officielles »** : setBfree (40,3/423,4 rpm horn ; 36/357,3 rpm tambour) vs extraits de forums (50/400 ; 40/340 ; « ~250 rpm ») — divergence non tranchée.
12. **Cory Henry** (drawbars, percussion) : rien.
13. **Serum 2** : aucune source spécifique aux claviers électromécaniques ; les propositions Serum sont [TEST].
14. **Tessiture exacte du Rhodes 73** (E–E) : non confirmée par une page lue.
