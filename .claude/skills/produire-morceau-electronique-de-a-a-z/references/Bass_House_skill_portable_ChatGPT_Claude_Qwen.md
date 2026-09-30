# Compétence portable — production Bass House

Utilisation : fournir ce fichier comme consigne ou document de référence à ChatGPT, Claude ou à un modèle Qwen lancé dans Ollama. Il contient les connaissances et méthodes; son import ne donne **aucun accès automatique** à Ableton, Serum 2, aux fichiers du projet ni au contrôle de l'ordinateur. Pour agir dans Live, l'assistant doit disposer d'un outil/bridge compatible et des permissions correspondantes.

## Instruction commune à l'assistant

Tu es un assistant de production musicale pour Ableton Live 12 Suite et Serum 2. Réponds en français, avec les noms de paramètres des instruments en anglais. Déduis le style, le BPM, la tonalité et le rôle du son à partir de la demande. Donne une recette concrète, des valeurs de départ, un motif MIDI et un contrôle dans le mix. Distingue ce qui est documenté par le fabricant de tes propres propositions de réglage. Pour une fonction incertaine, vérifie le manuel; si tu es hors ligne, explique l'incertitude. Ne prétends pas avoir écouté un audio, vu une vidéo, ouvert Live, changé un preset ou mesuré un signal si tu ne l'as pas fait. Ne copie pas Basic Shapes lorsque l'utilisateur demande une autre table. Sauvegarde l'identité des versions et ne remplace pas un projet existant sans demande explicite.

## Mode de réponse

1. Objectif sonore et rôle dans l'arrangement.
2. Source, oscillateurs, filtres, enveloppes et modulation, puis effets.
3. MIDI, automatisations et variations sur 4–16 mesures.
4. Contrôle kick/sub, niveau, mono, stéréo, transitoires, CPU et export.

---
## Recettes générales

# Recettes Bass House

Valeurs indicatives à ajuster au tempo, à la hauteur et au mix.

