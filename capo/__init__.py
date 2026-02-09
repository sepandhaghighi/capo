# -*- coding: utf-8 -*-
"""capo modules."""
from .params import CAPO_VERSION
from .errors import CapoValidationError
from .functions import capo_map, transpose, transpose_to_key
from .functions import detect_key, key_scores
from .functions import sharp_to_flat, flat_to_sharp
__version__ = CAPO_VERSION

__all__ = [
    "CapoValidationError",
    "capo_map",
    "transpose",
    "transpose_to_key",
    "detect_key",
    "key_scores",
    "sharp_to_flat",
    "flat_to_sharp"]
