---
titre: "Rapport de recherche — axe 2 : synth brass analogique vintage (Minimoog, SH-101, Juno-60/106, OB-X) et cuivres FM (Chowning, DX7 BRASS 1-3)"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: rapport de recherche
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE 2 — Synth brass analogique vintage et cuivres FM

Rapport de recherche pour le skill « cuivres » (Ableton Live 12 + Serum 2). Rédigé le 2026-09-24.

Convention des tags : **[DOC]** = documenté par un constructeur ou une source primaire lue (texte d'article Sound On Sound lu intégralement, données d'usine décodées, chartes Roland transcrites) ; **[HEUR]** = plage de départ issue d'un tutoriel, d'un preset communautaire ou d'une déduction ; **[TEST]** = à valider dans le Set ; **[MÉMOIRE, non vérifié]** = vient de ma mémoire et n'a pas pu être vérifié sur une page lue.

---

## 0. Conditions de la recherche — à lire d'abord

Le proxy réseau de l'environnement bloque presque tout le web grand public : reverbmachine.com, soundonsound.com, reverb.com, musicradar.com, syntorial.com, attackmagazine.com, perfectcircuit.com, vintagesynth.com, wikipedia.org (y compris mobile), web.archive.org, archive.org, ccrma.stanford.edu, ableton.com, xferrecords.com, sequential.com, oberheim.com, roland.com, moogmusic.com, korg.com, usa.yamaha.com, kvraudio.com, gearspace.com, synthtopia.com, medium.com, fandom.com, righto.com, dsprelated.com, arxiv.org, huggingface.co. La liste détaillée est en section 5.

Seuls **github.com**, **raw.githubusercontent.com** et **gitlab.com** passent. La recherche s'est donc appuyée sur des sources primaires hébergées sur GitHub, ce qui, paradoxalement, a donné des données plus solides que des tutoriels :

1. **La banque ROM1A du Yamaha DX7** (fichier sysex `rom1a.syx`, 4104 octets, checksum vérifié 0x33 = 0x33), décodée par mes soins avec un script Python écrit pour l'occasion : les valeurs de BRASS 1, BRASS 2 et BRASS 3 sont donc lues **dans les données d'usine elles-mêmes**, pas dans une analyse tierce.
2. **La série Synth Secrets de Sound On Sound**, compilée en EPUB par un tiers sur GitHub (`dlemmon/synth-secrets`, les 63 parties) : j'ai extrait et lu intégralement les parties 24, 25, 26, 27 (cuivres), plus les passages cuivres/vibrato des parties 8 et 10. La partie 26 (Minimoog) a aussi été obtenue en texte intégral par un second miroir (`Pointhairedboss/Willickr`).
3. **Les 128 patches d'usine du Roland Juno-106** (sysex brut, 18 octets par patch, issus de `juno106_factory_patches.ser`) embarqués dans `shorepine/amy/amy/juno.py`, décodés avec la table de champs du même fichier.
4. **Les 56 chartes d'usine du Roland Juno-60** transcrites des fiches Roland dans `joshjetson/phosphor` (`juno.rs`), positions de curseurs en fraction 0–1.
5. **Les valeurs de l'exemple de cuivre de Chowning (1973)** via trois transcriptions indépendantes (tutoriel Csound, notebook musx de Rick Taube, documentation CLM de Bill Schottstaedt) — le PDF original (CCRMA) étant bloqué.
6. Des presets communautaires en texte lisible (OB-Xd en LV2/TTL, recettes Hydrasynth) pour Jump et les cuivres Oberheim — tous **[HEUR]**.
7. Les fiches locales du dépôt (Operator et Serum 2, rédigées à partir des manuels lors de sessions précédentes).

Ce qui n'a **pas** pu être lu : les articles Reverb Machine (Jump, Axel F, Vangelis), MusicRadar, Syntorial, le wiki « DX7 Brass », les fiches Prophet-5 / OB-Xa / Jupiter-8 / CS-80 / Polysix. Voir section 6.

---

## 1. Synth brass analogique 1970–80 : faits et valeurs chiffrées

### 1.1 La théorie de référence — Synth Secrets 24 et 25 (Gordon Reid, SOS avril–mai 2001)

Source lue : texte intégral des parties 24 et 25 dans l'EPUB `dlemmon/synth-secrets` (miroir GitHub de https://www.soundonsound.com/techniques/synthesizing-brass-instruments, lui-même bloqué). Tag **[DOC]** pour tout ce paragraphe.

