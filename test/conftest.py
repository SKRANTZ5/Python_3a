# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:39:46 2024

@author: SKRANTZ5
"""

import pytest

@pytest.fixture
def numbers():
    return ["one", "two", "three"]