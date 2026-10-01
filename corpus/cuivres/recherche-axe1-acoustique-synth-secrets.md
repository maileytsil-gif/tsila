---
titre: "Rapport de recherche — axe 1 : acoustique des cuivres et synthèse classique (Synth Secrets, Chowning, DX7, STK, formants)"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: rapport de recherche
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE 1 — Acoustique des cuivres et synthèse classique des cuivres

Rapport de recherche pour le skill « sound design des cuivres » (Ableton Live 12 + Serum 2).
Date : 2026-09-24. Convention de hauteur : **MIDI 60 = C3** sauf mention contraire ; quand une source utilise la notation scientifique (C4 = MIDI 60), la conversion est indiquée.

## 0. Conditions de la recherche et légende des tags

Le proxy de sortie de la session bloque la quasi-totalité du web (soundonsound.com, Wikipédia, UNSW, arXiv, HAL, archive.org, éditeurs scientifiques, sites de tutoriels…). Seuls **raw.githubusercontent.com** (fichiers bruts GitHub) et l'API de recherche de code GitHub étaient joignables. La recherche web (WebSearch) fonctionnait, mais elle ne renvoie que des extraits, pas les pages.

Conséquence sur les tags :

- **[DOC]** : fait tiré d'une source primaire (ou d'une copie intégrale d'un article de référence) **réellement lue** dans cette session. Les quatre articles Synth Secrets de Gordon Reid ont été lus **intégralement** via la copie GitHub `micjamking/synth-secrets` (scrape du site Sound On Sound ; le texte inclut l'URL d'origine de chaque article).
- **[HEUR]** : plage de départ issue d'un tutoriel, d'un modèle logiciel ou de notes secondaires réellement lus.
- **[HEUR-extrait]** : valeur issue **uniquement d'un extrait de résultat de recherche** (page bloquée, non lue). À confirmer avant d'en faire une règle.
- **[MÉMOIRE, non vérifié]** : valeur de ma mémoire, sans page lue.
- **[TEST]** : à valider dans le Set (réservé au skill final).

---

## A. Faits et valeurs chiffrées

### A.1 Tessitures sonnantes (MIDI, C3 = 60)

Source principale lue : **MuseScore 3.6.2, `share/instruments/instruments.xml`** (fichier officiel du logiciel, tessitures « amateur » et « professionnel » en numéros MIDI sonnants ; `transposeChromatic` = transposition de l'instrument). URL : https://raw.githubusercontent.com/musescore/MuseScore/v3.6.2/share/instruments/instruments.xml [DOC]. Vérification croisée : **music21 `instrument.py`** (note la plus grave *écrite* et transposition) https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/instrument.py [DOC], et extraits Wikipédia (non lus) [HEUR-extrait].

| Instrument | MuseScore amateur (MIDI) | MuseScore pro (MIDI) | Noms C3=60 (pro) | Transposition | Recoupement |
|---|---|---|---|---|---|
| Trompette en si♭ | 52–80 | 52–85 | E2 … C#5 | −2 (sonne un ton sous l'écrit) | Wikipédia (extrait) : écrit F#3–C6 (sci.) → sonnant E3–B♭5 sci. = **MIDI 52–82** [HEUR-extrait] ; music21 : plus grave écrit F#3 sci. (= MIDI 54 écrit, 52 sonnant) [DOC] |
| Trombone ténor | 40–70 | 40–74 | E1 … D4 | 0 | Wikipédia (extrait) : E2–B♭4 sci. = **MIDI 40–70** [HEUR-extrait] ; music21 : plus grave E2 sci. = 40 [DOC]. L'entrée générique « trombone » de MuseScore descend à 36 (pro) pour les pédales. |
| Trombone basse | 32–68 | 27–72 | D#0 … C4 | 0 | music21 : plus grave B♭1 sci. = 34 [DOC] |
| Cor en fa | 41–69 | 31–77 | G0 … F4 | −7 (sonne une quinte sous l'écrit) | Extrait (Wikipédia/Tunable) : sonnant B1–F5 sci. = **MIDI 35–77** [HEUR-extrait] ; music21 : plus grave C2 sci. = 36 [DOC] |
| Tuba en si♭ | 28–58 | 22–72 | A#-1 … C4 | 0 | Extrait : D1–F4 sci. = **MIDI 26–65**, « cœur » C2–G3 sci. = 36–55 [HEUR-extrait] ; music21 : D1 sci. = 26 [DOC] |
| Tuba en ut | 26–60 | 24–72 | C0 … C4 | 0 | idem |
| Sax alto (mi♭) | 49–82 | 49–87 | C#2 … D#5 | −9 (sixte majeure) | Extrait Wikipédia : sonnant D♭3–A♭5 sci. = **MIDI 49–80** (A5 = 81 avec clé de fa# aigu) [HEUR-extrait] ; music21 : plus grave écrit B♭3 sci., transposition M-6 [DOC] |
| Sax ténor (si♭) | 44–77 | 44–82 | G#1 … A#4 | −14 (neuvième majeure) | Extrait : sonnant A♭2–E5 sci. = **MIDI 44–76** ; si♭ grave sonnant = 103,83 Hz, fa# aigu = 659,26 Hz [HEUR-extrait] ; music21 transposition M-9 [DOC] |
| Sax baryton (mi♭) | 37–70 | 36–75 | C1 … D#4 | −21 (treizième majeure) | Extrait : sonnant C2–A4 sci. = **MIDI 36–69** (avec clé de la grave) ; si♭ grave = 69,30 Hz [HEUR-extrait] ; music21 transposition M-13 [DOC] |

Lecture pratique pour le skill : la fourchette « pro » de MuseScore inclut les pédales et l'altissimo ; la fourchette « amateur » est la zone confortable d'une section pop/funk. Les extraits Wikipédia tombent systématiquement à l'intérieur des valeurs MuseScore, ce qui les recoupe.

### A.2 Physique de base des cuivres (Synth Secrets, Part 24)

Source : Gordon Reid, *Synth Secrets Part 24 : Synthesizing Wind Instruments*, SOS avril 2001. URL d'origine : http://www.soundonsound.com/sos/apr01/articles/synthsecrets.asp (bloquée) ; page actuelle https://www.soundonsound.com/techniques/synthesizing-wind-instruments (bloquée) ; **copie lue intégralement** : https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-24.md [DOC].

- Tuyau ouvert : longueur d'onde du fondamental = 2 × longueur ; exemple chiffré : tuyau de 0,34 m, célérité 340 m/s → aller 1 ms, retour 1 ms, période 2 ms, **500 Hz** ; toute la série harmonique est possible. [DOC]
- Tuyau fermé à une extrémité (lèvres sur l'embouchure) : longueur d'onde = 4 × longueur → **250 Hz** pour le même tuyau, et **seulement les harmoniques impairs** (cas de la clarinette, cylindrique). [DOC]
- Les cuivres sont des tuyaux « lip-valve » fermés mais **leur perce est en grande partie conique ou évasée** ; le cône et l'évasement (« flare ») sont, avec le tuyau ouvert, les seules formes qui rendent **la série harmonique complète** → d'où la dent de scie comme forme d'onde de départ, et non le carré. [DOC]
- Les lèvres agissent comme une valve produisant **un train d'impulsions de pression** dont la cadence, réglée par la tension des lèvres et la pression buccale, doit correspondre à un mode du tuyau. [DOC]
- Figure 8 (même note jouée piano et forte sur le même cuivre) : la note douce ne contient qu'**environ 6 harmoniques**, le fondamental dominant ; la note surblowée contient des amplitudes significatives sur **au moins 15 harmoniques**, et c'est **le 8ᵉ harmonique qui domine** (« squawk » trois octaves au-dessus). [DOC]
- Figure 9 : à amplitude égale, **les notes graves ont un spectre plus complexe que les aiguës** (réponse en fréquence finie de l'instrument) → en synthèse, le suivi de clavier du filtre doit être **inférieur à 1:1**. [DOC]
- Conclusion de l'article (base statique d'une trompette) : dent de scie ; filtre passe-bas dont la coupure monte et descend avec la dynamique ; **résonance qui augmente avec la dynamique** pour souligner les harmoniques hauts ; suivi de clavier partiel. [DOC]

### A.3 Compléments d'acoustique (notes secondaires lues, citant UNSW / Benade / arXiv)

Source : trois fiches de recherche « Trumpet / Trombone / French horn — acoustic research » d'un dépôt GitHub tiers (`Crack-Pantelimon/bespoke-mcp-data-pack`, fichiers `overtone/instruments/brass-instruments/*/RESEARCH.md`), lues intégralement. Ces notes citent UNSW (Joe Wolfe), Benade, Hirschberg 1996, Campbell 2019, Gilbert & Petiot 2008, Myers 2012, l'arXiv 1611.01025 et des mesures faites sur les échantillons Philharmonia. Elles sont de qualité mais **non primaires** ; leurs valeurs sont donc **[HEUR]** (et [HEUR-extrait] pour ce qu'elles reprennent d'ailleurs). URLs : https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/HEAD/overtone/instruments/brass-instruments/trumpet/RESEARCH.md (idem `.../trombone/RESEARCH.md` et `.../french-horn/RESEARCH.md`).

- Embouchure + pavillon **réalignent les modes** d'un cylindre 1:3:5:7 vers ≈ **2:3:4:5** (série harmonique sans son fondamental) ; sur une trompette réelle : mode 1 prédit 61,25 Hz → mesuré **233 Hz** ; mode le plus haut prédit 1653,75 Hz → mesuré 1617 Hz. [HEUR, cité d'UNSW]
- Niveau interne dans l'embouchure en *forte* : **166,9 dB (B♭3) / 167,2 dB (B♭4)** (cité de l'arXiv 1611.01025, simulation 3-D). Sur un crescendo, **le fondamental monte de ~8 dB alors que le 9ᵉ harmonique et au-delà montent de plus de 45 dB**. [HEUR]
- Perce de trompette **~1,4 m (LibreTexts) à 1,48 m** ; pression de souffle de **< 1 kPa à ~10 kPa**. [HEUR]
- L'embouchure est un résonateur de Helmholtz à faible Q → **formant fixe** de cuivre ; « popping frequencies » mesurées **745, 790, 820 Hz** ; ce formant **ne suit pas la hauteur**. [HEUR, cité d'UNSW]
- **Fréquence de coupure du pavillon** : presque aucune énergie n'est réfléchie **au-dessus de ~1500 Hz** pour la trompette (Benade) ; **700–800 Hz** pour le trombone (UNSW). Au-dessus, le pavillon rayonne au lieu de réfléchir → directivité et roll-off du filtre de réflexion d'un modèle guide d'onde. [HEUR]
- Sourdines : **formants forts dans la bande 1–3 kHz**. [HEUR, cité d'UNSW ; aussi extrait direct d'UNSW dans une recherche : « standard mutes produce strong formants at various frequencies in the 1-3 kHz range » [HEUR-extrait]]
- Trombone : perce **cylindrique 11–14 mm** sur la coulisse, longueur de classe ~2,7 m, pavillon 18–22 cm (cité de Wikipédia). Mesures sur clip Philharmonia (A2, mf) : **H2 le plus fort, H1 à −19,4 dB, centroïde 1351 Hz, attaque 46 ms**. [HEUR]
- Cor : perce conique, pavillon vers l'arrière ; sur clip Philharmonia (A2) : **H4 le plus fort, H1 à −19 dB, centroïde 859 Hz, attaque (−20 → −3 dB) 107 ms**, `odd_even_db` −2,9 dB (pairs légèrement plus forts). Fenêtre d'attaque jugée plausible pour le cor : **40–120 ms**. [HEUR]
- Un brevet cité dans un extrait de recherche donne des « cutoff frequencies » : **cor ≈ 636 Hz, trombone ≈ 1,38 kHz, trompette ≈ 2,56 kHz, post horn ≈ 4,19 kHz** (source : brevet US « Synthesizer for organ voices », extrait non lu). [HEUR-extrait]

