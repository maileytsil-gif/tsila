#!/usr/bin/env python3
"""Télécharger sur le Mac les pages que le conteneur cloud n'a pas pu lire, et les ranger dans le corpus.

Le conteneur Claude Code cloud ne peut lire que GitHub ; les manuels (Ableton, Xfer, NI, Waves…),
Sound On Sound, Wikipédia, les blogs, sont listés dans `sources-a-telecharger.json` avec leur
dossier cible. Sur le Mac (sans restriction réseau) :

  pip3 install html2text        # facultatif : conversion HTML → Markdown de meilleure qualité
  python3 corpus/scripts/fetch_sources.py            # télécharge tout ce qui manque
  python3 corpus/scripts/fetch_sources.py --force    # retélécharge aussi ce qui existe
  python3 corpus/scripts/build_index.py              # met à jour INDEX.md

Chaque page devient `<dossier>/<slug>.md` avec un en-tête YAML (titre, source, recupere_le,
mode: texte integral). Les échecs (403, 404, délai) sont listés en fin d'exécution ; les PDF sont
enregistrés tels quels à côté (le texte n'en est pas extrait ici).
"""
import argparse, html, json, os, re, sys, time, urllib.request, urllib.error

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(RACINE, "sources-a-telecharger.json")
UA = "Mozilla/5.0 (Macintosh) corpus-sound-design/1.0 (usage personnel)"

def slug(s):
    s = re.sub(r"https?://(www\.)?", "", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:90]

def html_vers_md(page):
    try:
        import html2text
        h = html2text.HTML2Text(); h.ignore_images = True; h.body_width = 0
        return h.handle(page)
    except ImportError:
        page = re.sub(r"(?is)<(script|style|nav|footer|header|noscript).*?</\1>", " ", page)
        page = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>|</li>|</tr>", "\n", page)
        page = re.sub(r"(?i)<h(\d)[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", page)
        page = re.sub(r"<[^>]+>", " ", page)
        page = html.unescape(page)
        return re.sub(r"\n\s*\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", page)).strip()

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dossier", default="", help="ne traiter qu'un dossier cible (cuivres, funk-claviers, constructeur)")
    a = ap.parse_args()
    with open(LISTE, encoding="utf-8") as f:
        sources = json.load(f)
    echecs, faits = [], 0
    for s in sources:
        if a.dossier and s["dossier"] != a.dossier:
            continue
        cible_dir = os.path.join(RACINE, s["dossier"]); os.makedirs(cible_dir, exist_ok=True)
        base = s.get("slug") or slug(s["url"])
        est_pdf = s["url"].lower().endswith(".pdf")
        cible = os.path.join(cible_dir, base + (".pdf" if est_pdf else ".md"))
        if os.path.exists(cible) and not a.force:
            continue
        try:
            req = urllib.request.Request(s["url"], headers={"User-Agent": UA, "Accept-Language": "fr,en"})
            with urllib.request.urlopen(req, timeout=60) as r:
                brut = r.read()
            if est_pdf:
                with open(cible, "wb") as f: f.write(brut)
            else:
                texte = html_vers_md(brut.decode("utf-8", errors="replace"))
                ent = (f'---\ntitre: "{s.get("titre", base)}"\nsource: {s["url"]}\nrecupere_le: {time.strftime("%Y-%m-%d")}\n'
                       f'mode: texte integral\nlangue: {s.get("langue", "en")}\naxe: {s.get("axe", "")}\nskills: {s.get("skills", "")}\n'
                       'usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités\n---\n\n')
                with open(cible, "w", encoding="utf-8") as f: f.write(ent + texte)
            faits += 1; print("ok ", s["url"])
            time.sleep(1.0)
        except Exception as e:
            echecs.append((s["url"], str(e))); print("KO ", s["url"], e)
    print(f"\n{faits} fichiers écrits, {len(echecs)} échecs")
    for u, e in echecs: print(" -", u, "→", e)

if __name__ == "__main__":
    main()
