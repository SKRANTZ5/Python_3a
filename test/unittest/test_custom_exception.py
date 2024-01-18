# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:34:08 2024

@author: SKRANTZ5
"""

from src.custom_exception import MyCustomError


def test_custom_exception():
    custom_error = MyCustomError("Test_Error", 404)
    assert custom_error.msg == "Test_Error"
    assert custom_error.code == 404
