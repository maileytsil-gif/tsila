# Palette de production et macros

Ces recettes sont des créations de départ fondées sur les fonctions des synthétiseurs, à régler à l'oreille et dans le morceau. Ne pas les attribuer à une vidéo sans transcription ou visionnage. Un rendu professionnel exige édition, resampling, arrangement, gain staging et comparaison dans le contexte; aucun chiffre isolé ne garantit ce rendu.

Pour le kick 808 doux et dur, lire [kick-808-detail.md](kick-808-detail.md) avant de donner un patch prêt à programmer.

## Modèle de livraison pour chaque preset

Écrire source/oscillateurs, registre, enveloppes en ms, filtres, modulation et effets avec leurs quantités, quatre macros nommées et assignées, motif MIDI, BPM/tonalité, variantes soft/hard, contraintes mono, resampling et vérification A/B au niveau égal. Tester chaque macro à 0, 50 et 100 % pour éviter saut de niveau, résonance excessive ou grave instable. Sauver preset sec et version avec effets; noter la version de Serum 2. Une macro peut agir sur plusieurs destinations avec polarités différentes, mais donner chaque plage réelle dans l'interface au moment de programmer.

| Macro type | Cibles suggérées | Usage |
|---|---|---|
| M1 Tone | cutoff + wavetable position ou FM faible | Ouvrir la couleur sans perdre la hauteur |
| M2 Motion | profondeur LFO + vitesse synchronisée si disponible | Varier couplet/réponse; vérifier aux deux BPM |
| M3 Edge | drive + part d'harmoniques/noise | Intensifier sans modifier sub propre |
| M4 Space | send delay/reverb + largeur du mid | Désactiver sur sub/kick; préserver mono |

## Kicks et percussions

| Famille | Sources et gestes | Version douce / dure | Macros utiles |
|---|---|---|---|
| 808 long | Sinusoïde avec enveloppe de hauteur descendante courte vers fondamentale, amplitude 300–900 ms selon espace; petite attaque optionnelle | Douce: moins de click et de drive, tail contrôlée. Dure: click court et saturation parallèle des harmoniques, garder corps propre | Pitch sweep, Tail, Click, Drive |
| Kick house court | Corps sinusoïdal 100–300 ms avec pitch envelope, transient discret; comparer avec DS Kick/Operator | Douce: attaque arrondie. Dure: attaque plus incisive et corps saturé modérément | Attack, Body, Click, Dirt |
| Kick 909 inspiré | Corps et attaque distincts, queue plus courte et accent médium, sans promettre émulation exacte | Soft/hard par équilibre transient, drive et durée, non par volume seul | Punch, Tail, Tone, Drive |
| Snare/clap | Oscillateur accordé bref + noise filtré; doubles couches seulement si chacune ajoute un rôle | Soft: noise sombre et decay court. Hard: transient sec, noise brillant, compression modérée | Snap, Noise, Body, Room |
| Hat/shaker | Noise filtré, enveloppe très courte ou ouverte, vélocité et accents variables | Soft: haut adouci. Hard: transient défini sans dureté continue | Bright, Decay, Grain, Pan/Space |
| Tom/perc FM | Sinus/triangle, pitch bend court, FM modérée; alternance de hauteur | Soft: moins de FM. Hard: attaque plus métallique; vérifier résonances | Pitch, Bend, Metal, Tail |

DS Kick, DS HH, DS Snare, DS Tom et DS FM dans Live offrent une voie native pour tester ces familles (instruments natifs : tolérés par la règle 6 d'`ableton-live-session`, contrairement aux effets natifs). Dans Serum 2, resampler les percussions en one-shots et contrôler les phases/transients à chaque déclenchement ; le kit retenu passe par `../../../producteur-rythmique/modules/drums-signature/GUIDE.md` (`kit_builder.py`, registre de signature) et la relation kick/sub par `../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`.

## Synthés, textures et transitions

| Famille | Recette de départ | Quatre macros spécifiques |
|---|---|---|
| Pluck house | Saw/triangle, filtre passe-bas, enveloppe filtre courte 80–250 ms, sustain faible, release qui laisse respirer; note de tension dans le voicing | Brightness, Decay, Bite, Space |
| Lead chantable | Source saw ou wavetable claire, mono/legato seulement si phrase liée, vibrato retardé, glide rare; préserver consonnes du motif | Color, Glide, Vibrato, Delay |
| Stab chord | 2 oscillateurs et voicing MIDI partiel, enveloppe courte, modulation de cutoff liée aux accents; ne pas empiler l'accord entier en grave | Attack, Filter, Crunch, Width |
| Pad | Deux sources légèrement détunées, attaque 200–1500 ms, release contrôlé, filtre lent et mouvement d'une seule dimension à la fois | Warmth, Motion, Air, Space |
| Drone | Note pédale ou bruit tonal, modulation très lente et spectre évolutif; automatiser tension avant changement d'accord | Root, Texture, Movement, Distance |
| Ambiance | Bruit filtré, enregistrement de terrain autorisé ou granular/sample, réverbération en retour et édition des silences | Texture, Filter, Width, Tail |
| Riser | Noise filtré montant + part tonale avec hauteur/pitch ou wavetable évolutive, automate 4/8/16 mesures; éviter sub continu | Rise, Bright, Tension, Width |
| Impact | Transient bref + corps tonal 100–500 ms + tail spatiale indépendante; imprimer et inverser pour transition | Hit, Body, Crunch, Tail |

## Vérification par style

- Tech house: laisser le riff court et les percussions lisibles; tester suppression d'un coup plutôt qu'ajout de couches.
- House: kick et basse se relayent; pluck/Rhodes porte une réponse de plusieurs mesures.
- Afro house: préciser la référence culturelle/rythmique si empruntée; l'ambiance et les percussions doivent laisser respirer le motif central.
- Bass house: sub stable, mid bass modulée, accents du motif transmis à FM/filtre; retour mono sur chaque note grave.
- Electro house: alternance sections larges et sèches, impacts proportionnés; vérifier que le lead subsiste sans riser.

Sources de fonctions: manuels Xfer Serum 2 et Ableton Live 12; le tutoriel Ableton « Drop It: The Kick in Electronic Music » distingue attaque, corps et queue et fournit des exemples Live; « Pad It Out » détaille les rôles de pads et les oscillateurs/detune. Voir [sources-videos.md](sources-videos.md).
