from capo import capo_map, transpose
from capo import detect_key, transpose_to_key, key_scores
from capo import sharp_to_flat

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


def test_capo_map_double_sharp_chords1():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = capo_map(chords=["C##", "D##", "E##", "F##", "G##", "A##", "B##"], current_capo=0, target_capo=0)
    assert result == ["D", "E", "F#", "G", "A", "B", "C#"]


def test_capo_map_double_sharp_chords2():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = capo_map(chords=["C##", "D##", "E##", "F##", "G##", "A##", "B##"], current_capo=0, target_capo=1)
    assert result == ["C#", "D#", "F", "F#", "G#", "A#", "C"]


def test_capo_map_double_sharp_chords3():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = capo_map(chords=["C##", "D##", "E##", "F##", "G##", "A##", "B##"], current_capo=0, target_capo=2)
    assert result == ["C", "D", "E", "F", "G", "A", "B"]


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


def test_capo_map_double_flat_chords1():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = capo_map(chords=["Cbb", "Dbb", "Ebb", "Fbb", "Gbb", "Abb", "Bbb"], current_capo=2, target_capo=0)
    assert result == ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def test_capo_map_double_flat_chords2():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = capo_map(chords=["Cbb", "Dbb", "Ebb", "Fbb", "Gbb", "Abb", "Bbb"], current_capo=1, target_capo=0, flat_mode=True)
    assert result == ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']


def test_capo_map_slash_chords1():  # Reference: https://muted.io/chord-transposer/
    result = capo_map(["C/G", "A", "C", "D", "D/B##", "D/Bbb"], current_capo=0, target_capo=1)
    assert result == ['B/F#', 'G#', 'B', 'C#', 'C#/C', 'C#/G#']


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


def test_transpose_double_sharp_chords1():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = transpose(chords=["C##", "D##", "E##", "F##", "G##", "A##", "B##"], semitones=0)
    assert result == ["D", "E", "F#", "G", "A", "B", "C#"]


def test_transpose_double_sharp_chords2():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = transpose(chords=["C##", "D##", "E##", "F##", "G##", "A##", "B##"], semitones=-1)
    assert result == ["C#", "D#", "F", "F#", "G#", "A#", "C"]


def test_transpose_double_sharp_chords3():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = transpose(chords=["C##", "D##", "E##", "F##", "G##", "A##", "B##"], semitones=-2)
    assert result == ["C", "D", "E", "F", "G", "A", "B"]


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


def test_transpose_double_flat_chords1():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = transpose(chords=["Cbb", "Dbb", "Ebb", "Fbb", "Gbb", "Abb", "Bbb"], semitones=2)
    assert result == ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def test_transpose_double_flat_chords2():  # Reference: https://muted.io/enharmonic-equivalent-chart/
    result = transpose(chords=["Cbb", "Dbb", "Ebb", "Fbb", "Gbb", "Abb", "Bbb"], semitones=1, flat_mode=True)
    assert result == ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']


def test_transpose_slash_chords1():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["C/G", "A", "C", "D", "D/A##", "D/Abb"], semitones=-1)
    assert result == ['B/F#', 'G#', 'B', 'C#', "C#/A#", "C#/F#"]


def test_transpose_slash_chords2():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["D/F#", "A/C#", "D/B", "E/C#"], semitones=-3)
    assert result == ['B/D#', 'F#/A#', 'B/G#', 'C#/A#']


def test_transpose_complex_chords1():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["Fmaj7", "Bb7", "Cmaj7", "Dm", "Cm"], semitones=-4)
    assert result == ['C#maj7', 'F#7', 'G#maj7', 'A#m', 'G#m']


def test_transpose_complex_chords2():  # Reference: https://muted.io/chord-transposer/
    result = transpose(["Cmaj7/G", "Dm", "B7add13", "C#", "Eb"], semitones=-3)
    assert result == ['Amaj7/E', 'Bm', 'G#7add13', 'A#', 'C']


def test_detect_key1(): # Reference: https://tabs.ultimate-guitar.com/tab/radiohead/lucky-chords-41315
    result = detect_key(["Em", "Am", "G", "Bm", "C", "A", "C7", "B7", "Em/F", "Emadd9", "G5/D", "Em/F#"])
    assert result == "Em"


def test_detect_key2(): # Reference: https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589
    result = detect_key(["G#", "G#", "Fm", "C#", "D#", "G#", "Fm", "C#", "D#"], flat_mode=True)
    assert result == "Ab"


def test_detect_key3(): # Reference: https://tabs.ultimate-guitar.com/tab/radiohead/lucky-chords-41315
    flat_chords = transpose(["Em", "Am", "G", "Bm", "C", "A", "C7", "B7", "Em/F", "Emadd9", "G5/D", "Em/F#"], semitones=0, flat_mode=True)
    result = detect_key(flat_chords)
    assert result == "Em"


