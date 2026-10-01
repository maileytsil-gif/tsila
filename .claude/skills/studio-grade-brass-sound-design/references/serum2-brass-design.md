# Serum 2 pour les cuivres

Faits constructeur : manuel Serum 2 dépouillé localement (`../../sound-designer-serum/references/moteurs-synthese.md`, `modulation-effets.md`, `serum2-fx-clip-arp.md`), manuel Serum 1.0.1 lu (contrôles LFO/voicing/unison identiques dans Serum 2 : `../../../../corpus/constructeur/`), extraits officiels xferrecords.com (site bloqué depuis le conteneur, à relire sur le Mac). Pilotage : Serum 2 n'expose rien à l'API de Live sauf paramètres mappés ; réglages par clics dans sa fenêtre et capture après chaque geste (`../../vst-sound-design/references/serum2.md`).

## Choix du moteur par famille

| Famille | Moteur OSC A | Pourquoi | Preuve |
|---|---|---|---|
| Émulation solo (trompette, cor) | **Wavetable** dent de scie, unison 1 | série harmonique complète, contrôle total de l'enveloppe de filtre | [DOC] SS24-26 |
| Émulation réaliste | **Multisample** (usine ou SFZ perso) | vraies couches de vélocité et vrai souffle | [DOC] Multisample = format SFZ ouvert ; cuivres d'usine référencés par des presets : `Factory/Winds/French Horns.sfz`, `Trumpets LE.sfz`, `Trombones Tenor LE.sfz`, `Trombones Cimbasso LE.sfz`, `Factory/Synth/Arp Solina - Horn.sfz` (corpus des 626 presets d'usine, `../../../../corpus/cuivres/`) ; contenu des « LE » à relever [TEST] |
| Tenue infinie d'une note réelle | **Spectral** (note tenue, position figée) | resynthèse harmonique en temps réel | [DOC-EXTRAIT] ; contrôle exact de la position [TEST] |
| Stab échantillonné | **Sample** (one-shot glissé) | un sample, pas de mapping | [DOC] samples d'usine `Factory/Brass/Brass Wall Low.flac`, `Trombone.flac`, `Trombone Alt.flac`, `Factory/Synth/DX Brass2 C2.flac` |
| Synth brass section | Wavetable scie, unison 2-4 | densité et désaccord voulus | [DOC] unison ≤ 16, « nombre magique 7 » trop pour un cuivre [HEUR] |
| Cuivre FM | Wavetable sinus + **Warp FM from B** Linear | index = warp amount | [DOC] trois variantes Linear/Exp/Thru-Zero |
| Braam, cuivre cinématique | Wavetable scie/pulse + Sub + Sample (hit réel) | trois couches indépendantes routées séparément | [DOC] routage Filter/Main/Direct/Bus |

Architecture relevée sur les presets d'usine [DOC] : 3 oscillateurs + Noise + Sub, 2 filtres, **4 enveloppes, 10 LFO, 8 macros**, 64 slots de matrice, 3 racks d'effets, arp et clip player ; aucun tag « Brass » dans les métadonnées, le classement par instrument passe par les dossiers.

## Réglages par fonction

**CORPS** — niveau d'oscillateur modéré ; Sub seulement pour tuba/trombone (carré −12) et braam ; `Direct` pour une couche qui doit éviter les filtres [DOC routage].

**BRILLANCE** — Filtre 1 `MG Low 12` ou `24` (ladder) [DOC types], `FAT` bas ; cutoff au repos 100–250 Hz ; `Key` track 90–100 % (idéal « un peu sous 1:1 ») ; **Env 2 → cutoff**, attaque plus lente que l'ampli (tenue : 300–600 ms ; stab : 20–80 ms), decay vers un sustain plus bas [DOC forme] ; ligne de matrice avec **aux source = Velocity** (« la vélocité décide de combien l'enveloppe ouvre le filtre » [DOC matrice]) ; **Modwheel → cutoff** et **Aftertouch → cutoff** pour la tenue [DOC sources disponibles : Velocity, Note, Pitch Bend, Aftertouch, Modwheel].

