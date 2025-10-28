# -*- coding: utf-8 -*-
"""capo functions."""

def normalize_root(root: str) -> str:
    """
    Normalize a root note to its sharp representation.

    :param root: root note
    """
    return ENHARMONIC_EQUIVALENTS.get(root, root)


def extract_parts(chord: str) -> tuple:
    """
    Split a chord into root, suffix, and optional bass note (for slash chords).

    :param chord: input chord
    """
    if "/" in chord:
        main, bass = chord.split("/", 1)
    else:
        main, bass = chord, None

    if len(main) > 1 and main[1] in ['#', 'b']:
        root = main[:2]
        suffix = main[2:]
    else:
        root = main[:1]
        suffix = main[1:]

    root = normalize_root(root)
    if bass:
        if len(bass) > 1 and bass[1] in ['#', 'b']:
            bass_root = normalize_root(bass[:2])
        else:
            bass_root = normalize_root(bass[:1])
    else:
        bass_root = None

    return root, suffix, bass_root


def transpose_root(root: str, semitones: int, flat_mode: bool = False) -> str:
    """
    Transpose a root note by given semitones.

    :param root: root note
    :param semitones: semitones
    :param flat_mode: flat mode flag
    """
    root_sharp = normalize_root(root)
    notes_system = NOTES_FLAT if flat_mode else NOTES_SHARP
    old_index = NOTES_SHARP.index(root_sharp)
    new_index = (old_index + semitones) % 12
    return notes_system[new_index]


def transpose_chord(chord: str, semitones: int, flat_mode: bool = False) -> str:
    """
    Transpose a full chord string by semitones.

    :param chord: input chord
    :param semitones: semitones
    :param flat_mode: flat mode flag
    """
    root, suffix, bass = extract_parts(chord)
    new_root = transpose_root(root, semitones, flat_mode)
    new_bass = transpose_root(bass, semitones, flat_mode) if bass else None

    return "{new_root}{suffix}/{new_bass}".format(new_root=new_root, suffix=suffix, new_bass=new_bass) if new_bass else "{new_root}{suffix}".format(new_root=new_root, suffix=suffix)



def capo_map(chords, current_capo: int, target_capo: int, flat_mode: bool = False):
    """
    Map a list of chords from current capo to target capo position.

    :param chords: chords list
    :param current_capo: current capo position
    :param target_capo: target capo position
    :param flat_mode: flat mode flag
    """
    if not isinstance(chords, list):
        raise TypeError("chords must be a list of strings")

    if not all(isinstance(ch, str) for ch in chords):
        raise TypeError("all chords must be strings")

    semitone_shift = target_capo - current_capo
    return [transpose_chord(ch, -semitone_shift, flat_mode) for ch in chords]