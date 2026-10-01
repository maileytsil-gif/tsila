---
titre: "Rapport de recherche — Axe F2 : synthés du funk historique 1972-1995 (Minimoog, ARP, talkbox, Oberheim, DX7, G-funk)"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: synth funk historique
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Axe F2 — Synthés du funk historique (1972-1995) : rapport de recherche

Rapport destiné au skill « sound design des synthés et claviers du funk moderne » (Ableton Live 12 + Serum 2). Date : 2026-09-24.

## 0. Conditions réelles de la recherche et convention de tags

**Contrainte majeure rencontrée.** Le proxy réseau de cette session bloque tous les domaines sauf `github.com` et `raw.githubusercontent.com`. Chaque tentative de lecture (WebFetch) vers reverbmachine.com, reverb.com, attackmagazine.com, syntorial.com, musicradar.com, synthtopia.com, soundonsound.com, wikipedia.org, kvraudio.com, gearspace.com, vintagesynth.com, guitarcloud.org, ehx.com, ableton.com, moogmusic.com, xferrecords.com, archive.org, medium.com, blogspot.com, etc. a échoué avec `EGRESS_BLOCKED` (liste complète en section 8). Le moteur WebSearch, lui, fonctionnait et renvoie des extraits de pages assez longs ; son budget de session (200 requêtes) s'est épuisé pendant ce travail.

Conséquence honnête : **aucune des pages web « grand public » (Reverb Machine, Attack, Syntorial, MusicRadar, SOS) n'a pu être lue intégralement**. Ce qui a pu être **réellement lu** : des sources primaires hébergées sur GitHub (données sysex des cartouches ROM DX7, code source Dexed, un miroir texte du manuel Ableton Live) et le corpus local du dépôt (Synth Secrets, fiches Operator/Serum 2 du skill). Les recettes de Reverb/Attack/MusicRadar proviennent des extraits renvoyés par le moteur de recherche, souvent précis au paramètre près, mais non vérifiés sur la page d'origine.

Convention de tags utilisée ci-dessous (plus fine que le modèle DOC/HEUR/TEST, pour ne rien surqualifier) :

- **[DOC]** : fait tiré d'une source primaire ou constructeur **réellement lue intégralement** (fichier sysex Yamaha, code source, manuel Ableton en miroir, corpus local).
- **[EXTR]** : fait tiré d'un **extrait de résultat de recherche** citant une page identifiée ; la page elle-même n'a pas pu être ouverte. À promouvoir en [DOC] après lecture de la page depuis un réseau non filtré, ou à garder comme plage de départ.
- **[HEUR]** : plage de départ issue d'un tutoriel, d'une recette de tiers ou de la pratique.
- **[TEST]** : à valider dans le Set.
- **[MÉMOIRE, non vérifié]** : de ma mémoire, sans page lue.

---

## 1. Synth bass Minimoog du P-Funk et de la Motown/Epic (Flash Light, Boogie On Reggae Woman, Thriller, Superstition)

### 1.1 Faits documentés

**« Flash Light » (Parliament, 1977, album Funkentelechy vs. the Placebo Syndrome)**

