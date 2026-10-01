# Architecture fonctionnelle des claviers et synthés funk

Le funk se joue avant de se régler : la main (durées, ghost notes, muting, syncopes) fait plus que le patch. Les sept fonctions ci-dessous servent à décrire un son ; le MIDI se décrit avec `playing-voicings-midi.md`.

## Familles couvertes
| Famille | Instruments | Ce qui fait le son |
|---|---|---|
| Électromécaniques | Rhodes, Wurlitzer, Clavinet, Hammond + Leslie | non-linéarité de captation (bark), trémolo, étouffoirs, drawbars, cabine tournante |
| Synth bass mono | Minimoog (P-Funk, Thriller), Odyssey (Chameleon), Juno (Chromeo), DX7 BASS 1, Sub 37 | enveloppes courtes, filtre bas résonant, glide, mono legato |
| Poly analogique | Prophet-5, OB-Xa/OB-8, Juno-60/106, Jupiter-8, JX-3P | chorus, PWM, stabs à enveloppe de filtre, cuivre (voir skill cuivres) |
| FM | DX7 E.PIANO 1, BASS 1, KOTO, MARIMBA, CLAV 1, SYN-LEAD 1 ; DX100 talkbox | ratios entiers + vélocité → index |
| Leads | G-funk « whistle » (Minimoog 2'), SYN-LEAD 1, Sub 37 Cory Henry | glide, vibrato à la molette, mono |
| Voix synthétique | talkbox (Zapp, Chromeo, 24K Magic), vocodeur | source scie/pulse + formants |
| Traitement signature | phaser/chorus sur Rhodes, auto-wah sur Clav, bande, compression « pumping » (SP-303 → Vulf) | voir `plugin-role-matrix.md` |

## Les sept fonctions
1. **CORPS** — le mécanisme : tine + tonebar (Rhodes), anche + pickup capacitif (Wurli), corde frappée par un pad et étouffée par un fil (Clav), 9 sinus (Hammond), oscillateurs (synth). Choisir le moteur qui modélise ce mécanisme ou qui le sample (`ableton-keys-design.md`, `serum2-keys-design.md`).
2. **ATTAQUE** — marteau et bruit d'impact (Electric Hammer Noise), clic de contact (Hammond 1–3 ms), « hammer-on » du Clav, coup de langue de la talkbox, transitoire d'un slap FM (DX7 BASS 1 ratios 5 et 9).
3. **DYNAMIQUE** — la vélocité change le timbre, pas seulement le niveau : bark Rhodes = harmonique 2 qui monte avec la force (position/distance tine-pickup) [HEUR/DOC secondaire] ; Wurli = non-linéarité 1/(1−y) du pickup [DOC openwurli] ; DX7 E.PIANO 1 = KVS 7 sur le modulateur 14:1 [DOC] ; Hammond = aucune vélocité [DOC].
4. **MOUVEMENT** — trémolo panoramique Suitcase (Speed/Intensity, forme triangle [HEUR]), trémolo Wurli 5,6 Hz fixe qui module le gain du préampli [DOC], vibrato/chorus scanner Hammond ≈ 7 Hz [DOC], Leslie (horn 0,67 → 7,06 Hz, tambour 0,60 → 5,96 Hz, rampes différentes [DOC setBfree]), auto-wah piloté par l'enveloppe (Mu-Tron III), PWM lente (Juno), glide (Minimoog, Sub 37).
5. **ARTICULATION** — staccato et muting du Clav, ghost notes du comping, legato sans retrigger du synth bass (Drift/Analog/Operator Voices = 1, Serum Mono + Legato), single-trigger de la percussion Hammond.
6. **TRAITEMENT** — phaser (Small Stone / Phase 90) et chorus sur Rhodes, Dyno (EQ 2 bandes + stéréo), ampli Twin repiqué au SM57 (Breakbot), compression opto (CLA-3A chez Ronson/Bhasker), « pumping » lo-fi (SP-303 → Vulf Compressor, sans threshold ni ratio [DOC-EXTRAIT]), bande (J37, Studer sur RAM).
7. **ESPACE** — room courte ou plate, slapback ; le Rhodes est souvent sec et le Clav toujours ; le Leslie est lui-même un espace.

## Propriété du registre
| Question | Réponses documentées |
|---|---|
| Qui possède le grave ? | basse électrique seule ; synth bass seule (Flash Light, Canned Heat) ; **doublage** (Jamiroquai : Toby Smith double la basse au Minimoog/Moog Source/Clavinet/Supernova [HEUR-extrait]) ; **alternance** : la basse électrique « pop » dans les trous de la synth bass (Premier Guitar [HEUR-extrait]) ; couches (Don't Start Now : sample réaliste + sub + slaps + synth [DOC-EXTRAIT SOS]) |
| Qui possède le médium ? | guitare rythmique ou Clav, rarement les deux à pleine longueur ; Rhodes en accords « à trous » (« laisse un trou spectral là où est la voix » [DOC-W]) |
| Où est la voix synthétique ? | talkbox = lead ou hook (24K Magic intro), jamais en même temps que le chant principal |

## Ordre de construction
1. Style, BPM, rôle, registre du clip, qui possède le grave et le médium.
2. Moteur (modèle physique, sample, synthèse) justifié en une phrase.
3. CORPS + DYNAMIQUE : jouer à vélocité 40 et 110 avant tout autre réglage.
4. ATTAQUE et release (dampers courts, étouffement, clic).
5. Le clip réel : durées, ghost notes, muting, swing (`playing-voicings-midi.md`) — corriger le MIDI avant le son.
6. MOUVEMENT : trémolo, Leslie, auto-wah, glide, avec leurs vitesses documentées.
7. TRAITEMENT dans l'ordre historique (instrument → ampli/DI → phaser/chorus → compression → bande), chaque plug-in avec son problème écrit.
8. Intégration (basse, guitare, voix), mono vérifié.
9. Macros, preset sauvé, validation (`validation-protocol.md`), réponse au format (`output-schema.md`).
