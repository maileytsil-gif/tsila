# Sampling dans Serum : synthèse de 30 tutoriels

Cette page résume `tutoriels-sampling-serum.md` (SE-01 à SE-30). L'étude a été faite le 05/10/2026 dans Claude in Chrome sur le Mac, son coupé. Pour chaque vidéo, la transcription YouTube et la description ont été lues. Rien n'a été entendu : un effet sonore cité ici est ce que dit le présentateur, jamais une écoute. [SOURCE SE-xx] = c'est dit dans la vidéo. (interp.) = interprétation de cette synthèse. [ASR ?] = passage douteux de la reconnaissance vocale. 23 vidéos portent sur Serum 2 (SE-01 à SE-23), 7 sur Serum 1 (SE-24 à SE-30). Les noms de contrôle ont été comparés à `serum2-cartographie.md` (§ 3.3 à 3.6, § 3.8, § 10). Chaque écart est signalé.

## Ce que dit le corpus avant tout

- **Un sample, trois moteurs.** Sample, Granular et Spectral lisent le même fichier. Passer de l'un à l'autre garde le sample et son découpage [SOURCE SE-04, SE-05]. La cartographie le confirme (§ 3.3).
- **Breaks : la chaîne est toujours la même.** Slice Auto, seuil, Send to Selected Clip, pattern dans le Clip, puis Tailed, Scan et Relative Loop pour le stutter [SOURCE SE-02, SE-03, SE-07, SE-08].
- **Scan ne fait pas la même chose partout.** En Sample, il change la vitesse, donc la hauteur [SOURCE SE-03, SE-04]. En Granular et en Spectral, il change la vitesse à hauteur constante [SOURCE SE-13, SE-19].
- **Basse tirée d'un sample : le sub reste à part.** Les deux recettes de basse dubstep posent un sub sinus sur un oscillateur et le sample en Spectral sur un autre [SOURCE SE-20, SE-21]. (interp.) C'est compatible avec la règle du projet : sub et basse médium séparés.
- **Serum 1 n'a pas de moteur Sample.** On importe l'audio en wavetable, ou on charge le sample dans le noise oscillator [SOURCE SE-24 à SE-29]. Le resampling interne passe par le menu [SOURCE SE-30].

## Gestes de base par moteur

