# -*- coding: utf-8 -*-
"""capo note."""

from .errors import CapoValidationError
from .params import NOTES_SHARP, NOTES_FLAT
from .params import ENHARMONIC_EQUIVALENTS
from .params import CHORD_FORMAT_ERROR_MESSAGE
from .validators import _validate_semitones


def _normalize_note(note: str) -> str:
    """
    Normalize a note to its sharp representation.

    :param note: input note
    """
    return ENHARMONIC_EQUIVALENTS.get(note, note)


def _transpose_note(note: str, semitones: int, flat_mode: bool = False) -> str:
    """
    Transpose a note by given semitones.

    :param note: input note
    :param semitones: semitones
    :param flat_mode: flat mode flag
    """
    note_sharp = _normalize_note(note)
    notes_system = NOTES_FLAT if flat_mode else NOTES_SHARP
    old_index = NOTES_SHARP.index(note_sharp)
    new_index = (old_index + semitones) % 12
    return notes_system[new_index]


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
