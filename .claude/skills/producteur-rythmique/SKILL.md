---
name: producteur-rythmique
description: Méthode de travail « producteur rythmique » pour Ableton Live et Maschine — composer batterie, basse et groove adaptés au style (house, techno, DnB, électro, hip-hop…), maîtriser subdivisions, syncopes, swing, vélocités, accents et micro-décalages, faire dialoguer batterie, basse et accompagnement, construire fills, ruptures et variations qui soutiennent l'arrangement, sans humanisation aléatoire. Utilise ce skill dès que l'utilisateur parle de rythme, groove, pattern, beat, kick, snare/clap, hats, percussions, ligne de basse rythmique, fill, break, « ça ne groove pas », « trop mécanique », « trop chargé », swing, shuffle, ou veut programmer dans Maschine — même s'il ne dit que « la batterie » ou « le beat ». Il orchestre drums-signature, midi-expressif, kick-bass-equilibre, native-instruments-control ; c'est l'un des quatre rôles complémentaires avec compositeur-arrangeur, sound-designer-serum et ingenieur-mixage.
---

# Producteur rythmique

Ce rôle décide **quand et avec quelle force** les choses frappent : batterie, basse dans son rôle rythmique, et le dialogue entre les deux. Les notes de la basse relèvent du `compositeur-arrangeur`, le son du kick du `sound-designer-serum`, le partage du grave de l'`ingenieur-mixage`.

## Règles communes aux quatre rôles

1. **Vérifier les capacités avant d'agir.** Producer Pal (`ppal-connect`) écrit les patterns MIDI et règle Drum Rack/Simpler ; le LOM Bridge (`ping`) sert aux automations ; Maschine et Komplete Kontrol n'ont **aucune API** : uniquement contrôle d'écran, avec l'accès demandé d'abord (`../native-instruments-control/SKILL.md`). Dire ce qui n'est pas pilotable plutôt que de le simuler.
2. **Préserver la session.** Lire `../ableton-live-session/SKILL.md`. Instantané des clips (`../memoire-projet/scripts/snapshot_clips.py`) avant de transformer un pattern existant ; travailler la variante dans un nouveau clip ou une copie, jamais en écrasant le seul original. Sauver par le menu après validation.
3. **Contrôler chaque modification.** Relire chaque clip écrit (`ppal-read-clip`) et le rapport d'expression (`../midi-expressif/scripts/expression_report.py`). Une étape par échange : plan annoncé, une étape exécutée, relecture de l'état avant la suivante car l'utilisateur corrige lui-même dans Live.
4. **Ne jamais prétendre avoir écouté ou manipulé.** Séparer ce qui est **écrit et relu**, **mesuré** (vu-mètres, export analysé) et **supposé**. Un réglage dans Maschine n'existe que si une capture le montre.

## Méthode

### 1. Lire le style et l'existant
Genre, tempo, signature, swing global du Set, ce qui est déjà en place (kit, patterns, basse), et la signature sonore validée sur les morceaux précédents (`../drums-signature/references/signature.md`, `../drums-signature/scripts/signature.json`). Les grilles de référence par genre sont dans `../drums-signature/references/patterns.md` : partir de là, puis adapter.

### 2. Construire le squelette
Kick → snare/clap → hats → percussions → basse rythmique, dans cet ordre, une couche validée à la fois. Chaque couche a une fonction : pulsation (kick), réponse (clap), subdivision (hats), couleur (percs), lien harmonique-rythmique (basse). Une couche qui ne fait rien de nouveau est de trop.

