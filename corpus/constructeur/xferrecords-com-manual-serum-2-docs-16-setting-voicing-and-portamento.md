---
titre: "xferrecords com manual serum 2 docs — Setting Voicing and Portamento (p. 215-218)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Setting Voicing and Portamento


<!-- page 215 -->

Serum 2 User Guide
215
Setting Voicing and Portamento
Voicing is the simultaneous vertical placement of notes in relation to each other. Portamento is a pitch
sliding from one note to another.
Serum Voicing and Portamento
Voicing Settings
The VOICING section contains controls that allow you to
change how Serum behaves when multiple notes play at
once.
Serum Voicing Controls

<!-- page 216 -->

﻿
Setting Voicing and Portamento
Serum 2 User Guide
216
Mono
Use the MONO switch to enable monophonic mode, causing Serum to only allow one active note at a
time. If a new note is pressed while a note is already playing, the earlier note is interrupted (technically
the note is re-pitched to the new pitch).
Legato
LEGATO is only audible when MONO is enabled. When a monophonic voice is interrupted, the state of
the LEGATO switch determines whether the envelopes/LFOs retrigger.
When LEGATO is enabled with MONO off, Serum behaves paraphonically (especially
noticeable when ENV 2 is modulating a filter). This means you can control envelope
retriggering modes for the effects assignments here also.
When LEGATO is enabled, the envelopes do not retrigger, which results in a smooth change to the new
note. However, sometimes you want the envelopes to retrigger so each note has the same definition; in
these cases, set LEGATO to off.
Note that you can set individual envelopes to behave opposite to the LEGATO setting. See “Inverting
the Legato Setting” on page 185 for more information.
Poly
Use the POLY (polyphony) setting to specify the number of simultaneous notes that can be played.
Sometimes, often for CPU reasons, you might want to place a limit on the simultaneous notes.
For instance if you are sending a flurry of notes (arpeggio) to a patch that has a long release (say 10
seconds), this could end up producing a large number of voices, potentially overloading your CPU.
Typically, eight voices is enough and 16 is generally considered a lot. Note that this control is disabled
when MONO is enabled.
Polyphony Count
This shows the number of voices playing against the total number of voices allowed. In the example,
“0 / 1” indicates that 0 out of a total possible number of 1 voices is playing.
If a note is played, the display would change to “1 / 1”. Similarly, if you enable a second oscillator, the
display would show “0 / 2” when no notes are playing. In other words, Serum totals the number of
voices you have active in a patch.
Single note voice count in Serum includes unison voices and, if one or more oscillators are
set to GRANULAR mode, grain count as well.

<!-- page 217 -->

﻿
Setting Voicing and Portamento
Serum 2 User Guide
217
Limiting Polyphony
You can choose to limit same note polyphony. This means that if a note (for example, note number 60)
is already sounding, pressing the same note again won’t trigger another layer of the same note. This
prevents “stacking” multiple instances of the same note, ensuring clarity in the sound and avoiding
unintended overlaps or muddiness.
Right-click the POLY field and choose Limit
Same Note Poly to 1 in the context menu.
This type of polyphony control is useful for
instruments or patches that need to remain
clean, such as bass lines, monophonic synths,
or drum kits where a single sound per note is
preferred.
Voice Steal Priority
In cases when the number of voices exceeds the polyphony setting, you can specify which active note
should be terminated when a new note is triggered.
Right-click the POLY field and use the the Voice Steal Priority submenu to choose which voices get
priority (are not stolen) when Serum performs voice stealing, from among the following:
Option
Description
Newest
Terminate the earliest played note.
Oldest
Terminate the most recently played note.
Highest
Terminate the lowest-pitched note.
Lowest
Terminate the highest-pitched note.
Velocity
Note with the lowest input velocity.
Portamento Settings
Portamento creates a slow glide/pitch bend from one note
to another. It is most commonly used (and is most useful)
when MONO is also enabled.
In this case, when one note plays and then another, the
pitch slowly changes from the first note to the second.
Serum Voicing Controls
Serum Portamento Controls

<!-- page 218 -->

﻿
Setting Voicing and Portamento
Serum 2 User Guide
218
Porta
Use the PORTA knob to control the rate of glide from one note to another.
Curve
Use the portamento CURVE to adjust the contour of glide from one note to another. If set convex
(typical use), the note pitch departs the beginning pitch quickly and slows down as it nears the
destination note frequency.
If set concave (dragged down below half), the opposite is true. In this case, the pitch slowly departs the
source pitch and later rapidly arrives at the destination pitch.
Always
When ALWAYS is activated, the portamento occurs on a new note even if no note is currently playing.
When disabled, a note must be held for portamento to occur on the (second) note.
Scaled
The SCALED switch is potentially useful for melodic leads when you want a less noticeable portamento
on short intervals.
When activated, the portamento rate is adjusted based on the distance between the source and
destination pitches. For example, if the portamento is a glide between two notes one octave apart, the
PORTA knob time value is used.
If the portamento is a glide between notes less than one octave apart, the time is faster and vice-versa
(notes larger than an octave are progressively slower).