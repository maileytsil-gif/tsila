# Contrebasse jazz dans Serum 2 — recette complète

Conçue le 18 septembre 2026 pour l'intro jazz de « deep chill minimal house ».
Méthode : 5 approches de synthèse conçues indépendamment, jugées par 3 juges (réalisme acoustique, faisabilité à la main, intégration au mix), puis fusionnées.
Contrainte : Serum 2 n'expose qu'un paramètre à l'API de Live, tout se règle à la main dans sa fenêtre.

---

## 1. L'approche retenue

**La wavetable à rampe harmonique balayée par enveloppe gagne**, et pas de justesse : c'est la seule des cinq classée dans les deux premières places par les trois juges (1ʳᵉ en faisabilité, 2ᵉ en réalisme, 2ᵉ en intégration — 13 points Borda contre 12 à la soustractive et 9 à l'hybride multisample). Sa raison d'être tient en une phrase : une corde ne se filtre pas, elle **perd ses harmoniques une par une du haut vers le bas**, et une wavetable change le *nombre* d'harmoniques là où un filtre n'applique qu'une *pente*. J'ai revérifié moi-même ses deux chiffres porteurs sur ce disque, par FFT frame par frame : `SawRounded.wav` a bien **26 frames**, la fondamentale est dominante dans les 26 (aucun saut d'octave au balayage), le contenu monte de H1/H2/H3 = 1 / 0,24 / 0,09 en frame 0 à 1 / 0,50 / 0,33 / 0,25 / 0,20 / 0,17 en frame 25 — la loi 1/n exacte de la dent de scie — et la RMS ne varie que de 0,504 à 0,610, soit **1,65 dB de creux maximum** au balayage. Elle remplace aussi les deux réglages invérifiables des concurrentes par deux chargements de fichier : bruit de doigt réel (`FretNoise B.flac`) au lieu d'un bruit blanc dosé sans référence, et corps en IR (`Woody.flac` en ϕ MIN) au lieu d'une cloche d'EQ dont personne ne justifie la fréquence.

**Trois corrections ont été apportées.** (a) Le défaut relevé par le juge qui la classait première — *trop d'opérations, aucune version minimale, et tout le réalisme suspendu à une seule ligne au sens contre-intuitif* — est traité par une scission stricte **NOYAU (22 étapes, ~20 min, 80 % du résultat) / PASSE 2**, avec un point de contrôle bloquant à l'étape 16 sur cette ligne précise. (b) Le défaut relevé par le juge « intégration au mix » — son `FILTER 2` en Peak 235 Hz / RES 30 % / key track 0 %, qui fabrique exactement l'incohérence de niveau note à note que `basses.md` interdit — est supprimé : **il n'y a plus aucune résonance dans le bas-médium**, le corps est fait par le CONVOLVE (fixe, sur la somme, donc physiquement une caisse partagée) et FILTER 2 est recyclé en simple coupe-bas du bruit. (c) Le creux anti-piano est **calculé et déplacé après la saturation**, au lieu d'être posé au jugé avant elle.

**Greffes** : la dérive de hauteur du pincement avec la vélocité en AUX SOURCE (approche FM), la procédure ordonnée du key tracking et les vélocités à écrire dans le clip (approche soustractive), les tests objectifs + la couche de vérité multisample + le routage Note → ENV 1 DEC (approche hybride), le câblage des macros dès le montage (approche Karplus-Strong).

---

## 2. Tableau d'opérations

### Avertissement de registre, à lire avant de commencer

MIDI 41 = **87,31 Hz**, MIDI 55 = **196,00 Hz** (convention Ableton, C3 = 60). La partie écrite vit donc entre 87 et 196 Hz, soit **une octave au-dessus d'une walking bass jazz ordinaire** (41–98 Hz). C'est jouable sur les cordes de Ré et de Sol, mais ce n'est pas le registre attendu, et 196 Hz entre en concurrence directe avec les voicings shell de la main gauche. Tous les chiffres ci-dessous sont calés sur 87–196 Hz. Si l'intention était le registre classique, transpose le clip de **−12** et applique la colonne « −12 » donnée en fin de tableau.

### NOYAU — étapes 1 à 22

