# Mixage par style : synthèse de 60 tutoriels

Synthèse du 05/10/2026 du corpus `tutoriels-mixage-par-style.md` : 60 vidéos YouTube, dix styles × 6. Bass house (BH-01 à BH-06), house classique (HC), tech house (TH), techno (TE), rave (RA), future bass / future rave (FB), deep / minimal / microhouse (DM), afro house (AF), drum and bass (DB), dubstep (DS).
L'étude a été faite dans Claude in Chrome sur le Mac. Les transcriptions ont été lues, son coupé : **rien n'a été entendu**. Aucune capture d'écran n'a été faite.
Les identifiants sont ceux de `tutoriels-mixage-par-style.md`. Les préfixes BH, HC, TE, RA, FB, DM et AF désignent d'autres vidéos dans le corpus des kicks (`../../drums-signature/references/kicks-serum-tutoriels.md`) : ne pas les confondre.
[SOURCE XX-nn] = dit dans la vidéo (transcription ou description). (interp.) = mon interprétation ou celle de l'étude. [ASR ?] = transcription automatique douteuse.
DAW filmés : Ableton Live dans 33 vidéos, FL Studio dans 16 (17 avec AF-06, probable), Studio One, Logic Pro et Reaper une fois chacun, DAW non dit dans 7. Une seule vidéo en français (TE-03).
Les niveaux en dB sont ceux que disent les vidéos (fader, crête ou meter, souvent sans unité claire) : des points de départ, pas des normes. Cadre du projet : `../SKILL.md`, `genres-et-espace.md`, `diagnostic-et-recettes.md`, `../../ingenieur-mixage/SKILL.md`.

## Ce que dit le corpus avant tout

- **Le grave d'abord, le kick roi.** Commencer par kick + basse, le reste muet [SOURCE RA-01, FB-01, DS-04, HC-06]. Kick élément le plus fort [SOURCE TH-02, DM-01, DM-04, DB-04, RA-01] ; low end au-dessus des drums [SOURCE TE-01, TE-06].
- **Sub et basse séparés, sub mono.** Sub en sinus sur sa piste, basse haute en passe-haut [SOURCE BH-03, HC-02, DM-01, DB-05, DS-03]. Mono sous une fréquence dite de 140 à 200 Hz selon la vidéo [SOURCE BH-01, BH-05, TH-02, RA-03, RA-05, DB-02].
- **Sidechain presque partout, mais dosé.** Trigger fantôme (ghost kick) plus court ou avancé [SOURCE BH-02, TE-02, RA-04, FB-06, DM-01, DM-03]. Limité au grave [SOURCE BH-01, TH-02, AF-01]. Trop profond, il creuse un trou [SOURCE TH-05] ; parfois inutile si la basse tombe entre les kicks [SOURCE HC-06].
- **Des bus par rôle, du clip avant le limiteur.** Bus kick & basse, drums, musique, voix, FX [SOURCE BH-01, HC-01, TE-04, DM-03, AF-02, DS-01]. Soft clip ou clipper sur kick et groupes [SOURCE HC-04, TE-01, TE-05, DB-01, DB-03, DS-01]. Compression parallèle des drums [SOURCE BH-01, HC-04, DB-01, DB-02].
- **Marge et référence.** Pré-master à −6 dB de crête [SOURCE TE-01, DM-01, DM-02, DM-04, AF-02, AF-03, AF-04, DB-02]. Référence dans le projet, à niveau égal [SOURCE BH-01, HC-02, TH-02, DM-02, DB-03, DS-03]. Juger en contexte, pas en solo [SOURCE HC-03, FB-03, AF-01, DB-05].
- **La sonie dépend du style.** Les cibles dites vont de −8,5 LUFS (disco house, HC-02) à −1,2 LUFS (dubstep, attribué à Nosphere, DS-03). Ce sont des témoignages, pas des consignes (`mastering-streaming-et-club.md`).

## Bass house

