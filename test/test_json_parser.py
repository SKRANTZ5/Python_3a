# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:40:10 2024

@author: SKRANTZ5
"""

from unittest.mock import patch, mock_open
import pytest

from src.json_parser import JsonParser

#@patch.object(JsonParser, "load_file")
#@patch("builtins.open", mock_open(read_data="Hello"))
@patch("src.json_parser.js.load", return_value="Hello")
def test_load_file(mock_json_open):
    json_parser = JsonParser()
    assert json_parser.load_file("C:\signal_database.json") == "Hello"
 
@pytest.mark.parametrize("identifier, expected", [
    ("123", None),
    ("11", "ECU Reset"),
])
def test_get_signal_titel(identifier, expected):
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_signal_title(identifier) == expected