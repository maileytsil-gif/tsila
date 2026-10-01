---
titre: "Abjad 3.31 instruments.py — classes Instrument, saxophones, FrenchHorn, Trumpet, trombones, Tuba (tessitures et transpositions LilyPond)"
source: https://files.pythonhosted.org/packages/76/9c/369810e498be649ebc531e9f6a78e66d28b45174f1f8f1b4af6bdf11bbf7/abjad-3.31.tar.gz
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: tessitures ; transpositions
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Fichier `source/abjad/instruments.py` de la sdist abjad-3.31 (PyPI). Notation LilyPond : c' = C4 = MIDI 60. `pitch_range` = tessiture sonnante ; `middle_c_sounding_pitch` = ce que sonne un do central écrit.

```python
class Instrument:
    """
    Instrument.
    """

    clefs: tuple[str, ...] = ()
    context: str = "Staff"
    # find_context_on_attach: typing.ClassVar[bool] = True
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("C4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[-inf, +inf]")

    check_effective_context: typing.ClassVar[bool] = True
    latent: typing.ClassVar[bool] = True
    persistent: typing.ClassVar[bool] = True
    redraw: typing.ClassVar[bool] = True
    site: typing.ClassVar[str] = "before"

    def __post_init__(self):
        assert isinstance(self.context, str), repr(self.context)
        assert isinstance(self.clefs, tuple), repr(self.clefs)
        assert all(isinstance(_, str) for _ in self.clefs)
        assert isinstance(self.pitch_range, _pcollections.PitchRange), repr(
            self.pitch_range
        )
        assert isinstance(self.middle_c_sounding_pitch, _pitch.NamedPitch), repr(
            self.middle_c_sounding_pitch
        )

    def _attachment_test_all(self, leaf):
        assert hasattr(leaf, "written_duration")
        if leaf._has_indicator(Instrument):
            string = f"Already has instrument: {leaf}."
            return string
        return True

    def _get_contributions(self):
        contributions = _contributions.ContributionsBySite()
        site = getattr(contributions, self.site)
        strings = self._get_lilypond_format()
        assert isinstance(strings, list), repr(strings)
        site.commands.extend(strings)
        return contributions

    def _get_lilypond_format(self, context=None):
        return []

    def _get_lilypond_type(self):
        if isinstance(self.context, type):
            return self.context.__name__
        elif isinstance(self.context, str):
            return self.context
        else:
            return type(self.context).__name__


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class SopraninoSaxophone(Instrument):
    """
    Sopranino saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Eb4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[Db4, F#6]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class SopranoSaxophone(Instrument):
    """
    Soprano saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Bb3")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[Ab3, E6]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class AltoSaxophone(Instrument):
    """
    Alto saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Eb3")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[Db3, A5]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class TenorSaxophone(Instrument):
    """
    Tenor saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Bb2")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[Ab2, E5]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class BaritoneSaxophone(Instrument):
    """
    Baritone saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Eb2")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[C2, Ab4]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class BassSaxophone(Instrument):
    """
    Bass saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Bb1")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[Ab2, E4]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class ContrabassSaxophone(Instrument):
    """
    Contrabass saxophone.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("Eb1")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[C1, Ab3]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class FrenchHorn(Instrument):
    """
    French horn.
    """

    clefs: tuple[str, ...] = ("bass", "treble")
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("F3")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[B1, F5]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class Trumpet(Instrument):
    """
    Trumpet.
    """

    clefs: tuple[str, ...] = ("treble",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("C4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[F#3, D6]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class AltoTrombone(Instrument):
    """
    Alto trombone.
    """

    clefs: tuple[str, ...] = ("bass", "tenor")
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("C4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[A2, Bb5]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class TenorTrombone(Instrument):
    """
    Tenor trombone.
    """

    clefs: tuple[str, ...] = ("tenor", "bass")
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("C4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[E2, Eb5]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class BassTrombone(Instrument):
    """
    Bass trombone.
    """

    clefs: tuple[str, ...] = ("bass",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("C4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[C2, F4]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)


class Tuba(Instrument):
    """
    Tuba.
    """

    clefs: tuple[str, ...] = ("bass",)
    context: str = "Staff"
    middle_c_sounding_pitch: _pitch.NamedPitch = _pitch.NamedPitch("C4")
    pitch_range: _pcollections.PitchRange = _pcollections.PitchRange("[D1, F4]")


@dataclasses.dataclass(frozen=True, order=True, slots=True, unsafe_hash=True)
```
