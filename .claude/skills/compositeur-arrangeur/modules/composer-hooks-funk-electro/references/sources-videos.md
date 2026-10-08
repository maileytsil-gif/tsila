# Sources et registre vidéo (29 septembre 2026)

## Documentation et pédagogie

- Xfer Serum 2, manuel: https://xferrecords.com/manual/serum-2 ; routage Direct: https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter . Source primaire pour vérifier commandes et routage.
- Ableton Live 12 Instrument Reference: https://www.ableton.com/en/manual/live-instrument-reference/ . Source primaire pour les instruments natifs.
- Ableton Low End Theory, 303/Reese/808: https://www.ableton.com/fr/blog/low-end-theory-make-four-classic-bass-sounds-in-live/ . Page et présentation accessibles; vidéo non visionnée intégralement.
- Ableton Made in Live, Tom Cosm: https://www.ableton.com/en/blog/made-in-ableton-live-tom-cosm/ . Page de présentation accessible; flux non visionné intégralement.
- Ableton, Drop It: https://www.ableton.com/fr/blog/drop-it-kick-electronic-music/ . Texte consulté: attaque, corps, queue, comparaison 808/909 et projet Live téléchargeable; l'audio intégré n'a pas été écouté.
- Ableton, Pad It Out: https://www.ableton.com/fr/blog/pad-it-out-10-ways-make-distinctive-pad-sounds/ . Texte consulté: rôle des pads, choix des formes d'onde et détune; les extraits intégrés n'ont pas été écoutés.
- Ableton Live 12 Max for Live Devices: https://www.ableton.com/en/manual/max-for-live-devices/ . DS Kick, Snare, HH, Tom, FM documentés.
- Xfer, macros et modulation: https://xferrecords.com/manual/serum-2/docs . PDF officiel volumineux repéré, non lu intégralement; vérifier les commandes particulières dans le manuel web avant toute instruction de clic.

## Vidéos à analyser avec preuve d'accès

| Source | URL | Accès constaté | Ce que l'on peut affirmer |
|---|---|---|---|
| Antidote Audio, Savage Bass House Basses | https://www.youtube.com/watch?v=eq2P4PteKlA | Transcription anglaise exportée le 29/09/2026; flux audio/vidéo noir, non visionné | Trois familles screecher, wubber, thumper; détails horodatés ci-dessous, chiffres non dits inconnus. |
| Sam Smyers, 5 Deep House Basses | https://www.youtube.com/watch?v=50QAf9gYgtg | Transcription automatique FR complète exportée le 29/09/2026; lecteur noir à 0:00, audio et écran non visionnés | Voir les étapes horodatées ci-dessous; valeurs manipulées sans être dites restent inconnues. Tutoriel de Serum antérieur à Serum 2. |
| EDMProd, Serum 2 advanced bass | https://www.youtube.com/watch?v=FMj-VZGx7pU | Titre/lien repéré seulement | À visionner, aucune technique attribuée. |
| Sam Smyers, Tech House | https://www.youtube.com/watch?v=llXSRqZQxH0 | Titre/lien repéré seulement | À visionner. |
| Dilby, bass patterns | https://www.youtube.com/watch?v=uQ0Sgy0Bikc | Titre/lien repéré seulement | À visionner. |
| Underdog, dotted basslines | https://www.youtube.com/watch?v=uVUjCXacvt0 | Transcription anglaise complète exportée; flux audiovisuel non visionné | Pattern tous les 3/16, phrasé et Wavetable détaillés ci-dessous. |
| Production Music Live, Perfect Kick Serum 2 | https://www.youtube.com/watch?v=vr0DHvuQX8E | Transcription horodatée exportée; audio non vérifié | Click, body et tail séparés; LFO en enveloppe de niveau et pitch, phase/retrigger à vérifier. |
| Proper Villains / Sound Collective NYC, 808 Kick Serum | https://www.youtube.com/watch?v=kUkMmFVtu6E | Transcription automatique FR exportée; audio non vérifié | Sinus G0 (nom dit dans la vidéo, convention d'octave non précisée : vérifier la fréquence), sweep pitch et attaque sample, traitement parallèle/Glue; traduction de « random phase » ambiguë. |

Ne marquer « visionné » que si lecture du flux audiovisuel est vérifiée. Une transcription complète permet d'analyser les paroles, pas de juger le timbre ou le geste audible. Lors d'une séance ultérieure, noter timecodes, paroles ou gestes observés, hypothèse de reconstruction, puis test dans Serum 2/Live. Une vidéo inaccessible nécessite une transcription ou un fichier fourni par l'utilisateur; ne pas inventer son contenu.

## Analyse de la transcription Sam Smyers

La transcription est automatiquement traduite en français; certains noms de commandes et détails peuvent être déformés. Confronter au manuel et à l'interface réelle. Les réglages dont l'auteur dit seulement « comme ceci » ne sont pas récupérables dans les paroles.

