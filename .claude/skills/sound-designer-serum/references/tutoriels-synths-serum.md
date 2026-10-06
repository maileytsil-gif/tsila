# Études : synthés conçus dans Serum (lead, pluck, hook, chords, pad, drone)

> Fichier remis par l'utilisateur le 05/10/2026 et intégré tel quel au skill `sound-designer-serum`. L'étude a été faite dans Claude in Chrome sur le Mac, par la lecture des transcriptions ; aucune vidéo n'a été écoutée. La synthèse utilisable, par type de synthé (lead, pluck, hook, accords, pad, drone), est dans `synths-serum-synthese.md`. Les identifiants (LE-01, PL-01, HO-01…) sont ceux de ce fichier.


6 types × 15 vidéos, en priorité house (≈ 8), puis drum and bass (≈ 4), puis dubstep (≈ 3). Chaque vidéo vérifiée sur sa transcription complète par un agent dans le Chrome de l'utilisateur. **Son jamais écouté. Captures d'écran pas encore faites** (voir « À vérifier à l'écran »).

| Type | Vidéos | House / DnB / Dubstep | Manques principaux |
|---|---|---|---|
| Lead | 15 | 8 / 4 / 3 | 2 tutos FR seulement ; 4 en Serum 2 |
| Pluck | 15 | 8 / 4 / 3 | pas de pluck tech house ; DnB surtout DNB Academy ; 2 en Serum 2 |
| Hook | 15 | 8 / 4 / 3 | DnB difficile (2 cas limites) ; 1 FR ; 2 en Serum 2 |
| Chords | 15 | 8 / 4 / 3 | tout en Serum 1 ; pas d'accords afro ou tech house ; 3e dubstep = future bass |
| Pad | 15 | 8 / 5 / 2 | aucun pad melodic dubstep fait dans Serum ; aucun FR |
| Drone | 15 | 8 / 4 / 3 | genres souvent attribués par l'agent (tutos génériques) ; DnB = DNB Academy seulement |



# Lead

## LEAD — leads designés dans Xfer Serum (préfixe LE)

Sélection : 15 vidéos (8 house, 4 DnB, 3 dubstep), 13 EN + 2 FR. Toutes vérifiées sur transcription (sous-titres auto YouTube lus dans le panneau Transcription). Valeurs = ce qui est DIT ; « (interp.) » = mon interprétation ; [ASR ?] = reconnaissance vocale douteuse. Aucun des IDs n'apparaît dans /tmp/outputs/etudes-videos-chrome.md ni dans chops/deja_vus.txt (ce dernier est vide).

---

## HOUSE (8)

### LE-01 SERUM Tutorial | Iconic Lead whoop, AFRO HOUSE | &ME, Rampa, Keinemusik — The Sound Design Channel (Leo Lauretti / Abstract Music Lab), 6:43, 2024-09-22, outil : Serum 1
URL: https://www.youtube.com/watch?v=Bcn0bxndBmI
Technique(s) : lead « whoop » afro house = enveloppe de pitch (ENV2 → semitones + Master Tune), filtre MG Low 18 avec LFO rapide, chaîne FX complète.
Transcription : oui (EN, auto)
- 0:52 Osc A : Basic MG (basic shapes), position WT « a lot up », octave -1 (« a bit down »), level un peu baissé.
- 1:13 Osc B : Init saw, -2 octaves, unison 3, detune un peu baissé, blend baissé, level baissé.
- 1:36 Noise : « AC Hum », un peu plus fort.
- 1:50 ENV2 : attack montée, sustain à 0, decay un peu baissé, release baissé ; courbes tordues (poignées).
- 2:24 ENV2 → semitones osc A et osc B en **unipolaire** = le « woo ». 2:40 Matrix : ENV2 → Global Master Tune en plus.
- 2:56 ENV1 (ampli) : sustain 0, release un peu monté, attack un peu montée, courbes ajustées.
- 3:21 Filtre MG Low 18, routé A + B + noise + sub, cutoff monté. 3:39 LFO1 → cutoff, faible quantité mais rate « a lot faster » (vibration). 3:56 ENV2 → cutoff aussi. 4:05 Drive monté, Fat un peu.
- 4:18 FX : Distortion Tube (wet baissé) → EQ (low cut + high shelf) → Chorus (mix baissé) → Delay (feedback baissé, filtre freq montée, Q baissé, wet baissé) → Reverb (low cut activé, mix monté).
- Genre : afro house (référence &ME & Rampa « More Love » remix, Keinemusik) — lead « whoop » signature du genre.
À vérifier à l'écran : 0:56 position WT exacte de Basic MG ; 2:20 profondeur ENV2 → semitones (nombre de demi-tons) ; 3:00 ADSR ENV1 en ms ; 3:47 rate LFO1 ; 4:34 réglages Tube et EQ.

### LE-02 The Ultimate Afro House Lead Tutorial — Sonance Sounds, 6:30, 2025-04-03, outil : Serum (version non précisée à l'oral, « new serum » = nouvelle instance ; FL Studio)
URL: https://www.youtube.com/watch?v=v1P0K_YNxEA
Technique(s) : 3 familles de leads afro house — lead rythmique saw filtré, lead arpégé square + vibrato rapide + bandpass, lead-pluck 1/16.
Transcription : oui (EN, auto ; noms d'artistes mal reconnus)
- 0:35 Style 1 [ASR ? « kind of six style »] : WT saw (« square saw »), MIDI : offbeat + note juste avant l'offbeat, hors grille. 0:57 sustain à 0, decay raccourci, un peu de release, **mono**. 1:06 Filtre Low 12, LFO1 → cutoff. 1:20 Noise + ENV1 routée. 1:29 FX Hyper/Dimension, chorus, reverb, delay, low cut. 1:38 Mod wheel → reverb, delay, cutoff (automation).
- 2:12 Style 2 [ASR ? « night free »] : square wave + portamento ; MIDI 6te → 5te en boucle (arp). 2:44 unison 5 voix + detune ; layer saw +1 octave, moins de sustain. 3:00 LFO2 → fine tune des 2 osc, rate très élevée. 3:11 LFO1 très rapide → Matrix → Master Tune à très faible quantité. 3:25 **Filtre bandpass**, mix 90 %. Noise ; distortion/OTT [ASR ?] ; retrait du bas.
- 4:29 Style 3 lead 1/16 : MIDI quantifié hors grille + vélocité aléatoire ; saw, sustain 0, mono ; filtre + drive ; enveloppe sans sustain, decay ~150 ms → cutoff. 5:41 FX distortion, chorus, EQ (résonance coupée), compresseur, reverb ; mod wheel → reverb/delay/cutoff.
- Genre : afro house (Keinemusik, Rampa, Hugel cités en description) — leads groovy/rythmiques typiques.
À vérifier à l'écran : 0:41 nom exact de la WT « square saw » ; 1:10 cutoff et quantité LFO1 ; 2:30 temps de portamento ; 3:03 rate LFO2 et quantité fine ; 5:24 decay ENV (~150 ms) et quantité vers cutoff.

### LE-03 HOW TO BASS HOUSE LEADS (Knock2, Tchami, Habstrakt) — Sam Smyers, 14:11, 2022-12-17, outil : Serum 1 (Ableton)
URL: https://www.youtube.com/watch?v=vxP3DrjmMWk
Technique(s) : 3 leads bass house — sync + Diode 2, pitch-bend par LFO→Master Tune piloté par macro, FM + noise « kick attack ».
Transcription : oui (EN, auto)
- Lead 1 (Knock2 « dashstar* ») 1:07 Sub on, octave -3. Osc A : Analog PWM Mini, +4 demi-tons, WT pos ~55, level baissé. 1:29 Osc B : +7 demi-tons, Analog Basic Shapes, warp **Sync ~1,9–2 %**, level ~50 %. Noise Analog J106 HP. 1:52 FX Multiband + **Distortion Diode 2** (le caractère). 2:12 ENV1 attack ~60 ms, decay court, sustain, release. 2:34 LFO1 1/4 mode Envelope → filtre MG Low 6 (osc B seulement). 2:56 mono. 3:06 FX filtre **Samp Hold** (dégradation façon bitcrush), Hyper/Dimension (hyper mix baissé), EQ, master baissé ; 4:07 Sausage Fattener, overdrive ; reverb automatisée on/off + reverse reverbs ; Kickstart 2. 5:03 dupliquer pour une couche sub séparée.
- Lead 2 (Habstrakt « Outer Space ») 6:11 Noise Analog Bright White ; osc B Basic Shapes → square, -3 octaves, warp PWM monté. 6:51 LFO1 1/8 mode Envelope ; LFO2 BPM off rate rapide mode Envelope. 7:13 Matrix LFO1 → Global Master Tune **+1**, unipolaire ; mono. 7:41 LFO2 → Master Tune **+24 (2 octaves)** unipolaire, Aux Source = **Macro 1** → automatiser la macro. 8:21 Distortion drive au max, multiband, EQ (low cut, aigus +), filtre FX MG Low 24 avec drive, reverb Hall ; automation wet reverb + EQ.
- Lead 3 (Tchami remix « You Know You Like It ») 10:42 Sub saw -2 oct. Osc A -3 oct, Digital « I Can Has Kick », WT montée, unison 2, detune bas, fine tune. 11:12 Osc B Monster 1 +7 demi-tons. 11:25 Osc A warp **FM from B 53 %**. 11:38 Noise « Kick Attack 29 » one-shot. 11:52 ENV2 → MG Low 12 (A+B+sub). Mono ; LFO1 mode Envelope → WT pos. 12:39 Tube (drive +, mix −), chorus, delay, Hyper/Dimension, EQ ; saturateur Ableton ; Kickstart 2.
- Genre : bass house (Knock2, Habstrakt, Tchami) — leads distordus mi-basse mi-lead, couche sub.
À vérifier à l'écran : 1:40 valeur sync exacte ; 2:20 ADSR ENV1 ; 7:20 forme LFO1/LFO2 (enveloppes) ; 8:05 courbe d'automation de la Macro 1 ; 11:30 FM 53 % et WT pos osc A.

### LE-04 How To Make A Transforming Bass/Tech House Lead (Matroda/Truth x Lies/Ship Wrek) | Dropgun Tutorials — Dropgun Samples (Jonah), 10:41, 2023-01-27, outil : Serum 1
URL: https://www.youtube.com/watch?v=dqVrATM87fU
Technique(s) : lead qui « se transforme » sur 3 temps via un LFO lent en mode libre utilisé comme automation (detune, decay, filtres), filtre Flanger négatif + Low 12/18.
Transcription : oui (EN, auto)
- 0:56 MIDI : mélodie de basse convertie en 1/16.
- 1:06 Osc A Analog Basic MG (saw) +1 octave. 1:31 Osc B Digital « Distorted Bass Dropper » (texture). 1:56 Osc A unison **2 voix** (phasing), osc B **4–6 voix** ; detune des deux juste au-dessus de 0 (préparés pour la modulation).
- 2:42 ENV1 : sustain 0, courbe de decay remontée (moins négative), decay réglé pour couper la queue → stab.
- 3:19 LFO1 : rampe montante, mode **Off** (libre), rate **1 bar**, forme qui finit à 3 temps (alt pour snapper). 4:04 LFO1 → detune des 2 osc (~midi), → decay ENV1.
- 4:41 Filtre : Flanges **Negative Flanger**, A+B, résonance et drive élevés ; LFO1 → **mix** du filtre en inverse (moins d'effet quand le son s'ouvre).
- 6:00 FX Distortion **Diode 1**, drive un peu. 6:23 FX filtre **Low 12 ou 18 dB**, cutoff ~11 h, LFO1 → cutoff à fond, résonance + drive. 7:02 ENV2 sustain 0 decay court → cutoff (quantité faible).
- 7:38 FX Flanger mix bas/moyen, Chorus (LP monté), Dimension Expander tard dans la chaîne, Compresseur (seuil pour léger GR + makeup). 8:40 courbe de modulation négative dans la Matrix. 9:10 Post : Neutron 3 Exciter, multiband Neutron, Pro-Q3 dynamique.
- Genre : tech house / bass house « fusion » (Matroda, Truth x Lies, Ship Wrek).
À vérifier à l'écran : 3:50 forme exacte du LFO1 (grille) ; 4:15 quantités LFO → detune/decay ; 5:15 cutoff/res/drive du Negative Flanger ; 6:40 cutoff 11 h et pente choisie ; 8:50 courbe Matrix.

### LE-05 SERUM 2 Tutorial | Rich Lead, Melodic House | Anjunadeep — The Sound Design Channel (Leo Lauretti), 9:09, 2025-06-01, outil : Serum 2
URL: https://www.youtube.com/watch?v=66RrYjW5Q24
Technique(s) : 3 oscillateurs Serum 2 avec warps (phase distortion depuis le noise, hard clip, bend), ENV1 bipolaire sur MG Low 24, bus FX + main FX.
Transcription : oui (EN, auto)
- 1:03 Osc A saw par défaut, unison monté, detune « a lot up », level baissé. 1:21 Osc A warp **Phase Distortion from Noise** ; noise activé (level bas, pitch bas) « AC Hum ».
- 1:46 Osc B : tables Serum « **Saw Drift 303** », warp **Hard Clip** (distortion), random 0, phase 0.
- 2:28 Osc C : Basic Shapes **sine**, level baissé, warp **Bend +/-** (presque une saw), phase/random 0.
- 2:59 ENV1 module (warp/osc (interp.)) ; ENV1 : un peu d'attack, moins de sustain, moins de decay, plus de release, poignées de courbes repositionnées.
- 3:57 Filtre **MG Low 24** sur A, B, C, cutoff monté, ENV1 en **bipolaire** (alt+shift), drive + fat (deux saturations différentes), résonance inchangée.
- 4:46 Filtre envoyé à 100 % vers **Bus 1** : Chorus (LP, moins de depth), Delay **1/8 pointée + 1/8** (freq +, Q −), Reverb **Plate** (moins d'aigus) + Reverb **Hall** plus grande, low cut.
- 6:50 Main : low cut, Distortion **Soft Clip**, ENV1 → drive, EQ bell (boost), Dimension (hyper à 0, size baissée), compresseur. 8:23 Plus serré : baisser le decay. 8:40 Macros (cutoff, width).
- Genre : melodic house / Anjunadeep (preset « Seagull »).
À vérifier à l'écran : 1:30 quantité de PD from noise ; 2:10 réglage du hard clip osc B ; 3:30 ADSR ENV1 en ms ; 4:20 quantité ENV1 bipolaire ; 5:50 temps du delay et réglages des deux reverbs.

### LE-06 Cinematic HOUSE LEADS Like RUFUS DU SOL / CamelPhat / Ytram (Serum Tutorial) — SynthHacker, 6:47, 2022-02-16, outil : Serum 1
URL: https://www.youtube.com/watch?v=bqdOdhEMVnQ
Technique(s) : lead cinématique — dérive de pitch type bande (LFO → fine), couche +1 octave unison 2 (pure largeur), enveloppes séparées ampli/filtre/noise, reverb qui monte pendant la tenue.
Transcription : oui (EN, auto)
- 1:37 Osc A WT **Hyper Digital Saw**, attack adoucie, long decay. 1:52 LFO → fine tune subtil (pitch drift « tape »). 2:10 unison + **blend baissé**.
- 2:32 Osc B : duplicata **+1 octave, unison 2 voix** (« seule valeur sans voix mono » → couche purement large), 2e LFO → fine (vibrato).
- 3:11 Filtre **Low 12 dB**, un peu de résonance et de drive, les 2 osc. 3:33 Enveloppe séparée attack/decay lentes → cutoff ; ampli avec attack plus courte.
- 4:12 Noise « **Arp White** » **hors filtre**, sa propre enveloppe (attack douce, decay plus court).
- 4:54 FX Dimension subtile ; delay subtil avant la reverb ; LFO lent en rampe montante (mode envelope) → **mix reverb** (plus de reverb quand la note est tenue). 5:38 saturation « tape » avec EQ interne coupant le bas ; EQ passe-haut final.
- Genre : melodic / « cinematic » house (Rüfüs Du Sol, CamelPhat, Ytram « Alive »).
À vérifier à l'écran : 1:45 attack/decay ENV1 ; 2:00 rate/forme du LFO de drift ; 3:20 cutoff/res/drive ; 3:50 ADSR de l'enveloppe filtre ; 5:15 forme du LFO → reverb mix.

### LE-07 Serum Tutorial - Future House Lead (Tchami/Curbi/Oliver Heldens) — SynthHacker, 13:08, 2015-10-18, outil : Serum 1
URL: https://www.youtube.com/watch?v=yYYWgmyqmKs
Technique(s) : lead future house classique — saw unison 7 en FM depuis un osc B muet 2 octaves au-dessus, ENV2 sur Low 18 + drive/fat, Dimension + Tube pre-HP.
Transcription : oui (EN, auto)
- 2:33 Osc A saw **-1 octave** ; osc B doit être **2 octaves au-dessus** de A. 3:02 Osc A **unison 7**, blend baissé.
- 3:33 Osc B : Analog « BD Sine » [ASR ?], **level à 0** → sert uniquement de source FM. 4:03 Osc A warp **FM from B** (au goût) ; alternative FM from sub/noise.
- 5:16 ENV1 : attack très sèche, sustain un peu au-dessus de la moitié, un peu de release. 5:50 ENV2 : decay **~2,6 s**, sustain **~17 %**, release **~380 ms**, courbes plus « sharp ».
- 6:41 Filtre **Low 18 dB**, cutoff bas, ENV2 → cutoff. 7:11 **Drive + Fat** montés. 7:57 **Random phase à 0** sur A et B (constance).
- 9:00 FX Hyper/Dimension : hyper mix bas, dimension mix haut, size un peu baissée. 10:30 Distortion **Tube**, mode pre-filtre **HP ~300 Hz**, drive poussé, mix plein. Seule reverb externe.
- Genre : future house (Tchami, Curbi, Oliver Heldens).
À vérifier à l'écran : 4:40 quantité FM ; 6:00 valeurs ENV2 affichées ; 7:20 drive/fat ; 9:30 réglages Dimension ; 10:45 drive Tube.

### LE-08 FUTURE RAVE LEAD sur SERUM - "Kill Me Slow" David Guetta & Morten — Strob Studio Mixing & Mastering, 7:59, 2022-02-24, outil : Serum 1
URL: https://www.youtube.com/watch?v=k4LlAbg3Wps
Technique(s) : lead future rave percussif — saw unison 16 sans detune pour pousser le drive du filtre, ENV2 très courte sur drive + bandes de l'OTT, pitch punch par LFO rapide → Master Tune. (FR)
Transcription : oui (FR, auto ; très bruitée)
- 0:32 Base saw : WT Digital « HyPA » [ASR ? « la haye pas / aipa »]. 0:46 bonne octave ; ENV1 très percussive : sustain très bas (~-60 dB dit), decay très court, un peu de release.
- 1:10 Noise « Bright » [ASR ?] indispensable, ENV1 sur son level, pitch monté.
- 1:32 Filtre MG Low 18 [ASR « ied 18 »], peu de résonance, coupe légère (limiter la fondamentale) ; drive monté. 1:55 ENV2 très courte **~50 ms** → drive (percussion) ; un peu de Fat.
- 2:57 Unison **16 voix**, **random 0 et detune 0** (juste plus de niveau dans le drive).
- 3:29 FX **OTT** (« quasi indispensable »). 3:40 ENV2 → bandes high + mid du multiband, unipolaire dans la Matrix.
- 4:07 EQ : grosse bell large ~2–3 kHz ; ENV3 (copie plus longue d'ENV2) → gain EQ. 4:55 Option : distortion en mode bandpass sur les médiums.
- 5:18 Reverb (session) ; 5:49 pousser clip / sortie OTT. 6:15 LFO très rapide, BPM off, mode Envelope → Matrix **Global Master Tune** (punch de pitch). 6:46 Variante plus ronde : autre enveloppe à attack arrondie → level osc (le noise attaque en premier).
- Genre : famille house (future rave, David Guetta & Morten) — classé ici en house/future house élargie.
À vérifier à l'écran : 0:40 nom exact de la WT Digital ; 1:00 ADSR ENV1 ; 2:05 temps ENV2 (~50 ms) et quantité → drive ; 3:50 réglages Matrix multiband ; 6:30 forme du LFO → Master Tune.

---

## DRUM AND BASS (4)

### LE-09 How to make LEADS like CULTURE SHOCK - THERE FOR YOU | Serum Tutorial — DNB Academy (Paulo), 7:52, 2021-04-24, outil : Serum 1
URL: https://www.youtube.com/watch?v=Z6z6OHZSimY
Technique(s) : pad saw sync modulé lentement, transformé en lead arpégé avec LFO « plucky » sur level et cutoff ; reverb avec pseudo-sidechain par LFO.
Transcription : oui (EN, auto)
- 1:05 Progression (racines A G E F B dites). 1:43 Osc A Basic Shapes saw ; osc B « MB Saw » [ASR ?]. 2:03 unison monté sur les deux, detune baissé sur les deux.
- 2:20 Warp **Sync** sur A et B, un LFO → sync des deux, **lent (2 bars)**, peu intense. 2:47 Osc B **+1 octave**, mix des niveaux. 2:57 ENV1 sustain baissé.
- 3:13 FX Hyper/Dimension (hyper mix bas) ; Distortion **Downsample** drive très bas, mix baissé (« dirt » dans les aigus) ; Reverb size + decay montés, low cut, high cut au minimum. 4:02 LFO mode Envelope, forme montante → mix reverb (« pseudo side-chain »).
- 4:47 Lead : patch dupliqué + **arpégiateur** (accords réduits à 3 notes). 5:40 LFO séparé forme « plucky » → level osc A et B ; filtre sur A+B, LFO → cutoff (shift+alt). Attack optionnelle, layer de quinte optionnel ; un peu de release.
- Genre : DnB liquid / dancefloor mélodique (Culture Shock).
À vérifier à l'écran : 2:35 forme/quantité LFO → sync ; 3:35 réglages Downsample ; 4:10 forme du LFO → reverb ; 5:00 réglages de l'arpégiateur ; 5:50 forme du LFO plucky et filtre choisi.

### LE-10 2 DANCE LEADS LEADS LIKE SUB FOCUS, DIMENSION, DARUDE! | Serum Drum and Bass Tutorial — STRANJAH, 11:27, 2020-09-23, outil : Serum 1
URL: https://www.youtube.com/watch?v=_zHeeqFQmEU
Technique(s) : deux leads dancefloor — supersaw (Dimension « Love to Me ») et stab square « Sandstorm » (triangle -7 + square +2 oct, distortion pre-HP).
Transcription : oui (EN, auto)
- Lead 1 : 1:37 un osc saw, unison ≥3 → **7**, detune baissé « pas trop ». 2:08 ENV1 release **200–400 ms**. 2:29 Hyper/Dimension, distortion drive +, delay + reverb. 3:04 Noise « Bright White » dans le filtre en **HP**, level bas. 3:46 EQ HP + boost médiums/aigus. 4:27 MIDI en **croches**.
- Lead 2 : 5:37 Osc A Basic Shapes → **triangle**, **-7 demi-tons** (quarte en dessous). 6:31 Osc B **square +2 octaves** (le ton aigu prioritaire). 7:24 Filtre **Low 24** A+B ~**1000 Hz**. 7:47 Distortion en mode **PRE** HP ~**200–300 Hz**, drive **au max**. Hyper/Dimension optionnel, EQ, reverb + delay. 9:08 Variantes : Hyper avant la distortion, release, niveaux osc au max (plus de drive). 9:50 MIDI en **doubles croches**.
- Genre : DnB dancefloor (Sub Focus, Dimension, Pendulum ; racines rave/Darude).
À vérifier à l'écran : 1:55 detune exact ; 2:40 réglages distortion lead 1 ; 5:55 position WT du triangle ; 8:10 type de distortion choisi ; 9:15 ordre des FX en variante.

### LE-11 Simple recreation of Subsonic's Emotional Square Lead from "Take it all" - Serum DNB tutorial — How to DNB, 14:18, 2026-02-04, outil : Serum 2
URL: https://www.youtube.com/watch?v=0qTJCHozon4
Technique(s) : square « 8-bit » émotionnel — Basic MG un peu vers le sinus, PD (ex-« FM » de Serum 1) depuis un sinus, hard clip, slap delay + plate, LFO de volume qui « respire » sur la noire.
Transcription : oui (EN, auto) — pub 2:30–5:10
- 5:24 Osc A : tables Serum 1 Analog **Basic MG** [ASR « basic MDC »], position WT légèrement vers le sinus (marge pour la distortion), octave haute ; osc B sinus octave basse ; 6:14 osc C sinus **-2 octaves**.
- 6:30 Osc A warp **PD (phase distortion)** from B (« ce qui s'appelait FM dans l'ancien Serum ») ; level de l'osc modulant baissé → léger vibrato ; coupé pour l'instant.
- 7:02 Reverb externe longue (celle de Serum jugée insuffisante). 7:32 Hyper/Dimension large, Chorus, mixes baissés. 8:08 Distortion **Hard Clip**. 8:24 Delay preset usine « slap delay » [ASR « unlin »]. 9:15 Reverb **Plate** en plus (mélanger plusieurs reverbs). 9:26 EQ bell ~**1 kHz**.
- 9:57 LFO → filtre (optionnel). 10:25 LFO → level : volume qui creuse et remonte dans la même noire. 10:57 PD subtil (plus = grain). 11:40 passage à -1 octave (interp. : osc C/B). 11:52 Limiteur/clipper (K-Clip) après la reverb.
- Genre : DnB dancefloor (Subsonic & Stealth, en do mineur).
À vérifier à l'écran : 5:35 position WT Basic MG ; 6:40 quantité PD ; 8:30 nom exact du preset de delay ; 10:30 forme du LFO → level ; 11:45 quel osc passe à -1 octave.

### LE-12 How to Make a Detuned Noisia-Like Lead in Serum 2 | DNB Sound Design — DNB Academy (Johno aka Frags), 9:37, 2025-07-02, outil : Serum 2
URL: https://www.youtube.com/watch?v=p7c9Ai0rzBo
Technique(s) : lead neuro désaccordé — 2 saws (-3 oct / -1 oct +4 demi-tons) avec FM 30, warps alternatifs Flip/Asymmetry, 3e osc DX Brass via filtre 2 Serum 2, chaîne FX Splitter + Convolve.
Transcription : oui (EN, auto)
- 0:17 Osc A saw simple [ASR « subwave »] **-3 octaves**. Osc B **-1 octave +4 demi-tons**. 0:55 Osc A warp FM (« new FM function ») **30** (précis, phasing) ; warp alternatif **Flip**. 1:39 Osc B warp alternatif **Asymmetry+**.
- 2:00 Osc C : Digital « DX Brass 2 » [ASR « DX Breast 2 »], **-1 octave**, WT pos **~35**, FM from B **30**.
- 2:51 **Always Legato + mono** (glide).
- 3:08 Filtre 1 **MG Low 12** (A+B), LFO forme « steady » → cutoff inversé (alt+shift). 4:04 level osc C baissé. 4:14 Filtre 2 : nouveau filtre Serum 2 « WSP » [ASR ?] sur osc C seul, même LFO, drive + morph montés.
- 5:00 FX : Distortion **Tape** légère, LFO → drive ; EQ (bas coupé, pic hauts-médiums, même modulation) ; Compresseur **multiband** ; 6:12 **Splitter L/H** (~**500 Hz**) : sur les hauts, **Convolve** « 10 Amp Box » [ASR ?] size **30–40**, plus brillant, modulation sur le mix ; Reverb **Plate** mix modulé.
- 7:45 Option sub -3 octaves en Direct Out. 8:19 Macro → Flip ~**5 %**, cutoff, FM, reverb.
- Genre : DnB neuro / techy (Noisia).
À vérifier à l'écran : 1:10 nom exact du mode FM Serum 2 et sa source ; 2:15 WT DX Brass 2 ; 4:20 nom du filtre 2 ; 6:30 IR choisie dans Convolve ; 8:25 profondeurs de la macro.

---

## DUBSTEP (3)

### LE-13 How to make melodic Dubstep lead in Serum — PHENOMSOUND, 9:31, 2023-06-17, outil : Serum 1 (FL Studio)
URL: https://www.youtube.com/watch?v=-KrbNAzW8s0
Technique(s) : lead melodic dubstep « Flux Pavilion » — un seul LFO1 d'1 mesure pilote WT, levels, filtre, Hyper, drive, EQ formantique et Flanger -1 ; vibrato LFO2 → Master Tune.
Transcription : oui (EN, auto)
- 1:13 Osc A Analog Basic MG [ASR « MDC »], LFO1 → WT pos **8**. LFO1 **1 bar**, forme d'enveloppe, **trigger on** ; LFO1 → level osc A.
- 1:53 Filtre [ASR « alt passes one »], LFO1 → cutoff et résonance ; res baissée, modulation ~**65**, cutoff ~**72** [ASR], drive **14 h**.
- 2:17 **Mono + legato**, porta **12 h**. 2:27 Sub, LFO1 → level sub **17**. 2:36 Noise (dossier Organics) [ASR « Air Can »] pitch **70**, level bas, LFO ~**15**.
- 3:04 FX Hyper/Dimension : les deux mixes + size à 0, LFO1 → **20** et **25–30**. 3:40 Distortion **Soft Clip** drive 0, LFO1 → drive ~**55**. 3:56 EQ : bande 1 ~**30 Hz**, LFO → fréquence **50**, gain ~**+12 dB** ; bande 2 fréquence au max, modulation vers le bas, gain **-10** → effet de formant. 4:43 Multiband gains ~10 dB [ASR « tender spell »].
- 4:54 FX filtre **Flange -1** cutoff **289 Hz**, LFO **7**, res **64 %**, mod **70**, drive **25 %**. 5:52 LFO2 → Master Tune **unipolaire 1**, rate **1/16**, vibrato doux.
- 6:55 Post : OTT + EQ. 7:27 Varier forme LFO1 / résonance → sons robotiques (riddim).
- Genre : melodic dubstep (Flux Pavilion).
À vérifier à l'écran : 1:30 forme de LFO1 ; 1:55 nom exact du filtre principal ; 2:40 nom du sample de noise ; 4:05 réglages EQ ; 5:05 Flanger -1.

### LE-14 Make a Dubstep Lead like Skrillex 'VOLTAGE' in Serum 2 Tutorial — Konstricta, 4:53, 2025-04-15, outil : Serum 2
URL: https://www.youtube.com/watch?v=pVkdRjBXHSo
Technique(s) : lead brostep early Skrillex — WT Acid + sync, osc B bend-, double warp Serum 2 (PD from C), osc C muet comme source PD, LFO1 mode Envelope sur tout, Diode 2.
Transcription : oui (EN, auto)
- 0:49 Osc A : Analog « Acid », octave ±3 [ASR « turn octave by three », sens à vérifier], random phase 0, WT pos ~**5**. 1:06 Warp **Sync ~1,10 %** [ASR ?], section du dessous à fond à droite (moins dure).
- 1:19 LFO1 pente simple, **mode Envelope** → sync. 1:38 level osc A baissé, LFO1 → level **90 %**.
- 1:55 Osc B : Basic Shapes, **+1 octave**, random 0 ; warp **Bend-**, LFO1 → **60 %**. 2:30 2e warp **PD from C 30 %** ; LFO1 → level.
- 2:47 Osc C : WT « JNO » [ASR ?], **-3 octaves**, **level 0** (source PD uniquement). 3:13 Bruit blanc, LFO1 → level noise léger.
- 3:43 FX : Distortion **Diode 2** drive ~moitié, mix baissé ; Hyper/Dimension subtil (tous les potards un peu baissés) ; **2 compresseurs multiband** (gain au goût) ; EQ boost aigus.
- Genre : dubstep / brostep (Skrillex « Voltage », original fait dans Massive selon l'auteur).
À vérifier à l'écran : 0:55 sens de l'octave osc A ; 1:10 valeur sync et « section du dessous » ; 1:25 forme LFO1 ; 2:50 nom de la WT osc C ; 3:50 réglages Diode 2.

### LE-15 Tutoriel Dubstep Episode 2 : Le Robot Lead — New Nova, 7:22, 2021-07-01, outil : Serum 1
URL: https://www.youtube.com/watch?v=0tqWZCoMEos
Technique(s) : « robot lead » dubstep — WT digitale en FM depuis une saw muette, filtre Misc **Reverb** avec keytrack, delay ultra court (~20 ms) sans feedback. (FR)
Transcription : oui (FR, auto)
- 0:42 Osc A octave **-2** ; WT Digital [ASR « jetteront évolution » — à identifier] (alternative : Spectral **Monster 3**).
- 1:14 LFO (forme comme l'épisode growl, **trigger on**) → WT pos + level osc (levels à 0) ; quantité réduite (esthétique).
- 2:00 Warp **FM from B** ; osc B **level 0** ; osc B Analog Basic Shapes **saw**. 3:19 osc B : réglage [ASR « cinq noms »] monté (fréquence plus haute, moins précise) (interp. : coarse/semitones).
- 3:51 Filtre uniquement sur A : **Misc → Reverb** (alternative Comb), bouton **keytrack** activé (harmoniques cohérentes entre notes), cutoff fixe [ASR], pas de modulation, un peu de drive.
- 4:46 FX : Compresseur **Multiband**, gain monté ; Hyper ~**30 %**, unison **7** ; Dimension ~**20 %**. 6:03 Delay très court : Link on, BPM off, ~**20 ms**, mix ~**70 %**, **pas de feedback**. Reverb optionnelle (decay petit, size grande) pour ponctuer.
- Genre : dubstep (lead « robot » ponctuel).
À vérifier à l'écran : 1:00 nom de la WT Digital ; 1:30 forme du LFO ; 3:25 paramètre monté sur osc B ; 4:10 cutoff/drive du filtre Reverb ; 6:15 temps de delay exact.

---

### Écartés
- 7_cFrG3O2oE « The Most Elusive Tech House / Bass House Lead Sound? » (Bthelick) — fait dans **Vital** (preset Vital 1.5.5), Serum seulement mentionné.
- yu-7mBPqqZU « How to make LEADS like SUB FOCUS - SOLAR SYSTEM » (DNB Academy) — aucun sous-titre/transcription disponible.
- Ovd4vp21p60 « How to make BETTER FUTURE HOUSE LEADS in SERUM (Mike Williams, Brooks) » (ZVCH, 6:19, 2020) — étudié et valide (Evil Sweep + Rounded Saw, ENV2 → coarse pitch unipolaire, noise Glass Lid 4 comme source de warp, Low 12, mono legato) ; retiré pour limiter la house à 8 (doublon future house avec LE-07). Bon remplaçant.
- 1rYTKTXbBtg « HOW TO MAKE A DOPE MELODIC DUBSTEP LEAD IN SERUM » (Paper Skies, 3:24, 2017) — étudié et valide (LFO1 très lent → Sync ~140–150 %, Basic Shapes mi-saw mi-square, porta ~80, multiband +5 dB / -12 dB) mais ASR très dégradé ; remplacé par un tuto FR (LE-15) pour le mix EN/FR. Bon remplaçant.
- iHbn1zld9tg (Aspen Lyon, lead Avaion) — vu ouvert par l'agent « hook » dans un autre onglet ; non étudié pour éviter le doublon.
- SGYEZPqF8o8 (Sam Smyers, Amana afro lead, 1:01), TPduGgaeDHM (Ekko acid lead, 0:48), CoLPSV1BcAA, vtF5VCTKdyc — Shorts/≤1 min.
- Packs/démos de presets (sLpO0hX953g, -g-nxzx-8BU, G6PO6euN0EM, thQBh_qpdDs, zZLARxdL3MI, 17n1Dp4QT68…) — publicités/presets sans vrai sound design pas à pas (non vérifiés en détail).
- PbAS0GlqDQ8 (melodic dubstep lead in **Vital**), Kz_6M1x8heE (lead **hardstyle**, hors genres), y042m5xRxOY (euphoric/trance), qUNIEASFZSs / oCl97abVbe8 / lHXXcI3wcAo (techno mélodique, hors house), Yc_Ju6eXR2o (Strob « Bla Bla Bla », italo dance) — hors genre ou hors priorité, non étudiés.

### Manque
- Trouvé : 15/15 (8 house, 4 DnB, 3 dubstep) + 2 remplaçants valides étudiés (Ovd4vp21p60, 1rYTKTXbBtg).
- FR : seulement 2 tutos FR authentiques (Strob Studio, New Nova) ; les nombreux titres FR des résultats sont des traductions automatiques de vidéos anglaises (Sam Smyers, The Sound Design Channel…). Aucun tuto FR de lead house « pure » (afro/tech/melodic) ni de lead DnB FR trouvé.
- Serum 2 : 4 vidéos sûres (LE-05, LE-11, LE-12, LE-14) + LE-02 dont la version n'est pas dite ; les autres sont en Serum 1.
- Pistes non creusées : 0mp5oPunekg (Sam Smyers, 23 leads tech house), zvER47Wwc5I (Sam Smyers, lead tech house 90's rave), M5qxu--dWp4 / 4sL-8hQQSx8 (TSDC deep/melodic house), 2HVL7_IntBE (Donkong future house), TM01prFw9sA (5 tips afro house leads), zoNbGxaP9zY et 2apl9MYe08k (DNB Academy Camo/Krooked, Sub Focus Timewarp), dT2x_tF2upA (YJ Music melodic dubstep), a3tC0c8lh9g (Celestric).

# Pluck

## PLUCK — tutoriels de plucks conçus dans Xfer Serum (préfixe PL)

Méthode : recherches YouTube EN + FR dans l'onglet Chrome de l'agent (« house pluck serum tutorial », « deep house pluck serum », « melodic house pluck serum 2 », « afro house pluck serum », « future house pluck serum », « tech house pluck serum », « liquid dnb pluck serum », « drum and bass pluck serum tutorial », « dnb pluck serum », « melodic dubstep pluck serum », « dubstep pluck serum tutorial », « future bass pluck serum tutorial », « seven lions / illenium / au5 pluck serum », « pluck serum tuto », « comment faire un pluck serum », « pluck serum 2 tutorial »…), ~180 vidéos listées, 22 ouvertes, transcription lue pour chacune des 15 retenues. Titres, durées et dates relus sur la page vidéo (ytInitialPlayerResponse), pas sur les titres auto-traduits. Aucune de ces vidéos n'avait été étudiée dans les fichiers basses / kicks / chops (5AzHm6JA6LQ et T_yHA6cSKWE n'y figurent que comme « écartés, pas de kick »).

Répartition : house 8 (PL-01 à PL-08), drum and bass 4 (PL-09, PL-10, PL-11, PL-14), dubstep / melodic bass 3 (PL-12, PL-13, PL-15). Serum 2 : PL-02, PL-03 ; les autres sont en Serum 1.

### PL-01 SERUM Tutorial | Deep Pluck, Deep House | Yuma, Selected — The Sound Design Channel (tuteur Leo Lauretti / Abstrakt Music Lab), 10:37, 2025-02-09, outil : Serum (1, probable — UI Hyper/Dimension, « MG Low 24 » (interp.))
URL: https://www.youtube.com/watch?v=Hu9mYruPnIU
Technique(s) : pluck « marble » deep house à 2 osc digitaux + noise, ENV2 multi-cibles (level, WT pos A/B, cutoff, distortion), LFO1 triangle inversé 4 bars sur le band (B+) d'osc A, ENV3 très court → Master Tune (clic d'attaque), note-on random → résonance.
Transcription : oui (anglais, auto)
- 1:06 Osc A : WT « Bottle Blow » (Digital), octave -1, Unison 3, Detune 0, Random 0 ; warp « Bend +» à 50 %.
- 1:39 Osc B : WT « Harmonic Morph » (Digital), Unison 0 [ASR ? « zero » = 1 voix], warp FLIP à 50.
- 1:58 Noise : « Glass Glits 5 » [ASR ? = Glass Glitch] (Attacks/Misc), keytrack ON, niveau 0 (ouvert ensuite par ENV2).
- 2:19 ENV2 → level noise, WT pos A (presque max), WT pos B ; forme : petite attaque, sustain 0, decay rapide, courbe tirée vers le bas, un peu de release.
- 3:19 LFO1 dessiné en triangle inversé, 4 bars, → band (B+) d'osc A, bipolaire (Alt+Shift), faible quantité.
- 4:13 Velocity → WT pos A (négatif) et B (plus négatif).
- 4:38 ENV1 (ampli) : attaque minime, decay très court, sustain bas (pas 0), un peu plus de release, courbe vers le bas.
- 5:18 ENV3 : A 0, D très court, S 0, R 0 → Global Master Tune = petit « click »/pitch à l'attaque.
- 5:57 Filtre MG Low 24, routé A/B/noise, cutoff presque fermé ; ENV2 → cutoff ; velocity → cutoff.
- 6:38 Matrix : Note On Rand → résonance du filtre ; résonance baissée, Drive un peu, Fat un peu.
- 7:14 FX : Hyper mix 0 / Dimension (size baissé, mix un peu) pour la largeur ; Distortion Diode 2 mix 0 + ENV2 → mix (un peu) ; Compressor threshold bas, release bas, gain +.
- 8:16 Reverb : size presque 0, decay bas, low cut monté, high cut haut, spin/spin depth 0, wet un peu monté.
- 9:00 Option : FX Filter MG Low 18 pour retirer la « glitchiness » aiguë ; Sub en saw, niveau 0 (à monter) et routé au filtre pour la texture.
- Genre : house (deep house, référence Yuma / Selected) — pluck court, sombre, joué en mélodie dans un pack deep house PML.
À vérifier à l'écran : 1:15 (warp mode exact d'osc A), 2:50 (forme exacte d'ENV2 et valeurs ms), 3:45 (LFO1 : quantité vers B+), 6:05 (cutoff Hz du MG Low 24), 8:30 (valeurs Reverb).

### PL-02 Make Pro Melodic Afro House Plucks EASILY with Serum 2 — Rhythm HQ, 10:08, 2025-11-01, outil : Serum 2
URL: https://www.youtube.com/watch?v=5AzHm6JA6LQ
Technique(s) : pluck saw init + enveloppe de filtre, motif joué par le Clip Sequencer de Serum 2 (une note longue déclenche le pattern), tremolo/grit via LFO1 rapide → fine tune, noise à phase/niveau aléatoires (Note On Random), macros wet/decay automatisées.
Transcription : oui (anglais, auto)
- 0:18 Init Serum 2 (saw par défaut, interp.) ; ENV1 « pluck » : sustain baissé à 0 (interp.), release un peu augmenté.
- 0:28 ENV → cutoff du filtre (pluck), quantité adoucie ; 0:43 Velocity → cutoff (notes douces = plus sombres).
- 1:02 Clip view (Serum 2) : mode Mono / « KB span mono », pattern dessiné, déclenché par une note D tenue ; 1:45 pattern sur 2 bars + ghost notes à basse vélocité.
- 2:28 Reverb + Delay mix à 0 puis Macro 1 « Wet » → mix des deux (intensité max réduite), à automatiser.
- 3:08 LFO1 → Fine tune, rate 1/128 (BPM) ; Macro 2 en « aux source » de cette modulation = intensité du tremolo ; il le garde assez haut pour le grain.
- 3:50 Distortion ajoutée (type non dit) ; 4:13 automation du cutoff de base toutes les 2 bars.
- 4:44 Osc Noise (type non dit) : Note On Random 1 → phase (start), Note On Random 2 → niveau, quantité réduite.
- 5:42 Decay de l'enveloppe → Macro 4, automatisé « up and down ».
- 6:47 Second pattern en triolets (grille triolet, boucle 1 bar), essais d'octaves ; 8:28 sidechain dupliqué depuis la basse ; 8:58 ajout d'une autre wavetable (non nommée).
- Genre : house (afro house mélodique, références Black Coffee / Meera dans la description) — pattern syncopé + triolets typiques afro.
À vérifier à l'écran : 0:24 (ADSR de l'ENV1 et quantité vers cutoff), 1:20 (pattern du Clip Sequencer), 3:14 (quantité LFO1 → fine), 3:55 (type de distortion), 8:58 (wavetable ajoutée).

### PL-03 SERUM 2 Tutorial | HUGE LFO Pluck like RIVO, Lynnic, Nohr | Melodic, Afro House - Sound Design — The Sound Design Channel (avec PRODUCER NOTES by François / PML), 10:52, 2025-03-26, outil : Serum 2
URL: https://www.youtube.com/watch?v=T_yHA6cSKWE
Technique(s) : « LFO pluck » : pas d'enveloppe percussive, c'est un LFO en rampe descendante (rate en Hz, contrôlé par macro) qui hache niveaux d'osc + cutoff ; saw + square unison 8 + noise dans un MG Low 24 fermé ; OTT/multiband « smile » ; reverb Hall 7 s limitée aux médiums. Automation du rate et du cutoff dans le morceau.
Transcription : oui (anglais, auto)
- 0:45 Init ; Osc A : Analog > Basic Shapes, WT pos 2 (saw) ; Osc B : Basic Shapes pos 4 (square) ; niveaux A et B ≈ 30 %.
- 1:17 Osc B : Unison 8 voix, detune ≈ 27 ; gain master ≈ 70 %.
- 1:33 Filtre 1 : MG Low 24 dB/oct, A + B routés ; 1:57 Noise « AC Hum 1 » (défaut) à 60 %, routé au filtre (N) ; 2:16 cutoff < 300 Hz (~280 Hz).
- 2:27 LFO1 dessiné en pente descendante (« downward slope ») → level A, level B, cutoff filtre 1 ; gain ramené ≈ 50 %.
- 3:10 LFO1 mode BPM → Hz, rate ≈ 0,8 [ASR ? « 8 » sans unité claire] ; Macro 1 « Rate » → rate LFO1.
- 3:58 Matrix : LFO1 → level osc B ≈ 30 %, LFO1 → cutoff ≈ 25 % puis 22 % ; Macro 1 → rate de 70 % à 25 %.
- 4:53 FX : Compressor en Multiband, gains de bandes montés (≈ 60 / 4 [ASR ?]), gains High/Low ≈ 44–46 « smile », release ≈ 530 ms (interp. unité).
- 5:51 Reverb Plate → Hall, mix monté, decay ≈ 7 s, size ≈ 50 %, low cut ≈ 80 Hz, high cut « ≈ 80 » [ASR ? valeur haute probable], gain ≈ 90 %.
- 6:49 EQ : low shelf -7 dB, Q ≈ 51 (valeur affichée).
- 7:07 Macro 4 « Filter » → cutoff, ramené à 35 % ; résonance filtre 1 de 10 % à 0.
- 7:58 Multiband : séparations de bandes réglées (high 50 %, puis 175 %, 160 % selon l'UI) ; gain master final ≈ 59 %.
- 9:13 Automations dans le DAW : Macro Rate qui descend puis remonte, Macro Filter qui s'ouvre/ferme puis s'ouvre en grand.
- Genre : house (melodic / afro house, références RIVO, Lynnic, Nohr) — la « pulsation » rythmique vient du LFO synchronisable, typique des drops melodic/afro 2024–25.
À vérifier à l'écran : 2:40 (forme exacte du LFO1), 3:20 (valeur du rate en Hz), 5:05 (réglages du multiband), 6:15 (high cut de la reverb), 9:25 (courbes d'automation Rate/Filter).

### PL-04 EDX / Nora en Pure Future House FM Bass & Pluck Serum Tutorial — DSTAR, 10:18, 2018-09-07, outil : Serum 1
URL: https://www.youtube.com/watch?v=gNmcWR4faog
Technique(s) : pluck « marimba » à base de sine propre (Analog) + ENV3 ultra-court → Master Tune comme « transient designer » interne ; une seule note MIDI transformée en accord par l'effet MIDI Chord d'Ableton (+15) + Scale (D mineur) ; layer avec une couche FM « bass » (deuxième moitié du titre).
Transcription : oui (anglais, auto ; narration rapide, ASR médiocre)
- 1:39 (couche FM bass, contexte) : Init, osc A « Digital default » [ASR ? = Default/Basic], warp poussé à fond → « crazy distorted sound » (warp type non clair) ; second warp « Square-ify » (retire les harmoniques impaires selon lui) ; Unison 3 [ASR ?] ; Sub triangle, octave -2 ; filtre « sharp » [ASR ?] avec ENV2 dessinée.
- 3:12 Matrix : ENV3 → Global Master Tune, ENV3 très courte = punch ; 3:55 FX Compressor en Multiband.
- 4:48 Patch pluck : MIDI Effect « Chord » (Ableton) sur une note → +15 demi-tons ; « Scale » (C mineur transposé en D) pour rester dans la gamme D mineur.
- 7:07 Osc : Analog, sine propre (préféré au sine « analog » plus sale), enveloppe ampli courte « plucky ».
- 7:22 ENV3 : sustain 0, release 0 (interp. « zero zero »), decay ≈ 20 ms → Master Tune via la Matrix = attaque synthétique (« transient designer »).
- 8:12 Hors Serum : transient designer tiers (Schaack [ASR ?]) pour plus de punch, petite room reverb ; 9:39 layer possible avec un one-shot ou des plucks Nexus.
- Genre : house (future house / deep house « EDX, Nora En Pure ») — plucks marimba percussifs en accords chromatiques house.
À vérifier à l'écran : 2:05 (type de warp « crazy distorted »), 2:45 (type de filtre et forme d'ENV2), 5:30 (réglages Chord/Scale), 7:15 (ADSR de l'ENV1 du pluck sine), 7:30 (quantité ENV3 → Master Tune).

### PL-05 How to make a Deep House PLUCK in Serum (FREE SERUM PRESET PACK) — The Preset Bros, 6:48, 2023-08-27, outil : Serum 1
URL: https://www.youtube.com/watch?v=Og2EaJ4wSFI
Technique(s) : pluck percussif « bambou creux » : sine + square à -5 st avec FM depuis le Sub, noise « Kick Attack » sur ENV3 ultra-courte, LFO1 en forme « plucky » → coarse pitch A/B + cutoff (le « knock »), mono, OTT/multiband pour le clic.
Transcription : oui (anglais, auto) — valeurs très précises dictées.
- 0:59 Osc A : Analog « BD Sine », semi -5, WT pos 0, warp FM (from Sub) 18 %, level 63.
- 1:18 Osc B : Basic Shapes, square, semi -5, Unison 2, WT pos « 4 », FM (from Sub) 36 %.
- 1:36 Sub : sine, octave 0, level 0 (sert seulement de modulateur FM).
- 1:49 Noise « Kick Attack » [ASR ? « kick attack 25 » = sample/numéro], phase 17, level 0 (ouvert par ENV3).
- 1:56 Osc B → filtre MG Low 24, cutoff au minimum, résonance 0, drive 37 %.
- 2:07 ENV1 : decay 433 ms, sustain ≈ 0, release 320 ms ; ENV2 : decay 298 ms, sustain ≈ 0, release 220 ms → cutoff, quantité 75.
- 2:37 ENV3 → level noise 68 ; decay 65 ms, sustain 0, release 13 ms.
- 2:53 LFO1 (forme « plucky », dessinée) → CRS (coarse) osc A et osc B à 45, → cutoff à 100 = le « knock ». 3:33 Mono activé.
- 3:39 FX : Compressor en Multiband (ajoute du clic) ; Hyper mix 15 ; Dimension size 14, mix 14 ; EQ : retrait des très aigus ≈ 6 kHz.
- 4:30 Reverb Hall : size 34, decay 3,4 s, low cut 30, high cut 63, mix 22.
- Genre : house (deep house selon le titre) — à noter : le morceau de démo est annoncé « in the style of Jack Ü » ; le pluck est un percussif mélodique type marimba/bambou utilisable en deep/tropical house (interp.).
À vérifier à l'écran : 1:00 (Osc A : WT exacte et mode de warp FM), 1:50 (nom exact du sample noise), 2:55 (forme du LFO1 et son mode trigger/env), 3:45 (réglages du multiband), 4:35 (valeurs reverb).

### PL-06 Créer un son de PLUCK à la manière de DEADMAU5 avec SERUM (niveau débutant) | SawUp — SawUp (Tana), 2:46, 2022-11-16, outil : Serum 1 (interp. : date et UI)
URL: https://www.youtube.com/watch?v=0Z2AQD2tRU4
Technique(s) : « tricher » sur le rythme : accords tenus en MIDI, et c'est un LFO1 en mode trigger (retrig à chaque note) sur le cutoff qui fabrique le « ploc » répété ; unison 4 voix pour épaissir ; reverb + delay ; finition cutoff / quantité de modulation / drive.
Transcription : oui (français, auto)
- 0:26 Définition : son percussif « cordes pincées » capable de jouer des accords d'accompagnement.
- 0:48 MIDI = simple suite d'accords tenus ; le rythme vient d'un LFO qui boucle.
- 0:59 Filtre activé (type non dit, défaut = MG Low 12 (interp.)), cutoff un peu baissé, LFO1 → cutoff « un peu mais pas trop ».
- 1:12 Forme du LFO1 redessinée (pente percussive, interp.) et mode Trig (« déclencher à chaque nouvelle note ») pour rester synchronisé.
- 1:28 Unison montée à 4 voix + léger detune.
- 1:42 Un peu de Reverb et de Delay ; 1:52 réglages finaux : cutoff, quantité LFO → cutoff, Drive du filtre.
- Genre : house (progressive / electro house façon deadmau5) — plucks d'accords rythmés par LFO, signature prog house.
À vérifier à l'écran : 1:00 (type de filtre et cutoff), 1:14 (forme et rate du LFO1, mode trig), 1:30 (detune exact), 1:55 (drive, quantité finale).

### PL-07 Serum Tutorial - Le Youth's PLUCK from his track 'Miraje' (Anjunabeats) — Abstrakt Music Lab, 9:51, 2021-11-09, outil : Serum 1
URL: https://www.youtube.com/watch?v=cI3iGdYasLo
Technique(s) : remake d'un pluck melodic house : saw par défaut + sine, noise piloté par ENV1, MG Low 18 très fermé + ENV2, second MG Low 18 en FX, ENV3 → « click » d'attaque ; velocity en Aux Source de ENV2 → cutoff ; deux macros automatisées (decay/cutoff et attaques) pour éviter un son statique.
Transcription : oui (anglais, auto) — valeurs précises dictées.
- 0:57 Osc A : WT par défaut (saw), level 47 % ; Osc B : sine, level 79 % ; Noise activé, level 0.
- 1:36 ENV1 : decay 840 ms, sustain -9,5 dB, release 542 ms ; ENV1 → level noise à 60.
- 2:11 Filtre MG Low 18 (corrigé à 8:01, pas 24), routé sur tout, cutoff 138 Hz, res 0, drive 29.
- 2:35 ENV2 : decay 1,05 s [ASR ? « 1.05 » sans le mot decay], sustain 63 [ASR ? unité], release 486 ms ; ENV2 → cutoff à 72.
- 3:05 FX Filter : MG Low 18, cutoff 35, ENV (FX) 35 [ASR ?], res 4 [ASR ? « resonant f4 »], drive 0, fat 19 %.
- 3:31 ENV3 : decay 1,64 s [ASR ?], sustain 0, release inchangé, courbe tirée au milieu ; ENV3 → (cutoff, interp.) à 10 = petite attaque.
- 4:06 Reverb : size 37 %, decay 5,4 s, low cut 35, high cut 24, spin/spin depth 0, wet 41 %.
- 4:35 EQ : low cut Q 44, fréquence 538 Hz ; high shelf 2055 Hz, Q 44, +4 dB.
- 5:12 Delay 1/8 – 1/8, freq 816 Hz, Q 0,8, mix 36 %.
- 5:59 Velocity → Aux Source de la ligne ENV2 → cutoff (notes douces plus sourdes), quantité un peu montée ; master 76 %.
- 7:30 Macro 1 : → level osc A 40 [ASR ? « 240 »], → decay ENV1 38, → decay ENV2 17, → cutoff 39 ; Macro 2 : → attack ENV1 20, decay ENV1 20, attack ENV2 30, attack ENV3 30 ; les deux automatisées par note.
- Genre : house (melodic / progressive house, Anjunabeats) — pluck mélodique très automatisé.
À vérifier à l'écran : 2:40 (ENV2 : decay/sustain exacts), 3:10 (FX filter : env, res), 3:35 (cible de l'ENV3), 6:08 (ligne Matrix velocity → aux source), 7:35 (valeurs macro 1).

### PL-08 How to make AFRO HOUSE PLUCKS — Sabo Limit, 8:59, 2024-02-28, outil : Serum (1, interp. : UI « Analog > Basic Mg », Hyper/Dimension)
URL: https://www.youtube.com/watch?v=q81yFaEkIYQ
Technique(s) : deux plucks saw afro house : (1) saw + enveloppe pluck → cutoff + bright white noise sur macro, chorus/delay/reverb ; (2) WT « Basic Mg » avec LFO non synchronisé 0,7 Hz en trigger → WT position (mouvement), second osc unison pour la largeur.
Transcription : oui (anglais, auto)
- 0:30 Pluck 1 : ENV1 sur la saw par défaut « plucky », un peu de sustain et de release ; 0:46 filtre + ENV → cutoff ; 0:58 WT remplacée par Basic Shapes position 2 (saw).
- 1:07 Noise « Bright White » ; ENV → level noise (bas) ou Macro 1 → level noise (à automatiser en build-up).
- 1:50 FX : Chorus, Delay, Reverb (« ce qui fait vivre le pluck ») ; EQ low cut ; Hyper/Dimension un peu ; type de filtre change le caractère ; noise routé au filtre possible.
- 2:55 Macros sur les mix d'effets (ex. delay qui monte dans le temps).
- 4:09 Largeur : Unison (effet flanger) ou 2e saw routée au filtre ; 4:37 ADSR : sustain bas = note qui disparaît même tenue.
- 5:12 Pluck 2 : Analog > « Basic Mg » [ASR ? = Analog_BD/Basic Mg], ENV → cutoff passé en unipolaire (Shift+Alt), petite attaque, bright white noise.
- 5:58 LFO1 forme dessinée, BPM off, rate 0,7 (Hz), → WT position ; Trig ON (redémarre à chaque note) ; cutoff plus ouvert ; WT position ≈ 52.
- 6:41 Chorus, delay, reverb ; 6:59 osc B même WT, plus bas en niveau, unison augmentée, routé au filtre ; Hyper/Dimension « a tiny bit » ; EQ.
- Genre : house (afro house) — plucks saw rapides sur groove kick/perc/shaker + reese, démontrés en contexte.
À vérifier à l'écran : 0:35 (ADSR exact du pluck 1), 1:10 (quantité ENV → noise), 5:15 (nom exact de la WT), 6:05 (forme du LFO1), 7:05 (unison/detune de l'osc B).

### PL-09 How To Make PLUCKS Like EMPEROR - All I Ever Wanted | Serum Tutorial — DNB Academy (Paulo), 7:57, 2021-12-16, outil : Serum 1 (+ post-traitement Ableton/Kilohearts)
URL: https://www.youtube.com/watch?v=SFXQGvFEXbw
Technique(s) : WT maison à 2 frames (sine → sine « squarifiée » à la main dans l'éditeur d'harmoniques), morph Spectral entre les deux, LFO enveloppe → WT position pour le transient du pluck ; unison + random phase modulés ; LFO → gain du compresseur pour creuser la dynamique ; post : distortion Kilohearts (sine shaper), split chain avec reverb 100 % wet filtrée.
Transcription : oui (anglais, auto)
- 1:17 Init ; osc A sine ; 1:31 dans l'éditeur WT : 2e frame = sine « squarifiée » en équilibrant les harmoniques (onde quasi-carrée).
- 2:14 Morph « Spectral » entre les 2 frames ; LFO (forme pluck, interp.) → WT position = transient du pluck.
- 2:49 Unison ajoutée, detune baissé et modulé (même LFO, interp.) ; random phase à 0 et modulée aussi [ASR ? « round face » = rand phase].
- 3:03 FX : Compressor, LFO similaire → gain du compresseur = gros pic transitoire puis niveau moyen bas (pour nourrir la distortion/transient shaper).
- 3:44 Post : distortion Kilohearts (« sine shaper » ; alternative Serum = Distortion Sine Shaper) puis baisse de niveau.
- 4:52 Audio Effect Rack en 2 chaînes : (1) son sec + petit high-pass ; (2) reverb 100 % wet, long decay, grande taille, puis EQ/filtre sur la reverb.
- 5:54 Optionnel : low-pass filter dans Serum, delays après le filtre.
- Genre : drum and bass (liquid / mélodique, intro de « All I Ever Wanted » d'Emperor) — pluck d'intro DnB.
À vérifier à l'écran : 1:40 (harmoniques de la frame 2), 2:30 (forme et rate du LFO → WT pos), 2:55 (quantités unison/detune/rand phase), 3:10 (LFO → gain compresseur), 5:15 (réglages reverb/EQ de la chaîne 2).

### PL-10 How To Make PLUCKS Like MADUK - FIRE AWAY | Serum Tutorial — DNB Academy (Paulo), 5:09, 2022-06-16, outil : Serum 1
URL: https://www.youtube.com/watch?v=rBesNtuIZz0
Technique(s) : saw unison 9 (voix centrale juste), Low 24 avec enveloppe pluck à plage de modulation précise, Hyper + reverb + multiband, EQ dont la fréquence suit le Note number (peak « expressif » qui suit la mélodie).
Transcription : oui (anglais, auto)
- 1:09 Init saw ; Unison 9 voix (nombre impair = une voix centrée juste).
- 1:19 Filtre Low 24 ; enveloppe (ENV2, interp.) → cutoff, courbe modulée [ASR ? « another fold into the curve »] ; forme pluck dessinée.
- 1:37 Cutoff ≈ 142 Hz, quantité de modulation 46 (il insiste : valeurs nécessaires sinon « trop crazy »).
- 2:02 FX : Hyper/Dimension, Reverb, Compressor multiband ; 2:12 EQ avec Note (keytrack) → fréquence d'un peak = résonance qui suit les notes ; EQ placé avant le compresseur.
- 3:04 Delay ajouté ; réglages clés à retoucher : filtre (tension), EQ (expression), plage de modulation du filtre.
- Genre : drum and bass (liquid, Maduk) — pluck mélodique de liquid.
À vérifier à l'écran : 1:25 (ADSR de l'enveloppe pluck), 1:40 (cutoff/quantité exacts), 2:15 (fréquence, gain, Q du peak EQ et quantité Note → freq), 2:08 (réglages Hyper/Reverb/multiband).

### PL-11 How to make BASS PLUCKS Like MADUK - GOT ME THINKING | Serum Tutorial — DNB Academy (Paulo), 6:52, 2021-03-19, outil : Serum 1
URL: https://www.youtube.com/watch?v=HfgvhVFVyBA
Technique(s) : « dancefloor pluck » grave (limite basse) : 2 squares -1 oct dont une +7 st (quinte), sub +, unison ; LFO1 en mode Envelope → cutoff (unipolaire, courbe), LFO2 en Envelope « falling » → Global Master Tune = clic ; distortion pré-filtre en high-pass (ne distord qu'au-dessus de 400 Hz) ; multiband release max.
Transcription : oui (anglais, auto)
- 1:03 Osc A et B : square ; A -1 octave ; B -1 octave et +7 demi-tons (ou -5 « as you prefer ») ; 1:35 Sub ajouté (+ octave [ASR ? « to octave sound »]) en Direct Out.
- 1:42 Unison ajoutée, detune baissé ; mix des couches : plus bas sur la couche grave, quinte remontée.
- 2:00 Filtre (type non dit) sur A et B ; LFO1 → cutoff, LFO1 en mode ENV (one-shot), forme pluck dessinée ; rate passé à 1/2 bar [ASR ? « bring the red to have a bar »] pour garder une queue.
- 2:37 Cutoff : modulation passée en unipolaire (Shift+Alt+clic), courbe abaissée ; résonance au goût.
- 3:14 Matrix : LFO2 → Global Master Tune, quantité forte, forme descendante, mode ENV, unipolaire = clic d'attaque (quantité baissée ensuite à 5:02).
- 3:51 FX Distortion en mode PRE, filtre High-pass ≈ 400 Hz → ne sature que le haut ; mix baissé.
- 4:20 Compressor multiband, release au max (« pas de queue gênante ») ; reverb légère ; EQ (bas-médium remonté à 5:10) ; son allongé ensuite.
- Genre : drum and bass (liquid / dancefloor, Maduk) — pluck bas-médium joué en riff ; à la frontière pluck/basse, retenu car traité comme pluck mélodique.
À vérifier à l'écran : 1:20 (niveaux et voix d'unison), 2:20 (forme et rate du LFO1), 2:50 (cutoff/type de filtre), 3:25 (forme LFO2, quantité vers Master Tune), 4:05 (réglages distortion).

### PL-12 Serum Tutorial - Seven Lions 'Don't Leave' Progressive Pluck — SynthHacker (Tom), 5:48, 2016-02-29, outil : Serum 1
URL: https://www.youtube.com/watch?v=0yxEwFiGxjc
Technique(s) : pluck « trance/progressive » à 2 couches : osc A 1 voix (centre mono) + osc B une octave au-dessus en unison 7 (large) ; ENV1 pluck aussi sur le cutoff d'un MG Low 24 fermé + drive ; noise passe-haut ; Hyper/Dimension + reverb.
Transcription : oui (anglais, auto)
- 2:08 Osc A : octave par défaut (saw par défaut, interp.), 1 voix ; Osc B : +1 octave, Unison 7, detune un peu baissé — explication : centre mono solide + couche élargie stéréo.
- 3:10 ENV1 : sustain un peu baissé, decay plus court, attaque légèrement montée (moins dure), release ≈ 150 ms.
- 3:30 Filtre MG Low 24, cutoff au minimum, A + B + noise routés ; noise « JP106 High Pass » [ASR ? « j106 highp pass »] (sans bas mou) ; ENV1 → cutoff, quantité un peu réduite.
- 4:08 Drive du MG filter poussé = saturation « analog » (penser à baisser le master ensuite).
- 4:34 FX : Hyper/Dimension, mix baissé ; Reverb : size augmentée, mix réduit, high cut et low cut un peu remontés.
- Genre : dubstep (famille melodic dubstep : Seven Lions) — attention, le morceau « Don't Leave » est décrit par le tuteur comme trance / progressive house ; pluck utilisable dans les intros/breaks melodic dubstep (interp.).
À vérifier à l'écran : 2:15 (WT des oscillateurs), 3:15 (ADSR exact de l'ENV1), 3:40 (nom exact du noise), 4:02 (quantité ENV1 → cutoff et drive), 4:40 (réglages reverb).

### PL-13 Serum tutorial - How to make a pluck Future Bass (Illenium, Nurko style) — Drayen, 5:36, 2021-06-05, outil : Serum 1
URL: https://www.youtube.com/watch?v=Fmu5oVmcRkM
Technique(s) : pluck d'arp « Illenium / Nurko » : saw simple + saw unison 7 (+1 octave), ENV1 pluck sur l'ampli et sur le cutoff d'un MG Low 24 (pente raide préférée au 12 dB), noise ; macro → cutoff automatisée en cloche ; Hyper/Dimension, OTT optionnel ; compresseur + Utility dans le DAW pour tenir le niveau quand le filtre s'ouvre.
Transcription : oui (anglais, auto ; le titre affiché était auto-traduit en français)
- 0:52 Init ; osc A saw (peu touché) ; osc B saw, Unison ≈ 7, detune ajusté ; 3:27 osc B (interp.) +1 octave.
- 1:13 ENV1 : attaque ≈ 3,8 ms [ASR ? « 3.8 attack »], un peu de sustain, decay/release ajustés « autour de là ».
- 1:39 Filtre activé pour B + noise ; 2:04 MG Low 24 (démontre que le 12 dB sonne moins bien) ; ENV1 → cutoff, cutoff placé assez bas.
- 2:44 Macro → cutoff (pour l'automation) ; 3:04 FX : Hyper/Dimension, reverb optionnelle.
- 3:34 Post : OTT optionnel ; EQ low cut vers les centaines de Hz, léger retrait des aigus.
- 4:01 Automation de la macro en forme de cloche (courbe adoucie avec Alt/Option) ; compresseur 4:1, attack et release rapides, threshold ≈ -12,7 dB + Utility automatisé pour le volume.
- Genre : dubstep (famille melodic dubstep / future bass : Illenium, Nurko) — arp pluck typique des intros/drops melodic bass. Classement dubstep par défaut faute de mieux (interp.).
À vérifier à l'écran : 1:15 (ADSR exact de l'ENV1), 2:12 (position du cutoff et quantité ENV1), 2:50 (plage de la macro), 3:05 (réglages Hyper/Dimension), 4:16 (courbe d'automation).

### PL-14 Use THIS Trick for Pluck Bass in Modern Drum and Bass | Ableton Serum tutorial — STRANJAH, 16:13, 2021-04-09, outil : Serum 1 (+ automation Ableton)
URL: https://www.youtube.com/watch?v=sjnaIDbanVo
Technique(s) : « pluck repeater » : la répétition vient d'un LFO1 en Trig, non synchronisé (Hz), forme pluck → level A/B + cutoff + drive de distortion ; le rate du LFO est automatisé dans Ableton (accélère/ralentit) ; pitch bend en fin de note. Registre grave (C0–C1) : pluck-basse, limite de la catégorie.
Transcription : oui (anglais, auto)
- 1:16 Définition : attaque rapide et dure + decay court ; ici pluck répété par LFO.
- 1:56 WT conseillées riches en harmoniques (Crush Wub, Mario, Cream, Analog PWM/Saw/Square, Acid, Filthy) ; choix : osc A « Saw Rounded » (WT pos montée), osc B « Square Saw » [ASR ? « square saw word »] +2 octaves +7 demi-tons (quinte).
- 3:34 ENV1 : attaque ≈ 5 ms si clic.
- 3:52 LFO1 dessiné en « aile » (attaque dure, chute rapide), pente ajustable, un peu de sustain au début → level A et B (level bas + quantité LFO haute = pluck plus marqué).
- 4:56 LFO1 : Trig ON, BPM OFF (rate libre, transitions douces).
- 5:46 Filtre MG Low 12, A + B routés, cutoff baissé, LFO1 → cutoff.
- 6:27 FX : Distortion drive ≈ 80 % puis réduit, LFO1 → drive (attaque plus dure) ; Reverb avec low cut fort, mix bas (raccourci assumé ; idéalement split hi/lo).
- 9:05 Notes C0–C1 ; rates en Hz : 5,6–5,7 (croche), 3,8 (croche pointée), 2,8 (noire) au tempo du morceau (calculateur BPM → Hz).
- 10:40 Automation Ableton (mode « show automation ») du rate LFO1 : départ rapide (≈ 5,8) puis ralentissement ; accélération sur la 2e moitié d'une note longue ; 13:30 pitch bend +2 st en fin de note (range ±2 ; 12 testé, trop fort).
- Genre : drum and bass (moderne / dancefloor, réf. Disrupta, Annix) — pluck-basse « repeater ».
À vérifier à l'écran : 2:20 (noms exacts des WT et positions), 4:05 (forme du LFO1), 4:30 (quantités LFO → levels), 6:35 (type de distortion), 12:15 (courbe d'automation du rate).

### PL-15 Serum Tutorial - Beautiful Au5 Style Pluck — Celune, 6:20, 2022-04-21, outil : Serum 1
URL: https://www.youtube.com/watch?v=00_DFR9c9SA
Technique(s) : pluck « Au5 » : sine (Basic CGV) avec warp Bend+ modulé par LFO1 (mouvement subtil), distortion Downsample dosée finement, attaque fabriquée par un sample noise « Guitar Mute 2 » en one-shot + keytrack (au lieu d'une enveloppe de pitch), couche saw unison 7 filtrée, enveloppe décroissante, ping-pong delay.
Transcription : oui (anglais, auto)
- 1:30 Osc A : WT « Basic CGV » (≈ sine) ; LFO1 → warp A, mode « Bend + », plage ≈ 20 (mouvement subtil).
- 2:00 Distortion mode Downsample, drive exactement 22, mix ≈ 30 (« 1 % de différence change beaucoup »).
- 2:23 EQ en mode high-pass pour retirer le bas.
- 2:53 Noise : Attacks > Misc > « Guitar Mute 2 », One Shot ON, Pitch tracking ON → transitoire plus marqué.
- 3:30 Osc B : saw, Unison 7, detune ≈ 0,04 ; filtre activé uniquement pour B, cutoff ≈ milieu.
- 3:54 Enveloppe (volume) en décroissance douce ; 4:01 Delay ping-pong ; 4:21 EQ retouché pour coller à la cible.
- Genre : dubstep (melodic dubstep / melodic bass, style Au5, pris d'un remix d'Au5) — pluck d'avant-break.
À vérifier à l'écran : 1:40 (forme et rate du LFO1), 2:05 (réglages distortion), 3:05 (niveau du noise), 3:40 (cutoff/type du filtre), 3:56 (forme de l'enveloppe et cible).

### Écartés
- ORinPlsdjYw « How To Make a Deep House LEAD PLUCK Like Meduza in Serum » (Aspen Lyon) : pas de transcription disponible, rien de vérifiable sans l'écran.
- GuCgYZNzkH0 « Basic Melodic Dubstep Pluck Serum tutorial » (TheOni) : pas de transcription.
- 90utS63gKdM « How to make a Dubstep pluck in Serum » (TheOni) : pas de transcription.
- I8I2kN1jC1A « How to make Future House (Serum Tutorial - Pluck) » (Function Loops) : vidéo muette (transcription = [Musique] seulement).
- 9LfeBZ0K6xg « How To Make EDX, JLV, Nu Aspect Style Pluck In Serum » (Sonance Sounds) : presque pas de narration, ASR inexploitable.
- zfyUWN8eWW4 « How to make ILLENIUM style Ambient Pluck » (REVERFALL) : fait dans Vital, pas Serum.
- xboswd-Ci8k « DUBSTEP PLUCK TUTORIAL + PRESET » (SJT) : fait dans Harmor, pas Serum.
- tA8j4ScNR5A « How To Make BASS PLUCKS like SHOCKONE - ALCHEMY » (DNB Academy) : quasi identique à PL-11 (squares, -2 oct +7 st), même chaîne : doublon.
- Vu7b_9ydxR4 « MELODIC HOUSE with LFO Plucks like NOHR "You" » (PRODUCER NOTES) : visite guidée d'un projet de 28 min, pas une construction pas à pas ; le même pluck LFO est construit de zéro en PL-03.
- dfQV4WSsOXA « 9 DnB Sounds Every DnB Producer Should Know » (Arc Nade) : chapitres basses seulement, aucun pluck.
- 39JKCKM_m9s (How to DNB, « bass plucks » très épais, 26 min) : non ouvert, il s'agit de basses.
- Non ouverts car hors sujet ou de faible valeur : vidéos de packs de presets (HNPcrFnt8Ec, M0W0LHzxCrs, 4yns6odr_vk, T-60PinUm-w…), Shorts de moins d'1 min (dO4JcwZT_fg, Q-Gd-IF6hMg, gen8bMx-JRs, haRLBQx1C20, tLDq_LGwrtg…), Massive / DIVA (aSJBqmQSzS4, i3Vfp6rXnb4), sons de type lead ou chord (M5qxu--dWp4, 66RrYjW5Q24, keZRCsFvLFM « chord pluck », laissé à l'agent accords).
- Non retenus pour garder des chaînes variées (The Sound Design Channel / PML a plus de 10 tutos de plucks Serum, utiles en réserve) : NgPX5wJnWzg (afro, &ME), iok0qJfmfPY (Serum 2, saw pluck), QWLuHDbBVok, WOxf3y3-btQ, AuR9RI0bxIE, 4VPi_5tSgZg, lNjWPd7ZLEI, _xcI1KrdzY0, E5AIcWnlkrQ, q_F-ux5Rtgo, EhHHvyE7h5Q. Autres réserves possibles : D4LNcFjsFPY et rnS7exuVDLk (Furcloud), VrhKCWoV2DQ et fJ7-2TUKxLw (Spaces), NZ166Lks890 / iuFyjTlC1U4 / Ady_w1Zt0VE (Hive, FR), 6GKyfazH8W0 (Rocket Powered Sound, future bass/house), PMb5yKMYjLk (Rocket Powered Sound).

