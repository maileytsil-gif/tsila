# Mixage et mastering « pro » : synthèse de 47 tutoriels

Synthèse du 06/10/2026 du corpus `tutoriels-mix-master-pro.md` : 48 fiches pour 47 vidéos YouTube, huit thèmes × six. Chaîne de mastering (CM), loudness et limiteur (LO), équilibre tonal et mid/side (TO), mixdowns commentés par des pros (MX), bas du spectre (BA), références et écoute (RE), pré-master et stem mastering (PR), outils pros (OU). RE-06 et MX-02 sont la même vidéo : elle est traitée une fois dans les références, et son mixage complet dans MX-02.
L'étude a été faite dans Claude in Chrome sur le Mac. Les transcriptions ont été lues, son coupé : **rien n'a été entendu**. Aucune capture d'écran n'a été faite : chaque fiche liste ses minutages « à vérifier à l'écran », et aucun réglage d'écran n'est confirmé.
Les identifiants sont ceux de `tutoriels-mix-master-pro.md`. Les préfixes BH, HC, TE, RA, FB, DM et AF désignent d'autres corpus (kicks, `../../../producteur-rythmique/modules/drums-signature/references/kicks-serum-tutoriels.md`) ; MX, TO, BA, RE, PR, OU, CM, LO sont propres à celui-ci. Les vidéos de `../../mixer-house-professionnel/references/tutoriels-mixage-par-style.md` (DB-03, DS-04…) n'y figurent pas.
[SOURCE XX-nn] = dit dans la vidéo (transcription ou description). (interp.) = interprétation de l'étude ou de cette synthèse. [ASR ?] = transcription automatique douteuse. « Présence sur le Mac non vérifiée » = outil cité par une vidéo, absent de l'inventaire `../../effets-plugins/references/fiches.md` et de `inventaire-local.md`.
Les niveaux et les durées sont ceux que disent les vidéos : des points de départ, pas des normes. Cadre du projet : `../../../SKILL.md`, `../../live-mix-mastering/GUIDE.md`, `../../mixage/GUIDE.md`, `notes-locales.md`, `mesures-et-livraison.md`.
Rédaction : quatre sections de deux thèmes chacune, relues ensuite ; les valeurs et les règles du projet citées ont été contrôlées **par échantillon** contre le corpus et contre les skills, pas une à une. Les contradictions les plus importantes sont réunies dans le tableau ci-dessous.

## Ce que dit le corpus avant tout

- **Comparer à niveau égal, toujours.** Le plus fort paraît meilleur : 0,1 dB d'écart peut fausser la préférence [SOURCE RE-01] ; référence baissée plutôt que mix poussé dans un limiteur [SOURCE RE-01, RE-02] ; bypass à niveau compensé en début et en fin de chaîne [SOURCE CM-01] ; gain match pendant le travail, compensation au dernier limiteur [SOURCE PR-06].
- **La référence ne passe pas par le traitement du master** : vers les sorties d'écoute, ou dernier insert post-fader, ou bus hors master [SOURCE RE-01, RE-02, RE-03]. Un limiteur sur le master pendant le mix donne un mix qui ne marche qu'écrasé [SOURCE RE-03].
- **Réparer avant de colorer, et par petits gestes.** Résonances d'abord, non-linéaire ensuite [SOURCE CM-01] ; 1 à 2 dB par étage [SOURCE CM-04, CM-06] ; au-delà de ≈ 4 dB de réduction un limiteur se dégrade, à 5-6 dB et plus apparaissent IMD, aliasing et pompage [SOURCE CM-01, LO-02].
- **Les pics isolés se traitent au mix, pas au master** : 2-3 échantillons, ≈ 2 dB au-dessus, tous les 4 à 7 temps [SOURCE LO-02] ; clipper par piste puis par bus, limiteur ensuite [SOURCE LO-03, OU-02]. Le hard clip est souvent le plus transparent sur les transitoires, le limiteur préféré sur le grave et les sons tenus [SOURCE LO-03].
- **Le grave se teste, il ne se décrète pas.** Mono du grave à vérifier sur la crête gagnée [SOURCE BA-04] ; alignement de phase kick/basse après le traitement de la basse [SOURCE BA-03] ; traduction par harmoniques plutôt que par plus de sub [SOURCE BA-02, RE-04] ; la décision finale est auditive [SOURCE BA-01] : elle revient à l'utilisateur.
- **La marge de pré-master est contestée.** −6 dB de crête demandés par la plupart [SOURCE PR-02, PR-04, PR-05] ; sans importance en 32 bits flottants selon PR-03, qui admet deux réserves (24 bits fixe, étages non linéaires). Le projet tient une position intermédiaire (tableau ci-dessous).
- **Le LUFS dépend du genre et du spectre** : DnB −6 à −4 (−5 choisi) [SOURCE LO-01] ; house commerciale ≈ −5,6 à −9, underground ≈ −12 [SOURCE LO-05] ; un titre à −5 LUFS demande déjà de la distorsion harmonique [SOURCE OU-02]. Le true peak d'un master du commerce dépasse 0 (+1,6 à +2,4 dBTP) [SOURCE LO-04].
- **Le stem mastering est un entre-deux** : plus de contrôle qu'un master stéréo, moins qu'un mix [SOURCE PR-05, PR-06] ; à annoncer comme tel, car il sort du périmètre d'un master stéréo.
- **Ce que le corpus n'a pas** : aucun LUFS ni true peak mesuré sur un export, aucune calibration SPL montrée en direct, aucun master house ou dubstep par un ingénieur reconnu, aucun mixdown de Chris Lake, Fred again.. ou d'un ingénieur de Skrillex.

## Chaîne de mastering complète

Six vidéos : CM-01 (Incidence Studio, techno, vinyle), CM-02 (Break, DnB), CM-03 (Zen World, tech house), CM-04 (STRANJAH, DnB), CM-05 (BassTi, dubstep), CM-06 (Cerky, électro, chaîne hybride, en français). Transcriptions lues, son coupé : **rien n'a été entendu**, les adjectifs sont ceux des vidéos. Aucune capture d'écran. [SOURCE XX-nn] = dit ; (interp.) = lecture de l'étude ; [ASR ?] = transcription douteuse. CM-01 (titre destiné à 012 et au vinyle) et CM-03 (master accepté par le label) portent sur des masters réels ; CM-03 dit ne pas être ingénieur de mastering ; CM-04 se dit « pas une autorité » ; CM-05 et CM-06 sont des producteurs ; CM-02 est une démonstration sur un titre de l'orateur.

### Ce que le corpus retient