### A.4 Formants / régions spectrales caractéristiques

**Source primaire lue :** Yan Maresz (CNSMDP), *Référence Formantique de l'Orchestre — étude quantitative des convergences spectrales instrumentales*, manuscrit LaTeX daté mars 2026 (soumission JNMR), 5 914 échantillons tenus de la base SOL2020 (IRCAM/Orchidea), validé contre Backus 1969, Gieseler et al. 1985, **Meyer 2009** et McCarty/CCRMA. URL : https://raw.githubusercontent.com/zseramnay/Orchestration/HEAD/publications/Maresz-Formant_Reference_Orchestra_JNMR.tex [DOC]. F1 = premier pic de l'enveloppe spectrale ; *Fp* = « formant principal » (centroïde pondéré, limité à la bande d'énergie maximale, aux points −6 dB).

| Instrument | F1 (Hz) | Fp (Hz) ± σ | F2 (Hz) | Zone vocalique (Maresz) |
|---|---|---|---|---|
| Trompette en ut | **786** (σ = 642 : très variable selon la nuance) | **1 046 ± 98** | 1 324 (σ 1 018) | /aa/ puis /a/ |
| Trompette + harmon | 2 358 (formant) | — | — | /i/ « brillance » |
| Cor en fa | **388** | **738 ± 112** | 1 106 | /o/ « plénitude » ; bande utile 600–1 400 Hz |
| Trombone | **237** | — | — | /u/ « profondeur » |
| Tuba basse | **226** | — | — | /u/ |
| Tuba contrebasse | 226 | — | — | /u/ |
| Sax alto | **398** | — | — | /o/–/aa/ (à 10 Hz du cor) |
| Famille cuivres | plage 162–2 358 Hz | | | |

Remarque de l'auteur : « Brass instruments present well-defined formants and strong spectral stability across dynamics (except the trumpet). » [DOC]

**Extrait HyperPhysics** (page bloquée, « Some Data on Orchestral Instruments ») : formants **trompette 1200–1400 Hz, trombone 600–800 Hz, cor 400–500 Hz, tuba 200–400 Hz**. [HEUR-extrait] — cohérent avec Maresz (Fp trompette 1 046, Fp cor 738, F1 trombone 237/tuba 226) à la différence de définition près (F1 vs pic large).

**Saxophones (extrait, JASA 83(5) p. 1900, « The saxophone spectrum », page bloquée)** : toutes les composantes suivent une enveloppe **E(x) = [N·x/(1+x⁷)]^(1/2)** avec x = f/f_b, où la « break frequency » vaut **f_b = 618 Hz (ténor) et 837 Hz (alto)** ; au-dessus, chute rapide. [HEUR-extrait] (Attribution Benade & Lutgen 1988 : [MÉMOIRE, non vérifié].)

### A.5 Brillance et dynamique : « brassiness », ondes de choc

- **Hirschberg, Gilbert, Msallam, Wijnands (1996), « Shock waves in trombones », J. Acoust. Soc. Am. 99(3), 1754–1758.** Texte intégral bloqué (tu-darmstadt.de, pure.tue.nl, semanticscholar). Extrait d'abstract : « The brightness of the sound generated by trombones is expected to be due to the essential nonlinearity of the wave propagation in the pipe. At fortissimo levels this leads to shock wave formation. […] Even for the weak shocks […] shock waves certainly correspond to a dramatic amount of high frequencies in the radiated sound: a bright "metallic" sound. » [HEUR-extrait]
- **Mémoire des Olympiades de Physique 2009, lycée D. Rousseau (Laval), « Peut-on produire un son cuivré à l'aide d'un tuyau d'arrosage ? »**, encadré par **Joël Gilbert et Jean-Pierre Dalmont (LAUM, Le Mans)** — lu intégralement (copie GitHub : https://raw.githubusercontent.com/alainjouve/olymphys7/HEAD/public/search/textes/16-eq-17-memoire-Peut-on%20produire%20un%20son%20cuivre%20avec%20un%20tuyau%20d'arrosage%20%20.txt) [DOC pour les mesures du mémoire] :
  - le fondamental (**350 Hz**, fréquence de vibration des lèvres) est identique en entrée et en sortie du tuyau ; ce qui change avec la nuance, c'est la richesse en harmoniques de rang élevé ;
  - le son ne « cuivre » **que pour le tuyau de 4 m, en mezzo-forte et surtout forte ; jamais avec le tuyau de 1 m** ni un trombone raccourci à 1 m → la **longueur** de propagation est déterminante ;
  - pression acoustique efficace en sortie d'embouchure en fortissimo : **2 471 Pa ≈ 162 dB SPL** ;
  - **le tuba cuivre moins que le trombone** : évasement plus rapide (perce conique) contre perce presque cylindrique ;
  - mécanisme : les maxima de pression se propagent plus vite que les minima → raidissement du front → **onde de choc** → harmoniques de rang élevé.
