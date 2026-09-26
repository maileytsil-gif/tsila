#!/usr/bin/env python3
"""Assembler une partie du corpus en un seul fichier (à coller dans un chat, ou en Modelfile Ollama).

Usage :
  python3 corpus/scripts/build_context.py --dossier cuivres > cuivres.md
  python3 corpus/scripts/build_context.py --dossier funk-claviers --max-mots 30000 > funk.md
  python3 corpus/scripts/build_context.py --dossier cuivres --modelfile qwen2.5:7b > Modelfile
      puis : ollama create cuivres -f Modelfile && ollama run cuivres

Le mode --modelfile met le corpus dans le SYSTEM du modèle : pratique pour les petits corpus,
mais la fenêtre de contexte du modèle limite la taille (num_ctx est fixé à 32768 ci-dessous).
Pour un corpus plus grand, préférer ask_corpus.py (recherche puis réponse).
"""
import argparse, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fichiers(dossier):
    for racine, _, fs in os.walk(dossier):
        if os.path.basename(racine) == "scripts":
            continue
        for f in sorted(fs):
            if f.lower().endswith((".md", ".txt")):
                yield os.path.join(racine, f)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dossier", default="", help="sous-dossier du corpus ; vide = tout")
    ap.add_argument("--max-mots", type=int, default=0, help="arrêter après ce nombre de mots (0 = illimité)")
    ap.add_argument("--modelfile", metavar="MODELE", help="produire un Modelfile Ollama basé sur ce modèle")
    a = ap.parse_args()
    dossier = os.path.join(RACINE, a.dossier) if a.dossier else RACINE
    morceaux, total = [], 0
    for chemin in fichiers(dossier):
        with open(chemin, encoding="utf-8", errors="replace") as fh:
            texte = fh.read()
        n = len(texte.split())
        if a.max_mots and total + n > a.max_mots:
            sys.stderr.write(f"limite atteinte avant {os.path.relpath(chemin, RACINE)}\n")
            break
        total += n
        morceaux.append(f"\n\n<!-- ===== {os.path.relpath(chemin, RACINE)} ===== -->\n\n{texte}")
    corps = "".join(morceaux)
    if a.modelfile:
        systeme = ("Tu es un assistant de sound design pour Ableton Live 12 et Serum 2. Réponds en français "
                   "à partir de la documentation ci-dessous, en citant le fichier source entre crochets et en "
                   "distinguant [DOC], [HEUR] et [TEST].\n" + corps)
        systeme = systeme.replace('"""', "'''")
        print(f"FROM {a.modelfile}\nPARAMETER num_ctx 32768\nPARAMETER temperature 0.2\nSYSTEM \"\"\"{systeme}\"\"\"")
    else:
        print(corps)
    sys.stderr.write(f"{len(morceaux)} fichiers, {total} mots\n")

if __name__ == "__main__":
    main()
