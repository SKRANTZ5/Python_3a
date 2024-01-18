# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:18:28 2024

@author: SKRANTZ5
"""

from unittest.mock import patch
import pytest
from src.custom_exception import MyCustomError

from src.yaml_parser import YamlParser


@patch("src.yaml_parser.yaml.safe_load", return_value="Hej")
def test_load_file_valid(mock_open):
    parser = YamlParser()
    with patch("builtins.open"):
        parser.load_file("some_file")
        assert parser.data == "Hej"


def test_load_file_invalid():
    parser = YamlParser()
    with pytest.raises(MyCustomError):
        parser.load_file("Hej")


def test_get_signal_titel():
    parser = YamlParser()
    parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert parser.get_signal_title("11") == "ECU Reset"


def test_get_signal_titel_invalid():
    parser = YamlParser()
    parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    with pytest.raises(MyCustomError):
        parser.get_signal_title("123")
