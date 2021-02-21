# test_mycalc1.py test calc functions using test fixture
import sys

import pytest
from mypytest.src.myadd3 import add
from mypytest.src.mycalc import MyCalc

@pytest.fixture(scope="module")
def my_calc():
    return MyCalc()

@pytest.fixture
def test_data():
    return {'x':10, 'y':5}

def test_add(my_calc, test_data):
    """ test case to validate two positive numbers"""
    assert my_calc.add(test_data.get('x'), test_data.get('y')) == 15

def test_subtract(my_calc, test_data):
    """ test case to validate two positive numbers"""
    assert my_calc.subtract(test_data.get('x'), test_data.get('y')) == 5

