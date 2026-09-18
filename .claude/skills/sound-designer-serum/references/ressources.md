# Ressources pour apprendre le sound design électronique

Relevé du 18 septembre 2026. Les mentions « non vérifiée » signalent les pages qui n'ont pas pu être lues par l'outil de recherche.

---

## Gratuit — priorité absolue

### Synth Secrets, Gordon Reid, Sound on Sound

**63 articles, mai 1999 à juillet 2004, intégralement gratuits.** C'est la référence de fond sur la synthèse, avec la physique et les formules plutôt que des recettes.

https://www.soundonsound.com/series/synth-secrets-sound-sound

**Si on ne lit que quatre articles** :
- *Modulation* (partie 11) — https://www.soundonsound.com/techniques/modulation
- *Envelopes, Gates & Triggers* (8) — https://www.soundonsound.com/techniques/envelopes-gates-triggers
- *More About Envelopes* (9) — https://www.soundonsound.com/techniques/more-about-envelopes
- *Of Responses & Resonance* (6) — https://www.soundonsound.com/techniques/responses-resonance

Autres parties utiles : 1 *What's In A Sound?*, 12–14 sur l'AM et la FM, 25 *Formant Synthesis*, plus les articles hors série sur le granulaire, les percussions et les risers.

**Miroir GitHub** en Markdown, lisible hors ligne et greppable : https://github.com/micjamking/synth-secrets — réserve : la numérotation des parties diffère de l'index officiel.

### Documentation constructeur

| Ressource | URL |
|---|---|
| **Manuel officiel Serum 2**, 354 pages | https://xferrecords.com/manual/serum-2/docs |
| Version web du même manuel | https://xferrecords.com/web-manual/serum-2/welcome |
| Manuel de référence des instruments Ableton Live 12 | https://www.ableton.com/en/manual/live-instrument-reference/ |
| Granulator III | https://www.ableton.com/en/packs/granulator-iii/ |
| **FabFilter Learn — Synthesis and Sound Design** : six articles illustrés + 2 vidéos | https://www.fabfilter.com/learn/synthesis-and-sound-design |
| Manuel FabFilter Saturn 2, lisible sans posséder le plug-in | https://www.fabfilter.com/help/saturn |

Le manuel Serum 2 existe bel et bien. Deux recherches indépendantes avaient conclu qu'il était introuvable et s'étaient rabattues sur le manuel de la version 1 : **vérifier dans le manuel officiel avant de croire un blog sur Serum 2.**

### Cours interactifs gratuits d'Ableton

- **Learning Synths** — cours dans le navigateur avec synthé jouable intégré : https://learningsynths.ableton.com/ *(page non vérifiée, l'outil de lecture n'a pas rendu son contenu)*
- **Learning Music** — mêmes fondamentaux, côté musical : https://learningmusic.ableton.com/

### Sites et blogs de qualité

| Ressource | URL | Ce qu'on y trouve |
|---|---|---|
| **Reverb Machine** | https://reverbmachine.com/articles/ | Reconstructions détaillées de sons célèbres (Daft Punk *Discovery*, Beach House, MGMT, Kaytranada, Rival Consoles, Kavinsky), avec **presets téléchargeables gratuits** |
| **Valhalla DSP** | https://valhalladsp.com/ | Explications DSP écrites par le concepteur : feedback, diffusion, pitch-shift, shimmer. Rare qualité technique |
| **Attack Magazine — Technique** | https://www.attackmagazine.com/technique/tutorials/ | Orienté house et techno. La série *Synth Secrets* maison donne des **patchs complets chiffrés** |
| **Production Music Live** | https://www.productionmusiclive.com/blogs/news | **350+ tutoriels gratuits.** Tuteurs publiant sur Diynamic, Afterlife, Innervisions, Anjunadeep, Drumcode, Terminal M |
| PML — mini-cours Serum gratuit | https://www.productionmusiclive.com/pages/join-mini-course | Flux de signal, oscillateurs, filtres |
| **Sound on Sound — Sound Advice** | https://www.soundonsound.com/sound-advice/ | Réponses courtes et précises (*How Phasers Work*, différence phasing/flanging) |
| Learning Modular — glossaire | https://learningmodular.com/glossary/ | Définitions courtes et exactes |
| Perfect Circuit — Signal | https://www.perfectcircuit.com/signal/ | Série *Learning Synthesis*, bon article sur les waveshapers |
| Ask.Audio | https://ask.audio/tutorials/Synth-Sound-Design | Articles gratuits ; les cours vidéo sont payants |
| iZotope | https://www.izotope.com/community/blog/ | Mixage et compréhension des effets |

