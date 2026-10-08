# 55 recettes Serum 2 à développer et valider

Ces 55 points de départ sont des constructions originales. Notation: A/B/C = oscillateurs, N = noise, SUB = sub, E = enveloppe d'amplitude, L = LFO, F = filtre. Les noms des tables et modes peuvent changer: sélectionner par propriété acoustique et vérifier les commandes dans la version installée. Chaque ligne donne **source → modulation/forme → rôle**. Paramètres chiffrés sont plages de départ, jamais une garantie « label ready ».

Pour chaque recette, créer les quatre macros indiquées **dans sa ligne**; elles priment sur le modèle général de [palette-production.md](palette-production.md). Documenter destinations et min/max réellement assignés dans le preset; comparer 0/50/100 %, compenser le volume. Garder kick/sub mono. Les cinq recettes d'une famille sont des variantes distinctes, pas cinq couches simultanées. Une ligne est une idée à développer: si le résultat demande un patch reproductible, préciser valeur/forme de chaque enveloppe et modulation, routage, macros et test avant de le livrer. Ne pas étiqueter ces esquisses « prêtes pour label ».

**Dans ce workflow.** Une recette se réalise par le rôle `../../../sound-designer-serum/SKILL.md` (choix du moteur, tableau section / paramètre / valeur / comment réglé / vérifié) puis `../../../sound-designer-serum/modules/vst-sound-design/GUIDE.md` (chargement sans hot-swap, clics dans la fenêtre de Serum 2, niveau mesuré avant/après). Serum 2 offre huit macros ; quatre par recette est un choix de gestes, pas une limite. Serum 2 n'expose à Live que « Device On » tant que ses paramètres ne sont pas configurés : pour automatiser une macro depuis l'arrangement, lire d'abord `../../../sound-designer-serum/references/serum2-automation-et-migration.md`. Les recettes percussives validées s'inscrivent au registre de `../../../producteur-rythmique/modules/drums-signature/GUIDE.md`.

## Basses

Fiches complètes (routage, enveloppes, LFO, macros, motif) des familles sub, pluck, FM, Reese, wub, growl, donk et screech : `../../../sound-designer-serum/modules/serum-2-basses-house-future-house/references/families.md`.

1. **Sub rond** — SUB sinusoïde route Direct; E attaque 2–8 ms, release 50–100 ms; note stable sous kick. M1 harmonic léger, M2 glide, M3 decay, M4 saturation parallèle haute.
2. **FM pluck** — A saw riche, B sinus modulateur ratio 2:1, B non audible, FM légère; E filtre 80–250 ms; riff syncopé. M1 FM, M2 decay, M3 drive, M4 haut médium.
3. **Growl appel/réponse** — A table riche, B FM modérée, L en enveloppe sur FM et F bandpass; phrase de deux mesures avec réponse différente. M1 vowel, M2 L depth, M3 edge, M4 mid width.
4. **Metallic donk** — A sinus/triangle, B rapport non entier ~1,4–1,7, FM brève, F bandpass; ponctuation hors sub. M1 ratio, M2 decay, M3 FM, M4 room.
5. **Reese legato** — Deux saw légèrement détunées, F passe-bas, mono/legato si notes chevauchées; sub indépendant. M1 detune, M2 motion, M3 drive, M4 width mid.

## Kicks

1. **808 velours** — A sinus, enveloppe pitch descendante rapide, E queue 400–900 ms selon espacement; click minimal. M1 pitch drop, M2 body, M3 harmonics, M4 tail.
2. **808 mordant** — même corps avec N transient 2–12 ms et saturation des harmoniques en parallèle; contrôler crest et phase. M1 click, M2 drive, M3 body, M4 tail.
3. **House compact** — sinus tonal avec pitch drop, queue 100–300 ms, transient discret; laisser basse entrer. M1 pitch, M2 attack, M3 punch, M4 tail.
4. **909 inspiré** — corps tonal plus court, couche d'attaque médium, saturation légère; comparer attaque/corps/queue séparément. M1 click, M2 tone, M3 drive, M4 decay.
5. **Kick hybride organique** — corps synthèse + transient de sample licencié dans N/Sample, aligner départs et polarité; imprimer one-shot. M1 blend, M2 tuning, M3 grit, M4 tail.

