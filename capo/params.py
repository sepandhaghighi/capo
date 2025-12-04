# -*- coding: utf-8 -*-
"""capo params."""
CAPO_VERSION = "0.4"

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

KRUMHANSL_SCHMUCKLER_MAJOR_PROFILE = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
            2.52, 5.19, 2.39, 3.66, 2.29, 2.88]

KRUMHANSL_SCHMUCKLER_MINOR_PROFILE = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
            2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

CHORDS_TYPE_ERROR_MESSAGE = "`chords` must be a list of strings."
CAPO_POSITION_ERROR_MESSAGE = "capo position must be a non-negative integer."
SEMITONES_TYPE_ERROR_MESSAGE = "`semitones` must be an integer."
CHORD_FORMAT_ERROR_MESSAGE = "invalid chord format or unknown note: `{chord}`"
