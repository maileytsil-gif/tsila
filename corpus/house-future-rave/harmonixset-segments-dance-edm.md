---
titre: "urinieto/harmonixset — segments annotés de 31 titres dance/EDM (Guetta, SHM, Calvin Harris, Afrojack, Avicii, deadmau5…) + conversion en mesures"
source: https://raw.githubusercontent.com/urinieto/harmonixset/main/dataset/segments/
recupere_le: 2026-09-24
mode: texte integral (fichiers de segments et metadata) + tableau de conversion en mesures calculé localement
langue: en
axe: arrangement et méthode de production (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---
# Harmonix Set — segments annotés (titres dance / EDM : Guetta, Swedish House Mafia, Calvin Harris, Afrojack, Avicii, deadmau5, Daft Punk, Tiësto, Skrillex, Steve Aoki)

Extraction du dépôt `urinieto/harmonixset` (dossier `dataset/segments/`, un fichier par titre : `temps_en_secondes<TAB>étiquette`, l'étiquette nomme la section qui commence à ce temps ; annotations humaines, Harmonix). Métadonnées depuis `dataset/metadata.csv`. Les fichiers sont reproduits tels quels ci-dessous ; le tableau « mesure » de chaque titre est un **calcul local** (downbeat le plus proche dans `dataset/beats_and_downbeats/<fichier>.txt`), non fourni par le dépôt. Vocabulaire des annotateurs : `chorus` = refrain chanté, `inst` = section instrumentale (souvent le drop dans un titre EDM-pop), `break`/`breakdown`, `prechorus` (souvent le build), `postchorus`, `stutter`, `transition`, `section` (bloc sans fonction chantée), `end`.

Citation demandée par les auteurs : Nieto, O., McCallum, M., Davies, M., Robertson, A., Stark, A., Egozy, E., *The Harmonix Set: Beats, Downbeats, and Functional Segment Annotations of Western Popular Music*, ISMIR 2019.

## Métadonnées (metadata.csv)

| File | Title | Artist | Release | Duration (s) | BPM | Genre |
|---|---|---|---|---|---|---|
| 0012_aroundtheworld | Around The World | Daft Punk | Homework | 154.601 | 121 | Dance/Electronic |
| 0251_sexychick | Sexy Chick | David Guetta | Now That’s What I Call Music! 32 | 161.033 | 130 | Pop |
| 0270_takeovercontrol | Take Over Control | Afrojack | Slam FM Grand Slam 2010, Volume 4 | 163.203 | 130 | Dance/Electronic |
| 0273_technologic | Technologic | Daft Punk | Human After All | 145.137 | 128 | Dance/Electronic |
| 0369_dontyouworrychild | Don't You Worry Child | Swedish House Mafia feat. John Martin | Now That's What I Call Music! 44 | 209.924 | 130 | Pop |
| 0383_feelsoclose | Feel So Close (radio edit) | Calvin Harris | Now That's What I Call Music! 80 | 202.263 | 128 | Pop |
| 0389_gettinoveryou | Gettin' Over You | David Guetta & Chris Willis | Now That's What I Call Music! 35 | 185.086 | 130 | Dance/Electronic |
| 0408_icanonlyimagine | I Can Only Imagine | David Guetta feat. Chris Brown & Lil Wayne | Now That's What I Call Music! 44 | 209.009 | 128 | Dance/Electronic |
| 0432_letsgo | Let's Go | Calvin Harris feat. Ne-Yo | Now That's What I Call Music! 43 | 225.114 | 128 | Dance/Electronic |
| 0445_memories | Memories | David Guetta feat. Kid Cudi | Now That's What I Call Music! 36 | 208.381 | 130 | Dance/Electronic |
| 0519_titanium | Titanium | David Guetta feat. Sia | Now That's What I Call Music! 43 | 211.022 | 126 | Pop |
| 0535_withoutyou | Without You | David Guetta feat. Usher | Now That's What I Call Music! 40 | 206.97 | 128 | Pop |
| 0655_earthquakey | Earthquakey People (The Sequel) | Steve Aoki feat. Rivers Cuomo | Ultra Dance 13 | 262.841 | 128 | Dance/Electronic |
| 0662_everytimewetouch | Everytime We Touch | David Guetta & Chris Willis feat. Steve Angello & Sebastian Ingrosso | Ultra Dance 10 | 290.241 | 129 | Dance/Electronic |
| 0672_feelitinmybones | Feel It in My Bones (extended mix) | Tiësto ft. Tegan and Sara | Ultra Dance 11 | 415.24 | 130 | Pop |
| 0674_feelsocloseextendedmix | Feel So Close (extended mix) | Calvin Harris | Ultra Dance 13 | 270.345 | 128 | Pop |
| 0689_gettinoveryou | Gettin' Over You (Sidney Samson remix) | David Guetta & Chris Willis feat. Fergie & LMFAO | Now That's What I Call Club Hits 2 | 317.902 | 130 | Dance/Electronic |
| 0750_ineedyourlove | I Need Your Love | Calvin Harris feat. Ellie Goulding | Halcyon | 235.154 | 125 | Pop |
| 0797_loveisgone | Love Is Gone (Fred Rister & Joachim Garruad extended mix) | David Guetta & Chris Willis | Ultra Dance 11 | 356.205 | 128 | Pop |
| 0810_memoriesextended | Memories (extended) | David Guetta feat. Kid Cudi | Ultra Dance 12 | 278.685 | 127 | Dance/Electronic |
| 0811_miami2ibiza | Miami 2 Ibiza (extended vocal mix) | Swedish House Mafia vs Tinie Tempah | Ultra Dance 12 | 252.305 | 127 | Dance/Electronic |
| 0821_myfeelingsforyou | My Feelings for You | Avicii | Ultra Dance 13 | 309.771 | 128 | Pop |
| 0869_raiseyourweapon | Raise Your Weapon | deadmau5 | Ultra Dance 13 | 473.02 | 140 | Pop |
| 0891_savetheworld | Save the World (radio remix) | Swedish House Mafia | Ultra Dance 13 | 204.669 | 128 | Pop |
| 0895_scarymonsters | Scary Monsters & Nice Sprites (Kaskade remix) | Skrillex | Ultra Dance 13 | 369.826 | 128 | Dance/Electronic |
| 0900_sexychickakon | Sexy Chick | David Guetta feat. Akon | Now That's What I Call Music! 32 | 193.191 | 130 | Dance/Electronic |
| 0909_sofineed | Sofi Needs a Ladder | deadmau5 | Ultra Dance 12 | 361.486 | 128 | Dance/Electronic |
| 0929_takeovercontrolext | Take Over Control (extended) | Afrojack feat. Eva Simmons | Ultra Dance 12 | 372.415 | 130 | Dance/Electronic |
| 0965_wakingupinvegascalvin | Waking Up in Vegas (Calvin Harris extended remix) | Katy Perry | Ultra Dance 11 | 271.704 | 131 | Dance/Electronic |
| 0966_wakingupinvegascalvinh | Waking Up in Vegas (Calvin Harris remix edit) | Katy Perry | Now That's What I Call Club Hits | 219.467 | 131 | Dance/Electronic |
| 0979_whenlovetakesover | When Love Takes Over | David Guetta feat. Kelly Rowland | Now That's What I Call Summer | 184.903 | 130 | Pop |

## Fichiers de segments (texte intégral)

### dataset/segments/0012_aroundtheworld.txt
```
0.0 intro
15.83716 chorus
47.496636 instrumental
55.41536 chorus
71.242464 instrumental
87.075984 chorus
126.646904 instrumental
134.565624 chorus
150.380448 end
```

### dataset/segments/0251_sexychick.txt
```
0.0 silence
1.846148 intro
8.769203 verse
37.846034 prechorus
68.307476 chorus
82.615123 verse
111.691954 prechorus
142.153396 chorus
156.92258 end
```

### dataset/segments/0270_takeovercontrol.txt
```
0.0 intro
7.356512 chorus
22.069536 verse
51.531552 prechorus
66.26256 chorus
80.99248 inst
110.45232 chorus
125.18224 chorus
139.91216 outro
154.64208 end
```

### dataset/segments/0273_technologic.txt
```
0.0 verse
37.664872 chorus
45.198418 verse
90.402662 bridge
105.467242 verse
120.529786 outro
135.60287 chorus
143.102374 end
```

### dataset/segments/0369_dontyouworrychild.txt
```
0.0666665 intro
5.6480585 verse
37.2759465 prechorus
52.1596585 chorus
67.0433705 inst
81.9270825 chorus
98.6712585 verse
130.2991465 prechorus
145.1828585 chorus
160.0665705 bridge
174.9502825 chorus
189.8339945 outro
204.7177065 end
```

### dataset/segments/0383_feelsoclose.txt
```
0.05859375 verse
30.05859375 prechorus
45.07030575 chorus
75.08055375 verse
105.08055375 chorus
135.08055375 bridge
165.08055375 chorus
195.08055375 outro
200.70555375 end
```

### dataset/segments/0389_gettinoveryou.txt
```
0.0610236291667 intro
3.735916 chorus
36.505114 verse
70.197388 prechorus
84.966604 chorus
114.505036 prechorus
132.966556 bridge
168.043444 prechorus
182.81266 end
```

### dataset/segments/0408_icanonlyimagine.txt
```
0.0835371583333 intro
7.580992 verse
37.112242 chorus
75.080992 inst
90.080992 verse
119.612242 chorus
157.580992 bridge
177.268492 verse
207.268492 end
```

### dataset/segments/0432_letsgo.txt
```
0.0444915625 intro
6.603174 verse
22.543156 prechorus
52.547828 chorus
82.5525 verse
97.086013 prechorus
126.621862 chorus
157.56418 bridge
186.631206 chorus
201.633542 chorus
217.573524 end
```

### dataset/segments/0445_memories.txt
```
0.0462598479167 intro
14.812828 chorus
44.35126 verse
73.889692 break
88.658908 chorus
118.19734 verse
147.735772 bridge
177.274204 verse
206.351098 end
```

### dataset/segments/0519_titanium.txt
```
0.0395299520833 intro
7.655671 verse
38.131831 chorus
68.607991 inst
83.846071 verse
114.322231 chorus
144.798391 inst
160.036471 bridge
175.274551 chorus
190.512631 inst
205.750711 end
```

### dataset/segments/0535_withoutyou.txt
```
0.0673912875 intro
15.052989 verse
45.052989 verse
75.052989 chorus
101.302989 verse
131.302989 verse
161.302989 chorus
187.552989 verse
202.552989 end
```

### dataset/segments/0655_earthquakey.txt
```
0.0554435520833 intro
30.060484 chorus
58.185484 stutter
75.060484 inst
105.060484 intro
135.060484 chorus
163.185484 stutter
180.060484 bridge
202.560484 inst
262.560484 end
```

### dataset/segments/0662_everytimewetouch.txt
```
0.0652610833333 intro
14.95096 chorus
44.718384 verse
73.555576 chorus
104.253232 inst
134.020656 verse
162.829112 chorus
193.526768 inst
223.294192 breakdown
238.1495 inst
267.85382 outro
289.956668 end
```

### dataset/segments/0672_feelitinmybones.txt
```
0.075 intro
29.843432 verse
44.612648 prechorus
58.458788 chorus
74.15108 verse
88.920296 prechorus
102.766436 chorus
117.535652 chorus
133.227944 inst
162.766376 bridge
176.612516 chorus
192.304808 bridge2
222.766316 chorus
238.458608 inst
253.227824 solo
314.15084 breakdown
327.073904 inst
356.612336 solo
386.150768 outro
414.377908 end
```

### dataset/segments/0674_feelsocloseextendedmix.txt
```
0.05859375 intro
15.04450975 chorus
45.04450975 guitar
60.04450975 inst
90.04450975 chorus
120.04450975 inst
150.04450975 breakdown
180.04450975 inst
210.04450975 outro
270.04450975 end
```

### dataset/segments/0689_gettinoveryou.txt
```
0.041666625 intro
29.580098625 chorus
66.503138625 inst
96.041570625 postchorus
125.580002625 chorus
155.118434625 inst
185.579942625 bridge
214.195298625 inst
258.502946625 outro
317.579810625 end
```

### dataset/segments/0750_ineedyourlove.txt
```
0.10714275 intro
6.82714275 chorus
23.14714275 inst
57.70714275 verse
87.46714275 chorus
103.78714275 inst
119.14714275 verse
148.90714275 chorus
165.22714275 inst
180.58714275 bridge
194.98714275 chorus
211.30714275 inst
228.58714275 end
```

### dataset/segments/0797_loveisgone.txt
```
0.05859375 intro
7.08984375 verse
37.08984375 verse
67.08984375 stutter
82.08984375 inst
134.58984375 break
142.08984375 inst
175.83984375 inst
205.83984375 intro
213.33984375 verse
243.33984375 verse
273.33984375 stutter
288.33984375 inst
303.33984375 bridge
318.33984375 breakdown
355.83984375 end
```

### dataset/segments/0810_memoriesextended.txt
```
0.075 intro
37.68372 chorus
67.770696 postchorus
97.857672 break
112.90116 chorus
142.988136 postchorus
173.075112 bridge
203.162088 postchorus
233.249064 inst
278.379528 end
```

### dataset/segments/0811_miami2ibiza.txt
```
0.0586855 intro
7.0734955 chorus
22.1145285 chorus
37.6281255 prechorus
52.6716135 inst
86.0493525 chorus
101.0928405 chorus2
131.6499255 inst
191.8238775 inst2
251.9978295 end
```

### dataset/segments/0821_myfeelingsforyou.txt
```
0.05859375 intro
11.30859375 chorus
26.30859375 verse
45.05859375 chorus
60.05859375 chorus
75.05859375 inst
82.55859375 chorus
105.05859375 chorus
135.05859375 altchorus
150.05859375 break
165.05859375 chorus
180.05859375 chorus
195.05859375 postchorus
210.05859375 postchorus
225.05859375 postchorus
240.05859375 instchorus
255.05859375 breakdown
285.05859375 saxobeat
309.43359375 end
```

### dataset/segments/0869_raiseyourweapon.txt
```
0.05859375 intro
30.05859375 prechorus
45.05859375 chorus
60.05859375 inst
90.05859375 verse
120.05859375 prechorus
135.05859375 chorus
150.05859375 break
180.05859375 verse
194.73348175 chorus
212.16076975 bridge
267.01785775 verse
294.44640175 prechorus
308.16067375 chorus
321.87494575 postchorus
363.01776175 chorus
376.73203375 inst2
404.16057775 intro
455.58909775 end
```

### dataset/segments/0891_savetheworld.txt
```
0.05859375 intro
7.55859375 verse
21.62109375 prechorus
36.62109375 chorus
67.55859375 inst
82.55859375 postchorus
99.43359375 verse
113.49609375 prechorus
128.49609375 chorus
159.43359375 postchorus
173.49609375 chorus
204.43359375 end
```

### dataset/segments/0895_scarymonsters.txt
```
0.05859375 intro
30.05859375 break
45.05859375 chorus
60.05859375 chorus
75.05859375 postchorus
90.05859375 postchorus
105.05859375 postchorus
120.05859375 build
166.93359375 inst
181.93359375 inst
196.93359375 inst2
211.93359375 inst2
226.93359375 inst2
241.93359375 inst2
256.93359375 break2
264.43359375 inst2
279.43359375 chorus
294.43359375 inst2
309.43359375 inst2
324.43359375 inst2
339.43359375 inst2
354.43359375 inst2
369.43359375 end
```

### dataset/segments/0900_sexychickakon.txt
```
0.041666625 intro
44.349314625 chorus
73.887746625 chorus2
103.426178625 verse
133.022302875 chorus
162.503042625 chorus2
192.099166875 end
```

### dataset/segments/0909_sofineed.txt
```
0.247934 intro
31.735538 section
61.735538 section
91.735538 section
121.735538 section
151.735538 section
181.735538 section
211.735538 section
241.735538 section
271.735538 section
301.735538 section
331.735538 outro
360.798038 end
```

### dataset/segments/0929_takeovercontrolext.txt
```
0.075 intro
29.613432 verse
59.151864 verse
88.690296 chorus
118.228728 section
145.921008 chorus2
162.536376 chorus
177.305592 verse
206.844024 chorus
236.382456 transition
251.20936425 section
280.690104 outro
308.382384 outro
339.766968 outro
369.36309225 end
```

### dataset/segments/0965_wakingupinvegascalvin.txt
```
0.277778 intro
16.766318 verse
44.247218 break
51.575458 transition
80.888418 chorus
110.201378 verse
137.682278 break
146.842578 transition
176.155538 chorus
205.468498 bridge
234.781458 break
242.109698 chorus
271.422658 end
```

### dataset/segments/0966_wakingupinvegascalvinh.txt
```
0.10714275 verse1
29.42010275 break
36.74834275 intro
51.40482275 chorus
66.06130275 verse2
95.37426275 break
102.70250275 transition
117.35898275 chorus
132.01546275 chorus
146.67194275 transition
176.0994065 break
183.31314275 chorus
197.96962275 chorus
212.7406065 outro
219.03831275 end
```

### dataset/segments/0979_whenlovetakesover.txt
```
0.08823525 intro
7.47284325 verse
22.2997515 verse2
37.01127525 chorus
51.78049125 verse3
66.54970725 verse4
81.31892325 chorus
96.08813925 break
110.85735525 bridge
125.6842635 outro
169.93421925 outro2
184.7611275 end
```


## Conversion en mesures (calcul local à partir de beats_and_downbeats)


### 0012_aroundtheworld — Daft Punk – Around The World (121 BPM, 2:34.6, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.00 | 0:00.0 | m.1 | intro (15.8 s) |
| 15.84 | 0:15.8 | m.9 | chorus (31.7 s) |
| 47.50 | 0:47.5 | m.25 | instrumental (7.9 s) |
| 55.42 | 0:55.4 | m.29 | chorus (15.8 s) |
| 71.24 | 1:11.2 | m.37 | instrumental (15.8 s) |
| 87.08 | 1:27.1 | m.45 | chorus (39.6 s) |
| 126.65 | 2:06.6 | m.65 | instrumental (7.9 s) |
| 134.57 | 2:14.6 | m.69 | chorus (15.8 s) |
| 150.38 | 2:30.4 | m.77 | end |

### 0251_sexychick — David Guetta – Sexy Chick (130 BPM, 2:41.0, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.00 | 0:00.0 | m.1 | silence (1.8 s) |
| 1.85 | 0:01.8 | m.1 | intro (6.9 s) |
| 8.77 | 0:08.8 | m.4 (temps 4) | verse (29.1 s) |
| 37.85 | 0:37.8 | m.20 (temps 3) | prechorus (30.5 s) |
| 68.31 | 1:08.3 | m.37 | chorus (14.3 s) |
| 82.62 | 1:22.6 | m.44 (temps 4) | verse (29.1 s) |
| 111.69 | 1:51.7 | m.60 (temps 3) | prechorus (30.5 s) |
| 142.15 | 2:22.2 | m.77 | chorus (14.8 s) |
| 156.92 | 2:36.9 | m.85 | end |

### 0270_takeovercontrol — Afrojack – Take Over Control (130 BPM, 2:43.2, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.00 | 0:00.0 | m.1 | intro (7.4 s) |
| 7.36 | 0:07.4 | m.5 | chorus (14.7 s) |
| 22.07 | 0:22.1 | m.13 | verse (29.5 s) |
| 51.53 | 0:51.5 | m.29 | prechorus (14.7 s) |
| 66.26 | 1:06.3 | m.37 | chorus (14.7 s) |
| 80.99 | 1:21.0 | m.45 | inst (29.5 s) |
| 110.45 | 1:50.5 | m.61 | chorus (14.7 s) |
| 125.18 | 2:05.2 | m.69 | chorus (14.7 s) |
| 139.91 | 2:19.9 | m.77 | outro (14.7 s) |
| 154.64 | 2:34.6 | m.85 | end |

### 0273_technologic — Daft Punk – Technologic (128 BPM, 2:25.1, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.00 | 0:00.0 | m.1 | verse (37.7 s) |
| 37.66 | 0:37.7 | m.21 | chorus (7.5 s) |
| 45.20 | 0:45.2 | m.25 | verse (45.2 s) |
| 90.40 | 1:30.4 | m.49 | bridge (15.1 s) |
| 105.47 | 1:45.5 | m.57 | verse (15.1 s) |
| 120.53 | 2:00.5 | m.65 | outro (15.1 s) |
| 135.60 | 2:15.6 | m.73 | chorus (7.5 s) |
| 143.10 | 2:23.1 | m.77 | end |

### 0369_dontyouworrychild — Swedish House Mafia feat. John Martin – Don't You Worry Child (130 BPM, 3:29.9, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.07 | 0:00.1 | m.1 | intro (5.6 s) |
| 5.65 | 0:05.6 | m.4 | verse (31.6 s) |
| 37.28 | 0:37.3 | m.21 | prechorus (14.9 s) |
| 52.16 | 0:52.2 | m.29 | chorus (14.9 s) |
| 67.04 | 1:07.0 | m.37 | inst (14.9 s) |
| 81.93 | 1:21.9 | m.45 | chorus (16.7 s) |
| 98.67 | 1:38.7 | m.54 | verse (31.6 s) |
| 130.30 | 2:10.3 | m.71 | prechorus (14.9 s) |
| 145.18 | 2:25.2 | m.79 | chorus (14.9 s) |
| 160.07 | 2:40.1 | m.87 | bridge (14.9 s) |
| 174.95 | 2:55.0 | m.95 | chorus (14.9 s) |
| 189.83 | 3:09.8 | m.103 | outro (14.9 s) |
| 204.72 | 3:24.7 | m.111 | end |

### 0383_feelsoclose — Calvin Harris – Feel So Close (radio edit) (128 BPM, 3:22.3, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | verse (30.0 s) |
| 30.06 | 0:30.1 | m.17 | prechorus (15.0 s) |
| 45.07 | 0:45.1 | m.25 | chorus (30.0 s) |
| 75.08 | 1:15.1 | m.41 | verse (30.0 s) |
| 105.08 | 1:45.1 | m.57 | chorus (30.0 s) |
| 135.08 | 2:15.1 | m.73 | bridge (30.0 s) |
| 165.08 | 2:45.1 | m.89 | chorus (30.0 s) |
| 195.08 | 3:15.1 | m.105 | outro (5.6 s) |
| 200.71 | 3:20.7 | m.108 | end |

### 0389_gettinoveryou — David Guetta & Chris Willis – Gettin' Over You (130 BPM, 3:05.1, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (3.7 s) |
| 3.74 | 0:03.7 | m.3 | chorus (32.8 s) |
| 36.51 | 0:36.5 | m.20 (temps 4) | verse (33.7 s) |
| 70.20 | 1:10.2 | m.39 | prechorus (14.8 s) |
| 84.97 | 1:25.0 | m.47 | chorus (29.5 s) |
| 114.51 | 1:54.5 | m.63 | prechorus (18.5 s) |
| 132.97 | 2:13.0 | m.73 | bridge (35.1 s) |
| 168.04 | 2:48.0 | m.92 | prechorus (14.8 s) |
| 182.81 | 3:02.8 | m.100 | end |

### 0408_icanonlyimagine — David Guetta feat. Chris Brown & Lil Wayne – I Can Only Imagine (128 BPM, 3:29.0, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.08 | 0:00.1 | m.1 | intro (7.5 s) |
| 7.58 | 0:07.6 | m.5 | verse (29.5 s) |
| 37.11 | 0:37.1 | m.20 (temps 4) | chorus (38.0 s) |
| 75.08 | 1:15.1 | m.41 | inst (15.0 s) |
| 90.08 | 1:30.1 | m.49 | verse (29.5 s) |
| 119.61 | 1:59.6 | m.64 (temps 4) | chorus (38.0 s) |
| 157.58 | 2:37.6 | m.85 | bridge (19.7 s) |
| 177.27 | 2:57.3 | m.95 | verse (30.0 s) |
| 207.27 | 3:27.3 | m.111 | end |

### 0432_letsgo — Calvin Harris feat. Ne-Yo – Let's Go (128 BPM, 3:45.1, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.04 | 0:00.0 | m.1 | intro (6.6 s) |
| 6.60 | 0:06.6 | m.4 (temps 3) | verse (15.9 s) |
| 22.54 | 0:22.5 | m.13 | prechorus (30.0 s) |
| 52.55 | 0:52.5 | m.29 | chorus (30.0 s) |
| 82.55 | 1:22.6 | m.45 | verse (14.5 s) |
| 97.09 | 1:37.1 | m.52 (temps 4) | prechorus (29.5 s) |
| 126.62 | 2:06.6 | m.68 (temps 3) | chorus (30.9 s) |
| 157.56 | 2:37.6 | m.85 | bridge (29.1 s) |
| 186.63 | 3:06.6 | m.100 (temps 3) | chorus (15.0 s) |
| 201.63 | 3:21.6 | m.108 (temps 3) | chorus (15.9 s) |
| 217.57 | 3:37.6 | m.117 | end |

### 0445_memories — David Guetta feat. Kid Cudi – Memories (130 BPM, 3:28.4, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.05 | 0:00.0 | m.1 | intro (14.8 s) |
| 14.81 | 0:14.8 | m.9 | chorus (29.5 s) |
| 44.35 | 0:44.4 | m.25 | verse (29.5 s) |
| 73.89 | 1:13.9 | m.41 | break (14.8 s) |
| 88.66 | 1:28.7 | m.49 | chorus (29.5 s) |
| 118.20 | 1:58.2 | m.65 | verse (29.5 s) |
| 147.74 | 2:27.7 | m.81 | bridge (29.5 s) |
| 177.27 | 2:57.3 | m.97 | verse (29.1 s) |
| 206.35 | 3:26.4 | m.112 (temps 4) | end |

### 0519_titanium — David Guetta feat. Sia – Titanium (126 BPM, 3:31.0, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.04 | 0:00.0 | m.1 | intro (7.6 s) |
| 7.66 | 0:07.7 | m.5 | verse (30.5 s) |
| 38.13 | 0:38.1 | m.21 | chorus (30.5 s) |
| 68.61 | 1:08.6 | m.37 | inst (15.2 s) |
| 83.85 | 1:23.8 | m.45 | verse (30.5 s) |
| 114.32 | 1:54.3 | m.61 | chorus (30.5 s) |
| 144.80 | 2:24.8 | m.77 | inst (15.2 s) |
| 160.04 | 2:40.0 | m.85 | bridge (15.2 s) |
| 175.27 | 2:55.3 | m.93 | chorus (15.2 s) |
| 190.51 | 3:10.5 | m.101 | inst (15.2 s) |
| 205.75 | 3:25.8 | m.109 | end |

### 0535_withoutyou — David Guetta feat. Usher – Without You (128 BPM, 3:27.0, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.07 | 0:00.1 | m.1 | intro (15.0 s) |
| 15.05 | 0:15.1 | m.9 | verse (30.0 s) |
| 45.05 | 0:45.1 | m.25 | verse (30.0 s) |
| 75.05 | 1:15.1 | m.41 | chorus (26.2 s) |
| 101.30 | 1:41.3 | m.55 | verse (30.0 s) |
| 131.30 | 2:11.3 | m.71 | verse (30.0 s) |
| 161.30 | 2:41.3 | m.87 | chorus (26.2 s) |
| 187.55 | 3:07.6 | m.101 | verse (15.0 s) |
| 202.55 | 3:22.6 | m.109 | end |

### 0655_earthquakey — Steve Aoki feat. Rivers Cuomo – Earthquakey People (The Sequel) (128 BPM, 4:22.8, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (30.0 s) |
| 30.06 | 0:30.1 | m.17 | chorus (28.1 s) |
| 58.19 | 0:58.2 | m.32 | stutter (16.9 s) |
| 75.06 | 1:15.1 | m.41 | inst (30.0 s) |
| 105.06 | 1:45.1 | m.57 | intro (30.0 s) |
| 135.06 | 2:15.1 | m.73 | chorus (28.1 s) |
| 163.19 | 2:43.2 | m.88 | stutter (16.9 s) |
| 180.06 | 3:00.1 | m.97 | bridge (22.5 s) |
| 202.56 | 3:22.6 | m.109 | inst (60.0 s) |
| 262.56 | 4:22.6 | m.141 | end |

### 0662_everytimewetouch — David Guetta & Chris Willis feat. Steve Angello & Sebastian Ingrosso – Everytime We Touch (129 BPM, 4:50.2, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.07 | 0:00.1 | m.1 | intro (14.9 s) |
| 14.95 | 0:15.0 | m.9 | chorus (29.8 s) |
| 44.72 | 0:44.7 | m.25 | verse (28.8 s) |
| 73.56 | 1:13.6 | m.40 (temps 3) | chorus (30.7 s) |
| 104.25 | 1:44.3 | m.57 | inst (29.8 s) |
| 134.02 | 2:14.0 | m.73 | verse (28.8 s) |
| 162.83 | 2:42.8 | m.88 (temps 3) | chorus (30.7 s) |
| 193.53 | 3:13.5 | m.105 | inst (29.8 s) |
| 223.29 | 3:43.3 | m.121 | breakdown (14.9 s) |
| 238.15 | 3:58.1 | m.129 | inst (29.7 s) |
| 267.85 | 4:27.9 | m.145 | outro (22.1 s) |
| 289.96 | 4:50.0 | m.157 | end |

### 0672_feelitinmybones — Tiësto ft. Tegan and Sara – Feel It in My Bones (extended mix) (130 BPM, 6:55.2, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.07 | 0:00.1 | m.1 | intro (29.8 s) |
| 29.84 | 0:29.8 | m.17 | verse (14.8 s) |
| 44.61 | 0:44.6 | m.25 | prechorus (13.8 s) |
| 58.46 | 0:58.5 | m.32 (temps 3) | chorus (15.7 s) |
| 74.15 | 1:14.2 | m.41 | verse (14.8 s) |
| 88.92 | 1:28.9 | m.49 | prechorus (13.8 s) |
| 102.77 | 1:42.8 | m.56 (temps 3) | chorus (14.8 s) |
| 117.54 | 1:57.5 | m.64 (temps 3) | chorus (15.7 s) |
| 133.23 | 2:13.2 | m.73 | inst (29.5 s) |
| 162.77 | 2:42.8 | m.89 | bridge (13.8 s) |
| 176.61 | 2:56.6 | m.96 (temps 3) | chorus (15.7 s) |
| 192.30 | 3:12.3 | m.105 | bridge2 (30.5 s) |
| 222.77 | 3:42.8 | m.121 (temps 3) | chorus (15.7 s) |
| 238.46 | 3:58.5 | m.130 | inst (14.8 s) |
| 253.23 | 4:13.2 | m.138 | solo (60.9 s) |
| 314.15 | 5:14.2 | m.171 | breakdown (12.9 s) |
| 327.07 | 5:27.1 | m.178 | inst (29.5 s) |
| 356.61 | 5:56.6 | m.194 | solo (29.5 s) |
| 386.15 | 6:26.2 | m.210 | outro (28.2 s) |
| 414.38 | 6:54.4 | m.225 (temps 4) | end |

### 0674_feelsocloseextendedmix — Calvin Harris – Feel So Close (extended mix) (128 BPM, 4:30.3, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (15.0 s) |
| 15.04 | 0:15.0 | m.9 | chorus (30.0 s) |
| 45.04 | 0:45.0 | m.25 | guitar (15.0 s) |
| 60.04 | 1:00.0 | m.33 | inst (30.0 s) |
| 90.04 | 1:30.0 | m.49 | chorus (30.0 s) |
| 120.04 | 2:00.0 | m.65 | inst (30.0 s) |
| 150.04 | 2:30.0 | m.81 | breakdown (30.0 s) |
| 180.04 | 3:00.0 | m.97 | inst (30.0 s) |
| 210.04 | 3:30.0 | m.113 | outro (60.0 s) |
| 270.04 | 4:30.0 | m.145 | end |

### 0689_gettinoveryou — David Guetta & Chris Willis feat. Fergie & LMFAO – Gettin' Over You (Sidney Samson remix) (130 BPM, 5:17.9, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.04 | 0:00.0 | m.1 | intro (29.5 s) |
| 29.58 | 0:29.6 | m.17 | chorus (36.9 s) |
| 66.50 | 1:06.5 | m.37 | inst (29.5 s) |
| 96.04 | 1:36.0 | m.53 | postchorus (29.5 s) |
| 125.58 | 2:05.6 | m.69 | chorus (29.5 s) |
| 155.12 | 2:35.1 | m.85 | inst (30.5 s) |
| 185.58 | 3:05.6 | m.101 (temps 3) | bridge (28.6 s) |
| 214.20 | 3:34.2 | m.117 | inst (44.3 s) |
| 258.50 | 4:18.5 | m.141 | outro (59.1 s) |
| 317.58 | 5:17.6 | m.173 | end |

### 0750_ineedyourlove — Calvin Harris feat. Ellie Goulding – I Need Your Love (125 BPM, 3:55.2, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.11 | 0:00.1 | m.1 | intro (6.7 s) |
| 6.83 | 0:06.8 | m.4 (temps 3) | chorus (16.3 s) |
| 23.15 | 0:23.1 | m.13 | inst (34.6 s) |
| 57.71 | 0:57.7 | m.31 | verse (29.8 s) |
| 87.47 | 1:27.5 | m.46 (temps 3) | chorus (16.3 s) |
| 103.79 | 1:43.8 | m.55 | inst (15.4 s) |
| 119.15 | 1:59.1 | m.63 | verse (29.8 s) |
| 148.91 | 2:28.9 | m.78 (temps 3) | chorus (16.3 s) |
| 165.23 | 2:45.2 | m.87 | inst (15.4 s) |
| 180.59 | 3:00.6 | m.95 | bridge (14.4 s) |
| 194.99 | 3:15.0 | m.102 (temps 3) | chorus (16.3 s) |
| 211.31 | 3:31.3 | m.111 | inst (17.3 s) |
| 228.59 | 3:48.6 | m.120 | end |

### 0797_loveisgone — David Guetta & Chris Willis – Love Is Gone (Fred Rister & Joachim Garruad extended mix) (128 BPM, 5:56.2, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (7.0 s) |
| 7.09 | 0:07.1 | m.5 | verse (30.0 s) |
| 37.09 | 0:37.1 | m.21 | verse (30.0 s) |
| 67.09 | 1:07.1 | m.37 | stutter (15.0 s) |
| 82.09 | 1:22.1 | m.45 | inst (52.5 s) |
| 134.59 | 2:14.6 | m.73 | break (7.5 s) |
| 142.09 | 2:22.1 | m.77 | inst (33.8 s) |
| 175.84 | 2:55.8 | m.95 | inst (30.0 s) |
| 205.84 | 3:25.8 | m.111 | intro (7.5 s) |
| 213.34 | 3:33.3 | m.115 | verse (30.0 s) |
| 243.34 | 4:03.3 | m.131 | verse (30.0 s) |
| 273.34 | 4:33.3 | m.147 | stutter (15.0 s) |
| 288.34 | 4:48.3 | m.155 | inst (15.0 s) |
| 303.34 | 5:03.3 | m.163 | bridge (15.0 s) |
| 318.34 | 5:18.3 | m.171 | breakdown (37.5 s) |
| 355.84 | 5:55.8 | m.191 | end |

### 0810_memoriesextended — David Guetta feat. Kid Cudi – Memories (extended) (127 BPM, 4:38.7, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.07 | 0:00.1 | m.1 | intro (37.6 s) |
| 37.68 | 0:37.7 | m.21 | chorus (30.1 s) |
| 67.77 | 1:07.8 | m.37 | postchorus (30.1 s) |
| 97.86 | 1:37.9 | m.53 | break (15.0 s) |
| 112.90 | 1:52.9 | m.61 | chorus (30.1 s) |
| 142.99 | 2:23.0 | m.77 | postchorus (30.1 s) |
| 173.08 | 2:53.1 | m.93 | bridge (30.1 s) |
| 203.16 | 3:23.2 | m.109 | postchorus (30.1 s) |
| 233.25 | 3:53.2 | m.125 | inst (45.1 s) |
| 278.38 | 4:38.4 | m.149 | end |

### 0811_miami2ibiza — Swedish House Mafia vs Tinie Tempah – Miami 2 Ibiza (extended vocal mix) (127 BPM, 4:12.3, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (7.0 s) |
| 7.07 | 0:07.1 | m.4 (temps 4) | chorus (15.0 s) |
| 22.11 | 0:22.1 | m.12 (temps 4) | chorus (15.5 s) |
| 37.63 | 0:37.6 | m.21 | prechorus (15.0 s) |
| 52.67 | 0:52.7 | m.29 | inst (33.4 s) |
| 86.05 | 1:26.0 | m.46 (temps 4) | chorus (15.0 s) |
| 101.09 | 1:41.1 | m.54 (temps 4) | chorus2 (30.6 s) |
| 131.65 | 2:11.6 | m.71 | inst (60.2 s) |
| 191.82 | 3:11.8 | m.103 | inst2 (60.2 s) |
| 252.00 | 4:12.0 | m.135 | end |

### 0821_myfeelingsforyou — Avicii – My Feelings for You (128 BPM, 5:09.8, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (11.2 s) |
| 11.31 | 0:11.3 | m.7 | chorus (15.0 s) |
| 26.31 | 0:26.3 | m.15 | verse (18.8 s) |
| 45.06 | 0:45.1 | m.25 | chorus (15.0 s) |
| 60.06 | 1:00.1 | m.33 | chorus (15.0 s) |
| 75.06 | 1:15.1 | m.41 | inst (7.5 s) |
| 82.56 | 1:22.6 | m.45 | chorus (22.5 s) |
| 105.06 | 1:45.1 | m.57 | chorus (30.0 s) |
| 135.06 | 2:15.1 | m.73 | altchorus (15.0 s) |
| 150.06 | 2:30.1 | m.81 | break (15.0 s) |
| 165.06 | 2:45.1 | m.89 | chorus (15.0 s) |
| 180.06 | 3:00.1 | m.97 | chorus (15.0 s) |
| 195.06 | 3:15.1 | m.105 | postchorus (15.0 s) |
| 210.06 | 3:30.1 | m.113 | postchorus (15.0 s) |
| 225.06 | 3:45.1 | m.121 | postchorus (15.0 s) |
| 240.06 | 4:00.1 | m.129 | instchorus (15.0 s) |
| 255.06 | 4:15.1 | m.137 | breakdown (30.0 s) |
| 285.06 | 4:45.1 | m.153 | saxobeat (24.4 s) |
| 309.43 | 5:09.4 | m.166 | end |

### 0869_raiseyourweapon — deadmau5 – Raise Your Weapon (140 BPM, 7:53.0, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (30.0 s) |
| 30.06 | 0:30.1 | m.17 | prechorus (15.0 s) |
| 45.06 | 0:45.1 | m.25 | chorus (15.0 s) |
| 60.06 | 1:00.1 | m.33 | inst (30.0 s) |
| 90.06 | 1:30.1 | m.49 | verse (30.0 s) |
| 120.06 | 2:00.1 | m.65 | prechorus (15.0 s) |
| 135.06 | 2:15.1 | m.73 | chorus (15.0 s) |
| 150.06 | 2:30.1 | m.81 | break (30.0 s) |
| 180.06 | 3:00.1 | m.97 | verse (14.7 s) |
| 194.73 | 3:14.7 | m.105 | chorus (17.4 s) |
| 212.16 | 3:32.2 | m.115 | bridge (54.9 s) |
| 267.02 | 4:27.0 | m.147 | verse (27.4 s) |
| 294.45 | 4:54.4 | m.163 | prechorus (13.7 s) |
| 308.16 | 5:08.2 | m.171 | chorus (13.7 s) |
| 321.87 | 5:21.9 | m.179 | postchorus (41.1 s) |
| 363.02 | 6:03.0 | m.203 | chorus (13.7 s) |
| 376.73 | 6:16.7 | m.211 | inst2 (27.4 s) |
| 404.16 | 6:44.2 | m.227 | intro (51.4 s) |
| 455.59 | 7:35.6 | m.257 | end |

### 0891_savetheworld — Swedish House Mafia – Save the World (radio remix) (128 BPM, 3:24.7, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (7.5 s) |
| 7.56 | 0:07.6 | m.5 | verse (14.1 s) |
| 21.62 | 0:21.6 | m.12 (temps 3) | prechorus (15.0 s) |
| 36.62 | 0:36.6 | m.20 (temps 3) | chorus (30.9 s) |
| 67.56 | 1:07.6 | m.37 | inst (15.0 s) |
| 82.56 | 1:22.6 | m.45 | postchorus (16.9 s) |
| 99.43 | 1:39.4 | m.54 | verse (14.1 s) |
| 113.50 | 1:53.5 | m.61 (temps 3) | prechorus (15.0 s) |
| 128.50 | 2:08.5 | m.69 (temps 3) | chorus (30.9 s) |
| 159.43 | 2:39.4 | m.86 | postchorus (14.1 s) |
| 173.50 | 2:53.5 | m.93 (temps 3) | chorus (30.9 s) |
| 204.43 | 3:24.4 | m.110 | end |

### 0895_scarymonsters — Skrillex – Scary Monsters & Nice Sprites (Kaskade remix) (128 BPM, 6:09.8, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.06 | 0:00.1 | m.1 | intro (30.0 s) |
| 30.06 | 0:30.1 | m.17 | break (15.0 s) |
| 45.06 | 0:45.1 | m.25 | chorus (15.0 s) |
| 60.06 | 1:00.1 | m.33 | chorus (15.0 s) |
| 75.06 | 1:15.1 | m.41 | postchorus (15.0 s) |
| 90.06 | 1:30.1 | m.49 | postchorus (15.0 s) |
| 105.06 | 1:45.1 | m.57 | postchorus (15.0 s) |
| 120.06 | 2:00.1 | m.65 | build (46.9 s) |
| 166.93 | 2:46.9 | m.90 | inst (15.0 s) |
| 181.93 | 3:01.9 | m.98 | inst (15.0 s) |
| 196.93 | 3:16.9 | m.106 | inst2 (15.0 s) |
| 211.93 | 3:31.9 | m.114 | inst2 (15.0 s) |
| 226.93 | 3:46.9 | m.122 | inst2 (15.0 s) |
| 241.93 | 4:01.9 | m.130 | inst2 (15.0 s) |
| 256.93 | 4:16.9 | m.138 | break2 (7.5 s) |
| 264.43 | 4:24.4 | m.142 | inst2 (15.0 s) |
| 279.43 | 4:39.4 | m.150 | chorus (15.0 s) |
| 294.43 | 4:54.4 | m.158 | inst2 (15.0 s) |
| 309.43 | 5:09.4 | m.166 | inst2 (15.0 s) |
| 324.43 | 5:24.4 | m.174 | inst2 (15.0 s) |
| 339.43 | 5:39.4 | m.182 | inst2 (15.0 s) |
| 354.43 | 5:54.4 | m.190 | inst2 (15.0 s) |
| 369.43 | 6:09.4 | m.198 | end |

### 0900_sexychickakon — David Guetta feat. Akon – Sexy Chick (130 BPM, 3:13.2, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.04 | 0:00.0 | m.1 | intro (44.3 s) |
| 44.35 | 0:44.3 | m.25 | chorus (29.5 s) |
| 73.89 | 1:13.9 | m.41 | chorus2 (29.5 s) |
| 103.43 | 1:43.4 | m.57 | verse (29.6 s) |
| 133.02 | 2:13.0 | m.73 | chorus (29.5 s) |
| 162.50 | 2:42.5 | m.89 | chorus2 (29.6 s) |
| 192.10 | 3:12.1 | m.105 | end |

### 0909_sofineed — deadmau5 – Sofi Needs a Ladder (128 BPM, 6:01.5, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.25 | 0:00.2 | m.1 (temps 2) | intro (31.5 s) |
| 31.74 | 0:31.7 | m.18 | section (30.0 s) |
| 61.74 | 1:01.7 | m.34 | section (30.0 s) |
| 91.74 | 1:31.7 | m.50 | section (30.0 s) |
| 121.74 | 2:01.7 | m.66 | section (30.0 s) |
| 151.74 | 2:31.7 | m.82 | section (30.0 s) |
| 181.74 | 3:01.7 | m.98 | section (30.0 s) |
| 211.74 | 3:31.7 | m.114 | section (30.0 s) |
| 241.74 | 4:01.7 | m.130 | section (30.0 s) |
| 271.74 | 4:31.7 | m.146 | section (30.0 s) |
| 301.74 | 5:01.7 | m.162 | section (30.0 s) |
| 331.74 | 5:31.7 | m.178 | outro (29.1 s) |
| 360.80 | 6:00.8 | m.193 (temps 3) | end |

### 0929_takeovercontrolext — Afrojack feat. Eva Simmons – Take Over Control (extended) (130 BPM, 6:12.4, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.07 | 0:00.1 | m.1 | intro (29.5 s) |
| 29.61 | 0:29.6 | m.17 | verse (29.5 s) |
| 59.15 | 0:59.2 | m.33 | verse (29.5 s) |
| 88.69 | 1:28.7 | m.49 | chorus (29.5 s) |
| 118.23 | 1:58.2 | m.65 | section (27.7 s) |
| 145.92 | 2:25.9 | m.80 | chorus2 (16.6 s) |
| 162.54 | 2:42.5 | m.89 | chorus (14.8 s) |
| 177.31 | 2:57.3 | m.97 | verse (29.5 s) |
| 206.84 | 3:26.8 | m.113 | chorus (29.5 s) |
| 236.38 | 3:56.4 | m.129 | transition (14.8 s) |
| 251.21 | 4:11.2 | m.137 | section (29.5 s) |
| 280.69 | 4:40.7 | m.153 | outro (27.7 s) |
| 308.38 | 5:08.4 | m.168 | outro (31.4 s) |
| 339.77 | 5:39.8 | m.185 | outro (29.6 s) |
| 369.36 | 6:09.4 | m.201 | end |

### 0965_wakingupinvegascalvin — Katy Perry – Waking Up in Vegas (Calvin Harris extended remix) (131 BPM, 4:31.7, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.28 | 0:00.3 | m.1 | intro (16.5 s) |
| 16.77 | 0:16.8 | m.10 | verse (27.5 s) |
| 44.25 | 0:44.2 | m.25 | break (7.3 s) |
| 51.58 | 0:51.6 | m.29 | transition (29.3 s) |
| 80.89 | 1:20.9 | m.45 | chorus (29.3 s) |
| 110.20 | 1:50.2 | m.61 | verse (27.5 s) |
| 137.68 | 2:17.7 | m.76 | break (9.2 s) |
| 146.84 | 2:26.8 | m.81 | transition (29.3 s) |
| 176.16 | 2:56.2 | m.97 | chorus (29.3 s) |
| 205.47 | 3:25.5 | m.113 | bridge (29.3 s) |
| 234.78 | 3:54.8 | m.129 | break (7.3 s) |
| 242.11 | 4:02.1 | m.133 | chorus (29.3 s) |
| 271.42 | 4:31.4 | m.149 | end |

### 0966_wakingupinvegascalvinh — Katy Perry – Waking Up in Vegas (Calvin Harris remix edit) (131 BPM, 3:39.5, Dance/Electronic)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.11 | 0:00.1 | m.1 | verse1 (29.3 s) |
| 29.42 | 0:29.4 | m.17 | break (7.3 s) |
| 36.75 | 0:36.7 | m.21 | intro (14.7 s) |
| 51.40 | 0:51.4 | m.29 | chorus (14.7 s) |
| 66.06 | 1:06.1 | m.37 | verse2 (29.3 s) |
| 95.37 | 1:35.4 | m.53 | break (7.3 s) |
| 102.70 | 1:42.7 | m.57 | transition (14.7 s) |
| 117.36 | 1:57.4 | m.65 | chorus (14.7 s) |
| 132.02 | 2:12.0 | m.73 | chorus (14.7 s) |
| 146.67 | 2:26.7 | m.81 | transition (29.4 s) |
| 176.10 | 2:56.1 | m.97 | break (7.2 s) |
| 183.31 | 3:03.3 | m.101 | chorus (14.7 s) |
| 197.97 | 3:18.0 | m.109 | chorus (14.8 s) |
| 212.74 | 3:32.7 | m.117 | outro (6.3 s) |
| 219.04 | 3:39.0 | m.120 (temps 3) | end |

### 0979_whenlovetakesover — David Guetta feat. Kelly Rowland – When Love Takes Over (130 BPM, 3:04.9, Pop)
| t (s) | mm:ss | mesure (downbeat le plus proche) | section |
|---|---|---|---|
| 0.09 | 0:00.1 | m.1 | intro (7.4 s) |
| 7.47 | 0:07.5 | m.5 | verse (14.8 s) |
| 22.30 | 0:22.3 | m.13 | verse2 (14.7 s) |
| 37.01 | 0:37.0 | m.21 | chorus (14.8 s) |
| 51.78 | 0:51.8 | m.29 | verse3 (14.8 s) |
| 66.55 | 1:06.5 | m.37 | verse4 (14.8 s) |
| 81.32 | 1:21.3 | m.45 | chorus (14.8 s) |
| 96.09 | 1:36.1 | m.53 | break (14.8 s) |
| 110.86 | 1:50.9 | m.61 | bridge (14.8 s) |
| 125.68 | 2:05.7 | m.69 | outro (44.2 s) |
| 169.93 | 2:49.9 | m.93 | outro2 (14.8 s) |
| 184.76 | 3:04.8 | m.101 | end |