# test_myadd3.py test suite for myadd function

import pytest
from mypytest.src.myadd3 import add


def test_add1():
    """ test case to validate two positive numbers"""
    assert add(10, 5) == 15


def test_add2():
    """ test case to validate two positive numbers"""
    assert add(10, -5) == 5, "should be 5"

def test_add3():
    """ test case to validate two positive numbers"""
    assert add(-10, 5) == -5

def test_add4():
    """ test case to validate two positive numbers"""
    assert add(-10, -5) == -15

def ttest_typeerror1():
    """ test case to check if we can handle non number input"""
    with pytest.raises(TypeError):
        add('a', 5)

def ttest_typeerror2():
    """ test case to check if we can handle non number input"""
    with pytest.raises(TypeError, match="only numbers are allowed"):
        add('a', 'b')