### Manque
- 15 vidéos trouvées sur 15. Répartition : 8 house, 4 DnB, 3 dubstep, soit exactement la cible.
- House : la deep, la melodic, l'afro, la progressive et la future house sont couvertes. Aucun vrai tuto de **pluck tech house** dans Serum n'a été trouvé : les résultats sont des basses ou des leads, et OzsGzJYWwak « Tech House Pluck Bass », 2:14, 85 vues, est une basse.
- DnB : 3 des 4 vidéos viennent de DNB Academy (même tuteur). Hors de cette chaîne, la seule alternative sérieuse trouvée est STRANJAH (PL-14). PL-11 et PL-14 sont des **plucks-basses** au registre grave, à la limite de la catégorie. Aucun pluck neuro ou jump-up trouvé.
- Dubstep : les vrais tutos de plucks Serum sont rares. PL-12 (Seven Lions) est un pluck progressive/trance d'un artiste melodic dubstep. PL-13 relève plutôt de la future bass (Illenium). Seul PL-15 (Au5) est clairement melodic dubstep. Aucun pluck riddim trouvé.
- Langue : un seul tuto est en français (PL-06, SawUp). Plusieurs titres apparaissaient en français mais étaient auto-traduits : les vidéos sont en anglais (Drayen, Abstrakt, PRODUCER NOTES…). Il reste des tutos FR de la chaîne Hive (NZ166Lks890, Ady_w1Zt0VE), non ouverts car le genre n'est pas précisé.
- Serum 2 : seulement 2 vidéos sur 15 (PL-02, PL-03). On peut en ajouter facilement depuis la réserve The Sound Design Channel (iok0qJfmfPY, QWLuHDbBVok, WOxf3y3-btQ).

