# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:02:55 2024

@author: SKRANTZ5
"""
from unittest.mock import patch
import pytest
from src.routes import signal_interpreter_app
from src.json_parser import JsonParser
from src.custom_exception import MyCustomError
from src.parser_factory import ParserFactory


@patch.object(JsonParser, "get_signal_title", return_value="ECU Reset")
def test_interpret_signal_valid(mock_signal_titel):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        my_payload = {"my_key": "my_value"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "ECU Reset"

# @patch.object(ParserFactory, "get_parser", return_value=JsonParser())
# @patch("src.routes.abort")
# @patch.object(JsonParser, "get_signal_title", side_effect=MyCustomError("hej",404))
# def test_interpret_signal_invalid(mock_signal_titel, mock_abort, mock_json_parser):
#     signal_interpreter_app.testing = True
#     my_app_instance = signal_interpreter_app.test_client()

#     with my_app_instance as client:
#         my_payload = {"my_key": "my_value"}
#         response = client.post("/", json=my_payload)
#         mock_abort.assert_called_once()
        