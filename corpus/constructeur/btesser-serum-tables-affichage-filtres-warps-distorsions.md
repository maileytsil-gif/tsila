---
titre: "Serum 1.3x — tables d’affichage lues dans le plug-in : types de filtre, warps, distorsions, stack d’unisson, formes du sub, EQ, modes de delay, ratios de compresseur, échelles de rate LFO et unités de 55 paramètres (btesser/serum2vital, tools/serum_display_tables.json)"
source: https://raw.githubusercontent.com/btesser/serum2vital/main/tools/serum_display_tables.json
recupere_le: 2026-09-24
mode: extraction
langue: en
axe: documentation constructeur ; Serum 2 ; format de preset et paramètres (rétro-ingénierie tierce)
skills: sound-designer-serum, vst-sound-design, studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---


# Tables d’affichage de Serum (lues dans le plug-in par serum2vital)

Conversion en Markdown du fichier JSON `tools/serum_display_tables.json` (Serum 1.3x, VST2 ; les listes de filtres, warps, distorsions et stacks sont conservées à l’identique dans Serum 2, qui y ajoute des entrées). Les échelles à 229 pas sont résumées par valeurs distinctes.

## Listes de menus (`enums`)

### Fil Type (96 pas, valeurs distinctes dans l’ordre)

MG Low 6 · MG Low 12 · MG Low 18 · MG Low 24 · Low 6 · Low 12 · Low 18 · Low 24 · High 6 · High 12 · High 18 · High 24 · Band 12 · Band 24 · Peak 12 · Peak 24 · Notch 12 · Notch 24 · LH 6 · LH 12 · LB 12 · LP 12 · LN 12 · HB 12 · HP 12 · HN 12 · BP 12 · BN 12 · PP 12 · PN 12 · NN 12 · L/B/H 12 · L/B/H 24 · L/P/H 12 · L/P/H 24 · L/N/H 12 · L/N/H 24 · B/P/N 12 · B/P/N 24 · Cmb + · Cmb - · Cmb L6+ · Cmb L6- · Cmb H6+ · Cmb H6- · Cmb HL6+ · Cmb HL6- · Flg + · Flg - · Flg L6+ · Flg L6- · Flg H6+ · Flg H6- · Flg HL6+ · Flg HL6- · Phs 12+ · Phs 12- · Phs 24+ · Phs 24- · Phs 36+ · Phs 36- · Phs 48+ · Phs 48- · Phs 48L6+ · Phs 48L6- · Phs 48H6+ · Phs 48H6- · Phs 48HL6+ · Phs 48HL6- · FPhs 12HL6+ · FPhs 12HL6- · Low EQ 6 · Low EQ 12 · Band EQ 12 · High EQ 6 · High EQ 12 · Ring Mod · Ring Modx2 · SampHold · SampHold- · Combs · Allpasses · Reverb · French LP · German LP · Add Bass · Formant-I · Formant-II · Formant-III · Bandreject · Dist.Comb 1 LP · Dist.Comb 1 BP · Dist.Comb 2 LP · Dist.Comb 2 BP · Scream LP · Scream BP

### FX Fil Type (96 pas, valeurs distinctes dans l’ordre)

MG Low 6 · MG Low 12 · MG Low 18 · MG Low 24 · Low 6 · Low 12 · Low 18 · Low 24 · High 6 · High 12 · High 18 · High 24 · Band 12 · Band 24 · Peak 12 · Peak 24 · Notch 12 · Notch 24 · LH 6 · LH 12 · LB 12 · LP 12 · LN 12 · HB 12 · HP 12 · HN 12 · BP 12 · BN 12 · PP 12 · PN 12 · NN 12 · L/B/H 12 · L/B/H 24 · L/P/H 12 · L/P/H 24 · L/N/H 12 · L/N/H 24 · B/P/N 12 · B/P/N 24 · Cmb + · Cmb - · Cmb L6+ · Cmb L6- · Cmb H6+ · Cmb H6- · Cmb HL6+ · Cmb HL6- · Flg + · Flg - · Flg L6+ · Flg L6- · Flg H6+ · Flg H6- · Flg HL6+ · Flg HL6- · Phs 12+ · Phs 12- · Phs 24+ · Phs 24- · Phs 36+ · Phs 36- · Phs 48+ · Phs 48- · Phs 48L6+ · Phs 48L6- · Phs 48H6+ · Phs 48H6- · Phs 48HL6+ · Phs 48HL6- · FPhs 12HL6+ · FPhs 12HL6- · Low EQ 6 · Low EQ 12 · Band EQ 12 · High EQ 6 · High EQ 12 · Ring Mod · Ring Modx2 · SampHold · SampHold- · Combs · Allpasses · Reverb · French LP · German LP · Add Bass · Formant-I · Formant-II · Formant-III · Bandreject · Dist.Comb 1 LP · Dist.Comb 1 BP · Dist.Comb 2 LP · Dist.Comb 2 BP · Scream LP · Scream BP

