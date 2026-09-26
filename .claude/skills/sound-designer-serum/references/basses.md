# Basses — fiche de référence

Recherche web du 18 septembre 2026, 15 pages lues. `[D]` = documenté. `[I]` = interprétation. `[⚠]` = les sources se contredisent.

---

## La seule règle sur laquelle tout le monde converge

`[D]` Sound on Sound, deux fois : éviter « les patches multi-oscillateurs désaccordés, parce que le battement peut faire fluctuer la fondamentale du sub de façon inacceptable ». Et : le synthé de renfort doit rester « un seul oscillateur, pour éviter une modulation de niveau indésirable ».

`[D]` Même source : « s'il y a plus d'une partie de basse, je n'en choisis normalement **qu'une seule** comme source principale de grave et je coupe-bas les autres autour de **100 Hz**, pour éviter les vicieuses annulations de phase ».

**Une seule source tient le fondamental, un seul oscillateur, sans désaccord. Tout le reste est coupé-bas.** C'est le seul point où toutes les sources sérieuses s'accordent, et c'est systématiquement absent des blogs.

Sources : https://www.soundonsound.com/sound-advice/q-whats-best-way-create-sub-bass-synth-sounds · https://www.soundonsound.com/techniques/mixing-bass

---

## 1. Sub

### Documenté

**Sinus ou triangle.** Le sinus est « effectivement une seule fréquence », sans contenu harmonique donc sans besoin de filtrage. SOS préfère explicitement le **triangle pour le layering** : il « se marie mieux avec, plutôt qu'écrase, le son auquel il est superposé ». Scie et carrée sont à éviter dans ce rôle.

**Mono.** La largeur stéréo dans le grave « peut réduire la puissance et la cohérence en mono, et pose problème au pressage vinyle ». Un patch stéréo risque une annulation telle que « les basses fréquences ne sortiront pas des systèmes de club ».

Trois raisons physiques `[D]` (mixanalog, https://blog.mixanalog.com/mono-low-end-guide) : le cerveau localise mal le bas du spectre (longueurs d'onde longues) ; les codecs lossy jettent le canal Side en premier ; sur vinyle le mouvement latéral (Mid) se grave sans problème, le vertical (Side) fait décrocher la pointe de lecture.

**Plage.** iZotope : le grave va de 20 à 250 Hz, la zone **20–160 Hz** contient typiquement le plus d'énergie pour kick et basses ; couper « 20 ou 30 Hz et en dessous » libère de la marge sans perte audible. Sonarworks chiffre le fondamental : kick 30–80 Hz, sub de synthé 30–100 Hz.

**Éviter le flou.** Cause n°1 selon SOS : quand le sub recouvre la fondamentale d'une basse déjà présente, « si les crêtes et les creux ne suivent pas celles de la fondamentale existante, la combinaison peut finir par sonner **moins** grave qu'avant ».

**Enveloppe.** Pas si rapide qu'elle crée des clics. Et « les parties de sub doivent être contrôlées assez serré en dynamique, sinon elles mangent vraiment la marge du morceau ».

**Filtre résonant sur un sub** : s'il y en a un, il **doit suivre la hauteur** (key tracking), sinon chaque note voit un harmonique différent boosté et le niveau devient incohérent.

### Points de départ

1. Un oscillateur sinus, mono, unison 1, pas de détune, pas de chorus. Coupe-bas 20–30 Hz. Amp A 3–8 ms, release ~20–30 ms.
2. Pour du corps : triangle + passe-bas raide. SOS dit « passe-bas assez sévèrement toute forme d'onde de sub non sinusoïdale » sans donner de valeur. `[I]` Cutoff de départ 120–150 Hz, 24 dB/oct.
3. **Glide** : LANDR donne ~200 ms comme référence. `[I]` À 120–126 BPM une croche fait 238–250 ms : 200 ms occupe presque toute la croche, très audible. Pour du deep house discret viser plutôt **40–80 ms**.

---

## 2. Reese

### Origine — le mécanisme d'origine n'est pas celui qu'on croit `[D]`

Quatre sources indépendantes concordent : **Kevin Saunderson, 1988, sous l'alias Reese, titre *Just Want Another Chance***, réalisé sur un **Casio CZ-5000**, donc en **synthèse par distorsion de phase**. Le son est passé au jungle en **1994** quand Renegade & Ray Keith l'ont samplé sur *Terrorist*.

`[I]` Les deux scies désaccordées sont la **reconstruction moderne**, pas le mécanisme original. C'est ce qui explique pourquoi les reconstructions sonnent Reese sans sonner comme le disque de 1988. Distinction rarement faite.

Sources : https://blog.native-instruments.com/reese-bass/ · https://toolroomacademy.com/features/everything-you-need-to-know-about-the-reese-bass/ · https://www.attackmagazine.com/technique/tutorials/reese-bass-redux/

### Le détune est un réglage de tempo, pas de largeur

`[D]` Attack Magazine : le désaccord crée « des harmoniques avec un mouvement rythmique, **dont le tempo peut être contrôlé en ajustant l'accord fin** ». C'est la formulation la plus utile.

`[I]` La fréquence de battement est la **différence** entre les deux fréquences. 30 cents sur un Fa1 (43,65 Hz) donnent ~0,76 Hz d'écart, soit un cycle toutes les 1,3 s. Sur un La1, plus rapide. **Conséquence jamais mentionnée : le battement change de vitesse selon la note jouée.** Une basse Reese ne pulse pas au même tempo en haut et en bas de la ligne. Régler le détune à l'oreille **sur la note la plus grave**, pas sur la plus aiguë.

### `[⚠]` Valeurs de détune

| Source | Oscillateurs | Détune |
|---|---|---|
| Attack Magazine | 2 sinus, mono | ±27 cents |
| Native Instruments | 2 saws, mono | ±30 cents ; version douce ±15 |
| LANDR | saw + saw/carrée | « 0,25 à 0,5 **cents** » |

La valeur LANDR est incohérente d'un facteur ~100 : à 0,3 cent sur un Fa1, le battement dure plus de deux minutes, donc inaudible. **Confusion cents / demi-tons presque certaine. À ignorer.**

Attack et NI, indépendants, convergent sur **±27 à ±30 cents**. C'est la fourchette à retenir.

`[⚠]` mineur sur la forme d'onde : Attack construit avec **deux sinus** (battement d'amplitude pur), NI et Toolroom avec des **saws** (battement + richesse harmonique). Ce ne sont pas les mêmes sons : la version Attack est un « sub qui respire », la version NI un Reese drum & bass.

