---
name: serum-2-basses-house-future-house
description: Fiches jouables de dix familles de basses Bass House, Future House (et leur passage en DnB) dans Serum 2 et Ableton Live 12 — sub sinus, pluck rond, hollow FM, organ bass, saw percussive, Reese, wub, growl vocal, donk métallique, screech — avec oscillateurs, routage Direct/None, filtre, enveloppes, LFO, trois ou quatre macros nommées, motif MIDI vérifié (C3 = 60), séparation sub / mid, adaptation au BPM en ms et en divisions, contrôle kick/sub et mono, et registre des tutoriels vidéo avec leur statut réel d'examen. Utilise ce skill dès que l'utilisateur demande une basse house, bass house, future house, un sub, un pluck de basse, une basse FM ou « hollow », un Reese, un wub, un growl, un donk, un screech, une mid bass, « la basse du drop », veut passer une basse d'un BPM à un autre, ou cite un tutoriel de basse Serum. Bibliothèque du rôle sound-designer-serum pour les basses : l'exécution dans Live passe par vst-sound-design et la discipline d'ableton-live-session.
---

# Basses House et Future House dans Serum 2

Ce skill dit **quelle basse construire et comment la programmer** ; le choix du moteur et le tableau de réglages vérifiés relèvent de `../sound-designer-serum/SKILL.md`, le chargement et les clics dans Serum de `../vst-sound-design/SKILL.md`, la relation kick/sub de `../kick-bass-equilibre/SKILL.md`, les notes de `../compositeur-arrangeur/SKILL.md`. Hors Claude Code (Codex), ces liens ne pointent vers rien : appliquer les règles ci-dessous.

## Règles du workflow qui priment sur les fiches

