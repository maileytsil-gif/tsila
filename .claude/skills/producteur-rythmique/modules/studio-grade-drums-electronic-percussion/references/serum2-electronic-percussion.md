# Serum 2 — Electronic Percussion

## Moteurs `[DOC]`
OSC A/B/C proposent Wavetable, Multisample, Sample, Granular et Spectral. Le choix du moteur doit suivre l'intention :
- Wavetable : hits numériques, FM/warp, bleeps, zaps, tonal percussion.
- Sample : one-shot hybride et resampling.
- Granular : glitch fragments, noisy bursts, micro-textures.
- Spectral : textures transformées / metallic-spectral inhabituelles.
- Multisample : tuned percussion multi-zones si les sources le justifient.

## Noise oscillator `[DOC]`
Le Noise oscillator est un lecteur de sample stéréo. Il peut apporter texture/réalisme ou être utilisé comme modulateur. Pour snare/hats/shaker, combiner bruit + corps tonal sans supposer que le bruit doit être large ou brillant.

## Routing `[DOC]`
Utiliser Main/Direct/Filter/None et BUS 1/2 pour séparer :
- transient direct ;
- body filtré ;
- texture traitée ;
- modulator inaudible (`None`) si utile.

## Architectures `[HEUR]`
- clap/snare : BODY tonal court + NOISE burst + optional tail.
- hat : NOISE ou partials métalliques + decay court + HP filtering.
- tom : sine/triangle + pitch drop subtil.
- FM hit : carrier + modulator ratio + envelopes indépendantes.
- zap : pitch drop/rise rapide + short body.
- glitch : Sample/Granular + window/position/motion macros.

## CPU
Pour de la percussion courte, préférer une architecture simple et resampler les systèmes très lourds une fois validés.