### WarpOscA (24 entrées)

0. Off
1. Sync
2. Sync 1/2 Win.
3. Sync Window
4. Bend +
5. Bend -
6. Bend +/-
7. PWM
8. Asym +
9. Asym -
10. Asym +/-
11. Flip
12. Mirror
13. Remap 1
14. Remap 2
15. Remap 3
16. Remap 4
17. Quantize
18. FM (from B)
19. AM (from B)
20. RM (from B)
21. FM (Noise)
22. FM (Sub)
23. 

### WarpOscB (24 entrées)

0. Off
1. Sync
2. Sync 1/2 Win.
3. Sync Window
4. Bend +
5. Bend -
6. Bend +/-
7. PWM
8. Asym +
9. Asym -
10. Asym +/-
11. Flip
12. Mirror
13. Remap 1
14. Remap 2
15. Remap 3
16. Remap 4
17. Quantize
18. FM (from A)
19. AM (from A)
20. RM (from A)
21. FM (Noise)
22. FM (Sub)
23. 

### Dist_Mode (16 entrées)

0. Tube
1. SoftClip
2. HardClip
3. Diode 1
4. Diode 2
5. Lin.Fold
6. Sin Fold
7. Zero-Square
8. Downsample
9. Asym
10. Rectify
11. X-Shaper
12. X-Shaper (Asym)
13. Sine Shaper
14. Stomp Box
15. Tape Sat.

### A Uni Stack (9 entrées)

0. off
1. 12 (1x)
2. 12 (2x)
3. 12 (3x)
4. 12+7(1x)
5. 12+7(2x)
6. 12+7(3x)
7. Center-12
8. Center-24

### SubOscShape (5 entrées)

0. Sine
1. RoundRect
2. Saw
3. Square
4. Pulse

### EQ TypL (3 entrées)

0. Shelf
1. Peak
2. LPF

### EQ TypH (3 entrées)

0. Shelf
1. Peak
2. LPF

### Dly_Mode (3 entrées)

0. Normal
1. Ping-Pong
2. Tap->Delay

### Hyp_Unison (8 entrées)

0. 0
1. 1
2. 2
3. 3
4. 4
5. 5
6. 6
7. 7

### Cmp_Rat (229 pas, valeurs distinctes dans l’ordre)

1:1 · 1.0:1 · 1.1:1 · 1.2:1 · 1.3:1 · 1.4:1 · 1.5:1 · 1.6:1 · 1.7:1 · 1.8:1 · 1.9:1 · 2:1 · 3:1 · 4:1 · 5:1 · 6:1 · 7:1 · 8:1 · 10:1 · 16:1 · 32:1 · Limit

### Dly_TimL (229 pas, valeurs distinctes dans l’ordre)

fast · 1/256 · 1/128 · 1/64 · 1/32 · 1/16 · 1/8 · 1/4 · 1/2 · bar · 2 bar · 4 bar

### Dly_TimR (229 pas, valeurs distinctes dans l’ordre)

fast · 1/256 · 1/128 · 1/64 · 1/32 · 1/16 · 1/8 · 1/4 · 1/2 · bar · 2 bar · 4 bar

## Noms des 316 paramètres VST de Serum 1 (`names`, index = ordre VST)

