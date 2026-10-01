# Radio edit depuis un club mix, et extended depuis un radio edit

## Cible
`Toute famille / radio et streaming 2:30–3:30, ou club 4:30–6:30 / mêmes blocs internes`

Faits vérifiés dans le Harmonix Set `[DOC]` : Memories (Guetta) radio 3:28 contre extended 4:39, Feel So Close (Calvin Harris) 3:22 contre 4:30, Take Over Control (Afrojack) 2:43 contre 6:12 : la différence est presque toute dans l'intro (4–8 → 16–24) et l'outro (8 → 24–48), plus un drop instrumental ajouté après chaque refrain ; les blocs de 16 ne changent pas.

## Radio edit depuis le club mix (dans le même Set)
1. Sauver Set Live sous « <titre> radio ».
2. Boucle sur l'intro DJ à supprimer (par exemple mesures 17–32 : garder 4–8 mesures d'intro), Edition › Sélectionner boucle → Edition › **Supprimer Zone temporelle** : clips, automations et repères se déplacent ensemble.
3. Même chose sur la moitié du breakdown si le premier drop tombe après 1:00, et sur l'outro (garder 4 mesures).
4. Build initial : le retirer ou le réduire à 8 mesures ; premier drop visé entre 0:37 et 1:00 (intro 4 + thème 8 + build 8 = 20 mesures = 37,5 s à 128).
5. `arrangement_map.py`, repère « FIN export » recalé, export 24 bits sans normalisation (`../../live-export-wav/SKILL.md`).
6. Cibles : 104–112 mesures ≈ 3:15–3:30 à 128 ; pop-EDM à la Guetta : refrain chanté 16 puis drop instrumental 8.

## Extended depuis un radio edit
1. Sauver sous « <titre> extended ».
2. Créer › **Insérer Silence** de 16 mesures avant la mesure 1 (intro DJ : kick, hats, percussions, filtre qui s'ouvre) et de 32–48 mesures à la fin (outro : soustraction inverse).
3. Remplir par duplication des clips voisins ; les automations tiennent leur dernière valeur, à redessiner sur le bus (filtre, largeur).
4. Optionnel, à la manière des extended Guetta : un drop instrumental de 16 mesures ajouté après chaque refrain.
5. Intro et outro **sans contenu plein spectre** ; sub absent en intro ; largeur réduite.

## Livrables
Original ou extended · radio edit · instrumental · acapella si libérée · stems drums, bass, music, FX, vocals depuis la mesure 1 (bus `BUS - …` ou pistes individuelles) · premaster à −6 dBFS de crête · nommage `Artist_Title_Version_BPM_Key_Date` ; `../references/arrangement-et-methode.md` § 4.

## Vérification
Chaque version relue par `arrangement_map.py` ; premier drop avant 1:00 en radio ; intro DJ mixable 16–32 en club ; même tonalité, même tempo, mêmes blocs internes ; mémoire du projet mise à jour avec la structure de chaque version.
