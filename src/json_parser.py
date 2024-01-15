# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:49:39 2024

@author: SKRANTZ5
"""

class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        with open(file_path, "r") as my_file:  # open the json file
            self.data = my_file.read()  # load the json file and save it to self.data
        return self.data

    def get_signal_title(self, identifier):
        for entry in self.data["services"]:  # loop through all services in self.data
            if entry["id"] == identifier:
                return entry["title"]
