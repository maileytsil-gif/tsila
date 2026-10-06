# Simpler d'Ableton Live : synthèse de 30 tutoriels

Synthèse du corpus `tutoriels-simpler.md` (30 tutoriels YouTube, SI-01 à SI-30).
L'étude date du 05/10/2026 ; elle a été faite dans Claude in Chrome sur le Mac.
Les transcriptions ont été lues, son coupé : **rien n'a été entendu**.
« Dit » signifie : présent dans la transcription ou la description. Le reste est marqué (interp.).
[ASR ?] signale une reconnaissance vocale douteuse.
Langues : 22 tutoriels en anglais, 7 en français (SI-02, 11, 14, 15, 18, 19, 30). SI-23 est en anglais, lu par un sous-titre français manuel.
Versions de Live dites : Live 12 (SI-14, 18, 19, 21), Live 11 (SI-12, 29), Live 10 (SI-05, SI-24), Live 9.5+ (SI-11, SI-17). Ailleurs, la version est déduite de la date (interp.).
Notes en numérotation Ableton : C3 = 60, donc C1 = 36.

## Ce que dit le corpus avant tout

- **Le mode Slice est le cœur de l'outil.** Découpe par transitoires par défaut, slice 1 sur C1 (MIDI 36), puis chromatique [SOURCE SI-10, SI-11, SI-24, SI-27]. Trop de slices : baisser Sensitivity [SOURCE SI-03, SI-05, SI-10, SI-14].
- **Deux chemins, deux usages.** Un seul Simpler en Slice permet un traitement global du break (filtre SMP, Thru, Gate) [SOURCE SI-04]. Slice to Drum Rack ou Slice to New MIDI Track donne un Simpler par pad, réglable un à un [SOURCE SI-10, SI-11, SI-13].
- **Préparer la source avant de découper.** Boucle propre et calée, start sur la première frappe, warp léger qui garde le groove du batteur [SOURCE SI-04, SI-06, SI-07]. Choisir un break proche du tempo visé : plus on warpe, plus les artefacts s'entendent, dit SI-05.
- **Simpler est aussi un synthé.** Une boucle très courte rend un son tonal [SOURCE SI-25, SI-29]. L'automation de Length, Loop, Start et Fade donne stutter et glitch [SOURCE SI-22, SI-23]. Les modes de warp Texture et Beats servent de pseudo-granulaire [SOURCE SI-24].
- **Lacunes avouées par le corpus.** Aucun riser fait dans Simpler. Le reverse n'est que mentionné (SI-10, SI-12).

## Gestes de base

