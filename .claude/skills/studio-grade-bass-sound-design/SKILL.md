---
name: studio-grade-bass-sound-design
description: Concevoir, traiter et intégrer des basses électroniques pour Minimal House, Tech House, Bass House, Future House et Techno avec Serum 2, Ableton Live 12 et, lorsque pertinent, Waves, FabFilter, iZotope, Native Instruments et Valhalla DSP. Utiliser pour sub sine, rolling bass, offbeat bass, growl/reese, FM/metallic, donk/bounce, techno rumble-bass, acid/resonant et call-response, avec intégration kick/basse et macros contrôlables par bridge.
---

# Studio-Grade Bass Sound Design — v9

Ce skill construit des basses **fonctionnelles dans le morceau**, pas seulement impressionnantes en solo. Il ne revendique aucune affiliation à un studio, label ou artiste.

## Ordre de lecture obligatoire

1. `references/source-authority.md`
2. `references/bass-architecture.md`
3. `references/genre-bass-specifications.md`
4. `references/kick-bass-ownership.md`
5. `references/serum2-bass-design.md` ou `references/ableton-bass-design.md`
6. `references/plugin-role-matrix.md`
7. la recette pertinente dans `recipes/`
8. `references/modulation-movement.md`
9. `references/mono-phase-stereo.md`
10. `references/validation-protocol.md`
11. `references/output-schema.md`

Les fichiers marque ne doivent être ouverts que si le processeur est utile à une fonction identifiée.

## Système de preuve

- **[DOC]** : capacité explicitement documentée par le fabricant.
- **[HEUR]** : pratique, plage de départ ou choix de production à valider à l'écoute.
- **[TEST]** : dépend du projet réel, de la tonalité, du tempo, du kick, du monitoring, de la version installée ou du bridge.

Ne jamais transformer une plage `[HEUR]` en « règle constructeur ».

## Architecture universelle d'une basse

Penser en cinq fonctions indépendantes :

1. **SUB** — fondamentale, poids, stabilité mono.
2. **BODY** — note et masse audibles sur systèmes normaux.
3. **ATTACK** — articulation ou transient du début de note.
4. **MOTION** — filtre, wavetable, FM, amplitude ou rythme qui crée le groove.
5. **AIR/SPACE** — largeur, texture, bruit, reverb/delay ; généralement exclu du vrai sub.

Une seule couche peut remplir plusieurs fonctions, mais chaque couche ajoutée doit justifier son rôle.

## Principe critique : séparer sub et caractère

Par défaut, une basse agressive ou large doit être pensée comme :

`SUB propre et stable + couche BODY/MOTION plus harmonique` [HEUR]

Dans Serum 2, une source sub peut être routée **Direct** pour contourner filtres et effets tandis que la couche de caractère passe dans les filtres/FX [DOC]. Dans Ableton, la séparation peut être faite par Instrument Rack, pistes parallèles ou resampling [DOC/HEUR].

Ne pas stéréoriser le sub par principe. Vérifier la somme mono avant de conserver une largeur importante [TEST].

## Choix du moteur

### Serum 2
Choisir Serum 2 pour : wavetable/morphing, architecture multi-source, granular/spectral, routage indépendant, double filtre, FM/relations de pitch, LFO complexes, huit macros, patches reproductibles et contrôle par bridge. Les OSC A/B/C peuvent utiliser Wavetable, Multisample, Sample, Granular ou Spectral [DOC].

### Ableton Live 12
- **Operator** : basses FM, sine sub, donk, metallic, basses percussives [DOC].
- **Wavetable** : sub intégré + couches wavetable, filtres et modulation [DOC].
- **Meld** : deux moteurs indépendants pour basses hybrides ou évolutives [DOC].
- **Drift/Analog** : basses soustractives/analogiques simples [DOC].
- **Sampler/Simpler** : basses resamplées, one-shots, couches audio [DOC].

## Familles obligatoires couvertes

- clean sine/sub bass ;
- Minimal House rubber bass ;
- Tech House rolling bass ;
- Future House offbeat/bounce bass ;
- Bass House growl/reese ;
- FM/metallic bass ;
- donk/bounce bass ;
- Techno rumble-bass ;
- acid/resonant bass ;
- call-response/multi-bass.

## Ordre de construction

1. Identifier style, BPM, tonalité et pattern.
2. Décider **qui possède le sub** : kick, basse, alternance ou rumble.
3. Construire d'abord SUB + envelope d'amplitude.
4. Ajouter BODY et harmonique utile.
5. Créer MOTION avec une seule idée claire.
6. Vérifier kick+basse avant d'ajouter width/reverb.
7. Ajouter saturation/FX par fonction, pas par habitude.
8. Resampler si la chaîne créative devient instable ou trop complexe.
9. Construire 4 à 8 macros musicales.
10. Valider en solo, avec kick, dans le mix, en mono et à faible niveau.

