---
titre: "Cycling ’74 — référence abl.dsp.meldosc~ (oscillateur Meld)"
source: https://docs.cycling74.com/reference/abl.dsp.meldosc~
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

abl.dsp.meldosc~ - Ableton DSP Reference | Cycling '74 Documentation 

 Package Ableton DSP 
# abl.dsp.meldosc~

 Meta-oscillator

## Description

 The abl.dsp.meldosc~ object wraps oscillators used in Live's Meld synthesizer.

## Arguments

### 
 
 frequency [number] 

 optional 

 Sets the oscillator frequency. Range: [0.0, 22050.0]

### 
 
 macro1 [number] 

 optional 

 Sets the value of Macro 1. Range: [0.0, 1.0]

### 
 
 macro2 [number] 

 optional 

 Sets the value of Macro 2. Range: [0.0, 1.0]

## Attributes

### 
 
 frequency [float] 

 Sets the oscillator frequency in Hz. Range: [0.0, 20500.0]

### 
 
 macro1 [float] 

 Sets Macro 1. Function depends on type . Range: [0.0, 1.0]

 Basic shapes: shape.

 Bitgrunge: frequency.

 Bubble: density.

 Chip: tone.

 Crackle: density.

 Dual basic shapes: shape.

 Extratone: pitch.

 Filtered noise: frequency.

 FM bass (squelch): FM amount.

 Fold FM: FM amount.

 Harmonic FM: FM amount.

 Noiseloop: rate.

 Noisy shapes: shape.

 Rain: tone.

 Shepard's Pi: rate.

 Simple FM: FM amount.

 Square 5th: 5th amount.

 Square sync: freq 1.

 Subosc: tone.

 Swarm oscillators: motion.

 Tarp: decay.

### 
 
 macro2 [float] 

 Sets Macro 2. Function depends on type . Range: [0.0, 1.0]

 Basic shapes: tone.

 Bitgrunge: mult.

 Bubble: spread.

 Chip: rate.

 Crackle: intensity.

 Dual basic shapes: detune.

 Extratone: env amount.

 Filtered noise: narrowness.

 FM bass (squelch): feedback.

 Fold FM: shape.

 Harmonic FM: FM ratio.

 Noiseloop: fade.

 Noisy shapes: rough.

 Rain: rate.

 Shepard's Pi: width.

 Simple FM: FM ratio.

 Square 5th: pulse width.

 Square sync: freq 2.

 Sub: aux.

 Swarm oscillators: spacing.

 Tarp: tone.

### 
 
 type [int] 

 Oscillator type
 
Possible values:

0 = 'Basic Shapes'
 (
 Basic Shapes
 )

 Morphs through classic synth waveforms,
 adds overtones or changes the pulse width.

1 = 'Bitgrunge'
 (
 Bitgrunge
 )

 A pseudo-random lo-fi square wave
 oscillator reminiscent of loading an old
 computer game from a tape.

2 = 'Bubble'
 (
 Bubble
 )

 A synthesized bubble generator.

3 = 'Chip'
 (
 Chip
 )

 A chiptune oscillator which provides pitch,
 pulse width and interval.

4 = 'Crackle'
 (
 Crackle
 )

 A synthesized crackle generator.

5 = 'Dual Basic Shapes'
 (
 Dual Basic Shapes
 )

 Morphs through classic synth waveforms,
 adds overtones or changes the pulse width.

6 = 'Extratone'
 (
 Extratone
 )

 An oscillator that retriggers a kick drum
 oscillator at fast rates to produce
 granular-esque tonal sounds.

7 = 'Filtered Noise'
 (
 Filtered Noise
 )

 A noise generator with a resonant band-pass
 filter.

8 = 'Fold Fm'
 (
 Fold FM
 )

 A harmonic FM oscillator with modulation
 amounts and wave folding.

9 = 'Harmonic Fm'
 (
 Harmonic FM
 )

 A harmonic FM oscillator with modulation
 ratio and amount.

10 = 'Noise Loop'
 (
 Noise Loop
 )

 An oscillator that loops a noise buffer at fast
 rates to produce granular-esque tonal
 sounds.

11 = 'Noisy Shapes'
 (
 Noisy Shapes
 )

 Morphs through classic synth waveforms
 and defines the amount of noise injection.

12 = 'Rain'
 (
 Rain
 )

 A rain generator with synthesized drops and
 wind.

13 = 'Shepard's Pi'
 (
 Shepard's Pi
 )

 A Shepard tone oscillator with depth and
 direction.

14 = 'Simple Fm'
 (
 Simple FM
 )

 A simple FM oscillator with modulation index
 and amount.

15 = 'Square 5th'
 (
 Square 5th
 )

 Morphs a square to a square pitched a fifth
 above with pulse width adjustment.

16 = 'Square Sync'
 (
 Square Sync
 )

 Two synced square waves where the
 frequency of each can be defined.

17 = 'Squelch'
 (
 FM Bass
 )

 A FM oscillator with modulation index
 amount and operator feedback.

18 = 'Sub'
 (
 Sub
 )

 A sub oscillator with waveform morphing and
 an additional sub (aux).

19 = 'Swarm Saw'
 (
 Swarm Saw
 )

 A swarm of saw waves with modulation and
 frequency spacing.

20 = 'Swarm Sine'
 (
 Swarm Sine
 )

 A swarm of sine waves with modulation and
 frequency spacing.

21 = 'Swarm Square'
 (
 Swarm Square
 )

 A swarm of square waves with modulation and
 frequency spacing.

22 = 'Swarm Triangle'
 (
 Swarm Triangle
 )

 A swarm of triangle waves with modulation and
 frequency spacing.

