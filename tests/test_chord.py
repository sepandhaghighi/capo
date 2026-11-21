import pytest
from capo import Chord, Note
from capo import CapoValidationError


TEST_CASE_NAME = "Chord tests"


def test_chord_init():
    result = Chord("C", "maj7", "G")
    assert result.root == Note("C")
    assert result.suffix == "maj7"
    assert result.bass == Note("G")


def test_chord_init_with_note_objects():
    root = Note("D")
    bass = Note("A")
    result = Chord(root, "m", bass)
    assert result.root is root
    assert result.bass is bass


def test_chord_init_without_bass():
    result = Chord("C")
    assert result.root == Note("C")
    assert result.suffix == ""
    assert result.bass is None


def test_chord_init_error_root():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `invalid`"):
        _ = Chord("invalid")


def test_chord_init_error_suffix():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `Cinvalid`"):
        _ = Chord("C", "invalid")


def test_chord_init_without_suffix_validation():
    result = Chord("C", "unknown", validate_suffix=False)
    assert result.suffix == "unknown"
    assert result.pitch_classes == [0]


def test_chord_init_error_bass():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `C/invalid`"):
        _ = Chord("C", "", "invalid")


def test_chord_init_error_root_type():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `1`"):
        _ = Chord(1)


def test_chord_init_error_bass_type():
    with pytest.raises(CapoValidationError, match=r"invalid chord format or unknown note: `C/1`"):
        _ = Chord("C", "", 1)


def test_chord_from_string():
    result = Chord.from_string("Cmaj7/G")
    assert result.root == Note("C")
    assert result.suffix == "maj7"
    assert result.bass == Note("G")
    assert str(result) == "Cmaj7/G"


def test_chord_from_string_without_bass():
    result = Chord.from_string("Am")
    assert result.root == Note("A")
    assert result.suffix == "m"
    assert result.bass is None


def test_chord_from_string_without_suffix_validation():
    result = Chord.from_string("Cunknown", validate_suffix=False)
    assert result.suffix == "unknown"
    assert result.pitch_classes == [0]


def test_chord_from_string_bass_is_note():
    result = Chord.from_string("C/Gb")
    assert isinstance(result.bass, Note)
    assert result.bass == Note("F#")


def test_chord_transpose():
    result = Chord.from_string("Cmaj7/G").transpose(2)
    assert result.sharp_notation == "Dmaj7/A"
    assert result.flat_notation == "Dmaj7/A"


def test_chord_transpose_flat_mode():
    result = Chord.from_string("C/G").transpose(1, flat_mode=True)
    assert result.flat_notation == "Db/Ab"


def test_chord_transpose_without_bass():
    result = Chord("A", "m").transpose(-1)
    assert result.sharp_notation == "G#m"
    assert result.bass is None


def test_chord_transpose_returns_self():
    result = Chord("C")
    assert result.transpose(1) is result


def test_chord_transpose_error():
    with pytest.raises(CapoValidationError, match=r"`semitones` must be an integer."):
        _ = Chord("C").transpose(1.5)


def test_chord_properties_and_pitch_classes():
    result = Chord("C", "maj7")
    assert result.root == Note("C")
    assert result.suffix == "maj7"
    assert result.bass is None
    assert result.pitch_classes == [0, 4, 7, 11]


def test_chord_pitch_classes_minor():
    assert Chord("A", "m").pitch_classes == [9, 0, 4]


def test_chord_pitch_classes_unknown_suffix_from_string():
    assert Chord.from_string("Cunknown").pitch_classes == [0]


def test_chord_string_and_repr():
    result = Chord("C", "m", "G")
    assert str(result) == "Cm/G"
    assert repr(result) == "Chord('C', 'm', 'G')"


def test_chord_string_without_bass():
    result = Chord("C", "maj")
    assert str(result) == "Cmaj"
    assert repr(result) == "Chord('C', 'maj', 'None')"


def test_chord_sharp_and_flat_notation():
    result = Chord("C#", "m", "G#")
    assert result.sharp_notation == "C#m/G#"
    assert result.flat_notation == "Dbm/Ab"


def test_chord_equality():
    assert Chord("C") == Chord("B#")
    assert Chord("C", "m") != Chord("C")
    assert Chord("C", "m", "G") != Chord("C", "m", "A")
    assert Chord("C") != "C"