- Quatre vrais mixages (BH-01 à BH-04), deux masters retenus faute de mieux (BH-05, BH-06). Kick plus fort que la basse : il porte le rythme [SOURCE BH-01].
- Sub en sinus à la fondamentale, basse haute coupée entre fondamentale et 2e harmonique [SOURCE BH-03]. Subs compressés fort, alignés à 1 dB près ; basses groupées avec multibande léger [SOURCE BH-01, BH-02, BH-04].
- Sidechain du sub seul, calé sur la longueur du kick [SOURCE BH-03] ; limité au grave, sans clic [SOURCE BH-01] ; kick dupliqué en clic court comme trigger [SOURCE BH-02].
- Basse haute élargie sans casser le mono : Haas (le moins sûr), chorus sans grave, ou une répétition en opposition de phase (préférée) [SOURCE BH-03]. Retours reverb/delay sidechainés au kick [SOURCE BH-01].
- Master : Glue en clipper, plus d'aigus dans les côtés, limiteur [SOURCE BH-02] ; soft clipper avant le limiteur [SOURCE BH-06].

| Paramètre | Valeur | Source |
|---|---|---|
| Kick au fader, départ | −10 à −15 dB ; référence baissée d'≈ 15 dB | BH-01 |
| Sidechain du sub ; multibande kick & basse | sous 150 Hz, release rapide ; bande grave, ratio 3:1 | BH-01 |
| Passe-haut basse haute | 60–63 Hz (sub 41 Hz, Mi1 ; harmonique 82 Hz) ; Haas < 30 ms | BH-03 |
| Mono | sous 200 Hz (100–200 selon le goût) | BH-01, BH-05 |
| Master | Glue ≈ 4 dB, attaque lente ; passe-haut 30–35 Hz ; crête −0,3 à −1,5 dB (lui −0,3) | BH-05 |
| Sonie | « −5 à −6 » (interp. : LUFS court terme) ; ≈ −6 visé [ASR ?] | BH-02, BH-06 |

Lire d'abord : BH-01, BH-03, BH-02.

## House classique

- Top-down : mix bus puis bus drums avant les pistes [SOURCE HC-01, HC-04]. HC-06 part au contraire du kick quand le problème n'est pas identifié.
- Drums en bus kick, low perc, high perc [SOURCE HC-01]. Chaîne de bus : saturation, EQ soustractive, compression, EQ additive, clip [SOURCE HC-04].
- Kick 909 : sustain réduit au transient designer plutôt qu'au compresseur [SOURCE HC-01] ; raccourci quand la basse tient ses notes [SOURCE HC-06]. Coupe-bas à 20–25 Hz [SOURCE HC-01, HC-03] ou aucun, par crainte de la phase [SOURCE HC-02].
- Sub neutre + mid-bass de caractère [SOURCE HC-02]. Sidechain presque inutile si la basse tombe entre les kicks [SOURCE HC-06].
- Pompage « French touch » : émulation Alesis 3630 sur le master, EQ avant le L2 [SOURCE HC-05].

| Paramètre | Valeur | Source |
|---|---|---|
| Mix bus / bus drums (SSL G) | 1–2 dB, attaque 30 ms, ratio 2 / 4–5 dB, filtre sidechain ≈ 150 Hz | HC-01 |
| Kick 909 | passe-haut ≈ 20 Hz, boost 56–60 Hz, coupe ≈ 200 Hz ; clap HP ≈ 165 Hz, hat ≈ 180 Hz | HC-01 |
| Kick (attaque) ; percussions | 800 Hz – 2 kHz ; rien autour de 50 Hz | HC-03 |
| Bus drums | Glue : rien sous 200 Hz compressé ; KClip ≈ 3,5 dB gagnés | HC-04 |
| Deux limiteurs master | ≈ 1 dB chacun ; sortie −1 dB, puis −0,2/−0,3 (true peak) | HC-02 |
| Sonie | ≈ −8,5 LUFS court terme ; visé −7 à −9 (interp.) | HC-02 |

Lire d'abord : HC-01, HC-04, HC-06.

## Tech house

- Kick le plus fort, comparé à la référence dans SPAN [SOURCE TH-02] ; kick > basse > voix > reste [SOURCE TH-06].
- Sub aussi fort ou un peu plus que son harmonique [SOURCE TH-01]. ShaperBox sur la basse, courbe inversée sur le kick : ils alternent [SOURCE TH-02]. Multibande commun ; sidechain trop profond = trou [SOURCE TH-05].
- « Les drums doivent occuper tout le champ stéréo » [SOURCE TH-04] ; clap au centre, shakers à gauche et à droite [SOURCE TH-02, TH-04].
- Bus drums compressé, sidechain filtré pour épargner le kick [SOURCE TH-02, TH-03, TH-04] ; clip avant le limiteur [SOURCE TH-03].
- Build : reverb qui monte, dernière phrase sèche ; gain master qui descend puis saute au drop ; largeur qui s'ouvre [SOURCE TH-01].

