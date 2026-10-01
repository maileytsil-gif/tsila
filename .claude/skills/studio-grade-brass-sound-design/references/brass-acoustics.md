# Acoustique des cuivres — ce qu'il faut reproduire, et pourquoi

Source principale : Gordon Reid, *Synth Secrets* parties 24 à 27 (Sound On Sound, avril–juillet 2001), texte intégral dans le corpus local : `../../../../corpus/synth-secrets/synth-secrets-24.md` à `synth-secrets-27.md`. Tout ce qui suit est `[DOC]` sauf mention contraire. Les chiffres de patch sont ceux de Reid sur Minimoog, SH101 et ARP Axxe : ils se transposent à Serum 2 et aux natifs de Live 12 (voir `serum2-brass-design.md`, `ableton-brass-design.md`).

## 1. Pourquoi une dent de scie, et une seule

- Les cuivres sont des tuyaux fermés par la « valve » des lèvres. Un tuyau cylindrique fermé ne produit que les harmoniques impairs (clarinette, son carré). Mais la perce des cuivres est conique puis évasée (pavillon), et le cône comme l'évasement redonnent **la série harmonique complète**. D'où le son « brash » et la **dent de scie** comme seule forme d'onde de départ ; le carré est inadapté. (partie 24)
- Pour une émulation réaliste, **un seul oscillateur** : deux oscillateurs désaccordés dérivent l'un contre l'autre, ce qui ne ressemble à rien dans l'instrument réel. (partie 26) Le synth brass de section (Rhea : trois oscillateurs à l'unisson « pour un tutti plus gras ») est un autre objet, moins réaliste mais utile — voir `brass-architecture.md`, fonction SECTION.
- Registre : trompette, cornet, sax alto et soprano jouent haut ; Reid met l'oscillateur en 4' (une octave au-dessus du piano à touche égale). Trombone, cor, tuba : 8' ou 16'. (partie 26)
- Tuba (patch d'usine SH101 analysé par Reid) : dent de scie à 60 % **plus** sous-oscillateur carré une octave dessous à 100 % ; la scie seule manque de corps, le carré seul sonne creux. Le mélange des formes définit le timbre autant que le filtre. (partie 27)
- Niveau d'oscillateur modéré (5/10 sur Minimoog) pour ne pas saturer l'entrée du filtre, sauf si la distorsion est voulue. (partie 26)

## 2. La brillance suit la force, la hauteur la réduit

- Note douce : fondamentale dominante, environ six harmoniques. Note forte, « overblown » : c'est le **8e harmonique** qui domine, perçu comme un couac trois octaves au-dessus ; les harmoniques bas perdent en amplitude relative. (partie 24, fig. 8)
- Conséquences : cutoff du passe-bas **proportionnel à la force de jeu** (vélocité, pression, molette), et **résonance qui augmente avec la force** pour accentuer les harmoniques hauts. (parties 24-25)
- Une note haute a moins d'harmoniques qu'une note basse : le filtre suit le clavier **un peu moins que 1:1** (Reid : ≈ 190 % par octave au lieu de 200 %). Sur Minimoog, les options sont 0, 33, 67, 100 % ; il choisit 100 %. Sur SH101 et Axxe, réglage continu « un peu sous 100 % ». (parties 24, 26, 27)

## 3. Le transitoire : l'ampli ouvre vite, le filtre plus lentement

- Enveloppe d'amplitude d'un cuivre = **ADS** ; l'attaque raccourcit quand on souffle plus fort → router la vélocité vers le temps d'attaque. Le coup de langue « T/D » (plosif) donne une attaque instantanée suivie d'une seconde montée plus lente ; un ADSR à attaque quasi nulle, arrondi par l'électronique, l'approche. (partie 25)
- Les harmoniques **sous** la fréquence de coupure naturelle de l'instrument atteignent leur niveau ensemble et vite ; ceux **au-dessus** montent plus lentement. Certains chercheurs y voient l'indice principal d'identification d'un instrument. (partie 25, fig. 11)
- Réalisation Minimoog (partie 26) : ampli attaque **100 ms**, sustain maximal, release quasi instantané ; filtre cutoff **au minimum**, quantité d'enveloppe **6,5/10**, attaque **600 ms**, decay **800 ms**, sustain **5/10**, release instantané ; résonance **2/10** (légère bosse, conforme aux mesures) ; suivi de clavier 100 %.
- Le « parp » : la bouffée initiale surjouée exige une enveloppe de filtre à **quatre étages** (montée puis redescente vers le sustain), pas un simple AR. La vélocité pilote la **quantité** d'enveloppe de filtre ; l'aftertouch ou la molette pilote la brillance pendant la tenue. (partie 25, fig. 13-14)
- Release : très court sur l'instrument réel, mais un release à zéro « claque » sur un synthé rapide ; Reid met **2/10** sur SH101 pour une fin lisse. (partie 27)
- Notes liées : un changement de piston ne redéclenche pas le transitoire → enveloppes en **gate seul, sans retrigger** en legato ; notes détachées à la langue → jeu staccato, retrigger. (partie 27)

## 4. Le « growl » d'installation : moduler le filtre, jamais la hauteur

- Chaque note met un temps à s'installer : une douzaine de cycles, soit **≈ 50 ms** vers 256 Hz, période d'instabilité de hauteur (« les cornistes ratent parfois l'attaque : c'est la faute de l'instrument »). (partie 25)
- Ne pas moduler l'oscillateur : toute modulation périodique de la fréquence crée des bandes latérales FM et détruit le timbre. Reid module **le cutoff** avec un **triangle vers 80 Hz**, dont la quantité est contrôlée par une enveloppe **AD** courte (le growl ne dure que le temps de l'installation), et que l'aftertouch peut réintroduire pour imiter le surjeu. (partie 25, fig. 15) — d'où sa remarque : un LFO plafonné à 25 Hz ne suffit pas.
- Sur Minimoog : Osc3 en 32', triangle, fine −1, sans suivi de clavier, dosé à la molette (60 % au départ de la note → 0 % au sustain sur SH101). Le patch tuba de Tom Rhea utilise le **bruit** comme modulateur du filtre à la place du triangle, « extrêmement efficace ». (parties 26-27)

## 5. Vibrato retardé, tremolo, gonflement

- Le vibrato vient de la tension des lèvres **après** le transitoire : il n'apparaît jamais dès l'attaque. Réalisation : LFO **≈ 5 Hz**, amplitude **très faible** (sinon « ça sonne électronique »), quantité montée par une rampe AR. (partie 25, fig. 16) Alternative : vibrato manuel à la molette de hauteur, souvent plus naturel. (partie 26)
- Tremolo (modulation de la pression d'air) : LFO sur le VCA, retardé. Gonflement / diminuendo : enveloppe à cinq étages ou contrôleur continu (molette, CC11). (partie 25)

## 6. Le souffle

- Bruit aérodynamique, **façonné par les formants** de l'instrument, presque inaudible en jeu normal ; il ajoute un « fond accordé » et beaucoup de réalisme si on l'introduit ainsi. Un bruit blanc non façonné sonne au contraire artificiel : Reid l'omet sur Minimoog et SH101. (parties 25-27) → dans Serum 2 ou Live, bruit **filtré passe-bande** ou passé par un filtre à formants, jamais brut.

## 7. Formants

- Un formant est une résonance fixe qui **ne suit pas la hauteur** ; trois suffisent à caractériser une famille d'instruments, et ils expliquent la cohérence de timbre d'un instrument à l'autre. (partie 23, texte dans `synth-secrets-23.md`) Reid reconnaît que son patch soustractif ignore les formants des cuivres : c'est la première amélioration possible (EQ fixe ou filtre à formants après le filtre suivant le clavier).
- Les valeurs de formants par instrument relevées dans la littérature acoustique sont dans `genre-brass-specifications.md` (section « Registres et formants ») avec leur source.

## 8. Limites de la synthèse soustractive, et ce qui fait mieux

- Les partiels réels ne sont pas exactement harmoniques (étirés), leurs phases ne sont pas alignées, leurs amplitudes évoluent séparément : « la synthèse soustractive n'est pas la voie idéale ». L'additif microtonal (Kawai K5000) fait mieux ; aujourd'hui, le **multisample** (Serum 2 Multisample, Sampler, Kontakt) et la **resynthèse spectrale** (Serum 2 Spectral) donnent le réalisme, la soustractive donne le synth brass. (partie 25)
- Le jeu compte autant que le patch : un patch parfait joué comme un piano ne sonnera pas cuivre (Reid cite Wendy Carlos). → `sampled-brass-midi-programming.md`.

## Résumé opératoire (à recopier dans un patch d'émulation)

| Élément | Réglage de départ | Preuve |
|---|---|---|
| Source | 1 dent de scie, niveau modéré ; tuba : + carré −1 octave | [DOC] SS26-27 |
| Ampli | A 100 ms (plus court à forte vélocité), S max, R court non nul | [DOC] SS25-27 |
| Filtre | LP, cutoff bas, env +65 %, A 600 ms / D 800 ms / S 50 %, Q léger, suivi ≈ 95 % | [DOC] SS26 |
| Vélocité | → quantité d'env. de filtre, → attaque plus courte | [DOC] SS25 |
| Molette / aftertouch | → cutoff (brillance en tenue), → growl | [DOC] SS25 |
| Growl | triangle ≈ 80 Hz ou bruit → cutoff, fondu AD ≈ 50-150 ms | [DOC] SS25-26, durée [HEUR] |
| Vibrato | 5 Hz, très faible, retardé ≈ 300-600 ms | [DOC] SS25, délai [HEUR] |
| Souffle | bruit passe-bande ou formant, presque inaudible | [DOC] SS25 |
| Formants | 2-3 pics fixes en aval, ne suivant pas le clavier | [DOC] SS23-25, valeurs voir spécifications |
| Legato | pas de retrigger sur notes liées | [DOC] SS27 |
