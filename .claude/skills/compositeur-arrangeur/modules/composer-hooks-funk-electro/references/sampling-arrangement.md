# Sampling de la source au morceau

## Choisir la source et l'outil

Avant de découper, consigner auteur, provenance, licence, droit d'usage en master commercial, attribution éventuelle et possibilité de redistribution d'un preset contenant l'audio. Un sample d'un disque commercial, une vidéo ou une acapella extraite ne devient pas libre parce qu'il est court, filtré ou resamplé. Privilégier voix, instruments et objets enregistrés par l'utilisateur, packs dont la licence couvre la sortie, ou autorisation explicite. Conserver fichier source intact, travail sur copie, nom et note de licence.

| Besoin | Outil recommandé | Raison |
|---|---|---|
| Découper une phrase de batterie/voix par transient, rejouer sur pads | Simpler Slicing → Drum Rack | Slices non destructives et MIDI distinct pour chaque fragment. |
| Jouer une note/prise en one-shot ou boucle avec enveloppes/filtre | Simpler Classic ou Sampler | Simpler pour warp et découpe rapide; Sampler pour zones et modulations plus poussées. |
| Créer un instrument à partir d'un enregistrement tonal | Serum 2 Sample ou Sampler | Accord, boucle, enveloppe et modulation contrôlables. |
| Étirer une syllabe/texture sans suivre strictement durée ou hauteur | Serum 2 Granular ou Granulator III si installé | Position, taille/densité et mouvement des grains. |
| Transformer le contenu fréquentiel d'une source tonale | Serum 2 Spectral | Resynthèse et mouvement spectral; vérifier artefacts et hauteur perçue. |
| Fabriquer un riser à temporalité et pitch exacts | Audio resamplé dans Arrangement | Edits et automation visibles, export déterministe. |

Dans ce workflow, la capture passe par `../../../sound-designer-serum/modules/resampling/GUIDE.md` et la recomposition d'un sample (chopping, reharmonisation, contrepoint) par `../../sampling-composition-avancee/GUIDE.md` ; Simpler, Sampler, Drum Rack et Granulator III sont des instruments (tolérés), Beat Repeat et Grain Delay des effets natifs soumis à la règle 6 d'`ableton-live-session` (voir `effets-groupes-vocoder.md` § Dans ce workflow). Les modes Sample, Granular et Spectral de Serum 2 sont documentés par Xfer; Simpler, Sampler, slice-to-Drum-Rack et warp par le manuel Live 12. Ne pas promettre que Sampler fait le slicing/warp de Simpler de manière identique. Vérifier la version exacte de Live pour les fonctions récentes de séparation de stems.