| # | Section de Serum 2 | Contrôle exact | Valeur | Pourquoi |
|---|---|---|---|---|
| 1 | Chargement | preset de départ | **Init** — surtout pas un preset Serum 1 | Un preset Serum 1 active tout seul le mode S1 Compatibility, dont la formulation officielle est « similarité **maximale** », pas identité. Tu ne réglerais pas le même moteur. |
| 2 | GLOBAL | **QUALITY** | **High (2×)**, puis le verrouiller | Le Quality est stocké dans le preset, et des correctifs Xfer montrent que le son des warps différait selon sa valeur. Le changer après avoir réglé à l'oreille casse le patch. |
| 3 | GLOBAL | **MONO / LEGATO / PORTA** | **ON / OFF / 0 ms** | Quand la main gauche se pose, elle étouffe la corde précédente : le mono reproduit ça exactement. LEGATO OFF pour que chaque noire des mesures 17-24 soit RE-pincée. PORTA 0 : les approches chromatiques sont pincées, pas glissées. |
| 4 | OSC A | moteur | **Wavetable** | Les warp modes appartiennent à ce moteur ; Sample / Multisample / Granular / Spectral ont d'autres contrôles. |
| 5 | OSC A | table | **Analog › SawRounded** (`/Library/Audio/Presets/Xfer Records/Serum 2 Presets/Tables/Analog/SawRounded.wav`) | 26 frames, H1 dominante partout, rampe harmonique monotone, 1,65 dB de variation RMS mesurée sur toute la table : aucun creux de volume au balayage. C'est la seule table d'usine qui soit une vraie rampe de série harmonique sans formant mobile. |
| 6 | OSC A | **WT POS** | **8 %** | ≈ frame 2, l'état « corde éteinte » (H95 = 2 harmoniques). **Sens contre-intuitif : le knob se gare EN BAS, c'est l'enveloppe qui monte.** Vérifié à l'étape 16. |
| 7 | OSC A | clic droit sur WT POS › **Smooth Interpolation** | **ON** | 26 frames en 160 ms = une frame toutes les 6,2 ms, soit moins d'une période d'onde à 87 Hz. Sans lissage, le balayage s'entend par paliers. |
| 8 | OSC A | **UNISON / DETUNE / WIDTH** | **1 / 0,00 / 0** | Règle non négociable : une seule source tient le fondamental, un seul oscillateur, aucun désaccord. Le battement entre voix module l'amplitude du fondamental et rend le grave instable. |
| 9 | OSC A | **PHASE / RAND** | phase fixe, **RAND 0 %** | La phase aléatoire sur une basse rend l'attaque imprévisible. La vie viendra de la vélocité et du canal NOISE, pas d'ici. |
| 10 | OSC A | **WARP 1** | **Distortion › Tube, 16 %** | Un warp agit **avant** le filtre : le filtre nettoie ensuite la distorsion, et le résultat est rond. C'est la non-linéarité d'une corde épaisse attaquée à la pulpe. |
| 11 | OSC A | **WARP 2** | **Distortion › Asym, 14 %, fixe, non modulé** | Harmoniques d'ordre **pair** = chaleur boisée. Simplification assumée : la version d'origine modulait un `Bend +/−` pour simuler la position de pincement, mais ce rapprochement-là n'est pas dans le manuel. Option A/B en fin de recette. |
| 12 | MIXER | en-têtes **SUB**, **OSC B**, **OSC C** | **tous éteints** | Il y a déjà un sub de synthèse ailleurs dans le morceau et une contrebasse n'a rien sous sa corde. SUB à OCT −1 est le moyen le plus rapide de transformer ce patch en basse électronique. |
| 13 | ENV 1 | **ATK / HOLD / DEC / SUS / REL** | **4 ms / 0 / 900 ms / 0 % / 220 ms**, courbe de DEC **concave** | ATK 4 ms et pas 0 : une corde met quelques ms à quitter le doigt, et 0 ms sur une onde lisse produit un clic. **SUS 0 % non négociable** : une corde pincée n'a aucun sustain. DEC 900 ms : à 120 BPM la blanche fait 1000 ms (la note meurt juste avant la suivante, mesures 9-16), la noire 500 ms (il reste de la queue, mesures 17-24). Concave parce qu'une corde décroît exponentiellement. |
| 14 | ENV 3 | **ATK / DEC / SUS / REL** | **0 ms / 160 ms / 0 % / 120 ms** | C'est l'enveloppe du **nombre d'harmoniques**. Ne pas la synchroniser au BPM : la décroissance d'une corde est une propriété du bois, pas du tempo. |
| 15 | MATRIX | ligne **M1** (détail au §3) | **ENV 3 → OSC A WT POS, +80 %, unipolaire** | Repos 8 % → pic 88 % (≈ frame 23, H95 = 9) → retour tout seul à 8 % en 160 ms. **C'est le routage central de toute la recette** : le spectre perd ses harmoniques du haut vers le bas pendant que la note tient encore, au lieu d'être couché en bloc sous une pente de filtre. |
| 16 | — | **POINT DE CONTRÔLE BLOQUANT** | jouer un **F1 tenu** | Tu dois entendre un pincement qui s'assombrit vite sur une note qui tient ~1 s. **Si la note démarre sombre et S'ÉCLAIRCIT**, la ligne M1 est à l'envers, ou le knob WT POS est garé en haut. Remets WT POS à 8 %, vérifie que l'amount est **positif et unipolaire**, et ne continue pas tant que ce n'est pas corrigé — les étapes suivantes seraient indébogables. |
| 17 | FILTER 1 | **TYPE** | **MG Low 24** (ladder Moog, 24 dB/oct) | Le ladder Moog est le circuit « crémeux », qui sature doucement dans le chemin de résonance. On veut que la fermeture du filtre soit grasse, pas nette. Si les notes hautes sonnent étouffées, passer en **MG Low 18**. |
| 18 | FILTER 1 | **CUTOFF / RES / DRIVE / VAR (étiqueté FAT) / MIX / PAN** | **380 Hz / 12 % / 15 % / 20 % / 100 % / 50 %** | 380 Hz tombe sur l'harmonique 4,35 du F1 : l'état « corde qui a fini de sonner ». **RES jamais au-delà de 12 %** — pas de résonance dans le grave. `FAT` apaise la résonance **en enrichissant** le spectre au lieu d'en retirer, ce qu'aucun EQ ne sait faire : c'est lui qui donne le bas-médium boisé. PAN à 50 % est le neutre documenté. |
| 19 | FILTER 1 | **Key Track sur le CUTOFF** | **55 %** | Ni 0 %, ni 100 %. À 100 % chaque note voit le même nombre d'harmoniques : c'est la définition d'un synthé. À 0 % la note aiguë est plus terne que la grave, l'inverse de la réalité. 55 % (dans la fourchette 0,5–0,7 documentée pour les pincements, choisie basse parce que le corps est désormais entièrement fixe dans les FX) fait passer le cutoff de **380 Hz sur F1 à 593 Hz sur G2** : les notes hautes sont relativement moins riches, comportement d'un instrument à caisse fixe. **Méthode 1** : clic droit sur CUTOFF › Key Track. **Méthode 2 si l'option n'existe pas sur le filtre de synthèse** : ligne de matrice Note → Filter 1 Cutoff, **et dans cet ordre impératif** — poser la ligne D'ABORD, puis tenir le F1 enfoncé et RE-régler le knob CUTOFF jusqu'à lire 380 Hz. |
| 20 | ENV 2 | **ATK / DEC / SUS / REL** | **0 ms / 260 ms / 0 % / 200 ms** | La pente résiduelle du filtre, troisième vitesse d'extinction. |
| 21 | MATRIX | ligne **M2** | **ENV 2 → FILTER 1 CUTOFF, ≈ +55 %, unipolaire** | **Ne te fie pas au pourcentage, règle-le à l'affichage** : clic droit sur la fenêtre du filtre › **Frequency Response & FFT**, joue un F1, et ajuste jusqu'à ce que le pic du balayage tombe vers **2,8 kHz** puis retombe à 380 Hz en 260 ms. Le mapping du knob de cutoff n'est pas linéaire et n'est pas documenté : le viser en Hz est la seule méthode fiable. Unipolaire impératif — en bipolaire, la moitié basse du cycle ferme le filtre **sous** son repos et mange le corps de la note. |
| 22 | NOISE | activer l'en-tête, puis **sample** | **`FretNoise B.flac`** (`…/Serum 2 Presets/Samples/Factory Non-Tonal/Noises/S2 Noises/FretNoise B.flac`) | C'est un vrai bruit de doigt sur corde enregistré : aucune synthèse ne fera mieux. Variantes du même dossier : `FretNoise A` (plus sec), `FretNoise C` (plus long), `Egtr Neck Down` (glissement). |
| 23 | NOISE | **one-shot / PITCH / départ aléatoire / LEVEL** | **one-shot ON · PITCH 0, key track OFF · départ aléatoire ON · LEVEL 0 %** | Le bruit du doigt est le même événement physique quelle que soit la note : s'il suit le clavier, on entend un instrument accordé qui n'existe pas. Le départ aléatoire est ce qui empêche l'effet mitraillette sur les 32 noires des mesures 17-24. LEVEL à 0 : le niveau viendra **uniquement** de ENV 4, sinon le bruit sonne pendant toute la traîne. *(Honnêteté : le dépouillement du manuel dont je dispose ne détaille pas les étiquettes exactes des contrôles du canal NOISE. Si tu ne trouves pas « one-shot » ou « RAND », les deux seules choses qui comptent sont : le sample ne doit pas boucler, et son point de départ doit varier à chaque note.)* |
| 24 | MIXER | routage du canal **NOISE** | **Filter**, knob du haut poussé **entièrement vers FILTER 2** | On isole le bruit pour le tailler sans toucher au corps. |
| 25 | FILTER 2 | **TYPE / CUTOFF / RES / DRIVE / Key Track / MIX** | **High 12 / 700 Hz / 0 % / 0 / 0 % / 100 %** — sortie vers **Main** | Règle : tout bruit superposé à un son tonal se coupe-bas **au-dessus de la fondamentale la plus haute**, ici le G2 à 196 Hz — 700 Hz est large et sûr. Pente 12 dB volontaire : à 24 dB on entend la coupure. **Key Track 0 % impératif.** *C'est ici que le défaut relevé par les juges est corrigé : FILTER 2 ne porte plus aucune résonance de caisse (l'ancienne version l'avait en Peak 235 Hz / RES 30 %, ce qui rendait le niveau inégal d'une note à l'autre). Le corps est passé dans les FX, où il est fixe et sur la somme — ce qui est la propriété physique d'une caisse partagée.* **Piège documenté** : un filtre reste grisé tant qu'aucun oscillateur ne lui envoie de signal. Fais l'étape 24 avant celle-ci. |
| 26 | ENV 4 | **ATK / DEC / SUS / REL** | **0 ms / 34 ms / 0 % / 30 ms** | Compromis assumé : la fiche de référence donne 26-30 ms pour une couche transitoire, l'approche FM 45 ms pour la dérive de hauteur, et Serum 2 n'a que **quatre** enveloppes — celle-ci fera les deux. Si tu veux les séparer : LFO 1 en **mode Env** (une seule passe, il devient une enveloppe dessinée à la main), RATE réglé pour une passe de 45 ms, dédié à la dérive de hauteur. |
| 27 | MATRIX | ligne **M3** | **ENV 4 → NOISE LEVEL, +100 %, unipolaire** | C'est ce qui transforme un souffle continu en claquement. **Dosage** : monte jusqu'à entendre un « tic » qui se détache nettement, **puis redescends de 4 dB**. Le critère n'est pas « je l'entends » mais « quand je le coupe, la note devient molle ». Cible finale : 12 à 18 dB sous le corps. |
| 28 | FX › rack **MAIN** | ajouter **CONVOLVE** | IMPULSE **`Woody.flac`** (`…/Serum 2 Presets/Impulses/Factory/Coloration/Woody.flac`) · **ϕ MIN ACTIVÉ** · SIZE **35 %** · TONE légèrement vers le grave · PRE-DLY **0** · DECAY court · **MIX 18 %** | **Le meilleur rapport effort/réalisme de toute la chaîne.** ϕ MIN laisse la réponse en fréquence inchangée mais supprime l'écho : le module cesse d'être une réverb et devient une pure coloration de corps. Une IR de bois bat deux cloches d'EQ sans comparaison possible. C'est aussi ce qui remplace la résonance de caisse retirée de FILTER 2. Alternatives : `Hollow Reso Barrel` (plus de caisse), `Woodpecker` (plus sec). |
| 29 | — | **CHECKPOINT NOYAU** | jouer les mesures 9-16 puis 17-24 | Tu dois déjà entendre une contrebasse plausible. Si oui, **sauvegarde sous `Contrebasse Pizz Trio v1`** et passe à la suite. Si non, le problème est dans les étapes 15, 21 ou 27 — pas ailleurs. |

