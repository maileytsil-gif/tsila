---
name: studio-grade-brass-sound-design
description: Concevoir, émuler, traiter et intégrer des cuivres — trompette, trombone, cor, tuba, saxophones de section — et des cuivres électroniques (synth brass analogique et FM, braam cinématique, accords future bass, horn trap/drill, horn stabs house/UKG, lead de festival, nappes et swells) dans Ableton Live 12 avec Serum 2, les instruments natifs (Analog, Operator, Wavetable, Drift, Sampler, packs Orchestral Brass / Brass Quartet), Kontakt / Session Horns si présents, et les plug-ins installés (REQ 6, Pro-Q 4, soothe3, API-2500, bx_glue, J37, Imager). Utilise ce skill dès que l'utilisateur parle de cuivres, trompette, trombone, cor, sax, section, horns, brass, stab de cuivres, fanfare, braam, « Jump », DX7 brass, ou veut « des cuivres sur le refrain », « un riff de section », « un hit cinématique » — même en deux mots. Recettes avec preuves [DOC]/[HEUR]/[TEST], corpus documentaire local, écriture de section et programmation MIDI réaliste, validation mesurée. Appelé par sound-designer-serum ; s'appuie sur vst-sound-design, midi-expressif, compositeur-arrangeur, effets-plugins.
---

# Studio-Grade Brass Sound Design — v1

Ce skill construit des cuivres **qui fonctionnent dans le morceau** : une trompette émulée qui répond à la voix, une section qui respire, un braam qui tient en mono, un stab qui tombe sur le bon contretemps. Il ne revendique aucune affiliation à un studio, un label ou un artiste. Il suit les règles communes des rôles (`../sound-designer-serum/SKILL.md`) : capacités vérifiées avant d'agir, session préservée (anti hot-swap), chaque réglage relu ou capturé, jamais « entendu » sans mesure.

## Ordre de lecture obligatoire
1. `references/source-authority.md` — d'où viennent les faits, et ce qui n'a pas pu être lu.
2. `references/brass-acoustics.md` — ce qu'il faut reproduire (Synth Secrets 24-27, formants, brassiness).
3. `references/brass-architecture.md` — sept fonctions, deux familles, rôle et propriété du médium, ordre de construction.
4. `references/genre-brass-specifications.md` — tessitures, formants, spécifications par style.
5. Le moteur : `references/serum2-brass-design.md`, `references/ableton-brass-design.md` ou `references/sampled-brass-midi-programming.md`.
6. La recette pertinente dans `recipes/`.
7. `references/modulation-expression.md`, puis `references/horn-section-writing.md` si une section est en jeu.
8. `references/plugin-role-matrix.md` et `references/mix-integration.md`.
9. `references/validation-protocol.md`, `references/macro-bridge-schema.md`, `references/output-schema.md`.
10. `references/registre-recherche.md` avant d'affirmer qu'une chose « n'existe pas » ou « est documentée ».

## Système de preuve
- **[DOC]** : documenté par un constructeur, une donnée d'usine décodée, du code source ou un article de référence lu intégralement.
- **[DOC-EXTRAIT]** : phrase d'une page officielle connue seulement par extrait (page bloquée depuis le conteneur).
- **[HEUR]** : point de départ de production, tutoriel ou preset communautaire lu ; **[HEUR-extrait]** si seulement en extrait.
- **[TEST]** : dépend du Set réel, de la banque installée, de la version, du tempo, du monitoring.
- **[MÉMOIRE, non vérifié]** : signalé comme tel, jamais transformé en règle.
Ne jamais transformer une plage `[HEUR]` en « règle constructeur ». Un réglage Serum 2 n'est acquis que si la capture le montre.

## Architecture universelle d'un cuivre
Sept fonctions indépendantes (`brass-architecture.md`) : **CORPS** (série harmonique, registre) · **ATTAQUE** (coup de langue, growl d'installation) · **BRILLANCE** (le spectre qui s'ouvre avec la force et après le niveau — la signature) · **SOUFFLE** (bruit façonné) · **EXPRESSION** (vibrato retardé, swell, fall, legato) · **SECTION** (plusieurs instruments, pas un unisson) · **ESPACE**.

Principe critique : **la brillance arrive après le niveau et suit la force de jeu**. Ampli rapide, filtre (ou index FM, ou skew de table) plus lent, vélocité vers la quantité d'enveloppe, molette ou aftertouch vers le cutoff en tenue [DOC Reid 25-26, DX7 BRASS 1, Vital, Surge]. Sans cela, rien ne sonne cuivre, quel que soit le moteur.

Deux familles, deux règles : **émulation** (un oscillateur ou un multisample, pas de désaccord, réalisme dans le MIDI) et **cuivre électronique** (unisson, détune, tables, FM, mouvement et traitement assumés).

## Rôle et propriété du médium
Toujours nommer : `LEAD / HOOK / STAB / LINE / PAD / HIT` et `BRASS OWNS HOOK / VOICE OWNS HOOK, BRASS ANSWERS / BRASS ACCENTS / BRASS IN BACKGROUND`. Deux éléments ne possèdent pas 1–4 kHz en même temps ; sur un morceau à voix, les cuivres jouent dans les trous ou à l'octave.