Lire les sources officielles: [Serum 2, cinq modes d'oscillateur](https://xferrecords.com/web-manual/serum-2/exploring-sound-design-in-serum), [Live 12 Simpler/Sampler](https://www.ableton.com/en/manual/live-instrument-reference/), [routage et resampling](https://www.ableton.com/en/manual/routing-and-i-o/), [droits d'usage commercial des sons Live](https://help.ableton.com/hc/fr-fr/articles/209768885-Droits-d-utilisation-commerciale-du-contenu-de-Live). Les sons Core/Packs peuvent entrer dans un morceau commercial sous les conditions d'Ableton; ne pas les reconditionner en pack de samples/presets autonome.

## Procédure commune

1. Écouter la source complète et isoler un geste qui a un rôle: consonne, attaque, note tenue, bruit respiré ou queue. Marquer début/fin, hauteur ou fondamentale si tonal, puis détecter la durée et le temps musical.
2. Découper aux passages silencieux ou zero crossings si possible; faire fondus courts pour supprimer clics sans arrondir le transient voulu. Aligner un chop au ressenti de son attaque audible, pas seulement au début du fichier.
3. Transposer sans déformer inutilement: écouter formants d'une voix, grains, phase et pitch; comparer plusieurs modes Warp sur la phrase. Si forte transformation, imprimer en audio puis travailler le résultat plutôt qu'empiler du temps réel.
4. Écrire une phrase MIDI ou audio de 1–4 mesures avec silences et variation identifiable. Le sample est une matière; sa place et son phrasé créent le hook.
5. Automatiser un seul axe principal par section (position, taille de grain, cutoff, hauteur ou densité). Programmer macros avec destinations/plages réelles, tester min/milieu/max et éviter les sauts de niveau.
6. Resampler en audio sur nouvelle piste avec marge, conserver la piste source désactivée, réécouter début/fin, phase et queue dans le mix. Documenter BPM, tonalité, version, droits et traitements.

## Huit recettes originales à programmer

**1. Vocal chop de break, 4 mesures.** Enregistrer une phrase originale de 1–2 secondes. Dans Simpler Slicing, placer 4–6 slices sur consonnes/voyelles, Slice to Drum Rack et programmer deux gestes de 3 attaques séparés par un silence. Dans Serum 2 Sample, alternative: charger une seule syllabe tonale, l'accorder et déclencher en notes différentes; ne pas prétendre que le Sample osc remplace le multi-slicing de Drum Rack. Filtrer les chops derrière la voix principale, ouvrir une réponse au début du break. Macros rack: start/choix de slice (si mappable), decay, filtre, send delay. Garder une version dry et tester intelligibilité sans paroles copiées.

**2. Stab de microhouse à partir d'un objet.** Enregistrer bois/verre ou bouche; choisir 100–300 ms d'attaque/queue, le placer dans Serum 2 Sample ou Simpler. Accorder la résonance si elle porte une note; enveloppe courte et filtre médium. Jouer sur 2&, 3a, puis une réponse modifiée m4; varier vélocité plus que pitch aléatoire. Macros: attack, decay, tone, grain/delay. Dans le pont, ne garder que le stab et une percussion; au drop revenir au motif sec.

**3. Pad granulaire d'un piano/Rhodes original.** Jouer un accord à quatre notes avec espace, enregistrer 4 secondes et choisir une zone sans attaque. Serum 2 Granular ou Granulator III: grains assez longs pour conserver la hauteur, position qui dérive lentement, filtre retirant le grave; attaque 300–1200 ms et release limité par la transition. Macros: position, grain size/density, dark/bright, espace. Dans le break, révéler la couleur; sous la voix, réduire densité et niveau. Contrôler mono et résolutions harmoniques à chaque accord.

**4. Riser vocal inversé, 8 mesures.** Prendre la dernière syllabe d'une prise autorisée, imprimer sa reverb, inverser la queue en audio, caler sa fin exactement sur le drop. Ajouter couche Serum 2 Sample/Granular avec position et filtre croissants; retirer le grave progressivement. Macros: rise/position, brightness, tension/dissonance, width du haut. Couper ou duck la queue à l'impact pour que kick/sub reviennent lisiblement; vérifier qu'aucune consonne inversée devient un mot non voulu.

**5. Percussion qui devient basse.** Enregistrer un tom/cowbell personnel, baisser d'une octave, sélectionner une boucle stable et raccourcir longueur de boucle ou augmenter pitch via enveloppe Sampler. Alternative Serum 2 Sample/Granular après export du micro-loop. Resampler une note résultante, accorder et bâtir un riff à silences. Macros: loop/position, pitch bend, decay, edge. Vérifier hauteur stable du sub; superposer une sinusoïde propre seulement si utile.

**6. Transition par resampling du hook, 2 mesures.** Imprimer le lead/stab original sur audio. Couper en 1/8 puis 1/16 choisis, rejouer une variation qui accélère sur la dernière demi-mesure, filtrer et inverser un fragment; silence de 1/8 avant retour. Une automation Beat Repeat/Grain Delay en bus peut remplacer les coupes si on imprime et sélectionne la bonne prise. Macros: density, filter, pitch, send. Ne pas faire un roulement continu qui masque le hook d'arrivée.

**7. Pont harmonique à partir d'une prise de guitare/cuivres.** Enregistrer deux notes ou un accord original, choisir attaque et fin de phrase, slice ou Sampler selon articulation. Transposer une quarte/voix de réponse en vérifiant formant/timbre; programmer une question m1–2, réponse m3–4, laisser la basse faire la fondamentale. Serum 2 Spectral pour texture secondaire, instrument réel/one-shot pour attaque lisible. Macros: timbre, envelope, motion, espace. Au retour, laisser une seule note signature sous le drop.

**8. Impact multicouche resamplé.** Source personnelle: frappe sèche, note grave synthétisée et bruit froissé. Imprimer séparément click, body et tail; aligner transients, accorder body, filtrer tail hors sub et exporter one-shot avec queue complète. Macros sur rack avant impression: hit, body, grit, tail. Dans le mix, comparer à un drop sans impact à niveau égal; si le kick semble disparaître, réduire plutôt que limiter plus fort.

## Placement narratif

| Section | Sample qui porte l'idée | Variation conseillée |
|---|---|---|
| Couplet/groove | Un chop sec ou percussion identitaire, répété | Vélocité/start point subtil, conserver les silences. |
| Break | Même matière allongée ou spectrale, basse retirée | Révéler harmonique et espace sans perdre le thème. |
| Pont | Réponse instrumentale issue d'une nouvelle prise, 4–8 mesures | Changer registre/accord et laisser un repère du hook. |
| Riser | Queue inversée ou texture granulaire, 4/8/16 mesures | Monter tension puis couper avant l'impact. |
| Drop | Version courte et sèche du fragment + kick/sub | Première attaque lisible; réintroduire les détails après 4/8 mesures. |

## Contrôle avant sortie

Revoir droits et crédits par fichier, absence de sample démo non licencié, juste accordage et tempo, fades sans clic, absence d'artefact vocal involontaire, basses en mono et phase par note, reverb/delay coupés intelligemment aux transitions, pics et dynamique du mix, écoutes à niveau égal sur système principal/petit système/casque. Réexporter avec les pistes resamplées et relire le fichier entier. Le statut « label ready » s'applique au morceau réellement audité, pas à une recette textuelle ou un preset.

## Vidéos et workshops ciblés

- [Ableton / Side Brain, guide de remix](https://www.ableton.com/en/blog/a-step-by-step-guide-to-remixing-a-track/): page officielle annonce stems, chops vocaux, audio→MIDI et kit 808; Live 12.3, donc vérifier la version avant le module de stems.
- [Made in Live: Beatrice](https://www.ableton.com/en/blog/made-in-ableton-live-beatrice/): présentation d'un morceau construit largement avec sa propre voix, transformations et resampling.
- [Made in Live: Freddie Joachim](https://www.ableton.com/en/blog/made-in-ableton-live-freddie-joachim-on-chopping-samples-beatmaking-and-more/): présentation du découpage de Rhodes et de breaks, puis guitare jouée.
- [Ableton / ZW Buckley, Paste Bounced Audio](https://www.ableton.com/en/blog/paste-bounced-audio-with-zw-buckley/): resampling et montage dans l'arrangement; vérifier que la fonction existe dans la version locale.
- [Ableton, vocal chops rythmiques](https://www.ableton.com/en/blog/make-rhythmic-vocal-chops-live/): tutoriel Point Blank sur warping, EQ, compression et chops rapides.

Ces pages donnent un choix de tutoriels. Pour décrire gestes exacts de vidéo, utiliser transcription intégrale horodatée ou lecture audiovisuelle; ne pas déduire des valeurs des seuls résumés de page.

### Transcription étudiée: Zdrewe, vocal chops

[« Ableton Tips to Make PRO Vocal Chops… »](https://www.youtube.com/watch?v=343jcCsYhgQ), transcription automatique horodatée consultée le 29/09/2026; audio impossible à lire et réglages visibles à l'écran non vérifiés. 0:25–0:41 réserver de l'espace dans l'arrangement; 0:43–1:25 choisir voyelle/phrase et répéter une cellule rythmique; 2:06–2:50 « Slice to new MIDI track », retirer des notes puis essayer MIDI Generate/Seed comme brouillon; 3:47–4:45 Granulator, automatiser position du fragment et taille des grains; 5:18–5:43 allonger une note, freeze/flatten ou resampler, puis re-découper. Le transfert vers Serum 2 Granular de la recette 3 est une adaptation proposée, pas une technique attribuée à cette vidéo.