| Paramètre | Valeur | Source |
|---|---|---|
| Gain staging ; niveaux | −12 dB pré-fader par piste, limiteur du mix 0 à −3 dB ; hat −0,5 dB, clap +1 dB | TH-02, TH-03 |
| Bus drums | SSL : attaque 30, ratio 2:1, HPF sidechain 185 Hz, ≈ 2 dB ; Glue : attaque 30 ms, ratio 4, ≤ 5 dB | TH-02, TH-04 |
| Kick / basse | sub ≈ 45 Hz, harmonique ≈ 96 Hz ; ShaperBox sous 516 Hz, à la noire ; bande sub ≈ 75 Hz | TH-01, TH-02, TH-05 |
| Reverb ; build | low cut ≈ 300 Hz, high cut ≈ 4–6 kHz ; gain master −0,8 puis +0,8 dB au drop | TH-01 |
| Master | mono sous ≈ 200 Hz ; limiteur −3/−4 dB max, attaque ≈ 1 ms | TH-02 |
| Sonie | non dite | — |

Lire d'abord : TH-02, TH-01, TH-03.

## Techno

- Low group (kick + basse) au-dessus des drums [SOURCE TE-01] ; hats jamais au-dessus du low end dans SPAN [SOURCE TE-06].
- Kick accordé sur la fondamentale ou la quinte ; pas de notes de basse sur les temps du kick [SOURCE TE-02]. EQ après la saturation, qui ajoute du grave [SOURCE TE-01].
- Compresseurs de kick et de basse avec filtre sidechain passe-haut : le sub passe sans compression [SOURCE TE-02]. Glue lente à l'attaque, rapide au release sur le low end [SOURCE TE-06].
- Soft clip des groupes qui dépassent le kick [SOURCE TE-01]. Hard techno : distorsion → soft clip → hard clip sur le bus kick, ni limiteur ni compresseur [SOURCE TE-05].
- Profondeur par filtres, delays et notch (dub techno) [SOURCE TE-04]. Atmo trop large à rétrécir ; polarité du kick inversée avec prudence [SOURCE TE-06].

| Paramètre | Valeur | Source |
|---|---|---|
| Pics des groupes | low group −11 contre drums ≈ −7 : à inverser ; export « −6 » | TE-01 |
| Soft clip (Saturator) | output au plafond voulu (−2, −4…), drive ≈ même valeur | TE-01 |
| Compresseur kick | HPF sidechain 100–200 Hz, ≈ 4 dB, attaque 20 ms, release 100–150 ms | TE-02 |
| Compresseur basse | HPF sidechain 138 Hz, ratio 4:1, attaque 10–30, release 60–200, ≈ 3 dB | TE-02 |
| Niveaux au spectre | fondamentale du kick −14 à −20 dB ; basse 3 à 6 dB dessous | TE-02 |
| Top kick hard techno | passe-haut 100–200 Hz ; clip ≈ 2 dB, ou 1,3 dB en hard clip seul | TE-05 |
| Sonie | ≈ −6 LUFS en hard techno / schranz ; techno classique non dite | TE-05 |

Lire d'abord : TE-02, TE-01, TE-06.

## Rave

- Vrais tutoriels rave introuvables : corpus élargi au hardgroove (RA-01, RA-02) et au UK hardcore (RA-03 à RA-06). Kick roi ; les loops de percussion s'emboîtent par leur choix, pas par le traitement [SOURCE RA-01].
- Rumble : un peu de sub coupé, passage en mono [SOURCE RA-01]. Creuser les résonances vers 200 Hz avant de distordre [SOURCE RA-02].
- Sidechain = pilier du style : le kick fait baisser leads, voix et basse, par un ghost kick court [SOURCE RA-04] ; sub ducké par le kick [SOURCE RA-03, RA-05].
- La fin du kick tombe où le sub démarre ; sub ≈ volume du kick, un peu plus bas [SOURCE RA-05]. Ne pas élargir le sub [SOURCE RA-04].
- Reverb gate parallèle sidechainée par le lead sec [SOURCE RA-02] ; reverb en send sidechainée par les leads et le kick [SOURCE RA-03].

