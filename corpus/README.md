# Corpus de sound design — documents lus pour les skills, exploitables en local (Qwen / Ollama)

Ce dossier conserve, en Markdown, les documents consultés pour construire les skills
`studio-grade-brass-sound-design` (cuivres) et `studio-grade-funk-keys-synth-sound-design`
(synthés et claviers du funk moderne). Chaque fichier commence par un en-tête YAML
(`titre`, `source`, `recupere_le`, `mode`) qui dit d'où vient le texte et comment il a été obtenu.

## Organisation

| Dossier | Contenu |
|---|---|
| `synth-secrets/` | Les 63 articles *Synth Secrets* de Gordon Reid (Sound On Sound), copiés depuis le miroir GitHub `micjamking/synth-secrets`. Texte intégral. Parties 23 à 27 = formants, vents, cuivres ; 42 à 45 = pianos ; 55 à 59 = orgue Hammond ; 12 à 13 = FM ; 15 = vocodeur |
| `cuivres/` | Pages lues pour le skill cuivres : acoustique, synth brass vintage, cuivres électroniques modernes, écriture de section, mix |
| `funk-claviers/` | Pages lues pour le skill funk : Rhodes, Wurlitzer, Clavinet, Hammond, synth funk historique, funk moderne, jeu et mix |
| `synthes-vintage/` | Données d'usine et sources de synthèse partagées par les deux skills : DX7 ROM1A décodée (32 voix), Juno-60/106 d'usine, presets OB-Xd, Chowning/CLM/Csound, Nord Modular Book |
| `constructeur/` | Pages de manuels : les 42 chapitres du manuel Live 12 (miroir GitHub), manuel Serum 1 et changelog Serum 2, format SFZ, cartes d'articulations Reaticulate (Session Horns Pro, CineBrass, Spitfire), notes tierces sur FabFilter Pro-Q 4, soothe2, Vulf Compressor, iZotope Imager |
| `sources-a-telecharger.json`, `sources-a-telecharger-funk.json` | Listes des pages que le conteneur n'a pas pu lire (sites constructeurs, Sound On Sound, Wikipédia, blogs) : 166 URL pour les cuivres et manuels, 368 pour le funk. `scripts/fetch_sources.py` les lit toutes les deux (dédoublonnées) et range chaque page dans son dossier |
| `scripts/` | `ask_corpus.py` (question → passages BM25 → réponse Ollama), `build_context.py` (assemblage en un fichier ou en Modelfile), `build_index.py` (régénère `INDEX.md` et `index.json`), `fetch_sources.py` (à lancer sur le Mac pour compléter le corpus) |
| `INDEX.md` | Liste de tous les documents avec source, mode d'obtention et skill(s) qui les citent |

## Trois modes d'obtention, indiqués dans l'en-tête de chaque fichier

- `mode: texte integral` — fichier téléchargé tel quel (miroir GitHub, dépôt public).
- `mode: synthese` — rapport de recherche rédigé en français par Claude à partir des sources lues (fichiers `recherche-*.md`) ; utile comme point d'entrée, pas comme source primaire.
- `mode: extraction` — le conteneur de travail ne peut pas télécharger la plupart des sites
  (politique réseau), la page a donc été lue par l'outil de lecture de Claude et **retranscrite
  en Markdown**. Le texte suit la page mais peut être incomplet (tableaux, images, encadrés,
  pages très longues). Pour un chiffre décisif, revérifier sur l'URL d'origine.

## Utiliser avec Ollama (Qwen ou autre modèle local)

Prérequis : Ollama installé, un modèle tiré (`ollama pull qwen2.5:7b`, ou `qwen2.5:14b`,
`qwen3`…). Aucune bibliothèque Python à installer.

```sh
# 1. Poser une question : les passages les plus pertinents du corpus sont cherchés (BM25),
#    puis envoyés au modèle avec la consigne de citer les fichiers.
python3 corpus/scripts/ask_corpus.py "comment obtenir le 'wow' d'un synth brass : enveloppe de filtre plus lente que l'ampli ?"
python3 corpus/scripts/ask_corpus.py --model qwen2.5:14b --dossier funk-claviers --k 8 "réglages Electric pour un Rhodes Mark I"

# 2. Voir quels passages seraient retenus, sans appeler le modèle
python3 corpus/scripts/ask_corpus.py --montrer "registrations Hammond funk"

# 3. Obtenir le prompt complet pour le coller dans une autre interface (Open WebUI, LM Studio…)
python3 corpus/scripts/ask_corpus.py --contexte-seul "..." > prompt.txt

# 4. Assembler un sous-dossier en un seul fichier (à glisser dans une « connaissance » Open WebUI)
python3 corpus/scripts/build_context.py --dossier cuivres > cuivres.md

# 5. Créer un modèle Ollama qui porte un petit corpus dans son prompt système
python3 corpus/scripts/build_context.py --dossier funk-claviers --max-mots 20000 --modelfile qwen2.5:7b > Modelfile
ollama create funk-claviers -f Modelfile && ollama run funk-claviers
```

Adresse d'Ollama : `OLLAMA_HOST` (défaut `http://localhost:11434`). Modèle par défaut :
`CORPUS_MODEL` ou `--model`.

Open WebUI : créer une *Knowledge* et y glisser les fichiers d'un sous-dossier (ou le fichier
produit par `build_context.py`), puis interroger avec `#nom-de-la-connaissance`.

## Compléter le corpus depuis le Mac

Le conteneur de travail ne lit que GitHub. Les pages constructeur, Sound On Sound, Wikipédia et
blogs cités par les skills sont donc listées dans les deux fichiers `sources-a-telecharger*.json`
et se téléchargent depuis une machine sans restriction réseau :

```bash
pip3 install html2text                                  # facultatif, meilleure conversion HTML → Markdown
python3 corpus/scripts/fetch_sources.py                 # les deux listes, ne télécharge que ce qui manque
python3 corpus/scripts/fetch_sources.py --dossier funk-claviers
python3 corpus/scripts/build_index.py                   # met à jour INDEX.md et index.json
```

Les échecs (403, 404, délai) sont listés en fin d'exécution ; les PDF sont enregistrés tels quels.

## Lien avec les skills

Les fichiers `references/source-authority.md` et `references/registre-recherche.md` de chaque
skill citent, pour chaque source, l'URL d'origine **et** le chemin du fichier local dans ce
dossier. Dans une session Claude Code, lire le fichier local évite une recherche web ; dans une
session Ollama, le corpus est la seule mémoire documentaire.

## Droits

Les textes restent la propriété de leurs auteurs et éditeurs (Sound On Sound, Ableton, Xfer,
Native Instruments, Waves, FabFilter, iZotope, oeksound, blogs cités). Copies conservées pour un
usage personnel de recherche ; ne pas rediffuser et garder le dépôt privé.
