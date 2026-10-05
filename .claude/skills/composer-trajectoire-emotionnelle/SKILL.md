---
name: composer-trajectoire-emotionnelle
description: Concevoir et vérifier la trajectoire émotionnelle d'un morceau électronique — une ambiance générale et 1 à 4 émotions (dont une dominante) placées en mesures, traduites en indices musicaux (harmonie, groove, timbre, transitions, dynamique), puis test de perception par l'utilisateur. Utiliser quand l'utilisateur parle d'émotion, d'ambiance, de ressenti ou veut un passage « plus mélancolique », « plus euphorique ».
---

# Composer une trajectoire émotionnelle

Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

## Cadrer les émotions

Définir une ambiance générale en une phrase, puis choisir **une à quatre émotions au maximum**, hiérarchisées : émotion dominante, éventuels contrastes et résolution. Distinguer émotion que la musique *semble exprimer* et émotion que l'auditeur *ressent*. Aucun paramètre musical ne garantit une émotion chez tout le monde; culture, vécu, contexte et référence modifient la réponse. Choisir avec l'utilisateur au moins une piste de référence selon le style, puis noter les passages précis qui produisent l'effet voulu sans les copier.

Donner pour chaque émotion une cible de valence (sombre ↔ lumineuse), d'énergie (calme ↔ intense) et de tension (stable ↔ suspendue), chacune sur 1–5 (reporter aussi l'énergie sur la courbe 1–9 de `../theorie-musicale-electronique/references/forme-tension.md` §4). Placer les émotions sur les repères relus de l'Original Mix (`../arrangement-avance/scripts/arrangement_map.py`), carte consignée dans `projet-<nom>.md` (`../memoire-projet/SKILL.md`) ; dériver ensuite l'Extended Mix avec la même identité et des phrases DJ supplémentaires. Ne jamais ajouter quatre émotions simplement pour atteindre la limite.

## Composer par faisceau d'indices

Lire [references/leviers.md](references/leviers.md). Manipuler plusieurs indices cohérents plutôt qu'un mode majeur/mineur isolé : registre, contour mélodique, vitesse des événements, accents, harmonie et voix des accords, densité, articulation, intensité, enveloppes et texture. Écrire au moins deux variantes A/B d'un passage en ne changeant qu'un groupe d'indices à la fois, chaque variante dans un nouveau clip ou une copie, instantané avant (`../memoire-projet/scripts/snapshot_clips.py`), une variante par échange, pour déterminer ce qui agit réellement. Conserver le hook reconnaissable au travers des changements de sections.

Utiliser `theorie-musicale-electronique` et `composer-hooks-funk-electro` pour les notes (via `compositeur-arrangeur`), `sound-designer-serum` et `serum-2-basses-house-future-house` pour les timbres, `produire-avec-maschine-mk3` pour le jeu et les transitions, `ingenieur-mixage` pour la profondeur (plug-ins tiers seulement, règle 6 de `../ableton-live-session/SKILL.md`). Garder sub et basse médium séparés. Le kick et la basse peuvent soutenir l'émotion par leur attaque, durée, rythme et mouvement sans transformer le grave en effet incontrôlé. Respecter le choix de routage Perform FX de l'utilisateur.

## Écrire la trajectoire

Pour chaque section, produire : émotion visée, trois indices audibles, degré d'énergie/tension, motif conservé, geste de transition, test d'écoute. Construire tension et détente avec retrait/réintroduction, anticipation rythmique, conduite harmonique, changement de registre et silence; doser risers, reverse cymbals et impacts. Dans les drops, varier la fin de chaque bloc de huit mesures sans effacer l'émotion dominante. Ne pas augmenter mécaniquement le volume pour simuler une progression.

## Tester et corriger

Lire [references/ecoute.md](references/ecoute.md). Faire écouter à l'utilisateur (Claude n'entend pas), à niveau comparable, sans révéler d'abord les étiquettes émotionnelles. Faire noter à l'utilisateur et, si possible, à quelques auditeurs cibles : émotion perçue, intensité 1–5 et moment de bascule en mesures. Tester une courte version sans texte/voix si la musique instrumentale doit elle-même porter l'émotion. Comparer les réponses à l'intention, vérifier confusions et réviser un seul groupe d'indices. Les réactions individuelles divergentes ne sont pas des erreurs de mesure.

Vérifier Original Mix et Extended Mix séparément : les passages communs doivent transmettre la même trajectoire; l'intro/outro DJ peut être plus fonctionnelle sans renverser l'ambiance générale. Ne pas déclarer « émotion obtenue » si aucune écoute réelle n'a eu lieu; parler d'hypothèse de composition.

## Livrables

Fournir carte émotionnelle en mesures pour les deux versions, référence choisie, progression et motifs MIDI exacts quand demandés (tableau de `../compositeur-arrangeur/SKILL.md` §6, numérotation Ableton C3 = 60, le numéro MIDI fait foi), recettes de timbre/jeu, transitions, variantes A/B, retours d'écoute et décisions de correction. Si l'utilisateur demande une session Live, manipuler seulement les outils disponibles et vérifier réellement les changements.

## Dans ce workflow

Intention et tableau de notes C3 = 60 : `../compositeur-arrangeur/SKILL.md` · variantes à partir de l'intention : `../melodie-composition/SKILL.md` · dispositifs de tension et courbe d'énergie : `../theorie-musicale-electronique/references/forme-tension.md` · repères et carte des sections : `../arrangement-avance/SKILL.md` · carte émotionnelle et instantanés A/B : `../memoire-projet/SKILL.md` · extraits A/B mesurés : `../live-export-wav/SKILL.md` · cadre du morceau (référence, Original/Extended Mix) : `../produire-demo-electro-rapide/SKILL.md` · vocal chops pour la montée, la tension, la surprise, le rythme et l'ambiance (65 tutoriels étudiés, usage émotionnel de chaque thème) : `../sampling-composition-avancee/references/vocal-chops-synthese.md`.