- **Réparer avant de colorer.** On retire d'abord l'indésirable (résonances), puis seulement les traitements non linéaires [SOURCE CM-01, 13:41]. Le déséquilibre gauche/droite est corrigé avant l'exciter et le saturateur, qui réagiraient différemment à gauche et à droite [SOURCE CM-01, 3:08–4:17].
- **Peu de réduction au limiteur.** « N'importe quel limiteur commence à se casser au-delà d'environ 4 dB de réduction » ; CM-01 gagne ≈ 5 dB de headroom en abaissant les crêtes à la main, à l'échantillon, plutôt qu'au clipper [SOURCE CM-01]. CM-04 vise 1–2 dB sur la dynamique et ≈ 1 dB de clip [SOURCE CM-04].
- **Plusieurs petits gestes plutôt qu'un gros.** CM-04 : SSL de mastering à 0,5–1 dB, Ozone Dynamics à 1–2 dB, clipper ≈ 1 dB [SOURCE CM-04]. CM-06 : trois clippers étagés (1–2 dB à l'entrée, ≈ 1 dB, un avant les limiteurs) puis deux ou trois limiteurs à gain modéré [SOURCE CM-06].
- **Comparer à niveau égal, en permanence.** Perception AB en bypass à niveau compensé au début et à la fin de chaque chaîne [SOURCE CM-01, 14:50] ; sortie d'EQ abaissée de −0,2 dB et de bx_digital de −0,6 dB pour comparer [SOURCE CM-04] ; bouton 1:1 du Pro-L 2 pour juger sans biais de volume [SOURCE CM-03].
- **Grave mono, aigus plus larges, Side contrôlé.** Tout sous 200 Hz en mono, bandes de plus en plus larges vers l'aigu [SOURCE CM-03] ; mono maker sous 111 Hz [SOURCE CM-04] ; basse en mono, aigus les plus larges, mode phase linéaire « très important » [SOURCE CM-05] ; corrélation du bas vérifiée pour un mono propre au vinyle [SOURCE CM-01].
- **Le vinyle impose des limites aiguës.** Information du Side au-dessus de 8 kHz problématique au pressage [SOURCE CM-01, 26:10–29:30] ; aigus extrêmes = problème au tour de gravure, livrer un prémaster un peu terne plutôt que trop brillant [SOURCE CM-02, 6:12 et 13:37–15:53].
- **Le limiteur ne sert pas qu'à monter le niveau.** Un limiteur final à curseur clip/limit réglé entre les deux : 100 % clip = distorsion sur les kicks, 0 % limiteur = le groove bouge [SOURCE CM-01, 53:47–55:40]. Chaque limiteur a son caractère (Pro-L « rond », Maximizer « net mais blocky », UAD « mou », Oxford « petite brillance ») [SOURCE CM-02, 19:21–21:20].
- **Une chaîne de mastering ne remplace pas le mix.** CM-05 : mix « aussi propre et fort que possible », un seul clipper sur le master, contre le multibande, « le mastering est surestimé » [SOURCE CM-05, 1:32–2:20]. CM-02 : multibande sur le haut « sans trop toucher la dynamique voulue par le producteur » [SOURCE CM-02, 18:11].
- **Gain après le limiteur pour la narration.** Automation Utility −1,5 dB juste avant le drop, placée après le limiteur pour ne pas le pousser [SOURCE CM-01, 1:02:02] ; Utility après les limiteurs, volume baissé sur les breaks pour que le drop frappe [SOURCE CM-03, 28:20–29:25] ; largeur automatisée vers ≈ 70 % en fin de montée [SOURCE CM-05, 2:26].

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Seuil de dégradation du limiteur | « au-delà d'environ 4 dB de réduction de gain » | CM-01 |
| Prémaster brut | crêtes proches de 0, corps du morceau vers −6 | CM-01 |
| Réduction manuelle des crêtes | crête −1,28 ramenée vers −7 ; ≈ 5 dB de headroom ; 14 min, destructif | CM-01 |
| Écart de canaux | canal droit ≈ 0,33 dB plus faible ; Gain RX sur le gauche « −1.35 » [ASR ?] | CM-01 |
| Exciter / Side | bande ≈ 200–500 Hz sur le Side puis bande dans le Mid ; automation de gain ≈ 5 dB dans le Side | CM-01 |
| Limiteur final | plafond −1 dBFS, gain de sortie 0, curseur clip/limit intermédiaire ; « minus 78 left » [ASR ?] | CM-01 |
| Gain avant drop | Utility −1,5 dB, après le limiteur | CM-01 |
| Niveau visé (Break) | « fort mais pas écrasé » vers « −5 RMS » (mètre non précisé) ; certains titres à « −1 RMS » | CM-02 |
| Mauvaise version (démo) | limiteur ≈ 1 dB de réduction ; multibande sur le kick vers « 120 Hz » [ASR ?] ; creux ≈ 140 Hz ; pics d'aigus 10–12 kHz | CM-02 |
| Corrections du haut | BAX en M/S : Side +1 ou 2 dB ; De-Esser vers 6–7 kHz ; creux 5–6 kHz souvent laissé | CM-02 |
| Coupe-bas début de chaîne | phase linéaire ; prudence même à 20 Hz en bass music | CM-02 |
| Cible et prémaster (tech house) | cible « −6.9 LUFS » ; crêtes ≈ −6 dB ; break moyen −12 à −6 dB | CM-03 |
| Mono (tech house) | tout sous 200 Hz en mono ; Stereoize évité (effet Haas) | CM-03 |
| Compresseur type SSL | attaque 1–3 ms (jusqu'à 10), release auto, ratio 2:1 ou 4:1 (« la plupart du temps 4:1 »), jusqu'à ≈ 4 dB | CM-03 |
| Limiteurs en série | au-delà de −8 LUFS : 2 × Pro-L 2, le 1er True Peak, suréchantillonnage 4x, lookahead court, style Punchy ; le 2e preset « Bring out the beat (loud) » | CM-03 |
| Résultat | ≈ −7 LUFS (variations −6,8 à −8) | CM-03 |
| Autres valeurs | bx_digital : clap 2,49 kHz, manque 2–5 kHz ; Match EQ montant « 19 » (une instance break, une drop) | CM-03 |
| Prémaster et niveaux | WAV 24 bits, 44,1 kHz ; 0 VU ≈ −18 dBFS ; +1 dB en entrée ; référence ≈ −8 LUFS | CM-04 |
| Maximizer | Ozone 9 IRC IV Modern, seuil −7, plafond −0,1 ou −0,2 dB | CM-04 |
| EQ et mono | AMEK : shelf > 3,5 kHz +0,9 dB, cloche 2,4 kHz +0,7 dB, largeur ≈ 120, mono maker < 111 Hz ; BAX : shelf +1,5 dB dès ≈ 7,1 kHz, coupe-haut 70 (ou 28) kHz, low-shelf 84 Hz | CM-04 |
| bx_digital V3 | Presence +1,3, Bass shift +0,3, shelf aigu −1,5 dB, sortie −0,6 dB | CM-04 |
| Dynamique | SSL 0,5–1 dB ; Ozone Dynamics : sidechain passe-haut, 2:1, attaque 75 ms, release ≈ 100 ms, 1–2 dB, makeup +1,5 dB | CM-04 |
| Clipper ; export | ≈ 1 dB de clipping ; export WAV 16 bits / 44,1 kHz | CM-04 |
| Dubstep | largeur ≈ 70 % en fin de montée ; un clipper (Saturate, défauts, sans drive) ; Pro-L 2 Aggressive facultatif ; LUFS non dite | CM-05 |
| Électro hybride | clipper d'entrée 1–2 dB ; clipper ≈ 1 dB ; bas jusqu'à ≈ 150 Hz ; shelf d'air « à partir de 17 » (kHz ? interp.) ; LUFS final non dit | CM-06 |

### Ordre de la chaîne (tel que dit ; le reste est l'ordre du fil de la vidéo, donc interp.)

- **CM-01** : RX De-clip/stats → gain de canal → crêtes à la main → true:balance sur courbe cible perso → Pro-Q 4 (résonances, natural phase) → charley dynamique → bell Side → Michelangelo → Ozone Low End Focus (Punch), **placé avant** Shadow Hills → Exciter M/S suréchantillonné → Basslane → limiteur clip/limit (−1 dBFS) → Utility **après** le limiteur [SOURCE CM-01]. Le Shadow Hills Class A (mode Digital, transformateur Steel/Iron) ne réduit presque pas le gain [SOURCE CM-01, 33:53–36:30].
- **CM-03** : Imager en tête → BASSROOM (2 références) → Exciter → EQ **après** la saturation → Gullfoss → compresseur → Match EQ **avant** le limiteur → Pro-L 2 n°1 → Pro-L 2 n°2 → Utility après [SOURCE CM-03]. Les positions de Gullfoss, du compresseur et de Match EQ entre eux ne sont pas dites (interp.).
- **CM-04** : limiteur posé dès le départ en fin de chaîne (« astuce de Break ») ; ensuite AMEK, bx_digital, Pro-MB 2 bandes (facultatif), Kramer HLS, BAX, Shadow Hills (couleur seule), SSL, Ozone Dynamics, clipper [SOURCE CM-04]. Position du clipper par rapport au Maximizer non dite.
- **CM-02** : limiteur en premier pour se placer au niveau final, puis correction de ce que la limitation révèle [SOURCE CM-02, 21:52] ; passe-haut/passe-bas en début de chaîne [SOURCE CM-02, 29:40]. « En premier » est ambigu : à lire comme CM-04, limiteur actif dès le début, en fin de chaîne (interp.).
- **CM-06** : clipper → color box (EQ, compresseur optique, spatialisation, Silk) → compresseur de bus → 2e color box (stéréo) → EQ elysia → convertisseur → clipper → multibande parallèle → 3e clipper → Vintage Limiter (Modern) → Maximizer en soft clip → limiteur « de couleur » → dernier limiteur [SOURCE CM-06]. Matériel analogique : sans équivalent dans le projet.
- **CM-05** : EQ → processeur stéréo multibande (phase linéaire) → Saturate (soft clip) → Pro-L 2 [SOURCE CM-05, ordre d'exposé] ; Stereo Tool au 6:43 (« centre fort, côtés très larges ») : rôle non précisé, sans doute un contrôle (interp.).

### Écarts et contradictions

- **Clipper : refusé ou central.** CM-01 refuse de dompter les crêtes au clipper (distorsion harmonique) ; CM-05 en fait le seul traitement du master ; CM-06 en met trois ; CM-04 vise ≈ 1 dB.
- **Multibande.** Contre sur le master (CM-05) ; si nécessaire sur le haut (CM-02) ; Pro-MB 2 bandes à sauter si on ne le maîtrise pas (CM-04) ; en parallèle comme compression ascendante (CM-06).
- **Phase de l'EQ.** Natural phase retenu, linéaire pour un M/S marqué (CM-01) ; linéaire en passe-haut/bas (CM-02) ; linéaire sur le processeur stéréo (CM-05).
- **Plafond.** −1 dBFS (CM-01) contre −0,1 ou −0,2 dB « contre les inter-sample peaks » (CM-04). CM-02, CM-03, CM-05 et CM-06 ne le disent pas.
- **Mono.** Sous 200 Hz (CM-03) contre sous 111 Hz (CM-04) ; CM-05 « basse en mono » sans fréquence ; CM-02 sans chiffre.
- **Sonie.** −7 LUFS atteint (CM-03), référence ≈ −8 LUFS (CM-04), « −5 RMS » sur un mètre non précisé (CM-02) : trois échelles, non comparables entre elles.

### Contradictions avec les skills du projet

- **Plafond −0,1/−0,2 dB** (CM-04) contre **−1,0 dBFS et ≤ −1 dBTP** (`ingenieur-mixage/SKILL.md`, contrôle qualité ; `ingenieur-mixage/modules/mixer-house-professionnel/references/mastering-streaming-et-club.md`). CM-01 (−1 dBFS) rejoint la règle en dBFS, sans mesure de true peak dite.
- **Mono jusqu'à 200 Hz** (CM-03) contre « sub mono ≤ 110 Hz, largeur au-dessus de 120 Hz » (`ingenieur-mixage/SKILL.md`). CM-04 (111 Hz) est à 1 Hz de la règle.
- **Sonie** : −6,9 visé et −6,8 atteint (CM-03) sont au-dessus de l'indicatif club −9 à −7 (`ingenieur-mixage/SKILL.md`) ; −7 est à la borne. Valeur indicative, à confirmer avec l'utilisateur.
- **Export 16 bits** (CM-04, 28:46) contre 24 bits sans normalisation (`ingenieur-mixage/modules/live-export-wav/GUIDE.md`). Le prémaster de CM-04 est bien en 24 bits.
- **Loudness au master** (CM-06 trois clippers et multibande ; CM-04 clipper) contre « source d'abord, bus et master en dernier » (`ingenieur-mixage/modules/mixage/GUIDE.md`) : acceptable si le mix est déjà propre ; CM-01 répare à l'échantillon un fichier stéréo, cas prévu par `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` (mix stéréo fourni) mais pas pour un Set à pistes séparées.
- **Natifs.** Seul Utility est filmé (CM-01, CM-03, CM-05) : toléré pour trim, mono, phase (règle 6, `producteur-live/SKILL.md`). La **largeur** automatisée d'Utility (CM-05) sort de cette liste : passer par Ozone Imager 2 (Width exposé).
- **Limiteur « en premier »** (CM-02) : le projet garde L2 en fin de BUS MASTER 3 (`ingenieur-mixage/modules/mastering-outils/references/notes-locales.md`).

### Dans l'installation du projet

Chaîne en place : BUS MASTER 3 = Tonal Balance Control 3 → SPAN → L2 (seuil −5,1, plafond −1,0 dBFS, ARC) ; Main = Utility 0 dB → Insight 2 ; REF → Main hors limiteur (`notes-locales.md`). Un seuil de L2 à −5,1 ne dit pas la réduction réelle : à lire sur le mètre, à comparer aux ≈ 4 dB de CM-01 (interp.).

| Outil de la vidéo | Équivalent dans le projet | Statut |
|---|---|---|
| Pro-Q 4 (CM-01) | Pro-Q 4 (résonance, dynamique, M/S, natural phase) | repéré, fenêtre seulement (`fiches.md`) |
| true:balance, Match EQ, BASSROOM, Perception AB | Tonal Balance Control 3 pour la courbe cible ; REF vers Main hors limiteur pour l'A/B | outils des vidéos : présence sur le Mac non vérifiée |
| Pro-L, Pro-L 2, Ozone Maximizer, Oxford, UAD Precision, « Limit One » | L2 (réglages exposés, ARC, Quantize, IDR) ou L4 (Clip, Over Sampling x2–x16, Ceiling ; True Peak non exposé) | Pro-L / Pro-L 2 : non repérés ; L2 et L4 repérés ; L4 en True Peak « à prober » |
| Clippers (CM-04, CM-05, CM-06), Saturate | RazorClip (GAIN 0–24 dB, OUTPUT, MIX, MODEL, BYPASS) ; Saturate : présence non vérifiée | RazorClip repéré, MODEL à identifier |
| Compresseur type SSL, SSL de mastering, Shadow Hills | SSLComp (repéré), bx_glue, API-2500 | Shadow Hills, UAD : présence non vérifiée |
| Ozone Dynamics, Exciter, Low End Focus, Match EQ | Ozone 12 Elements et 11 Elements repérés | modules cités non vérifiés dans ces éditions |
| Ozone Imager (CM-03), processeur stéréo, Stereo Tool | Ozone Imager 2 (Width, Stereoize exposés) ; mono maker de bx_glue | Imager 2 repéré ; « M stereo processor » : à lire |
| AMEK EQ 200, BAX, bx_digital V3, Acustica Sontec, elysia | REQ 6 (exposé), Q10, PuigTec ; bx_digital : présence non vérifiée | AMEK, BAX, elysia, Acustica : non vérifiés |
| Pro-MB, multibande | Waves C4, C6, LinMB (repérés, non fichés : prober) ; Pro-MB non repéré | à prober |
| Kramer HLS, saturation | J37 (exposé), KramerTape, Abbey Road Saturator ; « Kramer HLS » : non vérifié | à vérifier |
| Basslane, Gullfoss, Michelangelo, RX | aucun équivalent fiché | présence sur le Mac non vérifiée |
| Mesure LUFS/TP | Insight 2 en bout de Main ; WLM Plus (paramètres à relever) ; SPAN | repérés ; FFmpeg absent |

- Gain après limiteur (CM-01, CM-03) : le Utility du Main (0 dB) est déjà après BUS MASTER 3 ; son gain peut recevoir l'automation (`producteur-live/modules/live-automation/GUIDE.md`) sans toucher au plafond (interp.). Une atténuation seule ne monte pas la crête.
- Gain staging des valeurs de CM-04 (0 VU ≈ −18 dBFS) : aucun VU calibré dans l'inventaire ; ne pas recopier.

### Limites

- Valeurs [ASR ?] : « −1.35 » et « minus 78 left » (CM-01) ; multibande « 120 Hz » (CM-02) ; shelf d'air « à partir de 17 » (CM-06) ; noms d'outils (« Limit One », « Kramer HLS » lu « creamer »).
- Aucune vidéo ne donne un LUFS final pour CM-01, CM-05, CM-06 ; CM-02 donne des RMS sur un mètre non précisé.
- Aucun true peak chiffré dans ce thème : le plafond dit ne prouve pas le true peak (`ingenieur-mixage/modules/mastering-outils/references/mesures-et-livraison.md`).
- Tous les outils de CM-01 à CM-04 hors Pro-Q 4, Ozone Imager, SSLComp, API-2500, J37 sont des outils du Mac **non vérifiés** ; aucun n'a été chargé ni réglé.
- CM-06 : peu de chiffres à l'oral, matériel analogique non identifié (« à vérifier à l'écran »). Pas de master house classique ni dubstep par un ingénieur reconnu (manque du corpus). Les vidéos écartées du corpus ne sont pas reprises.

## Loudness, clipping et limiteur

Six vidéos : LO-01 et LO-02 (Warp Academy, DnB puis genre non nommé), LO-03 (Zerotonine, clip contre limiteur), LO-04 (Strob, true peak, en français), LO-05 (Olean's House, house), LO-06 (Joachim Garraud, en français, conférence). Lu sur transcription, rien entendu : « gel », « hot garbage », « distorsion plaisante » sont les jugements d'écoute des orateurs, pas les nôtres. LO-06 contient des affirmations historiques « à vérifier ».

### Ce que le corpus retient

- **La sonie utile est un compromis par style.** Pour un titre DnB, la zone dite est −6 à −4 LUFS, −6 le plus propre, choix final −5 [SOURCE LO-01, 13:19–17:07] ; −8 à −5 LUFS dans les drops, tous genres [SOURCE LO-02, 0:18] ; house commerciale ≈ −5,6 à −9 LUFS, underground ≈ −12 [SOURCE LO-05].
- **Mesure sur le drop, pas sur l'intégré seul.** LO-01 mesure l'intégré sur le drop [SOURCE LO-01, 1:52–2:25] ; LO-05 oppose LUFS intégré et short-term à relire à l'écran [SOURCE LO-05, « à vérifier »].
- **Les défauts de la sur-limitation sont listés.** Distorsion sur le propre (sub, voix, pads), IMD (ex. 808 à 30 Hz produisant 15 Hz), batterie molle, perte de largeur et de profondeur dans le Side, dureté aiguë, drop pas plus fort que la montée [SOURCE LO-01, 5:09–9:30] ; à 5–6 dB ou plus de réduction : IMD, aliasing, transitoires ternes, pompage [SOURCE LO-02, 1:06].
- **Le coupable est souvent un pic isolé.** Pics de 2–3 échantillons, ≈ 2 dB au-dessus, toutes les 4 à 7 temps ; à traiter dans le mix (hard clip, limitation manuelle), pas sur le master [SOURCE LO-02, 11:15–14:30].
- **Hard clip, soft clip, limiteur : trois gestes.** Le hard clip est souvent le plus transparent sur les transitoires ; sur sons tenus ou graves filtrés, la distorsion du clipper s'entend, le limiteur est préféré [SOURCE LO-03, 3:30–5:05 et 16:03/20:46].
- **Clipper par piste puis limiteur final.** Kick ≈ 2 dB, clap ≈ 2 dB, synthé ≈ 4 dB de headroom gagnés ; clipper de bus +0,5 à 1 dB ; le limiteur final a « 2 dB de réduction en moins » et ≈ 3 dB à faire, contre ≈ 3,5 dB pour le limiteur seul [SOURCE LO-03, 26:05–35:52].
- **Le true peak d'un master du commerce dépasse 0.** RX Loudness Control sur des titres de Skrillex (masters de Luca Pretolesi) : +1,6, +1,9, +2,4, +2,4 dB au-dessus de 0 ; la limitation true peak est jugée rare en électro [SOURCE LO-04].
- **Le LUFS dépend du spectre.** Le LUFS monte quand voix et synthés entrent ; spectre plat commercial plus fort, « baignoire » underground plus faible [SOURCE LO-05, 12:19–14:30].
- **RMS et loudness perçue.** Le RMS n'est pas la loudness perçue ; à −16 RMS égalisé, le mix le plus dynamique paraît le plus fort ; test de nul : chaque limiteur ajoute sa propre distorsion [SOURCE LO-06, 14:44–22:00].

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Plage testée | −14 à −2,5 LUFS intégrés (mesure sur le drop) ; gel vers −8, mieux à −6 ; −2,5/−3 « hot garbage » | LO-01 |
| Zone pour ce titre DnB | −6 à −4 ; −6 le plus propre ; choix final −5 ; −4 : distorsion sur la voix lead, craquements au Side seul | LO-01 |
| Grammy 2024 (Skrillex/Flowdan/Fred again..) | « un peu moins fort que −6 » dans le drop (affirmation de l'orateur, non mesurée dans le corpus) | LO-01 |
| Zone « loud » | −8 à −5 LUFS dans les drops et refrains | LO-02 |
| Limitation acceptable ou non | quelques dB, ≈ 3 dB acceptable ; 5–6 dB ou plus : IMD, aliasing, pompage | LO-02 |
| Cas d'étude | mix d'origine ≈ −14 LUFS dans le drop, re-mix ≈ −11 ; avec ≈ 3 dB de réduction chacun : −8,9 LUFS pour l'original | LO-02 |
| Pics isolés | 2–3 échantillons de long, ≈ 2 dB au-dessus, toutes les 4–7 temps | LO-02 |
| Clipping inaudible | 2–3 dB « généralement » ; limiteur seul ≈ −3,5 dB de réduction | LO-03 |
| Clip par piste | kick ≈ 2 dB, clap ≈ 2 dB, synthé ≈ 4 dB ; bus +0,5 à 1 dB ; limiteur final : 2 dB de réduction en moins, ≈ 3 dB restants à faire | LO-03 |
| StandardCLIP ; suréchantillonnage | hard clip, OS 8x, mode ratio 2:1 (compresse 50 % puis clippe) | LO-03 |
| True peak de titres (Skrillex) | +1,6, +1,9, +2,4 (« Joker »), +2,4 (« Ratata ») dB | LO-04 |
| Baisse pour TP = 0 | −2,4 dB de gain → TP 0,0, soit 2,4 dB de loudness perdus | LO-04 |
| Cible plateforme | Spotify −14 LUFS et −1 dBTP : « s'adresse aux distributeurs, pas aux ingénieurs mastering » | LO-04 |
| House commerciale (LUFS / RMS) | −8,55 / −9,0 ; ≈ −8,8 à −9 / −10 ; −10,3 / −11,2 ; −6,7 / −8 ; Fisher −5,6 / −7 | LO-05 |
| Underground, chill, long kick (LUFS / RMS) | Bandcamp −11,7 / −11,6 ; chill −10 / −11,5 ; kick et basse longs −8,5 / −10 | LO-05 |
| Cibles proposées (house « bouncy ») | −10 RMS et −9 LUFS ; moins en chill, plus avec basse et kicks longs | LO-05 |
| Rééditions vinyle | −11,8 / −11,7 et −13 / −13 : « trop faibles » | LO-05 |
| Dynamique (histoire) | 1924 : 60 dB, 0,3 % de distorsion ; aujourd'hui ≈ 12 dB, jusqu'à 20 % (ordre de grandeur de l'orateur) | LO-06 |
| Égalisation des mix | jazz −16 RMS, deuxième −9 RMS, troisième très compressé, ramenés à −16 RMS (« −14 comme Spotify ») | LO-06 |
| VU | calibré (ex. −12 dB), mixer autour de 0 VU | LO-06 |

### Procédure ou ordre (quand la vidéo la donne)

- **Test de sonie à l'aveugle** [SOURCE LO-01, 1:52–2:25] : rendre le même mix de −14 à −2,5 LUFS, mesurer sur le drop, normaliser tous au même niveau, écouter ; contrôler le Side seul (MSED), le passe-bas pour le bas, la montée contre le drop. (Copies d'écoute : aucun export de livraison n'est normalisé.)
- **Comparaison de deux limitations** [SOURCE LO-02, 3:24–4:05] : deux mix à 0 dBFS sample peak, même chaîne copiée, seuil ajusté pour une réduction de gain identique ; comparer ensuite le LUFS atteint.
- **Gain staging par clipping** [SOURCE LO-03, 28:23–35:52] : clip par piste (kick, clap, synthé), clipper de bus, puis limiteur final avec 2 dB de réduction en moins. L'ordre dit est piste → bus → limiteur.
- **Mesure TP** [SOURCE LO-04] : RX Loudness Control hors ligne ; gain négatif jusqu'à TP 0,0, avec perte de loudness équivalente.
- **Contrôle d'un titre à rejouer** [SOURCE LO-05, 14:42–16:10] : si le master est trop faible, refaire un master (limiteur + EQ) avant de le jouer en club ; les crêtes peuvent faire couper le sub par le système.

### Écarts et contradictions

- **Quelle sonie ?** DnB −6 à −4 avec −5 choisi (LO-01), −8 à −5 tous genres (LO-02), house −9 (LO-05) ; LO-01 dit que la DnB est plus forte que house, techno et trance. Les écarts suivent le style, non les vidéos.
- **Hard clip ou limiteur.** Hard clip souvent plus transparent sur transitoires (LO-03) ; pour le grave, le limiteur (LO-03) ; LO-02 renvoie les pics au mix et non au master.
- **True peak.** LO-04 dit que la limitation true peak est rarement activée en électro et que garder une marge rend le master moins fort ; LO-05 signale que des crêtes de master faible font couper le sub en club. Aucune vidéo ne mesure un TP sur DnB (manque du corpus).
- **RMS ou LUFS.** LO-05 donne les deux, avec un écart LUFS/RMS de ≈ 0,1 à 1,5 dB selon le titre (calcul sur les valeurs dites, interp.) ; LO-06 égalise en RMS (−16) et le rapproche de −14 LUFS : conflation des deux échelles (interp.).
- **Normalisation de plateforme.** À oublier en dance music, et désactivable (LO-05) ; la même normalisation sert d'outil de comparaison (LO-01, LO-02, LO-06).

### Contradictions avec les skills du projet

- **Plafond −1 dBTP** : LO-04 le dit destiné aux distributeurs, pas aux ingénieurs, et un master du commerce dépasse 0 dBTP (+1,6 à +2,4). Le projet impose **≤ −1 dBTP et plafond −1,0 dBFS** (`ingenieur-mixage/SKILL.md`) et cite la recommandation Spotify de moins de −1 dBTP, moins de −2 dBTP si plus fort que −14 LUFS (`ingenieur-mixage/modules/mixer-house-professionnel/references/mastering-streaming-et-club.md`). Contradiction directe, à trancher par l'utilisateur ; LO-04 n'apporte pas de mesure d'encodage.
- **Sonie** : −5 (LO-01), −8 à −5 (LO-02), jusqu'à −5,6 (LO-05, Fisher) sont plus forts que l'indicatif club −9 à −7 (`ingenieur-mixage/SKILL.md`). La cible house de LO-05 (−9 LUFS) est dans la plage.
- **Plafond d'échantillon.** L2 à plafond −1,0 ne garantit pas le true peak (`ingenieur-mixage/modules/mastering-outils/references/notes-locales.md`) : en accord avec LO-04 sur la différence entre fichier et reconstruction.
- **Source d'abord.** LO-02 (pics traités dans le mix) et LO-03 (clip par piste, crest factor bas dans le mix) rejoignent « source d'abord, bus et master en dernier » (`ingenieur-mixage/modules/mixage/GUIDE.md`) ; aucune contradiction.
- **Normalisation** : appliquée aux copies d'écoute dans LO-01/LO-02, jamais proposée à l'export ; l'export reste sans normalisation (`ingenieur-mixage/modules/live-export-wav/GUIDE.md`).
- **Natifs.** Aucun effet natif de Live n'est filmé dans ce thème (Ableton nommé seulement comme DAW dans LO-03).

### Dans l'installation du projet

| Outil de la vidéo | Équivalent dans le projet | Statut |
|---|---|---|
| Pro-L 2 (LO-03, style Aggressive), DMG Limitless (LO-02), limiteurs Ozone/FabFilter/DMG (LO-06) | L2 (Thresh, Ceiling, Release, ARC, Quantize, IDR, Noise Shaping) ou L4 (Clip, Release, Threshold, Ceiling, Over Sampling) | Pro-L / Pro-L 2 non repérés ; Limitless : présence sur le Mac non vérifiée |
| StandardCLIP, Saturate (LO-03) | RazorClip (GAIN, OUTPUT, MIX, MODEL) ; saturation J37 | RazorClip repéré ; StandardCLIP, Saturate : présence non vérifiée |
| Clip par piste et bus (LO-03) | RazorClip sur pistes (3rd-party, règle 6 respectée) ; TheBus (Threshold, Mix) pour le bus | repérés ; réglage à relire, jamais « écouté » |
| Youlean, RX Loudness Control, RX stats (LO-04, LO-05) | Insight 2 (LUFS, true peak) ; WLM Plus (paramètres à relever) | repérés ; capture nécessaire, exposition nulle |
| SPAN en RMS (LO-05) | SPAN (Mode, Avg Time) ; lecture RMS seulement | repéré, fenêtre seulement |
| Fuel (Music Hack), PSR (LO-01) | aucun équivalent fiché ; PSR : lecture dans Insight 2 non vérifiée (interp.) | présence sur le Mac non vérifiée |
| MSED (Side seul, LO-01) | Ozone Imager 2 ou SPAN en mode corrélation ; MSED : non vérifié | à confirmer |
| Test de nul (LO-06) | polarité d'une copie via Utility (toléré) ; protocole non fiché | (interp.) |
| VU-mètre calibré (LO-06) | aucun dans l'inventaire | présence sur le Mac non vérifiée |

- Suréchantillonnage : OS 8x de StandardCLIP (LO-03) ; L4 expose Over Sampling Off à x16 ; L2 : non listé (`fiches.md`).
- Mesure de réduction réelle : lire le mètre du L2/L4, pas le seuil. Le seuil −5,1 du L2 en place n'est pas une réduction chiffrée.
- Test d'écoute des cas de LO-01 (−6, −5, −4) : à faire par l'utilisateur ; l'agent peut produire les rendus mesurés (`analyze_wav.py` pour le sample peak) mais ni LUFS, ni true peak, ni écoute (règle 4, `AGENTS.md`).

### Limites

- **[ASR ?]** : titre « DJ S… » (LO-05) et styles « le dm, le dr » (LO-06) ; aucune valeur chiffrée n'est marquée douteuse dans ce thème, mais plusieurs sont des affirmations d'orateur non vérifiées : Skrillex/Grammy « un peu moins fort que −6 » (LO-01), Bob Ludwig +16 dB, TV −24 dB, 20 % de distorsion (LO-06, « à vérifier »).
- **Mesures de LO-04 et LO-05** lues à l'oral ; leur « À vérifier à l'écran » (valeurs RX, lectures Youlean intégré/short-term) n'a pas été fait.
- **Aucune cible club et streaming pour un même titre**, ni TP DnB (manque du corpus). LO-06 reste théorique ; LO-04 contient de la promo de formation.
- **Incohérence interne de LO-03** : limiteur seul ≈ 3,5 dB (27:11) contre « 2 dB en moins » puis ≈ 3 dB restants (35:52) ; non résolue sans l'écran.
- **Pas de valeur** de seuil/ratio pour StandardCLIP, Pro-L 2 Aggressive ou Limitless : « à vérifier à l'écran » (LO-02, LO-03).
- **Outils non vérifiés sur le Mac** : tous ceux marqués ci-dessus ; Pro-L / Pro-L 2 non repérés ; aucune capture, aucun réglage n'a été confirmé.
- **LUFS mesurés par les orateurs** sur des fichiers du commerce ou des extraits : ils ne remplacent pas une mesure du fichier livré (`mesures-et-livraison.md`).

## Équilibre tonal, EQ et mid/side

Six vidéos (TO-01 à TO-06), transcriptions lues, son coupé : **rien n'a été entendu**, aucune capture d'écran n'a été faite, aucun réglage d'écran n'est confirmé. Les minutages « à vérifier à l'écran » du corpus restent valables pour chaque fiche. [SOURCE XX-nn] = dit dans la vidéo ; (interp.) = interprétation ; [ASR ?] = transcription automatique douteuse. Les valeurs sont celles que disent les vidéos : des points de départ, pas des normes. Cadre du projet : `AGENTS.md`, `.claude/skills/ingenieur-mixage/SKILL.md`, `.claude/skills/ingenieur-mixage/modules/mixage/SKILL.md`.

### Ce que le corpus retient

- **Du bas vers le haut.** Si le grave et le bas-médium sont justes, il faut moins d'aigu (« un peu de poussière de fée ») [SOURCE TO-01].
- **Coupe-bas sur le Side seul, à la place d'un mono maker** : vers 80 Hz, pour un grave plus serré et plus facile à graver sur vinyle [SOURCE TO-01]. Zinn justifie le mono par les clubs : beaucoup ont un sub mono, parfois tout le système [SOURCE TO-05].
- **Coupes étroites, boosts larges** en mastering ; bandes dynamiques pour la boue après le kick (160 Hz) et pour le poids du bas-médium (240 Hz) [SOURCE TO-01].
- **L'équilibre avant le limiteur** compte plus pour le niveau perçu que d'écraser la dynamique ; l'énergie vers 1 kHz donne l'impression de volume [SOURCE TO-02]. Même logique chez Streaky : un shelf à 20 Hz retire de l'énergie avant le limiteur, qui peut alors monter plus fort [SOURCE TO-01].
- **Courbe d'isosonie** : sensibilité maximale à 500–1000 Hz et surtout 3–5 kHz, le sub est très peu perçu ; la dureté se cherche à 2–4 kHz, la boue vers 200–500 Hz ; EQ soustractive d'abord [SOURCE TO-03].
- **Cible tonale tirée des références, pas des cibles fournies** : cible personnalisée, mieux, construite sur les seuls drops consolidés des références [SOURCE TO-04]. Alt-clic pour isoler la zone coupable [SOURCE TO-04].
- **Le M/S sert à corriger mid et side différemment** : compression plus forte sur le Side que sur le Mid, filtre de détection qui coupe le grave, EQ Side resserrée et aigu ouvert, Mid avec « sparkle » [SOURCE TO-06]. Même schéma chez Streaky : shelf Mid à 1,7 kHz pour la présence, boost dynamique sur le Side pour l'air [SOURCE TO-01] ; que les deux se complètent est une interprétation (interp.).
- **Multibande de mastering à ratios différenciés** : grave et aigu plus compressés, médiums moins (l'oreille y perçoit mieux les variations), clip à la fin [SOURCE TO-03].
- **Hygiène à la réception** : Warp désactivé, headroom vérifié, ni compression ni brickwall sur le master reçu, sinon redemander un fichier [SOURCE TO-05].
- **Pas de dogme sur la brillance** : un mixdown trop brillant est à éviter, le juste milieu dépend du genre [SOURCE TO-02] ; à l'inverse, les références de TO-04 ont plus d'aigu et un grave plus creux que le template.

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Coupe-bas sur le Side seul | ≈ 80 Hz (pente non confirmée) | TO-01 |
| Low shelf | 20 Hz, −1 dB, Q remonté → bosse ≈ +0,5 dB vers 40 Hz | TO-01 |
| EQ dynamique sur le kick | ≈ 60 Hz, plage +2 dB (seuil non dit) | TO-01 |
| Creux anti-boue | 160 Hz, Q étroit, dynamique, −0,5 à −1 dB | TO-01 |
| Boost large dynamique | ≈ 240 Hz (gain non dit) | TO-01 |
| High shelf sur le Mid | ≈ 1,7 kHz, ≈ 1 dB, pente douce démarrant vers 500 Hz | TO-01 |
| Coupe spectrale (sibilance) | 5–8 kHz, large (plus haut si cymbales agressives) | TO-01 |
| Boost dynamique sur le Side | 8–10 kHz (fréquence et gain à confirmer) | TO-01 |
| Pente d'affichage de l'analyseur | bruit rose = 3 dB/oct (« un peu trop brillant ») ; lui : 4,5 dB/oct ; n'agit que sur l'affichage | TO-02 |
| Match EQ | amount 10–15 %, cible bruit rose, en cascade (bus drums, bus DnB, master) | TO-02 |
| Exemple DnB | drums ≈ +5 dB au-dessus de 0 → FX-3 + clipper, drive ≈ 1–2 dB ; basse au limiteur puis −3 dB | TO-02 |
| Résultat chiffré | −4,3 LUFS, drums + basse seuls [ASR ?] (type de mesure non confirmé) | TO-02 |
| Zones sensibles / dureté | 500–1000 Hz et 3–5 kHz ; dureté 2–4 kHz ; boue ≈ 500 Hz (pour lui 200–400 Hz) | TO-03 |
| Creux de master | 2–4 kHz si le morceau est dur (gain et Q non dits) | TO-03 |
| Multibande de master | sub ≤ 110 Hz ratio 8:1 ; > 6–7 kHz ratio 7:1 ; médiums moins compressés ; clip final | TO-03 |
| EQ dynamique maison | EQ Eight en passe-bande raide (pentes ×4) sur 2–5 kHz + Envelope Follower (« 50 » et « 0 ») sur le gain | TO-03 |
| Accent du compresseur de référence | à partir de ≈ 150 Hz, attaque lente, release rapide (hypothèse de l'auteur) | TO-04 |
| Mono bus : coupe-bas ; coupe étroite | < 30–35 Hz ; 200–500 Hz, ≈ 1–2 dB (zone trouvée au balayage) | TO-05 |
| Techno, niveau RMS ; réduction | −10 à −8 dB RMS, jamais au-delà de −8 ; ≈ 3 dB de gain réduit (même série, apQO4kzPevU) | TO-05 |
| Plafond | « minus three, minus four » [ASR ? probablement −0,3/−0,4 dBFS] | TO-05 |
| Vintage Compressor M/S | Side : gain +7,6 dB pour ≈ 3 dB de compression ; Mid : 2–2,5 dB de réduction, +2 dB de makeup | TO-06 |
| Attaque ; release | 24 ms (défaut) ; ≈ 100 ms, des deux côtés | TO-06 |
| Vintage EQ M/S | Side : coupe-bas 45 Hz, boost aigu dès 8 kHz ; Mid : boost « sparkle » très haut (fréquence non dite) | TO-06 |

Valeurs absentes : seuils des bandes dynamiques (TO-01), gains du creux de master (TO-03), fréquence du filtre de détection et du mono des graves à l'Imager (TO-06), tout chiffre en dB sur la cible personnalisée (TO-04).

### Procédures

- **Preset « dance » de Streaky** (ordre des minutages, probablement l'ordre de la chaîne, interp.) : coupe-bas Side 80 Hz → shelf 20 Hz → dynamique 60 Hz → creux 160 Hz → boost 240 Hz → shelf Mid 1,7 kHz → coupe spectrale 5–8 kHz → boost Side 8–10 kHz [SOURCE TO-01].
- **Matrice M/S dans Live** [SOURCE TO-05] : piste originale + copie en mono avec phase inversée dans Utility, sommées = Sides seuls → « stereo bus » ; copie mono sans inversion → « mono bus » ; les deux dans un « sum bus » ; copie « unprocessed » gardée pour l'A/B. Traitement : mono bus (coupe-bas puis coupe étroite 200–500 Hz), stereo bus (retrait du grave boueux en gardant le « room tone »).
- **Cible tonale par référence** [SOURCE TO-04] : groupe « reference » dont le solo coupe la chaîne de mastering (même touche) → écoute d'oreille → cible personnalisée → consolidation des seuls drops → vue Fine → alt-clic par zone → corrections (hats à monter, clap, lead à baisser).
- **Tonal avant limiteur** [SOURCE TO-02] : analyseur incliné à 4,5 dB/oct, EQ à la main jusqu'à la ligne droite, puis seulement limiteur ou clipper.
- **M/S Ozone** [SOURCE TO-06] : tape + Imager (grave mono) → Vintage Compressor M/S → Vintage EQ M/S.

### Écarts et contradictions

**Entre vidéos du thème**
- Coupe-bas du Side : 80 Hz (TO-01) contre 45 Hz (TO-06). Les vidéos écartées de ce thème en donnent 67 Hz (44VRYB4122g, rap/808) et « jusqu'à ≈ 100 Hz » (_NUXm8pslt0), hors électro. Le 30–35 Hz de TO-05 est un coupe-bas du mono bus entier, pas une fréquence de passage au mono.
- Zone de boue : 160 Hz étroit (TO-01), 200–400 Hz (TO-03), 200–500 Hz (TO-05) ; chacune est un point de départ à retrouver par balayage.
- Cible : pente générique 3 ou 4,5 dB/oct (TO-02) contre cible tirée des références (TO-04) ; TO-03 rappelle que le bruit rose n'est qu'un tilt.
- Niveau : TO-02 pousse jusqu'à −4,3 LUFS avec clip ; TO-05 parle de −10 à −8 dB RMS (RMS, pas LUFS : ne pas convertir) ; TO-06 reste à 2–3 dB de réduction.

**Contradictions avec les skills du projet**
- **Mono et largeur** : `ingenieur-mixage/SKILL.md` dit sub mono ≤ 110 Hz et largeur au-dessus de 120 Hz ; `ingenieur-mixage/modules/mixage/GUIDE.md` (étape 5) répète largeur au-dessus de 120 Hz. TO-01 laisse du Side dès 80 Hz et TO-06 dès 45 Hz : plus lâche que la règle, dans la bande 45/80–110 Hz. Aucune vidéo de ce thème ne donne de mono au-dessus de 110 Hz. Le « ≤ 110 Hz » de TO-03 est une bande de compression multibande, pas une fréquence mono : ne pas les confondre. Règle du projet à garder.
- **Plafond** : TO-05 (« minus three, minus four » [ASR ?]) contredit, s'il s'agit de −0,3/−0,4, le plafond −1,0 dBFS et la sortie ≤ −1 dBTP (`ingenieur-mixage/SKILL.md`, `ingenieur-mixage/modules/mixage/GUIDE.md` étape 9). Valeur douteuse : ne rien en tirer.
- **Sonie** : −4,3 LUFS (TO-02) est bien au-dessus de l'indicatif club −9 à −7 ; il est obtenu avec drums et basse seuls, clip compris, et sa mesure est [ASR ?].
- **Natifs de Live filmés** : EQ Eight + Envelope Follower (TO-03), Utility, EQ Eight, Saturator et Simple RMS Meter M4L (TO-05). Règle 6 d'`producteur-live/SKILL.md` : seul Utility (mono, trim, phase) est toléré ; tout le reste se traduit en tiers (tableau ci-dessous).
- **Source d'abord, bus et master en dernier** : TO-04, TO-05 et TO-06 sont des gestes de master, donc compatibles si les sources sont déjà réglées (interp.). TO-02 applique Match EQ en cascade au bus drums, au bus DnB puis au master ; la vidéo ne dit pas si les sources sont déjà corrigées, donc l'accord avec la règle du projet n'est pas établi.
- **EQ « aveugle »** : le preset de TO-01 est appliqué d'après l'oreille de Streaky ; `ingenieur-mixage/modules/mixer-house-professionnel/GUIDE.md` demande de mesurer le problème avant d'égaliser. Ne pas plaquer un preset sans diagnostic mesuré.

### Dans l'installation du projet

| Geste filmé (outil) | Outil du projet | Pilotage (`fiches.md`) |
|---|---|---|
| Pro-Q 4 : coupe-bas Side, bandes dynamiques, spectral (TO-01) | Pro-Q 4 | rien d'exposé : tout par fenêtre ; M/S non documenté dans la fiche : à vérifier ; capture obligatoire |
| EQ statique (shelf 20 Hz, creux, shelf Mid) | REQ 6 (Frq, Gain, Q, types) ou Pro-Q 4 | REQ 6 exposé ; M/S non documenté |
| EQ dynamique, EQ Eight + Envelope Follower (TO-03) | Pro-Q 4 (Make Dynamic) ou TDR Nova (EQ dynamique, installé) ; soothe3 pour la résonance | fenêtre ; soothe3 : double-clic + saisie |
| Mono bus, matrice M/S à Utility (TO-05) | Utility toléré (mono, phase) ; bx_glue Mono Maker Frequency | bx_glue exposé |
| Saturator du mono bus (TO-05) | J37 (une couleur par chaîne) | exposé |
| Imager grave mono, largeur (TO-06) | Ozone Imager 2 | Width exposé, bandes à la fenêtre |
| Limiteur / clipper avant la sortie (TO-02, TO-03) | L2 plafond −1,0 dBFS ou L4 ; RazorClip | L2 et L4 exposés ; mesure Insight 2 |
| Tonal Balance Control (TO-04) | Tonal Balance Control 3 ; SPAN moyennage 4 s | fenêtre ; REF → Main hors limiteur (`ingenieur-mixage/modules/mixage/GUIDE.md`) |
| Analyseur incliné (TO-02) | SPAN | réglage de pente d'affichage non fiché : à vérifier |

### Limites

- Pro-Q 4, soothe3, SPAN, TBC 3 et Insight 2 ne se règlent que par la fenêtre : ces chaînes ne sont reproduites que sur capture, jamais « réglées » sans preuve.
- Présence non vérifiée sur le Mac : Ozone 7 et Ozone 8 (Vintage Compressor, Vintage EQ, Match EQ) ; installés et non testés pour ces modules : Ozone 11 Equalizer, Ozone 12 Elements ; outils Bitwig (EQ+, FX-3, Reference Level, Peel), Envelope Follower et Simple RMS Meter M4L : équivalents non vérifiés. Crest factor de TBC (TO-04) : présence dans TBC 3 non vérifiée.
- [ASR ?] : plafond de TO-05, « 6 dB » et −4,3 LUFS de TO-02, noms (« Coryu », « Debukas », « Yoda's foreign »). Le « +7,6 dB » de TO-06 ne précise pas entrée ou sortie.
- TO-04 ne donne aucune valeur en dB ; TO-02 et TO-03 sont des témoignages d'auteurs non ingénieurs de mastering crédités (Polarity), ou d'un artiste dubstep (Virtual Riot). Le corpus signale l'absence d'EQ dynamique ou multibande chiffrée sur un master techno ou house réel.
- Aucune mesure de largeur (corrélation, % d'Imager) n'est donnée ; l'écoute de validation revient à l'utilisateur.

## Mixdowns commentés par des pros

Six vidéos (MX-01 à MX-06). On ne retient que des **gestes de mixage** ; aucun élément musical (mélodie, motif, paroles, enregistrement) des titres publiés n'est repris. Transcriptions lues, rien d'entendu, aucune capture. MX-01 et MX-04 portent sur le propre morceau de l'artiste ; MX-03 sur des stems d'entraînement ; MX-06 sur des boucles de démonstration, pas un morceau sorti. Les chiffres sont des points de départ.

### Ce que le corpus retient

- **Niveaux de départ bas** : drums dance à −15 dB habituellement, −12 ici [SOURCE MX-03] ; gain de canal par défaut −15 ou −10 dB, « je crois » [SOURCE MX-04] ; à l'inverse faders à 0 dB et niveau posé par un Utility par piste, pour attaquer les plug-ins à leur niveau optimal [SOURCE MX-05] ; mix reçu à 0 dB partout [SOURCE MX-02].
- **Bus drums légers** : Townhouse Bus Comp ≈ 2–3 dB sur le master [SOURCE MX-01] ; bus comp SSL attaque la plus lente, release la plus rapide, ≈ 2 dB, sans écraser le mix [SOURCE MX-02] ; Neve 33609 attaqué doucement, release auto, ratio le plus faible, « l'aiguille bouge à peine » [SOURCE MX-05]. Le bus comp sert aussi à juger les niveaux (hats et shaker trop forts, clap à monter) [SOURCE MX-05].
- **Grave : rôle de chaque élément** : fondamentale de la basse 40–60 Hz, du kick 60–80 Hz, creux ≈ 50 Hz sur le bus drums et ≈ 70 Hz sur la basse [SOURCE MX-03] ; résonance de basse trouvée par balayage vers 125 Hz [SOURCE MX-04] ; « la basse doit dominer le morceau, pas le mix » [SOURCE MX-04].
- **Séparer sans tout sidechainer** : fondus audio sur le sub, courbe inverse de la décroissance du kick, à la place du sidechain [SOURCE MX-01] ; kick plus grave, moins de sub dans la basse, moins d'aigu sur la snare [SOURCE MX-06] ; le sub disparaît avant le drop [SOURCE MX-01].
- **Compatibilité mono** : prioritaire pour le club [SOURCE MX-02] ; transitoires mono sur une boucle DnB [SOURCE MX-06] ; ne pas panoramiquer le sub lourd (graveurs vinyle) [SOURCE MX-05] ; corrélation négative = problème de phase, écoute mono et d'un seul côté [SOURCE MX-02].
- **Espace par automation** : reverb automatisée sur le bus drums dans le break pour le contraste au drop [SOURCE MX-01] ; mix d'un delay automatisé en fin de phrase [SOURCE MX-03].
- **Encoches plutôt que de-esser** sur la voix [SOURCE MX-01] ; soothe 3 « deboom » sur le grave en M/S [SOURCE MX-03].
- **Saturation avant compression** [SOURCE MX-03] ; saturation en parallèle sur la top loop et les percussions [SOURCE MX-03] ; « mur de son » par petites touches cumulées [SOURCE MX-05].
- **Chaîne de master courte, un peu de HP/LP toujours** [SOURCE MX-01] ; boost d'aigu dès le master pour en faire moins sur chaque piste [SOURCE MX-02].
- **Écoute** : changer souvent le niveau d'écoute, casque très bas pour juger la clarté [SOURCE MX-03] ; première écoute écran éteint, notes sur papier [SOURCE MX-04]. Ces gestes sont ceux de l'utilisateur : un agent n'écoute pas.

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Voix : reverb ; HPF ; encoches | VintageVerb preset par défaut, mix 16 % ; HPF 123 Hz ; ≈ 2,6 kHz et 6 kHz | MX-01 |
| Kicks | 2 kicks superposés, aucune EQ ; léger roll-off d'aigu puis transitoire + drive pour souder | MX-01 |
| Chaîne master | ajout vers 15 kHz, retrait vers 200 Hz ; bus comp ≈ 2–3 dB ; mono maker réglé « bas » (valeur non lue [ASR ?]) | MX-01 |
| Snare ; hats | coupe ≈ 2 kHz ; creux ≈ 1 kHz | MX-01 |
| Boost de master, exemple | +2 dB à 15 kHz | MX-02 |
| Massive Passive | petits boosts ≈ 16–18 kHz et ≈ 60 Hz | MX-02 |
| Headroom d'export | « 6 dB » par sécurité ; 3 dB suffisent si rien ne dépasse 0 (true peak) ; mesuré 3,2 dB | MX-02 |
| Analyse du grave | tranches 40 / 80 / 120 / 160 Hz, kick et basse coupés | MX-02 |
| Kick | EQ avant compression : +50 Hz, creux ≈ 200 Hz (résonance) ; compresseur à attaque lente | MX-02 |
| Clap ; basse | +1 kHz, attaque rapide, HPF (valeur non dite) ; mono maker « ≈ 7 » (unité du plug-in, non convertible en Hz) + largeur sur l'aigu ; LA-2A ≈ 3–4 dB [ASR « 340 D »] | MX-02 |
| Drums, fader | −15 dB habituel, −12 dB ici | MX-03 |
| EQ de boucle drums | pas de coupe-bas ; boost ≈ 70 Hz sur le Mid ; creux ≈ 500 Hz et ≈ 1,2 kHz ; boost ≈ 2,2 kHz ; creux 150–250 Hz | MX-03 |
| Kick / basse | basse 40–60 Hz, kick 60–80 Hz ; creux ≈ 50 Hz (bus drums), ≈ 70 Hz (basse) | MX-03 |
| Compresseur de basse | 1176 Rev A 4:1 ou 8:1, ≈ 5 dB de réduction, ≈ 7 dB « son EDM traité » | MX-03 |
| soothe 3 | preset « deboom the bass », 40–80 Hz, en M/S ; aigu des Sides coupé raide pour resserrer | MX-03 |
| Synthé | HPF ≈ 85 Hz raide ; high shelf dès ≈ 2 kHz sur les Sides ; creux ≈ 150 Hz ; boost ≈ 400 Hz Mid ; creux ≈ 1,2 kHz | MX-03 |
| StressBox ; FutureVerb | sortie −2,3 dB ; mix 100 % sur bus | MX-03 |
| Basse (bus) | résonance ≈ 125 Hz coupée de 3 à 5 dB ; boue 120–300 Hz ; balayage en boost 6–7 dB | MX-04 |
| Niveaux ; faders | gains Utility non dits ; faders à 0 ; bus comp en release auto 1, ratio minimal | MX-05 |
| Basse pleine bande | jusqu'à ≈ 18 kHz, pour creuser de grands trous | MX-06 |

Aucune sonie en LUFS, aucun plafond de sortie ni mention de normalisation à l'export dans ces six vidéos.

### Ordre du mix, tel que filmé

(interp. : l'ordre est celui des minutages, une vidéo commentée n'est pas une procédure.)
- **MX-01** : voix → kicks → chaîne master → snaps et snare → craquements → hats et metals → reverb du break → fondus de sub → éléments d'ambiance.
- **MX-02** (le seul à le dire) : **bus master d'abord**, « approche pré-mastering » [SOURCE MX-02, 8:59] → NLS → bus comp → Massive Passive → HG-2 et bande → headroom et corrélation → analyse du grave → kick → clap → bus drums → basse → pad.
- **MX-03** : drums (parallèle, renfort de kick) → niveaux → EQ de boucle → saturation M/S → kick/basse → compression de basse → soothe → synthé → ordre saturation/compression → reverbs et delays → plan de la voix.
- **MX-04** : écoute écran éteint → diagnostic (basse contre kick) → bus du template (1 drums, 2 bass, 3 FX, 4 synths, 5 vocals) → EQ de la basse.
- **MX-05** : niveaux par Utility → largeur de la basse → bus drums → bus synthés.
- **MX-06** : tout en mono → signature fréquentielle (fondamentale + zone de résonance) → séparation par la source → stéréo.

### Écarts et contradictions

**Entre vidéos du thème**
- Kick : aucune EQ (MX-01) ou EQ avant compression, +50 Hz et creux ≈ 200 Hz (MX-02) ou creux ≈ 50 Hz au bus drums (MX-03).
- Coupe-bas : pas en EDM sur la boucle drums (MX-03), mais ≈ 85 Hz sur le synthé (MX-03) et 123 Hz sur la voix (MX-01).
- Duck du grave : fondus audio sur le sub (MX-01) ; sidechain de départ puis séparation par la source (MX-06) ; basse « qui gêne les kicks » traitée à l'EQ (MX-04).
- Niveau de départ : −15/−10 dB (MX-03, MX-04) contre 0 dB + Utility (MX-02, MX-05). Headroom : 3 dB suffisent (MX-02) contre « 6 dB » par sécurité (même vidéo).
- Master : une EQ de grande couleur + comp + saturation (MX-01), plusieurs couleurs cumulées (NLS, Massive Passive, HG-2, bande : MX-02).

**Contradictions avec les skills du projet**
- **Source d'abord, bus et master en dernier** (`ingenieur-mixage/modules/mixage/GUIDE.md`, `ingenieur-mixage/modules/mixer-house-professionnel/GUIDE.md`) : MX-02 commence par le bus master. Sa justification : mix reçu presque prêt, faders à 0 [SOURCE MX-02]. Contradiction directe, applicable seulement à un mix déjà équilibré (interp.).
- **Sidechain plutôt qu'EQ** pour partager 40–120 Hz (`ingenieur-mixage/modules/mixage/GUIDE.md`, étape 2) : MX-06 et MX-01 le contournent par la source et les fondus. Compatible avec la hiérarchie « arrangement et source → niveau → EQ → compression/sidechain » de `ingenieur-mixage/modules/mixer-house-professionnel/GUIDE.md` ; à tester en contexte.
- **Coupe-bas partout sauf kick/sub** (`ingenieur-mixage/modules/mixage/GUIDE.md`, étape 4) : MX-03 refuse la coupe-bas sur la boucle drums, qui contient le kick (pas de contradiction stricte).
- **Marge** : crête pré-limiteur ≈ −4 à −6 dBFS (`ingenieur-mixage/SKILL.md`) ; MX-02 accepte 3 dB (mesuré 3,2 dB) tant que rien ne dépasse 0 en true peak. Plus étroit que la règle ; ne pas l'adopter.
- **Une seule couleur par chaîne** (`ingenieur-mixage/SKILL.md` § 3 ; J37 au master 1, `ingenieur-mixage/modules/mixage/GUIDE.md`) : MX-01 et MX-02 cumulent EQ colorée, saturation et bande au master.
- **Mono** : MX-01 pose un mono maker sur chaque master, MX-02 un mono maker « haut » sur la basse. Aucune fréquence lisible : impossible de comparer au ≤ 110 Hz du projet. Règle du projet à garder. Plafond, sonie, normalisation : aucune vidéo ne les contredit, aucune ne les donne.
- **Natifs de Live** : MX-05 filme Utility (toléré : trim) ; MX-04 est sous Mixbus, MX-03 sous Logic, MX-01 sous Pro Tools, donc aucun effet natif de Live à retraduire hormis Utility.

### Dans l'installation du projet

| Geste filmé (outil) | Outil du projet | Pilotage (`fiches.md`) |
|---|---|---|
| Equilibrium (MX-01), Q8 (MX-04), Massive Passive (MX-01, MX-02) | Pro-Q 4 (fenêtre) ou REQ 6 (Frq, Gain, Q, shelves exposés ; balayage et relecture possibles) | REQ 6 exposé ; Pultec/Q8 : couleur non reproduite (interp.) |
| Bus comp : Townhouse, SSL UAD, Neve 33609, VSC-2, API (MX-01, MX-02, MX-05) | bx_glue (Threshold, Ratio, Attack 0,1–30, Auto Release, filtre sidechain, Mix) ; TheBus (Attack 0,1/10/30, Release 50/400/800, filtre 20–500 Hz) ; API-2500 | exposés ; « release le plus rapide » non réglable avec Auto Release seul (interp.) |
| 1176, LA-2A, CLA-3A (MX-02, MX-03) | CLA-2A/3A cités dans `ingenieur-mixage/modules/mixage/references/outils.md` mais absents de `fiches.md` : prober ; API-2500 (ratios jusqu'à 10:1) ou Pro-C 3 | API-2500 exposé ; Pro-C 3 par fenêtre |
| soothe 3 (MX-03) | soothe3 | fenêtre ; double-clic + saisie |
| Mono maker bx_digital (MX-01), mono maker de basse (MX-02) | bx_glue Mono Maker Frequency ; Utility toléré (mono) ; Ozone Imager 2 | exposé ; bx_digital non listé |
| Utility par piste (MX-05) | Utility toléré (trim) | natif, valeurs lisibles |
| HG-2, Elevate, bande, saturation (MX-01, MX-02, MX-03) | J37 (une couleur) ; RazorClip pour l'écrêtage | exposés ; couleur différente (interp.) |
| VintageVerb mix 16 % (MX-01) | ValhallaVintageVerb | Mix en `raw`, `str_for_value` à ne pas croire |
| Fondus de sub (MX-01) | automation de volume (`producteur-live/modules/live-automation/GUIDE.md`) | via `apply` |
| Corrélation, mono (MX-02) | SPAN en mode corrélation ; Insight 2 pour LUFS/true peak | fenêtre |

Présence non vérifiée sur le Mac : Waves NLS, Waves Trigger, StressBox, Devil-Loc, Saturn, 1176 UAD/Rev A, Pro-R, Blackhole, FutureVerb, Valhalla Delay, Echoboy, BYOME, Replika, bx_room, Dimension D, Elevate, Townhouse Bus Comp, SSL Brainworx, Vertigo VSC-2, Neve 33609, Maag EQ4, RX 12.

### Limites

- Aucune capture : chaque fiche liste ses points « à vérifier à l'écran » (courbe d'Equilibrium, réduction du Townhouse, réglages du 33609, bandes de soothe 3). Rien n'est confirmé.
- [ASR ?] : mono maker de MX-01 (« a tea »), LA-2A de MX-02 (« 340 D »), plug-in « Loop Trotter » de MX-03, gain par défaut « je crois » de MX-04 ; la valeur « ≈ 7 » de MX-02 n'a pas d'unité connue.
- Vidéos presque sans valeurs : MX-05 (niveaux, seuils et attaque non dits), MX-06 (une seule fréquence, 18 kHz).
- Non retenus : réglages créatifs (Replika, granulateur de MX-01) et choix musicaux ; contenu protégé volontairement laissé de côté.
- Échantillon : MX-04 et MX-05 sont un épisode de cours chacun, MX-06 des boucles de démonstration ; aucun mixdown commenté par Chris Lake, Eats Everything, Fred again.. ou un ingénieur de Skrillex ; rien en français ; Pretolesi (cahztwJBn7c) écarté faute de sous-titres.
- Le DAW n'est pas Live pour MX-01 (Pro Tools), MX-03 (Logic), MX-04 (Mixbus) ; MX-02 : non nommé. La logique se transpose, pas les réglages d'écran.

## Bas du spectre, du mix au master

Six vidéos (BA-01 à BA-06), lues sur transcription, son coupé : **rien n'a été entendu**, aucune capture d'écran. [SOURCE XX-nn] = dit dans la vidéo ; (interp.) = interprétation ; [ASR ?] = transcription automatique douteuse. Les formateurs sont Strob Studio (BA-01), D Ramirez (BA-02), Projektor (BA-03), Warp Academy (BA-04), Streaky (BA-05), TheCosmicAcademy (BA-06). Règles du projet confrontées : `AGENTS.md` (sub et basse médium dans deux instruments, sub mono, plafond ≤ −1 dBTP), `ingenieur-mixage/SKILL.md` (sub mono ≤ 110 Hz, largeur au-dessus de 120 Hz, corrélation ≥ 0 dans 30–120 Hz), `producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md` (rôles, polarité, décalage −5 à −10 ms), `producteur-rythmique/modules/construire-low-end-electronique/GUIDE.md`.

### Ce que le corpus retient

- **Le déséquilibre kick/basse se lit d'abord à l'analyseur, se décide à l'oreille.** À l'analyseur, kick ≈ −10 et basse ≈ −20 : 10 dB d'écart, « indice de déséquilibre » sans obligation d'aligner au dB près [SOURCE BA-01]. L'outil visuel sert à illustrer ou à compenser une mauvaise écoute du bas ; la décision est auditive [SOURCE BA-01]. (interp.) l'écoute revient à l'utilisateur.
- **Le kick frappe grosso modo entre 30 et 60 Hz, la basse vit dans la même zone ; réglages : longueur, sidechain, phase** [SOURCE BA-01]. Raccourcir le kick par automation de gain fait perdre presque tout son sub ; le rallonger le rend « fat » sans changer la crête de la somme [SOURCE BA-01].
- **La basse doit décroître en harmoniques** : fondamentale > 1re harmonique > suivante, pour un son actuel ; sur la basse de la vidéo, les trois étaient à peu près égales [SOURCE BA-01]. Il remonte la fondamentale d'environ 10 dB (shelf puis filtre « bien violent »), puis un peu la 1re harmonique [SOURCE BA-01].
- **Piège du boost + filtre non linéaire en phase : post-ringing** après bounce, qui déstabilise la transition avec le kick ; corrections : imprimer en audio puis éditer, ou automation de gain avec petite pente en fin de note [SOURCE BA-01]. Projektor coupe le post-ringing avec LFO Tool avant le transitoire du kick suivant [SOURCE BA-03].
- **Alignement de phase : après le traitement de la basse**, parce que les filtres décalent la phase autour du cutoff ; saturation et compression ne sont pas en cause [SOURCE BA-03]. Aléa de phase d'oscillateur à 0 en basse, sinon le point de départ change à chaque note [SOURCE BA-03]. L'alignement ne peut pas être exact, le sinus du kick glissant en pitch [SOURCE BA-03] ; la relation de phase change à chaque note de basse : « pas de relation parfaite » [SOURCE BA-01].
- **Traduire le sub vers les petits systèmes par harmoniques, pas par plus de sub** : sous 60 Hz, rien ne passe sur téléphone, enceinte Bluetooth ou écouteurs [SOURCE BA-02]. Deux voies : sinus à +1 octave, ou distorsion puis passe-bas [SOURCE BA-02]. Même logique à bas niveau d'écoute : harmonique d'ordre 2 de la basse (50 → 100 Hz, 60 → 120 Hz) [SOURCE RE-04, thème suivant].
- **Mono du grave : à tester, pas à décréter.** Dans la démonstration tech house de Warp, supprimer les côtés sous 100 Hz ne gagne que 0,1 dB de crête, Bass Mono à 200 Hz également +0,1 dB, mais sur un autre mix commercial le titre passe presque 2 dB au-dessus (clip) [SOURCE BA-04]. Un passe-haut à forte pente tourne fortement la phase à la coupure : côtés et mid se désalignent, perte de punch [SOURCE BA-04].
- **Streaky (mastering)** : la règle « mono la basse » vient du vinyle (sillon, diamant) ; en mastering, ajouter de l'EQ grave sans monoïser donne un bas plus costaud ; le crossover trop haut amincit 200–400 Hz ; monoïser sous ≈ 50 Hz, « souvent mieux de ne pas monoïser du tout » [SOURCE BA-05]. Dance : grave au centre ; jamais sur indie/guitare sauf gros problème de phase [SOURCE BA-05].
- **Le limiteur écrase kick et basse** : écouter le delta (ce que le limiteur retire), passer en revue les modes, se concentrer sur ≈ 100 Hz et en dessous ; si le résultat reste mauvais, c'est un problème de mix en amont [SOURCE BA-06].

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Zones | sub ressenti 20–60 Hz ; basse audible 60–300 Hz | BA-02 |
| Kick (zone d'impact) | 30 à 60 Hz | BA-01 |
| Niveaux analyseur kick / basse | ≈ −10 / ≈ −20 (10 dB d'écart) ; basse remontée de +5 dB (≈ −15) en test | BA-01 |
| Boost de la fondamentale de basse | ≈ 10 dB au total, shelf puis filtre | BA-01 |
| Note de basse (Operator) | C3 ≈ 300, C2 ≈ 120, C1 ≈ 60 Hz ; note « optimale » F, plage F à B | BA-02 |
| Sinus d'appoint | 2e oscillateur à +1 octave (F → 60 + 120 Hz) | BA-02 |
| Vinyl Distortion | centré vers 158 Hz, basse stéréo distordue puis filtrée | BA-02 |
| Niveau kick / basse (SPAN) | kick ≈ 50 Hz à ≈ −33 (échelle SPAN) ; basse « légèrement en dessous » | BA-02 |
| Coupe-bas de la basse | aucun sur la basse (phase) ; coupe-bas fait sur le master | BA-02 |
| Utility Bass Mono | placé après Vinyl Distortion ; fréquence non dite | BA-02 |
| Aléa de phase d'oscillateur | 0 en basse | BA-03 |
| PHA-979 | mêmes réglages en L et en R ; exemple « 90 » sur les deux couches, à ne pas recopier | BA-03 |
| EQ coupe-bas comme déphaseur (kick) | coupe-bas sans couper ; deux EQ = effet doublé ; puis inversion de polarité | BA-03 |
| Côtés d'une basse (tech house) | énergie sous 100 Hz ; crête −5,5 dB ; mono : +0,1 dB (aussi à 200 Hz, Bass Mono) | BA-04 |
| Autre mix commercial | Bass Mono sous 200 Hz : presque +2 dB, clip | BA-04 |
| Côtés selon le genre | bass music jusqu'à 35 Hz ; Noisia : décroissance dès ≈ 120 Hz, plus rien vers 55 Hz | BA-04 |
| Mono au mastering | sous ≈ 50 Hz si l'on monoïse ; bas-médiums menacés 200–400 Hz | BA-05 |
| Limiteur : zone à surveiller | ≈ 100 Hz et en dessous ; passe-bas sur le delta (fréquence non dite) | BA-06 |
| Modes qui préservent le mieux le grave | Balanced, Crisp, Clipping ; « Modern » écrase davantage (lecture de la transcription, (interp.)) | BA-06 |

### Procédures données

**Phase kick/basse (BA-03)** : 1) oscilloscope en sidechain de la somme kick + basse, ou PHA-979 en mode couches ; 2) mesurer après les filtres de la basse ; 3) aligner les plus gros pics, mêmes réglages L et R ; 4) l'addition faisant monter le niveau, baisser la note (vélocité, ou mieux le niveau de tranche) ; 5) séparer les notes de basse qui chevauchent le kick et retirer leur 1re harmonique ; 6) placer le transitoire de la basse sur un passage à zéro du kick ; 7) option : coupe-bas léger sur le kick comme déphaseur puis inversion de polarité ; effet secondaire, le kick s'allonge (resampler ou couper à la LFO Tool). Valeurs de réglage de l'exemple non transférables [SOURCE BA-03].

**Équilibre kick/basse (BA-01)** : lire l'écart à l'analyseur ; ajuster longueur du kick et fin de queue de basse ; remonter la basse à l'EQ (balance par fréquence) ; contrôler le post-ringing après bounce ; astuce d'écoute : filtrer pour n'écouter que le grave.

**Test de mono (BA-04)** : SPAN en M/S, écouter les côtés seuls ; couper les côtés (ou Bass Mono) et relever la crête ; en phase minimale, alternative sans rotation : TDR Nova en mode difference, low shelf négatif, ou cloche soustractive jouant sur le Q ; analyser les références du genre.

**Contrôle téléphone (BA-02)** : simulation téléphone ; si la basse disparaît, ouvrir le filtre, baisser le sub, ajouter une cloche plus haut (Pro-Q 4). Conseil final : s'appuyer sur la mesure si la pièce n'est pas fiable.

**Limiteur (BA-06)** : delta, modes, ≈ 100 Hz et en dessous, loudness meter sur le delta passe-bas, puis réglage fin du curseur Character.

### Écarts et contradictions

**Entre vidéos.** Coupe-bas et phase : BA-02 évite tout coupe-bas sur la basse pour préserver la phase, BA-03 utilise au contraire un coupe-bas sur le kick pour décaler la phase, BA-04 chiffre la rotation de phase des passe-haut raides et propose la phase linéaire. Mono : BA-04 montre qu'une basse large construite en phase tient en mono et défend la largeur basse, BA-05 monoïse sous ≈ 50 Hz ou pas du tout, BA-02 passe la basse distordue en Bass Mono. Niveau relatif : BA-01 (10 dB d'écart comme indice) et BA-02 (basse légèrement sous le kick) convergent, mais sur des échelles d'analyseur différentes (−10/−20 contre −33), donc non comparables. Genre : Noisia coupe les côtés dès ≈ 120 Hz, la bass music les garde jusqu'à 35 Hz [SOURCE BA-04].

**Avec les règles du projet.**
- Mono jusqu'à 200 Hz testé en BA-04 et mono « sous ≈ 50 Hz, souvent pas du tout » en BA-05 : le projet impose le sub mono ≤ 110 Hz (`ingenieur-mixage/SKILL.md`, § Ordre de travail) et le grave centré sous 120 Hz sur le bus BASSES (`ingenieur-mixage/modules/mixage/GUIDE.md`). BA-05 va plus bas que la règle, BA-04 laisse des côtés jusqu'à 35 Hz dans le genre bass music : la règle du projet l'emporte pour le sub, tout écart se mesure (corrélation ≥ 0 dans 30–120 Hz).
- Pas de coupe-bas sur la basse, coupe sur le master (BA-02) : `producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md` prévoit un coupe-bas du kick de 25–30 Hz et, quand le kick tient le grave, un coupe-bas de basse de 60–80 Hz. Un coupe-bas sur le master n'est pas prévu par ces skills.
- « Une basse » en BA-01 et BA-02 (un seul son avec octave en 2e oscillateur) : `AGENTS.md` demande sub et basse médium dans **deux instruments séparés**. L'harmonique d'octave de BA-02 se place donc dans l'instrument de basse médium (`producteur-rythmique/modules/construire-low-end-electronique/GUIDE.md`, étape 6 : harmoniques sur un layer de mid-bass), pas en 2e oscillateur du sub.
- Limiteur « vers 0 dB » (BA-06) : plafond du projet ≤ −1 dBTP (L2 −1,0 dBFS ou L4 True Peak, `ingenieur-mixage/SKILL.md` § 5).
- Natifs filmés : Utility Bass Mono (BA-02, BA-04) et Utility en général restent tolérés (règle 6 d'`ableton-live-session`, Utility mono/trim/phase) ; EQ Eight M/S (BA-04), Vinyl Distortion, Auto Filter ajouté en chaîne, Roar [ASR ?] (BA-02) sont de **nouveaux effets natifs** : non autorisés dans les chaînes de mix. Operator (sinus de sub) est un instrument natif toléré.

### Dans l'installation du projet

| Geste filmé | Outil filmé | Traduction (`ingenieur-mixage/modules/effets-plugins/references/fiches.md` sauf mention) |
|---|---|---|
| Spectre, niveaux kick/basse, côtés | SPAN (BA-02, BA-04) | SPAN, installé ; fenêtre seule (Avg Time, Block Size) ; vues Mid/Side et corrélation. Chiffres relevés par capture. |
| Boost fondamentale, cloche soustractive, shelf | EQ, Pro-Q 3/4 (BA-01, BA-02, BA-04) | REQ 6 (Frq, Gain, Q, Hi-Pass, Bell, Hi-Shelf exposés ; shelf grave non listé dans les fiches) ou Pro-Q 4 (fenêtre ; M/S, phase linéaire, bande dynamique). Pro-Q 3 non nécessaire. |
| Bande dynamique en sidechain sur le kick | Pro-Q (BA-02) | Pro-Q 4 « Make Dynamic », fenêtre + capture. |
| Ducking de volume | Kickstart, LFO Tool (BA-02, BA-03) | ShaperBox 3 (fenêtre) ; Kickstart et LFO Tool : présence sur le Mac non vérifiée. Sinon API-2500 / bx_glue (filtre sidechain) ou TheBus (External Sidechain). Gain de piste automatisé : Utility toléré. |
| Mono du grave | Utility Bass Mono (BA-02, BA-04) | Utility toléré ; ou bx_glue (Mono Maker Frequency, exposé) ; largeur au-dessus de 120 Hz : Ozone Imager 2. |
| Soustraction M/S en phase minimale | TDR Nova (BA-04) | TDR Nova 2.2.2 repéré (`ingenieur-mixage/modules/mastering-outils/references/inventaire-local.md`), paramètres non relevés. |
| Alignement de phase | PHA-979 (BA-03) | présence sur le Mac non vérifiée ; en attendant : polarité par Utility (toléré), décalage −5 à −10 ms, mesure par `kick_bass_check.py` (`producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`). |
| Distorsion de basse, octave | Vinyl Distortion, Roar, Operator (BA-02) | harmoniques sur le layer de mid-bass (Serum 2) ; couleur : J37 ou RazorClip (modèle à identifier dans la fenêtre). Même couleur sur l'ensemble : une seule par chaîne. |
| Limiteur à plusieurs modes | Ozone Maximizer (IRC), Pro-L (BA-06) | Pro-L non repéré ; Ozone 12 Elements repéré, présence du Maximizer et du delta dans cette édition non vérifiée ; L2 (ARC, Release) et L4 (Over Sampling) exposés ; LUFS et true peak par Insight 2. |
| Simulation téléphone | Master Plan (BA-02) | présence non vérifiée ; (interp.) passe-haut + passe-bas REQ 6 sur un monitoring neutralisé avant export. |

### Limites

- **Outils non vérifiés** : Kickstart, LFO Tool, Voxengo PHA-979, Master Plan, Plugin Doctor, Mastering The Mix LEVELS, Pro-L (non repéré), Pro-Q 3. Maximizer d'Ozone 12 Elements non vérifié.
- **[ASR ?]** : le prénom du formateur de BA-01 (« Gor »), « Roar » (BA-02), « Cisco/size scope » et « fpa979 » (BA-03), l'ingénieur « de Mixbus TV » (BA-04), « Nick DeLorenzo » (BA-06) ; la lecture « higher LUFS values » (BA-06) est ambiguë : (interp.) lecture négative moins élevée. Les notes C1/C2/C3 en Hz de BA-02 sont arrondies.
- **Aucune cible chiffrée sub/kick en LUFS ou RMS au master** ; les −33 (SPAN) et −10/−20 (analyseur) dépendent des réglages d'affichage (note du corpus). Aucune vidéo de multibande appliquée au seul grave en master, ni de gravure vinyle filmée (BA-05 en parle à l'oral).
- **Fréquences non dites** : Bass Mono (BA-02), passe-bas du delta (BA-06), coupure de l'EQ servant de déphaseur (BA-03).
- **Vidéo sans valeurs** : BA-05 face caméra, une seule valeur (≈ 50 Hz). Candidat écarté faute de sous-titres : SINEE Global (I__tWZTk5-Q), à regarder à l'écran.
- Points à vérifier à l'écran listés par le corpus pour chaque fiche (BA-01 0:41, BA-02 18:49, BA-03 7:58–8:20, BA-04 3:31 et 5:17, BA-06 3:41) : aucun réglage d'écran n'est confirmé.

## Références, traduction et écoute

Six vidéos (RE-01 à RE-06), lues sur transcription, son coupé : **rien n'a été entendu**. RE-06 est la même vidéo que MX-02 (JC Concato, Point Blank, LUIXtDO4d8s) : traitée ici une seule fois, pour sa part « référence, mono, headroom, grave » ; le mixage complet de cette masterclass relève de MX-02. Formateurs : Strob Studio (RE-01), Protoculture pour Sonic Academy (RE-02), Jesco Lohan chez Underdog (RE-03), Incidence Studio (RE-04), Warp Academy x Sonarworks (RE-05, contenu sponsorisé), Point Blank (RE-06). Règles du projet confrontées : `AGENTS.md`, `ingenieur-mixage/SKILL.md` § 4 (REF vers Main hors limiteur, gain ajusté à ±0,5 dB), `ingenieur-mixage/modules/mixer-house-professionnel/references/track-reference-avec-outils.md`.

### Ce que le corpus retient

- **Égaliser le loudness est la règle d'or** ; le niveau d'écoute change la courbe de réponse de l'oreille ; 0,1 dB d'écart peut fausser la préférence [SOURCE RE-01]. Ne pas pousser son mix dans un limiteur pour rejoindre la référence : baisser le gain de la référence [SOURCE RE-01, aussi RE-02 : la référence masterisée est plus forte, et le plus fort paraît meilleur].
- **Comparer en short-term (ou momentary) sur le passage le plus fort, en boucle**, pas en intégré [SOURCE RE-01]. Section équivalente comparée (ici kick + basse), Match refait selon la section [SOURCE RE-02]. Chez Incidence aussi, rester toujours au même niveau d'écoute, y compris pendant les références [SOURCE RE-04].
- **Routage : la référence ne passe pas par le traitement du master** : directement vers les sorties d'écoute (7-8), bascule par solo [SOURCE RE-01] ; bus à part hors master bus, ou Metric AB en dernier insert du master post-fader (Control Room dans Cubase) [SOURCE RE-02] ; références vers la sortie en contournant le mix bus [SOURCE RE-03]. Un limiteur sur le master bus pendant le mix donne un mix qui ne marche qu'écrasé [SOURCE RE-03].
- **Calibration d'écoute par paliers** : niveau de travail 70–80 dB SPL [ASR ?], bruit rose, pondération C, slow, trois niveaux fixes (bas, moyen, fort) sans tourner le bouton en continu [SOURCE RE-03] ; repères visuels au feutre, crans numériques, dim RME [SOURCE RE-03]. Incidence : 85 dB SPL pondéré A recommandé couramment, lui travaille vers 75 dB et vérifie à 85 dB [SOURCE RE-04].
- **Vérifier très bas et très haut** : très bas (50–55 dB SPL), si kick et basse disparaissent, il manque de traduction dans les médiums, ajouter l'harmonique d'ordre 2 ; à bas niveau on entend mieux pompage et artefacts de compression [SOURCE RE-04]. Fort niveau (≈ 100 dB LAeq 60 s pour un club) : 100–200 Hz devient boueux, 4–8 kHz piquant, contrôle dynamique du kick par expansion sidechainée plutôt qu'EQ statique [SOURCE RE-04].
- **Le grave est la zone que la pièce rend le plus faussement** : c'est là que la référence aide le plus ; l'analyseur n'est qu'un appoint, le grave dépend aussi des bas-médiums, les derniers ±1–2 dB de sub se décident à l'oreille [SOURCE RE-01, RE-03]. Des enceintes 2 voies descendent vers 40–60 Hz ; 20–30 Hz hors de portée [SOURCE RE-03].
- **Casque : à garder comme point de référence de fin de mix**, mais sa réponse biaise : DT 990 Pro accentué au-dessus de 5 kHz, HD 650 plus plat ; ouverts dynamiques en chute sous 60 Hz ; grave qui décroît plus vite donc surmixage de la basse [SOURCE RE-05]. Correction maison de l'auteur : courbe SoundID +3 dB dans le grave [SOURCE RE-05].
- **Compatibilité mono** : capitale en club (RE-06 : bar, petits systèmes) ; stéréo seulement dans un couloir d'≈ 1 m au centre en sonorisation (RE-03) ; écouter en mono et d'un seul côté en mono ; corrélation négative = problème de phase, basse moins ronde, pas de gravure vinyle [SOURCE RE-03, RE-06].
- **Le titre doit tenir dans la fourchette de loudness des autres titres** : en DJ set, un titre trop dynamique à même moyenne dépasse le headroom ; un drop trop compressé perd son énergie face au break [SOURCE RE-03].

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Écart de loudness perceptible | 0,1 dB (préférence faussée) | RE-01 |
| Drop du mix, short-term | ≈ −6 LUFS ; référence −5,1, baissée de 0,9 dB → les deux à −6 | RE-01 |
| Routage de la référence | sorties d'écoute 7-8, sans traitement master ; solo pour basculer | RE-01 |
| Grave à l'analyseur | référence ≈ −5, mix ≈ −3/−4 : « dans la zone » ; à ne pas recopier | RE-01 |
| Metric AB, Match | −7,8 (dB selon l'étude, unité à vérifier à l'écran) ; Match par section et par référence | RE-02 |
| Metric AB, placement | inserts de la Control Room (Cubase) ; ailleurs : dernier insert du master, post-fader | RE-02 |
| Modes de lecture Metric AB | Latch, Cue, Sync, Manual | RE-02 |
| Niveau d'écoute (Underdog) | 70–80 dB SPL [ASR ? « 1780 »], bruit rose, pondération C, slow ; trois paliers | RE-03 |
| Mix à ce niveau | moyenne −23 LUFS (−18 avec de l'analogique) | RE-03 |
| Passe-bas d'écoute sur la sortie master | vers 150 Hz (ou 100) | RE-03 |
| Limites de matériel | enceintes d'Oscar : rien sous 150 Hz ; 2 voies : 40–60 Hz ; absorbeurs poreux jusqu'à ≈ 40 Hz ; 80–90 % du budget acoustique d'un studio pro sous 50 Hz | RE-03 |
| Subs de club | descendent à 20 Hz ; les plus petits chutent vers 40 Hz (un peu à 30) ; kick à 60 Hz plus léger qu'à 45 Hz | RE-03 |
| Coupe-bas par piste | sous 20 Hz sur les pistes, pas sur le mix bus ; pente 12 dB/oct (6 dB/oct = simple changement tonal), parfois 48 | RE-03 |
| Stéréo en sonorisation | couloir d'≈ 1 m au centre | RE-03 |
| Niveau d'écoute recommandé | 85 dB SPL pondéré A (ou 83) ; Incidence travaille à 75 dB, vérifie à 85 | RE-04 |
| Bas niveau / niveau club | 50–55 dB SPL (≈ 25 dB au-dessus de son bruit de fond, dépend de la pièce) ; club ≈ 100 dB LAeq 60 s | RE-04 |
| Harmoniques d'ordre 2 | basse 50 → 100 Hz ; 60 → 120 Hz | RE-04 |
| Zones sensibles | 6–8 kHz piquant ; 4–8 kHz délicat ; 100–200 Hz boueux à fort niveau | RE-04 |
| Casques | DT 990 Pro : excès > 5 kHz ; ouverts dynamiques : chute < 60 Hz ; angle 90° au casque contre 30° (triangle équilatéral) | RE-05 |
| Courbe maison SoundID | +3 dB dans le grave | RE-05 |
| Headroom avant mastering | 3 dB suffisent, ici 3,2 dB ; « règle des 6 dB » surtout pour ne pas dépasser 0, sample et true peak | RE-06 (= MX-02) |
| Magic AB | jusqu'à 9 titres, repères ; A = mix, B = référence | RE-06 |
| Bass Space | vérifier 40 / 80 / 120 / 160 Hz hors rouge, kick et basse coupés | RE-06 |
| Basse : mono maker | BX_control vers « 7 » (unité non dite), largeur plus grande en haut | RE-06 |
| Kick / master / bus | kick +50 Hz, creux ≈ 200 Hz ; +2 dB à 15 kHz sur le master ; SSL ≈ 2 dB, attaque lente ; Massive Passive 16–18 kHz et 60 Hz ; LA-2A 3–4 dB | RE-06 |

### Procédures données

**A/B de référence à niveau égal (RE-01, RE-02, RE-06)** : 1) référence hors traitement master ; 2) boucler le passage le plus fort de chaque, section équivalente ; 3) mesurer en short-term ; 4) baisser la référence (Match de Metric AB : −7,8 chez RE-02), jamais monter le mix dans un limiteur ; 5) comparer à l'oreille, spectre, dynamique, largeur, profondeur ; 6) appoint à l'analyseur sur le grave ; 7) refaire le Match à chaque section et chaque référence ; 8) Magic AB en fin de master jusqu'à 9 titres pour vérifier l'ordre de grandeur.

