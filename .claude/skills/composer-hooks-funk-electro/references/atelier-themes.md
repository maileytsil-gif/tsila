# Deux thèmes originaux à programmer

Convention 4/4, grille `1 e & a 2 e & a 3 e & a 4 e & a`. `2a` désigne la dernière double croche du temps 2 ; `:2` dure deux doubles croches. **Numérotation Ableton, C3 = 60** (le numéro MIDI fait foi ; en notation scientifique, ajouter 1 à chaque octave). Notes et exemples originaux, pas des transcriptions.

Chaque bloc `grille` ci-dessous est vérifié, depuis le dossier du skill, par `scripts/grille.py --verifier references/*.md` (notes d'accord, tensions résolues, chevauchements) ; `grille.py --fichier references/atelier-themes.md --titre funk` donne le tableau du rôle compositeur-arrangeur et la notation Producer Pal, `--transposer N` le transpose dans la tonalité du Set.

> Corrigé le 29 sept. 2026 par rapport à la version Codex : notes converties de C4 = 60 vers C3 = 60 (écrites telles quelles dans Live, elles sonnaient une octave trop haut) ; le La naturel du lead sur Bb13, présenté comme « tierce majeure », n'appartient pas à l'accord (tierce = Ré ; La = septième majeure, à un demi-ton du Lab et du Sib de l'accord) ; l'accord « A7alt » gardait une quinte juste (Mi) : il est renommé A7(b9,#9).

## Funk house 122 BPM

Accords (fa dorien, i9 – IV13) : m1–2 Fm9 (F Ab C Eb G), m3–4 Bb13 (Bb D F Ab C G). Le lead commence après le temps 1 et garde son rythme quatre mesures. Sur Bb13, il garde le Lab de départ (septième mineure de Bb, note commune) et fait entendre le Ré (tierce de Bb, note caractéristique du dorien) ; la dernière note, Sol (13e), remonte d'un demi-ton vers le Lab de la reprise.

```grille
titre: Funk house 122 BPM — lead et basse
tempo: 122
accords: Fm9 | Fm9 | Bb13 | Bb13
lead: Ab3[1&:2] C4[2a:1] Eb4[3&:2] C4[4&:1] | Ab3[1&:2] C4[2a:1] F4[3&:2] Eb4[4&:1] | Ab3[1&:2] C4[2a:1] D4[3&:2] C4[4&:1] | F4[1&:2] D4[2a:1] C4[3&:2] G3[4&:1]
basse: F0[1:4] C1[2&:1] Eb1[2a:1] F0[3:2] Ab0[3&:1] C1[4&:1] | F0[1:4] C1[2&:1] Eb1[2a:1] F0[3:2] Ab0[3&:1] C1[4&:1] Eb1[4a:1] | Bb0[1:4] F1[2&:1] Ab0[2a:1] Bb0[3:2] D1[3&:1] F1[4&:1] | Bb0[1:4] F1[2&:1] Ab0[2a:1] Bb0[3:2] D1[3&:1] C1[4a:1]
```

| m | Lead note[départ:durée] | Basse note[départ:durée] |
|---|---|---|
| 1 | Ab3[1&:2] C4[2a:1] Eb4[3&:2] C4[4&:1] | F0[1:4] C1[2&:1] Eb1[2a:1] F0[3:2] Ab0[3&:1] C1[4&:1] |
| 2 | Ab3[1&:2] C4[2a:1] F4[3&:2] Eb4[4&:1] | F0[1:4] C1[2&:1] Eb1[2a:1] F0[3:2] Ab0[3&:1] C1[4&:1] Eb1[4a:1] |
| 3 | Ab3[1&:2] C4[2a:1] D4[3&:2] C4[4&:1] | Bb0[1:4] F1[2&:1] Ab0[2a:1] Bb0[3:2] D1[3&:1] F1[4&:1] |
| 4 | F4[1&:2] D4[2a:1] C4[3&:2] G3[4&:1] | Bb0[1:4] F1[2&:1] Ab0[2a:1] Bb0[3:2] D1[3&:1] C1[4a:1] |

Registres (Ableton) : lead Ab3–F4 (MIDI 68–77), dans la zone C3–C5 d'un pluck/lead ; basse F0–F1 (MIDI 29–41, 43,7–87,3 Hz), fondamentale jouable par un sub, harmoniques à ajouter au médium si la basse doit s'entendre sur petit système (`../../kick-bass-equilibre/SKILL.md`).

Laisser basse et lead seuls avant d'ajouter le clav sur les contretemps. Variante B : omettre le sommet en m2 et m4 (F4). Ajuster la note d'approche de basse au retour vers F (le Do de 4a en m4 prépare le Fa), sans glide involontaire. Test de mémorisation : voir la fin de ce fichier.

## Acid jazz / pop 104 BPM

Accords : Dm9 (D F A C E), G13 (G B D F A E), Cmaj9 (C E G B D), A7(b9,#9) (A C# E G Bb C), retour Dm9. Voix supérieure du Rhodes :

```grille
titre: Acid jazz / pop 104 BPM — voix supérieure du Rhodes et réponse de cuivres
tempo: 104
accords: Dm9 | G13 | Cmaj9 | A7b9#9
rhodes: F3[1&:2] A3[2&:2] C4[3a:1] A3[4&:2] | F3[1&:2] B3[2&:2] D4[3a:1] B3[4&:2] | E3[1&:2] G3[2&:2] B3[3a:1] G3[4&:2] | G3[1&:2] C4[2&:2] Bb3[3a:1] E3[4&:2]
cuivres: | A3[3&:1] C4[4:1] D4[4&:1] | | G3[3&:1] E3[4:1] C#3[4&:1]
```

| m | Rhodes note[départ:durée] |
|---|---|
| 1 | F3[1&:2] A3[2&:2] C4[3a:1] A3[4&:2] |
| 2 | F3[1&:2] B3[2&:2] D4[3a:1] B3[4&:2] |
| 3 | E3[1&:2] G3[2&:2] B3[3a:1] G3[4&:2] |
| 4 | G3[1&:2] C4[2&:2] Bb3[3a:1] E3[4&:2] |

Réponse de cuivres en variante : m2 A3[3&:1] C4[4:1] D4[4&:1] (le Do est une note de passage entre la 9e et la quinte de G13), m4 G3[3&:1] E3[4:1] C#3[4&:1] (C#, sensible, prépare le Ré de Dm9). Pour laisser la réponse audible, le Rhodes réduit ces mesures à leurs deux premières attaques :

```grille
titre: Acid jazz / pop 104 BPM — variante B, Rhodes réduit sous les cuivres
tempo: 104
accords: Dm9 | G13 | Cmaj9 | A7b9#9
rhodes: F3[1&:2] A3[2&:2] C4[3a:1] A3[4&:2] | F3[1&:2] B3[2&:2] | E3[1&:2] G3[2&:2] B3[3a:1] G3[4&:2] | G3[1&:2] C4[2&:2]
cuivres: | A3[3&:1] C4[4:1] D4[4&:1] | | G3[3&:1] E3[4:1] C#3[4&:1]
```

Bb est b9 de A7, Do est #9 ; le Mi final du Rhodes (quinte juste de A7) monte d'un demi-ton vers le Fa de Dm9. Ajouter les voicings sous la voix supérieure seulement après que celle-ci reste identifiable (`../../theorie-musicale-electronique/scripts/theorie.py progression "Dm9 G13 Cmaj9 A7b9#9" --tonalite "D mineur"` pour le voicing lié et les limites du grave).

## Test de mémorisation (à faire par l'utilisateur)

Claude n'entend pas le Set : ces tests reviennent à l'utilisateur, Claude livre les contrôles mesurables (`grille.py`, relecture du clip, `check_scale.py`). Après une écoute, chanter le motif seul ; après dix minutes, noter son silence initial et son sommet. Comparer trois variantes dont une déplace les attaques. Si le motif est confondu, retirer des notes ou renforcer la réponse. Ce test est une heuristique, pas une garantie de succès.
