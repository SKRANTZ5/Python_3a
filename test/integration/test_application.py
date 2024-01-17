# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:45:51 2024

@author: SKRANTZ5
"""
import sys
import pytest
from unittest.mock import patch
from src.main import main
from src.routes import signal_interpreter_app
from src.json_parser import JsonParser


# @pytest.mark.parametrize("identifier, expected", [
#     ("11", "ECU Reset"),
#     ("27", "Security Access"),
#     ("e.", "No match"),
# ])
@patch("src.main.signal_interpreter_app.run")
@patch.object(sys, "argv", ["main.py", "--file_path", r"C:\test_basic.json"])
def test_application(mock_app_run, dummy_json):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    with my_app_instance as client:
        main()
        response = client.post("/", json=dummy_json)
        mock_app_run.assert_called_once()
        # assert response == "Security Access"
        
        
        