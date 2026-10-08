# Motifs MIDI de départ par famille

Exercices originaux, **numérotation Ableton C3 = 60** (le numéro MIDI fait foi ; F0 = MIDI 29 = 43,7 Hz, E0 = 41,2 Hz). Notation de grille du skill `composer-hooks-funk-electro` : position `1 e & a 2 e & a…`, durée en doubles croches, `|` entre mesures. Chaque bloc est vérifié par `../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/motifs.md` (depuis ce dossier de skill) ; `grille.py --fichier references/motifs.md --titre growl --format ppal` donne la notation Producer Pal, `--transposer N` la tonalité du Set.

Kick supposé sur les quatre temps (doubles croches 1, 5, 9, 13) : aucune attaque des motifs House ne tombe sur ces cases ; les tenues qui les recouvrent demandent un ducking ou un sidechain réglé sur les vrais coups de kick (`tempo-mix.md`, `../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`). Le sub joue la même ligne une octave sous la couche mid, sur une piste séparée dès que la couche mid est modulée (`families.md`, `tempo-mix.md`). Recomposer autour du vrai pattern de batterie du morceau, surtout en DnB.

## Bass House 128 BPM, Fa mineur — growl en réponse (familles 1 + 8)

Reprend l'exercice de `../bass-house-sound-design/references/recettes.md` (écrit à 126 BPM ; 128 est le tempo Bass House le plus courant documenté) : stab Ab–C–Eb sur les doubles croches 3 et 11, réponse de growl sur 7 et 15 plus une anacrouse sur 16, le reste vide.

```grille
titre: Bass House 128 — stab et growl en réponse, sub séparé
tempo: 128
accords: Fm7 | Fm7
stab: Ab3+C4+Eb4[1&:1] Ab3+C4+Eb4[3&:1] | Ab3+C4+Eb4[1&:1] Ab3+C4+Eb4[3a:1]
growl: F1[2&:2] F1[4&:1] Ab1[4a:1] | F1[2&:2] Eb1[4&:2]
sub: F0[2&:2] F0[4&:1] Ab0[4a:1] | F0[2&:2] Eb0[4&:2]
```

La seconde mesure déplace le deuxième stab d'une double croche (variante de l'exercice) et finit sur la septième (Eb) pour relancer la boucle.

## Bass House 128 BPM — wub en demi-mesures (famille 7)

```grille
titre: Bass House 128 — wub tenu après le kick
tempo: 128
accords: Fm7 | Fm7
wub: F1[1&:6] Ab1[3&:6] | F1[1&:6] Eb1[3&:2] F1[4&:2]
sub: F0[1&:6] Ab0[3&:6] | F0[1&:6] Eb0[3&:2] F0[4&:2]
```

LFO du filtre en 1/8 synchronisé et redémarré à chaque note : chaque tenue de six doubles croches porte trois « wub » identiques. Comparer 1/8 pointée et 1/16 sur la dernière note seulement.

## Bass House 128 BPM — donk syncopé (famille 9)

```grille
titre: Bass House 128 — donk en contretemps
tempo: 128
accords: Fm7 | Fm7
donk: F1[1&:1] F1[1a:1] F2[2&:1] F1[3&:1] F1[3a:1] Ab1[4&:1] C2[4a:1] | F1[1&:1] F1[1a:1] F2[2&:1] Eb2[3&:1] C2[3a:1] Ab1[4&:1] F1[4a:1]
```

Sub facultatif et sans excursion de pitch : le donk se suffit souvent au-dessus d'un kick long. Si un sub est ajouté, il ne suit que les fondamentales (F0) en contretemps.

## Future House 126 BPM, mi mineur — pluck / hollow en octaves (familles 1 + 2 ou 3)

Progression i–v–VI–VII (Em – Bm – C – D), exemple documenté dans `../../../references/patches-genres.md` § Future house.

```grille
titre: Future House 126 — pluck en octaves sur les contretemps, sub séparé
tempo: 126
accords: Em | Bm | C | D
pluck: E1[1&:1] E2[2&:1] E1[3&:1] E2[4&:1] | B0[1&:1] B1[2&:1] B0[3&:1] B1[4&:1] | C1[1&:1] C2[2&:1] C1[3&:1] C2[4&:1] | D1[1&:1] D2[2&:1] D1[3&:1] F#1[4&:1] D2[4a:1]
sub: E0[1&:2] E0[2&:2] E0[3&:2] E0[4&:2] | B0[1&:2] B0[2&:2] B0[3&:2] B0[4&:2] | C1[1&:2] C1[2&:2] C1[3&:2] C1[4&:2] | D1[1&:2] D1[2&:2] D1[3&:2] D1[4&:2]
```

Sub de E0 (41,2 Hz) à D1 (73,4 Hz) : le Si reste en B0 (61,7 Hz) plutôt que B-1 (30,9 Hz), inaudible sur la plupart des systèmes. Le rebond vient du LFO du filtre en 1/8 triolet (patch Attack Magazine de `patches-genres.md`), pas de notes supplémentaires.

## DnB 174 BPM — Reese long (famille 6), à recomposer sur le break

```grille
titre: DnB 174 — Reese long avec trous
tempo: 174
accords: Fm7 | Fm7
reese: F1[1:10] Ab1[3a:3] | F1[1:6] Eb1[2&:4] C1[4:4]
sub: F0[1:10] Ab0[3a:3] | F0[1:6] Eb0[2&:4] C0[4:4]
```

Tenues longues et trous d'une double croche ; ne pas accélérer un motif House. Le sub C0 (32,7 Hz) est à la limite basse : le remonter en C1 si le système ou le kick ne le portent pas.