23 = 'Tarp'
 (
 Tarp
 )

 An impulse/drum oscillator with decay and
 tone controls.

### Common Box Attributes

 Below is a list of attributes shared by all objects. If you want to change one of these attributes for an object based on the object box, you need to place the word sendbox in front of the attribute name, or use the object's Inspector .

### 
 
 annotation [symbol] 

 Sets the text that will be displayed in the Clue window when the user moves the mouse over the object.

### 
 
 background [int] : 0 

 Adds or removes the object from the patcher's background layer. background 1 adds the object to the background layer, background 0 removes it. Objects in the background layer are shown behind all objects in the default foreground layer.

### 
 
 color [4 floats] 

 Sets the color for the object box outline.

### 
 
 fontface [int] 

 Sets the type style used by the object. The options are:

 plain

 bold

 italic

 bold italic
 
Possible values:

0 = 'regular'
 
1 = 'bold'
 
2 = 'italic'
 
3 = 'bold italic'

### 
 
 fontname [symbol] 

 Sets the object's font.

### 
 
 fontsize [float] 

 Sets the object's font size (in points).
 
Possible values:

 '8'

 '9'

 '10'

 '11'

 '12'

 '13'

 '14'

 '16'

 '18'

 '20'

 '24'

 '30'

 '36'

 '48'

 '64'

 '72'

### 
 
 hidden [int] : 0 

 Toggles whether an object is hidden when the patcher is locked.

### 
 
 hint [symbol] 

 Sets the text that will be displayed in as a pop-up hint when the user moves the mouse over the object in a locked patcher.

### 
 
 ignoreclick [int] : 0 

 Toggles whether an object ignores mouse clicks in a locked patcher.

### 
 
 jspainterfile [symbol] 

 You can override the default appearance of a user interface object by assigning a JavaScript file with code for painting the object. The file must be in the search path.

### 
 
 patching_rect [4 floats] : 0. 0. 100. 0. 

 Aliases:
 patching_position, patching_size

 Sets the position and size of the object in the patcher window.

### 
 
 position [2 floats] 

 write-only 

 Sets the object's x and y position in both patching and presentation modes (if the object belongs to its patcher's presentation), leaving its size unchanged.

### 
 
 presentation [int] : 0 

 Sets whether an object belongs to the patcher's presentation.

### 
 
 presentation_rect [4 floats] : 0. 0. 0. 0. 

 Aliases:
 presentation_position, presentation_size

 Sets the x and y position and width and height of the object in the patcher's presentation, leaving its patching position unchanged.

### 
 
 rect [4 floats] 

 write-only 

 Sets the x and y position and width and height of the object in both patching and presentation modes (if the object belongs to its patcher's presentation).

### 
 
 size [2 floats] 

 write-only 

 Sets the object's width and height in both patching and presentation modes (if the object belongs to its patcher's presentation), leaving its position unchanged.

### 
 
 textcolor [4 floats] 

 Sets the color for the object's text in RGBA format.

### 
 
 textjustification [int] 

 Sets the justification for the object's text.
 
Possible values:

0 = 'left'
 
1 = 'center'
 
2 = 'right'

### 
 
 valuepopup [int] : 0 

 For objects with single values, enabling valuepopup will display the object's current value in a popup caption when the mouse is over the object or it is being changed with the mouse.

### 
 
 valuepopuplabel [int] : 0 

 Sets the source of a text label shown in a value popup caption.
 
Possible values:

0 = 'None'
 
1 = 'Hint'
 
2 = 'Scripting Name'
 
3 = 'Parameter Long Name'
 
4 = 'Parameter Short Name'

### 
 
 varname [symbol] 

 Sets the patcher's scripting name, which can be used to address the object by name in pattr , scripting messages to thispatcher , and the js object.

## Messages

### 
 float 

 First inlet: sets frequency.

 Second inlet: sets macro 1.

 Third inlet: sets macro 2.

### 
 reset 

 Resets the oscillator.

### 
 signal 

 First inlet: sets frequency.

 Second inlet: sets macro 1.

 Third inlet: sets macro 2.

## See Also

 Name 
 Description 

 abl.dsp.basicshapes~ 
 
 Basic shape oscillator 

 abl.dsp.bitgrunge~ 
 
 Bit-grunge oscillator 

 abl.dsp.bubble~ 
 
 Bubble generator 

 abl.dsp.chip~ 
 
 Square wave chiptune oscillator 

 abl.dsp.crackle~ 
 
 Crackle sound generator 

 abl.dsp.dualbasicshapes~ 
 
 Dual basic shape oscillator 

 abl.dsp.filterednoise~ 
 
 Filtered noise generator 

 abl.dsp.fmbass~ 
 
 Three operator FM oscillator 

 abl.dsp.foldfm~ 
 
 Wavefolding FM oscillator 

 abl.dsp.harmonicfm~ 
 
 Harmonic FM oscillator 

 abl.dsp.noiseloop~ 
 
 Noise buffer looper 

 abl.dsp.noisyshapes~ 
 
 Noisy dual basic shape oscillator 

 abl.dsp.rain~ 
 
 Rain sound generator 

 abl.dsp.shepard~ 
 
 Shepard tone oscillator 

 abl.dsp.simplefm~ 
 
 Two-operator FM oscillator 

 abl.dsp.squarefifth~ 
 
 Morphing square wave oscillator 

 abl.dsp.squaresync~ 
 
 Dual square wave oscillator 

 abl.dsp.subosc~ 
 
 Oscillator with sub bass 

 abl.dsp.swarm~ 
 
 Multi-oscillator swarm 

 abl.dsp.tarp~ 
 
 Kick/bass oscillator