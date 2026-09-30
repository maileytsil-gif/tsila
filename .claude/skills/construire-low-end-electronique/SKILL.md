---
name: construire-low-end-electronique
description: Bibliothèque du grave électronique (kick, sub, basse, 808) pour Ableton Live 12 et Serum 2 — physique (fondamentale et harmoniques, phase, mono, pièce), procédure en huit étapes, recettes de départ par genre (Bass House, Future Rave, Tech House, Minimal, Afro House, 808) et notes sourcées de *The Philosophy of Bass* (FabFilter). Utilise ce skill quand le grave manque de poids, masque le kick, fluctue d'une note à l'autre, disparaît sur petit haut-parleur ou en mono, ou ne passe pas du studio au club, et qu'il faut une recette de genre ou un tableau symptôme → preuve → changement ; rôle, accord, polarité et mesure passent par kick-bass-equilibre, le diagnostic de mix par ingenieur-mixage.
---

# Construire le low end électronique

Claude mesure (`kick_bass_check.py`, `analyze_wav.py`, `lom.py meters` en relatif) ; « écouter » désigne toujours l'utilisateur. Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu ») : `../ableton-live-session/SKILL.md` § Discipline.

## Dans ce workflow

- Rôle (qui tient le fondamental), accord, polarité, décalage, sidechain et mesure : `../kick-bass-equilibre/SKILL.md` (`kick_bass_check.py kick.wav sub.wav --band 30-120` sur exports séparés, `../live-export-wav/SKILL.md`). Ce skill-ci apporte la physique, les recettes par genre et les sources.
- Hauteurs en C3 = 60 (numérotation Ableton) : `../theorie-musicale-electronique/scripts/theorie.py sub <tonique>`.
- Sub / mid dans Serum 2 : `../serum-2-basses-house-future-house/references/tempo-mix.md` ; 808 et harmoniques : `../sound-designer-serum/references/basses.md`.
- Traitements : plug-ins tiers seulement (règle 6 d'`ableton-live-session`) ; outils par tâche `../mixage/references/outils.md`, pilotage `../effets-plugins/references/fiches.md`, installés `../mastering-outils/references/inventaire-local.md`.
- LUFS et true peak : Insight 2 ou WLM Plus en bout de Main, lus par capture (`../mastering-outils/SKILL.md`) ; `analyze_wav.py` ne donne que la crête sample.

## Entrées et priorité

Ouvrir par `lom.py ping` puis `lom.py state --json` ; demander ce qui ne s'observe pas : destination (streaming/club), référence légalement utilisable, symptôme. Relever BPM, tonalité, style et outils présents dans le Set. Sans audio exporté, présenter les réglages comme **points de départ à tester**, sans simuler une écoute. Lire `references/diagnostic-et-physique.md` pour la méthode, `references/recettes-ableton.md` pour les chaînes et `references/sources-videos-workshops.md` pour les sources et leur statut réel d'examen.

## Procédure

Annoncer les huit étapes, n'en exécuter qu'une par échange, état relu avant la suivante.

1. Sauver le Set sous un nouveau nom. Choisir une boucle du drop et une autre du break ; l'utilisateur compare à niveau d'écoute constant. Examiner kick seul, basse seule, ensemble, puis mix entier. Vérifier la ligne MIDI, les octaves et la longueur des notes avant les traitements.
2. Mesurer le kick (attaque, hauteur apparente, queue), le sub par note et leurs superpositions dans le temps. Identifier si l'arrangement donne la priorité temporelle au kick ou laisse le sub jouer sous lui. Ne pas appliquer une fréquence de crossover universelle.
3. Régler les faders d'abord. Chercher tout grave inutile dans voix, pads, reverbs, toms et impacts, mais filtrer seulement si la mesure et l'écoute de l'utilisateur le justifient. Garder les layers sub et mid-bass distincts si cela facilite le contrôle.
4. Comparer les polarités, formes d'onde et alignements temporels seulement pour des signaux qui se superposent réellement. Vérifier le résultat sur plusieurs notes ; un décalage qui renforce un coup peut dégrader les autres. Attention à la latence des plug-ins et au pre-ring d'un EQ linéaire sur transitoire.
5. Mettre un ducking piloté par le kick sur la basse si le chevauchement le demande (convention du projet : `../kick-bass-equilibre/SKILL.md` § 4). Régler attaque et relâchement avec le groove ; noter le gain réduit ; l'utilisateur écoute le retour avant le coup suivant. Si un contrôle temporel strict est requis, préférer une enveloppe d'amplitude dans le synthé (notes raccourcies, ENV de Serum 2) ou une automation de gain d'Utility (toléré, `../live-automation/SKILL.md`) ; bande dynamique de Pro-Q 4 (fenêtre + capture) si seul un conflit spectral ponctuel doit céder.
6. Créer de l'audibilité sur petits haut-parleurs par des harmoniques dosées sur une copie ou un layer de mid-bass, plutôt que par une hausse infinie du sub. Contrôler le gain après saturation et les intermodulations.
7. Comparer drop, break et référence après égalisation perceptive de niveau ; inspecter spectre moyen et court terme, crête, dynamique, mono et canaux L/R. Une courbe cible n'est pas une règle. L'utilisateur écoute au casque, sur les enceintes disponibles et, si possible, sur un système avec sub ; noter les limites acoustiques de la pièce.
8. Livrer un tableau « symptôme → preuve → changement → A/B → résultat », des paramètres de départ et des captures/mesures uniquement si réellement obtenues. Pour streaming et club, deux exports à partir d'un mix cohérent si nécessaire : mesurer leur true peak et leur LUFS dans Insight 2 ou WLM Plus en bout de Main (lus par capture) ; l'écoute des deux versions revient à l'utilisateur. Aucune valeur LUFS unique ne garantit la traduction.

## Décisions rapides

- Kick caché : vérifier d'abord son niveau, sa queue et la note de basse au même instant, puis le ducking ; lire `references/recettes-ableton.md`.
- Sub irrégulier : inspecter les notes, vélocités, enveloppes et énergie par fondamentale ; éviter une compression aveugle.
- Grave qui s'annule : tester sommation mono et polarité des layers, puis timing et filtrage ; conserver l'option qui fonctionne sur l'ensemble de la phrase.
- Club trop lourd / téléphone trop maigre : comparer avec une référence correctement nivelée ; réduire l'accumulation sub et travailler les harmoniques de la basse.
- Objectif théorique sans audio : fournir une recette de session reproductible et indiquer clairement ce qui reste à écouter.

## Vidéos et portabilité

- **Vidéos** : Claude n'entend jamais l'audio. En local, Claude in Chrome permet de lire la transcription et de capturer les démonstrations aux minutages ; en session cloud, YouTube est bloqué. Statut par vidéo : visionnée (captures) / transcription lue / description / inaccessible. Les A/B audibles sont à écouter par l'utilisateur. Suite à donner : `references/sources-videos-workshops.md` § Suite à donner.
- **Qwen Code** lit ce dossier par `.qwen/skills` (même fichiers) ; hors dépôt, les liens `../` ne pointent vers rien : appliquer les règles ci-dessus. Ne jamais affirmer avoir écouté un master ou modifié un projet sans l'avoir fait.
