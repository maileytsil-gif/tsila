---
name: native-instruments-control
description: Utiliser Maschine et Komplete Kontrol de Native Instruments, en logiciel autonome ou plug-in, et accompagner leur utilisation avec les contrôleurs Maschine et claviers Kontrol. Pour les presets NKS, patterns, sampling, arrangement, mixage, modulation, MIDI, intégration DAW, exports et dépannage de ces produits.
---

## Contexte local (lire d'abord)

- Maschine 3.6 et Komplete Kontrol 3.5 n'ont **aucune API** : uniquement contrôle d'écran au premier plan (`request_full_control`), capture après chaque geste, rien en arrière-plan ; l'utilisateur fait ce qui n'est pas atteignable. Ne pas inventer de coordonnées : les relever sur capture.
- Dans Live, Maschine, Komplete Kontrol et **Battery 4** (VST3 présent) se chargent par le navigateur du LOM Bridge avec la règle anti hot-swap de `../ableton-live-session/SKILL.md` ; vérifier `len(d.parameters)` après chargement (1 = fenêtre seulement) ; techniques de fenêtre dans `../ableton-live-session/references/plugins.md`. Les sons Battery utilisés par la batterie sont référencés dans `../drums-signature/references/sons.md`.
- Règles de session (transport, sauvegarde par menu, une étape par échange) : `../ableton-live-session/SKILL.md`.

# Maschine et Komplete Kontrol

## Identifier la cible
- Distinguer le logiciel Maschine de son contrôleur, et Komplete Kontrol du clavier Kontrol. Identifier version logicielle, modèle/génération matériels, mode autonome ou plug-in, hôte et instance cible. Ne demander que les informations nécessaires qui ne sont pas observables.
- Sur le Mac d’origine, les bundles VST3 et AU de Maschine 3.6.0 et Komplete Kontrol 3.5.4 ont été repérés le 14 septembre 2026. Ce constat ne prouve ni le fonctionnement, ni l'activation, ni la présence d'un contrôleur. Relire les versions si nécessaire dans les Info.plist des bundles sous /Library/Audio/Plug-Ins.
- L'utilisateur souhaite les logiciels ET le matériel. Matériel déclaré : Maschine MK3 et clavier **Komplete Kontrol A49** (confirmé par l'utilisateur le 26 sept. 2026 ; la mention « S48 » antérieure était erronée) : série A, ne pas lui prêter les fonctions de la série S (écrans, light guide). Ne pas assimiler MK3, Mikro, Jam et Maschine+, ni claviers A, M, S et générations MK1/MK2/MK3. Vérifier les fonctions supportées pour le couple matériel/logiciel exact.

## Choisir un moyen de contrôle réel
Privilégier un outil spécialisé disponible et documenté. À défaut, utiliser le contrôle d'interface pour les logiciels : observer la fenêtre cible, agir, puis relire le résultat. Ne pas inventer d'API Maschine/Komplete Kontrol, de raccourcis ou de coordonnées mémorisées.

Dans Ableton, lire le skill ableton-live-session pour le pilotage de l'hôte. Producer Pal et le LOM de Live ne donnent pas automatiquement accès au séquenceur interne, au navigateur et à tous les paramètres des plug-ins NI. Utiliser leur interface pour ce qui n'est pas effectivement exposé. Pour une automation d'arrangement Live, consulter live-automation.

Un clic logiciel ne constitue pas un appui physique sur un pad ou un encodeur. Utiliser une interface MIDI seulement si un outil et son protocole sont réellement disponibles ; sinon guider l'utilisateur pour le geste matériel indispensable. Ne jamais annoncer un test matériel effectué sans observation. Le skill apporte des méthodes, pas une garantie d'accès automatique à toutes les fonctions.

## Exécuter et vérifier
1. Lire le projet, la sélection et le transport : instance, Sound/Group ou instrument, pattern/scene, slot et page de paramètres selon le produit.
2. Adapter la modification à la demande. Avant un remplacement susceptible de perdre des éditions, préserver l'état concerné par duplication ou sauvegarde appropriée. Éviter de changer de projet pour une simple recherche de preset.
3. Lire la référence adaptée : [Maschine](references/maschine.md) ou [Komplete Kontrol](references/komplete-kontrol.md). Pour une fonction non détaillée, ouvrir le chapitre officiel pertinent et vérifier sa compatibilité avec la version installée. Ces références sont des guides de travail, pas une transcription exhaustive des manuels.
4. Effectuer une modification cohérente, puis vérifier sa cible et son effet. Distinguer valeur affichée, signal mesuré et résultat réellement écouté ; ne pas prétendre avoir écouté sans accès audio.
5. Sauvegarder les modifications demandées avec les ressources nécessaires. Pour un plug-in, vérifier la sauvegarde de l'hôte ; sauver séparément un preset ou projet NI si cela sert la demande. Signaler ce qui a été vérifié et les limites restantes.

## Diagnostic
Partir du symptôme : contrôleur non détecté, absence de MIDI, absence d'audio, preset manquant, plug-in absent ou paramètres non accessibles. Vérifier successivement la cible, son routage et les préférences pertinentes. Ne pas réinstaller, supprimer une base de données ou migrer un format de plug-in comme première réponse. Une demande de création de musique ne vaut pas demande d'achat, de mise à jour ou de changement de firmware.
