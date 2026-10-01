---
titre: "vibelang (trusch) — synthdefs braam, synth_brass, brass_section, trumpet, trombone (DSL audio lisible, oscillateurs/filtres/enveloppes chiffrés)"
source: https://github.com/trusch/vibelang/tree/main/crates/vibelang-std/stdlib
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: synth brass ; BRAAM ; recettes de synthèse
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

## braam

Source : https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/cinematic/braam.vibe

```
// Genre: Trailer, Epic | Character: Inception-style BRAAM
define_synthdef("braam")
    .param("freq", 55.0) // units: Hz, range: 20..20000, default: 55.0. Pitch frequency in Hz; higher raises the note or resonator center.
    .param("amp", 0.9) // units: linear, range: 0..1, default: 0.9. Output level multiplier; higher is louder.
    .body(|freq, amp| {
        // Long, powerful decay
        let amp_env = envelope()
            .perc(0.05, 2.0)
            .cleanup_on_finish()
            .build();

        // Filter envelope
        let filt_env = envelope()
            .perc(0.05, 1.5)
            .build();

        // Massive detuned oscillators
        let osc1 = saw_ar(freq * 0.99) * 0.2;
        let osc2 = saw_ar(freq) * 0.25;
        let osc3 = saw_ar(freq * 1.01) * 0.2;
        let osc4 = saw_ar(freq * 2.0) * 0.15;
        let osc5 = saw_ar(freq * 0.5) * 0.2;

        let mix = osc1 + osc2 + osc3 + osc4 + osc5;

        // Powerful filter sweep
        let cutoff = 200.0 + filt_env * 3000.0;
        rlpf_ar(mix, cutoff, 0.2) * amp_env * amp
    });

//
// # Usage: `braam`
//
// ```rhai
// import "stdlib/cinematic/braam.vibe" as braam;
//
// let braam = voice("doc_braam")
//     .synth("braam")
//     .set_param("freq", 440.0)
//     .set_param("amp", 0.5);
// braam.output("out").to_main();
// braam.run();
// ```
```

## synth_brass

Source : https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/synth_brass.vibe

```
// Synth Brass
// Genre: 80s, Synthwave | Character: Punchy, bright, fat
//
// Classic synth brass stab with detuned saw waves.

define_synthdef("synth_brass", |builder| {
    builder
        .param("freq", 220.0) // units: Hz, range: 20..20000, default: 220.0. Pitch frequency in Hz; higher raises the note or resonator center.
        .param("amp", 0.5) // units: linear, range: 0..1, default: 0.5. Output level multiplier; higher is louder.
        .param("gate", 1.0) // units: trigger, range: 0..1, default: 1.0. Gate or trigger input; positive edges fire the event or advance the clock.
        .param("detune", 0.5) // units: semitones, range: -12..12, default: 0.5. Oscillator detune amount; higher spreads voices farther apart in pitch.
        .body(|freq, amp, gate, detune| {
            // Fast attack envelope
            let env = envelope()
                .asr(0.03, 1.0, 0.1)
                .gate(gate)
                .cleanup_on_finish()
                .build();

            // Multiple detuned saws for fat sound
            let detune_amt = 0.005 + detune * 0.01;
            let saw1 = saw_ar(freq * (1.0 - detune_amt));
            let saw2 = saw_ar(freq * (1.0 - detune_amt * 0.5));
            let saw3 = saw_ar(freq);
            let saw4 = saw_ar(freq * (1.0 + detune_amt * 0.5));
            let saw5 = saw_ar(freq * (1.0 + detune_amt));

            let stack = (saw1 + saw2 + saw3 + saw4 + saw5) * 0.25;

            // Filter with envelope
            let filter_env = envelope()
                .asr(0.01, 1.0, 0.1)
                .gate(gate)
                .build();
            let filter_freq = 600.0 + filter_env * 3000.0;

            let brass = rlpf_ar(stack, filter_freq, 0.4);

            brass * env * amp
        })
});

//
// # Usage: `synth_brass`
//
// ```rhai
// import "stdlib/brass/synth_brass.vibe" as synth_brass;
//
// let synth_brass = voice("doc_synth_brass")
//     .synth("synth_brass")
//     .set_param("freq", 440.0)
//     .set_param("amp", 0.5)
//     .set_param("gate", 1.0)
//     .set_param("detune", 0.5);
// synth_brass.output("out").to_main();
// synth_brass.run();
// ```
```

## brass_section

Source : https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/brass_section.vibe

```
// Brass Section
// Genre: Orchestral, Jazz | Character: Powerful, majestic, bright
//
// Full brass section ensemble with rich harmonics.

define_synthdef("brass_section", |builder| {
    builder
        .param("freq", 220.0) // units: Hz, range: 20..20000, default: 220.0. Pitch frequency in Hz; higher raises the note or resonator center.
        .param("amp", 0.5) // units: linear, range: 0..1, default: 0.5. Output level multiplier; higher is louder.
        .param("gate", 1.0) // units: trigger, range: 0..1, default: 1.0. Gate or trigger input; positive edges fire the event or advance the clock.
        .body(|freq, amp, gate| {
            // Brass swell envelope
            let env = envelope()
                .asr(0.15, 1.0, 0.1)
                .gate(gate)
                .cleanup_on_finish()
                .build();

            // Multiple brass voices (detuned for section)
            let detune = 0.004;
            let v1 = saw_ar(freq * (1.0 - detune));
            let v2 = saw_ar(freq);
            let v3 = saw_ar(freq * (1.0 + detune));

            // Octave layer
            let oct_up = saw_ar(freq * 2.0) * 0.3;

            let section = (v1 + v2 + v3) * 0.35 + oct_up;

            // Brass filter sweep (brighter with envelope)
            let filter_env = envelope()
                .asr(0.075, 1.0, 0.1)
                .gate(gate)
                .build();
            let filter_freq = 800.0 + filter_env * 2500.0;

            let brass = rlpf_ar(section, filter_freq, 0.3);

            // Slight vibrato
            let vib = sin_osc_ar(4.5) * 0.002 + 1.0;

            brass * env * amp * vib
        })
});

