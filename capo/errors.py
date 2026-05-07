# -*- coding: utf-8 -*-
"""Capo errors."""

class CapoError(Exception):
    """Base exception for all Capo errors."""

    pass

class CapoValidationError(CapoError, ValueError):
    """Base class for validation errors in Capo."""

    pass
