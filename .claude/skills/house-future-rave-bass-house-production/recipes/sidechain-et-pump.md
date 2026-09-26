# Sidechain et pump : du « invisible » tech house au pompage de future rave

## Cible
`Kick → sub, basse mid, nappes, lead / par élément, profondeurs différentes / jamais sur un bus déjà compressé ni sur le master`

Valeurs de départ Music Production Wiki `[COMM]` et fiches de genre `[COMM JefroB, Fearvox]` ; les outils dessinés (LFO Tool, Kickstart, ShaperBox) sont absents de ce Mac : équivalents ci-dessous.

## Réglages par genre

| Genre | Élément | Réduction | Attaque | Release | Ratio |
|---|---|---|---|---|---|
| Tech house, deep house | basse | 2–4 dB « invisible » ; deep 2–3 | 5–20 ms | 60–100 ms | 4:1 |
| Bass house | sub, mid, top (les trois) | « tight ducking » 4–8 dB | 1–5 ms | 100–150 ms (« hard pump » 8:1 à 10:1) | 8:1 à 10:1 |
| Future rave, big room | sub et basse | 6–10 dB `[HEUR]` | 0,5–1 ms | 150–200 ms | 6:1 |
| Future rave, big room | nappes, lead | 6–10 dB audibles `[HEUR]` ; « sidechain everything » | 0,5–1 ms | 150–200 ms | 6:1 |
| French touch (pour situer) | tout | 8–12 dB | 0,1–1 ms | 150–250 ms | 6:1 |

Règles : release ≤ intervalle entre kicks (469 ms par noire, 234 par croche à 128) ; pompage audible = attaque 0,1–1 ms, « la douceur se règle au release » ; HPF de détection 80–100 Hz sur la basse, 100–140 sur un bus ; lier L/R ; seuil −18 à −10 dBFS sous la crête du déclencheur.

## Outils
| Besoin | Outil | Réglage |
|---|---|---|
| Sidechain compresseur | **Compressor natif** (déjà toléré) : Sidechain › Audio From « KICK » Pre FX, Peak, Ratio 6:1, Attack 1 ms, Release 150 ms, Knee 0 | par piste, jamais sur BUS déjà compressé |
| Sidechain externe filtré | **bx_glue** (Ext, Int Gain, HPF 80–100 Hz), **API-2500** S/C, **Pro-C 3** | bus BASSES ou HARMONIE |
| Courbe dessinée (remplace LFO Tool) | **Utility** (toléré) + automation de gain (`../../live-automation/SKILL.md`) | creux −6 à −12 dB sur chaque noire, retour en 60–70 % du temps `[HEUR]` |
| Kick fantôme | piste KICK dupliquée, clip muet ou sortie « Sends Only », routée vers les sidechains | garde le pump dans les breakdowns et pendant les fills |
| Par bande (remplace ShaperBox) | F6 bande 60–120 Hz en sidechain externe, attaque rapide | ne creuse que le grave d'un son |

## Procédure
1. `lom.py snapshot "<piste>" device` avant tout réglage.
2. Régler sur la boucle du drop, kick + élément seuls, puis avec tout le drop.
3. Vérifier au breakdown avec le kick fantôme.
4. `lom.py meters` avant et après : le niveau moyen de la basse baisse, sa crête reste.
5. Noter les valeurs (piste, outil, réduction, attaque, release) dans la mémoire du projet.

## Vérification
La basse revient à pleine valeur avant le kick suivant ; l'image stéréo ne bouge pas à chaque pump (L/R liés) ; en tech house on ne l'entend pas, en future rave on l'entend et il est en rythme ; aucun sidechain sur BUS MASTER.