//
// # Usage: `brass_section`
//
// ```rhai
// import "stdlib/brass/brass_section.vibe" as brass_section;
//
// let brass_section = voice("doc_brass_section")
//     .synth("brass_section")
//     .set_param("freq", 440.0)
//     .set_param("amp", 0.5)
//     .set_param("gate", 1.0);
// brass_section.output("out").to_main();
// brass_section.run();
// ```
```

## trumpet

Source : https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/trumpet.vibe

```
// Trumpet
// Genre: Jazz, Orchestral | Character: Bright, brilliant, piercing
//
// Solo trumpet with characteristic brightness and vibrato.

define_synthdef("trumpet", |builder| {
    builder
        .param("freq", 440.0) // units: Hz, range: 20..20000, default: 440.0. Pitch frequency in Hz; higher raises the note or resonator center.
        .param("amp", 0.5) // units: linear, range: 0..1, default: 0.5. Output level multiplier; higher is louder.
        .param("gate", 1.0) // units: trigger, range: 0..1, default: 1.0. Gate or trigger input; positive edges fire the event or advance the clock.
        .param("brightness", 0.7) // units: normalized, range: 0..1, default: 0.7. Tone brightness; higher values add more high-frequency content.
        .body(|freq, amp, gate, brightness| {
            // Trumpet envelope with quick attack
            let env = envelope()
                .asr(0.05, 1.0, 0.08)
                .gate(gate)
                .cleanup_on_finish()
                .build();

            // Bright sawtooth for brass
            let saw1 = saw_ar(freq);
            let saw2 = saw_ar(freq * 1.001) * 0.5;

            let tone = (saw1 + saw2) * 0.6;

            // Trumpet formants (brightness)
            let f1 = rlpf_ar(tone, 1200.0, 0.3);
            let f2 = rlpf_ar(tone, 2500.0, 0.25) * 0.5;
            let f3 = rlpf_ar(tone, 3800.0, 0.2) * 0.3 * brightness;

            let brass = f1 + f2 + f3;

            // Attack transient (lip buzz)
            let attack_env = envelope()
                .perc(0.001, 0.03)
                .build();
            let buzz = white_noise_ar() * attack_env * 0.1;

            // Vibrato
            let vib_rate = 5.5;
            let vib = sin_osc_ar(vib_rate) * 0.008 + 1.0;
            let mod_freq = freq * vib;

            (brass + buzz) * env * amp
        })
});

//
// # Usage: `trumpet`
//
// ```rhai
// import "stdlib/brass/trumpet.vibe" as trumpet;
//
// let trumpet = voice("doc_trumpet")
//     .synth("trumpet")
//     .set_param("freq", 440.0)
//     .set_param("amp", 0.5)
//     .set_param("gate", 1.0)
//     .set_param("brightness", 0.7);
// trumpet.output("out").to_main();
// trumpet.run();
// ```
```

## trombone

Source : https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/trombone.vibe

```
// Trombone
// Genre: Jazz, Orchestral | Character: Rich, warm, mellow
//
// Trombone with characteristic warm tone and slide capability.

define_synthdef("trombone", |builder| {
    builder
        .param("freq", 220.0) // units: Hz, range: 20..20000, default: 220.0. Pitch frequency in Hz; higher raises the note or resonator center.
        .param("amp", 0.5) // units: linear, range: 0..1, default: 0.5. Output level multiplier; higher is louder.
        .param("gate", 1.0) // units: trigger, range: 0..1, default: 1.0. Gate or trigger input; positive edges fire the event or advance the clock.
        .param("slide", 0.0) // units: normalized, range: 0..1, default: 0.0. Trombone slide position; higher values lower the tube resonance.
        .body(|freq, amp, gate, slide| {
            // Smooth attack envelope
            let env = envelope()
                .asr(0.1, 1.0, 0.15)
                .gate(gate)
                .cleanup_on_finish()
                .build();

            // Slide modulation (portamento effect)
            let slide_mod = 1.0 + slide * 0.1;
            let mod_freq = freq * slide_mod;

            // Rich brass tone
            let saw1 = saw_ar(mod_freq);
            let saw2 = saw_ar(mod_freq * 0.999) * 0.6;

            let tone = (saw1 + saw2) * 0.5;

            // Trombone formants (warmer than trumpet)
            let f1 = rlpf_ar(tone, 500.0, 0.3) * 0.6;
            let f2 = rlpf_ar(tone, 1200.0, 0.3);
            let f3 = rlpf_ar(tone, 2000.0, 0.25) * 0.4;

            let brass = f1 + f2 + f3;

            // Warm low pass
            let warm = lpf_ar(brass, 3000.0);

            // Slow vibrato
            let vib = sin_osc_ar(4.0) * 0.006 + 1.0;

            warm * env * amp * vib
        })
});

//
// # Usage: `trombone`
//
// ```rhai
// import "stdlib/brass/trombone.vibe" as trombone;
//
// let trombone = voice("doc_trombone")
//     .synth("trombone")
//     .set_param("freq", 440.0)
//     .set_param("amp", 0.5)
//     .set_param("gate", 1.0)
//     .set_param("slide", 0.0);
// trombone.output("out").to_main();
// trombone.run();
// ```
```