| Paramètre | Valeur | Source |
|---|---|---|
| Rumble ; kick | coupe de 20 à « 50 ou 60 » Hz ; creux 100–200 Hz | RA-01, RA-05 |
| Reverb en send | hall, decay 8 s, coupe sous ≈ 374 Hz | RA-03 |
| Gain staging | ≈ −9 dB ; Inflator +12 dB pendant le mix → 9–12 dB de marge | RA-03 |
| Mono | sous 180 Hz (master) ; sous 150 Hz (sub) | RA-03, RA-05 |
| Sub | limiteur ≈ 48 dB de réduction (« probablement overkill ») | RA-05 |
| Plafond / sonie | −0,1 dB ; LUFS non dite | RA-03 |

Lire d'abord : RA-01, RA-05, RA-03.

## Future bass / future rave

- Future rave : FB-01 et FB-02 seulement, en FL Studio ; Ableton : FB-03 seul. Commencer par le drop, kick + basse ; sidechain en miroir, « le kick et la basse ne se touchent jamais » [SOURCE FB-01].
- Une piste par couche de lead vers un bus commun, limiteur par bus [SOURCE FB-01] ; retirer la reverb d'origine des presets [SOURCE FB-02].
- « Penser propre » : pas de reverb sur les accords de base, reverb au niveau des leads [SOURCE FB-03]. FB-04 met au contraire le même plug-in de reverb sur presque tout.
- OTT après la reverb [SOURCE FB-01, FB-04] ; multibande avant la reverb, pour ne pas la compresser [SOURCE FB-06]. Équilibrer au bruit rose, très bas et en mono [SOURCE FB-01].
- Build : sub coupé, largeur et gain réduits jusqu'au drop [SOURCE FB-01, FB-02]. Master top-down, compresseur à moins de 1 dB, limiteur de sécurité [SOURCE FB-05].

| Paramètre | Valeur | Source |
|---|---|---|
| Limiteur par bus ; build | ≤ 6 dB de réduction ; largeur 0,8 (0,75–0,70 max), gain −1,5 à −2 dB max | FB-01 |
| EQ final master | HP 48 dB/oct ≈ 30 Hz ; LP 48 dB/oct 19,5 kHz ; +0,5 à +1 dB d'aigus | FB-01 |
| OTT ; Glue master | master < 10 % (5–7 %) ; Glue attaque 10 ms | FB-02 |
| OTT ; low cut | 43 % piano, 4 % accords ; lead ≈ 250 Hz | FB-04 |
| Mix bus | HP 12 dB/oct à 30 Hz ; compresseur < 1 dB, HPF sidechain 100 Hz | FB-05 |
| Sonie | non dite | — |

Lire d'abord : FB-01, FB-03, FB-05.

## Deep / minimal / microhouse

- Kick 909 en mono, sans compresseur [SOURCE DM-01, DM-02]. Basse en pistes LOW et HIGH, chorus sur la partie haute seulement [SOURCE DM-01, DM-02].
- Ghost kick muet comme source, le pompage continue sans kick [SOURCE DM-01] ; avancé de 10 ms [SOURCE DM-03]. « Règle des 6 dB » pour les niveaux [SOURCE DM-01].
- Compression en plusieurs étages légers ; multibande sur les bas-médiums plutôt qu'un passe-haut qui amaigrit [SOURCE DM-03].
- Boue entre 100 et 250 Hz, à creuser sur le canal mid seulement [SOURCE DM-05]. Kick long + sub long à éviter ; 80–90 % du mix = niveaux [SOURCE DM-06].
- Mixer surtout en mono ; master de travail mono + low-cut 100 Hz [SOURCE DM-02].

| Paramètre | Valeur | Source |
|---|---|---|
| Kick (EQ) ; split basse | passe-haut ≈ 40 Hz ; LOW / HIGH vers ≈ 200 Hz, les deux mono | DM-01 |
| Saturator basse LOW | drive 16–17 dB, output −17 dB, Soft Sine, soft clip | DM-01 |
| Niveaux sous le kick | basse −6 ; accords −6 / −15 ; pads −18 à −24 ; clap −6 ; hat −6 à −10 | DM-01 |
| Départ ; basse | kick ≈ −12, basse ≈ −15/−16 dB ; chorus au-dessus de ≈ 120–160 Hz ; creux dynamique 80–90 Hz (kick ≈ 94 Hz) | DM-02 |
| Glue drum bus | 2–3 dB (parfois ≈ 5), ratio 4, parallèle ≈ 43 % | DM-03 |
| Pré-master ; sonie | crête −6 dB ; ceiling final −0,1 dB ; LUFS non dite | DM-01, DM-02, DM-04 |

