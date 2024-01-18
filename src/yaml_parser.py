# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:13:58 2024

@author: SKRANTZ5
"""

import yaml
from src.custom_exception import MyCustomError
from src import logger


class YamlParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.data = yaml.safe_load(file)
                logger.info("File data read %s", self.data)
        except FileNotFoundError:
            raise MyCustomError("File not found", 400)

    def get_signal_title(self, identifier):
        # loop through all services in self.data
        for entry in self.data["services"]:
            logger.info("Current entry %s", entry)
            if entry["id"] == identifier:
                return entry["title"]
        raise MyCustomError("Signal not found", 404)