### Filtre et effets `[D]`

NI : passe-bas cutoff ~650 Hz, résonance ~14 % pour le son jungle lissé, puis overdrive et filtre à encoche balayé automatisé. LANDR : passe-bas entre 116 et 225 Hz, chorus à ~50 %.

### Le problème mono, et sa seule solution propre

`[D]` Attack identifie le symptôme sans le nommer phase : « cette version a un niveau de volume plutôt incohérent », visible sur le vu-mètre qui monte et descend. C'est le battement qui module l'amplitude de la fondamentale — exactement ce que SOS interdit sur un sub.

`[D]` LANDR donne le remède : centrer tout **en dessous de 120 Hz**, et la technique avancée « isoler les médiums et aigus du Reese, jouer la fondamentale sinus avec un synthé séparé ».

`[D]` Toolroom et Future Audio Workshop ne donnent **aucune** solution au problème mono.

`[I]` **Le Reese est structurellement incompatible avec le rôle de sub.** La seule architecture propre est à deux couches : sub sinus mono séparé, Reese coupé-bas au-dessus. Toutes les sources qui donnent un Reese full-range sans cette séparation produisent un grave instable — et **aucune source pro-détune ne mentionne cette contrainte**, ce qui est leur principale faiblesse.

### Points de départ

1. **Reese médium** : 2 saws, ±28 cents, mono/legato, LP 24 dB ~650 Hz, résonance ~14 %, **coupe-bas 120 Hz**, overdrive léger.
2. **Sub séparé** : 1 sinus mono, même ligne MIDI, LP 120 Hz, aucun détune.
3. ±15 cents = lent et doux, ±30 cents = signature drum & bass.

---

## 3. Neuro / growl

**Fiabilité faible** : ces sources sont des blogs de vendeurs de presets, chiffres non vérifiés et parfois recopiés entre eux.

### Chaîne documentée

Source : deux saws désaccordées, une wavetable Reese, ou une wavetable digitale râpeuse. Ordre : **mouvement de filtre → distorsion → compression → nettoyage EQ → phaser/flanger optionnel**. Filtres : notch, bandpass, comb, **voyelle (vowel)**, lowpass.

