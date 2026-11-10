# -*- coding: utf-8 -*-
"""capo note."""

from .errors import CapoValidationError
from .params import NOTES_SHARP, NOTES_FLAT
from .params import ENHARMONIC_EQUIVALENTS
from .params import CHORD_FORMAT_ERROR_MESSAGE
from .utils import _validate_semitones, _transpose_note



class Note:
    """Musical note."""

    def __init__(self, note: str):
        """
        Initialize a note.

        :param note: input note
        """
        try:
            self.note = _transpose_note(note, semitones=0)
        except Exception:
            raise CapoValidationError(
                CHORD_FORMAT_ERROR_MESSAGE.format(chord=note))

    def transpose(self, semitones: int, flat_mode: bool = False):
        """
        Transpose note by semitones.

        :param semitones: semitones
        :param flat_mode: flat mode flag
        """
        _validate_semitones(semitones)
        self.note = _transpose_note(
            self.note, semitones, flat_mode)
        return self

    def __str__(self):
        """Return string representation of Note."""
        return self.note

    def __repr__(self):
        """Return string representation of Note."""
        return "Note('{note}')".format(note=self.note)
