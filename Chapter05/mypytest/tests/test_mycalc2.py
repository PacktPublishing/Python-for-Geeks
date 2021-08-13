# test_mycalc2.py test calc functions using test fixture

import pytest
from mypytest.src.myadd3 import add
from mypytest.src.mycalc import MyCalc

@pytest.fixture(scope="module")
def my_calc():
    my_calc = MyCalc()
    yield my_calc
    del my_calc

@pytest.fixture
def data_set(request):
    dict = {'x':10, 'y':5}
    def delete_dict():
        del dict
    request.addfinalizer(delete_dict)
    return dict

def test_add(my_calc, data_set):
    """ test case to validate two positive numbers"""
    assert my_calc.add(data_set.get('x'), data_set.get('y')) == 15

def test_subtract(my_calc, data_set):
    """ test case to validate two positive numbers"""
    assert my_calc.subtract(data_set.get('x'), data_set.get('y')) == 5

