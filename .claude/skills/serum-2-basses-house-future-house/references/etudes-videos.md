# Études des tutoriels vidéo (transcriptions)

Étude du 05/10/2026, en session cloud, par un sous-agent de Claude Code. Sources : sous-titres automatiques anglais de YouTube récupérés avec `yt-dlp` (sans la vidéo), nettoyés en blocs minutés de 20 s ; transcriptions non conservées dans le dépôt. Les minutages viennent des horodatages des sous-titres, à ±5 s près. Identifiants : registre `tutoriels-a-consulter.md`. Après ces trois vidéos, YouTube a bloqué la session (vérification anti-robot) : les autres vidéos ★ restent à étudier sur le Mac ou par transcription collée (procédure de `sources.md`).

Conventions :
- Ce qui n'est pas marqué rapporte un geste **dit** dans la vidéo.
- **[DÉDUCTION]** marque une déduction sur l'effet ou sur le contrôle visé, vérifiée seulement contre la cartographie Serum 2 du dépôt (`sound-designer-serum/references/serum2-cartographie.md`).
- Les mots corrigés sont suivis de la correction entre crochets.
- Aucun son n'a été entendu et aucune image n'a été vue. Une valeur « montrée à l'écran, non dite » reste inconnue.
- Les noms des tables d'usine (« Square Up and Down », « JF Flute », « Bass Plug », « Softest Growl ») **ne figurent pas dans le dépôt** et sont à vérifier dans le navigateur de tables de Serum 2. Seules les familles sont confirmées : dossiers `S2 Tables/Analog/` et `S2 Tables/Digital/`, table `Spectral/Monster 8 [SL].wav`.

---

### F01-01 The FATTEST DNB Bass in Serum 2 (Huge Sub + Low-Mid Weight, Stupid Easy Method) — Art1fact (Serum 2, mise en ligne 08/02/2026, 21:55)

- **Statut :** transcription automatique anglaise étudiée le 05/10/2026. Image et son non vus ni entendus.
- **Version :** Serum 2 d'après le titre et la phrase « the fattest low end in Serum 2 » [0:05]. Numéro de version non dit. Le formateur dit ne pas avoir utilisé Serum depuis longtemps [2:05].
- **Chapitres :** 0:00 Project setup · 1:36 Building the core bass sound · 3:58 Advanced sound shaping · 9:02 Balancing and gain staging · 11:46 Character and modulation · 15:16 Workflow and design tips · 17:20 Layering and external effects · 19:40 Resources and conclusion.

**Recette pas à pas**
- **MIDI** [0:50–1:15] : il enregistre « a couple of MIDI notes », puis un motif « a bit more funky ». Notes, durées et tonalité non dites.
- **Enveloppe d'amplitude** [1:20–1:25] : « it's a bit clicky », donc attack et release montés « a bit ». Valeurs non dites.
- **Oscillateur sinus** [1:35–1:50] : le patch part d'un sinus, « just a sub bass », « obviously the main part ». L'oscillateur qui le porte (OSC A ou SUB) n'est pas dit. [DÉDUCTION] Le filtre est ensuite posé sur « just B » [2:40], donc le sinus est probablement sur A et la carrée sur B.
- **Oscillateur carré** [1:55–2:30] : il cherche une carrée, trouve « basic shapes » et passe d'une frame à l'autre jusqu'à la carrée (« can I go between them? Yeah, like this »). Il la place **une octave au-dessus du sub** (« one octave higher than the sub »), pour remplir « all the rest of the remaining low end ». [DÉDUCTION] Table `Analog/Basic Shapes`, WT POS sur la frame carrée ; position et octave absolue non dites.
- **Filtre 1** [2:35–2:55] : « filter just B », « take out the high end ». Type et cutoff non dits (« something like that »). Le récapitulatif [19:05–19:10] précise : « take those out first with a low pass ».
- **LFO** [3:05–3:45] :
  - « a really slow LFO » vers le cutoff du filtre 1 (« open up the filter »), puis « a bit slower », « maybe like a dotted pattern » [3:15].
  - Même LFO vers le **niveau de la carrée** (« more extreme on the square wave ») et, moins fort, vers le **niveau du sinus** [3:25–3:40].
  - « I don't want it to open quite so much » [3:45] : il réduit la profondeur vers le cutoff.
  - Forme, division exacte et mode non dits.