- La ligne de basse est jouée au **Minimoog** par **Bernie Worrell**, sur **au moins trois, peut-être quatre Minimoog reliés** ensemble. [EXTR] — Wikipedia « Flash Light (song) » : https://en.wikipedia.org/wiki/Flash_Light_(song) ; Reverb « The Essential Gear of Parliament-Funkadelic » : https://reverb.com/news/the-essential-gear-of-parliament-slash-funkadelic ; zZounds « Legends Series: Parliament-Funkadelic » : https://www.zzounds.com/lp/legends-parliament-funkadelic/530 (« three or four Minimoogs chained together »).
- Un README GitHub lu intégralement cite une interview de Worrell (powmag.net) : « Bernie Worrell recalled building Parliament's 'Flash Light' bass line from **three Minimoogs layered together** ». [DOC pour la citation du README, la source powmag elle-même n'a pas été lue] — https://raw.githubusercontent.com/keunwoochoi/subtractive-synthesizers.js/HEAD/README.md
- Description NYT reprise par Wikipedia : « descending and ascending chromatic line with a meaty tone and a certain swagger ». [EXTR] — même URL Wikipedia.
- Worrell « jouait le synthé » : il construisait et modifiait ses patches en temps réel sur scène. [EXTR] — Reverb « Video: The Synth Sounds of Parliament-Funkadelic's Bernie Worrell » : https://reverb.com/news/video-the-synth-sounds-of-parliament-funkadelics-bernie-worrell
- Citation attribuée à Worrell dans un extrait (page d'origine probable : interview MusicRadar) : « I told Bob Moog, they sent one of his technicians; the new stuff still isn't as fat, got the meat, like the old ones ». [EXTR, attribution de page incertaine] — https://www.musicradar.com/news/tech/bernie-worrell-talks-vintage-synths-elp-parliament-funkadelic-talking-heads-and-more-576154

**« Boogie On Reggae Woman » (Stevie Wonder, 1974, Fulfillingness' First Finale)**

- Basse jouée par Stevie Wonder sur **un Moog**, son créé avec Robert Margouleff et Malcolm Cecil (TONTO). Citation de Wonder : « it started with a Moog synthesizer », « had Bob and Malcolm come up with a bass sound I wanted ». [EXTR] — MusicRadar : https://www.musicradar.com/artists/the-groove-was-a-kind-of-blues-groove-and-i-think-i-drank-a-beer-because-i-wanted-to-have-a-kind-of-slurring-sound-in-my-voice-stevie-wonder-reveals-how-he-recorded-the-classic-moog-synth-bassline-and-laidback-vocals-on-boogie-on-reggae-woman
- Débat non tranché : Moog modulaire (TONTO) ou Minimoog. [EXTR] — KVR : https://www.kvraudio.com/forum/viewtopic.php?t=191274 ; Wikipedia : https://en.wikipedia.org/wiki/Boogie_On_Reggae_Woman (« pulsating Moog synthesizer bassline »).
- **Aucune recette chiffrée trouvée** pour ce titre précis (voir section 9).

**« Thriller » (Michael Jackson, 1982) — contradiction entre sources**

- Anthony Marinelli (programmeur sur l'album) affirme que l'ostinato de synth bass du titre « Thriller » a été joué sur **son ARP 2600 (Tonus)**. [EXTR] — Wikipedia « Thriller (song) » : https://en.wikipedia.org/wiki/Thriller_(song)
- L'article Wikipedia de l'album attribue les synth bass de « Thriller », « P.Y.T. » et « Wanna Be Startin' Somethin' » à **deux Minimoog modifiés par Richie Walbourn, côte à côte**, joués par Michael Boddicker, avec la « special multiple-mono compression » de Bruce Swedien. [EXTR] — https://en.wikipedia.org/wiki/Michael_Boddicker et https://equipboard.com/albums/michael-jackson-thriller
- « Billie Jean » : accords au **Yamaha CS-80**, basse **Minimoog** qui entre avec les accords ; paternité disputée entre Boddicker et Bill Wolfer. [EXTR] — https://forum.vintagesynth.com/viewtopic.php?t=33273
- Pour le skill : documenter les deux versions (ARP 2600 vs Minimoog ×2) et ne pas trancher. Le résultat sonore recherché est de toute façon « mono, deux oscillateurs, filtre passe-bas résonant, decay court ».

**« Superstition » (Stevie Wonder, 1972, Talking Book) — Clavinet, pas synthé**

- Riff joué sur un **Hohner Clavinet** (un extrait dit « Model C » ; la tradition dit D6 — [MÉMOIRE, non vérifié] pour le D6). Enregistré à Electric Lady, été 1972. [EXTR] — Wikipedia : https://en.wikipedia.org/wiki/Superstition_(song)
- Chaîne d'effets (Margouleff/Cecil) : « all kinds of funny guitar boxes. We had the **Mutron 5 phaser**, we had **wah wah pedals** and all kinds of **distortion boxes** coming out of the clavinet ». Ordre d'enregistrement : batterie d'abord, puis basse clavier, puis Clavinet. [EXTR] — WSDG/Pro Sound News : https://wsdg.com/pro-sound-news-behind-the-magic-recording-stevie-wonders-superstition/
- Pour Live 12 : le Clavinet n'est pas un synthé ; renvoyer vers Electric (le skill local documente `CHORDS Electric (LoungeLizard)` dans `.claude/skills/vst-sound-design/references/instruments-natifs.md`, ligne 7) ou un sample, puis Auto Filter en mode envelope follower + Phaser. [TEST]

### 1.2 Spécifications du Minimoog Model D utiles pour transposer (manuel Moog)

Valeurs issues de l'extrait de recherche pointant vers le PDF officiel du manuel (non ouvert, domaine bloqué) : [EXTR] — https://cdn.inmusicbrands.com/Moog/Model%20D/Minimoog_Model_D_Manual.pdf

- Attack Time : **1 ms à 10 s**.
- Decay Time : **4 ms à > 35 s** (un ancien service manual indiquait 10 ms à 10 s).
- Sustain Level : 0 à 100 % du pic de contour.
- Filter Contour (plage de balayage de l'enveloppe de filtre) : **0 à 4 octaves**.
- Glide : **1 ms à 1 s par octave**.
- Rappel d'architecture [DOC, corpus local Synth Secrets 8, `corpus/synth-secrets/synth-secrets-08.md` ligne 46] : les contour generators du Minimoog sont des **ADSD** — « the Release time equals the Decay time, or is zero » (interrupteur Decay). C'est pourquoi les recettes parlent de « Decay switch on » : le release = la valeur de decay.

### 1.3 Recettes trouvées pour « Flash Light », paramètre par paramètre

**Recette A — Reverb (vidéo Bernie Worrell), sur Minimoog Model D** [EXTR] — https://reverb.com/news/video-the-synth-sounds-of-parliament-funkadelics-bernie-worrell

- Osc 1 : **32'**, **sawtooth**.
- Osc 2 : **16'**, **sawtooth**, hauteur « légèrement montée » pour épaissir (désaccord positif, valeur non chiffrée).
- Osc 3 : **Lo** (mode LFO), **triangle**, hauteur « environ +5 » ; section Controllers : source **Osc 3 + LFO**, interrupteur **Oscillator Modulation ON** (vibrato/wobble pilotable à la molette).
- Filtre : **Cutoff Frequency ≈ +2** (échelle Moog −5…+5). Emphasis, Amount of Contour et enveloppes non présents dans l'extrait.
- Le « jeu » (pitch bend, molette de modulation, glide) fait « une grande partie du son ».

**Recette B — Attack Magazine « How To Remake 'Flash Light' », dans Ableton Wavetable** [EXTR] — https://www.attackmagazine.com/technique/synth-secrets/how-to-remake-flash-light-by-parliament/

- Osc 1 : **sawtooth**, position de table **40 %**.
- Voicing **Mono**, **glide 45 ms**.
- Osc 2 : **square**, position **100 %**, Effect **Modern**, **Warp −25 %** (modifie la largeur d'impulsion), **Semi −12** (une octave en dessous).
- Enveloppe d'ampli : **release 15-20 ms** pour une basse plus serrée.
- Filtre/résonance/enveloppe de filtre : absents de l'extrait (page non lue).

**Recette C — document de recherche GitHub (cours IDM, Ableton Analog), lu intégralement** [HEUR, auteur tiers ; il cite Reverb et Wikipedia] — https://raw.githubusercontent.com/ZacharySBrown/idm-course/HEAD/specs/ableton_course_ep2_analog_research.md

- Voices = 1, Glide = Prop, Legato on.
- OSC1 saw, OSC2 saw désaccordée **±12 cents**, Sub on.
- Filter 1 LP 24 dB, **cutoff ≈ 800 Hz, résonance ≈ 35 %**.
- Enveloppe de filtre : **Decay 80 ms, Sustain 0**.
- Pitch bend range 12 demi-tons (articulation « drop and recover » à la molette).
- Enveloppe d'ampli : attaque 200 ms (valeur douteuse pour une basse funk, à ne pas reprendre telle quelle) [TEST].
- Astuce VA : ajouter 5-8 cents d'« Error » par voix pour imiter la dérive de plusieurs unités.

**Recette D — Minimoog bass générique (MusicRadar « Master the Minimoog Model D »)** [EXTR] — https://www.musicradar.com/news/master-the-minimoog-model-d-create-classic-bass

- Osc A : saw, **−24 demi-tons (32')** ; Osc B : square, **−12 (16')** ; Osc C : même forme et accord que B ; B et C désaccordés en sens opposés d'**environ 10 cents** chacun ; B et C légèrement moins forts que A.
- Filtre « LP 24 dB Rich » (approximation du ladder), **cutoff ≈ 120 Hz**, **résonance 25 %**.

**Recette E — extrait Reverb « 5 Classic Minimoog Model D sounds » (patch non identifié dans l'extrait, probablement Thriller)** [EXTR, attribution au morceau incertaine] — https://reverb.com/news/video-the-synth-sounds-of-5-classic-minimoog-tracks

- Filtre : **Cutoff 0, Emphasis 3, Contour 5**.
- Les deux enveloppes : attaque rapide, **decay 600 ms**, **sustain à fond** ; **Glide off**, **interrupteur Decay on**.

### 1.4 Synthèse pour Serum 2 / Live 12 (basse P-Funk)

Plage de départ consolidée, à valider [TEST] ; chaque valeur renvoie aux recettes A-E :

- Serum 2 : OSC A saw à −24 st (A), OSC B square/pulse à −12 st avec PW ≈ 25-40 % (B), fine ±10-12 cents (C, D), SUB on si l'on veut la « troisième unité » (C).
- MONO + LEGATO, portamento **45 ms** (B) ; plage de pitch bend ±12 (C) — le « bend » descendant-remontant est l'articulation signature de Worrell (A, C).
- Filtre LP 24 dB « ladder-like », cutoff **120-800 Hz** selon la source (D vs C), résonance **25-35 %** (C, D) ; enveloppe de filtre : decay **80-600 ms** (C vs E), sustain **0** (C) ou plein (E) — deux esthétiques : « pluck » (C) ou « ouverte, jouée au bend » (E).
- Ampli : attaque minimale, release **15-20 ms** (B).
- Épaisseur « trois Minimoog » : dupliquer la piste ou utiliser Unison 2-3 voix, désaccord 5-8 cents (C).

---

## 2. Herbie Hancock : ARP Odyssey (« Chameleon »), « Rockit », Rhodes + Echoplex + wah

### 2.1 Faits documentés

- La basse de « Chameleon » (Head Hunters, 1973) est jouée par Hancock sur un **ARP Odyssey** ; le second solo est au **Fender Rhodes**. [EXTR] — Reverb « The Gear of Classic Herbie Hancock Albums » : https://reverb.com/news/the-gear-of-classic-herbie-hancock-albums ; Wikipedia « Chameleon (composition) » : https://en.wikipedia.org/wiki/Chameleon_(composition)
- Caractérisation : « basically a **two-oscillator detuned sawtooth** sound », « **downward envelope filter** », « farty resonance and rapid decay », « deep, punchy, juicy, gritty and chunky ». [EXTR] — Synthtopia : https://www.synthtopia.com/content/2015/04/21/the-iconic-sounds-of-synthesis-herbie-hancocks-chameleon-bassline/
- L'Odyssey (1972) est un mono deux VCO conçu contre le Minimoog, « rougher » ; la manière dont oscillateurs, filtre et enveloppes « distordent musicalement » y est difficile à reproduire ailleurs. [EXTR] — Vintage Synth Explorer forum : https://forum.vintagesynth.com/viewtopic.php?t=115235 ; arpsynth.com (Korg) : http://www.arpsynth.com/en/experience/sounds/2015/07/hisashi-saitoh/
- Hancock a « fait un usage extensif de l'**Echoplex** sur son Rhodes », avec de forts phasings sur d'autres enregistrements de l'époque ; l'Echoplex (Maestro) est un délai à bande qui permet d'enregistrer et de superposer en temps réel. [EXTR] — Reverb (même URL) ; herbiehancock.com « Electronic Instrument Glossary » : https://www.herbiehancock.com/2016/09/14/herbie-hancocks-electronic-instrument-glossary/
- Sextant (1973, même année) : effets **Fender Fuzz Wah**, **Countryman Phase Shifter**, **Echoplex**. [EXTR] — https://www.herbiehancock.com/music/discography/album/sextant/ . Aucune page lue ne cite nommément un « Maestro wah » sur « Chameleon » (section 9).

### 2.2 Recette « Chameleon » sur Korg ARP Odyssey (MusicRadar), paramètre par paramètre

[EXTR, extrait détaillé, page non lue] — https://www.musicradar.com/tuition/tech/how-to-recreate-the-chameleon-bass-sound-on-the-korg-arp-odyssey-620055

1. Réinitialiser tous les contrôles ; **les deux oscillateurs en sawtooth**, **niveaux à fond** dans le mixer.
2. Accord : le point médian de chaque oscillateur = do médian ; **désaccorder légèrement l'Osc 2** pour épaissir.
3. Filtre **Rev1** (le 2 pôles 12 dB de la première révision, sur le Korg réédité) ; **cutoff ≈ 1/4** de la course ; **résonance presque à fond**.
4. **Drive ON** (plus de niveau et de grain).
5. Filtre piloté par l'**ADSR**, quantité d'enveloppe vers le filtre **≈ 3/4** de la course.
6. ADSR : attaque **presque la plus rapide**, **decay court**, **un soupçon de sustain**, **release assez court**.
7. VCA sur l'enveloppe **AR** : attaque rapide, release assez court.
8. **Keyboard CV vers le filtre à moitié** (suivi de clavier 50 %).
9. Saleté supplémentaire : **S/H** — niveau d'entrée 1 du S/H à fond, mais **S/H → filtre bas**.

Autres recettes existantes mais non lisibles : Syntorial « Herbie Hancock - Chameleon | Bass Synth Preset Remake » (https://www.syntorial.com/preset-recipe/herbie-hancock-chameleon-bass/), Gearspace « Soft Synth - Herbie Hancock chameleon » (https://gearspace.com/board/music-computers/1168995-soft-synth-herbie-hancock-chameleon.html), TalkBass (https://www.talkbass.com/threads/herbie-hancock-chameleon.266646/).

Transposition Serum 2 [TEST] : 2 × saw, fine ±5-8 cents, MONO/legato, filtre 12 dB (pas 24) pour rester « Odyssey », cutoff bas (≈ 150-250 Hz), résonance haute (70-85 %), Env → cutoff fort (+50-70 %), decay filtre court (80-150 ms), sustain filtre faible, drive/distorsion douce avant le filtre (le « Drive ON »), suivi de clavier 50 %.

### 2.3 « Rockit » (1983, Future Shock)

- Le lead est joué sur un **Rhodes Chroma** ; base rythmique **Oberheim DMX** ; stab de guitare Led Zeppelin échantillonné au **Fairlight CMI**. [EXTR] — Reverb (URL ci-dessus) ; Wikipedia « Future Shock » : https://en.wikipedia.org/wiki/Future_Shock_(Herbie_Hancock_album)
- Crédits d'instruments de l'album : Fairlight CMI, Rhodes Chroma, Apple IIe, Yamaha DX7, E-mu 4060, Minimoog, Clavinet, Dr. Click, Alphacentauri, Yamaha GS1, vocoder Sennheiser, Yamaha CE20, Oberheim DMX, Synare. [EXTR] — Equipboard : https://equipboard.com/albums/herbie-hancock-future-shock
- Description du lead : « piercing bright timbre », motif syncopé de doubles-croches, entre à 0:27. [EXTR] — Syntorial : https://www.syntorial.com/preset-recipe/herbie-hancock-rockit-lead/ ; MusicRadar « 40 greatest synth sounds n°34 » : https://www.musicradar.com/news/the-40-greatest-synth-sounds-of-all-time-no-34-herbie-hancock-rockit
- **Aucune recette chiffrée lisible** (Syntorial et Cherry Audio « Doctor Mix / Quadra » bloqués).

---

## 3. Zapp & Roger : talkbox, synthé source, émulation numérique

### 3.1 Matériel documenté

- Roger Troutman utilisait une talkbox **Electro-Harmonix « Golden Throat »** avec un **Minimoog**, puis plus tard un **Yamaha DX100** (FM 4 opérateurs) pour sa portabilité. [EXTR] — Wikipedia : https://en.wikipedia.org/wiki/Roger_Troutman ; Equipboard : https://equipboard.com/pros/roger-troutman ; EHX Vault : https://www.ehx.com/blog/ehx-vault-golden-throat-roger-troutman/
- Sur le DX100, le patch utilisé serait **« SAWPULSE »** et non un sawtooth pur (témoignage d'un proche du groupe sur forum, anecdotique). [EXTR, non vérifiable] — Gearspace : https://gearspace.com/board/rap-hip-hop-engineering-and-production/188260-zapp-amp-roger-troutman-presets.html ; VSE « troutman dx100 patches » : https://forum.vintagesynth.com/viewtopic.php?t=80076
- Raison avancée du passage au DX100 : chaleur du Minimoog en scène (formulation confuse dans l'extrait : « tube fuses ») et petite taille du DX100. [EXTR, anecdotique] — même thread Gearspace.
- « More Bounce to the Ounce » (1980) : premier single, enregistré 1979-début 1980 aux **United Sound Studios (Detroit)**, coproduit par **Bootsy Collins** ; « Godzilla-sized synth bass line » ; Roger utilisait le **Minimoog « religieusement »**. [EXTR] — Wikipedia : https://en.wikipedia.org/wiki/More_Bounce_to_the_Ounce ; KVR : https://www.kvraudio.com/forum/viewtopic.php?t=92630 ; VSE : https://forum.vintagesynth.com/viewtopic.php?t=53164
- Oberheim chez Zapp : **rien de documenté trouvé** (section 9). « Computer Love » (1985) : pas de fiche instrument lisible.

### 3.2 Émulation dans Live 12 — Vocoder (manuel Ableton §28.42, lu via miroir GitHub)

Source lue intégralement : miroir texte du manuel Live (« 28.42 Vocoder » et « 28.42.1 Vocoder Tips ») — https://raw.githubusercontent.com/djaboxx/iron-static/main/docs/api/ableton/28-live-audio-effect-reference.md et https://raw.githubusercontent.com/GiovanniRaniolo/ableton-rack-generator/main/backend/data/knowledge/MANUAL_EXTRACT.txt (lignes 3945-4062). [DOC, sous réserve que le miroir soit fidèle ; il correspond mot pour mot au manuel officiel de mémoire]

Paramètres et comportements documentés :
- Le Vocoder s'insère **sur la piste du modulateur** (la voix). **Carrier** : Noise (X-Y downsampling/densité), **External** (routage interne, « l'option pour le robot voice classique »), Modulator (auto-vocodage), **Pitch Tracking** (oscillateur mono qui suit la hauteur du modulateur : **sawtooth ou trois pulse**, sliders High/Low, Pitch coarse ; ne met à jour la hauteur que sur une hauteur claire).
- **Enhance** : normalise spectre et dynamique du porteur (plus brillant). **Unvoiced** : volume d'un générateur de bruit pour « f » et « s » ; **Sens.** (100 % = toujours actif) ; **Fast/Slow**.
- **Bands** : nombre de filtres. **Range** : plage des passe-bande. **BW** : largeur (100 % = « la plus précise »). **Precise/Retro** (Retro : bandes plus étroites et plus fortes dans l'aigu). **Gate**, **Level**, **Depth** (100 % = vocodage classique ; 200 % = seuls les pics), **Attack/Release** (temps très courts = transitoires préservés, risque d'artefacts).
- Recette « Singing Synthesizer » du manuel : Vocoder sur la piste voix ; synthé (ex. Analog) sur une autre piste ; **Carrier = External**, **Audio From = piste synthé, Post FX** ; armer les deux pistes ; « **try sawtooth-based patches to improve the intelligibility** », ajuster **Unvoiced** et **Enhance**.
- Recette « Formant Shifter » : Carrier = Modulator, Depth 100 %, Enhance on, puis bouton **Formant**.

Talkbox ≠ vocodeur : avec une talkbox, la bouche forme les voyelles sur le son du synthé envoyé par un tube ; on ne parle pas. [EXTR] — Ali Jamieson : https://alijamieson.co.uk/2015/03/03/vocoder-v-talkbox/ . Le vocodeur de Live reste l'approche native la plus proche si la voix (micro) « mime » les voyelles sans les voiser ; Unvoiced bas, Bands élevé, BW ≈ 100 %, Depth 100 %, Attack/Release courts. [TEST]

### 3.3 Émulation par filtre à formants (Serum 2, Meld) et plug-ins

- **Serum 2** possède une famille de **filtres Formant** (« optimisés pour différentes transitions de voyelles quand on bouge le cutoff », modes Formant) parmi ~90 modes. [EXTR] — EDMProd : https://www.edmprod.com/serum-2-filters/ ; monosounds : https://monosounds.studio/serum-2-filters-explained/ ; manuel web Xfer (non lu) : https://xferrecords.com/web-manual/serum-2/welcome . Le nom exact « Vowel » n'a pas été confirmé pour Serum 2 ; la fiche locale `serum2.md` du skill ne liste pas les filtres. [TEST : vérifier la liste des filtres dans Serum 2]
- **Meld (Live 12)** propose un filtre **Vowel** [DOC local] — `.claude/skills/sound-designer-serum/references/ableton-instruments.md`, ligne 265.
- Table de formants pour régler un filtre à la main (Gordon Reid, Synth Secrets 23, lue dans le corpus local) [DOC] — `corpus/synth-secrets/synth-secrets-23.md` lignes 60-95 (voix d'homme, F1/F2/F3 en Hz) : « ee » 270/2300/3000 ; « oo » 300/870/2250 ; « i » 400/2000/2550 ; « e » 530/1850/2500 ; « u » 640/1200/2400 ; « a » 660/1700/2400. Pour « ee », gains/Q : F1 0 dB Q 5 ; F2 −15 dB Q 20 ; F3 −9 dB Q 50 ; largeur de bande ≈ 100 Hz. Le **deuxième formant est celui qui bouge le plus** (le plus important pour l'intelligibilité).
- Plug-ins talkbox : **MDA TalkBox** (gratuit, VST/AU/VST3), **iZotope VocalSynth 2** (module **Talkbox** : modes Dark / Classic / Bright, compatible Live 12), TAL-Vocoder, Cannabis Vocoder, Alter Ego (Plogue). [EXTR] — hiphopmakers : https://hiphopmakers.com/best-free-talkbox-vst-emulator-plugins ; iZotope : https://www.izotope.com/en/products/vocalsynth/features/talkbox-module ; KVR : https://www.kvraudio.com/product/talkbox_by_mda
- Ancienne recette Dubspot (Live) : MDA TalkBox + EQ Eight + Redux. [EXTR] — https://www.ableton.com/en/blog/talkbox-sounds-live-new-tutorial-dubspot/

Chaîne proposée pour le skill [TEST] : Serum 2, OSC A saw (ou « saw-pulse » : saw + pulse 30 %), MONO, legato, portamento 30-80 ms, léger vibrato LFO 5-6 Hz à la molette ; Filter 1 en mode Formant, cutoff modulé par macro/LFO lent ou par l'enveloppe pour parcourir « oo → a → ee » ; puis distorsion douce (ampli de talkbox) et EQ8 avec coupe-haut vers 5-6 kHz (le tube coupe les aigus). Alternative « vraie » voix : Vocoder de Live avec Carrier External sur le Serum saw, réglages de §3.2.

---

## 4. Prince : Oberheim OB-Xa / OB-8, Linn LM-1, DX7 (« 1999 », « When Doves Cry », « Kiss »)

### 4.1 Faits documentés

- « 1999 » a d'abord été enregistré avec un **OB-X** ; l'**OB-Xa** est utilisé sur l'album 1999 (et apparaît dans le clip) ; l'intro superpose **OB-Xa et ARP Omni-2** ; l'**OB-SX** est aussi cité. [EXTR] — Guitarcloud OB-Xa : https://www.guitarcloud.org/equipment/oberheim-ob-xa/ ; Guitarcloud OB-SX : https://guitarcloud.org/equipment/oberheim-ob-sx/ ; Wikipedia OB-SX : https://en.wikipedia.org/wiki/Oberheim_OB-SX
- Méthode Prince : **utiliser les presets** de l'OB et « **brighten the f**k out of it** » en ouvrant le filtre pour percer le mix. [EXTR] — MusicRadar : https://www.musicradar.com/news/princes-go-to-drum-machine-and-synths-a-career-in-music-tech-gear ; VSE : https://forum.vintagesynth.com/viewtopic.php?t=44457
- Reverb « The Synth Sounds of Prince's 1999 » : un **LFO module le VCO** pour la ligne « chorale » ; **plusieurs couches de chorus** essentielles ; affirmation (douteuse, à vérifier) qu'un « preset filter » OB-6 (2016) reprend ce son. [EXTR, l'affirmation OB-6 est à vérifier] — https://reverb.com/news/the-synth-sounds-of-princes-1999
- Astuce de reconstruction (MusicTech, OB-Xd) : partir d'un preset, **Filter Res 40 %**, **Drive +6 dB** pour compenser, **Reverb 10 %**, **Reverb Treble 100 %** (pas d'amortissement des aigus). [EXTR] — https://musictech.com/tutorials/weekend-workshop-prince-van-halen-synth-ob-xd/
- Les « brass » de Prince : **overdubs multiples avec différents renversements**, d'où la difficulté à isoler un voicing. [EXTR] — VSE thread ci-dessus.
- « When Doves Cry » (1984) : partie clavier principale au **Yamaha DX7, preset « KOTO »** (**patch 23 de ROM 1A / 22 de ROM 3B**) ; solo à l'**OB-Xa ou OB-8**. Prince utilisait « largement » les presets du DX7. [EXTR] — Guitarcloud : https://www.guitarcloud.org/faq/what-when-doves-cry-synth-sound/ et https://www.guitarcloud.org/faq/what-synth-presets-did-prince-use/
- **Paramètres complets du preset KOTO lus dans la cartouche ROM1A** : voir section 7.4 [DOC].
- « Kiss » (1986) : David Z programme la **LinnDrum** à Sunset Sound à partir d'une démo destinée à Mazarati ; un piano « à la Bo Diddley » ; Prince retire la basse et le hi-hat, ajoute le riff de guitare et le chant ; chœurs « ah-wah » adaptés de Brenda Lee. **Pas de synth stab documenté** sur ce titre. [EXTR] — Wikipedia : https://en.wikipedia.org/wiki/Kiss_(Prince_song) ; SOS Classic Tracks : https://www.soundonsound.com/techniques/classic-tracks-prince-kiss ; Mix : https://www.mixonline.com/recording/classic-tracks-princes-kiss-365014
- Linn LM-1 : Prince « désaccordait les percussions pour qu'elles ne sonnent plus comme des percussions » (Roger Linn). [EXTR] — MusicRadar (URL ci-dessus).
- DX7 sur Purple Rain ; OB-Xa sur l'intro « orgue d'église » de « Let's Go Crazy ». [EXTR] — Mixdown : https://mixdownmag.com.au/features/rig-rundown-princes-purple-rain/

### 4.2 Recette de départ « synth brass/stab OB-Xa façon 1999 » [HEUR/TEST]

Aucune valeur d'usine OB-Xa n'a pu être lue. À partir des éléments [EXTR] ci-dessus : 2 saw (ou saw + pulse) par voix, unison/désaccord modéré, filtre 12 dB Oberheim (Serum 2 : filtre 12 dB, résonance 30-40 %), enveloppe de filtre rapide (attaque 0, decay 200-400 ms, sustain 40-60 %), cutoff haut (« brighten »), LFO lent vers pitch faible pour la ligne chorale, **deux couches de chorus** (Live Chorus-Ensemble en Ensemble + un second Chorus lent), reverb courte 10 % avec aigus non amortis, drive +6 dB après filtre. Pour l'intro : doubler avec un string ensemble (Omni-2 → Live Analog en mode saw/pulse + Chorus-Ensemble).

---

## 5. G-funk (Dr. Dre, Warren G) : lead « whistle/worm » et basse

### 5.1 Faits documentés

- Le lead aigu de « Nuthin' but a 'G' Thang » (« G-Funk Whistle ») est décrit comme un **Minimoog** avec **glide/portamento**, réglages d'oscillateur et de glide spécifiques. [EXTR] — Syntorial : https://www.syntorial.com/preset-recipe/dr-dre-nuthin-but-a-g-thang-lead/ ; Reverb « 5 classic Minimoog » : https://reverb.com/news/video-the-synth-sounds-of-5-classic-minimoog-tracks ; Wikipedia G-funk : https://en.wikipedia.org/wiki/G-funk
- Vidéo TikTok d'Anthony Marinelli intitulée « Colin Wolfe didn't use a minimoog on Dr. Dre's 'Nothing but a G Thang'. It was a **Yamaha SY77**! » — contradiction avec la tradition Minimoog, non vérifiée. [EXTR, non vérifié] — https://www.tiktok.com/@anthonymarinellimusic/video/7415522299694255406
- Basse de « G Thang » : Colin Wolfe, **Yamaha BB2000** (basse électrique, sillets en laiton) ; la basse cite le morceau de Leon Haywood « I Want'a Do Something Freaky to You » (Wilton Felder). Wolfe utilisait un **Moog** sur « Dre Day » et « Deeez Nuts ». [EXTR] — Chad Kiser interview : https://chadkiser.com/2018/10/05/conversations-with-chad-colin-wolfe-talks-making-the-chronic-with-dr-dre-working-with-2pac-mc-breed/ ; VSE : https://forum.vintagesynth.com/viewtopic.php?t=50725
- « Regulate » (1994) : produit par Warren G ; interpolation de « I Keep Forgettin' » (Michael McDonald) ; claviers **Greg Geitzenauer** ; « whiny, woozy synthesizers and deep, slow-thumping bass ». [EXTR] — Wikipedia : https://en.wikipedia.org/wiki/Regulate_(song) ; RapReviews : https://www.rapreviews.com/2010/02/warren-g-regulate-g-funk-era/

### 5.2 Recette du lead « G Thang » sur Minimoog Model D (Reverb), paramètre par paramètre

[EXTR] — https://reverb.com/news/video-the-synth-sounds-of-5-classic-minimoog-tracks

- Osc 1 : **2'**, **sawtooth**.
- Osc 2 : **2'**, **square**, **légèrement désaccordé**.
- Osc 3 : volume **≈ 7** dans le mixer, une **octave en dessous** (« fuller, lower octave sound »).
- Filtre : **Cutoff 1**, **Emphasis 3**, **Amount of Contour 0** (ces valeurs, avec cutoff aussi bas, paraissent contradictoires pour un lead brillant : à revérifier sur la page ; il est possible que l'extrait ait tronqué « 10 » en « 1 ») [TEST].
- Glide activé (le « gliding, portamento effect » est la signature) ; mono. Valeur de glide et vibrato non chiffrés dans l'extrait.
- Résumé « n'importe quel synthé » : **un oscillateur sawtooth + mono + glide**. [EXTR] — note.com « What is G-Funk » : https://note.com/soundwitches/n/nc40e3009e51b?hl=en

Transposition Serum 2 [TEST] : OSC A saw +24 st, OSC B square +24 st fine +5-8 cents, SUB ou OSC C −12 st à 60-70 %, MONO legato, portamento 60-120 ms, LFO sinus 5-6 Hz vers pitch (profondeur ≈ 10-20 cents) à la molette, filtre LP 24 dB assez ouvert avec résonance 20-30 %, pas d'enveloppe de filtre (Contour 0), attaque 5-10 ms, release 100-200 ms, delay en envoi.

### 5.3 Basse G-funk

Aucune recette synthé chiffrée trouvée pour « Regulate » ou « G Thang » (basse électrique sur ce dernier). Point de départ [HEUR] : Minimoog bass générique de §1.3-D (saw 32' + square 16', cutoff bas, résonance 25 %) avec decay 300-500 ms et un peu de glide ; le « slow-thumping » vient du tempo (≈ 92-95 BPM) plus que du patch. [MÉMOIRE, non vérifié pour le tempo]

---

## 6. Electro-funk / boogie années 80 (Kashif, Mtume, Cameo, Midnight Star, Gap Band, Dâm-Funk)

### 6.1 Synthés typiques documentés par morceau/artiste

- **Midnight Star « Operator »** : **quatre Prophet-5 côte à côte**, utilisant les presets **bass, trumpet et keys** du Prophet-5. [EXTR] — In Sheep's Clothing : https://insheepsclothinghifi.com/5-songs-featuring-prophet-5/
- **Mtume « Juicy Fruit »** (1983) : **Linn LM-1** ; Phillip Fields (clavier principal) : **Crumar Performer, Oberheim OB-SX**, probablement Rhodes ; second claviériste avec **Minimoog D** et **OB-Xa ou OB-8** ; le riff aigu évoque un Oberheim Four Voice pour certains ; Bernie Worrell joue sur l'album (« Ready For Your Love » : Prophet-5, ARP String Ensemble). [EXTR] — VSE : https://forum.vintagesynth.com/viewtopic.php?t=42724 ; Wikipedia album : https://en.wikipedia.org/wiki/Juicy_Fruit_(album)
- **Cameo « Word Up! »** (1986) : ouverture sur **Linn** ; forum : « beaucoup de **DX7**, des **Jupiter** et **Juno** par-dessus, un peu de **Prophet-5**, possiblement du Fairlight » ; basses par Aaron Mills, Larry Blackmon, Michael Burnett ; studios Quad, Counter Point, Power Station, Sound Ideas (NYC). [EXTR] — VSE : https://forum.vintagesynth.com/viewtopic.php?t=56123 ; KVR : https://www.kvraudio.com/forum/viewtopic.php?t=262117 ; Wikipedia : https://en.wikipedia.org/wiki/Word_Up!_(album)
- **The Gap Band** : Minimoog et Prophet-5 « heavily » sur les titres électro-funk ; basses « more than likely Minimoog », influence Worrell/Junie Morrison ; Ronnie Wilson aux synthés ; accords possiblement Juno « filtre grand ouvert ». Crédits Gap Band IV (1982, Total Experience Studios, prod. Lonnie Simmons) : **Charlie Wilson — Mini Moog**. « Outstanding » : écrit par Raymond Calhoun ; **pas de fiche synthé spécifique** trouvée. [EXTR] — VSE : https://forum.vintagesynth.com/viewtopic.php?t=52850 ; KVR : https://www.kvraudio.com/forum/viewtopic.php?t=264868 ; Wikipedia : https://en.wikipedia.org/wiki/Gap_Band_IV ; https://en.wikipedia.org/wiki/Outstanding
- **Kashif** (Evelyn King « Love Come Down », etc.) : cité comme référence du « sweet spot synthé + vrais instruments » avec **Minimoog, Prophet-5, Oberheim ; DMX, DX, LinnDrum, 808** ; aucun détail par morceau. [EXTR] — Gearspace : https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/1147622-gear-used-post-disco-boogie-electro-funk.html
- **Dâm-Funk** (héritier) : **Roland Juno-60 / série Juno**, **Roland Alpha Juno 1** (Toeachizown, « exclusivement » des machines d'époque), **Moog Source**, **Oberheim DMX**, **LinnDrum**, boîtes à rythmes **Electro-Harmonix**, Casio et cassettes Maxell à ses débuts (1988). [EXTR] — RBMA : https://daily.redbullmusicacademy.com/2012/03/lecture-dam-funk/ ; Wikipedia : https://en.wikipedia.org/wiki/Dam-Funk ; VSE : https://forum.vintagesynth.com/viewtopic.php?t=54393&f=1
- Vue d'ensemble : « classic sound : Minimoog, Prophet 5, Pro One, OBXa » ; pour le modern funk, « Oberheim, Prophet 5, MiniMoog, Juno, DX7, JX8P ». [EXTR] — Gearspace : https://gearspace.com/threads/synth-shopping-for-electro-funk.1199730/

### 6.2 Synth bass DX7 « BASS 1 » / « SYN-BASS »

- **BASS 1** est le patch **15 de ROM1A** ; le slap bass de a-ha « Take On Me » est « le patch 15-Bass 1 du DX7 passé dans un chorus » ; « Take My Breath Away » utilise **BASS 2** (16 de ROM1A) ; « Danger Zone » un slap bass DX7. [EXTR] — Reverb Machine « Exploring the Yamaha DX7, Part Two » : https://reverbmachine.com/blog/exploring-the-yamaha-dx7-pt2/
- Les valeurs complètes de BASS 1 et BASS 2 (algorithme, ratios, feedback, enveloppes) ont été **lues directement dans la cartouche ROM1A** : section 7.3 [DOC]. Il n'existe pas de « SYN-BASS » dans ROM1A/ROM1B (noms lus : BASS 1, BASS 2 en ROM1A ; BASS 3, BASS 4 en ROM1B) [DOC].
- Un autre analyste (dépôt ossium19) confirme « BASS 1 : ROM1A slot 15, DX7 Algorithm 1 » — c'est **faux** d'après la cartouche (algorithme **16**) ; l'erreur vient probablement de leur remappage vers 8 algorithmes. [DOC pour la lecture, la valeur du dépôt est contredite] — https://raw.githubusercontent.com/tiltti/ossium19/HEAD/web/DX7_EXTRACTION_SUMMARY.md

### 6.3 Juno chorus keys

- Juno-106 : sub-oscillateur une octave sous l'oscillateur principal ; **Chorus I / II** (II plus fort), chorus à **BBD** apparenté aux pédales BOSS de l'époque ; pseudo-stéréo caractéristique ; pulse étroite = ton fin, large = plus plein. [EXTR] — Equipboard : https://equipboard.com/posts/roland-juno-106-guide ; Wikipedia : https://en.wikipedia.org/wiki/Roland_Juno-106 ; Roland specs : https://support.roland.com/hc/en-us/articles/201966419-Juno-106-Technical-Specifications
- Aucune vitesse/profondeur de chorus chiffrée n'a été lue. Point de départ Live 12 [HEUR/TEST] : Serum 2 ou Analog, saw + pulse 50 % + sub −12 st à −6 dB, filtre 24 dB cutoff 1-2 kHz, résonance 10 %, enveloppe ampli attaque 5 ms / release 300 ms, **Chorus-Ensemble de Live en mode Chorus, rate ≈ 0,5-0,8 Hz, amount 50-70 %, largeur max** (imitation Chorus I/II) — valeurs de pratique, non documentées.

### 6.4 Synth brass (renvoi) et lead square/pulse

- **Synth brass** : un autre skill « cuivres » couvre le sujet ; ici, deux références suffisent : (1) Gordon Reid, Synth Secrets 25-27 (théorie des cuivres, puis **brass sur Minimoog** et sur SH-101/Axxe), lisibles dans le corpus local `corpus/synth-secrets/synth-secrets-25.md` à `-27.md` [DOC local] ; (2) le preset DX7 **BRASS 1** (ROM1A #1, algorithme 22, feedback 7, six opérateurs dont quatre porteuses en ratio 1.0 désaccordées et un modulateur partagé), dont les paramètres sont en 7.5 [DOC]. Pour les stabs Oberheim/Prophet, voir §4.2.
- **Lead square/pulse électro-funk** : la seule recette chiffrée lue est FM : DX7 **SYN-LEAD 1** (ROM1A #14) en 7.5 [DOC]. Pour un lead analogique « square » type Minimoog, partir de §5.2 (G-funk) en remplaçant saw par square et en réduisant le glide [HEUR].

---

## 7. Yamaha DX7 dans le funk/R&B : E.PIANO 1, BASS 1, MARIMBA, CALIOPE, KOTO — analyse lue dans les cartouches d'usine

### 7.1 Sources et méthode (toutes lues intégralement)

- **ROM1A.SYX** (bulk dump 32 voix, 4104 octets, en-tête `F0 43 00 09 20 00`) : https://raw.githubusercontent.com/WouterVanNifterick/DX7/master/ROM1A.SYX [DOC — données Yamaha d'origine, redistribuées librement]. Noms lus : BRASS 1, BRASS 2, BRASS 3, STRINGS 1-3, ORCHESTRA, PIANO 1-3, **E.PIANO 1 (#11)**, GUITAR 1-2, SYN-LEAD 1 (#14), **BASS 1 (#15)**, BASS 2 (#16), E.ORGAN 1, PIPES 1, HARPSICH 1, CLAV 1 (#20), VIBE 1, **MARIMBA (#22)**, **KOTO (#23)**, FLUTE 1, ORCH-CHIME, TUB BELLS, STEEL DRUM, TIMPANI, REFS WHISL, VOICE 1, TRAIN, TAKE OFF.
- **ROM1B** (tableau C `syx_bank_1[]`, commentaire « file ROM1B.SYX ») : https://raw.githubusercontent.com/rheslip/2HPico-Sketches/main/PlaitsFM/ROMbanks/banks.cc [DOC]. Le preset s'y appelle **« CALIOPE » (#20, orthographe d'usine)**.
- Disposition du format « packed » (17 octets par opérateur, OP6 en premier ; octets 102-127 globaux) vérifiée dans `parse-rom.js` : https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/master/examples/dx7/parse-rom.js [DOC]. Contrôle croisé : le fichier `epiano.dsp` généré par ce même outil donne exactement les valeurs que j'ai lues pour E.PIANO 1 (algorithme 5, feedback 6, ratios 1/14/1/1/1/1, niveaux 99/58/99/89/99/79). https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/master/examples/dx7/dsp/epiano.dsp [DOC]
- Routages d'algorithmes (notation Faust de `parse-rom.js`, lus) [DOC] :
  - Alg 2 : `(op2~fb : op1), (op6 : op5 : op4 : op3)` — porteuses OP1 et OP3.
  - Alg 3 : `(op3 : op2 : op1), (op6~fb : op5 : op4)` — porteuses OP1 et OP4.
  - Alg 5 : `(op2 : op1), (op4 : op3), (op6~fb : op5)` — trois piles de 2, porteuses OP1, OP3, OP5.
  - Alg 7 : `(op2 : op1), (op4, (op6~fb : op5) :> op3)` — porteuses OP1 et OP3.
  - Alg 16 : `op2, (op4 : op3), (op6~fb : op5) :> op1` — **une seule porteuse OP1**, trois branches modulantes.
  - Alg 17 : `op2~fb, (op4 : op3), (op6 : op5) :> op1` — idem, feedback sur OP2.
  - Alg 18 : `op2, op3~fb, (op6 : op5 : op4) :> op1` — une porteuse.
  - Alg 22 : `(op2 : op1), (op6~fb <: op3, op4, op5)` — porteuses OP1, OP3, OP4, OP5.
- Conversion « rate DX7 → millisecondes » : j'ai porté en Python le générateur d'enveloppe de **Dexed** (`env.cc`, mode ACCURATE_ENVELOPE, tables mesurées sur deux TX7 par l'auteur, 44,1 kHz) et simulé chaque opérateur à C3 avec son rate scaling. https://raw.githubusercontent.com/asb2m10/dexed/master/Source/msfa/env.cc [DOC pour le code ; les ms sont une **estimation** ±20 % d'après les commentaires du code lui-même]. Les segments donnés ci-dessous sont : A = temps pour atteindre L1 depuis 0 ; D1 = L1→L2 ; D2 = L2→L3 (si atteint en 4 s) ; R = L3→L4 après relâchement.
- Detune DX7 : ≈ **0,9 à 1,3 cent par pas** (Dexed : ancien coefficient 12606/2^24 octave = 0,90 cent ; commentaire « 7.213 Hz per count at 9600 Hz » = 1,3 cent), donc ±7 ≈ ±6-9 cents. https://raw.githubusercontent.com/asb2m10/dexed/master/Source/msfa/dx7note.cc [DOC]
- Vitesse de LFO DX7 → Hz (table `lfoSource` de Dexed, « ces chiffres viennent de mon DX7 ») : speed 30 ≈ **4,8 Hz**, 34 ≈ 5,4 Hz, 35 ≈ 5,6 Hz, 37 ≈ 5,95 Hz. https://raw.githubusercontent.com/asb2m10/dexed/master/Source/msfa/lfo.cc [DOC]

### 7.2 E.PIANO 1 (ROM1A #11) — paramètres complets [DOC]

- **Algorithme 5**, **feedback 6** (sur OP6), Osc Key Sync off, transpose 0.
- LFO sinus, speed 34 (≈ 5,4 Hz), delay 33, **PMD 0, AMD 0** (le vibrato n'existe que via la molette), PMS 3. Pitch EG neutre (L = 50/50/50/50).
- Trois piles porteuse/modulateur :

| OP | Rôle | Ratio | Detune | Out level | EG rates R1-R4 | EG levels L1-L4 | Vél. (KVS) | Rate scaling | Level scaling | Temps estimés à C3 |
|---|---|---|---|---|---|---|---|---|---|---|
| OP1 | porteuse pile « cloche » | 1.000 | +3 (≈ +3 cents) | 99 | 96/25/25/67 | 99/75/0/0 | 2 | 3 | — | A 1 ms, D1 ≈ 2,2 s (→75), D2 lent, R ≈ 74 ms |
| OP2 | modulateur « attaque cloche » | **14.000** | 0 | **58** | 95/50/35/78 | 99/75/0/0 | **7** | 3 | — | D1 ≈ 140 ms, D2 ≈ 1,8 s, R ≈ 9 ms |
| OP3 | porteuse corps | 1.000 | 0 | 99 | 95/20/20/50 | 99/95/0/0 | 2 | 3 | — | D1 ≈ 0,75 s (→95), R ≈ 0,57 s |
| OP4 | modulateur corps | 1.000 | 0 | 89 | 95/29/20/50 | 99/95/0/0 | 6 | 3 | — | D1 ≈ 250 ms, R ≈ 0,5 s |
| OP5 | porteuse corps 2 | 1.000 | **−7** (≈ −6 cents) | 99 | 95/20/20/50 | 99/95/0/0 | 0 | 3 | — | comme OP3 |
| OP6 | modulateur corps 2 + feedback 6 | 1.000 | **+7** (≈ +6 cents) | 79 | 95/29/20/50 | 99/95/0/0 | 6 | 3 | breakpoint 41 (≈ E3), profondeur droite 19, −LIN | D1 ≈ 250 ms, R ≈ 0,44 s |

Lecture : le « tine » vient de la pile OP2→OP1 (ratio 14:1, niveau modéré 58 mais **très sensible à la vélocité, KVS 7**, decay rapide de la modulation ≈ 140 ms puis extinction en ≈ 2 s) ; le corps vient de deux piles 1:1 dont l'une est désaccordée de ±7 pas (battement lent ≈ 12 cents d'écart entre OP5 et OP6) avec feedback 6 qui « sale » légèrement ; les modulateurs de corps ont KVS 6 (brillance liée à la vélocité) ; OP6 perd du niveau au-dessus de E3 (level scaling), ce qui adoucit l'aigu. Cette structure correspond aux descriptions [EXTR] de KVR (« 14:1 for the bell-like attack », « 1:1 for the body ») : https://www.kvraudio.com/forum/viewtopic.php?t=223022 . Gordon Reid rappelle [DOC local, `corpus/synth-secrets/synth-secrets-42.md` ligne 49] que le DX7 excellait dans l'imitation des **pianos électriques** (Rhodes, Wurlitzer, Hohner) mais non du piano acoustique.

**Transposition dans Ableton Operator (4 opérateurs, 11 algorithmes)** — d'après la fiche locale [DOC local] `.claude/skills/sound-designer-serum/references/ableton-instruments.md` lignes 86-106 (lecture géométrique de la figure officielle) et le manuel [EXTR] (Coarse en ratios harmoniques, Fine en cents sur une octave ; Feedback disponible sur les oscillateurs non modulés) : https://www.ableton.com/en/manual/live-instrument-reference/

- Choisir l'**algorithme 8 « B→A ; D→C »** (deux paires FM parallèles) — il manque la troisième pile ; on la compense par **Spread** ou en doublant l'instrument. [TEST]
- A = porteuse, Coarse 1, Fine 0, Level 0 dB ; enveloppe A : attaque 1 ms, decay ≈ 2,2 s vers sustain ≈ −2,5 dB (L2 = 75/99), puis release ≈ 75-100 ms (release DX7 ≈ 74 ms).
- B = modulateur cloche, **Coarse 14**, Level ≈ −6 à −8 dB (58/99 en unités DX7 ≈ −9 dB si l'on prend 0,023 dB × 32 microsteps par unité, cf. `env.h`), **Lev < Vel 100 %** ; enveloppe B : attaque 1 ms, decay ≈ 140 ms vers sustain ≈ −2,5 dB puis ≈ 1,8 s vers 0 (Operator n'a qu'un decay : prendre decay 300-500 ms, sustain −12 dB, release 10 ms) [TEST].
- C = porteuse corps, Coarse 1, Fine 0, Level 0 dB ; enveloppe : attaque 1 ms, decay 750 ms vers sustain −0,4 dB (95/99), release 550 ms.
- D = modulateur corps, Coarse 1, **Fine +6 cents** (OP6 +7) — ou Fine 0 et Spread léger —, Level ≈ −1 dB (89/99), **Feedback ≈ 6/7 ≈ 85 %**, Lev < Vel ≈ 85 % ; enveloppe : attaque 1 ms, decay 250 ms, sustain −0,4 dB, release 450 ms ; **Lev < Key** négatif au-dessus de E3 (imite le level scaling de OP6).
- Global : pas de LFO par défaut ; Time = 100 % ; ajouter Chorus-Ensemble léger et un compresseur doux, comme sur les disques de l'époque [HEUR].

### 7.3 BASS 1 (ROM1A #15) et BASS 2 (ROM1A #16) — paramètres complets [DOC]

**BASS 1** : **algorithme 16** (une porteuse OP1 ; OP2, OP3←OP4, OP5←OP6 la modulent), **feedback 7** (sur OP6), **Osc Key Sync ON** (attaque identique à chaque note), **transpose −12**. LFO triangle speed 35, PMD/AMD 0. Pitch EG neutre.

| OP | Rôle | Ratio | Out level | EG rates | EG levels | KVS | Rate scaling | Level scaling | Temps estimés à C3 |
|---|---|---|---|---|---|---|---|---|---|
| OP1 | **porteuse** | 0.500 | 99 | 95/62/17/58 | 99/95/32/0 | 0 | **7** | bp 36 (≈ C3), gauche +57 +LIN, droite 14 −LIN | A 1 ms, D1 4 ms (→95), D2 lent (→32), R ≈ 45 ms |
| OP2 | modulateur grave (1:1 avec la porteuse) | 0.500 | 80 | 99/20/0/0 | 99/0/0/0 | 0 | 7 | bp 41 | decay long vers 0 (rate 20, plusieurs s), R très long |
| OP3 | modulateur corps | 0.500 | 99 | 88/96/32/30 | 79/65/0/0 | 3 | 6 | — | D1 3 ms (79→65), D2 ≈ 1,6 s, R ≈ 0,6 s |
| OP4 | modulateur de OP3 (« slap ») | **5.000** | 93 | 90/42/7/55 | 90/30/0/0 | **5** | 5 | — | D1 ≈ 470 ms (90→30), R ≈ 60 ms |
| OP5 | modulateur tenu | 0.500 | 62 | 99/0/0/0 | 99/0/0/0 | 3 | 7 | bp 52, gauche 75 −LIN | tenu tant que la note dure |
| OP6 | modulateur de OP5 (« clic ») + feedback 7 | **9.000** | 85 | 94/56/24/55 | 93/28/0/0 | **7** | 1 | — | D1 ≈ 370 ms (93→28), R ≈ 90 ms |

Lecture : la brillance percussive vient des ratios 5 (OP4) et 9 (OP6, avec feedback maximal = composante bruitée/« pick »), tous deux très dépendants de la vélocité (KVS 5 et 7) et décroissant en ≈ 400-500 ms ; les modulateurs 1:1 (OP2, OP3, OP5) donnent le corps « saw-like » ; le **rate scaling 7** sur OP1/OP2/OP5 raccourcit fortement les notes dans l'aigu ; le release de la porteuse ≈ 45 ms rend le son sec. C'est le patch de « Take On Me » [EXTR, §6.2].

**Transposition Operator** [TEST] : algorithme **7 « (B+C+D)→A »** (trois modulateurs sur une porteuse) — c'est la topologie la plus proche de l'algorithme 16 sans les sous-piles : A Coarse 0.5 (ou Coarse 1 avec Transpose −12 ; DX7 : ratio 0,5 et transpose −12) ; B Coarse 0.5 Level −2 dB (OP2) ; C **Coarse 5** Level −1 dB, Lev < Vel 70 %, enveloppe decay 470 ms sustain −inf (OP4, en sautant l'étage OP3) ; D **Coarse 9**, Level −2 dB, **Feedback 100 %**, Lev < Vel 100 %, decay 370 ms sustain −inf (OP6) ; enveloppe A : attaque 1 ms, decay 4 ms vers sustain −0,4 dB puis release 45 ms ; **Osc Retrig ON** sur tous (= Osc Key Sync) ; Time < Key positif pour imiter le rate scaling 7 ; Chorus-Ensemble derrière.

**BASS 2** : algorithme 17, feedback 7, transpose −12, LFO sinus speed 31 delay 33 PMD/AMD 0. Ratios : OP1 0.505, OP2 0.515, OP3 1.000 (+7), OP4 0.500, OP5 1.010, OP6 0.500 (+1) ; niveaux 99/80/68/99/75/87 ; enveloppes plus lentes (OP2 et OP6 : attaque rate 28/25 ≈ 0,8-0,9 s) : basse « ronde » avec gonflement. [DOC] Utile comme « synth bass 80s douce ».

### 7.4 KOTO (ROM1A #23, « When Doves Cry ») et MARIMBA (ROM1A #22) [DOC]

**KOTO** : **algorithme 2**, feedback 7 (OP2), Osc Key Sync ON, transpose 0. **LFO sinus speed 30 (≈ 4,8 Hz), delay 40, PMD 17, AMD 15, sync ON, PMS 2** : vibrato + trémolo retardés intégrés au preset. **Pitch EG R 85/99/75/0, L 49/50/50/50** : léger creux de hauteur à l'attaque (L1 = 49) — le « pincement » de corde.

| OP | Ratio | Out | EG rates | EG levels | KVS | RS | Temps estimés |
|---|---|---|---|---|---|---|---|
| OP1 (porteuse 1) | 1.000 | 90 | 94/62/58/34 | 99/92/0/0 | 3 | 6 | D1 6 ms, D2 ≈ 110 ms, R ≈ 350 ms |
| OP2 (mod. de OP1, feedback 7) | 4.000 | 99 | 99/68/28/48 | 99/83/0/0 | 0 | 6 | D1 7 ms, D2 ≈ 3,2 s |
| OP3 (porteuse 2) | 1.000 | 99 | 94/64/30/33 | 99/92/0/0 | 3 | 5 | D2 ≈ 3 s, R ≈ 0,42 s |
| OP4 (mod.) | 1.000 | 82 | 90/28/17/39 | 99/76/0/0 | 1 | 6 | D1 ≈ 0,7 s |
| OP5 (mod.) | 4.000 | 83 | 91/37/29/29 | 99/90/0/0 | 1 | 6 | D1 ≈ 95 ms, D2 ≈ 2,6 s |
| OP6 (mod. haut) | 3.000 | 81 | 82/53/37/48 | 99/81/0/0 | 1 | 6 | D1 ≈ 36 ms, D2 ≈ 1 s |

Transposition Operator [TEST] : algorithme 1 « D→C→B→A » ne convient pas (deux porteuses nécessaires) ; prendre **algorithme 8** : A Coarse 1 + B Coarse 4 Feedback 100 % (pile OP2→OP1) ; C Coarse 1 + D Coarse 3-4 (pile réduite OP6→OP5→OP4→OP3) ; pitch envelope −1 % à l'attaque avec decay 20 ms ; LFO sinus 4,8 Hz, delay ≈ 0,5 s, vers pitch faible (PMD 17 avec PMS 2 ≈ quelques cents) et vers niveaux (AMD 15).

**MARIMBA** : **algorithme 7**, **feedback 0**, Osc Key Sync ON, LFO triangle speed 35 sync ON (PMD/AMD 0). Ratios OP1 0.500 (porteuse), OP2 **3.000** (modulateur de OP1), OP3 0.500 (porteuse), OP4 **5.000**, OP5 **0.750**, OP6 **4.520** (inharmonique) ; niveaux 95/96/99/85/93/99 ; OP6 a une **attaque rate 0** (montée très lente, donc quasi inaudible sur des notes courtes) ; level scaling breakpoint 54 avec profondeur droite 46 sur OP2/OP4/OP5 (les modulateurs s'atténuent dans l'aigu, comme un vrai marimba qui perd son « bois » en montant) ; decay des porteuses ≈ 110-225 ms puis ≈ 0,85-1 s ; release ≈ 60-300 ms. Transposition Operator [TEST] : algorithme 8, A Coarse 0.5 / B Coarse 3 (ratio 6:1 relatif) et C Coarse 0.5 / D Coarse 5 (10:1 relatif) ; enveloppes de modulateurs decay 30 ms ; Lev < Key négatif sur B et D.

### 7.5 CALIOPE (ROM1B #20), BRASS 1 (ROM1A #1), SYN-LEAD 1 (ROM1A #14), CLAV 1 (ROM1A #20) [DOC]

**CALIOPE** : **algorithme 16**, feedback 5, Osc Key Sync ON. LFO triangle speed 30, delay 23, PMD/AMD 0. Ratios : OP1 1.000 (porteuse, out 98, attaque rate 60 ≈ 30 ms, L1 82 → L2 75 → L3 95 : léger « gonflement » de flûte), OP2 **4.600**, OP3 **2.020** (+7), OP4 2.000 (−7), OP5 2.000, OP6 **7.040** (+1) ; niveaux 98/75/67/75/56/82 ; modulateurs pairs (2.0/2.02, désaccordés ±7 ↔ battement ≈ 12 cents) pour le souffle d'orgue à vapeur, ratios inharmoniques 4.6 et 7.04 pour le « chiff ». Attaques 7-30 ms, release porteuse ≈ 270 ms. Aucun morceau funk/R&B utilisant CALIOPE n'a été documenté par une page lue (section 9).

**BRASS 1** : algorithme 22, feedback 7, Osc Key Sync ON, LFO sinus speed 37 (≈ 6 Hz) **PMD 5** (vibrato léger permanent), PMS 3. OP1 0.500 (+7) et OP2 0.500 (+7), OP3-OP5 1.000 (−2/0/+1), OP6 1.000 modulateur partagé (out 82, attaque rate 49 ≈ 36 ms, level scaling bp 39 gauche 54/droite 50 −EXP) ; porteuses OP4/OP5 avec decay ≈ 720 ms vers 98 puis sustain 98 ; attaques 9-17 ms ; releases ≈ 140 ms. Le désaccord des quatre porteuses (−2, 0, +1 et 0.5 +7) et le feedback 7 sur OP6 font l'épaisseur « section ». Renvoi vers le skill cuivres.

**SYN-LEAD 1** : algorithme 18, feedback 7 (OP3), **transpose +12**, LFO sinus speed 37 delay 42 **AMD 99** PMD 0 (trémolo profond retardé, ou par molette) ; ratios OP1 1.000 (+1), OP2 1.000 (−1), OP3 1.000, OP4 2.000 (+2), OP5 3.000 (−2), OP6 **17.000** ; niveaux 99/71/82/71/43/47 ; OP4 : L1 99 → L2 90 puis decay 2,6 s : brillance qui s'éteint lentement. Lead FM « square-like » (harmoniques impaires via 1/3 et le feedback). Transposition Operator [TEST] : algorithme 7 (B+C+D→A), A Coarse 1, B Coarse 1 Feedback 100 %, C Coarse 2, D Coarse 3 Level bas ; LFO vers niveaux à 6 Hz à la molette.

**CLAV 1** (pour le « Superstition » FM) : algorithme 3, feedback 5, Osc Key Sync ON, LFO speed 30 ; piles OP3→OP2→OP1 (6.0 → 0.5 → 0.5) et OP6→OP5→OP4 (8.0 → 0.5 → 2.0) ; modulateurs hauts (6 et 8) avec decay 6 ms (rate 87) : le « clic » de Clavinet ; porteuses decay 3 ms vers 90 puis longue tenue, release ≈ 110 ms ; KVS 6-7 sur OP5/OP6.

---

## 8. Pages consultées (statut réel)

### Lues intégralement (HTTP 200, contenu exploité)

1. https://raw.githubusercontent.com/WouterVanNifterick/DX7/master/ROM1A.SYX — cartouche ROM1A (4104 o) [DOC]
2. https://raw.githubusercontent.com/rheslip/2HPico-Sketches/main/PlaitsFM/ROMbanks/banks.cc — 8 cartouches ROM1A-4B en C (ROM1B exploitée) [DOC]
3. https://raw.githubusercontent.com/asb2m10/dexed/master/Source/msfa/env.cc et env.h — enveloppe DX7 (Dexed) [DOC]
4. https://raw.githubusercontent.com/asb2m10/dexed/master/Source/msfa/dx7note.cc et lfo.cc — detune, LFO [DOC]
5. https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/master/examples/dx7/parse-rom.js et dsp/epiano.dsp — format sysex, routages, E.PIANO 1 [DOC]
6. https://raw.githubusercontent.com/petersalomonsen/javascriptmusic/HEAD/examples/dx7/README.md [DOC]
7. https://raw.githubusercontent.com/tiltti/ossium19/HEAD/web/DX7_EXTRACTION_SUMMARY.md [DOC, contient une erreur d'algorithme pour BASS 1]
8. https://raw.githubusercontent.com/djaboxx/iron-static/main/docs/api/ableton/28-live-audio-effect-reference.md — miroir manuel Live, §28.42 Vocoder [DOC]
9. https://raw.githubusercontent.com/GiovanniRaniolo/ableton-rack-generator/main/backend/data/knowledge/MANUAL_EXTRACT.txt — miroir manuel Live, Vocoder Tips [DOC]
10. https://raw.githubusercontent.com/ZacharySBrown/idm-course/HEAD/specs/ableton_course_ep2_analog_research.md — recette Flash Light (tiers) [HEUR]
11. https://raw.githubusercontent.com/keunwoochoi/subtractive-synthesizers.js/HEAD/README.md — citation Worrell (3 Minimoog) [DOC pour la citation]
12. https://raw.githubusercontent.com/alextrzyna/mcp-muse/HEAD/dev-plans/CLASSIC_SYNTH_PRESETS_PLAN.md — sans valeur utile
13. https://raw.githubusercontent.com/knoguchi/dx7/main/dx7-app/examples/gen_gm_rom.rs — table GM → ROM (CALLIOPE = rom1b #20) [DOC]
14. https://gist.github.com/bryc/e997954473940ad97a825da4e7a496fa — sans valeur utile pour les presets
15. https://raw.githubusercontent.com/asb2m10/dexed/master/README.md — contexte Dexed
16. https://github.com/WouterVanNifterick/DX7 — liste des fichiers
17. Corpus local : `corpus/synth-secrets/synth-secrets-08.md`, `-23.md`, `-42.md` ; `.claude/skills/sound-designer-serum/references/ableton-instruments.md` ; `.claude/skills/vst-sound-design/references/instruments-natifs.md` et `serum2.md` [DOC local]

### Bloquées par le proxy (EGRESS_BLOCKED), contenu connu seulement par extraits de recherche

attackmagazine.com (Flash Light remake) ; syntorial.com (Flash Light, Chameleon, G Thang, Rockit) ; reverb.com (Bernie Worrell, 5 Minimoog tracks, Prince 1999, Herbie gear, Essential Gear P-Funk) ; reverbmachine.com (Exploring the DX7 pt 1 et 2, Legends presets) ; musicradar.com (Chameleon Odyssey, Thriller synths, Stevie Wonder, Minimoog bass, Operator guide, Prince gear) ; synthtopia.com (Chameleon, Thriller Minimoog, Troutman) ; guitarcloud.org (When Doves Cry, presets, OB-Xa, OB-SX) ; en.wikipedia.org (Flash Light, Roger Troutman, Thriller, Kiss, Regulate, Gap Band IV, Juicy Fruit, etc.) ; soundonsound.com (Swedien, Kiss, Herbie) ; kvraudio.com (E.Piano, Troutman, Boogie, Gap Band, Word Up) ; gearspace.com (Chameleon, Zapp presets, electro-funk) ; vintagesynth.com et forum.vintagesynth.com ; modwiggler.com ; talkbass.com ; mudcakesite.wordpress.com ; medium.com ; ehx.com ; ableton.com (manuel, blog Dubspot) ; forum.ableton.com ; alijamieson.co.uk ; djjondent.blogspot.com ; righto.com ; yamahablackboxes.com ; cdn.inmusicbrands.com (manuel Minimoog) ; moogmusic.com ; xferrecords.com ; web.archive.org / archive.org ; bing.com ; duckduckgo.com.

### Introuvables (404) sur GitHub

raw.githubusercontent.com/WouterVanNifterick/DX7/master/ROM1B.SYX ; asb2m10/dexed/master/Data/Dexed_01.syx, Data/ROM1B.syx, Data/Cart/rom1b.syx ; knoguchi/dx7/main/factory/rom1b.syx (le dépôt référence « factory/rom1b.syx » mais ne le publie pas) ; djaboxx/iron-static docs/api/ableton/27-live-instrument-reference.md (le chapitre Operator du miroir n'a pas été trouvé).

### Outils GitHub (API)

`mcp__github__get_file_contents` refuse tout dépôt autre que celui de l'utilisateur ; `mcp__github__search_code` fonctionne et a servi à localiser les fichiers ci-dessus.

---

## 9. Ce qui n'a pas été trouvé

1. **Aucune page Reverb Machine n'a été lue** ; ses articles « Exploring the DX7 » 1 et 2 existent (extraits : Take On Me = BASS 1 + chorus ; Take My Breath Away = BASS 2), mais rien de Reverb Machine sur Flash Light, Parliament, Worrell, Stevie Wonder, Michael Jackson ou Prince n'est ressorti des recherches — soit ces articles n'existent pas, soit le moteur ne les indexe pas.
2. **« Boogie On Reggae Woman »** : aucune recette chiffrée, ni confirmation Minimoog vs modulaire.
3. **« Thriller »** : la recette pas-à-pas MusicRadar (« recreate-thriller-synth-minimoog ») et la vidéo Synthtopia n'ont pu être lues ; seul l'extrait Reverb (cutoff 0 / emphasis 3 / contour 5 / decay 600 ms) est disponible, sans certitude qu'il concerne ce titre.
4. **Filtre/enveloppe de la recette Attack « Flash Light »** (seuls oscillateurs, glide et release sont dans l'extrait).
5. **« Rockit »** : aucune valeur de patch (Syntorial, Cherry Audio bloqués) ; seulement l'instrument (Rhodes Chroma).
6. **Wah/Maestro sur le Rhodes de « Chameleon »** : non confirmé par une page ; Echoplex et fuzz-wah confirmés sur l'époque (Sextant) seulement.
7. **Zapp** : pas de source sur un Oberheim ; pas de recette du synth bass de « More Bounce » ; forme d'onde de la talkbox = « Minimoog » puis « DX100 SAWPULSE » d'après un témoignage anonyme ; aucune fiche sur « Computer Love ».
8. **Prince** : aucune valeur de preset OB-Xa/OB-8 ; le nom de preset « Prince 1999 » sur OB-6 n'est pas vérifié ; aucun synth stab documenté sur « Kiss » (le titre repose sur LinnDrum, guitare, piano).
9. **G-funk** : la recette Syntorial (« G Thang » lead) n'a pu être lue ; valeur de glide et de vibrato absentes ; contradiction Minimoog vs Yamaha SY77 (Marinelli) non résolue ; aucune recette de basse G-funk ; identité du synthé lead de « Regulate » inconnue (claviers : Greg Geitzenauer).
10. **Electro-funk** : aucune fiche par morceau pour Kashif, Midnight Star (« No Parking »), Gap Band « Outstanding » ; pas de vitesse/profondeur chiffrée du chorus Juno ; Juicy Fruit : synthés listés mais pas de patch.
11. **CALLIOPE** : paramètres lus, mais aucune page ne documente son usage dans un morceau funk/R&B.
12. **Serum 2** : le nom exact du filtre « Vowel »/« Formant » et la liste des modes n'ont pas été lus dans le manuel Xfer (site bloqué) ; la fiche locale `serum2.md` ne les liste pas.
13. **Manuel Minimoog** : spécifications obtenues par extrait seulement ; les feuilles de patch d'usine (« Sound Charts », citées dans Synth Secrets 30) n'ont pas été lues.
14. **Chapitre Operator du manuel Live** : non trouvé en miroir GitHub ; la fiche locale `ableton-instruments.md` (§30.9) fait foi pour l'architecture, mais les plages en ms des enveloppes d'Operator restent [TEST].

### Recommandation pour la suite

Relancer la lecture, depuis un réseau non filtré, des cinq pages qui contiennent les recettes chiffrées les plus utiles : Attack (Flash Light), MusicRadar (Chameleon Odyssey ; Thriller Minimoog), Reverb (Bernie Worrell ; 5 Minimoog tracks) et Syntorial (G Thang lead, Rockit lead). Les données DX7 de la section 7 sont, elles, définitives : elles proviennent des cartouches Yamaha elles-mêmes.
