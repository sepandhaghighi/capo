# -*- coding: utf-8 -*-
"""capo functions."""

from typing import List, Dict, Any
from .errors import CapoValidationError
from .note import Note
from .chord import Chord
from .utils import _validate_semitones, _validate_chords, _validate_capo_position, _validate_key, _extract_parts, _cosine_similarity, _rotate_list
from .params import NOTES_SHARP
from .params import CHORD_QUALITIES
from .params import CHORDS_TYPE_ERROR_MESSAGE, CAPO_POSITION_ERROR_MESSAGE
from .params import CHORD_FORMAT_ERROR_MESSAGE
from .params import KEY_TYPE_ERROR_MESSAGE, KEY_FORMAT_ERROR_MESSAGE
from .params import KRUMHANSL_SCHMUCKLER_MAJOR_PROFILE
from .params import KRUMHANSL_SCHMUCKLER_MINOR_PROFILE



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
            result.append(str(Chord._from_string(chord).transpose(semitones, flat_mode)))
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
            chord_obj = Chord._from_string(chord, validate_bass=False)
            root_pc = NOTES_SHARP.index(Note(chord_obj.root).note)
            for interval in CHORD_QUALITIES.get(chord_obj.suffix, [0]):
                pc_vector[(root_pc + interval) % 12] += 1
        except Exception:
            raise CapoValidationError(CHORD_FORMAT_ERROR_MESSAGE.format(chord=chord))
    scores = dict()
    for i, note in enumerate(NOTES_SHARP):
        profile_major = _rotate_list(KRUMHANSL_SCHMUCKLER_MAJOR_PROFILE, i)
        profile_minor = _rotate_list(KRUMHANSL_SCHMUCKLER_MINOR_PROFILE, i)
        key_major = str(Note(note).transpose(0, flat_mode))
        key_minor = str(Chord._from_string("{note}m".format(note=note)).transpose(0, flat_mode))
        scores[key_major] = _cosine_similarity(pc_vector, profile_major)
        scores[key_minor] = _cosine_similarity(pc_vector, profile_minor)

    return scores


def detect_key(chords: List[str], flat_mode: bool = False) -> str:
    """
    Infer the most likely musical key from a list of chords.

    :param chords: chords list
    :param flat_mode: flat mode flag
    """
    scores = key_scores(chords=chords, flat_mode=flat_mode)
    best_key = max(scores, key=scores.get)
    return best_key



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

    target_pc = NOTES_SHARP.index(Note(target_root).note)

    current_pc = NOTES_SHARP.index(Note(current_root).note)

    semitones = target_pc - current_pc

    return transpose(
        chords=chords,
        semitones=semitones,
        flat_mode=flat_mode)


def sharp_to_flat(chords: List[str]) -> List[str]:
    """
    Convert chords from sharp notation to flat notation.

    :param chords: chords list
    """
    return transpose(chords, semitones=0, flat_mode=True)


def flat_to_sharp(chords: List[str]) -> List[str]:
    """
    Convert chords from flat notation to sharp notation.

    :param chords: chords list
    """
    return transpose(chords, semitones=0, flat_mode=False)