- **Wiki « Instrument acoustics and idiom » (tkgally/algorithmic-music)**, lu : la « brassiness/cuivré » est un enrichissement **non linéaire** (raidissement vers un front de choc dans la perce), **plus proche d'un effet de seuil que d'une courbe lisse**, distinct d'une simple loi « vélocité → cutoff » ; cite Norman, Chick, Campbell, Myers & Gilbert 2010 (Acta Acustica 96, 614–621) et Myers et al. 2012 (JASA 131(1), 678–688) ; le centroïde spectral monte avec la dynamique sur tous les instruments (Schubert & Wolfe 2006), le cuivre étant le cas le plus non linéaire. URL : https://raw.githubusercontent.com/tkgally/algorithmic-music/HEAD/wiki/instrument-acoustics-and-idiom.md [HEUR]
- **Brassiness potential (Myers, Campbell, Gilbert)** : extrait — les instruments « brillants » (trompette, trombone) ont un segment quasi cylindrique juste après l'embouchure ; les instruments coniques (saxhorns, bugles) atténuent le raidissement ; **sacqueboutes et trombones : B = 0,6 à 0,82**. [HEUR-extrait]
- **Synth Secrets 24/25** : « louder notes have more harmonics than quieter ones » ; « high harmonics are accentuated to a greater and greater degree as we play louder and louder » ; le harmonique le plus fort n'est pas forcément le fondamental. [DOC]
- Pentes de « bloom » (centroïde en Hz par dB) retenues par les fiches GitHub pour leurs propres modèles : cor **+60 Hz/dB**, trompette **+84** (ou +320 dans une version), trombone **+102 Hz/dB** (r = 0,95). Ce sont des choix de modélisation, pas des mesures publiées. [HEUR]

### A.6 Transitoire d'attaque et glissement de hauteur initial

- **Synth Secrets 25** [DOC] :
  - la mise en place de l'onde stationnaire prend « une douzaine de cycles » ; pour **256 Hz (do médian) ≈ 50 ms d'instabilité de hauteur**, « du même ordre que le temps mis par tous les harmoniques pour atteindre leur régime » ;
  - **les harmoniques sous la fréquence de coupure naturelle de l'instrument atteignent leur niveau ensemble et plus vite que ceux au-dessus** (Fig. 11) ; c'est, selon certains chercheurs, l'indice le plus important pour identifier un instrument ;
  - attaque en langue « T »/« D » (plosive) : amplitude **quasi instantanée puis seconde montée plus lente** jusqu'au sustain (contour A-(AL)-A2-S) ; un ADS à attaque « instantanée » sur analogique donne une forme proche par l'arrondi des circuits ;
  - une attaque vigoureuse peut rendre les harmoniques élevés dominants et **« pitcher » le transitoire une octave ou plus au-dessus** ;
  - le relâchement d'un cuivre est **« very short »**.
- **Luce & Clark (1965), « Durations of attack transients of nonpercussive orchestral instruments », JAES 13, 194–199** (extrait) : durées de **14 à 85 ms**, croissantes dans l'ordre **anches doubles < clarinette < cuivres < cordes < flûte** ; indépendantes de la nuance et de la présence de vibrato. [HEUR-extrait]
- **arXiv 1511.04247** (simulation temporelle trombone avec propagation non linéaire, extrait) : pendant l'attaque, la fréquence de jeu est **plus haute** quand la non-linéarité est prise en compte, **jusqu'à +45 Hz ≈ +157 cents vers 0,25 s**, écart qui **disparaît vers 0,35 s** (3 cents à 0,5 s) ; temps d'attaque **0,18 s (non linéaire) contre 0,35 s (linéaire)**. [HEUR-extrait]
- Mesures sur clips Philharmonia (fiches GitHub) : **trombone 46 ms, cor 107 ms** (montée −20 → −3 dB). [HEUR]
- **STK `Brass` (Cook & Scavone)**, valeurs par défaut du code lu : ADSR **attaque 5 ms, decay 1 ms, sustain 1,0, release 10 ms** ; à `noteOn`, la vitesse d'attaque de la pression = amplitude × 0,001 (la pression monte donc plus vite quand on joue fort) ; `noteOff` : vitesse de relâchement = amplitude × 0,005. URL : https://raw.githubusercontent.com/thestk/stk/master/src/Brass.cpp [DOC]

### A.7 Vibrato

