# test_myadd4.py test suite for myadd function using markers
import sys

import pytest
from mypytest.src.myadd3 import add

@pytest.mark.skip
def test_add1():
    """ test case to validate two positive numbers"""
    assert add(10, 5) == 15

@pytest.mark.skipif(sys.version_info > (3,6),
                    reason=" skipped for release > than Python 3.6")
def test_add2():
    """ test case to validate two positive numbers"""
    assert add(10, -5) == 5, "should be 5"

@pytest.mark.xfail(sys.platform == "darwin",
                   reason="ignore exception for mac")
def test_add3():
    """ test case to validate two positive numbers"""
    assert add(-10, 5) == -5
    raise Exception()

