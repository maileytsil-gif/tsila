# Conventions et exemples

## Notation sans ambiguïté

- Employer Do=C, Ré=D, Mi=E, Fa=F, Sol=G, La=A, Si=B ; expliciter les altérations.
- Employer la numérotation Ableton C3 = 60 (convention du dépôt) ; le numéro MIDI fait foi. Une note écrite en notation scientifique (C4 = 60) se convertit : octave Ableton = octave scientifique − 1 (`grille.py --source scientifique`).
- Employer des positions `mesure|temps` depuis 1|1 (notation Producer Pal, sortie de `grille.py`) pour les données programmables. En 4/4, les mesures commencent à 1|1, 2|1, 3|1, 4|1 ; une position p en noires depuis zéro devient mesure 1 + p // 4, temps 1 + p % 4.
- Expliciter la convention des degrés. Dans les exemples mineurs ci-dessous, III, VI et VII désignent les accords diatoniques du mineur naturel ; dans une convention relative au majeur ils s'écriraient ♭III, ♭VI et ♭VII.

## Exemple harmonique original en fa mineur

Ne pas attribuer cet exemple à Beethoven. Prendre 124 BPM, 4/4, quatre mesures, un accord par mesure.

Fa mineur naturel : F, G, A♭, B♭, C, D♭, E♭.

| Mesure | Début | Accord / degré | Voix supérieures (C3 = 60) | MIDI | Basse MIDI | Durée en noires |
|---|---:|---|---|---|---:|---:|
| 1 | 1\|1 | Fm / i | A♭2 C3 F3 | 56 60 65 | 41 (F1) | 4 |
| 2 | 2\|1 | D♭ / VI | A♭2 D♭3 F3 | 56 61 65 | 37 (D♭1) | 4 |
| 3 | 3\|1 | A♭ / III | A♭2 C3 E♭3 | 56 60 63 | 44 (A♭1) | 4 |
| 4 | 4\|1 | E♭ / VII | G2 B♭2 E♭3 | 55 58 63 | 39 (E♭1) | 4 |

Expliquer les notes communes et les petits déplacements dans les voix supérieures. Présenter cette progression comme une option accessible, non comme une formule obligatoire.

Pour une résolution plus marquée, remplacer la dernière mesure par C majeur (G2 C3 E3 = 55 60 64, basse C1 = 36), puis revenir à Fm. Expliquer E naturel comme sensible issue du mineur harmonique, extérieure au mineur naturel. Ne pas qualifier C majeur de diatonique au mineur naturel.

## Motif et variation

Proposer un motif original d'une mesure sur Fm : positions 1|1, 1|1.75, 1|2.5, 1|3.5 ; durées en noires 0.5, 0.25, 0.5, 1 ; notes F3, A♭3, C4, A♭3 (MIDI 65, 68, 72, 68). Laisser le dernier demi-temps libre. Expliquer que les départs hors temps créent de la syncope selon les accents.

Préserver le rythme pour identifier le motif sur les accords suivants, puis adapter certaines hauteurs aux notes d'accord. Ne pas recopier aveuglément les hauteurs sous toute nouvelle harmonie.

## Drop sur une note

Si le brief impose une basse F répétée, conserver sa hauteur et développer d'abord rythme, silences et registre des autres parties. Sous D♭ majeur, F est la tierce ; sous E♭ majeur, F crée une tension de neuvième. Évaluer la durée et le registre de ce frottement. Ne pas affirmer que toute combinaison est consonante parce que ses notes appartiennent à la même gamme.

Si le changement d'accord doit intervenir à la fin de chaque moitié d'un drop de 16 mesures, situer explicitement les changements aux mesures 8 et 16, sous réserve de la formulation exacte du brief. Distinguer changement d'accord, changement de note de basse et variation de timbre.

## Contrôle avant livraison

1. Recalculer les intervalles et les notes des accords ; vérifier les emprunts annoncés.
2. Vérifier la correspondance entre noms, octaves et numéros MIDI.
3. Vérifier que chaque événement reste dans la longueur prévue, sauf débordement intentionnel annoncé.
4. Vérifier collisions, doublons et raccord entre dernière et première mesure ; distinguer polyphonie voulue et chevauchement accidentel.
5. Vérifier les contraintes exactes : note fixe, nombre de mesures, placement des changements et variation finale.
6. Séparer faits musicaux, choix esthétiques et hypothèses d'écoute.
7. Pour l'apprentissage, relier explication, exemple et exercice à la même notion ; attendre la réponse avant de la corriger.