# Hook

## HOOK — hooks / riffs de drop / « signature synths » designés dans Xfer Serum (préfixe HO)

Sélection : 15 vidéos (8 house, 4 DnB, 3 dubstep), 14 EN + 1 FR. Toutes vérifiées sur la transcription YouTube (panneau Transcription, sous-titres auto sauf HO-14 manuels). Valeurs = ce qui est DIT ; « (interp.) » = mon interprétation ; [ASR ?] = reconnaissance vocale douteuse. Aucun ID n'apparaît dans LEAD.md, PLUCK.md, /tmp/outputs/etudes-videos-chrome.md ni chops/deja_vus.txt. Durées et dates lues dans ytInitialPlayerResponse (videoDetails / microformat).

---

### HO-01 How To - Fisher "Losing It" Drop Remake / Serum Tutorial [FREE DOWNLOADS] — XLNTSOUND, 16:04, 2019-08-14, outil : Serum 1 (+ Ableton : OTT, EQ Eight, Auto Filter, delay)
URL: https://www.youtube.com/watch?v=XUgwEvD4SB4
Technique(s) : unison x2 oscillateurs dont le level est piloté par un LFO dessiné (« double shark fin ») + bruit, filtre MG Low 12 très fermé à fort « Fat », EQ interne en notch-boost, double OTT en post.
Transcription : oui (anglais, auto)
- 0:49–1:56, 3:05–3:40, 10:24–11:36 : passages promo du pack, sans sound design.
- 2:44 le son étudié = le « horn lead all Serum » du drop (la basse est une guitare + sub).
- 3:47 init A et B. Osc A : unison 7, detune ~0.08, phase identique, random au max, level à 0 (sera modulé). Osc B : unison 7, detune ~0.41, random au max, level baissé.
- 4:56 Noise « bright white(s) » [ASR ?], level baissé.
- 5:13 LFO1 dessiné en « double shark fin » → levels A, B et noise (≈ au max chacun) ; 6:00 noise level 35 ; Osc B « 3100 » [ASR ?].
- 6:18 Osc B octave relevée (« up … 2 » [ASR ?]), fine -15, puis « +1/2 » [ASR ?].
- 6:40 Filtre MG Low 12, cutoff ~40 Hz, résonance 0, drive ~30 %, fat 92 %, mix max ; LFO1 → cutoff ; 7:19 LFO passé en mode Envelope.
- 7:48 FX EQ : bande gauche 155 Hz, Q ~35 %, +8.1 dB (« nice little mid boost ») ; bande droite 2939 Hz, Q 46 %, +1.7 ; puis filtre FX cutoff 714 Hz, res/drive/fat à 0, MG Low 6.
- 9:53 LFO1 aussi → fine (bipolaire, ~37) et → cutoff ; « 30 steps » [ASR ?] → plus rebondissant.
- 11:38 post Ableton : OTT (mids et highs expandés, output +6.9, dry/wet 55 %) → EQ (low cut, creux à ~310 Hz « là où est la boue », aigus réduits) → 2e OTT à 43 % (mids up, output des highs baissé) → EQ low cut → 2 Auto Filter + delay « tonal » automatisés, rack avec macros dans le téléchargement.
- Genre : house, tech house (Fisher « Losing It », hook du drop).
À vérifier à l'écran : 4:00 (unison/detune A et B), 5:13 (forme du LFO « shark fin »), 6:40 (valeurs filtre), 7:48–8:48 (EQ FX), 11:38 (réglages OTT).

