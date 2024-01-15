# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:14:21 2024

@author: SKRANTZ5
"""

from src.rock_paper_scissor_game import decide_who_will_win

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