# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:02:55 2024

@author: SKRANTZ5
"""
from unittest.mock import patch
from src.routes import signal_interpreter_app
from src.json_parser import JsonParser


@patch.object(JsonParser, "get_signal_title", return_value="ECU Reset")
def test_interpret_signal(mock_signal_titel):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        my_payload = {"my_key": "my_value"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "ECU Reset"