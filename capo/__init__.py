# -*- coding: utf-8 -*-
"""capo modules."""
from capo.params import CAPO_VERSION
from capo.errors import CapoValidationError
from capo.functions import capo_map, transpose, transpose_to_key
from capo.functions import detect_key, key_scores
__version__ = CAPO_VERSION

__all__ = ["CapoValidationError", "capo_map", "transpose", "transpose_to_key", "detect_key", "key_scores"]
