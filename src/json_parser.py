# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:49:39 2024

@author: SKRANTZ5
"""

import json as js
from src.custom_exception import MyCustomError


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        try:
            with open(file_path, "r") as my_file:  # open the json file
                #self.data = my_file.read()  # load the json file and save it to self.data
                self.data = js.load(my_file)
        except FileNotFoundError as er:
            raise MyCustomError("File not found", 400)

        else:
            return self.data


    def get_signal_title(self, identifier):
        for entry in self.data["services"]:  # loop through all services in self.data
            if entry["id"] == identifier:
                return entry["title"]
        raise MyCustomError("Signal not found", 404)
            