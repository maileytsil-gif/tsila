---
name: bass-house-serum2-sound-design
description: Concevoir et expliquer synthés, nappes, drones, stabs, risers, impacts, plucks, pads, keys, sub, mid-bass et leads Bass House/Electro avec Serum 2 et les instruments/effets natifs d'Ableton Live 12. Utiliser pour choisir le moteur, créer un patch, diagnostiquer un timbre ou le préparer au contrôle via bridge ; ne pas remplacer l'écriture musicale ou le mix complet.
---

# Bass House Sound Design — Serum 2 + Ableton Live 12 — v7 + Producer Intelligence

Concevoir le son à partir de sa **fonction musicale** et non à partir d'un preset. Choisir le moteur le plus simple capable de produire le comportement voulu, puis ajouter uniquement les couches nécessaires.

## Documentation requise

Lire d'abord `references/documentation-map.md`, `references/sound-family-documentation-map.md`, `references/serum2-verified.md` et `references/native-ableton-instruments.md`.

Pour la famille demandée, charger le fichier pertinent dans `references/sound-families/`, puis le fichier de sous-types correspondant dans `references/subtypes/` :
- `synth.md`
- `nappe.md`
- `drone.md`
- `stab.md`
- `riser.md`
- `impact.md`
- `pluck.md`
- `pad.md`
- `keys.md`

Sous-types : `synth-subtypes.md`, `nappe-subtypes.md`, `drone-subtypes.md`, `stab-subtypes.md`, `riser-subtypes.md`, `impact-subtypes.md`, `pluck-subtypes.md`, `pad-subtypes.md`, `keys-subtypes.md`.

Consulter aussi `references/sound-family-index.md`, `references/subtype-selection-matrix.md`, `references/professional-layering.md`, `references/macro-templates-v5.md` et `references/subtype-validation.md` pour choisir le moteur, `references/sound-families/synth-fx-routing.md` pour le routage/FX, et `references/family-validation-protocol.md` avant de déclarer le patch terminé.

Si une référence producteur/morceau intervient, lire `references/producer-intelligence.md` puis le dossier racine `producer-intelligence/`. Convertir la référence en vecteurs (`groove-first`, `rhythmic-sound-design`, etc.) avant de choisir le moteur.

## Système de preuve

- **[DOC]** : comportement/capacité décrit par une source officielle consultée.
- **[HEUR]** : pratique de sound design, plage de départ ou convention artistique ; à valider à l'écoute.
- **[TEST]** : dépend de la version/install/format VST3-AU/Set/bridge réel ; ne jamais déclarer fonctionnel sans essai.

Ne jamais transformer une heuristique en « règle du manuel ». Ne jamais inventer un nom de paramètre Serum/Ableton pour rendre une recette plus précise.

## Routage par famille

1. Identifier la famille exacte. Si `pad` et `nappe` sont ambiguës : pad = instrument harmonique jouable ; nappe = couche atmosphérique/texturale.
2. Si l'utilisateur impose **Serum 2**, utiliser seulement la branche Serum puis les FX Ableton si demandés.
3. S'il impose **Ableton natif**, ne pas proposer Serum comme composant nécessaire.
4. S'il demande « lequel utiliser ? », sélectionner selon l'architecture sonore recherchée, pas selon une préférence de marque.
5. Pour un son multicouche, justifier la fonction de chaque couche : fondamentale, corps, attaque, texture, air, tail. Supprimer les doublons.

## Workflow de conception

1. **Rôle** — synthé, nappe, drone, stab, riser, impact, pluck, pad, key, sub, mid-bass, lead, texture ou FX.
2. **Sous-type** — choisir un sous-type documenté v5 (analog moderne, granular cinematic, FM metallic, etc.) ou créer un hybride justifié.
3. **Attributs** — registre, attaque, decay/sustain, mouvement, matière, largeur et profondeur.
4. **Moteur** — choisir l'instrument/mode dont la structure correspond au besoin.
5. **Source** — oscillateur/sample/grain/spectral et accordage.
6. **Articulation** — enveloppe d'amplitude, note length, retrigger, mono/poly, glide si utile.
7. **Spectre** — filtre/routage et éventuellement saturation ; écouter avant les FX spatiaux.
8. **Mouvement** — enveloppes/LFO/Matrix/automation ; une modulation doit avoir une intention audible.
9. **Espace** — largeur, delay/reverb, traitement parallèle ; protéger le grave lorsqu'il doit rester stable.
10. **Contrôle** — créer 4–8 macros musicales lorsque le patch doit être automatisé ou piloté par bridge.
11. **Validation** — utiliser `family-validation-protocol.md`, puis comparer à niveau égal et en contexte.

