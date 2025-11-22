from capo import capo_map, transpose

TEST_CASE_NAME = "Functions tests"


def test_capo_map_sharp_chords1():  # Reference: https://www.guitarplayerbox.com/chord/list/capo/calculator/
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=0)
    assert result == ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def test_capo_map_sharp_chords2():  # Reference: https://www.guitarplayerbox.com/chord/list/capo/calculator/
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=1)
    assert result == ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']


def test_capo_map_sharp_chords3():  # Reference: https://www.guitarplayerbox.com/chord/list/capo/calculator/
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=2)
    assert result == ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']


def test_capo_map_sharp_chords4():  # Reference: https://www.guitarplayerbox.com/chord/list/capo/calculator/
    result = capo_map(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], current_capo=0, target_capo=3)
    assert result == ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


def test_capo_map_sharp_chords5():  # Reference: https://www.guitarplayerbox.com/chord/list/capo/calculator/
    result = capo_map(chords=['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'E#', 'B#'], current_capo=3, target_capo=6)
    assert result == ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'D', 'A']


def test_capo_map_sharp_chords6():
    # Reference1: https://www.guitarplayerbox.com/chord/list/capo/calculator/
    # Reference2: https://www.musictheoryacademy.com/understanding-music/enharmonic-equivalents/
    result = capo_map(chords=['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'E#', 'B#'], current_capo=3, target_capo=6, flat_mode=True)
    assert result == ['Ab', 'A', 'Bb', 'Cb', 'C', 'Db', 'D', 'Eb', 'Fb', 'F', 'Gb', 'G', 'D', 'A']


def test_capo_map_flat_chords1():  # Reference: https://bjmorrissey.github.io/capo_calculator/
    result = capo_map(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "Cb", "Fb"], current_capo=0, target_capo=2)
    assert result == ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A', 'D']


def test_capo_map_flat_chords2():  # Reference: https://bjmorrissey.github.io/capo_calculator/
    result = capo_map(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "Cb", "Fb"], current_capo=0, target_capo=4)
    assert result == ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G', 'C']


def test_capo_map_flat_chords3():
    # Reference1: https://bjmorrissey.github.io/capo_calculator/
    # Reference2: https://www.musictheoryacademy.com/understanding-music/enharmonic-equivalents/
    result = capo_map(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "Cb", "Fb"], current_capo=0, target_capo=4, flat_mode=True)
    assert result == ['Ab', 'A', 'Bb', 'Cb', 'C', 'Db', 'D', 'Eb', 'Fb', 'F', 'Gb', 'G', 'G', 'C']


def test_capo_map_slash_chords1():  # Reference: https://muted.io/chord-transposer/
    result = capo_map(["C/G", "A", "C", "D"], current_capo=0, target_capo=1)
    assert result == ['B/F#', 'G#', 'B', 'C#']


def test_capo_map_slash_chords2():  # Reference: https://muted.io/chord-transposer/
    result = capo_map(["D/F#", "A/C#", "D/B", "E/C#"], current_capo=0, target_capo=3)
    assert result == ['B/D#', 'F#/A#', 'B/G#', 'C#/A#']


def test_capo_map_complex_chords1():  # Reference: https://muted.io/chord-transposer/
    result = capo_map(["Fmaj7", "Bb7", "Cmaj7", "Dm", "Cm"], current_capo=0, target_capo=4)
    assert result == ['C#maj7', 'F#7', 'G#maj7', 'A#m', 'G#m']


def test_capo_map_complex_chords2():  # Reference: https://muted.io/chord-transposer/
    result = capo_map(["Cmaj7/G", "Dm", "B7add13", "C#", "Eb"], current_capo=0, target_capo=3)
    assert result == ['Amaj7/E', 'Bm', 'G#7add13', 'A#', 'C']


def test_transpose_sharp_chords1():  # Reference: https://muted.io/chord-transposer/
    result = transpose(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "E#", "B#"], semitones=0)
    assert result == ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "F", "C"]


def test_transpose_sharp_chords2(): # Reference: https://muted.io/chord-transposer/
    result = transpose(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "E#", "B#"], semitones=-1)
    assert result == ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'E', 'B']


def test_transpose_sharp_chords3():  # Reference: https://muted.io/chord-transposer/
    result = transpose(chords=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "E#", "B#"], semitones=2)
    assert result == ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "G", "D"]


def test_transpose_flat_chords1():  # Reference: https://muted.io/chord-transposer/
    result = transpose(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "Cb", "Fb"], semitones=-2)
    assert result == ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A', 'D']


def test_transpose_flat_chords2():  # Reference: https://muted.io/chord-transposer/
    result = transpose(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "Cb", "Fb"], semitones=-4)
    assert result == ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G', 'C']


def test_transpose_flat_chords3():
    # Reference1: https://muted.io/chord-transposer/
    # Reference2: https://www.musictheoryacademy.com/understanding-music/enharmonic-equivalents/
    result = transpose(chords=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "Cb", "Fb"], semitones=-4, flat_mode=True)
    assert result == ['Ab', 'A', 'Bb', 'Cb', 'C', 'Db', 'D', 'Eb', 'Fb', 'F', 'Gb', 'G', 'G', 'C']


def test_transpose_slash_chords1():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["C/G", "A", "C", "D"], semitones=-1)
    assert result == ['B/F#', 'G#', 'B', 'C#']


def test_transpose_slash_chords2():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["D/F#", "A/C#", "D/B", "E/C#"], semitones=-3)
    assert result == ['B/D#', 'F#/A#', 'B/G#', 'C#/A#']


def test_transpose_complex_chords1():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["Fmaj7", "Bb7", "Cmaj7", "Dm", "Cm"], semitones=-4)
    assert result == ['C#maj7', 'F#7', 'G#maj7', 'A#m', 'G#m']


def test_transpose_complex_chords2():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["Cmaj7/G", "Dm", "B7add13", "C#", "Eb"], semitones=-3)
    assert result == ['Amaj7/E', 'Bm', 'G#7add13', 'A#', 'C']
