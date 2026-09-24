#!/usr/bin/env python3
"""Interroger le corpus local avec un modèle Ollama (Qwen ou autre), sans dépendance.

Usage :
  python3 corpus/scripts/ask_corpus.py "comment synthétiser une trompette dans Serum 2 ?"
  python3 corpus/scripts/ask_corpus.py --model qwen2.5:14b --dossier cuivres --k 8 "..."
  python3 corpus/scripts/ask_corpus.py --contexte-seul "..."   # imprime le prompt sans appeler Ollama
  python3 corpus/scripts/ask_corpus.py --montrer "..."         # liste les passages retenus

Fonctionnement : les fichiers .md/.txt du corpus ET les fiches des skills (références et
recettes de .claude/skills/, qui contiennent les réglages chiffrés pour Live et Serum) sont
découpés en passages, classés par BM25 sur la question (accents et casse ignorés), et les k
meilleurs passages sont donnés au modèle avec la consigne de répondre en français en citant les
fichiers sources. `--sans-skills` limite la recherche au corpus seul ; `--dossier` accepte un
sous-dossier du corpus ou le nom d'un skill. Aucune bibliothèque externe : urllib vers
http://localhost:11434 (variable OLLAMA_HOST pour changer l'adresse).

Conseil : nommer explicitement les devices (« le device Electric d'Ableton », « Serum 2 »),
sinon un petit modèle lit « Electric » comme « électrique ».
"""
import argparse, json, math, os, re, sys, unicodedata, urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPOT = os.path.dirname(RACINE)
SKILLS = os.path.join(DEPOT, ".claude", "skills")
# Skills dont les références et recettes sont indexées avec le corpus
SKILLS_INDEXES = ["studio-grade-brass-sound-design", "studio-grade-funk-keys-synth-sound-design",
                  "studio-grade-bass-sound-design", "sound-designer-serum", "vst-sound-design"]
EXCLUS = {"README.md", "INDEX.md"}

def normaliser(texte):
    texte = unicodedata.normalize("NFD", texte.lower())
    texte = "".join(c for c in texte if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-z0-9]+", texte)

def lire_fichiers(dossier, base=None):
    base = base or RACINE
    for racine, _, fichiers in os.walk(dossier):
        if os.path.basename(racine) == "scripts":
            continue
        for f in sorted(fichiers):
            if f.lower().endswith((".md", ".txt")) and not (racine == RACINE and f in EXCLUS):
                chemin = os.path.join(racine, f)
                try:
                    with open(chemin, encoding="utf-8", errors="replace") as fh:
                        yield os.path.relpath(chemin, base), fh.read()
                except OSError:
                    pass

def racines(dossier, sans_skills):
    """Liste (dossier, base d'affichage) à indexer selon --dossier et --sans-skills."""
    if dossier and os.path.isdir(os.path.join(SKILLS, dossier)):
        return [(os.path.join(SKILLS, dossier), DEPOT)]
    r = [(os.path.join(RACINE, dossier) if dossier else RACINE, RACINE)]
    if not sans_skills:
        for nom in SKILLS_INDEXES:
            d = os.path.join(SKILLS, nom)
            if os.path.isdir(d):
                r.append((d, DEPOT))
    return r

def decouper(texte, taille=350, chevauchement=60):
    mots = texte.split()
    pas = max(1, taille - chevauchement)
    for debut in range(0, max(1, len(mots)), pas):
        morceau = " ".join(mots[debut:debut + taille])
        if morceau.strip():
            yield morceau
        if debut + taille >= len(mots):
            break

def bm25(passages, requete, k1=1.5, b=0.75):
    docs = [normaliser(p[1]) for p in passages]
    N = len(docs)
    if N == 0:
        return []
    moyenne = sum(len(d) for d in docs) / N
    df = {}
    for d in docs:
        for t in set(d):
            df[t] = df.get(t, 0) + 1
    q = normaliser(requete)
    scores = []
    for i, d in enumerate(docs):
        tf = {}
        for t in d:
            tf[t] = tf.get(t, 0) + 1
        s = 0.0
        for t in q:
            if t not in tf:
                continue
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            s += idf * tf[t] * (k1 + 1) / (tf[t] + k1 * (1 - b + b * len(d) / moyenne))
        scores.append((s, i))
    scores.sort(reverse=True)
    return scores

