# -*- coding: utf-8 -*-
"""capo params."""
CAPO_VERSION = "0.6"

NOTES_SHARP = ["C", "C#", "D", "D#", "E", "F",
               "F#", "G", "G#", "A", "A#", "B"]

NOTES_FLAT = ["C", "Db", "D", "Eb", "Fb", "F",
              "Gb", "G", "Ab", "A", "Bb", "Cb"]

ENHARMONIC_EQUIVALENTS = {
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
    "Bb": "A#",
    "Cb": "B",
    "Fb": "E",
    "E#": "F",
    "B#": "C",
    "B##": "C#",
    "C##": "D",
    "D##": "E",
    "E##": "F#",
    "F##": "G",
    "G##": "A",
    "A##": "B",
    "Dbb": "C",
    "Ebb": "D",
    "Fbb": "D#",
    "Gbb": "F",
    "Abb": "G",
    "Bbb": "A",
    "Cbb": "A#",
}

CHORD_QUALITIES = {
    "": [0, 4, 7],
    "maj": [0, 4, 7],
    "m": [0, 3, 7],
    "dim": [0, 3, 6],
    "aug": [0, 4, 8],
    "+": [0, 4, 8],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "sus": [0, 5, 7],

    "maj7": [0, 4, 7, 11],
    "M7": [0, 4, 7, 11],
    "Δ": [0, 4, 7, 11],


    "7": [0, 4, 7, 10],

    "m7": [0, 3, 7, 10],

    "m(maj7)": [0, 3, 7, 11],
    "mM7": [0, 3, 7, 11],

    "m7b5": [0, 3, 6, 10],
    "ø": [0, 3, 6, 10],


    "dim7": [0, 3, 6, 9],
    "°7": [0, 3, 6, 9],


    "6": [0, 4, 7, 9],
    "m6": [0, 3, 7, 9],
    "6#11": [0, 4, 7, 9, 18],
    "6add9": [0, 4, 7, 9, 14],
    "m6add9": [0, 3, 7, 9, 14],

    "9": [0, 4, 7, 10, 14],
    "maj9": [0, 4, 7, 11, 14],
    "M9": [0, 4, 7, 11, 14],
    "m9": [0, 3, 7, 10, 14],
    "m(maj9)": [0, 3, 7, 11, 14],
    "9b5": [0, 4, 6, 10, 14],
    "9#11": [0, 4, 7, 10, 14, 18],


    "11": [0, 4, 7, 10, 14, 17],
    "maj11": [0, 4, 7, 11, 14, 17],
    "m11": [0, 3, 7, 10, 14, 17],


    "13": [0, 4, 7, 10, 14, 17, 21],
    "maj13": [0, 4, 7, 11, 14, 17, 21],
    "m13": [0, 3, 7, 10, 14, 17, 21],
    "13b9": [0, 4, 7, 10, 13, 17, 21],
    "13#11": [0, 4, 7, 10, 14, 18, 21],
    "13#9": [0, 4, 7, 10, 15, 17, 21],


    "7b5": [0, 4, 6, 10],
    "7#5": [0, 4, 8, 10],
    "7b9": [0, 4, 7, 10, 13],
    "7#9": [0, 4, 7, 10, 15],
    "7#11": [0, 4, 7, 10, 18],
    "7b13": [0, 4, 7, 10, 20],

    "7sus4": [0, 5, 7, 10],
    "7sus": [0, 5, 7, 10],

    "add9": [0, 4, 7, 14],

    "aug#11": [0, 4, 8, 18],
    "maj7#5": [0, 4, 8, 11],
    "9#5": [0, 4, 8, 10, 14],
    "13#5": [0, 4, 8, 10, 14, 17, 21],
}


KRUMHANSL_SCHMUCKLER_MAJOR_PROFILE = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
                                      2.52, 5.19, 2.39, 3.66, 2.29, 2.88]

KRUMHANSL_SCHMUCKLER_MINOR_PROFILE = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
                                      2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

CHORDS_TYPE_ERROR_MESSAGE = "`chords` must be a list of strings."
CAPO_POSITION_ERROR_MESSAGE = "capo position must be a non-negative integer."
SEMITONES_TYPE_ERROR_MESSAGE = "`semitones` must be an integer."
CHORD_FORMAT_ERROR_MESSAGE = "invalid chord format or unknown note: `{chord}`"
KEY_TYPE_ERROR_MESSAGE = "key must be a string."
KEY_FORMAT_ERROR_MESSAGE = "invalid key format or unknown note: `{key}`"