Lire d'abord : DM-01, DM-03, DM-02.

## Afro house

- Deux vrais mixdowns seulement (AF-01, AF-02). Kick trop long : volume shaper en deux bandes ; sub ducké fort mais pas totalement, mid-bass plus doucement [SOURCE AF-01].
- « Toujours » un sidechain très court sur les percussions [SOURCE AF-01] ; shakers sidechainés au kick, très subtil [SOURCE AF-02].
- Shakers et aigus souvent trop forts : bande d'EQ dynamique [SOURCE AF-01] ; transient shaper sur le haut ; référence trop poussée à remplacer [SOURCE AF-05].
- Auto Pan subtil, en phase inversée sur deux percussions ou deux pads ; reverb automatisée avant les drops [SOURCE AF-02]. Centre réservé aux drums [SOURCE AF-03].
- Low-cut sur tout sauf kick et basse [SOURCE AF-04]. Voix : chaîne sans valeur dite [SOURCE AF-06].

| Paramètre | Valeur | Source |
|---|---|---|
| Séparation du volume shaper | ≈ 150 Hz | AF-01 |
| Marge | crête −6 dB sur la partie la plus forte | AF-02, AF-03, AF-04 |
| Low-cut hors kick/basse | jusqu'à ≈ 100 Hz, sinon 20–50 Hz ; « 50 Hz recommandé » | AF-04 |
| Chaîne master | EQ M/S sans grave dans le side, Compressor, Saturator, Multiband, EQ, Limiter : sans chiffres | AF-02 |
| Sonie | non dite | — |

Lire d'abord : AF-01, AF-02, AF-05.

## Drum and bass

- Kick, snare et basse d'abord, niveaux fixés par élément [SOURCE DB-01, DB-04] ; basse 2 à 3 dB sous le kick en crête [SOURCE DB-03].
- Un seul élément par zone dans le grave : passe-haut sur la mid bass ou la Reese [SOURCE DB-01, DB-05, DB-06]. Mono sous 140 Hz [SOURCE DB-02].
- Sidechain multibande du bus basses keyé par la snare [SOURCE DB-02] ; EQ dynamique keyée par sa fondamentale [SOURCE DB-06] ; sub keyé par le kick [SOURCE DB-02, DB-06].
- Clip sur snare, kick, bus basses et drums [SOURCE DB-01, DB-03, DB-04] ; compression parallèle des drums [SOURCE DB-01, DB-02, DB-06].
- Retours duckés par la voix [SOURCE DB-01, DB-06] ; build : passe-haut, gain et largeur réduits, tout remonte au drop [SOURCE DB-03].

| Paramètre | Valeur | Source |
|---|---|---|
| Niveaux | kick, snare −6 ; sub −9 « toujours » ; hats −9/−12 ; mid basses −6 ou −9 | DB-01 |
| Jump-up | kick juste sous 0 ; sub ≈ −3 ; hat ≈ −12 ; riser −27 | DB-04 |
| Sidechain multibande | ≈ 178–300 Hz et > 3,74 kHz, keyé snare ; attaque 0, release 52 ms | DB-02 |
| Sub / Reese | sub : HP < 30 Hz, LP > 100 Hz ; Reese : coupe < 100 Hz, creux 200–300 Hz, rien < 400 Hz sur les côtés | DB-06 |
| Build ; Maximizer | passe-haut jusqu'à ≈ 120 Hz, −2 dB, largeur 70–80 % ; True Peak, plafond −1 dB, 4–5 dB de réduction max | DB-03 |
| Sonie | ≈ −5 LUFS visé (−7 atteint) ; ≈ −6 LUFS ; RMS −3 à −6 dB | DB-01, DB-04, DB-02 |

Lire d'abord : DB-02, DB-01, DB-06.

## Dubstep

- Kick et snare touchent 0 dBFS dans un clipper ; drums les plus forts [SOURCE DS-01, DS-04, DS-05].
- Un seul élément dans le grave, basses sans grave [SOURCE DS-03, DS-04, DS-05] ; côtés sans grave [SOURCE DS-01, DS-02].
- Groupe « side chain » : tout sauf kick + snare passe par un même ducking [SOURCE DS-01]. Sidechain indispensable au drop, pas forcément en intro [SOURCE DS-03].
- Sonie construite piste par piste (OTT, soft clip, clip à 0) [SOURCE DS-03, DS-05] ; si le titre ne monte pas, le problème est dans les pistes [SOURCE DS-02]. Build moins fort que le drop [SOURCE DS-04].
- Niveau du sub contradictoire : 0 dB [SOURCE DS-03], −4 à −6 [SOURCE DS-04], −6 [SOURCE DS-05], ≈ −20 [SOURCE DS-06].

