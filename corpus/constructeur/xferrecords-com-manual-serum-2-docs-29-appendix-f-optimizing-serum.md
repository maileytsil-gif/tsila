---
titre: "xferrecords com manual serum 2 docs — Appendix F: Optimizing Serum (p. 348-348)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Appendix F: Optimizing Serum


<!-- page 348 -->

Serum 2 User Guide
348
Appendix F: Optimizing Serum
This appendix describes a series of easy-to-adopt approaches to optimizing your sound design results in
Serum.
Exploring CPU Optimization
Serum is designed to optimize audio processing and CPU performance. However, there certain
approaches that you can incorporate to help your sounds achieve the very best performance and
maintain the highest-quality in sound design.
Managing Unison
Unison is a powerful tool for enhancing the depth and richness of a sound by layering multiple voices
slightly detuned or panned, creating a fuller, more powerful tonal presence. However, overuse of unison
can potentially lead to quality and performance issues.
Consider doing the following:
•	 Keep unison counts low
Using more than three to seven unisons per oscillator is often unnecessary and can potentially
negatively impact efficiency. This is because higher unison counts not only significantly increase
CPU usage, but can also introduce phasing issues, potentially degrading your sound quality.
•	 Use chorus instead of unison
Instead of stacking unisons to create a thick, chorused sound, use a dedicated FX bus with a
chorus effect. This approach offers two principal advantages. First, by apply the effect once instead
of processing it for every voice, this approach is considerably more CPU friendly.
Second, this provides greater flexibility by allowing easier tweaking and layering of effects without
duplicating processing effort.