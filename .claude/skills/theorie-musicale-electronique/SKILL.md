---
name: theorie-musicale-electronique
description: Théorie musicale avancée appliquée à la production électronique, tous genres (house, techno, trance, DnB, dubstep, garage, trap, lo-fi, ambient, synthwave, hardstyle, future bass, afro, reggaeton, IDM…) : modes et gammes, harmonie de boucle, emprunts, médiantes, substitution tritonique, harmonie négative, voicings pour synthés et limites du grave, accordage kick/sub, rythmes euclidiens, claves, polyrythmie, swing chiffré, breakbeats, syncope mesurable, tempos, structures par genre, dispositifs de tension ; script de calcul (gammes, degrés, voicings, euclidiens, syncope, fréquences). Utilise ce skill dès que l'utilisateur pose une question de théorie (« quel mode », « quelle progression », « pourquoi ça sonne faux », « à quel BPM », « combien de mesures »), veut les conventions d'un genre, choisir ou justifier accords, gamme, rythme, structure ou build, ou dit « théorie », « harmonie », « explique-moi » — même hors Ableton. Savoir pour compositeur-arrangeur et producteur-rythmique ; ne pilote pas Live.
---

# Théorie musicale pour la production électronique

Ce skill est le **savoir** ; il ne touche pas au Set. Écrire dans Live relève des rôles `../compositeur-arrangeur/SKILL.md` (notes, forme) et `../producteur-rythmique/SKILL.md` (groove), qui appliquent les règles communes (capacités vérifiées, session préservée, une étape par échange, jamais « entendu » sans mesure). Les samples ont leur théorie propre dans `../sampling-composition-avancee/`.

## Références (charger seulement ce qui sert)

| Fichier | Contenu | Quand |
|---|---|---|
| `references/genres.md` | modes, progressions, basse, lead, particularités par genre | dès qu'un style est nommé ou déductible |
| `references/harmonie-avancee.md` | modes clair→sombre, chromatisme (emprunts, médiantes, tritonique, négative, modulation), harmonie non fonctionnelle, voicings et limites du grave, accordage, mélodie, cadences | choix d'accords, de gamme, de voicing, de hauteur de sub |
| `references/rythme-avance.md` | euclidiens, claves, polyrythmie/polymétrie, swing par genre, breakbeats, grilles par genre, syncope LHL | tout ce qui touche au placement |
| `references/forme-tension.md` | tempos, hypermètre, schémas de structure par genre, dispositifs de tension, développement | structure, build, drop, durée |

`scripts/theorie.py` (Python 3, sans dépendance, C3 = 60) : `gamme`, `modes`, `accord`, `progression` (degrés, voicing le plus lié, notes hors gamme, limites du grave), `transpose`, `inversion`, `negatif`, `euclid`, `syncope`, `freq`, `sub`. Le lancer avant d'affirmer une note ou un degré.

## Méthode : la théorie sert une décision

1. **Situer** : genre ou intention, tempo, tonalité et mode réels (pas supposés), contraintes du projet (mémoire : règle des drops, accord réservé, citation). Lire l'entrée du genre dans `genres.md` : ce que le style fait d'habitude devient le point de départ, jamais une obligation.
2. **Décider le modèle harmonique avant les accords** : combien d'accords dans la boucle (0, 1, 2, 4), pédale ou progression, rythme harmonique (un accord par mesure, par 2, par 8 ou 16), mode et sa note caractéristique. En musique de groove, l'harmonie est optionnelle et statique ; la tension vient souvent du rythme, du timbre et de la forme, pas des cadences.
3. **Choisir l'outil théorique pour l'effet voulu**, un seul à la fois :
   - couleur sans changer de fonction → emprunt modal, sus/add9, planing ;
   - surprise à un point de structure → médiante chromatique, cadence rompue, bII, modulation directe ;
   - lien plus fluide → voice leading parcimonieux, notes communes, substitution tritonique (basse chromatique) ;
   - section B « miroir » → harmonie négative ;
   - flottement → lydien, quartal, pédale ; tension sombre → phrygien, double harmonique, triton ;
   - groove → euclidien tourné, tresillo/clave, syncope moyenne, un seul swing chiffré ;
   - tension de forme → dominante tenue, filtre, roll, coupure, densification (voir le tableau de `forme-tension.md`).
4. **Vérifier avec le script** : degrés et notes hors gamme (`progression`), limites du grave (`accord`, `progression`), hauteur du sub (`sub`, `freq`), indice de syncope (`syncope`), rythme euclidien exact (`euclid`).
5. **Livrer** : la décision, les notes exactes (nom + octave Ableton + MIDI) ou la grille de 16 cases, la raison en une phrase simple (« la sixte majeure du dorien éclaircit le mineur sans le rendre majeur »), et ce qui reste un choix d'oreille de l'utilisateur.

## Règles de fiabilité

- Distinguer **établi** (théorie standard, sources académiques ou manuels), **usage courant** (pratique des producteurs, blogs) et **hypothèse** ; les références marquent « usage » ou « non sourcé » quand c'est le cas.
- Une convention de genre décrit une tendance ; le projet en cours peut la contredire volontairement. Ne pas « corriger » un frottement voulu (b2 en psytrance, triton en dubstep, désaccordage lo-fi).
- Le nom d'un accord n'est pas une preuve : dans un sample ou un stab sans fondamentale, la fonction dépend de la basse réelle.
- Une syncope, un swing ou une modulation se chiffrent ; « un peu plus de groove » n'est pas une instruction.
- Ne jamais présenter A = 432 Hz, l'inévitabilité du V–I ou l'interdiction des quintes parallèles comme des règles en musique électronique.

## Exemples de questions et de réponses attendues

- « Quel mode pour une deep house pas triste ? » → dorien (6te majeure), vamp i7–IV7 en la : Am7–D7, notes de la basse A puis D, hook sur A–E qui passe sur les deux accords ; script `gamme A dorien`.
- « Mon build ne monte pas » → tableau des dispositifs : dominante tenue + passe-haut 30→175 Hz + roll qui double toutes les 4 mesures + deux temps de silence ; vérifier que le grave a bien été retiré avant le drop.
- « Un rythme de hats moins carré à 128 » → E(7,16) tourné de 2, swing 56 %, ouverture sur « e » de 4 ; indice LHL affiché pour rester dans la syncope moyenne.
- « Le kick est-il accordé ? » → `sub F` : F0 = 43,65 Hz pour le sub, kick sur F1 (87,3 Hz) ou C1 (65,4 Hz, quinte) ; mesurer la fondamentale du kick à l'analyseur avant de trancher.

## Sources principales
Open Music Theory · Ethan Hein · Toussaint (rythmes euclidiens) · Butler, *Unlocking the Groove* · DeSantis, *Making Music* (Ableton) · Ableton Learning Music et manuel Live 12 · Tymoczko · Duinker, Biamonte (MTO) · Danielsen (RITMO), Frühauf 2013, Sioros & Guedes 2014 · Attack Magazine (Passing Notes, Beat Dissected, interview Roger Linn) · Wikipedia pour définitions et tempos. Détail et fiabilité par fichier de référence.
