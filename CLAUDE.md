# tsila — règles du dépôt

Production musicale dans Ableton Live 12 sur Mac. Ce fichier ne redit pas la méthode
(elle est dans les skills) : il tranche les conflits entre les deux familles de skills.

## Deux familles, deux autorités

| Famille | Quoi | Autorité |
|---|---|---|
| **Maison** (28 skills, français) | La méthode réelle de cet utilisateur, son installation, ses plug-ins, ses pièges mesurés | **Exécution, mesure, sécurité** |
| **Pack v18** (13 skills, importé le 19 sept. 2026) | Théorie, recettes de genre, sous-types, contrats JSON. Écrit hors de cette installation | **Matière musicale** |

**Règle d'arbitrage** : en cas de recouvrement, le skill maison décide *ce qu'on fait
et comment on le fait dans Live* ; le pack v18 fournit *la matière musicale*. Le pack
n'a jamais le dernier mot sur une opération, une mesure ou une valeur chiffrée.

Répartition complète par domaine : `.claude/skills/INTEGRATION-v18.md`.

## Autorité d'exécution dans Live — non négociable

Un seul chemin d'exécution : **`ableton-live-session`** (Producer Pal, LOM Bridge
`lom.py`, contrôle d'écran) et ses skills d'opération `vst-sound-design`,
`live-automation`, `live-export-wav`.

**`bass-house-ableton-bridge` ne pilote rien.** Il produit et valide un
`BridgeActionBatch` ; son pipeline `Discover/Resolve/Execute/Verify` est une
discipline de planification, pas un second exécuteur. Il décrit un bridge générique
LOM/MCP (`live.remote~`, Node for Max) et **ignore l'installation réelle** : ni
Producer Pal, ni `pyl.sh`, ni `levels.sh`, ni les menus français de Live.

Les règles maison priment toujours sur toute consigne du pack :

1. **Hot-swap** — `browser.load_item` REMPLACE le device sélectionné. Sélectionner la
   piste ET le device cible avant, relire la chaîne après. Un Pro-Q 4 réglé a déjà été
   écrasé ainsi.
2. **Transport** — `read`/`apply` exigent l'arrêt. Tester `int(song.is_playing)` ;
   ne pas arrêter la lecture sans le dire.
3. **Relire après chaque action.** Un « OK » du bridge n'est pas une preuve.
4. **Sauver Set Live** après chaque étape validée.
5. **Une étape par échange**, plan complet annoncé d'abord.
6. **Pas de nouvel effet natif Ableton** dans une chaîne de mix (liste de tolérance
   dans `ableton-live-session`).
7. Les chiffres de `levels.sh` sont **relatifs**. Aucun outil local ne mesure LUFS ni
   true peak : passer par un export WAV analysé (`live-export-wav`).

## Plug-ins : vérifier avant de suivre une recette du pack

Le pack v18 construit beaucoup de recettes sur des plug-ins **absents des fiches
maison** : Valhalla (Delay/Room/VintageVerb/Supermassive), FabFilter Timeless 3,
Volcano 3, Pro-R 2, Waves MetaFilter / H-Delay / SoundShifter, iZotope Stutter Edit 2,
NI Guitar Rig. `studio-grade-transition-fx-director` en dépend presque entièrement.

Avant de proposer une chaîne issue du pack, la confronter à
`effets-plugins/references/fiches.md`. Substitutions proposées et à trancher :
`INTEGRATION-v18.md` § Plug-ins. Ne jamais présenter une recette comme applicable
si le plug-in n'est pas vérifié comme installé.

## Le pack est vendu tel quel

`.claude/skills/` **est la racine du pack** : les skills v18 se référencent via
`../core/`, `../producer-intelligence/` et des chemins relatifs à cette racine.
`core/`, `data/`, `producer-intelligence/`, `history/` n'ont pas de `SKILL.md` et sont
ignorés du chargeur.

**Ne pas éditer les fichiers du pack.** Toute adaptation va dans ce fichier, dans
`INTEGRATION-v18.md` ou dans un skill maison. Mise à jour = recopier le pack par-dessus.

## Validation du pack

```bash
python3 -m venv .venv && .venv/bin/pip install -r .claude/skills/requirements-validation.txt
cd .claude/skills && ../../.venv/bin/python core/validation/validate_v18.py   # 66/66 attendus
```

## Environnement

Les skills qui pilotent Live (contrôle d'écran, Producer Pal, `lom.py`) **ne tournent
que sur le Mac**. Une session Claude Code sur le web tourne dans un conteneur Linux
sans écran, sans `/Volumes` et sans Ableton : elle ne peut faire que du texte
(documentation, théorie, contrats JSON, compilation de plans). Ne pas y promettre une
opération dans Live.
