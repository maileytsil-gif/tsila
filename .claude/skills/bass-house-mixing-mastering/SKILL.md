---
name: bass-house-mixing-mastering
description: Diagnostiquer et mixer une production Bass House, avec priorité au couple kick/sub, au sidechain/ducking, à la gestion spectrale et dynamique, au mono, au bus processing, au loudness et aux contrôles de traduction. Utiliser pour corriger un mix ou préparer un master ; ne pas inventer de mesures sans analyser l'audio.
---

# Bass House Mixing & Mastering — v7 Producer-informed — v3 documentée

Chercher la puissance par **arrangement → balance → phase → dynamique → spectre → espace → bus → master**. Le mastering ne doit pas réparer un conflit structurel entre kick, basse et arrangement.

## Documentation requise

Lire `references/documentation-map.md`, `references/kick-bass-system.md`, `references/native-tools-decision-tree.md` et `references/mix-master-checklist.md`. Si les plug-ins tiers sont disponibles, `references/third-party-tools.md` donne des usages documentés sans rendre le workflow dépendant d'une marque.

## Discipline de diagnostic

Pour chaque problème, séparer :
- **mesuré/entendu** — preuve disponible ;
- **cause probable** — hypothèse ;
- **test** — action réversible qui permet de confirmer ;
- **correction minimale** — changement le plus petit qui résout le problème ;
- **critère d'acceptation** — ce qui doit être meilleur après la correction.

Sans audio, stems ou mesures : fournir un protocole, jamais un diagnostic fictif.

## Workflow

1. Vérifier gain staging et référence à niveau compensé.
2. Isoler kick + sub/bass et résoudre timing, phase et partage temporel avant l'EQ détaillée.
3. Ajouter drums puis éléments principaux ; équilibrer les faders avant les chaînes complexes.
4. Employer EQ/dynamic EQ seulement pour un besoin identifiable.
5. Choisir compression, clipping, saturation ou ducking selon leur **fonction**, pas selon une recette.
6. Gérer largeur et espace en protégeant la stabilité du grave.
7. Traiter les bus uniquement si le groupe gagne en cohérence sans perdre le punch.
8. Masteriser avec marge de décision ; comparer niveau compensé et contrôler les transients.
9. Exporter/tester plusieurs systèmes ou au minimum casque + niveau faible + mono.

## Règles documentées transformées en décisions

- [DOC] Le Compressor de Live peut utiliser une entrée sidechain externe. Utiliser ce mécanisme lorsque le kick/signal doit réellement déclencher la réduction ; ne pas appeler « sidechain externe » une simple courbe LFO.
- [DOC] Utility propose un contrôle de largeur et une fonction Bass Mono avec fréquence réglable. C'est un outil possible, pas une obligation d'aplatir toute la zone grave.
- [DOC] Spectrum analyse le signal sans l'altérer : l'utiliser pour vérifier, jamais comme preuve que le mix « sonne bien ».
- [DOC] Saturator/Roar sont des outils de coloration/distorsion ; Limiter sert à contrôler les crêtes/plafond. Ne pas les interchanger conceptuellement.
- [DOC] Pro-Q 4 propose plusieurs modes de traitement. Linear Phase n'est pas « supérieur » par principe : choisir le mode en fonction du besoin et vérifier les effets secondaires.
- [DOC] Pro-C 3 expose attack, release, lookahead et external sidechain ; régler les temps d'après le signal réel.

## Bass House : heuristiques à tester

- [HEUR] Garder le contenu le plus bas centré/stable et créer la largeur plutôt avec les harmoniques supérieures.
- [HEUR] Laisser au kick et au sub des fenêtres temporelles perceptibles plutôt que tenter de tout régler par EQ.
- [HEUR] Un sidechain plus profond sur le sub que sur des couches hautes peut fonctionner, mais les dB exacts dépendent du kick, du tempo et de l'enveloppe.
- [HEUR] Clipper quelques crêtes avant le limiteur peut réduire le travail de ce dernier, mais seulement si le transient et le timbre restent meilleurs en A/B.
- [HEUR] Ne pas viser une valeur LUFS universelle. Le niveau final dépend de la destination, de la référence, du codec/plateforme et de l'intégrité du mix.

## Sortie attendue

Pour chaque intervention : piste/bus, problème, test, outil/fonction, paramètres de départ si utiles, métrique/écoute à comparer, condition de rollback. Les chiffres sont des points de départ [HEUR], jamais une preuve de correction.


## Références producteur v6

Quand une référence commerciale est utilisée pour guider le mix, lire `references/producer-informed-mix-principles.md`. Ne jamais déduire une cible numérique non vérifiée à partir du nom d’un artiste.

## Référencement v7

Pour comparer un mix à une référence commerciale, utiliser les fiches `../producer-intelligence/deep-tracks/` uniquement pour la **hiérarchie fonctionnelle**. Effectuer tout A/B à niveau perçu rapproché. Ne pas déduire les réglages de mastering, de compresseur ou d'EQ depuis le master stéréo. Les niveaux, fréquences et valeurs chiffrées restent [TEST] tant qu'ils ne sont pas mesurés.

## Kick / 808 / rumble v8

Pour la **conception** du kick, du pitch-drop, du sub tail et du rumble, lire `../studio-grade-kick-low-end-sound-design/SKILL.md`. Ce skill mix/master intervient ensuite pour l'équilibre global, le headroom et la finition ; ne pas utiliser le mastering pour réparer une architecture kick/basse mal choisie.
