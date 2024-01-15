# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:12:25 2024

@author: SKRANTZ5
"""

def decide_who_will_win(player, robot):
    if (player == "Scissor" and robot == "Paper") or (player == "Rock" and robot == "Scissor") or (player == "Paper" and robot == "Rock"):
        return "You won!"
    elif (player == "Scissor" and robot == "Scissor") or (player == "Rock" and robot == "Rock") or (player == "Paper" and robot == "Paper"):
        return "It was a tie"
    elif (player == "Scissor" and robot == "Rock") or (player == "Rock" and robot == "Paper") or (player == "Paper" and robot == "Scissor"):
        return "You lost"