**ATTAQUE** — growl : LFO en mode **Env** (parcourt sa forme une fois) [DOC], forme triangle dessinée en AD, vitesse **Hz** (BPM off) ≈ 80 Hz [DOC SS25], → cutoff ±10–20 % [HEUR] ; scoop facultatif : Env 3 → pitch, A 0, D 30–60 ms, S 0, −0,3 à −0,5 demi-ton [HEUR ; les patchs d'usine DX7/Juno n'ont aucun scoop [DOC]]. Stab : Env 1 A 0–5 ms.

**SOUFFLE** — NOISE couleur pink ou brown [DOC-EXTRAIT couleurs], routé Filter 2 passe-bande 1–4 kHz, niveau très bas, suit Env 1, quantité sur Aftertouch [HEUR].

**EXPRESSION** — vibrato : LFO sinus 5–6 Hz → pitch (bipolaire), profondeur faible, **Delay** 300–500 ms puis **Rise** 300–600 ms [DOC Rise/Delay/Smooth existent ; valeurs HEUR], profondeur sur Modwheel (aux source) ; mode **Mono + Legato** (enveloppes non retriggées en legato [DOC]), **Porta** 30–60 ms, **Always off** (glisse seulement sur les notes liées), **Scaled on** (vitesse proportionnelle à l'intervalle) [DOC], Porta Curve convexe [DOC].

**SECTION** — unison 2–4 voix, Blend 50–75 % [DOC défaut 75 %], Width ≤ 50 % ; ou effet **Hyper** 2–3 voix, que le manuel recommande à la place d'un unison élevé pour le CPU [DOC] ; **Chorus** 4 voix rate lent [DOC] ; toujours le test mono.

**ESPACE** — **Reverb** Plate/Hall/Vintage/Nitrous/Basin [DOC 5 types] sur BUS 1 avec LO CUT ; Compressor Single 3:1 pour tenir les stabs ; **Filter FX** avec Key Track (clic droit) pour un formant qui suit ou non le clavier [DOC 2.0.17].

## Formants
Filtre 2 en `Formant`/`Vowel` (cutoff morphe entre voyelles) [DOC Serum 1, à confirmer dans 2.1.5 [TEST]] ou Peak Q modéré, en parallèle à MIX bas ; ou deux cloches fixes dans l'EQ du rack. Valeurs par instrument : `genre-brass-specifications.md`.

## Multisample perso (SFZ)
Un multisample trompette minimal = régions `sample=`, `lokey/hikey`, `pitch_keycenter`, 2–3 couches `lovel/hivel`, `ampeg_release` [DOC spécification SFZ]. Import : Load SFZ ou glisser le .sfz sur l'oscillateur, ou dossier `Serum 2 Presets/Multisamples/User` puis rescan [HEUR éditeurs tiers ; chemin Mac à vérifier [TEST]]. Crossfade CC1 (`xfin/xfout_loccN`), legato (`trigger=legato`, `sw_previous`), keyswitches (`sw_*`) : sous-ensemble lu par Serum 2 **non documenté** → tester une opcode à la fois [TEST].

## Macros (8) — voir `macro-bridge-schema.md`
Brightness = cutoff + quantité Env 2 · Bite = quantité de growl · Breath = niveau Noise · Vibrato = profondeur LFO · Section = unison detune/width · Space = send BUS 1 · Fall = Env 3 pitch négatif · Drive = Distortion mix.

## Ce que Serum 2 ne fait pas
Pas de feedback d'opérateur FM documenté [MÉMOIRE, non vérifié] ; pas de keyswitch par note (utiliser des presets ou un Rack Live avec Chain Select) ; les effets sont monophoniques (après toutes les voix) [DOC] ; aucun paramètre exposé à l'automation de Live sans configuration préalable (`../../sound-designer-serum/references/serum2-automation-et-migration.md`).