0. MasterVol
1. A Vol
2. A Pan
3. A Octave
4. A Semi
5. A Fine
6. A Unison
7. A UniDet
8. A UniBlend
9. A Warp
10. A CoarsePit
11. A WTPos
12. A RandPhase
13. A Phase
14. B Vol
15. B Pan
16. B Octave
17. B Semi
18. B Fine
19. B Unison
20. B UniDet
21. B UniBlend
22. B Warp
23. B CoarsePit
24. B WTPos
25. B RandPhase
26. B Phase
27. Noise Level
28. Noise Pitch
29. Noise Fine
30. Noise Pan
31. Noise RandPhase
32. Noise Phase
33. Sub Osc Level
34. Sub Osc Pan
35. Env1 Atk
36. Env1 Hold
37. Env1 Dec
38. Env1 Sus
39. Env1 Rel
40. OscA>Fil
41. OscB>Fil
42. OscN>Fil
43. OscS>Fil
44. Fil Type
45. Fil Cutoff
46. Fil Reso
47. Fil Driv
48. Fil Var
49. Fil Mix
50. Fil Stereo
51. Env2 Atk
52. Env2 Hld
53. Env2 Dec
54. Env2 Sus
55. Env2 Rel
56. Env3 Atk
57. Env3 Hld
58. Env3 Dec
59. Env3 Sus
60. Env3 Rel
61. LFO1 Rate
62. LFO2 Rate
63. LFO3 Rate
64. LFO4 Rate
65. PortTime
66. PortCurve
67. Chaos1 BPM
68. Chaos2 BPM
69. Chaos1 Rate
70. Chaos2 Rate
71. A curve1
72. D curve1
73. R curve1
74. A curve2
75. D curve2
76. R curve2
77. A curve3
78. D curve3
79. R curve3
80. Mast.Tun
81. Verb Wet
82. VerbSize
83. Decay
84. VerbLoCt
85. Spin Rate
86. VerbHiCt
87. Spin Depth
88. EQ FrqL
89. EQ FrqH
90. EQ Q L
91. EQ Q H
92. EQ VolL
93. EQ VolH
94. EQ TypL
95. EQ TypH
96. Dist_Wet
97. Dist_Drv
98. Dist_L/B/H
99. Dist_Mode
100. Dist_Freq
101. Dist_BW
102. Dist_PrePost
103. Flg_Wet
104. Flg_BPM_Sync
105. Flg_Rate
106. Flg_Dep
107. Flg_Feed
108. Flg_Stereo
109. Phs_Wet
110. Phs_BPM_Sync
111. Phs_Rate
112. Phs_Dpth
113. Phs_Frq
114. Phs_Feed
115. Phs_Stereo
116. Cho_Wet
117. Cho_BPM_Sync
118. Cho_Rate
119. Cho_Dly
120. Cho_Dly2
121. Cho_Dep
122. Cho_Feed
123. Cho_Filt
124. Dly_Wet
125. Dly_Freq
126. Dly_BW
127. Dly_BPM_Sync
128. Dly_Link
129. Dly_TimL
130. Dly_TimR
131. Dly_Mode
132. Dly_Feed
133. Dly_Off L
134. Dly_Off R
135. Cmp_Thr
136. Cmp_Rat
137. Cmp_Att
138. Cmp_Rel
139. CmpGain
140. CmpMBnd
141. FX Fil Wet
142. FX Fil Type
143. FX Fil Freq
144. FX Fil Reso
145. FX Fil Drive
146. FX Fil Var
147. Hyp_Wet
148. Hyp_Rate
149. Hyp_Detune
150. Hyp_Unison
151. Hyp_Retrig
152. HypDim_Size
153. HypDim_Mix
154. Dist Enable
155. Flg Enable
156. Phs Enable
157. Cho Enable
158. Dly Enable
159. Comp Enable
160. Rev Enable
161. EQ Enable
162. FX Fil Enable
163. Hyp Enable
164. OscAPitchTrack
165. OscBPitchTrack
166. Bend U
167. Bend D
168. WarpOscA
169. WarpOscB
170. SubOscShape
171. SubOscOctave
172. A Uni LR
173. B Uni LR
174. A Uni Warp
175. B Uni Warp
176. A Uni WTPos
177. B Uni WTPos
178. A Uni Stack
179. B Uni Stack
180. Mod 1 amt
181. Mod 1 out
182. Mod 2 amt
183. Mod 2 out
184. Mod 3 amt
185. Mod 3 out
186. Mod 4 amt
187. Mod 4 out
188. Mod 5 amt
189. Mod 5 out
190. Mod 6 amt
191. Mod 6 out
192. Mod 7 amt
193. Mod 7 out
194. Mod 8 amt
195. Mod 8 out
196. Mod 9 amt
197. Mod 9 out
198. Mod10 amt
199. Mod10 out
200. Mod11 amt
201. Mod11 out
202. Mod12 amt
203. Mod12 out
204. Mod13 amt
205. Mod13 out
206. Mod14 amt
207. Mod14 out
208. Mod15 amt
209. Mod15 out
210. Mod16 amt
211. Mod16 out
212. Osc A On
213. Osc B On
214. Osc N On
215. Osc S On
216. Filter On
217. Mod Wheel
218. Macro 1
219. Macro 2
220. Macro 3
221. Macro 4
222. Amp.
223. LFO1 smooth
224. LFO2 smooth
225. LFO3 smooth
226. LFO4 smooth
227. Pitch Bend
228. Mod17 amt
229. Mod17 out
230. Mod18 amt
231. Mod18 out
232. Mod19 amt
233. Mod19 out
234. Mod20 amt
235. Mod20 out
236. Mod21 amt
237. Mod21 out
238. Mod22 amt
239. Mod22 out
240. Mod23 amt
241. Mod23 out
242. Mod24 amt
243. Mod24 out
244. Mod25 amt
245. Mod25 out
246. Mod26 amt
247. Mod26 out
248. Mod27 amt
249. Mod27 out
250. Mod28 amt
251. Mod28 out
252. Mod29 amt
253. Mod29 out
254. Mod30 amt
255. Mod30 out
256. Mod31 amt
257. Mod31 out
258. Mod32 amt
259. Mod32 out
260. LFO5 Rate
261. LFO6 Rate
262. LFO7 Rate
263. LFO8 Rate
264. LFO5 smooth
265. LFO6 smooth
266. LFO7 smooth
267. LFO8 smooth
268. FX Fil Pan
269. Comp_Wet
270. CompMB L
271. CompMB M
272. CompMB H
273. LFO1 Rise
274. LFO2 Rise
275. LFO3 Rise
276. LFO4 Rise
277. LFO5 Rise
278. LFO6 Rise
279. LFO7 Rise
280. LFO8 Rise
281. LFO1 Delay
282. LFO2 Delay
283. LFO3 Delay
284. LFO4 Delay
285. LFO5 Delay
286. LFO6 Delay
287. LFO7 Delay
288. LFO8 Delay
289. FX Dist Level
290. FX Flg Level
291. FX Phaser Level
292. FX Chorus Level
293. FX Delay Level
294. FX Comp Level
295. FX Reverb Level
296. FX DimExp Level
297. FX Filter Level
298. FX Hyper Level
299. LFO Bus 1
300. LFO Bus 2
301. LFO Bus 3
302. LFO Bus 4
303. LFO Bus 5
304. LFO Bus 6
305. LFO Bus 7
306. LFO Bus 8
307. LFO Bus 9
308. LFO Bus 10
309. LFO Bus 11
310. LFO Bus 12
311. LFO Bus 13
312. LFO Bus 14
313. LFO Bus 15
314. LFO Bus 16
315. Bypass

