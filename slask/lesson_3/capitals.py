# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:34:49 2024

@author: SKRANTZ5
"""


def get_capital(country):
    database = {"sweden": "stockholm"}
    if country in database.keys():
        return database[country]

def practice_capitals():
    country = input("Give me a country: ")
    try:
        capital = get_capital(country)
        print(f"The capital of {country} is {capital}")
    except KeyError:
        print(f"The country {country} does not exist in our dictornary")