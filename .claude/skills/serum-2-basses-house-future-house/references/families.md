# Dix familles de basses : programmation Serum 2

Valeurs originales de départ, à régler par l'oreille et à niveau comparable. A/B : oscillateurs; ENV 1 : amplitude. Si les noms de filtres/warp varient avec la version, choisir l'équivalent audible. Une source FM inaudible peut être routée `None`; `Direct` contourne seulement le filtre et les FX internes (`../../sound-designer-serum/references/serum2-fx-clip-arp.md`, routage).

**Conventions de ce workflow.** Notes en numérotation Ableton, C3 = 60 (F0 = 43,7 Hz ; la version d'origine donnait « F1–A1 » en notation scientifique). Trois ou quatre macros par famille : c'est un choix de gestes, Serum 2 en offre huit ; pour les automatiser depuis Live, configurer d'abord les paramètres exposés (`../../sound-designer-serum/references/serum2-automation-et-migration.md`). Modes de LFO : « Trigger » (redémarre à chaque note, indispensable pour un growl ou un wub reproductible, fiche 03 de `../../sound-designer-serum/references/fiches-pratiques.md`), « Envelope » (un seul cycle) et libre ; relever le libellé exact dans l'interface installée. Motifs MIDI vérifiés par famille : `motifs.md`. Réalisation dans Live : `../../vst-sound-design/SKILL.md` (chargement sans hot-swap, tableau paramètre / valeur / preuve).

| Famille | Usage | Geste principal |
| --- | --- | --- |
| 1 Sub sinus | fondation | fondamentale stable |
| 2 Pluck rond | Future House | decay de filtre |
| 3 Hollow FM | Future House | FM légère et timbre creusé |
| 4 Organ bass | Future House | partiels tenus, jeu staccato |
| 5 Saw percussive | Bass House | attaque brillante |
| 6 Reese | Bass House, DnB | battements d'oscillateurs |
| 7 Wub | Bass House | filtre périodique |
| 8 Growl vocal | Bass House, DnB | formants mouvants |
| 9 Donk métallique | Bass House | pitch et FM brefs |
| 10 Screech | accent | résonance haute |

## 1. Sub sinus

A sine, octave -1 ou -2 selon la note MIDI, mono, aucun unison; ENV 1 attaque 2–5 ms, sustain 100 %, release 50–100 ms. Très légère saturation parallèle si les petites enceintes exigent une seconde harmonique. Macro `Weight` dosage de saturation avec compensation du gain. Jouer les fondamentales F0–A0 (Ableton, 43,7–55 Hz) comme essai, notes courtes après le kick et une tenue de fin de phrase. Release 50–100 ms pour des notes espacées ; 20–30 ms si elles se suivent de près (`../../sound-designer-serum/references/basses.md` § Sub). Tester kick/sub ensemble en mono, chaque note et fin de queue. Éviter chorus, reverb et pitch mouvant.

## 2. Pluck rond

A saw ou square adoucie à octave 0/-1; low-pass 12/24, cutoff initial 200–500 Hz, peu de résonance. ENV 2 vers cutoff : attaque 0–5 ms, decay 120–280 ms, sustain 0–20 %; ENV 1 decay 200–450 ms, sustain 0–40 %. Saturation légère. Macros `Bite` amplitude ENV 2, `Length` decay, `Round` cutoff. Jouer staccato en contretemps, vélocité variable. Tester le key tracking du filtre si les notes montent d'une octave.

## 3. Hollow FM

A sine/square audible; B sine +12 ou +24 demi-tons, routé `None` si seul modulateur. FM de B sur A, profondeur initiale environ 5–20 % à l'oreille. Low-pass ou band-pass modéré. ENV 2 vers FM : decay 100–250 ms; ENV 1 pluck 150–350 ms. Macros `Hollow` FM, `Mouth` filtre, `Snap` decay. Notes espacées, sub séparé; vérifier la densité des médiums avec la batterie.

## 4. Organ bass

A sine à harmoniques empilées (dessinées dans l'éditeur d'harmoniques de la wavetable) ou wavetable d'orgue; B sine à +12 demi-tons à niveau réduit. (La version d'origine citait un « mode harmonique Serum 2 » qui n'apparaît pas dans la doc Serum 2 du dépôt : le vérifier dans l'interface avant de le prescrire.) ENV 1 attaque 2–10 ms, sustain 65–100 %, release 70–150 ms. Low-pass doux et compression légère si nécessaire. Macros `Drawbars` balance des partiels, `Gate` release, `Air` cutoff. Jouer en contretemps; les intervalles au-dessus sont permis, mais un sub séparé ne suit que la fondamentale.