### HO-02 The Best FISHER 'Losing It' Horn Tutorial on the Internet — Sam Smyers, 6:24, 2022-04-01, outil : Serum 1 (+ Ableton Utility, Pedal, EQ Eight)
URL: https://www.youtube.com/watch?v=QMoQo-Irulw
Technique(s) : même horn que HO-01, approche différente : deux wavetables analog + FM from B et Sync modulés par un LFO en mode enveloppe, filtre MG Low 6 drivé, éclaircissement lent sur la mesure.
Transcription : oui (anglais, auto)
- 0:39 Osc A wavetable analog « BS Subies » [ASR ?] ; Osc B « BS Filthy » ; 0:52 unison A 8, B 6 ; detune baissé ; level B baissé.
- 1:07 Warp FM from B + Sync (« just a little bit »).
- 1:20 ENV1 : attaque lente « comme un cor » + release.
- 1:43 Filtre sur A et B, MG Low 6, drive monté, résonance baissée, Fat un peu, cutoff bas ; ENV1 → cutoff.
- 2:23 LFO1 en mode Envelope, rate 1/4 ; ENV1 → WT position en négatif ; LFO1 → WT position + FM from B (grain au début de la note).
- 3:23 FX : Distortion (drive up), Chorus (LPF du chorus coupé, depth un peu baissée), Reverb avec low cut, EQ low cut.
- 4:17 Ableton : Utility (graves en mono), Pedal sur Overdrive (original très distordu), EQ Eight anti-brillance.
- 5:07 LFO2 en mode Envelope, rate « bar » → cutoff : le son s'éclaircit pendant la tenue de la note.
- Genre : house, tech house (Fisher).
À vérifier à l'écran : 0:39–1:05 (noms exacts des wavetables), 1:20 (ADSR ENV1), 2:23–3:16 (forme LFO1 et montants), 5:07 (montant LFO2).

### HO-03 JOYRYDE "I WARE HOUSE" SERUM LEAD TUTORIAL 🔥 (Free Preset) — Rocket Powered Sound, 7:40, 2017-05-12, outil : Serum 1
URL: https://www.youtube.com/watch?v=vp3-XWE31Qo
Technique(s) : triangle en FM par un carré + modulation d'amplitude dessinée, puis filtre Low 12 à forte résonance avec keytracking (tonalité « screech » qui suit les notes), distorsion Tube.
Transcription : oui (anglais, auto)
- 0:09 appelé « main bass » du drop, titré « lead » : c'est le riff principal du drop.
- 1:13 Osc A Basic Shapes, triangle ; 1:51 Warp FM from B ; level Osc B baissé à ~37 % (2:10) ; Osc B Basic Shapes → carré.
- 2:32 modulation d'amplitude imitant l'original : LFO dessiné en mode Trigger, rate 1/2 (2:53) (→ level, interp.).
- 3:06 FX Distortion Tube.
- 3:43 Filtre Low 12, résonance haute → tons stridents (comparé au « Nuclear » lead de Zomboy) ; 4:34 keytracking ON, puis cutoff accordé à l'oreille ; 4:51 la distorsion fait ressortir la résonance (sans elle, l'effet disparaît).
- 5:37 Hyper/Dimension placé APRÈS la distorsion ; Hyper ~9 % ; Dimension size ~2 %, mix 68 puis 46 ; 6:15 reverb mix bas.
- 6:27 variantes : Sync, autres formes d'onde.
- Genre : house, bass house (Joyryde).
À vérifier à l'écran : 2:32–2:57 (forme LFO et cible), 3:43–4:46 (cutoff/res/keytrack exacts), 5:56–6:10 (Hyper/Dimension).

### HO-04 How to Make Beltran "Passion" Lead in Serum 2 [Sound Design Tutorial] — Sam Smyers, 6:26, 2026-05-16, outil : Serum 2 (+ Ableton Utility, Kickstart)
URL: https://www.youtube.com/watch?v=vlCeajFE_j8
Technique(s) : son « funky » obtenu par Sync modulé par une enveloppe sur un carré et une scie, voicing mono, nouveau curseur Serum 2 de lissage de wavetable, panoramique automatisé avant la reverb.
Transcription : oui (anglais, auto) ; chapitres dans la description (0:38 Panning, 1:55 Sync, 2:30 Oscillator…)
- 0:38 panoramique automatique via Utility placé AVANT la reverb (sinon la reverb est aussi pannée) ; reverb ~5 % (1:43) ; Kickstart (sidechain).
- 1:57 le caractère vient du Sync modulé par une enveloppe.
- 2:28 voicing Mono ; ENV1 release ~7 ms ; Osc A carré oct -1 ; 2:55 Osc B scie, fine légèrement décalé, oct -1 ; niveaux différents.
- 3:15 Osc A warp Sync ; nouveau curseur Serum 2 qui lisse les bords de la wavetable (moins = plus agressif).
- 4:06 ENV2 → Sync A 27 % ; 4:34 ENV2 → Sync B 15 % ; fade du warp désactivé ; ENV2 decay long.
- 5:07 Chorus mix ~20 % ; 5:50 conseil : plus de chorus/flanger/phaser pour un style électro années 80.
- Genre : house, tech house (Beltran, vague tech house brésilienne).
À vérifier à l'écran : 2:30–2:45 (ADSR ENV1), 3:20 (curseur de lissage Serum 2), 4:06–4:47 (forme ENV2, montants 27/15 %), 5:12 (chorus).

### HO-05 TUTO HOUSE RAVE STAB Sur SERUM - Tout ce que vous devez savoir — Strob Studio Mixing & Mastering, 12:15, 2023-11-01, outil : Serum (version non précisée à l'oral ; Serum 1 vraisemblable, date 2023)
URL: https://www.youtube.com/watch?v=aJzVm6QrQ8E
Technique(s) : méthode en 4 « clés » pour un rave stab house : accord sur 2 oscillateurs, sources Juno avec random phase à 0, enveloppe de pitch sur le Master Tune, noise, filtre LP18 percussif, distorsion.
Transcription : oui (français, auto)
- 1:26 init sur une piste dupliquée, sidechain au gain pour le contexte.
- 2:00 clé 1 : le stab est un accord (rave stabs historiquement samplés d'accords) → 2e oscillateur ; choix du demi-ton par rapport à la note racine, testé « -2 / +10 » (3:09), selon la basse.
- 3:27 source : wavetables Juno (carré Juno, DCO) — « les goûts et les couleurs ».
- 4:06 random phase à 0 (son identique à chaque note, comme un sample) ; un peu d'unison pour la stéréo, compromis sur le random (5:22).
- 5:27 clé 2, le pitch : detune indépendant par oscillateur, puis ENV → Global Master Tune, plage 12 (une octave), enveloppe en mode « 1 bar » (pour agir sur la note longue de fin de pattern), bipolaire, léger mouvement au début ; 7:56 attaque un peu adoucie.
- 8:28 clé 3 : noise (indispensable pour le côté old school).
- 8:41 clé 4 : filtre Low Pass 18, enveloppe percussive → cutoff ; 9:25 astuce : limer la fondamentale dans le filtre plutôt qu'avec un EQ.
- 9:55 FX distorsion ; 11:12 filtre qui coupe les aigus (côté grunge/vintage) ; flanger pour colorer ; petit EQ.
- Genre : house (rave stab house / UK rave), le stab porte le hook.
À vérifier à l'écran : 2:51–3:09 (semitones des oscillateurs), 3:44 (nom exact de la wavetable Juno), 6:00–6:40 (forme de l'enveloppe de pitch), 8:56–9:25 (enveloppe filtre), 10:11 (type de distorsion).

### HO-06 Recreating Today's Hottest Tech House Synth [Serum Tutorial] — Tech House Market, 3:17, 2024-06-10, outil : Serum 1
URL: https://www.youtube.com/watch?v=EfRPAfD7CxA
Technique(s) : deux oscillateurs en intervalle (accord de 2 notes), enveloppe sur cutoff, mono legato, Dimension, delay ping-pong.
Transcription : oui (anglais, auto)
- 0:00 synthé attribué à « Chris tzy » [ASR ?, Chris Lorenzo ou Chris Lake ?], qui utiliserait un Roland ; MIDI d'« All Night Long ».
- 0:28 Osc A -2 octaves ; Osc B -1 octave ; « add a seventh » mais réglé à -5 demi-tons [incohérence à l'oral : -5 = quarte/quinte, pas une septième].
- 0:59 filtre sur A et B, ENV → cutoff, enveloppe façonnée, release ; 1:20 Mono Legato ; un peu plus de résonance.
- 1:33 FX Dimension (Hyper coupé) — attention, sinon « digital » ; EQ : aigus coupés, graves boostés ; delay « 18 » [ASR ?] en ping-pong ; reverb Plate élargie.
- Genre : house, tech house.
À vérifier à l'écran : 0:46 (semitones réels d'Osc B), 1:02–1:17 (ENV et filtre), 2:09 (réglage delay), 2:22 (reverb).

### HO-07 How to Make a Chris Lake Style Lead in Serum (Step-by-Step) — Sound Factory, 2:55, 2026-03-31, outil : Serum 2 (oscillateur C mentionné ; presets « for Serum 2 » dans la description)
URL: https://www.youtube.com/watch?v=ChK-tMJGgDE
Technique(s) : scies douces + sub, LFO rapide sur le fine d'A, LFO sur le Global Master Tune, départ à -12 demi-tons, mono.
Transcription : oui (anglais, auto)
- 0:15 sous-oscillateur une octave plus bas en scie ; Osc A scie « plus douce », unison 2 voix ; 0:31 Osc B scie (« 80 mother » [ASR ?]) ; 0:41 noise activé.
- 0:45 Filter 1 sur A, B et C, cutoff ouvert, drive.
- 0:58 LFO2 → fine d'Osc A, rate 1/64 (modulation rapide).
- 1:10 LFO1 → Global Master Tune (Matrix).
- 1:27 Mono ; un peu de release.
- 1:36 FX : EQ low cut, compresseur multibande, delay, reverb.
- 2:17 pitch réglé pour partir de -12 demi-tons ; ajustement final du montant LFO2 → fine.
- Genre : house, tech house (Chris Lake).
À vérifier à l'écran : 0:19 (wavetable « plus douce »), 0:33 (nom wavetable Osc B), 1:13–1:27 (forme/rate LFO1), 2:17 (cible exacte du -12 st).

### HO-08 How to Make the Lead from Dom Dolla "Miracle Maker" [Free Serum Preset Download] — Sam Smyers, 2:09, 2022-09-27, outil : Serum 1 (+ iZotope Trash)
URL: https://www.youtube.com/watch?v=2QXVJiNbimA
Technique(s) : scie à -1 octave et -7 demi-tons + carré à +1 octave, distorsion asymétrique à fond, compression multibande, distorsion externe.
Transcription : oui (anglais, auto)
- 0:07 analyse du preset : scie + carré ; FX Distortion, EQ, compresseur multibande.
- 0:23 Osc A Basic Shapes scie, oct -1, -7 demi-tons ; 0:30 Osc B (analog) Basic Shapes carré, oct +1.
- 0:38 FX Distortion Asym, drive au max ; EQ coupe les graves ; 0:53 compresseur multibande ; reverb repoussée.
- 1:12 iZotope Trash preset « Crunchy Taco » ; EQ qui arrondit les aigus ; reverb « très mono ».
- Genre : house, tech house (Dom Dolla).
À vérifier à l'écran : 0:28 (oct/semi Osc A), 0:42 (drive/mix distortion), 0:55 (réglages multibande).

### HO-09 How Sub Focus made that "WOW WOW" lead in Solar System - Serum Tutorial — How to DNB, 13:14, 2024-08-04, outil : Serum 1 (+ Serum FX comme visualiseur)
URL: https://www.youtube.com/watch?v=HYG4joE4j70
Technique(s) : « wow » vocal par filtre multi Band+Notch dont les deux fréquences se croisent sous un même LFO, montée de pitch par LFO unipolaire, 2 scies en stéréo désaccordées.
Transcription : oui (anglais, auto) ; pub 8:27–9:16
- 1:35 2 scies Basic Shapes (versions digitales, les plus riches) ; noise « AC Hum » à bas niveau pour la chaleur.
- 2:20 A et B légèrement différents, un pané à gauche, l'autre à droite ; unison A 16, B 8, detunes bas et différents.
- 3:23 LFO raide → coarse pitch de A et B, unipolaire, -10 (le son monte comme « wow ») ; 8:02 pente rendue plus raide.
- 4:03 filtre Multi « BN » (Band + Notch) : LFO de forme → cutoff (bande), même LFO inversé → 2e fréquence (notch) ; les deux bosses doivent presque se toucher, résonance un peu ; 8:19 filtre aussi activé sur B.
- 5:24 fine A vers le haut, B vers le bas (valeurs arbitraires différentes).
- 5:44 Distortion Stomp Box, drive modulé par le LFO (augmente dans le temps) ; Compressor (gain) ; Reverb prudente + low cut.
- 6:51 EQ : bande Sweep en cloche, fréquence modulée par le LFO des graves vers les médiums ; shelf aigus à goût ; Delay avec temps L/R différents, filtré sur les médiums.
- 9:16 mix du filtre réglé pour garder un peu d'aigus.
- 9:50 astuce : Serum FX (Note Latch + noise) pour visualiser un filtre « PP12 » (double pic), puis recopier cutoff/res/2e pic dans le patch.
- Genre : DnB dancefloor (Sub Focus « Solar System »).
À vérifier à l'écran : 2:43 (detunes A/B), 3:40 (forme LFO pitch), 4:40–5:15 (positions band/notch, résonance), 10:55–11:40 (valeurs PP12 recopiées).

### HO-10 How to make STABS like CULTURE SHOCK - BUNKER | Serum Tutorial — DNB Academy (Paolo), 6:45, 2021-03-12, outil : Serum 1 (+ Ableton Erosion, Overdrive)
URL: https://www.youtube.com/watch?v=WR4XyJ12UkE
Technique(s) : FM sinus/sinus avec wavetable B dessinée par harmoniques (fondamentale, quinte, 3e et 4e octave), LFO en mode enveloppe sur level, transient par LFO court sur pitch, filtre « pluck », layer de percussion.
Transcription : oui (anglais, auto)
- 0:04 « main stabs » de « Bunker » = hook du drop.
- 0:52 Osc A sinus ; Osc B sinus, level 0, FM from B monté ; octave de B relevée ; 1:15 éditeur de wavetable de B : fondamentale + quinte + 3e octave + 4e octave.
- 1:44 LFO1 dessiné, mode Envelope → level A ; noise Bright White.
- 2:07 transient ajouté avec un 2e LFO (« a different lfo ») sur le coarse pitch (« core speech » [ASR ?]), modulation unipolaire (Shift+Alt+clic), courbe très courte, mode Envelope.
- 2:29 FX Distortion ; Chorus (LPF monté) ; Compressor threshold bas, gain au max ; EQ boost médium ~500 Hz, Q bas.
- 3:19 Filtre, cutoff modulé par un LFO séparé, unipolaire, forme « pluck ».
- 3:40 post : reverb courte → EQ (harmoniques médium) → Overdrive (sature les médiums) → EQ → Erosion (bruit dans les aigus) → reverb.
- 4:29 layer d'une percussion (transient seul) avec la même chaîne + EQ low cut, reverb plus courte, pitch ajusté.
- Genre : DnB dancefloor (Culture Shock).
À vérifier à l'écran : 1:20–1:40 (harmoniques dessinées), 1:47 (forme LFO1), 2:17 (cible exacte du LFO transient), 3:30 (forme LFO filtre).

### HO-11 How to: Sub Focus / Culture Shock style INTRO leads like in "Recombine" - Serum Tutorial — How to DNB, 13:59, 2024-06-24, outil : Serum 1
URL: https://www.youtube.com/watch?v=h1iUtcinpJw
Technique(s) : scie MB Saw en unison 14 avec dispersion de position de wavetable par voix (onglet Global), glide mono, filtre Reverb keytracké, LFO 2 bars sur Master Tune (attaque de pitch puis descente « triste »).
Transcription : oui (anglais, auto) ; pub 8:09–8:51
- 0:33 motif en scie de la 2e partie de l'intro de « Recombine » (hook d'intro, pas du drop).
- 2:13 wavetable « MB Saw » (analog), position légèrement avancée ; unison 14, detune bas → macro.
- 3:23 ENV attack ~140 ms (sur chaque note), release ~3 s.
- 4:01 LFO1 (non synchronisé, rapide) → WT position un peu ; Global : distribution de WT position sur l'unison ~30 (chaque voix lit une position différente = largeur).
- 5:55 Reverb mix ~50 %, size montée → macro.
- 6:29 Mono + portamento ~100 ms, Legato (« Always »).
- 7:02 Distortion Asym, drive modulé par LFO1, mix baissé.
- 7:31 filtre « Reverb », cutoff ~100 Hz, keytracking, mix baissé, drive monté ; 12:19 un peu de résonance.
- 8:53 Chorus mix ~30 % ; Compressor (threshold bas, gain up) ; EQ shelf aigus ; 10:00 Hyper/Dimension en fin de chaîne après la reverb, mix/rate/detune baissés, size Dimension très bas.
- 10:52 LFO2 à 2 points → Master Tune, montant 1, bipolaire, 2 bars, mode Envelope (attaque de pitch à chaque note, descente sur les notes longues) ; 12:33 smooth sur LFO.
- Genre : DnB dancefloor (Culture Shock / Sub Focus).
À vérifier à l'écran : 2:50 (position WT), 4:30 (distribution WT dans Global), 7:40 (réglages filtre Reverb), 11:00–11:50 (forme LFO2).

### HO-12 Jump Up Drum and Bass Lead in Serum (Macky Gee, Hedex & DJ Guv) — Arc Nade, 7:11, 2022-06-09, outil : Serum 1 (+ OTT, Decimort 2, RBass Mono, Camel Crusher)
URL: https://www.youtube.com/watch?v=0tok0W7EjBw
Technique(s) : scie Basic Shapes avec warp Sync, LFO trigger sur le filtre MG Low 12 fermé (pluck), sub modulé, Diode distortion PRE + passe-haut, double OTT.
Transcription : oui (anglais, auto)
- 0:34 tempo 175 ; lead tiré de son morceau « Rudeboi » (description).
- 1:07 Osc A Basic Shapes, oct -2, random off, WT pos 2 ; warp Sync ~8 ; LFO en Trigger dessiné (cible : level/WT, interp.) ; level au max.
- 1:56 Filtre MG Low 12, cutoff tout en bas + LFO → cutoff (pluck en scie) ; drive up ; 2:20 sub -2 oct + LFO → level.
- 2:35 FX Distortion Diode 1 à fond, mode PRE avec passe-haut ; 3:27 Filter FX Low 18, LFO → cutoff et drive.
- 4:07 post : OTT (depth et time baissés, bandes un peu montées) ×2 ; Decimort 2 [ASR « decimal 2 »] preset « Action Movie » ; RBass Mono [ASR « rbase mono »] ; Camel Crusher « British Clean », compresseur baissé ; limiteur (Pro-L) ; sidechain.
- Genre : DnB jump up (Macky Gee, Hedex, DJ Guv). Attention : registre médium-grave (le « lead » jump-up est le riff du drop).
À vérifier à l'écran : 1:20–1:46 (Sync et LFO), 2:03 (forme LFO filtre), 2:44–3:07 (Diode/HPF), 4:11–4:34 (OTT).

### HO-13 the secret to melodic dubstep leads like Seven Lions — Ash // From Bedroom 2 Banger, 13:01, 2022-10-24, outil : Serum 1 (Vital cité comme alternative ; Ableton)
URL: https://www.youtube.com/watch?v=PIZtYJrNU3E
Technique(s) : hook construit sur un ostinato puis 4 couches Serum (lead principal sec, pluck BS2 Filthy avec reverb, « loose layer » legato avec filtre Reverb, couche MS Saw en Ring Mod).
Transcription : oui (anglais, auto) ; sketchs humoristiques 2:21–4:30 sans contenu technique
- 0:30 BPM 170 ; mélodie en ostinato (court motif répété, retour sur Mi) ; La majeur, scale lock dans Ableton.
- 2:46 Couche 1 (main) : Osc A scie de l'init, unison 3, detune modéré ; 4:30 LFO2 → noise (petite retombée) ; FX Distortion + Compressor + Filter (valeurs à l'écran) ; LFO2 → filtre MG Low ; post EQ graves/aigus + OTT modifié ; pas de reverb (lead devant).
- 5:33 Couche 2 (pluck) : wavetable « BS2 Filthy » (Analog), detune 0, ENV1 très court, passe-haut ; « Wombo Combo » (EQ + OTT) + reverb sur cette couche arrière.
- 6:39 Couche 3 (« loose layer ») : wavetable « Distorted Sub DKS » [ASR ?] (Digital), ENV1 sustain au max, Mono + Legato, filtre Reverb (Misc) mix au max, ENV2 → fréquence très faible ; Hyper/Dimension mix ~50 (alternative : Chorus-Ensemble d'Ableton) ; post EQ + reverb.
- 9:15 « secret sauce » Couche 4 : copie de la couche 3, wavetable « MS Saw » [ASR ?], filtre Ring Mod 2, compresseur (OTT) + chorus.
- 10:32 contre-mélodie au piano (VSCO 2) ; groupe : OTT, Saturator, Reverb, EQ.
- Genre : dubstep, melodic dubstep (Seven Lions « Stop Thinking »).
À vérifier à l'écran : 1:10 (notes de l'ostinato), 4:40–4:50 (Distortion/Compressor/Filter), 5:55 (ENV1 du pluck), 7:55–8:05 (forme ENV2), 10:00 (Ring Mod).

