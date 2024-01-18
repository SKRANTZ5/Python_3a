# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:14:39 2024

@author: SKRANTZ5
"""


from unittest.mock import patch
import pytest
from src.lesson5.car_translator import SwedishTranslator, ItalianTranslator, GermanTranslator, TranslatorFactory



class MockSwedishTranslator:
    def translate(self):
        pass

#@patch.object(SwedishTranslator, get_car, return_value="bil")
def test_car_translator_swedish():
    swe = SwedishTranslator()
    assert swe.get_car() == "bil"
    
def test_car_translator_italian():
    ita = ItalianTranslator()
    assert ita.get_car() == "macchina"
    
def test_car_translator_german():
    ita = GermanTranslator()
    assert ita.get_car() == "auto"
    
def test_translator_factory_reg():
    translator = TranslatorFactory()
    translator.register_language("Swedish", MockSwedishTranslator)
    assert translator._translators["Swedish"] == MockSwedishTranslator
    
def test_translator_factory_swedish():
    translator = TranslatorFactory()
    translator._translators["Swedish"] = MockSwedishTranslator
    assert translator.get_translator("Swedish") == MockSwedishTranslator

def test_translator_factory_no_language():
    translator = TranslatorFactory()
    with pytest.raises(ValueError):
        translator.get_translator("hej")
        
# @patch.object(SwedishTranslator, "get_car", return_value = "bil")
# def test_translate_car_swedish(mock_object):
#     assert translate_car("Swedish") == "bil"
#     mock_object.assert_called_once()
    
# @patch.object(ItalianTranslator, "get_car", return_value = "macchina")
# def test_translate_car_italian(mock_object):
#     assert translate_car("Italian") == "macchina"
#     mock_object.assert_called_once()
    
# @patch.object(GermanTranslator, "get_car", return_value = "auto")
# def test_translate_car_german(mock_object):
#     assert translate_car("German") == "auto"
#     mock_object.assert_called_once()

# def test_translate_car_invalid():
#     with pytest.raises(ValueError):
#         translate_car("English")
    