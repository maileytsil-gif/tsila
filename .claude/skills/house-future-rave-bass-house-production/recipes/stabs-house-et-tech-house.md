# Stabs et accords : house, tech house, bass house, future rave

## Cible
`HOUSE, TECH HOUSE, BASS HOUSE, FUTURE RAVE / STAB ou CHORDS / 124–128 BPM / voicings sans fondamentale, MIDI 55–75 / sur les « et » (tech house) ou en accents syncopés 1, et-de-2, 3, et-de-4 (future rave)`

## Moteur
Serum 2 (une touche = accord par SEMI 0 / +3 / +7, ou Stack **12+7** pour octave + quinte) ; Operator ou Wavetable ; multisample M1 Organ 2 pour le stab d'orgue rave.

## Patch (valeurs mesurées dotbeat et Attack)
| Étage | Valeur | Preuve |
|---|---|---|
| Oscillateurs | 2 saws, OSC B FINE +10 cents, UNISON 3 WIDTH 55 ; ou OSC A/B/C SEMI 0 / +3 / +7 (triade mineure dans le patch ; variante +5 / +8) ; OSC C OCT −1 pour doubler la basse | `[DOC-2]` |
| FILTER 1 | MG Low 24 ; CUTOFF **300–320 Hz** (deep house 250–350), RES ≈ 18 ; **ENV 2 → CUTOFF 80 %** | `[DOC-2]` |
| ENV 1 (ampli) | A **5 ms** · D **250** · S 0 · R **31 ms** (« la queue vient des sends ») ; techno stab : A 0 · D 66 · S 0 · R 29 | `[DOC-2 mesuré]` |
| ENV 2 (filtre) | A 3 ms · D **160** · S 0 · R 50 ; vélocité → filtre 35 % ; « c'est le decay qui fait le stab » | `[DOC-2]` |
| Couche corps | −12 st, cutoff 800 Hz, à −14 dB (78,6 % des patchs Chords sont scindés à l'octave) | `[DOC-2]` |
| Saturation | Tube 20 % | `[DOC-2]` |
| Orgue rave (M1 Organ 2) | sinus ou carrées aux harmoniques 1, 2, 3, 4 avec la 3e en avant ; A instantanée, D 150–300 ms, coupure nette ; mineur ou sus4 sur contretemps ; reverb gated ; petit pitch-up à l'attaque | `[DOC-2]` |

## Voicings
3e renversement (7e en bas), **sans la fondamentale** (la basse la tient, règle Kerri Chandler), laisser les temps du kick, varier le voicing d'un même accord ; tech house : Am7 sans tonique [64 67 72 76] sur basse A1, gate ≈ 36 % d'une croche, vélocité 67–77 sur les « et » de 2 et 4 ; future rave : quinte + octave + tierce mineure ou add9, gate 30–45 %, pas 1, 7, 9, 15, vélocités 96 × {1, 0,88, 0,95, 0,9} ; jamais de triades nues sous C2 (`../references/theorie-specifique.md` § 2).

## Chaîne
Reverb sur **BUS** (fiche 35 : jamais en insert sur un patch polyphonique modulé par enveloppe), send 18 %, delay 12 % ; Hyper/Dimension ; compression parallèle −30 dB 8:1 4 ms / 100 ms mix 35 % ; EQ HP 100 Hz sauf si le stab est la basse. Bass house : reverb **avant** la distorsion (Attack : Reverb → Overdrive 13 % → Saturator 10 dB → Drum Buss 26 %), mono, Diode. Automation du dernier accord de chaque phrase.

## Erreurs
Attaque 10–30 ms (« consensus zéro » : le punch vient du decay) ; triades nues ; fondamentale doublée ; cinq notes sur une supersaw ; même largeur que le lead.

## Vérification
Stabs sur les accents de la batterie ; en mono le corps reste ; avec la basse, aucune fondamentale doublée ; swing 56 % sur les stabs house seulement si le reste swingue.
