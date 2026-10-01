# Synth brass lead monophonique (Minimoog, SH-101, CS-80 swell)

Le cuivre « synthé » assumé : lead ou riff mono, gras, avec le « wow » du filtre. Sources : Reid SS26-27 [DOC] ; patchs de Tom Rhea et Roland [DOC] ; recette CS-80 tierce [HEUR].

## Cible
`LEAD ou HOOK / C2–C5 (C3 = 60) / riffs syncopés ou lignes tenues / BRASS OWNS HOOK`

## Architecture
CORPS : 1 scie (solo) ou 2–3 scies à l'unisson (tutti « Rhea ») · ATTAQUE : growl bref · BRILLANCE : filtre fermé, env +65 % lente · EXPRESSION : molette → growl, pitch bend → vibrato manuel · ESPACE : delay court.

## Réglages de départ (transposés des synthés d'origine)
| Paramètre | Solo (Reid, Minimoog) [DOC] | Tutti (Rhea) [DOC] | Tuba / trombone (Roland SH-101) [DOC] |
|---|---|---|---|
| Oscillateurs | 1 scie, 4' | 3 scies unisson, léger désaccord | scie 60 % + carré −1 octave 100 % |
| Niveau osc | 5/10 (pas de saturation du filtre) | idem | idem |
| Ampli | A 100 ms, S max, R ≈ 0 | A un peu plus lente, petit release | gate (carré) |
| Filtre | cutoff 0, env 6,5/10, Q 2/10, tracking 100 % | cutoff plus haut, env plus faible, Q 0, tracking 66 % | cutoff ≈ 0, env max, Q « une touche » |
| Env filtre | A 600 / D 800 ms / S 5/10 | A plus rapide | A 20 % / D 50 % / S 50 % / R 2 |
| Growl | Osc 3 triangle 32' → cutoff, molette | aucun | LFO triangle max → cutoff 60 % → 0 % |
| Vibrato | manuel, pitch wheel | manuel | bender |

Serum 2 : OSC A scie ; pour le tutti, unison **3**, detune 0,05–0,08, blend 75 % [DOC BLEND défaut], width 30 % ; Filtre MG Low 24 ; Env 2 → cutoff comme ci-dessus ; LFO 1 triangle 80 Hz mode Env → cutoff pour le growl ; Macro 1 = quantité de growl (molette). Mono Legato, portamento 30–60 ms sur les liaisons pour un lead « Moog » [HEUR].

Operator : porteuse unique Saw ou algorithme 11 avec trois oscillateurs Saw à Fine 0/+3/−3 (tutti), filtre LP 24 Play by Key, Freq < Env, LFO Hi 80 Hz → FIL avec enveloppe de LFO ; `Spread` pour le stéréo du tutti (coûteux en CPU [DOC]).

## Processing
`Saturator natif ou J37 → deux ou trois harmoniques de plus sans changer le filtre → drive 2–4 dB, A/B` · `Delay 1/8 pointé, feedback 20 %, mix 10 % → réponse en fin de phrase` · `Chorus-Ensemble léger uniquement sur le tutti` [HEUR].

## Variante — CS-80 « brass swell » [HEUR]
Recette tierce (Hydrasynth, citant SOS 26 et un tutoriel CS-80 ; `../../../../corpus/synthes-vintage/hydrasynth-recettes-archetypes.md`) : 2 scies (+8 cents) + scie −12 st à 60 %, LP ladder 24 cutoff bas, résonance 20 %, env → filtre +50 %, key track 40 % ; Env filtre A long (≈ 1–2 s) / S 70 % / R long ; Env ampli A ≈ 1 s ; **aftertouch → cutoff** ; chorus 55 %, hall 4 s. L'enveloppe du CS-80 a un niveau initial et un niveau d'attaque (IL/AL) sans sustain [DOC SS8] : dans Serum 2, LFO en mode Env dessiné avec un palier initial.

## Tests [TEST]
Riff syncopé : les notes courtes gardent le « wow » (raccourcir A du filtre à 150–250 ms sinon) · molette à zéro puis à fond : growl absent puis présent, sans changement de hauteur · tutti en mono : pas de creux · niveau relevé avant/après drive.
