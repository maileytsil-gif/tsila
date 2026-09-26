---
titre: "Manuel Serum 2 — Enabling pitch tracking"
source: https://xferrecords.com/web-manual/serum-2/enabling-pitch-tracking
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

XferRecords.com | Home of the Xfer Records VST Suite

###### Serum 2 Manual

 Welcome 

 └ Registering Serum 
 └ Getting in Touch 
 └ Downloading Serum 
 └ Installing Serum 
 Exploring Serum 

 └ Exploring Sound Design in Serum 
 Getting Started 

 └ Adding Serum to a Track 
 └ Loading a Serum Preset 
 └ Creating a New Sound 
 └ Saving Changes 
 
 └ Embedding Content When Saving a Preset 

 └ Dragging Audio to Your DAW 
 └ Exploring Basic Operations 
 
 └ Displaying Help (Tooltips) 
 └ Using the Serum Keyboard 
 └ Using Knobs and Sliders 
 └ Undo and Redo 
 └ Controlling the Main Output Volume 

 └ Using Oscillators and Filters 
 
 └ Enabling an Oscillator or Filter 
 └ Choosing Oscillator or Filter Options 
 └ Using Pitch Controls 
 └ Setting the Octave or Semitone Mode 
 └ Routing an Oscillator or Filter 
 └ Accessing the Oscillator or Filter Menu 
 
 └ Locking a Module └ Initializing a Module └ Copying a Module └ Enabling Pitch Tracking └ Pitch Bend Tracking 

 └ Resizing the UI 

### Enabling Pitch Tracking

 Pitch tracking instructs the oscillator to adjust its pitch in response to the MIDI note or key being played. This ensures that the oscillator’s frequency corresponds to the desired musical pitch. Pitch tracking is typically used with melodic and harmonic sounds, where the pitch needs to follow the keyboard. 

 Pitch tracking is enabled by default.

 You can choose to disable pitch tracking by right-clicking the oscillator label and toggling Enable Pitch Tracking off in the context menu. 

 You might choose to disable pitch tracking with the following types of sounds:

 Drones or static sounds

 This produces a constant, unchanging pitch regardless of the notes played. This is common with ambient soundscapes that don’t need pitch variation. This is also useful for layering a static tonal element beneath a dynamic lead or pad.

 Percussive sounds

 These sounds often don’t rely on pitch tracking since their character is defined more by their transient and timbral qualities than specific pitch. You can use this with a variety of drum sounds, such as kick drums, snares, or hi-hats, as well as metallic or inharmonic percussive textures.

 Noise-based effects

 Noise signals (white, pink, or custom noise) aren’t inherently pitched, so pitch tracking is irrelevant. You can also use this with wind, rain, or static effects, in addition to risers, sweeps, and impacts.

 Experimental sounds

 Disabling pitch tracking can lead to unexpected and unique sonic results. This can be helpful for creating unconventional or dissonant sounds. This can more easily allow you to explore textures where the focus is on timbre and modulation rather than pitch accuracy.

 You can also disable pitch tracking to add layers without harmonic conflicts. A non-pitch-tracked oscillator can add texture or depth without interfering with the harmonic structure (such as a static sub-bass tone underneath a harmonic element).

 When pitch tracking is disabled, the Multisample, Sample, Granular, and Spectral oscillators play C3 (MIDI note 60), whereas the Wavetable oscillator plays C-2 
(MIDI note 0), allowing it to be used as an LFO.

 Last updated: May 04, 2025