## Unités et plages affichées (`units`, 55 paramètres : min → max sur la course du bouton)

| Paramètre | Minimum | Milieu | Maximum |
|---|---|---|---|

| Fil Cutoff | 8 | 425 | 22050 |

| Env1 Atk | 0.0 | 1.00 | 32.0 |

| Env1 Dec | 0.0 | 1.00 | 32.0 |

| Env1 Rel | 0.0 | 1.00 | 32.0 |

| Env1 Hold | 0.0 | 1.00 | 32.0 |

| Env1 Sus | -oo | -12.0 | 0.0 |

| Env2 Sus | 0.00 | 50.00 | 100.00 |

| A UniDet | 0.00 | 0.25 | 1.00 |

| Fil Driv | 0 | 50 | 100 |

| Fil Reso | 0 | 50 | 100 |

| VerbSize | 0 | 50 | 100 |

| Dly_TimL | fast | 1/16 | 4 bar |

| Cho_Rate | 0.00 | 1.25 | 20.00 |

| Cho_Dly | 0.0 | 5.0 | 20.0 |

| Cho_Dep | 0.0 | 6.5 | 26.0 |

| Cho_Filt | 50 | 1000 | 20000 |

| Phs_Frq | 20 | 600 | 18000 |

| Phs_Rate | 0.00 | 1.25 | 20.00 |

| Flg_Rate | 0.00 | 1.25 | 20.00 |

| Hyp_Rate | 0 | 50 | 100 |

| Hyp_Detune | 0 | 50 | 100 |