| Geste | Comment | Sources |
|---|---|---|
| Charger un sample | Glisser le sample sur une piste MIDI : Simpler se crée seul. Ou le déposer dans « Drop sample here ». | SI-01, SI-16, SI-18, SI-27, SI-28 |
| Mode Classic | Sample réparti en hauteur sur le clavier ; Loop et ADSR ; polyphonique ; pour sons tenus et instruments. | SI-11, SI-12, SI-15, SI-30 |
| Mode One-Shot | Joue toute la longueur, quelle que soit la note ; Fade In ≈ attaque, Fade Out ≈ release ; pour les drums. | SI-11, SI-12, SI-27, SI-30 |
| Trigger / Gate | Trigger : la slice ou le son joue jusqu'au bout. Gate : la note tenue décide de la durée. | SI-01, SI-11, SI-17, SI-24 |
| Mode Slice | Découpe automatique ; slices jouées depuis C1 (MIDI 36), une par demi-ton. | SI-01, SI-10, SI-11, SI-27 |
| Slice by Transient | Choix par défaut ; Sensitivity plus basse = moins de slices, plus longues. | SI-03, SI-10, SI-11, SI-17 |
| Slice by Beat | Division régulière selon le BPM ; warper d'abord. | SI-02, SI-04, SI-10, SI-17 |
| Slice by Region | N slices égales entre start et end ; jusqu'à 64 ; « façon MPC ». | SI-04, SI-14, SI-16, SI-17, SI-24 |
| Slice Manual | Double-clic pour créer ou supprimer ; clic droit pour effacer toutes les slices. | SI-13, SI-14, SI-15 |
| Playback Mono / Poly / Thru | Mono : une slice à la fois. Poly : plusieurs (accords, finger drumming). Thru : la note tenue continue au-delà de la slice. | SI-02, SI-04, SI-10, SI-11 |
| Nettoyer une slice | Déplacer le début de la slice suivante contre un clic ; ajouter une slice pour isoler un défaut ; Fade global en dernier recours. | SI-11 |
| Slice to Drum Rack | Clic droit **dans** la forme d'onde ; un Simpler par pad, non destructif. | SI-10, SI-11, SI-12, SI-13, SI-14, SI-15, SI-19 |
| Slice to New MIDI Track | Clic droit sur le clip audio ; une slice par transitoire, par warp marker ou par division ; Preserve Warp Timing ; clip « en escalier » qui rejoue la phrase. | SI-04, SI-06, SI-08, SI-09, SI-11, SI-21 |
| Copier un réglage aux pads | Clic droit « Copy Value to Siblings » ; pour une macro : « Map to All Siblings ». | SI-06, SI-07, SI-19, SI-22 |
| Choke | Pads dans le même groupe : la dernière note coupe la précédente. | SI-11, SI-19 |
| Warp dans Simpler | Re-Pitch, Beats, Texture, Tones, Complex, Complex Pro ; boutons ×2 / ÷2 ; champ BPM du sample. | SI-01, SI-05, SI-12, SI-23, SI-24, SI-26 |
| Boucle courte | Loop ON ; Start, Length, Loop, Fade ; Snap (passage par zéro) actif ou non selon le but. | SI-22, SI-23, SI-25, SI-29 |
| Glide | Voices = 1 et Glide : la boucle continue et n'est que transposée (legato). | SI-22, SI-26 |
| Crop / Reverse | Clic droit sur la forme d'onde. | SI-11, SI-12, SI-15 |
| Accorder | Tuner après Simpler, puis Transpose et Detune. | SI-12, SI-25, SI-26, SI-30 |
| Chaînes aléatoires | Instrument Rack, chaînes en modes de warp différents, chain selector mappé et piloté au hasard. | SI-01 |
| Passer à Sampler | Clic droit « Simpler to Sampler » pour plus de contrôles. | SI-27 |

## Valeurs dites

| Paramètre | Valeur | Source |
|---|---|---|
| Sensitivity (slicing) | ≈ 50 % sur un Amen | SI-01 |
| Sensitivity (voix) | ≈ 75 % | SI-17 |
| Sensitivity (voix) | « 89 » → 23 tranches [ASR ? interp. : 89 %] | SI-19 |
| Slice by Beat | noire (1/4) | SI-02, SI-04 |
| Slice by Beat sur un resample | blanche (1/2) | SI-17 |
| Slice to New MIDI, division | 1/2 → 34 slices | SI-21 |
| Regions | 8 puis 16 | SI-16 |
| Regions | 16 puis 32 | SI-04 |
| Regions | 13 (nombre premier, résultat inattendu) | SI-17 |
| Regions | 64 (maximum) | SI-14, SI-24 |
| Transpose global du break | −3 demi-tons | SI-03 |
| Transpose des slices | +6 demi-tons | SI-06 |
| Warp Beats + Transpose | +2 demi-tons, pour approcher le son Re-Pitch | SI-07 |
| Plage de Transpose | −48 à +48 demi-tons ; choix −4 | SI-16 |
| Transpose d'une voix | −1 octave | SI-17 |
| Loop length des pads | 0 (0 %), contre pops et clics | SI-06, SI-07, SI-09 |
| Sustain / Decay des pads | Sustain 0 ; Decay « 2–3 s » pour resserrer (unité à vérifier, interp.) | SI-07 |
| Fade In contre les coupes | ≈ 15 ms | SI-16 |
| Decay par défaut | 600 ms | SI-27, SI-28 |
| Pitch Envelope (kick de sinus) | +44 demi-tons | SI-26 |
| Filtre auto-oscillant | Resonance au max ; Key tracking 100 % ; volume du sample à −∞ dB | SI-26 |
| LFO de filtre | 2 bars ; Retrigger désactivé | SI-26 |
| Detune après Transpose | ≈ 30,2 cents | SI-25 |
| Voices | 1 (basse, Glide) ; 6 (pluck vocal) | SI-22, SI-27, SI-28 |
| Track Delay | ≈ −40 ms, pour compenser le start | SI-27 |
| Cutoff Low-pass | de 22 kHz vers 3 kHz [dit « 22 Hertz »] | SI-28 |
| Enveloppe de filtre | Amount sur ±72, réglé à mi-course | SI-28 |
| Arpeggiator avant Simpler | Style Up, Rate 1/8 | SI-20 |
| Choke | groupe 16 pour tous les pads | SI-19 |
| Flam (outil MIDI Live 12) | 1 note, Position −100, valeur « 10 » [ASR ?] | SI-19 |
| Chain selector | première chaîne étirée jusqu'à ≈ 88 [ASR ?] | SI-01 |
| Fuzz sur le break | « 3 % de gain » [ASR ?] | SI-03 |
| Warp Beats, Envelope | 100 = pas de fondu ; 0 = décroissance quasi instantanée | SI-24 |
| Warp Texture | Flux à 0 ; ×2 = −50 % de vitesse [dit « by 100% »] | SI-24 |
| Boucle d'impact | Start 0 ; Loop et Length 100 % ; Snap désactivé | SI-22 |
| Tempos | 91 → 105 BPM (SI-03) ; ≈ 68 → 134 (SI-09) ; 170 (SI-06) ; 130 puis 133 (SI-07) ; 94 → 150 (SI-23) ; boucle 80 → 128 (SI-27) | voir colonne |

