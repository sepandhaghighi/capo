# -*- coding: utf-8 -*-
"""capo chord."""

from .errors import CapoValidationError
from .note import Note
from .utils import _validate_semitones, _extract_parts, _normalize_note
from .params import NOTES_SHARP, CHORD_QUALITIES
from .params import CHORD_FORMAT_ERROR_MESSAGE


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

        self._root = root
        self._suffix = suffix
        self._bass = bass

    @classmethod
    def _from_string(cls, chord: str, validate_bass: bool = True):
        """
        Create a chord from its string representation.

        :param chord: input chord
        :param validate_bass: validate optional bass note
        """
        root, suffix, bass = _extract_parts(chord)

        instance = cls.__new__(cls)
        instance._root = Note(root).note
        instance._suffix = suffix
        instance._bass = Note(bass).note if bass and validate_bass else bass

        return instance

    def transpose(self, semitones: int, flat_mode: bool = False):
        """
        Transpose chord by semitones.

        :param semitones: semitones
        :param flat_mode: flat mode flag
        """
        _validate_semitones(semitones)

        self._root = Note(self._root).transpose(
            semitones, flat_mode).note

        if self._bass:
            self._bass = Note(self._bass).transpose(
                semitones, flat_mode).note

        return self
    
    @property
    def root(self) -> str:
        """Return the root note of Chord."""
        return self._root
    
    @property
    def suffix(self) -> str:
        """Return the chord quality suffix."""
        return self._suffix
    
    @property
    def bass(self) -> str:
        """Return the bass note of the chord, if present."""
        return self._bass

    @property
    def pitch_classes(self) -> list:
        """Return pitch classes of Chord."""
        root_pc = Note(self._root).pitch_class
        return [(root_pc + interval) % 12 for interval in CHORD_QUALITIES.get(self._suffix, [0])]

    def __str__(self):
        """Return string representation of Chord."""
        return "{root}{suffix}/{bass}".format(
            root=self._root,
            suffix=self._suffix,
            bass=self._bass) if self._bass else "{root}{suffix}".format(
            root=self._root,
            suffix=self._suffix)

    def __repr__(self):
        """Return string representation of Chord."""
        return "Chord('{root}', '{suffix}', '{bass}')".format(
            root=self._root,
            suffix=self._suffix,
            bass=self._bass)
