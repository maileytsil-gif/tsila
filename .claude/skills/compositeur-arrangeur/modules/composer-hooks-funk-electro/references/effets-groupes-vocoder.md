# Effets de groupe, sections et vocoder

## Dans ce workflow : effets natifs et équivalents tiers

Les chaînes ci-dessous citent des effets natifs de Live (Auto Filter, Phaser-Flanger, Chorus-Ensemble, Auto Pan-Tremolo, Beat Repeat, Vocoder, Glue, Saturator). La règle 6 d'`../../../../producteur-live/SKILL.md` exclut tout **nouvel** effet natif des chaînes de mix (demande explicite de l'utilisateur) ; seuls sont tolérés Auto Filter déjà posé sur une piste MIDI, Utility, Compressor en sidechain déjà en place et Hybrid Reverb sur un retour. Avant de poser une chaîne, choisir dans cet ordre :

| Geste | Natif cité | Dans ce workflow (`../../../ingenieur-mixage/modules/effets-plugins/references/fiches.md`) |
|---|---|---|
| Passe-haut qui monte sur un groupe | Auto Filter | Waves REQ 6 : bande Hi-Pass, `Frq` exposé à Live → automation relue par `lom.py apply` (`../../../../producteur-live/modules/live-automation/GUIDE.md`, valeurs en `raw`) ; Auto Filter seulement s'il est déjà sur la piste MIDI |
| Flanger de transition | Phaser-Flanger | Waves MetaFlanger (Mix, Depth, Rate, FeedBack exposés, automatisables) |
| Glue de groupe | Glue Compressor | Plugin Alliance bx_glue |
| Saturation, « bite » | Saturator, Erosion | Waves J37 (Saturation) ; pour ce qui appartient au son, effets internes de Serum 2 (`../../../sound-designer-serum/references/serum2-fx-clip-arp.md`) |
| Réverb / delay communs | Reverb, Delay sur retour | Hybrid Reverb sur un retour (toléré) ; autre plug-in tiers seulement s'il est probé dans les fiches |
| « Coupe-coupe », gate rythmique | Auto Pan-Tremolo, Beat Repeat | Édition : coupes dans le MIDI ou dans l'audio resamplé (`../../../sound-designer-serum/modules/resampling/GUIDE.md`), ou automation de gain d'Utility (toléré) |
| Chorus, phaser, Grain Delay, Vocoder | natifs sans équivalent tiers relevé | Demander l'exception explicitement ; sinon effet interne de Serum 2 sur la source ; une fois le geste validé, imprimer en audio et retirer l'effet |

Les recettes restent valables comme description du geste ; seul l'outil change. Ne jamais poser un effet sur le Main « pour essayer ».

## Routage de départ dans Live 12

Créer des groupes Drums, Bass Mid, Music (claviers/leads/pads), Vocals, FX. Garder kick et sub hors du bus d'effet qui coupe le grave ou élargit le son, sauf transition intentionnelle imprimée et contrôlée. Placer un Audio Effect Rack sur le groupe concerné; une chaîne sèche et une chaîne traitée permettent de comparer et doser. Les Macro Controls du rack peuvent piloter plusieurs paramètres avec des plages différentes. Pour un delay/reverb long commun, préférer un return filtré. Automatiser entrée/sortie de l'effet et ses macros dans Arrangement; imprimer en audio le résultat final avant export pour contrôler queues et répétabilité.

| Section et intention | Bus | Chaîne de départ, à ajuster | Éviter |
|---|---|---|---|
| Break qui s'éloigne, 8 mesures | Music et percussion haute | Auto Filter high-pass ouvert graduellement (par exemple 80→600 Hz), résonance modérée; Phaser-Flanger en Flanger 5–20 % wet; send delay croissant | Couper sub et kick par surprise si le break les conserve; pic de résonance. |
| Pont qui devient large | Pads/stabs ou voix de réponse | Chorus-Ensemble ou Doubler léger, filtre des basses avant largeur, reverb sur return; garder thème central net | Élément central flou, phase faible en mono. |
| Sweep résonant vers drop | Percussion ou sample resamplé | Auto Filter band-pass/notch avec cutoff automatisé sur 4/8 mesures, Q/résonance contrôlée et gain compensé; imprimer sweep | Automatiser très forte résonance sur bus complet à plein niveau. |
| « Coupe-coupe » en fin de break | Music/FX, jamais master par défaut | Auto Pan-Tremolo en amplitude/tremolo synchronisé, ou Beat Repeat en Insert/Gate; 1/8→1/16 sur 1–2 temps; silence juste avant downbeat | Glitch permanent qui efface pulsation et attaque du retour. |
| Décélération/tape-stop | Hook imprimé, bus Music bref | Pitch/time automatiques sur audio dédié ou ralentissement de lecture échantillon, filtre qui se ferme; couper l'effet au retour | Tordre le morceau complet alors que la voix ou le kick doivent rester compréhensibles. |

