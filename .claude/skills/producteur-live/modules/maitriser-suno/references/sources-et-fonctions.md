# Suno : fonctions, plans et sources

Deux passes de vérification, à distinguer :
- **[AIDE 1/10]** : page de l'aide officielle lue par l'auteur du pack le 1er octobre 2026.
- **[RECOUPÉ 1/10]** : même fait retrouvé le 1er octobre 2026 par recherche web, l'aide Suno (`help.suno.com`, `suno.com`) étant inaccessible depuis la session cloud ; sources secondaires citées.

Ouvrir de nouveau la page officielle avant de prescrire une fonction payante, une durée ou un menu : les modèles et abonnements changent.

| Besoin | Fonction et source officielle | Vérification |
|---|---|---|
| Modèles | [v6, v6-wild, v6-mini](https://help.suno.com/en/articles/13924801), [sélection](https://help.suno.com/en/articles/13924993) : v6 et v6-wild en Pro et Premier, v6-mini sur tous les plans, Free compris ; jusqu'à 8 min par génération. Sortie le 9 sept. 2026 ([notes de version](https://suno.com/release-notes/introducing-v6)). | [AIDE 1/10] [RECOUPÉ 1/10] ([DataNorth](https://datanorth.ai/news/suno-launches-v6-v6-wild-and-v6-mini)) |
| Guidage | [Creative Sliders](https://help.suno.com/en/articles/6141377) en mode Custom : Weirdness (de Safe à Chaos, 50 % = normal) ; Style Influence (de Loose à Strong) ; Audio Influence, seulement avec un upload. Aucune valeur n'est une propriété musicale garantie. | [AIDE 1/10] [RECOUPÉ 1/10] ([Jack Righteous](https://jackrighteous.com/de-gb/blogs/guides-using-suno-ai-music-creation/suno-remix-sliders-guide-v4-5)) |
| Audio d'origine | [Audio Uploads](https://help.suno.com/en/articles/6141569) : jusqu'à 60 s en Free (Basic), 8 min en Pro et Premier. Une [autre page](https://help.suno.com/en/articles/2477633) donnait des limites différentes : vérifier sur le compte avant de prescrire une durée. | [AIDE 1/10] [RECOUPÉ 1/10] (page officielle en résultat de recherche) |
| Retouche | [Song Editor](https://help.suno.com/en/articles/6141505) : remplacer, modifier les paroles, étendre, couper, déplacer des sections, fondus ; [Replace Section](https://help.suno.com/en/articles/3271873), [Extend](https://help.suno.com/en/articles/2409601). | [AIDE 1/10] |
| Variantes | [Remaster](https://help.suno.com/en/articles/8105281) : Subtle (très proche, détails de production), Normal (durée et style gardés, légères variations), High (écarts nets, voix et éléments peuvent changer) ; [Cover](https://help.suno.com/en/articles/2872257) : change le style en gardant la mélodie, réinterprète des détails ; [Reuse Prompt](https://help.suno.com/en/articles/2417409). | [AIDE 1/10] [RECOUPÉ 1/10] ([Suno, Covers](https://suno.com/blog/covers)) |
| Studio | [Studio 2.0](https://help.suno.com/en/articles/13670529), [annonce](https://suno.com/blog/studio-2) du 13 août 2026 : **Premier seulement** ; MIDI enregistré, importé et édité ; synthé wavetable à deux oscillateurs ; Chat (bêta) qui construit aussi des plug-ins d'effet ; séparation de stems avancée ; automation ; pas de VST/AU tiers. | [AIDE 1/10] [RECOUPÉ 1/10] ([Music Business Worldwide](https://musicbusinessworldwide.com/suno-launches-studio-2-0-with-midi-support), [Dubspot](https://blog.dubspot.com/suno-studio-2-0)) |
| Export | [Exporting from Studio](https://help.suno.com/en/articles/13925249) : Full Song, Selected Time Range, Multitrack, WAV par clip ; multipistes et stems en 32 bits / 48 kHz sans plafond en Premier ; MIDI tiré d'un stem par Get MIDI, payé en crédits (10 selon une source secondaire, à vérifier) ; [stems](https://help.suno.com/en/articles/13925185), [tempo drift](https://help.suno.com/en/articles/8363457). | [AIDE 1/10] [RECOUPÉ 1/10] ([Music Business Worldwide](https://musicbusinessworldwide.com/suno-launches-studio-2-0-with-midi-support)) |
| Raccourcis Studio | [Shortcuts](https://help.suno.com/en/articles/13680385) : `Shift+F` fondu, `Shift+R` enregistrer, `Shift+C` métronome, `Shift+T` nouvelle piste (détail dans `tutoriels-video.md`). | [AIDE 1/10] [RECOUPÉ 1/10] |
| Droits | [Abonnement payant](https://help.suno.com/en/articles/9601665), [droit d'auteur](https://help.suno.com/en/articles/2746945), [pas de rétroactivité automatique](https://help.suno.com/en/articles/2425729). Vérifier aussi les conditions du distributeur et la provenance de chaque upload. | [AIDE 1/10] |

## Conseils de créateurs tiers
Ils ne sont pas des spécifications Suno. Exemple retenu comme heuristique `[HEUR]` : quatre à sept descripteurs dans Style, sous quatre Suno comble avec des choix par défaut, au-delà de sept les consignes se concurrencent ([Blake Crosley](https://blakecrosley.com/fr/blog/suno-style-field-style-influence)). À comparer sur plusieurs générations avant d'en faire une règle.

## Vidéos explicatives
- Page officielle [Suno Studio](https://www.suno.com/studio) : liste les sept tutoriels de Studio 2.0 (Introducing Studio 2.0 21:33, Getting Started 38:25, MIDI x Studio 8:09, Editing & Mixing 9:22, Instruments & Audio FX 11:48, Recording with Studio 6:37, Creating Plugins 5:54). Notes horodatées et liens vidéo par vidéo dans `tutoriels-video.md`.
- Le lien de playlist YouTube du pack d'origine (`list=PLcGl48v5p95s`) est **tronqué** : un identifiant de playlist compte une trentaine de caractères. Retrouver la playlist sur la chaîne officielle Suno et noter ici l'adresse complète.
- [Annonce officielle Studio 2.0](https://suno.com/blog/studio-2) : descriptions, captures et changements d'interface ; comparer au compte actuel.

## Intégrer une nouvelle vidéo
Noter URL, auteur, date, version de Suno, objectif, prompt exact, réglages visibles, démonstration audio, résultat reproductible et limites. Écarter les tutoriels anciens pour les libellés d'interface ; marquer toute technique de balise ou de curseur comme hypothèse tant qu'elle n'a pas été comparée sur plusieurs générations. Une vidéo ne prouve pas qu'un résultat se reproduit.
