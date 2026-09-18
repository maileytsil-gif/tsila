# Gabarits d'entrées de mémoire projet

## Ligne d'étape (journal.sh)
`- <date> : **<quoi>** — <où : pistes, mesures, clips> ; <valeurs exactes : dB, Hz, MIDI, refs o:…, unité> ; relu : <ce qui a été relu et le résultat> ; reste : <suite>. Set sauvegardé <heure>.`

Exemples :
- `15 sept. 2026 : **PIANO 9–25 stabs afro** — Fm9 [Ab3 C4 Eb4 G4] · Dbmaj9 [F3 Ab3 C4 Eb4], stabs sur 2 / 3 / 4.5 ; 176 notes ; relu mes. 9, 10, 24 ; reste : PAD 17–25 à réaligner. Set sauvegardé 00:41.`
- `15 sept. 2026 : envois PIANO (mixer refs o:494615:36 A / :40 C / :41 B, unité disp) 9–25 : A −14→−8 puis −16 (origine) ; C −20→−12, throw −4 à 24|4.75, −9 (origine) ; relu res 4 sur 24–25.`

## Décision de l'utilisateur
`- <date> : l'utilisateur a choisi **<option>** parmi <liste> (refusé : …) ; annulé le <date> → <état restauré>.`

## Question restée sans réponse
`- <date> : **question posée, sans réponse** : <texte de la question et options> — à reposer en début de session.`

## En-tête REPRISE (à réécrire en fin de session)
```
**REPRISE (<date>, Set sauvegardé <heure>)** : <état en 3 lignes : structure/durée, ce qui vient d'être fait, ce qui est validé à l'oreille ou non>.
En attente : <fichiers, réponses, décisions>.
Prochaines étapes proposées : 1) … 2) … 3) …
```

## Consignes permanentes (à garder en tête de fichier, jamais en bas)
Liste courte des règles données par l'utilisateur pour ce morceau (harmonie des drops, silence mesure 96 sauf clap/rim, hooks intouchables, pas de natifs dans les chaînes…), chacune avec la date et, si elle a été levée, la date de la levée.
