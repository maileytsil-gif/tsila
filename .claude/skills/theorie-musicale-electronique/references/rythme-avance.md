# Rythme et groove : théorie appliquée au séquenceur

Notation : grille de 16 doubles-croches par mesure de 4/4, `x` attaque, `.` silence, `|` tous les 4 pas. « et » de N = case 4N−1. `scripts/theorie.py euclid k n [rotation]` génère les rythmes euclidiens ; `theorie.py syncope "<grille>"` mesure la syncope.

## 1. Rythmes euclidiens (Toussaint 2005)

E(k,n) répartit k attaques sur n pas aussi uniformément que possible (algorithme de Bjorklund = algorithme d'Euclide). Beaucoup de rythmes traditionnels sont des rotations d'un rythme euclidien ; Butler les appelle « rythmes diatoniques » (impair sur pair). Une rotation change le temps fort perçu sans changer le collier.

| E(k,n) | Motif | Nom |
|---|---|---|
| E(3,8) | `x . . x . . x .` | **tresillo** (3-3-2) |
| E(5,8) | `x . x x . x x .` | **cinquillo** ; rotation = tango |
| E(3,4) | `x . x x` | cumbia, calypso |
| E(2,5) | `x . x . .` | Khafif-e-ramal ; démarré sur la 2e attaque = « Take Five » |
| E(3,7) | `x . x . x . .` | ruchenitza ; « Money » |
| E(4,9) | `x . x . x . x . .` | aksak turc |
| E(4,12) | `x . . x . . x . . x . .` | fandango 12/8 |
| E(5,12) | `x . . x . x . . x . x .` | venda (Afrique du Sud) |
| E(5,16) | `x . . x . . x . . x . . x . . .` | collier bossa-nova (bossa réelle = 3e attaque : `x . . x . . x . . . x . . x . .`) |
| E(7,12) | `x . x x . x . x x . x .` | bell pattern ouest-africain |
| E(7,16) | `x . . x . x . x . . x . x . x .` | collier samba (samba réelle = dernière attaque : `x . x . . x . x . x . . x . x .`) |
| E(9,16) | `x . x x . x . x . x x . x . x .` | Centrafrique ; rotation = cloche de samba |

Usage : hats et percussions (E(5,16), E(7,16) tournés), basses (E(3,8) = tresillo, base du dembow, du footwork, de la bass house), kicks brisés (E(3,8), E(5,16) sur deux mesures), polymètres par superposition de E(k,n) de longueurs différentes.

## 2. Claves et cellules afro-cubaines (16 cases)

| Cellule | Grille |
|---|---|
| Tresillo | `x . . . \| . . x . \| . . . . \| x . . .` (1, 7, 13) |
| Cinquillo (8) | `x . x x . x x .` |
| Habanera (8) | `x . . x x . x .` |
| Clave son 3-2 | `x . . x \| . . x . \|\| . . x . \| x . . .` |
| Clave son 2-3 | mesures inversées |
| Clave rumba 3-2 | `x . . x \| . . . x \|\| . . x . \| x . . .` (3e coup retardé) |
| Bossa-nova | `x . . x \| . . x . \|\| . . x . \| . x . .` |
| Bell pattern (4/4 binaire) | `x . . x \| . . x x \|\| . . x . \| x . . x` ; en 12/8 : `x . x . x x . x . x . x` |
| Dembow (reggaeton) | K `x . . . x . . . x . . . x . . .` S `. . . x . . x . . . . x . . x .` (snare 4, 7, 12, 15 = tresillo décalé) |

Le côté 3 est fort (antécédent), le côté 2 faible (conséquent) ; le tresillo est la première mesure de la clave son.

## 3. Polyrythmie, polymétrie, cycles asynchrones

- **Polyrythmie** : deux subdivisions dans la même mesure, temps forts alignés (3:2, 4:3, 5:4) ; cycle au PPCM (5:4 → 20 pas). Dans le séquenceur : 3 notes de 4/3 temps (grille 1/8T, une note toutes les deux croches de triolet) ; quintolet = notes de 0,8 temps.
- **Polymétrie** : même pulsation, mesures de longueurs différentes (4 mesures de 7/4 = 7 mesures de 4/4) ; les barres se réalignent au PPCM. Dans Live : clips de longueurs différentes (5 doubles contre 16 → réalignement à 80 doubles = 5 mesures).
- **Cycles asynchrones** (DeSantis) : plusieurs boucles de longueurs premières entre elles dérivent au maximum ; prévoir leur réinitialisation aux repères ou laisser la dérive comme processus (ambient, Berlin school).
- **Hémiole** : 3:2 vertical ou horizontal (6/8 → 3/4, accents 3+3+2+2+2). Krebs : dissonance de groupement (hémiole) vs de déplacement (même groupement, décalé).
- **Groupement additif** : 3+3+2 croches (tresillo), 3+3+3+3+4 doubles, 2+2+3 en 7/8 ; garde le 4/4 tout en déplaçant les accents.
- **Tuplets** : a:b = a notes dans la durée de b (3:2, 5:4, 7:4) ; dans Live grille triolet ou longueur de note calculée.

## 4. Swing et microtiming

- **Définition (Roger Linn, MPC)** : rapport entre la 1re et la 2e double-croche de chaque croche. 50 % = droit ; 66 % = triolet ; 54 % desserre sans « sonner swing » ; à 90 BPM, 62 % est plus relâché que 66 % ; plage utile 50–70 %. Convention Cubase/FL : 0 % = droit, 100 % ≈ 66 % Linn.
- **Valeurs par genre (Attack)** : techno 50–60 % · broken house 50 % (le groove vient des placements) · DnB 50–60 % · garage shuffle et 2-step 60–65 %, UK garage « MPC 16 swing 68–69 » · hip-hop / R&B 808 : 54–66 %, jusqu'à 70 · jazz : ratio long/court 1:1 à 3:1, plus large aux tempos lents.
- **Groove Pool de Live** : Base (résolution), Quantize, Timing (intensité du décalage), Random (jitter différent par voix), Velocity (−100…+100), Global Amount jusqu'à 130 % ; grooves « MPC 16 Swing-50…75 » fournis ; extraction depuis n'importe quel clip. Un seul swing pour hats et percussions, sinon elles ne respirent pas ensemble.
- **Laid-back / pushed** (Danielsen) : les batteurs experts jouent de façon reproductible en retard ou en avance de la pulsation, et frappent la caisse claire plus fort en laid-back ; la pulsation interne est une **zone** (beat bin), pas un point. Déviations typiques 0–50 ms. Frühauf 2013 : les décalages en avance sont jugés pires qu'en retard, et pires sur la caisse claire que sur le kick. Règle : décaler une couche entière de quelques ms, jamais des valeurs aléatoires par note (c'est du bruit, pas du groove).
- **Turning the beat around** (Butler) : contredire une pulsation établie (kick déplacé, boucle démarrée hors temps) puis la rétablir : outil de transition.

