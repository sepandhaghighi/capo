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
- Download [Version 0.2](https://github.com/sepandhaghighi/capo/archive/v0.2.zip) or [Latest Source](https://github.com/sepandhaghighi/capo/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install capo==0.2`						


## Usage

### Capo Map

```pycon
>>> from capo import capo_map
>>> capo_map(["A", "Em", "C", "G"], target_capo=2, current_capo=0)
['G', 'Dm', 'A#', 'F']
>>> capo_map(["A", "Em", "C", "G"], target_capo=2, current_capo=0, flat_mode=True)
['G', 'Dm', 'Bb', 'F']
```

### Transpose

```pycon
>>> from capo import transpose
>>> transpose(["A", "E", "Cm", "G", "Fmaj7"], semitones=3)
['C', 'G', 'D#m', 'A#', 'G#maj7']
>>> transpose(["A", "E", "Cm", "G", "Fmaj7"], semitones=3, flat_mode=True)
['C', 'G', 'Ebm', 'Bb', 'Abmaj7']
```

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template
 			

## References

<blockquote>1- <a href="https://www.guitarplayerbox.com/chord/list/capo/calculator/">Guitar chords capo calculator  - GuitarPlayerBox</a></blockquote>

<blockquote>2- <a href="https://www.musictheoryacademy.com/understanding-music/enharmonic-equivalents/">Enharmonic Equivalents - Music Theory Academy</a></blockquote>

<blockquote>3- <a href="https://bjmorrissey.github.io/capo_calculator/">Capo Calculator</a></blockquote>

<blockquote>4- <a href="https://muted.io/chord-transposer/">Chord Transposer: Online Tool to Transpose Chords</a></blockquote>


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