## Percussions

1. **Clap serré** — N filtré avec trois impulsions très rapprochées resamplées; E 80–180 ms. M1 spacing, M2 brightness, M3 crunch, M4 room.
2. **Snare tonal** — A sinus accordé + N bandpass, pitch drop court, deux queues séparées. M1 tune, M2 snap, M3 noise, M4 tail.
3. **Hat feutré** — N high-pass, E 30–100 ms, vélocités alternées. M1 cutoff, M2 decay, M3 grain, M4 width.
4. **Shaker mouvant** — N filtré, L léger sur amplitude à subdivisions; MIDI accents et silences définissent le groove. M1 tone, M2 rhythm depth, M3 transient, M4 pan.
5. **Tom FM** — A sinus + B modulation harmonique faible, pitch bend descendant, E 100–350 ms. M1 tune, M2 bend, M3 metal, M4 room.

## Synthés rythmiques et stabs

1. **Organ stab** — plusieurs harmoniques stables, E courte, F peu mobile; jouer voicings serrés médium. M1 harmonic, M2 gate, M3 drive, M4 room.
2. **Clav synth** — A saw/pulse, attaque vive, decay court, F enveloppé; ghost notes MIDI. M1 bite, M2 decay, M3 velocity response, M4 space.
3. **Chord stab FM** — A riche, B FM légère, E courte, accord partiel; éviter sub de chaque voix. M1 FM, M2 filter, M3 crunch, M4 width.
4. **Acid line** — source riche, F résonant, accent/enveloppe par note; slides seulement notes choisies. M1 cutoff, M2 resonance, M3 accent, M4 distortion.
5. **Piano synth percussif** — A sin/triangle + couche d'harmoniques décroissantes, E 200–700 ms; thème supérieur audible. M1 attack, M2 brightness, M3 body, M4 delay.

## Leads

1. **Vocal simple** — table à pics formantiques, L lent sur position, mono/legato selon phrase. M1 vowel, M2 glide, M3 vibrato, M4 delay.
2. **Saw anthem** — saw avec unison modéré, F ouvert, léger pitch scoop; jouer phrase chantable. M1 brightness, M2 spread, M3 edge, M4 space.
3. **FM glass** — A sinus, B FM harmonique faible, E moyenne; attaques nettes et longues fins choisies. M1 FM, M2 decay, M3 tone, M4 delay.
4. **Brass synth** — saw/pulse, F enveloppe d'ouverture, attaque 20–100 ms; appels avec silence de souffle. M1 filter, M2 attack, M3 rasp, M4 room.
5. **Mono glide** — saw/triangle, portamento 40–120 ms, notes chevauchées sélectivement; ne pas glisser sur chaque note. M1 glide, M2 tone, M3 drive, M4 delay.

## Plucks

1. **Wooden** — triangle + noise discret, F passe-bas, decay 100–300 ms. M1 knock, M2 decay, M3 tone, M4 room.
2. **FM bell** — A sinus, B FM non entière modérée, decay 250–900 ms, sub coupé. M1 metal, M2 decay, M3 damping, M4 delay.
3. **Future house** — saw/pulse, F enveloppé, attack courte, release maîtrisé; contretemps. M1 brightness, M2 pluck length, M3 grit, M4 width.
4. **Kalimba synth** — A sin + overtone court, N transient doux; vélocité expressive. M1 tine, M2 decay, M3 noise, M4 ambience.
5. **Rubber** — A riche, F résonant à sweep descendant court, modulation de pitch subtile. M1 vowel, M2 bounce, M3 drive, M4 room.

## Pads

1. **Warm analog** — saw + triangle détunés modérément, attaque 300–1000 ms, F lent. M1 warmth, M2 motion, M3 saturation, M4 width.
2. **Air choir** — source formant douce + N air, attaque longue, L lent. M1 vowel, M2 breath, M3 shimmer, M4 tail.
3. **Dark film** — source grave filtrée + harmonique haute séparée, modulation lente; retirer sub sous basse. M1 darkness, M2 instability, M3 grit, M4 depth.
4. **Rhythmic pad** — accord tenu, L amplitude discret synchronisé; silence sur attaque du kick. M1 cutoff, M2 pulse, M3 density, M4 space.
5. **Granular haze** — source sample/granular autorisée, mouvement faible, filtre mouvant, longue enveloppe. M1 grain, M2 drift, M3 noise, M4 tail.