**Calibration d'écoute (RE-03, RE-04)** : choisir un niveau et s'y tenir ; trois paliers fixes ; bruit rose, pondération C, slow [SOURCE RE-03] ; ou 75 dB de travail, 85 dB de vérification, et un passage à 50–55 dB et un autre près de 100 dB pour la traduction [SOURCE RE-04]. La vidéo ne montre aucun sonomètre en direct : valeur de calibration SPL du bruit rose absente ou [ASR ?] chez RE-03.

**Tests de traduction** : balayage d'un sinus Operator en mode Fixed vers le bas pour trouver la limite de ses enceintes (RE-03) ; cloakroom check (RE-03) ; mono et un seul côté en mono, surveillance de la corrélation (RE-06) ; casque en fin de mix (RE-05).

### Écarts et contradictions

**Entre vidéos.** Niveau d'écoute : RE-03 vise 70–80 dB SPL pondéré C (valeur [ASR ?]), RE-04 cite 85 dB pondéré A comme repère, travaille à 75 et vérifie à 85 : pondérations différentes, non comparables sans mesure (interp.). Routage : RE-01 envoie la référence directement aux sorties d'écoute, RE-02 passe par le dernier insert du master post-fader, RE-03 contourne le mix bus : trois architectures, une même exigence (référence non traitée). Comparer en short-term (RE-01) contre section stable en LUFS/RMS (RE-03). Grave au casque : RE-05 ajoute +3 dB de courbe maison pour compenser la décroissance, RE-04 recommande de vérifier à bas niveau en ajoutant de l'harmonique, deux remèdes distincts à un même constat. Coupe-bas : RE-03 sous 20 Hz sur les pistes et pas sur le mix bus ; BA-02 sur le master seulement (thème précédent).

