import pytest
from capo import capo_map, CapoValidationError

TEST_CASE_NAME = "Errors tests"


def test_chords_error1():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = capo_map(chords={"A", "Am"}, current_capo=0, target_capo=2)


def test_chords_error2():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = capo_map(chords=["A", "Am", 1], current_capo=0, target_capo=2)


def test_capo_position_error1():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=-1, target_capo=2)


def test_capo_position_error2():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=0, target_capo=-2)


def test_capo_position_error3():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=0, target_capo=1.2)


def test_capo_position_error4():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo=1.2, target_capo=4)


def test_chord_format_error():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `s`"):
        _ = capo_map(chords=["A", "Am", "s"], current_capo=0, target_capo=2)