- **Écoute avec le break de batterie** [4:00].
- **Filtre 2 en série** [4:10–4:15] : « run that first filter into filter two ».
- **Filtre 2, essai 1** [4:15–4:50] : « band reject », dans « miscellaneous » (= Bandreject, catégorie Misc), « let's make it wide ». [DÉDUCTION] VAR = WIDTH, la largeur du creux. Le LFO est envoyé sur ce cutoff [4:40]. « I've gone too low there… missing the whole beginning part » [4:50] : la plage de modulation était trop basse.
- **Filtre 2, essai 2** [5:15–5:50] : il est peu convaincu par le Bandreject et passe à un passe-bande. « There's a few different types of band passes… this one's got extra kind of shape… a little extra kind of peak ». Type exact non dit. [DÉDUCTION] Peut-être un type Multi « BP » (Band + Peak), à confirmer à l'écran.
- **FM entre les deux oscillateurs** [6:25–7:00] : il n'aime pas encore les aigus de la carrée. « We definitely want that octave range. So… maybe a bit of FM between them », puis « let's try the other way around » [6:50] et « that's quite nice there » [7:00]. Le sens retenu (A module B ou B module A) et la quantité ne sont pas dits. [DÉDUCTION] Warp FM (A) sur B, ou FM (B) sur A, sur un rapport d'octave.
- **Retouche du filtre** [7:10–7:15] : « dial in that filter a bit more sweetly ». Valeur non dite.
- **Warp sur la carrée** [7:55–8:15] : « adding a little warp to this square wave », « modulate that a bit on the bend », « that bend plus was still pretty good ». Mode **Bend +**, quantité non dite. La source de modulation n'est pas nommée. [DÉDUCTION] Le même LFO.
- **Unison sur la carrée** [8:25–8:30] : « sounds pretty good in stereo… we could actually detune it like this », « give a little bit more priority to the center ». Nombre de voix et detune non dits. [DÉDUCTION] « priority to the center » désigne probablement BLEND baissé ou peu de voix.
- **Modulation de la FM** [8:40] : « a bit of movement on that FM ». [DÉDUCTION] Le LFO va vers la quantité de FM.
- **Équilibre et contrôle** [9:25–11:40] :
  - Sub monté [9:25]. Forme du LFO retouchée [9:40].
  - Lecture sur SPAN [10:05] : « really nice and full », « sitting actually a little bit high for a D ».
  - Il essaie un sub supplémentaire [10:35] (« not really good practice to add another one in »), puis préfère monter le sinus existant [10:55–11:00] (« might be a bit cleaner »).
  - Le sub se place « in this sort of 40 area » [11:20]. Bilan [11:35] : « brought the sub up a bit, the square down a bit ».
- **Effets dans Serum** [11:45–13:30] :
  - « split the low high and just put a distortion on the high end », parce que « the Serum distortions… don't really work very well on the low end ». [DÉDUCTION] Module Splitter L/H, distorsion dans le sous-rack HIGHS. Fréquence de coupure non dite.
  - « too many high frequencies on that one » [12:25], puis « modulating the cutoff on this » [12:35]. [DÉDUCTION] FREQ du filtre interne de la Distortion, modulée par le LFO.
  - « Modulate the mix on this one » [12:50]. « Going to the left is a bit nicer » [13:10].
  - « Let me take that distortion off… it does help quite a lot » [13:25–13:30] : comparaison avec et sans. On ne sait pas si la distorsion reste dans la version finale.
- **LFO ralenti** [14:25] : « let's slow that down a bit more ». Puis « a bit more subtle… I prefer a little bit more subtle » [15:05–15:10].
- **Effets facultatifs** [16:25–17:05] : réverbération, « a bit more filter shaping », chorus. Aucun réglage dit.
- **Traitement après Serum** [17:20–18:15] :
  - « Double that over », puis SpaceBlender (plug-in tiers, lien affilié dans la description) : « turn the mix right up », « bring the time down », « bring that color and texture all the way up ».
  - « Be careful with that layer that we don't add loads of extra low end on top of it all again ».