**Avec les règles du projet.**
- Tolérance de niveau : RE-01 parle de 0,1 dB d'écart qui fausse la préférence, `ingenieur-mixage/SKILL.md` § 4 ajuste la REF à ±0,5 dB. La règle du projet est plus lâche que la vidéo : (interp.) viser le plus proche possible, lire l'écart dans Insight 2 ou WLM Plus.
- Sonie : drop à ≈ −6 LUFS short-term (RE-01) et mix à −23 LUFS (RE-03) ne sont pas des cibles : le projet donne un LUFS intégré club −9 à −7 indicatif (`ingenieur-mixage/SKILL.md` § 5). Court terme contre intégré, ne pas confondre.
- Headroom : RE-06 dit que 3 dB suffisent (3,2 dB) ; `ingenieur-mixage/SKILL.md` § 5 vise une crête pré-limiteur ≈ −4 à −6 dBFS (indicatif), plafond ≤ −1 dBTP. Le projet est plus prudent.
- Passe-bas ≈ 150 Hz sur la sortie master (RE-03) et courbe SoundID +3 dB (RE-05) : un traitement sur Main altère la référence ; `track-reference-avec-outils.md` § 2 et § 4 demande du monitoring commun, sans traitement qui modifierait la référence, et un Utility de monitoring neutralisé avant export.
- Mono maker à « 7 » (RE-06) : unité non dite, règle du projet : sub mono ≤ 110 Hz, largeur au-dessus de 120 Hz (`ingenieur-mixage/SKILL.md`). Pas de valeur de coupure transférable.
- « Titre prêt pour Spotify ≈ prêt pour le club » (RE-03) : le projet distingue deux exports (streaming ≈ −14, club −9 à −7 indicatif) et mesure leur true peak et LUFS séparément (`producteur-rythmique/modules/construire-low-end-electronique/GUIDE.md`, étape 8).
- Natifs filmés : Spectrum d'Ableton (RE-03) et Operator en sinus Fixed (RE-03) : l'instrument natif Operator est toléré, Spectrum est un effet natif (remplacé par SPAN). Aucune autre vidéo du thème ne filme d'effet natif dans une chaîne de mix.

