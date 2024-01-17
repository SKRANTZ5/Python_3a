# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:38:27 2024

@author: SKRANTZ5
"""
from unittest.mock import patch
from src.lesson4.convert_to_comma import convert_to_comma_seperated_string, convert_to_space_seperated_string



def test_convert_to_comma_seperated_string(numbers):
    assert convert_to_comma_seperated_string(numbers) == "one,two,three"


def test_convert_to_space_seperated_string(numbers):
    assert convert_to_space_seperated_string(numbers) == "one two three"