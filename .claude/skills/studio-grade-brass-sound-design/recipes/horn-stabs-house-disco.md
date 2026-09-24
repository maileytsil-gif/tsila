# Horn stabs house, disco, french house, UK garage

Le stab de cuivres échantillonné, filtré, pitché, joué sur les contretemps. Sources : fiches de genre lues [HEUR-lu], extraits Wikipédia « French house » et forums [HEUR-extrait], rebuild du stab M1 [HEUR-lu].

## Cible
`STAB / 120–140 BPM / voicings sans fondamentale 55–75, m7-m9-7sus4 (UKG), stabs orchestraux (Chicago/Detroit) / BRASS ACCENTS`

## Source
1. Section de cuivres réelle jouée staccato (Orchestral Brass, Session Horns Pro, Serum 2 Multisample `Trumpets LE`) puis **resamplée** en audio (`../../resampling/SKILL.md`) : un stab d'accord de 3–4 notes, 300–600 ms.
2. Sample d'usine Serum 2 `Factory/Brass/Brass Wall Low.flac` ou `DX Brass2 C2.flac` [DOC corpus] dans l'oscillateur **Sample** (one-shot, transposition, `Rate`) [DOC-EXTRAIT].
3. Vieux disque funk/soul : « pitched-up EQ'd brass stab with pitch envelope » [HEUR-extrait] — respecter le droit d'auteur (`../../sampling-composition-avancee/SKILL.md`).

## Traitement du stab [HEUR]
- Simpler Classic ou One-Shot : transpose ±5–7 st (le pitch-up donne le grain « rave ») ; enveloppe amp decay 150–400 ms ; **reverb gatée** ou coupée court ; **filtre LP 200 Hz fermé → 8 kHz ouvert** automatisé sur 4–16 mesures (french house), phaser léger (Phaser-Flanger) ; sidechain pompant ; delay throw 1/8 pointé en fin de phrase.
- Rebuild du stab Korg M1 (rave/jungle) [HEUR-lu] : sample brillant à attaque dure, decay 400–800 ms, passe-bande sous 200 Hz, +1–3 kHz, plate 1–1,5 s, léger chorus.
- UKG : trompette samplée ou synth brillant **500 Hz–5 kHz**, staccato, reverb courte, compression ; disco : section 300 Hz–6 kHz, présence 2–4 kHz, room.
- Piste : `REQ 6 (HP 150–200 Hz, cloche +2 dB 2,5 kHz) → API-2500 3:1 attaque 10 ms → Auto Filter automatisé → envoi reverb/delay`.

## Écriture
Stabs courts sur les contretemps et fins de phrase, voicings serrés (punch) ou larges (chaleur), harmonie réelle 3–4 voix, « une section de cuivres est une section de percussions avec des hauteurs » [HEUR-lu] ; swing des hats 52–56 % pour que les stabs respirent. Tech house (Fisher « Losing It ») : le « horn » est un synthé mono, pas un sample [HEUR-extrait].

## Tests [TEST]
Le stab reste net sous le filtre fermé (sinon garder un peu de 1–3 kHz) · la reverb gatée ne clique pas · le pitch-up ne casse pas la tonalité (relever la hauteur réelle du sample, `synthese-reference` si besoin) · mono OK.
