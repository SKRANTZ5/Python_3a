# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:07:22 2024

@author: SKRANTZ5
"""

from unittest.mock import patch
import pytest
from src.custom_exception import MyCustomError

from src.xml_parser import XmlParser


@patch("src.xml_parser.ET.parse")
@patch("src.xml_parser.ET.tostring")
@patch("src.xml_parser.xmltodict.parse", return_value={"hej": "tja"})
def test_load_file_valid(mock_open, mock_tostring, mock_parse):
    parser = XmlParser()
    with patch("builtins.open"):
        parser.load_file("some_file")
        assert parser.data == {"hej": "tja"}


def test_load_file_invalid():
    parser = XmlParser()
    with pytest.raises(MyCustomError):
        parser.load_file("Hej")


def test_get_signal_titel():
    parser = XmlParser()
    parser.data = {'services': {'service': [
        {'@id': '11', 'title': 'ECU Reset'}, {'@id': '27', 'title': 'Security Access'}]}}
    assert parser.get_signal_title("11") == "ECU Reset"


def test_get_signal_titel_invalid():
    parser = XmlParser()
    parser.data = {'services': {'service': [
        {'@id': '11', 'title': 'ECU Reset'}, {'@id': '27', 'title': 'Security Access'}]}}
    with pytest.raises(MyCustomError):
        parser.get_signal_title("123")