## Drones

1. **Tonal pedal** — sinus + octave/harmoniques discrètes, très longue E, root fixe. M1 root color, M2 slow motion, M3 edge, M4 distance.
2. **Industrial** — FM basse non harmonique hors sub, saturation contrôlée, long mouvement de F. M1 metal, M2 motion, M3 grit, M4 room.
3. **Organic wind** — N bandpass + source tonale faible, L aléatoire lent; fond sans masquer voix. M1 wind, M2 drift, M3 pitch, M4 tail.
4. **Suspense cluster** — deux notes proches dans médium, battement lent; relâcher à la résolution. M1 interval, M2 beating, M3 darkness, M4 space.
5. **Sub atmosphere** — fondamentale très faible + harmonique audible sur petit système, gain bas; mono dans bas. M1 harmonics, M2 movement, M3 texture, M4 tail mid.

## Ambiances

1. **Tape room** — N rose filtré, légère fluctuation, réverbération en retour. M1 hiss, M2 wobble, M3 warmth, M4 size.
2. **City futuristic** — échantillon autorisé + synth tonal, filtrage et automation; éviter de promettre lieu réel. M1 detail, M2 motion, M3 tone, M4 distance.
3. **Underwater** — bruit bas filtré, pitch/modulation lente, délais sombres. M1 depth, M2 bubble, M3 modulation, M4 space.
4. **Vinyl haze** — noise/transient rares, pad doux, largeur contrôlée; aucun sample sans droits. M1 crackle, M2 lowpass, M3 flutter, M4 room.
5. **Night air** — N highpass doux, notes sporadiques et longue queue, garder un silence musical. M1 air, M2 event rate, M3 tone, M4 width.

## Risers

1. **Noise sweep** — N filtré avec cutoff croissant sur 4/8/16 mesures, gain contrôlé. M1 duration, M2 brightness, M3 grit, M4 width.
2. **Pitch climb** — A source harmonique avec automate de hauteur, tension vers note cible; imprimer audio. M1 range, M2 speed, M3 edge, M4 delay.
3. **FM tension** — A/B, FM croissante et F bandpass montant, maîtriser aigus. M1 FM, M2 cutoff, M3 density, M4 width.
4. **Reverse vocal** — sample vocal autorisé resamplé/inversé + fade et reverb; Serum sample si adapté. M1 formant, M2 rise, M3 grit, M4 tail.
5. **Perc roll** — N transient court répété avec accélération MIDI/automation; retirer avant impact. M1 density, M2 pitch, M3 brightness, M4 room.

## Impacts

1. **Clean hit** — N transient + corps sin 150–400 ms et queue indépendante. M1 click, M2 body, M3 tone, M4 tail.
2. **Metal slam** — FM non harmonique brève, bruit filtré, réverbération coupée par section. M1 metal, M2 punch, M3 distortion, M4 size.
3. **Sub drop** — sinus pitch descendant 150–600 ms, rien d'autre en grave au même instant. M1 range, M2 decay, M3 harmonics, M4 click.
4. **Cinematic boom** — transient + corps grave + noise large, imprimer trois stems pour équilibre. M1 hit, M2 sub, M3 grit, M4 tail.
5. **Reverse impact** — imprimer reverb d'un hit et inverser, couper précisément au drop; son final resamplé. M1 rise, M2 filter, M3 width, M4 release.

## Contrôle de sortie

Accorder kicks longs et éléments tonals, contrôler le grave en mono et la somme kick/sub par note. Écouter à faible niveau et sur petit haut-parleur; mesurer pics, corrélation et dynamique sans fixer de cible universelle. Comparer une référence licite à niveau perçu comparable, vérifier fatigue/aigus, préserver marges de mix, imprimer stems propres et versions sèches. Validation de piste et décision de sortie se font sur le morceau, après écoute réelle, pas sur cette liste de recettes.
