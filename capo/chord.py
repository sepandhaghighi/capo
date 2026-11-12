# -*- coding: utf-8 -*-
"""capo chord."""

from typing import Optional, Union, List
from .errors import CapoValidationError
from .note import Note
from .utils import _validate_semitones, _extract_parts
from .params import NOTES_SHARP, CHORD_QUALITIES
from .params import CHORD_FORMAT_ERROR_MESSAGE


class Chord:
    """Musical chord."""

    def __init__(self, root: Union[str, Note], suffix: str = "", bass: Optional[Union[str, Note]] = None):
        """
        Initialize a chord.

        :param root: chord root note
        :param suffix: chord quality
        :param bass: optional bass note
        """
        try:
            root = Note(root) if isinstance(root, str) else root
            if not isinstance(root, Note) or root.note not in NOTES_SHARP:
                raise ValueError

            if suffix not in CHORD_QUALITIES:
                raise ValueError

            if bass is not None:
                bass = Note(bass) if isinstance(bass, str) else bass
                if not isinstance(bass, Note) or bass.note not in NOTES_SHARP:
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
    def _from_string(cls, chord: str, validate_bass: bool = True) -> "Chord":
        """
        Create a chord from its string representation.

        :param chord: input chord
        :param validate_bass: validate optional bass note
        """
        root, suffix, bass = _extract_parts(chord)

        instance = cls.__new__(cls)
        instance._root = Note(root)
        instance._suffix = suffix
        instance._bass = Note(bass) if bass and validate_bass else bass

        return instance

    def transpose(self, semitones: int, flat_mode: bool = False) -> "Chord":
        """
        Transpose chord by semitones.

        :param semitones: semitones
        :param flat_mode: flat mode flag
        """
        _validate_semitones(semitones)

        self._root.transpose(semitones, flat_mode)

        if self._bass:
            self._bass.transpose(semitones, flat_mode)

        return self
    
    @property
    def root(self) -> Note:
        """Return the root note of Chord."""
        return self._root
    
    @property
    def suffix(self) -> str:
        """Return the chord quality suffix."""
        return self._suffix
    
    @property
    def bass(self) -> Optional[Note]:
        """Return the bass note of the chord, if present."""
        return self._bass

    @property
    def pitch_classes(self) -> List[int]:
        """Return pitch classes of Chord."""
        root_pc = self._root.pitch_class
        return [(root_pc + interval) % 12 for interval in CHORD_QUALITIES.get(self._suffix, [0])]

    def __str__(self) -> str:
        """Return string representation of Chord."""
        return "{root}{suffix}/{bass}".format(
            root=self._root.note,
            suffix=self._suffix,
            bass=self._bass.note) if self._bass else "{root}{suffix}".format(
            root=self._root.note,
            suffix=self._suffix)

    def __repr__(self) -> str:
        """Return string representation of Chord."""
        return "Chord('{root}', '{suffix}', '{bass}')".format(
            root=self._root.note,
            suffix=self._suffix,
            bass=self._bass.note if self._bass else None)