## 5. Breakbeats

**Amen** (The Winstons 1969, ≈ 136 BPM, 4 mesures) :
```
Mes. 1-2  K: x . x . | . . . . | . . x x | . . . .      S: . . . . | x . . x | . x . . | x . . g
Mes. 3    K: x . x . | . . . . | . . x . | . . . .      S: . . . . | x . . x | . x . . | . . x g
Mes. 4    K: . . x . | . . . . | . . x x | . . . .      S: . x . . | x . . x | . x . . | . . x .   + crash case 11
```
Ride en croches. Ce qui groove : la caisse claire du 4e temps repoussée sur le « et » de 4 en mesures 3–4, les pickups en doubles, et le fait que presque rien n'est exactement sur la grille. Le timbre compte autant que le placement.

**Funky Drummer** (Clyde Stubblefield) : hats en doubles continues, ouvertures sur « e » de 2 et « e » de 4, snare 2 et 4, ghosts entre (la plus dure sur « a » de 3) ; quantisé, « ça n'a plus la même force ». **Think** (Lyn Collins), **Apache** (Incredible Bongo Band) : mêmes principes, grilles à relever sur le sample.

**Half-time / double-time** : le tempo ne change pas, le ressenti est divisé ou multiplié par deux. Dubstep 140 → snare sur le 3 → ressenti 70 ; trap 140/70 avec hats en doubles, triolets, roulements de 32e ; DnB 174 → ressenti 87 ; alterner full-time et half-time est une transition en soi (footwork, DnB).

