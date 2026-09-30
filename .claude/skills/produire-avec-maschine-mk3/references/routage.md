# Routage Maschine 3 et Ableton Live 12

## Décision Perform FX pour cette installation

| Besoin | Chemin | Vérification |
| --- | --- | --- |
| Jeu Smart Strip/Perform FX du Master Maschine | Sound → Group → Master principal → piste Live | Solo du Sound, action Perform FX, enregistrer wet; vérifier qu'il n'existe pas de doublon dry |
| Mix individuel dans Live sans ce Perform FX | Sound/Group → Ext. 2 à 16 (Ext. 1 = sortie par défaut du Master, = paire 1/2 dans Live) → piste audio Live « Audio From » Maschine, paire (2n−1)/(2n) ; correspondance à confirmer par capture de la page de routage | Master muet pour cet élément, niveau sur la seule piste dédiée |
| Perform FX et piste individuelle | Chemin Master pendant la performance, capturer la prise wet, importer la prise alignée dans Live | Comparer départ, durée et niveau; garder la prise dry si possible |

Le routage vers Ext.1–16 existe dans le manuel NI. Un départ vers une sortie externe évite le traitement placé en aval sur le Master. La limitation formulée par l'utilisateur concerne son Perform FX Master; ne pas généraliser à toute insertion de Perform FX au niveau Sound ou Group sans test du setup réel.

## Intégration Live

1. Charger Maschine 3 par `lom.py load "<piste>" "<nom du plug-in>"` (anti hot-swap), puis vérifier `len(d.parameters)` (1 = fenêtre seulement) : `../../native-instruments-control/SKILL.md`. Confirmer le plugin effectivement chargé et la synchronisation de tempo.
2. Pour multi-out, assigner la sortie Sound ou Group dans Maschine, créer une piste audio Live recevant la paire correspondante et tester une seule percussion avant de multiplier les pistes. Vérifier écoute, monitoring et enregistrement sur chaque paire.
3. Transférer Pattern par glisser-déposer audio ou MIDI selon l'objectif. Le glisser-déposer se fait au premier plan ou par l'utilisateur ; relire le clip obtenu (`ppal-read-clip`). Tester une boucle, l'alignement et la queue d'effet avant un transfert en masse. Pour un effet imprimé, conserver audio wet et indication du chemin.
4. Pour garder le MIDI dans Live, vérifier canaux/notes et routage vers le kit Maschine. Pour les basses Serum, préférer pistes MIDI dédiées.
5. Sauvegarder le projet Maschine avec samples, le Set Live et les exports nommés; rouvrir, relire le routage (capture, `lom.py state`) et faire écouter un passage de chaque route.

Le template de contrôle MK3 pour Live 12.1+ relève du mode Control Surface et ne remplace pas le routage audio du plugin. Suivre la notice officielle correspondant à la version installée.

## Sources officielles

- Routage Sound/Group/Master et sorties Ext. : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/audio-routing%2C-remote-control%2C-and-macro-controls
- Insertion d'effets aux différents niveaux : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/using-effects
- Smart Strip et Perform FX : https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/playing-on-the-controller
- Export audio vers DAW : https://support.native-instruments.com/support/solutions/articles/69000879553-how-to-export-audio-from-maschine-to-a-daw-track
- Template MK3 pour Live : https://support.native-instruments.com/support/solutions/articles/69000879783-native-instruments-how-to-install-maschine-templates-for-ableton-live
- Kits Maschine depuis Live : https://support.native-instruments.com/support/solutions/articles/69000879820-maschine-triggering-drum-kits-from-ableton-live