**Formants** : filtre formant, résonance **20–40 %** pour que les voyelles restent définies, LFO lent ou enveloppe sur le cutoff avec de **petites** plages. Warp `Bend` à 30–50 % donne un grognement nasal ; FM à 15–25 % un râle guttural ; au-delà de 40 % c'est métallique et hurlant. **Unison à 1 pendant la conception** : un growl mono frappe plus fort.

**Traitement** : Overdrive 40–60 %, phaser rate 1/2 sync feedback 60 % mix 50 %, EQ coupe-bas 120 Hz et creux −3 dB vers 400 Hz, compresseur multibande ciblant 2–5 kHz.

**Patch complet mesurable** (BassGorilla) : Osc A warp Bend ± = 6, Osc B = 47, filtre **High Notch 12**, cutoff 141 Hz, résonance 49, LFO 1 en modulation **inversée −74** sur le cutoff, rate 1/2, **trigger mode « Trigger »**, distorsion Diode 2 drive 20, flanger depth 30 feedback 64, pitch bend ±12.

**Resampling** : Serum 2 permet « Resample to Oscillator » pour transformer le son traité en table sans quitter le plug-in. « Après deux ou trois passes le son prend une densité qu'aucune passe unique n'atteint. » Minimum deux passes, avec un rythme de modulation différent à chaque cycle.

### Trois avertissements `[I]`

**Le trigger mode « Trigger » est essentiel et souvent omis.** Sans lui le LFO tourne librement et chaque note attrape le growl à une phase différente. C'est la différence entre un growl reproductible et un growl aléatoire.

**Les recettes en ligne sont calées sur 140–150 BPM.** Un LFO à 1/2 vaut **952 ms à 126 BPM** : beaucoup trop lent pour de la bass house. Transposer vers 1/4 ou 1/8.

**Les cutoffs cités ne sont pas des valeurs de basse.** Le 141 Hz de BassGorilla est un High Notch balayé par un LFO à −74 : c'est le point de départ du balayage, pas la coupure du son.

Sources : https://monosounds.studio/serum-2-dubstep-growls/ · https://bassgorilla.com/serum-tutorial-super-growl-bass-in-ableton-live/ · https://edmtemplates.net/blogs/edm-templates-blog/how-to-make-neuro-dnb-bass-in-serum-2

---

## 4. 808

### Le circuit `[D]`

Roland (source primaire) : « le timbre unique vient de la combinaison d'un oscillateur sinus, d'un filtre passe-bas et d'un VCA », donnant « le timbre d'une grosse caisse combiné à celui d'une timbale ».

MusicRadar : « le kick de la 808 est essentiellement un circuit résonant ; la constante de temps détermine sa fréquence et son temps de déclin ». La fonction **Accent double la fréquence d'oscillation pendant la durée d'un demi-cycle**. La machine était **théoriquement accordée à 56 Hz**, mais les exemplaires réels variaient beaucoup.

### Pourquoi il est kick ET basse `[D]`

Le kick 808 « pouvait décliner bien plus longtemps que n'importe quelle caisse acoustique — **assez longtemps pour qu'une fois accordé sur une note, il cesse d'être une caisse et devienne un instrument de basse** ».

Roland recommande de privilégier les **intervalles forts** (octave, quinte juste, quarte juste) plutôt que des hauteurs absolues, « puisque certaines sub-fréquences sont presque inaudibles ».

### Accordage et déclin `[D]`

Accorder avec un accordeur ou un patch de synthé initialisé. **Utiliser un sampler avec une vraie enveloppe ADSR** plutôt qu'une lecture simple, car **la hauteur dérive pendant le long déclin**, dérive amplifiée par la distorsion. Point technique rarement mentionné.

Glide : basculer le sampler en **Legato** puis régler le Glide Time. Signature trap et drill.

### Distorsion et fondamentale manquante `[D]`

La distorsion règle le problème de **traduction** sur petites enceintes : la saturation génère des harmoniques plus haut dans le spectre et **l'oreille reconstruit la fondamentale manquante à partir de ces harmoniques**. Phénomène documenté.

