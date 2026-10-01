---
titre: "LilyPond Music Glossary — accent, breath mark, doit, fall, glissando, legato, staccato, tenuto (définitions multilingues) — extrait"
source: https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/music-glossary.tely
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: notation ; articulations
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

```texinfo
@node accent
@section accent

ES: acento,
I: accento,
F: accent,
D: Akzent,
NL: accent,
DK: accent,
S: accent,
FI: aksentti, korostus.

The stress of one tone over others.

@morerefs
No cross-references.
@endmorerefs

@node breath mark
@section breath mark

ES: respiración,
I: respiro,
F: respiration,
D: Atemzeichen, Trennungszeichen,
NL: repercussieteken,
DK: vejrtrækningstegn,
S: andningstecken,
FI: hengitysmerkki.

Indication of where to breathe in vocal and wind instrument parts.

@morerefs
@ref{caesura}.
@endmorerefs

@node doit
@section doit

ES: elevación [de tono],
I: portamento indeterminato verso l'alto/l'acuto,
F: saut,
D: Glissando aufwärts zu unbestimmter Tonhöhe,
NL: ?,
DK: glissando stigende til udefineret tonehøjde,
S: ?,
FI: nousu.

Indicator for an indeterminately rising pitch bend.  Compare with
@emph{glissando}, which has determinate starting and ending pitches.

@morerefs
@ref{fall},
@ref{glissando}.
@endmorerefs

@node fall
@section fall

ES: caída [de tono],
I: portamento indeterminato verso il basso/il grave,
F: chute,
D: Glissando abwärts zu unbestimmter Tonhöhe,
NL: ?,
DK: glissando faldende til udefineret tonehøjde,
S: ?,
FI: lasku.

Indicator for an indeterminately falling pitch bend.  Compare with
@emph{glissando}, which has determinate starting and ending pitches.

@morerefs
@ref{doit},
@ref{glissando}.
@endmorerefs

@node glissando
@section glissando

ES: glissando,
I: glissando,
F: glissando,
D: Glissando,
NL: glissando,
DK: glissando,
S: glissando,
FI: glissando, liukuen.

Letting the pitch slide fluently from one note to the other.

@morerefs
No cross-references.
@endmorerefs

@node legato
@section legato

ES: legato,
I: legato,
F: legato, lié,
D: legato, gebunden,
NL: legato,
DK: legato,
S: legato,
FI: legato, sitoen.

To be performed (a) without any perceptible interruption between the
notes, unlike (b) @notation{leggiero} or @notation{non-legato}, (c)
@notation{portato}, or (d) @notation{staccato}.

@lilypond[quote,notime,line-width=13.0\cm]
<<
  \context Staff \relative c'' {
    c4-( d e-) \bar "||"
    c4-- d-- e-- \bar "||"
    c4-.-( d-. e-.-) \bar "||"
    c4-. d-. e-. \bar "||"
  }
  \lyrics {
    a2.
    b
    c
    d
  }
>>
@end lilypond

@morerefs
@ref{staccato}.
@endmorerefs

@node staccato
@section staccato

ES: picado,
I: staccato,
F: staccato, piqué, détaché,
D: staccato,
NL: staccato,
DK: staccato,
S: staccato,
FI: staccato, lyhyesti, terävästi.

Playing the note(s) short.  Staccato is indicated by a dot above or
below the note head.

@lilypond[quote,relative=2]
\key d \major
\time 4/4
  \partial 8 a8 |
  d4-\staccato cis-\staccato b-\staccato cis-\staccato |
  d2.
  \bar "||"
@end lilypond

@morerefs
No cross-references.
@endmorerefs

@node tenuto
@section tenuto

ES: subrayado (tenuto),
I: tenuto,
F: tenue, tenuto,
D: gehalten, tenuto,
NL: tenuto,
DK: tenuto,
S: tenuto,
FI: viiva, tenuto.

An indication that a particular note should be held for the whole
length, although this can vary depending on the composer and era.

@morerefs
No cross-references.
@endmorerefs
```
