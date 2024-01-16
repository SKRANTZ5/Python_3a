import os
from subprocess import call
from invoke import task


# Absolute paths
# CURR_DIR = os.path.abspath(os.path.dirname(__file__))
# SRC_DIR = os.path.join(CURR_DIR, "src")
# UNIT_TEST_DIR = os.path.join(CURR_DIR, "test")
# COV_PATH = os.path.join(CURR_DIR, ".coveragerc")

# Relative paths
SRC_DIR = "src"
UNIT_TEST_DIR = "test"
COV_PATH = ".coveragerc"

@task
def style(_):
    call(f"pycodestyle {SRC_DIR}", shell=True)
    
@task
def lint(_):
    call(f"pylint {SRC_DIR}", shell=True)
    
@task
def unit_test(_):
    cmd = f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR}  --cov-config={COV_PATH}"
    #cmd = f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR}"
    call(cmd, shell=True)