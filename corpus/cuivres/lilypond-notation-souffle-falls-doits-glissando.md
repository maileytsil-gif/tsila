---
titre: "LilyPond Notation Reference (expressive.itely) — Breath marks (\breathe), Falls and doits (\bendAfter), Glissando — extrait"
source: https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/notation/expressive.itely
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: notation ; articulations de cuivres
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Sections « Breath marks », « Falls and doits » et « Glissando » du chapitre Expressive marks (source Texinfo).

```texinfo
@node Breath marks
@subsection Breath marks

@cindex breath mark
@cindex pause mark
@funindex \breathe

The @code{\breathe} command calls for the performer to shorten the
previous note to take a breath.

@lilypond[verbatim,quote]
\fixed c'' { c2. \breathe d4 }
@end lilypond

@noindent
For a short break in sound that is not taken away from the
previous note, @pxref{Caesuras}.

Unlike other expressive marks, a breath mark is treated as a
separate music event; therefore, any expressive marks pertaining
to the preceding note, and any brackets indicating manual beams,
slurs, or phrasing slurs, must be placed before @code{\breathe}.
@code{\breathe} does not accept articulations itself, but
@pxref{Caesuras}.

A breath mark ends an automatic beam; to override this,
@pxref{Manual beams}.

@lilypond[verbatim,quote]
\fixed c'' { c8 \breathe d e f g2 }
@end lilypond

@cindex breath mark symbol, changing
@cindex changing breath mark symbol
@cindex check mark
@cindex symbol, breath mark, changing
@cindex tick mark

The @code{breathMarkType} context property controls which of
several predefined breath marks the @code{\breathe} command
creates.  @xref{List of breath marks}.

@lilypond[verbatim,quote]
\fixed c'' {
  \set breathMarkType = #'tickmark
  c2. \breathe d4
}
@end lilypond


@morerefs
Music Glossary:
@rglos{breath mark}.

Notation Reference:
@ref{Caesuras},
@ref{Divisiones}.

Snippets:
@rlsr{Expressive marks}.

Internals Reference:
@rinternals{BreathingEvent},
@rinternals{BreathingSign},
@rinternals{Breathing_sign_engraver}.
@endmorerefs

@node Falls and doits
@subsection Falls and doits

@cindex fall
@cindex doit
@funindex \bendAfter

@notation{Falls} and @notation{doits} can be added to notes using
the @code{\bendAfter} command.  The direction of the fall or doit
is indicated with a plus or minus (up or down).  The number
indicates the pitch interval that the fall or doit will extend
@emph{beyond} the main note.

@lilypond[verbatim,quote]
\relative c'' {
  c2\bendAfter 4
  c2\bendAfter -4
  c2\bendAfter 6.5
  c2\bendAfter -6.5
  c2\bendAfter 8
  c2\bendAfter -8
}
@end lilypond


@snippets

@lilypondfile[verbatim,quote,texidoc,doctitle]
{snippets/adjusting-the-shape-of-falls-and-doits.ly}

@morerefs
Music Glossary:
@rglos{fall},
@rglos{doit}.

Snippets:
@rlsr{Expressive marks}.
@endmorerefs

@node Glissando
@subsection Glissando

@cindex glissando
@funindex \glissando

A @notation{glissando} is created by appending @code{\glissando}
to a note:

@lilypond[verbatim,quote]
\relative {
  g'2\glissando g'
  c2\glissando c,
  \afterGrace f,1\glissando f'16
}
@end lilypond

A glissando can connect notes across staves:

@lilypond[verbatim,quote]
\new PianoStaff <<
  \new Staff = "right" {
    e'''2\glissando
    \change Staff = "left"
    a,,4\glissando
    \change Staff = "right"
    b''8 r |
  }
  \new Staff = "left" {
    \clef bass
    s1
  }
>>
@end lilypond

@funindex \glissandoMap

A glissando can connect notes in chords.  If anything other than a
direct one-to-one pairing of the notes in the two chords is required,
the connections between the notes are defined by setting
@code{\glissandoMap} to a Scheme list.  The elements are pairs of
integers; each pair @var{(x . y)} creates a glissando line from the
@var{x}-th note of the first chord to the @var{y}-th note of the second
chord.  Notes are numbered from zero in the order in which they appear
in the input @file{.ly} file.  Not all notes need be part in a
glissando.

@lilypond[verbatim,quote]
\relative {
  <c' e>2\glissando g'
  <c, e>\glissando <g' b>
  \break
  \set glissandoMap = #'((0 . 1) (1 . 0))
  <c, g'>\glissando <d a'>
  \set glissandoMap = #'((0 . 0) (0 . 1) (0 . 2))
  c\glissando <d f a>
  \set glissandoMap = #'((2 . 2) (0 . 0))
  <f d a'>\glissando <c f c'>
}
@end lilypond

Different styles of glissandi can be created.  For details, see
@ref{Line styles}.


@snippets

@cindex contemporary glissando
@cindex glissando, contemporary
@lilypondfile[verbatim,quote,texidoc,doctitle]
{snippets/contemporary-glissando.ly}

@cindex timing mark, for glissando
@cindex glissando, timing marks
@lilypondfile[verbatim,quote,texidoc,doctitle]
{snippets/adding-timing-marks-to-long-glissandi.ly}

@anchor{Making glissandi breakable}
@cindex breakable glissando
@cindex glissando, breakable
@lilypondfile[verbatim,quote,texidoc,doctitle]
{snippets/making-glissandi-breakable.ly}

@anchor{Extending glissandi across repeats}
@cindex glissando, across repeats
@cindex repeat, and glissandi
@lilypondfile[verbatim,quote,texidoc,doctitle]
{snippets/extending-glissandi-across-repeats.ly}

@morerefs
Music Glossary:
@rglos{glissando}.

Notation Reference:
@ref{Line styles}.

Snippets:
@rlsr{Expressive marks}.

Internals Reference:
@rinternals{Glissando}.
@endmorerefs

@knownissues
Printing text over the line (such as @notation{gliss.})@: is not
supported.
```
