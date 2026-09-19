# Serum 2 — Transition Design

Sources :
- https://xferrecords.com/web-manual/serum-2/exploring-sound-design-in-serum
- https://xferrecords.com/web-manual/serum-2/enabling-pitch-tracking
- https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter
- https://xferrecords.com/web-manual/serum-2/exploring-serum

## Capacités [DOC]
OSC A/B/C peuvent employer Wavetable, Multisample, Sample, Granular ou Spectral. Serum 2 propose des LFO/enveloppes assignables à de nombreux contrôles. Xfer cite explicitement les **risers, sweeps et impacts** parmi les effets où désactiver le pitch tracking peut être pertinent. Les oscillateurs/filtres se routent vers Filter, Main, Direct ou None et vers les bus.

## Architectures [HEUR]

### Noise riser
- Noise/static source, pitch tracking off ;
- LP/HP ou band-pass en mouvement ;
- LFO/envelope 4 ou 8 bars ;
- macro `TONE` = cutoff, `MOTION` = rate/amount, `SPACE` = FX wet.

### Tonal riser
- Wavetable sine/saw ou Sample ;
- pitch envelope/LFO montant ;
- harmoniser avec la tonalité ou assumer un sweep continu ;
- couper la queue avant le downbeat si le pitch final devient conflictuel.

### Granular uplifter
- source texture/vocal/non-tonale ;
- mouvement de scan + grain density/position ;
- filtre high-pass progressif ;
- resample recommandé si le résultat doit être précisément édité.

### Impact
- transient/noise séparé du body ;
- layer tonal si musicalement utile ;
- layer Direct possible pour conserver une attaque propre pendant que d'autres couches passent par FX `[DOC+HEUR]`.
