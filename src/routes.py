# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:33:09 2024

@author: SKRANTZ5
"""

from flask import Flask, request, jsonify
from src.json_parser import JsonParser

signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()

# @signal_interpreter_app.route("/", methods=["GET"])
# def hello():
#     return "Hello World!"


# @signal_interpreter_app.route("/", methods=["POST"])
# def mirror_data():
#     data = request.get_json()
#     return data

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    payload = request.get_json()
    title = json_parser.get_signal_title("27")
    return jsonify(title)

#signal_interpreter_app.run()