## Fiches par usage

### Breaks et Slice to MIDI

- Geste : couper une boucle parfaite, caler le premier kick sur 1.1 (« Set 1.1 Here »), puis découper [SOURCE SI-06, SI-07].
- Warp markers sur les frappes fortes, transitoires sur les faibles ; dans Think, viser la snare et non le tambourin [SOURCE SI-07].
- Slice to New MIDI Track « per warp marker » ; ajouter un marqueur tout à la fin, sinon la dernière slice est mal coupée [SOURCE SI-06].
- Dans le Drum Rack : Loop length 0, Transpose puis « Copy Value to Siblings » [SOURCE SI-06, SI-07, SI-09].
- Un seul Simpler : Gate ON, Playback Thru, warp Re-Pitch, notes raccourcies pour un effet staccato [SOURCE SI-01, SI-04].
- À lire d'abord : SI-07, SI-06, SI-04, puis SI-01 (variantes aléatoires par chaînes). Rythme du chopping : `rythme-forme.md`.

### Slicing et modes

- Geste : choisir le mode d'après la source. One-Shot pour les drums, Classic pour les sons tenus, Slice pour une boucle ou une phrase [SOURCE SI-11, SI-30].
- Slicing manuel : effacer les slices auto, double-clic sur chaque attaque, Crop, zoom [SOURCE SI-13, SI-15].
- Piège dit : en Mono, Slice to Drum Rack met tous les pads dans le même groupe de Choke. Passer en Poly **avant** de convertir pour superposer [SOURCE SI-11].
- Ajouter un peu de Fade avant de convertir en Drum Rack [SOURCE SI-11].
- Accorder d'abord (Tuner, Transpose) ; warp Complex ou Complex Pro pour caler une boucle tonale [SOURCE SI-12].
- À lire d'abord : SI-11 (le plus complet), SI-10, SI-12, SI-14.

### Vocal chops

- Geste : voix en Slice, garder **quelques** slices choisies, pas toutes [SOURCE SI-17, SI-20].
- Sensitivity ≈ 75 % ; Region en nombre premier (13) pour des découpes inattendues ; Complex Pro pour garder la tonalité [SOURCE SI-17].
- Arpeggiator avant Simpler (Up, 1/8, puis Random) : les notes tenues arpègent les chops [SOURCE SI-20].
- Live 12 : Slice to Drum Rack ou Slice to New MIDI, puis Generate › Seed sur la plage des slices ; Choke 16 pour un son plus découpé [SOURCE SI-19, SI-21].
- Resampler le groove puis re-slicer, contre l'effet « boucle de 8 mesures » [SOURCE SI-17, SI-21]. Capture : `../../resampling/SKILL.md`.
- À lire d'abord : SI-17, SI-19, SI-20. SI-21 n'est sur Simpler qu'en partie (sa 3e méthode utilise Granulator III).

