# -*- coding: utf-8 -*-
"""capo params."""
CAPO_VERSION = "0.1"

NOTES_SHARP = ["C", "C#", "D", "D#", "E", "F",
               "F#", "G", "G#", "A", "A#", "B"]

NOTES_FLAT = ["C", "Db", "D", "Eb", "E", "F",
              "Gb", "G", "Ab", "A", "Bb", "B"]

ENHARMONIC_EQUIVALENTS = {
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
    "Bb": "A#"
}

REVERSE_EQUIVALENTS = {v: k for k, v in ENHARMONIC_EQUIVALENTS.items()}
