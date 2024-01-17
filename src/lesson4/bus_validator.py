# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:50:18 2024

@author: SKRANTZ5
"""
import os
import json
import yaml
import logging.config

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
#LOG_SETTINGS_PATH = os.path.join(CURR_DIR, "log_settings.json")
LOG_SETTINGS_PATH = os.path.join(CURR_DIR, "log_settings.yaml")

with open(LOG_SETTINGS_PATH, "r") as f:
    #config = json.load(f)
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("Test_Logger")

# if not os.path.exists("Logs"):
#     os.makedirs("Logs")

# import logging
# logging.basicConfig(
#     filename=os.path.join("Logs","debug.log"),
#     level=logging.DEBUG,
#     format="%(asctime)s - %(lineno)d - %(funcName)s - %(message)s")
# logger = logging.getLogger(__name__)


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
        hej = "hej"
        logger.error("Func ended %s", hej)
        
if __name__ == "__main__":
    bus_validator()
        