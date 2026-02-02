<div align="center">
<img src="https://github.com/sepandhaghighi/capo/raw/main/otherfiles/logo.png" width="320">
<h1>Capo: A Python Library for Guitar Chord Transposition</h1>
<br/>
<a href="https://codecov.io/gh/sepandhaghighi/capo"><img src="https://codecov.io/gh/sepandhaghighi/capo/graph/badge.svg?token=usSRXlFCQe"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/capo"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/capo"></a>
<a href="https://badge.fury.io/py/capo"><img src="https://badge.fury.io/py/capo.svg" alt="PyPI version"></a>
</div>			
				
## Overview	

<p align="justify">		
<b>Capo</b> is a lightweight Python library for guitarists and developers that provides precise chord transposition across capo positions. It allows users to easily convert chord progressions from one capo setting to another, supporting sharps, flats, complex chord types, and slash chords. Whether you’re building a songwriting assistant, a practice tool, or a music theory application, <b>Capo</b> delivers a clear, reliable foundation for working with chord mappings and capo calculations in Python.
</p>

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/capo"><img src="http://pepy.tech/badge/capo"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/capo"><img src="https://img.shields.io/github/stars/sepandhaghighi/capo.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/capo/actions/workflows/test.yml/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/capo/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>
<table>
    <tr> 
        <td align="center">Code Quality</td>
        <td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/capo"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/capo/badge" alt="CodeFactor"></a></td>
        <td align="center"><a href="https://app.codacy.com/gh/sepandhaghighi/capo/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/1b9fef09bee3491392a76b7273177580"></a></td>
    </tr>
</table>


## Installation		

### Source Code
- Download [Version 0.6](https://github.com/sepandhaghighi/capo/archive/v0.6.zip) or [Latest Source](https://github.com/sepandhaghighi/capo/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install capo==0.6`						


## Usage

### Capo Map

Automatically converts chords between different capo positions while preserving harmonic relationships.

```pycon
>>> from capo import capo_map
>>> capo_map(["A", "Em", "C", "G"], target_capo=2, current_capo=0)
['G', 'Dm', 'A#', 'F']
>>> capo_map(["A", "Em", "C", "G"], target_capo=2, current_capo=0, flat_mode=True)
['G', 'Dm', 'Bb', 'F']
```

### Transpose

Shifts chords up or down by a specified number of semitones to change the song's key.

```pycon
>>> from capo import transpose
>>> transpose(["A", "E", "Cm", "G", "Fmaj7"], semitones=3)
['C', 'G', 'D#m', 'A#', 'G#maj7']
>>> transpose(["A", "E", "Cm", "G", "Fmaj7"], semitones=3, flat_mode=True)
['C', 'G', 'Ebm', 'Bb', 'Abmaj7']
```

### Key Scores

Returns all possible keys and their corresponding scores for a given list of chords using the Krumhansl-Schmuckler algorithm.

```pycon
>>> from capo import key_scores
>>> key_scores(["Em", "Am", "G", "Bm", "Em", "C", "G", "Bm", "Em"])
{'A#m': 0.4871417233740239, 'G#': 0.4774543026320962, 'A#': 0.5520334829280494, 'D': 0.7477367635967468, 'Am': 0.6716505683174476, 'Gm': 0.6750401588831327, 'A': 0.6622255631674839, 'Dm': 0.6367313900369936, 'G': 0.8399547248439911, 'F#m': 0.6173531647275109, 'Fm': 0.530630809877153, 'C#m': 0.5987423938857308, 'D#': 0.5377480823857491, 'C': 0.7278176839673419, 'F#': 0.5572647563660749, 'F': 0.5820127037844264, 'Em': 0.8254612345527799, 'C#': 0.4563950736636346, 'E': 0.7179587455649095, 'B': 0.7088375508524547, 'G#m': 0.6478594798186766, 'D#m': 0.564206942839128, 'Cm': 0.6280335727363678, 'Bm': 0.8030131913724882}
>>> key_scores(["G#", "G#", "Fm", "C#", "D#", "G#", "Fm", "C#", "D#"], flat_mode=True)
{'Cbm': 0.5059430034954594, 'D': 0.47214060767880817, 'Fbm': 0.5663422985823668, 'Am': 0.626082212718544, 'Gm': 0.6473142793320639, 'Gb': 0.6249570609550481, 'Dm': 0.5984541508829389, 'G': 0.5502083795108782, 'Fm': 0.8274571550716174, 'Dbm': 0.6608315888220377, 'Bbm': 0.7017791458623973, 'Abm': 0.7402210552899815, 'Ab': 0.8839844066440953, 'Bb': 0.6867751194296899, 'Ebm': 0.6941303268339243, 'Db': 0.7655343684259058, 'F': 0.6847698356536668, 'Fb': 0.573580307659009, 'Gbm': 0.5507809081451287, 'Eb': 0.8043262373344897, 'Cb': 0.5963990540758232, 'C': 0.6631957481323153, 'Cm': 0.8049063265566369, 'A': 0.4962731607074994}
```

### Detect Key

Automatically identifies the musical key from a sequence of chords using the Krumhansl-Schmuckler algorithm.

```pycon
>>> from capo import detect_key
>>> detect_key(["Em", "Am", "G", "Bm", "Em", "C", "G", "Bm", "Em"])
'G'
>>> detect_key(["G#", "G#", "Fm", "C#", "D#", "G#", "Fm", "C#", "D#"], flat_mode=True)
'Ab'
```

### Transpose to Key

Automatically transposes a list of chords from their current key to a target key.  
If the current key is not provided, it will be detected automatically.

⚠️ Chords are shifted chromatically; chord qualities are not adjusted to the target key's scale.

```pycon
>>> from capo import transpose_to_key
>>> transpose_to_key(["Am", "F", "C", "G"], target_key="C")
['Em', 'C', 'G', 'D']
>>> transpose_to_key(["Am", "F", "C", "G"], current_key="A", target_key="C")
['Cm', 'G#', 'D#', 'A#']
>>> transpose_to_key(["Am", "F", "C", "G"], current_key="A", target_key="C", flat_mode=True)
['Cm', 'Ab', 'Eb', 'Bb']
```


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template
 			

## References

<blockquote>1- <a href="https://www.guitarplayerbox.com/chord/list/capo/calculator/">Guitar chords capo calculator  - GuitarPlayerBox</a></blockquote>

<blockquote>2- <a href="https://www.musictheoryacademy.com/understanding-music/enharmonic-equivalents/">Enharmonic Equivalents - Music Theory Academy</a></blockquote>

<blockquote>3- <a href="https://bjmorrissey.github.io/capo_calculator/">Capo Calculator</a></blockquote>

<blockquote>4- <a href="https://muted.io/chord-transposer/">Chord Transposer: Online Tool to Transpose Chords</a></blockquote>

<blockquote>5- <a href="https://muted.io/enharmonic-equivalent-chart/">Enharmonic Equivalent Chart with Enharmonic Note Names</a></blockquote>

<blockquote>6- Schmuckler, M.A., 1989. Expectation in music: Investigation of melodic and harmonic processes. <i>Music Perception, 7(2)</i>, pp.109-149.</blockquote>

<blockquote>7- <a href="https://yourguitarbrain.com/chord-interval-chart-how-chords-are-made/">Chord Interval Chart: How Chords Are made (Notes and Interval Formulas)</a></blockquote>

<blockquote>8- <a href="https://www.fachords.com/guitar-chord/">Guitar Chords Explained: Diagrams, Exercises, Theory, Tips & Tricks</a></blockquote>



## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>

