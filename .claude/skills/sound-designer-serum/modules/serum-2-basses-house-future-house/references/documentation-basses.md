# Documentation de fond pour concevoir une basse

Relevé du 4 octobre 2026. Ce fichier rassemble des faits **vérifiables** (physique, perception, synthèse) qui expliquent pourquoi une recette de `families.md` sonne comme elle sonne. Il complète `../../../references/basses.md` (sources chiffrées sur sub, Reese, growl, 808) et `../../../references/ressources.md` (index de Synth Secrets, manuel Serum 2, FabFilter Learn), sans les répéter. Les tutoriels vidéo sont dans `tutoriels-a-consulter.md`.

**Étiquettes.** [LU] : fait relevé dans une page réellement lue, source citée. [CALCUL] : obtenu par une formule d'une source lue, recalculé dans cette session. [DÉDUCTION] : conséquence pour Serum 2 tirée par Claude, à vérifier à l'oreille par l'utilisateur. Aucune valeur de ce fichier n'a été entendue.

**Pages lues.** En session cloud, seuls GitHub et raw.githubusercontent.com répondaient : le miroir Markdown de *Synth Secrets* (Gordon Reid, Sound On Sound, 1999-2004, [github.com/micjamking/synth-secrets](https://github.com/micjamking/synth-secrets), numérotation propre au miroir, parties 60 à 62 tronquées), la fonction [iso226.m](https://github.com/IoSR-Surrey/MatlabToolbox/blob/master/+iosr/+auditory/iso226.m) de l'université de Surrey (paramètres de la norme ISO 226:2003) et le README de [pdsynth](https://github.com/keithadler/pdsynth) (code tiers, pas une documentation Casio). Tous les autres sites essayés (Wikipedia, arXiv, DAFx, Sound On Sound, Xfer, EDMProd…) étaient bloqués.

## 1. FM et modulation de phase : hollow, métallique, tearout

- [LU] Les composantes d'une FM sinusoïdale tombent à fc ± n·fm ; leur position ne dépend que du modulateur, leur amplitude de l'indice β = Δf / fm, qui croît avec le niveau du modulateur et baisse quand sa fréquence monte. Largeur utile : B = 2·fm·(1 + β) ; exemple de l'article : 500 Hz modulé par 300 Hz avec β = 5 donne environ 3 600 Hz et 24 composantes. Avec β ≤ 0,1 le résultat ressemble à de l'AM. ([SS 12](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-12.md))
- [LU] Amplitude de la bande d'ordre n : fonction de Bessel Jn(β) ; les fréquences négatives se replient avec la phase inversée. ([SS 13](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-13.md))
- [CALCUL] J0…J3 : β = 1 → 0,765 / 0,440 / 0,115 / 0,020 ; β = 2 → 0,224 / 0,577 / 0,353 / 0,129 ; β = 5 → −0,178 / −0,328 / 0,047 / 0,365. La porteuse s'éteint vers β ≈ 2,405 (premier zéro de J0) : en montant la FM, la fondamentale peut **baisser** puis revenir.
- [LU] Rapport porteuse:modulateur (SS 13) : 1:1 → toute la série harmonique, proche d'une scie ; **1:2 → harmoniques impairs seulement, son « hollow » proche d'un carré** ; 1:3 → proche d'une impulsion à 33 % ; 1:4 → impairs, proche d'un carré ; rapport non entier → spectre inharmonique, la porteuse n'est plus la composante la plus grave. Un opérateur rebouclé sur lui-même donne une scie ; deux modulateurs sur une porteuse additionnent leurs spectres.
- [LU] Si le modulateur suit le clavier, le timbre reste le même sur toute la tessiture ; un modulateur à fréquence fixe rend chaque note différente et inharmonique. (SS 11 et 12)
- [CALCUL] Traduction dans Serum 2, osc A porteuse, osc B modulateur à hauteur relative : B à +12 demi-tons (1:2) → composantes 1, 3, 5, 7… × fA ; B à +24 (1:4) → impairs aussi ; **B à −12 (1:0,5) → composantes à 0, 0,5, 1, 1,5, 2… × fA** : série de fA / 2, donc une octave plus grave, plus une composante continue ; B à +7 (1:1,498, tempérament égal) → presque une série de fA / 2, légèrement inharmonique.
- [DÉDUCTION] Hollow Future House (fiche 3) : B à +12 ou +24 et FM faible. Basse métallique, donk, tearout (fiches 9, F11) : rapport non entier ou FM forte, en vérifiant la fondamentale perçue note par note. FM avec B à −12 : surveiller l'octave perçue et filtrer le continu (coupe-bas très bas) avant la distorsion.
- [LU] Distorsion de phase type Casio CZ, d'après l'implémentation tierce pdsynth : lecture d'un sinus à phase courbée ; DCW à 0 donne le sinus pur ; huit formes (saw, square, pulse, double sine, saw pulse, reso saw, reso triangle, reso trapezoid) ; les formes « reso » y balaient un formant du 3e au 13e harmonique. À rapprocher du warp PD de Serum 2 sans supposer qu'il est identique.

## 2. Formants : growl, talking bass, yoi

- [LU] Trois premiers formants, homme adulte, voyelles anglaises (SS 23, [part-23.md](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-23.md)) :

| Voyelle (mot anglais) | F1 Hz | F2 Hz | F3 Hz |
| --- | --- | --- | --- |
| « ee » (leap) | 270 | 2300 | 3000 |
| « oo » (loop) | 300 | 870 | 2250 |
| « i » (lip) | 400 | 2000 | 2550 |
| « e » (let) | 530 | 1850 | 2500 |
| « u » (lug) | 640 | 1200 | 2400 |
| « a » (lap) | 660 | 1700 | 2400 |

- [LU] Pour « ee » : gains 0 / −15 / −9 dB, Q 5 / 20 / 50 ; formants larges d'environ 100 Hz chez l'homme. Q = fréquence centrale / demi-largeur à mi-gain. Trois formants suffisent à reconnaître une voyelle ; F2 est celui qui bouge le plus. (SS 23)
- [LU] Un banc de formants fixes ne suit pas la note : sur une scie à 100 Hz, des pics à 400 / 800 / 1 200 Hz accentuent les harmoniques 4, 8 et 12 ; à 200 Hz ils tombent entre deux harmoniques. (SS 23)
- [LU] Un passe-bas résonant s'imite par deux formants : l'un à 0 Hz avec Q ≈ 0,1, l'autre à la coupure avec Q ≈ 10 ; l'amplitude du second règle la résonance perçue. (SS 23)
- [DÉDUCTION] Le mot « yoi » décrit un glissement de F2 du grave vers l'aigu, de l'ordre de « oo » (870 Hz) vers « ee » (2 300 Hz) : balayer le morph ou la coupure du filtre formant avec une enveloppe ou une LFO en mode Envelope, et lire la voyelle sur la note la plus jouée (un formant fixe ne suit pas la note). Ces voyelles sont anglaises : elles ne correspondent pas exactement aux voyelles françaises, et la table n'a pas de /o/.
- [LU] Vocoder : Homer Dudley, Bell Labs, 1939 ; porteuse habituelle : la scie. ([SS 15](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-15.md))

## 3. Unison et désaccord : Reese, rolling

- [LU] Deux sinus de 100 et 101 Hz battent à 1 Hz : le battement vaut l'écart de fréquence, l'amplitude va de la somme à zéro. Deux scies désaccordées « s'épaississent » sans s'annuler autant ; un vibrato à une vitesse différente du battement enrichit le son. ([SS 46](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-46.md))
- [CALCUL] Battement = f · (2^(c/1200) − 1), c étant l'**écart total** en cents entre les deux voix (± 15 cents font 30 cents d'écart). Le battement double à chaque octave, et l'harmonique k bat k fois plus vite :

| Note (C3 = 60) | Hz | 10 cents | 20 cents | 30 cents | 60 cents |
| --- | --- | --- | --- | --- | --- |
| E0 (MIDI 28) | 41,2 | 0,24 Hz | 0,48 Hz | 0,72 Hz | 1,45 Hz |
| A0 (MIDI 33) | 55,0 | 0,32 Hz | 0,64 Hz | 0,96 Hz | 1,94 Hz |
| E1 (MIDI 40) | 82,4 | 0,48 Hz | 0,96 Hz | 1,44 Hz | 2,91 Hz |
| A1 (MIDI 45) | 110,0 | 0,64 Hz | 1,28 Hz | 1,92 Hz | 3,88 Hz |

- [DÉDUCTION] La fourchette ±15 à ±30 cents de la fiche Reese (`families.md`, fiche 6) donne sur A0 un battement de la fondamentale de 0,96 à 1,94 Hz, et bien plus rapide sur les harmoniques : régler le désaccord sur la note la plus jouée, et garder le sub sans désaccord, car un battement de la fondamentale est une variation de niveau dans le grave.

## 4. Repliement, distorsion et FM forte

- [LU] Une composante au-delà de la moitié de la fréquence d'échantillonnage se replie à égale distance en dessous (10 kHz échantillonné à 11,11 kHz → 1,11 kHz) ; le repliement ne s'enlève plus après coup. ([SS 17](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-17.md))
- [DÉDUCTION] FM forte, warps agressifs et distorsions empilées créent des partiels très aigus : ceux qui se replient deviennent des composantes inharmoniques qui ne suivent pas la note. Activer le suréchantillonnage quand l'outil en propose un (à vérifier dans l'interface de Serum 2 et des plug-ins), et vérifier les notes aiguës d'un growl à part.
- Littérature à lire hors session cloud (trouvée, non lue) : antialiasing par primitive (ADAA) dans les waveshapers, [DAFx 2020](https://dafx2020.mdw.ac.at/proceedings/papers/DAFx2020_paper_35.pdf), [DAFx 2023](https://www.dafx.de/paper-archive/2023/DAFx23_paper_61.pdf), [DAFx 2024](https://dafx.de/paper-archive/2024/papers/DAFx24_paper_33.pdf).

## 5. Filtres et phase : pente, peigne, alignement kick/sub

- [LU] La coupure se définit à −3 dB ; 6 dB/oct par pôle (12, 18, 24 dB/oct pour 2, 3, 4 pôles), un 4 pôles passant par des zones à 6, 12 et 18 dB/oct avant d'atteindre 24. ([SS 5](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-5.md)) Passe-bas RC : −45° de phase à la coupure, vers −90° au-dessus. ([SS 4](https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-4.md))
- [LU] Un cycle de 100 Hz dure 10 ms ; décaler une copie de 5 ms annule le 100 Hz et renforce le 200 Hz : deux copies décalées font un filtre en peigne. (SS 4)
- [CALCUL] Décalage qui annule une fréquence (demi-période) : 40 Hz → 12,5 ms ; 50 Hz → 10 ms ; 60 Hz → 8,3 ms ; 80 Hz → 6,25 ms ; 100 Hz → 5 ms.
- [DÉDUCTION] Un kick et un sub décalés de quelques millisecondes (sidechain avec lookahead, latence de plug-in, sample mal calé) peuvent se creuser l'un l'autre dans 40-100 Hz : mesurer avec `../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md` plutôt que de corriger à l'EQ.
- [LU] Key tracking à 100 % puis 66 % dans des patchs de type Minimoog (SS 26) ; un filtre en auto-oscillation peut remplacer un oscillateur, et s'accorde en jouant sur l'auto-oscillation puis en baissant la résonance (SS 41, SS 49 ; passages relevés, articles non lus en entier).

## 6. Grave et perception

- [LU] Seuil d'audition ISO 226:2003 (dB SPL) : 20 Hz 78,5 ; 25 Hz 68,7 ; 31,5 Hz 59,5 ; 40 Hz 51,1 ; 50 Hz 44,0 ; 63 Hz 37,5 ; 80 Hz 31,5 ; 100 Hz 26,5 ; 1 kHz 2,4. Validité : 20 Hz-12,5 kHz, 20 à 80 phones (iso226.m).
- [CALCUL] Même sonie que 80 dB à 1 kHz (80 phones) : 119,0 dB à 20 Hz, 109,6 à 31,5 Hz, 105,3 à 40 Hz, 101,7 à 50 Hz, 98,4 à 63 Hz, 92,5 à 100 Hz. Pour passer de 40 à 50 phones : +4,9 dB à 20 Hz, +6,2 dB à 50 Hz, contre +10 dB à 1 kHz.
- [DÉDUCTION] Dans le sub, quelques décibels changent beaucoup la sonie perçue, et cette sonie dépend du volume d'écoute : régler le sub par petits pas (0,5 à 1 dB), à volume d'écoute fixe et noté, et vérifier à faible volume (contrôle déjà prévu dans la procédure du skill).
- [CALCUL] Fréquences en tempérament égal, MIDI 69 = 440 Hz, nom Ableton (C3 = 60) : MIDI 21 A-1 27,5 Hz ; 24 C0 32,70 Hz ; 28 E0 41,20 Hz ; 29 F0 43,65 Hz ; 33 A0 55,0 Hz ; 36 C1 65,41 Hz ; 40 E1 82,41 Hz ; 45 A1 110,0 Hz.
- Trouvé, non lu : la fondamentale manquante (des harmoniques produites par une non-linéarité font percevoir une fondamentale absente sur un petit haut-parleur, d'après l'extrait d'un brevet US 8625813). Raison documentée de la légère saturation du sub dans la fiche 1, à confirmer à l'écoute sur petit haut-parleur.

## 7. Thèmes sans source lue : à compléter

- **OTT** (Xfer) : aucune page officielle lue. Les descriptions trouvées (trois bandes, compression vers le haut et vers le bas, Depth, Time) viennent d'extraits secondaires ([EDMProd](https://www.edmprod.com/ott-plugin/), [Bedroom Producers Blog](https://bedroomproducersblog.com/2022/05/04/xfer-records-ott/)) : ne pas les présenter comme vérifiées.
- **Chaînes de resampling « neuro » et « riddim »**, **wavefolding**, **intermodulation dans le grave**, **formants des voyelles françaises**, **pages précises du manuel Serum 2** (warps, filtres, FM entre oscillateurs, modes de LFO, granulaire, spectral) : aucune source lue dans cette session. Le manuel Serum 2 est recensé dans `../../../references/ressources.md` ; sa cartographie dans `../../../references/serum2-cartographie.md`.
- Ouvrages de référence : la limite de recherche a été atteinte avant de pouvoir vérifier titres et auteurs ; aucun livre n'est donc cité.
- Trouvés, non lus, à ouvrir sur le Mac : [Perfect Circuit, phase distortion et FM](https://www.perfectcircuit.com/signal/phase-distortion-frequency-modulation) ; [CMU, FM Synthesis](https://www.cs.cmu.edu/~music/icm-online/readings/fm-synthesis/fm_synthesis.pdf) ; [DSPRelated, Sinusoidal FM](https://www.dsprelated.com/freebooks/mdft/Sinusoidal_Frequency_Modulation_FM.html) ; [Electric Druid, Phase Distortion Synthesis](https://electricdruid.net/phase-distortion-synthesis/) ; [revue des mesures de formants, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6002811/) ; [table Peterson & Barney du manuel Praat](https://www.fon.hum.uva.nl/praat/manual/Create_formant_table__Peterson___Barney_1952_.html).
