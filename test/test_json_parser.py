# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:40:10 2024

@author: SKRANTZ5
"""

from unittest.mock import patch, mock_open

from src.json_parser import JsonParser

#@patch.object(JsonParser, "load_file")
@patch("builtins.open", mock_open(read_data="Hello"))
def test_load_file():
    json_parser = JsonParser()
    assert json_parser.load_file("my_file_path") == "Hello"
    
def test_get_signal_titel():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_signal_title("11") == "ECU Reset"