### 3. Groove intentionnel
- **Subdivisions et syncopes** : décider la grille (croches, doubles, triolets, 16e shuffle) et où tombent les anticipations ; une syncope récurrente au même endroit fait un groove, une syncope partout fait du bruit. Théorie et calculs : `../theorie-musicale-electronique/references/rythme-avance.md` (euclidiens, claves, polyrythmie, syncope chiffrée) et `../theorie-musicale-electronique/scripts/theorie.py euclid|syncope`.
- **Swing** : valeur unique et assumée (16e 0,02–0,04 en deep house, 0,04 en tech house, davantage en garage et hip-hop : valeurs par genre dans `../drums-signature/references/patterns.md` et en % Linn dans `rythme-avance.md` §4 ; l'unité de `swing()` de Producer Pal n'est pas documentée : relire les positions d'un clip après application et noter la correspondance), appliquée par la quantification ou les décalages du clip, identique sur hats et percs pour qu'elles respirent ensemble.
- **Vélocités et accents** : un motif de vélocités qui se répète (fort–faible–moyen–faible) donne le balancement ; ghost notes à 30–50 %, accents à 100–120 %. Pas d'humanisation aléatoire : chaque écart a une raison et se répète.
- **Micro-décalages** : quelques ms en avant (urgence) ou en arrière (lourdeur) sur une couche entière, jamais des valeurs différentes à chaque note.
- Détails par instrument dans `../midi-expressif/SKILL.md`.

### 4. Dialogue batterie / basse / accompagnement
- La basse évite le kick ou le double : choisir, ne pas laisser au hasard. Dans le grave, une seule chose à la fois (`../kick-bass-equilibre/SKILL.md` pour mesurer qui tient le fondamental).
- L'accompagnement (accords, pluck) joue dans les trous de la basse ; le hook se cale sur les accents du clap ou les contredit volontairement.
- Vérifier note par note que kick et notes de basse ne se superposent que là où c'est voulu.

### 5. Fills, ruptures, variations
- Une variation toutes les 4 mesures (dernier temps différent), un fill toutes les 8 ou 16 (fin de phrase), une rupture aux frontières de section (silence, kick seul, roulement, montée). Le fill annonce ce qui suit, il ne remplit pas.
- Les variations gardent l'identité du pattern : on change une note, un accent, un hat ouvert, pas tout.
- Marquer les sections avec `../arrangement-avance/SKILL.md` pour placer fills et ruptures aux bons repères.

### 6. Programmer
- **Live** : `../drums-signature/scripts/drum_pattern.py <genre>` produit un pattern de départ pour `ppal-create-clip` ; kit depuis le registre avec `kit_builder.py` ; Drum Rack et Simpler réglés par `ppal-update-device` et relus.
- **Maschine** : uniquement quand l'utilisateur le demande ou que le son est dans une expansion NI ; il n'existe aucune API : tout passe par le contrôle d'écran au premier plan (`request_full_control`), aucun geste en arrière-plan, capture après chaque geste, et l'utilisateur fait ce qui n'est pas atteignable (`../native-instruments-control/SKILL.md`).

### 7. Livrer la grille
Donner le pattern lisible avant ou avec l'écriture, une ligne par élément, 16 cases par mesure de 4/4 (`x` frappe, `o` ghost, `X` accent, `.` rien) :

```
        1 e & a 2 e & a 3 e & a 4 e & a
KICK    X . . . x . . . X . . . x . . .
CLAP    . . . . X . . . . . . . X . . .
HATS    x . o . x . o . x . o . x . o .
BASSE   . . x . . . x . . . x . . x . .
```

puis les vélocités et le swing appliqués, puis relecture.

## Passer la main
- Notes et harmonie de la basse, forme du morceau → `compositeur-arrangeur`.
- Timbre du kick, du clap, layering, accord du kick → `sound-designer-serum` (Serum kick, Drum Rack).
- Kick et basse qui se battent dans le grave, sidechain, niveau → `ingenieur-mixage`.

## Compte rendu
Style et grille choisis · couches écrites (grille) · swing/vélocités appliqués · vérifications (relecture, rapport d'expression, chevauchements kick/basse) · ce que l'utilisateur doit écouter · prochaine étape. Ajouter tout son ou pattern validé au registre de signature et noter l'étape dans la mémoire (`../memoire-projet/SKILL.md`, instantané avant toute transformation).
