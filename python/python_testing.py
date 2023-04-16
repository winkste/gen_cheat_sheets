"""This cheatsheet mainly covers tips for testing in python.

"""

# using pytest in python
pip install pytest

# use a generic configuration file that helps pytest to execute.
# locate the file in the root folder of the project
pyconf.py

# check for the result in pytest
assert value == expected

# check for exceptions in the execution
with pytest.raises(TypeError):
    assert proc_barcode(test_input) is expected

# this file can be used to define test fixtures and parameters
import pytest
from src.pointsale import get_total

@pytest.fixture()
def clean_totals():
    """This is a setup fixture to clean totals
    """
    get_total()
    yield

# using the parameter feature to combine test data
@pytest.mark.parametrize("test_input,expected", [(12345, "$7.25"), (23456, "$12.50"), (45456, "$5.25")])

def test_given_right_barcode_proc_barcode_returns_value(test_input, expected):
    """This test case checks if barcodes not known return None

    Args:
        test_input (_type_): input value
        expected (_type_): expected result
    """
    assert proc_barcode(test_input) == expected

# use a fixture to setup and tear down environment before executing a test function
@pytest.fixture()
def prep_25_dollars():
    """This fixture cleans the totals and
        add barcodes with the value of 25$
    """

    get_total()
    proc_barcode(12345)
    proc_barcode(23456)
    proc_barcode(45456)
    yield
    get_total()

# use coverage already installed by pytest to see the code coverage
# https://coverage.readthedocs.io/en/7.1.0/

# run test coverage together with pytest
coverage run -m pytest

# get a reoprt showing the coverage
coverage report

# generates a detailed html based report which allow tracing the files in
# browser
coverage html

# coverage can also be used just executing the program
coverage run my_program.py


