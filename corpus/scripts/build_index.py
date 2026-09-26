#!/usr/bin/env python3
"""Régénérer corpus/INDEX.md et corpus/index.json à partir des en-têtes YAML des fichiers.

Usage : python3 corpus/scripts/build_index.py
Chaque fichier .md du corpus commence par un bloc `---` … `---` avec au moins `titre`, `source`
(ou `miroir`), `recupere_le`, `mode` (texte integral | extraction) et, si connu, `skills`
(liste des skills qui le citent) et `axe` (thème). L'index reprend ces champs.
"""
import json, os, re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def entete(chemin):
    with open(chemin, encoding="utf-8", errors="replace") as fh:
        texte = fh.read(4000)
    m = re.match(r"---\n(.*?)\n---", texte, re.S)
    champs = {}
    if m:
        for ligne in m.group(1).splitlines():
            if ":" in ligne:
                k, v = ligne.split(":", 1)
                champs[k.strip()] = v.strip().strip('"')
    return champs

def main():
    lignes, entrees = [], []
    for dossier in sorted(os.listdir(RACINE)):
        chemin_dossier = os.path.join(RACINE, dossier)
        if not os.path.isdir(chemin_dossier) or dossier == "scripts":
            continue
        fichiers = sorted(f for f in os.listdir(chemin_dossier) if f.endswith(".md"))
        if not fichiers:
            continue
        lignes.append(f"\n## `{dossier}/` ({len(fichiers)} fichiers)\n")
        lignes.append("| Fichier | Titre | Source | Mode | Skills |")
        lignes.append("|---|---|---|---|---|")
        for f in fichiers:
            c = entete(os.path.join(chemin_dossier, f))
            source = c.get("source") or c.get("miroir") or ""
            titre = c.get("titre", f)
            mode = c.get("mode", "?")
            skills = c.get("skills", "")
            mots = len(open(os.path.join(chemin_dossier, f), encoding="utf-8", errors="replace").read().split())
            lignes.append(f"| `{f}` | {titre} | {source} | {mode} | {skills} |")
            entrees.append({"fichier": f"{dossier}/{f}", "titre": titre, "source": source,
                            "mode": mode, "skills": skills, "axe": c.get("axe", ""),
                            "recupere_le": c.get("recupere_le", ""), "mots": mots})
    total = sum(e["mots"] for e in entrees)
    tete = (f"# Index du corpus — {len(entrees)} documents, {total} mots\n\n"
            "Généré par `scripts/build_index.py` à partir des en-têtes des fichiers. "
            "`texte integral` = fichier téléchargé tel quel ; `extraction` = page retranscrite par l'outil de lecture, "
            "possiblement incomplète (voir README.md).\n")
    with open(os.path.join(RACINE, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write(tete + "\n".join(lignes) + "\n")
    with open(os.path.join(RACINE, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(entrees, fh, ensure_ascii=False, indent=1)
    print(f"{len(entrees)} documents, {total} mots")

if __name__ == "__main__":
    main()