### Stutter, glitch, pseudo-granulaire

- Geste : Loop ON, note tenue, puis faire varier Length ; Length est un pourcentage de la zone start–end, pas des ms [SOURCE SI-22].
- Fade bas et Snap désactivé : harmoniques puis glitchs inharmoniques [SOURCE SI-23].
- « Balle rebondissante » : Start qui parcourt le sample et Length qui diminue, en automation de clip [SOURCE SI-23].
- « Exponential groove » : Drum Rack de Simplers bouclés, Length sur une macro « Map to All Siblings », notes en legato [SOURCE SI-22].
- Warp Texture : Flux 0, ×2 répété, Grain Size ; Beats : Preserve et Envelope bas pour un effet rythmique [SOURCE SI-23, SI-24].
- À lire d'abord : SI-22, SI-24, SI-23 ; instrument micro-boucle : SI-25.

### Basses, leads et astuces

- Basse sample-based : one-shot de basse, Low-pass, type modélisé avec Drive, Voices 1, enveloppe de filtre [SOURCE SI-28, SI-29].
- Lead tonal : une toute petite partie d'un hi-hat, bouclée [SOURCE SI-29]. Plus la boucle est courte, plus la hauteur est nette [SOURCE SI-25].
- Kick de sinus : Pitch Envelope +44 demi-tons, vitesse de descente réglée par le Decay [SOURCE SI-26].
- Accords de voix synchrones : Warp ON en Complex [SOURCE SI-26]. LFO sans Retrigger : chaque note a un cutoff différent [SOURCE SI-26].
- One-shot tonal hors de C : corriger Transpose et Detune dans Simpler [SOURCE SI-30].
- À lire d'abord : SI-28, SI-26, SI-27. Paramètres exposés à l'API : `../../vst-sound-design/references/instruments-natifs.md`. Au-delà de Simpler : `tutoriels-sampler.md`.

## Limites

- **Captures d'écran non faites.** Chaque fiche du corpus liste ses moments « à vérifier à l'écran ». Toute position de bouton reste à confirmer dans Live.
- **Transcription automatique** pour 28 tutoriels sur 30 (SI-12 en partie manuelle, SI-23 en sous-titre manuel traduit). Les valeurs [ASR ?] ne se recopient pas sans vérification.
- **Versions de Live.** Beaucoup de tutoriels datent de Live 9.5 ou 10. Seuls SI-14, 18, 19 et 21 sont dits Live 12. Seed, Connect et Ornament n'existent que dans Live 12 (SI-19, SI-21).
- **Droits des samples.** Amen, Think, Funky Drummer, Cold Sweat, « Chameleon », « Rockafeller Skank » et les voix de packs servent d'exemples dans le corpus. Ne jamais réutiliser un enregistrement sans droits dans une sortie : break, voix ou boucle. Travailler sur une matière libre ou produite par l'utilisateur.
- **Effets natifs de Live.** Le corpus en ajoute souvent : Drum Buss (SI-07), Echo (SI-13), Erosion (SI-29), reverb, delay, chorus, Soft Shaper, compresseur (SI-17, SI-18, SI-24). Règle du projet : pas de nouvel effet natif de Live dans les chaînes de mix ; passer par des plug-ins tiers.
- **Instruments natifs tolérés.** Simpler, Drum Rack, Instrument Rack et Sampler restent utilisables.
- **Max for Live à signaler.** Expression Control (SI-01) et Granulator III (SI-21) sont des devices Max for Live ; vérifier leur présence avant de les proposer.
- **Lacunes.** Pas de riser dans Simpler ; le plus proche : automation de Length, Loop, Start (SI-22, SI-23), Pitch Envelope (SI-26), Glide (SI-22, SI-26). Reverse seulement mentionné (SI-10, SI-12).
