# -*- coding: utf-8 -*-
"""capo params."""
CAPO_VERSION = "0.2"

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
}

CHORDS_TYPE_ERROR_MESSAGE = "`chords` must be a list of strings."
CAPO_POSITION_ERROR_MESSAGE = "capo position must be a non-negative integer."
SEMITONES_TYPE_ERROR_MESSAGE = "`semitones` must be an integer."
CHORD_FORMAT_ERROR_MESSAGE = "invalid chord format or unknown note: `{chord}`"
