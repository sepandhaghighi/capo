import pytest
from capo import capo_map, transpose, transpose_to_key
from capo import detect_key, CapoValidationError

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


def test_detect_key_chords_error1():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = detect_key(chords={"A", "Am"})


def test_detect_key_chords_error2():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = detect_key(chords=["A", "Am", 1])


def test_transpose_to_key_chords_error1():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = transpose_to_key(chords={"A", "Am"}, target_key="B")


def test_transpose_to_key_chords_error2():
    with pytest.raises(CapoValidationError, match=r"`chords` must be a list of strings."):
        _ = transpose_to_key(chords=["A", "Am", 1], target_key="B")


def test_transpose_to_key_key_error1():
    with pytest.raises(CapoValidationError, match=r"key must be a string."):
        _ = transpose_to_key(chords=["A", "Am"], target_key=1, current_key="A")


def test_transpose_to_key_key_error2():
    with pytest.raises(CapoValidationError, match=r"key must be a string."):
        _ = transpose_to_key(chords=["A", "Am"], target_key="B", current_key=1)


def test_transpose_to_key_key_error3():
    with pytest.raises(CapoValidationError, match=r"invalid key format or unknown note: `s`"):
        _ = transpose_to_key(chords=["A", "Am"], target_key="s", current_key="B")


def test_transpose_to_key_key_error4():
    with pytest.raises(CapoValidationError, match=r"invalid key format or unknown note: `s`"):
        _ = transpose_to_key(chords=["A", "Am"], target_key="B", current_key="s")
        

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


def test_capo_map_capo_position_error5():
    with pytest.raises(CapoValidationError, match=r"capo position must be a non-negative integer."):
        _ = capo_map(chords=["A", "Am", "D"], current_capo="a", target_capo=4)


def test_transpose_semitones_error1():
    with pytest.raises(CapoValidationError, match=r"`semitones` must be an integer."):
        _ = transpose(chords=["A", "Am", "D"], semitones=1.3)


def test_transpose_semitones_error2():
    with pytest.raises(CapoValidationError, match=r"`semitones` must be an integer."):
        _ = transpose(chords=["A", "Am", "D"], semitones="b")


def test_capo_map_chord_format_error():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `s`"):
        _ = capo_map(chords=["A", "Am", "s"], current_capo=0, target_capo=2)


def test_transpose_chord_format_error():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `s`"):
        _ = transpose(chords=["A", "Am", "s"], semitones=2)


def test_detect_key_chord_format_error():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `s`"):
        _ = detect_key(chords=["A", "Am", "s"])
