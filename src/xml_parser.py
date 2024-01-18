# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import xmltodict
from src.custom_exception import MyCustomError
from src import logger


class XmlParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        try:
            tree = ET.parse(file_path)
            data = tree.getroot()
            xml_string = ET.tostring(data, encoding="utf-8", method="xml")
            self.data = dict(xmltodict.parse(xml_string))
            logger.info("File data read %s", self.data)
        except FileNotFoundError:
            raise MyCustomError("File not found", 400)

    def get_signal_title(self, identifier):
        # loop through all services in self.data
        for entry in self.data["services"]["service"]:
            logger.info("Current entry %s", entry)
            if entry["@id"] == identifier:
                return entry["title"]
        raise MyCustomError("Signal not found", 404)
