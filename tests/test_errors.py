import pytest
from capo import capo_map, transpose, CapoValidationError

TEST_CASE_NAME = "Errors tests"


def test_capo_map_chords_error1():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = capo_map(chords={"A", "Am"}, current_capo=0, target_capo=2)


def test_capo_map_chords_error2():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = capo_map(chords=["A", "Am", 1], current_capo=0, target_capo=2)


def test_transpose_chords_error1():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = transpose(chords={"A", "Am"}, semitones=1)


def test_transpose_chords_error2():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = transpose(chords=["A", "Am", 1], semitones=1)


def test_capo_map_capo_position_error1():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=-1, target_capo=2)


def test_capo_map_capo_position_error2():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=0, target_capo=-2)


def test_capo_map_capo_position_error3():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=0, target_capo=1.2)


def test_capo_map_capo_position_error4():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=1.2, target_capo=4)


def test_semitones_error():
    with pytest.raises(CapoValidationError, match=r"`semitones` must be an integer."):
        _ = transpose(chords=["A", "Am", "D"], semitones=1.3)


def test_chord_format_error1():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `s`"):
        _ = capo_map(chords=["A", "Am", "s"], current_capo=0, target_capo=2)


def test_chord_format_error2():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `s`"):
        _ = transpose(chords=["A", "Am", "s"], semitones=2)