## 6. Grilles par genre

```
Four-on-the-floor       K x...x...x...x...   C ....x.......x...   H(off) ..x...x...x...x.
UK garage 2-step        K x.........x.....   S ....x.......x...   swing 65–69, hats shuffle, ghosts
DnB two-step (174)      K x.........x.....   S ....x.......x...   + break haché, ghosts, ride
Dubstep (140)           K x... libre, syncopes en fin de mesure   S ........x.......
Trap (140/70)           808 sur 1 + figures ; S/C ........x.......  hats 8e→16e→triolets→32e
Reggaeton / dembow      K x...x...x...x...   S ...x..x....x..x.
Techno (130–135)        K x...x...x...x...   snare hors 2/4 qui remplit entre les kicks, tom case 15, hats E(k,16) tournés
Broken beat             K x sur 1 + contretemps ; snap 2 et 4 ; hats médium moteurs
Footwork (160)          kicks « beat-skipping » (tresillo), sub, alternance full/half-time
Amapiano (112)          log drum en syncopes E(3,8)/E(5,16), shakers en doubles, kick discret
```
UK garage = house sans les kicks 2 et 4 ; house et rock partagent les mêmes patterns, seuls le tempo et les hats diffèrent.

## 7. Syncope mesurable (Longuet-Higgins & Lee 1984)

Poids métriques sur 16 cases : case 1 → 0 ; case 9 → −1 ; cases 5, 13 → −2 ; cases 3, 7, 11, 15 → −3 ; cases paires → −4. Une note sur une position faible **non suivie** d'une attaque sur la position plus forte suivante (silence ou liaison) est une syncope ; son score = différence de poids ; l'indice = somme. Four-on-the-floor = 0 ; tresillo = 4. Une syncope modérée maximise l'envie de bouger (Witek 2017) : viser le milieu, pas le maximum. **Anticipation** : la note syncopée appartient au temps fort suivant, jouée en avance (basse cubaine sur « 2 et » et « 4 »). **Hypermètre** : les mesures deviennent des temps ; hypermesures de 4 = norme ; rompre l'unité de 4 (phrase de 6, 10) est une dissonance hypermétrique utile pour surprendre.

## Sources
Toussaint, *The Euclidean Algorithm Generates Traditional Musical Rhythms* (cgm.cs.mcgill.ca/~godfried/publications/banff.pdf) · Wikipedia (Euclidean rhythm, Clave, Tresillo, Cinquillo, Habanera, Bell pattern, Polyrhythm, Polymeter, Hemiola, Tuplet, Hypermeter, Syncopation, Amen break, Funky Drummer, Half-time, Turning the beat around) · Ethan Hein (polymeter vs polyrhythm ; building the Amen break ; building the Funky Drummer) · Ableton Making Music (asynchronous loops), Learning Music (backbeats, rock and house), manuel Live 12 (Using Grooves) · Attack Magazine (interview Roger Linn ; DAW & drum machine swing ; Beat Dissected : UK garage, rolling 2-step, garage shuffle, raw D&B, mystik dubstep, thumping techno, broken house, 808 R&B, UK drill) · Danielsen / RITMO (beat bin, laid-back) · Frühauf, Kopiez & Platz 2013 · Sioros & Guedes 2014, Sioros ISMIR 2019 (LHL) · Biamonte MTO 20.2 · Butler 2006 · MusicRadar (Amen, reggaeton) · DrumsTheWord (Amen, Funky Drummer).
