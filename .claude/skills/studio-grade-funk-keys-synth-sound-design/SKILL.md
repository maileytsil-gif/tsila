---
name: studio-grade-funk-keys-synth-sound-design
description: Concevoir, émuler, jouer, traiter et intégrer les claviers et synthés du funk moderne dans Ableton Live 12 — Rhodes, Wurlitzer, Clavinet, Hammond + Leslie (Electric, Tension, packs Electric Pianos / Clav / Electric Keyboards, Scarbee), synth bass Minimoog / Odyssey / Juno / DX7 (Drift, Analog, Operator, Serum 2), stabs Oberheim / Prophet, lead G-funk, talkbox Zapp / Chromeo / 24K Magic (Vocoder, formants), basse en couches nu-disco, chaîne « pumping » SP-303 / Vulf, avec auto-wah, phaser, trémolo, chorus, bande, compression (Auto Filter, Phaser-Flanger, Auto Pan-Tremolo, Chorus-Ensemble, J37, API-2500, bx_glue, soothe3). Utilise ce skill dès que l'utilisateur parle de funk, boogie, P-Funk, G-funk, néo-soul, nu-disco, Rhodes, Wurli, Clav, orgue, B3, Leslie, synth bass, talkbox, Vulfpeck, Bruno Mars, Chromeo, Kaytranada, « comping », « stab », « clavier funky », « Superstition », « Flash Light », « Chameleon » — même en deux mots. Recettes avec preuves [DOC]/[HEUR]/[TEST], données d'usine décodées (DX7, Juno), voicings et grilles MIDI chiffrés, corpus documentaire local. Appelé par sound-designer-serum et compositeur-arrangeur ; s'appuie sur vst-sound-design, midi-expressif, producteur-rythmique, effets-plugins, kick-bass-equilibre.
---

# Studio-Grade Funk Keys & Synth Sound Design — v1

Ce skill construit des claviers et synthés funk **qui groovent dans le morceau** : un Rhodes qui aboie seulement quand on le frappe, un Clavinet qu'on n'entend que par doubles-croches, un synth bass qui laisse le kick sur le un, une talkbox qui parle. Il ne revendique aucune affiliation à un artiste, un studio ou un label, et ne présente jamais un réglage tiers comme « le son de » quelqu'un. Il suit les règles communes des rôles (`../sound-designer-serum/SKILL.md`) : capacités vérifiées, session préservée, chaque réglage relu ou capturé, jamais « entendu » sans mesure.

## Ordre de lecture obligatoire
1. `references/source-authority.md` — provenance des faits, ce qui n'a pas pu être lu.
2. `references/keys-architecture.md` — familles, sept fonctions, propriété du grave et du médium, ordre de construction.
3. `references/electromechanical-keys.md` — Rhodes, Wurlitzer, Clavinet, Hammond + Leslie : mécanismes, valeurs documentées, erreurs classiques.
4. `references/synth-bass-leads.md` — Minimoog, Odyssey, Juno, Prophet/Oberheim, G-funk, funk moderne.
5. `references/dx7-fm-keys-bass.md` — E.PIANO 1, BASS 1, KOTO, MARIMBA, CLAV 1 décodés, transposition Operator.
6. Le moteur : `references/ableton-keys-design.md`, `references/serum2-keys-design.md`.
7. La recette dans `recipes/`.
8. `references/playing-voicings-midi.md` — voicings chiffrés, grilles, vélocités, swing, orgue en MIDI. **Corriger le MIDI avant le son.**
9. `references/genre-keys-specifications.md`, `references/modern-funk-production.md`.
10. `references/plugin-role-matrix.md`, `references/mix-integration.md`.
11. `references/validation-protocol.md`, `references/macro-bridge-schema.md`, `references/output-schema.md`, puis `references/registre-recherche.md` avant d'affirmer qu'une chose « n'existe pas ».

## Système de preuve
**[DOC]** donnée d'usine décodée, code source, manuel ou article de référence lu intégralement · **[DOC-EXTRAIT]** phrase d'une page officielle ou d'une interview connue par extrait (pages bloquées depuis le conteneur) · **[HEUR]** tutoriel ou compilation lue · **[HEUR-extrait]** tutoriel en extrait · **[TEST]** dépend du Set, de la banque, de la version · **[MÉMOIRE, non vérifié]** signalé. Ne jamais transformer une plage `[HEUR]` en règle constructeur ; un réglage Serum 2 n'est acquis que si la capture le montre.

## Principes critiques
1. **La vélocité change le timbre, pas seulement le niveau** : bark Rhodes (captation), grogne Wurli (pickup capacitif), tine FM (KVS 7 sur le ratio 14), slap FM (ratios 5 et 9) [DOC] ; le Hammond n'a pas de vélocité [DOC]. Un Saturator après l'instrument n'est pas un bark.
2. **Le funk se joue en doubles-croches et en espaces** : interlock, ghost notes 10–35, staccato 30–50 %, anticipations, « the one » ; la recherche dit qu'une grille quantifiée avec décalages **fixes par instrument** bat le jitter aléatoire [HEUR citant Frühauf, Senn, Danielsen].
3. **Les mouvements ont des vitesses documentées** : trémolo Wurli 5,6 Hz de gain (mono), trémolo Suitcase panoramique, scanner Hammond ≈ 7 Hz en C3, Leslie horn 0,67 → 7,06 Hz et tambour 0,60 → 5,96 Hz avec des rampes différentes, Mu-Tron attaque 5–8 ms / release 120–180 ms [DOC / HEUR].
4. **Qui possède le grave** : basse électrique, synth bass, doublage ou alternance (la basse « pop » dans les trous) ; main gauche sans fondamentale au-dessus de 48 quand une basse joue [DOC / HEUR].
5. **Honnêteté sur le funk moderne** : Vulf Compressor = SP-303, sans threshold ni ratio, aucun réglage signature publié ; Silk Sonic sans instrument documenté ; « Uptown Funk » = jam live, synthés « Zapp/Troutman », mix ITB.

