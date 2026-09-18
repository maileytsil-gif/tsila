---
name: synthese-reference
description: Analyser un extrait audio de référence FOURNI (fichier WAV/MP3 d'une basse, d'un lead, d'un pluck, d'une nappe, d'un arpège, d'une texture) et reconstruire un son jouable dans Serum ou un instrument natif Ableton, avec chaîne d'effets, comparaison mesurée et sauvegarde ; scripts analyze_synth.py, report_to_patch.py, compare_reports.py, test_clip.py. Utilise ce skill quand un fichier audio de référence est disponible ou peut l'être ; distinguer synthèse, resynthèse et simple lecture de sample ; sans fichier, le rôle sound-designer-serum conçoit le son de mémoire.
---

# Analyser puis reconstruire un son de synthé

## Résultat attendu et accès
Produire une analyse argumentée, un patch jouable et sa chaîne d'effets adaptée, puis un test comparatif. Le résultat doit identifier ce qui est observé, estimé et effectivement réalisé. Ne pas promettre de retrouver exactement un synthé, un preset ou tous les réglages à partir du seul audio : plusieurs architectures peuvent produire des résultats proches.

Ce skill est utilisable dans Claude Desktop/claude.ai, Claude Code et les environnements compatibles avec SKILL.md. Ses ressources sont relatives au dossier du skill. Il ne fournit pas Serum, les licences, les effets ou les connexions au Mac. Vérifier accès aux fichiers, audio, synthés et outils de contrôle. Un terminal distant ne donne pas automatiquement accès à Live. Sans pilotage disponible, fournir une fiche de patch et de chaîne exploitable ; sans écoute, présenter l'analyse comme technique et la ressemblance comme restant à valider.

Dans cette configuration, « synthé natif » désigne par défaut les instruments d'Ableton. Si l'utilisateur précise Native Instruments, identifier l'instrument concerné : Komplete Kontrol est un hôte de navigation/contrôle, pas un moteur de synthèse unique. Adapter alors la méthode au moteur effectivement disponible.

## 1. Référence
Lire [references/analyse.md](references/analyse.md). Utiliser l'extrait fourni et le passage visé. Pour une demande future sans référence accessible, demander seulement le fichier ou passage manquant ; la création de ce skill ne nécessite pas de son à analyser maintenant.

Relever note(s), registre, durée, vélocité si connue, tempo si pertinent, stéréo et contexte sec/traité. Préférer une note isolée avec attaque, tenue et relâchement quand disponible. Dans un mix, documenter les sources concurrentes et la limite de séparation ; ne pas attribuer à la synthèse les caractéristiques du kick, des voix ou du mastering.

L'analyseur optionnel `scripts/analyze_synth.py` fournit enveloppe RMS, spectre, stéréo et hypothèses de hauteur pour une note isolée. Lire son usage et ses limites dans la référence. Il ne reconnaît pas un preset et ne remplace pas l'écoute.

## 2. Hypothèse de synthèse
Lire [references/reconstruction.md](references/reconstruction.md). Choisir le synthé demandé s'il permet le résultat ; si le choix est libre, retenir l'architecture la plus simple qui couvre les indices importants. Vérifier version et instruments autorisés dans l'édition de Live.

Séparer le cœur du timbre des effets : oscillateurs/bruit → enveloppes et filtre → modulations/jeu → effets. Garder une hypothèse principale et une alternative quand l'audio est ambigu. Présenter les indices qui orientent le choix, sans pourcentage de certitude inventé.

La synthèse à partir d'oscillateurs est le point de départ pour un patch jouable. L'import en wavetable, la resynthèse spectrale ou le sampling sont des voies possibles si elles correspondent au résultat demandé ; les annoncer clairement. Ne pas présenter la simple lecture du fichier de référence comme une reconstruction par synthèse.

## 3. Construction
Créer une piste de travail ou une version préservée de la piste cible pour la reproduction demandée. Ne pas modifier l'arrangement ou remplacer une chaîne existante au-delà de cette demande. Charger un état initial ou un preset de départ explicitement choisi ; observer la cible pour éviter un remplacement accidentel par hot-swap.

