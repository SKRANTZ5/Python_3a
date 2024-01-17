# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:55:34 2024

@author: SKRANTZ5
"""

from unittest.mock import patch, call
from src.lesson_3.is_hex import is_hex
import pytest


@pytest.mark.parametrize("value, expected", [
    ("123", True),
    ("78AA", True),
    ("kys", False),
    ("din mamma", False),
])
def test_is_hex(value, expected):
    assert is_hex(value) == expected