SOS dit la même chose côté mixage : « une arme secrète pour mixer n'importe quelle basse, ce sont ses fréquences hautes, à peu près tout au-dessus de 300 Hz », et préfère la **distorsion en parallèle** plutôt qu'en insert, avec un passe-bas « autour de 2–3 kHz » si le boost est important, pour ne pas étouffer l'air des voix.

### Points de départ `[D]`

1. Superposer un kick court **vers 80–100 Hz** pour le punch. Coupe-bas à **20–25 Hz** sur le 808 pour éliminer le grondement inaudible qui ruine la traduction.
2. Boost **100–600 Hz** avec une saturation douce pour la présence bas-médium.
3. Sidechain à attaque et release **rapides** pour que le kick superposé fasse ducker le 808 sans écrasement audible.

---

## 5. Deep house contre bass house

### Tempo `[D]`

Bass house = **128 BPM standard**, certains titres à 130 ; il vient de l'electro house, écrit lui aussi à 128. Deep house = **120 BPM**. `[I]` 126 BPM est entre les deux, plus proche du bass house.

### Ce qui distingue les deux basses `[D]`

Bass house : lignes « crasseuses et modulées qui dominent souvent le mix », fusion d'éléments du dubstep et de l'electro house. `[I]` C'est pourquoi les techniques de growl de la section 3 s'y appliquent et pas au deep house.

Deep house : basse « plus lisse et mélodique », « **portante et arrondie** plutôt que sculptée pour l'impact ». Définition la plus précise trouvée : les basses deep house « tendent à être des sinus, ou plutôt des saws filtrées au point d'être presque des sinus ».

### Patch deep house documenté (ModeAudio, sur Massive)

Osc 1 sinus, Osc 2 même table montée vers la carrée, accordé **−12 demi-tons**, plus un ring-mod à −12. Filtre **Lowpass 4** (pente raide). Résonance accordée vers le **5e harmonique**, cutoff placé pour donner un caractère de **tierce majeure**. Et surtout : **une enveloppe dédiée sur le cutoff avec une attaque allongée** — c'est elle qui donne « la qualité arrondie caractéristique qui fonctionne vraiment dans une ligne de basse deep house ».

`[I]` Attaque d'enveloppe de filtre de **20–60 ms** pour cet arrondi.

### Patch bass house documenté (EDMProd)

Base **sinus + FM**, modulateur « monté de 2 octaves et 7 demi-tons » (deux octaves et une quinte : rapport **6:1** `[CALC]` ; une octave et une quinte donneraient 3:1). **LFO en mode enveloppe sur le cutoff**. Puis OTT, EQ, distorsion, sidechain.

Sur le kick : choisir un kick « punchy, mais moins que pour du tech house, un kick qui peut s'écarter du chemin de la basse, c'est-à-dire pas trop de grave ». `[I]` Énoncé côté kick, c'est l'arbitrage de la section 6 : **en bass house, la basse tient le fondamental, pas le kick.**

---

## 6. Division du grave

### `[⚠]` Fréquence de passage en mono — personne ne justifie son chiffre

| Source | Valeur |
|---|---|
| SOS | coupe-bas des couches secondaires ~100 Hz |
| LANDR | centrer sous 120 Hz |
| Weapon Sounds | 120 Hz strict |
| musicguymixing / Ask Audio | tout sous 150 Hz en mono |
| mixanalog | balayer, le point utile est **entre 100 et 200 Hz** |
| Forum Ableton | 250 Hz vs ~100 Hz |

`[I]` Le désaccord n'est pas idéologique : les auteurs répondent à des questions différentes. 100–120 Hz = « où le sub s'arrête ». 200 Hz = « où l'annulation cesse d'être audible ». 250 Hz = prudence maximale.

**La méthode de mixanalog est supérieure aux valeurs fixes** : balayer un coupe-bas et écouter **où le grondement hors phase disparaît**, plutôt que poser 120 Hz par habitude.

### Architecture documentée (Weapon Sounds)

Encodage M/S. Canal **MID coupe-bas à 120 Hz** pour isoler l'énergie sub pure en mono. Canal **SIDE** pleine bande avec boost optionnel 200–300 Hz pour le corps, élargi au-dessus de 500 Hz. Décodage.

**Vérification** : si le sub disparaît ou s'amincit nettement en mono, c'est un problème de phase, pas de niveau.

### Mono maker `[D]`

