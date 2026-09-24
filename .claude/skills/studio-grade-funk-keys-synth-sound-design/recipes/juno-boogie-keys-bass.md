# Juno-60 / 106 : basse « sub + octave », keys en chorus (boogie, Chromeo, Dâm-Funk)

## Cible
`BASSE ou COMPING / boogie 105–120 BPM, électro-funk moderne / basse 28–52, keys 48–72`

## Faits [DOC-EXTRAIT / HEUR-extrait / DOC]
Chromeo : le Juno-106 est « le plus polyvalent, le chorus est incroyable, on pourrait faire tout un morceau avec » ; basse Juno = **sub osc + osc une octave au-dessus, enveloppe à goût** ; Dâm-Funk : Juno-60, Alpha Juno 1, Moog Source ; Lifelike : PWM Jupiter/Juno pour basses, pads, arpèges. Données d'usine Juno-106 décodées [DOC] : « A11 Brass Set 1 » etc. dans `../../../../corpus/synthes-vintage/roland-juno-106-patches-usine-amy.md` — les patches « BASS » s'y lisent avec le même décodeur (16 octets : lfo_rate, lfo_delay, dco_lfo, dco_pwm, dco_noise, vcf_freq, vcf_res, vcf_env, vcf_lfo, vcf_kbd, vca_level, env_a, env_d, env_s, env_r, dco_sub + switches). Chorus I / II à BBD, pseudo-stéréo [HEUR-extrait] ; aucune vitesse chiffrée lue.

## Basse Juno (Analog ou Serum 2) [HEUR/TEST]
Osc 1 Rectangle PW 50 % ; **Sub on** (carré −1 octave) à fond ; Osc 2 Saw +12 st bas ; LP 24 dB 300–600 Hz, résonance 10–20 % ; Fil Env A 0 D 150–300 ms S 20–40 % ; Amp A 0–5 ms R 100–300 ms ; poly ou mono selon le jeu. Serum 2 : Sub carré + OSC A pulse, MG Low 24.

## Keys Juno en chorus [HEUR/TEST]
Analog : Osc 1 Saw, Osc 2 Rectangle PW 45 % **PWM par LFO 0,3–0,6 Hz**, Sub −6 dB ; LP 4e ordre 1–2 kHz, résonance 10 % ; Amp A 5 ms R 300 ms ; **Chorus-Ensemble Classic (I) ou Ensemble (II), Rate 0,5–0,8 Hz, Amount 50–70 %, Width max**. Serum 2 : Chorus 4 voix ; Wavetable : unison Classic 2 + Chorus-Ensemble. Le chorus est **dans le patch**, avant tout traitement.

## Chaîne
Basse : `→ Saturator Soft Sine → Compressor RMS 3:1 → Bass Mono`. Keys : `→ REQ 6 HP 150 Hz → API-2500 2:1 Thrust Med → J37 léger`.

## Tests [TEST]
Basse : mono, sub et octave dans la même phase (pas de creux) · keys : le chorus reste large sans disparaître en mono · PWM ne dérive pas la hauteur.