## Politique des plugins tiers

Chaque plugin doit résoudre un problème ou créer un comportement nommé. Exemple acceptable :

`Serum 2 → Saturn 2 (upper harmonics) → Pro-Q 4 (résonance dynamique) → Pro-C 3 (ducking kick) → Utility (Bass Mono)`

Exemple à éviter : empiler plusieurs saturateurs/compresseurs sans A/B à niveau égal.

### Waves
- **Renaissance Bass / MaxxBass** : générer des harmoniques psychoacoustiques pour rendre le grave perceptible sur petits systèmes ; ne pas les confondre avec des générateurs de sous-harmoniques [DOC].
- **Smack Attack** : modeler attaque et sustain d'une basse pluck/donk/percussive [DOC].
- Les traitements de caractère supplémentaires ne sont utilisés que s'ils sont présents et documentés dans l'installation [TEST].

### FabFilter
- **Pro-Q 4** : EQ corrective, dynamique et spectral dynamics pour résonances variables [DOC].
- **Pro-C 3** : sidechain externe, Host Sync ou MIDI trigger selon le besoin ; idéal pour ducking reproductible [DOC].
- **Saturn 2** : saturation multibande, feedback, dynamics, tone et modulation par bande [DOC]. Le sub peut rester plus propre tandis que le haut de la basse est plus traité [HEUR].

### iZotope
- **Neutron 5 Exciter** : saturation multibande et modes de caractère blendables [DOC].
- **Neutron 5 Transient Shaper** : ajustement de l'attaque et de la tenue, avec traitement multibande [DOC].
- **Neutron 5 Clipper/Density/Phase/Unmask** : outils de contrôle de crête, poids, phase et masquage lorsque le diagnostic le justifie [DOC/HEUR].
- **Trash** : distorsion créative + Convolve ; utiliser surtout sur BODY/MOTION ou en parallèle, et vérifier la version car l'interface diffère selon génération [DOC/TEST].

### Native Instruments
- **Massive X** : moteur alternatif wavetable/phase modulation semi-modulaire ; ses Performers permettent des modulations rythmiques complexes [DOC]. Ne pas le choisir à la place de Serum 2 sans avantage clair.
- **Transient Master** : contrôle attack/sustain indépendant du niveau absolu [DOC].
- **Supercharger GT** : compression à caractère + trois niveaux de saturation, utile pour densité/body [DOC].

### Valhalla DSP
Valhalla est réservé principalement à **AIR/SPACE/MOTION** :
- **ValhallaDelay** : délai modulé, pitch/reverse selon mode, ducking sur certains modes [DOC].
- **Supermassive** : feedback, densité, modulation et longues queues [DOC].
- **Room/VintageVerb** : profondeur sur upper bass, sends et FX [DOC].

Appliquer un low cut au retour spatial lorsque le sub doit rester sec et central [HEUR].

## Intégration kick/basse

Toujours nommer l'un de ces modèles :

- **KICK OWNS SUB** — kick long ; bassline évite/ducke davantage le fondamental.
- **BASS OWNS SUB** — kick court ; la basse porte le sous-grave musical.
- **ALTERNATING OWNERSHIP** — kick et basse se partagent le registre par le rythme/ducking.
- **KICK + RUMBLE** — techno ; le rumble est un élément séparé et contrôlé.

Le ducking n'est pas une valeur fixe. Il doit être ajusté à l'enveloppe réelle du kick et au pattern [TEST].

## Macros minimales recommandées

Pour un patch Serum 2 complexe, préférer des macros musicales :

1. **TONE** — cutoff / harmonic balance.
2. **MOVEMENT** — profondeur LFO/WT/FM.
3. **BITE** — saturation / resonance / upper harmonics.
4. **WEIGHT** — balance sub/body, sans changer brutalement le niveau total.
5. **WIDTH** — uniquement BODY/AIR, pas le vrai sub.
6. **SPACE** — send/reverb/delay upper layer.
7. **ATTACK** — transient/envelope.
8. **VARIATION** — variation contrôlée pour fills/fin de phrase.

Chaque macro destinée au bridge doit avoir plage sûre, valeur par défaut et fonction audible.

## Exigences de sortie

Toute réponse issue de ce skill doit donner :
- style/BPM/tonalité/pattern ;
- modèle de propriété du sub ;
- architecture `SUB/BODY/ATTACK/MOTION/AIR` ;
- choix Serum 2 ou Ableton avec justification ;
- paramètres de départ `[HEUR]` ;
- modulation et macros ;
- chaîne de traitement avec raison pour chaque plugin ;
- stratégie de ducking/phase/mono ;
- au moins 4 tests `[TEST]` ;
- ce qui doit être mesuré ou écouté dans le Set réel.

Ne jamais déclarer une basse « parfaite », « pro » ou « prête au mastering » sans l'entendre avec le kick et le morceau.
