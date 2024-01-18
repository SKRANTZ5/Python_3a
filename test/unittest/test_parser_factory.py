# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:22:18 2024

@author: SKRANTZ5
"""


import pytest
from src.parser_factory import ParserFactory


class MockParser:
    def translate(self):
        pass


@pytest.mark.parametrize("val", [
    ("xml"),
    ("yaml"),
    ("json"),
])
def test_register_format(val):
    parser_factory = ParserFactory()
    parser_factory.register_format(val, MockParser)
    assert isinstance(parser_factory._parsers[val], MockParser)


def test_set_signal_database_format():
    parser_factory = ParserFactory()
    parser_factory.set_signal_database_format("Format")
    assert parser_factory._signal_database_format == "Format"


def test_get_parser_valid():
    parser_factory = ParserFactory()
    parser_factory.register_format("format", MockParser)
    parser_factory.set_signal_database_format("format")
    assert isinstance(parser_factory.get_parser(), MockParser)


def test_get_parser_invalid():
    parser_factory = ParserFactory()
    with pytest.raises(ValueError):
        parser_factory.get_parser()