| Moteur | Geste | Comment | Sources |
|---|---|---|---|
| Sample | Charger | En-tête de l'osc › Sample, ou glisser-déposer. Dossiers factory et « Factory Non-Tonal ». Une wavetable se charge aussi comme sample. Un MP3 ne marche pas. | SE-01, SE-05, SE-17 |
| Sample | Boucler | One-shot par défaut. Forward loop ou forward-reverse ; crossfade monté contre le clic. | SE-01 |
| Sample | Slice auto | Clic droit sur la forme d'onde › Slice Auto. Ligne jaune du seuil : plus haut, moins de slices. Première slice sur C1. | SE-03, SE-04, SE-06, SE-17 |
| Sample | Slice manuel | Slice Manual, puis déplacer les marqueurs. Alt+clic ajoute ou retire une slice. Snap to Zero, Snap to Beats. | SE-03, SE-06, SE-07 |
| Sample | Note racine, options | Clic droit › Root Note (C1 → C2). Play Slice to End, Play Single Slice. | SE-01, SE-04 |
| Sample | Tailed | Menu de boucle › Tailed, pour les slices pitchées vers le haut ou un break ralenti. **Écart** : la cartographie dit que Tailed boucle la queue (moitié → fin du sample) pendant la décroissance, comme SE-19 ; « une queue par slice » est la lecture de SE-03 (interp.). | SE-03, SE-07, SE-08, SE-19 |
| Sample | Scan | Vitesse et sens : 100 = normal, négatif = reverse. Range jusqu'à 800 % au clic droit. Pitch bend → scan par la matrice. **Écart** : SE-02 dit que Scan time-stretche chaque slice sans changer le timing ; SE-03, SE-04 et la cartographie disent vitesse donc hauteur. | SE-02, SE-03, SE-07, SE-08 |
| Sample | Stutter | Forward loop + Relative Loop, puis LE réduit sur une macro ; LFO sur loop end. **Écart** : SE-03 lit LE comme « loop length » ; la cartographie et SE-02 : LE = Loop End. | SE-02, SE-03 |
| Clip | Envoyer les slices | Clic droit › Send to Selected Clip. Le break doit faire un nombre exact de mesures. | SE-04, SE-07, SE-08 |
| Clip | Jouer le pattern | Dessiner, Ctrl/Cmd+D, Retrig ON, Launch Quantize 1/8, Edit All, Trigger Mode Mono. | SE-07, SE-08 |
| Clip | Modes | Random (tranche 1/8), Random no duplicates, Random start. **Écart** : SE-07 cite aussi normal, reverse, pendulum ; la cartographie ne les donne que pour le MODE de l'éditeur de pattern ARP. | SE-02, SE-07, SE-09 |
| Clip | KB Span, octave de lancement | Offset : un segment par touche selon la quantize. Off : clips lancés depuis l'octave 0 (SE-07) ou −2 (SE-08). **Écart** : les deux vidéos se contredisent ; cartographie : octave MIDI la plus basse par défaut. | SE-07, SE-08 |
| Clip | Start offset | Drapeau de sample offset mappé sur une macro ; quantize 1/8 ou 1/4. (interp.) = marqueur de start offset de la cartographie. | SE-07, SE-08 |
| Clip | Vers Live | Glisser le clip dans le DAW, puis désactiver le clip dans Serum. | SE-01, SE-05 |
| Arp | Sur des slices | Arp ON, accord tenu : l'arp déclenche les slices. Shift et Range ; Random ; mode chord. | SE-04, SE-15, SE-16 |
| Granular | Base | Rien ne sonne sans sample. Scan à hauteur constante, Density, Length, randoms par paire, fenêtre Hann par défaut. | SE-11, SE-12, SE-13 |
| Granular | Rythme | Clic droit sur Density ou Length › BPM sync ; LFO d'une mesure sur Density. | SE-13 |
| Granular | Manual | Scan devient position ; scrub par modulation. | SE-12, SE-13 |
| Granular | Grains tonals | Length très courte, clic droit › key track. **Écart** : la cartographie place Key Track dans le menu de SCAN, pas de LENGTH. | SE-12 |
| Granular | Crossfade | Contre les clics ; « élargit la stéréo » (SE-10). **Écart possible** : cartographie, sans effet si Loop Grains n'est pas coché. | SE-10, SE-11, SE-12 |
| Spectral | Base | Scan 100 = normal, négatif = reverse. Filtre spectral dessiné. Warps peak follow, gate, comb, harmonics, shift. **Écart** : « peak follow » n'est pas un libellé confirmé par la cartographie (§ 4.3). | SE-03, SE-19, SE-20 |
| Spectral | Batterie, tonal | Option Transients pour les boucles de batterie ; Phase Lock pour moins de flou. **Écart léger** : SE-19 les met au clic droit sur Scan ; la cartographie en fait des contrôles à part. | SE-19 |
| Spectral | Bornes, position | Barre latérale = coupe brick-wall basse et haute (interp. : FREQ LO / HI). Manual : position par enveloppe, LFO ou aftertouch. | SE-18, SE-19, SE-20 |
| Multisample | Charger, régler | SFZ ou usine ; SF2 à convertir. Enveloppe Override, Vel Track, Random = phase, Timbre inverse le mapping. | SE-23 |
| Serum 1 | Audio en wavetable | Glisser sur l'osc ; choisir le mode d'import ; ou taper la note dans le champ de formule avant. | SE-24, SE-26, SE-27, SE-29 |
| Serum 1 | Noise comme sampler | Noise ON, sample déposé, key track à activer, one-shot. | SE-25, SE-26, SE-28 |
| Serum 1 | Resampling | Render osc warp ; Resample to osc A (1 mesure) ; Resample to A+B (stéréo). | SE-30 |

Autres écarts avec la cartographie :

- SE-22 nomme un import « dynamic pitch average ». Ce mode n'existe pas. La cartographie liste Dynamic Pitch - Zero Snap, Dynamic Pitch - Follow, Constant framesize (Pitch Average).
- SE-09 baisse la « chance » de notes du clip. La cartographie ne connaît CHANCE que dans le PLAYBACK de l'ARP.
- SE-29 tape « F1 » et obtient 505 samples par cycle (≈ 87 Hz). La cartographie cite le manuel : 2048 samples ≈ 22 Hz = « F1 ». Les octaves ne concordent pas : à tester.
- SE-01 appelle « fonction cachée » le glisser de la sortie près du logo. C'est l'export audio par glisser de l'icône d'onde (cartographie § 2.3, § 12).
- SE-05 : le MP3 ne marche pas. La cartographie laisse la liste des formats MUET : le corpus la complète.

## Valeurs dites

