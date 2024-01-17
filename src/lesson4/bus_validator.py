# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:50:18 2024

@author: SKRANTZ5
"""

def bus_validator():
    age = input("Gimme your age: ")
    try:
        age = int(age)
    except ValueError as err:
        print("You need to enter a number")
    else:
        if age >= 24:
            print("Congratulations, you are old enough to drive a bus")
        elif age <= 23:
            print(f"Sorry, you have to wait {24-age} more years")
    finally:
        print("Good bye")