| Famille | Construction | Enveloppe / modulation | Vérification |
|---|---|---|---|
| Sub | Sine Operator ou Serum 2, mono | Attaque 2–10 ms si clic, release 60–100 ms, plus courte que l'écart entre deux notes (`kick-bass-equilibre` §2) ; notes enchaînées : legato mono plutôt qu'une release courte, glide si voulu | Somme kick/sub et phase; laisser des silences MIDI |
| Wobble / growl | Wavetable riche, filtre LP/BP, FM légère et saturation dosée | LFO sync 1/8 ou motif dessiné; moduler table et filtre | Réponse au kick; sub séparé si timbre très variable |
| Reese | Deux saw désaccordées de ±15 (doux) à ±30 cents (DnB) ; sub sinus séparé | Filtre lent, unison prudent | Contrôler battements et mono du grave |
| Donk / métallique | Operator FM, carrier et modulateur sine, ratio 2 puis 2,7 | Decay modulateur 30–200 ms; pitch bref en option | Ratio non entier souvent inharmonique; contrôler aigus |
| Stab / pluck | Saw ou square, filtre LP/BP | A 0–10 ms, D 80–300 ms, S bas, R 50–180 ms | Contretemps choisis, espaces de la basse |
| Pad chaud / sombre | Saw peu désaccordées, LP, éventuellement noise | A 300–1500 ms, R 1–4 s; mouvement lent | Écarter du sub, réduire dans le drop si masquage |
| Pad rythmique | Pad simple et gate de volume | Motif 1/8 ou 1/16 avec silences | Préserver transitoires kick/basse |
| Lead | Saw/square ou FM modérée; mono si glide | Portamento initial 30–120 ms, bends; delay interne de Serum 2 ou plug-in tiers sur retour (règle 6 d'`ableton-live-session`) | Hook bref, répété et varié, lisible en mono |
| Impact | Hit, bruit, queue; sub tonal facultatif | Enveloppes distinctes, reverse d'une queue | Éviter cumul de sub avec kick du drop |

## Exercice à 126 BPM en Fa mineur

Sur une mesure de 16 doubles croches, kick sur 1, 5, 9, 13; stab Ab–C–Eb sur 3 et 11; réponse growl sur 7 et 15. Garder les autres positions vides. Variante: déplacer le second stab à 12, puis comparer au groove réel.

## Diagnostic

- FM: le ratio, l'index et l'enveloppe déterminent ensemble le timbre; aucune paire de ratios ne garantit un son « robot ».
- Écouter kick et sub ensemble avant de choisir un coupe-bas ou sidechain.
- Resampler plusieurs variations, découper sans clic puis vérifier la hauteur et les transitoires après transposition.
- Comparer toute saturation/soothe/compression au même niveau; enlever l'effet si le son perd son attaque ou son groove.


## Wavetable Ableton

# Wavetable dans Live 12 : applications Bass House

Références vérifiées : [manuel officiel, section 30.13](https://www.ableton.com/en/manual/live-instrument-reference/#wavetable), [pads évolutifs](https://www.ableton.com/fr/blog/pad-it-out-10-ways-make-distinctive-pad-sounds/), [charge CPU](https://help.ableton.com/hc/en-us/articles/360000036930-Managing-CPU-load-when-using-Wavetable).

## Architecture et réglage

- Deux oscillateurs wavetable principaux; déplacer leur **position** change le timbre, pas la note. Commencer avec un seul et écouter les positions avant d'ajouter un second.
- Sous-oscillateur : **Tone 0 %** donne une onde sinusoïdale; monter Tone ajoute des harmoniques. Comparer avec un sub sur piste séparée pour garder un contrôle indépendant.
- Deux filtres et un onglet **Matrix**; l'onglet **Mod Sources** contient l'enveloppe Amp, Env 2, Env 3 et deux LFO. Assigner explicitement Env 2 au cutoff pour une attaque de pluck; l'enveloppe Amp règle sa longueur audible.
- Dans Matrix, moduler la position de table et le cutoff avec des quantités distinctes. Pour un wobble, choisir un LFO synchronisé au tempo; tester Retrigger activé pour une attaque répétable, désactivé pour un mouvement continu. Le mouvement de table seul peut être faible si les formes adjacentes sont proches : écouter puis choisir une autre table ou élargir la plage.
- Mono + Glide pour une basse/lead glissée; Glide agit lorsque les notes se chevauchent en mode Mono. Poly pour les accords de pad. Choisir l'unison avec parcimonie : Classic pour une largeur classique, Position Spread pour répartir les positions de table. Vérifier le bas en mono.

## Trois prototypes à construire et comparer

1. **Wobble body** : OSC 1 riche → filtre LP/BP → LFO sync sur cutoff, avec modulation de position plus lente ou de moindre amplitude. Note courte sur les trous de la basse; sub séparé au départ. Saturation : Drive du filtre de Wavetable ou plug-in tiers (pas de Saturator natif, règle 6 d'`ableton-live-session`), ajustée dans le morceau.
2. **Stab** : OSC 1 saw → Env 2 court sur cutoff; Amp avec attaque brève et sustain faible. Tester vélocité sur cutoff dans l'onglet MIDI; jouer deux accents différents en contretemps et comparer.
3. **Pad évolutif** : poly, unison Classic modéré, Amp à attaque/release longs; LFO 1 lent sur position OSC 1 et LFO 2 à autre vitesse sur filtre. Automatiser niveau et filtre par section. L'article Ableton décrit aussi une modulation croisée LFO 1 → vitesse LFO 2 → position de table.

## Performance et contrôle

- Oscillateur supplémentaire, voix d'unison, longues releases et second filtre multiplient le travail CPU. Dans un accord à trois notes, deux oscillateurs et huit voix d'unison peuvent produire 48 voix. Imprimer le patch en audio une fois stabilisé.
- Le mode Hi-Quality (nom à vérifier dans l'interface) peut changer subtilement le son; comparer avant le rendu final et ne pas le présenter comme une amélioration automatique.
- Vérifier en contexte avec kick, sub et hats. Les fréquences de coupe et niveaux de sidechain restent dépendants du mix, pas de l'instrument.


## Traitement spectral Ableton

# Traitement spectral dans Ableton Live 12 Suite

Sources : [manuel des effets Live 12, Spectral Resonator et Spectral Time](https://www.ableton.com/en/manual/live-audio-effect-reference/), [explication FFT par Ableton](https://www.ableton.com/en/blog/spectral-sound-a-look-at-live-11s-new-spectral-devices/), [guide Spectral Time](https://www.ableton.com/fr/blog/freeze-delay-and-deconstruct-sound-design-with-spectral-time/). Vérifié le 28 septembre 2026.

**Dans ce workflow** : Spectral Resonator et Spectral Time sont des effets natifs ; la règle 6 d'`ableton-live-session` les exclut des chaînes de mix. Les employer seulement sur une piste de sound design dédiée, imprimer le résultat (`resampling`) puis retirer le device ; jamais sur un retour ni dans une chaîne de mix. Les écoutes demandées ci-dessous reviennent à l'utilisateur.

## Clarifier le vocabulaire

Il n'existe pas un unique « mode spectral » commun à Wavetable et aux effets de Live. **Wavetable** est un instrument qui parcourt des formes d'onde; ses effets d'oscillateur sont FM, Classic et Modern selon le manuel. **Spectral Resonator** et **Spectral Time** sont des effets audio qui décomposent le signal par FFT, modifient ses composantes fréquentielles puis le resynthétisent. **Spectrum** ne fait qu'analyser et afficher le signal; il ne le transforme pas.

| Effet | Action principale | Usage Bass House |
|---|---|---|
| Spectral Resonator | Résonances accordées, harmoniques, decay et modulation | Tonaliser un hit, vocal chop, percussion; générer une réponse métallique ou un pad à partir d'une source courte |
| Spectral Time | Gel spectral et retard dont les bandes de fréquences peuvent évoluer différemment | Transition figée, queue d'impact, texture glitch, riser et espace mouvant |
| Spectrum | Mesure des fréquences | Vérifier la hauteur et les zones d'énergie, sans traitement audio (dans ce workflow : SPAN, plug-in tiers ; pas de nouveau Spectrum, règle 6) |

## Spectral Resonator : procédure

1. Placer l'effet après une source audio courte et riche (clap, voix, bruit, stab), de préférence en parallèle pour préserver l'attaque originale. Essayer une note de tonalité en mode **Internal**; en mode **MIDI**, choisir une piste MIDI dans External Source et jouer les notes ou accords voulus.
2. Régler **Decay** selon la place dans le groove; **Harmonics** détermine la brillance et **HF/LF Damp** atténuent les partiels hauts/bas. **Stretch** change l'espacement des harmoniques : explorer avec prudence si l'effet devient dissonant. **Shift** transpose le spectre de l'entrée, pas celui du résonateur.
3. Tester **None**, **Chorus**, **Wander** et **Granular** dans la section Modulation. Pour un son robotique court, commencer sans modulation ou avec Chorus subtil; pour une texture mouvante, essayer Wander; Granular donne un grain fragmenté.
4. Sur la piste de sound design dédiée, régler Dry/Wet à 100 %, filtrer au besoin la sortie traitée et imprimer une sélection audio. En MIDI Poly, MIDI Gate est toujours actif; garder de courtes notes pour des réponses rythmiques.

## Spectral Time : procédure

1. Choisir **Freezer** pour tenir une tranche de son, ou **Delay** pour répéter des composantes. Le gel peut être manuel, déclenché à la détection de transitoires (**Onsets**) ou à intervalles synchronisés (**Sync**).
2. Sur une voix ou un impact de fin de phrase, activer Freeze juste avant le changement de section; automatiser le volume de retour puis enregistrer la queue. Pour un glitch, utiliser Retrigger Sync et raccourcir l'intervalle.
3. Dans Delay, **Tilt** retarde différemment graves et aigus, **Spray** disperse les temps de manière aléatoire, **Mask** limite Tilt/Spray à une région grave ou aiguë, **Shift** déplace la fréquence des répétitions. Garder la basse principale hors de la sortie traitée si elle trouble le kick.
4. **Resolution** élevé améliore la précision mais augmente la latence; réduire en jeu/monitoring si nécessaire. L'ordre Freezer → Delay ou Delay → Freezer se choisit selon l'effet désiré. Dry/Wet global à 100 %, puis imprimer et retirer le device.

## Vérifications

- Écouter en solo puis dans le drop à niveau égal. Les effets FFT peuvent étirer les attaques et produire des queues qui recouvrent la mesure suivante.
- Imprimer en audio et aligner les transitoires si le résultat doit rester très serré; regarder la latence de l'appareil dans Live au besoin.
- Vérifier hauteur, mono et conflit avec sub/kick; garder l'effet comme couche de caractère lorsque la fondamentale du son principal doit rester stable.


## Stabs Serum 2 sans Basic Shapes

# Stabs House dans Serum 2, sans Basic Shapes

Références Xfer Records : [sélection des tables](https://xferrecords.com/web-manual/serum-2/choosing-oscillator-or-filter-options), [routage des oscillateurs](https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter), [manuel Serum 2](https://xferrecords.com/manual/serum-2/docs) (liste des warps relevée dans le dépôt : `sound-designer-serum/references/moteurs-synthese.md`), [modulation des commandes](https://xferrecords.com/web-manual/serum-2/using-knobs-and-sliders). Les catégories **Analog, Digital, S2 Tables, Spectral, Vowel** sont visibles dans le sélecteur. Les noms individuels varient avec bibliothèque/version : spécifier catégorie + caractère et auditionner plusieurs tables. Réglages ci-dessous = points de départ personnels, pas valeurs prescrites par Xfer.

Notes en numérotation Ableton, C3 = 60 (la version d'origine les écrivait en notation scientifique, une octave au-dessus : « Ab3 C4 Eb4 ») ; le numéro MIDI fait foi. Filtres : noms de Serum 2 `Low 12/24`, `Band` (`MG Low` pour la variante ladder). La catégorie « S2 Tables », le nom « Default Shapes » et le preset `- Init -` ne figurent pas dans la doc Serum 2 du dépôt : les relever dans l'interface avant de les prescrire. Effets : ceux de Serum 2 (DISTORTION, CHORUS, DELAY, REVERB internes) ; dans Live, plug-ins tiers seulement (règle 6 d'`ableton-live-session`), Hybrid Reverb toléré sur un retour.

## Démarrage commun

Partir de `- Init -`. Dans OSC A choisir Wavetable et une table de la catégorie proposée, jamais Basic Shapes/Default Shapes. Activer FILTER 1; contrôler le routage OSC A → FILTER 1 (le filtre peut être désactivé sur le preset initial). ENV 1 règle la durée audible; ENV 2 modulera le cutoff. Dans Serum 2, le routage **Direct** contourne filtre et effets : ne pas l'utiliser sur une couche censée être filtrée. Écouter sur une note médium avant de programmer l'accord.

| Patch | Oscillateurs et filtre | ENV 1 (A/D/S/R) | ENV 2 → cutoff et traitement |
|---|---|---|---|
| **Organ chord sec** | OSC A catégorie Analog, choisir table à harmoniques régulières; WT POS à l'oreille, Unison 1–2. FILTER 1 `Low 12`, cutoff médium. | 3 ms / 180 ms / 0–15 % / 90 ms | ENV 2 : 0 / 120 ms / 0 / 70 ms, plage positive modérée; DISTORTION douce interne, petite room sur retour (Hybrid Reverb ou plug-in tiers). Chord Fm7 sans F grave : Ab2 C3 Eb3 (MIDI 56 60 63). |
| **Vowel stab « wah »** | OSC A catégorie Vowel, choisir table dont les positions contrastent; Unison 1. FILTER 1 `Band`, résonance prudente. | 2 ms / 220 ms / 0 / 80 ms | ENV 2 : 0 / 160 ms / 0 / 60 ms sur WT POS et cutoff, mouvements de sens ou profondeur différents; distorsion légère. Tester Ab2–C3 (MIDI 56–60) au contretemps, puis faire écouter en mono. |
| **Metallic / robot** | OSC A catégorie Digital ou Spectral (table wavetable, pas oscillateur de synthèse Spectral); Unison 1. Tester le warp `Sync`, ou une FM depuis OSC B ou SUB (source routée `None`) à faible profondeur. FILTER 1 `Band` ou `Low 24`. | 0–3 ms / 130 ms / 0 / 70 ms | ENV 2 : 0 / 90 ms / 0 / 40 ms sur cutoff et Warp, faible plage. EQ après distorsion si les aigus sifflent; pour un hit vraiment métallique, jouer une seule note puis resampler. |
| **Warm disco / piano-like** | OSC A catégorie S2 Tables ou Analog, choisir une table douce mais riche; OSC B optionnel, table contrastée à -12 dB environ, routée aussi au filtre. FILTER 1 `Low 24`. | 4 ms / 280 ms / 10–25 % / 150 ms | ENV 2 : 0 / 190 ms / 0 / 80 ms sur cutoff. CHORUS discret interne, puis delay filtré (DELAY interne ou plug-in tiers en retour); accord Fm9 sans fondamentale : Ab2 C3 Eb3 G3 (MIDI 56 60 63 67). |
| **Rave sync stab** | OSC A catégorie Analog ou Digital, table riche; Warp Sync en montant doucement jusqu'à l'attaque désirée. FILTER 1 `Low` ou `Band` selon couleur. | 0–3 ms / 120–200 ms / 0 / 60 ms | ENV 2 courte sur Warp et cutoff; automate la quantité de Warp aux fins de phrases. Une seule triade brève suffit avant le drop. |

## MIDI et arrangement

À 126 BPM, essayer kick sur 1, 5, 9, 13 de la grille 1/16; stab sur 3 et 11 pour les contretemps, puis déplacer le second à 12 si le groove le réclame. Longueur MIDI initiale 1/16–1/8; la queue réelle dépend de ENV 1 et des effets. Accentuer la première vélocité et diminuer la seconde. Tester d'abord une seule recette dans le break puis une version raccourcie dans le drop. Si la fondamentale du stab se bat avec la basse, enlever la fondamentale de l'accord ou monter l'octave.

## Diagnostic

- Si le filtre ne répond pas, vérifier FILTER 1 activé et route OSC A → FILTER 1 avant d'augmenter ENV 2.
- Si le stab reste continu, raccourcir ENV 1 et vérifier les retours delay/reverb. ENV 2 seule ne coupe pas le volume.
- Si « wah » ne parle pas, essayer une autre position/table Vowel avant de multiplier les effets; garder la modulation formant distincte de l'amplitude.
- Si l'accord brouille le kick/sub, réduire la durée et le niveau avant EQ/sidechain. Comparer l'attaque à volume égal avec et sans saturation.


## Sources et vidéos

# Sources et vidéos

Pages et descriptifs consultés le 28 septembre 2026. Le contenu complet des vidéos n'a pas été visionné; vérifier l'interface et les étapes avant de citer un réglage exact.

## Documentation officielle

- [Manuel Ableton Live 12](https://www.ableton.com/en/live-manual/12/) : Operator, Wavetable, Simpler, effets et routage.
- [Wavetable dans le manuel Live 12](https://www.ableton.com/en/manual/live-instrument-reference/#wavetable) : architecture, Matrix, sources de modulation, sub, filtres, unison et qualité.
- [Pad It Out, Ableton](https://www.ableton.com/fr/blog/pad-it-out-10-ways-make-distinctive-pad-sounds/) : mouvements de table et LFO pour pads.
- [Gestion de la charge CPU de Wavetable, Ableton](https://help.ableton.com/hc/en-us/articles/360000036930-Managing-CPU-load-when-using-Wavetable) : calcul des voix et coût des effets.
- [Learn Live : Wavetable, Ableton](https://www.ableton.com/en/live/learn-live/instruments-and-effects/) : courtes leçons sur les oscillateurs, effets, modulation et unison.
- [Spectral Resonator et Spectral Time, manuel Live 12](https://www.ableton.com/en/manual/live-audio-effect-reference/) : paramètres et conseils officiels des deux effets.
- [Spectral Sound, Ableton](https://www.ableton.com/en/blog/spectral-sound-a-look-at-live-11s-new-spectral-devices/) : explication du traitement FFT.
- [Freeze, Delay and Deconstruct, Ableton](https://www.ableton.com/fr/blog/freeze-delay-and-deconstruct-sound-design-with-spectral-time/) : usages créatifs de Spectral Time.
- [Instruments Live](https://www.ableton.com/en/manual/live-instrument-reference/) : FM, wavetable et sampling.
- [Effets Live](https://www.ableton.com/en/manual/live-audio-effect-reference/) : notamment Saturator.
- [Manuel Serum 2, Xfer Records](https://xferrecords.com/web-manual/serum-2/welcome) : oscillateurs, filtres et modulation.
- [Getting Started With Serum, Xfer](https://support.xferrecords.com/article/50-getting-started-with-serum) : article Serum 1 ; ne pas en reprendre les emplacements pour Serum 2.
- [Serum 2 : sélection et routage](https://xferrecords.com/web-manual/serum-2/choosing-oscillator-or-filter-options) et [routage des oscillateurs](https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter) : catégories et chemin vers FILTER 1.
- [Manuel Serum 2, index](https://xferrecords.com/manual/serum-2/docs) : page d'accueil du manuel ; liste des warps (Sync, FM…) relevée dans `sound-designer-serum/references/moteurs-synthese.md`.

## Vidéos repérées

- [Smooth Operator, Ableton](https://www.ableton.com/en/blog/smooth-operator-watch-sound-design-maestro-lives-fm-synth/) : démonstration Operator, hits, pads et Reese.
- [Wavetable Synth – Full Guide for Beginners](https://www.youtube.com/watch?v=aLOYhVQbhp8) : tour des fonctions (vidéo tierce).
- [FM synthesis with Ableton Operator](https://www.youtube.com/watch?v=s1cxl_AiWqE) : série vidéo sur la FM (vidéo tierce).
- [Ableton Synths Tutorial: Analog, Wavetable, Operator](https://www.youtube.com/watch?v=Z5ivvUJHY6E) : subs, plucks et leads (vidéo tierce).

Les manuels font foi pour les noms des commandes. Pour un exemple Serum 2 récent, vérifier sa version et l'auteur avant d'en reprendre les paramètres.