## Sélection des instruments natifs [DOC]

- **Operator** : FM/additive/soustractive à quatre oscillateurs, enveloppes individuelles, pitch/filter/LFO ; plucks digitaux, keys FM, transients, basses.
- **Drift** : synthèse soustractive légère, deux oscillateurs + bruit, Cycling Envelope, LFO et modulation ; synthés, stabs, plucks, risers simples.
- **Wavetable** : deux oscillateurs wavetable, deux filtres et modulation ; synthés, pads, nappes, timbres mobiles.
- **Meld** : deux moteurs indépendants avec filtres/LFO/matrices ; pads, nappes et hybrides modernes.
- **Analog** : deux oscillateurs + bruit, deux filtres, enveloppes/LFO ; stabs, pads et synthés classiques.
- **Electric** : piano électrique modélisé ; keys/EP.
- **Collision** : mallet + bruit vers resonators ; plucks/keys percussifs/résonants.
- **Tension** : modèle de corde avec exciters/damper/body ; plucks et keys organiques.
- **Simpler/Sampler** : one-shots, stabs, impacts, multisamples et resampling.
- **Drum Sampler** : one-shot avec AHD, pitch/filter et effets de lecture dont Pitch Env/Punch/Sub/Noise ; impacts et transients.
- **Granulator III** : granular, modes dont Cloud, capture audio et MPE ; nappes, drones, pads, textures et risers.

## Serum 2 — contraintes documentées

- [DOC] Les oscillateurs **A/B/C** peuvent employer Wavetable, Multisample, Sample, Granular et Spectral.
- [DOC] OSC A/B/C, SUB et NOISE peuvent être routés vers filtres/Main/Direct/None et les bus selon les options disponibles.
- [DOC] Le pitch tracking peut être désactivé ; Xfer cite drones, percussions, noise FX, risers et impacts comme usages possibles.
- [DOC] Avec tracking désactivé, le comportement de hauteur diffère selon le moteur ; ne pas supposer une référence universelle.
- [DOC] Granular est adapté aux textures/pads et peut être plus coûteux en CPU.
- [DOC] La Matrix, les enveloppes/LFO/macros et les modules ARP/CLIP offrent des sources de mouvement internes ; les distinguer de l'automation DAW.
- [DOC] Limiter l'unison inutile ; plus de voix augmente la charge et n'améliore pas automatiquement le son.

## Modulation : terminologie stricte

- **Enveloppe** : geste déclenché par note ; articulation, pluck, transient, mouvement one-shot.
- **LFO** : mouvement répétitif ou forme de modulation ; mode/retrigger à vérifier.
- **Automation Live** : valeur persistante/éditable dans le DAW selon le paramètre exposé.
- **Clip modulation** : modulation relative au réglage de base dans Live.
- **Sidechain/ducking** : réduction liée à un signal/déclencheur ; ne pas appeler automatiquement « sidechain » une simple courbe de volume.

## Patch bridge-friendly

Créer des macros d'intention stables (`TONE`, `MOTION`, `WIDTH`, `SPACE`, `ATTACK`, etc.) et mapper des plages sûres. Les macros servent d'interface artistique ; elles ne prouvent pas que tous les paramètres internes de Serum sont accessibles à Live. L'accessibilité réelle reste [TEST].

## Route spécialisée kick / 808 / rumble v8

Pour toute demande de **kick 808, kick club, techno rumble, relation kick/sub ou design low-end**, déléguer les spécifications et la chaîne de traitement au skill racine `../studio-grade-kick-low-end-sound-design/SKILL.md`. Serum 2 reste le moteur de synthèse lorsque choisi, mais les traitements tiers doivent être sélectionnés par fonction et non empilés automatiquement.

## Livrable obligatoire

Utiliser `references/family-patch-output-schema.md`. Choisir explicitement **famille + sous-type** et expliquer le choix. Donner au minimum : rôle ; moteur et justification ; sources ; voix ; amplitude ; timbre/routage ; modulation ; FX ; macros ; test ; risques ; points [TEST]. Toute valeur chiffrée de recette non officielle doit être étiquetée comme point de départ [HEUR].

## Références commerciales v7

Si une référence figure dans `../producer-intelligence/deep-track-index.md`, utiliser sa fiche pour extraire **fonction du timbre, articulation, densité et rôle spectral**. Ne jamais tenter de recréer un preset reconnaissable depuis le master. Traduire l'attribut en patch original et marquer toute déduction non observable comme [HEUR]/[TEST].
