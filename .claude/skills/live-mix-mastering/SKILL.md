---
name: live-mix-mastering
description: Effectuer le mixage puis le mastering d'un morceau dans Ableton Live, ou masteriser un fichier stéréo fourni. Utiliser pour équilibrer pistes et bus, corriger le spectre et la dynamique, contrôler la stéréo, préparer un prémaster, atteindre une sonie adaptée et vérifier les exports finaux. Ne pas déclencher pour une simple composition MIDI ou création de preset.
---

## Contexte local (lire d'abord)

Lire `references/notes-locales.md` : chaîne de bus masters en place, limiteur, absence de ffmpeg, natifs interdits en mix, et renvois vers `../ableton-live-session/SKILL.md` (règles de session), `../ingenieur-mixage/SKILL.md` (diagnostic et contrôle qualité), `../mixage/SKILL.md` (procédure de mix), `../effets-plugins/references/fiches.md` (pilotage des plug-ins), `../mastering-outils/SKILL.md` (fiches des outils). Vérifier les outils réellement connectés (Producer Pal, LOM Bridge, écran) avant d'agir ; sans accès, guider et dire la limite.

# Mixage puis mastering

## Cadrage et outils
Lire le skill ableton-live-session avant d'agir dans Live ; utiliser ses moyens disponibles de lecture, pilotage et sauvegarde. Respecter la préférence enregistrée de l'utilisateur pour des effets tiers dans les chaînes de mix, sauf instruction actuelle contraire. Vérifier les plug-ins réellement présents et les paramètres accessibles ; les listes historiques ne prouvent pas leur disponibilité. Utiliser le contrôle d'interface pour les paramètres non exposés, avec observation avant et après.

Identifier la source : Set avec pistes séparées, stems ou mix stéréo. Sur un mix stéréo, ne pas promettre de corriger indépendamment des pistes absentes. Relever genre/intention, référence éventuellement fournie et destination si connus. Ne demander que ce qui change une décision ; sans référence, progresser sur l'état observable sans inventer une esthétique imposée.

Présenter brièvement les phases diagnostic → mix → prémaster → mastering → export. Respecter le rythme de travail demandé par l'utilisateur : le skill de session conserve une préférence pour une étape à la fois ; une demande explicite d'exécuter l'ensemble autorise leur enchaînement. La création ou installation de ce skill ne déclenche aucune modification du Set.

## 1. Diagnostic
- Lire le Set actuel : routages, bus, sends, effets, bypass, automations, solos/mutes, pistes de référence et étendue du morceau. Vérifier où se trouve réellement le traitement final ; ne pas déduire le trajet audio du seul nom « MASTER ».
- Préserver une version de départ et relever les états qui seront modifiés. Garder les choix sonores intentionnels, y compris les traitements de bus déjà structurants.
- Inspecter les passages denses, les passages exposés et les transitions. Mesurer puis écouter si un accès audio existe. Distinguer clairement observations sonores et mesures ; sans écoute, fournir un travail technique vérifié et signaler ce qui nécessite une validation auditive.

## 2. Mixage
Lire [references/mixage.md](references/mixage.md). Commencer par l'équilibre et le routage ; choisir ensuite les traitements justifiés par un problème observé. Pour chaque changement, identifier la piste, l'objectif et l'effet vérifiable. Comparer à niveau perçu comparable, dans le morceau autant qu'en solo.

Traiter les problèmes locaux à leur source avant le bus global. Relire après chaque groupe de changements et sauvegarder les étapes cohérentes. Ne pas imposer une chaîne identique à chaque piste, un coupe-bas systématique ou une cible de crête fixe pour tous les instruments.

## 3. Prémaster
Vérifier équilibre, transitoires, grave, mono, transitions et fins. Désactiver uniquement les traitements de sonie finale qui doivent être réservés au mastering, après avoir préservé leur état ; conserver les effets créatifs et la compression qui participent au mix.

Produire un prémaster sans normalisation et sans écrêtage involontaire, avec une marge suffisante pour la chaîne suivante. Une crête exactement à −6 dBFS n'est pas une condition obligatoire. Préserver fréquence d'échantillonnage et résolution pertinentes ; un fichier de travail flottant peut convenir si le flux le supporte. Vérifier que la référence n'est pas incluse.

## 4. Mastering
Lire [references/mastering-mesures.md](references/mastering-mesures.md). Partir du prémaster vérifié ou du mix stéréo fourni. Régler équilibre global, dynamique et sonie selon la destination et l'intention, avec un nombre de traitements justifié. Ne pas remplacer le mixage par une limitation intensive.

Vérifier si le mastering se fait dans le Set, un Set distinct ou sur fichier ; éviter de faire repasser un master traité dans la même chaîne. Comparer avant/après à niveau comparable. En cas de pompage, distorsion, perte de punch ou grave instable, corriger l'étage responsable plutôt qu'ajouter un limiteur supplémentaire par défaut.

## 5. Livraison
Utiliser live-export-wav pour le dialogue et la vérification d'export, mais déterminer chemins, fréquence, durée et format à partir du projet actuel : ses exemples ne sont pas des valeurs obligatoires. Appliquer les distinctions de mesure de la référence mastering, notamment pour l'écrêtage et les true peaks.

Livrer le master et, si utile ou demandé, le prémaster/stems, sans écraser les versions précédentes. Donner les chemins, formats, durée, LUFS intégrés, true peak et limites de vérification réellement disponibles. Ne jamais annoncer « prêt à publier » sur la seule base d'un plafond de crête. Ne pas prétendre qu'un simple contrôle structurel de fichier constitue une écoute.
