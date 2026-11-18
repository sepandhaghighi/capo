# -*- coding: utf-8 -*-
"""capo note."""

from .errors import CapoValidationError
from .params import NOTES_SHARP, NOTES_FLAT
from .params import ENHARMONIC_EQUIVALENTS
from .params import CHORD_FORMAT_ERROR_MESSAGE
from .utils import _validate_semitones, _transpose_note, _normalize_note



class Note:
    """Musical note."""

    def __init__(self, note: str) -> None:
        """
        Initialize a note.

        :param note: input note
        """
        try:
            if note not in NOTES_SHARP and note not in NOTES_FLAT:
                note = _normalize_note(note)
                if note not in NOTES_SHARP:
                    raise ValueError
            self._note = note
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
        """Return the original note representation."""
        return self._note
    
    @property
    def sharp_notation(self) -> str:
        """Return the sharp notation of Note."""
        return NOTES_SHARP[self.pitch_class]

    @property
    def flat_notation(self) -> str:
        """Return the flat notation of Note."""
        return NOTES_FLAT[self.pitch_class]

    @property
    def pitch_class(self) -> int:
        """Return pitch class of Note."""
        return NOTES_SHARP.index(_normalize_note(self._note))

    def __str__(self) -> str:
        """Return string representation of Note."""
        return self._note

    def __repr__(self) -> str:
        """Return string representation of Note."""
        return "Note('{note}')".format(note=self._note)
    
    def __eq__(self, other: object) -> bool:
        """Check equality of Note."""
        if not isinstance(other, Note):
            return False
        return self.pitch_class == other.pitch_class
