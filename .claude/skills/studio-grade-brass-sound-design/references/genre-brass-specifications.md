# Spécifications par instrument et par style

## Registres et formants des cuivres réels

Tessitures **sonnantes** en MIDI (C3 = 60 dans ce projet ; les sources notent C4 = 60, la conversion est faite), d'après MuseScore 3.6.2/4.4.4 `instruments.xml` [DOC], recoupé music21 et Abjad [DOC] (`../../../../corpus/cuivres/musescore-instruments-tessitures-cuivres.md`). « Confort » = plage amateur MuseScore, « pro » ajoute pédales et suraigu.

| Instrument | Confort (MIDI) | Pro (MIDI) | Transposition écrit → sonnant | Formant principal [DOC Maresz 2026] | Autres repères |
|---|---|---|---|---|---|
| Trompette si♭ | 52–80 | 52–85 | −2 st | F1 786 Hz (très variable selon la nuance), **Fp 1 046 ± 98 Hz** ; + harmon : 2 358 Hz | zone « sweet » 67–79 [HEUR] ; pavillon ne réfléchit plus au-dessus de ≈ 1 500 Hz [HEUR UNSW] ; embouchure ≈ 750–820 Hz [HEUR] |
| Bugle | 52–79 | 52–82 | −2 st | — | timbre entre trompette et cor [DOC-W] |
| Cor en fa | 41–69 | 31–77 | −7 st | F1 388 Hz, **Fp 738 ± 112 Hz**, F2 1 106 Hz ; bande utile 600–1 400 Hz | attaque mesurée ≈ 107 ms [HEUR] |
| Trombone ténor | 40–71 | 36–74 | 0 | **F1 237 Hz** ; pavillon ≈ 700–800 Hz [HEUR] | glissando ≤ triton [DOC-W] ; pédale si♭1 (34) fréquente en commercial ; attaque ≈ 46 ms [HEUR] |
| Trombone basse | 32–65 | 21–77 | 0 | ≈ trombone | — |
| Tuba | 28–58 | 22–72 | 0 | **F1 226 Hz** | cuivre moins que le trombone (perce conique) [DOC LAUM] |
| Sax soprano | 56–87 | 56–91 | −2 st | — | — |
| Sax alto | 49–80 | 49–92 | −9 st | **F1 398 Hz** ; enveloppe spectrale coupée vers 837 Hz [HEUR-extrait JASA] | — |
| Sax ténor | 44–75 | 44–87 | −14 st | coupure ≈ 618 Hz [HEUR-extrait] | — |
| Sax baryton | 36–68 | 36–80 | −21 st | — | — |

Repères larges HyperPhysics [HEUR-extrait] : trompette 1 200–1 400 Hz, trombone 600–800, cor 400–500, tuba 200–400. Sourdines : cup ≈ passe-bande 800–1 200 Hz ; harmon ≈ pic 1 500–2 400 Hz + wah ; straight « middle-bright » ; bucket très assourdi ; plunger = wah manuel ; toutes agissent surtout au-dessus de 1 kHz [HEUR-extrait UNSW, DOC Maresz pour harmon].

Équilibre de section [DOC Rimsky-Korsakov] : en forte, 1 trompette = 1 trombone = 1 tuba = 2 cors ; en piano tous à égalité.

## Cuivres électroniques : spécifications de départ par style [HEUR sauf mention]

| Style | BPM | Rôle du cuivre | Source | Enveloppe / durée | Registre MIDI | Mouvement | Traitement type |
|---|---|---|---|---|---|---|---|
| Synth pop / synthwave 80s | 100–120 | stab, pad, hook | 2–3 scies détunées ou unison 7–9 [DOC Surge Sawteeth : 9 + 8 voix, 12/20 cents, LP 12 dB] | stab A 4–40 ms gate ; pad A 300–600 ms | accords 48–72, lead 60–79 | vibrato molette/aftertouch, cutoff ← vélocité | chorus, delay pointé, plate 1–2 s |
| Future bass | 140–160 (ressenti 70–80) | accords « brass » supersaw | unison 7, detune 0,12, blend 75 % ; 3 notes max | A 5–20 ms, S élevé | 60–84, maj9/m9/add9 | pitch ±10–50 cents à 1/8–1/16 ; LFO cutoff/volume | HPF 250 Hz, OTT 20–45 %, sidechain 4–6 dB, grande reverb |
| Trap / drill | 130–145 | horn lead sombre, stab | scie 4–6 voix (+ scie +12) [DOC Vital Mid Horn : 14 + 13 voix, LP 942 Hz] | A 6 ms, D 150 ms, S 75 %, R 1,5 s | 55–70 | scoop −7 st en 80 ms sur les stabs [DOC Vital] | distorsion, OTT, reverb 4 s, mono porta 50 ms |
| Braam / cinématique | libre | hit, drone d'impact | 5 scies ±1 % + octaves + sub [DOC synthdef] ; ou unison 16 −12 st + sub sinus + bruit [DOC Vital] | A 50 ms, D 2–3 s | C1–C2 (24–36) | pitch drop −2 à −12 st sur la queue, LP 3,2 kHz → 200 Hz en 1,5 s | drive, OTT, reverb 5–6 s, EQ −11 dB à 98 Hz sur la scie |
| Big room / festival | 126–132 | lead 1–2 notes | unison 7 detune 0,25–0,30 + B −1 oct 3 voix −6 dB | A 0, S 95 % | 60–79 | filtre brillant | flanger léger, reverb, sidechain |
| Hardstyle screech | 148–160 | stab/lead distordu | 2 × 7–16 voix, très détunées, B +1 oct | pitch env DEC/AMT | 60–84 | LFO pitch ≈ 20 Hz, LFO Env → tune | distorsion, Peak 12 résonant, resample |
| House / disco / french house | 120–128 | stab sur contretemps | sample de section staccato ou synth 300 Hz–6 kHz | decay 150–400 ms, reverb gatée | voicings sans fondamentale 55–75 | LP 200 Hz → 8 kHz automatisé, phaser | compression, slapback, sidechain |
| UK garage | 130–140 | horn stab | trompette samplée ou synth brillant 500 Hz–5 kHz | staccato | m7/m9/7sus4, 55–75 | filtré | reverb courte, slapback |
| Afrobeat / afro house / dancehall | 100–130 | section réelle : stabs contretemps, unisson, call-and-response | Session Horns / samples ; 3 instruments (bari, trompette, ténor chez Fela) | staccato, fp | 52–80 | tierces/sixtes parallèles | slapback court, room, présence 2–4 kHz |
| Funk / soul / pop | 90–120 | stabs dans les trous de la voix, riffs unisson, tenues | section réelle ou synth brass | staccato 20–30 % du temps ; tenues ≤ 2 mesures | 2 tpt + sax + tbn | falls, doits, shakes | bus glue 2,5:1, HPF 150 Hz, −2 dB 400 Hz, +2 dB 2,5 kHz |

Les valeurs de LFO synchronisées des sources ne donnent jamais leur BPM : retransposer au tempo du Set. Aucune source lue ne documente de cuivres dans l'amapiano ni chez Keinemusik/Black Coffee ; le saxophone y apparaît en live seulement [HEUR-extrait].