**Le device Utility d'Ableton a un bouton « Bass Mono » avec fréquence de crossover réglable, depuis Live 10.** Tout ce qui est en dessous passe en mono. C'est l'outil natif direct, pas besoin d'un Mono Maker tiers.

Avant Live 10, la méthode manuelle : Audio Effect Rack avec deux EQ Three et un Utility à Width 0 sur la chaîne grave.

Autres outils cités : Brainworx Mono-Maker, iZotope Ozone Imager 2 (gratuit), Nugen Monofilter.

---

## 7. Kick et basse

### Le diagnostic `[D]`

SOS : « le conflit sous-100 Hz le plus critique dans les mixes modernes est celui entre la basse et le kick : leurs basses fréquences sont normalement responsables de **la part du lion du niveau de sortie du bus master** ».

Sonarworks : kick 30–80 Hz fondamental / 300–600 Hz boîte à creuser / 4–8 kHz clic. Basse : sub 30–100 Hz / 150–400 Hz zone boueuse / 800 Hz–2 kHz clarté.

### `[⚠]` Profondeur du sidechain

SOS, le plus conservateur : ducker brièvement la basse de **2–3 dB** à chaque kick, pour conserver la marge en gardant le poids des deux.

Splice et LANDR : **ratio 10:1** si on veut complètement dégager la basse, « ce qui peut produire un son pompant » ; 2:1 ou 4:1 pour un effet naturel.

`[I]` Ce n'est pas une erreur mais une différence d'objectif : SOS mixe pour la marge, le dance mixe pour l'effet rythmique. **En house et techno, le pompage est un élément musical.**

**Mise en garde SOS spécifique et absente partout ailleurs** : sur la compression de basse, l'attaque est critique — « trop rapide, le compresseur arrondit les crêtes individuelles de la forme d'onde grave, **ce qui produit de la distorsion** ; trop lente, la réduction de gain ne rattrape pas les pics brefs ». Valable quel que soit l'objectif.

**Sidechain multibande** : ne ducker que la bande de recouvrement, typiquement **sous 100–200 Hz**, au lieu de tout le signal.

iZotope inverse le raisonnement habituel : c'est **le kick qui compresse la basse** plutôt que l'inverse, « parce que le kick n'est là que pour le rythme ». `[I]` Affirmation contestable en house et techno, où le kick porte une part du fondamental.

### `[⚠]` Accordage du kick — désaccord de fond non résolu

**Position A**, majoritaire : accorder le kick à la tonalité. « Quand la note du kick correspond aux harmoniques du morceau, les fondamentales tonales sont alignées. »

**Position B**, opposée : « accorder le kick pour que son fondamental **ne soit pas** dans la même plage de fréquence que les notes de basse fondamentales », pour éviter le masquage.

`[I]` Les deux sont défendables et incompatibles. Accorder à la tonique maximise la fusion tonale **et** le masquage. Décaler minimise le masquage mais peut sonner à côté. **C'est un arbitrage de production, pas une règle.**

Repères de hauteur `[D]` : kick grave à 50 Hz ≈ Sol1, kick haut à 70 Hz ≈ Do#2, kick 22" en accord médium ≈ 60 Hz ≈ Si1.

### Phase et polarité `[D]`

Le device **Utility a un bouton d'inversion de phase** qui retourne la polarité de 180°. Procédure : inverser la polarité de la basse et comparer les deux orientations **sur un oscilloscope**, pour voir dans quelle version les formes d'onde du kick et de la basse bougent dans la même direction.

Si plusieurs échantillons de kick sont superposés, leurs attaques doivent s'aligner et leurs polarités correspondre. Passer kick et basse en mono pour ce contrôle.

### Ordre d'opération `[I]`, synthèse des sources

1. Décider qui tient 30–80 Hz.
2. Coupe-bas l'autre à 100–120 Hz.
3. Vérifier la polarité à l'oscilloscope.
4. **Seulement ensuite** le sidechain.
5. Release calé pour que la basse soit revenue avant la frappe suivante. À 126 BPM une noire fait 476 ms, donc release ≤ 200–250 ms.

---

## 8. Ce qui n'est documenté nulle part

- La fréquence de battement d'un Reese en fonction de la note. Calculable, jamais expliquée.
- Le transport des réglages de growl d'un tempo à l'autre. Toutes les recettes sont en 140–150 BPM.
- Des valeurs de release de sidechain liées au tempo. Aucune source n'en donne.
