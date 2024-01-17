# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:14:57 2024

@author: SKRANTZ5
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from argparse import ArgumentParser
from routes import signal_interpreter_app, json_parser
from custom_exception import MyCustomError
from src import logger


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        _ = json_parser.load_file(args.file_path)
    except MyCustomError as e:
        logger.exception("Exception occured %s", e)
        print(f"Error {e.code}: {e.msg}")
    else:
        signal_interpreter_app.run()

if __name__ == "__main__":
    main()