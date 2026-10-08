# Maschine MK3 : production et jeu

## Recette de 8 mesures

1. Charger ou bâtir un kit, nommer les 16 pads du Group et contrôler les droits et l'origine des samples.
2. Enregistrer (kick si le chemin Maschine est retenu), snare/clap, hats et percussion sur 4 ou 8 mesures. Faire trois Patterns A/B/C : A sobre, B réponse syncopée, C transition. Ne changer qu'une ou deux variables à la fois.
3. Ajuster vélocité et timing aux pads. Pas d'humanisation aléatoire (`../../../SKILL.md` §3) : vélocités en motif répété, micro-décalage par couche ; Variation/Humanize seulement à la demande de l'utilisateur, résultat relu puis figé. Ne pas randomiser le kick principal.
4. Échantillonner une source autorisée, définir les points de coupe et slicer; exporter les slices vers Sound/Group, relire le Pattern créé (capture) et le faire écouter. Resampler une phrase si la texture fait partie du hook; conserver la source.
5. Combiner Patterns dans Scenes intro/drop/break, puis Sections en Song view. Pour un fill spécifique, vérifier si le Pattern est partagé et rendre la variation locale.
6. Comparer groove/énergie à la référence sélectionnée à niveau comparable; écrire ce qui est différent dans notre composition.

Pour les drops de 16 ou 32 mesures, marquer les frontières toutes les 8 mesures. Déclencher une variation de kit à chacune, avec des intensités différentes : mini-fill, réponse de percussions, reverse cymbal ou retrait bref. Placer le pic du reverse juste avant le temps 1 suivant, puis tester sa collision avec crash, kick et basse. Prévoir un fill plus marqué au changement de section. Enregistrer les gestes Perform FX seulement sur les éléments routés par le Master principal dans la configuration de l'utilisateur.

## Fonctions à distinguer

Le détail de Patterns, Scenes, Sections, Clips, sampling et export est dans `../../native-instruments-control/references/maschine.md` ; ne sont gardées ici que les distinctions utiles à la production.

- Ideas view : expérimenter Patterns et Scenes sans arrangement linéaire.
- Song view : Sections et Clips pour structurer un morceau. Une modification d'un Pattern référencé peut toucher plusieurs occurrences.
- Variation : générer ou humaniser selon le contexte, toujours contrôler les notes finales.
- Maschine 3 : certaines installations offrent stem separation, bounce in place, édition MIDI étendue et tempo par Scene; vérifier version, licences et résultat avant d'en dépendre.
- MK3 comme contrôleur du plugin Maschine et MK3 en mode contrôle Live avec template sont deux configurations distinctes.

## Sources Native Instruments

- Patterns, Clips, Variation : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/working-with-patterns-and-clips
- Ideas/Song/Scenes : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/working-with-the-arranger
- Sampling et slicing : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/sampling-and-sample-mapping
- Export et sauvegarde avec samples : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/managing-sounds%2C-groups%2C-and-your-project
- Compatibilité et fonctions Maschine 3 : https://support.native-instruments.com/support/solutions/articles/69000879554-guide-to-maschine-3-features-and-compatibility
