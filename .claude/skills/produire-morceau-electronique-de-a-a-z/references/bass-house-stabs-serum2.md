# Stabs House dans Serum 2, sans Basic Shapes

Références Xfer Records : [sélection des tables](https://xferrecords.com/web-manual/serum-2/choosing-oscillator-or-filter-options), [routage des oscillateurs](https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter), [modes Warp](https://xferrecords.com/manual/serum-2/docs), [modulation des commandes](https://xferrecords.com/web-manual/serum-2/using-knobs-and-sliders). Les catégories **Analog, Digital, S2 Tables, Spectral, Vowel** sont visibles dans le sélecteur. Les noms individuels varient avec bibliothèque/version : spécifier catégorie + caractère et auditionner plusieurs tables. Réglages ci-dessous = points de départ personnels, pas valeurs prescrites par Xfer.

## Démarrage commun

Partir de `- Init -`. Dans OSC A choisir Wavetable et une table de la catégorie proposée, jamais Basic Shapes/Default Shapes. Activer FILTER 1; contrôler le routage OSC A → FILTER 1 (le filtre peut être désactivé sur le preset initial). ENV 1 règle la durée audible; ENV 2 modulera le cutoff. Dans Serum 2, le routage **Direct** contourne filtre et effets : ne pas l'utiliser sur une couche censée être filtrée. Écouter sur une note médium avant de programmer l'accord.

| Patch | Oscillateurs et filtre | ENV 1 (A/D/S/R) | ENV 2 → cutoff et traitement |
|---|---|---|---|
| **Organ chord sec** | OSC A catégorie Analog, choisir table à harmoniques régulières; WT POS à l'oreille, Unison 1–2. FILTER 1 LP 12, cutoff médium. | 3 ms / 180 ms / 0–15 % / 90 ms | ENV 2 : 0 / 120 ms / 0 / 70 ms, plage positive modérée; Saturation douce, petite room sur retour. Chord Fm7 sans F grave : Ab3 C4 Eb4. |
| **Vowel stab « wah »** | OSC A catégorie Vowel, choisir table dont les positions contrastent; Unison 1. FILTER 1 BP, résonance prudente. | 2 ms / 220 ms / 0 / 80 ms | ENV 2 : 0 / 160 ms / 0 / 60 ms sur WT POS et cutoff, mouvements de sens ou profondeur différents; distorsion légère. Tester Ab3–C4 au contretemps puis écouter en mono. |
| **Metallic / robot** | OSC A catégorie Digital ou Spectral (table wavetable, pas oscillateur de synthèse Spectral); Unison 1. Tester Warp Sync ou FM à faible profondeur. FILTER 1 BP ou LP 24. | 0–3 ms / 130 ms / 0 / 70 ms | ENV 2 : 0 / 90 ms / 0 / 40 ms sur cutoff et Warp, faible plage. EQ après distorsion si les aigus sifflent; pour un hit vraiment métallique, jouer une seule note puis resampler. |
| **Warm disco / piano-like** | OSC A catégorie S2 Tables ou Analog, choisir une table douce mais riche; OSC B optionnel, table contrastée à -12 dB environ, routée aussi au filtre. FILTER 1 LP 24. | 4 ms / 280 ms / 10–25 % / 150 ms | ENV 2 : 0 / 190 ms / 0 / 80 ms sur cutoff. Chorus discret puis delay filtré en retour; accord Fm9 sans fondamentale : Ab3 C4 Eb4 G4. |
| **Rave sync stab** | OSC A catégorie Analog ou Digital, table riche; Warp Sync en montant doucement jusqu'à l'attaque désirée. FILTER 1 LP ou BP selon couleur. | 0–3 ms / 120–200 ms / 0 / 60 ms | ENV 2 courte sur Warp et cutoff; automate la quantité de Warp aux fins de phrases. Une seule triade brève suffit avant le drop. |

## MIDI et arrangement

À 126 BPM, essayer kick sur 1, 5, 9, 13 de la grille 1/16; stab sur 3 et 11 pour les contretemps, puis déplacer le second à 12 si le groove le réclame. Longueur MIDI initiale 1/16–1/8; la queue réelle dépend de ENV 1 et des effets. Accentuer la première vélocité et diminuer la seconde. Tester d'abord une seule recette dans le break puis une version raccourcie dans le drop. Si la fondamentale du stab se bat avec la basse, enlever la fondamentale de l'accord ou monter l'octave.

## Diagnostic

- Si le filtre ne répond pas, vérifier FILTER 1 activé et route OSC A → FILTER 1 avant d'augmenter ENV 2.
- Si le stab reste continu, raccourcir ENV 1 et vérifier les retours delay/reverb. ENV 2 seule ne coupe pas le volume.
- Si « wah » ne parle pas, essayer une autre position/table Vowel avant de multiplier les effets; garder la modulation formant distincte de l'amplitude.
- Si l'accord brouille le kick/sub, réduire la durée et le niveau avant EQ/sidechain. Comparer l'attaque à volume égal avec et sans saturation.
