# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:33:09 2024

@author: SKRANTZ5
"""

from flask import Flask, request, jsonify, abort
from src.parser_factory import ParserFactory
from src.custom_exception import MyCustomError

signal_interpreter_app = Flask(__name__)
parser_factory = ParserFactory()

# @signal_interpreter_app.route("/", methods=["GET"])
# def hello():
#     return "Hello World!"


# @signal_interpreter_app.route("/", methods=["POST"])
# def mirror_data():
#     data = request.get_json()
#     return data

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    parser = parser_factory.get_parser()
    try:
        title = parser.get_signal_title("11")
        #title = json_parser.get_signal_title("11")
    except MyCustomError as e:
        abort(e.code, description=e.msg)
    else:
        return jsonify(title)

#signal_interpreter_app.run()