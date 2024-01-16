# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:54:55 2024

@author: SKRANTZ5
"""

def is_hex(val):
    try:
        int(val, 16)
        return True
    except ValueError:
        return False