# Fiches pratiques de sound design

Base de connaissances utilisable en session. Une fiche par idée actionnable, tirée des recherches du 18 septembre 2026.

**Convention** : `[D]` documenté par la source citée · `[I]` interprétation ou extrapolation, à vérifier à l'oreille. **Les exemples par genre sont majoritairement `[I]`** : les sources donnent la technique, rarement son application à un genre précis.

**Repères de temps** — 120 BPM : noire 500 ms, croche 250 ms, mesure 2 s. 126 BPM : noire 476 ms, croche 238 ms, mesure 1,905 s. 174 BPM : noire 345 ms, croche 172 ms, mesure 1,379 s.

---

## FICHE 01 — Une seule source tient le fondamental

**Problème résolu** — Le grave est flou, la basse « sonne moins grave » quand on ajoute un sub, le niveau du sub fluctue d'une note à l'autre.

**Explication** — Deux oscillateurs désaccordés produisent un battement, c'est-à-dire une modulation d'amplitude lente de la fondamentale. Sur un médium c'est un effet ; sur un sub c'est un fader de volume aléatoire. Et quand deux sources couvrent la même fondamentale, leurs crêtes et creux ne coïncident pas : la somme peut être plus faible que chaque partie.

**Serum 2** — Oscillateur unique, sinus ou triangle. **Unison 1**. Détune 0. Width 0. Pas de chorus. Si un filtre résonant est utilisé, activer le **key tracking**, sinon chaque note voit un harmonique différent boosté.

**Ableton Live 12** — Décider quelle piste tient 30–80 Hz, puis coupe-bas **100 à 120 Hz, 24 dB/oct** sur toutes les autres. Utility en fin de chaîne avec **Bass Mono** activé. Vérifier en mono : si le sub maigrit, c'est de la phase, pas du niveau.

**Par genre** `[I]` — **Bass house** : la basse tient le fondamental, le kick est choisi « pas trop grave » pour lui laisser la place. **Future house** : même logique, le lead vit au-dessus de 200 Hz. **DnB** : le sub sinus tient 40–60 Hz, le Reese est coupé-bas au-dessus, c'est une architecture à deux couches obligatoire.

**Erreurs fréquentes** — Empiler un sub sous une basse qui a déjà sa fondamentale. Mettre de l'unison sur le sub « pour l'épaissir ». Vérifier le grave uniquement en stéréo.

**Source** — Sound on Sound, *Mixing Bass* et *Q. What's the best way to create sub-bass synth sounds?* C'est le seul point sur lequel toutes les sources sérieuses convergent.

---

## FICHE 02 — Le détune d'un Reese est un réglage de tempo, pas de largeur

**Problème résolu** — Le Reese « pulse » trop vite ou trop lentement, et son mouvement change quand la ligne de basse monte ou descend.

**Explication** — La fréquence de battement est la **différence** entre les deux fréquences, pas un pourcentage. À 30 cents sur un Fa1 (43,65 Hz), l'écart est de 0,76 Hz, soit un cycle toutes les 1,3 seconde. La même valeur de détune sur une note une octave plus haut donne un battement **deux fois plus rapide**. `[I]` Aucune source ne le dit, c'est une conséquence arithmétique.

**Serum 2** — 2 oscillateurs saw, mono, legato. Détune **±28 cents** comme point de départ. ±15 = lent et doux, ±30 = signature drum & bass. Filtre LP 24 dB vers 650 Hz, résonance ~14 %.

**Ableton Live 12** — Régler le détune **à l'oreille sur la note la plus grave** de la ligne, pas sur la plus aiguë. Coupe-bas 120 Hz sur la piste du Reese, sub sinus mono sur une piste séparée jouant la même ligne MIDI.

**Par genre** `[I]` — **DnB** : c'est le terrain d'origine, ±30 cents, ligne tenue sur 1 à 2 mesures pour que le battement ait le temps de se déployer. **Bass house** : ±15 cents suffisent, les notes sont plus courtes. **Future house** : rarement utilisé, le genre préfère les basses filtrées nettes.

**Erreurs fréquentes** — Croire que le détune règle la largeur stéréo. Laisser le Reese tenir le fondamental. Régler le détune sur une note aiguë puis s'étonner que le grave batte trop lentement.

**Source** — Attack Magazine *Reese Bass Redux* et Native Instruments, concordants sur ±27 à ±30 cents. Le Reese d'origine (Kevin Saunderson, 1988) était fait sur un Casio CZ en distorsion de phase, pas avec deux scies.

---

## FICHE 03 — Le LFO d'un growl doit être en mode Trigger

**Problème résolu** — Le growl ne sonne pas pareil d'une note à l'autre, impossible à reproduire, impossible à caler sur le rythme.

**Explication** — En mode libre, le LFO tourne en continu et chaque note l'attrape à une phase différente. Le mouvement du filtre commence donc au hasard. En mode Trigger, la forme du LFO redémarre à chaque note : le growl devient déterministe.

**Serum 2** — LFO en **mode Trig**. Destination : cutoff d'un filtre formant, High Notch, ou le warp de l'oscillateur. Profondeur **négative** (−50 à −75) pour que le filtre se ferme quand le LFO monte. Résonance 20–40 % pour que les voyelles restent définies.

**Ableton Live 12** — Rien à faire côté Live, c'est un réglage interne. Mais si le growl doit changer entre sections, mapper la vitesse du LFO à une macro et automatiser la macro, pas le LFO.

**Par genre** `[I]` — **Bass house 126 BPM** : LFO en 1/8 ou 1/16. **DnB 174 BPM** : 1/8 ou 1/16, mais les valeurs absolues diffèrent. **Future house** : le genre utilise peu le growl, plutôt un filtre qui s'ouvre sur l'enveloppe.

**Erreurs fréquentes** — Laisser le mode Off par défaut. Confondre mode Env (une seule passe, donc une enveloppe) et mode Trig (redémarre et boucle).

**Source** — Patch BassGorilla sur Serum, corroboré par monosounds. Blogs de vendeurs de presets : chiffres à vérifier, mécanisme fiable.

---

## FICHE 04 — Les recettes de growl trouvées en ligne sont calées sur 140–150 BPM

**Problème résolu** — On applique un tutoriel à la lettre et le growl est mou, lent, sans rapport avec le groove.

**Explication** — La quasi-totalité des tutoriels de growl visent le dubstep et le drum & bass, à 140 ou 150 BPM. Un LFO noté « 1/2 » y dure environ 850 ms. **À 126 BPM, le même 1/2 dure 952 ms** : presque une seconde de balayage, ce qui n'a plus rien à voir avec le rythme d'un morceau de bass house.

**Serum 2** — Diviser par deux ou par quatre la valeur annoncée. Un 1/2 de tutoriel devient un 1/4 ou un 1/8. Vérifier à l'oreille contre la batterie, pas contre le compteur.

**Ableton Live 12** — Régler le LFO en synchro tempo, pas en Hz, pour que le patch survive à un changement de BPM. Serum 2 synchronise aussi les **enveloppes** au BPM : donner à Env 2 un decay d'une noire plutôt qu'une valeur en millisecondes.

**Par genre** `[I]` — **Bass house 126** : 1/8 pour un growl qui parle, 1/16 pour un growl agressif. **Future house 125** : idem. **DnB 174** : les valeurs des tutoriels s'appliquent presque telles quelles, c'est le tempo d'origine.

**Erreurs fréquentes** — Copier une valeur de LFO sans regarder le tempo du tutoriel. Régler le LFO en Hz puis changer le tempo du projet.

**Source** — Observation transversale sur les patchs relevés (BassGorilla, monosounds, EDMTemplates), tous en 140–150 BPM. `[I]` Le calcul de transposition est de moi.

---

## FICHE 05 — Donner du grain à un sub sans casser le mono

**Problème résolu** — Le sub sinus est propre mais inaudible sur petite enceinte ; dès qu'on l'épaissit avec de l'unison ou un chorus, la mono s'effondre.

**Explication** — Toute technique d'épaississement basée sur plusieurs voix ou sur le temps (unison, chorus, delay court) crée des différences de phase entre canaux. Sous 120 Hz, ces différences s'annulent en mono. La seule voie propre est de **déformer la forme d'onde elle-même**, ce qui ajoute des harmoniques sans créer de voix multiples.