| HypDim_Size | 0 | 50 | 100 |

| Hyp_Unison | 0 | 4 | 7 |

| Dist_Freq | 8 | 330 | 13290 |

| Dist_Drv | 0 | 50 | 100 |

| EQ FrqL | 22 | 656 | 20000 |

| Cmp_Thr | 0.0 | -18.1 | -120.0 |

| Cmp_Rat | 1:1 | 2:1 | Limit |

| Cmp_Att | 0.1 | 250.1 | 1000.0 |

| Cmp_Rel | 0.1 | 249.9 | 999.1 |

| CmpGain | 0.0 | 18.8 | 30.1 |

| PortTime | 0 | 250 | 8.00 |

| A CoarsePit | -64.00 | -- | 64.00 |

| Noise Pitch | 0 | 50 | 100 |

| LFO1 Rise | 0.0 s | 2.0 s | 4.0 s |

| LFO1 Delay | 0.0 s | 2.0 s | 4.0 s |

| LFO1 smooth | 0 | 50 | 100 |

| Dist_Mode | Tube | Downsample | Tape Sat. |

| Dly_Freq | 40 | 849 | 18000 |

| Dly_BW | 0.8 | 4.5 | 8.2 |

| A curve1 | 0 | 50 | 100 |

| Dist_L/B/H | 0 | 50 | 100 |

| Cho_Feed | 0 | 48 | 95 |

| Chaos1 Rate | 0.000 | 31.250 | 1000.000 |

| Bend U | -24 | 0 | 24 |

| MasterVol | 0% (-oo dB) | 50% (-18.1 dB) | 100% (0.0 dB) |

| A Vol | 0% (-oo dB) | 50% (-12.0 dB) | 100% (0.0 dB) |

| Amp. |  |  |  |

| Mast.Tun |  |  |  |

| A Uni WTPos | -100 | 0 | 100 |

| A Uni Warp | -100 | 0 | 100 |

| A Uni LR | 0 | 50 | 100 |

| VerbLoCt | 0 | 50 | 100 |

| VerbHiCt | 0 | 50 | 100 |

| Comp_Wet | 0 | 50 | 100 |


## Échelles complètes (`tables`)


### LFO1 Rate [B0] (229 pas)

32 bar · 16 bar · 8 bar · 4 bar · 2 bar · bar · 1/2 · 1/4 · 1/8 · 1/16 · 1/32 · 1/64 · 1/128 · 1/256 · fast


### Chaos1 Rate [B0] (229 pas)

0.000 · 0.001 · 0.002 · 0.003 · 0.004 · 0.005 · 0.007 · 0.008 · 0.010 · 0.013 · 0.016 · 0.019 · 0.023 · 0.028 · 0.033 · 0.039 · 0.046 · 0.054 · 0.064 · 0.074 · 0.085 · 0.098 · 0.113 · 0.129 · 0.146 · 0.166 · 0.188 · 0.212 · 0.239 · 0.268 · 0.299 · 0.334 · 0.372 · 0.414 · 0.458 · 0.507 · 0.560 · 0.617 · 0.679 · 0.745 · 0.817 · 0.894 · 0.977 · 1.065 · 1.160 · 1.262 · 1.371 · 1.487 · 1.611 · 1.743 · 1.883 · 2.033 · 2.191 · 2.360 · 2.538 · 2.728 · 2.928 · 3.140 · 3.365 · 3.602 · 3.852 · 4.115 · 4.393 · 4.686 · 4.994 · 5.318 · 5.659 · 6.017 · 6.393 · 6.788 · 7.201 · 7.635 · 8.090 · 8.565 · 9.063 · 9.584 · 10.128 · 10.697 · 11.291 · 11.911 · 12.559 · 13.234 · 13.937 · 14.671 · 15.435 · 16.230 · 17.058 · 17.920 · 18.815 · 19.747 · 20.714 · 21.720 · 22.764 · 23.848 · 24.972 · 26.139 · 27.349 · 28.603 · 29.903 · 31.250 · 32.645 · 34.089 · 35.584 · 37.131 · 38.731 · 40.386 · 42.097 · 43.866 · 45.693 · 47.581 · 49.531 · 51.544 · 53.622 · 55.767 · 57.979 · 60.262 · 62.616 · 65.042 · 67.544 · 70.121 · 72.777 · 75.513 · 78.330 · 81.231 · 84.217 · 87.290 · 90.453 · 93.706 · 97.052 · 100.494 · 104.032 · 107.669 · 111.407 · 115.248 · 119.195 · 123.249 · 127.412 · 131.687 · 136.076 · 140.582 · 145.206 · 149.951 · 154.819 · 159.813 · 164.934 · 170.187 · 175.572 · 181.093 · 186.751 · 192.551 · 198.493 · 204.581 · 210.818 · 217.206 · 223.748 · 230.447 · 237.305 · 244.325 · 251.511 · 258.864 · 266.389 · 274.087 · 281.963 · 290.019 · 298.257 · 306.682 · 315.296 · 324.103 · 333.105 · 342.306 · 351.710 · 361.319 · 371.137 · 381.167 · 391.413 · 401.878 · 412.565 · 423.479 · 434.623 · 445.999 · 457.614 · 469.468 · 481.567 · 493.914 · 506.514 · 519.369 · 532.483 · 545.862 · 559.508 · 573.425 · 587.618 · 602.091 · 616.847 · 631.891 · 647.228 · 662.861 · 678.794 · 695.033 · 711.580 · 728.441 · 745.621 · 763.123 · 780.952 · 799.113 · 817.610 · 836.448 · 855.632 · 875.166 · 895.056 · 915.305 · 935.919 · 956.903 · 978.262 · 1000.000


