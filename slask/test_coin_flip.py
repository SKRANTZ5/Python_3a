# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:20:49 2024

@author: SKRANTZ5
"""

from unittest.mock import patch, call
from src.lesson_3.coin_flip import get_three_heads 


@patch("builtins.print")
@patch("src.lesson_3.coin_flip.random.choice", side_effect=["heads", "heads", "tails", "heads"])
def test_get_three_heads(mock_random_choice, mock_print):
    get_three_heads()
    assert mock_print.mock_calls == [call("Got heads"), call("Got heads"), call("Got tails"), call("Got heads"), call("Number of tries until three heads: 4")]