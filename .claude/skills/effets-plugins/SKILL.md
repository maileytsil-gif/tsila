---
name: effets-plugins
description: Construire, régler et vérifier les chaînes d'effets dans Ableton Live avec les plug-ins tiers de l'utilisateur (FabFilter Pro-Q 4, Waves REQ 6/API-2500/L2/J37/MetaFlanger/F6, Plugin Alliance bx_glue, oeksound soothe3, iZotope Imager/Insight/Tonal Balance, Voxengo SPAN) et, si demandé, les natifs : routage, ordre des devices, paramètres réellement pilotables, comparaison à niveau équivalent, sidechain, limiteur d'export. Utilise ce skill dès que l'utilisateur parle d'EQ, de compression, de glue, de réverb/delay en envoi, de saturation, de limiteur, de chaîne, de bus, de « laisse de la place au kick », de résonance, ou nomme un plug-in.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Effets et plug-ins : ce qui est pilotable, comment vérifier

## Avant de régler
1. Lire la chaîne (`[d.name for d in t.devices]`) et le routage (skill `ableton-live-session`).
2. Ouvrir la **fiche du plug-in** dans `references/` (une par plug-in et version) : paramètres exposés à Live (scriptables et relisibles), opérations qui exigent la fenêtre, méthode de vérification, réglages déjà validés. Plug-in inconnu → `probe_params.py` (skill `vst-sound-design`) sur une piste vide, puis créer sa fiche.
3. Charger avec `lom.py load "<piste>" "<plug-in>"` (anti hot-swap vérifié) ; pour insérer avant un device existant, charger en fin puis `ppal-update-device toPath`.

## Régler
- Exposé → `helpers.solve(p, valeur)` / `set_enum(p, 'label')` (skill `ableton-live-session`), relecture `str_for_value`.
- Fenêtre seulement → clics/glisser/molette avec capture après chaque geste ; ce qui ne passe pas en arrière-plan (saisie clavier FabFilter, glisser Serum) → plein écran ou demander à l'utilisateur ; ne jamais affirmer un réglage non relu.
- Toujours à **niveau équivalent** : comparer les crêtes du bus device actif / `is_active = False` sur une boucle (`lom.py meters`), compenser par le makeup ou un Utility, pas par un fader automatisé.
- « Laisser de la place » : coupe-bas et creux sur la piste qui gêne (REQ 6), sidechain sur celle qui doit céder (source = piste kick, Post FX), plutôt qu'un boost sur l'autre.
- Dynamique/spectral à la source (soothe3, F6, Pro-Q dynamique), master léger ; limiteur uniquement en fin de BUS MASTER 3, la REF routée hors limiteur.

## Fiches
`references/fiches.md` — index et fiches par plug-in (exposé / fenêtre / vérification / réglages validés). `references/chaine-actuelle.md` — la chaîne complète du morceau en cours avec toutes les valeurs.
