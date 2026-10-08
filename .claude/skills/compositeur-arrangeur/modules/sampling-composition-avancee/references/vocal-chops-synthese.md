# Vocal chops : synthèse de 65 tutoriels par usage

Synthèse du 05/10/2026 du corpus `tutoriels-vocal-chops.md` : 65 vidéos YouTube en cinq thèmes. Montée (MO-01 à MO-15), Tension (TE-01 à TE-05), Surprise (SU-01 à SU-15), Rythme (RY-01 à RY-15), Ambiance et reverse (AR-01 à AR-08 pour l'ambiance, AR-09 à AR-15 pour le reverse).
L'étude a été faite dans Claude in Chrome sur le Mac. Les transcriptions et les descriptions ont été lues, son coupé : **rien n'a été entendu**.
[SOURCE XX-nn] = dit dans la vidéo (transcription ou description). (interp.) = mon interprétation. [ASR ?] = transcription automatique douteuse.
Les vidéos déjà étudiées pour Simpler et Sampler sont exclues du corpus. Synthèses voisines : `simpler-synthese.md` et `sampler-synthese.md`. Capture audio : `../../../sound-designer-serum/modules/resampling/GUIDE.md`.
Outils filmés : Ableton Live surtout, puis FL Studio, Logic Pro, Pro Tools et Bitwig ; une seule vidéo Serum 2 (AR-03) ; aucune Maschine.
Notes en numérotation Ableton : C3 = 60, donc C1 = 36. Le numéro MIDI fait foi.

## Ce que dit le corpus avant tout

- **Un fragment et un paramètre qui bouge.** La plupart des effets viennent d'un mot ou d'une syllabe, puis d'une seule automation : cadence, hauteur ou longueur de boucle [SOURCE MO-01, MO-04, MO-08, TE-02, AR-02].
- **Imprimer, puis retravailler.** Consolidate, Freeze/Flatten, resampling ou bounce reviennent dans tous les thèmes [SOURCE MO-08, MO-09, SU-01, SU-02, RY-03, RY-13, AR-07, AR-09, AR-12].
- **Peu de chops, répétés, et une variation en fin de cycle.** « Two or three chops » [SOURCE RY-05] ; 5 chops seulement [SOURCE RY-14] ; structures ABAC ou A B A C A B A E [SOURCE SU-14, SU-05] ; question puis réponse en fin de mesure [SOURCE TE-04].
- **Tonalité d'abord.** Accorder le chop avant de l'utiliser : transposition, Tuner, Auto Shift ou Auto-Tune [SOURCE SU-05, SU-06, SU-11, SU-14, RY-01, RY-03, RY-05, RY-14, AR-04, AR-08]. TE-03 choisit une note « dans la tonalité ».
- **Écrire contre le reste de la piste.** Construire les chops sur drums et basse seuls [SOURCE RY-09] ; basse simple pour laisser de la place [SOURCE RY-05, RY-03] ; chop filtré en couche de fond, pas en lead [SOURCE RY-06, AR-01, AR-08].
- **Le silence fait partie du geste.** Voix coupée avant le drop [SOURCE MO-01, TE-03] ; creux de volume et de basses sur le bus du riser [SOURCE MO-12] ; un seul mot quand tout s'arrête [SOURCE SU-03].

## Montée

- Roll qui double à chaque palier sur le premier mot de la section suivante : 1/2, 1/4, 1/8, 1/16, puis 1/32 ; le clip est raccourci à chaque palier [SOURCE MO-01]. Même roll joué en notes MIDI dans un sampler, pour rester calé [SOURCE MO-02].
- Boucle qui raccourcit : automation de la fin de boucle [SOURCE MO-03] ou de Loop Length dans Simpler jusqu'à ≈ 10 % [SOURCE MO-04]. MO-04 ajoute un Pitch Bend par enveloppe de clip MIDI, de 0 au maximum.
- Arpeggiator en mode Free devant Sampler ; Rate automatisé de ≈ 700 ms à ≈ 20 ms, puis ralenti à l'arrivée de la section [SOURCE MO-05].
- Syllabe dupliquée bout à bout, crossfades ou non, consolidée, puis enveloppe de Transposition [SOURCE MO-08, MO-10]. Chop alterné endroit/envers pour un son continu [SOURCE MO-09].
- Une macro pour tout : boucle plus courte, pitch, formant et filtre ensemble [SOURCE MO-07, Bitwig].
- Gate 1/16 en parallèle avec le signal sec, puis frequency shifter [SOURCE MO-13]. Snares posées sur chaque attaque de la voix [SOURCE MO-03].
- Accompagner : reverb longue qui monte, passe-haut résonant qui s'ouvre [SOURCE MO-10, MO-11] ; bus du riser qui baisse et perd ses basses [SOURCE MO-12].
- Divergence : MO-11 passe en Stretch pour monter sans accélérer ; MO-06 cherche au contraire l'illusion d'accélération du re-pitch. Deux buts, deux réglages.

| Paramètre | Valeur | Source |
|---|---|---|
| Paliers de roll | 1/2 → 1/4 → 1/8 → 1/16 → 1/32 | MO-01 |
| Roll en MIDI | noires 4 mesures, croches 2 mesures, puis doubles-croches | MO-02 |
| Pitch range (FL) | 5 | MO-02 |
| Pitch range (FL Sampler) | 1 par défaut, jusqu'à 48 ; MIDI sur 12 mesures | MO-06 |
| Pitch automatisé | jusqu'à 12 (demi-tons, interp.), dès le milieu du build | MO-03 |
| Loop Length (Simpler) | descente jusqu'à ≈ 10 % | MO-04 |
| Arpeggiator Rate (Free) | ≈ 700 ms → ≈ 20 ms ; départ « 5.518 » [ASR ?] | MO-05 |
| Arpeggiator Gate / Steps | ≈ 120–121 (%, interp.) / 0 | MO-05 |
| Reverb | ≈ 35 % dry/wet, bas coupé | MO-05 |
| Macro unique | 0 → ≈ 85 ; formant −12 ; modulation de formant 24 ; pitch +12 | MO-07 |
| Transposition (clip) | 0 → 11, dit « an octave » | MO-08 |
| Transposition en paliers | +3 sur 4 mesures, puis +12 sur les 3 dernières | MO-09 |
| Transposition | +12 sur les 2 dernières mesures | MO-10 |
| Slide note (FL) | C5 → C6 (+1 octave), boucle de 7 mesures | MO-11 |
| Gate parallèle | 1/16 | MO-13 |
| Séquence vocale | « straight 16 » | MO-14 |
| Macro des delays | ramenée vers 55 ; fondu sur 4 mesures | MO-15 |

- Contradiction : MO-08 pousse la fin à 11 mais dit « an octave » (12). MO-12 dit « on met à 22 » [ASR ?] : valeur inutilisable.
- Lire d'abord : MO-01, MO-04, MO-05, MO-10.
- Usage émotionnel (interp.) : anticipation du build vers le drop. C'est la ligne « Suspense/tension » de `../../composer-trajectoire-emotionnelle/references/leviers.md` : registre montant, densité graduée. Le drop doit ensuite offrir un contraste.

## Tension

- Boucle de voix de longueur irrégulière, non calée sur le BPM : elle « entre et sort du groove » [SOURCE TE-01]. Pitch monté lentement (ShaperBox) ; return de delay 1/8 dont seul le volume est automatisé, en fondu avant le drop [SOURCE TE-01].
- Dernière mesure avant le drop : Warp Beats, Preserve 1/16, Transient Envelope réduite et automatisée par clip (Live 12) ; transposition de +1 demi-ton, « entre les notes » [SOURCE TE-02].
- Formants baissés juste avant le drop : cela « indique subtilement » une nouvelle section [SOURCE TE-02].
- Swell inversé sur une note de la tonalité, puis **silence** avant le drop, tous les instruments coupés [SOURCE TE-03].
- Question / réponse : « are you afraid » comme appel, réponse seulement en fin de mesure [SOURCE TE-04].
- Breakdown : une ou deux voix courent tout le break, un fragment répété, une voix au milieu prépare la montée [SOURCE TE-05].

| Paramètre | Valeur | Source |
|---|---|---|
| Delay en return | 1/8, 100 % wet, send au maximum | TE-01 |
| Warp Beats, Preserve | 1/16 | TE-02 |
| Transposition | +1 demi-ton | TE-02 |
| Auto Shift | mi mineur, formants baissés | TE-02 |
| OTT, crossover bas | 250 Hz | TE-02 |
| Shifter au drop | 50/50 wet/dry | TE-02 |
| Reverb avant inversion | mix ≈ 40 % (sous 50 %), decay ≈ 7 s | TE-03 |
| Vocoder | porteuse Noise | TE-04 |

- Seulement 5 vidéos sur 15 visées : le corpus le dit, le thème est rare sur YouTube.
- Lire d'abord : TE-02, TE-03, TE-01.
- Usage émotionnel (interp.) : suspense du break et de la dernière mesure avant le drop. Leviers de leviers.md : « retard de résolution, retrait avant résolution, reverse dosé » (leviers.md). L'« appel sans réponse » de TE-04 reste une hypothèse non démontrée.

## Surprise

- Lead de drop en chops, avec un mot ou une réponse qui change à chaque passage [SOURCE SU-03, SU-05, SU-11, SU-12, SU-13].
- Hard-tune sur des notes interdites, pour tirer une mélodie neuve de la même phrase [SOURCE SU-01, SU-12]. Glides gardés exprès [SOURCE SU-12, SU-13].
- Huit mesures « de folie », puis duplication avec une variation légère, pour que le public puisse chanter [SOURCE SU-01].
- Call & response imbriqué [SOURCE SU-04] ; « call, response, different response » [SOURCE SU-05] ; nouveauté seulement au 4e temps de la mesure C [SOURCE SU-14].
- Stutter et glitch : Warp Beats en 1/16 [SOURCE SU-02] ; Decay de Simpler modulée par un LFO Random [SOURCE SU-06] ; start et effets randomisés puis resamplés [SOURCE SU-08] ; gate fixe ou LFO qui ralentit [SOURCE SU-09].
- Roll « no no no » enregistré à la main hors grille : « it doesn't sound like it's synced » [SOURCE SU-02].
- Ear candy : dernier mot doublé à +1 puis +2 octaves ; one-shots filtrés quand l'oreille a anticipé [SOURCE SU-07]. Mot isolé après une coupure générale [SOURCE SU-03]. Reverb ouverte une demi-seconde [SOURCE SU-15].
- Reverse reverb pour adoucir une entrée trop brusque [SOURCE SU-01, SU-07, SU-10].

| Paramètre | Valeur | Source |
|---|---|---|
| Auto-Tune | retune speed 0, une note autorisée par mot | SU-01 |
| Pitch d'un mot | +3 demi-tons (SoundShifter) | SU-01 |
| Formant (Little AlterBoy) | −4 à −6 | SU-01 |
| Glitch 2 | mix 50 % | SU-02 |
| Pro-R / H-Delay | decay rate 0, mix ≈ 60 / 22 ms, mono | SU-03 |
| Pitch | +2 puis inversé ; +1 octave en Complex Pro, formants préservés | SU-04 |
| Mise en tonalité | +3 ; transpositions +9 / +10 | SU-05 |
| EQ | creux ≈ 734 Hz [ASR ?], boost ≈ 2,5 kHz | SU-05 |
| LFO → Decay (Simpler) | Random, 1/16, depth 100 ; offset −100 / +100 (≈ 2 s) | SU-06 |
| Echo | dry/wet ≈ 30 | SU-06 |
| LFO Tool | 1/32 triolet [ASR ?] | SU-07 |
| Transposition | −2 puis +12, soit +10 (sol majeur) | SU-11 |
| Vocoder | mode Precise, 20 bandes | SU-11 |
| Auto Pan | 1/8, accents en 1/16, amount ≈ 80 % | SU-11 |
| Valhalla Reverb | 20 % | SU-12 |
| Pitch de boucle | +300 cents ; ne pas dépasser 3 demi-tons | SU-14 |

- Contradiction : SU-14 déconseille de pitcher une boucle de plus de 3 demi-tons ; d'autres montent de +10 à +13 [SOURCE SU-11, RY-04, RY-15] avec Complex Pro ou les formants. SU-12 : « G minor » puis do mineur [ASR ?].
- Manque dit : aucun tutoriel de fake drop vocal, seulement cité (SU-11) ; « silence puis chop » seulement chez SU-03.
- Lire d'abord : SU-14, SU-05, SU-03, SU-06.
- Usage émotionnel (interp.) : drop et fin de chaque bloc de huit mesures. Lignes « Puissance/énergie » (répétition avec réponse) et « Joie/euphorie » de leviers.md. Dans SU-01 et SU-07, la surprise s'appuie sur un motif déjà répété.

## Rythme

- Slices calées sur les syllabes : warp markers posés à la main, puis Slice to New MIDI Track « Warp Markers » [SOURCE RY-02] ; chaque mot sur un temps donne « a lot more bounce » [SOURCE RY-10].
- Écrire le rythme avec un son « stabby » sans effets, puis le confier aux slices [SOURCE RY-02].
- Séquençage aléatoire, puis tri des bonnes parties : Random [SOURCE RY-02], MDD Snake [SOURCE RY-03], LFO sur Sample Start et vélocités dans un Drum Rack [SOURCE RY-01].
- UKG : voix « carrées » en croches droites, stabs de début de mesure dans un Drum Rack, swing activé (méthode Todd Edwards) [SOURCE RY-04] ; choke group et « silent choke » [SOURCE RY-05].
- Voix tenue découpée par trémolo synchro (Auto Pan), deuxième couche à un autre rythme [SOURCE RY-07] ; enveloppe de volume dessinée à la grille [SOURCE RY-08] ; gate 1/16 par Warp Beats [SOURCE RY-06].
- Stutters Beat Repeat 1/32 imprimés sous le hook [SOURCE RY-11]. Deux pistes de slices : fond discret et lead [SOURCE RY-12].
- One-shot percussif : cri, chop sur une voyelle, formants, resampling en chaîne [SOURCE RY-13].
- Mélange consonnes / voyelles et notes courtes / longues [SOURCE RY-14] ; finir la boucle par la vraie fin de phrase [SOURCE RY-09, RY-15].

| Paramètre | Valeur | Source |
|---|---|---|
| Release (Simpler, Classic) | ≈ 50 ms | RY-01 |
| LFO Random → Sample Start | synchro 1 mesure | RY-01 |
| Transpose par macro | −48 / +48 ; 50 = 0 ; ≈ 62,5–63 = +12 | RY-01 |
| Auto Shift | mi bémol majeur, smoothing off | RY-01 |
| Random | 36 notes adressées ; glitch enregistré sur 16 mesures ; couche à −12 | RY-02 |
| Pitch du hook | +13 (voix déjà à +1) | RY-04 |
| Accord (Span) / pitch | +44 cents / +3 demi-tons | RY-05 |
| Échos | noire, puis croche pointée | RY-05 |
| Tempo UKG | ≈ 130 BPM, 2-step | RY-07 |
| Auto Pan | Sync, phase 0 (mono) ; Saw inversée pour le ducking | RY-07 |
| Coupures dessinées | jusqu'à 1/32 | RY-08 |
| Boucle de chops | 2 mesures | RY-09 |
| Reverb « compressed room » | room amount ≈ 70 % | RY-10 |
| Beat Repeat | grille 1/32 ; boucle de 16 mesures | RY-11 |
| Auto-Tune | speed 0,1 ms, transition 0,1 ms, correction 100 | RY-14 |
| Chops | −2 (la mineur), puis +3, +5, +7 | RY-14 |
| Transposition | +12 | RY-15 |

- Contradiction : RY-04 baisse le swing car les voix rap sont droites ; RY-06 en demande « a bit » ; RY-05 le recommande mais modifie les vélocités à la place. Aucune valeur de swing chiffrée.
- Lire d'abord : RY-02, RY-05, RY-01, RY-07.
- Usage émotionnel (interp.) : groove du drop et des couplets. Lignes « Puissance/énergie » (accents nets) et « Joie/euphorie » (rebond) de leviers.md. leviers.md cite Witek : syncope intermédiaire préférée dans une expérience, à tester sur le morceau.

## Ambiance et reverse

- Chops tenus dans un Drum Rack, choke commun, pan différent par pad, de-ess et passe-bas pour reculer [SOURCE AR-01].
- Micro-boucle déplacée dans l'acapella, envoyée dans des returns ; jouée en Session et enregistrée en Arrangement [SOURCE AR-02].
- Nappe granulaire : Serum 2 en mode Manual, position modulée par LFO [SOURCE AR-03] ; Granulator sur une note chantée en bougeant la bouche [SOURCE AR-04].
- Pad bouclé : Loop ON, Fade à 100 %, attaque et release lentes [SOURCE AR-05] ; effets posés **avant** de boucler, pour cacher les points de boucle [SOURCE AR-06].
- Pad imprimé : reverb à decay maximal, Freeze/Flatten, puis rejoué dans Simpler [SOURCE AR-07]. « Vocal bed » sur une note, accordé au Tuner [SOURCE AR-08].
- Reverse reverb, ordre dit : reverse, reverb 100 % wet, impression, garder la queue, re-reverse [SOURCE AR-09, AR-12]. Sur le **premier** son de la phrase [SOURCE AR-09, AR-10, AR-11].
- Faire chevaucher la fin du swell et l'attaque du mot ; fondu [SOURCE AR-10, AR-11]. Copie remise à l'endroit sous la coupure [SOURCE AR-15].
- Avant le drop : élément inversé et Transposition à −1 demi-ton qui remonte [SOURCE AR-13]. Reverse delay en temps réel sur un bus [SOURCE AR-14].

| Paramètre | Valeur | Source |
|---|---|---|
| Transposition par pad | +5 / −4 demi-tons | AR-01 |
| Delay (EchoBoy) | 1/8, mode Telephone | AR-01 |
| Grille de déplacement | 1/64 ou 1/128 | AR-02 |
| Reverb en return | « 14 secondes » | AR-02 |
| Auto Pan | amount 33 | AR-02 |
| Serum 2 granulaire | position ≈ 12–84 % ; length 1/2 mesure ; density 1/4 de mesure | AR-03 |
| Serum 2 granulaire | autres ≈ 30–40 % ; pitch random max 0,1 (0,3 en démo) ; Direction au max | AR-03 |
| Note chantée | sol, descendue de 7 demi-tons | AR-04 |
| Simpler (pad) | Voices 6 → 32 ; Fade 100 % ; Attack 3 000 ms ; Release 3 s (essai 4 s) | AR-05 |
| Delay / Reverb (pad) | 3/16 ping-pong, feedback ≈ 50 % / decay 4,5 s | AR-06 |
| Enveloppe (pad) | attack 3 s, release 3 s | AR-06 |
| Couche pitchée / OTT | −7 / ≈ 30 % | AR-07 |
| Reverb inversée | 100 % wet, decay ≈ 15–16 s | AR-09 |
| Swell | sur toute la phrase de 4 mesures | AR-10 |
| Voix principale / chops | low cut 200 Hz / slices 1/8 à 136 BPM ; « +60 » [ASR ?] | AR-11 |
| Transposition avant le drop | −1 demi-ton qui remonte | AR-13 |
| Reverse delay | 1/4 ; depth 2, rate 0,12 ; envoi ≈ −12 dB | AR-14 |

- Contradiction : TE-03 garde la reverb sous 50 % (au-dessus, « boueux ») ; AR-09 et AR-12 la mettent à 100 % wet. Le but diffère : TE-03 imprime le chop et sa queue, AR-09 ne garde que la queue (interp.). Decay : 7 s (TE-03), 15–16 s (AR-09), « pas trop » sur une phrase chargée (AR-12).
- Lire d'abord : AR-05, AR-06, AR-09, AR-10.
- Usage émotionnel (interp.) : intro, break, outro. Lignes « Apaisement », « Nostalgie/tendresse » et « Mélancolie » de leviers.md (réverbération qui laisse la phrase intelligible). Le reverse sert l'anticipation (« reverse dosé »). Méthode : `../../composer-trajectoire-emotionnelle/GUIDE.md`.

## Traduction dans l'installation du projet

| Vidéo et outil | Geste | Équivalent dans le projet |
|---|---|---|
| MO-02 (FL) | Make unique as sample, roll en notes, pitch automatisé | Simpler et notes MIDI ; Pitch Bend par enveloppe de clip MIDI, comme MO-04 dans Live. Plage de bend : voir `sampler-synthese.md` (SA-02). |
| MO-03 (FL, DirectWave) | Fin de boucle automatisée | Loop Length de Simpler automatisé [SOURCE MO-04] ; dans Sampler, Aux Env → Loop Start et LFO → Loop Length (SA-14). |
| MO-06, MO-11, MO-12 (FL) | Edison, loop points, pitch automatisé | Sampler en boucle de sustain (`sampler-synthese.md`) et Transpose. Pour monter sans accélérer (MO-11) : clip warpé en Complex Pro et enveloppe de Transposition [SOURCE MO-09, MO-10]. |
| MO-07 (Bitwig, Macro-4) | Une macro, quatre paramètres | Macro d'Instrument Rack sur Simpler : Loop Length, Transpose, Filter. Le corpus ne donne pas d'équivalent au formant de Simpler ; Complex Pro a des formants (SU-04, RY-15). |
| TE-01 (DAW non nommé) | Boucle irrégulière | Boucle de Simpler hors grille (interp.) ; ShaperBox est un plug-in tiers, à chercher dans l'installation. |
| TE-03 (Logic), AR-15 (tout DAW) | Bounce in place, File > Reverse | Freeze/Flatten ou Bounce, puis R [SOURCE AR-12, AR-13] ; capture : `../../../sound-designer-serum/modules/resampling/GUIDE.md`. |
| SU-01 (Pro Tools, AudioSuite) | Imprimer chaque traitement | Resampling ou Freeze/Flatten (`../../../sound-designer-serum/modules/resampling/GUIDE.md`). |
| SU-03 (Logic, Melodyne) | Chops faits dans Melodyne | Melodyne dans Live comme SU-12, s'il est installé ; sinon découpe en Slice dans Simpler. |
| SU-09, SU-10 (FL, Gross Beat, PanOMatic) | Gate et trémolo | Warp Beats et Transient Envelope [SOURCE TE-02, SU-02] ; enveloppe de volume dessinée [SOURCE RY-08] ; LFO → Volume carré dans Sampler (SA-13). |
| SU-09 (FL, ghost channel) | MIDI muet qui pilote le volume | Pas d'équivalent dans le corpus. (interp.) Gate ou compresseur tiers en sidechain. |
| SU-10, SU-14 (FL, Slicex) | Slices jouées en MIDI | Simpler en Slice ou Slice to Drum Rack (`simpler-synthese.md`). |
| AR-03 (Serum 2 dans Bitwig) | Granulaire Manual, LFO sur la position | Même plug-in dans Live 12 ; valeurs du tableau Ambiance reprises telles quelles. |
| AR-14 (DAW non nommé) | H-Delay puis Initial Reverse sur un bus | Plug-ins tiers à vérifier. Le corpus suggère Beat Repeat (interp. de l'étude) : effet natif, exclu. |
| SU-07, SU-15 (DAW non nommé) | Throws de reverb, LFO Tool | Automation d'envoi vers un retour ; le corpus ne nomme pas de réglage Live. |

- Arpeggiator devant Simpler ou Sampler (MO-05) : outil MIDI natif de Live, déjà vu dans SI-20 (`simpler-synthese.md`).
- Maschine : aucune vidéo du corpus. Gestes proches dits ailleurs : Slice, Choke group, Polyphony = 1, Edit › Reverse, Stretch avec Formant, Loop avec X-Fade. Voir `../../../producteur-rythmique/modules/produire-avec-maschine-mk3/references/sampling-maschine-synthese.md`. Rappel d'AGENTS.md : une sortie directe de Maschine contourne le Perform FX du Master.
- Serum 2 : seulement AR-03. Aucun Clip Sequencer de Serum 2 appliqué aux chops (manque dit du thème Rythme).
- Paramètres de Simpler et Sampler exposés à l'API : `../../../sound-designer-serum/modules/vst-sound-design/references/instruments-natifs.md`.

## Limites

- **Captures non faites.** Chaque fiche liste ses points « À vérifier à l'écran ». Aucune position de bouton n'est confirmée.
- **Transcriptions automatiques** presque partout ; MO-03 est la seule dite manuelle, TE-01 et TE-02 sont de type non vérifié. MO-12 est « très bruitée ». Points [ASR ?] : « 5.518 » et « 17 mesures » (MO-05), « 22 » et le raccourci (MO-12), mode « Cycles » (MO-07), plugin « Mela » (MO-13), « five pro reverb » (TE-05), ≈ 734 Hz (SU-05), 1/32 triolet (SU-07), preset Gross Beat (SU-09), « 24 » (SU-13), « OT » (RY-02), générateur non nommé (RY-06), « stray » (AR-04), « +60 » (AR-11), « log set to 4 » (AR-14).
- **Versions.** Dates de 2011 à 2026. Live 12 dit ou requis : Transient Envelope et Auto Shift (TE-02, RY-01, RY-03). Live 11 : AR-07, AR-12. Live 10 : MO-04. Live 9 : SU-13. FL Studio 11 : MO-06. Serum 2 dans Bitwig 6 : AR-03.
- **Effets natifs de Live filmés** : Utility (MO-01, SU-02), Overdrive (MO-01, SU-05, SU-06), Compressor (MO-05, TE-02, AR-02), Glue Compressor (TE-02, AR-01), Reverb (MO-05, MO-10, MO-15, SU-13, AR-05, AR-06, AR-09, AR-12), Hybrid Reverb (RY-05), Auto Filter (MO-10, SU-08, AR-01, AR-07), Ping Pong Delay et Simple Delay (MO-15, SU-08, SU-13), Filter Delay (AR-02), Delay (AR-06), Echo (TE-04, SU-02, SU-06, RY-05), Beat Repeat (SU-08, AR-02, RY-11), Grain Delay (SU-08), Auto Pan (SU-11, RY-07, AR-02, AR-08), Saturator (SU-12, AR-07, AR-08), Chorus (SU-05), Drum Buss (RY-14), EQ Eight (TE-02, SU-13), Auto Shift (TE-02, RY-01, RY-03), Shifter (TE-02), Vocoder (TE-04, SU-11), Spectral Resonator (TE-04, SU-05). L'« OTT » de TE-02 (« stock plugins ») serait le preset de Multiband Dynamics (interp.).
- **Règle du projet** (règle 6 de `../../../../producteur-live/SKILL.md`) : pas de nouvel effet natif de Live dans les chaînes de mix ; passer par des plug-ins tiers (`../../../ingenieur-mixage/modules/effets-plugins/references/fiches.md`). Tolérés : instruments natifs (Simpler, Sampler, Drum Rack), Utility, Compressor en sidechain déjà en place, Auto Filter déjà posé sur une piste MIDI, Hybrid Reverb sur un retour. Arpeggiator et Random sont des effets MIDI, pas des traitements de mix (interp., à confirmer avec l'utilisateur).
- **Max for Live à signaler** : LFO (SU-06, RY-01), random numbers de Woulg (SU-08), MDD Snake (RY-03), Granulator (AR-04). Vérifier leur présence avant de les proposer.
- **Plug-ins tiers du corpus** (Little AlterBoy, Valhalla, EchoBoy, ShaperBox, Glitch 2, VocalSynth 2, Manipulator, MAutoPitch…) : leur présence sur le Mac n'est pas vérifiée.
- **Droits des voix.** Le corpus utilise des acapellas publiées (Chris Brown en MO-09, « Starchild » en MO-05, une « acapella connue » en RY-08) et des packs (Splice, Loopcloud, Zero-G, Black Octopus). Ne jamais réutiliser une voix d'un titre publié ni un enregistrement sans droits dans une sortie (règle « Référence » d'AGENTS.md). Partir d'une voix enregistrée par l'utilisateur (RY-13, AR-04) ou d'un pack dont la licence est vérifiée.
- **Numérotation des notes.** C3 = 60 dans Live ; le numéro MIDI fait foi. FL Studio nomme « C5 » la note d'origine (MO-02, MO-03, MO-11) : (interp.) c'est le MIDI 60, à vérifier avant de recopier. RY-01 met la première boucle sur C1 (MIDI 36).
- **Pas d'écoute.** « Punchy », « wavy », « plus large », « alien », « eerie » sont les mots des vidéos. Les tests d'écoute reviennent à l'utilisateur.
- **Manques du corpus.** Aucune Maschine dans les cinq thèmes. Serum 2 : AR-03 seul. Tension : 5 vidéos sur 15 ; pas de chops dissonants, ni d'« appel sans réponse » démontré, ni de tutoriel français. Surprise : pas de fake drop vocal ; pitch-dive et tape-stop absents. Rythme : ni afro house, ni polyrythmie 3 contre 4 enseignée, swing jamais chiffré. Ambiance : pas de « vocal freeze » ni de PaulStretch. Montée : le roll de chops doublé de snares n'existe que dans MO-03.