| Paramètre | Valeur | Source |
|---|---|---|
| Hats ; basse vs mélodie | creux 3–4 kHz ; mélodie 300–500 Hz → creux 400 Hz sur la basse | DS-01 |
| Master Ozone | 3–4 dB de réduction ; aigus 7:1, parallèle ≈ 90 % | DS-01 |
| Côtés ; sub au spectre | coupe vers 150–180 Hz ; sub sur la ligne −30 dB de SPAN | DS-02 |
| Sub ; wobble | coupe au-dessus de 100–110 Hz ; HP > 100 Hz, creux 4–8 kHz, LP 16 kHz | DS-03, DS-05 |
| Build ; riddim | −1 puis −2 dB, intro ≈ 1 dB sous le drop ; kick ≈ −10, 3 claps à −20, master ≤ −10 avant la chaîne | DS-04, DS-06 |
| Sonie | ≥ −6 LUFS, −3/−4 avec GClip seul ; −5 au plus calme, −2 voire −1,2 cités ; drop −2,4/−3 | DS-02, DS-03, DS-04 |

Lire d'abord : DS-01, DS-04, DS-02.

## Tableau comparatif

| Style | Sonie dite | Kick / basse | Sidechain | Largeur | Particularité |
|---|---|---|---|---|---|
| Bass house | −5 à −6 (interp. LUFS) | kick plus fort ; sub séparé | grave seul, < 150 Hz | mono < 200 Hz ; basse haute élargie | clip au master |
| House classique | ≈ −8,5 LUFS | sustain 909 réduit ; sub + mid-bass | léger, parfois inutile | non chiffrée | pompage « French touch » |
| Tech house | non dite | kick le plus fort ; ils alternent | ShaperBox < 516 Hz, inversé | drums sur tout le champ ; mono < 200 Hz | gain et largeur automatisés au build |
| Techno | ≈ −6 (hard techno) ; sinon non dite | basse 3–6 dB sous le kick | filtre sidechain ; ghost kick | atmo rétrécie | soft et hard clip |
| Rave (UK hardcore) | non dite ; plafond −0,1 dB | sub ≈ kick, un peu plus bas | « pilier » : leads, voix, basse | mono < 150–180 Hz | reverb gate sidechainée |
| Future bass / rave | non dite | sub ≈ kick ou un peu plus bas | miroir parfait | largeur 0,8 au build | limiteur par bus de lead |
| Deep / minimal | non dite ; crête −6 dB | basse ≈ 6 dB sous le kick | ghost kick avancé de 10 ms | chorus > 120–160 Hz | règle des 6 dB |
| Afro house | non dite ; crête −6 dB | volume shaper 2 bandes | très court sur les percussions | Auto Pan inversé ; centre aux drums | shakers et aigus à dompter |
| Drum and bass | ≈ −5 à −6 LUFS | basse 2–3 dB sous le kick ; sub −9 | multibande keyé par la snare | mono < 140 Hz | niveaux fixes par élément |
| Dubstep | −6 à −1,2 LUFS | kick et snare à 0 dBFS (clip) | un groupe « side chain » | côtés sans grave < 150–180 Hz | sonie construite par piste |

## Traduction dans l'installation du projet

Règle 6 de `../../ableton-live-session/SKILL.md` : pas de nouvel effet natif de Live dans les chaînes de mix. Tolérés : instruments natifs, Auto Filter déjà posé sur une piste MIDI, Utility (mono, trim, phase), Compressor en sidechain déjà en place, Hybrid Reverb sur un retour. Plug-ins : `../../effets-plugins/SKILL.md`, `../../effets-plugins/references/fiches.md`, `../../mixage/references/outils.md`.

