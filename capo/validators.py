# -*- coding: utf-8 -*-
"""capo validators."""

from typing import Any
from .errors import CapoValidationError
from .params import SEMITONES_TYPE_ERROR_MESSAGE, CHORDS_TYPE_ERROR_MESSAGE


def _is_int(number: Any) -> bool:
    """
    Check that input number is integer or not.

    :param number: input number
    """
    try:
        if int(number) == number:
            return True
        return False
    except Exception:
        return False


def _validate_semitones(semitones: Any) -> bool:
    """
    Validate semitones.

    :param semitones: semitones
    """
    if not _is_int(semitones):
        raise CapoValidationError(SEMITONES_TYPE_ERROR_MESSAGE)
    return True


def _validate_chords(chords: Any) -> bool:
    """
    Validate chords.

    :param chords: chords list
    """
    if not isinstance(chords, list) or len(chords) == 0:
        raise CapoValidationError(CHORDS_TYPE_ERROR_MESSAGE)
    if not all(isinstance(chord, str) for chord in chords):
        raise CapoValidationError(CHORDS_TYPE_ERROR_MESSAGE)
    return True
