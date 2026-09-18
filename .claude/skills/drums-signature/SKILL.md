---
name: drums-signature
description: Grilles de batterie par genre et signature sonore dans Ableton Live — grille rythmique de référence (house deep/minimal/tech, techno, melodic techno, drum & bass, électro), choix des samples ou synthés par élément (Drum Rack, Serum kick, Battery 4) et **registre de signature** réutilisable (chemins, accord, gains, chaîne) pour retrouver la même identité d'un morceau à l'autre ; scripts drum_pattern.py (pattern de départ) et kit_builder.py (kit depuis le registre). Utilise ce skill quand il faut un kit, un pattern de départ pour un genre, « le même son que sur le morceau précédent », ou enregistrer un son validé ; le groove, le swing et les vélocités relèvent du rôle producteur-rythmique, qui appelle ce skill.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Batteries par genre + signature sonore

## 1. Lire la signature avant de choisir un son
`references/signature.md` (registre lisible) et `scripts/signature.json` (données) décrivent les sons **déjà validés** de l'utilisateur : chemin du sample ou preset, note du pad, gain/pan de chaîne, accord, chaîne d'effets, morceau d'origine. Pour un nouveau morceau du même univers : partir de ces sons, puis varier une ou deux pièces (hats, perc) — c'est ça, la signature. Quand un son nouveau est validé à l'écoute par l'utilisateur, l'**ajouter au registre** (nom, chemin, réglages, date, morceau).

## 2. Choisir le genre → la grille (`references/patterns.md`)
| genre | BPM | kick | clap/snare | hats | ce qui fait le genre |
|---|---|---|---|---|---|
| deep/minimal house | 118–124 | 4 temps, rond et court | clap/rim discrets sur 2 et 4 | contretemps + doubles fantômes, swing 16e 0,02–0,04 | espace, percs organiques, peu d'éléments |
| tech house | 124–128 | 4 temps, plus sec | clap 2 et 4 + rim syncopé | offbeat marqué, open hat « et » du 4 | groove de percs, shuffle |
| techno | 128–135 | 4 temps, long/ténébreux ou sec | clap 2/4 ou snare décalée, rides | 16es droites, offbeat ; peu de swing | hypnose, répétition, rumble |
| drum & bass | 170–176 | 1 et « et » de 3 (two-step) | snare 2 et 4, ghosts | 8es/16es, shuffle léger, breaks samplés | break + sub, syncope |
| électro (electro/breaks/808) | 125–135 | cassé : 1, « et » de 2, 3.5… | snare/clap 808 sur 2 et 4 | 16es 808, ouverts en syncope | 808, robotique, silences |
Écrire en notation Producer Pal (`scripts/drum_pattern.py <house|techhouse|melodictechno|techno|dnb|electro> [--bars 8] [--variant A|B] [--fixe]` : pattern avec accents, ghosts et variations ; `--fixe` donne des vélocités fixes, sans plage aléatoire, conformément à la règle « pas d'humanisation aléatoire » de `../producteur-rythmique/SKILL.md`). Toujours : motif de vélocités répété (pas d'aléatoire), une variation toutes les 4/8 mesures, un fill avant les transitions, les downbeats exacts.

## 3. Choisir sample ou synthé (`references/sons.md`)
- **Kick** : synthé (Serum « DR - Kick Minimal », banques TKNVLT/F Brooks, Operator) quand il faut accorder et régler la longueur ; sample (Drum Booth, Core Library) pour un caractère acoustique/vintage. Toujours : accord ≈ tonique ou quinte du morceau, sub complémentaire (le kick au-dessus de 50 Hz si le sub tient le fondamental), sidechain.
- **Clap/snare** : superposer 2 couches (corps + transitoire), rim/snap discret pour la house, snare courte compressée pour la DnB, 808 pour l'électro.
- **Hats/percs** : samples courts (Core Library one-shots, Skitter and Step, Drive and Glow) ; percs « organiques » (congas, cabasa, shakers) pour la house ; rides/metal pour la techno ; breaks pour la DnB.
- Recherche : `ppal-library` (kind audio, type oneshot, tags Kick/Clap/Hihat…, `findSimilar` sur un son de la signature pour rester cohérent).

## 4. Construire dans Live
- Un Drum Rack par famille (KIT Kick / KIT Clap-Rim / KIT Hats / KIT Perc) : `scripts/kit_builder.py <signature> [famille]` imprime les `params` prêts pour `ppal-create-device` (pads, samples, gains) ; chaîne par piste → `AUDIO - X` → `BUS - BATTERIE` (skills `mixage`, `effets-plugins`).
- Écrire les clips par section (`ppal-create-clip`), relire (`ppal-read-clip`), mesurer le niveau avant fader (kick ≈ −3 dB), poser le sidechain sur sub/basse.
- Sauver ; mettre à jour le registre si un son nouveau est retenu ; journal de la mémoire projet (`../memoire-projet/SKILL.md`).
