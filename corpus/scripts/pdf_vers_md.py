#!/usr/bin/env python3
"""Extraire le texte des PDF du corpus en fichiers Markdown voisins, lisibles par ask_corpus.py et Ollama.

  pip3 install pymupdf
  python3 corpus/scripts/pdf_vers_md.py             # tous les PDF sans .md compagnon
  python3 corpus/scripts/pdf_vers_md.py --force     # refait tout
  python3 corpus/scripts/pdf_vers_md.py --decouper 40   # un fichier par chapitre (signets) si le PDF dépasse 40 pages

Chaque `<nom>.pdf` donne `<nom>-texte.md` (ou `<nom>-NN-<chapitre>.md` en mode découpé) avec un en-tête
YAML (titre tiré du PDF ou du nom, source = chemin du PDF, mode: texte integral (PDF → texte)).
"""
import argparse, glob, os, re, sys, time
try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf manquant : pip3 install pymupdf")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60] or "chapitre"

def entete(titre, source, note=""):
    return (f'---\ntitre: "{titre}"\nsource: {source}\nrecupere_le: {time.strftime("%Y-%m-%d")}\n'
            f'mode: texte integral (PDF → texte)\nlangue: en\naxe: documentation constructeur\nskills: \n'
            f'usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités\n---\n\n{note}')

def texte_pages(doc, debut, fin):
    parts = []
    for i in range(debut, fin):
        t = doc[i].get_text("text")
        t = re.sub(r"[ \t]+\n", "\n", t)
        parts.append(f"\n\n<!-- page {i + 1} -->\n\n{t.strip()}")
    return "".join(parts)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--decouper", type=int, default=60, help="découper par signets au-delà de ce nombre de pages (0 = jamais)")
    ap.add_argument("fichiers", nargs="*", help="PDF précis ; défaut : tous ceux du corpus")
    a = ap.parse_args()
    pdfs = a.fichiers or sorted(glob.glob(os.path.join(RACINE, "*", "*.pdf")))
    for p in pdfs:
        base = p[:-4]
        deja = glob.glob(base + "-texte.md") + glob.glob(base + "-[0-9][0-9]-*.md")
        if deja and not a.force:
            continue
        try:
            doc = pymupdf.open(p)
            n = doc.page_count
            if n == 0:
                raise ValueError("0 page")
        except Exception as e:
            print("KO ", os.path.relpath(p, RACINE), e); continue
        titre = (doc.metadata or {}).get("title") or os.path.basename(base).replace("-", " ")
        rel = os.path.relpath(p, RACINE)
        toc = [(lvl, t, pg) for lvl, t, pg in doc.get_toc() if lvl == 1 and 1 <= pg <= n]
        if a.decouper and n > a.decouper and len(toc) >= 3:
            for k, (lvl, t, pg) in enumerate(toc):
                fin = toc[k + 1][2] - 1 if k + 1 < len(toc) else n
                if fin < pg: fin = pg
                cible = f"{base}-{k + 1:02d}-{slug(t)}.md"
                with open(cible, "w", encoding="utf-8") as f:
                    f.write(entete(f"{titre} — {t} (p. {pg}-{fin})", rel, f"# {t}\n") + texte_pages(doc, pg - 1, fin))
            print(f"ok  {rel} → {len(toc)} chapitres ({n} pages)")
        else:
            with open(base + "-texte.md", "w", encoding="utf-8") as f:
                f.write(entete(f"{titre} (texte du PDF, {n} pages)", rel) + texte_pages(doc, 0, n))
            print(f"ok  {rel} → 1 fichier ({n} pages)")

if __name__ == "__main__":
    main()
