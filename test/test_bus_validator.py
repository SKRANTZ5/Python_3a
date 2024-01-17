# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:59:06 2024

@author: SKRANTZ5
"""

from unittest.mock import patch, call
from src.lesson4.bus_validator import bus_validator

@patch("src.lesson4.bus_validator.logger")
@patch("builtins.print")
@patch("builtins.input", return_value=25)
def test_bus_validator_above_24(mock_input, mock_print, mock_logger):
    bus_validator()
    assert mock_print.mock_calls == [call("Congratulations, you are old enough to drive a bus"), call("Good bye")]
 
@patch("src.lesson4.bus_validator.logger")
@patch("builtins.print")
@patch("builtins.input", return_value=23)
def test_bus_validator_below_23(mock_input, mock_print, mock_logger):
    bus_validator()
    assert mock_print.mock_calls == [call("Sorry, you have to wait 1 more years"), call("Good bye")]
   
@patch("src.lesson4.bus_validator.logger")
@patch("builtins.print")
@patch("builtins.input", return_value="hej")
def test_bus_validator_not_int(mock_input, mock_print, mock_logger):
    bus_validator()
    assert mock_print.mock_calls == [call("You need to enter a number"), call("Good bye")]