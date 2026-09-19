# Nappe — sous-types professionnels v5

Une nappe est traitée ici comme **couche atmosphérique** plutôt que clavier polyphonique principal.

## 1. Nappe airy / high-air
**Rôle** : remplir le haut du spectre sans ajouter beaucoup de corps.

**Serum 2** : Wavetable douce + NOISE/Granular très dosé ; high-pass de la couche diffuse.  
**Ableton** : Wavetable ou Granulator III en couche ; Hybrid Reverb/Echo pour profondeur.  
**HEUR** : modulation lente, attack 0.5–4 s, release 1–6 s ; réduire les informations sous ~150–300 Hz selon contexte.  
**Macros** : `AIR`, `SHIMMER`, `WIDTH`, `SPACE`, `MOTION`.  
**Test** : si la nappe disparaît à faible volume, réduire reverb et renforcer légèrement le contenu sec plutôt que monter simplement le niveau.

## 2. Nappe cinematic
**Rôle** : profondeur, mouvement lent, sensation de taille.

**Serum 2 [DOC]** : Wavetable CORE + Granular TEXTURE ; filtres/bus séparés.  
**Ableton [DOC]** : Granulator III convient aux pads/textures et Cloud aux drones/textures ; Rack avec couche tonale + texture.  
**HEUR** : trois temps : entrée douce, plateau évolutif, queue contrôlée. Hybrid Reverb en send ou branche tail.  
**Macros** : `SIZE`, `DISTANCE`, `TEXTURE`, `DARK↔BRIGHT`, `MOTION`.  
**Test** : 16 mesures sous harmonie ; la texture doit évoluer sans distraire du hook.

## 3. Nappe granular diffuse
**Rôle** : texture non périodique, aérienne ou cassée.

**Serum 2 [DOC]** : Granular réarrange/étire des fragments de sample.  
**Ableton [DOC]** : Granulator III Cloud cible drones et textures expérimentales.  
**HEUR** : choisir un sample source riche mais lisible ; réduire densité si le résultat devient bruit blanc uniforme. Moduler position/taille plus lentement que les grains eux-mêmes.  
**Macros** : `GRAIN`, `POSITION`, `DENSITY`, `BLUR`, `SPACE`.  
**Test** : écouter sans reverb ; vérifier que la granularité elle-même crée l'intérêt.

## 4. Nappe spectrale / frozen tone
**Rôle** : matière éthérée, resynthétisée, presque immobile mais complexe.

**Serum 2 [DOC]** : Spectral permet une transformation par analyse/resynthèse du spectre.  
**Ableton** : Granulator III + Corpus/Resonators/Hybrid Reverb comme alternative de texture, sans prétendre reproduire la synthèse spectrale Serum.  
**HEUR** : conserver une référence harmonique faible sous la couche spectrale si l'accord doit rester évident.  
**Macros** : `SPECTRAL`, `TONE`, `MOTION`, `WIDTH`, `SPACE`.  
**Test** : changements d'accord ; si la couche spectrale brouille la tonalité, diminuer son niveau ou la rendre plus statique.

## 5. Nappe noise + tonal
**Rôle** : mélange de souffle/vent/texture et d'une note ou d'un accord discret.

**Serum 2** : OSC tonal + NOISE, routes distinctes ; filtre plus haut sur tonal, band-pass/high-pass sur noise.  
**Ableton** : Drift/Meld + chaîne de noise/sample dans un Rack.  
**HEUR** : le bruit doit bouger différemment du noyau tonal. Éviter qu'un LFO unique fasse respirer toutes les couches ensemble.  
**Macros** : `CORE↔NOISE`, `TONE`, `MOTION`, `AIR`, `SPACE`.  
**Test** : passer en mono ; le noyau tonal doit survivre même si la texture se réduit.

## 6. Nappe sidechain-pulsed
**Rôle** : nappe rythmique respirant avec le groove sans devenir un pluck.

**Serum/Ableton** : source soutenue ; modulation de volume/filtre en rythme. [DOC] Distinguer modulation interne, automation Live et sidechain audio.  
**HEUR** : profondeur 20–70 % selon densité ; conserver un fond continu si l'intention est atmosphérique.  
**Macros** : `PULSE`, `DEPTH`, `TONE`, `SPACE`.  
**Test** : écouter sans kick ; la courbe doit avoir un sens rythmique même avant sidechain externe.