- Synth Secrets 25 : le vibrato est produit par les lèvres **une fois le régime atteint** → **vibrato retardé** (rampe AR sur la profondeur) ; « modulating frequencies **in the region of 5Hz** sound the most realistic » ; **profondeur « very low »**, sinon le timbre devient électronique. Part 27 (ARP Axxe) : LFO sinus **≈ 5 Hz**. [DOC]
- STK `Brass` : fréquence de vibrato par défaut **6,137 Hz** ; gain max 0,4 (CC1) ; fréquence réglable 0–12 Hz (CC11). [DOC]
- DX7 « BRASS 1 » (ROM1A voix 1) converti par un outil tiers : LFO **6,13 Hz**, profondeur 0,051. [HEUR — conversion tierce]
- Csound (exemple Chowning, commentaires du code) : `ivibhz = 5 ; FROM 5 TO 6.5 Hz AVERAGE`, jitter aléatoire à **125 Hz** et portamento initial « FROM MORRILL TRUMPET DESIGN » (D. Morrill, trompette FM, 1977). URL : https://raw.githubusercontent.com/mjladd/devcontainer-csound/HEAD/csound_score_examples/FmChowningA.csd [DOC pour le code ; attribution Morrill 1977 : MÉMOIRE, non vérifié]
- Extraits (Wikipédia « Vibrato », étude multicentrique) : rate typique **4,5–6,5 Hz** ; « wind and bowed instruments generally use vibratos with an extent of **less than half a semitone either side** ». [HEUR-extrait]

### A.8 Sourdines

- **MusicXML 4.0 (schéma W3C, lu)** — liste normative des sourdines : `straight, cup, harmon-no-stem, harmon-stem, bucket, plunger, hat, solotone, practice, stop-mute, stop-hand, echo, palm` ; attribut `harmon-closed` = `yes / no / half` (harmon ouvert, fermé, demi). URL : https://raw.githubusercontent.com/w3c/musicxml/v4.0/schema/musicxml.xsd [DOC]
- Effets spectraux (extraits, pages bloquées) [HEUR-extrait] :
  - **cup** : laisse passer environ **800–1200 Hz** (bande passante) ; « middle-soft » ;
  - **harmon** : projette surtout **1500–2000 Hz** ; « far-bright » ; introduit des **formants prononcés** dans l'impédance et décale les pics vers le haut ; forte résistance pour le joueur ; « wah » à la main sur le tube ;
  - **straight** : « middle-bright » ;
  - les sourdines agissent surtout **au-dessus de 1 kHz** ;
  - **bucket** : « the most muffled sound », rond et doux, réduit la brillance ;
  - **plunger** : effet « wah-wah »/« talking », toute la tessiture disponible car il ne rentre pas dans le pavillon.
- Maresz (lu) : **trompette + harmon → formant à 2 358 Hz** (zone /i/). [DOC]
- Wiki tkgally (lu) : cup ≈ passe-bande **800–1200 Hz** ; toutes les sourdines réduisent la dynamique/tessiture pratiques et peuvent altérer la justesse aux extrêmes. [HEUR]
- Faust `brassModel` (lu) : la sourdine est modélisée comme **l'ouverture du pavillon (0–1)** dans la terminaison `wBell(opening)`. [DOC]
- Cor bouché (« hand-stopping », extrait) : la main dans le pavillon **monte la hauteur jusqu'à un demi-ton** et change fortement le timbre (bouché ≠ demi-bouché ≠ ouvert). [HEUR-extrait]

### A.9 Articulations

- **MusicXML 4.0 (lu)** [DOC] :
  - `scoop` : « indeterminate slide attached to a single note […] appears **before** the main note and comes **from below** » ;
  - `plop` : idem, **avant** la note, **depuis au-dessus** ;
  - `doit` : « appears **after** the main note and goes **above** » ;
  - `falloff` : **après** la note, **vers le bas** ;
  - `shake` : « similar appearance to an inverted-mordent » ;
  - articulations standard : `accent`, `strong-accent` (marcato, accent vertical), `staccato` (point), `staccatissimo` (coin), `spiccato` (trait), `tenuto`, `detached-legato` (tenuto + point), `stress`, `soft-accent` (<>).
- Extraits (pages de pédagogie des cuivres, bloquées) [HEUR-extrait] :
  - **fall** : « a longer, measured dive to a pitch (determined or undetermined) after a note » ; **doit** : montée vers une hauteur indéterminée en finissant la note ; **scoop** : on attaque un peu bas et on glisse jusqu'à la note ; **plop** : descente rapide sur la note depuis au-dessus ;
  - **flutter tongue** : roulement de la langue, modulation typiquement **15–30 Hz**, jusqu'à **~50 Hz** ; **growl** : chanter une autre hauteur en jouant (modulation de fréquence, son « sale »), ou vibration de l'arrière de la langue ;
  - **shake** : « a very fast lip trill […] between two adjacent partials », aidé en secouant l'instrument ; pas de fréquence chiffrée trouvée ;
  - **glissando de trombone** : la coulisse a **7 positions à un demi-ton** ; l'ambitus maximal d'un glissando continu est **un triton** (1ʳᵉ → 7ᵉ position) ; sur les cuivres à pistons, le glissando « vrai » n'existe que par lip-slur entre partiels voisins (wiki tkgally, lu) [HEUR].
- Synth Secrets 27 (lu) : notes détachées à la langue → courte interruption (jouer légèrement staccato) ; changement de piston sans ré-attaque → **pas de redéclenchement des enveloppes** (mode Gate seul). [DOC]

---

## B. Recettes de synthèse complètes

### B.1 Synth Secrets Part 25 — le « patch idéal » modulaire (Gordon Reid, SOS mai 2001)

URL d'origine : http://www.soundonsound.com/sos/may01/articles/synthsecrets.asp ; page actuelle https://www.soundonsound.com/techniques/synthesizing-brass-instruments (bloquée) ; copie lue : https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-25.md. Titre exact : « Synth Secrets, Part 25: Synthesizing Brass Instruments ». **Il n'existe pas d'article intitulé « Practical Brass Synthesis »** : la mise en pratique est répartie sur les parties 26 (Minimoog) et 27 (SH-101/Axxe). [DOC]

Structure (Fig. 18 de l'article, « block diagram from a single-oscillator synth ») :

1. **Oscillateur** : une seule dent de scie (série harmonique complète). Pas de modulation périodique de la hauteur pendant le transitoire : « any form of periodic […] modulation applied to the frequency of the oscillator will result in FM […] and side-bands » qui détruisent le timbre.
2. **VCA / enveloppe d'amplitude** : ADSR (l'attaque des cuivres soufflés doucement ou vigoureusement suit une forme ADS ; Fig. 1) ; **la vélocité raccourcit l'attaque** (pression de souffle) ; **release très court** ; idéalement contour à **5 étages** pour le « swell brass » (Fig. 6a) + **LFO sur le VCA pour le trémolo** (retardé ou non) ; avec un ADSR classique on se contente de Fig. 6b (Odyssey, Prophet 5, OB-X, Memorymoog).
3. **VCF passe-bas** : coupure = f(CV de hauteur, capteur de dynamique) ; **résonance proportionnelle à la dynamique** ; contour **ADSR** (pas AR) pour recréer le « parp » de l'impulsion initiale (Fig. 13) ; **quantité d'enveloppe de filtre commandée par la vélocité** (Fig. 14) ; **aftertouch → brillance** pendant le sustain.
4. **Growl (instabilité initiale)** : onde **triangle ≈ 80 Hz** appliquée **à la coupure du filtre** (pas à l'oscillateur), à travers un VCA piloté par une enveloppe **AD** pour que le growl ne dure que le temps de l'instabilité (≈ 50 ms à 256 Hz) ; aftertouch → réintroduire le growl (surblow) ; l'auteur en déduit qu'un LFO plafonné à 25 Hz est insuffisant.
5. **Vibrato retardé** : LFO **≈ 5 Hz** sur la hauteur, profondeur **très faible**, introduit par une rampe **AR** sur la quantité.
6. **Bruit** : bruit turbulent **filtré par les formants de l'instrument**, niveau presque indétectable ; ajoute un « undertone » accordé.
7. Ce que l'article **ne traite pas** : enveloppe de hauteur/portamento volontaires, formants du timbre tonal, phases des harmoniques, variation individuelle des harmoniques (partiels **légèrement étirés vers l'aigu**) → « subtractive synthesis is not an ideal way » ; la synthèse additive (Kawai K5/K5000) serait meilleure.

