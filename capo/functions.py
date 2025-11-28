# -*- coding: utf-8 -*-
"""capo functions."""
from typing import List, Any
from .errors import CapoValidationError
from .params import NOTES_SHARP, NOTES_FLAT
from .params import ENHARMONIC_EQUIVALENTS
from .params import CHORDS_TYPE_ERROR_MESSAGE, CAPO_POSITION_ERROR_MESSAGE
from .params import CHORD_FORMAT_ERROR_MESSAGE, SEMITONES_TYPE_ERROR_MESSAGE

def _cosine_similarity(vector1: list, vector2: list) -> float:
    """
    Cosine similarity.

    :param vector1: vector 1
    :param vector2: vector 2
    """
    dot = 0.0
    norm1 = 0.0
    norm2 = 0.0
    for a, b in zip(vector1, vector2):
        dot += a * b
        norm1 += a * a
        norm2 += b * b
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / ((norm1 ** 0.5) * (norm2 ** 0.5))


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


def _validate_chords(chords: Any) -> bool:
    """
    Validate chords.

    :param chords: chords list
    """
    if not isinstance(chords, list):
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


def _validate_semitones(semitones: Any) -> bool:
    """
    Validate semitones.

    :param semitones: semitones
    """
    if not _is_int(semitones):
        raise CapoValidationError(SEMITONES_TYPE_ERROR_MESSAGE)
    return True


def _normalize_note(note: str) -> str:
    """
    Normalize a note to its sharp representation.

    :param note: input note
    """
    return ENHARMONIC_EQUIVALENTS.get(note, note)


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


def _transpose_chord(chord: str, semitones: int, flat_mode: bool = False) -> str:
    """
    Transpose a full chord string by semitones.

    :param chord: input chord
    :param semitones: semitones
    :param flat_mode: flat mode flag
    """
    root, suffix, bass = _extract_parts(chord)
    new_root = _transpose_note(root, semitones, flat_mode)
    new_bass = _transpose_note(bass, semitones, flat_mode) if bass else None

    return "{new_root}{suffix}/{new_bass}".format(
        new_root=new_root,
        suffix=suffix,
        new_bass=new_bass) if new_bass else "{new_root}{suffix}".format(
        new_root=new_root,
        suffix=suffix)


def transpose(chords: List[str], semitones: int, flat_mode: bool = False) -> List[str]:
    """
    Transpose chords by semitones.

    :param chords: chords list
    :param semitones: semitones
    :param flat_mode: flat mode flag
    """
    _validate_chords(chords)
    _validate_semitones(semitones)
    result = []
    for chord in chords:
        try:
            result.append(_transpose_chord(chord, semitones, flat_mode))
        except Exception:
            raise CapoValidationError(CHORD_FORMAT_ERROR_MESSAGE.format(chord=chord))
    return result


def capo_map(chords: List[str], target_capo: int, current_capo: int = 0, flat_mode: bool = False) -> List[str]:
    """
    Map a list of chords from current capo to target capo position.

    :param chords: chords list
    :param target_capo: target capo position
    :param current_capo: current capo position
    :param flat_mode: flat mode flag
    """
    _validate_chords(chords)
    _validate_capo_position(target_capo, current_capo)

    semitones = target_capo - current_capo
    return transpose(chords=chords, semitones=-semitones, flat_mode=flat_mode)
