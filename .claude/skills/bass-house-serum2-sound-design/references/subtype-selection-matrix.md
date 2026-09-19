# Matrice de sélection — famille → sous-type → moteur

Utiliser cette matrice avant de proposer un patch. Le but est de sélectionner une **architecture**, pas un preset au hasard.

| Famille | Sous-type | Serum 2 | Ableton natif | Quand le choisir |
|---|---|---|---|---|
| Synthé | Analog moderne | Wavetable simple + filtre | Drift / Analog | timbre direct, chaleureux, contrôlable |
| Synthé | Digital wavetable | Wavetable | Wavetable | mouvement spectral audible |
| Synthé | FM métallique | Wavetable en Ratio/FM selon besoin | Operator | cloche, métal, edge numérique |
| Synthé | Hybride morphing | Wavetable + Granular/Spectral | Meld | timbre évolutif à deux identités |
| Synthé | Supersaw/stack | Wavetable + unison mesuré | Wavetable / Rack | largeur et énergie harmonique |
| Nappe | Airy | Wavetable + Noise/Granular | Wavetable + reverb | couche haute, légère |
| Nappe | Cinematic | Granular + Wavetable | Granulator III + Meld/Rack | profondeur et évolution lente |
| Nappe | Granular diffuse | Granular | Granulator III Cloud | texture non périodique |
| Nappe | Spectrale | Spectral | Granulator III + effects | matière abstraite/éthérée |
| Drone | Tonal stable | Wavetable, tracking off/on selon rôle | Wavetable/Meld | fondamentale continue |
| Drone | Granular | Granular, tracking off possible | Granulator III Cloud | texture statique-évolutive |
| Drone | Industrial/noise | Sample/Granular + Noise | Granulator III/Roar | tension, matière bruitée |
| Stab | House chord | Wavetable | Drift/Analog | accord court, groove |
| Stab | Bass House metallic | Wavetable/Ratio + Noise | Operator/Drift | mordant et médium agressif |
| Stab | Organ/rave | Wavetable/Harmonics | Operator/Analog | empilement harmonique franc |
| Stab | Sampled | Sample/Multisample | Simpler/Sampler | caractère d'un one-shot |
| Riser | Noise | Noise/Sample | Auto Filter/Rack | montée large non tonale |
| Riser | Tonal pitch | Wavetable + CRS | Drift/Shifter | montée de hauteur claire |
| Riser | Granular | Granular | Granulator III | densité/texture croissante |
| Riser | Feedback/distortion | Wavetable/Sample + FX | Roar/Echo | tension agressive |
| Impact | Club sub | Sample + simple sub | Drum Sampler/Simpler | transition avec poids bas |
| Impact | Cinematic | Sample + layers | Simpler + Corpus + Hybrid Reverb | grande taille/profondeur |
| Impact | Metallic | Sample/Noise | Corpus/Collision | clang/résonance |
| Impact | Tonal | Wavetable/Sample | Operator/Drum Sampler | impact accordé |
| Pluck | House bright | Wavetable | Drift/Wavetable | pluck clair et moderne |
| Pluck | FM metallic | Wavetable/Ratio | Operator | attaque digitale/metal |
| Pluck | Organic string | Sample/Multisample | Tension | pincé organique |
| Pluck | Resonant/glassy | Wavetable | Collision/Corpus | verre, marimba, résonance |
| Pad | Warm analog | Wavetable simple | Analog/Drift | soutien harmonique chaud |
| Pad | Airy | Wavetable + Noise | Wavetable | haut doux et large |
| Pad | Digital evolving | Wavetable | Wavetable/Meld | mouvement spectral contrôlé |
| Pad | Granular cinematic | Granular + stable layer | Granulator III + Rack | texture cinéma sans perdre l'accord |
| Pad | Dark/dystopian | Spectral/Granular | Meld/Roar | tension sombre |
| Keys | Electric piano | Multisample si source adaptée | Electric | EP vivant/réactif |
| Keys | FM digital | Wavetable/Ratio | Operator | DX-style/digital bell keys |
| Keys | Organ | Wavetable Harmonics | Operator/Analog | harmoniques fixes, sustain |
| Keys | House piano/sample | Multisample | Sampler/Simpler | attaque piano/house réaliste |
| Keys | Mallet | Sample/Multisample | Collision | percussif/résonant |
| Keys | Synth key | Wavetable | Drift/Wavetable | clavier synthétique polyvalent |

## Décision rapide

1. Si **l'échantillon lui-même** porte le caractère → Sample/Multisample/Simpler/Sampler.
2. Si **la position/morphing du spectre** porte le caractère → Wavetable.
3. Si **les grains et l'étirement** portent le caractère → Granular/Granulator III.
4. Si **l'analyse/resynthèse fréquentielle** porte le caractère → Spectral.
5. Si **les rapports d'oscillateurs/FM** portent le caractère → Operator ou modes Ratio de Serum.
6. Si **la réponse physique** est la priorité → Electric, Collision ou Tension.
7. Si deux identités doivent coexister/morpher → Meld ou Instrument Rack.
