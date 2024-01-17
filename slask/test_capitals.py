# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:35:35 2024

@author: SKRANTZ5
"""
from unittest.mock import patch, call

from src.lesson_3.capitals import practice_capitals

@patch("builtins.print")
@patch("builtins.input", return_value = "sweden")
def test_capitals_no_error(mock_input, mock_print):
    practice_capitals()
    mock_print.assert_called_with("The capital of sweden is stockholm")

@patch("src.lesson_3.capitals.get_capital", side_effect=KeyError)
@patch("builtins.print")
@patch("builtins.input", return_value = "hej")
def test_capitals_error(mock_input, mock_print, mock_error):
    practice_capitals()
    mock_print.assert_called_with("The country hej does not exist in our dictornary")