1. **Lire le Set avant de proposer** : tempo, tonalité, rôle de chaque piste basse, présence d'un sub (`lom.py state --json`, mémoire du projet). Sans Set : 128 BPM Bass House, 126 BPM Future House (tempos les plus courants documentés dans `../sound-designer-serum/references/patches-genres.md`), en le disant.
2. **C3 = 60** (numérotation Ableton) pour toute note ; le numéro MIDI fait foi. Un motif s'écrit dans la grille de `composer-hooks-funk-electro` et se vérifie avec `../composer-hooks-funk-electro/scripts/grille.py` (degrés, chevauchements, notation Producer Pal).
3. **Une étape par échange** : annoncer le programme (famille → patch → motif → sub/mid → contrôle), exécuter une étape, faire écouter.
4. **Jamais « entendu »** : Claude n'entend ni le Set ni une vidéo. Distinguer réglé et relu (capture), mesuré (export, niveaux relatifs), proposé.
5. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`) ; ce qui appartient au son reste dans les effets internes de Serum 2.

## Procédure

1. **Famille et rôle** : sub, corps, mouvement, attaque ou ponctuation (`references/families.md`, tableau de choix). Garder une basse principale dans le drop, avec des réponses ponctuelles.
2. **Patch** depuis un preset initialisé : oscillateurs, octaves, routage, warp et filtre, ENV et LFO avec mode et division, FX, trois ou quatre macros nommées avec leurs bornes, note d'essai. Les valeurs des fiches sont des points de départ construits, jamais des réglages attribués à une vidéo. Livrer le tableau section / paramètre / valeur / comment réglé / vérifié de sound-designer-serum (§ 7).
3. **Motif** de deux mesures : partir de `references/motifs.md` (cinq motifs vérifiés, transposables), l'adapter au vrai pattern de kick, vérifier avec `grille.py`, écrire par Producer Pal, relire.
4. **Sub** : un oscillateur `Direct` contourne filtres et FX internes, mais une modulation globale de pitch ou les effets après Serum peuvent l'altérer. Pour une mid bass très modulée (unison, pitch mobile, formants, FX larges), séparer la piste sub et la couche mid, puis vérifier leur somme en mono.
5. **BPM** : une LFO synchronisée garde sa division ; une enveloppe en ms qui doit garder la même proportion métrique est multipliée par BPM initial / BPM final ; attaque, glide et release expressifs restent en temps absolu. Reprogrammer notes et ducking sur les vrais coups de kick, en particulier de House vers DnB. Changer de BPM ne change pas la hauteur (`references/tempo-mix.md`).
6. **Contrôle** : mesurable par Claude (relecture des paramètres, niveaux relatifs `lom.py meters`, export et `kick_bass_check.py`) ; à l'écoute par l'utilisateur, solo puis avec kick/sub puis dans le drop, notes extrêmes, deux bornes de chaque macro, mono, pics de formant, faible volume, A/B à volume comparable.
7. **Vidéos** : statut exact de chaque source (visionnée, transcription étudiée, description consultée, inaccessible) dans `references/sources.md` ; 230 tutoriels Bass House, Dubstep et DnB classés en quinze familles avec identifiant (`F08-03`…), avec leur statut, dans `references/tutoriels-a-consulter.md` ; ce qu'en disent réellement les pages lues et les transcriptions étudiées dans `references/etudes-pages-house.md`, `references/etudes-pages-dubstep-dnb.md`, `references/etudes-captures.md` (valeurs lues sur les captures d'écran) et `references/etudes-videos.md` (les 24 vidéos ★ : 3 transcriptions en session cloud, 21 dans Claude in Chrome, plus deux vidéos intégrées à des pages). En session cloud, les domaines s'ouvrent dans les réglages réseau de l'environnement, mais YouTube finit par bloquer la session (vérification anti-robot, à ne pas contourner) ; en local, Claude in Chrome permet transcription et captures aux minutages (valeurs visibles lues, son jamais entendu) ; sinon, demander la transcription à l'utilisateur. Signaler les fonctions propres à Serum 2 quand la source montre Serum 1.

## Réponse attendue

Un tableau de choix, puis pour chaque basse une fiche jouable : rôle, paramètres Serum 2, motif MIDI (grille vérifiée + notation Producer Pal), macros avec bornes, variation au BPM demandé, chaîne de traitement et test audible à faire par l'utilisateur. Expliquer quel geste produit le timbre plutôt que d'empiler des effets. Consigner le patch retenu (nom du preset sauvé, macros) dans la mémoire du projet (`../memoire-projet/SKILL.md`).

## Voir aussi

- Fondements documentés, sources chiffrées et contradictions : `../sound-designer-serum/references/basses.md` (sub, Reese, growl, 808, division du grave) et `patches-genres.md` (patchs chiffrés bass/future house, OTT).
- Physique et perception du grave, avec ce qui a été lu, calculé ou déduit : `references/documentation-basses.md` (FM et rapports d'octave, formants des voyelles, battements d'unison par note, repliement, peigne kick/sub, courbes d'égale sonie).
- Recettes Bass House du corpus : `../produire-morceau-electronique-de-a-a-z/references/bass-house-recettes.md`, `bass-house-stabs-serum2.md`, `bass-house-wavetable.md`.
- Gestes de basse liés au phrasé et 55 recettes courtes : `../composer-hooks-funk-electro/references/sound-design.md`, `cinquante-cinq-recettes.md`.
- Stabs, pads, leads et impacts qui dialoguent avec la basse : `../bass-house-sound-design/SKILL.md`. Grave dans le mix (poids, mono, traduction club) : `../construire-low-end-electronique/SKILL.md`.

## Installation hors dépôt

Claude Code : copier ce dossier dans `~/.claude/skills/` (ou `<projet>/.claude/skills/`), Codex : dans `~/.codex/skills/`, puis relancer la session. Une version déjà installée se déplace **hors** de ces dossiers avant la copie : laissée à côté sous un autre nom, elle serait chargée comme un second skill du même `name`.
