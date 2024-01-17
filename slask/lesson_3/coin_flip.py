# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:20:34 2024

@author: SKRANTZ5
"""

import random


def get_three_heads():
    tries = 0
    heads = 0
    while True:
        tries += 1
        flip = random.choice(["heads", "tails"])
        print(f"Got {flip}")
        if flip == "heads":
            heads += 1
            if heads == 3:
                print(f"Number of tries until three heads: {tries}")
                break
            
get_three_heads()