## Choix du moteur
- **Serum 2** : émulation soustractive contrôlée (scie unique + ladder + LFO Env pour le growl), multisample d'usine (`Factory/Winds/` : cors, trompettes, trombones) ou perso (SFZ), spectral, sample one-shot (`Factory/Brass/`), synth brass et cuivres électroniques avec macros ; réglages par clics et captures, rien d'exposé à l'API sans configuration.
- **Live 12 natif** : Analog (synth brass, vibrato retardé natif, filtre formant), Operator (FM 1:1, feedback, LFO audio pour le growl, Voices = 1), Wavetable, Drift, Sampler/Simpler, packs Orchestral Brass et Brass Quartet (articulations par macro de Rack) ; tout relisible par `ppal-read-device`.
- **Banques** : Session Horns Pro dans Kontakt Player si possédé (Smart Voice Split, 34 articulations), Kontakt Factory Library 2 ; écran seulement.
Justifier le choix en une phrase ; préférer le natif quand la reproductibilité compte plus que le timbre.

## Familles couvertes (recettes)
| Famille | Recette |
|---|---|
| Trompette solo émulée, sourdine harmon | `recipes/trumpet-emulation-solo.md` |
| Synth brass lead mono (Minimoog, SH-101, CS-80) | `recipes/mono-synth-brass-lead.md` |
| Synth brass poly 80s (Juno, Jupiter, « Jump », JX-3P) | `recipes/analog-poly-brass-80s.md` |
| Cuivre FM (Chowning, DX7 BRASS 1-3, Operator) | `recipes/fm-brass-dx7-operator.md` |
| Section réaliste échantillonnée | `recipes/horn-section-realistic-sampled.md` |
| Lignes afro et funk | `recipes/afro-funk-horn-lines.md` |
| Horn stabs house, disco, french house, UKG | `recipes/horn-stabs-house-disco.md` |
| Braam, hit cinématique | `recipes/braam-cinematic-brass-hit.md` |
| Accords « brass » future bass | `recipes/future-bass-supersaw-brass.md` |
| Horn trap / drill, brass stab | `recipes/trap-drill-dark-brass.md` |
| Nappe, swell, fanfare, riser de section | `recipes/synth-brass-pad-swell.md` |
| Lead de festival, screech hardstyle | `recipes/festival-lead-screech.md` |

## Ordre de construction
1. Rôle, propriété du médium, registre réel du clip (C3 = 60), durée des notes, BPM, formation.
2. Famille (émulation ou électronique) et moteur, justifiés.
3. CORPS + enveloppe d'ampli ; BRILLANCE : enveloppe plus lente, vélocité, molette.
4. Jouer le clip réel : registre complet, vélocités basses et hautes, legato ; **corriger le MIDI avant le son** (`sampled-brass-midi-programming.md`, `../midi-expressif/SKILL.md`).
5. ATTAQUE (growl, stab), SOUFFLE, EXPRESSION.
6. SECTION seulement si le rôle l'exige, mono vérifié ; voicings depuis l'accord (`horn-section-writing.md`, `../compositeur-arrangeur/SKILL.md`).
7. ESPACE et traitement, chaque plug-in avec son problème écrit (`plugin-role-matrix.md`).
8. Macros (4–8, `macro-bridge-schema.md`), preset sauvé sous un nouveau nom, niveau relevé.
9. Validation (`validation-protocol.md`), réponse au format (`output-schema.md`), journal dans la mémoire du projet (`../memoire-projet/SKILL.md`).

## Politique des plug-ins tiers
Chaque plug-in résout un problème nommé : `REQ 6 (coupe-bas, boue) → Pro-Q 4 ou soothe3 (dureté mesurée contre la voix) → API-2500 (tenue) → J37 léger → reverb commune` ; bus de section `bx_glue parallèle → REQ 6 → Imager (stabs mono seulement)`. Comparer à niveau égal ; retirer ce qui n'apporte rien.

## Macros minimales recommandées
Brightness · Bite · Breath · Vibrato · Section · Space · Fall · Drive — plages sûres et valeur par défaut pour chacune ; la dynamique note à note et les articulations restent dans le MIDI (vélocité, CC1, CC11, keyswitches).

## Corpus documentaire local
Tout ce qui a été lu est conservé dans `../../../corpus/` (Synth Secrets intégral, manuel Live 12, ROM DX7 décodée, Juno d'usine, patchs Surge/Vital, formants, tessitures, rapports de recherche) avec un index et des scripts pour Qwen/Ollama (`corpus/README.md`). Lire le fichier local avant de chercher en ligne ; les pages bloquées depuis le cloud sont listées dans `corpus/sources-a-telecharger.json` à télécharger sur le Mac.

## Exigences de sortie
Toute réponse donne : style/BPM/tonalité/rôle/registre ; propriété du médium ; architecture en sept fonctions ; moteur justifié ; paramètres de départ avec leurs tags ; modulation et macros ; chaîne de traitement avec raison par plug-in ; intégration (voix, pans, bus, MIDI) ; au moins 4 tests `[TEST]` dont vélocité basse/haute, avec la voix, mono ; ce qui doit être mesuré ou écouté par l'utilisateur ; une variante.

Ne jamais déclarer un cuivre « réaliste », « pro » ou « prêt » sans l'avoir joué sur tout le registre, à deux vélocités, avec la voix et en mono.

## Passer la main
Notes, voicings, registre → `compositeur-arrangeur` ; placement rythmique des stabs → `producteur-rythmique` ; le son est bon seul mais se bat avec la voix ou le kick → `ingenieur-mixage` ; référence audio disponible → `synthese-reference` ; capture d'une phrase pour en faire des stabs → `resampling`.