def test_detect_key4(): # Reference: https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589
    flat_chords = transpose(["G#", "G#", "Fm", "C#", "D#", "G#", "Fm", "C#", "D#"], semitones=0, flat_mode=True)
    result = detect_key(flat_chords, flat_mode=True)
    assert result == "Ab"


def test_detect_key5(): # Reference: https://tabs.ultimate-guitar.com/tab/radiohead/creep-chords-4169
    result = detect_key(["G", "B", "C", "Cm"])
    assert result == "G"


def test_detect_key6(): # Reference: https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/californication-chords-202765
    result = detect_key(["Am", "F", "C", "G", "Dm", "Fmaj7", "F#m", "D", "Bm", "A", "E"])
    assert result == "Am"


def test_key_scores1(): # Reference: https://tabs.ultimate-guitar.com/tab/radiohead/lucky-chords-41315
    result = key_scores(["Em", "Am", "G", "Bm", "C", "A", "C7", "B7", "Em/F", "Emadd9", "G5/D", "Em/F#"])
    assert isinstance(result, dict)
    assert all(map(lambda x: isinstance(x, float), result.values()))
    assert sorted(result, key = lambda x : result[x], reverse=True)[0] == "Em"


def test_key_scores2(): # Reference: https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589
    result = key_scores(["G#", "G#", "Fm", "C#", "D#", "G#", "Fm", "C#", "D#"], flat_mode=True)
    assert isinstance(result, dict)
    assert all(map(lambda x: isinstance(x, float), result.values()))
    assert sorted(result, key = lambda x : result[x], reverse=True)[0] == "Ab"


def test_key_scores3(): # Reference: https://tabs.ultimate-guitar.com/tab/radiohead/lucky-chords-41315
    flat_chords = transpose(["Em", "Am", "G", "Bm", "C", "A", "C7", "B7", "Em/F", "Emadd9", "G5/D", "Em/F#"], semitones=0, flat_mode=True)
    result = key_scores(flat_chords)
    assert isinstance(result, dict)
    assert all(map(lambda x: isinstance(x, float), result.values()))
    assert sorted(result, key = lambda x : result[x], reverse=True)[0] == "Em"


def test_key_scores4(): # Reference: https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589
    flat_chords = transpose(["G#", "G#", "Fm", "C#", "D#", "G#", "Fm", "C#", "D#"], semitones=0, flat_mode=True)
    result = key_scores(flat_chords, flat_mode=True)
    assert isinstance(result, dict)
    assert all(map(lambda x: isinstance(x, float), result.values()))
    assert sorted(result, key = lambda x : result[x], reverse=True)[0] == "Ab"


def test_key_scores5(): # Reference: https://tabs.ultimate-guitar.com/tab/radiohead/creep-chords-4169
    result = key_scores(["G", "B", "C", "Cm"])
    assert isinstance(result, dict)
    assert all(map(lambda x: isinstance(x, float), result.values()))
    assert sorted(result, key = lambda x : result[x], reverse=True)[0] == "G"


def test_key_scores6(): # Reference: https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/californication-chords-202765
    result = key_scores(["Am", "F", "C", "G", "Dm", "Fmaj7", "F#m", "D", "Bm", "A", "E"])
    assert isinstance(result, dict)
    assert all(map(lambda x: isinstance(x, float), result.values()))
    assert sorted(result, key = lambda x : result[x], reverse=True)[0] == "Am"


def test_transpose_to_key1(): # Reference: https://muted.io/chord-transposer/
    result = transpose_to_key(["Am", "F", "C", "G"], current_key="A", target_key="C")
    assert result == ["Cm", "G#", "D#", "A#"]


def test_transpose_to_key2(): # Reference: https://muted.io/chord-transposer/
    result = transpose_to_key(["Am", "F", "C", "G"], target_key="C")
    assert result == ['Am', 'F', 'C', 'G']


def test_transpose_to_key3(): # Reference: https://muted.io/chord-transposer/
    result = transpose_to_key(["Am", "F", "C", "G"], current_key="Db", target_key="Gb")
    assert result == ["Dm", "A#", "F", "C"]


def test_transpose_to_key4(): # Reference: https://muted.io/chord-transposer/
    result = transpose_to_key(["Am", "F", "C", "G"], current_key="Db", target_key="Gb", flat_mode=True)
    assert result == ["Dm", "Bb", "F", "C"]


def test_sharp_to_flat1():
    result = sharp_to_flat(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
    assert result == ["C", "Db", "D", "Eb", "Fb", "F", "Gb", "G", "Ab", "A", "Bb", "Cb"]


def test_sharp_to_flat2():
    result = sharp_to_flat(["C", "Db", "D", "Eb", "Fb", "F", "Gb", "G", "Ab", "A", "Bb", "Cb"])
    assert result == ["C", "Db", "D", "Eb", "Fb", "F", "Gb", "G", "Ab", "A", "Bb", "Cb"]
