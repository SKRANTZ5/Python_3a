# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:51:15 2024

@author: SKRANTZ5
"""

from unittest.mock import patch, call
from src.lesson_3.joke_of_the_day import joke_of_the_day

@patch("builtins.input", return_value="fun")
@patch("builtins.print")
def test_joke_of_the_day_right(mock_print, mock_input):
    joke_of_the_day()
    assert mock_print.mock_calls == [call("joke of the day"), call("joke"), call("correct")]
    
    
@patch("builtins.input", return_value="hej")
@patch("builtins.print")
def test_joke_of_the_day_wrong(mock_print, mock_input):
    joke_of_the_day()
    assert mock_print.mock_calls == [call("joke of the day"), call("joke"), call("wrong, correct answer is: fun")]