| Paramètre | Valeur | Source |
|---|---|---|
| Clip en Random, taille de tranche | 1/8 | SE-02 |
| Grille du clip, tempo de la démo | 1/8 à 120 BPM | SE-01 |
| Longueur du clip de break | 2 mesures | SE-03 |
| Launch Quantize | 1/8 (1/16 et 1/32 possibles) | SE-07, SE-08 |
| Grille du clip de stutter | 1/32 | SE-08 |
| Quantize du sample offset | 1/8 ou 1/4 ; 1/16 donne glitches et silences | SE-08 |
| Range du Scan | jusqu'à 800 % | SE-08, SE-19 |
| Scan Spectral, réglage de démo | vers 50 % (plage 200 % par défaut) | SE-19 |
| Scan pour figer un grain | 0 % | SE-04, SE-16 |
| Scan granular, glitch | 100 % → 40 % | SE-10 |
| Density | 0 = transitoire seul ; 1 à 10 en usage courant | SE-12 |
| Random pitch granular | 0 à 12 st ; ≈ 1/4 de demi-ton = effet inquiétant | SE-13 |
| Accordage d'un sample | D → C : −2 st ; G → C : +5 st | SE-12 |
| Grains tonals, valeur au clic droit sur length | 56 (paramètre exact flou) | SE-12 |
| Arp : Shift / Range | Shift 3 st ; Range 8 avec Shift 2 | SE-04 |
| Arp sur voix | Random, rate 1, gate 50 %, 1 mesure ; « 3 » sans paramètre [ASR ?] | SE-15 |
| Transposition d'une voix (F mineur → C# mineur) | −4 st | SE-15 |
| Riser : LFO1 → pitch | 48 st, rampe, mode envelope, 2 mesures ; riser sur 4 mesures | SE-14 |
| Resynthèse flûte : attack et decay liés | ≈ 750 ms ; rate du LFO ramené vers 0,001 | SE-18 |
| Tempo de la démo de basse spectrale | 145 BPM | SE-20 |
| Compression parallèle sur bus | threshold −50, ratio 8, release rapide | SE-06 |
| Reverb Basin sur bus 1 | mix 100 ; LFO4 1 mesure | SE-03 |
| LFO2 path (cutoff / formant) | 2 mesures, free | SE-03 |
| Glitch FX : LFO S&H | LFO3 1/8 ; LFO4 1/16 ; LFO5 2 mesures retrig ; LFO6 1,5 mesure pointée | SE-10 |
| Multisample : delay de l'override | BPM sync 1/16, 1/8, triolet, pointé | SE-23 |
| Hybrid sampler (S1) | LFO1 rate 0,6, BPM OFF ; grid 8 → 64 ; unison 8, octave +1 | SE-26 |
| Voix en wavetable (S1) | LFO1 1 s ; FFT 256 garde la parole, ≈ 2 s max ; passe-haut 90 Hz | SE-27 |
| Cycle échantillonné (S1) | Do4 = 261,63 Hz → 245,28 BPM ; pitch noise 1 % = 1 st, 12 % = octave | SE-28 |
| Import note tapée (S1) | F1 → 505 samples ; ≈ 100 frames gardées sur 149 ; valeur en Hz [ASR ?] | SE-29 |
| Resample to osc A (S1) | 1 mesure ; Render warp = 256 frames | SE-30 |

SE-28 dit « Do4 » pour 261,63 Hz. Dans la numérotation du projet (C3 = 60), c'est C3.

## Fiches par usage

**Breaks et slicing**
- Geste : Sample, break déposé, Slice Auto, seuil réglé, Send to Selected Clip, pattern redessiné [SOURCE SE-03, SE-04, SE-07, SE-08].
- Réglages dits : Retrig ON, Launch Quantize 1/8, Trigger Mode Mono, Tailed pour pitcher vers le haut [SOURCE SE-07, SE-08].
- Chevauchements : release monté et Mono ON [SOURCE SE-05].
- Stutter : Relative Loop + LE sur macro [SOURCE SE-02, SE-03] ; clip de stutter en 1/32 [SOURCE SE-08]. (interp.) Bon outil pour la variation de batterie avant chaque frontière de huit mesures.
- Lire d'abord : SE-03, SE-07, puis SE-04 (arp glitch). Détail Clip et Arp : `serum2-fx-clip-arp.md` § D–E.