**Serum 2** — Oscillateur sinus, **unison 1**, width 0. `WARP` = **`Odd/Even` à 30 %** (dominante impaire, plus creux et plus carré) ou **`Sine Shaper`** à faible dose. Le paramètre `Odd/Even` à 50 % est le neutre documenté.

**Ableton Live 12** — En alternative native : Saturator ou Drum Buss en insert, mais attention, le paramètre `Transients` du Drum Buss **n'agit qu'au-dessus de 100 Hz**, il ne fera rien sur le sub. Vérifier avec Utility Bass Mono activé que rien ne change.

**Par genre** `[I]` — **Bass house et future house** : un peu d'`Odd/Even` rend le sub audible sur un laptop sans l'élargir. **DnB** : la couche sub reste sinus pur, le grain vient du Reese au-dessus.

**Erreurs fréquentes** — Ajouter un chorus « juste un peu » sur le sub. Confondre largeur et épaisseur.

**Source** — Manuel officiel Serum 2 pour `Odd/Even` et `Sine Shaper`. `[I]` L'application au sub mono est mon raisonnement.

---

## FICHE 06 — La fondamentale manquante : saturer pour traduire

**Problème résolu** — La basse disparaît sur un téléphone, une enceinte Bluetooth ou un laptop, alors qu'elle est parfaite au studio.

**Explication** — Une petite enceinte ne reproduit pas 40 Hz. Mais si le son contient des harmoniques à 80, 120 et 160 Hz, **l'oreille reconstruit la fondamentale absente** à partir de leur espacement. La note perçue reste la même. C'est un phénomène psychoacoustique documenté, pas un truc de mixage.

**Serum 2** — Warp `Tube`, `Tape Sat.` ou `Soft Sat.` sur l'oscillateur, ou un filtre avec le paramètre **`FAT`**, qui ajoute de la saturation dans le chemin de résonance.

**Ableton Live 12** — Sound on Sound préfère la **distorsion en parallèle** plutôt qu'en insert : une copie de la basse, saturée, avec un **passe-bas vers 2–3 kHz** si le boost est important, pour ne pas étouffer l'air des voix. Dans un Audio Effect Rack, chaîne sèche + chaîne saturée, dosage au fader.

**Par genre** `[I]` — **Bass house** : la saturation fait partie du son, pas seulement de la traduction. **Future house** : dose légère, le genre est plus propre. **DnB** : essentiel, le sub seul ne passe aucun système grand public.

**Erreurs fréquentes** — Booster 40 Hz à l'EQ pour compenser, ce qui mange la marge sans rien rendre audible. Saturer sans passe-bas, ce qui encombre les médiums.

**Source** — MusicRadar et Amped Studio sur les 808 ; Sound on Sound *Mixing Bass* pour la distorsion parallèle. Phénomène de la fondamentale manquante confirmé par l'article ISMIR 2024 sur la 808.

---

## FICHE 07 — Accorder le kick : ce que dit la recherche

**Problème résolu** — Faut-il accorder le kick à la tonalité, et qu'est-ce que ça coûte de le descendre.

**Explication** — La grosse caisse de la TR-808 a une fondamentale médiane mesurée à **49,48 Hz, soit un sol**. La descendre coûte cher et de façon non linéaire : une quarte plus bas, on perd **11,8 dB** sur la fondamentale, dont 6,3 dB dus à la réponse moyenne des enceintes et 5,5 dB à la sensibilité de l'oreille. Mais si le kick est **saturé**, donc riche en partiels, la même transposition ne coûte que **4,5 dB**.

**Serum 2** — Kick sinus + enveloppe de pitch. Pour le rendre transposable vers le bas, ajouter un warp de distorsion qui crée des partiels. Enveloppe de pitch **20–70 ms** pour un caractère 808, **200–500 ms** pour un caractère 909.

**Ableton Live 12** — Analyser le kick avec SPAN pour lire sa fréquence dominante entre 60 et 100 Hz. Rester **dans ±3 demi-tons** sur un sample pour éviter les artefacts d'étirement.

**Par genre** — **Bass house en la mineur** : La1 = 55 Hz, **au-dessus** du sol natif, donc situation favorable, aucun arbitrage. **Deep house en fa mineur** : Fa1 = 43,65 Hz, deux demi-tons sous le natif mais au-dessus du seuil de 41,2 Hz identifié comme limite. Gérable, et la saturation suffit à compenser. **DnB** : le kick est court et le sub tient la note, l'argument s'applique faiblement.

**Erreurs fréquentes** — Se tromper d'octave : l'article utilise la notation scientifique, **le sol de la 808 s'affiche G0 dans le piano roll d'Ableton** (Do3 = 60). Croire qu'on perd la justesse : non, seul le timbre change.

**Source** — Emmanuel Deruty, *Harmonic and Transposition Constraints Arising from the Use of the Roland TR-808 Bass Drum*, ISMIR 2024, p. 78–85. Réserve : aucune mesure sur machine réelle, aucun test d'écoute, valeurs modélisées.

---

## FICHE 08 — Ce qui fait qu'un pluck sonne

**Problème résolu** — Le pluck sonne « coupé » ou « électronique » au lieu de sonner pincé.

**Explication** — Ce n'est pas le decay court qui fait le pluck, c'est le **différentiel entre l'enveloppe de filtre et l'enveloppe d'amplitude**. Sur une corde réelle, l'harmonicité chute **plus vite** que l'amplitude : le son s'assombrit en s'éteignant. Un decay d'ampli court avec un filtre statique donne un son tronqué, pas un pluck.

**Serum 2** — Amp : A 0 ms, D 180–250 ms, S 0. Filtre LP 24 dB, cutoff au repos 600–800 Hz, key tracking 0,5–0,7. **ENV 2** (A 0, D **120–160 ms**, S 0) vers le cutoff, pic vers 3–4 kHz. Règle : **le decay du filtre vaut 60 à 70 % de celui de l'ampli**. Résonance 15–25 % maximum.

**Ableton Live 12** — Même logique dans Wavetable avec Env 2 vers le cutoff, ou dans Operator avec une enveloppe sur le niveau du modulateur, ce qui produit le même effet **sans filtre**.

**Par genre** `[I]` — **Future house** : le pluck est le son signature du genre, souvent FM à ratio non entier pour le côté cloche. **Bass house** : pluck plus court et plus saturé. **DnB** : pluck très court, 80–120 ms, pour ne pas encombrer un tempo rapide.

**Erreurs fréquentes** — Raccourcir l'ampli en gardant le filtre fixe. Mettre trop de résonance, qui produit un sifflement qui date le son.

**Source** — Sound on Sound *Synthesizing Plucked Strings* pour la physique. Patch chiffré : Attack Magazine, *Pluck Organ with UVI Falcon*.

---

## FICHE 09 — La couche transitoire séparée

**Problème résolu** — Le pluck ou le kick se perd dans un mix dense dès qu'on baisse son fader.

**Explication** — Un son dont l'attaque et le corps sortent du même générateur voit les deux baisser ensemble. En faisant de l'attaque un **son séparé**, on peut doser l'un sans l'autre, et l'attaque reste lisible même quand le corps est en retrait.

**Serum 2** — Oscillateur B dédié à la transitoire : decay **25 à 30 ms**, sustain 0, niveau environ **6 dB sous** l'oscillateur principal. Bruit en one-shot fonctionne aussi.

**Ableton Live 12** — Passe-haut vers **140 Hz** sur la couche transitoire, pour qu'elle ne mange pas le kick. Si les deux couches sont sur des pistes séparées, vérifier leur **alignement à l'échantillon près** et leur polarité.

**Par genre** `[I]` — **Bass house et future house** : indispensable, c'est ce qui fait qu'un pluck traverse. **DnB** : la couche transitoire porte une part du groove, la décaler de 5 à 15 ms crée un effet de flam.

**Erreurs fréquentes** — Ajouter la transitoire sans la filtrer, ce qui encombre le grave. Oublier de vérifier la phase entre les deux couches.

**Source** — Attack Magazine, patch *Pluck Organ* : couche 2 à decay 26,9 ms, gain −5,90 dB, passe-haut 139 Hz.

