# Instruments natifs de Live 12 pour les cuivres

Faits constructeur : texte du manuel Live 12 (ch. 24 racks, 28 effets, 30 instruments) lu sur copie intégrale (`../../../../corpus/constructeur/`), fiche locale `../../sound-designer-serum/references/ableton-instruments.md`. Tous les paramètres sont pilotables et relisibles par `ppal-update-device` / `ppal-read-device` (`../../vst-sound-design/references/instruments-natifs.md`) : préférer le natif quand la reproductibilité et le pilotage comptent plus que le timbre.

## Quel instrument pour quel cuivre

| Cuivre | Premier choix | Alternative | Raison [DOC sauf mention] |
|---|---|---|---|
| Synth brass analogique (section, stab, pad) | **Analog** | Wavetable | 2 oscillateurs saw/rectangle avec PWM par LFO, Sync, filtres 2e/4e ordre dont **formant**, enveloppes avec Legato, LFO avec Delay/Attack, **Vibrato dédié** avec Delay, Attack, Error et Amt < MW, Unison 2/4 voix |
| Lead mono rapide | **Drift** | Analog | Saw / Shark Tooth, Mono avec Thickness (4 voix), Legato, Glide |
| Cuivre FM | **Operator** | Serum 2 | 11 algorithmes, feedback sur tout oscillateur non modulé, enveloppe par oscillateur (3 temps/3 niveaux, Vel et Key), pitch envelope avec End, LFO audio (8 Hz–12 kHz) avec sa propre enveloppe, Voices = 1 → legato |
| Émulation par soustractif | Analog ou Operator (Saw seul) | Wavetable | filtre `Play by Key` (466 Hz, Freq < Key 100 %), Freq < Env ≈ 9 octaves à 100 % |
| Cuivre réel | **Orchestral Brass** (Live Suite, SONiVOX, Simpler + racks à macro d'articulations), **Brass Quartet** (Spitfire, macro Technique) | Sampler avec multisample perso | packs [DOC-EXTRAIT] : solo et ensembles cor/trombone/trompette/tuba, « articulations commutables par une seule macro » ; tailles et listes non vérifiées [TEST] |
| Multisample perso | **Sampler** | Simpler (one-shot) | zones Key/Velocity/Sample Select, crossfades, Round Robin ; Glide mono ou Portamento poly ; **pas de legato ni de keyswitch documentés** |
| Stab échantillonné | **Simpler** One-Shot ou Drum Rack | Sample de Serum 2 | trois modes Classic/One-Shot/Slicing |
| Corps de tuyau, formant | effet **Corpus** (Pipe/Tube, Opening, Radius, sidechain MIDI), **Vocoder** (Formant, self-vocoding), **Auto Filter** Vowel | filtre formant d'Analog | résonateurs Pipe/Tube documentés ; Vocoder « Modulator » = resynthèse |
| Hybride, textures | **Meld** | — | aucun oscillateur cuivre, mais filtre **Vowel** (formants morphables), Swarm Saw, Harmonic FM, glide Porta/Gliss en poly |

## Analog — recette synth brass [HEUR, capacités DOC]
Osc 1 Saw ; Osc 2 Saw Detune +6–8 cents (ou Rectangle PW 45 % + LFO lent sur la largeur) ; Filtre 1 LP 4e ordre cutoff 600–900 Hz, résonance faible, Env < Vel ; Env filtre A 60 ms (stab) à 400 ms (tenue) / D 250–800 ms / S 50–60 % ; Env ampli A 20–40 ms, R 100 ms, **Legato** on pour les lignes ; **Vibrato** Delay 0,4 s, Attack 0,5 s, Error faible, Amt < MW ; Unison 2 voix Delay court ; Glide Legato + Prop. Filtre 2 en **formant** en parallèle, dosé bas, pour le pavillon [TEST]. Pitch Env (Initial −2 st, Time 60 ms) = scoop natif, facultatif.

## Operator — cuivres FM (voir `../recipes/fm-brass-dx7-operator.md`)
Pile B→A sinus 1:1, index = enveloppe de B (A ≈ 100 ms) avec Lev < Vel ; algorithme 9 (D → A, B, C) avec Feedback sur D pour approcher BRASS 1 ; LFO Hi 60–80 Hz vers `FM Drive` ou FIL avec enveloppe de LFO courte = growl sans toucher la hauteur [DOC cible FM Drive] ; enveloppe de LFO = vibrato retardé natif [DOC].

## Wavetable
Osc 1 Basic Shapes saw, unison **Classic** 2–3 voix (jamais Phase Sync) [DOC modes], Sub off ; Env 2 → Flt 1 Freq avec Velocity en amount dans la matrice ; **Note → Filter Freq 100 % = suivi exact** [DOC] (mettre 90 %) ; LFO 1 → Osc 1 Transp avec **Attack Time** pour le vibrato retardé [DOC] ; Env 3 → pitch pour un scoop ; Mono/Poly, Glide en Mono.

## Racks : articulations et « keyswitch »
Un Instrument Rack avec une chaîne par articulation (sustain, staccato, fall) et **Chain Select** piloté par une macro [DOC ch. 24] ; c'est le mécanisme des packs Ableton. Une zone avec fondu = coupure au changement, sans fondu = les queues d'effets finissent. Le keyswitch par note MIDI n'existe pas nativement : automation de la macro dans l'arrangement (`../../live-automation/SKILL.md`).

## Effets natifs utiles [DOC capacités]
- **Chorus-Ensemble** : mode Ensemble (3 lignes, phases réparties) rate 1–1,8 Hz, faible ; Vibrato mode pour un vibrato externe.
- **Saturator** : Soft Sine ou Analog Clip, Drive faible, **Color** pour ne saturer que 800 Hz–4 kHz.
- **Multiband Dynamics** : bande haute seule > 5 kHz, attaque/release rapides = dé-durcissement ; le preset OTT (compression ascendante + descendante sur 3 bandes) pour le future bass.
- **Glue Compressor** sur le bus de section : 2:1–4:1, attaque 10–30 ms, Auto Release, Range −60/−70 dB = matériel d'origine.
- **Auto Filter** Vowel + envelope follower ; **Corpus** Pipe à Dry/Wet faible = corps accordé sur la note.

## Ce que le natif ne fait pas
Sampler : pas de vrai legato, pas de keyswitch, import SFZ non documenté (REX/ACID/Soundtrack seulement) ; Wavetable et MPE non confirmés par le texte lu ; le Core Library ne documente aucun instrument « Brass » (relever dans le navigateur [TEST]).