**Textures, pads et risers granulaires**
- Pad : grains longs, density haute, petite boucle forward-reverse, detune d'unison baissé, reverb puis filtre [SOURCE SE-11, SE-12].
- Pad grave : transposer de plusieurs octaves, sans time-stretch [SOURCE SE-12].
- Grains rythmiques : Density et Length en BPM sync [SOURCE SE-13].
- Riser : crash inversée, octaves en bas, scan très bas, LFO1 → pitch 48 st sur 2 mesures [SOURCE SE-14].
- Finir pile sur la mesure : rendre en audio, couper, fade in [SOURCE SE-14]. Voir `../modules/resampling/GUIDE.md`.
- Lire d'abord : SE-13, SE-11, SE-14.

**Voix**
- Chops : Sample, Slice Auto, mélodie au piano roll [SOURCE SE-17].
- Texture : Granular, scan bas, density, random pitch léger = chorus [SOURCE SE-15, SE-16]. Scan 100 et randoms à 0 = chops normaux [SOURCE SE-15].
- Accords et plucks : auto slice OFF, région choisie à la main, enveloppe courte [SOURCE SE-16].
- Rester en tonalité : transposer la voix, ici −4 st [SOURCE SE-15].
- Synthé vocal Serum 1 : import constant pour une note tenue, FFT 256 pour la parole [SOURCE SE-27].
- Lire d'abord : SE-15, SE-17. SE-15 emploie la voix d'un titre publié : ne pas la reprendre.

**Basses à partir de samples (spectral, resynthèse)**
- Geste : sub sinus sur un osc, sample tonal en Spectral une octave en bas sur un autre [SOURCE SE-20, SE-21].
- Couleur : warps spectraux harmonics et shift ; enveloppe ou LFO sur main tuning pour les pitch bends [SOURCE SE-20, SE-21].
- Piège : router l'osc spectral vers le filtre, sinon le filtre n'agit pas [SOURCE SE-21]. Un stab de kick marche moins bien [SOURCE SE-20].
- Voie wavetable : one-shot importé, LFO sur la position, nettoyage, unison car l'import est mono [SOURCE SE-22, SE-24].
- Resynthèse réaliste : fondamentale coupée au filtre spectral, remplacée par un sinus ; position en mode Manual [SOURCE SE-18].
- Lire d'abord : SE-21, SE-18. Sub et mid : `../modules/serum-2-basses-house-future-house/GUIDE.md` ; moteurs : `moteurs-synthese.md`.

**Multisample**
- Geste : en-tête de l'osc › Multisample, instrument d'usine ou SFZ ; SF2 à convertir [SOURCE SE-23].
- Réglages : Override de l'enveloppe, delay en BPM sync, Vel Track, Random = phase, Timbre [SOURCE SE-23].
- Clip MIDI sur basse multisample, monophonique, −2 octaves [SOURCE SE-09].
- Drums multisample : vélocité → start ; Mono = effet de choke group [SOURCE SE-09].
- Lire d'abord : SE-23, SE-09. Corpus faible : un seul tutoriel dédié.

**Serum 1**
- Taper la note dans le champ de formule avant l'import [SOURCE SE-26, SE-29]. Tester plusieurs octaves [SOURCE SE-26].
- Avant l'import : silence retiré, fade de fin, consolidation [SOURCE SE-29]. Après : x-fade des bords, frames inutiles retirées [SOURCE SE-26, SE-27, SE-29].
- Noise osc : key track à activer, one-shot, sample brut en couche sous la wavetable [SOURCE SE-25, SE-26, SE-27].
- Resampling : Resample to osc A ou A+B [SOURCE SE-30]. En Serum 2 : menu principal › Resample to (cartographie § 9).
- Lire d'abord : SE-26, SE-30.

## Limites

- **Captures non faites.** Chaque fiche du corpus liste ses points « À vérifier à l'écran ». Aucun n'a été vérifié.
- **Transcription automatique.** Termes déformés possibles ; SE-29 et SE-30 sont très bruitées. Les [ASR ?] restent à confirmer.
- **Version de Serum.** Les vidéos Serum 2 datent de mars 2025 à juillet 2026. La cartographie suit le manuel 2.0.18 ; la version installée est 2.1.5. Un écart peut venir d'une mise à jour (interp.).
- **Numérotation des octaves.** Les tutoriels ne suivent pas tous C3 = 60. Le numéro MIDI fait foi.
- **Rien n'a été entendu.** Aucun résultat sonore n'est garanti. Les tests d'écoute reviennent à l'utilisateur.
- **Droits des samples.** Le corpus utilise breaks célèbres, packs Splice, OST de jeu, voix de titres publiés. Ne jamais réutiliser un enregistrement sans droits dans une sortie. Utiliser ses propres prises ou des samples dont les droits sont vérifiés.
