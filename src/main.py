# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:14:57 2024

@author: SKRANTZ5
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from argparse import ArgumentParser
from src.xml_parser import XmlParser
from src.json_parser import JsonParser
from src.yaml_parser import YamlParser
from src.routes import signal_interpreter_app, parser_factory #json_parser
from src.custom_exception import MyCustomError
from src import logger


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()

def register_parsers():
    parser_factory.register_format("xml", XmlParser)
    parser_factory.register_format("json", JsonParser)
    parser_factory.register_format("yaml", YamlParser)

def find_signal_database(file_path):
    parser_factory.set_signal_database_format(file_path.split(".")[1])

def main():
    args = parse_arguments()
    register_parsers()
    find_signal_database(args.file_path)
    try:
        parser = parser_factory.get_parser()
        logger.info("parser is %s", isinstance(parser, JsonParser))
        parser.load_file(args.file_path)
        #_ = json_parser.load_file(args.file_path)
    except ValueError as e:
        logger.exception("Exception occured %s", e)
    except MyCustomError as e:
        logger.exception("Exception occured %s", e)
    else:
        signal_interpreter_app.run()

if __name__ == "__main__":
    main()