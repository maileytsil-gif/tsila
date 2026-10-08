# Deux kicks 808 entièrement spécifiés comme points de départ

Serum 2 init. Adapter les noms de paramètres à l'interface installée. Faire une note MIDI assez longue pour que la queue ne soit pas coupée. Les fréquences sont à régler selon le morceau; aucune fréquence de kick n'est universelle.

## Velours

- OSC A: sinusoïde, une voix, niveau plein, sortie directe; B/C/N coupés. Note de test F0 en numérotation Ableton (MIDI 29, 43,65 Hz ; « F1 » en notation scientifique) puis toutes les notes réelles de la ligne ; table kick/sub d'une tonique : `../../theorie-musicale-electronique/scripts/theorie.py sub F`.
- ENV1 volume: attaque 3 ms, decay 650 ms, sustain 0 %, release 80 ms. Courbe de decay légèrement arrondie; éviter clic de départ.
- ENV2 pitch OSC A: départ environ +24 demi-tons, retour à 0 en 35–55 ms, sustain 0. Dessiner chute rapide au début puis ralentissement. Vérifier que l'assignation n'ajoute pas +24 demi-tons au repos.
- Saturation après synthèse: parallèle sur copie high-pass si besoin de traduction sur petit haut-parleur; garder sinus principal propre.
- M1 Drop: quantité ENV2 de +12 à +36 demi-tons; M2 Body: ENV1 decay 300–850 ms; M3 Harmonics: niveau de copie saturée 0–20 %; M4 Tail: release 30–140 ms. Choisir dans l'interface la polarité et le minimum exacts, puis vérifier la hauteur au repos.

## Mordant

- Garder le corps ci-dessus, ENV1 decay 350–650 ms selon distance entre kicks.
- N: court click/noise filtré passe-haut, enveloppe séparée attaque 0–1 ms, decay 4–12 ms, sustain 0; écouter sa polarité et son alignement avec OSC A.
- Distorsion légère sur couche médium seulement ou resampling parallèle; volume égal à la version velours pour comparaison.
- M1 Click: niveau N de 0 à discret mais audible; M2 Drive: saturation parallèle 0–25 %; M3 Punch: ENV2 durée 25–65 ms; M4 Tail: ENV1 decay 250–700 ms. Tester les extrêmes à chaque hauteur jouée.

## Validation

Exporter un one-shot avec début à zéro exact et fin sans rupture; comparer attaque/corps/queue séparément. Observer la fondamentale avec analyseur, contrôler polarité/phase avec basse, écouter en mono et sur petit système, puis replacer dans la boucle. Si kick et sub ne se répartissent pas dans le temps, raccourcir la queue ou le pattern avant d'augmenter le sidechain. Ces valeurs sont des hypothèses de synthèse et non une transcription d'une vidéo.

Dans ce workflow : réglage dans Serum 2 par `../../../sound-designer-serum/SKILL.md` → `../../../sound-designer-serum/modules/vst-sound-design/GUIDE.md` (chargement sans hot-swap, tableau paramètre / valeur / preuve) ; rôle kick/sub, accord et phase mesurés par `../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md` ; one-shot imprimé par `../../../sound-designer-serum/modules/resampling/GUIDE.md` ; kick validé inscrit au registre de signature de `../../../producteur-rythmique/modules/drums-signature/GUIDE.md` pour le retrouver sur le morceau suivant.
