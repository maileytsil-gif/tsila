#!/usr/bin/env python3
"""Extraire le texte des PDF du corpus en fichiers Markdown voisins, lisibles par ask_corpus.py et Ollama.

  pip3 install pymupdf
  python3 corpus/scripts/pdf_vers_md.py             # tous les PDF sans .md compagnon
  python3 corpus/scripts/pdf_vers_md.py --force     # refait tout
  python3 corpus/scripts/pdf_vers_md.py --decouper 40   # un fichier par chapitre (signets, sinon sommaire imprimé) au-delà de 40 pages

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

def entete(titre, source, note="", skills=""):
    return (f'---\ntitre: "{titre}"\nsource: {source}\nrecupere_le: {time.strftime("%Y-%m-%d")}\n'
            f'mode: texte integral (PDF → texte)\nlangue: en\naxe: documentation constructeur\nskills: {skills}\n'
            f'usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités\n---\n\n{note}')

def texte_pages(doc, debut, fin):
    parts = []
    for i in range(debut, fin):
        t = doc[i].get_text("text")
        t = re.sub(r"[ \t]+\n", "\n", t)
        parts.append(f"\n\n<!-- page {i + 1} -->\n\n{t.strip()}")
    return "".join(parts)

def sommaire_imprime(doc, n):
    """Chapitres lus dans le sommaire imprimé quand le PDF n'a pas de signets : une ligne de titre
    sans points de conduite suivie d'une ligne qui n'est qu'un numéro de page (« Welcome » / « 13 »)."""
    chap, fin_sommaire = [], 0
    for i in range(min(n, 20)):
        lignes = [l.strip() for l in doc[i].get_text("text").splitlines() if l.strip()]
        trouves = []
        for a, b in zip(lignes, lignes[1:]):
            if (b.isdigit() and not a.isdigit() and not re.search(r"(\. ?){3,}", a)
                    and len(a) > 3 and not a.lower().startswith(("serum", "table of contents"))):
                trouves.append((a, int(b)))
        points = sum(1 for l in lignes if re.search(r"(\. ?){3,}\s*\d+$", l))
        if trouves and points >= 3:   # page de sommaire : des lignes à points de conduite
            chap += trouves; fin_sommaire = i + 1
    chap = [c for k, c in enumerate(chap) if c[1] <= n and (k == 0 or c[1] > chap[k - 1][1])]
    if len(chap) < 3:
        return []
    # décalage page imprimée → page du PDF : première page après le sommaire qui porte le titre du chapitre
    decalage = 0
    t0, p0 = chap[0]
    for i in range(fin_sommaire, min(n, p0 + 20)):
        if t0.lower() in doc[i].get_text("text").lower():
            decalage = (i + 1) - p0; break
    return [(1, t, p + decalage) for t, p in chap if 1 <= p + decalage <= n]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--decouper", type=int, default=60, help="découper par signets au-delà de ce nombre de pages (0 = jamais)")
    ap.add_argument("--skills", default="", help="skills qui citent ce document (en-tête YAML), ex. « sound-designer-serum, vst-sound-design »")
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
        if a.decouper and n > a.decouper and len(toc) < 3:
            toc = sommaire_imprime(doc, n)
        if a.decouper and n > a.decouper and len(toc) >= 3:
            if toc[0][2] > 1:   # couverture, version, sommaire
                with open(f"{base}-00-sommaire.md", "w", encoding="utf-8") as f:
                    f.write(entete(f"{titre} — couverture et sommaire (p. 1-{toc[0][2] - 1})", rel, "", a.skills)
                            + texte_pages(doc, 0, toc[0][2] - 1))
            for k, (lvl, t, pg) in enumerate(toc):
                fin = toc[k + 1][2] - 1 if k + 1 < len(toc) else n
                if fin < pg: fin = pg
                cible = f"{base}-{k + 1:02d}-{slug(t)}.md"
                with open(cible, "w", encoding="utf-8") as f:
                    f.write(entete(f"{titre} — {t} (p. {pg}-{fin})", rel, f"# {t}\n", a.skills) + texte_pages(doc, pg - 1, fin))
            print(f"ok  {rel} → {len(toc)} chapitres ({n} pages)")
        else:
            with open(base + "-texte.md", "w", encoding="utf-8") as f:
                f.write(entete(f"{titre} (texte du PDF, {n} pages)", rel, "", a.skills) + texte_pages(doc, 0, n))
            print(f"ok  {rel} → 1 fichier ({n} pages)")

if __name__ == "__main__":
    main()
