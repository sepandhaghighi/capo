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