## Familles couvertes (recettes)
| Famille | Recette |
|---|---|
| Rhodes Mark I bark, trémolo Suitcase, phaser, Twin repiqué | `recipes/rhodes-mark1-bark-electric.md` |
| Wurlitzer 200A, trémolo de gain 5,6 Hz | `recipes/wurlitzer-200a-electric.md` |
| Clavinet + envelope filter (« Higher Ground », « Superstition ») | `recipes/clavinet-funk-envelope-filter.md` |
| Hammond B-3 + Leslie (registrations, percussion, rack Leslie) | `recipes/hammond-leslie-funk.md` |
| DX7 E.PIANO 1 dans Operator | `recipes/dx7-epiano-operator.md` |
| DX7 BASS 1 slap FM | `recipes/dx7-bass1-slap-operator.md` |
| Synth bass P-Funk (« Flash Light », Thriller) | `recipes/pfunk-minimoog-bass.md` |
| Basse « Chameleon » (Odyssey 12 dB) | `recipes/chameleon-odyssey-bass.md` |
| Juno : basse sub + octave, keys en chorus | `recipes/juno-boogie-keys-bass.md` |
| Stabs Oberheim / Prophet (« 1999 », 24K Magic) | `recipes/oberheim-prophet-stabs.md` |
| Lead G-funk « whistle » | `recipes/gfunk-whistle-lead.md` |
| Talkbox (Zapp, Chromeo, Mr Talkbox) | `recipes/talkbox-zapp-modern.md` |
| Basse en couches nu-disco, Sub 37, doublage | `recipes/modern-funk-layered-bass.md` |
| Chaîne « pumping » lo-fi SP-303 / Vulf | `recipes/lofi-pumping-vulf-chain.md` |
Synth brass et cuivres : `../studio-grade-brass-sound-design/SKILL.md`.

## Choix du moteur
- **Natifs Live 12** (premier choix quand la reproductibilité compte) : Electric (Rhodes R / Wurli W, modèle physique), Tension (Clavinet approché), Drift et Analog (synth bass mono, poly 80s), Operator (DX7, orgue additif), Wavetable, packs Electric Pianos / Electric Keyboards / Clav / Microtron ; effets Auto Filter (Vowel, envelope follower), Phaser-Flanger, Chorus-Ensemble, Auto Pan-Tremolo (Panning, Tremolo Harmonic/Vintage), Pedal, Amp/Cabinet, Vocoder, Compressor/Glue, Saturator, Redux, Vinyl. Tout relisible par `ppal-read-device`.
- **Serum 2** : synth bass mono (portamento Always/Scaled, ladders MG), multisample d'usine « Elec.Piano Suitcase », samples « Bass/ » (JB/PB Fingerstyle, Alu Slap), FM from B, formants ; réglages par clics et captures.
- **NI** (si possédés [TEST]) : Scarbee Mark I / A-200 / Clavinet, Vintage Organs, Monark ; écran seulement.
Justifier le choix en une phrase.

## Ordre de construction
1. Style, BPM, rôle, registre du clip (C3 = 60), qui possède le grave et le médium.
2. Moteur justifié ; CORPS + DYNAMIQUE : jouer à vélocité 40 et 110 avant tout.
3. ATTAQUE et release (dampers, étouffement, clic).
4. Le clip réel : voicings rootless 48–72, grilles, ghost notes, muting, swing ou Track Delay fixe (`playing-voicings-midi.md`, `../midi-expressif/SKILL.md`, `../producteur-rythmique/SKILL.md`).
5. MOUVEMENT aux vitesses documentées.
6. TRAITEMENT dans l'ordre historique, chaque plug-in avec son problème écrit (`plugin-role-matrix.md`).
7. Intégration (basse, guitare, voix), mono vérifié (`mix-integration.md`, `../kick-bass-equilibre/SKILL.md`).
8. Macros, preset sauvé sous un nouveau nom, validation, réponse au format, journal (`../memoire-projet/SKILL.md`).

## Corpus documentaire local
`../../../corpus/` : manuel Live 12 ch. 28/30, Synth Secrets intégral (dont 42-43, 55-59), ROM1A/ROM1B décodées, Juno d'usine, setBfree, openwurli, STK, miroirs Wikipédia, leçons de voicings, rapports de recherche, scripts pour Qwen/Ollama (`corpus/README.md`). Lire le fichier local avant de chercher en ligne ; `corpus/sources-a-telecharger-funk.json` liste les pages à relire sur le Mac.

## Exigences de sortie
Style/BPM/rôle/registre ; propriété du grave et du médium ; architecture en sept fonctions ; moteur justifié ; paramètres nommés comme dans l'instrument avec leurs tags ; jeu et MIDI (vélocités, durées, grille) ; chaîne avec raison par plug-in ; intégration ; au moins 4 tests `[TEST]` dont vélocité basse/haute, avec basse et batterie, mono, tenue de 8 mesures ; une variante.

Ne jamais déclarer un clavier « authentique », « Vulf » ou « prêt » sans l'avoir joué à deux vélocités, avec la section rythmique et en mono.

## Passer la main
Notes, voicings, harmonie → `compositeur-arrangeur` ; groove, ghost notes, swing → `producteur-rythmique` ; grave et sidechain → `kick-bass-equilibre` ; le son est bon seul mais se bat avec la basse ou la voix → `ingenieur-mixage` ; cuivres et synth brass → `studio-grade-brass-sound-design` ; référence audio → `synthese-reference`.
