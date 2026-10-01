---
titre: "ClyphX — live_instant_mapping.md, extrait : banques de paramètres Electric et Tension (noms exacts des paramètres Live)"
source: https://raw.githubusercontent.com/nuno-andre/clyphx/master/docs/live_instant_mapping.md
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: Ableton Live 12 : Electric, Tension, Operator, Vocoder, packs (documents tiers et miroirs)
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

> Extrait : introduction et sections « Electric » et « Tension » seulement (document établi pour Live 10.1.30).

Live Instant Mapping Info for Ableton Live v10.1.30
===================================================

The following document covers the parameter banks accessible via Ableton Live's
_Instant Mapping_ feature for each built in device. This info also applies to
controlling device parameters via **ClyphX**'s _Device Actions_.

> **NOTE:** The order of parameter banks is sometimes changed by Ableton. If you
find the information in this document to be incorrect, you can recreate it with
**ClyphX** by triggering an action named `MAKE_DEV_DOC`. That will create a new
version of this file in your user/home directory.

* * *

## Electric

| `B0`: Best of Banks | `B1`: Mallet and Tine | `B2`: Tone and Damper | `B3`: Pickup       | `B4`: Modulation    | `B5`: Global     |
| :------------------ | :-------------------- | :-------------------- | :----------------- | :------------------ | :--------------- |
| `P1`: M Stiffness   | `P1`: M Stiffness     | `P1`: F Tone Decay    | `P1`: P Symmetry   | `P1`: M Stiff < Vel | `P1`: Volume     |
| `P2`: M Force       | `P2`: M Force         | `P2`: F Tone Vol      | `P2`: P Distance   | `P2`: M Stiff < Key | `P2`: Voices     |
| `P3`: Noise Amount  | `P3`: Noise Pitch     | `P3`: F Release       | `P3`: P Amp In     | `P3`: M Force < Vel | `P3`: Semitone   |
| `P4`: F Tine Vol    | `P4`: Noise Decay     | `P4`: Damp Tone       | `P4`: P Amp Out    | `P4`: M Force < Key | `P4`: Detune     |
| `P5`: F Tone Vol    | `P5`: Noise Amount    | `P5`: Damp Balance    | `P5`: Pickup Model | `P5`: Noise < Key   | `P5`: KB Stretch |
| `P6`: F Release     | `P6`: F Tine Color    | `P6`: Damp Amount     | `P6`:              | `P6`: F Tine < Key  | `P6`: PB Range   |
| `P7`: P Symmetry    | `P7`: F Tine Decay    | `P7`:                 | `P7`:              | `P7`: P Amp < Key   | `P7`:            |
| `P8`: Volume        | `P8`: F Tine Vol      | `P8`:                 | `P8`:              | `P8`:               | `P8`:            |

[Back to Device Index](#device-index)

* * *


## Tension

| `B0`: Best of Banks  | `B1`: Excitator and String | `B2`: Damper      | `B3`: Termination and Pickup | `B4`: Body          | `B5`: Vibrato        | `B6`: Filter        | `B7`: Envelope and LFO | `B8`: Global        |
| :------------------- | :------------------------- | :---------------- | :--------------------------- | :------------------ | :------------------- | :------------------ | :--------------------- | :------------------ |
| `P1`: Filter Freq    | `P1`: Excitator Type       | `P1`: Damper On   | `P1`: Term On/Off            | `P1`: Body On/Off   | `P1`: Vibrato On/Off | `P1`: Filter On/Off | `P1`: FEG On/Off       | `P1`: Unison On/Off |
| `P2`: Filter Reso    | `P2`: String Decay         | `P2`: Damper Mass | `P2`: Term Mass              | `P2`: Body Type     | `P2`: Vib Delay      | `P2`: Filter Type   | `P2`: FEG Attack       | `P2`: Uni Detune    |
| `P3`: Filter Type    | `P3`: Str Inharmon         | `P3`: D Stiffness | `P3`: Term Fng Stiff         | `P3`: Body Size     | `P3`: Vib Fade-In    | `P3`: Filter Freq   | `P3`: FEG Decay        | `P3`: Porta On/Off  |
| `P4`: Excitator Type | `P4`: Str Damping          | `P4`: D Velocity  | `P4`: Term Fret Stiff        | `P4`: Body Decay    | `P4`: Vib Speed      | `P4`: Filter Reso   | `P4`: FEG Sustain      | `P4`: Porta Time    |
| `P5`: E Pos          | `P5`: Exc ForceMassProt    | `P5`: Damp Pos    | `P5`: Pickup On/Off          | `P5`: Body Low-Cut  | `P5`: Vib Amount     | `P5`: Freq < Env    | `P5`: FEG Release      | `P5`: Voices        |
| `P6`: String Decay   | `P6`: Exc FricStiff        | `P6`: D Damping   | `P6`: Pickup Pos             | `P6`: Body High-Cut | `P6`: Vib < ModWh    | `P6`: Freq < LFO    | `P6`: LFO On/Off       | `P6`: Octave        |
| `P7`: Str Damping    | `P7`: Exc Velocity         | `P7`: D Pos < Vel | `P7`: T Mass < Vel           | `P7`: Body Mix      | `P7`: Vib Error      | `P7`: Reso < Env    | `P7`: LFO Shape        | `P7`: Semitone      |
| `P8`: Volume         | `P8`: E Pos                | `P8`: D Pos Abs   | `P8`: T Mass < Key           | `P8`: Volume        | `P8`: Volume         | `P8`: Reso < LFO    | `P8`: LFO Speed        | `P8`: Volume        |

[Back to Device Index](#device-index)

* * *
