# Études des tutoriels vidéo (transcriptions et captures)

Étude du 05/10/2026, en session cloud, par un sous-agent de Claude Code. Sources : sous-titres automatiques anglais de YouTube récupérés avec `yt-dlp` (sans la vidéo), nettoyés en blocs minutés de 20 s ; transcriptions non conservées dans le dépôt. Les minutages viennent des horodatages des sous-titres, à ±5 s près. Identifiants : registre `tutoriels-a-consulter.md`. Après ces trois vidéos, YouTube a bloqué la session (vérification anti-robot). Les 21 autres vidéos ★, plus deux vidéos intégrées à des pages d'agrégateur, ont été étudiées le même jour dans Claude in Chrome sur le Mac : seconde partie de ce fichier, avec ses propres conventions.

Conventions de cette première partie :
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

---

## Vidéos étudiées dans Claude in Chrome sur le Mac (05/10/2026)

Étude faite par Claude in Chrome dans le Chrome de l'utilisateur sur le Mac, **son coupé** : transcription YouTube (automatique sauf mention), description, et captures d'écran aux minutages utiles. Fichier remis par l'utilisateur le même jour et intégré tel quel, titres de section ramenés au niveau de ce fichier.

- **23 vidéos** : les 21 vidéos YouTube ★ restantes, plus F05-02 et F08-03 (vidéos YouTube intégrées aux pages d'agrégateur : `UxXCeAcmO7g` et `RmFDYc_8-9s`, dont les résumés écrits sont dans `etudes-pages-house.md` et `etudes-pages-dubstep-dnb.md`).
- **Minutages** : ceux de la transcription ; « écran » = valeur lue sur une capture ; « dit » = valeur prononcée. Quand les deux diffèrent, les deux sont notés : ne retenir ni l'un ni l'autre sans vérification.
- **Lecture des captures** : image de YouTube réduite ; les petits chiffres (temps d'enveloppe, compresseur) sont à confirmer avant d'en faire un réglage. Les noms de tables, de warps et de filtres lus à l'écran sont à retrouver dans le navigateur de Serum 2 (`sound-designer-serum/references/serum2-cartographie.md` ne les contient pas tous).
- **Sans transcription** : F03-03 et F12-01 (étude sur captures seules).
- **Jamais entendu** : aucun effet sonore n'est confirmé (règle 4 d'`AGENTS.md`). Les mots « aigu bizarre », « croquant », « punch » rapportent ce que dit le formateur.
- **Serum 1** : F02-03, F03-03, F06-02, F09-01, F11-01, F11-02, F12-01, F12-02, F14-02 et F15-02 montrent Serum 1 ; traduire les gestes dans Serum 2 et vérifier les noms de contrôle.
- **Corrections reportées dans le registre** : F05-03 est de Zen World / EvoSounds (et non Sam Smyers), en Serum 2 ; F05-02 est aussi de Zen World / EvoSounds ; F02-01 et F07-02 sont de DNB Academy ; F14-02 de MilleniumBE ; F12-01 est un lead d'après sa description.

### F02-01 Try this Heavy DNB Reese Bass in Serum 2 — DNB Academy (Frags), 8:30, 17/10/2025, Serum 2
Chapitres : 0:00 intro, 0:30 oscillateurs, 2:08 filtre et modulation, 3:23 LFO et enveloppe, 4:29 distorsion et effets, 5:29 traitement final.
- 0:46 deux scies (osc A et B), −3 octaves chacune, fine −38 et +38 (cents).
- 1:08 osc C : table Analog « DM - Oscar » (transcrit « D amp Oscar »), +7 demi-tons ; aigu bizarre assumé, corrigé par le filtrage.
- 1:35 sub activé, −3 octaves, routé dans le filtre 1 « pour un grave plus concis ».
- 1:53 noise activé (un des nouveaux bruits blancs de Serum 2, non nommé).
- 2:08 tout routé dans le filtre ; type Misc > Combs ; cutoff « vers 30-31 », « temp » (probablement résonance ou mix) 50 %.
- 2:37 mono + legato.
- 2:50 phase distortion (warp PD) « pour fondre les couches », vers 74 ; revue à 7:01 : « 73 is the key ».
- 3:24 LFO lent (1 ou 2 mesures), forme montée-descente, sur la coupure, quantité ~45 %.
- 4:04 baisse du niveau de l'osc C (« trop fort »).
- 4:29 FX : Overdrive (Distortion) puis une deuxième ; enveloppe évoquée vers 5:20 (non claire).
- 5:31 chorus ; 5:46 filtre FX en coupe-bas « pour contrôler les aigus » (dit « low cut », contradiction possible) ; 6:07 compresseur ; 6:13 multibande ; 6:27 EQ pour nettoyer les médiums.
- 7:30 réglage final : réintroduire la table Oscar, 2 voix d'unison.
Captures (1:45, 3:53, 6:35, 6:55) :
- Osc A et B « Default Shapes » (scies), OCT −3 (écran : −2 affiché sur A et −3 sur B à 1:45 ; à confirmer), fine −38 / −28 lus (écran : « FIN −38 » et « −28 » ; la voix dit −38 / +38) ; osc C « DM - OSCAR », OCT 0, SEM +7. Sub à −3 octaves (écran : OCT −3).
- Noise « HP12 …sreo) » (table de noise filtrée), start 3.
- Filtre 1 « Combs » ; les cases A, B, C, N, S cochées.
- Warp de A « PD (B) » : écran 6:55 « A Warp : 64 % » (la voix dit 74 puis 73 : valeur affichée différente, peut-être une autre lecture du même bouton).
- LFO 1 : Retrig, forme montée rapide puis descente lente, 2 mesures.
- Voicing : mono + legato (« 5 / 5 »), Always activé.
- FX (6:35) : Distortion, Chorus, Filter « MG Low 6 », Compressor Multiband (seuil −18,1 dB, ratio 4:1, attaque 90,1, release 90,1, gain 4,2, bandes 128 / 2500 Hz), Equalizer (bande basse 210 Hz, Q 80, 0 dB ; bande haute en creux à 484 Hz, Q 80, −15,6 dB).
Écart à noter : la voix parle de « low cut » pour le filtre FX ; l'écran montre un MG Low 6 (passe-bas).