---

## FICHE 10 — La courbe de détune d'un supersaw n'est pas linéaire

**Problème résolu** — Le bouton de détune ne fait presque rien pendant la moitié de sa course puis devient inutilisable.

**Explication** — Sur le JP-8000, mesuré à la FFT : sept scies, une centrale que le détune ne touche jamais. **À mi-course du bouton, on n'obtient que 10 % de l'écart maximal**, soit environ ±18 cents. La courbe ne monte franchement qu'après la moitié et explose après 90 %. L'écart maximal atteint **deux demi-tons**, et il est asymétrique : −202 cents en bas, +177 en haut.

**Serum 2** — Unison **7 voix** (le nombre magique documenté par Xfer), MODE Linear. Pour une nappe douce : détune correspondant à ±18 cents. Pour un lead plein : ±2 demi-tons. **BLEND** laissant la voix centrale environ **2,5 dB sous** les latérales reproduit le comportement Roland au maximum.

**Ableton Live 12** — Dans Wavetable, mode d'unison **Classic**. Le paramètre `Range` de Serum fixe l'étendue en demi-tons couverte par le bouton Detune : le régler à 5–7 demi-tons génère un accord directement dans l'oscillateur.

**Par genre** `[I]` — **Future house** : lead supersaw plein, ±2 demi-tons. **Bass house** : plus étroit, le lead doit laisser la place à la basse. **DnB** : les nappes en ±18 cents, les leads rarement en supersaw.

**Erreurs fréquentes** — Régler le détune « au milieu » en croyant obtenir un effet moyen. Croire que plus de voix donne plus de largeur : c'est le nombre de voix **et leur phase** qui comptent, pas le détune.

**Source** — Adam Szabo, *How to Emulate the Super Saw*, KTH Stockholm 2010, mesures FFT sur JP-8000 et JP-8080.

---

## FICHE 11 — La phase aléatoire par note

**Problème résolu** — Le supersaw sonne « statique », chaque note attaque exactement pareil, le son est identifiable comme numérique.

**Explication** — Sur un JP-8000, les sept oscillateurs sont **libres, avec une phase aléatoire à chaque déclenchement**. Chaque note a donc une forme d'onde légèrement différente et un transitoire d'attaque unique. Un supersaw en phase fixe ne sonnera jamais comme l'original.

**Serum 2** — Mettre **`RAND`** sur la phase d'oscillateur. Contrepartie documentée : la phase fixe sur un passage par zéro évite un clic sur les attaques très rapides. Il y a donc un arbitrage entre clic et vie.

**Ableton Live 12** — Dans Wavetable, utiliser le mode d'unison **Classic** ou **Random note**. **Surtout pas Phase Sync**, qui fige précisément la phase à chaque note.

**Par genre** `[I]` — **Future house et bass house** : phase aléatoire sur les leads et nappes, phase fixe sur les basses où le clic d'attaque fait partie du punch. **DnB** : phase fixe sur le sub, obligatoire pour la cohérence du grave.

**Erreurs fréquentes** — Utiliser Phase Sync en croyant que « synchronisé » vaut mieux. Mettre la phase aléatoire sur un sub, ce qui rend son attaque imprévisible.

