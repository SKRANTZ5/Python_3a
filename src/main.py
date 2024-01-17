# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:14:57 2024

@author: SKRANTZ5
"""
from argparse import ArgumentParser
from src.routes import signal_interpreter_app, json_parser

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()

def main():
    args = parse_arguments()
    _ = json_parser.load_file(args.file_path)
    signal_interpreter_app.run()

if __name__ == "__main__":
    main()