Un **sweep de résonance** est le mouvement d'un pic ou creux de filtre, pas un boost fixe. Commencer avec résonance faible et régler dans le mix à niveau égal; écouter surtout les fréquences agressives et le grave. Le **coupe-coupe** peut être une modulation d'amplitude (tremolo), un gate synchronisé ou une répétition de fragments: choisir selon que l'on veut du silence réel ou un bégaiement. Auto Pan-Tremolo, Auto Filter, Beat Repeat, Chorus-Ensemble et Phaser-Flanger sont documentés dans [le manuel Live 12](https://www.ableton.com/en/manual/live-audio-effect-reference/). [Tom Cosm présente flanger, phaser et chorus en contexte](https://www.ableton.com/en/blog/rediscover-classic-effects-flanger-phaser-and-chorus/); sa vidéo intégrée n'a pas été vérifiée ici.

## Rack « Break to Drop » original, 8 mesures

Groupe Music seulement: M1 **Distance** mappe Auto Filter HP 40→500 Hz et dry/wet reverb return 0→20 %; M2 **Swirl** mappe Flanger wet 0→15 % et feedback faible→modéré; M3 **Cut** mappe profondeur de tremolo 0→100 % à cadence 1/8 ou 1/16 au dernier temps seulement; M4 **Throw** envoi delay filtré 0→25 %. Mesures 1–4: Distance monte de 0 à 35; 5–7: 35→75, Swirl 0→40; m8: Cut seulement sur temps 3–4, Throw sur dernier fragment, puis toutes macros reviennent à zéro **avant** premier kick du drop. Les plages chiffrées sont un prototype à ajuster selon le signal et la version de Live, non une consigne de loudness. Contrôler dry/wet contre phase/volume et imprimer le groupe sur une nouvelle piste pour inspecter début et fin.

## Vocodeur: principe et routage

Le **modulateur** fournit l'articulation spectrale/rythmique (voix, bouche, percussion); la **porteuse** fournit la matière harmonique (saw Serum 2, Wavetable, noise, pad). Dans Live, insérer Vocoder sur la piste du modulateur, sélectionner Carrier External puis la piste synthé dans Audio From; vérifier Pre/Post FX, monitoring et niveau de la porteuse. Le manuel explique Bands, Range, BW, Gate, Depth, Attack/Release, Formant et mode mono/stéréo dans [Vocoder](https://www.ableton.com/en/manual/live-audio-effect-reference/). Tester d'abord une phrase parlée claire et une porteuse saw simple, sans autres effets.

| Recette | Modulateur → porteuse | Traitement / quatre commandes de rack |
|---|---|---|
| Basse « robot qui répond » | Courte syllabe originale « wah/yo » → mid bass saw Serum 2, sub sin séparé | Vocoder uniquement mid; 8–20 bandes comme essai, Attack assez court pour consonnes, Release sous note suivante; M1 Formant, M2 Depth, M3 Bite/saturation post, M4 Delay mid. Call/response tous les 2 temps. |
| Percussion métallique parlante | Hat/clave rythmé → porteuse FM accordée, pas de grave | Ajuster Range sur médium, Gate pour silences, resampler quatre variations; M1 Formant, M2 bands/BW, M3 edge, M4 space. Accent dans pont ou fill. |
| Pad vocal sans texte | Souffle/phrase originale lente → accord saw/pad | Plus de bandes et Release plus long comme essais, reverb sur return; M1 vowels/formant, M2 depth, M3 dark, M4 tail. Vérifier que la voix principale reste devant. |
| Growl hybride | Growl Serum 2 rythmé comme porteuse, percussion/bouche comme modulateur | Imprimer le mid, saturer modérément après vocoder, filtrer bas du mid; M1 formant, M2 motion, M3 crunch, M4 width. Comparer à la basse sans vocoder à niveau égal. |
| Transition robotique | Une seule syllabe tenue → porteuse bruit+saw, moduler formant et cutoff sur 4 mesures | Imprimer, inverser une queue, couper au drop; M1 rise, M2 speech, M3 grain, M4 tail. Ne pas occuper le sub pendant montée. |

Les valeurs de bandes et de temps restent des points de départ: choisir selon intelligibilité, note de basse et densité du mix. Le vocodeur peut faire disparaître la fondamentale; garder un sub propre indépendant, contrôler la phase et ne pas élargir le bas. Tester si la modulation d'une percussion rend la hauteur instable; réaccorder ou retirer la couche tonale. [Ableton présente aussi des usages de vocoder sur basses et percussions](https://www.ableton.com/en/blog/vocoder-not-just-for-vocals/) et [Vespers combine vocoder, phaser, flanger et saturation](https://www.ableton.com/en/blog/vespers-tutorial-bass-shapes/); les vidéos liées restent à analyser par transcription/visionnage avant d'attribuer des valeurs exactes.

## Contrôle de livraison

À niveau égal, comparer groupe sec/traité dans la section et au retour du drop; inspecter crêtes de résonance, intelligibilité de la voix, phase/mono, grave et queue d'effet. Le bypass doit rendre le rythme encore compréhensible. Enregistrer automation et version audio imprimée, vérifier le bounce entier après export. Un rack spectaculaire en solo peut être rejeté s'il diminue l'impact du morceau.