### Dans l'installation du projet

| Geste filmé | Outil filmé | Traduction |
|---|---|---|
| Piste de référence hors traitement master, bascule par solo | routage Live (RE-01, RE-03) | déjà en place : REF → Main hors limiteur ; limiteur en fin de BUS MASTER 3 (`track-reference-avec-outils.md` § 2). |
| Mesure short-term, niveau égal | Decibel, Clarity (RE-01) ; Metric AB Match (RE-02) | Insight 2 en bout de Main (short-term, capture) ou WLM Plus ; Decibel, Clarity et Metric AB : présence sur le Mac non vérifiée. Gain de la REF : Utility de la piste REF (toléré, trim) ou fader. |
| A/B jusqu'à 9 titres avec repères | Magic AB, Metric AB (RE-02, RE-06) | présence non vérifiée ; en attendant : pistes REF 1 à 3, repères de clip Live, solo/mute (`track-reference-avec-outils.md` § 2). |
| Spectre de la référence contre le mix | analyseur M/S, SPAN (RE-01, RE-03) | SPAN (Avg Time, Block Size, courbe Side) et Pro-Q 4 (spectre d'une autre instance) ; Tonal Balance Control 3 pour la courbe cible. Pas de lecture de qualité sur un graphique. |
| Passe-bas d'écoute 100–150 Hz sur la sortie | passe-bas master (RE-03) | REQ 6 (Low-Pass exposé) en monitoring seulement, neutralisé avant export ; (interp.). |
| Cloche à 60 Hz, creux ≈ 200 Hz, +2 dB à 15 kHz | Massive Passive, EQ du master (RE-06) | REQ 6 ou Pro-Q 4 ; PuigTec repéré (`inventaire-local.md`). Aucune de ces valeurs n'est une consigne. |
| Compression de bus lente, ≈ 2 dB | UAD SSL Bus Comp (RE-06) | bx_glue (Attack, Ratio, Auto Release, Mix) ou Waves SSLComp repéré. |
| Compression du grave, tape 15 IPS, LA-2A 3–4 dB | UAD tape, LA-2A (RE-06) | J37 (Speed, Formula, Saturation) ; API-2500 ; CLA-2A (repéré selon `mixage-par-style-synthese.md`). |
| Harmoniques paires/impaires, loudness perçu | Black Box HG-2 (RE-06) | J37 ou RazorClip ; différence de couleur (interp.). |
| Mono maker de basse, largeur en haut | BX_control (RE-06) | bx_glue (Mono Maker Frequency exposé) ; Ozone Imager 2 au-dessus de 120 Hz. |
| Bass Space (40/80/120/160 Hz) | module de Mastering The Mix (RE-06) | présence non vérifiée ; alternative mesurée : SPAN et `kick_bass_check.py` sur exports kick/basse séparés. |
| Expansion sidechainée sur le kick à fort niveau | expandeur multibande (RE-04) | bande dynamique Pro-Q 4 (fenêtre) ; ShaperBox 3 ; TDR Nova repéré. |
| Limiteur adaptatif issu du vinyle | Schwabe Digital [ASR ?] (RE-04) | présence non vérifiée ; L2 ou L4 déjà en place. |
| Correction casque et pièce | Sonarworks SoundID Reference (RE-05) | présence non vérifiée ; utiliser sur le monitoring seulement et bypass avant export (interp.). |
| Sinus Fixed balayé vers le bas | Operator (RE-03) | Operator natif (instrument toléré) ou sinus de Serum 2. |
| Mono, trim, phase | Utility | toléré (règle 6). |

### Limites

- **Outils non vérifiés (présence sur le Mac non vérifiée)** : Process Audio Decibel, TC Electronic Clarity, ADPTR Metric AB, Sample Magic Magic AB, Sonarworks SoundID Reference, Mastering The Mix LEVELS / Bass Space, Schwabe Digital, BX_control, Manley Massive Passive, Black Box HG-2, UAD SSL Bus Comp, UAD tape, LA-2A UAD, CanOpener, SubPac. TDR Nova, PuigTec et SSLComp sont repérés comme fichiers (`inventaire-local.md`) ; CLA-2A l'est selon `mixage-par-style-synthese.md` mais leurs paramètres ne sont pas relevés.
- **[ASR ?]** : « 1780 » pour 70–80 dB SPL et la valeur exacte de calibration (RE-03, 36:35) ; « Hiful » pour Schwabe Digital, « Hassenda Mastering » (RE-04) ; « Audeze » (RE-05) ; Mastering The Mix LEVELS et Bass Space (RE-06) ; transcription française de RE-01 de mauvaise qualité. L'unité « dB » de −7,8 (RE-02) est ajoutée par l'étude.
- **Unités floues** : mono maker « 7 » (RE-06) ; « +50 Hz » pour le kick (RE-06) à lire à l'écran ; grave à l'analyseur −5 / −3 / −4 (RE-01) sans échelle.
- **Pas de calibration SPL montrée en direct** : RE-03 cite la méthode, RE-04 donne les plages 75/85/100 dB sans montrer la mesure (note du corpus). Aucune valeur de calibration de sonomètre n'est donc à reprendre ici.
- **Vidéos sans valeur utile pour le projet** : RE-02 est un tutoriel d'outil (Cubase, Metric AB) ; RE-05 est sponsorisé et donne une seule valeur (+3 dB). RE-06 : détail de mixage dans MX-02.
- **Manques du corpus** : pas de comparaison chiffrée master club contre streaming sur un même titre ; pas de démonstration des modules d'analyse de Metric AB ni de Mastering The Mix REFERENCE ; correction de pièce couverte seulement par une vidéo sponsorisée.
- Points « à vérifier à l'écran » du corpus (RE-01 7:58, RE-02 9:08, RE-03 14:19, 24:00–25:41, 36:35, RE-04 3:55, 7:44, RE-05 9:34, RE-06 22:08, 24:58, 40:46) : aucun confirmé.

## Pré-master et stem mastering

Six vidéos (PR-01 à PR-06), lues sur transcription, son coupé : **rien n'a été entendu**, aucune capture n'a été faite. PR-01 à PR-04 portent sur le niveau, la marge et le limiteur du pré-master ; PR-05 et PR-06 sont deux sessions de stem mastering (hip-hop/électronique, électro-pop/2-step : aucune house ni techno). [SOURCE PR-xx] = dit dans la vidéo ; (interp.) = interprétation ; [ASR ?] = transcription automatique douteuse. Les valeurs sont celles que disent les vidéos, des points de départ et non des normes ; les règles du projet sont rappelées plus bas avec leur fichier.

### Ce que le corpus retient

- **Calibration au VU.** Point de départ du gain staging analogique : 0 dB VU = −18 dBFS ; l'objectif de Pretolesi est que la somme des stems, sur la partie la plus forte, tombe à 0 VU [SOURCE PR-01 1:23, 4:06–4:18]. Kirk Degiorgio calibre pareil, chaque bus (kick + basse, drums sans kick, reste) tournant autour de 0 VU [SOURCE PR-02 3:06–3:25]. (interp.) Un VU lit une moyenne : ce n'est pas la même grandeur que les « −6 dB » de crête demandés par les ingés mastering.
- **Recaler au gain d'entrée, pas aux faders.** Les plugins sont pré-fader et recevraient toujours trop de niveau ; boucle sur la partie la plus chargée puis −10 dB sur tous les stems pour atteindre 0 VU [SOURCE PR-01 5:20–6:38]. À niveau constant, un preset de compresseur réagit pareil d'un morceau à l'autre [SOURCE PR-01 8:25–8:43]. Après un traitement, retour à 0 VU à la main, sans faire confiance à l'auto-gain [SOURCE PR-01 12:29, 13:34].
- **Marge demandée au pré-master.** « −6 dB » = environ 6 dB sous le full scale, pour que l'ingé puisse limiter et clipper [SOURCE PR-02 6:00–6:21] ; crêtes à −6 dB maximum [SOURCE PR-04 12:07–12:21] ; bounce avec 3 à 6 dB de marge puis mastering dans un projet séparé [SOURCE PR-05 43:12–43:26].
- **La marge est contestée.** PR-03 cite la règle d'or (crêtes à −6 dBFS, encore demandée par les ingés) puis la réfute : en 32 bits flottants, +35 dB sur une piste et −35 dB au master, export, réimport et inversion de phase donnent un silence total, donc aucune perte ; la marge n'a pas d'importance tant qu'on reste en flottant [SOURCE PR-03 0:16–0:39, 2:02–8:20]. Deux réserves dites dans la même vidéo : en 24 bits fixe, distorsion et pas de null [SOURCE PR-03 11:40–13:02] ; les émulations analogiques non linéaires gardent besoin d'un gain staging [SOURCE PR-03 8:41–9:24].
- **Pas de limiteur dans le fichier livré, mais la couleur du bus reste.** PR-02 : pas de limiteur sur le master bus, le mètre sert de repère [SOURCE PR-02 1:26–1:41]. PR-04 : on peut écrire dans un limiteur, mais il cache les écrêtages internes et fait négliger le gain staging ; erreur courante : couper toute la chaîne de mix bus avant l'envoi, « la magie disparaît » ; garder la coloration et la colle du bus drums, enlever seulement le limiteur [SOURCE PR-04 5:11–6:21, 11:36–12:07, 13:10–13:20].
- **On ne décide pas d'un niveau de kick à travers un limiteur.** Kick ±2 dB sans limiteur : différence nette ; avec limiteur, 3–4 dB s'entendent à peine, selon la vidéo [SOURCE PR-04 7:19–8:03].
- **Comparer à gain égal.** Metric AB en gain match rapproche le morceau des références masterisées [SOURCE PR-04 2:40–4:41] ; gain match pendant le travail, compensation au dernier limiteur [SOURCE PR-06 54:30–54:36].
- **Stem mastering = entre-deux.** Les stems sont des sous-mixes déjà traités : plus de contrôle qu'un master stéréo, moins qu'un mix complet [SOURCE PR-05 1:10–1:39]. Méthode en deux temps : correction et rééquilibrage des stems, puis passage dans la chaîne finale [SOURCE PR-06 0:55–1:18]. Raison donnée : un défaut du mix qu'on ne pouvait plus corriger au mix [SOURCE PR-06 3:13–3:56].
- **Hygiène de bounce.** Stems ni très forts ni très faibles, sans écrêter [SOURCE PR-05 43:32–44:43] ; queue coupée en fin de bounce à corriger, un peu de silence au début [SOURCE PR-05 35:44–36:28, 37:26] ; export sans warp (ou en haute qualité) et à la fréquence de la session [SOURCE PR-03 14:06–14:39].

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Référence VU | 0 VU = −18 dBFS (−20 possible dans le Dorrough) ; « minus 13 » [ASR ?] écarté | PR-01 1:23, PR-02 4:24–5:12 |
| Recalage des stems | −10 dB sur tous pour atteindre 0 VU | PR-01 6:12–6:38 |
| Compression du kick | ≈ 5 dB, puis make-up au même niveau de crête | PR-01 10:24–10:47 |
| Marge au pré-master | ≈ 6 dB sous le full scale (« −6 dB ») | PR-02 6:00–6:21 |
| Crêtes max | −6 dB ; moyenne « −5 LS » [ASR ?] | PR-04 12:07–12:21 |
| Marge du bounce | 3 à 6 dB ; somme baissée à ≈ −10 sur le bus (« −10 n'est pas une mauvaise idée ») | PR-05 43:12, 43:32–44:43 |
| Marge à l'import des stems | 10 dB, faders bas | PR-05 4:16–5:18 |
| Null test | +35 dB piste / −35 dB master ; piste à ≈ +34 au-dessus de 0 ; « −75 dB » [ASR ?] pour le retour | PR-03 2:02–7:00 |
| Format du null parfait | 32 bits flottants (« forcément flottant » dans Ableton) ; 24 bits fixe : distorsion, pas de null | PR-03 3:41, 11:40 |
| Fréquence d'export | celle de la session (48 kHz chez lui), warp désactivé | PR-03 14:06–14:39 |
| Bus de mastering (PR-05) | mono sous 100 Hz (120 Hz au départ) ; coupe-bas 23 Hz ; coupe-bas doux 12 dB/oct | PR-05 6:00–7:19, 16:03 |
| Dynamique (PR-05) | compresseur de bus 4:1, attaque longue, release rapide ou Auto, < 1 dB de réduction | PR-05 45:09–46:08 |
| Limiteur multibande (PR-05) | ≈ +7 dB au L3 ; gain staging : départ −10 dB, petites hausses, +7 dB au L3 | PR-05 12:10, 47:41 |
| Sonie (PR-05) | broadcast −24 (US) / −23 (Europe) ; le morceau ≈ −11 ; −10/−9 évoqués | PR-05 13:07–13:54 |
| Latence du Maximizer | mode Low Latency « 7,9 » (unité non dite) ; IRC 5 « 649 seconds » puis « 300 » [ASR ? probablement ms] | PR-04 1:06–2:20 |
| Valeurs de PR-06 | « +10 −10 », « 8 dB, au moins 8.4 », « 925 » / « −0.2 », « −40 / −30 », « 06 », « 330 » : toutes [ASR ?], à ne pas reprendre | PR-06 15:38, 54:50–56:17, 1:04:42, 52:46, 1:07:42 |

### Procédure quand la vidéo la donne

1. **Pré-master (PR-01, PR-02, PR-04).** Calibrer le mètre ; recaler les stems au gain d'entrée ; relever crêtes et overs sur tout le morceau ; enlever le limiteur final et garder la chaîne de couleur et de colle ; exporter avec la marge voulue, sans warp, à la fréquence de la session [SOURCE PR-01 4:06–6:38, PR-02 6:30–7:02, PR-04 11:36–12:07, PR-03 14:06].
2. **Ordre écrêtage / limiteur.** Aucune vidéo du thème ne donne l'ordre clipper → limiteur (il est dans OU-01 et OU-02). PR-05 donne l'ordre d'un bus de mastering : mono du bas, coupe-bas, compresseur de colle, EQ, couleur, L3 ; sur le compresseur SSL, attaque longue « pour laisser passer le punch avant le limiteur » [SOURCE PR-05 6:00–12:34, 45:09–45:42]. PR-06 : pas de clipper à ce stade car tout repasse ensuite dans la chaîne analogique [SOURCE PR-06 33:59–34:05].
3. **Passage en stems.** Bounce du mix avec 3 à 6 dB de marge, mastering dans un projet séparé ; correction par stem, bus parallèle sur les drums ; automation de volume si un élément ressort après compression ; contrôle du mid et des sides puis mono avant l'impression ; en cas de retour client, refaire la même chaîne avec le gain d'impression noté [SOURCE PR-05 26:16–27:19, 35:07, 43:12, PR-06 46:23–46:42, 1:01:49–1:07:42].
4. **Mesure de la sonie.** Mesure LUFS dans le projet de mastering [SOURCE PR-05 13:07–13:54] ; A/B à gain égal, compensation au dernier limiteur [SOURCE PR-04 2:40, PR-06 54:30]. Aucune cible de sonie n'est donnée comme règle.

### Écarts et contradictions

**Entre vidéos.**
- **Headroom.** PR-02, PR-04 et PR-05 (3 à 6 dB) demandent de la marge ; PR-03 dit qu'elle est sans importance en 32 bits flottants. Les deux camps ne parlent pas du même format : PR-03 lui-même admet le problème en 24 bits fixe. PR-01 raisonne en niveau moyen (0 VU = −18 dBFS), les autres en crête (interp.).
- **PR-05 se nuance lui-même** : 10 dB de marge à l'import et bus à ≈ −10, mais « 3 à 6 dB » de marge conseillés au bounce ; ce sont deux étapes différentes (interp.).
- **Limiteur pendant l'écriture.** PR-02 : pas de limiteur sur le master bus ; PR-04 en garde un (Ozone 12 Maximizer, IRC Low Latency) en écrivant mais le retire à l'envoi.
- **Mètre.** PR-01 et PR-02 travaillent au VU, PR-03 au dBFS et au null test, PR-05 au LUFS : aucune vidéo ne les relie par une valeur.

**Contradictions avec les skills du projet (règle citée, fichier).**
- **Marge de −6 dBFS.** Le projet ne la fait pas obligatoire : `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` § 3 « Prémaster » dit « Une crête exactement à −6 dBFS n'est pas une condition obligatoire », demande un prémaster « sans normalisation et sans écrêtage involontaire, avec une marge suffisante » et admet qu'« un fichier de travail flottant peut convenir si le flux le supporte » ; `ingenieur-mixage/modules/mastering-outils/GUIDE.md` § Préparer, point 2, dit « ni demander arbitrairement une crête de prémaster à −6 dBFS ». Les cibles indicatives du projet sont une crête **pré-limiteur** de −4 à −6 dBFS (`ingenieur-mixage/modules/live-mix-mastering/references/notes-locales.md`, `ingenieur-mixage/SKILL.md`). PR-03 va plus loin que le projet (marge sans importance) ; PR-02, PR-04 et PR-05 rejoignent les valeurs indicatives, sans en faire une norme.
- **Pourquoi PR-03 ne s'applique pas tel quel (interp.).** `ingenieur-mixage/modules/live-export-wav/GUIDE.md` fixe l'export à **24 bits**, normalisation Off : c'est le cas du PR-03 11:40 (distorsion au-delà de 0 dBFS). Le « sans écrêtage involontaire » du projet reste donc nécessaire dans le fichier. La chaîne du projet contient des étages non linéaires (J37, API-2500, L2) : l'exception de PR-03 8:41–9:24 s'y applique. Un export 32 bits flottant n'est pas décrit dans `live-export-wav` ; à vérifier dans la fenêtre d'export avant de le proposer.
- **Export sans normalisation.** Aucune vidéo du thème ne parle de normalisation : la règle de `live-export-wav` n'est ni confirmée ni contredite.
- **Sonie club indicative −9 à −7 LUFS** (`ingenieur-mixage/SKILL.md`). PR-05 cite ≈ −11 LUFS, −10/−9 évoqués, sur un titre hip-hop/électronique : pas de contradiction nette ; PR-04 et PR-06 ne donnent aucune valeur fiable.
- **Plafond ≤ −1 dBTP.** PR-06 cite « −0.2 » [ASR ?] pour le dernier limiteur : trop douteux pour être une contradiction ; PR-02 à PR-05 ne donnent aucun plafond.
- **Natifs (règle 6 d'`ableton-live-session`).** Aucun natif de mix dans PR-01 à PR-06 hors Utility (tolérée : trim, mono, phase) ; l'export et la démonstration de PR-03 sont des opérations de Live, pas des effets de chaîne.
- **Stem mastering et périmètre.** `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` : « sur un mix stéréo, ne pas promettre de corriger indépendamment des pistes absentes » ; `ingenieur-mixage/modules/mastering-outils/GUIDE.md` : une modification qui dépasse le mastering stéréo « doit être explicitée ». PR-05 et PR-06 retouchent des stems : c'est un périmètre à annoncer, pas un geste de mastering stéréo par défaut.
- **Contournement du limiteur.** Cohérent avec le projet : `ingenieur-mixage/modules/live-mix-mastering/references/notes-locales.md` demande de contourner le L2 de BUS MASTER 3 après avoir noté son état, et le skill de conserver les effets créatifs et la compression du mix (PR-04 11:36–12:07).

### Dans l'installation du projet

Chaîne en place : BUS MASTER 1 (Pro-Q 4 → bx_glue → J37), BUS MASTER 2 (API-2500 parallèle → Ozone Imager 2), BUS MASTER 3 (Tonal Balance Control 3 → SPAN → L2, plafond −1,0 dBFS), Main (Utility 0 dB → Insight 2) ; REF → Main hors limiteur (`ingenieur-mixage/modules/live-mix-mastering/references/notes-locales.md`).

| Geste ou outil de la vidéo | Dans le projet |
|---|---|
| Gain d'entrée des stems (PR-01) | Utility en trim (tolérée) ou gain de clip ; pas les faders, comme le dit la vidéo (les plugins sont pré-fader : (interp.) c'est aussi le cas des devices de Live) |
| VU 0 = −18 dBFS, Waves Dorrough (PR-01, PR-02) | Aucun VU dans l’inventaire ; Dorrough : présence sur le Mac non vérifiée. Mesures disponibles : `lom.py meters` / `levels.sh` (post-fader, relatifs, sous-estiment les crêtes), `analyze_wav.py` (crête sample, RMS, écrêtage), Insight 2 (LUFS, true peak, par capture), WLM Plus (insert) |
| Limiteur d'écriture, Ozone 12 Maximizer (PR-04) | L2 en fin de BUS MASTER 3 (Threshold, Ceiling, Release, ARC exposés) à contourner pour le pré-master ; L4 (Over Sampling exposé, mode True Peak non exposé). Ozone 12 Elements est repéré : ses modules dépendent de l'édition (`ingenieur-mixage/modules/mastering-outils/GUIDE.md`), le Maximizer d'Ozone 12 de PR-04 n'est pas vérifié |
| Metric AB (PR-04) | Présence sur le Mac non vérifiée. Équivalent : REF vers Main hors limiteur, gain ajusté à ±0,5 dB, Tonal Balance Control 3 / SPAN (`ingenieur-mixage/SKILL.md` § 4) |
| Compresseur API, SSL de bus (PR-05) | API-2500 (Thresh, Ratio, Attack, Release exposés), bx_glue (Attack jusqu'à 30, Auto Release, filtre de sidechain), SSLComp (bundle repéré, paramètres non relevés) |
| Mono sous une fréquence (PR-05) | bx_glue Mono Maker Frequency (exposé) ou Utility (mono) ; contrainte du projet : sub mono ≤ 110 Hz, largeur au-dessus de 120 Hz (`ingenieur-mixage/SKILL.md`) |
| EQ Maag, Pultec, coupe-bas (PR-05) | Pro-Q 4 (fenêtre), REQ 6 (paramètres exposés), PuigTec (bundle repéré) |
| Waves L3 (PR-05) | L3 Multi / Ultra (bundles repérés, paramètres non relevés : prober) |
| Waves NLS, 1176 / LA-2A UAD, Distressor, transient designers (PR-05, PR-06) | Présence sur le Mac non vérifiée ; aucun transient shaper tiers repéré (`mixage-par-style-synthese.md`) |
| Imageur, M/S (PR-05, PR-06) | Ozone Imager 2 (Width, Stereoize exposés) ; Pro-Q 4 en M/S (fenêtre) |
| Export (PR-03) | `live-export-wav` : 24 bits, Normaliser Off, REF muette, durée exacte, puis `analyze_wav.py` ; dither : le décider une seule fois, à la réduction finale (`ingenieur-mixage/modules/live-mix-mastering/references/mastering-mesures.md`) |

### Limites

- **Outils non vérifiés** : Waves Dorrough, Metric AB, Waves NLS, UAD (1176, LA-2A, SSL), Distressor, plugin Pulsar, ReaComp (Reaper). Le « gold clip » de PR-06 est [ASR ?] (peut-être GClip) : aucune équivalence à poser.
- **[ASR ?]** : « minus 13 » (PR-01), « −75 dB » (PR-03), « 649 seconds » / « 300 » et « −5 LS » (PR-04), toutes les valeurs de PR-06 ; l'unité de la latence « 7,9 » est non dite.
- **Vidéos presque sans valeurs** : PR-06 (« peu de valeurs chiffrées », beaucoup de passages musicaux). PR-04 donne des niveaux de kick sans valeur de fader.
- **Hors périmètre** : aucun ingé mastering techno ou DnB sur un export complet (bit depth, dither, format de livraison) ; le dither n'est dit qu'en OU-04 ; pas de vidéo française d'ingé reconnu sur la préparation du mix.
- **Titres listés mais non ouverts par le corpus** (Dan Worrall, Strob, Streaky, Distinct Mastering, Sean Divine) : rien n'en est tiré ici.
- **À vérifier à l'écran** : 4:06 et 6:38 de PR-01, 4:24–5:07 de PR-02, 4:06 de PR-03 (options d'export), 1:06 de PR-04, 12:29 de PR-05, 54:50–56:17 de PR-06.

## Outils pros

Six vidéos (OU-01 à OU-06), lues sur transcription, son coupé : **rien n'a été entendu**. Elles montrent des outils précis : clippers (OU-01, OU-02), compresseur de bus SSL (OU-03), chaîne tout natif de Live (OU-04), Ozone 11 (OU-05), Pro-MB (OU-06). Trois d'entre elles utilisent des natifs de Live (OU-02, OU-03, OU-04) et plusieurs outils cités ne sont pas repérés sur le Mac : voir « Dans l'installation du projet ». Les niveaux « RMS » des vidéos ne sont pas des LUFS.

### Ce que le corpus retient

- **Deux clippers, un en bus drums, un sur le bus stéréo (Pretolesi).** Lift Mix sur le bus drums, Lift Master sur le bus stéréo, objectif −4 RMS avec deux plugins ; clipping en mode 3 sur le mid seulement pour ne pas détruire les transitoires ni ce qui est hors du mono ; mode 2, plus doux, en stéréo sur le bus final, qui sert de plafond « ni hard ni soft » [SOURCE OU-01 0:33–1:23, 3:34–5:12]. Vidéo liée à une promo Acustica ; la méthode et les valeurs sont données.
- **Clipper avant le limiteur.** Une série de clippers (pistes, bus, juste avant Pro-L 2) fait travailler le limiteur beaucoup moins, ce qui permet moins d'attaque et une release plus courte [SOURCE OU-02 5:45–6:52]. Avec Pro-L 2 seul, le son est détruit à −8/−4 LUFS ; allonger la release et raccourcir l'attaque rend le son « splatty » [SOURCE OU-02 2:18–3:18]. Chaque ajout de son oblige à revérifier les étages de clipping [SOURCE OU-02 22:48–23:04].
- **Transparent jusqu'à environ 10 dB sur le kick.** Saturator en Analog Clip : +10/−10 gagne environ 6 dB sans différence audible, +15/−15 environ 10 dB mais la saturation s'entend ; KClip 3 transparent à 13/−13, distorsion audible vers 14 [SOURCE OU-02 9:53–15:11]. Contre-exemple : une queue de réverbe, où le clipper s'entend [SOURCE OU-02 18:55–22:40].
- **Limites de la sonie.** −5 LUFS ne convient pas à ce morceau : la musique qui supporte ces niveaux a déjà de la distorsion harmonique et un spectre penché vers l'aigu [SOURCE OU-02 23:04–24:23]. L'EQ avant le limiteur n'a pas permis de dépasser −10 LUFS sans distorsion sur ce titre [SOURCE OU-02 4:00–5:30]. −14 LUFS suffirait pour le streaming seul [SOURCE OU-05 15:42–15:55].
- **Compresseur de bus type SSL « à la techno ».** 4:1, release Auto, attaque 30 ms (en dessous, les transitoires du kick s'écrasent), juste « chatouiller » pour la colle et la largeur ; variante « slam » : release la plus rapide, attaque la plus lente, sans coupe-bas de sidechain, signal envoyé très fort [SOURCE OU-03 1:27–2:47]. Selon la vidéo, le hardware garde plus de poids dans le bas ; les plugins élargissent mais retirent un peu au signal mono [SOURCE OU-03 7:04–8:21].
- **Chaîne tout natif (Live 10).** Écouter en 4 bandes, référence du même style [SOURCE OU-04 1:11–1:30] ; EQ en M/S via deux Utility mappés [SOURCE OU-04 11:21–11:40] ; petits mouvements d'EQ (1,36 dB « déjà beaucoup ») [SOURCE OU-04 14:09] ; double limiteur dont le premier sert de détecteur [SOURCE OU-04 18:23–19:48].
- **Plafond à −1 dB pour la diffusion en ligne.** Selon OU-04, la conversion MP3/OGG/AAC ajoute environ 1 dB et peut écrêter [SOURCE OU-04 20:16–21:47]. OU-02 règle Pro-L 2 à −1 dBTP avec oversampling [SOURCE OU-02 1:19–2:04]. OU-05 descend à −0,01 dBFS avec true peak [SOURCE OU-05 17:35–17:53].
- **Assistant de mastering = point de départ.** Master Assistant sur la boucle du passage le plus fort, gain match pour comparer, courbe cible perso car le premier résultat est trop dur ; EQ de l'assistant ≈ ±1 dB ; plusieurs modules retirés après écoute en Delta (Impact, Stabilizer), Dynamic EQ conservé [SOURCE OU-05 0:51–14:31].
- **Pro-MB sur un pré-master reçu.** Sidechain du sub par le kick sans les stems : déclenchement de la bande sur « Free », plage de déclenchement calée sur la fondamentale du kick, attaque 0 %, release rapide, lookahead poussé [SOURCE OU-06 0:21–0:51, 2:46–3:45, 6:23–7:11].

### Valeurs dites

| Paramètre | Valeur dite | Source |
|---|---|---|
| Repères de sonie | streaming ≈ −12/−14 LUFS ; Beatport et mixes club ≈ −8 à −4 LUFS | OU-02 0:07–0:21 |
| Pro-L 2 | true peak −1 dBTP, oversampling activé (mètre LUFS utilisé) | OU-02 1:19–2:04 |
| Limite sans clipper | impossible de dépasser −10 LUFS sans distorsion (ce titre) ; −5 LUFS refusé | OU-02 4:00–5:30, 23:04 |
| Saturator Analog Clip, kick | +10/−10 : crête −3,64 → −9,61 dB (≈ 6 dB) ; +15/−15 ≈ 10 dB, audible ; transparent jusqu'à ≈ 10 dB | OU-02 9:53–13:13 |
| KClip 3, kick | 13/−13 transparent ; distorsion audible vers 14 | OU-02 14:36–15:11 |
| KClip 3, bus drums | 13/−13 : crête −11,2 dB, ≈ 1 dB gagné en plus | OU-02 16:28–17:31 |
| KClip 3, master avant limiteur | crête −5,6 dB sans clip, « nettement moins » avec (valeur non dite) | OU-02 17:54–18:45 |
| Queue de réverbe | Glue attaque minimale, seuil ≈ −12 ; KClip Crisp 8/−8 | OU-02 18:55–22:40 |
| Lift Mix, bus drums | mode 3 sur le mid ; entrée +12 dB, saturation 80, clipping 100, sortie baissée ; haut ouvert vers 7–10 kHz | OU-01 0:33–1:33 |
| Sonie de OU-01 | objectif −4 RMS ; oscille −4,5 à −5 RMS ; bypass du Lift drums : RMS « f dB » [ASR ?] mais perception 2 à 3 dB | OU-01 0:33, 2:14–2:47 |
| Lift Master | clipping stéréo mode 2 ; ouverture à 2 kHz | OU-01 3:34–3:55 |
| Glue / SSL classique | 4:1, release Auto, attaque 30 ms | OU-03 2:28–2:47 |
| « Slam » | release la plus rapide, attaque la plus lente, 4:1, sans HPF de sidechain | OU-03 1:27–1:36 |
| Largeur perçue (pad gaté) | 15 à 20 % plus large avec le compresseur | OU-03 3:28–3:56 |
| Décentrage du kick | ±1 dB entre 30 et 80 Hz sur un canal | OU-03 10:51–11:08 |
| Crêtes du master | −10 à −6 dB sur la partie la plus forte, référence au même niveau de crête | OU-04 1:58–2:30 |
| Compresseur (OU-04) | attaque 5–10 ms (« tick »), 25–50 voire 60 (épais), retient ≈ 20 ms ; release de 1 à 10 ; ratio ramené à 2:1 (démo extrême : 10:1, attaque 0) | OU-04 6:17–9:14 |
| EQ M/S (OU-04) | boue 150–600 Hz (mid) ; présence 1–3 kHz ; coupe-bas prudent dans le side | OU-04 12:48–15:25 |
| Limiteur 1 (détecteur) | gain jusqu'à ≈ 7,5 dB, puis reculer un peu | OU-04 19:28 |
| Plafond (OU-04) | −1 dB (MP3/OGG/AAC ≈ +1 dB) | OU-04 20:16–21:47 |
| Sonie (OU-04) | cible RMS Ableton −9 à −7 ; −7/−8 dans le drop ; ≈ −2 dB de limitation pour ≈ −7 RMS | OU-04 22:12–23:33 |
| Export (OU-04) | 24 ou 16 bits, dither POW-r 3 | OU-04 25:16–25:29 |
| Entrée Ozone (OU-05) | 44,1 kHz / 24 bits, aucune crête > 0, marge ; EQ assistant ≈ ±1 dB ; coupe-bas 24 dB/oct, voire 12, plutôt que 48 ; Clarity réduit d'≈ 5 % | OU-05 0:17, 3:49–4:59, 9:20–10:31 |
| Maximizer (OU-05) | IRC (« modern » [ASR ?]), Fast/Loud, True Peak ; emphase transitoire ≈ 50 ; plafond −0,01 dBFS (appris −0,3 « à l'époque du L2 ») | OU-05 16:21–17:53 |
| Pro-MB | range −30 dB (cas extrême) ; pente 48 dB/oct ; limite basse de bande « 36 » [ASR ? unité non dite] ; attaque 0 %, release rapide | OU-06 2:04–6:33 |

### Procédure quand la vidéo la donne

1. **Ordre écrêtage → limiteur.** OU-02 : clippers sur les pistes, les bus et le master, juste avant le limiteur ; le limiteur travaille moins, attaque et release se règlent plus court ; revérifier chaque étage dès qu'un son est ajouté [SOURCE OU-02 5:45–6:52, 22:48–23:04]. OU-01 : Lift Mix sur le bus drums, Lift Master sur le bus stéréo comme plafond [SOURCE OU-01 0:33, 4:39–5:12]. OU-04 : Color Limiter → Compressor → Utility → EQ Eight → Limiter → Limiter ; le premier limiteur (lookahead très court) détecte, le dernier fixe le plafond [SOURCE OU-04 0:21–0:31, 18:23–21:47].
2. **Réglage d'un clipper (OU-02).** Entrée et sortie liées ; monter jusqu'à l'audibilité de la distorsion, puis revenir ; vérifier en « Wet » ce qui est écrêté ; tester la queue de réverbe, où le clip s'entend [SOURCE OU-02 14:36–15:58, 18:55–22:40].
3. **Colle de bus (OU-03).** Mêmes réglages sur Glue et SSL : release la plus rapide, ratio 4, attaque 30 ms ; pousser jusqu'à ce que le bas perde sa vie, revenir, compenser au gain ; vérifier le centrage du kick à l'analyseur L/R [SOURCE OU-03 4:35–5:43, 9:16–10:18].
4. **Assistant (OU-05).** Boucle du drop → analyse → gain match → mode avancé ; retirer ce qui ajoute du grave inexistant ou enlève le poids du kick (test en Delta) ; couper le gain match pour régler le niveau final avec mètres RMS + crête ou LUFS intégré / court terme [SOURCE OU-05 0:51–15:06].
5. **Sidechain du sub en pré-master (OU-06).** Bande sur le sub, seuil baissé, déclenchement « Free » calé sur la fondamentale du kick, bande solotée pour écouter ce qui est creusé, pente 48 dB/oct, attaque 0 %, release rapide [SOURCE OU-06 2:04–6:33].
6. **Mesure de la sonie.** OU-02 lit le LUFS dans Pro-L 2 ; OU-04 lit le RMS dans les mètres d'Ableton ; OU-05 propose RMS + crête ou LUFS intégré / court terme [SOURCE OU-02 1:19, OU-04 22:12, OU-05 14:37–15:06].

### Écarts et contradictions

**Entre vidéos.**
- **Sonie.** OU-02 cite −8 à −4 LUFS pour Beatport et le club mais refuse −5 LUFS sur son titre ; OU-04 vise −9 à −7 en RMS ; OU-01 vise −4 RMS ; OU-05 veut « plus fort » que −14 LUFS sans chiffre. Ces valeurs mélangent RMS et LUFS : non comparables (interp.).
- **Plafond.** −1 dB (OU-04), −1 dBTP (OU-02), −0,01 dBFS avec true peak (OU-05).
- **Clipper contre limiteur.** OU-01 et OU-02 écrêtent avant le limiteur ; OU-04 n'a pas de clipper, seulement deux limiteurs.
- **Coupe-bas.** OU-05 : 24 dB/oct, voire 12, pas 48 ; OU-06 pose 48 dB/oct pour une bande de sidechain ; usages différents (interp.).
- **Colle.** OU-03 recommande de ne pas filtrer le sidechain pour le « slam » ; OU-04 règle le filtre de sidechain interne pour que la réduction ne suive plus le kick [SOURCE OU-04 9:50–11:11].

**Contradictions avec les skills du projet (règle citée, fichier).**
- **Natifs (règle 6 d'`producteur-live/SKILL.md`).** OU-04 est une chaîne entièrement native (Color Limiter, Compressor, EQ Eight, deux Limiter) ; OU-02 passe par le Saturator et le Glue Compressor ; OU-03 par le Glue Compressor. Le projet n'autorise pas de nouvel effet natif dans les chaînes de mix et de master (`ingenieur-mixage/modules/live-mix-mastering/references/notes-locales.md`) ; seule l'Utility (mono, trim, phase) est tolérée. On garde la logique, on traduit par des plug-ins tiers.
- **Plafond ≤ −1 dBTP** (`ingenieur-mixage/SKILL.md`, `ingenieur-mixage/modules/mixage/GUIDE.md`). OU-05 : −0,01 dBFS, contradiction ; OU-04 (−1 dB) et OU-02 (−1 dBTP) concordent. Le L2 du projet a un plafond en sample peak : −1,0 dBFS ne garantit pas le true peak, qu'on lit dans Insight 2 (`ingenieur-mixage/modules/mastering-outils/references/notes-locales.md`).
- **Sonie club indicative −9 à −7 LUFS.** OU-02 donne −8 à −4 LUFS comme repère de club : la partie −6 à −4 dépasse l'indicatif du projet ; OU-01 (−4 RMS) aussi, en RMS. OU-02 lui-même refuse −5 LUFS sur son titre. Ces cibles ne sont pas imposées (`ingenieur-mixage/modules/live-mix-mastering/references/mastering-mesures.md`).
- **−14 LUFS.** `ingenieur-mixage/modules/mastering-outils/GUIDE.md` : ne pas l'imposer à tous les styles ; OU-02 et OU-05 le donnent comme streaming seulement : accord.
- **Mètres de Live.** OU-04 règle la sonie au RMS d'Ableton : `mastering-mesures.md` dit que les vu-mètres de Live ne certifient pas l'export et qu'on ne déduit pas les LUFS du RMS.
- **Glue sans filtre de sidechain (OU-03).** `ingenieur-mixage/modules/mastering-outils/references/outils-et-reglages.md` demande de vérifier que la détection ne fait pas pomper tout le master à chaque grave ; `ingenieur-mixage/SKILL.md` garde le grave mono et centré (OU-03 10:51 parle du même risque). Le « slam » est donc à tester avec corrélation 30–120 Hz (SPAN ou `kick_bass_check.py`).
- **Pro-MB en pré-master (OU-06).** `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` : sur un mix stéréo on ne promet pas de corriger indépendamment des pistes absentes ; `ingenieur-mixage/SKILL.md` : sidechain plutôt qu'EQ, à la source. Dans le projet, le Set a les pistes : le sidechain du sub se règle au mix (`kick-bass-equilibre`) ; le geste d'OU-06 est un secours sur fichier reçu, à annoncer comme tel.
- **Objectif −4 RMS en deux plugins (OU-01).** `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` : « ne pas remplacer le mixage par une limitation intensive » ; `ingenieur-mixage/modules/mastering-outils/GUIDE.md` : un clipper n'est pas une étape obligatoire.
- **Dither POW-r 3 (OU-04).** Pas de contradiction : `mastering-mesures.md` autorise un dither à la réduction finale vers un PCM entier, une seule fois ; il ne se cumule pas avec celui du limiteur.

### Dans l'installation du projet

| Outil de la vidéo | Statut sur le Mac | Équivalent installé |
|---|---|---|
| Acustica Diamond Lift (OU-01) | présence sur le Mac non vérifiée | RazorClip (GAIN 0–24 dB, OUTPUT ±24 dB, MIX, MODEL exposés ; fonctions à lire dans son manuel) pour l'écrêtage ; J37 pour la saturation ; Pro-Q 4 ou REQ 6 pour le haut 7–10 kHz. Écrêtage du seul mid : aucun équivalent identifié |
| Kazrog KClip 3 (OU-02) | présence sur le Mac non vérifiée | RazorClip (interp.) ; la paire entrée/sortie liée de KClip n'a pas d'équivalent établi (GAIN et OUTPUT sont séparés) |
| FabFilter Pro-L 2 (OU-02) | non repéré (`inventaire-local.md`) | L4 (Threshold, Ceiling, Over Sampling exposés ; mode True Peak à prober) ou L2 en fin de BUS MASTER 3 ; mètre LUFS : Insight 2 ou WLM Plus |
| Saturator, Glue Compressor, Compressor, Color Limiter, EQ Eight, Limiter (OU-02, OU-03, OU-04) | natifs : interdits comme nouveaux effets | Glue : bx_glue (Attack jusqu'à 30, donc « la plus lente » = 30 ; Auto Release ; filtre de sidechain ; Mono Maker ; Mix) ou API-2500 ; Saturator / Color Limiter : J37 ou RazorClip (couleur différente, interp.) ; EQ Eight : Pro-Q 4 (M/S, fenêtre) ou REQ 6 ; Limiter : L2 / L4 |
| UAD SSL G Bus Compressor (OU-03) | présence sur le Mac non vérifiée | SSLComp (bundle repéré, paramètres non relevés), bx_glue, API-2500 |
| AudioScape Buss Compressor, hardware (OU-03) | sans objet | aucun ; le poids du bas et le centrage se vérifient par corrélation (SPAN) |
| Utility en mono et side seul (OU-04) | natif toléré | Utility (mono, trim, phase) ; largeur : Ozone Imager 2 (Width, Stereoize exposés) |
| Ozone 11 Advanced : Master Assistant, EQ, Dynamic EQ, Imager, Maximizer (OU-05) | non vérifié ; sont repérés Ozone 12 Elements, Ozone 11 Elements, Ozone 11 Equalizer | Assistant : Ozone 12 Elements, modules selon l'édition ; EQ : Pro-Q 4 ou Ozone 11 Equalizer ; Dynamic EQ : TDR Nova, Pro-Q 4 dynamique ou soothe3 ; Imager : Ozone Imager 2 ; Maximizer : L2 / L4 ; courbe cible : Tonal Balance Control 3. Master Rebalance, Impact, Clarity, Stabilizer : aucun équivalent identifié |
| FabFilter Pro-MB (OU-06) | non repéré (`inventaire-local.md`) | bande dynamique de Pro-Q 4 avec sidechain externe (à vérifier : fenêtre seulement), TDR Nova (EQ dynamique), Waves LinMB / C4 / C6 / F6 (bundles repérés ; F6 avec sidechain à router) |

- **Chaîne cible (interp.).** Un clipper tiers, s'il est retenu, se place avant le L2 de BUS MASTER 3 ; Insight 2 reste en bout de Main ; le fichier est ensuite analysé (`ingenieur-mixage/modules/live-export-wav/GUIDE.md`, `analyze_wav.py` : crête sample, RMS, écrêtage, sans LUFS ni true peak).
- **Éviter l'empilement** : EQ dynamique, soothe3 et multibande sur la même zone sans problème distinct (`ingenieur-mixage/modules/mastering-outils/GUIDE.md`) ; une seule solution de limitation comparée à la fois (`waves-mastering.md`).
- **Grave** : le sidechain sub / kick d'OU-06 respecte la règle des deux instruments (sub mono) seulement s'il est fait au mix ; au pré-master, contrôler la corrélation 30–120 Hz.

### Limites

- **Outils non vérifiés sur le Mac** : Diamond Lift, KClip 3, Pro-L 2, Pro-MB, Ozone 11 Advanced, UAD SSL G, AudioScape, Ozone 12 Maximizer (OU-05 et PR-04 cités). RazorClip est repéré mais son protocole est à lire avant tout usage comme clipper.
- **[ASR ?]** : « f dB » (OU-01 2:38), IRC « modern » (OU-05), « 100 ms » d'Impact (OU-05), limite basse « 36 » sans unité (OU-06).
- **Mètres** : OU-01 et OU-04 donnent des RMS sans dire quel mètre ; ne pas les convertir en LUFS.
- **Valeurs partielles** : crête du master avec KClip non chiffrée (OU-02 17:54–18:45) ; OU-03 n'a aucun chiffre de seuil ni de réduction (« à vérifier à l'écran » 4:53–5:43) ; OU-04 : réglages d'EQ M/S sans courbe chiffrée ; OU-05 : aucun LUFS final dit.
- **Corpus** : pas de vidéo dédiée au Pro-L 2 par un ingé mastering électronique ; aucun StandardCLIP ni GClip vérifié ; Ozone : une seule session réelle (DnB), rien en français, rien en house ou techno ; Pretolesi seul ingé reconnu qui démontre des outils (OU-01, promo Acustica).
- **Écarté, non retenu** : vidéo Kazrog sur KClip 3 (r4d0F7VaW7E), dont le corpus note qu'un second clipper à 0 dBFS non suréchantillonné ajoute des crêtes inter-échantillons (+1,8 dB dans la démo) ; à garder en tête pour le plafond ≤ −1 dBTP, sans valeur reprise ici.
- **À vérifier à l'écran** : 1:25 et 3:37 de OU-01 ; 2:04, 10:19 et 14:52 de OU-02 ; 1:27 de OU-03 ; 3:33, 9:14–10:43 et 19:28 de OU-04 ; 16:21–17:19 de OU-05 ; 2:23 et 5:23–5:47 de OU-06.

## Contradictions avec les skills du projet, en un tableau

Les vidéos sont des points de vue d'orateurs, souvent des producteurs et non des ingénieurs de mastering ; le projet garde ses règles. Chaque ligne renvoie à la section du thème qui la détaille. Plafond, sonie et mono sont à **trancher avec l'utilisateur** : la synthèse du mixage par style (`../../mixer-house-professionnel/references/mixage-par-style-synthese.md`) relève déjà les mêmes écarts.

| Sujet | Ce que disent les vidéos | Règle du projet | Fichier de la règle |
| --- | --- | --- | --- |
| Plafond | −0,1 ou −0,2 dB (CM-04) ; −0,01 dBFS avec true peak (OU-05) ; limiteur « vers 0 dB » (BA-06) ; masters du commerce à +1,6 à +2,4 dBTP, le −1 dBTP de Spotify étant « pour les distributeurs » (LO-04) ; « minus three, minus four » [ASR ?] (TO-05) | plafond −1,0 dBFS et ≤ −1 dBTP ; −1 dBTP et moins de −2 dBTP si plus fort que −14 LUFS pour le streaming | `ingenieur-mixage/SKILL.md` ; `ingenieur-mixage/modules/mixer-house-professionnel/references/mastering-streaming-et-club.md` |
| Mono du grave | tout sous 200 Hz (CM-03) ; test à 200 Hz et côtés gardés jusqu'à 35 Hz en bass music (BA-04) ; ≈ 50 Hz ou pas du tout (BA-05) ; côtés coupés dès 80 Hz (TO-01) ou 45 Hz (TO-06) ; 111 Hz (CM-04) ; 100-120 Hz (PR-05) | sub mono ≤ 110 Hz, largeur au-dessus de 120 Hz, corrélation ≥ 0 dans 30-120 Hz | `ingenieur-mixage/SKILL.md` ; `ingenieur-mixage/modules/mixage/GUIDE.md` |
| Sonie | −6,9 et −6,8 (CM-03) ; −5 (LO-01) ; −8 à −5 (LO-02) ; −5,6 (LO-05) ; −8 à −4 pour un club (OU-02) ; −4,3 [ASR ?] (TO-02) ; −4 RMS (OU-01) | club −9 à −7 LUFS indicatif, streaming ≈ −14, à confirmer avec l'utilisateur | `ingenieur-mixage/SKILL.md` ; `ingenieur-mixage/modules/live-mix-mastering/references/notes-locales.md` |
| Marge de pré-master | « sans importance en 32 bits flottants » (PR-03) ; 3 dB suffisent (MX-02, RE-06) ; −6 dB demandés (PR-02, PR-04, PR-05) | crête pré-limiteur ≈ −4 à −6 dBFS indicatif ; « −6 dBFS pas obligatoire » mais pas d'écrêtage involontaire ; export 24 bits, normalisation Off | `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` ; `ingenieur-mixage/modules/mastering-outils/GUIDE.md` ; `ingenieur-mixage/modules/live-export-wav/GUIDE.md` |
| Export | WAV 16 bits (CM-04) | 24 bits, sans normalisation ; un seul dither, à la réduction finale | `ingenieur-mixage/modules/live-export-wav/GUIDE.md` ; `ingenieur-mixage/modules/live-mix-mastering/references/mastering-mesures.md` |
| Effets natifs de Live | chaîne tout natif (OU-04) ; Saturator, Glue Compressor (OU-02, OU-03) ; Vinyl Distortion, Roar, EQ Eight M/S (BA-02, BA-04) ; Spectrum (RE-03) ; EQ Eight et Envelope Follower (TO-03) ; largeur par Utility (CM-05) | pas de nouvel effet natif dans les chaînes de mix ; Utility toléré pour trim, mono, phase ; instruments natifs tolérés | `producteur-live/SKILL.md` (règle 6) |
| Ordre du travail | bus master d'abord (MX-02) ; sonie poussée au master (CM-04, CM-06) ; limiteur « en premier » (CM-02) | source d'abord, bus et master en dernier ; L2 en fin de BUS MASTER 3 | `ingenieur-mixage/modules/mixage/GUIDE.md` ; `ingenieur-mixage/modules/mastering-outils/references/notes-locales.md` |
| Sub et basse | « une basse » avec une octave en 2e oscillateur (BA-01, BA-02) ; aucun coupe-bas sur la basse, coupe sur le master (BA-02) | sub et basse médium dans deux instruments ; coupe-bas de basse 60-80 Hz si le kick tient le grave | `AGENTS.md` ; `producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md` ; `producteur-rythmique/modules/construire-low-end-electronique/GUIDE.md` |
| Partage du grave | fondus audio sur le sub, EQ plutôt que sidechain (MX-01, MX-04, MX-06) | sidechain plutôt qu'EQ à la source | `ingenieur-mixage/modules/mixage/GUIDE.md` (étape 2) |
| Une couleur par chaîne | EQ colorée, bande, saturation cumulées au master (MX-01, MX-02) | une seule couleur par chaîne | `ingenieur-mixage/SKILL.md` |
| Tolérance de niveau A/B | 0,1 dB d'écart fausse la préférence (RE-01) | REF à ±0,5 dB : la règle du projet est plus lâche que la vidéo ; viser le plus proche possible | `ingenieur-mixage/SKILL.md` § 4 |
| Mesure de la sonie | RMS des mètres de Live (OU-04) ; RMS sans mètre précisé (OU-01, CM-02) | ne pas déduire les LUFS du RMS ; mesurer le fichier livré | `ingenieur-mixage/modules/live-mix-mastering/references/mastering-mesures.md` ; `ingenieur-mixage/modules/mastering-outils/references/mesures-et-livraison.md` |
| Périmètre du stem mastering | retouche des stems (PR-05, PR-06, OU-06) | sur un mix stéréo, ne pas promettre de corriger des pistes absentes ; l'annoncer | `ingenieur-mixage/modules/live-mix-mastering/GUIDE.md` ; `ingenieur-mixage/modules/mastering-outils/GUIDE.md` |

**Là où les vidéos rejoignent le projet** : un seul niveau d'écoute et une référence hors limiteur (RE-01 à RE-03) ; pics traités au mix et clip par piste (LO-02, LO-03) ; limiteur d'écriture retiré pour le pré-master mais couleur du bus gardée (PR-04) ; −14 LUFS réservé au streaming (LO-04, OU-02, OU-05) ; Spotify −1 dBTP et plus bas (OU-02, OU-04).


## Limites générales

- **Rien d'écouté, aucun réglage d'écran confirmé.** Les adjectifs (« gel », « rond », « blocky », « mou ») sont ceux des orateurs.
- **Les échelles de niveau ne se convertissent pas** : LUFS, RMS (mètre souvent non précisé), VU (0 VU = −18 dBFS) et crêtes sont mélangés dans les vidéos. Aucune conversion n'est proposée ici.
- **Valeurs [ASR ?] à ne pas recopier** : gain RX « −1.35 » et « minus 78 left » (CM-01) ; multibande « 120 Hz » (CM-02) ; shelf d'air « à partir de 17 » (CM-06) ; −4,3 LUFS et « 6 dB » (TO-02) ; plafond de TO-05 ; mono maker « ≈ 7 », « a tea » et LA-2A « 340 D » (MX-01, MX-02, RE-06) ; niveau d'écoute « 70-80 dB SPL » (RE-03, lu « 1780 ») ; « minus 13 » (PR-01) ; « −75 dB » (PR-03) ; « 649 seconds » et « 300 » (PR-04) ; presque toutes les valeurs de PR-06 ; « f dB » (OU-01) ; limite basse « 36 » sans unité (OU-06) ; unité « dB » de −7,8 (RE-02), ajoutée par l'étude.
- **Incohérence interne de LO-03** : limiteur seul ≈ 3,5 dB (27:11) contre « 2 dB de moins » puis ≈ 3 dB restants (35:52), non résolue sans l'écran.
- **Outils absents de l'inventaire** (présence sur le Mac non vérifiée) : Pro-L et Pro-L 2, Pro-MB, KClip 3, Diamond Lift, Ozone 7, 8, 9 et 11 Advanced (les Elements 11 et 12 sont repérés, leurs modules ne sont pas vérifiés), true:balance, Perception AB, Metric AB, Magic AB, Decibel, Clarity, Sonarworks, Mastering The Mix (LEVELS, BASSROOM, Bass Space), PHA-979, Basslane, Gullfoss, Michelangelo, Fuel, RX, Kickstart, LFO Tool, Master Plan, Waves NLS, UAD (SSL, 1176, LA-2A, Shadow Hills), AMEK, BAX, elysia, Dorrough. Chaque section donne l'équivalent installé quand il existe (Pro-Q 4, REQ 6, API-2500, L2, L4, J37, bx_glue, soothe3, Ozone Imager 2, Insight 2, Tonal Balance Control 3, SPAN, RazorClip, TheBus, ShaperBox 3, Pro-C 3, TDR Nova, ValhallaVintageVerb).
- **Pro-Q 4, soothe3, SPAN, Tonal Balance Control 3 et Insight 2 ne se règlent que par la fenêtre** : ces chaînes ne sont reproduites que sur capture.
- **Manques du corpus** : aucune cible club et streaming pour un même titre ; aucun true peak chiffré sur un titre de DnB ; pas de multibande appliquée au seul grave en master ; pas de calibration SPL en direct ; peu de vidéos en français (LO-04, LO-06, RE-01, CM-06) ; plusieurs vidéos sont des promotions de formation ou de plug-in (LO-04, OU-01, RE-05).
- **Le test d'écoute revient à l'utilisateur** : un agent peut produire des rendus et des mesures de crête, d'écrêtage et de RMS (`analyze_wav.py`), mais ni LUFS, ni true peak, ni écoute (règle 4 d'`AGENTS.md`).
