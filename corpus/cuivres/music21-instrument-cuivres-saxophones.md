---
titre: "music21 instrument.py — classes Saxophone (soprano→baryton) et BrassInstrument (Horn, Trumpet, Trombone, BassTrombone, Tuba) : tessitures et transpositions"
source: https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/instrument.py
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: tessitures ; transpositions
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Extrait : seules les classes de saxophones et de cuivres. Convention music21 : C4 = MIDI 60, soit C3 dans Ableton Live (même numéro MIDI, nom d’octave décalé). `lowestNote` = note la plus grave sonnante ; `transposition` = intervalle écrit → sonnant.

```python
class Saxophone(WoodwindInstrument):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Saxophone'
        self.instrumentAbbreviation = 'Sax'
        self.instrumentSound = 'wind.reed.saxophone'
        self.midiProgram = 65

        self.lowestNote = pitch.Pitch('B-3')


class SopranoSaxophone(Saxophone):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Soprano Saxophone'
        self.instrumentAbbreviation = 'S Sax'
        self.instrumentSound = 'wind.reed.saxophone.soprano'
        self.midiProgram = 64

        self.transposition = interval.Interval('M-2')


class AltoSaxophone(Saxophone):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Alto Saxophone'
        self.instrumentAbbreviation = 'A Sax'
        self.instrumentSound = 'wind.reed.saxophone.alto'
        self.midiProgram = 65

        self.transposition = interval.Interval('M-6')


class TenorSaxophone(Saxophone):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Tenor Saxophone'
        self.instrumentAbbreviation = 'T Sax'
        self.instrumentSound = 'wind.reed.saxophone.tenor'
        self.midiProgram = 66

        self.transposition = interval.Interval('M-9')


class BaritoneSaxophone(Saxophone):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Baritone Saxophone'
        self.instrumentAbbreviation = 'Bar Sax'
        self.instrumentSound = 'wind.reed.saxophone.baritone'
        self.midiProgram = 67

        self.transposition = interval.Interval('M-13')




class BrassInstrument(Instrument):
    def __init__(self, **keywords):
        super().__init__(**keywords)
        self.instrumentName = 'Brass'
        self.instrumentAbbreviation = 'Brs'
        self.midiProgram = 61


class Horn(BrassInstrument):
    '''
    >>> hn = instrument.Horn()
    >>> hn.instrumentName
    'Horn'
    >>> hn.midiProgram
    60
    >>> 'BrassInstrument' in hn.classes
    True
    '''

    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Horn'
        self.instrumentAbbreviation = 'Hn'
        self.instrumentSound = 'brass.french-horn'
        self.midiProgram = 60

        self.lowestNote = pitch.Pitch('C2')
        self.transposition = interval.Interval('P-5')


class Trumpet(BrassInstrument):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Trumpet'
        self.instrumentAbbreviation = 'Tpt'
        self.instrumentSound = 'brass.trumpet'
        self.midiProgram = 56

        self.lowestNote = pitch.Pitch('F#3')
        self.transposition = interval.Interval('M-2')


class Trombone(BrassInstrument):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Trombone'
        self.instrumentAbbreviation = 'Trb'
        self.instrumentSound = 'brass.trombone'
        self.midiProgram = 57

        self.lowestNote = pitch.Pitch('E2')


class BassTrombone(Trombone):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Bass Trombone'
        self.instrumentAbbreviation = 'BTrb'
        self.instrumentSound = 'brass.trombone.bass'

        self.lowestNote = pitch.Pitch('B-1')


class Tuba(BrassInstrument):
    def __init__(self, **keywords):
        super().__init__(**keywords)

        self.instrumentName = 'Tuba'
        self.instrumentAbbreviation = 'Tba'
        self.instrumentSound = 'brass.tuba'
        self.midiProgram = 58

        self.lowestNote = pitch.Pitch('D1')


# ------------
```
