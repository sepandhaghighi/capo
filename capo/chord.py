
# -*- coding: utf-8 -*-
"""capo chord."""

from .errors import CapoValidationError
from .note import Note, _normalize_note
from .validation import _validate_semitones
from .params import NOTES_SHARP, CHORD_QUALITIES
from .params import CHORD_FORMAT_ERROR_MESSAGE


def _extract_parts(chord: str) -> tuple:
    """
    Split a chord into root, suffix, and optional bass note (for slash chords).

    :param chord: input chord
    """
    if "/" in chord:
        main, bass = chord.split("/", 1)
    else:
        main, bass = chord, None

    if len(main) > 2 and main[1:3] in ['##', 'bb']:
        root = main[:3]
        suffix = main[3:]
    elif len(main) > 1 and main[1] in ['#', 'b']:
        root = main[:2]
        suffix = main[2:]
    else:
        root = main[:1]
        suffix = main[1:]

    root = _normalize_note(root)
    if bass:
        if len(bass) > 2 and bass[1:3] in ['##', 'bb']:
            bass_root = _normalize_note(bass[:3])
        elif len(bass) > 1 and bass[1] in ['#', 'b']:
            bass_root = _normalize_note(bass[:2])
        else:
            bass_root = _normalize_note(bass[:1])
    else:
        bass_root = None

    return root, suffix, bass_root


class Chord:
    """Musical chord."""

    def __init__(self, root: str, suffix: str = "", bass: str = None):
        """
        Initialize a chord.

        :param root: chord root note
        :param suffix: chord quality
        :param bass: optional bass note
        """
        try:
            root = _normalize_note(root)
            if root not in NOTES_SHARP:
                raise ValueError

            if suffix not in CHORD_QUALITIES:
                raise ValueError

            if bass is not None:
                bass = _normalize_note(bass)
                if bass not in NOTES_SHARP:
                    raise ValueError

        except Exception:
            raise CapoValidationError(
                CHORD_FORMAT_ERROR_MESSAGE.format(
                    chord="{root}{suffix}/{bass}".format(
                        root=root,
                        suffix=suffix,
                        bass=bass) if bass else "{root}{suffix}".format(
                            root=root,
                            suffix=suffix)))

        self.root = root
        self.suffix = suffix
        self.bass = bass

    @classmethod
    def _from_string(cls, chord: str, validate_bass: bool = True):
        """
        Create a chord from its string representation.

        :param chord: input chord
        :param validate_bass: validate optional bass note
        """
        root, suffix, bass = _extract_parts(chord)

        instance = cls.__new__(cls)
        instance.root = Note(root).note
        instance.suffix = suffix
        instance.bass = Note(bass).note if bass and validate_bass else bass

        return instance

    def transpose(self, semitones: int, flat_mode: bool = False):
        """
        Transpose chord by semitones.

        :param semitones: semitones
        :param flat_mode: flat mode flag
        """
        _validate_semitones(semitones)

        self.root = Note(self.root).transpose(
            semitones, flat_mode).note

        if self.bass:
            self.bass = Note(self.bass).transpose(
                semitones, flat_mode).note

        return self

    def __str__(self):
        """Return string representation of Chord."""
        return "{root}{suffix}/{bass}".format(
            root=self.root,
            suffix=self.suffix,
            bass=self.bass) if self.bass else "{root}{suffix}".format(
            root=self.root,
            suffix=self.suffix)

    def __repr__(self):
        """Return string representation of Chord."""
        return "Chord('{root}', '{suffix}', '{bass}')".format(
            root=self.root,
            suffix=self.suffix,
            bass=self.bass)