def construire_prompt(question, retenus):
    contexte = "\n\n".join(f"### Source : {chemin}\n{texte}" for chemin, texte in retenus)
    return (
        "Tu es un assistant de sound design pour Ableton Live 12 et Serum 2. Réponds en français, "
        "uniquement à partir des extraits ci-dessous. Cite le fichier source de chaque affirmation "
        "entre crochets, par exemple [corpus/cuivres/xxx.md] ou [.claude/skills/.../recipes/xxx.md]. "
        "Distingue ce qui est documenté [DOC], ce qui est un point de départ pratique [HEUR] et ce "
        "qui reste à vérifier dans le Set [TEST]. Si les extraits ne répondent pas, dis-le.\n"
        "Vocabulaire : Electric, Tension, Analog, Operator, Wavetable, Drift, Meld, Simpler, Sampler "
        "sont des instruments natifs d'Ableton Live 12 (« réglages Electric » = réglages du device "
        "Electric, pas de l'instrument électrique) ; Auto Filter, Phaser-Flanger, Chorus-Ensemble, "
        "Auto Pan-Tremolo, Saturator, Glue Compressor sont des effets natifs de Live ; Serum 2 est le "
        "plug-in Xfer ; les noms en gras dans les tableaux des recettes sont des paramètres de device. "
        "Quand une recette donne des valeurs chiffrées, reproduis-les telles quelles.\n\n"
        f"## Extraits du corpus\n\n{contexte}\n\n## Question\n{question}\n"
    )

def appeler_ollama(modele, prompt, hote):
    corps = json.dumps({"model": modele, "messages": [{"role": "user", "content": prompt}],
                        "stream": False, "options": {"temperature": 0.2}}).encode()
    req = urllib.request.Request(f"{hote}/api/chat", data=corps,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)["message"]["content"]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("question")
    ap.add_argument("--model", default=os.environ.get("CORPUS_MODEL", "qwen2.5:7b"))
    ap.add_argument("--dossier", default="", help="sous-dossier du corpus (cuivres, funk-claviers, synth-secrets, constructeur) ou nom d'un skill (studio-grade-funk-keys-synth-sound-design…)")
    ap.add_argument("--sans-skills", action="store_true", help="ne pas indexer les fiches des skills, corpus seul")
    ap.add_argument("--k", type=int, default=6, help="nombre de passages retenus")
    ap.add_argument("--contexte-seul", action="store_true", help="imprimer le prompt sans appeler Ollama")
    ap.add_argument("--montrer", action="store_true", help="afficher les passages retenus et leur score")
    a = ap.parse_args()

    passages = [(chemin, morceau) for d, base in racines(a.dossier, a.sans_skills)
                for chemin, texte in lire_fichiers(d, base) for morceau in decouper(texte)]
    if not passages:
        sys.exit(f"Aucun fichier .md/.txt pour --dossier {a.dossier!r}")
    classement = bm25(passages, a.question)[: a.k]
    retenus = [passages[i] for s, i in classement if s > 0]
    if a.montrer:
        for (s, i) in classement:
            print(f"{s:6.2f}  {passages[i][0]}")
            print("        " + passages[i][1][:160].replace("\n", " ") + "…")
        return
    prompt = construire_prompt(a.question, retenus)
    if a.contexte_seul:
        print(prompt)
        return
    hote = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    if not hote.startswith("http"):
        hote = "http://" + hote
    try:
        print(appeler_ollama(a.model, prompt, hote))
    except Exception as e:
        sys.exit(f"Ollama injoignable sur {hote} ({e}). Lancer `ollama serve` et `ollama pull {a.model}`, "
                 "ou utiliser --contexte-seul pour coller le prompt ailleurs.")

if __name__ == "__main__":
    main()
