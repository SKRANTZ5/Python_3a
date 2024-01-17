# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:50:18 2024

@author: SKRANTZ5
"""
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def bus_validator():
    try:
        age = int(input("Gimme your age: "))
        logger.info("User gave age: %d", age)
    except ValueError as err:
        print("You need to enter a number")
        logger.exception("Exception occurred %s", err)
    else:
        if age >= 24:
            print("Congratulations, you are old enough to drive a bus")
        else:
            print(f"Sorry, you have to wait {24-age} more years")
    finally:
        print("Good bye")
        
if __name__ == "__main__":
    bus_validator()
        