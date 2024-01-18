# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:59:53 2024

@author: SKRANTZ5
"""


class MyCustomError(Exception):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
