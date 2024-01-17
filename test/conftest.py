# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:39:46 2024

@author: SKRANTZ5
"""

import pytest
import json

@pytest.fixture
def numbers():
    return ["one", "two", "three"]


@pytest.fixture
def dummy_json():
    with open(r"C:\test_basic.json", "r") as file:
        return json.load(file)
        #return file.read()