# Traduire une analyse de référence en automations exécutables — v7

Le bridge ne doit jamais recevoir « reproduis l'automation de tel morceau » comme instruction brute.

1. Lire la fiche de référence et choisir un **vecteur abstrait** : montée de brightness, retrait du sub, assèchement avant impact, variation de width, augmentation de send, etc.
2. Demander des paramètres réellement exposés dans Live.
3. Créer une courbe originale liée à la durée du projet utilisateur.
4. Snapshot avant écriture/modulation ; vérifier valeur après action ; restaurer en cas d'échec.
5. Distinguer mouvement temps réel et enveloppe persistante selon les capacités réellement installées.

Exemple abstrait : `brightness 0.25→0.70 sur 8 mesures; reverb_send 0.10→0.35 puis 0.05 juste avant impact; sub mute pendant la dernière demi-mesure`. Les valeurs sont un exemple [HEUR], jamais une transcription d'une référence commerciale.
