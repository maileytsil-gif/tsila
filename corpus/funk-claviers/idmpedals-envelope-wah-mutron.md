---
titre: "IDMNYU/IDMPEDALS — pedals.md, extrait : Envelope Wah et Auto-Wah (principe du Mu-Tron III, suiveur d'enveloppe, Vactrol, paramètres)"
source: https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/master/docs/pedals.md
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: Clavinet D6, auto-wah Mu-Tron III, envelope filter
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

> Extrait : sections « EQ: Envelope Wah » et « EQ: Auto-Wah » (lignes 171–246) ; les autres pédales sont omises.

### EQ: Envelope Wah

<a href="https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/main/docs/img/Wah.png" target="_new"><img src = "./img/Wah.png" title="Wah patcher" alt="Wah patcher"></a>

<details>
	<summary>More Info...</summary>

This pedal is a [wah-wah](https://en.wikipedia.org/wiki/Wah-wah_pedal) algorithm where the position of the filter is controlled not by an expression pedal but by the amplitude of the input signal, via an [envelope follower](https://en.wikipedia.org/wiki/Envelope_detector). This technique was first used to great acclaim in the 1972 [Mu-Tron III](https://en.wikipedia.org/wiki/Mu-Tron_III) envelope filter.

The algorithm in this pedal has four parameters:
* **knob3_base** sets the fundamental (bottom) frequency of the wah effect, brought in as a value from 0.0 to 0.8; this maps to 0% to 80% of the range of the filter, later scaled to MIDI.
* **knob4_range** sets the range of the input signal's amplitude on the wah, ranging from very subtle to covering the entire range of the filter.
* **knob5_slew** sets the attack/release characteristics of the envelope follower algorithm, with a low value causing the envelope to closely track the input signal, and a high value generating a smoother - but less responsive - control value.
* **knob6_res** sets the resonance of the wah itself, with higher values creating a stronger peak at the cutoff frequency.

The envelope follower algorithm in the pedal follows the path colored blue in the patcher: it takes the input signal, rectifies it with the **abs** operator to set the values positive, and then *lowpasses* the signal using the **slide** operator. The second and third inlets of the **slide** operator control the denominator of the filter in the rising and falling direction, respectively, with higher values making smoother output values; the values for the operator are controlled by **knob5_slew**. This rectified and lowpassed value is then scaled up, clipped in the range of 0.0 to 1.0, and finally transformed into an exponential signal using a **sqrt** operator. This value is the final envelope signal.

Once the input signal's envelope is calculated, the value is multipled by **knob4_range** and offset by **knob3_base** to generate a signal that controls the cutoff frequency of the wah. It also illuminates **led2** on the Daisy Petal board. Before going into the **genlores** subpatch, this value is converted to frequency by scaling the value to a MIDI range and then to Hertz using the **mtof** operator.

<a href="https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/main/docs/img/genlores.gendsp.png" target="_new"><img src = "./img/genlores.gendsp.png" title="Lores patcher" alt="Lores patcher"></a>

The actual wah effect in this pedal consists of a 2nd order, resonant lowpass filter solved by the calculation in the **genlores** subpatch pictured above:

```
y[n] = ax[n] - by[n-1] - cy[n-2]
where...
x = the input signal
y = the output signal
n = time (n is now, n-1 is one sample ago, etc.)
Fc = cutoff frequency
R = resonance value
SR = sampling rate

Ω = Fc*2π/SR (sampling increment)
G = e^R*0.125 * 0.882497 (resonant coefficient)

c = G*G
b = -2.0*cos(Ω)*G
a = 1.0 + b + c
```

As with the Mu-Tron III that inspired this design, this pedal will respond the the dynamic range of the input instrument by opening the filter on louder notes. The different controls allow you to fine tune both the range and resonance characteristics of the wah itself as well as - just as importantly - the slew of the envelope follower. The original Mu-Tron pedals used a [Vactrol](https://en.wikipedia.org/wiki/Resistive_opto-isolator) with its characteristic response curve to couple the envelope follower to the filter; the photoresistor replaced the potentiometer that would have been attached to the rocker pedal on a conventional wah.

</details>

### EQ: Auto-Wah

<a href="https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/main/docs/img/Wah2.png" target="_new"><img src = "./img/Wah2.png" title="Wah2 patcher" alt="Wah2 patcher"></a>

<details>
	<summary>More Info...</summary>

This pedal uses the same premise as the last - a [wah-wah](https://en.wikipedia.org/wiki/Wah-wah_pedal) controlled by something other than a rocker pedal, and builds it out so that the wah frequency can be controlled by an [low frequency oscillator](https://en.wikipedia.org/wiki/Low-frequency_oscillation) (LFO). It also has a (simplified) version of the Mu-Tron-style envelope follower in the previous pedal that can be activated with a switch. The filter in this pedal is more complex as well: instead of a 2nd order lowpass filter, the filter is Peter McCulloch's [implementation](https://cycling74.com/tools/pm-ladder-moog-ladder-filter) of the [Moog Ladder Filter](https://www.uaudio.com/blog/moog-ladder-filter/).

Like the Mu-Tron-style wah, this pedal has four parameters:
* **knob3_manual** sets the center frequency of the wah effect, brought in as a value from 0.0 to 1.; the LFO then oscillates above this setting; when the LFO depth is set to 0.0 the filter will be fixed at this so-called *manual* value.
* **knob4_depthe** sets the amplitude of the LFO, which is then added in to the *manual* setting.
* **knob5_rate** sets the rate of the LFO from 1 to 10 Hertz. The input knob outputs values from 0.1 to 1. which are put through an exponential scaling function by inverting the value, taking its square root, and then inverting it again. This gives more control bandwidth to the lower (slower) values.
* **knob6_res** sets the resonance of the wah itself, with higher values creating a stronger peak at the cutoff frequency.

Finally, the pedal design uses a toggle switch (**param sw5**) to disengage the LFO via the **selector** operator and use a simplified [envelope follower](https://en.wikipedia.org/wiki/Envelope_detector) from the previous pedal (colored in green in the patcher) to create an envelope filter effect.

The LFO is a [sine wave](https://en.wikipedia.org/wiki/Sine_wave) oscillator generated by a **cycle** operator set in *phase* index mode, which allows it to be driven directly by a **phasor** operator. This **phasor** generates the core LFO based on the smoothed and scaled output of **knob5_rate**. The sine wave is mapped to the range of 0 to 1. The **selector** operator (controlled by **sw5**) switches between the LFO output and the envelope follower, which uses a **slide** operator to smooth the absolute value of the input signal.

The output of the LFO / envelope follower is then amplified with the *depth* parameter and offset with the *manual* parameter. This final signal controls the cutoff frequency of the wah. It also illuminates **led2** on the Daisy Petal board. Before going into the **ICST_MoogLP24** subpatch, this value is converted to frequency by scaling the value to a MIDI range.

<a href="https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/main/docs/img/ICST_MoogLP24.gendsp.png" target="_new"><img src = "./img/ICST_MoogLP24.gendsp.png" title="Moog ladder filter patcher" alt="Moog ladder filter patcher"></a>

The **ICST_MoogLP24** subpatch implements a digital model of the classic 4-pole resonant low-pass "Ladder Filter" developed by Robert Moog for his synthesizers. This filter has a 24dB roll-off and can resonate to the point of self-oscillation. One thing of note is that the filter module is modelled even to the point of using Moog's [1V / Octave scaling](https://en.wikipedia.org/wiki/CV/gate) to represent frequency; as a result, the incoming pitch value is converted into this range using the **center-frequency-calc** subpatcher:

<a href="https://raw.githubusercontent.com/IDMNYU/IDMPEDALS/main/docs/img/center-frequency-calc.png" target="_new"><img src = "./img/center-frequency-calc.png" title="Moog ladder filter patcher" alt="Moog ladder filter patcher"></a>

[Auto-wah](https://en.wikipedia.org/wiki/Auto-wah) effects - where the filter is controlled by the input signal's envelope or by an LFO, are common effects, and the underlying algorithms for designing the envelope followers and oscillators can be used with many other types of processing.

</details>
