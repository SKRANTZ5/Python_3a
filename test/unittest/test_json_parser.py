# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:40:10 2024

@author: SKRANTZ5
"""

from unittest.mock import patch
import pytest
from src.custom_exception import MyCustomError

from src.json_parser import JsonParser


@patch("src.json_parser.js.load", return_value="Hej")
def test_load_file_valid(mock_json_open):
    json_parser = JsonParser()
    with patch("builtins.open"):
        json_parser.load_file("some_file")
        assert json_parser.data == "Hej"


def test_load_file_invalid():
    json_parser = JsonParser()
    with pytest.raises(MyCustomError):
        json_parser.load_file("Hej")


def test_get_signal_titel():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_signal_title("11") == "ECU Reset"


def test_get_signal_titel_invalid():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    with pytest.raises(MyCustomError):
        json_parser.get_signal_title("123")
