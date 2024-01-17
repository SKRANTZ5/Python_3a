# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:14:21 2024

@author: SKRANTZ5
"""

from unittest.mock import patch

from src.lesson2.rock_paper_scissor_game import decide_who_will_win, RandomClass, play_game

def test_decide_who_will_win_paper_vs_rock():
    assert decide_who_will_win("Paper", "Rock") == "You won!"
    
def test_decide_who_will_win_paper_vs_paper():
    assert decide_who_will_win("Paper", "Paper") == "It was a tie"
    
def test_decide_who_will_win_paper_vs_scissor():
    assert decide_who_will_win("Paper", "Scissor") == "You lost"

def test_decide_who_will_win_rock_vs_rock():
    assert decide_who_will_win("Rock", "Rock") == "It was a tie"
    
def test_decide_who_will_win_rock_vs_paper():
    assert decide_who_will_win("Rock", "Paper") == "You lost"
    
def test_decide_who_will_win_rock_vs_scissor():
    assert decide_who_will_win("Rock", "Scissor") == "You won!"
    
def test_decide_who_will_win_scissor_vs_rock():
    assert decide_who_will_win("Scissor", "Rock") == "You lost"
    
def test_decide_who_will_win_scissor_vs_paper():
    assert decide_who_will_win("Scissor", "Paper") == "You won!"
    
def test_decide_who_will_win_scissor_vs_scissor():
    assert decide_who_will_win("Scissor", "Scissor") == "It was a tie"
    
@patch("src.lesson2.rock_paper_scissor_game.random.choice", return_value="Scissor")
def test_get_robot_choice_scissor(mock_input):
    robot = RandomClass()
    assert robot.get_robot_choice() == "Scissor"

@patch("src.lesson2.rock_paper_scissor_game.decide_who_will_win", return_value="You won!")
@patch.object(RandomClass, "get_robot_choice", return_value="Scissor")
@patch("builtins.input", return_value="Rock")
def test_play_game(mock_input, mock_get_robot_choice, mock_decide_who_will_win):
    assert play_game() == "You won!"
    mock_decide_who_will_win.assert_called_with("Rock", "Scissor")
    