Aucune valeur ADSR en ms n'est donnée dans la Part 25 ; seules valeurs chiffrées : 80 Hz (growl), 5 Hz (vibrato), 50 ms (instabilité). [DOC]

### B.2 Synth Secrets Part 26 — Minimoog (SOS juin 2001)

URL d'origine : http://www.soundonsound.com/sos/jun01/articles/synthsecrets.pt26.asp ; page actuelle https://www.soundonsound.com/techniques/brass-synthesis-minimoog (bloquée) ; copie lue : https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-26.md. [DOC]

| Section | Réglage | Raison donnée |
|---|---|---|
| Osc 1 | **dent de scie, 4'** (une octave au-dessus du piano) | trompette/cornet/sax alto-soprano sont aigus ; un seul oscillateur car deux VCO qui dérivent ne représentent pas l'instrument |
| Osc 2 | inutilisé | — |
| Osc 3 | **triangle, 32', fine −1, Keyboard Control off**, sert de modulateur audio du filtre | rasp/growl constant quelle que soit la note |
| Mixer | Osc 1 à **5/10** ; bruit off | éviter l'overdrive de l'entrée du filtre |
| Loudness Contour | **Attack 100 ms, Sustain 10/10, Decay indifférent, Decay switch OFF** (release instantané) | un cuivre s'arrête net |
| Filter | **Cutoff −5** (fermé), **Emphasis 2/10**, **Amount of Contour 6,5/10**, **Keyboard Control 1 + 2 ON = 100 %** (idéal théorique ≈ 190 % par octave, soit un peu moins de 1:1) | bosse résonante toujours à la même position relative à la note |
| Filter Contour | **Attack 600 ms, Decay 800 ms, Sustain 5/10**, release instantané | les harmoniques hauts « parlent » plus tard que les bas (Fig. 16) ; les bas passent dès 100 ms, les hauts « one by one over the course of about half a second » |
| Filter Modulation | ON ; Modulation Mix = 0 (Osc 3 seul) ; **molette de modulation** dosée à la main pour faire disparaître le growl après l'attaque | pas de VCA/EG libre |
| Vibrato | à la **molette de pitch**, manuellement | Osc 3 est pris ; le vibrato manuel est plus naturel |
| Bruit | omis | pas de formantage possible |

