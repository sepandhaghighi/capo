import pytest
from capo import Note, CapoValidationError


TEST_CASE_NAME = "Note tests"


def test_note_init():
    result = Note("C")
    assert result.note == "C"


def test_note_init_flat():
    result = Note("Db")
    assert result.note == "Db"


def test_note_init_enharmonic_equivalent():
    result = Note("E#")
    assert result.note == "F"
    assert result.pitch_class == 5


def test_note_init_double_accidental():
    result = Note("C##")
    assert result.note == "D"
    assert result.pitch_class == 2


def test_note_init_error():
    with pytest.raises(CapoValidationError):
        _ = Note("H")


def test_note_init_error_type():
    with pytest.raises(CapoValidationError):
        _ = Note(1)


def test_note_transpose():
    result = Note("C").transpose(2)
    assert result.note == "D"


def test_note_transpose_negative():
    result = Note("C").transpose(-1)
    assert result.note == "B"


def test_note_transpose_flat_mode():
    result = Note("C").transpose(1, flat_mode=True)
    assert result.note == "Db"


def test_note_transpose_wraps_octave():
    assert Note("B").transpose(1).note == "C"
    assert Note("C").transpose(-1).note == "B"


def test_note_transpose_returns_self():
    result = Note("C")
    assert result.transpose(1) is result


def test_note_transpose_error():
    with pytest.raises(CapoValidationError, match=r"`semitones` must be an integer."):
        _ = Note("C").transpose(1.5)


def test_note_notation():
    result = Note("Db")
    assert result.sharp_notation == "C#"
    assert result.flat_notation == "Db"


def test_note_notation_for_enharmonic_equivalent():
    result = Note("E#")
    assert result.sharp_notation == "F"
    assert result.flat_notation == "F"


def test_note_pitch_class():
    assert Note("C").pitch_class == 0
    assert Note("B").pitch_class == 11
    assert Note("Cb").pitch_class == 11


def test_note_string_and_repr():
    result = Note("Db")
    assert str(result) == "Db"
    assert repr(result) == "Note('Db')"


def test_note_equality():
    assert Note("C") == Note("B#")
    assert Note("Db") == Note("C#")
    assert Note("C") != Note("D")
    assert Note("C") != "C"
