# -*- coding: utf-8 -*-
"""capo note."""

from .errors import CapoValidationError
from .params import NOTES_SHARP, NOTES_FLAT
from .params import ENHARMONIC_EQUIVALENTS
from .params import CHORD_FORMAT_ERROR_MESSAGE
from .utils import _validate_semitones, _transpose_note



class Note:
    """Musical note."""

    def __init__(self, note: str) -> None:
        """
        Initialize a note.

        :param note: input note
        """
        try:
            self._note = _transpose_note(note, semitones=0)
        except Exception:
            raise CapoValidationError(
                CHORD_FORMAT_ERROR_MESSAGE.format(chord=note))

    def transpose(self, semitones: int, flat_mode: bool = False) -> "Note":
        """
        Transpose note by semitones.

        :param semitones: semitones
        :param flat_mode: flat mode flag
        """
        _validate_semitones(semitones)
        self._note = _transpose_note(
            self._note, semitones, flat_mode)
        return self
    
    @property
    def note(self) -> str:
        """Return the normalized note representation."""
        return self._note

    @property
    def pitch_class(self) -> int:
        """Return pitch class of Note."""
        return NOTES_SHARP.index(self._note)

    def __str__(self) -> str:
        """Return string representation of Note."""
        return self._note

    def __repr__(self) -> str:
        """Return string representation of Note."""
        return "Note('{note}')".format(note=self._note)