- Un cuivre produit la **série harmonique complète** (perce conique/évasée) → « la dent de scie est la seule forme d'onde courante qui fasse de même » ; la carrée (harmoniques impaires) est « tout à fait inadaptée ».
- **Plus fort = plus d'harmoniques** : une note jouée doucement « ne contient que six harmoniques », la même note fortissimo « au moins quinze », et « la huitième harmonique domine la note sur-soufflée » (Part 24, Fig. 8). D'où : filtre passe-bas dont la coupure suit la loudness, **et résonance proportionnelle à la loudness** pour accentuer les harmoniques hautes.
- **Les notes aiguës ont moins d'harmoniques que les graves** → suivi de clavier du filtre **un peu inférieur à 1:1** ; Part 26 chiffre : « si la fréquence double, le filtre devrait s'ouvrir d'un facteur légèrement inférieur à deux… disons 190 pour cent ».
- **Contour d'amplitude** : ADS(R) classique convient ; le cas « plosif » (coup de langue en T/D) exige une double attaque A-(niveau)-A2-S que seuls des synthés numériques offrent ; l'attaque « instantanée » d'un ADSR analogique, arrondie par l'électronique, s'en approche. **Release très court** (« sur un cuivre, ce temps est très court »).
- **Vélocité → attaque plus courte** (« à mesure que la vélocité augmente, l'étage Attack raccourcit ») et vélocité → quantité d'enveloppe sur le filtre ; **aftertouch → brillance** pendant le sustain.
- **Contour de tonalité** : les harmoniques sous la coupure naturelle « atteignent leur niveau de sustain ensemble, et plus vite que celles au-dessus » (Fig. 11). Un simple AR sur le filtre donne un résultat « très peu convaincant » : il faut un **ADSR sur le filtre** pour recréer le « parp » initial.
- **Growl (instabilité d'attaque)** : le temps d'établissement de l'onde stationnaire dure « environ une douzaine de cycles », soit « environ **50 ms** » pour un do médian à 256 Hz. Reid **déconseille de moduler l'oscillateur** (cela crée des bandes latérales FM) et module **le filtre** avec un **triangle à environ 80 Hz**, via un VCA piloté par une enveloppe AD (courte). Il note qu'un LFO plafonné à 25 Hz est « inadéquat » pour ça.
- **Vibrato retardé** : « le vibrato ne se produit pas pendant le transitoire », donc « vibrato retardé… implémenté par une rampe AR contrôlant la quantité de modulation » ; « des fréquences de l'ordre de **5 Hz** sonnent le plus réaliste, et l'amplitude doit être **très faible**, sinon le timbre sonne électronique ».
- **Bruit** : un peu de bruit filtré par les formants ajoute du réalisme ; sur Minimoog et SH-101 le bruit blanc brut « sonne très artificiel » → à omettre (Parts 26 et 27).
- Phrase à retenir : « certains des plus grands sons de cuivres synthétisés sont sortis de synthés à ADSR, comme l'**ARP Odyssey**, le **Sequential Prophet 5**, l'**Oberheim OBX** et le **Moog Memorymoog** ».
- Part 10 (Modulation) chiffre les régimes de modulation du filtre : « ~0,1 Hz = balayage lent… 1 ou 2 Hz = effet wah-wah… **10 à 20 Hz = growl, superbe pour simuler les cuivres** ».
- Part 8 (More About Envelopes) : le « spit brass » (psst puis gonflement) est **impossible avec un ADSR**, parce que « le niveau maximal survient forcément à la fin de l'attaque » et « le sustain commence au niveau de fin de decay ». Il faut une enveloppe multi-segments avec un L1 inférieur au maximum (type DX7/EX800). Le **CS-80** est cité : son enveloppe de filtre a « **Initial Level**, **Attack Level**, plus Attack, Decay, Release », sans étage de sustain défini (structure héritée du GX-1).

### 1.2 Minimoog — recette complète de Gordon Reid (Synth Secrets 26, SOS juin 2001) **[DOC]**

Source lue : texte intégral (miroirs GitHub `Pointhairedboss/Willickr` et EPUB `dlemmon/synth-secrets`, de https://www.soundonsound.com/techniques/brass-synthesis-minimoog, bloqué).

| Section | Réglage (valeurs d'origine Minimoog) |
|---|---|
| Osc 1 | **dent de scie**, plage **4'** (une octave au-dessus du piano, pour trompette/cornet) ; Osc 2 inutilisé ; Osc 3 réservé à la modulation |
| Mixer | Osc 1 seul, niveau **5/10** (au-delà, l'oscillateur sature l'entrée du filtre) |
| Loudness Contour | **Attack 100 ms**, **Sustain 10/10** (le Decay devient sans effet), **switch Decay OFF** → release instantané |
| Filter | Cutoff **−5** (= 0 % : filtre fermé au repos), **Amount of Contour 6,5/10**, **Emphasis (résonance) 2/10**, Keyboard Control 1 + 2 **ON** = suivi **100 %** (options : 0 / 33,3 / 66,7 / 100 %) |
| Filter Contour | **Attack 600 ms, Decay 800 ms, Sustain 5/10**, release instantané |
| Growl | Osc 3 en **triangle**, plage **32'**, fine −1, switch Osc 3 keyboard **OFF** (fréquence fixe), Modulation Mix = 0 (Osc 3 seul, pas de bruit), Filter Modulation **ON**, quantité dosée à la **molette de modulation** à la main au début de la note |
| Vibrato | aucun LFO disponible : vibrato **manuel** à la molette de pitch |

Explication donnée : « comme le filtre s'ouvre plus lentement que l'ampli (l'attaque du filtre est à 600 ms), les harmoniques supérieures entrent une à une pendant environ une demi-seconde ». C'est **la** définition documentée du « wow » de cuivre : **attaque ampli ≈ 100 ms, attaque filtre ≈ 600 ms**, ratio ≈ 6.

Comparaison avec les *Minimoog Sound Charts* de Tom Rhea (1977, Norlin) rapportée par Reid : le **Trumpet** de Rhea utilise **les trois oscillateurs à l'unisson** (« add oscillators for progressively 'Fatter' tutti sounds »), attaque un peu plus lente, petit decay au relâchement, **suivi de clavier 66 %**, attaque de filtre plus rapide, cutoff initial plus haut, **pas de résonance**, Amount of Contour plus bas — Reid le juge « un peu étouffé ». Le **Tuba** de Rhea utilise **un seul oscillateur dent de scie** et **le bruit** (pas Osc 3) pour « rugueusifier » le filtre — « extrêmement efficace ». Le **Jazz Trombone** ajoute Osc 3 en vrai LFO sur le filtre **et** de la modulation d'oscillateur (vibrato).

Avertissement de Reid : « si vous vous éloignez trop de ces réglages — autre forme d'onde, attaques instantanées, forte résonance — rien ne sonnera cuivre ».

### 1.3 Roland SH-101 et ARP Axxe (Synth Secrets 27, SOS juillet 2001) **[DOC]**

- SH-101 : VCO **4'**, **dent de scie seule** (pulse, sub-osc et bruit à zéro ; Mod VCO à zéro). **VCA en mode Gate** (déconnecté de l'ADSR, contour carré) pour libérer l'unique ADSR au profit du **filtre** ; Env en mode **Gate** (pas Trig) pour ne pas retrigger en legato ; **Release ≈ 2** pour éviter le claquement. VCF : **Freq proche de zéro, Env au maximum ou presque, « juste une touche » de résonance, suivi clavier un peu sous 100 %**. Growl : LFO au **rate maximal**, **triangle**, fader Mod du VCF à environ **60 %** au début de la note, ramené à **0 %** quand le contour atteint le sustain (à la main).
- ADSR de référence SH-101 (repris pour l'Axxe) : **A 20 %, D 50 %, S 50 %, R 20 %**.
- Patches d'usine SH-101 analysés : le **Trumpet** du manuel Roland est « très décevant » (A/D trop courts, Env sur filtre trop faible, cutoff initial trop haut, aucune modulation) ; le **Tuba** est bien meilleur : **scie à 60 %** + **sub-oscillateur carré une octave dessous à 100 %** (« la scie seule manque de corps, le sub seul est creux »).
- ARP Axxe : scie au maximum, VCF Freq et Resonance « légèrement » relevés, ADSR→VCF élevé, Kybd CV modéré ; VCA piloté par l'ADSR (gain initial 0, sinon le son ne s'arrête jamais) ; ajustements finaux : **Decay plus long, Sustain plus bas, ADSR→VCF réduit** « pour accentuer le parp initial ». LFO plafonné à **20 Hz** → pas de growl possible, donc **vibrato ≈ 5 Hz** via le pad de pression PPC.

### 1.4 Roland Juno-60 — chartes d'usine (transcription des fiches Roland) **[DOC]** (transcription tierce, positions de curseurs 0–1)

Source lue : https://raw.githubusercontent.com/joshjetson/phosphor/main/crates/phosphor-dsp/src/juno.rs — « every slider position and switch state in BANK was measured from the printed panel of its chart ». Ordre des champs : lfo [RATE, DELAY] ; dco [LFO, PWM, SUB, NOISE] ; waves [pulse, saw, sub] ; range 1 = 8' ; vcf [FREQ, RES, ENV, LFO, KYBD] ; env [A, D, S, R] ; chorus 0/I/II.

| Charte | LFO rate / delay | DCO (LFO, PWM, sub, noise) | Ondes | VCF (freq, res, env, lfo, kybd) | VCA | ENV A/D/S/R | Chorus |
|---|---|---|---|---|---|---|---|
| **17 BRASS** | 0,511 / **0,665** | **0,168** / 0,008 / 0 / 0 | saw seule | **0,000** / 0,008 / **0,854** / 0,022 / 0,412 | env, niveau 0,692 | **0,258 / 0,398 / 0,623 / 0,217** | **I** |
| 18 PHASE BRASS | 0,608 / 0 | 0,008 / 1,000 (PWM par Env) / 0,992 / 0 | pulse + saw | 0,322 / 0,105 / 0,552 / 0,008 / 1,000 | gate, 0,412 | 0,238 / 0,440 / 0,440 / 0,322 | I |
| **42 TRUMPET** | 0,258 / **0,629** | **0,168** / 0,008 / 0 / 0,014 | saw seule | 0,014 / 0,022 / **0,846** / 0 / 0,420 | env, 0,700 | **0,146 / 0,406 / 0,588 / 0,217** | off |
| 43 HORN | 0,266 / 0,678 | 0,008 / 0,008 / 0,014 / 0 | saw seule | 0,217 / 0,008 / 0,552 / **0,203** / 0,412 | env, 0,714 | 0,398 / 0,497 / 0,580 / 0,343 | off |
| 52 WAH BRASS | 0,602 / 0,189 | 0,308 / 0,008 / 0 / 0,014 | saw seule | 0,315 / **0,706** / 0,440 / 0 / 0,580 | gate, 0,678 | 0,175 / 0,286 / 0,406 / 0,258 | off |

Lecture : le cuivre Juno-60 « canonique » = **scie seule, filtre fermé (0), enveloppe → filtre ≈ 85 %, résonance quasi nulle, suivi clavier ≈ 41 %, attaque ≈ 15–26 %, sustain ≈ 60 %, release court**, **vibrato retardé** (DCO LFO 0,168 avec **delay 0,63–0,67**) et chorus I sur le « BRASS » de section. Le HORN remplace le vibrato de hauteur par une **modulation LFO du filtre** (0,203). Le ratio « attaque de filtre plus lente que l'ampli » n'existe pas sur Juno (une seule enveloppe) : c'est **la quantité d'enveloppe sur le filtre et le cutoff à zéro** qui produisent le « wow ».

### 1.5 Roland Juno-106 — patches d'usine décodés depuis le sysex **[DOC]** (données Roland ; conversions en ms **[HEUR]**)

Source lue : https://raw.githubusercontent.com/shorepine/amy/main/amy/juno.py (liste `_PATCHES`, 128 patches, « juno106_factory_patches.ser ») + table de décodage du même fichier : 16 octets 0–127 dans l'ordre `lfo_rate, lfo_delay, dco_lfo, dco_pwm, dco_noise, vcf_freq, vcf_res, vcf_env, vcf_lfo, vcf_kbd, vca_level, env_a, env_d, env_s, env_r, dco_sub`, puis 2 octets de switches (plage 16'/8'/4', pulse, saw, chorus ; PWM manuel/LFO, polarité VCF, VCA gate/env, HPF). Le manuel Juno-106 (cité dans juno.py, p. 32) donne un decay max de **12 s**.

| Patch | Plage | Ondes | Sub | PWM | VCF freq / res / env / kbd | HPF | VCA | ENV A / D / S / R | LFO rate / delay / DCO-LFO | Chorus |
|---|---|---|---|---|---|---|---|---|---|---|
| **A11 Brass Set 1** | 16' | saw | 0 | 102 (manuel, pulse off) | **35 / 13 / 58 / 86** | 1 | env 108 | **3 / 49 / 45 / 32** | 20 / 49 / **0** | I |
| A12 Brass Swell | 8' | saw | 70 | 56 | 43 / 17 / 26 / 84 | 0 | env 75 | **64** / 118 / 38 / 37 | 6 / 48 / 0 | I |
| **A13 Trumpet** | 8' | saw | 0 | 102 | 55 / 34 / 24 / 59 | 2 | env 127 | **5 / 66 / 48 / 16** | **52 / 45 / 8** | off |
| A34 Brass III | 8' | saw | 22 | 35 | 66 / 24 / 11 / 12 | 0 | env 127 | **58** / 100 / **94** / 37 | 52 / 20 / 0 | I |
| A35 Fanfare | 16' | saw + pulse | 50 | 70 (LFO) | 44 / 0 / 32 / 67 | 0 | env 33 | **72** / 104 / 75 / 49 | 47 / 0 / 0 | I |
| A43 Brass Ensemble | 8' | saw | 31 | 102 | 46 / 44 / 29 / 59 | 1 | env 103 | 16 / 103 / 97 / 34 | 52 / 45 / 0 | I |
| **B31 Brass** | 8' | saw | 0 | 73 (LFO) | **0 / 0 / 94 / 127** | 0 | **gate** 72 | **3 / 44 / 51 / 11** | 51 / 127 / 0 | I |
| B55 Brass Ensemble | 8' | saw + pulse | 0 | 73 (LFO) | 47 / 34 / 35 / 65 | 0 | env 39 | 6 / 68 / 67 / 38 | 25 / 94 / 0 | I |
| B73 Meow Brass | 8' | saw | 0 | 73 (LFO) | 45 / **100** / 35 / 65 | 0 | gate 84 | 4 / 90 / 0 / 27 | 51 / 127 / 0 | off |
| B82 Piccolo Trumpet | 8' | saw | 0 | 73 (LFO) | 0 / 0 / 94 / 127 | 0 | gate 97 | 3 / 44 / 51 / 11 | 51 / 127 / 0 | off |

Conversions mesurées par l'auteur d'AMY sur les démos audio des presets d'usine **[HEUR]** : Attack 3 ≈ 30 ms, 8 ≈ 68 ms, 13 ≈ 100 ms, 23 ≈ 200 ms, 44 ≈ 355 ms, 58 ≈ 440 ms, 72 ≈ 600 ms ; Release 12 ≈ 86 ms, 16 ≈ 240 ms, 25 ≈ 340 ms, 37 ≈ 1000 ms, 49 ≈ 1200 ms ; LFO ≈ 0,6·2^(0,04·v) − 0,1 Hz (0,5–30 Hz) ; VCF freq ≈ 13·2^(0,0938·v) Hz.

Lecture : trois familles apparaissent nettement. **Stab** (A11, B31, B82) : attaque 3 (~30 ms), filtre presque fermé, enveloppe → filtre 58–94 %, sustain ≈ 45–51, release 11–32, **VCA en mode gate** sur B31/B82 (exactement l'astuce SH-101 de Reid). **Swell/pad** (A12, A34, A35) : attaque 58–72 (~440–600 ms), sustain 75–94, sub-oscillateur, chorus I. **Lead** (A13 Trumpet) : attaque 5, 8', **vibrato retardé** (DCO-LFO 8, delay 45, rate 52 ≈ 2,4 Hz selon la régression AMY), HPF 2, pas de chorus. Aucun patch cuivre Juno n'a de « pitch scoop » : la machine n'a pas d'enveloppe de hauteur.

### 1.6 Oberheim OB-X / OB-Xa et « Jump »

- **Faits [DOC] lus** : Synth Secrets 25 place l'« Oberheim OBX » parmi les synthés à ADSR ayant produit « certains des plus grands sons de cuivres synthétisés ». Synth Secrets 44 (miroir `juvation/synth_documents`) rappelle que Prophet 5, OBX, Jupiter 8 et Memorymoog **n'ont pas de sensibilité à la vélocité**.
- **Attribution [HEUR]** (aucune source primaire lue) : les résumés de recherche (Reverb.com, Wikipedia, MusicRadar — pages bloquées) affirment que l'OB-Xa apparaît dans le clip mais que l'enregistrement utiliserait l'**OB-X**, joué à travers un stack Marshall ; le README de `keunwoochoi/subtractive-synthesizers.js` dit « OB-Xa » en citant MusicRadar. **Contradiction non tranchée** : marquer [MÉMOIRE, non vérifié] toute affirmation OB-X vs OB-Xa.
- **Presets OB-Xd (émulation OB-X) lus en clair [HEUR]** — valeurs normalisées 0–1 de l'instrument OB-Xd, banque Zynthian :
  - « **Here Goes Jump** » (FMR Patch Book) — https://raw.githubusercontent.com/zynthian/zynthian-data/master/presets/lv2/Obxd_000-FMR_Patch_Book.presets.lv2/000-FMR_Patch_Book_Here_Goes_Jump_OB-Xd.ttl : osc1 **saw** + osc2 **saw**, **oscillator2detune 0,40**, unison 0, voicedetune 0, brightness 1,0, **cutoff 1,0**, **resonance 0,888**, fourpole 0 (**2 pôles**), filterkeyfollow 1,0, **filterenvamount 1,0**, ampli **A 0 / D 1,0 / S 1,0 / R 0**, filtre **A 0,156 / D 0,284 / S 0 / R 0,496**, LFO sinus 0,192, lfoamount1 0,028 (hauteur), lfoamount2 0,004, LFO→osc1+osc2 et →PW1/PW2, pulsewidth 0,288 (sans effet, pulses off), pans des 8 voix légèrement dispersés. Attention [TEST] : un cutoff à 1,0 **et** une enveloppe à 1,0 sont contradictoires (le filtre est déjà ouvert) ; à vérifier à l'oreille, la valeur stockée est peut-être une erreur du preset.
  - « **Dont Jump IW** » (KVR Brass Synths) — https://raw.githubusercontent.com/zynthian/zynthian-data/master/presets/lv2/Obxd_003-KVR_Brass_Synths.presets.lv2/003-KVR_Brass_Synths_Dont_Jump_IW.ttl : saw + saw, **osc2 detune 0,444**, portamento 0,368, brightness 1,0, **cutoff 0,288**, resonance 0,104, filter_warm 1, **filterenvamount 0,86**, ampli A 0 / D 0,596 / S 1,0 / R 0,576, filtre **A 0,28 / D 0,272 / S 0,508 / R 0,424**, LFO 0,336, vibrato 0,056, envelopedetune 0,024, filterdetune 0,104 (dispersion par voix). Recette plus « plausible » que la précédente.
  - « **Comp Horns OB-Xa** » (KVR Brass Synths) — https://raw.githubusercontent.com/zynthian/zynthian-data/master/presets/lv2/Obxd_003-KVR_Brass_Synths.presets.lv2/003-KVR_Brass_Synths_Comp_Horns_OB-Xa.ttl : osc1 **pulse** + osc2 **pulse**, PW 0,508, **hard sync on**, voicedetune 0,312, **cutoff 0,136**, resonance 0, **fourpole 1 (24 dB)**, filterenvamount 0,412, keyfollow 1,0, ampli A 0 / D 0 / S 1,0 / R 0,404, filtre **A 0,368 / D 0,376 / S 0,372 / R 0,312**, LFO 0,604, vibrato 0,036.
- Notes tierces **[HEUR]** (`mekedron/claude-amen-sessions`, document de synthèse non sourcé) : « OB-Xa : filtre commutable 12/24 dB ; le réglage **12 dB** donne la qualité 'section de cuivres' ; **unison** empilant les huit voix avec détune, c'est le son de Jump et de Subdivisions » ; rebuild proposé « 6–8 voix scie, spread **±15 cents**, LPF 12 dB, enveloppe de filtre **rapide et profonde**, accords plaqués ». À prendre comme point de départ seulement.

### 1.7 Roland Jupiter-8 / « Axel F »

- Rien de primaire lu. Résumé de recherche (pages bloquées) : lead Jupiter-8 « saw lead » avec portamento, **stabs de cuivres sur JX-3P**, basse Moog modulaire, marimba DX7, LinnDrum **[HEUR]**.
- Spec d'un projet d'émulation (`lukemosse/axelF`, https://raw.githubusercontent.com/lukemosse/axelF/main/AxelF_Synth_Spec.md, sans source citée) **[HEUR]** : lead « **DCO-1 scie 8', DCO-2 désaccordé ≈ 6 cents, unison** », filtre 4 pôles IR3109, patch « Axel Lead » : cutoff ≈ 65 %, résonance 15 %, enveloppe → filtre +30 %, Env 1 (filtre) **A 5 ms / D 400 ms / S 70 % / R 200 ms**, Env 2 (ampli) A 5 ms / D 0 / S 100 % / R 300 ms, vibrato à la molette, portamento 0–5 s en mode solo. JX-3P : chorus intégré **I (léger) / II (profond)** comme trait déterminant des stabs.

### 1.8 Prophet-5, CS-80, Polysix, Polymoog

- **Prophet-5** : cité par Reid parmi les meilleurs cuivres à ADSR [DOC] ; aucune fiche d'usine lue.
- **CS-80** : enveloppe de filtre à **Initial Level / Attack Level / A / D / R sans sustain** (Synth Secrets 8) [DOC] ; le reste (Vangelis, ribbon, aftertouch → brillance) n'est connu que par résumés et par la recette Hydrasynth « cs80_brass_swell » (section 4.9) [HEUR].
- **Polysix** : rien de lu au-delà de listes de noms.
- **Polymoog 203a** : huit presets d'usine « Strings, Piano, Organ, Harpsichord, Funk, Clavi, Vibes, **Brass** » (fiche `existential-engineering/catalog` citant vintagesynth.com) [HEUR].

---

## 2. Cuivres FM

### 2.1 Chowning 1973 — l'exemple « brass-like » (valeurs par transcriptions concordantes)

Le PDF original (https://ccrma.stanford.edu/sites/default/files/user/jc/fm_synthesispaper-2.pdf) est bloqué. Trois transcriptions indépendantes ont été lues ; elles concordent sur l'essentiel. Tag **[DOC] via transcription** :

1. **Tutoriel Csound** (https://raw.githubusercontent.com/mjladd/devcontainer-csound/main/docs/tutorials/singer_tutorial.md) : « Chowning's text specifies the parameters to be used for brass-like tones » → `i1 0 0.6 10000 440 440 0 5` = **durée 0,6 s, porteuse 440 Hz, modulatrice 440 Hz (ratio 1:1), I1 = 0, I2 = 5** ; enveloppe unique pour amplitude **et** index : `linseg 0, dur/6, 1, dur/6, .75, dur/2, .65, dur/6, 0` = **montée à 1 en 1/6 de la durée (100 ms), descente à 0,75 en 1/6, plateau à 0,65 pendant 1/2, retour à 0 en 1/6**. Déviation : `dev1 = I1·fm`, `dev2 = (I2 − I1)·fm`, index instantané = dev1 + dev2·env.
2. **Notebook musx** (Rick Taube, https://raw.githubusercontent.com/musx-admin/musx/main/tutorials/audio.ipynb) : `proto_fm(P3=.6, P5=440, P6=440, P7=0, P8=5, amp_env=[0,0, 1/12,1, 1/3,.6, 5/6,.5, 1,0], index_env=amp_env)` — mêmes ratio/index/durée, forme d'enveloppe légèrement différente (attaque en **1/12**, plateau à 0,5).
3. **Doc CLM** (Bill Schottstaedt, https://raw.githubusercontent.com/spurious/snd-mirror/master/fm.html) : `(fm 0 0.5 400 .5 1.0 5.0 '(0 0 20 1 40 .6 90 .5 100 0))` = ratio **1,0**, index max **5,0**, enveloppe 0→1 à 20 %, 0,6 à 40 %, 0,5 à 90 %, 0 à 100 %.

Principe documenté partout : **l'index de modulation suit la même enveloppe que l'amplitude** (« brass timbre emerges with parallel envelope shapes for index and amplitude »), ratio **1:1** → série harmonique complète. Autres exemples de la même famille, pour situer : bois `900/300 (1:1/3), I 0→2`, basson `500/100, I 0→1,5`, clarinette `900/600 (2:3), I 4→2` (index **décroissant**), cloche `200/280, I 0→10, 8–15 s, enveloppe exponentielle`.

Nord Modular Book (J. Clark, https://raw.githubusercontent.com/aolney/nord-modular-book/master/all.md) **[DOC]** : « pour émuler les cuivres en FM, mettez la fréquence du modulateur **égale** à celle de la porteuse ; utilisez un générateur d'enveloppe pour le niveau de modulation, d'où l'éclaircissement caractéristique pendant l'attaque » ; clarinette = modulateur à **2×** la porteuse avec **enveloppe inversée** ; basson = modulateur à un **sous-multiple**.

Csound Book (Fischman, `1115.sco`, https://raw.githubusercontent.com/ReneNyffenegger/csound-instruments/master/csound-book/11/1115.sco) **[DOC]** — « BRASS, AFTER CHOWNING (1973) » réinterprété : `i 1115 … 8.03 1 1.0007 8 2 1 41 41` = ratio **1 : 1,0007** (léger désaccord pour battement), **index max 8, min 2**, table d'index f41 : 0→1 en 86/512, 0,75 à 172, 0,6 à 426, 0 à 512 ; table d'amplitude f40 : 0→1 en 64/512, 0,75 à 128, 0,45 à 256, 0,2 à 384, 0 à 512.

### 2.2 Yamaha DX7 « BRASS 1 » — décodage direct de la ROM1A **[DOC]**

Fichier : https://raw.githubusercontent.com/benny-sparra/fm1-dx7-patch-importer/main/public/dx7-banks/factory/rom1a.syx (4104 octets, en-tête `F0 43 00 09 20 00`, checksum 0x33 vérifié). Script de décodage : `scratchpad/research/decode_dx7.py` (format packé 128 octets/voix, 17 octets par opérateur, ordre OP6→OP1). Deux dépôts tiers (`rueire/SoundGenerator`, `gpasquero/vx7`) donnent les mêmes valeurs globales (algorithme 22, feedback 7, LFO 37/0/5, PMS 3, transpose 24, PEG 84-95-95-60 / 50-50-50-50), ce qui confirme le décodage.

**BRASS 1 — globaux** : **Algorithme 22**, **Feedback 7 (max)**, Osc Key Sync ON, **Transpose 24 = C3**, Pitch EG rates 84/95/95/60 levels **50/50/50/50 (= aucune enveloppe de hauteur, donc aucun « scoop »)**, LFO **sinus, speed 37, delay 0, PMD 5, AMD 0, PMS 3**, sync off.

| OP | Ratio (coarse+fine) | Detune | Output Level | EG R1–R4 | EG L1–L4 | Key scaling (BP / LD / RD / RS) | AMS / KVS |
|---|---|---|---|---|---|---|---|
| **6** (modulateur avec feedback) | **1,00** | 0 | **82** | **49 / 99 / 28 / 68** | **98 / 98 / 91 / 0** | 39 / 54 −EXP / 50 −EXP / RS 4 | 0 / **2** |
| 5 (porteuse) | 1,00 | **+1** | 98 | 77 / 36 / 41 / 71 | 99 / 98 / 98 / 0 | 39 / 0 / 0 / 0 | 0 / 2 |
| 4 (porteuse) | 1,00 | 0 | 99 | 77 / 36 / 41 / 71 | 99 / 98 / 98 / 0 | 39 / 0 / 0 / 0 | 0 / 2 |
| 3 (porteuse) | 1,00 | **−2** | 99 | 77 / **76 / 82** / 71 | 99 / 98 / 98 / 0 | 39 / 0 / 0 / 0 | 0 / 2 |
| 2 (modulateur d'OP1) | **0,50** | +7 | 86 | 62 / 51 / 29 / 71 | 82 / 95 / 96 / 0 | 27 / 0 / 7 −EXP / 0 | 0 / 0 |
| 1 (porteuse) | **0,50** | +7 | 98 | 72 / 76 / 99 / 71 | 99 / 88 / 96 / 0 | 39 / 0 / 14 +LIN / 0 | 0 / 0 |

Topologie de l'algorithme 22 : le commentaire d'un import tiers lu (`Ethycs/symcrash_python_AP`, « DX7 algorithm 22 (engine carriers: Op1, Op3, Op4, Op5), feedback 7 ») confirme **quatre porteuses (1, 3, 4, 5)** ; que **OP6 module OP3, OP4 et OP5** et **OP2 module OP1** est [MÉMOIRE, non vérifié] (cohérent avec le fait que OP6 porte le feedback et que le feedback DX7 n'est que sur un modulateur).

Lecture du patch (mon analyse **[HEUR]** à partir des valeurs [DOC]) :
- Trois porteuses **1:1 légèrement désaccordées (−2, 0, +1)** + une porteuse à **0,5 (sous-octave, detune +7)** = le « battement chaud » du BRASS 1 ; c'est un **détune de porteuses**, l'équivalent FM des deux VCO désaccordés.
- **L'index** (OP6, niveau 82, feedback 7 → spectre proche d'une scie) suit une enveloppe **R1 = 49** (attaque nettement plus lente que celle des porteuses, R1 = 77) → **la brillance arrive après l'amplitude** : c'est exactement le « wow » de Reid et l'enveloppe d'index de Chowning, mais l'index ne redescend qu'un peu (L3 = 91) au lieu de 0,65.
- La porteuse 3 a un decay plus court (R2 76, R3 82) : petite « crête » d'attaque.
- Key scaling d'OP6 (−EXP des deux côtés du point 39) = **moins d'index dans le grave et l'aigu** → filtre implicite qui suit le clavier, comme le « 190 % » de Reid ; KVS 2 sur OP6 et sur les porteuses = **vélocité → brillance et niveau**.
- **Vibrato immédiat et léger** (PMD 5, delay 0) ; pas de vibrato retardé sur ce patch d'usine.

BRASS 2 (même algorithme 22, feedback 7) : toutes les ratios à **0,50**, detunes 0/+1/−2/−3/+7/+7, toutes les enveloppes **99 / 39 / 32 / 71 – 99 / 98 / 80–88 / 0** (attaque instantanée : une version « stab » de BRASS 1), PMD 0.
BRASS 3 : **algorithme 18, feedback 6**, transpose 12, LFO triangle speed 35 PMD 5, OP6 ratio **8,47**, OP5 **3,18**, OP1–4 à 1,00, rate scaling élevé sur OP6 — un cuivre plus « cor » avec composantes inharmoniques dans l'attaque (L2–L4 d'OP6 = 0 : la composante 8,47 ne vit que dans le transitoire).

Précaution : les rates/levels DX7 (0–99) ne sont **pas** des millisecondes ; je n'ai lu aucune table de conversion fiable → laisser en valeurs d'origine et calibrer à l'oreille [TEST].

### 2.3 Traduction dans Ableton Operator

Faits **[DOC]** issus de la fiche locale `.claude/skills/sound-designer-serum/references/ableton-instruments.md` (rédigée depuis le manuel Live, §30.9) : 4 oscillateurs, **11 algorithmes** (le manuel ne les décrit que par une image ; lecture géométrique locale : n° 9 = D→(A, B et C) ; n° 8 = B→A et D→C ; n° 7 = (B+C+D)→A ; n° 11 = additif) ; **Feedback disponible sur tout oscillateur non modulé** ; une enveloppe par oscillateur avec **trois temps et trois niveaux** (Attack/Decay/Release + Init/Peak/Sustain), attaque linéaire, decay/release exponentiels ; **FM Drive** comme cible de modulation (« module le volume de tous les oscillateurs qui en modulent d'autres ») ; filtre avec Freq < Env (100 % ≈ 9 octaves) ; LFO jusqu'en audio (8 Hz–12 kHz) ; **Voices = 1 → legato sans retrigger** ; Glide polyphonique ; **Spread** (deux voix panées/désaccordées). Fixed mode jusqu'à 0,1 Hz, quantize des ratios (`Q`).

Mapping proposé **[HEUR]** :
- **Chowning brass** (2 opérateurs) : algorithme B→A (n° 8 ou tout algo à pile de deux), A et B sinus, **Coarse 1 / Fine 0 sur les deux** (1:1), enveloppe de **B** (= index) avec Attack ≈ **100 ms** (1/6 de 0,6 s), Peak 100, Decay ≈ 100 ms vers Sustain ≈ **65–75 %**, Release ≈ 100 ms ; enveloppe de A parallèle ; **B Level** fixe l'index max (la valeur qui donne I ≈ 5 se règle à l'oreille [TEST] : le manuel ne chiffre pas l'index).
- **BRASS 1 approché** : **algorithme 9 (D → A, B, C)**, A/B/C sinus Coarse 1 avec **Fine 1–3** de dispersion (Operator : ratio = Coarse + Fine/1000 [MÉMOIRE, non vérifié]), **D sinus Coarse 1, Feedback élevé** (le feedback n'est autorisé que sur D ici, non modulé), enveloppe de D : Attack plus lente que celle des porteuses (ordre de grandeur **80–150 ms contre 20–40 ms** [HEUR], calibré sur R1 49 vs 77), Sustain ≈ 90 %. La paire OP2→OP1 à 0,5 (sous-octave) ne tient pas dans le même algorithme : soit **deux instances Operator dans un Rack**, soit un oscillateur A en Coarse 0,5 (Operator accepte 0,5) sans son propre modulateur.
- **Vélocité → index** : « Lev < Vel » sur D ; **key scaling** de l'index : « Lev < Key » négatif sur D ; vibrato : LFO sinus ≈ 5–6 Hz vers la hauteur, amount faible, avec l'**enveloppe du LFO** pour le retard (Operator a une enveloppe de LFO [DOC]).
- Filtre d'Operator en sortie pour le « wow » analogique si l'on veut un hybride : Play by Key (466 Hz, Freq < Key 100 %) puis Freq < Env avec attaque plus lente que l'ampli.

### 2.4 Traduction dans Serum 2

Faits **[DOC]** issus de la fiche locale `.claude/skills/sound-designer-serum/references/moteurs-synthese.md` (manuel Serum 2) : la FM est un **warp mode** ; sources : **FM / PD / AM / RM depuis l'oscillateur B ou C, le Noise, le Sub, le Filter 1 ou 2** ; trois variantes : **Linear** (garde la hauteur, « propre, musical »), **Exp** (plus brillant/dur), **Thru-Zero** (inversion de phase quand la porteuse passe sous zéro) ; unison jusqu'à 16 voix, BLEND défaut 75 %.

Mapping proposé **[HEUR]** :
- **Chowning brass** : Osc A sinus (table Basic Shapes, position sinus), **Warp = FM (from B)**, Osc B sinus **même octave/semi/fine (1:1)** ; **Warp amount = index**, modulé par **Env 2** avec la forme 1/6 – 1/6 – 1/2 – 1/6 (Attack ≈ 100 ms, Decay ≈ 100 ms vers Sustain ≈ 70 %, Release ≈ 100 ms pour une note de 0,6 s) ; Env 1 (ampli) même forme. Mode **Linear** (la PM du DX7 garde la hauteur ; Exp introduit une dérive de hauteur). [TEST] : vérifier si le **niveau de B dans le mixeur** doit rester à 0 (B ne sert que de modulateur) et à quelle valeur de Warp l'index atteint l'équivalent de 5.
- **BRASS 1 approché** : Osc A sinus, **unison 3–4 voix, detune très faible** (l'équivalent des porteuses −2/0/+1) ; **FM (from B)** avec B sinus 1:1 ; pas de feedback d'opérateur dans Serum 2 [MÉMOIRE, non vérifié] → compenser la richesse du feedback 7 en prenant **B = scie** au lieu de sinus (le feedback DX7 tend le modulateur vers une scie) ou en ajoutant un **Warp Distortion** léger sur B ; Osc C (ou Sub) à −12 st pour la paire 0,5 ; **Velocity → Warp amount** (KVS 2) ; **Note → Warp amount négatif** de part et d'autre de C3 (key scaling) ; LFO 1 sinus ≈ 5–6 Hz vers la hauteur, amount faible, **Rise** du LFO pour le retard.
- Ajouter un **filtre ladder (MG Low 24)** derrière la FM avec Env 3 → cutoff plus lente que l'ampli reproduit le « wow » analogique sur un corps FM (hybride 80s).

---

## 3. Techniques transversales du synth brass — ce que disent les sources lues

1. **Le « wow » = enveloppe de filtre qui s'ouvre après l'ampli** [DOC] : Minimoog de Reid **ampli 100 ms / filtre 600 ms** (ratio ~6), decay filtre 800 ms, sustain 5/10, cutoff initial 0, amount 6,5/10 ; SH-101 : VCA en gate (instantané) + ADSR 20/50/50/20 % sur le filtre à Env max ; Juno-60 « 17 BRASS » : cutoff **0**, Env→VCF **0,854**, A 0,258 ; Juno-106 B31 : cutoff **0**, Env **94/127**, kbd 127, VCA gate ; DX7 BRASS 1 : attaque de l'index (R1 49) plus lente que celle des porteuses (R1 77). Dans les deux mondes, la brillance arrive **après** le niveau. Chowning : même forme pour index et amplitude, mais l'index part de 0 alors que l'amplitude aussi — la « lenteur » vient de ce que l'oreille perçoit la brillance monter pendant les 100 ms d'attaque.
2. **Le petit glissement de hauteur d'attaque (« scoop »)** : **absent des recettes documentées**. Reid déconseille explicitement toute modulation de l'oscillateur au début de la note (bandes latérales) et préfère un growl **sur le filtre** (triangle ~80 Hz pendant ~50 ms, ou 10–20 Hz) [DOC] ; le DX7 BRASS 1/2/3 a une **pitch EG plate (50/50/50/50)** [DOC] ; les Juno n'ont pas d'enveloppe de hauteur [DOC]. Le scoop est donc une habitude de tutoriel moderne **[HEUR]** ; s'il est utilisé, le garder minuscule et court ([TEST] : −20 à −50 cents sur 20–40 ms [HEUR]).
3. **Vibrato retardé** [DOC] : Reid ≈ **5 Hz, amplitude très faible, rampe AR** ; Juno-60 17 BRASS / 42 TRUMPET : DCO-LFO 0,168 avec **LFO delay 0,63–0,67** ; Juno-106 A13 Trumpet : DCO-LFO 8/127, delay 45/127, rate 52 (≈ 2,4 Hz selon régression AMY [HEUR]) ; DX7 BRASS 1 : PMD 5 sans delay (léger, immédiat). Vibrato **manuel** (molette, aftertouch, PPC) jugé « bien plus naturel » par Reid.
4. **Détune de deux oscillateurs** : Reid, pour une **trompette solo**, l'interdit (« l'interaction de deux oscillateurs… est tout à fait non représentative de l'instrument ») et n'utilise **qu'un oscillateur** [DOC] ; Rhea (Minimoog Sound Charts) empile **3 oscillateurs à l'unisson** pour un tutti « plus gras » [DOC] ; les presets Jump communautaires : osc2 detune **0,40–0,44** (unités OB-Xd) ; Axel-F spec : **≈ 6 cents** ; notes tierces : **6–12 cents** (Jupiter), **±15 cents** en unison OB-Xa ; DX7 BRASS 1 : porteuses à −2/0/+1 unités de detune. Règle qui ressort : **solo = 1 oscillateur (ou detune ≤ 6 cents), section = 2–3 oscillateurs / unison + chorus** [HEUR].
5. **Stab vs pad vs lead** (données Juno-106 d'usine [DOC], section 1.5) : **stab** = attaque ≈ 30 ms, filtre fermé, enveloppe→filtre 60–94 %, sustain ≈ 45–50, release 50–250 ms, souvent VCA gate ; **pad/swell** = attaque 440–600 ms, sustain 75–95, sub-osc, chorus I ; **lead** = attaque ≈ 50 ms, 8', vibrato retardé, HPF léger, pas de chorus, résonance un peu plus haute (34/127). Reid (Part 27) : jouer **staccato** pour un cuivre « tongué », **legato sans retrigger** (Env en Gate) pour un changement de piston.
6. **Résonance** : faible partout — Reid **2/10** (« un léger bump »), Juno-60 brass **0,008–0,022**, Juno-106 A11 **13/127**, Comp Horns 0, Dont Jump 0,104. Exception : « Here Goes Jump » à 0,888 (douteux) et « Meow Brass » 100/127 (effet spécial). Reid : « une forte résonance… rien ne sonnera cuivre ».
7. **Suivi de clavier du filtre** : 100 % (Minimoog, faute de mieux), idéal « un peu sous 100 % » (190 %/octave) [DOC] ; Juno-60 brass **0,41**, Juno-106 A11 **86/127**, B31 **127/127**, presets OB-Xd **1,0**.
8. **Chorus/ensemble** : Juno-60 « BRASS » et 7 des 11 cuivres Juno-106 d'usine sont en **chorus I** [DOC] ; JX-3P chorus I/II décrit comme déterminant pour les stabs d'Axel F [HEUR].
9. **Erreurs classiques** (Reid, [DOC]) : onde carrée ou triangle (spectre creux) ; attaques instantanées sur le filtre ; forte résonance ; noise blanc brut (« très artificiel ») ; vibrato trop profond (« électronique ») ; oublier le growl → son « statique, ennuyeux » ; sur ARP, VCA Gain > 0 (le son ne s'arrête jamais). Reid : « Synthesis is not just about sounds; it's also about performance ».

---

## 4. Recettes complètes trouvées, paramètre par paramètre

**R1 — Trompette Minimoog (Reid, SOS Synth Secrets 26) [DOC]** — source : https://www.soundonsound.com/techniques/brass-synthesis-minimoog (lu via https://github.com/dlemmon/synth-secrets et le miroir Willickr). Voir tableau §1.2 : Osc1 saw 4' ; mixer 5 ; Loudness A 100 ms, S 10, Decay switch off ; Filter cutoff −5, contour 6,5, emphasis 2, KB 1+2 on ; Filter contour A 600 ms / D 800 ms / S 5 ; Osc3 triangle 32' fine −1, KB off, Mod Mix 0, Filter Mod on, molette.

**R2 — Cuivre SH-101 (Reid, SOS Synth Secrets 27) [DOC]** — VCO 4' saw seule ; VCA Gate ; Env Gate, A 20 % / D 50 % / S 50 % / R 2 (≈ 20 %) ; VCF Freq ≈ 0, Env ≈ max, résonance « une touche », Kybd un peu < 100 % ; LFO triangle rate max, Mod VCF 60 % → 0 % à la main ; Bender VCO faible pour vibrato manuel.

**R3 — Cuivre ARP Axxe (Reid, SOS 27) [DOC]** — saw max ; VCF Freq et Res « légèrement » ; ADSR→VCF élevé ; Kybd CV modéré ; VCA Gain 0, ADSR→VCA on ; ADSR ≈ 20/50/50/20 % puis **Decay plus long, Sustain plus bas, ADSR→VCF réduit** ; LFO ≈ 5 Hz sinus vers VCO via PPC.

**R4 — Juno-60 chartes d'usine 17 BRASS / 42 TRUMPET / 43 HORN / 52 WAH BRASS [DOC]** — https://raw.githubusercontent.com/joshjetson/phosphor/main/crates/phosphor-dsp/src/juno.rs — tableau §1.4.

**R5 — Juno-106 patches d'usine A11, A12, A13, A34, A35, A43, B31, B55, B73, B82 [DOC]** — https://raw.githubusercontent.com/shorepine/amy/main/amy/juno.py — tableau §1.5 (valeurs brutes 0–127, conversions ms [HEUR]).

**R6 — OB-Xd « Here Goes Jump », « Dont Jump IW », « Comp Horns OB-Xa » [HEUR]** — URLs et valeurs §1.6.

**R7 — DX7 BRASS 1 (et 2, 3) [DOC]** — tableau §2.2, source `rom1a.syx` décodée.

**R8 — Chowning brass [DOC via transcription]** — §2.1 : c = m = 440 Hz, I 0→5, 0,6 s, enveloppe 1/6–1/6–1/2–1/6 (1 / 0,75 / 0,65 / 0).

**R9 — Recettes Hydrasynth (curated, `TheAndrewStaker/mcp-midi-control`) [HEUR]** — https://raw.githubusercontent.com/TheAndrewStaker/mcp-midi-control/main/packages/core/src/protocol-generic/recipes/patchArchetype.curated.ts (auteur : « generalized starting point, not a verbatim clone », cite SOS 26, Perfect Circuit, Synthtopia « How To Program A Yamaha CS-80 », MusicRadar) :
- `cs80_brass_swell` : 2 saws (osc2 +8 cents) + saw −12 st (60 %), LP Ladder 24, cutoff 30, res 22, **env→filtre +50**, keytrack 40, Env1 (filtre) attack 2560 / decay 1280 / sustain 70 / release 7680 (indices), Env2 (VCA) attack 1920 / sustain 110 / release 10000, voicedensity 2 detune 12, chorus 55 %, Hall 4 s 35 %, LFO 5,77 Hz ; **aftertouch → cutoff**.
- `fm_september_brass` (DX7-like) : 2 saws (+6 cents), **FM-Linear ratio unité (1:1), depth 4600, feedback 1800**, LP Ladder 24 cutoff 30 res 14 **env +48**, keytrack 88, drive 28, Env1 A 14 / D 576 / S 40 / R 128, Env2 A 6 / D 160 / S 120 / R 144, chorus 35 %, room 3,1 s 14 %.
- `fm_soft_horn_swell` : saw + triangle (+8 c) + saw −12 ; FM-Linear 1:1 depth 2600 feedback 700 wet 80 ; LP Ladder 12 cutoff 52 env +42 ; Env1 A 320 / D 1280 / S 70 / R 2560 ; Env2 A 40 / D 640 / S 110 / R 2304 ; glide 12 ; chorus 45 %, Hall 6,5 s.

**R10 — Spec « Axel Lead » Jupiter-8 (lukemosse/axelF) [HEUR]** — §1.7.

---

## 5. Pages et fichiers consultés

### Lus avec succès (contenu réellement lu)
1. `rom1a.syx` — https://raw.githubusercontent.com/benny-sparra/fm1-dx7-patch-importer/main/public/dx7-banks/factory/rom1a.syx (téléchargé, checksum OK, décodé).
2. https://raw.githubusercontent.com/rueire/SoundGenerator/main/dx7_analysis/generate_syx/generate_syx.py (en-tête BRASS 1 : alg 22, fb 7, LFO, PEG — concordant).
3. https://raw.githubusercontent.com/gpasquero/vx7/main/presets/factory.py (résumé partiel obtenu : alg 22, fb 7, LFO 37/0/5 sinus).
4. Dépôt https://github.com/dlemmon/synth-secrets cloné ; EPUB « Synth Secrets.epub » (63 parties) — parties **24, 25, 26, 27, 8, 10** extraites et lues ; 51–53 sondées (flûtes/pan pipes, hors sujet).
5. Texte intégral Synth Secrets 26 via https://github.com/Pointhairedboss/Willickr (`SyntheoryGordonReid/25_Brass Synthesis On A Minimoog.md`) et fragments SOS 44/21/13 via https://github.com/juvation/synth_documents.
6. https://raw.githubusercontent.com/shorepine/amy/main/amy/juno.py (128 patches Juno-106 + décodeur + mesures A/D/R).
7. https://raw.githubusercontent.com/joshjetson/phosphor/main/crates/phosphor-dsp/src/juno.rs (56 chartes Juno-60).
8. https://raw.githubusercontent.com/mjladd/devcontainer-csound/main/docs/tutorials/singer_tutorial.md (Chowning brass/bell en Csound).
9. https://raw.githubusercontent.com/mjladd/devcontainer-csound/main/docs/tutorials/survey_classic_synthesis_techniques.md (Csound Book, recettes Chowning).
10. https://raw.githubusercontent.com/ReneNyffenegger/csound-instruments/master/csound-book/11/1115.sco (BRASS after Chowning, tables f40/f41).
11. https://raw.githubusercontent.com/musx-admin/musx/main/tutorials/audio.ipynb (proto_fm de Chowning, 7 exemples).
12. https://raw.githubusercontent.com/spurious/snd-mirror/master/fm.html (CLM, Schottstaedt).
13. https://raw.githubusercontent.com/aolney/nord-modular-book/master/all.md (§2.2 FM brass/clarinet/bassoon).
14. https://raw.githubusercontent.com/zynthian/zynthian-data/master/presets/lv2/Obxd_000-FMR_Patch_Book.presets.lv2/000-FMR_Patch_Book_Here_Goes_Jump_OB-Xd.ttl
15. https://raw.githubusercontent.com/zynthian/zynthian-data/master/presets/lv2/Obxd_003-KVR_Brass_Synths.presets.lv2/003-KVR_Brass_Synths_Dont_Jump_IW.ttl
16. https://raw.githubusercontent.com/zynthian/zynthian-data/master/presets/lv2/Obxd_003-KVR_Brass_Synths.presets.lv2/003-KVR_Brass_Synths_Comp_Horns_OB-Xa.ttl
17. https://raw.githubusercontent.com/TheAndrewStaker/mcp-midi-control/main/packages/core/src/protocol-generic/recipes/patchArchetype.curated.ts
18. https://raw.githubusercontent.com/lukemosse/axelF/main/AxelF_Synth_Spec.md
19. https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/10-instruments/03-analog-polysynths.md (notes non sourcées).
20. https://gist.github.com/bryc/e997954473940ad97a825da4e7a496fa (32 algorithmes DX7 en image seulement — sans valeur de patch).
21. Fiches locales : `.claude/skills/sound-designer-serum/references/ableton-instruments.md` (§2 Operator), `moteurs-synthese.md` (§2 FM, Serum 2 warp), `fiches-pratiques.md` (contrainte ADSR de Reid), `studio-grade-brass-sound-design/references/output-schema.md` (format de tags).
22. Recherches GitHub (code search) ayant fourni des fragments cités : `Ethycs/symcrash_python_AP` (commentaire alg 22 carriers), `keunwoochoi/subtractive-synthesizers.js` (README), `existential-engineering/catalog` (Polymoog).

### Échecs (bloqués par le proxy « EGRESS_BLOCKED », sauf mention)
- https://reverb.com/news/the-synth-sounds-of-van-halens-jump
- https://www.soundonsound.com/techniques/synthesizing-brass-instruments
- https://reverbmachine.com/blog/vangelis-blade-runner-synth-sounds/ ; https://reverbmachine.com/blog/vangelis-tears-in-rain-blade-runner/
- https://synthesizer-design.fandom.com/wiki/DX7_Brass
- https://www.musicradar.com/tuition/tech/how-to-make-a-van-halen-jump-style-synth-sound-213604 ; https://www.musicradar.com/tuition/tech/get-the-sound-of-harold-faltermeyers-axel-f-541573
- https://www.syntorial.com/preset-recipe/van-halen-jump-brass/
- https://en.wikipedia.org/wiki/Jump_(Van_Halen_song) ; https://en.m.wikipedia.org/wiki/Jump_(Van_Halen_song) ; …/Axel_F ; …/Yamaha_CS-80
- https://ccrma.stanford.edu/sites/default/files/user/jc/fm_synthesispaper-2.pdf
- https://www.dsprelated.com/freebooks/sasp/Frequency_Modulation_FM_Synthesis.html
- https://www.perfectcircuit.com/signal/what-is-fm-synthesis
- https://www.synthtopia.com/content/2009/06/30/van-halen-jump-demo-oberheim-obx-a/
- https://www.vintagesynth.com/oberheim/ob-xa
- https://djjondent.blogspot.com/2019/10/yamaha-dx7-algorithms.html
- https://www.kvraudio.com/forum/viewtopic.php?t=73801&start=285 ; https://gearspace.com/… (Jump soft synth)
- https://www.presetpatch.com/articles/van-halen-jump-patch-tutorial
- https://www.righto.com/2021/11/reverse-engineering-yamaha-dx7.html
- https://web.archive.org/… (fetch impossible) ; https://archive.org/… ; https://arxiv.org/abs/2104.12922 ; https://huggingface.co/datasets
- http://www.codemist.co.uk/AmsterdamCatalog/20/index.html
- https://www.ableton.com/en/manual/live-instrument-reference/ ; https://xferrecords.com/products/serum-2
- https://medium.com/music-engineering/notes-i-synth-secrets-e32dc342e65f ; https://asb2m10.github.io/dexed/
- https://usa.yamaha.com/…/micro_tutorial/20170525/ ; https://sequential.com/product/prophet-5/ ; https://oberheim.com/products/ob-x8/ ; https://www.roland.com/global/products/rc_jupiter-8/ ; https://www.attackmagazine.com/technique/synth-secrets/ ; https://www.moogmusic.com/synthesizers/minimoog-model-d/ ; https://www.korg.com/us/products/synthesizers/polysix/
- https://pypi.org/project/mido/ (« Client Challenge », inutile) ; https://music.stackexchange.com/… (fetch impossible)
- 404 : https://raw.githubusercontent.com/asb2m10/dexed/master/Documentation/dx7_rom_cartridges.md ; https://raw.githubusercontent.com/Ursinus-CS472A-S2021/CoursePage/main/ClassExercises/Week4/Week4_Envelopes/index.html
- https://raw.githubusercontent.com/ales27pm/junoNATIVE/main/src/patches/factoryPatches.ts : accessible mais octets sysex remplacés par des placeholders (inutilisable).

---

## 6. Ce qui n'a pas été trouvé

1. **Les articles Reverb Machine** (Jump, Axel F, synthwave brass, Prince, Michael Jackson, Vangelis) : aucun miroir GitHub ; leurs recettes restent à vérifier depuis une machine sans proxy.
2. **Une source primaire sur le synthé exact de « Jump »** (OB-X vs OB-Xa, Marshall) : seulement des résumés de moteur de recherche et un README tiers. Aucune fiche d'usine OB-X/OB-Xa (patch sheets) en texte.
3. **Le preset brass d'usine du Prophet-5** (Rev 3 program charts) et **du Jupiter-8** : rien en texte sur GitHub ; les presets Repro-5 / TAL-J-8 ne sont pas publiés en clair. Seuls les 500 programmes Prophet-6 (sysex Sequential) existent décodés dans `joshjetson/phosphor`, non exploités ici (autre machine, byte map à reconstruire).
4. **CS-80** : panneau des presets fixes (« Brass 1/2/3 ») et réglages Vangelis : rien de primaire ; seule la structure IL/AL/A/D/R de l'enveloppe de filtre (SOS 8) est documentée.
5. **Polysix** et **Polymoog** : aucune valeur de patch ; seul le nom du preset Brass du Polymoog.
6. **Le papier de Chowning lui-même** : valeurs obtenues par trois transcriptions concordantes (ratio 1:1, I 0→5, 0,6 s), mais la forme exacte de l'enveloppe de la figure diverge légèrement entre transcriptions (attaque 1/6 vs 1/12 de la durée) : à trancher sur le PDF.
7. **La topologie exacte de l'algorithme 22 du DX7** (OP6 → OP3/4/5, OP2 → OP1) : porteuses confirmées par un commentaire tiers, routage des modulateurs de mémoire.
8. **Table de conversion des rates DX7 en millisecondes**, et **valeur d'index FM chiffrée** dans Operator/Serum 2 (les manuels ne donnent pas l'index) : calibration à l'oreille [TEST].
9. **Manuel Serum 2 en direct** (xferrecords.com bloqué) : le comportement du niveau de l'oscillateur B en mode « FM from B » et l'existence d'un feedback d'opérateur restent [TEST]/[MÉMOIRE].

---

## 7. Fichiers produits dans le scratchpad (`…/scratchpad/research/`)

- `rom1a.syx` — banque DX7 ROM1A (sha256 91416e81…104d), `decode_dx7.py` — décodeur (sortie BRASS 1/2/3 complète).
- `amy_juno.py` — patches Juno-106 + décodeur ; `phosphor_juno.rs` — chartes Juno-60 ; `nord_modular_book.md` ; `polysynths.md`.
- `synth-secrets/` — clone du dépôt, `synth-secrets/epub_full/ch024.txt … ch027.txt, ch008.txt, ch010.txt` — textes extraits des parties SOS.
