# Lead de festival et screech (big room, trance, hardstyle, rawstyle)

Le « brass » assumé synthétique : lead supersaw à une ou deux notes, screech distordu. Sources : extraits Myloops/ADSR/Screech House [HEUR-extrait], fiches de genre lues [HEUR-lu] (`../../../../corpus/cuivres/recherche-axe3-cuivres-electroniques-modernes.md`).

## Cible
`LEAD / big room 126–132 BPM (mineur), hardstyle 148–155, rawstyle 150–160 / 60–84, 1–2 notes au drop / BRASS OWNS HOOK`

## Lead supersaw (big room, trance) [HEUR-extrait/HEUR-lu]
- OSC A scie **unison 7, detune 0,25–0,30, blend 0,8** ; OSC B scie unison 3, detune 0,15, **−1 octave, −6 dB** (« l'octave basse ancre la hauteur quand le haut s'élargit ») ; ou GMS : 3 scies 0/+7/−7 cents, unisono 6–8, stéréo 75 %.
- Filtre LP cutoff ≈ 85 %, résonance 20 % ; Env 1 A 0, D 25 %, S 95 %, R 35 % (valeurs en % du plugin d'origine, à convertir [TEST]).
- Hyper/Dimension pour l'unisson supplémentaire [HEUR-extrait] ; FX : flanger léger + reverb ; sidechain du kick.
- Registre 60–79 ; le drop = kick + basse + un seul lead.

## Screech hardstyle (Serum, d'après ADSR) [HEUR-extrait]
1. Init ; wavetable **Basic CJW** (dossier Analog) ; copier A → B ; **7 voix chacun**, détune monté.
2. **LFO 1 → Coarse pitch des deux oscillateurs, BPM sync off, ≈ 20 Hz** (vibrato rapide) ; **LFO 2 en mode Env → Master Tune** (rampe de hauteur) ; enveloppe de pitch inclinée avec DEC et AMT.
3. Filtre **Peak 12** résonance montée, cutoff par LFO 2 ; même LFO sur cutoff et WT POS.
4. Distorsion : monter **Drive et FAT** progressivement ; puis **resampler, re-pitcher, répéter** (fiche hardstyle lue : « saws détunées → distorsion → passe-bande résonant → resample → re-pitch ») (`../../resampling/SKILL.md`).
- Variante rawstyle (Sylenth1) : 1–2 osc, 6–8 voix, détune poussé, pitch env DEC + AMT (+ un peu d'ATT), LFO de pitch rapide à attaque courte, distorsion et chorus internes.
- Lead hardstyle (Screech House) : 2 oscillateurs × 16 voix, fortement détunés, B +1 octave.

## Stab EDM (Producer School) [HEUR-extrait]
Sample de cuivre staccato + copie à +1 octave, EQ corps (bas-médiums) + présence, chaque couche traitée séparément, distorsion, compression, reverb, sidechain. Fiche hard dance lue : pile de saws détunées, attaque/decay rapides sans sustain, 300 Hz–6 kHz, compression serrée, reverb courte.

## Live natif
Wavetable 2 osc saw unison Classic 8 voix, LP ≈ 5 kHz avec enveloppe, drive modéré [HEUR-lu] ; Saturator Hard Curve → Multiband Dynamics OTT → Reverb ; Auto Filter Peak pour le screech.

## Tests [TEST]
Mono : le lead ne s'effondre pas (réduire Width, garder l'octave basse) · niveau du screech après distorsion compensé · aucun LFO synchronisé hérité d'une source sans BPM · CPU : Hyper plutôt que 16 voix.