| Natif filmé (vidéos) | Dans le projet |
|---|---|
| EQ Eight, EQ Three, Channel EQ (BH-01, BH-05, TE-02, RA-01, AF-02, DS-02, DS-05) | Pro-Q 4 (M/S, dynamique, natural phase ; fenêtre seulement) ou REQ 6 (paramètres exposés). |
| Glue Compressor (BH-05, HC-04, TH-03, TH-04, TE-06, RA-06, FB-02, DM-01, DB-03, DS-05, AF-02…) | bx_glue (Threshold, Ratio, Attack, Auto Release, filtre sidechain, Mono Maker, Mix) ; API-2500 ; Waves SSLComp (repéré). Glue en clipper (BH-02, DS-05, TE-05) : RazorClip, modèles à identifier (interp.). |
| Compressor (TE-02, AF-02, DM-01) | Toléré s'il sert de sidechain déjà en place ; sinon API-2500 ou Pro-C 3 en sidechain externe (`diagnostic-et-recettes.md`, recette A). |
| Saturator, Erosion, Overdrive, Roar, Amp, Pedal, Color Limiter (TE-01, TE-02, TE-03, TE-05, RA-02, DM-01, DS-01) | J37 pour la couleur ; RazorClip pour l'écrêtage (à vérifier) ; Kramer Tape, Trash, Abbey Road Saturator (repérés). Couleur différente (interp.). |
| Utility (HC-06, TE-06, DM-01, AF-02) | Toléré : mono, polarité, trim. Largeur automatisée (TH-01, DB-03) : Ozone Imager 2, Width exposé (interp.). Grave mono : aussi bx_glue Mono Maker. |
| Multiband Dynamics, OTT (BH-05, AF-02, DS-03 ; OTT d'Xfer en FL) | Waves C4, C6, LinMB (repérés, non fichés : prober). Pro-MB non repéré. OTT d'Xfer : présence non vérifiée. |
| Limiter (TE-01, AF-02) | L2 en fin de BUS MASTER 3 ; L4 en True Peak (à prober) ; mesure par Insight 2 ou WLM Plus en bout de Main. |
| Drum Buss (TE-02, RA-02, FB-03, DM-03, DS-01) | Pas d'équivalent fiché ; (interp.) J37 ou RazorClip, API-2500 ; aucun transient shaper tiers repéré. |
| Auto Filter (DB-03, DS-03) | Toléré s'il est déjà sur une piste MIDI ; sur un bus, automation de REQ 6 (`../../live-automation/SKILL.md`). |
| Reverb, Convolution Reverb (TE-03, RA-02, AF-02, DS-01) | Hybrid Reverb sur un retour (toléré) ou ValhallaVintageVerb (paramètres exposés). |
| Auto Pan, Echo, Filter Delay, Chorus (TE-01, RA-06, DM-01, DM-03, AF-02, DS-01) | Auto Pan : ShaperBox 3 (interp.). Delay : H-Delay (à prober). Chorus : aucun équivalent fiché. |
| Spectrum, Envelope Follower, Frequency Shifter (RA-02, AF-02, TE-02, DM-03) | SPAN (`diagnostic-et-recettes.md`, recette G). Bande dynamique de Pro-Q 4 en sidechain externe, ou TDR Nova. Accord du kick : transposer le sample dans Simpler (interp.). |

- Sidechain volumique filmé (LFO Tool, Kickstart, Volume Shaper, Duck Buddy, OneKnob Pumper) : ShaperBox 3 est repéré (fenêtre) ; sinon Compressor de sidechain déjà en place ou API-2500.
- Plug-ins filmés et repérés sur le Mac (fichiers présents, fonctionnement non testé) : Pro-Q 4 (pour Pro-Q 2/3), Pro-C 3 (pour Pro-C 2), soothe3 (pour soothe2), J37, L3, Kramer Tape, Vitamin, C6, F6, S1 Imager, Ozone Imager, SPAN, ValhallaVintageVerb, ShaperBox, PuigTec, dbx-160, CLA-2A, API-550/560. Ozone 8/9/11 filmés : seules Ozone 12 et 11 Elements sont repérées.
- Présence non vérifiée : Pro-L / Pro-L 2 et Pro-MB (non repérés), Decapitator, Saturn 2, KClip, GClip, StandardCLIP, JST Clip, Oxford Inflator, Kickstart, LFO Tool, OTT, Neutron, Gullfoss, Trackspacer, Metric AB, bx_digital V3, Transpire, Saturate, Camel Crusher, CamelPhat, iHeartNY, RVox, Fresh Air, CLA Vocals, Alloy, Rift, Youlean.
- « Mixer dans un limiteur » (TH-02, DB-02, DB-04) : ici, le limiteur reste en fin de BUS MASTER 3 et la REF part vers le Main hors limiteur.
- La règle « sub et basse médium dans deux instruments, sub mono » d'AGENTS.md rejoint BH-03, HC-02, DM-01, DB-05 et DS-03 ; accord et phase : `../../kick-bass-equilibre/SKILL.md`. Les gestes de kick du corpus ne remplacent pas la signature du kick sous 124 BPM : à tester en contexte. Aucune vidéo ne montre Maschine.

## Limites

- **Captures non faites.** Chaque fiche du corpus liste ses points « À vérifier à l'écran ». Aucun réglage d'écran n'est confirmé.
- **Transcriptions automatiques** partout ; TE-03 très bruitée. Points [ASR ?] : « bass ism », « 80 heads why 1 and a half » (BH-01) ; « minus 60 b », « 1.3 » (BH-06) ; release « 0.05 » (TH-02) ; « 0.10 », « 80b » (TH-03) ; « minus 60b » (TE-06) ; « 50 dBs » (DM-01) ; « 1,5 bars » (RA-05) ; « minus six », « −2 » (FB-01) ; « 410,000 Hz » (DB-01) ; « one 15 », « −16 to4 » (DS-04) ; échelle « 34–38 » (DS-03) ; noms de plug-ins (« Infinite », « night shine », « S-turn »).
- **Unités floues.** Beaucoup de niveaux sont dits sans préciser fader, crête ou RMS (DB-03 « −18 », DS-06, RA-03). Ne pas les recopier comme des dBFS.
- **DAW autres que Live** : 27 vidéos sur 60. Maximus, Fruity Limiter, Fruity Balance, Soundgoodizer, Edison n'ont pas d'équivalent direct ; seule la logique se transpose.
- **Contradictions entre vidéos.** Compresseur sur le kick : non (BH-01, DM-01, DM-02, TE-05) ou oui (TE-02, TE-06, DS-06). Coupe-bas du kick : aucune (HC-02), 20–25 Hz (HC-01, HC-03, DM-02), 40 Hz (DM-01), 60 Hz (DB-06). OTT après la reverb (FB-01, FB-04) ou multibande avant (FB-06). Top-down (HC-01, HC-04, FB-05, DS-02) ou depuis le kick (HC-06, FB-03). soothe déconseillé (DM-04) ou utilisé (TH-01, AF-01, DB-06). EQ en solo d'abord (FB-06) ou jamais (FB-03, AF-01, DB-05). Sidechain indispensable (RA-04, DM-02, DS-03) ou presque inutile (HC-06).
- **Contradictions avec les skills du projet.** Mono jusqu'à 140–200 Hz ici ; `../../ingenieur-mixage/SKILL.md` dit sub mono ≤ 110 Hz et largeur au-dessus de 120 Hz ; `genres-et-espace.md` refuse une fréquence universelle. Plafonds de −0,1 à −0,3 dB (RA-03, DM-04, BH-05, HC-02) contre −1,0 dBFS et ≤ −1 dBTP dans ingenieur-mixage et la recommandation Spotify de `mastering-streaming-et-club.md`. Sonies de −1,2 à −8,5 LUFS, plus fortes que l'indicatif club (−9 à −7) d'ingenieur-mixage. Top-down contre la hiérarchie « source d'abord, bus et master en dernier » de `../SKILL.md`. Stems normalisés à l'export (DB-03) contre l'export sans normalisation de `../../live-export-wav/SKILL.md`. `genres-et-espace.md` ne couvre que Bass House, Future Rave, Tech House et Minimal.
- **Rien n'a été entendu.** « Punchy », « muddy », « boomy » sont les mots des vidéos. Les tests d'écoute reviennent à l'utilisateur. La mesure aussi : export analysé, LUFS et true peak lus dans Insight 2 ou WLM Plus (`../../mastering-outils/SKILL.md`).
- **Manques du corpus.** Une seule vidéo en français. Bass house : aucun artiste de référence, mixdowns surtout de 2020. House classique : ni voix soulful ni basse 303, une seule cible LUFS. Tech house, deep / minimal, future bass, afro : aucune LUFS dite. Techno : pas de mixdown hard techno complet. Rave : élargi au UK hardcore. Afro house : deux vrais mixdowns ; deux vidéos sans transcription à voir à l'écran (62o-tvJMwvo, iwXOO2UXEiU). Drum and bass : peu d'Ableton, pas de liquid chiffré. Dubstep : ni UK 140 ni melodic, riddim couvert par une vidéo amateur.
