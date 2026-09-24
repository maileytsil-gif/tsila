# Cuivre FM (Chowning 1973, DX7 BRASS 1-3) dans Operator et Serum 2

Le cuivre FM : porteuse et modulateur au rapport **1:1** (série harmonique complète), et un **index de modulation qui suit l'enveloppe** — la brillance arrive avec, puis après, le niveau. Sources : transcriptions concordantes de Chowning [DOC via transcription], ROM1A décodée [DOC] (`../../../../corpus/synthes-vintage/dx7-rom1a-32-voix-decodees.md`), Nord Modular Book [DOC], rapport axe 2.

## Cible
`LEAD, STAB ou HOOK / C2–C5 / 80s, synthwave, funk électro, hybride moderne / BRASS OWNS HOOK`

## Le principe documenté
- Chowning : porteuse 440 Hz, modulateur 440 Hz, **index 0 → 5**, note de 0,6 s ; **la même enveloppe** pilote amplitude et index : montée en 1/6 de la durée (≈ 100 ms), descente à 0,75 en 1/6, plateau 0,65 sur la moitié, retour à 0 en 1/6 [DOC transcriptions Csound/musx/CLM].
- Nord Modular Book : « modulateur à la fréquence de la porteuse ; enveloppe sur le niveau de modulation, d'où l'éclaircissement caractéristique pendant l'attaque » [DOC].
- DX7 BRASS 1 (ROM1A, voix 1) [DOC] : algorithme 22, feedback 7 ; porteuses OP3/4/5 à 1,00 désaccordées −2/0/+1 et paire OP2→OP1 à 0,50 (+7) ; modulateur OP6 niveau 82 avec **EG R1 49** (plus lent que les porteuses R1 77) → l'index s'installe après l'amplitude ; key scaling négatif des deux côtés de la touche 39 → moins d'index dans le grave et l'aigu ; KVS 2 → vélocité vers brillance ; LFO sinus 6,1 Hz PMD 5 sans délai ; **pas d'enveloppe de hauteur** (PEG 50/50/50/50).
- BRASS 2 : même algorithme, tout à 0,50, attaques instantanées (99) → version **stab**. BRASS 3 : algorithme 18, feedback 6, OP6 à 8,47 et OP5 à 3,18 ne vivant que dans le transitoire → composante inharmonique d'attaque, plus « cor » [DOC].

## Operator (Live 12) [HEUR, faits Operator DOC]
1. **Chowning à deux opérateurs** : algorithme B→A (pile de deux), A et B en Sine, Coarse 1 / Fine 0 sur les deux ; enveloppe de **B** (= index) A ≈ 100 ms, Peak 100 %, D ≈ 100 ms vers S ≈ 70 %, R ≈ 100 ms ; enveloppe de A parallèle ; **B Level** fixe l'index — le manuel ne chiffre pas l'index, régler à l'oreille jusqu'à un spectre proche d'une scie filtrée [TEST]. `B Lev < Vel` positif (vélocité → brillance) ; `B Lev < Key` négatif (key scaling).
2. **BRASS 1 approché** : algorithme **9** (D → A, B, C) : A/B/C en Sine Coarse 1 avec Fine +2 / 0 / −2 (dispersion), D en Sine Coarse 1 avec **Feedback** élevé (autorisé : D n'est pas modulé) [DOC feedback sur osc non modulé] ; enveloppe de D : A 80–150 ms contre 20–40 ms pour les porteuses ; D Sustain 90 %. La paire sous-octave (0,50) : second Operator dans un Instrument Rack, ou porteuse A en Coarse 0,5 sans modulateur propre.
3. Vibrato : LFO sinus 5–6 Hz → A/B/C, amount faible, **enveloppe du LFO** pour le retard [DOC enveloppe de LFO]. Voices = 1 pour un lead legato [DOC].
4. Growl FM (alternative à Reid) : moduler **FM Drive** par le LFO en plage Hi (60–80 Hz) avec l'enveloppe du LFO courte : change la brillance de toute la structure sans toucher la hauteur [DOC cible FM Drive].
5. Hybride 80s : filtre LP 24 `Play by Key` derrière, Freq < Env avec attaque plus lente que l'ampli.

## Serum 2 [HEUR, faits Serum 2 DOC]
- OSC A sinus (Basic Shapes), **Warp = FM from B**, mode **Linear** (garde la hauteur ; Exp dérive) [DOC variantes], OSC B sinus même octave/semi/fine (1:1), niveau de B dans le mixeur à 0 si B ne sert que de modulateur [TEST].
- **Warp amount = index** : Env 2 → Warp, forme 1/6–1/6–1/2–1/6 (A 100 ms, D 100 ms, S 70 %, R 100 ms pour 0,6 s) ; Env 1 (ampli) même forme.
- BRASS 1 approché : unison 3, detune très faible (porteuses −2/0/+1) ; pas de feedback d'opérateur dans Serum 2 [MÉMOIRE, non vérifié] → prendre **B = scie** au lieu de sinus (le feedback DX7 pousse le modulateur vers une scie) ou un Warp Distortion léger sur B ; Sub à −12 st pour la paire 0,50 ; Velocity → Warp ; Note → Warp négatif de part et d'autre de C3 ; LFO 1 sinus 6 Hz → pitch, Rise 300 ms.
- Stab (BRASS 2) : mêmes rapports, Env 1 et 2 A 0–5 ms, S 80 %, R 150 ms, accords plaqués.
- Filtre MG Low 24 optionnel derrière avec Env 3 → cutoff plus lent : hybride « FM + wow ».

## Processing
`Chorus (patch) → J37 léger (bande, +2 harmoniques) → Pro-Q 4 cloche −2 dB 2,5–3,5 kHz si la FM « pique » → Reverb plate 1,2 s 10 %` [HEUR]. Les valeurs DX7 0–99 ne sont pas des millisecondes : caler à l'oreille [TEST].

## Tests [TEST]
Vélocité 40 / 120 : l'index suit (plus terne / plus brillant) · note grave C2 et aiguë C5 : l'aigu n'est pas strident (key scaling) · A/B avec le patch analogique : le FM est plus « cuivré » dans l'attaque, moins « rond » en tenue · CPU et niveau relevés.
