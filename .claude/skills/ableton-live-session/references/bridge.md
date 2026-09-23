# LOM Bridge — mémo d'usage (lom.py, Remote Script UDP 7421)

- `python3 lom.py ping` → version + session ; les références `o:<session>:<n>` changent à chaque relance de Live.
- `python3 lom.py py "<expr>"` : expression Python dans Live (`song`, `app`). Pour un script : `scripts/pyl.sh fichier.py` (mettre le retour dans `result`, listes plutôt que dicts).
- `python3 lom.py param "<piste>" "<device|mixer>" "<param>"` → `ref nom min max valeur affichage …` (la ref sert à `read`).
- `python3 lom.py read "<piste>" <paramRef> <tA> <tB> <res>` : valeur réelle le long de la plage (transport ARRÊTÉ). `res` = points par temps : 0,25 = un par mesure, 1 = un par temps.
- `python3 lom.py apply spec.json [--dry]` : écrit l'automation d'arrangement. Attendre la fin : boucler sur `python3 lom.py jobs` tant que `running|queued`.
- Depuis 0.5.0, chaque écriture (`apply`, `shape`, `clear`) est **tout ou rien** (un clip qui échoue → tout est remis, message « étape annulée automatiquement ») puis **relue** : ligne `relecture: exact|sampled, n points, écart max …` dans le journal d'`apply`. `relecture: interrupted` = écrit mais non contrôlé → relire avec `read`. Un plan refusé pour « automation surchargée » = un paramètre automatisé a été bougé à la main : `python3 lom.py py "song.re_enable_automation()"` puis relancer.
- `python3 lom.py ping` prévient si le bridge chargé dans Live n'a pas la version du script sur le disque (après un chargement de Set, le rechargement à chaud est perdu : relancer Live).

## Spec d'automation
```json
{"beatsPerBar":4,"automations":[
 {"track":"BUS - HARMONIE","device":"REQ 6 Stereo","param":"Band1 Frq","unit":"raw","res":8,"curve":"lin",
  "accept":["fades","warp","clamp"],"points":[["25|1",0.2565],["32|4.75",0.5615],["33|1",0.031]],"note":"…"}]}
```
- `device` : nom (unique sur la piste) ou `mixer` (`Volume`, `Pan`, `Send A`…). `unit` : `disp` (valeur affichée, résolue par dichotomie — échoue si l'affichage est arrondi, ex. Hz entiers de REQ 6 → utiliser `raw`), `raw` (0–1), `rel`.
- Une fenêtre = deux temps distincts ; un saut à la fin = deux points au même instant. `curve` `lin` sur un paramètre brut logarithmique (fréquences) donne une montée régulière en octaves ; `exp` reste longtemps bas.
- **Rien n'est automatisable hors d'un clip** : sur un bus/piste audio sans clip, poser un clip audio silencieux comme support (skill `live-automation`). Bus en Monitor In : le clip ne joue pas, l'automation reste.
- Les clips d'arrangement n'exposent pas leurs enveloppes ; le bridge reconstruit le clip (audio réimporté avec warp automatique → accepter `warp`). Après « Insérer Silence » de Live, clips, automations et repères se décalent ensemble (bonne méthode pour allonger une section : poser la boucle par `song.loop_start/loop_length`, vue Arrangement, Edition › Sélectionner boucle, Créer › Insérer Silence, relire).
- Charger un VST : `app.browser.plugins` → dossier `VST3` → chercher par `name` (récursif, profondeur 3) → `song.view.selected_track = t ; song.view.select_device(t.devices[-1]) ; app.browser.load_item(item)`. Presets Live natifs : `app.browser.sounds`.
- Vu-mètres : lire `output_meter_left/right` par appels séparés pendant la lecture (`start_playing()` puis `current_song_time = …`).
