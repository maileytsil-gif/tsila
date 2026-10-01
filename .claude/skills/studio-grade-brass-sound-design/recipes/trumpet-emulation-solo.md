# Trompette solo émulée (et sourdine harmon)

Émulation réaliste d'un cuivre soliste par synthèse soustractive, d'après le patch théorique et les patchs Minimoog/SH-101 de Gordon Reid (`../references/brass-acoustics.md`), complété par les formants mesurés (Maresz 2026) et les tessitures MuseScore. Pour un réalisme supérieur, préférer un multisample (`horn-section-realistic-sampled.md`) ; cette recette vaut quand le son doit rester un synthé pilotable et reproductible.

## Cible
`LEAD ou LINE / registre trompette sonnant E2–C#5 (MIDI 52–85, zone confortable 52–80) [DOC MuseScore] / notes tenues et phrases legato / BRASS OWNS HOOK ou VOICE OWNS HOOK, BRASS ANSWERS`

## Architecture
- CORPS : **une** dent de scie, une octave au-dessus du clavier si le clip est écrit au registre piano [DOC].
- ATTAQUE : ampli rapide, growl bref sur le cutoff.
- BRILLANCE : enveloppe de filtre plus lente que l'ampli, vélocité → quantité, molette → cutoff.
- SOUFFLE : bruit passe-bande très faible.
- EXPRESSION : vibrato retardé 5 Hz, legato sans retrigger.
- SECTION : aucune (soliste).
- ESPACE : pièce courte ou plate.

## Serum 2 [HEUR sauf mention]
| Section | Réglage | Preuve |
|---|---|---|
| OSC A | Basic Shapes, position dent de scie, unison **1**, octave +1 si nécessaire, niveau ≈ 50 % | [DOC] scie unique, niveau modéré (SS26) |
| OSC B, Sub | off | [DOC] pas de second oscillateur pour un soliste |
| NOISE | bruit blanc, niveau −30 à −40 dB, routé vers le filtre, suit Env 1 | [DOC] principe, niveau [HEUR] |
| Filtre 1 | **MG Low 24** (ladder), cutoff ≈ 150–250 Hz au repos, résonance 10–20 %, `Key` track ≈ 90–100 % [DOC ladder existe] | [DOC] tracking ≈ 95 %, Q léger |
| Env 1 (ampli) | A 40–100 ms, D 0, S 100 %, R 60–120 ms | [DOC] A 100 ms, R court non nul |
| Env 2 → cutoff | quantité +60–75 %, **A 300–600 ms, D 600–800 ms, S 50–60 %**, R 100 ms | [DOC] 600/800/5 (Minimoog) |
| Matrice | Velocity → quantité d'Env 2 (aux source sur la ligne Env 2 → cutoff) ; Velocity → A d'Env 1 négatif (attaque plus courte fort) ; Modwheel → cutoff +20 % ; Aftertouch → cutoff | [DOC] vélocité → quantité et attaque, aftertouch → brillance ; matrice Serum 2 : Velocity, Modwheel, Aftertouch disponibles [DOC] |
| LFO 1 (growl) | triangle, **80 Hz** (mode Hz, non synchronisé), mode **Env**, → cutoff ±10–20 %, `Rise` 0, forme dessinée en AD qui retombe en 50–150 ms | [DOC] 80 Hz, ≈ 50 ms ; LFO mode Env + Rise [DOC] |
| LFO 2 (vibrato) | sinus 5 Hz → pitch ±4–8 cents, `Rise`/Delay 300–600 ms | [DOC] 5 Hz, très faible, retardé |
| Voix | Mono, **Legato**, Portamento 0 (ou 20–40 ms en mode legato pour les liaisons) | [DOC] pas de retrigger en legato |
| FX | EQ : deux cloches fixes (formants) **≈ 1 050 Hz Q 2 +3 dB** et **≈ 1 300 Hz Q 3 +2 dB** ; Compressor léger ; Reverb plate 1,2 s, pré-delay 20 ms, mix 12 % | formants [DOC Maresz Fp 1 046 ± 98 Hz], gains [HEUR] |

## Ableton Live 12 natif
- **Analog** (voir `../references/ableton-brass-design.md`) : Osc 1 saw, Osc 2 off, filtre LP 24, Env de filtre plus lente que l'ampli, LFO 1 pour le growl si sa vitesse le permet, sinon Operator.
- **Operator** : algorithme à porteuse unique (n° 11, D seul actif) avec onde Saw, filtre LP 24 `Play by Key`, Filter Env A 500 ms / D 800 ms / S 50 %, Freq < Vel, Freq < Env ≈ 40 %, LFO plage Hi triangle 80 Hz vers FIL avec enveloppe de LFO courte [DOC Operator LFO Hi 8 Hz–12 kHz, enveloppe de LFO], Voices = 1 pour le legato [DOC].
- Suivi : `ppal-read-device` avant/après, niveau `lom.py meters` (`../../vst-sound-design/SKILL.md`).

## Processing
`Pro-Q 4 → formants fixes (cloches ci-dessus) et coupe-bas 120 Hz → test A/B` · `API-2500 → tenue de la ligne, 2:1, attaque 10 ms, release auto, 1–2 dB → la phrase reste égale sans écraser les attaques` · `Reverb native ou envoi commun → distance → mix 10–15 %, retour coupé sous 200 Hz`.

## MIDI et jeu
Ce qui fait le réalisme est dans le clip : vélocité 60–110 avec accents sur les têtes de phrase, notes liées en legato (chevauchement 10–20 ms), respiration toutes les 2–4 mesures (silence ≥ 1/8), vibrato par CC1 ou pitch bend en fin de tenue, scoop occasionnel par pitch bend −50 cents remonté en 40 ms, fall en fin de phrase par pitch bend descendant sur 200–400 ms [HEUR ; MusicXML définit scoop/fall DOC]. Voir `../references/sampled-brass-midi-programming.md`.

## Tests [TEST]
1. Vélocité 40 puis 120 sur la même note : le timbre s'assombrit puis s'ouvre, pas seulement le niveau.
2. Note tenue 4 s : le vibrato n'apparaît qu'après 300 ms et reste discret.
3. Legato deux notes : aucun second growl sur la seconde note.
4. Registre 52 → 85 : pas de note trop brillante en haut (baisser le tracking à 90 %) ni sourde en bas.
5. Dans le mix avec la voix : la trompette répond dans les trous ou double à l'octave.
6. Mono : identique (patch mono par construction).

## Variante — sourdine harmon
Même patch + Filtre 2 en **passe-bande** ou cloche étroite **≈ 2 350 Hz Q 4 +6 dB** [DOC Maresz : formant harmon 2 358 Hz], coupe-bas 400 Hz, corps réduit de 6 dB, résonance 25 % ; « wah » de plunger par macro sur la fréquence de cette cloche (800 → 2 400 Hz) [HEUR]. Sourdine cup : passe-bande 800–1 200 Hz, brillance −6 dB [HEUR-extrait UNSW].