| Timecode | Construction dite dans la transcription | Interprétation/test Serum 2 |
|---|---|---|
| 0:28–3:11 Growl | Init, oscillateur à -2 octaves, unison 7 avec detune réduit, mono; compresseur multibande puis distorsion Tube; filtre MG Low 12 puis 24, ENV1 vers cutoff, résonance; delay croche pointée optionnel retiré pour version plus propre. | Tester sans delay puis en retour; comparer le growl au même volume. L'auteur mentionne Meduza comme référence, mais ne fournit pas de preset d'artiste. |
| 3:26–6:22 FM pluck | A sin à -2, B quasi inaudible, FM from B; ENV2 vers quantité FM, puis option LFO en mode enveloppe très rapide; mono et compresseur. | Comparer ENV2 vs LFO pour l'attaque. Les valeurs de FM et les courbes ne sont pas dites; ne pas les inventer. |
| 6:25–8:40 Wide FM | A carré -2 avec unison 3, B saw -2, FM from B; filtre A+B, ENV2 vers cutoff, drive/fat; EQ retirant un peu grave et aigu. | Isoler sub mono si on élargit mid; vérifier la somme au grave plutôt que suivre aveuglément l'unison à -2. |
| 8:45–11:38 Reese | A saw -2, unison 16, filtre drive/fat, ENV2 vers cutoff; mono, portamento possible, LFO sinus sur fine tuning, compresseur. | Diminuer voix/detune si le grave fluctue; enregistrer séparément mid Reese et sub pur. |
| 11:38–14:07 Subby | A carré -2, B saw -1, filtre LP24 A+B et EQ de bas-médium; l'auteur explique que les harmoniques rendent la basse audible par rapport à une sinusoïde pure. | Il s'agit d'une basse harmonique avec présence, pas d'un sub sinusoïdal pur. Tester sous kick et sur petit haut-parleur. |

Cette source prouve les paroles et l'ordre pédagogique, pas le rendu audio ni le résultat exact des mouvements visibles. Elle complète nos recettes expérimentales; elle ne remplace pas le contrôle d'écoute.

## Analyse de la transcription Antidote Audio

| Timecode | Technique expliquée | Essai adapté |
|---|---|---|
| 0:35–1:31 Screecher | Saw, unison, distorsion, compression multibande, sub, filtre fermé modulé par ENV1. | Construire le mid agressif sans élargir le sub; automatiser une seule ouverture par appel. |
| 1:49–2:10 | Soft clip/saturation et sidechain au kick; importance de l'ADSR pour attaque, decay et release du phrasé. | Tester le motif MIDI à niveau égal avant/après sidechain; raccourcir release si deux notes se recouvrent. |
| 2:43–4:17 Wubber | Départ sinus modifié par éditeur d'harmoniques; distorsion et multibande révèlent les harmoniques; ENV1 pilote cutoff et forme le wub. | Faire question courte/réponse longue, comparer filtre seul et saturation. |
| 4:39–6:42 Thumper | Source proche sinus, attaque courte, decay court, sustain nul, distorsion Stompbox, compression puis low-pass; l'auteur met en garde contre unison trop large et propose Hyper/Dimension subtil. | Garder la frappe au centre; vérifier mono, transitoire et tail contre le kick. |

La transcription ne donne pas les valeurs numériques déplacées à l'écran. Les trois recettes du skill sont des adaptations, pas les presets exacts de la vidéo.

## Analyse de la transcription Underdog, dotted basslines

| Timecode | Technique dite | Test adapté |
|---|---|---|
| 1:18–4:13 | Attaques espacées de trois doubles croches; grille 1/16, une note puis deux cases vides, notes MIDI raccourcies pour pluck; variations de turnaround, réinitialisation sur le temps 1 d'une phrase de deux mesures. | Écrire deux mesures exactes avant le patch et marquer la note de retour. |
| 4:36–6:00 | Progression A vers F (vi–IV en do majeur ou i–VI en la mineur), note de turnaround liée aux accords. | Adapter les notes d'approche à la vraie progression sans déplacer le motif identitaire. |
| 6:21–7:20 | Groove Pool « Funk Modern », diminuer Timing et Velocity si effet trop fort. | Comparer timing seul, vélocité seule, les deux, puis original. |
| 8:45–11:10 | Wavetable saw, LPF et ENV2 pluck vers cutoff par matrice; ensuite table à caractère formant et automation de position, octave abaissée si trop brillante. | Transposer dans Serum 2 avec modulation équivalente, pas reproduire un pourcentage d'un synthé différent. |
| 11:42–13:15 | Unison discret, mono/glide, filtre 24 dB avec drive; delay ping-pong filtré dont durée diffère de l'intervalle des notes, Valhalla Room. | Garder le sub sec et central, envoyer seulement les harmoniques vers espace. |

Les valeurs perceptives et les choix exacts à l'écran ne peuvent pas être confirmés par la seule transcription. La notion « tous les 3/16 » peut créer un déplacement d'accent; la remise au temps 1 à la fin de phrase garde la forme dans un cycle 4/4.

## Deux tutoriels kicks analysés par transcription

- **Production Music Live, Serum 2**: 0:36–1:19 distingue click, corps/punch, tail sub; 1:22–2:43 montre le besoin de contrôler amplitude/pitch avec scope, spectre et spectrogramme; 2:48–4:15 sinusoïde accordée en G et LFO1 en mode enveloppe sur level, random à zéro pour répétabilité; 4:23–5:42 LFO2 unipolaire sur coarse pitch avec descente rapide; 5:48–7:37 OSC B carré +2 octaves et attaque LFO3 très brève avec distorsion momentanée; 7:46–9:57 alternative sample d'attaque OSC C, filtrage et retard du corps pour dégager le click. Chiffres et courbes seulement visibles restent à inspecter sur un flux qui fonctionne.
- **Proper Villains / Sound Collective NYC, Serum**: 0:09 vise un kick 808 court house/techno; 1:31–4:30 sinus G0, LFO1 enveloppe de niveau et LFO2 unipolaire sur pitch, sweep annoncé autour de deux octaves et vitesse libre; 4:36–5:10 sample d'attaque; 5:12–6:58 Glue Compressor autour de 4:1, environ 5 dB de réduction, saturateur doux puis EQ; 7:23–8:25 alternatives d'attaque, triangle vers 909 ou carré filtré pour electro/techno. Les sous-titres semblent contredire le commentaire sur « random phase »: vérifier visuellement avant de prescrire ce réglage.