### LFO1 Rate [B1] (229 pas)

0.000 Hz · 0.001 Hz · 0.002 Hz · 0.003 Hz · 0.004 Hz · 0.005 Hz · 0.006 Hz · 0.007 Hz · 0.009 Hz · 0.01 Hz · 0.02 Hz · 0.03 Hz · 0.04 Hz · 0.05 Hz · 0.06 Hz · 0.07 Hz · 0.08 Hz · 0.09 Hz · 0.1 Hz · 0.2 Hz · 0.3 Hz · 0.4 Hz · 0.5 Hz · 0.6 Hz · 0.7 Hz · 0.8 Hz · 0.9 Hz · 1.0 Hz · 1.1 Hz · 1.2 Hz · 1.3 Hz · 1.4 Hz · 1.5 Hz · 1.6 Hz · 1.7 Hz · 1.8 Hz · 1.9 Hz · 2.0 Hz · 2.1 Hz · 2.2 Hz · 2.3 Hz · 2.4 Hz · 2.5 Hz · 2.7 Hz · 2.8 Hz · 2.9 Hz · 3.0 Hz · 3.1 Hz · 3.3 Hz · 3.4 Hz · 3.6 Hz · 3.7 Hz · 3.9 Hz · 4.0 Hz · 4.2 Hz · 4.3 Hz · 4.5 Hz · 4.7 Hz · 4.9 Hz · 5.0 Hz · 5.2 Hz · 5.4 Hz · 5.6 Hz · 5.8 Hz · 6.0 Hz · 6.2 Hz · 6.5 Hz · 6.7 Hz · 6.9 Hz · 7.2 Hz · 7.4 Hz · 7.7 Hz · 7.9 Hz · 8.2 Hz · 8.5 Hz · 8.7 Hz · 9.0 Hz · 9.3 Hz · 9.6 Hz · 9.9 Hz · 10.2 Hz · 10.6 Hz · 10.9 Hz · 11.2 Hz · 11.6 Hz · 11.9 Hz · 12.3 Hz · 12.7 Hz · 13.0 Hz · 13.4 Hz · 13.8 Hz · 14.2 Hz · 14.6 Hz · 15.0 Hz · 15.5 Hz · 15.9 Hz · 16.4 Hz · 16.8 Hz · 17.3 Hz · 17.8 Hz · 18.2 Hz · 18.7 Hz · 19.2 Hz · 19.8 Hz · 20.3 Hz · 20.8 Hz · 21.4 Hz · 21.9 Hz · 22.5 Hz · 23.1 Hz · 23.7 Hz · 24.3 Hz · 24.9 Hz · 25.5 Hz · 26.1 Hz · 26.8 Hz · 27.4 Hz · 28.1 Hz · 28.8 Hz · 29.5 Hz · 30.2 Hz · 30.9 Hz · 31.6 Hz · 32.4 Hz · 33.1 Hz · 33.9 Hz · 34.7 Hz · 35.5 Hz · 36.3 Hz · 37.1 Hz · 38.0 Hz · 38.8 Hz · 39.7 Hz · 40.6 Hz · 41.5 Hz · 42.4 Hz · 43.3 Hz · 44.3 Hz · 45.3 Hz · 46.2 Hz · 47.2 Hz · 48.2 Hz · 49.2 Hz · 50.3 Hz · 51.3 Hz · 52.4 Hz · 53.5 Hz · 54.6 Hz · 55.7 Hz · 56.9 Hz · 58.0 Hz · 59.2 Hz · 60.4 Hz · 61.6 Hz · 62.8 Hz · 64.1 Hz · 65.4 Hz · 66.6 Hz · 67.9 Hz · 69.3 Hz · 70.6 Hz · 72.0 Hz · 73.3 Hz · 74.7 Hz · 76.2 Hz · 77.6 Hz · 79.1 Hz · 80.6 Hz · 82.1 Hz · 83.6 Hz · 85.1 Hz · 86.7 Hz · 88.3 Hz · 89.9 Hz · 91.5 Hz · 93.2 Hz · 94.8 Hz · 96.5 Hz · 98.3 Hz · 100.0 Hz


