import pytest
from capo import capo_map

TEST_CASE_NAME = "Functions tests"


def test_capo_map_sharp_chords1():
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=0)
    assert result == ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def test_capo_map_sharp_chords2():
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=1)
    assert result == ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']


def test_capo_map_sharp_chords3():
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=2)
    assert result == ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']


def test_capo_map_sharp_chords4():
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=3)
    assert result == ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


def test_capo_map_sharp_chords5():
    result = capo_map(chords=['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'], current_capo=3, target_capo=6)
    assert result == ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']


def test_capo_map_flat_chords1():
    result = capo_map(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"], current_capo=0, target_capo=2)
    assert result == ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']


def test_capo_map_flat_chords2():
    result = capo_map(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"], current_capo=0, target_capo=4)
    assert result == ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']





