# -*- coding: utf-8 -*-
"""capo functions."""
from typing import List, Dict, Any
from .errors import CapoValidationError
from .params import NOTES_SHARP, NOTES_FLAT
from .params import ENHARMONIC_EQUIVALENTS, CHORD_QUALITIES
from .params import CHORDS_TYPE_ERROR_MESSAGE, CAPO_POSITION_ERROR_MESSAGE
from .params import CHORD_FORMAT_ERROR_MESSAGE, SEMITONES_TYPE_ERROR_MESSAGE
from .params import KEY_TYPE_ERROR_MESSAGE, KEY_FORMAT_ERROR_MESSAGE
from .params import KRUMHANSL_SCHMUCKLER_MAJOR_PROFILE, KRUMHANSL_SCHMUCKLER_MINOR_PROFILE


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
    return dot / ((norm1 ** 0.5) * (norm2 ** 0.5))


def _rotate_list(input_list: list, n: int) -> list:
    """
    Rotate a list to the right by *n* positions.

    :param input_list: input list
    :param n: number of positions to rotate
    """
    return input_list[-n:] + input_list[:-n]


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

    semitones = current_capo - target_capo
    return transpose(chords=chords, semitones=semitones, flat_mode=flat_mode)


def key_scores(chords: List[str], flat_mode: bool = False) -> Dict[str, float]:
    """
    Return scores for all possible keys based on a list of chords.

    :param chords: chords list
    :param flat_mode: flat mode flag
    """
    _validate_chords(chords)
    pc_vector = [0] * 12

    for chord in chords:
        try:
            root, suffix, _bass = _extract_parts(chord)
            root_pc = NOTES_SHARP.index(root)
            for interval in CHORD_QUALITIES.get(suffix, [0]):
                pc_vector[(root_pc + interval) % 12] += 1
        except Exception:
            raise CapoValidationError(
                CHORD_FORMAT_ERROR_MESSAGE.format(chord=chord)
            )

    scores = dict()
    for i, note in enumerate(NOTES_SHARP):
        profile_major = _rotate_list(KRUMHANSL_SCHMUCKLER_MAJOR_PROFILE, i)
        profile_minor = _rotate_list(KRUMHANSL_SCHMUCKLER_MINOR_PROFILE, i)

        key_major = _transpose_chord(note, 0, flat_mode)
        key_minor = _transpose_chord("{note}m".format(note=note), 0, flat_mode)

        scores[key_major] = _cosine_similarity(pc_vector, profile_major)
        scores[key_minor] = _cosine_similarity(pc_vector, profile_minor)

    return scores


def detect_key(chords: List[str], flat_mode: bool = False) -> str:
    """
    Infer the most likely musical key from a list of chords.

    :param chords: chords list
    :param flat_mode: flat mode flag
    """
    scores = key_scores(chords)
    best_key = max(scores, key=scores.get)
    return _transpose_chord(best_key, semitones=0, flat_mode=flat_mode)


def transpose_to_key(
        chords: List[str],
        target_key: str,
        current_key: str = "auto",
        flat_mode: bool = False) -> List[str]:
    """
    Transpose a list of chords from one musical key to another.

    :param chords: chords list
    :param target_key: target key
    :param current_key: current key, "auto" means detect automatically
    :param flat_mode: flat mode flag
    """
    _validate_chords(chords)
    _validate_key(target_key, current_key)

    if current_key.strip().lower() == "auto":
        current_key = detect_key(chords)

    target_root, _, _ = _extract_parts(target_key)
    current_root, _, _ = _extract_parts(current_key)

    target_pc = NOTES_SHARP.index(target_root)
    current_pc = NOTES_SHARP.index(current_root)

    semitones = target_pc - current_pc

    return transpose(chords=chords, semitones=semitones, flat_mode=flat_mode)