Régler d'abord note, octave, accordage, gain et enveloppe d'amplitude ; ensuite source harmonique, filtre, enveloppes de timbre et modulations. Changer une famille de paramètres à la fois et relire les valeurs. Les coordonnées d'une ancienne interface et les noms supposés de paramètres ne sont pas une preuve de contrôle.

Dans Live : `../ableton-live-session/SKILL.md` (règles, hot-swap) et `../vst-sound-design/SKILL.md` ; Serum 2 se règle par clics dans sa fenêtre selon `../vst-sound-design/references/serum2.md` (ce qui passe en arrière-plan et ce qui ne passe pas) ; les natifs par `ppal-update-device` avec relecture. Ne pas supposer que Producer Pal expose tous les paramètres natifs : lire les paramètres de l'instance actuelle.

## 4. Chaîne d'effets
Lire [references/effets.md](references/effets.md). Choisir les effets audibles dans la référence et ceux nécessaires à l'intégration, en distinguant ces deux rôles. Respecter la préférence connue pour les effets tiers, notamment Waves, sauf demande de chaîne entièrement native. Les effets internes de Serum restent un choix de patch à préciser.

Détailler l'ordre, les réglages importants, le dosage, les routages/sends et le but de chaque étage. Préserver les sidechains et automations existantes à moins que la demande nécessite leur modification. Garder une version sèche pour isoler les causes d'écart.

## 5. Comparer et livrer
Lire [references/comparaison-livraison.md](references/comparaison-livraison.md). Comparer aux mêmes notes, durées et niveau d'écoute cohérent. Vérifier timbre sec, attaque, tenue, queue et version traitée. Un score spectral, une corrélation ou un signal de différence ne sont pas un pourcentage objectif de ressemblance.

Corriger les écarts les plus audibles, puis tester plusieurs notes et vélocités pour confirmer que le patch est jouable. Sauvegarder le preset natif, la chaîne/rack, les ressources externes nécessaires et un extrait de démonstration lorsque les outils le permettent. Vérifier le rappel. Si l'export de preset n'est pas disponible, fournir une fiche des paramètres et annoncer cette limite au lieu de fabriquer un faux fichier de preset.

## 6. Boucle mesurée dans Live (ajout local, 14 sept. 2026)
Sans oreilles, la comparaison se fait par mesures, à niveau égalisé, avec trois scripts (`scripts/`) :
1. `analyze_synth.py` sur la référence → `report_to_patch.py rapport.json --tempo BPM` : **fiche de départ** chiffrée (f0 et stabilité, ADSR estimé sur la RMS, profil pair/impair → forme d'onde candidate, centroïde → cutoff de départ, side/mid → unisson/largeur, niveau RMS cible). Chaque ligne est une hypothèse ; une attaque « longue » sur un extrait de mix peut venir du sidechain ou d'un fondu, pas du synthé.
2. Construire le patch (skill `vst-sound-design` : natifs par API, Serum 2 par clics), puis `test_clip.py` — le copier dans le scratchpad avant d'éditer PISTE/NOTES, pour ne pas désynchroniser les deux copies du skill — (via `../ableton-live-session/scripts/pyl.sh`) : pose un clip MIDI de test hors morceau (mesure 131 par défaut, mêmes notes que la référence, 2 s + silence) ; exporter cette plage avec « Piste convertie » = la piste (skill `live-export-wav`), analyser le rendu avec les mêmes options, puis `test_clip.py` avec `SUPPRIMER = True`.
3. `compare_reports.py reference.json candidat.json` : écarts hiérarchisés (hauteur en cents, centroïde en octaves, H2–H8, attaque/decay/sustain, largeur) avec le **paramètre candidat** à corriger ; un seul changement par cycle, dans l'ordre hauteur → attaque → tenue → mouvement → effets.
Notes propres à ce Mac (dépendances installées, liens vers les skills de pilotage) : `references/notes-locales.md`.
