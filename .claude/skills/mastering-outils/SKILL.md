---
name: mastering-outils
description: Fiches des outils de mastering disponibles sur ce Mac, appelées par live-mix-mastering — Waves (L4, L2/L3, WLM Plus, F6, TG Mastering Chain), Ozone Elements, FabFilter Pro-Q et Pro-C, Insight, SPAN, TDR Nova : choisir, régler puis vérifier chaque outil, mesurer sonie LUFS, true peak, punch, équilibre tonal, livrer. Utilise ce skill quand la procédure de mastering (live-mix-mastering) est engagée et qu'il faut choisir ou régler un limiteur, un mesureur ou un traitement stéréo précis, ou quand l'utilisateur nomme un de ces outils ; pour reprendre les pistes séparées, mixage / ingenieur-mixage.
---

# Mastering et outils

## Domaine et accès
Partir d'un mix stéréo, d'un prémaster ou du bus final du Set désigné. Le travail comprend diagnostic, choix des traitements, réglages, comparaison et vérification du rendu. Une demande de création ou d'installation du skill ne demande pas de traiter un morceau.

Ce skill est autonome et utilisable dans Claude Desktop/claude.ai, Claude Code et tout environnement compatible avec SKILL.md. Les références sont relatives à ce dossier. Il ne fournit ni les plug-ins, ni leurs licences, ni une connexion au logiciel audio. Vérifier les outils réellement disponibles ; un terminal distant ne donne pas accès au Mac par défaut. À défaut de pilotage, analyser les fichiers accessibles et guider les réglages qui nécessitent l'utilisateur, en précisant ce qui a effectivement été fait.

Dans Ableton, utiliser ableton-live-session s'il est installé pour les commandes de l'hôte. Sinon observer les pistes, le routage, la chaîne et le transport via les outils connectés. Éviter le hot-swap : confirmer le slot cible et relire la chaîne après chargement. Pour les paramètres non exposés, utiliser une interface observée et les valeurs affichées. Ne pas inventer une API de plug-in ni réutiliser des coordonnées d'une ancienne capture.

## Préparer
1. Identifier source, format, tempo si pertinent, début/fin et traitements déjà appliqués. Préserver l'original et la version de départ du Set. Pour un fichier importé à des fins de mastering, vérifier que l'hôte ne change pas sa vitesse ni sa hauteur par warp ou adaptation au tempo.
2. Préciser intention et destination avec les informations déjà disponibles. Une cible de normalisation de plateforme n'est pas automatiquement une cible artistique de mastering. Ne pas imposer −14 LUFS à tous les styles, ni demander arbitrairement une crête de prémaster à −6 dBFS.
3. Vérifier le trajet de la référence et du signal traité : écoute comparative à niveau comparable, référence exclue de l'export, absence de double passage dans une chaîne de mastering.
4. Mesurer l'original et écouter si l'accès audio existe. Repérer passages denses, transitoires et fins. Une courbe de spectre ne suffit pas à décider qu'un morceau sonne mal ; sans écoute, distinguer constat technique et jugement auditif.

## Choisir les outils
Lire [references/outils-et-reglages.md](references/outils-et-reglages.md) pour sélectionner un traitement selon sa fonction et régler l'instance. Lire [references/inventaire-local.md](references/inventaire-local.md) pour les plug-ins repérés sur le Mac d'origine ; un bundle présent ne prouve pas que l'hôte le charge ou que sa licence est active.

Respecter la préférence de l'utilisateur pour les effets tiers lorsqu'elle s'applique. Utiliser les outils disponibles avant de proposer un achat. Ne pas traiter Ozone Elements comme Standard/Advanced, ni un WaveShell comme la preuve que tous les plug-ins Waves sont disponibles.

Exemple d'ordre de travail, à adapter : correction tonale → dynamique si nécessaire → couleur/espace si nécessaire → limitation → mesure finale. Cet ordre n'impose aucun nombre de plug-ins. Ne pas empiler EQ dynamique, réduction de résonances et multibande sur la même zone sans problème distinct identifié.

Pour Waves Audio, lire [references/waves-mastering.md](references/waves-mastering.md) : sélection, EQ, compression, multibande, couleur, stéréo, limiteurs et mesure. Distinguer notamment la comparaison Gain Match de L4 et son état de sortie final, ainsi que la mesure seule et le traitement de WLM Plus.

## Régler et comparer
- Donner un objectif à chaque étage et ajuster progressivement. Relire paramètres, unités, état de bypass et gain de sortie. Comparer à volume perçu comparable ; la version plus forte ne doit pas gagner par défaut.
- Préserver les transitoires et le grave. Si la limitation pompe ou déforme le kick, déterminer si la cause est le mix, le grave, la compression précédente ou le limiteur. Corriger la cause ; une hausse de LUFS n'est pas une amélioration suffisante.
- Les suggestions d'un assistant de mastering sont un point de départ. Vérifier la section analysée, les modules effectivement engagés et le résultat sur le morceau entier.
- Vérifier mono, centre et largeur après un traitement stéréo. Contrôler les effets de l'oversampling et des modes de qualité lorsqu'ils existent, particulièrement si les paramètres de rendu diffèrent de l'écoute.
- Sauver les étapes utiles. Une modification du mix qui dépasse le mastering stéréo doit être explicitée et rester dans le périmètre demandé.

## Rendu et livraison
Lire [references/mesures-et-livraison.md](references/mesures-et-livraison.md). Contrôler l'export final, pas seulement le limiteur en temps réel. La mesure doit porter sur le fichier effectivement livré et le programme entier.

Fournir le master et son nom/version, format, fréquence, résolution, durée, LUFS intégrés, true peak et éventuellement LRA. Nommer l'analyseur et indiquer les valeurs non mesurées. Résumer les traitements utiles et la vérification auditive réalisée ou encore nécessaire. Ne pas inventer de mesure ou affirmer « prêt à publier » à partir du seul plafond affiché.

Notes propres à ce Mac (liens vers les autres skills, FFmpeg absent, chaîne en place) : `references/notes-locales.md`.