## 5. Saw percussive

A saw, unison 2 voix avec detune discret sur la seule couche mid. ENV 1 decay 140–300 ms, sustain 0–30 %; ENV 2 ouvre un low-pass en 80–200 ms. Distortion douce puis EQ pour contenir l'attaque. Macros `Punch` enveloppe de filtre, `Dirt` drive, `Tail` decay. Placer notes répétées dans les espaces du kick, fill en doubles croches. Vérifier la pointe et le déclenchement du compresseur de bus.

## 6. Reese

A/B saw ou saw + square à même hauteur, désaccordés de ±15 cents (lent, doux) à ±30 cents (signature DnB), fourchette où convergent Attack Magazine et Native Instruments (`../../sound-designer-serum/references/basses.md` § Reese) ; la version d'origine proposait ±4–10 cents, battement très lent (vers un cycle toutes les 2 s sur La0). Le battement accélère avec la hauteur : régler sur la note la plus jouée. Unison modéré. ENV 1 sustain élevé; low-pass mobile. Distortion, chorus ou Hyper uniquement sur le mid, coupé sous 100–120 Hz ; sub sinus séparé sur la même ligne MIDI (le Reese est incompatible avec le rôle de sub). LFO 1 lent en mode libre pour la dérive, Trigger pour la répétabilité, vers cutoff; ne pas déplacer le pitch du sub. Macros `Beat` detune, `Motion` cutoff, `Grit` drive. Alterner tenues et silences; tester plusieurs notes en mono.

## 7. Wub

A saw/square riche; low-pass ou band-pass résonant. LFO 1 courbe montée/descente en mode Trigger, sync 1/8 ou 1/4 vers cutoff. ENV 1 sustain haut, release 50–120 ms. Distortion après filtre, sub indépendant stable. Macros `Rate` choix de divisions, `Depth` quantité de filtre, `Vowel` couleur. Une note tenue sur demi-mesure dialogue avec le kick; comparer 1/8, 1/8 pointée et 1/16 pour les fills.

## 8. Growl vocal

A saw ou wavetable spectrale; B sine modulant A par FM légère si besoin. Filtre formant (Formant-I/II/III selon version), cutoff/morph piloté par LFO 1 à 1/4 ou 1/8 en mode Envelope ou Trigger, résonance 20–40 % pour garder des voyelles lisibles; essayer aussi un warp `Bend` 30–50 % ou FM 15–25 % (`basses.md` § Neuro / growl). « VAR FORMNT », cité par la version d'origine, ne figure pas dans la liste documentée des warps Serum 2 (`../../sound-designer-serum/references/moteurs-synthese.md`) : à vérifier dans l'interface. Distortion puis EQ des pics nasaux; effets larges seulement sur le mid. Macros `Talk` formant, `Snarl` FM/drive, `Width` effets, `Dry` mix. Laisser un silence avant chaque réponse; resampler plusieurs prises. Séparer le sub si le pitch global est automatisé.

## 9. Donk métallique

A sine/triangle fondamentale; B sine en ratio harmonique 2:1 ou 3:1 pour FM modérée. ENV 2 excursion locale de pitch initiale +12 à +24 demi-tons, decay 20–60 ms; autre enveloppe ou même geste sur FM 40–130 ms. ENV 1 decay 130–300 ms, sustain 0. Saturation douce. Macros `Knock` pitch, `Metal` FM, `Body` longueur. Syncopes courtes et doubles occasionnels; retirer l'excursion de la piste sub.

## 10. Screech

A saw ou wavetable riche, FM de sine B éventuellement légère. Band-pass, formant ou comb selon le timbre; résonance limitée, balayage ENV 2/LFO 1, distortion après filtre puis EQ des crêtes. ENV 1 100–400 ms; glide uniquement sur cette couche. Macros `Scream` fréquence, `Rasp` drive, `Fall` glide, `Space` delay court. Accent en fin de phrase; contrôler le haut médium vers 1–5 kHz à faible volume.

## Assemblages

Future House : 1 + 2 ou 3, 4 en section de réponse. Bass House : 1 + 5 ou 7, puis 8 en réponse, 9/10 ponctuels. DnB : 1 + 6 ou 8 avec rythme de break réécrit; ne pas se contenter d'accélérer un pattern House. Un motif de départ pour chacun : `motifs.md`.