### HO-14 BEAUTIFUL MELODIC DUBSTEP SPIRIT LEADS!!!! (Serum Tutorial) — Celestric, 8:08, 2022-06-20, outil : Serum 1 (+ FL Studio, Ozone Imager, Soothe)
URL: https://www.youtube.com/watch?v=4CJr4lw7Abs
Technique(s) : spirit lead = carré filtré Low 24 avec Noise OSC qui module le coarse pitch (cri), distorsion Asym en tête, multibande, vibratos d'amplitude et de pitch sur macro.
Transcription : oui (anglais, manuelle)
- 0:31 Osc A Basic Shapes carré ; filtre ON ; Mono, portamento ~31 ms ; cutoff ~9 kHz Low 24, Fat monté, résonance un peu.
- 1:11 Noise « Alpha NZ », level 0 ; Noise OSC → coarse pitch d'Osc A, sortie Matrix ~25 % (léger cri).
- 1:52 FX : Distortion Asym avant Hyper/Dimension (défaut), filtre post ~13 kHz, drive au max ; Compressor multiband, threshold -10/-13 dB, ratio 1:4 ; EQ passe-haut 600 Hz, Q 45 %, -4/-5 dB + cloche à Q 60 % sur une résonance ; Reverb low cut 21 %, high cut, Plate, width max, mix 50 %.
- 3:42 post : EQ (<650 Hz et >16.5 kHz) ; Ozone Imager ~50 % (vers le mono, le son était trop phasé) ; Fruity Blood Overdrive -0.400 / 0.600–0.700 ; send saturation 2.1 + passe-haut 250 Hz ; OTT ~25 % (graves coupés) ; reverb ; EQ (<350 Hz, creux 425 Hz) ; compresseur attack 0.1 ms, make-up 4 dB ; Soothe sharpness -3.3 (résonance ~1 kHz).
- 6:46 LFO1 → level -45, rate 1/16 (vibrato d'amplitude) ; menu « Create Vibrato » → LFO → Master Tune 2 % bipolaire, aux source passée du mod wheel à une macro « Vibrato » à 50 %.
- Genre : dubstep, melodic dubstep (aussi future bass).
À vérifier à l'écran : 0:50–1:03 (filtre), 1:30–1:40 (Matrix noise → pitch), 2:06–2:46 (FX), 6:50–7:48 (LFO vibrato).

### HO-15 HOW TO MAKE A DOPE MELODIC DUBSTEP LEAD IN SERUM | TUTORIAL — Paper Skies, 3:24, 2017-06-14, outil : Serum 1 (+ FL Studio)
URL: https://www.youtube.com/watch?v=1rYTKTXbBtg
Technique(s) : « signature lead » : warp Sync très haut modulé par un LFO très lent, position Basic Shapes entre scie et carré, glide mono, Hyper/Dimension, multibande.
Transcription : oui (anglais, auto ; reconnaissance médiocre)
- 0:23 écrire d'abord la mélodie (avec des slides) ; Mono ; portamento ~80.
- 0:43 LFO1 rate abaissé → modulateur très lent du Sync ; warp Sync ; 1:04 montant (petit knob bleu) ~20–25 % ; Sync ~140–150 %.
- 1:23 wavetable Basic Shapes (Analog), position à mi-chemin scie/carré.
- 1:51 FX Hyper/Dimension (réglages à l'écran) ; Distortion ~75 % ; Compressor multiband, gain ~5 dB, threshold ~-12 dB ; reverb ~10 %, delay ~2 % [ASR ?].
- Genre : dubstep, melodic dubstep.
À vérifier à l'écran : 0:53–1:10 (mode Sync et montant LFO), 1:30 (position WT), 2:04 (Hyper/Dimension), 2:40 (ratio multiband).

---

### Écartés
- iHbn1zld9tg Aspen Lyon « Deep House Lead like Avaion - Wacuka » : aucune transcription (vidéo sans voix), impossible à vérifier.
- ab54oUHXZRo W. A. Production « Sub Focus & Wilkinson - Illuminate » : aucune transcription.
- OnDipGYsvEc Samstone « DNB Foghorn » : 4 basses (wobble 808, foghorn PWM, FM, phaser/flanger), pas de hook médium/aigu.
- fuYIzCLd1gc XLNTSOUND « Badadan » : remake d'une « fill bass » (basse), longs passages promo.
- QlezOQa3UsM DNB Academy « Power Stab Serum 2 » : stab de basse (sinus -3 oct, « for any kind of bass »).
- J0vcyBEnRdQ How to DNB « Dimension DJ Turn It Up rave stabs » : hook DnB, mais le cœur du son vient du sampler Rave Generator 2 ; Serum ne sert qu'aux couches supersaw et hypersaw → pas « designé dans Serum ». Bon remplaçant si une source hybride est acceptée.
- aN1lZZa24_E BLZE « Future Rave Dreams » : voix de synthèse très succincte (ENV A 5.4 / D 64 / S 27.5 / R 118, noise Bright White), trop pauvre, et LEAD.md couvre déjà le future rave.
- IKre-UrLLg4 W. A. Production « Tchami style lead » : lead soutenu plutôt que hook ; recoupe LE-07 (lead future house).
- dT2x_tF2upA YJ Music « Most Versatile Melodic Dubstep Lead » : valable (square + WT Dis.., FM from Noise 50 %, portamento 260, delay L 1/8 R 1/16) mais redondant avec HO-13/14 ; 4e choix dubstep.
- Non ouverts (repérés seulement) : CCtjRaOEVWU, jpz9oKyTdVs (autres remakes du horn de Fisher, même morceau que HO-01/02), qSVtVduruPs, P6g2a3Va-WY (Sam Smyers, déjà 3 vidéos de lui), 2eX5z8VeRdY (Arc Nade, stab jump-up, déjà HO-12), 6M4Aljayy0Q (neuro lead, type LEAD).

### Manque
- 15/15 trouvées, répartition 8 house / 4 DnB / 3 dubstep respectée.
- La DnB a été la famille la plus difficile : beaucoup de « hooks » DnB sont des basses (rejetées). HO-11 est un hook d'intro (pas de drop) et HO-12 un lead jump-up en registre médium-grave.
- Le français est faible : 1 seule vidéo FR (HO-05) ; aucun autre tuto FR de hook dans Serum n'a été trouvé.
- Concentration de chaînes : Sam Smyers ×3 (HO-02/04/08), How to DNB ×2 (HO-09/11).
- Serum 2 : seulement HO-04 et HO-07 ; le reste est en Serum 1.

# Chords

## CHORDS — synthés d'accords conçus dans Serum (stabs house, accords DnB, accords dubstep / future bass)

Ordre : house (8) → drum and bass (4) → dubstep / melodic dubstep / future bass (3). Toutes les vidéos retenues sont en Serum 1 : aucun tutoriel d'accords Serum 2 avec réglages réellement commentés n'a été trouvé (voir Écartés). Les valeurs viennent des transcriptions (souvent auto) : « (interp.) » = mon interprétation, [ASR ?] = mot douteux dans la reconnaissance vocale.

---

### CH-01 How to Make Classic 90s House Stabs in Serum | Tutorial — LÄMMERFYR, 9:35, 2024-12-28, outil : Serum 1
URL: https://www.youtube.com/watch?v=xH42aOTPh7I
Technique(s) : accord intégré dans le patch (une touche = un accord mineur), sub en dent de scie comme fondamentale, enveloppe pluck sur le filtre, bruit transitoire, dérive analogique par fine tune opposés.
Transcription : oui (EN, auto)
- 0:24 principe : l'accord est construit dans les oscillateurs, on joue une seule note → stab « samplé » années 90
- 0:49 sub osc = fondamentale, forme saw ; 1:00 filtre activé sur tous les oscillateurs ; 1:07 type German LP (MK)
- 1:13 osc A saw par défaut, +7 demi-tons (quinte) ; 1:38 osc B wavetable « Basic MG », position montée, level monté, +3 demi-tons → triade mineure (fondamentale / +3 / +7)
- 2:02 remarque : jouer la même forme sur d'autres notes donne des accords hors gamme (couleur house classique)
- 2:13 osc A unison 5 voix, petit detune ; 2:24 LFO1 → position WT osc B, BPM off, vitesse lente
- 3:04 noise « Bright White », one-shot, phase aléatoire, level réglé ; 3:30 ENV2 sustain 0, decay court, un peu de release (pluck) ; 3:50 ENV2 → level du noise (montant réduit)
- 4:13 ENV2 → cutoff ; 4:28 résonance montée ; 4:41 drive monté ; 4:56 ENV1 sustain un peu baissé, release, decay ajustés
- 5:26 fine tune ≈ -5 sur un oscillateur et valeur opposée sur l'autre (dérive)
- FX : 6:27 chorus par défaut, mix baissé ; 6:35 distortion Tape, mix baissé, drive ≈ 15 % ; 6:50 delay 1/8, feedback bas, ping-pong, low cut dans l'EQ du delay ; 7:07 reverb Hall, size montée, decay baissé, low cut, mix ≈ 16 % ; 7:30 compressor par défaut + gain ; 8:09 essai d'attack sur ENV2
- Genre : house (classic / 90s house stab) — référence explicite aux stabs house 90s, accord mineur dans une note.
À vérifier à l'écran : 1:07 type de filtre exact et cutoff de départ ; 1:38 position WT de l'osc B ; 2:24 vitesse et montant du LFO1 ; 4:13 montant ENV2→cutoff et valeurs ADSR ENV2 ; 6:35 réglages Tape distortion.

### CH-02 Deep house stab sound design (Eli & Fur style) - Serum Beginners Tutorial — The Audio Journey, 12:50, 2021-01-06, outil : Serum 1
URL: https://www.youtube.com/watch?v=zjK85YIzyfg
Technique(s) : stab deep house à partir de saw + wavetable FM, enveloppe d'amplitude percussive, filtre qui se referme, flanger/chorus, LFO aléatoire léger sur le cutoff ; accords joués en MIDI (MIDI en lien dans la description).
Transcription : oui (EN, manuelle)
- Référence : Eli & Fur « Feel The Fire » ; MIDI de l'accord en description
- 1:39 osc A saw par défaut ; 1:45 osc B : essai FM_Splat puis FM_Freak retenu
- 2:11 ENV1 attack ≈ 10–11 ms, sustain 0 ; 2:36 decay ≈ 500 ms, release ≈ pareil ; 3:00 réglage de la courbe de l'enveloppe
- 3:44 filtre activé, osc B routé dessus (vérifier A) ; 4:11 drive + fat ; 4:35 ENV1 → cutoff (filtre ouvert puis qui se referme) ; 5:27 un peu de résonance
- 5:52 reverb + delay par envois Ableton ; 6:24 Flanger mix ≈ 1/3 ; 6:48 chorus discret
- 7:02 EQ de Serum : bande basse, Q baissé, ≈ 150 Hz pour enlever le bas (interp. : rôle de low cut / shelf)
- 7:38 LFO → cutoff, BPM off, quelques Hz, petit montant (vie / aléatoire)
- Hors Serum : 9:49 EQ Eight boost aigus, low cut, creux dans les médiums ; 11:02 Saturator Analog Clip ≈ 4 dB de drive, soft clip, dry/wet 50 % ; 11:55 essais d'unison et d'autres oscillateurs
- Genre : house (deep / melodic house, style Eli & Fur) — stab deep house annoncé dans le titre.
À vérifier à l'écran : 1:45 position WT FM_Freak ; 3:44 routage des oscillateurs vers le filtre et type de filtre ; 4:35 montant ENV1→cutoff et cutoff de départ ; 7:38 vitesse exacte du LFO ; MIDI de l'accord (voicing) dans la description.

### CH-03 How To Make A Chord Stab For Those House, Garage & Minimal Tunes in Serum! — Zac Stanton, 13:49, 2023-05-07, outil : Serum 1 (interp. d'après l'interface décrite)
URL: https://www.youtube.com/watch?v=rMnnssrXxsc
Technique(s) : deux sinus à une octave d'écart en unison, bruit « poussiéreux », filtre très bas ouvert par l'enveloppe, downsample, enveloppe sur le fine tune (petit « pitch drop »), accord mineur 7 swingué.
Transcription : oui (EN, auto) ; chapitres : osc 0:17, filtre & ADSR 1:26, FX 3:23, modulation de pitch 5:40, accord Am7 6:39, essais 9:40, résumé 12:34
- 0:24 osc A Basic Shapes sinus, -1 octave, unison 4 voix, detune ≈ 10 ; 0:41 osc B pareil, +1 octave, 4 voix, detune ≈ 10
- 1:14 noise [ASR « Argan nose » ; probablement un sample de bruit d'orgue] pour la « poussière » ; 1:25 A, B et noise vers le filtre
- 1:43 cutoff ≈ 100 Hz, ENV1 → cutoff montant ≈ 40 ; 2:04 drive monté, résonance essayée puis baissée, fat
- 2:37 sustain baissé (pluck), decay rallongé ; 2:53 attack 5 ms, un peu de release
- FX : 3:29 Dimension pour élargir ; 3:45 distortion Downsample, placée avant le filtre (pre) ; 4:26 mix ≈ 30 ; 4:30 chorus ; 4:53 reverb decay ≈ 4 s ; 5:21 delay synchro 1/8, feedback baissé
- 5:51 enveloppe → fine tune des deux oscillateurs (courbe tirée à gauche) = léger glissement de hauteur à l'attaque
- Voicing : 6:46 accord La mineur 7 (Am7), joué avec du swing ; 8:52 vélocité ≈ 80
- 9:52 essai wavetable MB saw et positions ; 12:13 forme LFO ; decay 2 s
- Genre : house (house / garage / minimal stab) — annoncé dans le titre.
À vérifier à l'écran : 1:14 nom exact du sample de noise ; 1:43 type de filtre et valeurs exactes cutoff/montant ; 3:45 réglages Downsample ; 5:51 montant de l'enveloppe sur le fine ; 6:46 notes MIDI de l'Am7 (voicing).

### CH-04 Use Serum To Make An Organ Sound For Those House, Garage & Tech House Tracks! — Zac Stanton, 11:24, 2023-02-04, outil : Serum 1
URL: https://www.youtube.com/watch?v=Hh0Cxu8hTA0
Technique(s) : stab d'orgue (type M1 / garage) par sinus empilés (fondamentale + 2 octaves), bruit d'orgue, filtre MG Low 12, Hyper pour un caractère « carré », harmoniques ajoutées dans l'éditeur de wavetable.
Transcription : oui (EN, auto) ; chapitres : osc 0:16, filtre 3:34, FX 4:34, éditeur WT 6:20, enveloppe 8:33, résumé 9:51
- 0:23 osc A Basic Shapes sinus ; 0:43 osc B sinus +7 demi-tons (quinte) 0:58, puis +1 octave 1:02, préférence finale +2 octaves 1:13 (son « garage »)
- 1:45 ENV1 attack 5 ms ; 1:55 hold ≈ 50 ms ; 2:30 decay 1 s, sustain 0
- 2:48 noise one-shot [ASR « Argan nose » = organ noise ?], level baissé, ENV1 → level du noise ≈ 10
- 3:39 filtre MG Low 12, A+B routés, cutoff ≈ 100, ENV1 → cutoff ≈ 30, résonance ≈ 25, drive
- 4:30 mono ; FX : 4:37 Hyper, mix monté → plus carré / garage ; 5:01 distortion mix ≈ 25 ; 5:14 compressor ; 5:24 chorus ; 5:36 reverb decay ≈ 3 s (ou 2 s), low cut monté 6:09
- 6:26 éditeur WT (additif) : harmonique (bin) 2/3 montée à ≈ 30 ; 7:16 copier-coller vers osc B ; 7:52 essai bin 3 ≈ 15
- 8:39 decay plus court / plus long (2 s), release
- Genre : house (garage / tech house, orgue façon M1) — annoncé dans le titre.
À vérifier à l'écran : 1:13 octave finale de l'osc B ; 3:39 cutoff et résonance exacts ; 4:37 réglages Hyper ; 6:26 quelles harmoniques et à quel niveau ; 8:39 valeurs finales d'ADSR.

### CH-05 TUTO HOUSE RAVE STAB Sur SERUM - Tout ce que vous devez savoir — Strob Studio, 12:15, 2023-11-01, outil : Serum 1 (interp.)
URL: https://www.youtube.com/watch?v=aJzVm6QrQ8E
Technique(s) : rave stab = accord samplé recréé par intervalle entre oscillateurs, wavetables type Juno, phase non aléatoire « comme un sample », enveloppe longue sur le Master Tune, bruit, filtre LP 18 percussif, distortion/flanger « vintage ».
Transcription : oui (FR, auto)
- 2:00 clé 1 : les rave stabs étaient des accords samplés → ajouter un 2e oscillateur à un intervalle (accord de 2 notes), éventuellement un 3e avec le sub
- 3:09 demi-tons essayés « -2 / +10 » (équivalent octave au-dessus) — à choisir selon la note de basse
- 3:28 wavetables : sources type Juno (Juno square, Juno DCO…) ; 4:06 phase : random à 0 pour l'oldschool (chaque coup identique comme un sample) ; 4:27 un peu d'unison pour la stéréo (compromis random/phase 4:50)
- 5:27 clé 2 pitch : désaccorder les oscillateurs séparément 5:38 ; 5:49 ENV → Master Tune global, range 12 (1 octave) 6:00 ; longueur d'enveloppe 1 mesure (synchro BPM) 6:08 ; bipolaire, léger mouvement haut/bas ; 7:56 attack raboté
- 8:28 clé 3 : bruit (oldschool) ; 8:41 clé 4 filtre : Low Pass 18 8:51, enveloppe percussive → cutoff 8:56
- 9:25 astuce : filtre/EQ interne pour raboter la fondamentale (bas-médiums)
- FX : 9:55 distortion ; 11:12 passe-bas pour enlever les aigus (« grunge vintage ») ; 11:20 flanger comme coloration de filtre ; 11:43 EQ pour raboter les aigus
- Genre : house (rave / oldschool house stab) — annoncé dans le titre ; vidéo FR.
À vérifier à l'écran : 3:09 demi-tons finaux de chaque oscillateur ; 3:28 wavetable Juno retenue ; 6:08 forme et montant de l'enveloppe sur le Master Tune ; 8:56 ADSR de l'enveloppe filtre ; 9:55 type de distortion.

### CH-06 SERUM Tutorial | Chord Stab, Melodic House & Techno | Oliver Giacomotto, Artbat — The Sound Design Channel, 7:36, 2024-02-04, outil : Serum 1
URL: https://www.youtube.com/watch?v=Yz7rAfSjBps
Technique(s) : stab melodic house avec saw + saw à la quinte en warp Bend +/-, LFO lent sur fine/bend (analogique), sub saw, bruit, filtre fermé ouvert par ENV2, reverb dont le mix est modulé par l'enveloppe.
Transcription : oui (EN, auto)
- 0:51 osc A saw init, unison un peu monté, detune baissé ; 1:09 LFO1 → fine osc A très faible, en Hz (pas BPM), lent (dérive analogique)
- 1:45 osc B saw +7 demi-tons (quinte), unison monté, detune baissé ; 2:08 warp « Bend +/- », level baissé ; LFO1 → Bend +/- 2:20 et → fine (plus) 2:33
- 2:41 sub saw -1 octave ; 2:51 noise Bright White, level monté
- 3:07 filtre sur A + B + noise + sub, cutoff fermé à fond 3:17 ; ENV2 → cutoff 3:24, sustain 0, decay un peu baissé ; 3:47 drive et fat montés
- FX : 4:08 Hyper/Dimension (mix Hyper 0, Dimension monté, size baissé) ; 4:39 distortion drive monté, mix bas ; 4:52 chorus LP monté, mix bas ; 5:12 delay 1/8 et 1/16, ping-pong, feedback monté, fréquence du filtre baissée, Q baissé, mix bas ; reverb size bas, decay haut, sans grave, high cut monté, spin depth monté, mix 0 modulé par ENV2 6:00–6:29
- 6:38 hors Serum : ShaperBox + EQ
- Genre : house (melodic house & techno, style Artbat / Oliver Giacomotto) — annoncé dans le titre.
À vérifier à l'écran : 2:08 montant du warp Bend +/- ; 3:24 ADSR ENV2 et montant sur cutoff ; 5:12 réglages delay ; 6:00 montant ENV2 → mix reverb.

### CH-07 How to make a Future house chord in serum 2021🔥 — Axe 391, 4:20, 2021-08-04, outil : Serum 1
URL: https://www.youtube.com/watch?v=h50Y5MwVwxA
Technique(s) : accord future house (style Don Diablo) : deux oscillateurs à 9 voix, filtre MG Low 24, chute de pitch par ENV3 sur le coarse, LFO redessiné sur le cutoff.
Transcription : oui (EN, auto)
- 0:12–0:52 écriture des accords en MIDI
- 0:54 osc A unison 9 voix, detune baissé ; 1:21 osc B pareil
- 1:31 les deux oscillateurs dans le filtre « MG Low 24 »
- 1:53 ENV3 decay court → coarse pitch des deux oscillateurs [ASR « correct b » = coarse ?], montant -22 (chute de pitch, « technique unique »)
- 3:00 LFO1 redessiné → cutoff à fond ; 3:27 réglage de la vitesse du LFO pour un effet « wobble » [ASR « oval type »]
- Genre : house (future house) — annoncé dans le titre.
À vérifier à l'écran : 0:52 voicing des accords dans le piano roll ; 1:53 ADSR ENV3 et montant exact (−22 ?) ; 3:00 forme et vitesse du LFO1 ; FX éventuels non commentés.

### CH-08 Serum Tutorial - Mellow CHORD SYNTH Keys (Nu Disco / House / Future Pop) — SynthHacker, 13:50, 2021-04-30, outil : Serum 1
URL: https://www.youtube.com/watch?v=YH26TVrLguw
Technique(s) : keys d'accords doux : saw, enveloppe pluck, panoramique aléatoire par note (Note-On Random) au lieu de l'unison, LP 24 dB avec enveloppe séparée, bruit, Dimension/chorus/Hall.
Transcription : oui (EN, auto)
- 1:18 MIDI gratuit en lien ; 1:20 forme saw [ASR « moog saw » = « MG Saw » ?], ENV1 forme pluck
- 1:37 « spread » analogique polyphonique : matrice Note-On Random → pan de l'oscillateur (pan aléatoire par note plutôt que l'unison)
- 2:29 Low Pass 24 dB, enveloppe séparée decay court et release plus long → cutoff ; 3:02 même enveloppe → level d'un noise (sample de bruit personnalisé)
- FX : 3:35 Dimension expander ; 3:50 chorus discret ; 4:04 reverb Hall
- 4:27 hors Serum : D16 Decimort (downsampling façon Medasin), RC-20 (vinyle), sidechain ; 12:13 automation cutoff/résonance du synthé d'accords
- (8:24 basse et 11:17 pad Repro-5 : hors sujet)
- Genre : house (nu disco / house, aussi future pop) — annoncé dans le titre.
À vérifier à l'écran : 1:20 nom exact de la wavetable ; 1:37 montant Note-On Random → pan ; 2:29 cutoff et ADSR de l'enveloppe filtre ; 3:35 réglages Dimension.

### CH-09 How to make STABS like CULTURE SHOCK - BUNKER | Serum Tutorial — DNB Academy, 6:45, 2021-03-12, outil : Serum 1
URL: https://www.youtube.com/watch?v=WR4XyJ12UkE
Technique(s) : stab DnB FM sinus, harmoniques (dont la quinte) dessinées dans l'éditeur WT, enveloppe par LFO en mode envelope, compression/EQ, couche percussive.
Transcription : oui (EN, auto)
- 0:52 osc A sinus ; 0:55 osc B sinus level 0, FM from B monté ; 1:13 osc B une octave plus haut
- 1:18 éditeur WT : fondamentale, quinte, 3e octave, 4e octave (accord de quinte dans la wavetable)
- 1:44 LFO1 en mode envelope → level osc A ; 1:58 noise Bright White
- 2:08 un autre LFO, courbe courte en enveloppe → [ASR « core speech » = rate ?] du LFO1, unipolaire (shift+alt) → transitoire
- FX : 2:31 distortion, chorus LP monté, compressor threshold baissé gain monté, EQ boost médiums ≈ 500 Hz Q baissé
- 3:19 filtre activé, LFO séparé unipolaire en forme pluck → cutoff
- 3:40 hors Serum : reverb courte, EQ, overdrive, EQ, erosion, reverb ; 4:31 couche transitoire percussive, même chaîne + EQ low cut
- Genre : DnB (style Culture Shock, dancefloor / liquid-rolling) — référence à « Bunker ».
À vérifier à l'écran : 1:18 niveaux des harmoniques dans l'éditeur ; 1:44 forme du LFO1 ; 2:08 cible exacte de la modulation [ASR ?] ; 3:19 forme et montant du LFO de filtre.

### CH-10 How To Make KEYS & BASSES Like CALIBRE in Serum | Ableton Tutorial — DNB Academy, 10:19, 2021-04-04, outil : Serum 1
URL: https://www.youtube.com/watch?v=B7jdMh3lD_E
Technique(s) : keys liquid DnB en sinus (fondamentale + octave), decay court, delay filtré et reverb ; voicing Cm7 → Si bémol avec note de mélodie gardée.
Transcription : oui (EN, auto)
- Voicing : 0:51 progression Do mineur 7 (Cm7) ; 1:00 après 4 mesures, même accord + octave de la fondamentale empilée ; 1:15 dernière mesure → Si bémol (A#) avec son octave, en gardant le Do comme note de mélodie
- 1:39 osc A sinus ; 1:48 ENV1 sustain 0, decay ≈ 108 [ms ? ASR], point de courbe monté, un peu d'attack
- 2:29 osc B sinus +1 octave, level plus bas
- FX : 2:48 delay 1/8, filtre ≈ 1700 Hz, mix monté, feedback pour une traîne plus longue ; 3:27 reverb (rêveuse)
- Hors Serum : 3:46 couche piano à queue Ableton avec beaucoup de reverb + filtre ; 4:30 resample des keys -12 demi-tons, reverse, fin de mesure, Complex Pro formants 0
- (6:32–7:55 basse : hors sujet)
- Genre : DnB (liquid, style Calibre / remix T.E.E.D « Garden »).
À vérifier à l'écran : 1:48 decay exact ; 2:48 réglages du delay ; 0:51–1:15 notes MIDI du voicing.

### CH-11 How to Make Liquid D&B Pads (with Serum, No Music Theory Needed) — STRANJAH, 17:06, 2020-02-11, outil : Serum 1
URL: https://www.youtube.com/watch?v=sr31vDqnpjg
Technique(s) : accords liquid (7e et 9e) dérivés de la ligne de basse, saw + WT spectrale, LP multipôle avec attack d'enveloppe, unison 6, doublure des fondamentales à l'octave inférieure (titre « pads » mais l'essentiel = écriture/voicing d'accords ; recoupement possible avec la liste PAD).
Transcription : oui (EN, auto)
- Voicing : 0:57 saw basique, +2 octaves 1:11 (accords calqués sur la basse) ; 2:00 Mi mineur vs La mineur ; 3:11 transposer en La mineur (touches blanches), « plier » le clavier ; 4:02 triades : empiler 1-3-5 (une touche blanche sur deux) ; 5:12 ajout de la 7e, 6:00 ajout de la 9e (le liquid utilise 7e/9e)
- 6:16 filtre LP (plus de pôles = plus rond), un peu de résonance, drive, master baissé (5 notes) 6:54, fat
- 7:12 ENV2 attack → cutoff (balayage montant), montant ajusté ; 8:26 LFO1 → cutoff faible, 1/4 ou BPM off
- 9:35 reverb + EQ ; 10:46 unison ≈ 6 ; 11:15 phase aléatoire gardée (plus épais) ; 11:42 comparaison des formes, préfère la saw
- 12:20 osc B wavetable spectrale, routée au filtre, +2 octaves (essais +1 / -1)
- 13:28 EQ Eight low cut 220 Hz (ou 110) ; 14:22 doublure des fondamentales une octave plus bas ; 15:18 doublure de la quinte en bas essayée puis retirée, seule la couche fondamentale gardée
- Genre : DnB (liquid) — annoncé dans le titre.
À vérifier à l'écran : 6:16 type de filtre et cutoff ; 7:12 ADSR ENV2 ; 10:46 detune de l'unison ; 12:20 nom de la WT spectrale.

### CH-12 How to make STABS like DELTA HEAVY - Take The Stairs | Serum Tutorial — DNB Academy, 7:00, 2021-04-19, outil : Serum 1
URL: https://www.youtube.com/watch?v=nAIUiCF66qM
Technique(s) : stab DnB à partir d'une wavetable spectrale aux harmoniques « bizarres » (le formant), pluck, LFO sur le fine, passe-bande + distortion forte, EQ utilisée comme contrôle de formant. Réserve : la première moitié traite du sub ; stab mono plutôt qu'accord voicé (retenu pour atteindre 4 DnB).
Transcription : oui (EN, auto)
- 3:24 stab : WT spectrale aux harmoniques étranges, « une des dernières de Monster 1 » [ASR ?], qui détermine le formant
- 4:22 sustain 0, pluck ; 4:33 LFO → fine tune (trop rapide = phasing)
- FX : 4:52 filtre bandpass ; 5:09 distortion forte ; 5:17 chorus ; 5:25 compressor gain ; 5:30 EQ qui coupe tout sauf les aigus ; 5:35 reverb
- Genre : DnB (style Delta Heavy, dancefloor / neuro-mélodique).
À vérifier à l'écran : 3:24 nom exact de la wavetable ; 4:33 vitesse du LFO ; 5:09 type de distortion ; 5:30 forme de l'EQ.

### CH-13 here's how I ALWAYS make Melodic Dubstep Chords now (like Seven Lions) (emotional) — Ash // From Bedroom 2 Banger, 14:19, 2022-10-12, outil : Serum 1 (+ alternative Vital, chœur sforzando, Ableton)
URL: https://www.youtube.com/watch?v=H4YcXoEONLU
Technique(s) : écriture d'accords melodic dubstep à partir de la basse (triades, renversement de la tierce), chaos S&H sur le coarse pitch, couches (chœur, couche médium carrée, basses).
Transcription : oui (EN, auto)
- 0:31 170 BPM, La majeur avec scale lock ; 0:44 changement de note en contretemps une demi-temps en avance ; 1:13 notes de transition
- Voicing : 1:28 basse → accords : une octave plus haut, ctrl-drag en sautant une note ×2 (triades) ; 1:59 Easy Chord Rack (gratuit) ; 3:09 renversement : monter la tierce (note du milieu) d'une octave → plus propre et plus plein ; 3:46 accords sur la « chaos saw », notes graves mutées (gardées pour la basse)
- 3:59 onglet Global de Serum : chaos rate au maximum, mode sample & hold ; 4:09 Chaos1 → coarse pitch [ASR « chorus pitch »] montant 20 dans la matrice ; 4:15 unison +5
- 5:18 FX [ASR « Wambo combo »], EQ low/high cut ; 5:33 couche chœur (sforzando, soundfont Roland), OTT, reverb hybride ≈ 35 %, utility width
- 6:52 couche médium : Serum/Vital init, osc2 Basic Shapes → carré, -12 demi-tons, filtre HP, attack lente
- (9:25–12:24 basses Reese / buzz / sub : hors sujet direct)
- Genre : dubstep (melodic dubstep, style Seven Lions).
À vérifier à l'écran : 3:59 réglages Chaos exacts ; 4:09 montant et cible exacte (coarse ?) ; 4:15 detune de l'unison ; 3:09 voicing final dans le piano roll.

### CH-14 WE ARE BACK! | Huge Melodic Dubstep Chords in SERUM and HARMOR in FL Studio — Ghosthack, 23:10, 2020-06-16, outil : Serum 1 + Harmor (partie Serum 12:49–20:00)
URL: https://www.youtube.com/watch?v=Qccz1EfsYF4
Technique(s) : mur d'accords par couches : saws très désaccordées (9 voix) + saws propres (3 voix) + basse + sub + sirène + bruit stéréo + arp ; phaser pour flouter les harmoniques ; voicing large.
Transcription : oui (EN, auto)
- 2:04 problème : une seule pile de saws + sub = ennuyeux → empiler des couches ; 2:25 accords voicés larges, « mur de fréquences » sur l'EQ
- 13:05 Serum saws désaccordées : saw 9 voix, detune ≈ 22 [ASR ? peut-être 0.22], blend pour que la voix centrale = les autres 13:20 ; 13:28 phaser (rate/depth/freq/feedback bas, peu de mix) pour flouter les harmoniques ; 13:41 atténuer les aigus perçants
- 13:59 accords propres : saw 3 voix, detune ≈ 0.04 14:05, phaser, low + high cut
- 14:38 couche basse : saw 9 voix peu désaccordées + osc B WT Monster, distortion sine fold 15:18, phaser, Hyper/Dimension, multibande ; 16:08 sub : éditeur WT fondamentale + quelques harmoniques, un peu d'attack/release
- 16:52 « sirène » aiguë : saw très désaccordée, LFO → fine 8,2 Hz, noise, drive ; 17:45 bruit stéréo : noise panoramiqué à gauche + FM from B avec WT folles (+4 octaves, hauteurs impaires) panoramiqué à droite 18:18–19:06 ; 19:16 arp saw, enveloppe sur le level, phaser, LFO pan 1/4 triolet
- 21:09 spectre plein, laisser de la place pour la voix
- Genre : dubstep (melodic dubstep) — annoncé dans le titre.
À vérifier à l'écran : 13:05 valeur exacte du detune (22 ou 0.22) ; 13:28 réglages du phaser ; 14:05 detune des saws propres ; 2:25 voicing des accords.

### CH-15 FUTURE BASS Chords Serum Tutorial! — Antidote Audio, 6:40, 2021-07-18, outil : Serum 1 (interp.)
URL: https://www.youtube.com/watch?v=1o_3NzyqgVg
Technique(s) : accord future bass « Power Saw » avec formes de base (triangle + carré + sub), « wub » par LFO sur les levels, FM from B, distortion avant Hyper/Dimension, OTT, reverb ; MIDI des accords en description.
Transcription : oui (EN, sous-titres d'apparence manuelle)
- 0:13 recrée le preset « Power Saw » du pack Sunset ; 0:25 osc A Basic Shapes triangle ; 0:37 osc B Basic Shapes carré ; sub activé
- 0:49 LFO1 avec courbe montée → levels osc A, osc B et sub (le « wub » de pompage) 0:55–1:07 ; 1:16 noise « AC Hum » à bas niveau, LFO1 → level du noise, pitch ajusté 1:30
- 1:36 vitesse du LFO1 = vitesse du wub, ex. 1/8
- 2:04 FM from B (sur osc A) monté
- FX : 2:18 distortion placée avant l'Hyper/Dimension, drive baissé ; 2:32 Hyper/Dimension : mix baissé, size baissé, mix (dimension) un peu monté ; 2:42 multibande / OTT, valeurs vertes (upward) remontées ; 3:04 reverb size montée, low cut monté, high cut monté, mix baissé 3:50 (la traîne déborde sur le changement d'accord) ; 3:25 EQ high pass, Q baissé, coupe du sub
- 3:58 phase aléatoire on/off : on = variations, off = attaque identique à chaque note
- 4:42–6:06 hors Serum : chaîne parallèle Ableton (EQ mid/side, seulement les côtés, Utility, Spectral Blur) pour l'effet « Flume »
- Genre : future bass (famille dubstep / future bass du TYPE) — annoncé dans le titre ; style Flume.
À vérifier à l'écran : 0:37–0:49 réglages unison (passage non commenté dans la transcription) ; 0:55 forme exacte du LFO1 ; 2:04 montant FM ; 2:42 réglages OTT ; MIDI des accords (voicing) en description.

---

### Écartés
- 0dXHNoi4Lm4 LÄMMERFYR « UK Garage Chords like Sammy Virji / Conducta / MPH » — bon tutoriel (sinus unison 5, ENV2 → Master Tune range 12 st pour des accords qui plient, warp Bend+, Downsample) mais genre UK garage, hors familles prioritaires ; même chaîne que CH-01. Réserve n° 1 côté house.
- MPuKJQbHosc Sonance Sounds « How To Selected Style Chords In Serum » (3:26, deep house façon « Sunflower ») — transcription très confuse, valeurs inexploitables. Réserve.
- -yxXg2GW8jA Durosai « Serum House Stab Tutorial in Ableton! » — stab lead mono, pas d'accord ; transcription clairsemée. Réserve.
- 3zJAE9liPNc Myshko — fait dans Electric (piano Ableton) + Auto Filter, pas Serum.
- 2fgpTZAfiVk LÄMMERFYR orgue M1 — plugin Korg M1 + Sylenth1 + Pigments, pas Serum.
- N6P-apLRdvc Olean's house formant stabs — sampling/Simpler/Helm, pas Serum.
- vRisDsU5nVc Groove Selective orgue M1 Serum 2 — charge son propre preset, pas de sound design (surtout arrangement).
- inG4rMF-CRA Sound Factory « FISHER Freaks » — 3:13, sans transcription, description = pub de preset.
- KqbTF28FShs Synthesis « Dubby Chord Stabs with Serum » — sans transcription ; dub techno sur Push.
- xcUexBkeCTE ErikVanTools deep house stab chords Serum 2 — sans narration, transcription vide.
- jo7FFv8E43o Arylith « Melodic Dubstep Chords Using ONLY SERUM » — narration quasi absente, aucune valeur dite, presets.
- 0RC1uRAELrs DNB Academy CESCO ABR stabs — surtout basse/sub one-shot, pas d'accord ; même chaîne.
- 2qD4GHjKOx0 DNB Academy neuro stab Serum 2 — stab de basse mono, pas d'accord.
- Vus dans la recherche « future bass chords serum » mais non étudiés (diversité de chaînes) : n3TrRtFoIKU Ghosthack (chaîne déjà en CH-14), Ho5348u2C-U Ash (chaîne déjà en CH-13), autres résultats plus anciens/courts.

### Manque
- 15 retenues / 15 visées : 8 house (dont 1 en FR), 4 DnB, 3 dubstep/future bass (2 melodic dubstep + 1 future bass).
- Aucun tutoriel Serum 2 d'accords exploitable : les deux candidats Serum 2 trouvés (vRisDsU5nVc, xcUexBkeCTE) étaient sans sound design commenté.
- Une seule vidéo en français (CH-05) ; pas trouvé de tuto FR d'accords deep/afro house avec réglages commentés.
- Afro house et tech house : pas de tutoriel d'accords spécifique (CH-03/CH-04 couvrent tech house / garage / minimal).
- CH-12 est plus un stab mono qu'un accord voicé (retenu pour atteindre 4 DnB, faute de mieux) ; CH-11 recoupe la catégorie PAD.
- Dubstep « pur » (riddim) : aucun tutoriel d'accords ; la 3e place dubstep est occupée par de la future bass.

# Pad

## PAD — tutoriels de pads designés dans Xfer Serum (préfixe PA)

Ordre : house (8) → drum and bass (5) → dubstep / melodic bass (2). Les valeurs viennent des transcriptions (sous-titres auto EN) et sont notées comme dites ; « (interp.) » = mon interprétation, [ASR ?] = mot douteux de la reconnaissance vocale.

---

### PA-01 Serum Tutorial - JUNO Inspired DEEP HOUSE Pad Synth — SynthHacker, 6:19, 2021-12-14, outil : Serum 1
URL: https://www.youtube.com/watch?v=bUxbwEvxjNQ
Technique(s) : pad façon Juno (saw + unison), double oscillateur à l'octave, vibrato et trémolo par LFO dont la vitesse est elle-même modulée, enveloppes sur cutoff et résonance, chorus.
Transcription : oui (EN, auto)
- 0:47 OSC A : wavetable saw « Juno », unison 5
- 1:01 enveloppe d'ampli : attack doux, decay long
- 1:20 OSC B = copie de A, +1 oct
- 1:38 LFO → fine (pitch) + level de l'OSC B : vibrato et trémolo légers
- 2:05 LFO2 en enveloppe décroissante sur 2 mesures → rate du LFO1 (le mouvement ralentit pendant la note)
- 2:54 filtre LP 12 ; 3:10 enveloppe lente → cutoff ; 3:28 enveloppe plus courte → résonance
- 3:57 EQ passe-haut ; 4:14 chorus (son LPF interne ouvert) ; 4:42 reverb avec decay baissé ; 5:02 petit delay placé avant la reverb
- Aucune valeur chiffrée n'est dite à part l'unison : tout est à lire à l'écran.
- Genre : house (deep house), annoncé dans le titre, avec le son Juno typique du genre.
À vérifier à l'écran : 0:47 nom de la wavetable et detune ; 1:38 profondeur et rate du LFO1 ; 2:05 forme et durée du LFO2 ; 3:10 ADSR de l'ENV2 et montant sur le cutoff ; 4:14 rate et mix du chorus.

### PA-02 10 ways to make BETTER House pads | Serum tutorial — LÄMMERFYR, 11:08, 2023-02-16, outil : Serum 1 (+ Ozone Imager, RC-20 en bonus)
URL: https://www.youtube.com/watch?v=AQymNM6FVRM
Technique(s) : 10 astuces cumulées sur un même pad : enveloppe, filtre MG Low 12, unison, couche de bruit, LFO sur le pitch, LFO dont la vitesse est modulée, sub à l'octave haute, phaser, chorus, EQ, image stéréo.
Transcription : oui (EN, auto)
- 0:25 ENV1 : attack + pente adoucie, decay ~2–2,5 s, release ~360 ms
- 0:52 filtre MG Low 12, ENV1 → cutoff
- 1:09 OSC A et B désaccordés, unison 5 chacun, B +1 oct
- 1:40 oscillateur noise (nom [ASR ?] « air can one »), one-shot, keytrack, ~+24 demi-tons (interp.), envoyé dans le filtre
- 2:19 LFO1 (rate non synchronisé, lent, lissé) → fine de B (montant négatif) + level de B + level du noise
- 3:11 LFO2 en mode envelope → rate du LFO1, montant ~20, rate du LFO2 ~2,5 (non sync)
- 4:10 sub en triangle, +2 oct, envoyé dans le filtre ; LFO1 → level du sub
- 5:06 phaser à rate très lent, mix ~25 % ; 5:47 chorus mix ~40 %, rate baissé
- 6:29 EQ : low cut ~170 Hz, Q baissé ; 7:28 Ozone Imager : mono sous 180 Hz, médiums resserrés, aigus élargis
- 8:59 bonus RC-20 (noise, wobble, distortion, magnetic, EQ)
- Genre : house (deep, melodic et garage house cités).
À vérifier à l'écran : 0:25 courbe et valeurs de l'ENV1 ; 1:40 nom exact de l'échantillon noise ; 2:19 forme du LFO1 et montants dans la matrice ; 3:11 réglages du LFO2 ; 4:10 octave et level du sub.

### PA-03 SERUM Tutorial | Pad Sound, Afro House | Keinemusik - Tutorial — The Sound Design Channel (Leo Lauretti / Abstract Music Lab), 9:15, 2024-09-08, outil : Serum 1
URL: https://www.youtube.com/watch?v=EIn9k6cDRCo
Technique(s) : pad afro house façon Keinemusik (« Nostalgia ») : sine et wavetable avec beaucoup d'unison, LFO sur la position de wavetable synchronisé à la mesure, couche de bruit avec son enveloppe et un pan qui bouge, MG Low 18, chaîne d'effets compresseur → delay → reverb → EQ.
Transcription : oui (EN, auto)
- 1:04 OSC A : sine (Basic Shapes), unison 9, detune légèrement baissé
- 1:22 OSC B : wavetable « Basic Weird -1 » [ASR ?], unison 12, detune baissé, la position de wavetable change pour un son proche d'une saw
- 1:55 LFO1 → WT pos de B, synchronisé à la mesure (wobble lent)
- 2:27 noise « Inharm 5 » [ASR ? « inarm five »], level 0 ; ENV2 → level du noise (attack long, release long)
- 3:26 LFO2 triangle en BPM → pan du noise (bipolaire)
- 3:57 ENV1 : attack long avec courbe, sustain baissé, release monté
- 4:38 filtre MG Low 18 sur A + B + noise, cutoff bas, résonance et drive un peu montés, note (keytrack) → cutoff, petit montant
- 5:29 effets : compresseur multibande (release et gain montés, mix bas, bandes ajustées) → delay 1/8 des deux côtés, feedback ~40 [ASR ?], wet monté → reverb (wet et decay montés, low cut, spin et depth montés) → EQ (low cut presque total, bell ~700 Hz, Q ~59 [ASR ?], en coupe)
- Écouté dans un contexte avec sidechain
- Genre : house (afro house, Keinemusik).
À vérifier à l'écran : 1:22 nom de la wavetable de B et WT pos ; 2:27 nom du noise et ADSR de l'ENV2 ; 3:57 ADSR de l'ENV1 ; 4:38 cutoff, résonance et drive ; 5:29 valeurs du delay et de l'EQ.

### PA-04 SERUM 2 Tutorial | Stunning LFO Pad | Progressive and Melodic House | Anjunadeep — The Sound Design Channel (Leo Lauretti), 7:42, 2025-11-10, outil : Serum 2
URL: https://www.youtube.com/watch?v=zZOAXW9wyd0
Technique(s) : pad rythmique par LFO façon Anjunadeep (« Moongate ») : arpégiateur en mode chord, filtre ladder fermé et ouvert par plusieurs LFO, LFO en marches sur l'octave, bus FX Serum 2 (delay ping-pong, Convolve).
Transcription : oui (EN, auto)
- 0:39 shader désactivé ; 0:44 Arp en mode « chord », 1/16 (défaut)
- 0:56 OSC A : wavetable « Serum Analog Mother » [ASR ?], volume baissé
- 1:15 filtre ladder (« MS ladder » [ASR ? « mees ladder »]) sur A, cutoff tout en bas
- 1:29 LFO1 → cutoff, grille 3 [ASR ?], rate 1/2, forme dessinée
- 2:06 LFO2 saw descendante en mode envelope, 1/16 → cutoff
- 2:40 LFO3 en BPM 1/2, forme en marches (Shift) → octave de l'OSC A, unipolaire, petit montant
- 3:08 résonance et drive montés, pas de smoothing
- 3:18 envois vers Bus 1 et Bus 2
- 3:29 Bus 2 : delay 100 % wet, ping-pong, « 1/32 » [ASR ?], feedback monté, puis coupes à l'EQ
- 4:14 Bus 1 : Convolve, réponse impulsionnelle d'usine « Weird > Moon reflection », wet 100 %, gain de l'IR baissé, EQ
- 5:14 Main : EQ low cut → distorsion tube (wet bas) → reverb Hall (decay monté, low et high cut) → EQ (low cut + bell) → compresseur (gain)
- Genre : house (progressive / melodic house, Anjunadeep).
À vérifier à l'écran : 0:56 nom de la wavetable ; 1:15 type exact du filtre ; 1:29 forme du LFO1 ; 2:40 montant du LFO3 sur l'octave ; 3:29 division et feedback du delay du Bus 2.

### PA-05 How To Make Your Own Lush Pad In The Style Of Selected in Serum Synth (Free Serum Preset Pack) — The Preset Bros (Josh), 10:07, 2023-09-07, outil : Serum 1
URL: https://www.youtube.com/watch?v=MFQTRQZmxo4
Technique(s) : pad deep house façon label Selected (référence « Interesante ») : sine pliée avec Bend et FM depuis A, noise, MG Low 18, trois enveloppes (ampli, cutoff, drive de la distorsion), Hyper/Dimension, distorsion Diode, reverb Hall. C'est le tutoriel le plus chiffré du lot.
Transcription : oui (EN, auto)
- 0:41 gros low cut avant la reverb externe (Respace (interp.))
- 1:43 OSC A : « Analog BD sine » [ASR ?], WT pos au max, warp Bend+/- −32 %, level 67
- 1:58 OSC B : « Basic MCB » [ASR ?], WT pos au max, unison 3, detune 0,06, FM depuis A 39 %, level 73
- 3:01 noise « J106 high pass » [ASR ?], level 22
- 3:09 filtre MG Low 18, cutoff 469 Hz, résonance 22 %, drive 22 % (A, B, noise)
- 3:25 ENV1 : attack 41 ms (dit « release » par erreur [ASR ?]), decay 1,76 s, sustain −5,7 dB, release 1,20 s
- 3:43 ENV2 : A 25 ms, D 1,79 s, S 65 %, R 632 ms → cutoff, montant 15
- 4:32 ENV3 → drive de la distorsion, montant 39 ; 4:43 LFO1 → fine de A ~20 ; 5:02 LFO2 → level
- 5:12 Hyper/Dimension : mix Hyper 16 [ASR ?], Dimension 9, mix 20
- 5:25 distorsion Diode 1, filtre pré-distorsion (passe-haut (interp.)), drive 52 %, mix 34 %
- 6:18 EQ : atténuation des graves + notch (avec l'idée d'un LFO sur la fréquence) ; 7:20 chorus ; filtre placé après la distorsion
- 7:48 reverb Hall mix 61 % ; 8:06 conseils pour personnaliser
- Genre : house (deep house, Selected).
À vérifier à l'écran : 1:43 nom de la wavetable de A ; 1:58 nom de la wavetable de B ; 3:01 nom du noise ; 3:25 attack de l'ENV1 ; 5:25 réglage du filtre pré-distorsion.

### PA-06 Serum Tutorial - OCULA Style LFO Pad — Furcloud, 4:18, 2023-05-25, outil : Serum 1
URL: https://www.youtube.com/watch?v=HTGQFo74-pQ
Technique(s) : pad rythmé par LFO façon OCULA : deux saws analogiques, LFO 1/16 sur le cutoff, vibrato, LFO sur la WT pos, portamento.
Transcription : oui (EN, auto)
- 0:41 filtre activé sur A + B (type non dit)
- 0:56 OSC A : « Analog Saw Rounded » [ASR ?], WT pos ~18
- 1:13 OSC B : même wavetable, +1 oct, detune unison 0,03, WT pos 8, level 50 %
- 1:43 ENV1 : attack 9 ms, release ~350 ms
- 2:02 LFO1 → cutoff, rate 1/16, avec rise (montée progressive du LFO (interp.))
- 2:33 LFO2 → fine de A et B, montant 13 (vibrato)
- 2:55 LFO3 → WT pos de B, rate 1/2
- 3:09 portamento ~50–55 ms ; 3:26 coupes à l'EQ ; 3:45 reverb
- Genre : house (melodic house, OCULA / Anjunadeep).
À vérifier à l'écran : 0:41 type de filtre et cutoff ; 1:13 nombre de voix d'unison ; 2:02 forme du LFO1 et montant ; 3:45 réglages de la reverb.

### PA-07 SERUM Tutorial | Analog PAD, Melodic House & Techno | Stephan Bodzin - Tutorial — The Sound Design Channel (présenté par Furcloud), 6:57, 2023-04-09, outil : Serum 1
URL: https://www.youtube.com/watch?v=LA26gLKjQkc
Technique(s) : pad analogique façon Bodzin : A et B à l'octave pannés à droite, sub saw panné à gauche, bruit blanc, deux enveloppes lentes, filtre FX animé par LFO, Chaos → Master Tune pour la dérive analogique.
Transcription : oui (EN, auto)
- 1:02 filtre sur A, B, noise et sub (type non dit), drive ~15 %, résonance 0 %
- 1:33 OSC A : Analog > « Basic Shapes » [ASR ?], WT pos ~4, pan 10 R, level ~30 %
- 2:14 OSC B : +1 oct, pan 10 R, level ~30 % ; 2:41 SUB actif en saw, pan −10
- 2:57 noise Analog > « White » [ASR ?]
- 3:12 ENV1 : attack ~500–570 ms [ASR ? « 500 and 7D »], release ~960–970 ms
- 3:55 ENV2 → cutoff : attack 900 ms, release ~670 ms
- 4:40 chorus mix ~30 % ; reverb size 60 %, mix ~36 % (ou 30), high cut 50 %, low cut ~30 %
- 5:32 filtre FX + LFO → cutoff du filtre FX, rate 1 mesure
- 6:01 Chaos 1 → Global Master Tune, montant ~4 (dérive analogique)
- Genre : house (melodic house & techno, Afterlife / Bodzin).
À vérifier à l'écran : 1:02 type de filtre et cutoff ; 1:33 nom de la wavetable ; 3:12 valeur exacte de l'attack de l'ENV1 ; 3:55 montant de l'ENV2 sur le cutoff ; 6:01 rate du Chaos.

### PA-08 How To Create Deep House SYNTHS Like Gaskin 🎹 — SOTA Sounds, 12:50, 2025-09-01, outil : Serum (Serum 2 probable, à vérifier)
URL: https://www.youtube.com/watch?v=ROx6_4kZ4lE
Technique(s) : deux pads minimal / deep house façon Gaskin (« Closer ») : saw avec unison large et phaser, puis une wavetable modulée par un LFO de 4 mesures sur la WT pos et le warp. Les pads occupent 0:54–5:58 ; le reste de la vidéo traite des keys, du piano, d'un vocal synth et d'un pluck.
Transcription : oui (EN, auto)
- 1:47 Pad 1 : saw, comparaison unison 16 / 7 (7 semble retenu (interp.)), detune + blend ; enveloppe : attack court, decay et release plus longs
- 2:41 le phaser transforme le son
- 2:51 Pad 2 : wavetable « MB saw » [ASR ?], unison + detune, enveloppe similaire
- 3:17 enveloppe lente (montée et chute) → cutoff
- 3:36 LFO de 4 mesures → WT pos + warp
- 3:53 effets : delay, filtre qui coupe les aigus, grande reverb (size et decay), EQ
- 4:34 MIDI : Cm (+ F add11) et Bbm7
- 11:56 Auto Pan utilisé comme ducking à la place d'un sidechain
- Description : preset Serum gratuit du pad Gaskin, pack pour Serum 2
- Genre : house (minimal / deep house, Gaskin, Up The Stuss).
À vérifier à l'écran : 1:47 interface Serum 1 ou 2 et nombre de voix retenu ; 2:41 réglages du phaser ; 2:51 nom de la wavetable du Pad 2 ; 3:36 montants du LFO sur la WT pos et le warp.

### PA-09 How to Make Liquid D&B Pads (with Serum, No Music Theory Needed) — STRANJAH, 17:06, 2020-02-11, outil : Serum 1
URL: https://www.youtube.com/watch?v=sr31vDqnpjg
Technique(s) : pad liquid construit pas à pas : saw +2 oct, accords empilés (triade, 7e, 9e) sans théorie, LP avec ENV2 et LFO sur le cutoff, unison, wavetable spectrale en couche, basse doublée dans le MIDI.
Transcription : oui (EN, auto)
- 0:55 init, saw sur l'OSC A, +2 oct
- 2:22–6:08 accords : basse transposée en La mineur, triades (1-3-5) empilées, ajout de la 7e et de la 9e
- 6:14 filtre LP (plus de pôles = son plus rond), résonance + drive pour épaissir, master baissé
- 7:10 ENV2 → cutoff, attack monté (balayage), cutoff et montant ajustés
- 8:26 LFO1 → cutoff, rate 1/4 puis BPM désactivé
- 9:35 reverb + EQ ; 10:44 unison ~6, phase aléatoire laissée haute
- 11:42 comparaison sine / saw / triangle / carré : la saw est préférée
- 12:20 OSC B : wavetable spectrale, envoyée dans le filtre, +2 oct (ou +1), unison
- 13:28 EQ Eight : coupe sous 220 Hz (ou 110) ; 14:22 MIDI : fondamentales doublées à l'octave basse, quinte en option
- Genre : DnB (liquid, présenté comme la partie 3 d'une série liquid).
À vérifier à l'écran : 6:14 type de filtre (12 / 24) et cutoff ; 7:10 ADSR de l'ENV2 ; 8:26 rate libre du LFO1 ; 12:20 nom de la wavetable spectrale.

### PA-10 How to Make Lush, Dreamy Pads in Serum 2! (Step-by-Step Guide) — DNB Academy, 10:52, 2025-03-25, outil : Serum 2
URL: https://www.youtube.com/watch?v=u4DPfvDX7Sg
Technique(s) : pad Serum 2 à trois couches : wavetable d'accords sur A et B, oscillateur granulaire C en boucle inversée, deux filtres, nouveau noise « Rain », Splitter grave/aigu dans les effets, macros sur les cutoffs.
Transcription : oui (EN, auto)
- 0:13 rappel des types d'oscillateur (wavetable, multisample, granular, spectral)
- 0:44 OSC A : tables S2 > Digital > « Chords » [ASR ? « code »], octave −4
- 1:19 OSC B : même wavetable, octave −3 puis semi −12, levels ajustés, unison sur B, detune baissé
- 2:42 OSC C granulaire : sample de la suite DNB Academy, zone de lecture réduite, boucle inversée, octave haute, X-fade, random, scan rate, density, pan aléatoire
- 4:31 Filter 1 sur A + B, résonance ; 5:38 Filter 2 sur C, résonance
- 6:00 enveloppe : attack long, sustain haut, release long
- 6:19 noise « Rain 100 High » (nouveau dans S2), level ajusté, pas en one-shot
- 7:05 effets : Convolve, chorus avec mix baissé, Splitter grave/aigu à ~300 Hz (graves : légère distorsion ; aigus : delay + courbe), mix baissé
- 8:13 Macro 1 → cutoff du Filter 2 (osc C), Macro 2 → cutoff du Filter 1 + résonance
- 9:28 EQ low cut
- Genre : DnB (chaîne DNB Academy, usage liquid / ambient), sans sous-genre nommé.
À vérifier à l'écran : 0:44 nom exact de la wavetable ; 2:42 paramètres du granulaire ; 4:31 types des Filter 1 et 2 ; 6:00 ADSR ; 7:05 réglages du Splitter.

### PA-11 Atmospheric DnB Pads Deconstructed — Tim Cant, 20:22, 2024-07-15, outil : Serum 1 (partie Serum 0:49–5:42 ; le reste = Roland D-50, Korg M1, JV-1080)
URL: https://www.youtube.com/watch?v=U5526pQUQaM
Technique(s) : pad atmosphérique minimal en 7 points : polyphonie au maximum, ADSR longs, saw, LP avec keytrack, ENV2 longue sur le cutoff, résonance, unison, accords étendus jusqu'au m11.
Transcription : oui (EN, auto)
- 0:57 voix au maximum (polyphonie) pour les accords étendus
- 1:11 enveloppe d'ampli : attack et release longs ; 1:19 saw par défaut
- 1:31 filtre LP activé, keytrack activé
- 1:54 ENV2 → cutoff : attack, decay et release très longs (balayage)
- 2:14 résonance montée ; 2:27 voix d'unison + detune pour la largeur
- 3:00 delay (Ableton Delay) et reverb (FabFilter Pro-R) hors de Serum
- 3:30 accords : m → m7 → m9 → m11 ; 4:35 récapitulatif des 7 points
- 5:10 idées en plus : LFO sur le cutoff, phaser
- Genre : DnB (atmospheric DnB, d'après le titre).
À vérifier à l'écran : 1:11 temps d'attack et de release ; 1:54 ADSR et montant de l'ENV2 ; 2:27 nombre de voix et detune ; 1:31 type de LP.

### PA-12 How To Make PADS Like LENZMAN - WORDSWORTH | Serum Tutorial — DNB Academy (Paulo), 5:41, 2021-07-18, outil : Serum 1 (+ Auto Pan Ableton)
URL: https://www.youtube.com/watch?v=_k_4oSt0alE
Technique(s) : pad liquid façon Lenzman : deux oscillateurs avec beaucoup d'unison, B à l'octave, LP 24, LFO de 2 mesures sur le cutoff, chaîne d'effets riche, trémolo rythmique par Auto Pan.
Transcription : oui (EN, auto)
- 1:11 init, accord Mi mineur 7 ; 1:22 sub actif, OSC A en sine (interp., [ASR ? « soundwave »]), même chose sur B
- Beaucoup d'unison sur les deux, B +1 oct
- 1:40 filtre 24 dB/oct (LP) sur tout, volume baissé
- 1:52 LFO → cutoff, rate 2 mesures [ASR ? « toolbars »], forme lisse dessinée
- 2:17 Hyper/Dimension ; EQ : bell boost avec Q baissé, fréquence de la bande modulée (« map this », source non nommée) + 2e bell qui monte les aigus
- 2:44 phaser avec la fréquence tout en bas ; chorus
- 3:06 compresseur multibande (release et gain montés) ; reverb
- 3:26 après Serum : EQ (graves baissés, médiums montés), Auto Pan (amount 100, phase 0, rate 1/16, offset 180, mix baissé) pour un trémolo rythmique
- Genre : DnB (liquid, Lenzman / Metalheadz, The North Quarter).
À vérifier à l'écran : 1:22 forme des oscillateurs et nombre de voix ; 1:52 rate exact du LFO ; 2:17 source de modulation de l'EQ ; 3:06 réglages du compresseur multibande.

### PA-13 Deep Liquid Drum & Bass Tutorial | Serum, Ableton, Pad Design and Beat — STRANJAH, 11:31, 2020-09-03, outil : Serum 1 (+ Ableton Chord)
URL: https://www.youtube.com/watch?v=2otsi7S5cwA
Technique(s) : pad liquid sombre : wavetable spectrale « glassy » doublée à l'octave basse, sub saw, Hyper/Dimension, chorus, LFO en enveloppe → Master Tune pour un glissé de pitch à l'attaque.
Transcription : oui (EN, auto)
- 1:06 preset du MIDI effect Chord d'Ableton (nom [ASR ?]) = triade mineure
- 1:54 la saw convient, mais les wavetables spectrales sont plus glassy ; choix « Solid Phase 1 » [ASR ?], WT pos ajustée
- 2:43 unison 6, detune baissé ; 3:00 OSC B : même wavetable −1 oct, unison
- 3:31 attack de l'ampli ; 3:40 sub −2 oct en saw
- 4:00 Hyper/Dimension : retrig activé, rate et detune baissés, mix Dimension monté
- 4:31 chorus : rate lent, delay court [ASR ? « decay »], LPF tout ouvert, feedback et mix montés
- 5:19 EQ : low shelf / coupe des graves + LP sur les aigus avec résonance
- 6:05 reverb : mix monté, low cut, size / decay
- 6:29 LFO1 en mode envelope 1/4, forme du milieu vers le bas ; matrice LFO1 → Master Tune −12 (ou −5 / −9) = glissé de pitch vers le haut à l'attaque
- 8:00 suite (hors pad) : batterie, basse, voix R&B
- Genre : DnB (deep / dark liquid, Ivy Lab, Halogenix, Visages cités).
À vérifier à l'écran : 1:54 nom exact de la wavetable et WT pos ; 3:31 valeur de l'attack ; 4:31 réglages du chorus ; 6:29 forme du LFO1 et montant sur Master Tune.

### PA-14 Beautiful Pads with Serum 2 — Virtual Riot, 15:28, 2025-09-23, outil : Serum 2 (titre affiché auto-traduit en FR : « Des pads magnifiques avec Serum 2 »)
URL: https://www.youtube.com/watch?v=oW4C7txJEgM
Technique(s) : pads à partir de samples dans l'oscillateur spectral de Serum 2 en mode Manual (gel de l'audio façon paulstretch), position modulée par LFO S&H lissé (texture granulaire), enveloppe sur la position, empilement de couches.
Transcription : oui (EN, auto)
- 1:06 oscillateur spectral + loop mélodique (song starter stacks) glissée dedans
- 1:38 mode one-shot → Manual : le bouton règle la position et fige l'audio
- 2:05 position calée sur un accord, puis compresseur + delay + reverb
- 2:34 filtre spectral pour couper les graves trop forts ; 2:49 OSC B : 2e sample en Manual, même tonalité, aigus filtrés
- 3:39 LFO → position : S&H, lissé, rapide, faible profondeur (effet granulaire)
- 4:54 violoncelle d'usine en spectral, Manual ; 5:37 ENV → position (de la fin vers le début, montée) + enveloppe d'ampli qui retombe
- 6:10 S&H plus lent et plus fort ; 8:10 piano + forme de LFO dessinée sur la position
- 9:26 LFO lent sur la position = progression d'accords
- 10:33 sample de basse en spectral Manual ; 10:55 clic droit sur position → phase lock = son plus net
- 11:17 nouveau pad à partir de zéro : 3 samples empilés, LFO aléatoires pour le flutter
- 13:51 unison 3, detune baissé, stack 12 (une voix à +1 oct) ; compresseur, delay, reverb, filtre spectral pour éclaircir
- Genre : dubstep / melodic bass, mais ce n'est qu'une interprétation : aucun genre n'est nommé, seul l'artiste (Virtual Riot) est associé au dubstep.
À vérifier à l'écran : 1:38 mode Manual et emplacement du bouton de position ; 3:39 rate, smooth et profondeur du LFO S&H ; 5:37 montant de l'ENV sur la position ; 13:51 réglages de l'unison et du stack.

### PA-15 Future Bass Fat Chord Synth Pad with Serum Vst - Sound Design from Scratch — Production Music Live, 13:47, 2015-08-26, outil : Serum 1
URL: https://www.youtube.com/watch?v=ePFO8uZ6LTs
Technique(s) : pad d'accords future bass épais : saws avec unison, sub triangle, clic de kick à l'attaque, filtre German LP sur macro, LFO en enveloppe → level de A (effet « wawa »), ENV2 → mix de la reverb.
Transcription : oui (EN, auto)
- 1:19 OSC A et B activés, « M saw » [ASR ?] ; 1:53 OSC B : wavetable Digital « long Grease » [ASR ?], WT pos au max / pos 3, volume baissé (saturation)
- 2:40 oscillateur +1 oct ; 2:51 unison 4 sur A, detune et blend par défaut ; 3:11 unison sur B
- 4:09 SUB −1 oct triangle ; 4:30 noise « Attack Kick 13 » [ASR ?] = clic à l'attaque
- 5:22 filtre German LP (A, B), un peu de drive, cutoff bas, résonance montée ; 5:57 Macro « Cutoff » → cutoff
- 6:38 level du sub ; 7:17 sub en Direct Out
- 7:52 effets : chorus (mix baissé), reverb, compresseur, EQ high shelf monté
- 9:27 LFO1 forme dessinée (montée lisse), rate 1/4 triolet [ASR ? « 14 + triplet dot »], mode envelope → level de l'OSC A en négatif = « wawa »
- 11:50 ENV2 → mix de la reverb : delay 800 ms, decay monté, sustain 100 %
- 12:54 EQ Ableton low cut, compresseur
- Genre : dubstep au sens large (future bass) : la vidéo vient à la place d'un tutoriel melodic dubstep qui manque.
À vérifier à l'écran : 1:53 nom de la wavetable de B ; 4:30 nom du noise ; 5:22 cutoff et résonance ; 9:27 rate exact du LFO1 ; 11:50 ADSR de l'ENV2.

---

### Écartés
- nbS1pT8V7YU (Olean's House, pads house classiques, 18:47) : plusieurs synthés ; la partie Serum (3:41–6:51, unison 16) est courte et générique.
- IbdncSrV2Nc (Matt Flanc, « Serum | How to make pads ») : pad pour musique de jeu vidéo, survol d'un preset de pack, presque aucune valeur, hors genres.
- G6v72ck8uLw (Drayen, pad future bass, 15:28) : 7 min de discussion et de voicings, partie Serum faible (unison 3, osc −1 oct, LFO → cutoff).
- H4YcXoEONLU (Ash // From Bedroom 2 Banger, accords melodic dubstep façon Seven Lions) : empilement multi-plugins (Serum chaos saw, chœur, Vital), plutôt « chords » / supersaw qu'un pad designé dans Serum.
- OK0_prnX2M8 (Spy Nasaurus, pad dubstep heavy en fond) : aucune parole, Serum + Vital.
- jo7FFv8E43o (Arylith, accords melodic dubstep avec seulement Serum, 2018) : presets chargés, presque aucun réglage dit, surtout du traitement dans FL Studio.
- Résultats de recherche vus mais non retenus, car ce sont des leads, des morceaux complets ou d'autres types de son : 1rYTKTXbBtg, dT2x_tF2upA (leads melodic dubstep) ; pSClfd9yqoY, RlvDcAN5h3E (morceaux melodic dubstep complets) ; -HV4lYh7yjg, BOLa6T_Yr_o, OdInZtaxqGY (SDC : pad vocal, noise pad, LFO lead/pad, melodic techno, non étudiés).

### Manque
- 15 vidéos retenues : 8 house (deep, afro, melodic / progressive, minimal), 5 DnB (liquid ×3, deep liquid, atmospheric) et 2 en dubstep au sens large (PA-14 sans genre nommé, PA-15 future bass).
- Il manque au moins un vrai tutoriel de pad melodic dubstep fait dans Serum. Les vidéos trouvées sont des leads, des empilements d'accords multi-synthés ou des morceaux complets. La DnB a donc 1 vidéo de plus que prévu (5 au lieu de 4).
- Aucun tutoriel en français n'a été retenu : aucun tuto FR de pad house / DnB / dubstep n'a passé le tri. Toutes les transcriptions sont des sous-titres automatiques en anglais.
- Les titres de PA-01 à PA-05, PA-08 et PA-15 ont été vérifiés par l'oEmbed de YouTube.

# Drone

## DRONE — drones, atmosphères et textures évolutives dans Serum

Agent DRONE (préfixe DR). Toutes les valeurs viennent des transcriptions automatiques (ASR) et des descriptions ; celles dont la transcription est douteuse sont marquées [ASR ?], mes déductions « (interp.) ». Peu de tutos de drone portent un label de genre : quand le genre n'est pas dit dans la vidéo, je l'indique comme une affectation de ma part.

Répartition : 8 « house » au sens large (afro, melodic house, melodic techno / breakdowns, progressive), 4 DnB, 3 dubstep / intro sombre. Quelques tutos house/techno labellisés existent, mais aucun drone n'est étiqueté explicitement « tech house », « bass house » ou « minimal ».

---

### DR-01 Serum Tutorial | Atmo Ambient Texture | Rüfüs Du Sol Style (Melodic House) — The Sound Design Channel (Furcloud), 6:18, 2021-10-19, outil : Serum 1
URL: https://www.youtube.com/watch?v=eJVh0McnQQk
Technique(s) : texture faite uniquement avec l'oscillateur Noise, filtrée et résonante ; le filtre est sculpté par une ENV et par un LFO dessiné, puis le tout est noyé dans les effets.
Transcription : oui (EN, auto)
- 1:07 seul l'oscillateur Noise est actif, les autres sont coupés ; 1:23 osc A off, filtre on
- 1:35 cutoff, résonance « 20 20 20 » [ASR ?], drive
- 1:58 niveau du Noise à 50 % ; 2:02 sample de noise « Soar Electricity » [ASR ? « store electricity »] (type goutte d'eau)
- 2:19 pitch du noise 18 ; 2:23 bouton clavier (keytrack) activé (interp.)
- 2:32 ENV1 : attack et release 1.27 (s ?) ; 3:00 ENV -> résonance
- 3:13 LFO1 forme dessinée à la main ; 3:48 rate 2 bars ; 3:57–4:03 LFO1 -> cutoff + résonance
- 4:26–5:05 FX : chorus mix 15 %, delay mix ~43 %, reverb mix 50 %, high cut 0 %, low cut 0, decay 8 s ; 5:28 EQ off
- Genre : house (melodic house) : le titre dit « Rüfüs Du Sol Style (Melodic House) ». Texture d'intro ou de breakdown.
À vérifier à l'écran : 1:35 type de filtre et valeurs cutoff/res/drive ; 2:02 nom exact du sample de noise ; 2:32 réglages ADSR d'ENV1 ; 3:13 forme du LFO1 ; 4:48 paramètres de la reverb.

### DR-02 SERUM Tutorial | Atmo Pad, Afro House | Maz, Keinemusik — The Sound Design Channel (Leo Lauretti), 12:51, 2025-03-15, outil : Serum 1
URL: https://www.youtube.com/watch?v=AmlnEO82a7Q
Technique(s) : FM de B vers A, couche de noise « verre », LFO en escalier sur le niveau (petites « gouttes »), modulation de LFO par un LFO, delay et reverb lourds.
Transcription : oui (EN, auto)
- 1:19 osc A WT « Dist Sub » ? [ASR ? « disc sub dis »], niveau très bas (1:31) ; 1:38 osc B WT « Cream » [ASR ?], niveau un peu bas
- 1:50–2:00 osc A FM from B, puis FM augmentée ; 2:09–2:15 osc B : unison un peu monté, detune baissé, position WT un peu montée
- 2:24 warp « Symmetry Plus » ? [ASR ?], un tout petit peu
- 2:34 noise « Attacks > Misc > Glass Lid 5 » [ASR ?], keytrack on, pitch monté, niveau monté
- 3:02 sub sinus niveau 0, +1 octave
- 3:16–4:00 ENV1 : attack très montée, courbe, sustain un peu baissé, decay baissé, release montée
- 4:04 ENV2 -> FM from B (agressif), attack un peu montée, sustain plus bas, release montée
- 5:03 filtre MG12 [ASR ? « mg12 »] sur A+B, cutoff un peu baissé, drive monté ; 5:22 ENV2 -> cutoff
- 5:34–6:15 LFO1 triangle 2 bars (BPM/anchor off) -> detune de B (peu) + pan du noise (bipolaire)
- 6:29–8:06 LFO2 et LFO3 en escalier, trig, 1/4 ; LFO4 rampe montante 4 bars, qui module les LFO2/3 (« LFO bus » [ASR ?])
- 8:10–9:01 LFO2 -> niveau (pas 100 %), LFO3 -> niveau = « petits plucks »
- 9:06–10:06 reverb : low cut monté, spin & depth baissés, wet monté ; delay : feedback baissé, 1/8 et 1/8 pointée, fréquence beaucoup montée, Q baissé, mix ++
- 10:10–10:39 EQ : low cut ~35 Hz + high shelf boost ; 10:45–11:08 filtre FX MG Low 12 [ASR « Melo 12 »] modulé par ENV2
- 11:11–11:37 compresseur : threshold baissé, ratio 3:1, attack/release courts, gain monté ; 11:42 chorus, mix faible
- Genre : house (afro house, Keinemusik) : c'est dit dans le titre. Atmo de breakdown, « gouttes de pluie » (preset « Raindrops »).
À vérifier à l'écran : 1:19 et 1:38 noms des wavetables ; 2:34 sample de noise ; 7:15 routage de LFO4 (LFO bus) ; 10:10 fréquences de l'EQ ; 11:11 réglages du compresseur.

### DR-03 How to Make Atmospheric Drones in Serum (+Preset & Midi) — Furcloud, 6:53, 2021-09-16, outil : Serum 1
URL: https://www.youtube.com/watch?v=VMJ1tFf1WQk
Technique(s) : deux wavetables analogiques, warp Bend modulé lentement, LFO rapide sur le cutoff et LFO de 8 bars sur le niveau de B, puis delay ping-pong et reverb longue. Le bas est coupé pour laisser la place à un autre pad.
Transcription : oui (EN, auto)
- 1:05 filtre on, osc A et B routés dedans (type de filtre non dit)
- 1:18–1:24 ENV1 release ~2.40 (s)
- 1:35–1:52 osc A +1 octave, WT « Analog > Analog_BD_Sin » [ASR « analog bd sign »], position WT ~130 (milieu)
- 1:55–1:59 unison 4, detune ~0.08
- 2:08–2:25 warp Bend +/-, modulé par une « envelope » [ASR ? c'est plutôt un LFO, rate ~4 bars]
- 2:39–2:53 osc B WT « Analog > 4088 » [ASR « 4040 4088 »], position ~214
- 3:17–3:33 LFO1 -> cutoff, rate 1/16 ; 3:46 ENV1 -> cutoff aussi
- 4:13–4:26 LFO3 -> niveau de l'osc B, rate 8 bars
- 4:47–5:03 delay mix ~38 %, ping-pong
- 5:13–5:24 reverb mix ~50 %, decay ~8 s, high cut 0 %
- 5:34–5:47 EQ : coupe des basses
- Genre : house (melodic house). Affectation de ma part : la chaîne Furcloud est orientée melodic house / Rüfüs Du Sol (la description renvoie vers des presets « Melodic House » et un pack Rüfüs Du Sol).
À vérifier à l'écran : 1:05 type de filtre et cutoff ; 2:12 source et forme de la modulation du warp ; 2:42 nom exact de la WT de l'osc B ; 3:22 forme et profondeur de LFO1 ; 5:34 réglages de l'EQ.

### DR-04 SERUM 2 Tutorial | Cinematic Atmosphere for Breakdowns | Melodic Techno — The Sound Design Channel (Leo Lauretti), 10:57, 2025-04-27, outil : Serum 2
URL: https://www.youtube.com/watch?v=mTP1LcQVqpQ
Technique(s) : deux saws très peu fortes avec FM depuis l'osc Sub, filtre passe-haut par oscillateur (Serum 2), trois LFO très lents (jusqu'à 32 bars) en cascade sur le cutoff, rate du LFO modulé par une ENV. Mono + portamento, puis une longue chaîne d'effets avec Splitter Mid/Side.
Transcription : oui (EN, auto)
- 1:04 init, osc A saw par défaut : unison un peu monté, detune très baissé, niveau baissé, fine un peu baissé (fine de B monté -> stéréo)
- 1:31 FM from Sub ; le sub est une saw, niveau 0, FM du sub d'abord à fond en bas puis modulée
- 1:53 filtre HP sur l'osc A (filtre par oscillateur de Serum 2, interp.)
- 2:03–2:32 osc B saw par défaut « four waves » (4 voix d'unison [ASR ?]), detune monté, fine monté, niveau très bas, HP ; 2:41 pas de warp
- 2:47 LFO1 en mode envelope, 2 bars, triangle -> FM from Sub
- 3:08 ENV1 : attack très haute -> M2 (macro ?) [interp.], release montée
- 3:46 filtre sur A et B [ASR ? « sub A et B »], cutoff baissé
- 3:59 LFO2 4 bars, retrig, smooth (devient un sinus) -> cutoff
- 4:42 LFO3 32 bars, rise 2 bars, delay 1 bar, smooth -> cutoff ; 6:02 forme du LFO3 redessinée
- 5:30 ENV1 -> rate d'un LFO ; 5:52 mono + un peu de portamento
- 6:37 Hyper mix « all the way down », Dimension wet baissé
- 6:56 EQ : low cut + cloche en coupe (boue)
- 7:36 compresseur en mode single : threshold très bas, attack/release plus courts, gain monté
- 8:03 reverb Hall : low cut monté, size montée, decay très long, wet ++, spin depth monté
- 8:48 distortion Tube : drive haut, wet baissé
- 9:04 delay ping-pong 1/4 : feedback monté, freq montée, Q baissé, wet ++
- 9:41 Splitter Mid/Side (Serum 2) -> EQ sur le Side, low cut ~32 [ASR ?]
- 10:11 filtre d'oscillateur « MG Low 18 »
- Genre : melodic techno (titre), à placer en breakdown ou avant un drop de melodic house/techno. Je le range dans la famille house.
À vérifier à l'écran : 1:31 réglages FM from Sub ; 3:08 cible exacte d'ENV1 (M2 ?) ; 4:42 réglages de LFO3 ; 8:03 valeurs de la reverb Hall ; 9:41 réglage du Splitter et de l'EQ du Side.

### DR-05 SERUM Tutorial | CRAZY Noise Pad, Melodic Techno | Anyma, Afterlife - Tutorial — The Sound Design Channel, 11:25, 2023-11-22, outil : Serum 1
URL: https://www.youtube.com/watch?v=BOLa6T_Yr_o
Technique(s) : une seule note tenue, rendue animée par l'arpégiateur Ableton (random, rate automatisé). Position WT et warp Bend modulés par LFO, LFO très rapide sur l'osc B (bourdonnement), noise blanc, vélocité routée vers cutoff/niveau/pan, Macro de cutoff automatisée avant le drop.
Transcription : oui (EN, auto)
- 1:34 MIDI : une seule note tenue (fondamentale F)
- 1:51–2:40 arpégiateur DAW (Ableton Arp) en « random once », rate en « free », automation du rate lent -> rapide -> lent (effet de roulement)
- 2:57–3:08 osc A WT « Mellow but Unstable » [ASR ? « mellow but in stable »], position vers le milieu, LFO bipolaire (shift+option clic) -> position WT
- 3:23–3:28 unison 2 voix, detune bas, +1 octave
- 3:37–3:56 warp Bend + LFO
- 4:08–4:20 osc B « Basic CJW » [ASR ? peut-être Basic Shapes], position WT à moitié, LFO2 de forme perso très rapide -> position WT (buzz)
- 4:36–4:49 osc B -1 octave, unison 2, detune un peu
- 5:17 filtre + drive
- 5:27–5:56 noise « ARP White » [ASR ?], phase + rand
- 6:16 ENV1 : attack court, release assez long, un peu de sustain
- 6:44–7:15 ENV2 -> cutoff, forme plucky (sustain bas, decay plus court, release plus long), peu d'ouverture
- 7:17 vélocité -> cutoff, -> niveau du noise, -> pan de l'osc et pan du noise
- 8:08 Hyper/Dimension : rate baissé, mix monté ; 8:29 Distortion Diode 2, mix bas ; 8:39 Reverb Plate filtrée ; 8:56 Delay ping-pong
- 9:06–9:48 Macro1 « cutoff » -> cutoff, automation en montée avant le drop
- Genre : melodic techno (Anyma / Afterlife, dit dans le titre). Tension avant drop dans de la melodic house/techno ; je le range dans la famille house.
À vérifier à l'écran : 2:57 nom de la WT de l'osc A ; 4:08 WT de l'osc B ; 4:20 forme du LFO2 ; 5:27 sample de noise ; 7:17 profondeurs de vélocité dans la matrice.

### DR-06 How To Make A Bass Drone / Pad in Serum 2 — Full Tilt Recordings, 20:08, 2025-04-04, outil : Serum 2
URL: https://www.youtube.com/watch?v=YqODGiqh7gk
Technique(s) : drone grave en mono avec deux saws (-2/-1 oct), MG Low 24 résonant, LFO lent sur le cutoff. Un 3e osc (Serum 2) et le noise sont envoyés vers le Bus 1 pour une chaîne d'effets parallèle. Une macro pilote les deux filtres pour les transitions.
Transcription : oui (EN, auto)
- 2:02–2:10 osc A basic saw -2 oct
- 2:18–2:42 filtre MG Low 24, un peu de résonance, un peu de drive ; 2:46 mono
- 2:54–3:19 osc B routé vers le filtre, -1 oct (une octave au-dessus de A) ; 3:26–3:37 unison de B à 11 voix
- 4:01 démo : drone d'une note sous un pad aérien ; 4:27 usage en intro/breakdown, ou en couche de basse
- 4:46 release courte + attack un peu montée (tick) ; 5:06 cutoff un peu monté = growl ; 5:22 portamento en option
- 5:52–7:11 LFO -> cutoff, 2 bars puis 1 bar, retrig, profondeur 55 % pour la démo puis ~6 % ; 7:18 la résonance est la clé
- 8:00 automation du cutoff pour transitions et buildups
- 9:27–9:44 osc C (nouveau dans Serum 2) à 0 oct (A -2, B -1, C 0) ; 9:53 unison de C large
- 10:06 noise « Juno Chorus »
- 10:41–11:06 osc C et noise : sortie Main off, 50 % vers Bus 1
- 11:30–12:39 FX Main (A+B) : distortion Diode 1, résonance réduite, mix
- 12:48 Mix : bus 1 ; 13:19–14:53 FX Bus1 : distortion, delay ping-pong feedback élevé, reverb Vintage size+ mix+, EQ HPF Q bas au-dessus du filtre principal, filtre Low 24
- 15:55–16:16 macro « Filter » -> cutoff du filtre principal + filtre du bus 1
- 17:13 niveau d'envoi vers le bus « ~3:00 » (position du potard) [ASR ?] ; 18:56 feedback et mix du delay montés pour la transition
- Genre : le label est orienté trance/progressive (la description parle d'Ethereal Trance Vocals et d'un pack progressive). Je l'affecte à la progressive/melodic house (affectation de ma part : drone sous les pads en intro et breakdown).
À vérifier à l'écran : 2:22 valeurs res/drive du MG Low 24 ; 6:04 forme du LFO ; 10:52 routage des sorties vers Bus 1 ; 13:32 réglages des FX du Bus1 ; 16:01 plages de la macro Filter.

### DR-07 How to Create the Perfect Drone in Serum 2? [Free Preset Inside] — Ghosthack, 14:01, 2026-02-25, outil : Serum 2
URL: https://www.youtube.com/watch?v=o_y0SyyUQf4
Technique(s) : méthode d'« évolution imprévisible ». Une WT est mise en mouvement, le filtre aussi, et chaque mouvement est perturbé par un 2e LFO aléatoire. Un 2e osc rejoint le même filtre, avec saturation, delay, reverb et phaser communs. Enfin, le rate d'un LFO est modulé par un autre LFO.
Transcription : oui (EN, auto)
- 1:33–1:41 osc A : S2 Tables > Analog > « at plates » [ASR ? nom de WT incertain]
- 2:16–3:03 LFO triangle -> position WT sur environ la moitié de la plage, mode free (pas retrig), rate baissé et passé de BPM en Hz
- 3:24–3:59 nouvelle forme « random curved » (preset de forme de LFO), petite profondeur -> position WT, rate baissé
- 4:08–4:30 passage dans le filtre (type non dit) + LFO triangle -> cutoff, profondeur réduite
- 4:52–5:15 LFO randomisé -> cutoff, vers le bas, faible profondeur
- 6:14–7:07 voicing (unison) ; LFO frais -> detune, clip de ~4 bars : largeur stéréo
- 7:19–8:13 osc B : WT « digital » (nom non dit), +1 octave, balayage de la position ; LFO de 4 bars -> position WT de B ; B routé vers le même filtre
- 8:15–8:30 LFO aléatoire du filtre -> aussi sur B (« delivery »)
- 8:46–10:18 FX : saturation, delay, reverb
- 10:29–11:08 phaser, monté plus haut dans la chaîne (traitement commun)
- 11:22–12:09 nouveau LFO, free, en Hz, très lent, forme randomisée -> rate du 1er LFO ; réglage de la plage dans la Matrix
- 12:37–13:17 récapitulatif de la méthode ; preset complet en téléchargement
- Genre : générique (aucun genre dit ; la description renvoie à des presets « Keta Rave »). Je l'affecte à la deep/minimal house (affectation de ma part : nappe de fond qui évolue sans être prévisible, utile pour les longs morceaux minimal ou deep). Peu de valeurs chiffrées.
À vérifier à l'écran : 1:41 nom exact de la WT ; 2:54 rate en Hz du LFO1 ; 7:28 WT de l'osc B ; 8:46 réglages saturation/delay/reverb ; 12:02 plage dans la Matrix.

### DR-08 SERUM 2: MAKING DRONES WITH SPECTRAL OSCILLATORS! — MAYGE, 7:11, 2025-03-19, outil : Serum 2
URL: https://www.youtube.com/watch?v=NASj9fdcn5s
Technique(s) : deux oscillateurs Spectral en mode Manual (sample figé en « wavetable »), warps Detune/Spread, Gate spectral, couche de vinyl crackle ; reverb Nitrous, Splitter M/S avec low cut sur le Side, OTT.
Transcription : oui (EN, auto)
- 0:08–0:18 osc A -> Spectral, sample aléatoire glissé ; 0:23 en C3 = lecture normale
- 0:35 mode Manual : le spectral devient une « wavetable » figée ; 0:56 chercher le sweet spot (position)
- 1:14–1:20 warp modes Detune et Spread
- 1:39–1:51 spectral Gate (retire les harmoniques faibles), off pour l'osc A
- 2:04–2:48 osc B Spectral, 2e sample, Manual, position, Gate on ; 2:58–3:01 octave down ; 3:12 warp Spread
- 3:35–3:41 foley : noise « vinyl crackle »
- 4:02–4:18 delay triplet ping-pong
- 4:24–4:47 reverb, nouveau mode « Nitrous », mode « Spin Space » ? [ASR ?], dry/wet 50 %
- 5:10–5:31 Splitter M/S -> EQ sur le Side, coupe sous 250 Hz
- 5:51–6:07 chorus, preset « K… » [ASR ?]
- 6:09–6:24 multiband comp, preset Factory « MB OTT » ? [ASR « mbot »]
- 6:28 release montée ; 6:50 crackle baissé
- Genre : générique (non dit). Je l'affecte à la deep/minimal house (affectation de ma part : drone tonal propre en stéréo, crackle vinyle, graves mono via le Splitter M/S, compatible avec un kick/sub house). Comble le manque de drones labellisés house.
À vérifier à l'écran : 0:56 position spectrale choisie ; 1:20 quantités de warp ; 4:24 mode et réglages de la reverb ; 5:14 fréquence de coupure sur le Side ; 6:09 preset du compresseur multibande.

### DR-09 How to Make Creepy Drones in Serum 2 — DNB Academy, 11:22, 2025-08-08, outil : Serum 2
URL: https://www.youtube.com/watch?v=K1SOw6vC324
Technique(s) : couches de samples dans les oscillateurs Sample de Serum 2 (pitch très bas, loops avant/arrière), grosse reverb à convolution, note tonale, ouverture du filtre en riser, filtres notch modulés par un LFO random.
Transcription : oui (EN, auto)
- 1:43 note E grave
- 2:01 section Sample de Serum 2, sample « spatial » ; 2:48 pitch -2 oct puis plus bas
- 3:25 grosse reverb à convolution « Long »
- 3:50 2e osc en couche : sample SFX plus aigu ; 5:14 3e couche « noises » sporadiques
- 5:46 one-shots passés en loop forward/reverse pour faire des textures
- 6:24 ajout d'une note tonale
- 7:01 ouverture du filtre dans le temps -> riser de suspense en intro
- 7:45 multiband : boost des aigus pour le riser ; 8:04 HPF
- 8:40–9:03 filtres notch + LFO random
- 9:41 usage : intros « droney » en « atmospheric dark drum and bass », qui laissent place au drop
- Genre : DnB (dark / atmospheric) : c'est dit à 9:41 et c'est le sujet de la chaîne.
À vérifier à l'écran : 2:01 nom du sample ; 2:48 valeur exacte du pitch ; 3:25 réglages de la convolution ; 5:46 réglages de loop ; 8:50 rate et profondeur du LFO random.

### DR-10 Build Huge Atmospheres in Serum 2 (Ambient Sound Design Guide) — DNB Academy (Tomic), 10:32, 2025-06-04, outil : Serum 2
URL: https://www.youtube.com/watch?v=e52VL0yLEP4
Technique(s) : accord de sinus construit avec les 3 osc (quinte, tierce, septième), noise « Geiger », effets épais, bounce dans Serum 2, puis resampling dans l'osc Granular (chaos, pan aléatoire des grains). L'osc Spectral est proposé en option.
Transcription : oui (EN, auto)
- 0:30 wavetables puis resampling en granulaire ; 0:44 sinus sur les 3 osc
- 1:20 accord construit avec les 3 osc (semi) : 2:12 quinte (+7) ; 2:51 tierce +3 = mineur (+4 = majeur) ; 3:17 septième sur le 3e osc ; 3:31 autre forme d'onde
- 3:44–3:50 noise « Geiger » ? [ASR « geer »], « count » monté
- 4:05–4:54 FX (bus ou FX master plutôt que par osc ?), distortion : épais et large
- 5:01–6:13 essai en saw
- 6:21–6:50 export (icône à gauche du logo Serum) = bounce de la dernière note
- 7:03–7:08 init, osc Granular, glisser le sample ; 7:32–7:38 effets granulaires, « chaos »
- 7:55 compression pour le niveau ; 8:05 mono, attack montée
- 8:27 option : osc Spectral ; 8:36 pan aléatoire des grains ; 9:00 re-bounce et itération
- Genre : DnB (chaîne DNB Academy, nappes d'intro/breakdown pour liquid/atmospheric) ; dans la vidéo elle-même, le contexte est « ambient ».
À vérifier à l'écran : 1:20 transpositions des 3 osc ; 3:44 nom du noise ; 4:36 chaîne d'effets ; 7:38 réglages granulaires (density, chaos) ; 8:36 profondeur du random pan.

### DR-11 Making Dreamy Atmospheres in Serum 2 — DNB Academy (Tomic), 13:10, 2026-02-13, outil : Serum 2
URL: https://www.youtube.com/watch?v=vatU4W_cPTA
Technique(s) : WT « Bottle Blow » en accord Fm7, unison impair, noise FM avec vinyl étiré, OTT, S&H sur le fine. Bounce in place, puis osc Spectral en mode Manual dont on balaie la position, avec un filtre spectral. Idée bonus : poser une reese en dessous.
Transcription : oui (EN, auto)
- 0:49–1:09 WT douce « Bottle Blow » (sinus + harmoniques)
- 1:36–1:42 accord F mineur 7 (DnB)
- 1:49–1:56 unison avec un nombre impair de voix
- 2:08–2:11 Noise -> FM (noise FM) ; 2:31–2:45 sample vinyl crackle / « stretched vinyl »
- 2:56–3:37 FX : chorus, reverb, delay, distortion, compression OTT (beaucoup)
- 3:52–4:18 S&H smooth au max -> fine tune, rate monté
- 4:28 bounce in place ; 4:45 nouvelle instance de Serum 2, osc Spectral (4:57), sample déposé (5:16)
- 5:36 la note F jouée = pitch d'origine (C = -5 demi-tons)
- 6:03–6:48 mode Manual = position figée, balayage de la position
- 6:55–7:24 filtre (retire les aigus), filtre spectral bas/haut
- 7:32–8:30 unison, distortion, reverb (tail coupée au bounce : 7:46), compression 8:00, delay 8:16, EQ 8:30
- 9:08 note tenue aussi longtemps que voulu ; 9:31–9:36 S&H -> fine tune à nouveau
- 9:47 en couche avec une reese = idée DnB ; 11:00 n'importe quelle source (samples de pads)
- La description de la vidéo mentionne : intros/breakdowns, LFO lent, noise filtré, shimmer/plate, mid/side
- Genre : DnB (liquid / atmospheric, accord Fm7 « DnB » à 1:36, layering de reese à 9:47).
À vérifier à l'écran : 1:56 nombre de voix d'unison ; 2:11 quantité de noise FM ; 3:56 rate et profondeur du S&H ; 6:23 position spectrale ; 7:05 réglages du filtre spectral.

### DR-12 Build Moody Ambient Pads for DNB | Depth, Movement & Atmosphere — DNB Academy (John Do aka Fries), 8:17, 2026-01-08, outil : Serum 2
URL: https://www.youtube.com/watch?v=Sr4ebVdfgAM
Technique(s) : deux saws à -2 oct (dont une à +3 demi-tons), osc C « Vocal Hum » de Serum 2, filtre résonant et drivé, LFO lent sur la position WT et le cutoff, filtre FX modulé, OTT, sub en direct out.
Transcription : oui (EN, auto)
- 0:51–1:12 osc A+B saw, -2 oct, B +3 demi-tons, 2 voix d'unison, detune bas
- 1:28 un peu de portamento
- 1:37–1:54 osc C table S2 « Digital > Vocal Hum », position WT 230, -1 oct, +3 demi-tons
- 2:11–2:20 filtre « Misc > High EQ 6 » ? [ASR ?] cutoff ~26, appliqué à tous les osc ; 2:31–2:44 résonance montée, drive ; niveau du Vocal Hum monté
- 3:00–3:25 LFO lent 2 bars -> position WT (vers 0) + cutoff
- 3:42 chorus par défaut, HPF on
- 4:02–4:36 filtre FX MG Low + LFO 1/8 en mode envelope (rampe plate puis montée) -> cutoff, drive
- 4:39–5:16 reverb Vintage : size 30 %, low ~90 (low cut ?), decay monté, mix monté
- 5:22 delay ping-pong subtil 1/4 ; 5:46 compresseur OTT multibande ; 6:03 size de la reverb montée
- 6:31–6:50 osc sub en direct out, -1 oct
- 6:54–7:04 release de l'ENV montée
- 7:28 usage : « neurofunk / hard drum and bass »
- Genre : DnB (neuro / hard DnB, dit à 7:28 ; titre « for DNB »).
À vérifier à l'écran : 2:17 type exact du filtre ; 3:03 profondeurs du LFO ; 4:02 forme du LFO du filtre FX ; 4:39 réglages de la reverb ; 6:33 niveau du sub.

### DR-13 Making Atmospheric/Drone Sounds in Serum — TARANT info, 7:41, 2017-09-06, outil : Serum 1
URL: https://www.youtube.com/watch?v=KyFMNz3n_Gw
Technique(s) : bruit de fond minimal pour les intros de deep dubstep : init détunée, filtre, enveloppe decay/sustain, un peu de noise, reverb essentielle ; une variante rythmique.
Transcription : oui (EN, auto)
- 0:16 contexte « deep dubstep » : bruit de fond d'intro, minimal
- 0:40–0:51 init, detune (« tune in a bit »)
- 0:58–1:06 filtre (type non dit ; « nice and shirt » [ASR ?])
- 1:07–1:24 decay / sustain de l'ENV
- 1:30–1:44 noise très bas
- 1:55–2:24 reverb indispensable pour remplir ; « alternating » [ASR ?]
- 3:58 offset ; 4:36 macro ou contrôle (interp.)
- 5:12 variante rythmique rapide façon « Alex Rome » ? [ASR ?]
- 6:41 usage : intros de deep dubstep de 8/16/32 mesures
- Genre : dubstep (deep dubstep, dit à 0:16 et 6:41). Très peu de valeurs sont dites : la lecture à l'écran est indispensable.
À vérifier à l'écran : 0:40 WT et réglages d'unison ; 0:58 type de filtre et cutoff ; 1:07 ENV1 ; 1:37 type et niveau du noise ; 2:08 réglages de la reverb.

### DR-14 Serum Tutorial - Ambient Drone Pro Tips — ADSR Music Production Tutorials (Echo Sound Works), 13:52, 2015-11-02, outil : Serum 1
URL: https://www.youtube.com/watch?v=WtgMa3nDJD8
Technique(s) : resynthèse. Un piano est samplé, noyé dans une reverb longue, bouncé, puis chargé comme sample dans l'oscillateur Noise de Serum. Il est superposé à une WT en unison 7 voix avec ENV1 à 19 s d'attack, et un LFO de 8 bars fait légèrement bender le Master Tune.
Transcription : oui (EN, auto)
- 1:20–1:31 usages cités : bandes-annonces, « dubstep, melodic dubstep », trance ; 1:34 tenir la tonique
- 2:08 ENV1 attack 19 s (drone ; en la baissant, on obtient un pad jouable)
- 3:00 1 osc WT + l'osc Noise utilisé comme sampler
- 3:53–4:14 sampler un piano en C4 (registre C3–C4), vélocité modérée
- 4:42–5:30 Valhalla VintageVerb en mode Ambience, decay ~30 (s), mix ~70 ; 5:35 bounce en audio
- 6:52–7:18 copier le wav dans le dossier de presets Serum > Noises > User > Ambient, puis relancer Serum
- 7:28–7:36 deux boutons du noise activés (one-shot / keytrack ? interp.), pitch +12, niveau monté ; 7:50–7:57 un peu de phase random
- 8:00–8:17 attack longue + release ; 8:54 ENV1 attack ~19 s, hold
- 9:24 LPF basique sur l'osc A seulement (le noise n'est pas routé dans le filtre) ; 9:38 ENV -> cutoff en option
- 9:54–10:18 osc A WT « basique », unison 7 voix, detune, large
- 11:06 FX : distortion, delay, reverb, EQ
- 11:22–11:39 LFO1 en rampe légère, 8 bars -> Master Tune (petit bend)
- 12:16 récapitulatif : attack longue sur ENV1, ne pas trop filtrer le sample
- Genre : dubstep (dubstep / melodic dubstep, cités à 1:20 parmi d'autres usages) : nappe d'intro ou de breakdown en melodic dubstep.
À vérifier à l'écran : 7:31 boutons du noise et pitch ; 9:58 nom de la WT de l'osc A ; 11:06 réglages des FX ; 11:25 forme et profondeur du LFO1 sur le Master Tune ; 8:54 ENV1 complète.

### DR-15 Comment faire des Dark Drones & Pads / Cinematic - Tuto Xfer Serum FR — Strob Studio Mixing & Mastering, 21:34, 2020-11-20, outil : Serum 1
URL: https://www.youtube.com/watch?v=2BSNiToeog8
Technique(s) : FM avec des formes quasi-sinus. Osc A porteur, osc B modulateur (niveau 0) accordé sur un ratio non entier (désaccordé) pour l'inharmonicité ; jeu 2–3 octaves plus bas, en notes à l'octave sans accords. Filtre passe-bande drivé, notch modulé par Chaos, LFO lent sur le Master Tune.
Transcription : oui (FR, auto)
- 1:53 formes d'onde simples type sinus + FM
- 2:09–2:21 porteur = osc A, modulateur = osc B à niveau 0 (3:04–3:09 : routage FM from B)
- 2:24–2:48 WT maison : sinus un peu plus riche, 2e frame identique à l'octave, 3e légèrement différente -> morph
- 2:56 le modulateur est un sinus pur
- 3:21 ratio FM non entier (désaccordé) ; 4:07 valeurs « -12 et … » [ASR ?]
- 4:38–5:04 ENV1 : attack longue, sustain un peu baissé, beaucoup de release
- 5:12 reverb indispensable (interne à Serum ou externe), « aux alentours de 70-80 » [interp. : size ou mix ?] à 5:24 ; 5:43 OTT léger pour remonter les tails
- 5:56 jouer 2–3 octaves plus bas
- 6:57–7:22 piano roll : 2 notes à l'octave (pas d'accords)
- 8:47 pitch du modulateur « -15 +3 » [ASR ?] ; 9:03 affinage autour de -12
- 9:50–10:13 wavetables Digital « Harmonic series » / « Harmonics » ? [ASR ?] en alternatives
- 10:44 filtre passe-bande BP12 [ASR « bn 12 »] : garder le grave et le bas-médium ; 11:25 drive
- 12:00 ENV2 très longue (attack longue, release, sustain qui descend) -> léger mouvement (cible non dite)
- 13:59 mouvement sur la FM et la position WT
- 14:51–15:23 FX filtre : notch qui se balade dans le bas-médium, modulé par un LFO puis par « Chaos » [ASR « en carrosse »], lent
- 16:03 ne pas trop pousser la FM
- 19:46–20:41 LFO3 -> Global Master Tune, unipolaire, rampe à mi-chemin, 4 bars, profondeur de quelques demi-tons (désaccord lent)
- Genre : cinématique / trailers / horreur (dit à 0:58–1:07). Je l'affecte aux intros sombres de dubstep (deep/dark) ou de DnB (affectation de ma part : drone grave inharmonique). Seul tuto FR retenu.
À vérifier à l'écran : 3:04 FM from B et quantité de FM ; 8:47 coarse/fine exacts du modulateur ; 10:44 type de filtre et cutoff ; 15:15 réglages Chaos/notch ; 20:01 profondeur du LFO3 sur le Master Tune.

---

### Écartés
- ImUxpzcNYXk How To Make Drone Bass For Techno Like Enrico Sangiuliano | Serum (Zen World - EvoSounds, 2:34) : bien fait dans Serum 1 mais très court, peu de valeurs (saw -2/-1 oct, LPF mi-ouvert, distortion, chorus, attack longue) et ASR confus ; c'est le 16e, tenu en réserve (techno).
- vo-TvYp3XUM How to make Melodic Deep Dubstep in Ableton using Serum 2 (ception.) : surtout des wamps/stabs ; une seule nappe « sustain » (WT S2 « AM Sine Harmonics » pos 177, saturator + Amp Blues + Hybrid Reverb dans Ableton). Ce n'est pas un vrai tuto de drone.
- 30se6SSmqgw Deeper Dubstep Sounds in Serum | Tarant Tip #32 : c'est une wobble bass deep dubstep, pas un drone.
- 2ykDKH9jnQI Big Z, Pro Atmosphere For House : Omnisphere + samples, pas Serum.
- Y3eB64YwCow Durosai, atmos minimal house : Podolski + samples (arrangement), pas Serum.
- sM-ok0m_VlE Zahand, ambiances organic house : Cube, Kontakt, samples Splice, pas Serum.
- tVRJxl-nmNc Pick Yourself, techno drones : Ableton Wavetable (Serum seulement mentionné).
- cYDLq5_GZ4M Dowden, drone pads tous genres : pas de transcription, hashtags #ableton, synthé non confirmé.
- s7M8jcGThN4 BassWobbleTv, Dance Atmos Intro & drop Serum 2 : session décousue, l'atmo se résume à ~30 s de white noise (5:52–6:35), quasi pas de valeurs.
- 3pjXO3yG02c Deuteroz, dark atmosphere : ni transcription ni description, invérifiable.
- Repérés mais non étudiés (préréglages/ventes, autres synthés, hors genre ou Shorts) : packs de presets (Anton Anru, Datacode, KRYXAL…), N-c5yIEL_8w/gfdbTBuuGTk Hive (synthwave), VIYRzJMYb5Q (psytrance), VotgShcw6cU (horreur), UShjYsGgWcM Venus Theory (multi-synthés), IcFEVozEgEw (Ableton).

### Manque
- 15 retenus sur 15 : 8 en famille house (dont seulement 3 labellisés house/afro/melodic house, 2 melodic techno, 1 trance/progressive et 2 génériques que j'ai affectés à la deep/minimal house), 4 DnB, 3 en dubstep / intro sombre (1 seul explicitement deep dubstep, 1 qui cite le dubstep parmi d'autres usages, 1 cinématique FR que j'ai affecté au dubstep).
- Aucun tuto Serum de drone/atmo étiqueté tech house, bass house, future house ou minimal house n'a été trouvé (les « atmos house » trouvées sont faites dans Omnisphere, Podolski, Cube ou avec des samples).
- Côté dubstep, aucun tuto Serum d'« intro drone » dédié de bonne qualité : seulement TARANT (peu de valeurs) ; les deux autres entrées sont des drones génériques que j'ai affectés au dubstep.
- Un seul tuto FR retenu (Strob Studio).