### F02-03 Comment faire une Reese Bass sur Xfer Serum — Strob Studio (Igor Chevalier), 12:48, 29/07/2020 → Serum 1
Transcription automatique française très bruitée (« risques baisse » = Reese bass, « des thunes » = désaccorder).
- 1:36 principe : battement entre deux formes identiques, l'une légèrement désaccordée (annulations de phase dans le temps).
- 2:05 deux scies (osc A et B) ; 2:13 désaccord de l'une.
- 2:28 mono + un peu de portamento.
- 2:36 plus on désaccorde, plus le battement est rapide, mais on perd la note : chercher le milieu ; mieux vaut désaccorder les deux en sens opposé : au lieu de 40 sur un seul, « 22 de chaque côté » (unité non dite, fine en cents probable).
- 3:33 toute table riche en harmoniques marche (exemple pris dans une table spectrale), la scie est l'idéale.
- 4:17 la fondamentale bat aussi → ajouter le sub (osc sub) en triangle, baisser un peu A et B.
- 5:56 astuce pour un sub parfaitement constant : monter A et B d'une octave et laisser le sub une octave plus bas (sépare les bandes) ; mais la Reese est moins grave ; alternative : traitement post-design par bandes. Il revient ensuite au sub à la même octave.
- 7:15 couche classique façon phaser : tout router dans le filtre 1, type phaser « positif » (transcrit « abbé et seube », probablement un Phaser +), un peu de drive ; sub routé ou non dans le filtre (« direct ») pour garder un grave stable.
- 8:05 LFO très lent sur le filtre.
- 8:40 battement trop lent dans l'aigu : moduler le désaccord par la source Note (« note à signer ») pour que les notes aiguës battent plus vite.
- 9:11 FX : distorsion ; il préfère la distorsion multibande hors du sub ; OTT pour un son plus moderne ; distorsion avec mix vers 50 % pour garder un sub propre ; filtre FX possible.
- 11:25 sa méthode : distorsion après le design, en plug-in externe multibande (Saturn, Trash 2).
Captures (3:21, 8:21, 10:45) :
- Osc A et B : table « Default » (scie), OCT 0, fine −21 / +21 (3:21) puis −20 / +20 (8:21) : le « 22 de chaque côté » se lit 20-21 à l'écran.
- Sub en triangle (écran 8:21), OCT 0, Direct Out activé (le sub ne passe pas dans le filtre).
- Filtre « Phs 36+ » (8:21) sur A et B (et une case S visible), donc le « phaser positif » est le Phs 36+ ; ENV non utilisé ; LFO 1 triangle, 4 mesures, sur la coupure.
- ENV 1 : attaque 0,5 ms, hold 0, decay 1,00 s, sustain 0,0 dB, release 15 ms ; mono + legato ; portamento non lu.
- 10:45 : Distortion « Tube », filtre OFF ; source Note visible dans la matrice (désaccord suivant la note).