### PASSE 2 — étapes 30 à 41 (raffinement, ~30 min)

| # | Section de Serum 2 | Contrôle exact | Valeur | Pourquoi |
|---|---|---|---|---|
| 30 | MATRIX | lignes **M4 à M9** | voir §3 | La vélocité pilote le timbre (nombre d'harmoniques, dureté du doigt, cutoff, claquement) et pas seulement le volume. Sans elles, les vélocités écrites dans le clip ne produisent rien. |
| 31 | MATRIX | ligne **M10** | **ENV 4 → OSC A FINE, ≈ +12 cents au pic, unipolaire, AUX SOURCE = Velocity** | **Greffe de l'approche FM, et le meilleur réglage à ajouter en dernier.** Une corde fortement déplacée est momentanément sous tension plus élevée : elle démarre trop haut et se cale en quelques dizaines de millisecondes. L'AUX SOURCE en vélocité est physiquement juste — plus on pince fort, plus la corde part haut. À comparer en bypass : l'effet est petit et immédiatement reconnaissable. Ne PAS le router sur autre chose que OSC A. |
| 32 | MATRIX | lignes **M11 et M12** | voir §3 | Key tracking du timbre et de la durée. **Attention au signe** : les sources dont je dispose se contredisent sur la normalisation de la source Note (l'une la dit à 0 au MIDI 0, l'autre centrée sur C3). Ne fais confiance à aucune des deux : joue F1 puis G2, le **G2 doit être plus court et relativement moins riche**. Si c'est l'inverse, inverse le signe. |
| 33 | LFO 3 | forme **Random / S&H**, **BPM OFF, HOST OFF**, **trigger mode `Trig`**, RATE ~0,7 Hz | — | `Trig` est essentiel et systématiquement omis : sans lui le LFO tourne librement et chaque note attrape une valeur au hasard **dans** le cycle, ce qui n'est pas reproductible. Et dans Serum 2, contrairement à Serum 1, le switch HOST agit **même quand BPM est désactivé** : un LFO vraiment libre exige les deux coupés. |
| 34 | MATRIX | lignes **M13 et M14** | voir §3 | L'intonation d'un contrebassiste n'est jamais deux fois la même, et les notes ne s'éteignent pas toutes à la même vitesse. |
| 35 | OSC C | **moteur Multisample**, fichier **`Double Bass Pizz Jazz.sfz`** (`…/Serum 2 Presets/Multisamples/Factory/Strings/Double Bass Pizz Jazz.sfz`) | COARSE 0 · FINE 0 · **LEVEL −20 dB sous OSC A** · UNISON 1 · routage **Main, bouton « enveloppe » ACTIVÉ** | **La couche de vérité, et la correction honnête de la limite n°1 de cette approche.** Les 30 à 60 premières millisecondes d'un pizz réel sont du bruit chaotique inharmonique qu'aucune enveloppe ne fabrique ; seul un enregistrement le donne. À −20 dB il ne pilote rien, il **authentifie**. Routé vers Main avec le bouton enveloppe activé, il est gaté par ENV 1 et joue sa propre décroissance naturelle : aucune enveloppe supplémentaire nécessaire. Fichier d'usine, donc zéro conversion, zéro dépendance externe, embarquement natif. **Si tu préfères t'en passer** (RAM, ou version 2.0.21 où un correctif concerne justement la RAM des multisamples d'usine) : OSC C en Wavetable sur `S2 Tables › Digital › WoodDonk`, **WT POS figé à 50 %** (frame 1 remesurée : H1/H2/H3 = 1 / 1,54 / 1,38, H95 = 6, un choc boisé sans hauteur), LEVEL −21 dB, routage Main **bouton enveloppe DÉSACTIVÉ**, et une ligne de matrice ENV 4 → OSC C LEVEL. Ne jamais balayer cette table, ses 3 frames sautent. |
| 36 | FX › MAIN | chaîne complète | voir §4 | — |
| 37 | MACROS | **MACRO 1 « DOIGT »** | → NOISE LEVEL (0 à +6 dB) + MIX du CONVOLVE (10 → 26 %) | **À câbler maintenant, pas après.** Serum 2 n'expose quasiment rien à l'API d'Ableton tant qu'on n'a pas fait clic droit › Automate puis Configure sur chaque contrôle : **les macros sont les seuls leviers automatisables depuis l'arrangement**. Les poser après coup oblige à tout re-dialer. |
| 38 | MACROS | **MACRO 2 « CORDE »** | → WT POS de repos (8 → 20 %) + CUTOFF FILTER 1 (380 → 700 Hz) | Une seule intention verbalisable : « plus ouvert ». |
| 39 | MACROS | **MACRO 3 « CORPS »** | → MIX du CONVOLVE + DRIVE de la DISTORTION | « Plus de bois ». |
| 40 | MACROS | **MACRO 4 « ÉTOUFFÉ »** | → ENV 1 DEC (900 → 250 ms) | Pour basculer en jeu étouffé si la contrebasse survit à la mesure 25, sans changer de preset. |
| 41 | Sauvegarde | preset | **`Contrebasse Pizz Trio v2`**, avec **Embed** coché (wavetables, sample de bruit, IR, multisample) | Sans Embed, le preset référence des fichiers externes et casse au premier déplacement. Et **note la version exacte de ton Serum 2 dans la mémoire du projet** : le plug-in n'est pas forward compatible, une session sauvée avec une version plus récente se recharge avec le bon *nom* de preset et le son Init. Un hot-swap accidentel efface une heure de travail. |

### La hiérarchie des quatre décroissances — le cœur du patch, chiffré

| Enveloppe | Rôle | DEC | Rapport à l'ampli |
|---|---|---|---|
| ENV 4 | bruit de doigt + dérive de hauteur + saturation d'attaque | **34 ms** | **3,8 %** |
| ENV 3 | nombre d'harmoniques (WT POS) | **160 ms** | **17,8 %** |
| ENV 2 | pente résiduelle du filtre | **260 ms** | **28,9 %** |
| ENV 1 | amplitude | **900 ms** | **100 %** |

Le son perd son bruit de doigt en 34 ms, ses harmoniques hautes en 160 ms, sa brillance résiduelle en 260 ms, et son volume seulement en 900 ms. **Écart délibéré avec la règle de référence « decay de filtre = 60 à 70 % du decay d'ampli »** : ce 60-70 % est calibré sur un pluck house de 250 ms, et le rapport n'est pas invariant d'échelle. Sur une corde grave et épaisse, les partiels supérieurs sont amortis par la raideur de la corde, le chevalet et le doigt en 100 à 250 ms alors que la fondamentale tient une seconde et demie. Appliquer 65 % ici (585 ms de filtre) redonne instantanément un pluck de deep house. **Ce qu'il faut retenir de la règle est le principe — l'harmonicité doit chuter plus vite que l'amplitude — pas le nombre.**

### Colonne « −12 » (si le clip est transposé une octave plus bas)

FILTER 1 CUTOFF de repos **380 → 240 Hz** · FILTER 2 HIGH 12 **700 → 500 Hz** · ENV 1 DEC **900 → 1 400 ms** · EQUALIZER #1 High Pass **45 → 30 Hz** · EQUALIZER #2 : le conflit avec le piano disparaît, remplacer les deux cloches par **une seule PEAKING 300 Hz, −1,5 dB, Q 1,0** · UTILITY MONO BASS **200 → 140 Hz**. Rien ne change dans les oscillateurs ni dans la matrice.

---

## 3. Matrice de modulation

Onglet MATRIX. 64 slots disponibles, 14 utilisés. Colonnes : source · destination · quantité · uni/bipolaire · Curve · Aux Source.

**Noyau (indispensables) :**

| Ligne | Source | Destination | Quantité | Polarité |
|---|---|---|---|---|
| **M1** | ENV 3 | OSC A **WT POS** | **+80 %** | unipolaire |
| **M2** | ENV 2 | FILTER 1 **CUTOFF** | **≈ +55 %** — à caler à l'affichage FFT pour un pic à 2,8 kHz | unipolaire |
| **M3** | ENV 4 | **NOISE LEVEL** | **+100 %** | unipolaire |

**Passe 2 — vélocité (rend la ligne écrite vivante) :**

| Ligne | Source | Destination | Quantité | Polarité |
|---|---|---|---|---|
| **M4** | ENV 4 | OSC A **WARP 1** (Tube) | **+18 %** | unipolaire |
| **M5** | VELOCITY | OSC A **WARP 1** (Tube) | **+26 %** | unipolaire |
| **M6** | VELOCITY | OSC A **WT POS** | **+12 %** | unipolaire |
| **M7** | VELOCITY | FILTER 1 **CUTOFF** | **+22 %** | unipolaire |
| **M8** | VELOCITY | **NOISE LEVEL** | **+45 %** | unipolaire |
| **M9** | VELOCITY | **ENV 2 DEC** | **+15 %** | unipolaire |

**Passe 2 — physique de la corde :**

| Ligne | Source | Destination | Quantité | Polarité |
|---|---|---|---|---|
| **M10** | ENV 4 | OSC A **FINE** | **≈ +12 cents au pic** · **AUX SOURCE = Velocity** | unipolaire |
| **M11** | NOTE (key track) | OSC A **WT POS** | **−10 %** | unipolaire |
| **M12** | NOTE (key track) | **ENV 1 DEC** | **−22 %** | unipolaire |

**Passe 2 — anti-mitraillette :**

| Ligne | Source | Destination | Quantité | Polarité |
|---|---|---|---|---|
| **M13** | LFO 3 (Random/S&H, `Trig`, BPM off, HOST off, ~0,7 Hz) | OSC A **FINE** | **±4 cents** | **bipolaire** |
| **M14** | LFO 3 | **ENV 1 DEC** | **±8 %** | **bipolaire** *(optionnelle)* |

**Notes de matrice, à lire avant de poser les lignes.**

- **Aucun LFO cyclique sur la hauteur. C'est un choix, pas un oubli.** Une walking bass jazz est jouée **sans vibrato** : un vibrato permanent sur une contrebasse pincée est le marqueur immédiat du synthé. Le seul LFO du patch est aléatoire, non périodique, et sert à casser la répétition. Si tu veux un vibrato sur les blanches tenues des mesures 9-16 (ce qu'un bassiste ferait effectivement), rends-le **joué et non automatique** : LFO 1 en mode `Trig`, 4,5 Hz, `Rise` réglé pour un fondu d'entrée de ~350 ms, destination OSC A FINE ±5 cents — à 350 ms il n'existera que sur les notes longues.
- **Si une destination refuse l'assignation** (`ENV 1 DEC` et `ENV 2 DEC` ne sont pas garantis comme destinations de matrice dans toutes les builds) : M9, M12 et M14 sont des raffinements, pas des fondements. Passe.
- **Si la source `RAND` / `Random` n'existe pas telle quelle** dans la liste de matrice de ta version, le repli documenté est exactement équivalent : un LFO en forme Random avec **trigger mode `Trig`**, ce qui est déjà ce que prescrit l'étape 33.
- **Aucune enveloppe sur un paramètre du rack FX.** Le manuel est explicite : le rack opère sur la **somme** de la sortie du moteur, pas par voix. Une enveloppe posée là se re-déclencherait à chaque note. Tout ce qui doit bouger par note est en amont.

---

## 4. Chaîne d'effets

### Rack MAIN de Serum 2 — le flux va du haut vers le bas, structure strictement série

**1. EQUALIZER #1 — nettoyage, AVANT la saturation**
- bande gauche : **HIGH PASS, 45 Hz** — sous la fondamentale du F1 (87,31 Hz) il n'y a rien à garder. Ça libère de la marge et ça dégage totalement la place pour le sub de synthèse qui arrive à la mesure 25. *(Le GAIN est sans effet quand High Pass est sélectionné : normal, ne le cherche pas.)*
- bande droite : **PEAKING, 420 Hz, −2,0 dB, Q moyen** — la zone boueuse. La creuser **avant** l'étage de distorsion est délibéré : on ne veut pas que la saturation se nourrisse de boue.

**2. DISTORTION**
- **TYPE : Tube** (défaut) · filtrage **POST** · TYPE de filtrage morphé vers **passe-bas**, **FREQ 2,8 kHz**, Key Track OFF, Q bas · **DRIVE 12 %** · **MIX 25 %**
- Le MIX à 25 % fait de cet étage une saturation quasi **parallèle**, ce que les sources recommandent explicitement sur une basse plutôt qu'un insert franc. Le rôle n'est pas de salir : c'est la **traduction**. Ces harmoniques sont ce à partir de quoi l'oreille reconstruit la fondamentale manquante sur un téléphone ou un laptop. Sur une intro jazz écoutée en mobilité, c'est ce qui fait que la contrebasse existe encore.

**3. COMPRESSOR**
- **MODE SINGLE** · **RATIO 3:1** · **ATTACK 12 ms** · **RELEASE 160 ms** · THRESH réglé pour **−3 à −4 dB** de réduction sur les crêtes · **GAIN +3 dB**
- **ATTACK 12 ms et pas 1 ms** : avertissement documenté et systématiquement ignoré — sur une basse, une attaque trop rapide « arrondit les crêtes individuelles de la forme d'onde grave, **ce qui produit de la distorsion** ». 12 ms laisse passer le claquement de doigt intact et ne travaille que sur le corps. RELEASE 160 ms : bien sous les 500 ms d'une noire à 120 BPM, donc le compresseur est revenu avant la note suivante.

**4. CONVOLVE — le corps de l'instrument** *(déjà posé à l'étape 28)*
- IMPULSE **`Woody.flac`** · **ϕ MIN ACTIVÉ** · SIZE **35 %** · TONE légèrement vers le grave · PRE-DLY **0** · DECAY court · **MIX 18 %**

