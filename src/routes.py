# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:33:09 2024

@author: SKRANTZ5
"""

from flask import Flask, request

my_app = Flask(__name__)

@my_app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


@my_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    return data

my_app.run()