### Chaos1 Rate [B1] (229 pas)

0.000 · 0.001 · 0.002 · 0.003 · 0.004 · 0.005 · 0.007 · 0.008 · 0.010 · 0.013 · 0.016 · 0.019 · 0.023 · 0.028 · 0.033 · 0.039 · 0.046 · 0.054 · 0.064 · 0.074 · 0.085 · 0.098 · 0.113 · 0.129 · 0.146 · 0.166 · 0.188 · 0.212 · 0.239 · 0.268 · 0.299 · 0.334 · 0.372 · 0.414 · 0.458 · 0.507 · 0.560 · 0.617 · 0.679 · 0.745 · 0.817 · 0.894 · 0.977 · 1.065 · 1.160 · 1.262 · 1.371 · 1.487 · 1.611 · 1.743 · 1.883 · 2.033 · 2.191 · 2.360 · 2.538 · 2.728 · 2.928 · 3.140 · 3.365 · 3.602 · 3.852 · 4.115 · 4.393 · 4.686 · 4.994 · 5.318 · 5.659 · 6.017 · 6.393 · 6.788 · 7.201 · 7.635 · 8.090 · 8.565 · 9.063 · 9.584 · 10.128 · 10.697 · 11.291 · 11.911 · 12.559 · 13.234 · 13.937 · 14.671 · 15.435 · 16.230 · 17.058 · 17.920 · 18.815 · 19.747 · 20.714 · 21.720 · 22.764 · 23.848 · 24.972 · 26.139 · 27.349 · 28.603 · 29.903 · 31.250 · 32.645 · 34.089 · 35.584 · 37.131 · 38.731 · 40.386 · 42.097 · 43.866 · 45.693 · 47.581 · 49.531 · 51.544 · 53.622 · 55.767 · 57.979 · 60.262 · 62.616 · 65.042 · 67.544 · 70.121 · 72.777 · 75.513 · 78.330 · 81.231 · 84.217 · 87.290 · 90.453 · 93.706 · 97.052 · 100.494 · 104.032 · 107.669 · 111.407 · 115.248 · 119.195 · 123.249 · 127.412 · 131.687 · 136.076 · 140.582 · 145.206 · 149.951 · 154.819 · 159.813 · 164.934 · 170.187 · 175.572 · 181.093 · 186.751 · 192.551 · 198.493 · 204.581 · 210.818 · 217.206 · 223.748 · 230.447 · 237.305 · 244.325 · 251.511 · 258.864 · 266.389 · 274.087 · 281.963 · 290.019 · 298.257 · 306.682 · 315.296 · 324.103 · 333.105 · 342.306 · 351.710 · 361.319 · 371.137 · 381.167 · 391.413 · 401.878 · 412.565 · 423.479 · 434.623 · 445.999 · 457.614 · 469.468 · 481.567 · 493.914 · 506.514 · 519.369 · 532.483 · 545.862 · 559.508 · 573.425 · 587.618 · 602.091 · 616.847 · 631.891 · 647.228 · 662.861 · 678.794 · 695.033 · 711.580 · 728.441 · 745.621 · 763.123 · 780.952 · 799.113 · 817.610 · 836.448 · 855.632 · 875.166 · 895.056 · 915.305 · 935.919 · 956.903 · 978.262 · 1000.000

