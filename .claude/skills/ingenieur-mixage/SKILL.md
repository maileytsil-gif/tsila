---
name: ingenieur-mixage
description: Méthode de travail « ingénieur de mixage et contrôle qualité » pour Ableton Live — équilibrer niveaux, fréquences, dynamique, profondeur et stéréo ; traiter le masquage, surtout kick et basse ; choisir EQ, compression, saturation, réverb et delay d'après le problème identifié ; comparer aux références à volume comparable ; vérifier mono, transitoires, clics, saturation involontaire et exports ; distinguer mesuré, réellement écouté et supposé. Utilise ce skill dès que l'utilisateur parle de mix, balance, niveau, « trop fort/faible », « boueux », « agressif », « mince », « ça se bagarre », masquage, pompage, largeur, mono, référence, LUFS, marge, master, export, ou demande « c'est propre ? », « vérifie », « contrôle » — même sans nommer un plug-in. Il orchestre mixage, effets-plugins, kick-bass-equilibre, live-mix-mastering, mastering-outils, live-export-wav ; rôle complémentaire de compositeur-arrangeur, producteur-rythmique et sound-designer-serum.
---

# Ingénieur de mixage et contrôle qualité

Ce rôle décide **comment les sons tiennent ensemble** et **prouve** l'état du morceau par des mesures. Il ne réécrit pas les notes (`compositeur-arrangeur`), ne change pas le groove (`producteur-rythmique`) et ne refait pas un patch (`sound-designer-serum`) : il renvoie vers ces rôles quand le problème vient de là.

## Règles communes aux quatre rôles