---

## Payant

| Ressource | URL | Description |
|---|---|---|
| **Syntorial** | https://www.syntorial.com/ | Cours interactif **à l'oreille** : 199 leçons, entraînement gamifié sur formes d'onde, filtres, enveloppes, LFO. **Démo gratuite sans limite de temps : 22 leçons sur 199.** Le meilleur rapport effort/résultat pour apprendre à programmer sans regarder les boutons |
| PML — Serum 2 and Sound Design | https://www.productionmusiclive.com/products/course-serum-2 | Parcours complet Serum 2 |
| PML — Advanced Sound Design with Serum 2 | https://www.productionmusiclive.com/products/course-advanced-sound-design-with-serum-2 | Suite avancée |
| PML — Modern Melodic Techno | https://www.productionmusiclive.com/products/course-serum-sound-design-modern-melodic-techno | Création de presets originaux, orienté melodic techno |
| Ask.Audio Academy | https://academy.ask.audio/course/3523/sound-design-synthesis-and-sampling/ | Soustractive, additive, wavetable, sampling, granulaire |

---

## Livres

**Refining Sound**, Brian K. Shepard, Oxford University Press — https://books.apple.com/us/book/refining-sound/id807510560

Suit les étapes de la synthèse dans l'ordre chronologique, des matières premières jusqu'au polissage par les effets. **Site compagnon avec plus de 40 démonstrations interactives.** C'est le livre le plus proche d'un travail dans Serum.

**Designing Sound**, Andy Farnell, MIT Press — https://mitpress.mit.edu/9780262014410/designing-sound/

Créer des effets sonores **à partir de rien** en Pure Data : physique du phénomène, puis modèle, puis implémentation. Orienté audio procédural et sound design pour l'image plus que musique électronique. À prendre pour la méthode de pensée, pas pour des recettes house.

---

## Sources académiques repérées

**Adam Szabo, *How to Emulate the Super Saw***, KTH Royal Institute of Technology, 2010 — https://www.adamszabo.com/internet/adam_szabo_how_to_emulate_the_super_saw.pdf

Mesures FFT sur JP-8000 et JP-8080 : structure exacte du supersaw, courbe de détune non linéaire, comportement du contrôle Mix, phase libre. La meilleure source du dossier sur les leads.

**Emmanuel Deruty, *Harmonic and Transposition Constraints Arising from the Use of the Roland TR-808 Bass Drum***, ISMIR 2024, p. 78–85 — https://arxiv.org/abs/2502.07524

Pourquoi la 808 s'accorde naturellement en Sol, ce que coûte une transposition vers le bas, et pourquoi la stabilité de sonie limite la variété harmonique. Voir `percussions.md`.

---

## Chaînes vidéo, non vérifiées

Les résultats de recherche citent **Au5**, **SeamlessR** (environ 1000 tutoriels gratuits, très orienté FL Studio et bass music), **In The Mix** et **ADSR**. Aucune de ces chaînes n'a été visitée, elles sont donc citées sans garantie.

---

## Ce qui n'a pas été trouvé

- **Aucune source de référence sur les courbes exponentielles contre linéaires dans les enveloppes.** Le sujet n'est traité frontalement nulle part.
- L'article Sound on Sound *Practical Percussion Synthesis* renvoie un **HTTP 410**, il a été retiré.
- Deux pages ont refusé la lecture avec un **HTTP 403** : Point Blank sur les risers, Perfect Circuit sur l'histoire du supersaw.
