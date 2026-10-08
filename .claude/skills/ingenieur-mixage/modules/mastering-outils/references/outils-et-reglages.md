# Choisir et régler les outils de mastering

Consulter seulement les fiches nécessaires. Les commandes détaillées doivent correspondre à la version ouverte. Les liens ci-dessous pointent vers les éditeurs ; ne pas recopier une recette de réglages indépendamment du signal.

Pour les outils Waves Audio, consulter aussi [waves-mastering.md](waves-mastering.md).

## EQ — Pro-Q 4, Ozone Equalizer

Pour un défaut stable, commencer par une correction statique justifiée : fréquence, largeur, gain et canal traité. Utiliser une correction dynamique si le problème varie avec le signal. Dans Pro-Q 4, distinguer dynamique de bande et traitement spectral de fréquences à l'intérieur de la bande. Un mode spectral ne rend pas automatiquement une correction transparente. [Manuel Pro-Q](https://www.fabfilter.com/help/pro-q), [dynamique spectrale](https://www.fabfilter.com/help/pro-q/using/spectral-dynamics).

Vérifier le mode stéréo ou M/S avant édition. En M/S, confirmer que la correction cible bien centre ou côtés et que la sommation mono reste cohérente. Choisir le mode de phase selon les besoins et écouter les transitoires ; le mode linéaire n'est pas obligatoire en mastering. Ne pas imposer un coupe-bas sur chaque master. Comparer le résultat avec gain compensé.

## EQ dynamique et résonances — TDR Nova, soothe3

NOVA permet d'associer égalisation et dynamique aux bandes. Identifier zone, seuil, ratio et comportement temporel disponibles ; vérifier la réduction et comparer la correction active/bypass dans les passages concernés. Réserver le traitement dynamique aux variations que l'EQ fixe résout mal. [Manuel NOVA](https://docs.tokyodawn.net/nova-manual/).

Pour soothe3, consulter le manuel de la génération 3 avant d'appliquer des habitudes de soothe2. Délimiter la zone sensible et vérifier ce qui est retiré lorsqu'une écoute de différence est disponible. Réduire la quantité si le timbre perd sa présence ou sa vie ; ne pas multiplier les réducteurs de résonances pour obtenir une courbe visuellement lisse. [Manuel soothe3](https://oeksound.com/manuals/soothe3/).

## Compression — Pro-C 3, bx_glue, API-2500 si disponible

Définir si la compression vise cohésion, contrôle de niveau ou forme de l'attaque. Dans Pro-C 3, choisir un style adapté et régler seuil/ratio/knee puis attaque/relâchement selon la matière. Surveiller réduction, transitoires et récupération entre événements. Les comportements temporels diffèrent selon les styles ; ne pas transposer mécaniquement les millisecondes d'un autre compresseur. Vérifier auto-gain et compensation de niveau lors de la comparaison. [Vue d'ensemble Pro-C](https://www.fabfilter.com/help/pro-c/using/overview), [commandes temporelles](https://www.fabfilter.com/help/pro-c/using/timecontrols).

bx_glue et API-2500 peuvent être choisis pour un caractère de bus lorsque ce caractère sert le morceau. Relever les commandes actuelles de sidechain, mix parallèle et couplage stéréo. Vérifier que la détection ne fait pas pomper tout le master à chaque grave. Ne pas forcer une réduction fixe sur tout le morceau. [Manuel bx_glue](https://files.plugin-alliance.com/products/bx_glue/bx_glue_manual.pdf).

## Mastering assisté — Ozone 12 Elements

Vérifier l'édition affichée. Ozone Elements offre un workflow d'assistance au mastering ; les fonctions et modules des éditions supérieures ne doivent pas être supposés présents. Choisir les intentions ou cibles réellement proposées, analyser une section représentative puis évaluer le résultat sur les autres sections et sur la durée entière. [Présentation officielle Elements](https://www.izotope.com/products/ozone-elements).

Ne pas ajouter automatiquement une chaîne complète avant une assistance qui applique déjà des traitements similaires. Après analyse, lire les contrôles accessibles et ajuster les quantités utiles. Vérifier le comportement de limitation et de plafond de cette édition par une mesure indépendante du fichier final.

## Limitation, clipping et couleur

Choisir un limiteur disponible qui permette le résultat demandé. Régler la quantité de limitation en observant la réduction et en écoutant punch, grave et cymbales. Si une fonction true peak est disponible, vérifier son état et mesurer malgré tout le fichier exporté. Une crête d'échantillon et une true peak sont deux mesures différentes.

Le L2 Waves historique possède seuil, plafond et options de relâchement/dithering selon sa version. Ne pas interpréter son plafond comme une garantie de true peak. Lire la documentation exacte et vérifier le rendu avec un mesureur adapté. [Manuel L2](https://www.waves.com/1lib/pdf/plugins/l2-ultramaximizer.pdf).

Un clipper ou une saturation sont des choix de traitement, pas des étapes obligatoires. Vérifier manuel, réglages de qualité et compensation de gain de l'outil disponible avant usage. Contrôler distorsion, aliasing audible et modification des transitoires. Le nom d'un bundle tel que RazorClip ne suffit pas à déduire son protocole ni ses contrôles.

## Stéréo — Ozone Imager 2 et contrôles mono

Distinguer réglage de largeur et création de stéréo. Dans Imager, vérifier Width et l'état de Stereoize dans la version présente. Comparer stéréo/mono à niveau cohérent et garder le centre stable. Ne pas imposer une quantité d'élargissement ou une fréquence universelle de mono du grave. [Guide officiel Imager](https://www.izotope.com/community/blog/6-tips-for-using-imager-in-ozone-9).

## Mesure — Insight 2, SPAN, Tonal Balance Control

Placer le mesureur sur le trajet final et vérifier le point de prélèvement, notamment si un fader ou un traitement agit après lui. Insight fournit notamment sonie intégrée, momentary, short-term et LRA ; son paramétrage et sa remise à zéro doivent correspondre à la lecture du programme entier. Contrôler aussi les true peaks avec le mode approprié. [Insight](https://www.izotope.com/products/insight), [manuel](https://downloads.izotope.com/docs/insight200/en/index.html).

SPAN sert à inspecter le spectre et la corrélation. Garder les mêmes réglages d'analyse pour les comparaisons et ne pas assimiler un spectre incliné à un défaut. SPAN n'est pas utilisé ici comme substitut présumé à une mesure complète de LUFS et true peak. [Documentation SPAN](https://www.voxengo.com/product/span/).

Tonal Balance Control peut aider à comparer un équilibre tonal : vérifier les fonctions de la version 3 dans son aide intégrée. La zone de référence choisie est un indicateur, pas une obligation d'EQ. Une mesure ou une courbe cible ne remplace jamais l'évaluation du morceau.