**5. EQUALIZER #2 — anti-piano, APRÈS la saturation ET après le CONVOLVE**
- bande gauche : **PEAKING, 262 Hz, −2,5 dB, Q serré (≈ 2,5)**
- bande droite : **PEAKING, 349 Hz, −1,5 dB, Q ≈ 1,8**
- **Calcul à l'appui, et c'est la correction du défaut relevé par le juge « intégration ».** L'harmonique 3 du Fa1 tombe à **261,9 Hz**, c'est-à-dire exactement sur le **Do3 du piano (261,63 Hz)**. L'harmonique 4 du Fa1 est à **349,2 Hz**. Les voicings shell de la main gauche occupent 261 à 523 Hz : ce sont ces deux points-là qui se bagarrent, pas « 300 Hz au jugé ». **Et la position dans la chaîne est aussi importante que la fréquence** : posé avant la DISTORTION, le creux serait partiellement rebouché par les harmoniques que la saturation régénère dans cette même zone, puis recoloré par le CONVOLVE. Ici, rien ne repasse derrière. Ne creuse pas plus de −4 dB au total : au-delà la contrebasse devient creuse et perd son bois.

**6. UTILITY — dernier module**
- **LPF 5 kHz** · HPF off *(déjà fait par l'EQUALIZER #1, deux passe-haut en série changent la phase pour rien)* · **MONO BASS ON, FREQ 200 Hz** · **WIDTH 45 %** · PAN centre
- Le **passe-bas à 5 kHz** est le meilleur geste anti-balais de toute la chaîne, et il est gratuit : une contrebasse pizzicato n'a rien d'utile au-dessus. Tout ce qui dépasse est du souffle de la couche de bruit, de la fizz de saturation ou de l'aliasing de balayage — et ça vit exactement là où la batterie au balai occupe tout.
- **WIDTH 45 % et pas 100 %** : le CONVOLVE met de l'énergie décorrélée dans les côtés entre 250 Hz et 4 kHz, précisément là où le piano et les balais ont besoin du champ stéréo. Une contrebasse de trio est un point dans l'espace.

**Ce qu'il ne faut PAS mettre** : ni REVERB interne, ni HYPER, ni DIMENSION, ni CHORUS, ni FLANGER, ni PHASER. Tous cassent la compatibilité mono et fabriquent une largeur qu'un instrument acoustique unique n'a pas — le chorus étant désigné comme le plus destructeur pour la mono.

### En aval, dans Live

- **Réverb de pièce sur un RETURN partagé** avec le piano et les balais, jamais dans Serum. Règle : une réverb en insert à mix élevé appartient au *patch*, une réverb en départ à mix faible appartient au *mix*. Un trio jazz doit sonner dans **une seule pièce**. Room courte 1,0-1,4 s, pre-delay 15-20 ms, **coupe-bas du départ à 250-300 Hz**, envoi de la contrebasse nettement plus faible que celui du piano (≈ −20 dB) : dans un trio, c'est le piano qui remplit la pièce, la basse reste devant. Le CONVOLVE Woody n'est pas une pièce, c'est le bois de l'instrument : les deux coexistent.
- **Pas de coupe-bas supplémentaire** (déjà fait à 45 Hz dans Serum).
- **Pas de sidechain sur les mesures 1-24** : il n'y a pas encore de kick four-to-the-floor, seulement des balais. Le sidechain arrive à la mesure 25.
- **Niveau** : crête ≈ **−15 dBFS** sur la piste, soit 4 à 6 dB sous la main gauche du piano (pour repère, ta piste LEAD du projet est notée à −17,8 dBFS). Dans un trio jazz, la contrebasse se *sent* plus qu'elle ne s'entend : si on l'entend distinctement à l'écoute frontale, elle est trop forte.
- **Bounce** une fois validé (resampling, pas freeze : une piste resamplée reste automatisable). Ça fige le patch, libère le CPU, et permet surtout d'éditer l'attaque de chaque note à la main — ce qu'aucun réglage de Serum ne remplacera.

### Côté MIDI — sans ça, la moitié de la matrice ne sert à rien

- **Mesures 9-16, blanches** : vélocités **95 à 105**, fondamentale légèrement au-dessus de la quinte (98 / 92).
- **Mesures 17-24, noires** : temps 1 et 3 à **108-116**, temps 2 et 4 à **88-96**.
- **Approches chromatiques** : **72 à 82**. Ce sont des notes de passage, pas des points d'arrivée.
- **Ghost notes optionnelles** sur quelques contretemps : **20 à 30**. À cette vélocité il ne restera presque que le bruit de doigt — ce qui est littéralement ce qu'est une note fantôme. C'est le geste le plus rentable de tout le clip.
- **Durées à 80-90 % de la valeur**, et **aucun chevauchement** : le patch est en MONO, deux notes qui se touchent d'un tick et l'attaque de la seconde disparaît.
- Un **pitch bend de ±4 à 8 cents, différent, sur quelques notes seulement** : un contrebassiste joue sans frettes, chaque note est très légèrement fausse. C'est du travail manuel et c'est efficace.

---

## 5. Limites honnêtes

**1. L'inharmonicité des cordes — c'est le plafond dur, et il n'est pas contournable.** Une wavetable est par construction une série harmonique **exacte** : le partiel n est à exactement n fois la fondamentale. Une vraie corde de contrebasse est raide, donc son partiel n est à f·n·√(1+B·n²) — un étirement progressif, croissant avec le rang, et sur une corde aussi épaisse le partiel 10 est déjà sensiblement trop haut. Cette légère fausseté interne est une grosse part de ce qui fait l'épaisseur d'une contrebasse, et de ce qui fait qu'un synthé sonne propre et mort. Aucun réglage de `SawRounded`, aucun warp, aucun filtre ne la produit. Les seules issues seraient un léger désaccord (interdit sur une basse : il fait fluctuer la fondamentale), une FM à rapport non entier (qui détruit la stabilité de hauteur), ou un échantillon.

**2. Deux dimensions pour une vérité qui en a N.** ENV 3 (WT POS) et ENV 2 (cutoff) approximent, à deux échelles de temps, un phénomène qui en a des dizaines : sur une corde réelle **chaque harmonique a sa propre enveloppe d'amplitude**. Toutes les nôtres s'éteignent en bloc, dans un ordre fixe. À l'écoute, ça donne un assombrissement « lisse » là où une vraie corde a un assombrissement « grumeleux ». La rampe wavetable est nettement plus proche qu'une pente de filtre seule — c'est pour ça qu'elle gagne — mais elle reste une approximation.

**3. Aucune résonance sympathique.** Quand un contrebassiste pince un Fa, les trois autres cordes vibrent en réponse et remplissent l'espace entre les notes du walking. Serum n'a aucun mécanisme pour ça, et le patch est mono, donc il n'y a même pas de voix à coupler. **L'espace entre deux noires sera plus vide que sur un disque**, et c'est souvent ce qui trahit un instrument virtuel avant le timbre lui-même. Contournement partiel hors Serum : un Collision ou un Tension d'Ableton en insert derrière, en mode résonateur, à mix très faible — coûteux en CPU et délicat à régler (Ableton avertit lui-même qu'il est « très facile de trouver des combinaisons qui ne produisent aucun son »).

**4. Un seul timbre pour toutes les notes.** Pas de corde à vide contre corde bouchée (une corde à vide sonne beaucoup plus longtemps et plus brillamment que sa voisine bouchée, et c'est une part du groove réel d'un walking), pas de changement de corde, pas de note faible ni forte, pas de wolf note, **pas de round robin tonal** — Serum 2 n'en fait pas. Les lignes M13 et M14 récupèrent peut-être 20 % de cette variation. Les 80 % restants ne sont accessibles qu'en éditant l'audio après resampling, note par note. Sur 32 noires consécutives, l'oreille finira par entendre la répétition.

**5. Pas de main gauche — c'est-à-dire la moitié du réalisme d'un walking bass.** Glissandos vers la note cible, étouffements à la paume, harmoniques naturelles, doubles cordes. Ça ne s'écrit pas au piano roll et Serum ne le produira pas. Le walking des mesures 17-24 sonnera **correct mais pas joué**.

**6. L'attaque reste le point faible, malgré `FretNoise B`.** Les 30 à 60 premières millisecondes d'un pizzicato réel contiennent du bruit chaotique et inharmonique : la pulpe qui accroche puis lâche, la corde qui claque contre la touche, le bois qui répond. Un vrai échantillon de bruit de doigt est beaucoup mieux qu'une rafale de bruit blanc, et la couche multisample de l'étape 35 comble une part du reste — mais c'est l'écart le plus **audible** du patch, et celui qui s'entend le plus dès qu'on monte le fader.

**7. Pas d'archet, pas de bruit entre les notes.** Ce patch est strictement pizzicato ; un archet demanderait un modèle d'excitation continue stick-slip, hors de portée. Et les glissements de main gauche, le frottement des doigts sur la touche, le claquement d'une corde lors d'un déplacement se produisent quand **aucune note MIDI n'est déclenchée** : un synthé ne peut par construction rien produire à ce moment-là.

**8. Où ça va se voir dans ce morceau précisément.** **Mesures 17-24 : ça passera.** Le piano masque, les notes sont courtes, l'oreille n'a pas le temps d'analyser la traîne. **Mesures 9-16 : c'est là que le risque est maximal.** Des blanches, dans une texture très clairsemée, exposées, avec 1 000 ms pour entendre que la queue de la note est une décroissance lisse. Si ce patch doit être jugé, c'est sur ces huit mesures — dépense ton temps de réglage là, et écoute-les en contexte avec le piano avant de toucher à quoi que ce soit d'autre.

**9. Deux réserves de méthode.** Le routage `Bend +/−` présenté ailleurs comme « position de pincement » est une interprétation, pas une affirmation du manuel : c'est pour ça qu'il est remplacé ici par un `Asym` fixe. Et je ne peux pas garantir les étiquettes exactes de trois contrôles dans ta build — le `one-shot` et le départ aléatoire du canal NOISE, le `Key Track` par clic droit sur le CUTOFF du filtre **de synthèse** (il est documenté sur celui du module FILTER du rack FX), et l'existence de `ENV 1 DEC` / `ENV 2 DEC` comme destinations de matrice. Chacun a son repli dans le tableau. Je préfère te le dire que d'inventer un nom.

**10. Et le point qu'il faut dire en dernier, parce qu'il compte : quand faut-il plutôt un instrument échantillonné.** Sur le seul critère du réalisme, `Double Bass Pizz Jazz.sfz` chargé **seul** dans OSC A en moteur Multisample battra ce patch, sans discussion possible, et en dix minutes au lieu de deux heures. La littérature est franche sur le sujet parallèle du piano : « il n'y a jamais eu de piano acoustique convaincant produit par synthèse soustractive, additive ou FM ; seuls les échantillons semblent y parvenir. » La contrebasse pincée est plus facile qu'un piano — attaque plus simple, traîne plus sourde — donc la synthèse s'en sort beaucoup mieux, mais le classement ne s'inverse pas.

**Prends le multisample seul si** : la contrebasse doit être exposée en solo plus de quelques secondes ; l'intro doit sonner « vraie prise jazz de 1962 » ; ou tu veux les articulations (glissando, étouffé, corde à vide).

**Garde ce patch si** : tu veux un timbre **entièrement modulable par la vélocité et par la note** (un multisample ne te donne que les couches enregistrées, et ce patch répond en continu — c'est ce qui rend les ghost notes à vélocité 20-30 possibles gratuitement) ; zéro RAM et zéro dépendance à un fichier externe ; un son qui appartient au disque plutôt qu'à une bibliothèque ; et surtout un patch qui pourra **morpher vers la partie électronique à la mesure 25** avec une seule macro. Dans un mix avec piano et balais, à niveau modéré, il se lira comme une contrebasse. En solo pendant trente secondes, il se trahira. **Les mesures 9 à 24 sont un accompagnement, pas un solo : c'est le bon usage de cette approche.**

**Piège à éviter au passage** : ne tente pas de glisser un `.aif` de ta bibliothèque Ableton dans Serum pour remplacer `FretNoise B` ou le multisample. J'ai vérifié les en-têtes — ce sont des fichiers **AIFC** dont le tag de compression du chunk COMM vaut `able`, le codec lossless propriétaire d'Ableton. **Serum 2 ne les lit pas.** Il faudrait les réexporter en WAV depuis Live. Les fichiers d'usine de Serum 2 listés ci-dessus évitent entièrement ce détour.

---

## 6. Vérification

### À l'oreille — six tests, dans cet ordre

1. **Le différentiel.** Tiens un F1. À mi-parcours de la note (≈ 450 ms) elle doit être devenue **presque sourde tout en restant clairement audible**. Si elle est encore brillante à mi-parcours, baisse ENV 3 DEC puis ENV 2 DEC. Si elle devient inaudible en même temps qu'elle s'assombrit, monte ENV 1 DEC. C'est le test le plus important : c'est précisément là que le patch devient une contrebasse, et le réglage donne l'impression, knob par knob, qu'on étouffe le son.
2. **Le bruit de doigt.** Coupe le canal NOISE. La note doit devenir **molle**, pas « moins claquante ». Si tu entends disparaître un « tic » identifiable comme événement séparé, il était trop fort : −4 dB.
3. **La dérive de hauteur.** Bypass de la ligne M10, A/B sur la même note. L'effet est petit et **immédiatement reconnaissable** : sans lui, le son devient figé, « échantillonné », il perd le côté vivant. Si tu n'entends aucune différence, la quantité est trop faible.
4. **Le corps.** Bypass du CONVOLVE. Le son doit passer nettement de « bois » à « synthé ». Si rien ne change, le MIX est trop bas.
5. **Le registre.** Joue F1 puis G2. Le **G2 doit être plus court et relativement moins riche** que le F1. Si c'est l'inverse, le signe de M11/M12 est faux (les sources se contredisent sur la normalisation de la source Note : c'est ce test qui tranche, pas le chiffre).
6. **La répétition.** Joue la même note **quinze fois de suite**. Elle ne doit pas sonner deux fois exactement pareil. Si si, LFO 3 n'est pas en mode `Trig`, ou le départ aléatoire du NOISE n'est pas actif.

### À la mesure — six contrôles objectifs

7. **SPAN sur la piste seule, F1 tenu.** Le pic du spectre doit se situer vers **175 Hz (H2)** ou **262 Hz (H3)**, **PAS sur 87,31 Hz**. Sur une vraie contrebasse à 87 Hz, la fondamentale est faible — la caisse rayonne mal si bas, et l'oreille reconstruit la hauteur à partir des harmoniques 2 à 5. **Si le pic est sur la fondamentale, tu as fabriqué une basse de synthèse.**
8. **Contenu de la traîne.** 300 ms après l'attaque, il ne doit plus rien y avoir de significatif **au-dessus de 1,2 kHz**. C'est la garantie que la queue de la note ne viendra pas encombrer la zone des balais. Avec un cutoff de repos à 380 Hz et une pente de 24 dB/oct, 1,2 kHz est à −40 dB : si tu mesures plus, c'est que M2 est trop fort ou que ENV 2 DEC est trop long.
9. **Temps de montée de la crête.** Zoome sur la forme d'onde d'une note : la crête doit être atteinte en **8 à 15 ms**. Une basse de synthèse atteint sa crête en 1 ms ; une contrebasse met une dizaine de millisecondes parce que la caisse doit se mettre à rayonner. **C'est le test le plus discriminant du lot, et le seul totalement objectif.**
10. **Balayage du filtre.** Clic droit sur la fenêtre de FILTER 1 › **Frequency Response & FFT**, F1 tenu : le pic doit atteindre **2,8 kHz** puis retomber à **380 Hz en 260 ms**. Ajuste la quantité de M2 entre 45 et 65 % pour y arriver — le chiffre donné est un point de départ, la vérification est visuelle.
11. **Mono.** Passe le master en mono via l'Utility de Live. **Rien ne doit s'amincir.** Si la basse maigrit nettement, c'est un problème de phase, pas de niveau — regarde WIDTH sur l'UTILITY et le MIX du CONVOLVE.
12. **Niveau et contexte.** Crête vers **−15 dBFS** sur la piste avant tout bus, soit 4 à 6 dB sous la main gauche du piano. Puis, le seul test qui décide vraiment : **joue les mesures 9 à 16 avec le piano, et rien d'autre**. Huit blanches nues dans une texture clairsemée. Si ça tient là, ça tiendra partout dans ce morceau.