Conseils : « with sympathetic EQ and a suitable reverb, it's remarkable how close you can get », surtout pour **trombone et tuba** (oreille moins sensible aux nuances des graves) ; ne pas s'écarter des principes (autre forme d'onde, attaques instantanées, forte emphasis → plus rien de cuivré).

Comparaison avec *Minimoog Sound Charts* (Tom Rhea, 1977, Norlin) [DOC, description qualitative] :
- **Trumpet (Rhea)** : 3 oscillateurs à l'unisson (« Fatter tutti sounds »), pas de modulation, attaque un peu plus lente, petit decay au relâchement, tracking 66 %, attaque de filtre plus rapide, cutoff initial plus haut, **pas d'emphasis**, Amount of Contour plus faible → jugé « muted », sans mouvement.
- **Tuba (Rhea)** : une dent de scie, **le générateur de bruit module le filtre** (au lieu d'Osc 3, sans risque de bandes latérales) — « extremely effective » ; jouer avec Amount of Contour et Cutoff pour plus ou moins cuivré.
- **Jazz Trombone (Rhea)** : une dent de scie, Osc 3 en vrai LFO sur le filtre + modulation d'oscillateur (vibrato) ; difficile de limiter le vibrato à la molette.

### B.3 Synth Secrets Part 27 — Roland SH-101 et ARP Axxe (SOS juillet 2001)

URL d'origine : http://www.soundonsound.com/sos/jul01/articles/synthsecrets27.asp ; page actuelle https://www.soundonsound.com/techniques/roland-sh101-arp-axxe-brass-synthesis (bloquée) ; copie lue : https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-27.md. [DOC]

**SH-101 :**
- VCO : **dent de scie 4'** ; pulse, sub-osc, bruit à **0** ; Mod (vibrato LFO) à **0**.
- VCA : mode **Gate** (déconnecté de l'ADSR : enveloppe carrée d'amplitude, montée limitée seulement par la vitesse du VCA) — les harmoniques bas entrent « rather too quickly » (Fig. 10b), masqué par le growl.
- ENV (unique, réservé au filtre) : **A 20 %, D 50 %, S 50 %, R 2** (« 2 » pour éviter le clic ; mode **Gate** seul, pas Trig, pour ne pas redéclencher lors des changements de piston).
- VCF : **Freq près de 0**, **Res « just a touch »**, **Env au maximum ou presque**, **Kybd tracking un peu < 100 %** ; **Mod ≈ 60 % au début de la note, ramené à 0 % au moment où le contour atteint le sustain** (à la main).
- LFO : **triangle, vitesse maximale** (growl).
- Vibrato manuel possible au bender (VCO Bender à petite valeur), mais alors sans growl.
- Patch d'usine Roland « Trumpet » : jugé décevant (A/D trop courts, Env trop faible, cutoff initial trop haut, aucune modulation).
- Patch d'usine Roland « Tuba » : **dent de scie à 60 % + sub-oscillateur carré à l'octave inférieure à 100 %** → spectre plus complexe qu'une simple dent de scie, « lacks body » sans le sub, « hollow » avec le sub seul.

**ARP Axxe :**
- Mixer : dent de scie au maximum ; carré et bruit à 0.
- VCF : Freq et Résonance **légèrement** relevés ; **ADSR tracking élevé**, **Kybd CV modéré** ; LFO sinus sur le VCF à 0.
- VCA : gain initial finalement **à 0** et **ADSR → VCA** (sinon le son ne s'arrête jamais).
- ADSR : « approximating the SH101's **20 %, 50 %, 50 %, 20 %** » puis, à l'oreille, **Decay allongé, Sustain baissé, ADSR→VCF réduit** pour souligner le « parp ».
- Growl impossible (LFO max **20 Hz**) → **vibrato sinus ≈ 5 Hz** à la place, de préférence via le pad de pression (PPC) plutôt qu'en fixe.
- Leçon : « Once you've learned how to create a brass patch on one synth, you can recreate it on any synth capable of doing so. »

### B.4 Synth Secrets Part 24 — recette statique de trompette

Dent de scie ; passe-bas dont la coupure suit la dynamique ; résonance croissante avec la dynamique ; tracking de la coupure < 1:1 pour que les aigus aient moins d'harmoniques. [DOC] (voir A.2)

### B.5 Synth Secrets Part 23 — formants (SOS mars 2001)

Copie lue : https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-23.md [DOC]. Ne parle pas des cuivres (sinon pour annoncer la suite) mais donne la méthode utile pour A.4 : un banc de passe-bande fixes (exemple 400/800/1200 Hz sur une dent de scie à 100 Hz accentue les harmoniques 4, 8 et 12 ; à 200 Hz ce sont les 3ᵉ, 7ᵉ, 11ᵉ) → **les formants ne suivent pas la hauteur** ; Q = f_c / largeur à mi-hauteur (ex. 1 kHz / 100 Hz → Q = 10) ; largeur des formants vocaux ≈ 100 Hz. Application cuivres : placer des pics fixes aux valeurs de A.4 (Maresz/HyperPhysics) [TEST].

### B.6 FM « Chowning brass » (Csound, exemple d'après Chowning 1973 / Dodge & Jerse)

Fichier lu : https://raw.githubusercontent.com/mjladd/devcontainer-csound/HEAD/csound_score_examples/FmChowningA.csd [DOC pour les paramètres du code].

- Instrument 1 (FM simple) : **porteuse 440 Hz, modulateur 440 Hz → rapport 1:1**, **index de modulation de 0 → 5**, durée 0,6 s ; **même enveloppe (f2) sur la porteuse et sur le modulateur** → l'index suit l'amplitude (principe de Chowning pour les cuivres : brillance ∝ dynamique).
- Enveloppe f2 « ADSR Trumpet Envelope — fig 1.11 » (GEN07, 513 points) : 0 → 1 sur 1/6 de la durée (**attaque ≈ 100 ms pour 0,6 s**), 1 → 0,75 au tiers, 0,75 → 0,65 à la moitié, 0,65 → 0,50 aux 5/6, 0,50 → 0 à la fin.
- À titre de comparaison, les autres timbres du même fichier : bois 900:300 index 0→2 ; basson 500:100 index 0→1,5 ; anche 900:600 index 4→2 ; cloche 200:280 index 0→10.
- Instrument 2 (double porteuse) : seconde porteuse à **2 100 Hz** = formant fixe dont on fait varier amplitude et largeur (index 0,2–0,9) ; balayage de formant 600 → 3 600 Hz.
- Instrument 3 (soprano de Chowning, mais avec commentaires « FROM MORRILL TRUMPET DESIGN ») : vibrato **5 Hz** (« 5 to 6.5 Hz average »), jitter 125 Hz, portamento initial 0,05, largeur de vibrato 0,002 × log2(f).

### B.7 DX7 « BRASS 1 » (ROM1A, voix 1/32) — paramètres d'usine

Deux conversions tierces du sysex, lues : https://raw.githubusercontent.com/fxrobin/infinite-synthwave/HEAD/synthwave/patches/library/dx7_BRASS_1.yaml et https://raw.githubusercontent.com/Ethycs/symcrash_python_AP/HEAD/presets/instruments/dx7_brass_1_v0.yaml [DOC pour les valeurs brutes du patch ; HEUR pour les conversions en ms].

- **Algorithme 22, feedback 7** (porteuses Op1, Op3, Op4, Op5 ; modulateurs Op2 → Op1 et **Op6 avec feedback** → Op3/4/5).
- Rapports : Op1 **0,50** (detune +7), Op2 0,50 (+7), Op3 **1,00** (−2), Op4 1,00 (0), Op5 1,00 (+1), Op6 1,00 (0) — soit, en fréquences fines, 0,503 / 0,503 / 0,9983 / 1,0 / 1,0009 / 1,0 : **trois porteuses à l'unisson légèrement désaccordées + une à l'octave inférieure**, modulées à **1:1** (spectre de type dent de scie) avec **feedback 7** (« You cannot get a horn without that feedback », extrait de tutoriel DX7 non lu [HEUR-extrait]).
- Niveaux de sortie (0–99) : Op1 98, Op2 86, Op3 99, Op4 99, Op5 98, Op6 82.
- EG (rates/levels DX7) : Op1 R 72/76/99/71, L 99/88/96/0 ; Op2 R 62/51/29/71, L 82/95/96/0 ; Op3 R 77/76/82/71, L 99/98/98/0 ; Op4 et Op5 R 77/36/41/71, L 99/98/98/0 ; Op6 R 49/99/28/68, L 98/98/91/0.
- Conversion en temps par l'outil tiers : porteuses **attaque ≈ 19–31 ms**, sustain ≈ 0,77–0,92, release ≈ 145 ms ; modulateur Op2 **attaque ≈ 106 ms, decay ≈ 275 ms** ; **modulateur Op6 (feedback) attaque ≈ 425 ms, decay ≈ 1 040 ms, sustain 0,55**, key-scale rate 0,57 → **la brillance s'installe plus lentement que l'amplitude**, exactement le principe de Reid (filtre 600 ms vs VCA 100 ms). [HEUR — conversion]
- LFO : sinus **6,13 Hz**, profondeur 0,051, sans délai.

### B.8 Modèles physiques (paramètres de code, utiles comme références de plage)

- **STK `Brass`** (https://raw.githubusercontent.com/thestk/stk/master/src/Brass.cpp) [DOC] : guide d'onde (ligne à retard = 2 × période + 3 échantillons, « play a harmonic »), **filtre de lèvres biquad résonant à la fréquence jouée, rayon 0,997, gain 0,03** ; pression de bouche = 0,3 × pression ; pression de perce = 0,85 × retour de ligne (absorption) ; **tension des lèvres CC2 : f_lèvres = f × 4^(2v−1)** (± 2 octaves) ; **longueur de coulisse CC4 : délai × (0,5 + v)** ; vibrato CC11 (0–12 Hz, défaut 6,137 Hz) ; gain de vibrato CC1 (max 0,4) ; ADSR 5 ms / 1 ms / 1,0 / 10 ms.
- **Faust `physmodels.lib`** (https://raw.githubusercontent.com/grame-cncm/faustlibraries/master/physmodels.lib) [DOC] : `brassLipsTable(tubeLength, lipsTension)` = gain 0,03 → résonateur 2 pôles (rayon 0,997) accordé sur `l2f(tubeLength) × 4^(2·lipsTension − 1)` → produit → clipping ±1 ; `brassLips` : absorption 0,85, pression × 0,3, `dcblocker` ; `brassModel(tubeLength, lipsTension, mute, pressure)` = lèvres → `openTube` → `wBell(mute)` (la **sourdine = ouverture du pavillon 0–1**) ; UI : tubeLength 0,01–2,5 m (défaut 0,5), lipsTension 0–1 (0,5), mute 0–1 (0,5), + `envAttack`, `vibratoFreq`, `vibratoGain`.

### B.9 Autres recettes trouvées seulement en extrait (pages bloquées) [HEUR-extrait]

- Forums modulaires (Mod Wiggler « best way to synthesize brass horns ») : « rapid modulation to add harmonics and simulate turbulence by modulating the filter or applying FM […] with a quick burst of a fast LFO » ; « a brief and dramatic envelope (**as much as one octave**) applied to oscillator pitch at the start of the note » ; « immediate attack and quick decay in a fast blast » ; vibrato retardé par une enveloppe lente sur l'amplitude de l'LFO. (Note : Reid déconseille la modulation de hauteur dans le transitoire ; à trancher [TEST].)
- Tutoriels « synth brass » 80s (LiveKeyboardist, YouTube) : dent de scie unique ; « more sharpness at the beginning […] then mellows out » → attaque rapide de l'enveloppe de filtre ; léger « swoop » vers la hauteur pour simuler l'attaque ; dérive de hauteur lente d'un LFO pour la densité d'une section.
- Serum (Mystic Alankar, « brass pluck ») : Osc A « Hypa », Osc B « Analog BD Sine », LFO 1 en mode enveloppe sur la position de warp des deux oscillateurs et le niveau de A.
- Yamaha « Manny's Modulation Manifesto: Solo Brass Voices », Baratatronix « Brass Synthesis », Attack Magazine (Synth Secrets : « Baddadan horn synth bass ») : **titres et URLs identifiés, contenu non lu**.

---

## C. Pages consultées

### C.1 Lues intégralement (fichiers récupérés)

1. https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-24.md — Synth Secrets 24 (SOS avril 2001) — 3 322 mots.
2. https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-25.md — Synth Secrets 25 (SOS mai 2001) — 3 187 mots.
3. https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-26.md — Synth Secrets 26 (SOS juin 2001) — 3 956 mots.
4. https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-27.md — Synth Secrets 27 (SOS juillet 2001) — 4 245 mots.
5. https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-23.md — Synth Secrets 23 Formant Synthesis (mars 2001) — parcouru (lignes Hz).
6. https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-12.md et part-13.md — FM (avril/mai 2000) — téléchargés ; **aucune mention de cuivre** (grep « brass/trumpet/horn » = 0).
7. https://raw.githubusercontent.com/micjamking/synth-secrets/master/README.md — index des 63 parties (via WebFetch).
8. https://raw.githubusercontent.com/musescore/MuseScore/v3.6.2/share/instruments/instruments.xml — tessitures MIDI (570 ko, parsé).
9. https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/instrument.py — tessitures/transpositions.
10. https://raw.githubusercontent.com/w3c/musicxml/v4.0/schema/musicxml.xsd — articulations et sourdines.
11. https://raw.githubusercontent.com/thestk/stk/master/src/Brass.cpp et include/Brass.h — modèle physique STK.
12. https://raw.githubusercontent.com/grame-cncm/faustlibraries/master/physmodels.lib — modèle physique Faust (sections brassLipsTable, brassLips, brassModel, wBell).
13. https://raw.githubusercontent.com/mjladd/devcontainer-csound/HEAD/csound_score_examples/FmChowningA.csd — FM Chowning.
14. https://raw.githubusercontent.com/fxrobin/infinite-synthwave/HEAD/synthwave/patches/library/dx7_BRASS_1.yaml — DX7 BRASS 1.
15. https://raw.githubusercontent.com/Ethycs/symcrash_python_AP/HEAD/presets/instruments/dx7_brass_1_v0.yaml — DX7 BRASS 1 (conversion ms).
16. https://raw.githubusercontent.com/zseramnay/Orchestration/HEAD/publications/Maresz-Formant_Reference_Orchestra_JNMR.tex — formants de l'orchestre (Maresz, 2026).
17. https://raw.githubusercontent.com/alainjouve/olymphys7/HEAD/public/search/textes/16-eq-17-memoire-Peut-on%20produire%20un%20son%20cuivre%20avec%20un%20tuyau%20d'arrosage%20%20.txt — mémoire Olympiades 2009 (LAUM).
18. https://raw.githubusercontent.com/tkgally/algorithmic-music/HEAD/wiki/instrument-acoustics-and-idiom.md — wiki acoustique (section Brass + principes transversaux + sources).
19. https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/HEAD/overtone/instruments/brass-instruments/trumpet/RESEARCH.md (+ trombone, french-horn) — notes tierces.
20. https://github.com/micjamking/synth-secrets/blob/master/part-25.md — page HTML GitHub (test de chargement OK).

### C.2 Bloquées par le proxy (EGRESS_BLOCKED / CONNECT 403) — non lues

- Sound On Sound : https://www.soundonsound.com/techniques/synthesizing-brass-instruments ; https://www.soundonsound.com/techniques/brass-synthesis-minimoog ; https://www.soundonsound.com/techniques/synthesizing-wind-instruments ; https://www.soundonsound.com/techniques/roland-sh101-arp-axxe-brass-synthesis (contenu obtenu via la copie GitHub).
- UNSW Joe Wolfe : https://newt.phys.unsw.edu.au/jw/brassacoustics.html ; https://www.phys.unsw.edu.au/jw/brassacoustics.html ; pages saxophone UNSW.
- Hirschberg 1996 : https://theorie.ikp.physik.tu-darmstadt.de/qcd/moore/ph225/shock.pdf ; https://pure.tue.nl/ws/files/1503964/617406.pdf ; https://www.semanticscholar.org/paper/Shock-waves-in-trombones-Hirschberg-Gilbert/… ; https://pubs.aip.org/asa/jasa/article-abstract/99/3/1754/751797/
- Acoustics Today (Moore) : https://acousticstoday.org/wp-content/uploads/2018/08/The-Acoustics-of-Brass-Musical-Instruments-Thomas-R.-Moore.pdf
- Benade 1973 : https://ccrma.stanford.edu/marl/Benade/documents/Benade-Trumpet-1973.pdf
- Pressbooks « Brass Techniques and Pedagogy » : https://pressbooks.palni.org/brasstechniquesandpedagogy/chapter/brass-acoustics/
- HyperPhysics : http://hyperphysics.phy-astr.gsu.edu/hbase/Music/orchins.html
- Wikipédia (en, fr, m) : Trumpet, Pitch of brass instruments, Trompette, etc.
- arXiv : https://arxiv.org/abs/2503.11536 (et tous les PDF arXiv cités).
- Tutoriels : https://yamahasynth.com/learn/synth-programming/mannys-modulation-manifesto-solo-brass-voices/ ; https://www.baratatronix.com/blog/brass-synthesis ; http://www.javelinart.com/FM_Synthesis_of_Real_Instruments.pdf ; Attack Magazine ; Reverb Machine ; Perfect Circuit.
- Sourdines/articulations : https://courses.physics.illinois.edu/phys406/…/G_Formosa_P498POM_Final_Report_Sp10.pdf ; https://brass.tonebase.co/blog/complete-guide-to-playing-mutes-on-a-trumpet ; https://kgumusic.com/blogs/news/the-art-of-muting-effects-and-techniques-for-brass-instruments ; https://www.evanrogersmusic.com/blog-contents/big-band-arranging/articulation ; https://offtonic.com/theory/book/3-3.html ; https://themoderntrumpet.com/2020/10/13/flutter-tongue-doodle-tongue-and-growl/
- Tessitures : https://tunableapp.com/instruments/trumpet-bb/range/ ; https://andrewhugill.com/OrchestraManual/trumpet_range.html ; https://timbreandorchestration.org/isfee/extreme-orchestration/brass/horn-family
- Divers testés en curl : hal.science, web.archive.org, archive.org, link.springer.com, researchgate.net, core.ac.uk, academia.edu, vsl.co.at, dsprelated.com, europepmc.org, jstor.org, musicradar.com, ableton.com, xferrecords.com, bing.com, duckduckgo.com — tous 403.
- GitHub API : `musescore/MuseScore` non autorisé via l'outil MCP (mais le fichier brut v3.6.2 était accessible en raw ; le chemin `master/share/instruments/instruments.xml` renvoie 404 sur la branche actuelle).

### C.3 Consultées seulement par extraits de recherche (WebSearch)

Wikipédia (Trumpet, Alto/Tenor/Baritone saxophone, Vibrato, Flutter-tonguing, Hand-stopping), HyperPhysics (formants), Luce & Clark 1965 (JAES), arXiv 1511.04247, JASA « The saxophone spectrum », Springer « Brassiness in Wind Instruments », Historic Brass Society Journal 2014 (Campbell, Chick & Myers), Tonebase (harmon), Mod Wiggler, LiveKeyboardist, Mystic Alankar (Serum), tutoriels DX7 (tonalux, deepsonic), brevets USPTO. Toutes marquées [HEUR-extrait] dans le rapport.

---

## D. Ce qui n'a pas été trouvé (ou pas lu)

1. **Valeurs de Meyer (« Acoustics and the Performance of Music »)** en accès direct : uniquement indirectement, via la validation de Maresz (concordance 93 % avec Meyer 2009) et l'extrait HyperPhysics. Aucune page de Meyer, Benade ni Fletcher & Rossing n'a pu être lue.
2. **Texte intégral de Hirschberg et al. 1996** : seul l'abstract (extrait). Les amplitudes de pression dans l'embouchure et la distance de formation du choc ne sont donc pas chiffrées à partir de l'article lui-même ; les 162 dB / 2 471 Pa viennent du mémoire lycéen encadré par le LAUM, les 166,9–167,2 dB d'une simulation (arXiv 1611.01025, via notes tierces).
3. **Durée d'attaque de la trompette seule** en ms (Luce & Clark ne donnent, en extrait, que la fourchette globale 14–85 ms et l'ordre des familles). Valeurs disponibles : trombone 46 ms et cor 107 ms (mesures tierces sur Philharmonia), 50 ms d'instabilité de hauteur (Reid), 0,18 s d'attaque simulée (arXiv 1511.04247).
4. **Amplitude de vibrato des cuivres en cents mesurée** : seulement « < ½ demi-ton de chaque côté » (Wikipédia, extrait) et « very low » (Reid). Pas de valeur pour le shake (rate en Hz).
5. **Spectres chiffrés des sourdines bucket et plunger**, et du cor bouché : uniquement des descriptions qualitatives. Pour straight, on n'a que « middle-bright » et « formants 1–3 kHz » (UNSW, extrait).
6. **Formants des saxophones ténor et baryton** : seules les « break frequencies » 618 Hz (ténor) et 837 Hz (alto) (extrait JASA) ; Maresz ne couvre que l'alto (F1 398 Hz).
7. **Un article SOS intitulé « Practical Brass Synthesis »** : n'existe pas sous ce titre ; les articles pratiques sont les parties 26 et 27. Les parties 12/13 (FM) ne contiennent pas de recette de cuivre FM ; la référence FM cuivre est Chowning 1973 (via l'exemple Csound) et le DX7 BRASS 1.
8. **Recettes Serum / Attack Magazine / Reverb Machine / Perfect Circuit / Yamaha « Manny's » / Baratatronix** : URLs identifiées, contenu non lisible (proxy). À relire dans un environnement sans blocage.
9. **Patchs d'usine Prophet-5 / OB-X « Brass »** avec valeurs : rien de lisible sur GitHub.
10. **Lecture directe des pages UNSW** (brassacoustics, saxophone) : impossible ; les faits UNSW ne sont présents qu'à travers des citations tierces (fiches GitHub, wiki tkgally) et un extrait.

---

## E. Synthèse opérationnelle pour le skill (à convertir en règles [DOC]/[HEUR]/[TEST])

1. **Source** : une dent de scie unique (cuivres = série harmonique complète) [DOC Reid 24/26/27] ; pour tuba/trombone, dent de scie ≈ 60 % + sub carré −1 oct à 100 % [DOC Reid 27, patch Roland].
2. **Amplitude** : attaque ≈ 100 ms (Minimoog) / carrée (SH-101), release quasi nul [DOC] ; vélocité → attaque plus courte [DOC] ; attaque « T » = montée instantanée puis seconde montée [DOC].
3. **Filtre** : passe-bas fermé au départ, enveloppe ADSR longue (600 ms A / 800 ms D / S 50 %) plus lente que l'amplitude ; résonance faible (2/10, « just a touch ») ; tracking 100 % ou un peu moins ; quantité d'enveloppe ∝ vélocité ; aftertouch → brillance [DOC Reid 25/26/27].
4. **Brassiness** : la brillance doit croître **beaucoup plus vite que le niveau** (fondamental +8 dB vs H9+ > 45 dB sur un crescendo [HEUR]) et de façon quasi seuil (choc au-delà d'un niveau, tuyau long/cylindrique cuivre plus que conique [DOC mémoire LAUM, HEUR-extrait Hirschberg]) → prévoir saturation/waveshaper pilotés par vélocité/macro plutôt qu'un simple cutoff [TEST].
5. **Growl d'attaque** : triangle ≈ 80 Hz sur la coupure pendant ≈ 50 ms, dosé par enveloppe AD et vélocité/aftertouch ; pas de modulation de hauteur pendant le transitoire [DOC Reid 25] — alternative FM/pitch-blip d'une octave signalée par des forums [HEUR-extrait, TEST].
6. **Vibrato** : 5–6,5 Hz (Reid 5 Hz, STK 6,137 Hz, DX7 6,13 Hz), très faible profondeur (< ½ demi-ton crête), retardé [DOC/HEUR-extrait].
7. **Formants fixes** (EQ/pics ne suivant pas la note) : trompette ≈ 1 050 Hz (Fp) / 1 200–1 400 Hz (pic large) ; cor ≈ 400 Hz + 740 Hz ; trombone ≈ 240 Hz + 600–800 Hz ; tuba ≈ 230 Hz + 200–400 Hz ; sax alto ≈ 400 Hz (+ coupure d'enveloppe ≈ 840 Hz), sax ténor coupure ≈ 620 Hz ; embouchure de trompette ≈ 750–820 Hz [DOC Maresz / HEUR-extrait HyperPhysics, JASA sax / HEUR UNSW].
8. **Sourdines** : straight = « middle-bright », cup = passe-bande ≈ 800–1 200 Hz, harmon = pic ≈ 1 500–2 400 Hz (Maresz : 2 358 Hz) + wah, bucket = très assourdi, plunger = wah manuel [DOC Maresz / HEUR-extrait].
9. **Articulations** : scoop (monte vers la note), plop (descend vers la note), doit (monte après), fall (descend après, plus long), shake (trille de lèvres rapide entre partiels), flutter 15–30 Hz (jusqu'à ~50), growl = FM par la voix, glissando trombone ≤ triton, pas de redéclenchement d'enveloppe en legato à pistons [DOC MusicXML / HEUR-extrait / DOC Reid 27].
10. **Tessitures** : voir tableau A.1 (MIDI sonnant, MuseScore) [DOC].
