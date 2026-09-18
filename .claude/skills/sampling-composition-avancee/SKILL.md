---
name: sampling-composition-avancee
description: Composer et transformer un morceau à partir de samples avec analyse harmonique avancée, conduite des voix, reharmonisation, chopping, contrepoint, polymétrie et développement motivique. Utiliser pour créer un sample flip, recomposer une boucle ou bâtir une composition à base de fragments audio. Pour une simple capture audio sans composition, utiliser resampling.
---

# Composition avancée par sampling

## Intention et périmètre

Traiter les samples comme des objets musicaux qui portent simultanément des hauteurs, un rythme, une articulation, un timbre et un espace. Choisir la théorie qui sert l'intention musicale ; ne pas appliquer tous les procédés ni augmenter systématiquement la densité. Expliquer les choix en français accessible, avec les notes réelles lorsque cela aide.

Pour intervenir dans Ableton, lire `../ableton-live-session/SKILL.md` et relire le Set. Pour capturer ou imprimer de l'audio, utiliser `../resampling/SKILL.md`. Lire `../melodie-composition/SKILL.md` si des voix MIDI complémentaires sont nécessaires ; `../arrangement-avance/SKILL.md` pour construire l'arrangement ; `../vst-sound-design/SKILL.md` pour charger ou transformer un instrument échantillonné. Respecter les outils et instruments disponibles. Ne pas modifier un Set si la demande porte seulement sur une analyse ou une proposition.

Les demandes de ce skill autorisent la composition demandée, pas un remplacement global du mix. Conserver les sources et travailler sur des copies. Appliquer le workflow de session par étapes, sauf demande contraire explicite.

## 1. Cartographier le matériau

Identifier le contexte : rôle attendu, style, centre tonal éventuel, métrique, tempo, plage, éléments à conserver. Déduire ce qui peut l'être ; demander seulement ce qui change réellement la composition.

Pour chaque fragment utile, relever :
- identifiant et emplacement source ; début, fin et queue ;
- attaques et accents, durée musicale, anacrouse éventuelle ;
- basse audible, notes saillantes et voix supérieure ;
- accord ou ensemble de hauteurs possible, évolution interne ;
- timbre, densité et traitements déjà imprimés ;
- degré de confiance : confirmé, probable ou indéterminé.

Ne pas confondre le pic spectral le plus fort avec la fondamentale, ni la note la plus grave avec la fondamentale harmonique. Un accord isolé ne prouve pas une tonalité. Une transcription automatique ou une séparation de sources reste une hypothèse à contrôler. Si les notes ne sont pas accessibles avec suffisamment de fiabilité, proposer des lectures alternatives ou choisir une écriture peu dépendante de l'harmonie ; ne pas inventer une analyse exacte.

Séparer les hauteurs simultanées des notes qui se succèdent. Une queue peut porter l'accord précédent au-delà de la prochaine attaque : l'inclure dans l'analyse des chevauchements.

## 2. Choisir le niveau de transformation

- **Citation / boucle** : préserver la phrase ; composer surtout la basse, les réponses et la forme.
- **Chopping** : recomposer des unités porteuses d'un geste ou d'une harmonie ; les transitoires ne sont qu'un point de départ pour les découpes.
- **Instrument échantillonné** : isoler une note, une frappe ou une syllabe pour la rejouer ; contrôler accordage et enveloppe.
- **Transformation de texture** : étirement, granulaire, reverse ou réenregistrement ; vérifier si la hauteur reste assez stable pour une fonction harmonique.

Pour la théorie des hauteurs, lire [Harmonie et transformations](references/harmonie.md), complétée par `../theorie-musicale-electronique/references/harmonie-avancee.md` (modes, voicings, limites du grave) et `../theorie-musicale-electronique/scripts/theorie.py` (transpose, inversion, progression). Pour l'organisation temporelle et le développement, lire [Rythme, contrepoint et forme](references/rythme-forme.md) et `../theorie-musicale-electronique/references/rythme-avance.md` (euclidiens, polymétrie, syncope). Charger seulement les parties nécessaires. Avant toute transformation de clips existants : instantané (`../memoire-projet/SKILL.md`).

## 3. Écrire une proposition concrète

Définir d'abord un noyau reconnaissable : contour, cellule rythmique, intervalle, timbre ou silence. Choisir ensuite une trajectoire de tension et une arrivée. Une harmonie modale ou une forme ouverte n'exige pas de cadence tonale.

Préparer une carte d'événements, adaptée au travail : position, fragment, durée, transposition en demi-tons, accord/basse résultants, rôle et traitement. Préciser l'unité temporelle et la convention d'octave ; dans le workflow Ableton de l'utilisateur, MIDI 60 = C3.

Écrire les appuis et la basse avant les couches de remplissage. Lorsque le sample contient déjà une basse, tenir compte de cette voix plutôt que d'ajouter automatiquement un sub. Une coupe fréquentielle ne garantit pas la disparition d'une note et de ses harmoniques.

Vérifier chaque choix à trois échelles : raccord immédiat, phrase, section. Une variation doit modifier une dimension perceptible tout en conservant assez de repères pour appartenir au même morceau.

## 4. Réaliser sans confondre audio et partition

Une transposition globale déplace toutes les notes d'un sample polyphonique ensemble. Pour changer une voix interne, utiliser un autre fragment, une source séparée vérifiée ou une reconstruction ; ne pas promettre un changement d'accord impossible avec une simple commande de pitch.

Distinguer repitch, transposition avec durée préservée et étirement temporel. Avec lecture à vitesse variable, le rapport vaut `2^(n/12)` pour n demi-tons ; la durée est divisée par ce rapport. Inspecter le Warp et les limites réelles du sampleur avant de combiner pitch et rythme.

Le reverse audio inverse aussi les enveloppes : il n'est pas équivalent à un rétrograde de notes réarticulées. Le découpage et le redéclenchement conservent davantage les attaques d'origine.

Lors du layering, attribuer une fonction à chaque couche et contrôler chevauchement, phase et grave. Lors du resampling, garder la prise précédente, éviter de doubler les chaînes déjà imprimées et n'aplatir que lorsque cela sert le résultat demandé.

## 5. Vérifier et restituer

Relire les événements réellement écrits : fragments, positions, durées, pitch, Warp, enveloppes, routage et fin des queues. Comparer notes prévues et notes effectivement présentes lorsqu'elles sont vérifiables. Contrôler la jonction de boucle et les points de changement harmonique, y compris les réverbs.

Avec écoute disponible, vérifier lisibilité du motif, groove, conflits de registre et évolution de tension. Sans écoute, préciser les limites : cohérence théorique et vérification technique ne valent pas validation sonore. Ne pas affirmer que le sample est juste, accordé ou agréable sans preuve correspondante.

Résumer le matériau conservé, les transformations, la logique harmonique et rythmique, les mesures concernées et les incertitudes restantes. Présenter les concepts avancés à travers leur effet musical, pas sous forme d'un inventaire de jargon.