### F03-03 How to make a future house bass like Mike Williams & Mesto — Sonance Sounds, 1:51
Aucune transcription (vidéo sans voix, FL Studio à 128 BPM). Description : preset Serum gratuit sur theartistunion.com. Étude sur 4 captures (0:15, 0:41, 1:06, 1:31) ; Serum 1 (interface).
- Osc A : « SawRoundedToSquare » (en position carrée), position modulée (bulle « A WTPos 17 »), OCT −1 (écran 0:41), unison 1. Pas d'osc B, ni sub, ni noise.
- Filtre « MG Low 12 », ENV 2 sur la coupure (bulle « Env 2 → Fil Cutoff 42 »).
- ENV 1 : attaque 0,5 ms, hold 0, decay 1,00 s, sustain 100 %, release 15 ms. ENV 2 : attaque 0,5 ms, hold 0, decay 966 ms, sustain 38,24 %, release 308 ms.
- FX : Distortion « Tube » avec filtre PRE passe-bas (≈ 2893 Hz, Q 0,1 ; d'abord 330 Hz par défaut) ; Compressor (mode simple) ; EQ avec bande basse en « Peak ».
- Voicing : mono, legato (« 0 / 16 » voix).
Patch court ; les valeurs de drive, de seuil et de gains d'EQ ne sont pas lisibles.


### F05-01 Recreating Chris Lake's TOXIC Bass in Serum 2 — Zen World / EvoSounds, 8:14, 26/03/2025, Serum 2
- 0:25 notes dites : D#, E, F#, E, F#, E, D#, C# (transcription approximative), jeu sur les demi-tons du mode mineur.
- 1:10 osc sub : sample « analog bass sub » importé (version bêta ; sinon une table sinus) ; dans le mixeur de Serum 2, sortie directe (Direct Out) pour contourner les effets.
- 1:58 osc saw : tables Serum 2 « Model D », position sur la scie ; warp distorsion « pour l'épaissir un peu ».
- 2:40 filtre 1 passe-haut sur la scie (seule) : retirer le grave pour ne pas interférer avec le sub.
- 2:56 phase random à 0 (retrig) sur les deux oscillateurs.
- 3:07 option : warp Tube sur le sub pour l'épaissir.
- 3:33 ENV 1 (amplitude) : sustain baissé, le decay façonne la basse.
- 3:57 FX 1 : filtre « MG Ladder » (émulation Moog) ; cutoff 175 (Hz) ; ENV 2 sur la coupure, sustain bas, decay = punch ; résonance « 16 … disons 12 % » ; sustain remonté pour tenir la note.
- 5:19 EQ : creux (fréquence non dite) qui « fait briller » la basse.
- 5:59 compresseur, preset « 1176 Glue », attaque basse, release haute : remonte la scie face au sub (contrôle à l'analyseur Span).
- 6:31 EQ +2,2 dB à 343 Hz.
- 6:45 filtre final retirant des aigus « numériques ».
- 7:08 macro sur coupure + résonance du filtre pour le geste de filtre façon Chris Lake.
Captures (2:55, 5:05, 6:35), preset « BA - Toxic » :
- Osc A « AT Model D » (table Serum 2), phase 52°, random 0 ; osc B « Basic Shapes » en sinus avec warp « Tube » (c'est le sub sinus de la variante) ; osc C allumé avec un warp « Asym » (lecture incertaine) ; noise « Geiger », stéréo 0.
- Filtre 2 « High 24 » (le passe-haut de la scie).
- ENV 1 : attaque 1,0 ms, hold 0, decay 247 ms (237 ms à 6:35), sustain −2,6 dB (−6,1 dB à 6:35), release 420 ms ; ENV 2 : decay 289 ms, sustain −inf ; mono + legato, Always.
- Macros : The Wubs, Control Cutoff, Wubs, Noise Top Layer, No Low End, 3rd Layer.
- FX : Filter « MG Ladder » (« FX Fil Reso 12 % ») ; Equalizer (185 Hz, Q 73, −6,2 dB ; bande haute ~118, Q 55, −6,2 : lecture incertaine) ; Compressor en mode Single : seuil −26,4 dB, ratio 4:1, attaque 0,6, release 260, gain 9,2 ; Equalizer (343 Hz, Q 41, +2,2 dB ; ~2040 Hz, Q 67, −6,2 dB) ; Filter « MG Low 6 ».
- Le preset « 1176 Glue » est un réglage du compresseur de Serum 2 (mode Single), pas un plug-in externe.


### F05-02 This Slept-On Effect Makes Tech House Bass Sound Filthy (page agrégateur : « Gritty Tech House Bass Design in Serum 2 ») — Zen World / EvoSounds, 11:09, 14/09/2026, Serum 2
Vidéo YouTube intégrée à la page : UxXCeAcmO7g. Transcription + 2 captures (6:13, 9:21). Référence : « Bad B » de Julian Jordan (pas de sub, rien sous 60 Hz).
- 1:12 idée : Convolve avec une IR de baffle de guitare électrique, pour le « grain », au prix du grave (tout ce qui est sous ~60 Hz disparaît).
- 2:29 Distortion avec pré-filtre passe-haut (retire le grave accumulé par le baffle) ; puis OTT : Compressor Multiband, le réglage « below » fait l'effet OTT ; « l'EQ fait souvent mieux ».
- 4:01 filtre FX Sample & Hold : la coupure baisse la fréquence d'échantillonnage, la résonance baisse la résolution (son « Atari »).
- 5:03 construction : scie à −2 octaves (grave entre 30 et 60 Hz) ; filtre « Low 24 » qui retire le haut ; ENV 2 un peu de punch sur la coupure ; retrig (phase identique à chaque note).
- 5:54 Convolve : catégorie Factory > Cab, IR « Cab 2 » (écran : « ELECTRIC GUITAR CAB 2 »), niveau baissé (écran : « Conv Level −8,6 dB », lecture approximative), taille réduite.
- 6:52 Distortion (écran : mode « Diode » / « APPR », lecture incertaine), pré-filtre passe-haut ; OTT par Multiband « below » (écran 9:21 : seuil −18,1 dB, ratio 4:1, attaque 90,1, release 90,1, gain 9,5) ; plus on monte, plus c'est « EDM ».
- 8:10 « distorsion dynamique » : enveloppe sur le drive pour un pic à l'attaque.
- 8:38 filtre FX « Sample & Hold » (écran : « Samphold ») avec résonance.
- 9:33 sub optionnel : osc sub en Direct Out, −2 octaves, remonté à l'EQ Eight d'Ableton.
- 9:55 ENV 1 : sustain bas, decay tiré : l'attaque sature plus que le corps → punch.
Ordre FX à l'écran (9:21) : Convolve, Distortion, Compressor, Filter.


### F05-03 I Cracked That Mau P Bass — Just A Little Bit More — Zen World / EvoSounds (et non Sam Smyers), 7:43, 11/09/2026, Serum 2 (hashtag #Serum2)
- 0:39 une scie quelconque ; pas de retrig sauf besoin.
- 0:56 logique acid : filtre « MG Low 18 », coupure basse, un peu de résonance et de drive / FAT (le FAT compense la perte de grave due à la résonance).
- 1:20 ENV 2 très punchy sur la coupure, mouvement faible (sinon trop « acid »).
- 1:43 scie à −2 octaves (basse jouée entre C2 et C3).
- 1:58 principe : couper les aigus, accentuer une zone (résonance), puis la distorsion recrée les harmoniques supérieures.
- 2:28 distorsion = effet sensible au niveau : sans dynamique « ça fait un pâté » → enveloppe d'amplitude (« ENV 1 ou ENV 3 » transcrit GLP1/GLP3) avec sustain bas, decay ajusté, pour que l'attaque sature davantage.
- 3:02 pente du filtre : 12 retenu, 6 aussi valable (plus de pente ouverte = plus d'harmoniques après distorsion).
- 3:32 compression multibande (OTT) pour tenir cette basse acide très dynamique ; remonter un peu le grave.
- 4:23 sidechain ajouté (méthode non précisée).
- 4:33 EQ pour accentuer certaines zones (fréquences non dites) ; niveau général monté ; plus d'ENV sur le filtre ; compression poussée « sans castrer ».
- 5:43 mono + legato + portamento avec courbe ; puis legato désactivé (portamento seul) pour garder le punch des enveloppes à chaque note.
- 6:36 résumé : scie, filtre résonant qui oriente la distorsion, distorsion dosée avec soin, OTT/multibande, EQ final d'épaisseur.
Captures (1:50, 5:00, 6:35) :
- Osc A « Basic Shapes » en scie, OCT −2, random 100 (pas de retrig).
- Filtre 1 « MG Low 18 » ; ENV 2 punchy (attaque 0,5 ms, decay ~301 ms).
- ENV 1 (5:00) : decay ~143 ms, sustain −8,3 dB (approximatif), release 15 ms.
- FX (6:35) : Distortion « Tube » ; Compressor Multiband (seuil −20,9 dB, ratio 5:1, attaque 95,6, release 9,0 environ, bandes 120 Hz et 2500 Hz) ; Equalizer (142 Hz, Q 53, +5,5 dB ; 818 Hz, Q 46, +0,7 dB).
- Sidechain : Kickstart 2 (Nicky Romero) sur la piste, hors Serum.
- Voicing : mono, legato désactivé à la fin.
Les valeurs du compresseur et des enveloppes sont petites à l'écran : à confirmer.


### F06-01 Serum 2 Bass Tutorial | Easy "Jump Up" Bass! — Antidote Audio, 5:40, 16/11/2025, Serum 2 (preset gratuit en lien Dropbox ; extrait du pack « Radium »)
Transcription + 5 captures (fenêtre Chrome petite : petits chiffres lus avec réserve).
- 0:38 init ; sub −2 octaves.
- 0:43 osc A : table Serum 2 Digital « Squibble », −2 octaves ; position de table choisie à l'oreille ; random de phase à 0, phase ~101 (écran 1:41 : 180° affiché sur A, valeur dite 101 non confirmée).
- 1:06 osc B : « Default Shapes » (scie), sert de source FM, niveau à 0.
- 1:11 osc C : table Serum 1 Digital « Harmonic Subtle », random 0 ; écran 3:17 : position 256 (tout en haut).
- 1:23 LFO 1 : rampe montée-descente, 1/8, sur le niveau de A (vers le bas) et de C ; écran 1:41 : LFO 1 en mode Retrig, forme montée-descente.
- 2:04 noise « White » (couleur nouvelle de Serum 2) ; LFO 2 séparé, 1/8, sur le noise ; stéréo 100 (écran 2:47).
- 2:36 mono.
- 2:41 FM depuis B sur A : 21 % dit, écran 2:47 « A Warp 2 : 22 % ».
- 2:54 filtre 1 type « Flg L6+ » (flanger) ; écran 3:17 : coupure 1276 Hz pendant le réglage ; tous les boutons « vers midi » sauf le drive ; résonance ~59 % ; key tracking essayé puis retiré (4:51), coupure finale dite 893 Hz ; mix un peu baissé.
- 3:43 FX (écran 4:06) : Distortion « Tube », filtre de distorsion OFF (Freq 425, Q 1,0 affichés) ; Compressor en mode Multiband : seuil −18,1 dB, ratio 4:1, attaque 90,1, release ~90,1, gain 10,7 dB, bandes 120 Hz et 2500 Hz ; il remonte les aigus puis revient en arrière ; un peu plus de drive ensuite.
- 4:45 filtrer le white noise pour qu'il soit moins grave (filtre et valeur non précis).


### F06-02 Ableton Tutorial: Create JAUZ/Donk Bass In Serum — Slynk, 13:04, 12/05/2017 → Serum 1
Transcription + 3 captures (2:26, 3:17, 4:15).
- 0:51 principe : FM. Sinus sur A et sur B (« Basic Shapes »), warp de B = « FM (from A) » ; niveau de A à 0.
- 1:28 B à −2 octaves, A à +1 octave (écran 2:26 : OCT +1 sur A, −2 sur B).
- 1:49 ENV 1 (déjà sur l'amplitude) assigné à la quantité FM, pas trop haut ; écran 2:26 : ENV 1 attaque ~71 ms, hold 0, decay ~319 ms, sustain −inf dB, release ~424 ms (lecture à confirmer).
- 2:35 filtre sur A, B, noise ; type MG Low 24 (écran : MG Low 12 puis Low 24) ; même ENV 1 sur la coupure ; résonance à 0 (« pas terrible si on la monte ») ; un peu de drive ; FAT sans effet utile.
- 3:35 sub −2 octaves, Direct Out ; EQ FX en coupe-bas vers 170-180 Hz sur A/B pour laisser la place au sub.
- 4:53 largeur : unison 2 sur A et B, detune à l'oreille.
- 5:33 FX : Distortion en mode filtre passe-haut ~200 Hz (n'abîme que médiums/aigus), drive à l'oreille, forme « CH » (probablement Soft Clip / tube : nom non lu), mix un peu baissé.
- 6:02 Reverb : high cut ouvert, low cut monté (pas de réverb dans le grave), taille et decay à l'oreille.
- 6:31 Compressor en mode multibande ; bande haute descendue ; gain monté ; attaque et release basses donnent un effet « buzzy », il revient à plus propre.
- 7:21 variantes : table « Saw Rounded to Square » avec position de table modulée par enveloppe ; autres tables ; attaque de l'enveloppe à 0 et octaves plus basses pour un son plus « donk » ; niveau de A remis en partie.
- 10:00 autres filtres essayés : Comb (son préféré, surtout avec attaque), Reverb (filtre), Sample & Hold négatif, formant ; noise court en transitoire d'attaque.


### F07-02 How to Make a Wobble with the Sampler in Serum 2 — DNB Academy (Scream Arts), 11:56, 19/09/2025, Serum 2
Transcription peu chiffrée + 3 captures (6:01, 6:40, 10:40). Tempo du projet : 174. Malgré le titre, le « wobble » n'est pas expliqué en détail : c'est une basse DnB faite uniquement avec l'oscillateur Sample et ses samples d'usine.
- 1:47 les trois oscillateurs en mode Sample, samples internes de Serum 2. Écran : osc A « True Kora » (en one-shot, sert d'attaque), osc B « Brass Wall Low » (couche haute), osc C « Upright Short » (contrebasse, couche grave).
- 4:00 filtre 1 passe-haut (écran : « High 18 », lecture incertaine) sur A et B seulement : C reste propre en grave.
- 4:42 distorsion tout de suite (« essentielle pour les sons neuro/agressifs »).
- 5:05 boucler le sample de C sur une zone stable de la forme d'onde, crossfade pour éviter les clics (écran 6:01 : C en mode boucle).
- 6:26 mouvement de filtre sur A et B : écran 6:40 : LFO 1 en Retrig, forme décroissante, 1/4.
- 6:48 compression multibande, plus d'aigus ; filtre FX final pour le mouvement.
- 8:12 réverb à convolution (essai d'IR : ajoute trop de grave), Hyper/Dimension, réverb classique, encore de la distorsion.
- 9:45 noise (aussi un sampler) puis FM du noise « pour des aigus craquants » (écran 10:40 : noise « White », warp de C « FM (Noise) » visible).
- 10:50 en pratique il mettrait un sinus en sub sur A ; ici démonstration samples seulement : A attaque, B couche haute, C sub.


### F08-01 Growl tutorials Suck, this one DON'T (Virtual Riot style growls, Serum 2 only) — Holo Rival, 17:01, 13/02/2026, Serum 2
Transcription + 4 captures (2:51, 4:40, 7:51, 11:31). Tempo du projet : 150. Petite chaîne (304 abonnés) ; preset gratuit et pack payant via sa page.
- 0:44 méthode « FM de sinus en chaîne » (attribuée à la pratique FM8) : A, B, C en sinus « Basic Shapes » ; B et C muets ; chaîne FM C → B → A (warp FM sur A depuis B, sur B depuis C). Écran 2:51 : warps FM visibles sur A et B.
- 1:28 jouer très grave (patchs FM à 3 étages sonnent différemment dans l'aigu, constat personnel).
- 2:28 quantités FM sur une macro (macro 1).
- 2:40 filtre 1 passe-bande (écran : « Band 24 »), zone ~100-600 Hz, un peu de résonance.
- 3:25 FX : Distortion légère, puis EQ calé sur le pic du passe-bande, aigus fortement limités.
- 4:16 « secret » : filtre FX de type diffuseur/dispersion (Serum 2), effet proche du vocoder ; dupliqué (2 filtres).
- 5:01 trois compresseurs en Multiband (preset d'usine « Multiband OTT »), gain poussé ~12 dB ; écran 7:51 : seuil ~−18,1 dB, ratio 4:1, attaque 90,1, release ~99,1, gain 13,2 / 12,5, bandes 88 Hz et 2500 Hz.
- 5:52 retouche de la FM sur A : « du crunch, pas du désordre » ; l'EQ change beaucoup le croquant.
- 7:17 Phaser figé : rate au minimum, depth 0, seuls fréquence et feedback ; 4 pôles recommandés (écran 7:51 : Phs Freq 205 Hz). Deuxième phaser réglé pareil.
- 8:51 OTT supplémentaire ; puis EQ avant les compresseurs avec une encoche aiguë ; nombre d'étages du diffuseur réduit.
- 11:00 Chorus pour la largeur, mode passe-haut (élargit seulement le haut), délais coupés, rate 8 Hz, depth et feedback bas (écran 11:31 : chorus en tête des derniers effets).
- 11:40 LFO sur les macros ; macro 5 → Global Main Tuning dans la matrice, bipolaire, ~13 %, piloté par LFO Tool (plug-in externe) à 1 mesure : variation de hauteur du growl.
- 13:00 EQ : plus de médiums et de grave ; troisième phaser, feedback bas ; compresseur simple (non multibande) à la fin ; retouches (bend de position, gain de distorsion).
Ordre FX vu à l'écran (4:40, 11:31) : Distortion, EQ, Filter, Filter, Compressor ×3, Phaser, Phaser, EQ, EQ, Chorus, Compressor ×3.


### F08-03 How to Make a Heavy Growl Bass in Serum 2 for Drum & Bass (page agrégateur : « Growl Bass Sound Design in Serum 2 for Drum and Bass ») — DNB Academy, 2:02 (format vertical, sans voix-off pédagogique détaillée), 12/09/2026, Serum 2
Vidéo YouTube intégrée : RmFDYc_8-9s. Transcription + 4 captures (0:15, 0:31, 1:24, 1:56).
- 0:02 osc A : scie « Default Shapes », −3 octaves (écran : OCT −3) ; osc B : « Basic Shapes » (Analog), position 3 (triangle à l'écran), unison 3 ; warp de A « PD (B) » (phase distortion depuis B).
- 0:16 warp de B : Distortion « Rectify » au maximum.
- 0:20 un peu de noise (écran : « White », stéréo 67).
- 0:24 filtre 1 « Diffuser » (écran) : coupure 118, étages « 72-75 » (dit « 7275 »).
- 0:32 LFO (forme non décrite) sur de nombreux paramètres : la quantité PD (~35), l'osc scie, le noise…
- 0:50 FX : Distortion Overdrive agressive ; Chorus en mode passe-haut pour la largeur ; filtre FX « Combs » coupure presque au maximum ; EQ de nettoyage (écran 1:24 : creux à 437 Hz, Q 60, −17,6 dB) et contrôle des aigus.
- 1:15 filtre FX « Phs 36+ » (phaser), coupure ~57, LFO en bipolaire.
- 1:28 Splitter : Convolve sur la bande haute, IR courte (écran : « L90 PLATE - DRUM - TIGHT PLATE »).
- 1:39 Compressor Multiband, bande par bande, gain ~7 (écran : seuil −18,1 dB, ratio 4:1, attaque 90,1, release 90,1, gain 7,2, X-Low 128).
- 1:47 filtre final passe-bas (écran : « MG Low 6 ») avec LFO 1 sur la coupure ; Distortion Soft Clip en fin de chaîne.

### F09-01 HOW TO VR "YOI" BASS (SERUM TUTORIAL) — DraGonis, 1:47, 05/08/2020 → Serum 1 (FL Studio)
« Pas un tutoriel, un speedrun » (description). Transcription courte + 4 captures (0:14, 0:34, 0:47, 1:07).
- 0:03 osc A : table « Monster 5 [SL] » (écran).
- 0:07 LFO 1 en forme de bosse (montée arrondie puis descente) ; LFO 1 sur le niveau de A et la position de table.
- 0:14 warp de A : « FM (from B) » (écran), quantité modulée par LFO 1.
- 0:18 osc B : sinus « Analog_BD_Sin » (écran), niveau baissé.
- 0:21 filtre « HP 12 » (écran) sur A seul, résonance haute ; cutoff et FREQ (le second bouton du filtre) modulés par LFO 1 en sens opposés (« l'un vers l'autre »).
- 0:39 warp de B « Bend − » ; LFO 2 en forme dessinée, rate 1/2 ; LFO 2 sur le Bend − (écran 0:47 : B Warp modulé par LFO 2).
- 0:48 FX Hyper/Dimension, mixes modulés, taille baissée.
- 1:05 EQ modulé par LFO 1 (écran 1:07 : fréquence de la bande basse, en coupe-bas). Écran 1:07 aussi : Distortion « Tube » avec filtre LP à 330 Hz, Q 1,9 ; compresseur en mode Multiband actif.
- 1:29 rate du LFO piloté par une macro.


### F10-01 Make Easy RIDDIM BASSES in SERUM 2 Tutorial — Konstricta, 8:44, 26/03/2025, Serum 2
Riddim/trench façon « Square 4 » (Infekt, Samplifire, MVRDA) sans la table d'origine. Transcription + 3 captures (2:05, 3:21, 6:35).
- 1:02 osc A : table Serum 2 « Dying Square », −3 octaves (écran OCT −3), random 0 ; position ~100 (écran 100).
- 1:15 LFO 1 : bosse arrondie (écran : Retrig, 1/4) ; sur la position de A ~7 % ; sur le niveau de A ; niveau de A un peu baissé.
- 2:03 osc B : table de la catégorie Vowel (écran : « OOH_YAH_00 », lecture approximative), −3 octaves, random 0.
- 2:21 LFO 2 à plusieurs points sur la position de B, rate 1/2 ; warp de B « Asym+ » (écran) modulé par le même LFO ; LFO 1 sur le niveau de B. LFO 2 en mode Envelope avec point de bouclage au milieu (joue le début puis boucle).
- 3:24 noise ajouté, niveau sur LFO 1, en Direct Out.
- 3:43 filtre passe-haut simple sur A et B, coupure légèrement modulée par LFO 1.
- 4:12 LFO 3 rate 1/2 → matrice : Global > Main Tuning, ~10 %, bipolaire ; LFO 3 en Envelope avec point de bouclage au milieu.
- 4:59 FX : Convolve (catégorie Short, IR « wide vocal » ; écran : « … WIDE VOX ») pour l'élargissement, mix sur LFO 1.
- 5:29 Distortion « Diode 2 », drive au maximum, mix sur LFO 1 ~70 %.
- 5:48 « le plus important » : filtre FX « Cmb HL6− » (comb), coupure ~110 Hz, LFO 2 sur la coupure 30 %, résonance, bouton HL Wid monté à l'oreille.
- 6:37 LFO 4 rate 1 mesure, déclenché en fin de séquence, sur la coupure du comb ~12 %.
- 7:06 trois OTT empilés, gain jusqu'à ce que ça frappe en restant propre ; EQ final avec un peu d'aigus.
- 7:37 variante sustain : dupliquer ; LFO 1 plat en haut et en Envelope ; LFO 2 sans point de bouclage, rate 1/4 ; idem LFO 3 ; LFO 4 désactivé ou adouci.


### F10-02 ECKA's Serum Session: Riddim Bass — ECKA, 9:24, 15/04/2025, Serum 2 (table de l'osc C offerte via MediaFire)
Petite chaîne (136 vues). Transcription + 4 captures (1:16, 3:06, 5:30, 8:20).
- 0:32 osc A : table Digital « Dying Square » (dit « D square »), position ~120 (écran 120).
- 0:51 LFO 1 : pic puis descente exponentielle (écran : Retrig, 1/4) sur la position de A ; variations ajoutées.
- 1:08 macro 1 « Rate » sur le rate du LFO (réglée pour garder une pulsation à la noire) ; macro 2 « Index A » sur la position de A, aussi via la matrice.
- 2:19 osc B : scie « Default Shapes » (dit « triangle »), écran 3:06 ; unison 2 sur A ; warp de A « Sync » (écran).
- 3:19 FX : Hyper/Dimension (rate à 0, taille ~65, mix ~65) ; Distortion Overdrive, deux étages ; EQ : écran 5:30 bande basse en coupe-bas/shelf 180 Hz, Q 46, gain 2,5 ; bande haute 2041 Hz, Q 60, +2,5.
- 4:47 Compressor Multiband : seuil −11,6 dB, ratio 4:1, attaque 0,1, release 0,1, gain 3,1 dB, bandes 128 Hz et 2500 Hz (écran).
- 5:13 Reverb « Vintage », coupe-bas 0 / coupe-haut 35, rate 25, depth 20 (écran).
- 5:58 optionnel : osc C table utilisateur « frog table » (écran, position 116), warp de A « FM (C) » ; macros 3 « Index C » et 4 « Texture C ».


### F11-01 HOW TO MACHINE GUN BASSES (SVDDEN DEATH, CODE: PANDORUM…) — Rocket Powered Sound (Shane), 7:06, 10/05/2020 → Serum 1
Transcription + 2 captures (3:17, 5:39).
- 0:56 tout allumer, empiler des sources qui se heurtent : noise ~72 (écran : noise « AC hum1 », lecture incertaine), osc A table Spectral « Creeper [SN] », osc B carré « Basic Shapes » à niveau faible.
- 1:51 filtre « Combs » sur A et B : coupure laissée à ~425 Hz, résonance ~98, drive au fond, damping monté pour corriger le timbre.
- 2:44 le « machine gun » vient de l'ENV 1 (amplitude), pas d'un LFO : attaque ~0,5 ms, hold 0, decay 116 ms, sustain −inf, release 52 ms (écran) ; le rythme se dessine avec les notes MIDI.
- 3:55 FX : Distortion « Tube », mix à 50 % (moitié sèche) ; filtre FX : deuxième Combs, résonance haute.
- 4:42 Phaser : rate 0, depth 0, freq 0, un peu de feedback (« effet guitare »).
- 5:03 Hyper/Dimension : detune un peu, mix ; écran : unison 4.
- 5:15 Compressor Multiband, seuil à doser selon l'intensité voulue.
- 5:25 Delay court, Link, BPM désactivé, ~15 ms (écran : 12,87 / 12,79 ms), mix monté : teinte métallique.
- 5:52 post-traitement hors Serum : Multipass (Kilohearts) en façon OTT, un peu d'aigus coupés.


### F11-02 PhaseOne & Virtual Riot "Kung Fu" METALLIC GROWL in Serum — Rocket Powered Sound (Shane), 13:24, 20/01/2017 → Serum 1
« Aucun traitement externe, tout dans Serum. » Transcription + 2 captures (6:35, 11:01).
- 1:04 osc A : table « Phase Verb » (écran : « Phase Werb [SL] », lecture incertaine) ; unison monté (écran : 4 voix), detune très bas, random de phase à 0 : effet d'étirement « riddim ».
- 2:21 LFO 1 sur la position de A (au-delà du bout de course), 1/4 ; forme : montée raide puis plateau puis descente (écran : bosse en plateau, mode Trig) ; LFO 1 aussi sur le niveau de A.
- 3:51 menu de la table A : Process > Squarify (son plus « carré »).
- 5:01 osc B : table Spectral « Monster 4 [SL] » pour le grave « de gorge » ; warp « Mirror » (écran) ; unison 6, detune, random 0 ; LFO 1 sur sa position jusqu'à mi-course.
- 6:48 filtre « Flanger − » (dit « flanger negative » ; écran 6:35 encore sur MG Low 12) sur A et B, résonance 50 ; key tracking ; coupure tapée 649 Hz (Global > double-clic pour saisir) ; mix ~50 %, LFO 1 le pousse à 100 %.
- 8:24 FX : Hyper 34, Dimension taille 1 à 3 % puis mix ; écran : unison 4.
- 8:55 Compressor Multiband + gain.
- 9:07 EQ : bande haute en passe-bas, Q ~39 (moins de résonance), fréquence ~222 Hz modulée vers le haut (« filtre passe-bas fait avec l'EQ »).
- 9:58 filtre FX « Bandreject » (écran) : coupure ~93 Hz modulée +30, largeur ~80 modulée vers ~76 (à l'envers), résonance : effet de voix « qui parle ».
- 11:30 Delay court : Link, BPM off, ~1360 (unité non dite), mix et feedback montés.
- 12:01 LFO 1 sur Global Master Amp (après les effets, contourne compresseur et delay).


### F12-01 Virtual Riot SCREECHING FM Bass Serum Tutorial — Rocket Powered Sound, 3:38, 17/12/2017 → Serum 1
Pas de transcription proposée ; étude sur 7 captures (0:41 à 3:16). La description précise que c'est un lead, pas une basse (« bass » dans le titre pour la recherche) ; correction de l'auteur : à 2:49 il voulait dire « LFO 2 ».
- Osc A : scie « Basic Shapes » (scie descendante), OCT 0, unison 16, detune modulé ; warp « FM (from B) ».
- Osc B : table « Default » (scie), OCT +3, unison 16 ; sert de modulateur.
- Filtre « MG Low 12 » (état visible, réglage non suivi).
- ENV 1 : attaque 0,5 ms, hold 0, decay 1,00 s, sustain 0,0 dB, release 15 ms.
- LFO 1 : Trig, 1/8, forme montée raide puis descente linéaire (écran 1:57), ajouté sur l'oscillateur B (cible exacte non visible).
- LFO 2 → warp FM de A : 69 (écran 2:53).
- FX : Distortion « Diode 1 », filtre de distorsion OFF (330 Hz, Q 1,9 par défaut), drive et mix réglés (valeurs non lisibles).
- Voicing : mono non visible ; portamento/legato non lus.


### F12-02 How to Make a Dubstep Screech Bass in Serum (43 Semitone Trick) — EDMProd (Aden), 17:29, 29/06/2021 → Serum 1
Transcription + 3 captures (6:11, 8:51, 13:26). Chapitres : 0:23 corps, 3:10 astuce 43 demi-tons, 6:34 filtre screech, 9:11 compression et détails, 14:30 post-traitement optionnel.
- 0:46 notes autour de F0 (fa mineur), F#, G#… : registre grave pour garder la fondamentale.
- 1:12 osc A : table Massive « Groan 2 » (écran : « 04-Groan II », tables Massive importées, lien en description) ; un peu d'attaque contre le clic (écran : ENV 1 attaque 6,1 ms, hold 0, decay 1,00 s, sustain 0,0 dB, release 15 ms).
- 1:47 LFO 1 en mode Envelope, rate 1/2 pointée : montée rapide courbée puis lente descente (« pseudo-sidechain ») ; sur la position de A, quantité réduite.
- 3:00 mono.
- 3:17 osc B = copie de A (même table, position un peu différente, même modulation), niveau à 0 : source FM seulement ; random de phase à 0 sur A et B (FM cohérente, alignement avec le sub).
- 4:15 warp de A « FM (from B) ».
- 4:42 l'astuce des 43 demi-tons : B monté de +3 octaves et +7 demi-tons (36 + 7 = 43 ; écran : OCT +3, SEM +7) ; la quinte ajoute un intérêt harmonique dans le médium.
- 5:50 quantité FM au milieu, puis LFO 1 sur la FM (écran 6:11 : « LFO 1 → A Warp : 26 »).
- 6:53 filtre « High 24 » sur A seul (écran 8:51), drive, coupure basse, FAT monté, résonance en pic dans le bas-médium, LFO 1 sur la coupure. Pas de key tracking (son plus constant).
- 8:01 sub (sinus) hors filtre, phase alignée avec A et B, niveau modulé par LFO 1 pour suivre le mouvement du filtre.
- 9:31 FX : Hyper/Dimension, 3 voix, detune bas, mix bas (« détune old school ») ; EQ : grave remonté ; EQ placé plus haut dans la chaîne.
- 10:45 Chorus en mode passe-haut (HPF), mix et depth bas.
- 11:14 Distortion « SoftClip » (écran), bon drive : distordre après l'élargissement donne du croquant sur les côtés.
- 11:38 Compressor Multiband, bandes moins écrasées, gain ; médium à préserver ; aigus domptés.
- 12:31 Reverb « Plate » (écran), peu de mix, low cut, peu de high cut, taille et pré-délai bas.
- 13:44 retour : position de table baissée (moins agressive), plus de filtre.
- 14:30 post-traitement optionnel (Ableton) : Compressor 4:1, attaque et release rapides, makeup, en parallèle ; EQ : creux 100-300 Hz (place au kick et à la snare), boost vers 9 kHz, shelf grave raide ; sidechain kick + snare rapide.
Ordre FX à l'écran (13:26) : Hyper/Dimension, EQ, Chorus, Distortion, Compressor, Reverb.


### F13-02 How to Make Your Neurofunk Basses More Expressive (Serum 2) — Art1fact, 12:05, 26/04/2026, Serum 2 (preset « The Waiting Game »)
Transcription + 3 captures (1:21, 4:05, 7:51). Patch présenté déjà fait, puis expliqué.
- 0:11 le rythme se cale avec la phase de départ des deux sinus ; la vitesse du mouvement avec le fine tune.
- 0:49 cœur : FM croisée, A dans B et B dans A en même temps (nouveauté Serum 2). Une quantité vers 20 %, l'autre vers 15 % ; 21 % donne déjà un autre rythme.
- 1:50 deux sinus « Default Shapes » ; A −2 octaves, B −1 octave (écran : OCT −2 / −1), tous deux un peu désaccordés (fine visible sur A, valeur ~31 illisible avec certitude) ; phases différentes (écran : ~136° et ~232°). Warps doubles : A « Diode 1 » + « FM (B) », B « Tube » + « FM (A) ».
- 2:52 aigus : noise « Paper Bag » avec pitch au maximum (bruit blanc granuleux plutôt que transitoires lentes).
- 3:17 filtrage en encoche dans le bas-médium (« là où est l'expression ») : un seul LFO, triangle 2 mesures (écran : LFO 1 Triangle, Retrig, 2 bar). Filtre 1 en pic/encoche avec drive (écran : « Notch 24 » puis « Peak 24 », lecture incertaine) ; filtre 2 en encoche sur une autre zone, modulé en sens inverse (contre-mouvement : le médium reste plein) ; mix du filtre 2 baissé.
- 5:20 FX : Bode (frequency shifter) = toute la stéréo : blur monté, léger décalage, mix ~20 % ; Hyper/Dimension discret ; Chorus avec mouvement sur son passe-bas, mix ≤ 25 %.
- 6:49 principe : garder le mono puissant dans le patch, ajouter la stéréo après (couches en post).
- 7:21 Splitter L/H : Distortion Overdrive sur la bande haute ; fréquence de séparation sur LFO 1 de ~200 à ~650 Hz (écran : « Split Freq 197 Hz », modulé par LFO 1).
- 8:13 Delay (ping-pong à l'écran) et Reverb vers 10 % chacun : juste une queue au relâchement.
Ordre FX à l'écran (7:51) : Bode, Hyper/Dimension, Chorus, Splitter L/H (Distortion dans la bande haute), Delay, …


### F13-03 I Made a Neurofunk Drum and Bass Preset in Serum 2 FROM SCRATCH — Art1fact, 27:12, 19/02/2026, Serum 2 (preset « Super Growler »)
Séance improvisée, peu de valeurs dites. Transcription + 3 captures (6:40, 13:01, 21:30). Tempo 174.
- 0:54 point de départ unique : un carré (osc A « Basic Shapes » en position carrée ; écran : OCT −2 lu avec réserve, unison ~3).
- 1:54 Distortion Overdrive avec « stacks » élevés (étages) : timbres très différents ; problème de clic à l'attaque → ENV 1 sur le mix (et le drive), puis un filtre passe-bas ouvert par une enveloppe lente (écran 6:40 : ENV 2 attaque ~296 ms, sustain 50 %) pour masquer le début.
- 5:27 unison désaccordé à travers l'overdrive : mouvement imprévisible ; ralentir le detune ; jouer sur la phase.
- 7:27 essai de tables ; LFO 2 sur la position/forme (mouvement contrôlé) en plus du mouvement aléatoire (écran : LFO 2 décroissant, Retrig, 1/4) ; warp de A visible « Asym+ » (13:01).
- 9:53 noise (pas le blanc classique ; écran : nom commençant par « JKB HP… », illisible) bas, à travers la distorsion.
- 10:33 filtre « Reverb » avant la distorsion (écran : filtre 2 « Reverb ») ; LFO 3 plus lent (écran : triangle, 1 mesure) ; la convergence des trois mouvements crée de nouvelles dynamiques ; un LFO de plus baisse le mix du filtre au moment où il devient trop aigu.
- 16:36 filtre passe-bas après la distorsion, sur LFO ; Hyper/Dimension (préféré au Dimension seul) ; filtre band reject (dit « band reject » avant, puis un second après la distorsion) sur un des LFO.
- 19:14 aigus : Splitter L/H ; distorsion Rectify essayée sur la bande haute puis abandonnée ; Convolve « Digital Gated » (écran) à ~30 % sur la bande haute pour adoucir.
- 21:29 EQ : léger boost dans les médiums « pour l'expression ».
- 22:40 varier les phases des LFO et le detune ; chaque relance donne un mouvement différent : enregistrer plusieurs prises (resampling) et garder les meilleurs morceaux.
Ordre FX à l'écran (21:30) : Distortion, Filter, Hyper/Dimension, Filter, Splitter L/H (Convolve dans les aigus), EQ.


### F14-01 SERUM 2 FOGHORN BASS Tutorial — Antidote Audio, 6:50, 24/08/2025, Serum 2 (preset gratuit en lien Dropbox ; pack « Radium »)
Transcription + 4 captures (0:51, 2:51, 4:18, 4:46).
- 0:14 trois sinus « Default Shapes » ; A −2 octaves (seul audible) ; B et C muets, sources FM.
- 0:24 B : +1 octave +4 demi-tons (écran : OCT +1, SEM +4) ; C : octave passé en mode Ratio (clic droit), ratio 4,000 (écran : RAT 4.000).
- 0:39 chaîne FM « à l'ancienne » : A reçoit de B, B de C. Écran 0:51 : warps « PD(B) » sur A et « PD(C) » sur B (phase distortion, pas FM linéaire : à vérifier, la voix dit « frequency modulation »).
- 1:05 LFO 1 (Retrig, triangle, 2 mesures) sur la quantité de modulation de A.
- 1:28 astuce : unison 2 sur B avec largeur à 0 (écran : unison 2) ; detune piloté par LFO 2 (2 mesures, rampe montante puis retour).
- 2:18 LFO 3 (2 mesures, forme custom : montée rapide, plateau descendant, chute ; écran) sur le niveau de B ; dernière quantité FM vers « 4 ».
- 3:14 FX (écran 4:18) : Distortion « Diode 1 » (essai de Diode 2), filtre de distorsion OFF ; deuxième Distortion « Stomp Box » ; Compressor Multiband : seuil −18,1 dB, ratio 4:1, attaque 90,1, release 90,1, gain 9,7, bandes 128 Hz et 2500 Hz ; médiums un peu baissés.
- 3:51 filtre « Comb 2 » (nouveau type Serum 2) ; ses résonances favorisent certaines notes : petit réglage pour que le fa tape.
- 4:23 Reverb « Plate » large (écran : coupe-bas 45, coupe-haut 0) ; plus de réverb à la fin.
- 4:42 mono + legato (écran : Mono, Legato, portamento).
- 4:58 plus de sub ; B passé de +4 à +7 demi-tons pour une variante ; saturateur sur le master de la session (hors Serum).


### F14-02 How To Make A DnB FOGHORN BASS in Xfer SERUM! (Like Bou, etc...) — MilleniumBE, 15:07, 01/05/2020 → Serum 1 (FL Studio ; preset en lien OneDrive)
Premier tutoriel de l'auteur (327 abonnés). Transcription + 3 captures (2:20, 7:00, 10:00).
- 2:00 osc A : table Analog « PWM DS » (dite « PM WDS ») ; écran 10:00 : position finale 40 (100 au départ).
- 2:32 unison 7 (écran : 7), detune et blend par défaut ; puis Global > largeur d'unison des osc 1 et 2 à 0 (mono : évite les problèmes de phase).
- 3:22 A −1 octave (écran : OCT −1).
- 3:29 osc B : sinus (écran : « Analog_BD_Sin »), +2 octaves (écran : OCT +2), niveau baissé ; warp de A « FM (from B) ».
- 4:15 sub −1 octave (écran : forme sinus, OCT −1), Direct Out.
- 4:32 FX : Hyper/Dimension (rate et detune un peu baissés) pour rendre de la stéréo ; Distortion « Tube » drive poussé (écran).
- 5:15 noise « BrightWhite » (écran) pour plus d'aigus, niveau et pitch ajustés.
- 5:41 Reverb (écran : mode Hall) : low cut monté, high cut baissé, spin baissé.
- 6:09 Compressor en mode normal (pas multibande : garder le grain du grave), attaque presque à 0, release un peu montée, gain ~7 dB.
- 6:47 EQ : léger boost des aigus (écran : « EQ VolH 3,2 dB »), Q baissé.
- 7:19 filtre « Low 24 » (écran ; dit « lo 24 ») sur A, noise et sub (écran : cases A, N, S), drive, FAT, résonance.
- 7:43 ENV 2 sur la coupure (écran 10:00 : attaque 132 ms, hold 0, decay 2,42 s, sustain 0 %, release 15 ms) ; courbe ajustée ; modulation passée en unipolaire dans la matrice ; coupure de base ~30 Hz, quantité montée (« 26 » dit).
- 9:21 niveaux des couches automatisés à volonté ; quantité FM montée ; chercher le bon couple position de table / FM.
- 10:18 post-traitement FL Studio : Fruity Waveshaper (légère saturation), EQ coupe-bas doux ~84 Hz, boost médiums/aigus, delay.


### F15-02 ERB N DUB - ROLLER BASS SERUM TUTORIAL — ERB N DUB, 5:36, 30/08/2019 → Serum 1 (Cubase ; patch « BA A Team » du pack Serum Rollers)
Patch déjà fait, rétro-ingénierie expliquée. « Tout dans Serum, pas de traitement externe. » Transcription + 3 captures (1:55, 3:13, 4:11).
- 1:04 osc A : « Analog_BD_Sin », sans unison, detune, blend ni random ; position fixe (écran : 256) ; niveau 27 % ; −1 octave (écran : OCT −1) ; fine modulé par la macro 4 (écran : « A Fine, Assigned Modulators : Macro 4 ») ; warp « FM (Sub) ».
- 1:43 le sub ne sert qu'à moduler : niveau à 0, −1 octave (écran : OCT 1 affiché, à confirmer), fine-tuné.
- 1:57 osc B : « SawRoundedToSquare » (écran ; position 11), −2 octaves, fine +28 (écran : FIN 28), phase au milieu, random 0, warp « FM (Sub) », niveau 9 % ; A et B désaccordés l'un contre l'autre : effet proche de la Reese. « Des tables simples ; une table chargée ne donnera jamais ce poids. »
- 2:55 filtre « MG Low 6 », résonance et drive montés, une enveloppe sur la coupure et le FAT, mix 91 %.
- 3:10 noise « AlphaNz » (dit « alpha and Zed »), pitch monté, key track, niveau qui retombe sous ENV 1 (écran : ENV 1 attaque 67 ms, hold 0, decay 946 ms, sustain −4,4 dB, release 343 ms).
- 3:24 FX : Distortion « Diode 1 », mix 100 %, ENV 2 sur le drive (écran 4:11 : ENV 2 attaque 387 ms, decay 1,00 s, sustain 100 %, release 15 ms) ; EQ en « sourire » (grave et aigus montés), sans modulation.
- 3:46 Hyper : mix 12, unison 3 (écran : 3) pour un peu de stéréo.
- 3:57 filtre FX « MG Low 6 », mix 44 %, coupure ~505 Hz : dompte les aigus.
- 4:14 Reverb (écran : Hall) dont le mix monte sous LFO 4 en mode Envelope, synchronisé, 4 mesures : une traîne qui arrive.
- 4:34 Global : mono, un peu de portamento, pitch bend +12, largeur de l'unison à 0 (« le plus de mono possible »).
- 4:55 principe : longs mouvements par LFO lents ou enveloppes lentes ; macros ajoutées (écran : FM, Bend, Verb, FM).
