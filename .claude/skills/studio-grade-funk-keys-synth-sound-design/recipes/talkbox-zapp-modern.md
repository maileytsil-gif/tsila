# Talkbox (Zapp, Chromeo, « 24K Magic ») — émulation par vocodeur et formants

## Cible
`VOIX SYNTHÉTIQUE : hook ou intro / source scie ou « saw-pulse » / mono, legato, glide / jamais en même temps que le chant principal`

## Faits
Troutman : Golden Throat + Minimoog puis **DX100** (portable ; patch « SAWPULSE » selon un témoignage anonyme) [HEUR-extrait] ; Chromeo : DX100 avec les patches Troutman → **Rocktron Banshee 2** → « un peu d'EQ et de compression » ; « plus humain que le vocodeur » [DOC-EXTRAIT] ; Mr Talkbox (24K Magic) : DX100 → **MXR M222** [DOC-EXTRAIT/HEUR-extrait]. Talkbox ≠ vocodeur : la bouche forme les voyelles sur le son envoyé par un tube, on ne chante pas [HEUR-extrait].

## Voie 1 — Vocoder de Live avec une voix qui mime [DOC manuel, réglages HEUR/TEST]
Piste voix (micro, voyelles non voisées ou chuchotées) avec **Vocoder** ; **Carrier = External**, Audio From = piste du synthé (Post FX) ; synthé : Analog ou Serum 2 **scie** (« essayez des patches à base de dent de scie pour l'intelligibilité » [DOC]) ou scie + pulse 30 %, MONO legato, porta 30–80 ms ; Bands élevé, BW ≈ 100 %, **Depth 100 %**, Attack/Release courts, **Unvoiced bas** (une talkbox n'a pas de « s »), Enhance on, **Retro** pour le grain, Formant léger ; puis EQ coupe-haut 5–6 kHz (le tube coupe les aigus) et Saturator doux (ampli).

## Voie 2 — Filtre à formants sans voix [HEUR/TEST]
Serum 2 : OSC A scie, MONO legato ; Filtre 1 en mode Formant (nom exact à relever en 2.1.5) ou PZ_SVF dessiné ; **macro ou LFO lent** qui parcourt « oo → a → ee » ; table SS23 (homme) : « oo » 300 / 870 / 2250 Hz, « a » 660 / 1700 / 2400, « ee » 270 / 2300 / 3000, largeur ≈ 100 Hz, **le 2e formant bouge le plus** [DOC]. Natif : **Auto Filter Vowel** (Pitch, Formant a-e-i-o-u, Morph) automatisé par note, ou Meld filtre Vowel [DOC].

## Voie 3 — plug-ins dédiés (si installés [TEST])
MDA TalkBox (gratuit), iZotope VocalSynth 2 (module Talkbox Dark/Classic/Bright) [HEUR-extrait].

## Chaîne
`Vocoder ou Serum → EQ Eight coupe-haut 5–6 kHz, cloche +3 dB 1–2 kHz → Saturator Soft Sine → Compressor Peak 4:1 attaque 5 ms → room courte`. Mono, centré.

## Tests [TEST]
Les voyelles se distinguent (F2 bouge) · pas de « s » sifflants · glide entre notes liées · niveau stable d'une voyelle à l'autre.
