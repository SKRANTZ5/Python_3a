# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:33:09 2024

@author: SKRANTZ5
"""

from flask import Flask, request

signal_interpreter_app = Flask(__name__)

# @signal_interpreter_app.route("/", methods=["GET"])
# def hello():
#     return "Hello World!"


@signal_interpreter_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    return data

signal_interpreter_app.run()