# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:39:55 2024

@author: SKRANTZ5
"""

from unittest.mock import patch
from src.main import parse_arguments, ArgumentParser, main
from src.json_parser import JsonParser

class MockArgs:
    file_path = "C:\signal_database.json"  # Fick lägga på c disk pga volvo strula upp med syntaxen på mapparna

@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")

@patch("src.main.signal_interpreter_app.run")
@patch("src.main.parse_arguments", return_value=MockArgs)
@patch.object(JsonParser, "load_file")
def test_main(mock_load_file, mock_parse_arguments, mock_app_run):
    main()
    mock_load_file.assert_called_once()
    mock_load_file.assert_called_with(MockArgs.file_path)
    

    