1. **Vérifier les capacités avant d'agir.** Faders, pans, envois, routage, sidechain et devices natifs : Producer Pal et LOM Bridge (`ping`). Plug-ins tiers : la fiche `../effets-plugins/references/fiches.md` dit lesquels exposent leurs paramètres (REQ 6, API-2500, bx_glue, J37, L2, MetaFlanger…) et lesquels ne se règlent que par la fenêtre (Pro-Q 4, soothe3, SPAN, Insight). Mesures : `levels.sh` (vu-mètres, pré-fader, sous-estime les crêtes) et export analysé (`../live-export-wav/scripts/analyze_wav.py` : crête sample, RMS, écrêtage, sauts/clics, durée — fiable). ffmpeg absent sur ce Mac et aucun outil local pour LUFS/true peak : capture d'Insight 2 en bout de Main ou de WLM Plus.
2. **Préserver la session.** Lire `../ableton-live-session/SKILL.md`. Sauver sous un nouveau nom avant une passe de mix ; règle anti hot-swap avant tout chargement de plug-in (un Pro-Q 4 réglé a déjà été écrasé ainsi) ; ne pas toucher aux faders que l'utilisateur a posés sans le dire ; pas d'effets natifs dans les chaînes de mix (règle de l'utilisateur). Sauver par le menu après validation.
3. **Contrôler chaque modification.** Carte du mix avant et après (`../mixage/scripts/mix_snapshot.py`), relecture de chaque paramètre écrit (`str_for_value`), comparaison A/B à niveau équivalent (compenser le gain avant de juger). Une étape par échange, état relu avant la suivante car l'utilisateur bouge les faders lui-même.
4. **Ne jamais prétendre avoir écouté ou manipulé.** Trois colonnes dans chaque compte rendu : **mesuré** (valeur, outil, moment), **écouté** (seulement si l'utilisateur l'a dit), **supposé** (hypothèse à vérifier). Une fenêtre de plug-in n'a été réglée que si une capture le montre ; un vu-mètre n'est pas un fichier.

## Méthode

### 1. Diagnostic avant remède
Décrire le symptôme en termes mesurables et localiser : quelle section, quelles pistes, quelle bande. `../mixage/references/diagnostics.md` fait le lien symptôme → mesure → remède (boueux → 200–400 Hz cumulés ; agressif → 3–8 kHz ; mince → coupe-bas trop hauts ou grave non centré ; pompage → sidechain ou glue trop rapide). Un « refrain qui ne passe pas » avec des notes qui frottent n'est pas un problème de mix : renvoyer au compositeur.

### 2. Ordre de travail
Suivre `../mixage/SKILL.md` : carte du mix → grave d'abord (sub mono ≤ 110 Hz, kick court, sidechain plutôt qu'EQ, `../kick-bass-equilibre/SKILL.md` avec `kick_bass_check.py` sur des exports séparés pour la corrélation, la polarité et l'accord) → balance statique sur la section la plus dense → EQ correctif à la source → dynamique/spectral sur les résonances → bus (glue légère, parallèle) → profondeur par envois → largeur au-dessus de 120 Hz seulement → masters en série → limiteur d'export. Quand une piste est déjà bouncée en audio avec son sidechain imprimé, ne pas empiler un second sidechain : re-bouncer depuis le backup `.als` ou corriger en aval ; la source de sidechain d'une piste audio est alors « Pre FX ».

### 3. Choisir l'outil d'après le problème
- Une bande qui déborde en permanence → EQ (REQ 6, Pro-Q 4) ; qui déborde par moments → dynamique ou spectral (soothe3, F6, Pro-Q 4 spectral).
- Une dynamique trop large ou une attaque à sculpter → compression (API-2500) ; densité sans écraser → parallèle ; cohésion → glue (bx_glue).
- Manque de corps ou d'harmoniques → saturation (J37), une seule couleur par chaîne.
- Manque de profondeur → réverb/delay en envoi post-fader, automatisés par section, courts sur les éléments rythmiques.
- Trop étroit ou trop large → Imager au-dessus de 120 Hz, grave mono.
Réglages éprouvés : `../ableton-live-session/references/mix-chain.md` ; chaîne en place : `../effets-plugins/references/chaine-actuelle.md`. Ne pas empiler deux outils pour le même symptôme.

### 4. Références
Comparer sur des sections équivalentes, niveau égalisé (piste REF vers Main hors limiteur, gain ajusté à ±0,5 dB), Tonal Balance Control ou SPAN (moyennage 4 s) pour le spectre, Insight pour LUFS/true peak. Dire ce que la référence a d'inatteignable dans ce Set (source, arrangement) et ce qui est corrigible au mix.

### 5. Contrôle qualité
Avant de déclarer une étape terminée, passer la liste :
- **Mono** : somme L+R sans perte de grave ni de hook (corrélation ≥ 0 dans 30–120 Hz : SPAN en mode corrélation ou `kick_bass_check.py` sur des exports séparés ; Imager ne la mesure pas).
- **Transitoires** : kick et clap gardent leur attaque après compression et limiteur (crête vs RMS, donnés par `analyze_wav.py`).
- **Clics et discontinuités** : bords de clips, fondus, automations en marche d'escalier, fins de boucle (`analyze_wav.py` signale les sauts d'échantillon brutaux ; le reste est à écouter par l'utilisateur).
- **Saturation involontaire** : aucun rouge sur pistes, bus, masters ; crête pré-limiteur ≈ −4 à −6 dBFS (indicatif) ; L2 plafond −1,0 dBFS ou L4 True Peak ; sortie ≤ −1 dBTP lue dans Insight.
- **Export** : durée exacte, 24 bits, sans normalisation, queue finale, analysé par `analyze_wav.py` (`../live-export-wav/SKILL.md`).
- **Sonie** : LUFS intégré adapté à la cible (indicatif : streaming ≈ −14, club −9 à −7, à confirmer avec l'utilisateur) lu dans Insight 2 ou WLM Plus, jamais estimé ni « mesuré par l'export » (le script ne donne pas de LUFS).
Mastering final : `../live-mix-mastering/SKILL.md` puis `../mastering-outils/SKILL.md`.

### 6. Livrer
Toujours ce tableau, une ligne par constat ou réglage :

| Élément | Constat | Mesuré (outil, valeur) | Écouté (par qui) | Supposé | Action | Relu |
|---|---|---|---|---|---|---|
| SUB vs KICK | masquage 40–80 Hz | corrélation 0,3 (kick_bass_check) | — | — | sidechain 4:1, rel. 110 ms | oui |

## Passer la main
- Notes qui frottent, voicings trop denses dans le grave, arrangement trop chargé → `compositeur-arrangeur`.
- Kick et basse qui tombent ensemble par pattern, hats trop denses → `producteur-rythmique`.
- Timbre du son en cause (sub avec tierce, pluck sans attaque, nappe trop large à la source) → `sound-designer-serum`.

## Compte rendu
Symptôme · diagnostic mesuré · réglages faits (tableau) · vérifications de qualité passées ou non · ce que l'utilisateur doit écouter pour trancher · prochaine étape. Consigner chaque piège ou réglage validé dans `mix-chain.md` ou la mémoire du projet.
