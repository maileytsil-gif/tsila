#!/usr/bin/env python3
"""Télécharger sur le Mac les pages que le conteneur cloud n'a pas pu lire, et les ranger dans le corpus.

Le conteneur Claude Code cloud ne peut lire que GitHub ; les manuels (Ableton, Xfer, NI, Waves…),
Sound On Sound, Wikipédia, les blogs, sont listés dans `sources-a-telecharger.json` (cuivres,
constructeur) et `sources-a-telecharger-funk.json` (funk, constructeur) avec leur dossier cible. Sur le Mac (sans restriction réseau) :

  pip3 install html2text        # facultatif : conversion HTML → Markdown de meilleure qualité
  python3 corpus/scripts/fetch_sources.py            # télécharge tout ce qui manque
  python3 corpus/scripts/fetch_sources.py --force    # retélécharge aussi ce qui existe
  python3 corpus/scripts/fetch_sources.py --liste corpus/sources-a-telecharger-funk.json   # une seule liste
  python3 corpus/scripts/build_index.py              # met à jour INDEX.md

Chaque page devient `<dossier>/<slug>.md` avec un en-tête YAML (titre, source, recupere_le,
mode: texte integral). Si Python n'a pas ses certificats SSL (erreur CERTIFICATE_VERIFY_FAILED sur
macOS), le script bascule de lui-même sur `curl` ; pour corriger Python durablement :
`open "/Applications/Python 3.13/Install Certificates.command"` (adapter le numéro de version). Les échecs (403, 404, délai) sont listés en fin d'exécution ; les PDF sont
enregistrés tels quels à côté (le texte n'en est pas extrait ici).
"""
import argparse, html, json, os, re, subprocess, sys, time, urllib.request, urllib.error

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTES = [os.path.join(RACINE, "sources-a-telecharger.json"),
          os.path.join(RACINE, "sources-a-telecharger-funk.json")]
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) "
      "Version/17.0 Safari/605.1.15 corpus-sound-design/1.1")

def telecharger(url):
    """Octets de la page : urllib d'abord ; si Python n'a pas ses certificats (CERTIFICATE_VERIFY_FAILED,
    fréquent sur macOS) ou refuse, réessai avec curl, qui utilise les certificats du système."""
    e1 = None
    if not os.environ.get("CORPUS_FORCE_CURL"):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr,en",
                                                       "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            e1 = e
    try:
        out = subprocess.run(["curl", "-fsSL", "--max-time", "90", "-A", UA, "-H", "Accept-Language: fr,en", url],
                             capture_output=True, check=True)
        return out.stdout
    except FileNotFoundError:
        raise RuntimeError(f"{e1} ; curl absent")
    except subprocess.CalledProcessError as e2:
        detail = e2.stderr.decode(errors="replace").strip().splitlines()
        raise RuntimeError(f"urllib : {e1} ; curl : {detail[-1] if detail else e2}")

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
    ap.add_argument("--liste", action="append", default=[], help="fichier JSON à lire (répétable) ; défaut : les deux listes du corpus")
    a = ap.parse_args()
    sources, vus = [], set()
    for chemin in (a.liste or LISTES):
        if not os.path.exists(chemin):
            print("liste absente :", chemin, file=sys.stderr); continue
        with open(chemin, encoding="utf-8") as f:
            for s in json.load(f):
                cle = re.sub(r"https?://(www\.)?", "", s["url"]).rstrip("/")
                if cle in vus:
                    continue
                vus.add(cle); sources.append(s)
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
            brut = telecharger(s["url"])
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
