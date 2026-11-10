# -*- coding: utf-8 -*-
"""capo validators."""

from typing import Any
from .errors import CapoValidationError
from .params import NOTES_SHARP
from .params import SEMITONES_TYPE_ERROR_MESSAGE, CHORDS_TYPE_ERROR_MESSAGE
from .params import CAPO_POSITION_ERROR_MESSAGE, KEY_TYPE_ERROR_MESSAGE, KEY_FORMAT_ERROR_MESSAGE


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


def _validate_capo_position(target_capo: Any, current_capo: Any) -> bool:
    """
    Validate capo position.

    :param target_capo: target capo position
    :param current_capo: current capo position
    """
    if not _is_int(current_capo) or not _is_int(target_capo):
        raise CapoValidationError(CAPO_POSITION_ERROR_MESSAGE)
    if current_capo < 0 or target_capo < 0:
        raise CapoValidationError(CAPO_POSITION_ERROR_MESSAGE)
    return True


def _validate_key(target_key: str, current_key: str) -> bool:
    """
    Validate musical keys for transposition.

    :param target_key: target key
    :param current_key: current key ("auto" means auto-detect)
    """
    if not isinstance(target_key, str):
        raise CapoValidationError(KEY_TYPE_ERROR_MESSAGE)

    if not isinstance(current_key, str):
        raise CapoValidationError(KEY_TYPE_ERROR_MESSAGE)

    root, _, _ = _extract_parts(target_key)
    if root not in NOTES_SHARP:
        raise CapoValidationError(KEY_FORMAT_ERROR_MESSAGE.format(key=target_key))

    if current_key.strip().lower() == "auto":
        return True

    root, _, _ = _extract_parts(current_key)
    if root not in NOTES_SHARP:
        raise CapoValidationError(KEY_FORMAT_ERROR_MESSAGE.format(key=current_key))
    return True