**Valeurs dites**
- Carrée une octave au-dessus du sinus de sub [2:25–2:30].
- LFO « really slow », puis plus lent, « dotted pattern » [3:05–3:15] ; ralenti encore [14:25].
- Profondeur du LFO plus forte sur le niveau de la carrée que sur celui du sinus [3:35–3:40].
- Filtre 1 → filtre 2 en série [4:10].
- Filtre 2 : Bandreject (Misc) « wide » [4:15–4:35], puis un passe-bande [5:20–5:45].
- Warp Bend + sur la carrée [8:15].
- Sub autour de « 40 » sur SPAN [11:20] ; unité non dite, Hz probable.
- SpaceBlender : mix au maximum, color et texture au maximum, time baissé [17:55–18:00].

**Valeurs non dites (à lire à l'écran)**
- Attack et release [1:25].
- Position de table de la carrée et octaves absolues [2:10–2:30].
- Type et cutoff du filtre 1 [2:40–2:55].
- Division, forme et profondeurs du LFO [3:05–3:45, 9:40, 13:35–14:30].
- Cutoff et largeur du Bandreject [4:30–4:50].
- Type de passe-bande [5:40–5:50].
- Sens et quantité de FM [6:40–7:00].
- Quantité de Bend + [8:00–8:15].
- Voix, detune et blend [8:25–8:30].
- Niveaux finaux [11:35].
- Fréquence de split, mode et drive de distorsion, cutoff et mix modulés [11:50–13:25].
- Réverbération, filtre et chorus [16:25–17:05].
- Time de SpaceBlender [17:55].
- Longs passages sans parole ([music]) : 5:25–6:20, 7:15–7:45, 13:40–14:15, 16:10–16:25, 16:40–16:55, 17:05–17:20. Les gestes y sont montrés, pas dits.

**Conseils de jeu, de mix, de resampling**
- La formule [15:15–15:40, 18:35–19:35] : un sinus pour le sub, plus une carrée « an octave higher that fills out basically the whole rest of the range ». Soigner le volume et le fine tuning, un peu d'unison, de la FM entre les deux « if it helps ».
- Ordre de filtrage de la carrée : d'abord un low-pass contre ses aigus « quite horrible », puis un second filtre pour « the main shaping », qui accentue certaines fréquences [19:05–19:30].
- Ne pas distordre le grave dans Serum : séparer graves et aigus, distordre les aigus seulement [11:50–12:05].
- Vérifier sur un analyseur (SPAN) que le sub tient la zone voulue [10:05–11:20]. Écouter avec la batterie [4:00].
- Le caractère haut s'ajoute par couches après Serum, sans rajouter de grave [17:20–18:15]. La vidéo assume que les aigus manquent [15:45].
- « You can make it faster, more snappy » [16:00] : la formule sert de point de départ.

**Incertitudes de transcription**
- « for a D » [10:25] : la note ré, ou « DnB » ?
- « 40 area » [11:20] : unité non dite.
- « dotted pattern » [3:15] : division pointée, ou forme en pointillés ?
- « The other way around » [6:50] : sens de FM final inconnu.
- « Add another one in » [10:35] : couche ajoutée inconnue, et son maintien incertain.
- « Going to the left » [13:10] : bouton tourné vers la gauche, ou modulation négative ?
- « it does help quite a lot » [13:30] : on ne sait pas si la distorsion est gardée.
- « Slurpy [snorts] derp » [0:00] : bruit d'introduction, sans contenu.

**Utilité pour une recette du skill :** la recette « sinus + carrée à +12, LP puis second filtre de mise en forme, FM d'octave, Bend +, LFO lent » s'applique aux familles F01 (sub) et F15 (rolling) du registre, et à la fiche 1 de `families.md`. La règle du projet impose de la scinder en **deux instruments** : le sinus seul et mono, et la carrée filtrée dans la basse médium. Il faut aussi rapporter la division du LFO au BPM house.

---

### F13-01 How to Make a Neuro Bass in Serum 2 — DNB Academy (Serum 2, mise en ligne 15/10/2025, 9:55)

- **Statut :** transcription automatique anglaise étudiée le 05/10/2026. Image et son non vus ni entendus.
- **Version :** Serum 2 d'après le titre, « the new serum wave tables » [0:25], « the new S2 wave tables » [1:05], « now on serum we've got this extended view » [4:40], et la phase distortion présentée comme « the old serum FM » [1:30]. Numéro de version non dit. Formateur : « John Doe aka Frags » [0:00], nom probablement mal reconnu.
- **Chapitres :** 0:00 Introduction to the sound · 0:13 Configuring oscillators · 2:20 Adding noise and shaping · 3:22 Filter and LFO modulation · 5:50 Applying Serum effects · 7:34 Final shaping and filtering · 9:21 Outro and preset promotion.

**Recette pas à pas**
- **Intention** [0:15] : une basse qui « relies a lot on movement and harmonic content ».
- **OSC A** [0:25–0:45] :
  - Nouvelles tables de Serum 2, dossier « analogs », table « square up and down » [nom de table incertain], « pretty much just like square waves » quand on parcourt les positions.
  - « Bring this down to three » [0:44]. [DÉDUCTION] OCT −3, par analogie avec « two, −2 » pour B.
  - RAND (phase aléatoire) baissé [0:54] : « keep this quite gentle… control the overall stereo of our sound ». Valeur non dite.
- **OSC B** [1:05–1:20] : nouvelles tables S2, dossier « digitals », « JF flute » [nom de table incertain], « almost looks like… subtly distorine [distorted sine] wave ». Réglages :
  - OCT −2 [1:19–1:20] ;
  - LEVEL baissé, « because we're going to FM this ».
- **Phase distortion** [1:25–1:35] : « we're going to PD on this one. We're going to face distort [phase distort] it… the old serum FM… keep it like halfway through precisely at like 50 ». L'oscillateur qui porte le warp n'est pas dit. [DÉDUCTION] Warp PD (B) sur OSC A à 50 %, B servant de modulateur à niveau bas.
- **Positions de table** [1:35–1:49] : « the wavetable position again also at top… important that we nail this part », puis « the wavetable position of this one as well… keep this one at **54** ». Une position est « at top » [sens incertain], l'autre à 54. On ne sait pas laquelle va à quel oscillateur.
- **Unison** [1:55–1:58] : « two voices », « bring down the D chin [detune] a little bit ». Oscillateur non dit. Detune non chiffré.
- **NOISE** [2:20–2:25] : « It's going to help us with distortion… set this to white noise stereo ». [DÉDUCTION] Bruit de couleur White, avec le bouton STEREO que fait apparaître ce type ; ce peut aussi être un fichier d'usine de ce nom.
- **Warp de distorsion** [2:30–2:43] : « go to the wave table here… choose the distortion warping mode… we don't really want to destroy the sound… soft clip ». Warp Distortion › **Soft Clip**. Oscillateur et quantité non dits ; [DÉDUCTION] probablement OSC A.
- **RAND** baissé « as well » [2:50], sur un autre oscillateur. [DÉDUCTION] B.
- **Passe-haut** [3:00–3:15] : « filter this out and highpass it… skip the messiness… on the lower end ». L'élément filtré n'est pas dit. [DÉDUCTION] Le FILTER du bruit de couleur (passe-haut) ou un warp Filter HPF ; à voir à l'écran.
- **FILTER 1** [3:25–3:45] : allumé, routé **sur A seulement** (« assign this one just to A… we don't really hear that wavetable [B]. It's just there for the FM purposes »). Premier type non nommé.
- **LFO 1** [3:50–4:45] :
  - Forme dessinée « to design really small gaps… and small changes within one bar » ; « something like this », sans formule.
  - Vitesse « slower like a bar » [4:11], donc 1 mesure.
  - Dessiné dans la « extended view of our envelope ». [DÉDUCTION] C'est le LFO Editor (grand canevas).
  - Mode RETRIG, confirmé plus tard : « make it re-trigger again and bar long just as we added before » [8:06].
- **Assignations de LFO 1** [4:55–5:40] :
  - « First one noise » [4:55]. [DÉDUCTION] Le niveau du NOISE.
  - Type du filtre 1 changé en **French LP** [5:10] (« better than the normal one because you can buff [BOEUF] this up »), plus « a little bit of drive » [5:17]. [DÉDUCTION] « buff » est le VAR **BOEUF** du French LP, une seconde résonance (cartographie § 6).
  - LFO 1 → cutoff, « not too abrupt of a movement » [5:25–5:35]. Profondeur non dite.
- **FX, dans l'ordre dit** [5:50–7:25] :
  1. « A little bit of dimension » [5:57] pour la largeur. [DÉDUCTION] Module Hyper/Dimension, partie DIMENSION.
  2. Distortion « with overdrive » [6:04–6:09] ; « we're going to stack two ». LFO 1 → **Drive** [6:14], « crunch this sine wave », puis « a more extreme spot » [6:25]. Overdrive est un mode ajouté par Serum 2 d'après la cartographie. « Stack two » peut désigner deux modules Distortion ou un réglage d'étages [incertain].
  3. Chorus « a little bit » [6:36], « a little bit more of a mess around some frequencies ».
  4. EQ [6:45–7:25] : « I create a notch », LFO 1 → **gain** et → **frequency**. Fréquence « like **300** » [7:16], unité non dite, Hz probable. « Let's make it bigger. Q. » On entend « that ramp going up and down ». [DÉDUCTION] Bande Peak en gain négatif, Q élevé.
- **FILTER 2** [7:40–8:30] :
  - Catégorie « miscellaneous », type « add base » [Add Bass] [7:49].
  - Un nouveau LFO, [DÉDUCTION] LFO 2, va sur le cutoff « one direction from left to right » [7:55–8:00]. [DÉDUCTION] Modulation unipolaire positive.
  - « Going a sort of A and B in this case » [8:00]. [DÉDUCTION] Filtre 2 routé sur A et B.
  - LFO 2 en RETRIG, 1 mesure [8:06–8:08].
  - Forme : « this like sort of like curve around here… super narrow… put it more down the center » [8:12–8:27]. [DÉDUCTION] Une bosse étroite vers le milieu de la mesure. Résultat : « another hit of a filter that comes in in the right spot » [8:30].
  - Drive et résonance du filtre 2 retouchés [8:42–8:46]. Valeurs non dites.
- **Fin de chaîne** [8:50–9:15] : retour à l'EQ, « choose a frequency that is more convenient to the sound we want ». Valeur non dite.

**Valeurs dites**
- OSC A : OCT « down to three », lu −3 [0:44].
- OSC B : OCT −2 [1:19–1:20].
- PD à « 50 » [1:35].
- Une position de table à **54** [1:49].
- Unison 2 voix [1:55].
- NOISE « white noise stereo » [2:24].
- Warp Distortion **Soft Clip** [2:43].
- Filtre 1 routé sur A seul [3:35] ; type **French LP** [5:10].
- LFO 1 : 1 mesure [4:04–4:11], RETRIG [8:06].
- Distortion **Overdrive**, « stack two » [6:04–6:09].
- EQ : creux vers **300** [7:16].
- Filtre 2 : **Add Bass** [7:49], LFO 2 en RETRIG sur 1 mesure [8:06–8:08].

**Valeurs non dites (à lire à l'écran)**
- RAND de A et de B [0:54, 2:50].
- Position « at top » [1:37].
- Niveau de B [1:20] et detune [1:58].
- Niveau et passe-haut du bruit [2:24–3:15].
- Quantité de Soft Clip [2:43].
- Cutoff, BOEUF et drive du filtre 1 [5:10–5:35].
- Formes et profondeurs de LFO 1 et LFO 2 [4:15–4:35, 8:12–8:27].
- Dimension [5:57], drive de l'Overdrive [6:14–6:25], chorus [6:36].
- Gain et Q du creux [7:00–7:25].
- Cutoff, drive et résonance du filtre 2 [8:40–8:46].
- Fréquence de l'EQ final [9:00–9:15].

**Conseils de jeu, de mix, de resampling**
- Un seul LFO dessiné sur une mesure, en RETRIG, conduit tout le mouvement : bruit, cutoff, drive de distorsion, gain et fréquence du creux d'EQ. Un second LFO d'une mesure pose un accent de filtre précis dans la mesure [3:50–8:30].
- L'oscillateur modulateur (B) reste presque inaudible : le filtre 1 ne traite que A [3:35–3:45].
- RAND gardé bas pour tenir l'image stéréo [0:54].
- Distorsion d'oscillateur douce (Soft Clip) : « we don't really want to destroy the sound » [2:35–2:43].
- Rien sur le jeu MIDI, l'enveloppe d'amplitude, le sub, le BPM ni le resampling.

**Incertitudes de transcription**
- « John Doe aka Frags » [0:00] : nom du formateur.
- « square up and down » [0:29] et « JF flute » [1:10] : noms de table incertains.
- « distorine » [1:13] = distorted sine.
- « face distort » [1:27] = phase distort.
- « D chin » [1:58] = detune.
- « buff » [5:15] = BOEUF.
- « add base » [7:49] = Add Bass.
- « at top » [1:37] : sens incertain.
- « stack two » [6:09] : deux modules, ou un réglage d'étages ?
- « going a sort of A and B » [8:00] : routage du filtre 2 ?
- « extended view of our envelope » [4:40] : la forme décrite est celle d'un LFO.
- « Heat. » [9:20] : bruit reconnu à tort.

**Utilité pour une recette du skill :** cette vidéo nourrit les familles F13 (neuro) et F08 (growl) du registre, et la fiche 8 de `families.md`, avec un patron transposable en Bass House sur la seule couche médium. A carrée à −3 oct, PD (B) à 50, Soft Clip, French LP avec BOEUF. Un LFO RETRIG d'une mesure va vers le bruit, le cutoff, le drive Overdrive et un creux d'EQ vers 300 Hz. Un second filtre Add Bass reçoit un LFO 2 en bosse étroite. Le sub reste séparé.

---

### F08-02 How to Make Dubstep GROWLS in SERUM 2 Tutorial — Konstricta (Serum 2, mise en ligne 19/03/2025, 11:27)

- **Statut :** transcription automatique anglaise étudiée le 05/10/2026. Image et son non vus ni entendus. 
- **Version :** Serum 2. La description dit « Serum 2 which just dropped » ; la vidéo dit « one of the first sounds I've made with Serum 2 » [0:10] et présente les trois oscillateurs, le nouvel éditeur de LFO Path et le double warp. [DÉDUCTION] Mise en ligne deux jours après le PDF officiel « What's New in Serum 2 » du 17/03/2025 : une toute première 2.0.x, dont les libellés ont pu changer depuis.
- **Chapitres :** 0:00 Intro · 0:19 Preview · 0:45 Serum · 7:24 Serum FX · 10:46 Finished Sound · 11:03 Outro.
- **Inspiration annoncée** [0:05] : Virtual Riot, Barely Alive, « Nima » [Nimda d'après la description].

**Recette pas à pas**
- **Nouveautés présentées** [0:30–0:40] : trois oscillateurs, « a new LFO path editor ». L'usage explicite d'un LFO de type Path n'est pas dit ensuite.
- **OSC A** [0:45–1:05] :
  - « Moving octave A down three » : OCT −3.
  - « We're going to be using FM from B so let's choose a clean wavetable for oscillator A ; a good one I've found is BAS plug [Bass Plug ? nom de table incertain] which works very well for gravels [growls] ».
  - RAND à **0** [1:00–1:05].
- **LFO 1** [1:05–1:25] : « create some slopes » (forme dessinée, rampes), rate « a bar ». Mode non dit.
- **Niveau de A** [1:30–1:40] : « set the level knob to 0% and then drag LFO 1 onto it ». [DÉDUCTION] Le niveau de A n'existe que par LFO 1 : les pentes dessinées deviennent le contour d'amplitude de A dans la mesure. Profondeur non dite.
- **WARP 1 de A** [1:40–1:55] : « in Serum 2 you're allowed to use two instead of one ». Mode **Bend −**.
- **LFO 2** [2:00–2:45] :
  - « Check out the new shapes » (formes d'usine), puis LFO 2 → « this Bend minus warp » [2:15–2:20].
  - Rate « a bar so it matches with our LFO one » [2:20].
  - « Maybe turn down the level slightly » [2:30–2:40] : quel « level » ? [incertain] Profondeur de modulation ou LEVEL de A.
  - « I'm liking the sound of this oval shape » [2:45] [« oval » incertain : nom de forme d'usine ?].
- **WARP 2 de A** [2:45–2:55] : « PD from B ». Selon lui, « the same as FM from B in Serum one ».
- **LFO 3** [3:00–3:15] : « something simple, I'll make a mini triangle », rate « a bar » ; LFO 3 → quantité de PD from B.
- **OSC B** [3:20–4:05] :
  - Allumé, « turn it down three » : OCT −3.
  - « A gritty wavetable with lots of texture ; the stock monster wavetables are really good options ». Laquelle des tables Monster : non dit.
  - RAND à **0** [3:45–3:50].
  - Position de table « near the middle » [3:50–3:55] ; LFO 3 → position de table.
- **Warp de B** [4:05–4:20] : « ASM minus » [Asym −] ; LFO 2 dessus.
- **OSC C** [4:45–5:55] :
  - Allumé, « for an extra layer ». « A vocal wavetable ; I know the wavetable softest gravel [Softest Growl ? nom incertain] is a good one » [4:55–5:00].
  - RAND retiré « so it stays consistent » [5:05].
  - LFO 1 → position de table [5:10–5:20].
  - Warp « ASM plus minus » [Asym +/−] [5:20–5:25] ; LFO 2 dessus [5:40].
  - « Move down the level knob and then drag LFO 1 onto it ; let's set this to about **80%** » [5:40–5:55]. Le 80 % vise-t-il la profondeur de LFO 1 ou le niveau ? [incertain]
- **NOISE** [5:55–6:35] :
  - « The stock noise sample works fine » ; « change this to **direct** so it bypasses our fix [FX] ».
  - « Drag elephant one [LFO 1] onto this mix and adjust the volume accordingly ». [DÉDUCTION] LFO 1 → niveau du NOISE.
  - D'après la cartographie, Direct contourne les filtres **et** les FX.
- **FILTER 1** [6:35–7:15] :
  - « High Notch 12 is one of the best for gravel [growl] sounds ». [DÉDUCTION] Type Multi « HN » 12 dB (High + Notch).
  - « Make sure A and C are highlighted », donc routage de A et C ; B n'est pas cité. [DÉDUCTION] B sort sans ce filtre.
  - LFO 1 → cutoff [6:50–6:55].
  - « Raise the drive, resonance and frequency knobs » [7:05]. [DÉDUCTION] « frequency » = VAR FREQ, cutoff du second SVF des types Multi.
  - « Let's modulate this as well » [7:10] : paramètre et source non dits.
- **FX, dans l'ordre dit** [7:25–10:55] :
  1. « A new filter… a new one in Serum 2 that behaves somewhat like a disperser ; let's adjust the knob to make it sound more big » [7:30–7:55]. [DÉDUCTION] Module Filter, type **Diffusor** (catégorie New), VAR = STAGES.
  2. « Some EQs » [7:55–8:15] : plusieurs modules, « simple notches », « raise the high end on the first one to give us more clarity ». Passage sans parole de 8:20 à 8:55, puis « see how drastically these can affect our growl » [9:00].
  3. Distortion **Hard Clip** [9:05–9:15], drive monté, LFO 1 → **mix**.
  4. « Some chorus and dimension to give the sound more width » [9:45].
  5. « Multiband OTT », « let's use three of them », puis « raise the gain till it sounds loud enough » [10:10–10:25]. [DÉDUCTION] Compressor en MODE Multiband. « Three of them » : trois instances ou trois bandes [incertain].
  6. EQ final [10:35–10:55] : « remove the low end and boost some of the highs ».
- **Fin** [10:55] : « pretty close to being finished ». L'enveloppe d'amplitude, le MIDI et le BPM ne sont jamais mentionnés.

**Valeurs dites**
- OCT A −3 [0:45–0:50] et OCT B −3 [3:20–3:25].
- RAND à 0 sur A [1:00], B [3:45] et C [5:05].
- LFO 1, LFO 2 et LFO 3 à « a bar » [1:25, 2:20, 3:10].
- LEVEL de A à **0 %** + LFO 1 [1:30].
- A : WARP 1 **Bend −** [1:50], WARP 2 **PD from B** [2:50].
- B : position de table « near the middle » [3:50] ; warp **Asym −** [4:15].
- C : table vocale [4:55] ; warp **Asym +/−** [5:25] ; « about 80 % » [5:55].
- NOISE routé **Direct** [6:20].
- Filtre **High Notch 12** sur A et C [6:45–6:50].
- **Hard Clip** [9:10] ; LFO 1 → mix de la distorsion [9:15].
- OTT multibande, « three of them » [10:20].
- EQ final : graves retirés, aigus montés [10:35].

**Valeurs non dites (à lire à l'écran)**
- Noms exacts des tables A, B et C [0:55, 3:35, 5:00].
- Formes de LFO 1, 2 et 3 (« slopes », « oval », « mini triangle ») et leur mode [1:05–3:15].
- Toutes les profondeurs de modulation et quantités de warp [1:30–5:55].
- Positions de table [3:50, 5:10].
- Niveau du NOISE [6:25–6:35].
- Cutoff, résonance, drive et FREQ du filtre [6:45–7:15].
- Réglage du Diffusor [7:40–7:55].
- Fréquences, gains et Q des EQ [7:55–9:00].
- Drive du Hard Clip [9:10].
- Chorus et Dimension [9:45].
- Réglages et gain de l'OTT [10:15–10:25].
- Fréquences de l'EQ final [10:35–10:55].

**Conseils de jeu, de mix, de resampling**
- Tous les LFO sur une mesure, « so it matches » : le mouvement se répète à l'identique chaque mesure [2:20].
- RAND à 0 sur chaque oscillateur « so it stays consistent » [5:05].
- Le bruit passe en Direct pour échapper aux filtres et aux FX, et son niveau suit LFO 1 [6:20–6:35].
- Filtre High Notch 12 pour les growls [6:45].
- L'OTT rend le son « loud enough », puis l'EQ final retire le grave [10:20–10:55]. [DÉDUCTION] Couche médium seule, à poser sur un sub séparé.
- « Getting good sounds is all about trial and error » [11:10].

**Incertitudes de transcription**
- « dubic rails » [0:05] = dubstep growls.
- « fat girls » [0:15], « gravel(s) » [1:00, 6:45, 9:00] et « grow » [10:55] = growl(s).
- « alfo », « elepha », « alpha », « alpo », « ELO », « Alo », « alha », « elephant » = LFO.
- « BAS plug » [0:55] : nom de table.
- « softest gravel » [5:00] : nom de table.
- « oval shape » [2:45].
- « ASM » [4:15, 5:25] = Asym.
- « fix » [6:20] = FX.
- « Co » [9:45] = chorus.
- « Nima » [0:10] = Nimda.
- « level » [2:30] et « about 80 % » [5:50] : cible incertaine.
- « three of them » [10:20].
- « High Notch 12 » : libellé à confirmer dans le menu des filtres Serum 2.

**Utilité pour une recette du skill :** cette vidéo donne un patron complet pour la famille F08 (growl) du registre et la fiche 8 de `families.md` : trois oscillateurs à −3 oct, RAND 0, et trois LFO d'une mesure sur le niveau, les positions de table et les doubles warps (Bend −, PD from B, Asym). S'y ajoutent un filtre HN 12 sur A et C, du bruit en Direct, Diffusor, Hard Clip, OTT, puis un EQ qui retire le grave. En Bass House, on le transpose tel quel sur la couche médium, sub à part. Il faut fixer le mode du LFO en RETRIG, que la vidéo ne précise pas, pour que le patch soit reproductible.