**Source** — Szabo (phase libre mesurée), manuel Serum 2 (paramètre `RAND` et piège du clic), manuel Ableton (les six modes d'unison).

---

## FICHE 12 — Les trois échelles de temps d'une nappe

**Problème résolu** — La nappe est belle pendant deux mesures puis devient un fond dont on n'entend plus rien.

**Explication** — Le système auditif normalise tout stimulus invariant. Trois patchs professionnels relevés utilisent la même architecture : un mouvement de **grain** vers 13 Hz, une **respiration** vers 0,5 Hz, et une **enveloppe d'arrangement de 12 à 15 secondes** qui fait entrer une couche entière. À 120 BPM, 15 secondes valent très exactement **8 mesures**.

**Serum 2** — LFO 1 rapide (5–20 Hz) vers un sync d'oscillateur ou un pan. LFO 2 lent (0,1–1 Hz) vers le cutoff. Une enveloppe à attaque très longue vers le **niveau d'un oscillateur entier**, qui n'apparaît qu'après plusieurs mesures.

**Ableton Live 12** — Les LFO de Wavetable ont un fade-in et des modes de boucle None / Trigger / Loop. Pour l'échelle d'arrangement, préférer une **automation de piste** dessinée sur 8 ou 16 mesures, plus lisible et relisible que l'enveloppe interne.

**Par genre** `[I]` — **Future house et bass house** : l'échelle d'arrangement suffit, les nappes y sont secondaires. **DnB et melodic techno** : les trois échelles, la nappe porte l'évolution.

**Erreurs fréquentes** — Mettre le LFO lent sur une période rationnelle simple, par exemple 1/8 de mesure : il devient un motif rythmique reconnaissable. Animer deux éléments à la même vitesse dans la même bande, ce qui produit un brouillard mouvant.

**Source** — Trois patchs Attack Magazine relevés (FabFilter Twin 3, u-he Hive 2, Sylenth1). `[I]` La correspondance 15 s = 8 mesures est mon calcul.

---

## FICHE 13 — Reverb en insert ou en départ : deux fonctions

**Problème résolu** — On ne sait pas s'il faut mettre la réverb dans le patch ou en send, et le son change quand on resample.

**Explication** — Une réverb en **insert à mix élevé, 60 à 100 %**, appartient au patch : elle sera resamplée avec, automatisée avec, et elle définit le timbre. Un des patchs relevés est à **mix 100 %**, il n'y a plus de signal sec du tout. Une réverb en **départ à mix faible, 10 à 30 %**, appartient au mix : elle est partagée, dosable, et place le son dans un espace commun.

**Serum 2** — Réverb interne en insert pour la réverb-matière. Attention : elle sera figée si on resample vers un oscillateur.

**Ableton Live 12** — Filtrer le bas sur le départ de réverb pour éviter que les basses fréquences encombrent le grave. Un pad de melodic techno a normalement **les deux** : une réverb interne qui fait son timbre, et un envoi vers le retour commun.

**Par genre** `[I]` — **Future house** : réverb courte en send sur les plucks, rien en insert. **DnB** : réverb longue en insert sur les nappes, très filtrée. **Bass house** : peu de réverb, le genre est sec.

**Erreurs fréquentes** — Tout mettre en send, ce qui interdit les textures. Tout mettre en insert, ce qui empêche de doser au mix et fait exploser le CPU.

**Source** — Attack Magazine, patch ambient techno (Pro-R 2 à mix 100 %) et *How To Use Reverb In A Mix*.

---

## FICHE 14 — Un seul élément large à la fois

**Problème résolu** — Le mix est large mais flou, on ne distingue plus les éléments, et il s'effondre en mono.

**Explication** — La largeur perçue est relative. Si tout est large, plus rien ne l'est, et les corrélations de phase se dégradent. `[I]` Règle : si le pad est en unison 8 voix width 100 %, le lead doit être étroit, ou l'inverse.

**Serum 2** — Réduire `WIDTH` plutôt que de réduire l'unison : on garde la densité et on perd l'étalement. CFA-Sound recommande explicitement de réduire Width pour garder le focus stéréo.

**Ableton Live 12** — Utility en fin de chaîne pour mesurer et contraindre. Vérifier avec un corrélamètre. Le conflit voix contre synthé se situe en **1 à 4 kHz** ; le remède documenté est un EQ dynamique déclenché par la voix, plutôt qu'un creux statique qui reste quand la voix est absente.

**Par genre** `[I]` — **Future house** : le lead est large, la basse et les plucks sont étroits. **Bass house** : la basse domine, tout le reste s'efface pendant le drop. **DnB** : le Reese occupe les médiums, les nappes restent en arrière.

**Erreurs fréquentes** — Élargir chaque élément individuellement en solo. Utiliser un élargisseur stéréo sur le bus master pour rattraper.

**Source** — Splice sur les leads, CFA-Sound sur Serum. `[I]` La règle du seul élément large est une synthèse.

---

## FICHE 15 — La queue d'un clap n'est pas une réverb

**Problème résolu** — Le clap sonne faux quand on lui ajoute une réverb, ou reste sec et plat sans elle.

**Explication** — Dans le circuit de la TR-808, le clap est fait de **trois impulsions de 10 ms suivies d'une décharge de 20 ms**, et **en parallèle** un second chemin porte une enveloppe de 100 ms qui produit la queue. Cette queue est câblée dans le circuit : elle fait partie du son, elle n'est pas un espace.

**Serum 2** — Bruit blanc, passe-bande centré ~1 kHz. Reproduire les impulsions avec un LFO en mode Env ou par un delay très court. Enveloppe de queue séparée à 100 ms.

**Ableton Live 12** — Si le sampler ne fait pas les impulsions : **delay 1/64 ou 1/32 avec trois répétitions à feedback court**, placé **en série avant** l'enveloppe de queue. Puis réverb très courte, decay 150 à 300 ms, pre-delay 0, **imprimée** sur le sample et re-shapée à l'enveloppe.

**Par genre** `[I]` — **Bass house et future house** : clap serré, queue courte. **DnB** : la caisse claire prend le rôle, la queue est plus longue et plus bruitée.

**Erreurs fréquentes** — Poser une réverb de pièce sur un clap et s'étonner qu'il sonne lointain. Confondre la queue du clap et l'espace du morceau.

**Source** — Analyse du circuit 808 (Baratatronix). Valeurs confirmées par une implémentation logicielle : attaques à 0, 7,6, 15,5 et 23,0 ms.

---

## FICHE 16 — Le facteur de crête, métrique du punch

**Problème résolu** — On ne sait pas si un traitement a ajouté du punch ou seulement du volume.

**Explication** — Le facteur de crête est la différence en dB entre la crête et le niveau moyen. C'est mesurable, donc vérifiable sans oreilles.

| Signal | Facteur de crête |
|---|---|
| Batterie non traitée | 16 à 18 dB |
| Master bien équilibré | 8 à 12 dB |
| Pop et EDM contemporaines | parfois 3 à 5 dB |

Sous 9 ou 10 dB sur un master, on est en surcompression.

**Serum 2** — Sans objet, c'est une mesure de mix.

**Ableton Live 12** — Mesurer avec Insight 2 ou SPAN sur le bus batterie **avant et après** chaque traitement. Cible **12 à 16 dB avant le master**. En compression parallèle, remonter la chaîne compressée jusqu'à ce que le facteur de crête baisse de **2 dB maximum**.

**Par genre** `[I]` — **DnB** : facteur de crête bas assumé, le genre est très compressé. **Deep et minimal house** : garder haut, le punch vient de la dynamique. **Bass house** : intermédiaire.

**Erreurs fréquentes** — Juger le punch au volume perçu. Empiler les traitements sans mesurer. Gagner 3 dB de sonie en perdant 4 dB de crête et croire qu'on a amélioré.

**Source** — iZotope, *What Is Crest Factor*.

---

## FICHE 17 — Cinq millisecondes suffisent à annuler un kick

**Problème résolu** — Deux couches de kick superposées sonnent plus faibles que chacune séparément.

**Explication** — **À 100 Hz, 5 ms représentent une demi-longueur d'onde, donc une annulation complète.** Un décalage de quelques millisecondes entre deux couches suffit à effacer le grave. Les problèmes de phase sont les pires sous 200 Hz et s'entendent surtout en mono.

**Serum 2** — Sans objet.

**Ableton Live 12** — Procédure : superposer les formes d'onde, tester l'inversion de polarité avec Utility, garder la version qui a le plus de grave, puis **déplacer une couche par pas de 0,1 à 1 ms** jusqu'à maximiser le grave. Viser une **corrélation proche de +1 dans la bande 30 à 80 Hz**.

**Test de diagnostic** — Écouter en mono et couper chaque couche tour à tour. **Si le kick devient plus fort quand on enlève une couche, cette couche annule de l'énergie utile.**

**Par genre** `[I]` — **Bass house** : deux couches maximum, attaque passe-haut 150 Hz et corps passe-bas 150 Hz. **DnB** : plus de couches, donc contrôle de phase impératif.

**Erreurs fréquentes** — Empiler trois ou quatre couches sans vérifier. Régler l'alignement à l'œil sur la forme d'onde sans mesurer.

**Source** — Hardwave Studios sur la phase des kicks layés, Attack Magazine sur le layering.

---

## FICHE 18 — Un transient shaper n'est pas un compresseur

**Problème résolu** — On essaie de rattraper une attaque molle au compresseur et on écrase le son.

**Explication** — Un compresseur réagit à un **seuil**, donc il traite différemment un coup fort et un coup faible. Un transient shaper fonctionne par **suiveurs d'enveloppe détectant la vitesse de variation du niveau** : comme cette vitesse est indépendante du niveau absolu, **les transitoires sont traités de la même façon qu'ils soient forts ou faibles**. C'est la différence de fond.

**Serum 2** — Sans objet.

**Ableton Live 12** — Utiliser le paramètre *Attack* seul, +2 à +4 dB. Enveloppe **lente sur le kick** pour le poids, **rapide sur le clap** pour le claquement. Avertissement documenté : remonter l'attaque **augmente les crêtes** et peut faire écrêter en aval. Et les transient shapers standards **ne savent pas accentuer sélectivement les transitoires graves** : pour un kick maigre, il faut du parallèle avec EQ ou du multibande.

**Par genre** `[I]` — Tous genres. En DnB, le transient shaper sur la caisse claire remplace souvent une compression qui tuerait le groove.

**Erreurs fréquentes** — Utiliser le transient shaper pour renforcer le sustain : Sound on Sound préfère explicitement la **compression parallèle** pour ça, « musicalement plus appropriée ».

**Source** — Sound on Sound, *Using Transient Processors*.

---

## FICHE 19 — Bipolaire ou unipolaire, le piège du cutoff

**Problème résolu** — La basse disparaît un temps sur deux quand on module son filtre.

**Explication** — C'est un réglage de la **matrice**, pas du LFO. En bipolaire, la modulation oscille **autour** du point de repos : **la moitié basse du cycle ferme le filtre sous sa valeur de repos et mange le corps du son à chaque tour**. En unipolaire, elle part de la valeur posée et ne va que dans un sens.

**Serum 2** — Flèche de direction dans la ligne de matrice. **Bipolaire** pour ce qui doit osciller autour d'un repos réglé à l'oreille : pitch, pan, position de wavetable, cutoff d'un pad. **Unipolaire** pour ce qui part d'une valeur et monte : send de réverb, drive, ouverture d'un filtre en build.

**Ableton Live 12** — Même logique dans la matrice de Wavetable. Les sources MIDI disponibles y sont Velocity, Note pitch, Pitch Bend, Aftertouch et Modwheel. Astuce : si une destination n'apparaît pas, **cliquer le paramètre sur l'écran principal le fait apparaître**.

**Par genre** `[I]` — **Bass house** : unipolaire sur le cutoff de la basse, sinon elle clignote. **Future house** : bipolaire sur la position de wavetable du lead. **DnB** : bipolaire sur le filtre du Reese, c'est le mouvement recherché.

**Erreurs fréquentes** — Laisser le réglage par défaut sans le regarder. Compenser en remontant le cutoff de repos, ce qui rend le son trop ouvert la moitié du temps.

**Source** — Manuel Serum 2 et guides de sa matrice.

---

## FICHE 20 — L'ADSR ne peut pas tout faire, et le mode Env du LFO est la parade

**Problème résolu** — On veut un son qui gonfle **après** son attaque, et c'est impossible à obtenir.

**Explication** — Gordon Reid démontre neuf contraintes de l'ADSR, dont celle-ci : **le niveau maximal survient forcément à la fin de l'attaque**. Un cuivre réaliste, qui a un bruit d'attaque puis un gonflement progressif, est donc hors de portée d'un ADSR. Reid écrit : « il existe de nombreux sons très courants que les synthétiseurs ne peuvent pas synthétiser ».

**Serum 2** — Mettre le LFO en **mode Env** : il parcourt sa forme **une seule fois**, et devient une enveloppe multi-segments dessinée à la main. Le paramètre `Rise` lui donne un fondu d'entrée. Serum 2 ajoute aussi DELAY et HOLD à l'enveloppe classique, donc un DAHDSR.

**Ableton Live 12** — Wavetable offre trois enveloppes et des LFO avec loop modes None / Trigger / Loop et fade-in. Pour un contour vraiment libre, passer par une **automation de clip** sur un macro.

**Par genre** `[I]` — **Future house** : le lead qui gonfle après l'attaque est une signature. **DnB** : utile sur les nappes de fond. **Bass house** : moins, le genre veut des attaques franches.

**Erreurs fréquentes** — Empiler deux enveloppes en croyant contourner la limite : elles restent toutes deux contraintes. Confondre mode Env (une passe) et mode Trig (redémarre et boucle).

**Source** — Sound on Sound, *More About Envelopes* et *Envelopes, Gates & Triggers*. Manuel Serum 2 pour les modes de LFO.

---

## FICHE 21 — Saturation avant ou après le filtre : même drive, deux sons

**Problème résolu** — Le son est trop brillant ou trop terne et on ne sait pas quel réglage corriger.

**Explication** — **Saturation après le filtre** : les harmoniques générées ne sont plus filtrées, le son reste brillant même cutoff baissé. **Saturation avant le filtre** : le filtre nettoie la distorsion, le résultat est rond. C'est le même réglage de drive et deux sons différents. `[I]` C'est le levier le plus sous-estimé du sound design.

**Serum 2** — Un warp de distorsion sur l'oscillateur agit **avant** le filtre. Un effet de distorsion dans la page FX agit **après**. Les deux existent, choisir sciemment.

**Ableton Live 12** — Réordonner Saturator et Auto Filter dans la chaîne. Et **comparer à niveau égalisé**, sinon on choisit toujours la version la plus forte.

**Par genre** `[I]` — **Bass house** : saturation après le filtre, on veut que la basse reste mordante même filtrée. **Deep house** : saturation avant, on veut l'arrondi. **DnB** : les deux, sur des couches différentes.

**Erreurs fréquentes** — Juger sans compenser le gain. Ajouter de l'EQ pour corriger un problème qui est un problème d'ordre.

**Source** — Chaînes de référence documentées (Strymon, Reverb), qui disent explicitement que l'ordre standard est un point de départ, pas une loi.

---

## FICHE 22 — Flanger, phaser, chorus : trois mécanismes, pas trois réglages

**Problème résolu** — On choisit au hasard entre les trois et l'effet devient une signature envahissante.

**Explication** — Le **flanger** applique un délai court à tout le signal, ce qui crée un filtre en peigne aux dents **nombreuses et régulièrement espacées**, donc harmoniques. Le **phaser** n'utilise aucun délai : des filtres all-pass déphasent et produisent **peu d'encoches, inégalement espacées, donc non harmoniques**. Quatre étages donnent deux encoches, dix étages en donnent cinq. Le **chorus** utilise un délai plus long avec variation de hauteur, imitant plusieurs instrumentistes.

**Serum 2** — Les trois existent dans la page FX. Le feedback change la forme des encoches sur un phaser.

**Ableton Live 12** — Ordre d'utilité `[I]` : **phaser** sur un pad ou un rhodes, il ne trahit pas la source et ne détruit pas la mono. **Chorus** sur nappes et stabs, avec la réserve que c'est **le plus destructeur pour la compatibilité mono**. **Flanger** comme événement d'arrangement, une transition ou un fill, rarement comme couleur permanente.

**Par genre** `[I]` — **Future house** : chorus sur les leads. **DnB** : phaser sur les nappes, flanger sur les transitions. **Bass house** : phaser sur la basse pour du mouvement sans perdre la mono.

**Erreurs fréquentes** — Laisser un flanger en permanence : ses dents harmoniques régulières deviennent la signature du morceau. Utiliser un chorus sur quoi que ce soit sous 150 Hz.

**Source** — Sound on Sound, *How Phasers Work* et *Q. What's the difference between phasing and flanging?*

---

## FICHE 23 — Resampler ferme une décision

**Problème résolu** — On règle un patch indéfiniment sans jamais avancer, et certains gestes sont impossibles.

**Explication** — `[I]` Le vrai intérêt du resampling n'est pas le CPU, c'est de transformer un processus en objet. Tant que la chaîne est vivante, on continue de la régler. Une fois figée, on peut faire des choses impossibles en amont : reverse, warp extrême, découpage au transitoire, réinjection avec une nouvelle enveloppe.

**Serum 2** — **« Resample to Oscillator »** transforme le son traité en wavetable sans quitter le plug-in. Deux à trois passes successives, avec un rythme de modulation différent à chaque cycle, donnent une densité qu'aucune passe unique n'atteint.

**Ableton Live 12** — Piste audio avec l'entrée **« Resampling »**. Distinction importante et documentée : **une piste gelée ne peut pas être automatisée, une piste resamplée si**. Pour exclure réverb et delay d'une capture, **désactiver ces devices manuellement** avant d'enregistrer.

**Par genre** `[I]` — **Bass house et DnB** : le resampling est la technique centrale des basses complexes. **Future house** : moins nécessaire, le genre est plus direct.

**Erreurs fréquentes** — Supprimer l'original au lieu de le désactiver. Nommer le bounce « audio 3 » : nommer avec l'étape, par exemple `pad_v2_reverb+bitcrush`, sinon la chaîne n'est plus reconstituable.

**Source** — Manuel Serum 2, documentation Ableton sur Freeze et Flatten, Sonic Bloom.

---

## FICHE 24 — Concevoir une macro qui reste musicale sur toute sa course

**Problème résolu** — La macro ne sert que dans ses vingt derniers pour cent, ou elle casse le mix dès qu'on la bouge.

**Explication** `[I]` — Quatre règles, tirées de la pratique et non d'une source.

1. **Une seule intention par macro**, verbalisable en trois mots : « plus sale », « plus loin », « plus ouvert ». Si on ne peut pas la nommer, c'est un fourre-tout.
2. **Compenser l'énergie.** Un cutoff qui monte doit s'accompagner d'un gain ou d'un drive qui baisse, sinon la macro est aussi un fader de volume déguisé.
3. **Plages asymétriques et décalées.** Étaler les assignations sur des portions différentes de la course, par exemple drive de 0 à 40 % et send de 30 à 100 %.
4. **Tester 0, 50 et 100 % en contexte**, sur la section la plus dense.

**Serum 2** — Quatre macros, chacune agrégeant plusieurs destinations à des profondeurs différentes. Critère de choix documenté : privilégier les paramètres à **grande amplitude sonore**, le dry/wet d'une réverb ou la coupure d'un passe-bas.

**Ableton Live 12** — Les **Macro Variations** de Live 11+ mémorisent des états complets : la macro devient un sélecteur de versions. Et une macro est **automatisable et relisible** par le pont, contrairement à la plupart des paramètres internes de Serum.

**Par genre** `[I]` — Tous genres. En bass house, une macro « drop » qui ouvre le filtre, monte le drive et coupe la réverb d'un seul geste.

**Erreurs fréquentes** — Assigner huit paramètres sans plage définie. Automatiser les paramètres internes plutôt que la macro, ce qui rend l'automation illisible.

**Source** — Manuel Serum 2 et MusicRadar pour les macros. Les quatre règles sont `[I]`.

---

## FICHE 25 — Le paramètre FAT pour dompter une résonance

**Problème résolu** — La résonance du filtre siffle dans les 2 à 4 kHz et un EQ qui creuse rend le son terne.

**Explication** — Le paramètre `FAT` de Serum 2 **ajoute de la saturation dans le chemin de la résonance**. Documentation Xfer : effet d'apaisement sur la résonance **et** enrichissement du contenu harmonique. Il dompte donc le sifflement en ajoutant de la matière, là où un EQ en enlève.

**Serum 2** — `FAT` à 20–40 % sur un filtre à résonance élevée. Fonctionne particulièrement avec les filtres de type ladder.

**Ableton Live 12** — Pas d'équivalent exact. Le plus proche est un Saturator après le filtre, mais il sature tout le signal, pas seulement la résonance. Alternative de correction : soothe3, qui traite le sifflement dynamiquement.

**Par genre** `[I]` — **Bass house** : indispensable sur les basses à filtre très résonant. **DnB** : sur le Reese quand la résonance devient agressive. **Future house** : sur les plucks brillants.

**Erreurs fréquentes** — Baisser la résonance pour supprimer le sifflement, ce qui supprime aussi le caractère. Creuser à l'EQ, ce qui rend terne.

**Source** — Manuel officiel Serum 2.

---

## FICHE 26 — Un creux de volume au balayage de WT POS vient de l'interpolation

**Problème résolu** — Quand on balaie la position de wavetable, le volume plonge à certains endroits.

**Explication** — Une wavetable ne contient souvent que quelques frames réelles ; les autres sont **interpolées**, par **crossfading** ou par **morphing spectral**. Un crossfade entre deux formes d'onde produit des **annulations de phase**, donc des creux de niveau. Un morphing spectral reste lisse. Serum embarque le **type** d'interpolation, pas les formes interpolées, et les calcule au chargement.

**Serum 2** — Clic droit sur `WT POS` → **Smooth Interpolation** (écrit « Smooth Interpretation » dans le manuel, coquille probable). Non destructif. Si le creux persiste, changer de table plutôt que de compenser au volume.

**Ableton Live 12** — Wavetable ne documente pas ses méthodes d'interpolation ; tester à l'oreille en balayant lentement la position.

**Par genre** `[I]` — **Future house et bass house** : un creux au milieu du balayage se traduit par un trou audible en plein drop.

**Erreurs fréquentes** — Automatiser le volume pour compenser le creux, ce qui masque le symptôme. Croire que deux tables « identiques » se comportent pareil au balayage.

**Source** — Manuel officiel Serum 2, section sur l'interpolation des frames.

---

## FICHE 27 — Hi-Quality de Wavetable : le piège qui change un preset d'un morceau à l'autre

**Problème résolu** — Le même preset Wavetable sonne différemment dans deux projets.

**Explication** — Le mode **Hi-Quality** de Wavetable est **désactivé par défaut depuis Live 11.1** sur les nouvelles instances et les presets de la Core Library, mais **activé** sur les sets antérieurs. Désactivé, la modulation est calculée **tous les 32 échantillons** et économise jusqu'à 25 % de CPU, au prix de la précision.

Deuxième piège documenté : les oscillateurs de Wavetable sont **sans aliasing à n'importe quelle hauteur — tant qu'aucune modulation n'est appliquée**. La restriction est explicite dans le manuel et omise par la plupart des tutoriels.

**Serum 2** — Sans objet.

**Ableton Live 12** — Vérifier l'état de Hi-Quality avant de comparer deux instances. Sur un son très modulé et aigu, l'activer.

**Par genre** `[I]` — Tous genres, mais surtout audible sur les leads aigus fortement modulés, donc future house et DnB.

**Erreurs fréquentes** — Comparer deux presets sans vérifier ce réglage. Attribuer à la table une différence qui vient du mode de calcul.

**Source** — Manuel Ableton Live 12, référence des instruments.

---

## FICHE 28 — Le riser ne fonctionne pas par sa montée

**Problème résolu** — Le riser monte bien mais le drop ne frappe pas.

**Explication** `[I]` — Ce qui fait l'effet, c'est **la coupure nette au temps 1**, pas la montée. Le drop frappe contre le silence soudain. Deuxième point : riser et downlifter doivent **se croiser** — le downlifter sur la dernière mesure fait descendre l'attention pendant que le riser la monte, ce qui crée l'ambiguïté qui rend le drop lisible.

**Serum 2** — Les formes simples, scie ou carrée, **répondent le mieux à la modulation**. Bruit filtré avec un passe-haut automatisé de 200 Hz à 8 kHz, résonance ~30 %.

**Ableton Live 12** — Riser sur 8 mesures : bruit filtré + couche tonale avec pitch +12 à +24 demi-tons sur les deux dernières mesures + queue de réverb inversée. Downlifter sur 1 mesure : pitch −12 à −24, passe-bas qui se ferme, réverb qui monte en send. **Aligner les points de crête** : maximum à la fin pour un riser, au début pour un impact.

**Par genre** `[I]` — **Bass house et future house** : riser court, 4 mesures, coupure franche. **DnB** : riser plus long, souvent doublé d'un downlifter.

**Erreurs fréquentes** — Laisser la réverb du riser déborder sur la mesure 1 du drop, ce qui noie l'attaque. Monter le volume sans couper.

**Source** — Sound on Sound, *Cubase: Creating Risers & Impacts*. Point Blank pour la coupure au downbeat (page non lue intégralement, erreur 403).

---

## FICHE 29 — Le plancher de bruit doit être hors sidechain

**Problème résolu** — On ajoute un fond de bruit ou de crackle pour coller le morceau, et il se met à pomper.

**Explication** — Un plancher de bruit tient le morceau ensemble parce qu'il est **constant**. Dès qu'il est compressé par le master ou ducké par le sidechain, il devient rythmique, donc audible comme élément, et il perd sa fonction.

**Serum 2** — Oscillateur de bruit interne, ou mieux, une piste audio séparée pour garder le contrôle du routage.

**Ableton Live 12** — Bus dédié, **passe-haut vers 300 Hz** pour ne pas encombrer le grave, niveau « senti plus qu'entendu », `[I]` autour de −45 à −55 dBFS RMS. **Exclure du sidechain et de la compression master.** Sources natives : Vinyl Distortion et son générateur Crackle, Erosion en modes Noise ou Wide Noise, ou un room tone enregistré au téléphone.

**Par genre** `[I]` — **Deep et minimal house** : très efficace, c'est ce qui donne le côté analogique. **DnB** : moins, le mix est déjà dense. **Bass house** : peu utile.

**Erreurs fréquentes** — Router le bruit vers le même bus que le reste. Le monter jusqu'à ce qu'on l'entende : à ce moment-là il est déjà trop fort.

**Source** — Liveschool (centre de formation certifié Ableton) et MusicRadar sur le crackle et le tape hiss.

---

## FICHE 30 — Un rapport FM entier donne un son harmonique, un rapport non entier une cloche

**Problème résolu** — On cherche un son de cloche et on obtient un son de synthé, ou l'inverse.

**Explication** — Les bandes latérales de la FM tombent à ωc ± n·ωm. **Si le rapport est entier, elles retombent sur des harmoniques de la fondamentale** et l'oreille les fusionne en une hauteur unique. Si le rapport n'est pas entier, elles tombent **entre** les harmoniques, la fusion échoue et on entend du métal. C'est la physique des cloches.

Rapports documentés : **1:1** série harmonique complète · **1:2** impaires seulement, sonne comme une carrée filtrée · **1:3** approche une pulse à 33 % · **1:4** approche une carrée.

**Serum 2** — La FM est un warp mode, avec trois variantes : **Linear** (garde la hauteur globale, propre et musical, idéal cloches et pads), **Exp** (plus dur), **Thru-Zero** (la phase s'inverse quand la porteuse passe sous zéro, « lush metallic »).

**Ableton Live 12** — Dans Operator, `Coarse` fixe le rapport en entiers (harmonique), `Fine` en fractions (inharmonique). Le bouton `Q` force la quantification. Dans Wavetable, l'effet FM à **50 % ou −50 % vaut une octave, 100 % deux octaves** ; entre ces valeurs, rapports inharmoniques.

**Par genre** `[I]` — **Future house** : le lead cloche est la signature, rapport non entier type 1:3,5. **Bass house** : rapport 1:1 pour une basse au spectre riche. **DnB** : rapport entier sur la basse, non entier sur les percussions métalliques.

**Erreurs fréquentes** — **Un piège documenté** : un guide publié prescrit pour une cloche un « rapport non entier de 4:1 ou plus ». **4:1 est entier** et donne un spectre harmonique. Pour une cloche il faut 1:1,41 ou 1:3,14. Suivre Sound on Sound, pas ce guide.

**Source** — Sound on Sound, *An Introduction To Frequency Modulation* et *More On Frequency Modulation*. Manuel Serum 2 pour les variantes de warp FM.

---

## FICHE 31 — Débloquer l'automation de Serum depuis Live

**Problème résolu** — Serum n'expose qu'un seul paramètre à l'API de Live, « Device On », ce qui interdit tout pilotage par script.

**Explication** — **Ce n'est pas Serum, c'est Live.** Le manuel d'Ableton dit que Live crée un panneau automatiquement **pour les plug-ins ayant jusqu'à 64 paramètres**. Au-delà, le device « s'ouvre avec un panneau vide ». Et l'API ne voit que le panneau. Serum ayant beaucoup plus de 64 paramètres, le panneau est vide, donc `parameters` = `[Device On]`. C'est mécanique.

**Serum 2** — Il y a une seconde couche, propre à Serum 2 et confirmée par le staff Xfer : **les paramètres d'effets ne sont pas exposés statiquement**. Il faut faire **clic droit → Automate** sur chaque contrôle FX. C'est un choix de conception, pour éviter un menu que les DAW auraient replié. Les pages OSC, filtres, mixer, LFO, enveloppes et matrice sont exposées normalement.

**Ableton Live 12** — La procédure, dans l'ordre : clic droit → Automate dans Serum · **bypass puis unbypass du device** si le paramètre n'apparaît pas · seulement ensuite **Configure** dans Live. Note documentée : « pour certains plug-ins, il peut être nécessaire de **réellement changer la valeur** » — un simple clic ne suffit pas toujours.

**Par genre** — Sans objet, c'est technique.

**Erreurs fréquentes** — Chercher la cause du côté de Serum. Passer par Configure avant d'avoir fait le clic droit Automate sur les paramètres FX.

**Source** — Manuel Live 12, section instruments et effets. Forum officiel Xfer, réponse de steve_xfer, avril 2025.

---

## FICHE 32 — Stabiliser l'index des paramètres

**Problème résolu** — Un script écrit sur le bon index, et après rechargement du Set il pilote le mauvais paramètre.

**Explication** — Dans le panneau Configure, **l'ordre est celui que vous fixez**, pas celui de Serum, et c'est lui qui détermine l'index dans `device.parameters`. Cet ordre n'est pas garanti stable : le changelog de Serum documente un bug réel où « le rappel d'automation des paramètres d'effets était **décalé d'un index après rechargement du projet** ».

**Serum 2** — Deux autres pièges du changelog : ajouter un module FX **arrêtait l'automation en cours**, et Live pouvait **afficher de mauvais noms de macros après chargement d'un set**. Donc identifier un paramètre par son nom n'est pas fiable non plus.

**Ableton Live 12** — **Le levier : construire une fois une configuration de référence dans l'ordre voulu, puis clic droit sur la barre de titre du device → « Save as Default Configuration ».** Toutes les futures instances exposeront alors les mêmes paramètres aux mêmes index. La limite devient fixe et connue au lieu d'être vide.

**Par genre** — Sans objet.

**Erreurs fréquentes** — Configurer les paramètres au fil de l'eau, ce qui produit un ordre différent par instance. Se fier au nom plutôt qu'à l'index, ou l'inverse, sans vérifier les deux.

**Source** — Documentation Ableton sur la sauvegarde des configurations de plug-in. Changelog officiel Serum, versions 2.0.17, 2.0.18 et 2.0.21.

---

## FICHE 33 — Trois choses qui cassent la reproductibilité d'un preset Serum 2

**Problème résolu** — Le même preset ne sonne pas pareil d'une ouverture à l'autre, ou revient en Init.

**Explication** — Trois causes documentées.

**Serum 2** —
1. **Serum 2 n'est pas forward compatible.** Une session sauvée avec une version plus récente se recharge avec **le bon nom de preset mais le son Init**. Silencieusement avant la 2.0.19. **Noter la version exacte dans la mémoire de projet.**
2. **Le mode S1 Compatibility** s'active automatiquement sur un preset Serum 1. La formulation officielle est « similarité **maximale** », pas identité. Le même fichier sonne différemment selon l'état du réglage.
3. **Le réglage Quality** (Draft 1×, High 2×, Ultra 4×) **est stocké dans le preset sauf si on le verrouille**. Ce n'est pas qu'une affaire de CPU : des correctifs montrent que **le son des warps FM, AM, PD et RM différait selon le Quality**.

**Ableton Live 12** — Pour une automation rythmique rapide, activer **Disable Smoothing** : le lissage s'applique aussi aux changements par la souris, et sans lui on n'obtient pas la valeur exacte à l'échantillon près.

**Par genre** — Sans objet.

**Erreurs fréquentes** — Croire qu'un preset est un contrat. Ne pas embarquer les samples, wavetables et réponses impulsionnelles externes, ce qui rend le preset non portable.

**Source** — Manuel Serum 2 page 319 pour le mode S1, changelog officiel, forum Xfer pour la non-forward-compatibilité.

---

## FICHE 34 — Ne pas transposer une recette Serum 1 telle quelle

**Problème résolu** — On rejoue un patch Serum 1 dans Serum 2 et le résultat diffère sans qu'on comprenne pourquoi.

**Explication** — **Le moteur DSP est entièrement reconstruit.** Et une recette rejouée à la main, sans le mode S1, ne donnera pas le même résultat qu'un preset Serum 1 importé, qui lui active ce mode automatiquement.

**Serum 2** — Quatre changements qui piègent :
- **Le switch HOST des LFO a changé de sémantique** : « contrairement à Serum 1, HOST a maintenant un effet **quand BPM est désactivé** ». Un LFO vraiment libre exige HOST désactivé. Mêmes réglages visuels, comportement différent.
- **Un warp spectral a été renommé** en 2.0.19 : « Pitch Shift » est devenu « Pitch Blend », et un nouveau « Pitch Shift » a pris le nom. **Un patch qui dit « Pitch Shift » ne désigne pas la même chose avant et après.**
- **Un boost de 1,37 dB a été retiré** du volume master des FX en 2.0.23. Le même patch ne sort pas au même niveau.
- **Le verrouillage par paramètre a été supprimé**, remplacé par un verrouillage groupé.

**Ableton Live 12** — **Serum 2 n'existe pas en VST2**, seulement VST3, Audio Unit et AAX. Les deux versions s'installent côte à côte et sont **deux plug-ins distincts** : les anciens projets ne sont pas convertis, volontairement.

**Par genre** — Sans objet.

**Erreurs fréquentes** — Chercher les LFO 7 à 10 sans les trouver : **ils sont invisibles tant que le LFO 6 n'est pas assigné**. C'est probablement ce qui fait qu'un test de presse annonce six LFO alors que la documentation en annonce dix.

**Source** — Manuel Serum 2, changelog officiel, FAQ de migration Xfer.

---

## FICHE 35 — Les effets de Serum ne sont pas par voix

**Problème résolu** — Une enveloppe sur un paramètre d'effet produit un résultat erratique sur des accords.

**Explication** — Le manuel est explicite : le rack FX est un process DSP **qui opère sur la somme de la sortie du moteur, pas par voix**. Trois formulations officielles : « les effets sont monophoniques », « les effets sont comme des inserts après Serum », comportement dit **paraphonique**, particulièrement avec l'effet Filter.

**Conséquence signalée dans le manuel** : sur une partie polyphonique, moduler un contrôle d'effet avec une source par voix, donc une enveloppe, fait **re-déclencher la modulation à chaque nouvelle note**. Sur un accord arpégé, l'effet repart à chaque note.

**Serum 2** — Pour du mouvement par voix, moduler **dans la section de synthèse**, pas dans les FX. Exception documentée : les bandes du Compressor en mode Multiband acceptent des assignations de matrice, et le manuel cite l'usage sidechain du bas du spectre.

**Ableton Live 12** — Même logique : un effet en insert sur la piste est forcément paraphonique.

**Par genre** `[I]` — **Bass house** : sans conséquence, la basse est mono. **Future house** : piège réel sur les stabs d'accords. **DnB** : idem sur les nappes.

**Erreurs fréquentes** — Mettre une enveloppe sur le mix d'une réverb dans un patch polyphonique.

**Source** — Manuel officiel Serum 2, page 159.

---

## FICHE 36 — Le lead future house vient de la basse creuse UK garage

**Problème résolu** — Obtenir le lead métallique et élastique du genre, alors qu'aucun tutoriel chiffré n'existe.

**Explication** — La filiation est documentée : la basse future et deep house moderne est « une version moderne d'un son de l'UK garage appelé **hollow bass**, créé à l'origine avec **deux sinus et de la FM** ». Et ce son ancêtre est, lui, entièrement chiffré.

Le patch d'origine : porteuse à **−24**, modulateur à **−12**, donc un **ratio 2:1 harmonique** qui donne le creux façon orgue. **Le métallique vient de la variante à −12,30** : trente centièmes de demi-ton de désaccord rendent le spectre légèrement inharmonique et battant. **Ce sont les deux seuls chiffres publiés qui expliquent le son du genre.**

**Serum 2** — Warp **FM** sur OSC A avec OSC B comme modulateur, une octave au-dessus. Filtre à **25 % de cutoff, résonance 0**, piloté **à fond** par une enveloppe à **sustain 0**. Mono, glide 10 à 15 %. Puis une saturation type lampe légère et un élargisseur discret. Pour le lead, **monter le patch d'une ou deux octaves**.

**Ableton Live 12** — Tempo 126 BPM. Le genre monte à 128, plage 120 à 130.

**Par genre** — **Future house** : c'est la recette. **Bass house** : même base, plus de saturation et un LFO sur le cutoff. **DnB** : sans objet, le genre a son propre vocabulaire.

**Erreurs fréquentes** — Chercher un rapport non entier en croyant faire une cloche : ici le rapport est **entier**, c'est le **désaccord** qui fait le métal. Pour une vraie cloche, il faut un rapport non entier d'au moins 4 ou 5 avec une enveloppe rapide **sur le modulateur seul**.

**Source** — Attack Magazine, *Synth Secrets: Garage Bass*. Filiation documentée par ADSR et par la fiche Wikipédia du genre.

---

## FICHE 37 — Ce qui sépare une basse bass house d'une basse dubstep

**Problème résolu** — On applique une recette de growl dubstep en bass house et le grave devient illisible.

**Explication** — **La différence est rythmique et spectrale, pas timbrale.** En dubstep, la batterie est en demi-temps et clairsemée, la basse a tout l'espace. **En bass house, la basse doit cohabiter avec un kick sur les quatre temps.**

**Serum 2** — Le growl bass house est un **mid-bass**, pas un son pleine bande : **coupe-bas vers 100 Hz** sur le growl, et un **sub sinus mono séparé** en dessous, en mono sous 120 Hz. C'est là que les recettes dubstep induisent en erreur, puisque leur growl descend jusqu'au sub.

**Ableton Live 12** — Répartition chiffrée : kick concentré **50 à 80 Hz** plutôt que sous 40 Hz, clic de présence 3 à 5 kHz. Basse coupe-bas 30 à 40 Hz, nettoyage de boue 200 à 300 Hz.

**Par genre** — **Bass house 126 BPM**, structure par blocs de 8 mesures, swing 55 à 65 %. **Future house** : même logique, basse plus propre. **DnB** : le sub tient tout, le Reese vit au-dessus.

**Erreurs fréquentes** — Garder un growl pleine bande. Et un piège documenté côté kick : il doit être « punchy, **mais moins qu'un kick tech house** », et « **pouvoir s'écarter du chemin de la basse, donc pas trop de grave** ».

**⚠ Contradiction non résolue** — Une source place le poids du kick à 50–80 Hz et laisse le sub à la basse ; une autre dit de faire un kick pauvre en grave. Les deux ne se concilient qu'en décidant explicitement qui tient le fondamental.

**Source** — EDMProd et Preset Drive pour les chiffres, Icon Collective pour le masquage.

---

## FICHE 38 — Traiter le sub seul dans Wavetable

**Problème résolu** — On veut filtrer ou saturer uniquement le sub d'un patch Wavetable, sans toucher aux oscillateurs.

**Explication** — Le mode de routage **Split** envoie Osc 1 vers le filtre 1 et Osc 2 vers le filtre 2, et **coupe le sub en deux** pour l'envoyer aux deux. Le manuel donne alors une astuce peu connue : « **si les deux oscillateurs principaux sont désactivés et les deux filtres actifs, Split permet un traitement supplémentaire du seul Sub** ».

Autre particularité de Split : **si l'un des filtres est éteint, le signal de l'oscillateur correspondant reste audible**.

**Serum 2** — Équivalent par le mixer : router un oscillateur en **Direct**, ce qui **contourne le filtre et la section d'effets**.

**Ableton Live 12** — Le sub de Wavetable a un paramètre **Tone** : à 0 % c'est un sinus pur, au-delà le contenu harmonique augmente. Commutateurs −1 et −2 octaves.

**Par genre** `[I]` — **Deep house** : traiter le sub seul permet de lui donner du grain sans élargir. **Bass house** : utile pour saturer le sub indépendamment du growl.

**Erreurs fréquentes** — Utiliser Serial en croyant isoler quelque chose : Serial envoie **tous** les oscillateurs au filtre 1 puis au filtre 2.

**Source** — Manuel Ableton Live 12, section 30.13.4.

---

## FICHE 39 — Deux vérités d'Operator qui vont à l'encontre de l'intuition

**Problème résolu** — On optimise le CPU au mauvais endroit, et on cherche le growl au mauvais paramètre.

**Explication** — Deux affirmations documentées et contre-intuitives.

**Éteindre les oscillateurs d'Operator ne fait PAS économiser de CPU.** Le manuel le dit en toutes lettres. Seuls comptent le filtre, le LFO, Interpolation, Antialias, Spread et le nombre de voix. Et **Spread est très gourmand**.

**FM Drive est une cible de modulation**, qui « module le volume de **tous les oscillateurs qui en modulent d'autres**, donc le timbre ». `[I]` C'est **la cible la plus musicale pour un growl** : une seule modulation change la brillance FM de toute la structure sans toucher au filtre.

**Serum 2** — Équivalent : moduler le montant du warp FM plutôt que le cutoff.

**Ableton Live 12** — Autres chiffres utiles d'Operator : le LFO monte jusqu'à **12 kHz** en plage Hi, donc il fonctionne comme un cinquième oscillateur. **Rate < Key à 100 % lui fait doubler sa fréquence par octave.** La forme **Noise** est un **bruit filtré passe-bande**, et le manuel la désigne comme « **la clé des bons hi-hats et snares** ».

**Par genre** `[I]` — **Bass house et DnB** : FM Drive modulé par un LFO synchronisé remplace avantageusement un wobble de filtre, parce qu'il **ne fait pas disparaître le fondamental**.

**Erreurs fréquentes** — Désactiver des oscillateurs pour soulager le processeur. Laisser Spread actif à 0 %, ce qui coûte quand même.

**Source** — Manuel Ableton Live 12, sections 30.9.6 à 30.9.10.

---

## FICHE 40 — Série donne un passe-bande, parallèle donne un coupe-bande

**Problème résolu** — On combine deux filtres et on obtient soit du silence, soit rien du tout.

**Explication** — La règle est contre-intuitive et rarement énoncée. **Deux filtres en série produisent un passe-bande**, et seulement si les bandes se recouvrent, donc si la coupure du passe-bas est **au-dessus** de celle du passe-haut. **Les deux mêmes filtres en parallèle produisent un coupe-bande**, et seulement si elles ne se recouvrent pas.

Inverser ces conditions donne soit le silence, soit un signal quasi intact.

**Serum 2** — Le routage série ou parallèle des deux filtres est un choix explicite. Le paramètre **VAR** change de fonction selon le type de filtre, ce qui est un piège pour un script.

**Ableton Live 12** — Dans Wavetable, les trois routages sont Serial, Parallel et Split.

**Par genre** `[I]` — **DnB** : le coupe-bande en parallèle est la base du Reese traité. **Bass house** : le passe-bande en série resserre un growl.

**Erreurs fréquentes** — Attendre d'un passe-bande la même pente qu'un passe-bas. Sur les machines mesurées, un multimode qui donne **12 dB/oct en passe-bas et passe-haut ne donne que 6 dB/oct en passe-bande et en coupe-bande**, parce qu'un passe-bande issu d'un filtre à 4 pôles consomme 2 pôles de chaque côté.

**Source** — Sound on Sound, glossaire et série Synth Secrets. **Réserve honnête** : deux exemples numériques différents circulent attribués à cette source, et n'ont pas pu être vérifiés par lecture directe. **La règle série contre parallèle, elle, est cohérente entre les deux occurrences.**
